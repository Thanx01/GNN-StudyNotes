import torch
import matplotlib.pyplot as plt
from torch.nn import Linear
from torch_geometric.nn import GCNConv
from torch_geometric.datasets import KarateClub
from torch_geometric.utils import to_networkx
import networkx as nx

# 学习的可视化展示分类效果图
def visualize_grajh(G, color):
    plt.figure(figsize=(7, 7))
    plt.xticks([])
    plt.yticks([])
    nx.draw_networkx(G, pos=nx.spring_layout(G, seed=42), with_labels=False,
                     node_color=color, cmap="Set2")
    plt.show()


def visualize_embedding(h, color, epoch=None, loss=None):
    plt.figure(figsize=(7, 7))
    plt.xticks([])
    plt.yticks([])
    h = h.detach().cpu().numpy()
    plt.scatter(h[:, 0], h[:, 1], s=140, c=color, cmap="Set2")
    if epoch is not None and loss is not None:
        plt.xlabel(f'Epoch: epoch),Loss: {loss.item() :.4f}', fontsize=16)
    plt.show()


dataset = KarateClub()
print (f' Dataset: {dataset} : ')
print('===============')
print (f' Number of graphs: {len(dataset)}')
print(f' Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')
# 四分类任务
data = dataset[0]
# print(data)

edge_index = data.edge_index
print(edge_index.t())


G = to_networkx(data, to_undirected=True)
# visualize_grajh(G, color=data.y)


# GCN网络结构定义
class GCN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(1234)
        self.conv1 = GCNConv(dataset.num_features, 4)  # 定义输入特征和输出特征
        self.conv2 = GCNConv(4, 4)
        self.conv3 = GCNConv(4, 2)
        self.classifier = Linear(2, dataset.num_classes)

    def forward(self, x, edge_index):
        h = self.conv1(x, edge_index)  # 输入特征与邻接矩阵
        h = h.tanh()
        h = self.conv2(h, edge_index)
        h = h.tanh()
        h = self.conv3(h, edge_index)
        h = h.tanh()

        out = self.classifier(h)
        return out, h


model = GCN()
print(model)

model = GCN()
print(model)
_, h = model(data.x, data.edge_index)
print(f' Embedding shape: {list(h.shape)}')
visualize_embedding(h, color=data.y)



