
---
title: 'ES6新增语法(五)——Promise详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7097'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 23:26:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=7097'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Promise介绍</h1>
<p>promise是一个对象，从它可以获取异步操作的消息。有all、race、reject、resolve这几个方法，原型上有then、catch等方法。</p>
<p>Promise的两个特点：</p>
<ul>
<li>对象的状态不受外界影响。Promise对象获取的是异步操作，有三种状态：pending(进行中)、fulfilled(已成功)、reject(已失败)。除了异步操作的结果，其他操作都无法改变这个状态。</li>
<li>一旦状态改变，就不会再变。从pending变为fulfilled和从pending变为rejected状态，只要处于fulfilled和rejected，状态就不会再变。</li>
</ul>
<p>状态的缺点：</p>
<p>无法取消Promise，一旦新建它就会立即执行，无法中途取消。</p>
<p>如果不设置回调函数，Promise内部抛出错误，不会反应到外部。</p>
<p>当处于pending状态时，无法得知目前进展到哪一阶段。</p>
<p><strong>使用语法：</strong></p>
<p>let p = new Promise( (resolve,reject)=>&#123;</p>
<p>//resolve 和reject是两个函数</p>
<p>&#125;)</p>
<p>p.then(</p>
<p>()=>&#123;&#125;, // 传入的resolve函数，resolve翻译成中文是解决</p>
<p>()=>&#123;&#125; //传入的reject函数，reject翻译成中文是拒绝</p>
<p>).catch((reason,data)=>&#123;</p>
<p>console.log("catch失败执行回调抛出原因",reason)</p>
<p>&#125;)</p>
<h1 data-id="heading-1">then方法</h1>
<p>then方法接收两个参数作为参数，第一个参数是Promise执行成功时的回调，第二个参数是Promise执行失败的回调，两个函数只会有一个被调用。</p>
<p>通过.then添加的回调函数，不论什么时候，都会被调用，而且可以添加多个回调函数，会一次按照顺序并且独立运行。</p>
<pre><code class="copyable">const p =new Promise((resolve,reject)=>&#123;
 resolve("成功")
&#125;)
p.then((res)=>&#123;
 console.log(res)//返回成功
&#125;,(err)=>&#123;
 console.log(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带有多个回调函数时</p>
<pre><code class="copyable">const p =new Promise((resolve,reject)=>&#123;
 resolve(1)
&#125;)
p.then((res1)=>&#123;
 console.log('res1',res1) // 1
 return res1 * 2;
&#125;).then((res2)=>&#123;
 console.log('res2',res2) //2
&#125;).then((res3)=>&#123;
 console.log('res3',res3) //undefined
 return Promise.resolve('resolve')
&#125;).then(res4=>&#123;
 console.log('res4',res4) //resolve
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">catch用法</h1>
<p>与Promise对象方法then并行的还有一个catch方法，用来捕获异常的，与try...catch类似，</p>
<pre><code class="copyable">const p1 = new Promise((resolve,reject)=>&#123;
 var num = Math.random()*10 ;//随机生成一个0-10的数字 
 console.log("num",num)
 if(num > 5)&#123;
  resolve('大于5')
 &#125;else&#123;
  reject("小于5")
 &#125;
&#125;)
p1.then(res=>&#123;
 console.log("res",res) // res 大于5
&#125;).catch(err=>&#123;
 console.log("err",err) // err 小于5
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">all方法</h1>
<p>all方法表示所有的异步操作完成后才执行回调，返回结果，返回的数据是个数组，多个请求返回的数据组合。与then方法同级。</p>
<p>使用语法：Promise.all([ p,p1,p2.... ]).then()</p>
<p>使用实例如下：</p>
<pre><code class="copyable">const p1 = new Promise((resolve,reject)=>&#123;
 resolve(&#123;
  name:'倩倩'
 &#125;)
&#125;)
const p2 = new Promise((resolve,reject)=>&#123;
 resolve(['a','b'])
&#125;)
const p3 = new Promise((resolve,reject)=>&#123;
 resolve('二傻子')
&#125;)
Promise.all([p1,p2,p3]).then(res=>&#123;
 console.log(res)//[&#123;name:'倩倩'&#125;, ['a','b'], "二傻子"]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">race方法</h1>
<p>all是等所有的异步操作都执行完成了再执行回调，而race方法是相反的，只要有一个执行完成，不论结果是成功还是失败，都开始执行回调，其余的不会再进入race的回调。返回的数据取决于最早执行完毕返回的数据。</p>
<pre><code class="copyable">const p1 = new Promise((resolve,reject)=>&#123;
 resolve(&#123;
  name:'倩倩'
 &#125;)
&#125;)
const p2 = new Promise((resolve,reject)=>&#123;          
 setTimeout(()=>&#123;
  resolve(['a','b'])
 &#125;,1000)
&#125;)
const p3 = new Promise((resolve,reject)=>&#123;
 setTimeout(()=>&#123;
  resolve('二傻子')
 &#125;,2000)
&#125;)
Promise.race([p1,p2,p3]).then(res=>&#123;
 console.log(res)//&#123;name:'倩倩'&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">为什么使用Promise？</h1>
<p>Promise的优点</p>
<ul>
<li>指定回调函数的方式更加灵活。</li>
<li>支持链式调用，可以解决回调地狱问题。回调地狱就是回调函数嵌套调用，外部回调函数异步执行的结果是嵌套的回调函数的执行条件。回调地狱的缺点是不便于阅读和异常处理。</li>
</ul>
<p>Promise的缺点</p>
<ul>
<li>无法取消Promise，一旦新建就会立即执行，无法暂停和取消。</li>
<li>如果不设置回调函数，Promise内部抛出的错误，不会反应到外部。</li>
<li>当处于pending(进行中)状态时，无法得知目前进展到哪一个阶段。</li>
</ul></div>  
</div>
            