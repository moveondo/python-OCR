# encoding: utf-8

from tabula import wrapper

df = wrapper.read_pdf("/Users/my/Documents/program/消费行业周报20190111.pdf")
print(df)
for indexs in df.index:
    # 遍历打印企业名称
    print(df.loc[indexs].values[1].strip())