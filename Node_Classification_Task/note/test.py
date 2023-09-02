from torch_geometric.datasets import Planetoid#下载数据集用的
from torch_geometric.transforms import NormalizeFeatures
dataset = Planetoid(root='data/Planetoid', name='Cora', transform=NormalizeFeatures()) #transform预处理
print()
print(f' Dataset: {dataset} : ')
print('=========')
print(f' Number of graphs: {len(dataset)}')
print(f'Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')
data = dataset[0]# 获得第一个图对象
print()
print(data)
print('=========')

print(f'Number of nodes: {data.num_nodes}')
print (f'Number of edges: {data.num_edges}')
# 计算平均节点度
print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
print(f'Number of training nodes: {data.train_mask.sum()}')
print(f'Training node label rate: {int (data.train_mask. sum()) / data.num_nodes :.2f}')
print(f'Has isolated nodes: {data.has_isolated_nodes()}')
print(f' Has self-loops: {data.has_self_loops()}')
print(f'Is undirected: {data.is_undirected()}')
