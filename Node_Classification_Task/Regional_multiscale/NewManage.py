import os

# 源文件夹路径
source_folder = r"E:\GNNStudy\Proj1\Node_Classification_Task\data\曼哈顿数据集-细区域\result"
# 目标文件夹路径
target_folder = r"E:\GNNStudy\Proj1\Node_Classification_Task\data\曼哈顿数据集-细区域\result\merged_files"

# 新建目标文件夹
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 整合文件
for class_num in range(1, 14):
    merged_file_path = os.path.join(target_folder, f"{class_num}.txt")
    with open(merged_file_path, "w",encoding='utf-8') as merged_file:
        for i in range(1, 34):
            file_name = f"{class_num}_{i}.txt"
            file_path = os.path.join(source_folder, file_name)
            if os.path.exists(file_path):
                with open(file_path, "r",encoding='utf-8') as source_file:
                    merged_file.write(source_file.read())
                    merged_file.write("\n")  # 可根据需要添加分隔符

print("文件整合完成！")
