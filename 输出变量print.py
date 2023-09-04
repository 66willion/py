#可以输出数字
print(520)
#输出字符串时要加引号
print('hello world')
#将数据输出到文件中
#a是读写的方式创建文档，+是如果没有就创建新的，fp是变量
fp=open('D:/text.txt',a+)
#将hello world输入到fp文件中
print('hello world',file=fp)
#关闭fp文件
fp.close()
#不进行换行输出
print("hello","world","Python")
