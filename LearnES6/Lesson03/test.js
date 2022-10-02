const data = 10;
console.log(data);
// data = 100; //TypeError: Assignment to constant variable.

const list = [10, 20, 30];
console.log(list);

list[0] = 100;
console.log(list);
// ⚠️ 列表中元素的值可以改 但是不能直接 list = [1,2,3]

list.push(99);
console.log(list);

// list = [1, 2, 3]; //TypeError: Assignment to constant variable.