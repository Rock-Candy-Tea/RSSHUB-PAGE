
---
title: 'this的改变者(call apply bind)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7801'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:20:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=7801'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">三者区别及用法</h4>

























<table><thead><tr><th align="left">bind</th><th align="left">call</th><th align="left">apply</th></tr></thead><tbody><tr><td align="left">(this,param1,param2,param3,...)</td><td align="left">(this,param1,param2,param3,...)</td><td align="left">(this,[param1,param2,param3,...])</td></tr><tr><td align="left">返回的是fn的拷贝,改变了this的指向,保留了fn的参数</td><td align="left">fn的执行结果</td><td align="left">fn的执行结果</td></tr><tr><td align="left">不立即执行</td><td align="left">立即执行</td><td align="left">立即执行</td></tr></tbody></table>
<p>bind使用场景</p>
<pre><code class="copyable">let user = &#123;
  data:[
    &#123;name:'张三',age:'18'&#125;,
    &#123;name:'王五',age:'25'&#125;,
  ],
  getUserAge(name)&#123;
    let &#123;age=''&#125; = this.data.find(item=>item.name === name) || &#123;&#125;
    console.log(age)
  &#125;
&#125;
user.getUserAge('王五')

如果不执行call,apply,bind 此时的this-->user;age-->'25'

let person = &#123;
  data:[
    &#123;name:'李四',age:'20'&#125;
  ]
&#125;

person需要getUserAge方法,不需要重新定义注入,直接借用user的即可

person.getUserAge = user.getUserAge.bind(person,'李四')
person.getUserAge() //此时的this-->person;age-->'20'

<span class="copy-code-btn">复制代码</span></code></pre>
<p>call使用场景</p>
<pre><code class="copyable">  Object.prototype.toString.call 检验类型

  let argArray = &#123;
    0:'王权',
    1:'富贵',
    length:2
  &#125;

  Array.prototype.push.call(argArray,'星星','竹海') // &#123; '0': '王权', '1': '富贵', '2': '星星', '3': '竹海', length: 4 &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>apply使用场景</p>
<pre><code class="copyable">const arr = [0,1,22,66,2,11]
const max = Math.max.apply(Math,arr)
const min = Math.min.apply(Math,arr)
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拓展：</p>
<p>new 关键字</p>
<pre><code class="copyable">不用关键字new

创建一个构造函数
function Person(name,age)&#123;
  this.name = name;
  this.age = age;
&#125;

添加方法
Person.prototype.sayHi = function () &#123;
  console.log(this.name)
&#125;

调用
const person1 = Person('夏有凉风',18)
console.log(person1,'person') // undefined
console.log(window.name) // this -->  window  '夏有凉风'

关键字new
const person2 = new Person('冬有雪',88)
console.log(person2,'person') // Person &#123; name: '冬有雪', age: 88 &#125;
person2.sayHi() // '冬有雪'

实现new 
1.创建一个新的对象
2.新对象[[Prototype]]被赋值位为构造函数的prototype属性
3.构造函数内部的this被赋值为新对象
4.给新对象添加属性
5.返回新的对象
function _new(fn,arguments)&#123;
  cosnt newObj = &#123;&#125;
  newObj._proto_ = fn.prototype; // prototype是函数属性  _proto_ 对象的属性
  fn.apply(newObj,arguments)
  return newObj
&#125;

注意点：如果构造函数返回了非空的对象

function Person(name,age)&#123;
  this.name = name;
  this.age = age;
  return &#123;car:'奔奔'&#125;
&#125;

const person2 = new Person('冬有雪',88) // &#123; car: '奔奔' &#125;

此时new 返回的就是该非空的对象


整合：
function _new(fn,...args)&#123;
  cosnt newObj = Object.create(fn.prototype)
  const res = fn.apply(newObj,args)
  return res instabceof Object ? res : newObj
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            