# 一、 标题

在想要设置为标题的文字前面加#来表示\
一个#是一级标题，二个#是二级标题，以此类推。支持六级标题。

示例：
```
# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题
```
<br/><br/>
# 二、 字体

- **加粗**

要加粗的文字左右分别用两个*号包起来

例：**这是加粗**
<br/><br/>

+ **斜体加粗**

要倾斜和加粗的文字左右分别用三个*号包起来

例： ***这是斜体加粗***
<br/><br/>

* **删除线**

要加删除线的文字左右分别用两个~~号包起来

例： ~~这是删除线~~
<br/><br/>

# 三、 引用

在引用的文字前加>即可。引用也可以嵌套，如加两个>>三个>>>

例：>>这是引用
<br/><br/>
# 四、 分割线

三个或者三个以上的 - 或者 * 都可以。

例：
___
***
<br/><br/>
# 五、 图片

语法：
```
![图片alt](图片地址 "图片标题")

图片alt ：就是在图片下方显示的文字，相当于对图片的解释
图片地址 ：不需要双引号
图片标题 ：当鼠标移动到图片上时，显示的文字，可以不加
```
示例：

![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

<br/><br/>
# 六、 超链接

语法：

```
[超链接名](超链接地址 "超链接title")

超链接title 可以不加
```
示例：

[百度](https://www.baidu.com)

<br/><br/>
# 七、 列表

- **无序列表**

    语法：\
    无序列表用 -+*任意一种符号表示都可以

    ```
    - 列表内容
    + 列表内容
    * 列表内容

    注意：符号与内容之间必须有一个空格
    ```

+ **有序列表**

    语法：\
    数字加点

    ```
    1. 列表内容
    2. 列表内容
    3. 列表内容
    ```
    效果如下：

    1. 列表内容
    2. 列表内容

* **嵌套列表**

    语法：\
    上一级和下一级之间敲三个空格

    例：

    - 一级无序列表内容

       - 二级无序列表内容
       + 二级无序列表内容
    
    + 一级无序列表内容

       + 二级无序列表内容
       * 二级无序列表内容
    
    1. 一级有序列表内容

       1. 二级有序列表内容
       2. 二级有序列表内容
    
    2. 一级有序列表内容

       1. 二级有序列表内容
       2. 二级有序列表内容
<br/><br/>
# 八、 表格

语法：

```
表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容
内容|内容|内容

第二行分割表头和内容。
- 有一个就行，为了对齐，多加个几个
文字默认居左
-两边加 : 表示居中
-右边加 : 表示居右
注意：原生的语法，两边都要用 | 包起来
```
示例：

姓名|技能|排行
---|:--:|---:
刘备|哭|大哥
关羽|打|老二
张飞|骂|老三

# 九、 代码

语法：\
单行代码:代码之间分别用一个反引号括起来

`单行代码内容`

代码块:代码块之间用三个反引号括起来,且两边的反引号单独占一行

```
    代码...
    代码...
    代码...
```

示例：

单行代码\
`create database hero;`

代码块\
```
    function fun(){
        echo "这是一句非常牛逼的代码";
    }
    fun();
```
<br/><br/>
# 十、 流程图

```
flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&
```

示例：

```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```