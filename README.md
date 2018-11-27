# Python

1. 创建虚拟环境

    1. 进入工程目录；
    2. 运行命令:

        `python -m venv venv`
    3. 启动虚拟环境:

        linux: `source venv/bin/activate`
        windows: `venv\Scripts\activate`

2. 替换 PIP 安装的源

    清华源(推荐，5分钟同步一次) : `https://pypi.tuna.tsinghua.edu.cn/simple`
    豆瓣源 : `http://pypi.douban.com/simple/`

    命令 : `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests`


# JavaScript


# linux配置代理
1. 主机使用SSR，开始局域网代理，配置端口
2. linux网络配置代理，地址为 主机IP地址，端口为 SSR端口
3. 在 `.bashrc`、 `/etc/profile` 中配置代理设置 

`export http_proxy=host:prot` 

`export https_proxy=host:prot`