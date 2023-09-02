import os
# 指定文件夹的路径
folder_path = 'E:/GNNStudy/Proj1/Node_Classification_Task/data/曼哈顿多区域数据集-2022.9.14/13个区域'
# 获取文件夹下所有的.txt文件的路径
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
# 循环遍历每个文件的路径
for file_path in file_paths:
    # 打印当前处理的文件名
    print(f'Processing {file_path}')
    # 使用utf-8编码和读写模式打开文件
    with open(file_path, mode='r+', encoding='utf-8') as f:
        # 读取文件内容为一个列表，每一行为一个元素
        lines = f.readlines()
        # 将文件指针移动到开头
        f.seek(0)
        # 清空文件内容
        f.truncate()
        # 循环遍历每一行
        for line in lines:
            # 去掉行尾的换行符和句号
            line = line.rstrip('\n.')
            # 如果行不为空，就写入文件，并换行
            if line:
                f.write(line + '\n')
