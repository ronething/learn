循环我的对象
===========

## 知识点

* 可迭代的对象
* 迭代的方法

## 实战演习

~~~js
let list  = [10, 20, 30];
let mystr = '你好啊';
let mymap = new Map();
mymap.set('JS', 'Javascript');
mymap.set('PL', 'Perl');
mymap.set('PY', 'Python');

for(let val of list){
	console.log(val);
}

for(let val of mystr){
	console.log(val);
}

for(let [key,value] of mymap){
	console.log(key, value);
}

let it = mymap.values();
let tmp;
while(tmp = it.next()){
	if (tmp.done) break;
	console.log(tmp.value, tmp.done);
}
~~~

## 课程文件

https://gitee.com/komavideo/LearnES6

## 小马视频频道

http://komavideo.com
