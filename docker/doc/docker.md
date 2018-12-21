# docker

- 基础命令

   0. 搜索、拉取镜像
        ```
        docker search python
        docker pull python:3.6
        ```

   1. 查看docker镜像

        `docker images`
   2. 运行一个容器

        ```
        docker run -d -i -t ubuntu:15.10 /bin/bash
        -- 进入容器的命令
        docker exec -it 554fa06d51fd /bin/bash
        docker attach aa97ba3292ce
        ```
   3. 退出

        `exit   ctrl+d`
   4. 查看正在运行的容器

        ```
        docker ps
        docker ps -a
        docker ps -l
        ```
   5. 启动、停止、重启容器aa97ba3292ce的命令：

        ```
        docker start aa97ba3292ce
        docker stop aa97ba3292ce
        docker restart aa97ba3292ce
        ```
   6. 删除容器、镜像
        ```
        docker rm 容器id、容器name
        docker rmi 镜像id、镜像name

        注意：删除容器前需要停止容器；删除镜像前，需要删除这个镜像产生的所有容器

        ```
   7. 批量停止、删除容器；批量删除镜像

        ```
        docker stop $(docker ps -aq)
        docker rm $(docker ps -aq)
        docker rmi $(docker ps -aq)
        ```


   7. 安装工具钳，需要升级apt-get update
      1. 运行apt-get update失败后，应先运行:
          ```
              RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
              echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list && \
              echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list && \
              echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list
          ```
      2. 再运行

            `apt-get update`
    
    8. 把容器打包成一个新的镜像

        `docker commit -m "提交信息" -a "用户名" aa97ba3292ce tsjcxd/ubuntu:vim`




# 容器命令

```
attach    附着到一个运行的容器上
build     从一个Dockerfile建立镜像
commit    将一个变更后的容器创建为一个新镜像
cp        在容器和本地文件系统之间复制文件/目录
create    创建一个新的容器
diff      检测容器文件系统的变更
events    从服务器获取实时事件
exec      在一个运行中的容器内执行命令
export    将一个容器的文件系统输出为tar压缩包
history   显示一个镜像的历史
images    列出镜像列表
import    从tarball压缩包导入内容以创建一个文件系统镜像
info      显示系统信息
inspect   返回容器或镜像的底层信息
kill      杀死一个运行中的容器
load      从一个tar压缩包或STDIN加载一个镜像
login     登入Docker注册表（Docker registry）
logout    从Docker注册表登出
logs      抓取一个容器的日志
network   管理Docker网络
pause     暂停一个容器内的所有进程
port      列出该容器的所有端口映射或指定端口映射
ps        列出容器列表
pull      从注册表拉取一个镜像或仓库
push      往注册表推送一个镜像或仓库
rename    重命名容器
restart   重启容器
rm        删除一个或多个容器
rmi       删除一个或多个镜像
run       在一个新的容器中运行一条命令
save      将镜像保存至tar压缩包
search    在Docker Hub搜索镜像
start     启动一个或多个容器
stats     显示容器资源使用情况的实时信息流
stop      停止一个运行中的容器
tag       向注册表标记一个镜像
top       显示一个容器下运行的进程
unpause   恢复运行一个容器里所有被暂停的进程
update    更新容器的资源
version   显示Docker版本信息
volume    管理Docker卷
wait      阻塞对指定容器的其他调用方法,直到容器停止后退出阻塞。 
```