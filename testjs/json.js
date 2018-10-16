//JSON对象序列化成字符串

var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp']
};

var s = JSON.stringify(xiaoming);
console.log(s);

//输出好看些
var s = JSON.stringify(xiaoming,null,'  ');
console.log(s);

//第二个参数用来筛选对象的键值，可以只输出指定的属性,可以传入 Array：
var s = JSON.stringify(xiaoming,['name','skills'],'  ');
console.log(s);

//还可以传入一个函数
function convert(key,value){
    if (typeof value === 'string'){
        return value.toUpperCase();
    }
    return value
}

var s = JSON.stringify(xiaoming,convert,'  ');
console.log(s);

//序列化部分JSON的数据，定义toJSON()方法
var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
    toJSON: function(){
        return {
            'Name':this.name,
            'Age':this.age
        };
    }
};

var s = JSON.stringify(xiaoming,null,'  ');
console.log(s);


//反序列化
//拿到一个JSON格式的字符串，我们直接用JSON.parse()把它变成一个JavaScript对象：

var obj = JSON.parse('[1,2,3,true]');
console.log(obj);
var obj = JSON.parse('true');
console.log(obj);
var obj = JSON.parse('{"name":"小明","age":14}');
console.log(obj)
var obj = JSON.parse("13.14");
console.log(obj);

//用函数转化json中的value值
var obj = JSON.parse('{"name":"小明","age":14}',function(key,value){
    if (key === 'name'){
        return value+'同学';
    }
    return value;
});
console.log(obj);