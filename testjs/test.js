/*
var arr = [1, "2", "abc"];
a = arr.indexOf("2");
console.log(a);

arr.slice(0, 3);
// 尾部添加元素
arr.push(5, 6);
arr.pop();

// 头部添加元素
arr.unshift("a");
arr.shift();
arr.sort();
// 反转
arr.reverse();
//连接数组
var arr2 = arr.concat([1, 2, 3]);


var b = "111233";
b.substring(2, 5);

//join()
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
*/


/*
function printlog(a){
    console.log(a)
}

var xiaoming = {
    name : "小明"
};

ax = xiaoming.hasOwnProperty("name");
printlog(ax);
bx = xiaoming.hasOwnProperty("toString");
printlog(bx);

var a = 10;
printlog(a);
*/

/* for循环：
var a = ["a","b","c"];
for (var i in a){
    console.log(i);
    console.log(a[i])
}

var b = {
    name:"小明",
    age:18,
    width:200
}
for (var i in b){
    if(b.hasOwnProperty(i)){
        console.log(i)
    }
}
*/

/*
//map(可以支持key不是字符串的值)

var m = new Map();
m.set('Adam', 67);
m.set('Bob', 50);
m.has('Adam');
m.get('Adam');
m.delete('Adam');
m.has('Adam');

//set
var s = new Set([1,2,3])
console.log(s.add(4))
*/

/*
//iterable
var a = ["A","B","C"];
var s = new Set([1,2,3]);
var m = new Map([[1,'X'],[2,'Y'],[3,'Z']]);
for (var i of a){
    console.log(i);
}

for (var i of s){
    console.log(i);
}

for (var i of m){
    console.log(i[0] + '=' + i[1]);
}
*/


/*
//forEach(遍历 array、set、map 里的数据)

var a = ["A","B","C"];
var s = new Set([1,2,3]);
var m = new Map([[1,'X'],[2,'Y'],[3,'Z']]);

a.forEach(function (value, index, array){
    console.log(value);
    console.log(index);
});

s.forEach(function (value,value2,set){
    console.log(value);
    console.log(value2);
});

s.forEach(function (value,set){
    console.log(value);
});

m.forEach(function (value,key,map){
    console.log(value);
    console.log(key)
})
*/

/*
//rest、arguments
function sum(...rest){
    var sum = 0;
    rest.forEach(function (value,array){
        sum += value;
    })
    return sum;
}
var sum_a;
sum_a = sum(1,2,3,4,5,6);
console.log(sum_a);


var a = [1,2,3,4,5];    
var sum = 0;
a.forEach(function (value,array){
    sum += value;
})
console.log(sum);
*/


/*
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};

console.log(person.name,person.age)
var {name,age} = person;
console.log('name = ' + name + ', age = ' + age );
*/


/*
//this
function getAge() {
    var y = new Date().getFullYear();
    return y-this.birth;
}

var xdchen = {
    name:"xdchen",
    birth:1990,
    age:getAge
};

console.log(xdchen.age());
//使用apply或者call方法，指定this指向
var age = getAge.apply(xdchen,[])
console.log(age)
*/


/*
var count = 0;
var oldParseInt = parseInt;

parseInt = function(){

    count += 1;
    return oldParseInt.apply(null,arguments);
};

parseInt();
parseInt();
parseInt();
console.log(count)
*/


/*
//高阶函数
function add(x,y,f){
    return f(x) + f(y);
}

var x = add(5,-6,Math.abs)
console.log(x)

var arr = [1, 3, 5, 7, 9];



// 利用reduce求积
function product(arr) {
    function sum(x,y){
        return x*y;
    }
    result = arr.reduce(sum)
    return result;
}

result = product([1, 3, 5, 7, 9]);
console.log(result);

if (product([1, 2, 3, 4]) === 24 && product([0, 1, 2]) === 0 && product([99, 88, 77, 66]) === 44274384) {
    console.log('测试通过!');
}
else {
    console.log('测试失败!');
}


//把一个字符串 '12345' 变成整数 12345
    function string2int(x){
        var arr = [];
        for (var i in x){
            arr.push(x[i]);
        }
        var newarr = arr.map(function(c){
            return c*1
        })
        return newarr.reduce(function(d,e){
            return d*10 + e;
        })
    }

//请把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。

function setName(arr){
    return arr.map(function (name) {
        var first_name = name.substring(0,1).toUpperCase();
        var other_name = name.substring(1,name.length).toLowerCase();
        return first_name+other_name;
    });
}

arr = ['adam', 'LISA', 'barT']
console.log(setName(arr))


// filter 筛选出素数
function get_primes(arr){
    return arr.filter(function (x){
        if (x===0 || x===1){
            return false;
        }
        for (var i ;i<= x/2;i++){
            if (x%i === 0){
                return false;
            }
        }
        return true;
    })
}

var
    x,
    r,
    arr = [];
for (x = 1; x < 100; x++) {
    arr.push(x);
}
r = get_primes(arr);
if (r.toString() === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].toString()) {
    console.log('测试通过!');
} else {
    console.log('测试失败: ' + r.toString());
}


// sort，排序，返回1，换位置；返回-1，不换位置；返回0，不换位置
//从大到小排列

var arr = [10, 20, 1, 2];
arr.sort(function (x,y){
    if (x>y){
        return 1;
    }
    if (x<y){
        return -1;
    }
    return 0;
})
console.log(arr)

//从大到小排列
var arr2 = [10, 20, 1, 2];
arr2.sort(function(x,y){
    if (x>y){
        return -1;
    }
    if (x<y){
        return 1;
    }
    return 0;
})
console.log(arr2)
*/


/*
//闭包
//求和

function lazy_sum(arr){
    var sum = function(){
        return arr.reduce(function(x,y){
            return x+y;
        })
    }
    return sum;
}

var arr = [10, 20, 1, 2];
var f = lazy_sum(arr);
console.log(f());
*/


