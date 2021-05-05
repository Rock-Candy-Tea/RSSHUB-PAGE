
---
title: '浅析Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2359'
author: 掘金
comments: false
date: Tue, 04 May 2021 18:27:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=2359'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Promise 的用途</h2>
<p>Promise是异步编程的一种解决方案，比传统的解决方案更合理和规范。</p>
<p>相比较传统方法，Promise的三大好处有：</p>
<ol>
<li>
<p>回调的名字和顺序规范</p>
</li>
<li>
<p>避免回调地狱,让代码可读性更强</p>
</li>
<li>
<p>方便捕获错误</p>
</li>
</ol>
<h2 data-id="heading-1">如何创建一个 new Promise</h2>
<p><code>return new Promise((resolve,reject)=>&#123;...&#125;)</code></p>
<p>任务成功则调用<code>resolve(result)</code></p>
<p>任务失败则调用<code>reject(error)</code></p>
<p><code>resolve</code>和<code>reject</code>会再去调用成功和失败函数</p>
<h2 data-id="heading-2">如何使用 Promise.prototype.then</h2>
<pre><code class="copyable">getData(1)
.then(function(x)&#123;
  console.log(x)
  return getData(2)
&#125;, e=>&#123;console.log(e)&#125;)
.then(function(x)&#123;
  console.log(x)
  return getData(3)
&#125;, e=>&#123;console.log(e)&#125;)
.then(function(x)&#123;
  console.log(x)
&#125;, e=>&#123;console.log(e)&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>then()</code>接受两个函数</p>
<p>成功的时候执行第一个函数,失败的时候执行第二个函数</p>
<h2 data-id="heading-3">如何使用 Promise.all</h2>
<p>当我们需要获得多个数据才进行下一步时使用<code>Promise.all</code>：</p>
<pre><code class="copyable">Promise.all([func1(), func2(), func3()]).then()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise.all</code>需要传入一个数组,数组中的元素都是Promise对象,当这些对象都执行成功,执行then中的第一个函数，失败时只能获得第一个失败Promise的错误数据</p>
<p><code>Promise.all</code>是大家一起到终点,一个失败全都失败</p>
<h2 data-id="heading-4">如何使用 Promise.race</h2>
<p><code>Promise.race</code>和<code>Promise.all</code>相对应,哪个Promise对象最快得到结果,就最先用谁的结果（只要快就行,不管失败还是成功）</p></div>  
</div>
            