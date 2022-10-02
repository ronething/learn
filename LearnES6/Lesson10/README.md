数组循环(for...of)
=======

## 知识点

* 新的数组循环方式

## 实战演习

~~~js
let list = [10, 20, 30];
//Array.prototype.Len = function(){};

// ⚠️ 只对数组中的值遍历
for(let val of list)
    console.log(val);

// for in  ⚠️ 循环对象
for(let val in list)
    console.log(val, list[val]);
~~~

## 课程文件

https://gitee.com/komavideo/LearnES6

## 小马视频频道

http://komavideo.com
