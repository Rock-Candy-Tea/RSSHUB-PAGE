
---
title: 'ES6新增语法(一)——let、const、var的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b0380294b7446f868aa4a49d73dd59~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:09:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b0380294b7446f868aa4a49d73dd59~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>ES6简介
ES6是ECMAScript 6.0的简称，是javascript语言的下一代标准，已经在2015年6月正式发布上线。目的就是为了统一javascript的语法标准，可以用来开发大型应用程序，称为企业级开发语言。</p>
<p>ES6与JavaScript的关系:</p>
<p>ES6是JavaScript的规范标准，JavaScript是ES6的一种实现。</p>
<p>变量/赋值
块级作用域&#123;&#125;</p>
<p>ES5中作用域有：全局作用域、函数作用域，没有块作用域的概念。ES6新增了块级作用域，块作用域由&#123;&#125;包括，if语句里面的&#123;&#125;也属于块级作用域。</p>
<p>复制代码
//通过定义的变量可以跨块作用域访问到
&#123;
var a = 12;
console.log("a",a)
&#125;
console.log("a",a)
复制代码
//通过var定义的变量不能通过跨函数作用域访问到
(function()&#123;
var b = 5;
&#125;)()
console.log("b",b) // not defined
var 与let和const区别：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b0380294b7446f868aa4a49d73dd59~tplv-k3u1fbpfcp-watermark.image" alt="1626250108(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>const定义的对象属性是否可以改变？</p>
<p>实例：修改对象的属性值。</p>
<p>const per = &#123;
name:'倩倩'
&#125;
per.name = "我是嘻哈"
console.log("per.name",per.name) //打印出我是嘻哈
通过上个实例，我们发现对象的属性是可以修改的，这是什么原因呢？</p>
<p>对象是引用类型的，per中保存的仅是对象的指针，意味着指针不会发生改变，修改对象的属性不会改变对象的指针，所以是允许修改的。</p>
<p>赋值：新增解构赋值，就是对数据拆解并赋值。解构赋值的两个规则：</p>
<p>左右两边模式必须一致
必须让定义和赋值同步完成。
实例：正确的结构赋值</p>
<p>let [a,b,c] = [1,2,3]
console.log("a",a)//1
console.log("b",b)//2
console.log("c",c)//3</p>
<p>实例：左右两边模式一致，数据长短不同时</p>
<p>let [bar, foo] = [1];
console.log("bar",bar)//1
console.log("foo",foo) // undefined
上述解构不成功，变量值等于undefined。</p>
<p>注意：对象也是可以解构的，但是需要注意的是对象和数组的解构有很大的区别，对象的属性没有次序，变量必须与属性同名，才能取到正确的值。</p>
<p>复制代码
let &#123; bar,foo &#125; = &#123;
foo:'aaa',
bar:'bbb'
&#125;
console.log('bar',bar)
console.log('foo',foo)
console.log('baz',baz) // not defined
复制代码</p></div>  
</div>
            