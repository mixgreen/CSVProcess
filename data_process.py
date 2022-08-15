# 程序作用：提取某个文件夹中所有 CSV 文件特定列的数据，并粘合在一个文件里
# 实现方法：利用 pandas 包中的 read_csv 方法读取目标数据，并用 merge 方法将数据粘合。
# 使用方法：将该文件放入数据文件夹中（与数据文件在同一级），运行即可。重复运行时，要删掉前一次运行的文件
# 版本：V1.0
# 作者：葛云瑞
# 时间：2022年8月15日

import os
import pandas as pd

all_file_list = os.listdir('./')            # 得到该路径下的所有文件,并生成一个列表
del all_file_list[0:2]                      # 本程序会创造两个文件（本文件和一个运行文件），要删掉
data = pd.DataFrame(data=None)              # 生成初始 DataFrame 对象
for single_file in all_file_list:           # 遍历文件名列表
    # 用 pandas 的 read_csv 函数读取目标文件
    data_temp = pd.read_csv(single_file, header=2, usecols=(0, 1), encoding='utf8')
    # 更改列名
    data_temp.columns = ["Frequency", single_file.replace(".CSV", "")]
    # 由于粘贴函数需要两个 DataFrame 对象，所以读取的第一个对象无法粘合，要分情况讨论
    if single_file == all_file_list[0]:
        # 第一个 CSV 文件数据导入初始的 DataFrame 对象
        data = data_temp
    else:
        # 后面的 CSV 文件数据与前面的粘连
        data = pd.merge(data, data_temp, left_on="Frequency", right_on="Frequency")

data.to_csv("data.csv")                     # 导出 CSV 文件
