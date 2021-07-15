
---
title: '手写 Vue2 系列 之 异步更新队列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=211'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 16:23:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=211'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇文章 <a href="https://juejin.cn/post/6983827167079563295" target="_blank" title="https://juejin.cn/post/6983827167079563295">手写 Vue 系列 之 computed</a> 实现了 Vue 的 computed 计算属性。</p>
<h1 data-id="heading-1">目标</h1>
<p>本篇文章是 <code>手写 Vue 系列</code> 的最后一篇，实现 Vue 的异步更新队列。</p>
<p>读过源码，相信大家都知道 Vue 异步更新的大概流程：依赖收集结束之后，当响应式数据发生变化 -> 触发 setter 执行 dep.notify -> 让 dep 通知 自己收集的所有 watcher 执行 update 方法 -> watch.update 调用 queueWatcher 将自己放到 watcher 队列 -> 接下来调用 nextTick 方法将刷新 watcher 队列的方法放到 callbacks 数组 -> 然后将刷新 callbacks 数组的方法放到浏览器的异步任务队列 -> 待将来执行时最终触发 watcher.run 方法，执行 watcher.get 方法。</p>
<h1 data-id="heading-2">实现</h1>
<p>接下来会完整实现 Vue 的异步更新队列，让你彻底理解 Vue 的异步更新过程都发生了什么。</p>
<h2 data-id="heading-3">Watcher</h2>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用来标记 watcher</span>
<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>

**
 * @param &#123;*&#125; cb 回调函数，负责更新 DOM 的回调函数
 * @param &#123;*&#125; options watcher 的配置项
 */
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Watcher</span>(<span class="hljs-params">cb, options = &#123;&#125;, vm = <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-comment">// 标识 watcher</span>
  <span class="hljs-built_in">this</span>.uid = uid++
  <span class="hljs-comment">// ...</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">watcher.update</h2>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 响应式数据更新时，dep 通知 watcher 执行 update 方法，
 * 让 update 方法执行 this._cb 函数更新 DOM
 */</span>
Watcher.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.lazy) &#123; <span class="hljs-comment">// 懒执行，比如 computed 计算属性</span>
    <span class="hljs-comment">// 将 dirty 置为 true，当页面重新渲染获取计算属性时就可以执行 evalute 方法获取最新的值了</span>
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 将 watcher 放入异步 watcher 队列</span>
    queueWatcher(<span class="hljs-built_in">this</span>)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">watcher.run</h2>
<blockquote>
<p>/src/watcher.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 由刷新 watcher 队列的函数调用，负责执行 watcher.get 方法
 */</span>
Watcher.prototype.run = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.get()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">异步更新队列</h2>
<blockquote>
<p>/src/asyncUpdateQueue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 异步更新队列
 */</span>

<span class="hljs-comment">// 存储本次更新的所有 watcher</span>
<span class="hljs-keyword">const</span> queue = []

<span class="hljs-comment">// 标识现在是否正在刷新 watcher 队列</span>
<span class="hljs-keyword">let</span> flushing = <span class="hljs-literal">false</span>
<span class="hljs-comment">// 标识，保证 callbacks 数组中只会有一个刷新 watcher 队列的函数</span>
<span class="hljs-keyword">let</span> waiting = <span class="hljs-literal">false</span>
<span class="hljs-comment">// 存放刷新 watcher 队列的函数，或者用户调用 Vue.nextTick 方法传递的回调函数</span>
<span class="hljs-keyword">const</span> callbacks = []
<span class="hljs-comment">// 标识浏览器当前任务队列中是否存在刷新 callbacks 数组的函数</span>
<span class="hljs-keyword">let</span> pending = <span class="hljs-literal">false</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">queueWatcher</h3>
<blockquote>
<p>/src/asyncUpdateQueue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将 watcher 放入队列
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>watcher 待会儿需要被执行的 watcher，包括渲染 watcher、用户 watcher、computed
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queueWatcher</span>(<span class="hljs-params">watcher</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!queue.includes(watcher)) &#123; <span class="hljs-comment">// 防止重复入队</span>
    <span class="hljs-keyword">if</span> (!flushing) &#123; <span class="hljs-comment">// 现在没有在刷新 watcher 队列</span>
      queue.push(watcher)
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 正在刷新 watcher 队列，比如用户 watcher 的回调函数中更改了某个响应式数据</span>
      <span class="hljs-comment">// 标记当前 watcher 在 for 中是否已经完成入队操作</span>
      <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">false</span>
      <span class="hljs-comment">// 这时的 watcher 队列时有序的(uid 由小到大)，需要保证当前 watcher 插入进去后仍然有序</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = queue.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
        <span class="hljs-keyword">if</span> (queue[i].uid < watcher.uid) &#123; <span class="hljs-comment">// 找到了刚好比当前 watcher.uid 小的那个 watcher 的位置</span>
          <span class="hljs-comment">// 将当前 watcher 插入到该位置的后面</span>
          queue.splice(i + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, watcher)
          flag = <span class="hljs-literal">true</span>
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
      <span class="hljs-keyword">if</span> (!flag) &#123; <span class="hljs-comment">// 说明上面的 for 循环在队列中没找到比当前 watcher.uid 小的 watcher</span>
        <span class="hljs-comment">// 将当前 watcher 插入到队首 </span>
        queue.unshift(watcher)
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (!waiting) &#123; <span class="hljs-comment">// 表示当前 callbacks 数组中还没有刷新 watcher 队列的函数</span>
      <span class="hljs-comment">// 保证 callbacks 数组中只会有一个刷新 watcher 队列的函数</span>
      <span class="hljs-comment">// 因为如果有多个，没有任何意义，第二个执行的时候 watcher 队列已经为空了</span>
      waiting = <span class="hljs-literal">true</span>
      nextTick(flushSchedulerQueue)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">flushSchedulerQueue</h3>
<blockquote>
<p>/src/asyncUpdateQueue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 负责刷新 watcher 队列的函数，由 flushCallbacks 函数调用
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushSchedulerQueue</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 表示正在刷新 watcher 队列</span>
  flushing = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// 给 watcher 队列排序，根据 uid 由小到大排序</span>
  queue.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a.uid - b.uid)
  <span class="hljs-comment">// 遍历队列，依次执行其中每个 watcher 的 run 方法</span>
  <span class="hljs-keyword">while</span> (queue.length) &#123;
    <span class="hljs-comment">// 取出队首的 watcher</span>
    <span class="hljs-keyword">const</span> watcher = queue.shift()
    <span class="hljs-comment">// 执行 run 方法</span>
    watcher.run()
  &#125;
  <span class="hljs-comment">// 到这里 watcher 队列刷新完毕</span>
  flushing = waiting = <span class="hljs-literal">false</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">nextTick</h3>
<blockquote>
<p>/src/asyncUpdateQueue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将刷新 watcher 队列的函数或者用户调用 Vue.nextTick 方法传递的回调函数放入 callbacks 数组
 * 如果当前的浏览器任务队列中没有刷新 callbacks 的函数，则将 flushCallbacks 函数放入任务队列
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextTick</span>(<span class="hljs-params">cb</span>) </span>&#123;
  callbacks.push(cb)
  <span class="hljs-keyword">if</span> (!pending) &#123; <span class="hljs-comment">// 表明浏览器当前任务队列中没有刷新 callbacks 数组的函数</span>
    <span class="hljs-comment">// 将 flushCallbacks 函数放入浏览器的微任务队列</span>
    <span class="hljs-built_in">Promise</span>.resolve().then(flushCallbacks)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">flushCallbacks</h3>
<blockquote>
<p>/src/asyncUpdateQueue.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 负责刷新 callbacks 数组的函数，执行 callbacks 数组中的所有函数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushCallbacks</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 表示浏览器任务队列中的 flushCallbacks 函数已经被拿到执行栈执行了</span>
  <span class="hljs-comment">// 新的 flushCallbacks 函数可以进入浏览器的任务队列了</span>
  pending = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">while</span>(callbacks.length) &#123;
    <span class="hljs-comment">// 拿出最头上的回调函数</span>
    <span class="hljs-keyword">const</span> cb = callbacks.shift()
    <span class="hljs-comment">// 执行回调函数</span>
    cb()
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">总结</h1>
<p>到这里 <code>精通 Vue 系列</code> 就要结束了，现在我们再回头看下整个系列：从 <code>Vue 源码解读</code> 开始到现在的 <code>手写 Vue</code>，总共 20 篇文章。如果你是从头到尾跟下来的，相信我们最初定的目标早已实现，这会儿你是否可以在自己的简历上写上：精通 Vue 源码原理。</p>
<h1 data-id="heading-12">关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank" title="https://juejin.cn/user/1028798616461326">掘金账号</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F359669053" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/359669053" ref="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-13">链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/column/6960553066101735461" target="_blank" title="https://juejin.cn/column/6960553066101735461">精通 Vue 技术栈的源码原理</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F359669053%2Fchannel%2Fdetail%3Fcid%3D178493" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/359669053/channel/detail?cid=178493" ref="nofollow noopener noreferrer">配套视频</a></p>
</li>
<li>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank" title="https://juejin.cn/pin/6958238190398341134">学习交流群</a></p>
</li>
</ul></div>  
</div>
            