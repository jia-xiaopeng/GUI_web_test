
import os

def Get_address():
    path = os.path.realpath(__file__)
    return path

print("当前文件路径："+Get_address())