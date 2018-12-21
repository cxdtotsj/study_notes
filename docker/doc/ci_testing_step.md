# 部署CI的步骤

1. 下载基础镜像，调试能否运行
2. 构建Dockerfile，基础镜像，不包括代码
3. 通过git把代码加载到容器

## 步骤

    ```
    docker build -t x .     # 构建镜像

    # 在项目跟目录下运行容器,'pwd'获取当前目录, /test 为容器中创建的命令，把 pwd 下的文件挂在到容器 test 目录下
    docker run -v 'pwd':/test -it --rm x sh  

    cd atd_test # 代码目录

    python3 -m unittest discover -v     # 运行测试  

    ```

