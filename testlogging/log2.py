##亭子
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
对logging进行更加灵活的控制：需要了解Logger,Handler,Formatter,Filter

步骤
1. 创建logger实例并配置
2. 创建formatter对象
3. 创建你需要的handler对象并配置
4. 将handler加载到logger实例中
5. 写日志

这个模块主要包含了几个内容
1. 输出日志到控制台中
2. 输出日志到指定的日志文件中
3. 输出的日志按照指定的大小来自动管理，当文件达到指定的大小后，自动创建新文件
4. 输出的文件按照时间来自动管理，当文件达到指定的时候后，自动创建新文件
'''

import logging
from logging import handlers
import time

if __name__ =="__main__":
    #初始化logger
    logger = logging.getLogger()
    # 配置日志级别，如果不显示配置，默认为Warning，表示所有warning级别已下的其他level直接被省略，
    # 内部绑定的handler对象也只能接收到warning级别以上的level，你可以理解为总开关
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s",
                                  datefmt="%m/%d/%Y %I:%M:%S %p")  # 创建一个格式化对象

    console = logging.StreamHandler() # 配置日志输出到控制台
    console.setLevel(logging.WARNING) # 设置输出到控制台的最低日志级别
    console.setFormatter(formatter)  # 设置格式
    logger.addHandler(console)

    # file_logging = logging.FileHandler("example.log") # 配置日志输出到文件
    # file_logging.setLevel(logging.WARNING)
    # file_logging.setFormatter(formatter)
    # logger.addHandler(file_logging)

    # 和上面的FIleHandler差不多，只是handler对象可以管理文件大小，当文件大于指定的大小后，会自动将当前文件改名，然后重新创建一个新的同名文件继续输出
    # file_rotating_file = handlers.RotatingFileHandler("cat.log",maxBytes=1024,backupCount=3)
    # file_rotating_file.setLevel(logging.INFO)
    # file_rotating_file.setFormatter(formatter)
    # logger.addHandler(file_rotating_file)

    # 和上面的handler有点类似，不过，它是通过判断文件大小来决定何时重新创建日志文件，而是间隔一定的时候自动创建日志文件。
    # 代表每7天备份文件
    file_time_rotating = handlers.TimedRotatingFileHandler("app.log",when="s",interval=10,backupCount=5)
    file_time_rotating.setLevel(logging.INFO)
    file_time_rotating.setFormatter(formatter)
    logger.addHandler(file_time_rotating)

    #use logger
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical message")

    time.sleep(12)

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical message")
