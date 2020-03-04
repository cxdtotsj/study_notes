# linux基础命令整理

## 文件目录管理
1. scp: linux间传输文件
    ```
    # filename: 想要传输的文件名
    # username: 目标服务器用户名
    # ip: 目标服务器地址
    # /usr/local: 文件在目标服务器上的存放路径
    $ scp filename username@ip:/usr/local/
    ```

2.  rz sz: 上传、保存文件
    ```
    # 选择终端所在本机的文件上传至linux服务器
    $ rz

    # filename: linux服务器中的文件, 保存至终端所在本机
    $ sz filename
    ```

3. wget: 从网址上下载文件至linux服务器
    ```
    # url: 资源在远程服务器上的地址
    $ wget url
    ```

4. tar: 解压 tar.gz 格式文件， 或者把文件压缩成 tar.gz 格式( tar.gz 为linux的常用压缩方式)
    ```
    # 解压
    # filename: 文件格式为 ***.tar.gz
    $ tar -zxvf filename

    # 压缩
    # filename.tar.gz: 压缩后的文件名
    # /usr/local/example: 想要压缩的文件夹或文件
    $ tar -zcvf filename.tar.gz /usr/local/example
    ```

5. cat/head/tail/more/less: 查看文件
    ```
    # 完全打开一个文件(在终端上显示)
    $ cat filename

    # 打开一个文件的前100行(在终端上显示)
    $ head -100 filename

    # 打开一个文件的后100行(在终端上显示)
    $ tail -100 filename

    # 实现显示文件新增内容(即查看日志实时输出)
    $ tail -f filename

    # 翻页显示一个文件(只能向后翻页)
    $ cat filename | more

    # 翻页显示一个文件(可前后查看)
    $ cat filename | less
    ```

6. grep: 过滤查找
    ```
    # 查看一个指定进程
    # | grep mysql: 从所有进程中，只显示带有mysql关键字的进程
    $ ps -ef | grep mysql

    # 在文件中显示关键字
    # keyword: 想要通过 grep 查看的关键字
    $ cat filename | grep keyword
    ```

7. mv: 重命名一个文件(可移动目录)
    ```
    # 在当前目录下重命名一个文件
    $ mv filename new_filename

    # 重命名文件并移动至新的目录
    $ mv filename /usr/local/new_filename
    ```

8. cp: 复制一个文件至新的目录
    `$ cp filename /usr/local/`

9. chmod: 给文件或者文件夹赋权限
    ```
    # 给用户增加读权限
    chmod u+r filename
    # 给用户增加写权限
    chmod u+w filename
    # 给用户增加执行权限
    chmod u+x filename

    # 给用户组增加读权限
    chmod g+r filename
    # 给用户组增加写权限
    chmod g+w filename
    # 给用户组增加执行权限
    chmod g+x filename  

    # 给非用户组成员增加读权限
    chmod o+r filename
    # 给非用户组成员增加写权限
    chmod o+w filename
    # 给非用户组成员增加执行权限
    chmod o+x filename
    ```

10. mkdir: 新增一个目录
    `mkdir folder`

11. rm: 删除一个文件或者文件夹
    ```
    # 删除一个文件
    $ rm -f filename

    # 删除一个文件夹
    $ rm -rf folder

    # 模糊删除多个文件
    $ rm -f filename*
    ```

12. pwd: 显示当前目录路径

13. find: 查找
    ```
    # /: 要查找的起始目录(如果只想要查找 /usr/local/ 目录下的文件，则写成 $ find /usr/local/ filename)
    # filename: 查找的文件名
    $ find / filenames
    ```

14. vim: 编辑文件
    ```
    # 编辑文件(如果提示vim命令未找到，用vi)
    $ vim filename
    # 输入字符按 i
    $ i
    # 保存
    $ :wq!
    ```


## 系统资源
1. top: 查看整个服务器资源情况

2. free: 查看内存
    `free -m`

3. df: 查看磁盘使用情况
    `df -h`

4. netstat: 查看端口
    ```
    # 想要查看 33242 端口是否存在
    $ netstat -ntlp | grep 33242

    tcp6       0      0 :::33242                :::*                    LISTEN      59608/java
    ```

5. ps: 查看进程
    ```
    # 查看 mysql 进程是否存在
    $ ps -ef | grep mysql
    ```

6. ss: 查看sockets连接
    ```
    # 查看 mysql 的socket连接
    $ ss -nlp | grep mysql
    ```

7. kill: 强制杀掉进程
    ```
    # 首先查看一个进程的进程号
    $ ps -ef | grep 

    root     144595  94358  0 21:48 pts/3    00:00:00 grep --color=auto hotdb-management.jar

    # 其中，144595 就是查找到的进程号
    # 杀掉该进程
    $ kill -9 144595
    ```

## 网络管理
1. ifconfig: 查看本机IP
    ```
    # 普遍用，但正在淘汰
    $ ifconfig

    # 新标准
    $ ip addr
    ```

2. ping: 测试服务器是否可连接
    `$ ping ip`

3. telnet: 测试端口是否可连接
    ```
    # 如果不显示任何信息，代表可连接
    $ telnet ip port
    ```

## 系统管理
1. ssh: 连接远程服务器
    ```
    # 连接服务器，默认22端口
    # username: 远程服务器用户名
    # ip: 远程服务器地址
    $ ssh username@ip

    # 连接服务器，指定端口
    $ ssh -p port username@ip
    ```

2. 配置环境变量
    ```
    # 编辑用户环境变量
    $ vim ~/.bashrc
    # 保存后，需要source
    $ source ~/.bashrc  

    # 编辑系统环境变量(所有用户生效)
    $ vim /etc/profile
    # 保存后， 需要source
    $ source /etc/profile
    
    # 把一个新的执行命令添加到 PATH
    $ vim /etc/profile
    # 在文件底部添加 /usr/local/example/bin/ 至 PATH
    $export PATH=/usr/local/example/bin/:$PATH
    # 保存
    :wq!
    # 更新环境变量
    $ source /etc/profile
    ```