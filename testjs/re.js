

//正则表达式
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');
console.log(re1);
console.log(re2);


var re = /^\d{3}\-\d{3,8}$/;

var a = re.test('000-000');
console.log(a);
var b = re.test('018-12345678');
console.log(b);

//切分字符串

x1 = 'a b  c'.split(' ');
console.log(x1);

x1 = 'a b  c'.split(/\s+/);
console.log(x1);

x1 = 'a,b,, c   d'.split(/[\s\,]+/);
console.log(x1);

x1 = 'a,b;; c  d'.split(/[\s\,\;]+/);
console.log(x1);

// 分组
// ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

var re = /^(\d{0,3})-(\d{3,8})$/;
var x2 = re.exec("021-888888");
console.log(x2);

//贪婪匹配
var re = /^(\d+)(0*)$/;
var x2 = re.exec("1023000");
console.log(x2);

//非贪婪匹配?
var re = /^(\d+?)(0*)$/;
var x2 = re.exec("1023000");
console.log(x2);