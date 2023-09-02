# 导入difflib库，用于比较文本差异
import difflib

# 定义两组文件的公共路径
mht_path = "E:\\GNNStudy\\Proj1\\Node_Classification_Task\\data\\曼哈顿多区域数据集-2022.9.14\\13个区域\\"
merged_path = "E:\\GNNStudy\\Proj1\\Node_Classification_Task\\data\\merged\\"

# 定义输出文件的公共路径
output_path = "E:\\GNNStudy\\Proj1\\Node_Classification_Task\\data\\补集\\"

# 定义一个循环，从1到13遍历每一对文件
for i in range(1, 14):
    # 拼接每一对文件的完整路径
    mht_file = mht_path + "mht-" + str(i) + ".txt"
    merged_file = merged_path + "merged_" + str(i) + ".txt"
    output_file = output_path + "diff_" + str(i) + ".txt"

    # 以读取模式打开两个文件，并读取内容
    with open(mht_file, "r",encoding='utf-8') as f1:
        mht_data = f1.read()
    with open(merged_file, "r",encoding='utf-8') as f2:
        merged_data = f2.read()

    # 将内容按行分割成列表
    mht_lines = mht_data.splitlines()
    merged_lines = merged_data.splitlines()

    # 使用difflib的ndiff函数比较两个列表，并返回一个生成器对象
    diff = difflib.ndiff(mht_lines, merged_lines)

    # 以写入模式打开输出文件，并写入差异内容
    with open(output_file, "w",encoding='utf-8') as f3:
        for line in diff:
            # 只写入以-开头的行，表示mht-1.txt中有而merged_1.txt中没有的三元组
            if line.startswith("-"):
                f3.write(line[2:] + "\n") # 去掉-和空格，只保留三元组内容，并换行

# 打印完成提示信息
print("比较完成，差异内容已保存在" + output_path)
