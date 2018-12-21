# from datetime import datetime

# a = datetime.now().weekday()
# print(a)

# time1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(time1)

# class Functio:

#     def func_test(self):
#         dollor = input("输入美元：")
#         money = 6.28 * float(dollor)
#         print("转换后的金额为： %.2f" % money)
#         print("转换后的金额为：{:.2f}".format(money))
    

# if __name__ == '__main__':
#     f = Functio()
#     f.func_test()

lists = []
for i in range(5):
    name = input("请输入嘉宾姓名: ")
    lists.append(name)
    print(lists)