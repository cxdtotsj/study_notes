# 软件测试52讲 11-20课程记录

## lesson13 Page Object模型
1. page类: 封装元素
2. scripts类: 封装执行动作

## lesson14
操作函数: 颗粒度不能太细(每个元素执行都封装成一个方法), 也不能太粗(用例不能重用)

## lesson15
测试数据:
1. 测试输入数据(比如登录: 需要用户名和密码)
2. 测试依赖数据(比如登录，先要注册这个用户)

创建测试依赖数据的方法:
1. API调用
2. 数据库操作
3. API调用和数据库操作

创建测试依赖数据的时机:
1. 测试执行过程中，实时创建，称为 On-the-fly
2. 测试用例执行前， 称为 Out-the-fly

在实际项目中，对于创建数据的技术手段而言，最佳的选择是利用 API 来创建数据，只有当 API 不能满足数据创建的需求时，才会使用数据库操作的手段。
实际上，往往很多测试数据的创建是基于 API 和数据库操作两者的结合来完成，即先通过 API 创建基本的数据，然后调用数据库操作来修改数据，以达到对测试数据的特定要求。

而对于创建数据的时机，在实际项目中，往往是 On-the-fly 和 Out-of-box 结合在一起使用。
对于相对稳定的测试数据，比如商品类型、图书类型等，往往采用 Out-of-box 的方式以提高效率；而对于那些只能一次性使用的测试数据，比如商品、订单、优惠券等，往往采用 On-the-fly 的方式以保证不存在脏数据问题。


On-the-fly 和 Out-of-box 的互补
1. 对于相对稳定、很少有修改的数据，建议采用 Out-of-box 的方式，比如商品类目、厂商品牌、部分标准的卖家和买家账号等。
2. 对于一次性使用、经常需要修改、状态经常变化的数据，建议使用 On-the-fly 的方式。
3. 用 On-the-fly 方式创建测试数据时，上游数据的创建可以采用 Out-of-box 方式，以提高测试数据创建的效率。以订单数据为例，订单的创建可以采用 On-the-fly 方式，而与订单相关联的卖家、买家和商品信息可以使用 Out-of-box 方式创建。