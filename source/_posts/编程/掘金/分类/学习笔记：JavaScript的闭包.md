
---
title: '学习笔记：JavaScript的闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6322'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 23:13:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=6322'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>了解闭包的前提，需要先知道JavaScript的变量作用域</p>
<ol>
<li>
<p>全局变量</p>
</li>
<li>
<p>局部变量</p>
<p>const a = 1
function func()&#123;
console.log(a);
&#125;
func() // 1 函数内部可以读取全局变量</p>
<p>function f1()&#123;
const a=1;
&#125;
console.log(a) // Uncaught ReferenceError: a is not defined  函数外部无法读取函数内的局部变量</p>
</li>
</ol>
<p>此外ES6的const和let本身就有块级作用域的概念。</p>
<p>有时候，我们就需要得到函数内的局部变量，那怎么办？闭包的出现，就是为了解决这个问题。</p>
<pre><code class="copyable">function f1()&#123;
  
    const n=1;
    
    function f2()&#123;
        console.log(n);
    &#125;

    return f2;
&#125;

const result=f1();

result(); // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以<strong>闭包</strong>的概念，我个人是这样理解：<strong>闭包是一个函数，这个函数定义在某个函数的内部。</strong></p>
<p>理解有不对的地方请指正~</p>
<p>f2 函数就是一个闭包，这个函数定义在f1的内部。</p>
<p>闭包除了让外部函数可以读取函数内部的变量外，另一个用户就是让这些变量的值始终保持在内存中。</p>
<pre><code class="copyable">function f1() &#123;

    let n = 1;

    function f2() &#123;
        n = n + 1;
        console.log(n);
    &#125;

    return f2;

&#125;

const result = f1();

result();  // 2
result();  // 3
result();  // 4
result = null // 释放对闭包的引用 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数f1中的变量n一直保存在内存中，并没有在f1调用后被自动清除。因为f1是f2的父函数，而f2被赋给了全局变量result，这导致f2始终在内存中，而f2的存在依赖于f1，因此f1也始终在内存中，不会在调用结束后，被垃圾回收机制回收。</p>
<p>闭包常见的应用场景是<strong>创建私有变量和方法</strong></p>
<pre><code class="copyable">function Person() &#123;

    // 私有变量
    const age = 11;

    function run() &#123;
        console.log(2);
    &#125;

    // 访问方法
    this.getAge = function () &#123;
        return age;
    &#125;;
&#125;

const age = new Person();
console.log(age.getAge());  // 11
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            