import torch
import torch.nn.functional as F
from torch_geometric.loader import NeighborLoader
from tqdm import tqdm
import numpy as np
from torch_geometric.data import Data


def train_SMAHD_fast(
    features,
    edge,
    emb_dim=64,
    weights=[1, 1],
    n_epochs=200,
    lr=0.001,
    train_batch_size=1024,
    infer_batch_size=2048,
    num_neighbors=[10, 10],
    weight_decay=1e-5,
    train_device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu'),
    infer_device=torch.device('cpu'),
    Conv_Encoder=None,
    Conv_Decoder=None,
    SMAHD_class=None  # 你自定义的 SMAHD 类
):
    """Mini-batch 快速训练版 SMAHD"""

    # --- 初始化模型 ---
    hidden_dims = [x.shape[1] for x in features] + [emb_dim]
    model = SMAHD_class(hidden_dims, device=train_device, Conv_Encoder=Conv_Encoder, Conv_Decoder=Conv_Decoder)
    model.to(train_device)

    # --- 构建大图 ---
    features_cat = torch.cat(features, dim=1)
    data = Data(x=features_cat, edge_index=edge)

    # --- NeighborLoader 采样训练 ---
    train_loader = NeighborLoader(
        data,
        num_neighbors=num_neighbors,
        batch_size=train_batch_size,
        shuffle=True
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    loop = tqdm(range(1, n_epochs + 1))

    for epoch in loop:
        model.train()
        total_loss = 0

        for batch in train_loader:
            batch = batch.to(train_device)
            edge_index = batch.edge_index
            x_split = torch.split(batch.x, [x.shape[1] for x in features], dim=1)
            x_split = [x.to(train_device) for x in x_split]

            optimizer.zero_grad()
            z, x_rec = model(x_split, edge_index)

            # Reconstruction loss
            rec_loss = 0
            for i, (x, x_r) in enumerate(zip(x_split, x_rec)):
                rec_loss += weights[i] * F.mse_loss(x, x_r)

            rec_loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5)
            optimizer.step()
            total_loss += rec_loss.item()

        loop.set_description(f"Epoch [{epoch}/{n_epochs}]")
        loop.set_postfix(loss=total_loss / len(train_loader))

    # --- 推理阶段 ---
    model.eval()
    data = data.to(infer_device)
    full_loader = NeighborLoader(data, num_neighbors=[-1], batch_size=infer_batch_size, shuffle=False)
    z_list = []

    with torch.no_grad():
        for batch in full_loader:
            batch = batch.to(infer_device)
            edge_index = batch.edge_index
            x_split = torch.split(batch.x, [x.shape[1] for x in features], dim=1)
            x_split = [x.to(infer_device) for x in x_split]
            z, _ = model(x_split, edge_index)
            z_list.append(z.cpu())

    z_all = torch.cat(z_list, dim=0).numpy()
    return z_all
