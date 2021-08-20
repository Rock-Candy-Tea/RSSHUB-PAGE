
---
title: 'js 异步队列的并发控制 ，推荐一个好用的插件包 js-asyncpool'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50a8d9de2f1d4f688c827ee204f0c10b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 03:25:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50a8d9de2f1d4f688c827ee204f0c10b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">问题场景</h2>
<p>Promise.all 在跑异步的时候是全部并发同时处理的。这样对一些大量的xhr请求 对服务器压力太大会无法响应请求</p>
<h2 data-id="heading-1">需求</h2>
<p>同时并发指定的数量（1个或者多个）后，不再增加，除非有进程结束后，从promise任务中按照顺序启动新的异步任务</p>
<h2 data-id="heading-2">过程</h2>
<p>使用前</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50a8d9de2f1d4f688c827ee204f0c10b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用插件限制并发为5个后</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce89d5611e6435ab5a8c3a0fa200d52~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe12337f9ee4a71a9118b72e60fbc90~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只有指定数量的任务结束，才会启动新的任务</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bccaf8d80282491cb771f177da748d80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">插件说明</h2>
<p>npm 地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjs-asyncpool" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/js-asyncpool" ref="nofollow noopener noreferrer">www.npmjs.com/package/js-…</a></p>
<h3 data-id="heading-4">说明</h3>
<blockquote>
<p>同Promise.all 一样，实际上是一个函数，它接受一个 promises 数组并返回一个 Promise,并可以限制同时并发异步的数量</p>
</blockquote>
<h5 data-id="heading-5">0. 安装</h5>
<pre><code class="copyable">npm i js-asyncpool --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">1. 引入</h5>
<pre><code class="copyable">import jsAsyncPool from 'js-asyncpool'

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">2. 参数说明</h5>
<p>jsAsyncPool.asyncPool(promiseArr,limit)</p>

















<table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>promiseArr</td><td>promise 对象组成的数组</td></tr><tr><td>limit</td><td>可同时并发几个,以此类推</td></tr></tbody></table>
<h5 data-id="heading-8">3. 例子</h5>
<pre><code class="copyable">import jsAsyncPool from 'js-asyncpool'

let arr = []
function createPromise (j) &#123;
  return ()=>&#123;
    return new Promise(resolve => &#123;
      console.log(`promise$&#123;j&#125; start`);
      setTimeout(() => &#123;
        console.log(`promise$&#123;j&#125; over------`);
        resolve();
      &#125;, 3000);
    &#125;)
  &#125;
&#125;

arr.push(createPromise(1))
arr.push(createPromise(2))
arr.push(createPromise(3))
arr.push(createPromise(4))
arr.push(createPromise(5))
arr.push(createPromise(6))
arr.push(createPromise(7))
console.log(arr,'----arr')
jsAsyncPool.asyncPool(arr,3)

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<ol start="0">
<li>更新</li>
</ol>
<pre><code class="copyable">npm update js-asyncpool
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">相关知识点</h2>
<h5 data-id="heading-10">一、Pomise.all的使用</h5>
<p>常见使用场景 ： 多个异步结果合并到一起</p>
<p>Promise.all可以将多个Promise实例包装成一个新的Promise实例。用于将多个Promise实例，包装成一个新的Promise实例。</p>
<p>1.它接受一个数组作为参数。</p>
<p>2.数组可以是Promise对象，也可以是其它值，只有Promise会等待状态改变。</p>
<p>3.当所有的子Promise都完成，该Promise完成，返回值是全部值的数组。</p>
<p>4.如果有任何一个失败，该Promise失败，返回值是第一个失败的子Promise的结果。</p>
<p>代码例子</p>
<pre><code class="copyable">let p1 = new Promise((resolve, reject) => &#123;
  resolve('成功了')
&#125;)

let p2 = new Promise((resolve, reject) => &#123;
  resolve('success')
&#125;)

let p3 = Promse.reject('失败')

Promise.all([p1, p2]).then((result) => &#123;
  console.log(result)               //['成功了', 'success']
&#125;).catch((error) => &#123;
  console.log(error)
&#125;)

Promise.all([p1,p3,p2]).then((result) => &#123;
  console.log(result)
&#125;).catch((error) => &#123;
  console.log(error)      // 失败了，打出 '失败'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">二、Promise.race的使用</h5>
<p>类似于Promise.all() ,区别在于 它有任意一个返回成功后，就算完成，但是 进程不会立即停止</p>
<p>常见使用场景：把异步操作和定时器放到一起，如果定时器先触发，认为超时，告知用户</p>
<pre><code class="copyable">let p1 = new Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    resolve('成功了')
  &#125;, 2000);
&#125;)

let p2 = new Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    resolve('success')    
  &#125;, 5000);
&#125;)


Promise.race([p1, p2]).then((result) => &#123;
  console.log(result)               //['成功了', 'success']
&#125;).catch((error) => &#123;
  console.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            