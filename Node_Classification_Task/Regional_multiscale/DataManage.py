import os

folder_path = r'E:\GNNStudy\Proj1\Node_Classification_Task\data\曼哈顿多区域数据集-2022.9.14\13个区域'
file_paths = [os.path.join(folder_path, f'mht-{i}.txt') for i in range(1, 14)]

special_triplets = {}

for file_path in file_paths:
    with open(file_path, 'r',encoding="utf-8") as current_file:
        for line in current_file:
            triplet = line.strip().split(' ')
            subject = triplet[0]
            predicate = triplet[1]
            object_ = triplet[2]

            matching_files = []

            for other_file_path in file_paths:
                if other_file_path != file_path:
                    with open(other_file_path, 'r',encoding="utf-8") as other_file:
                        for other_line in other_file:
                            other_triplet = other_line.strip().split(' ')

                            if (
                                    other_triplet[0] == subject and
                                    other_triplet[1] == predicate and
                                    other_triplet[2] == object_
                            ):
                                matching_files.append(os.path.basename(other_file_path))

                    other_file.close()

            if matching_files:
                special_triplets[f'{subject} {predicate} {object_}'] = matching_files

        current_file.close()

for triplet, files in special_triplets.items():
    print(f'Special Triplet: {triplet}')
