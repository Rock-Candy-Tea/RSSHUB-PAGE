
---
title: 'async和await'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6080'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:01:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=6080'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">小结</h2>
<pre><code class="copyable">await后面接一个会return new promise的函数并执行它
await只能放在async函数里
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">什么是async</h2>
<pre><code class="copyable">ES7 提出的async 函数，终于让 JavaScript 对于异步操作有了终极解决方案。No more callback hell。
async 函数是 Generator 函数的语法糖。使用 关键字 async 来表示，在函数内部使用 await 来表示异步。
想较于 Generator，Async 函数的改进在于下面四点：
- **内置执行器**。Generator 函数的执行必须依靠执行器，而<font color=#A52A2A>Aysnc</font>函数自带执行器，调用方式跟普通函数的调用一样
- **更好的语义**。async 和 await 相较于 * 和 yield 更加语义化
- **更广的适用性**。co 模块约定，yield 命令后面只能是 Thunk 函数或 Promise对象。而 async 函数的 await 命令后面则可以是 Promise 或者 原始类型的值（Number，string，boolean，但这时等同于同步操作）
- **返回值是 Promise**。async 函数返回值是 Promise 对象，比 Generator 函数返回的 Iterator 对象方便，可以直接使用 then() 方法进行调用
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">如何使用async</h2>
<pre><code class="copyable">结果必须return，不然值都为undefined， 建议使用箭头函数
可以return各种数据类型的值，皆为resolve
但是返回如下结果，则判定失败reject
1. 内部含有直接使用未声明的变量或函数
2. 内部抛出一个错误throw new Error 或者返回reject状态 return Promise.reject('执行失败')
3. 函数方法执行错误
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">什么是await</h2>
<pre><code class="copyable">await意思是async wait(异步等待)。这个关键字只能在使用async定义的函数里面使用。
任何async函数都会默认返回promise，并且这个promise解析的值都将会是这个函数的返回值，而async函数必须等到内部所有的 await 命令的 Promise 对象执行完，才会发生状态改变。
正常情况下，await 命令后面跟着的是 Promise ，如果不是的话，也会被转换成一个 立即 resolve 的 Promise。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">async function testSometing() &#123;
    console.log("testSomething");
    return "return testSomething";
&#125;

async function testAsync() &#123;
    console.log("testAsync");
    return Promise.resolve("hello async");
&#125;

async function test() &#123;
    console.log("test start...");

    const testFn1 = await testSometing();
    console.log(testFn1);

    const testFn2 = await testAsync();
    console.log(testFn2);

    console.log('test end...');
&#125;

test();

var promiseFn = new Promise((resolve)=> &#123; 
    console.log("promise START...");
    resolve("promise RESOLVE");
&#125;);
promiseFn.then((val)=> console.log(val));

console.log("===END===")

结果：
test start...
testSomething
promise START...
===END===
return testSomething
test end...
testAsync
promise RESOLVE
hello async
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">1. 执行test(), 先输出"test start..."
2. 声明函数await testSometing()，先执行console.log("testSomething")输出，后跳出test()，执行后面代码
3. 执行promiseFn，输出"promise START..."，遇Promise，放置Promise队列第一位，跳出函数，向下执行
4. 输出"===END==="，返回test()，继续执行console.log(testFn1)，testSometing()被调用，输出"return testSomething"
5.声明函数await testAsync()，先执行console.log("testAsync")输出，后跳出test()，执行后面代码
6. 这时需要执行之前的Promise队列第一位，输出"promise RESOLVE"，返回test()，继续执行console.log(testFn2)，testAsync()被调用，遇Promise，放置当前Promise队列第一位，因当前没有其他代码执行，故输出"hello async"
7. 最后输出"test end..."
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            