
---
title: '前端js基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6428'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 19:21:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=6428'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前端知识 （JS）</h2>
<h3 data-id="heading-1">1.Promise、Promise.all、Promise.race 分别怎么用？</h3>
<ol>
<li>
<p>Promise 用法</p>
<pre><code class="copyable"> function fn()&#123;
   return new Promise((resolve, reject)=>&#123;
      成功时调用 resolve(数据)
      失败时调用 reject(错误)
   &#125;)
&#125;
fn().then(success, fail).then(success2, fail2)      
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Promise.all 用法</p>
<pre><code class="copyable"> Promise.all([promise1, promise2]).then(success1, fail1)
 promise1和promise2都成功才会调用success1   
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>举例:<br>
promise.all 是解决并发问题的，多个异步并发获取最终的结果（如果有一个失败则失败）<br>
Promise.all(iterable) 方法返回一个 Promise 实例，此实例在 iterable 参数内所有的promise都“完成（resolved）”或参数  中不包含promise时回调完成(resolve)；<br>
如果参数中promise有一个失败(rejected)，此实例回调失败(reject)，失败的原因是第一个失败promise的结果。它通常在启动多  个异步任务并发运行并为其结果创建承诺之后使用，以便人们可以等待所有任务完成。<br>
参数iterable表示一个可迭代对象，如 Array 或 String。<br>
示例：<br>
Promise.all 的使用，Promise.all 等待所有都完成（或第一个失败）。</p>
<pre><code class="copyable">var p1 = Promise.resolve(3);
var p2 = 1337;
var p3 = new Promise((resolve, reject) => &#123;
setTimeout(resolve, 100, 'foo');
&#125;); 
Promise.all([p1, p2, p3]).then(values => &#123; 
console.log(values); // [3, 1337, "foo"] 
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.Promise.race 用法</p>
<pre><code class="copyable">Promise.race([promise1, promise2]).then(success1, fail1)
promise1和promise2只要有一个成功就会调用success1；
promise1和promise2只要有一个失败就会调用fail1；
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总之，谁第一个成功或失败，就认为是race的成功或失败。<br>
Promise.race 用来处理多个请求，采用最快的(谁先完成用谁的)。<br>
Promise.race(iterable)方法返回一个promise，一旦迭代器中的某个promise解决或拒绝，返回的 promise就会解决或拒绝。</p>
<pre><code class="copyable">const promise1 = new Promise((resolve,reject) =>&#123;
setTimeout(resolve,500,'one');
&#125;);
const promise2 = new Promise ((resolve,reject) => &#123;
setTimeout(resolve,100,'two');
&#125;);
Promise.race([promise1,promise2]).then((value) => &#123;
console.log(value);
// Both resolve,but promise2 is faster
&#125;)  //expected output:"two"
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-2">2.手写函数防抖和函数节流</h3>
<p>函数节流(throttle) 可理解为 cd 冷却时间，可用在拉动滚动条时,每隔一段时间判断是否已经滚动到底。</p>
<pre><code class="copyable">function fn()&#123;&#125;
  var cd = false
  button.onclick = function()&#123;
  if(cd)&#123;
    //
  &#125;else &#123;
    fn()
    cd = true
    var timerId = setTemeout(()=>
      cd = false
    &#125;,3000)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或：</p>
<pre><code class="copyable">// 节流（执行一次之后，在一段时间内就不再执行第二次）
  function throttle(fn, delay)&#123;
    let canUse = true
    return function()&#123;
      if(canUse)&#123;
         fn.apply(this, arguments)
         canUse = false
         setTimeout(()=>canUse = true, delay)
       &#125;
    &#125;
  &#125;
  const throttled = throttle(()=>console.log('hi'))
  throttled()
  throttled()
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数防抖(debounce) 即带着一起做(如抢外卖订单去送)任务频繁触发的情况下，只有任务触发的间隔超过指定间隔的时候，任务才会执行。在事件被触发n秒后再执行回调，如果在这n秒内又被触发，则重新计时。可用在用户名注册检查：在一定时间内检查输入框输入的用户名是否存在或合法。</p>
<pre><code class="copyable">var timerId = null
button.onclick = function()&#123;
   if(timerId)&#123;
      window.clearTimeout(timerId)
   &#125;
   timerId = setTimeout(()=>&#123;
      fn()
      timerId = null
   &#125;,5000)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或：</p>
<pre><code class="copyable">// 防抖（一段时间内会等，超过这段时间后会带着一起做）
function debounce(fn, delay)&#123;
  let timerId = null
  return function()&#123;
    const context = this
    if(timerId)&#123;window.clearTimeout(timerId)&#125;
    timerId = setTimeout(()=>&#123;
       fn.apply(context, arguments)
       timerId = null
    &#125;,delay)
  &#125;
&#125;
const debounced = debounce(()=>console.log('hi'))
debounced()
debounced()
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-3">3. 手写Ajax</h3>
<pre><code class="copyable">// 常规版      
var request = new XMLHttpRequest()
request.open('GET','/a/b/c?name=ff',true)
request.onreadystatechange =function()&#123;
   if(request.readyState ===4)&#123;
      console.log('请求完成') 
      if(request.status >=200 && request.status <300)&#123;
         console.log('请求成功'）// console.log(request.responseText)
      &#125;else&#123;
      &#125;
    &#125;
&#125;
request.send()    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>or</p>
<pre><code class="copyable">// 简化版
var request = new XMLHttpRequest()
request.open('GET','/xxxx')
request.onload = ()=>&#123;console.log('请求成功')&#125;
request.send()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">AJAX 是什么?</h5>
<p>AJAX（Asynchronous-JavaScript-and-XML），指的是通过JavaScript的异步通信，从服务器获取XML文档从中提取数据，再更新当前网页的对应部分，而不用刷新整个网页。<br>
后来，AJAX这个词就成为JavaScript脚本发起HTTP通信的代名词，也就是说，只要用脚本发起通信，就可以叫做 AJAX 通信。</p>
<h5 data-id="heading-5">AJAX的步骤：</h5>
<p>1.创建XMLHttpRequest实例对象<br>
2.发出Http请求<br>
3.服务器返回XML格式的字符串<br>
4.JS解析XML，并更新局部页面</p>
<p>不过随着历史进程的推进，XML 已经被淘汰，取而代之的是 JSON。
JSON（JavaScript Object Notation，JavaScript对象表示法）是一种由 Douglas Crockford 构想和设计、轻量级的数据交换语言。它是 JavaScript 的一个子集，因此 JSON 在语法上保留了很多 JavaScript 的特征。</p>
<h5 data-id="heading-6">区别：</h5>
<p>JSON 没有 function、undefined，也没有 Number 中的 NaN 和 Infinity;<br>
JSON 字符串的首尾必须是双引号，这意味着对象的键也必须加上双引号;<br>
JSON只是一种数据格式，数据格式其实就是一种规范，格式、形式、规范是不能用来存储数据的。因此诸如 var obj = &#123;"width":100,"height":200,"name":"rose"&#125;
这样的不能称之为 JSON 对象，而是一种 JSON 格式的 JS 对象。<br>
XMLHttpRequest对象是AJAX的主要接口，用于浏览器与服务器之间的通信。尽管名字里面有XML和HTTP，它实际上可以使用多种协议（比如file或ftp），发送任何格式的数据（包括字符串和二进制）。</p>
<h4 data-id="heading-7">注意：</h4>
<p>AJAX 只能向同源网址（协议、域名、端口都相同）发出 HTTP 请求，如果发出跨域请求，就会报错。<br>
XMLHttpRequest 的实例属性<br>
XMLHttpRequest.readyState<br>
XMLHttpRequest.readyState 属性返回一个 XMLHttpRequest 代理当前所处的状态。</p>
<hr>
<h3 data-id="heading-8">4. 闭包/立即执行函数是什么?</h3></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            