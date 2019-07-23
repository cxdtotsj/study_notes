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

# lists = []
# for i in range(5):
#     name = input("请输入嘉宾姓名: ")
#     lists.append(name)
#     print(lists)

# movices = [
#     {"name": "《环太平洋:雷霆再起》",
#      "srs": ["9:30", "10:00", "10:30"]},
#     {"name": "《环太平洋:雷霆再起》", 
#     "srs": ["9:30", "10:00", "10:30"]}
#     ]


# def mf():
#     mn = [movice["name"] for movice in movices]
#     i = 0
#     infos = []
#     for name in mn:
#         i = i+1
#         info = "{}、{}".format(i, name)
#         infos.append(info)
#     return "".join(infos)



# def main_info():
#     print("欢迎使用自动售票机~~~")
#     m = mf()
#     name = input("请选择正在上映的电影： {}\n".format(m))


# main_info()


import random

for name in random.sample(range(100),3):
    print(name)