let name = "Koma"
let address = "网吧"
let fmtstr = markdown`你好，${name}！
晚上一起去${address}玩吗？
等你的回信。`
console.log(fmtstr)

function markdown(formats, ...args){
  console.log(formats)
  console.log(args)
  var result = "# 信息标题\n";
  for(var i = 0; i < formats.length; i++)
    result += formats[i] + "**" + (args[i] || '') + "**";
  return result;
}

// ⚠️ 你懂的 https://wesbos.com/tagged-template-literals/
let hh = hello();
let hhh = hello``;
console.log(hh);
console.log(hhh);
function hello(formats,...args){
  console.log(formats);
  console.log(args);
  return "hello world";
}