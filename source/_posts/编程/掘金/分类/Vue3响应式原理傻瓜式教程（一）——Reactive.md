
---
title: 'Vue3响应式原理傻瓜式教程（一）——Reactive'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2866968105a94938ab3a35baa1fb52d9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 01:41:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2866968105a94938ab3a35baa1fb52d9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>参考教程：<a href="https://www.vuemastery.com/courses/vue-3-reactivity/" target="_blank" rel="nofollow noopener noreferrer">Vue Mastery</a></p>
<h2 data-id="heading-0">理解响应式</h2>
<p>什么是响应式呢？举个简单的例子。</p>
<pre><code class="copyable">let price = 5;
let quantity = 2;
let total = price * quantity; // 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们将<code>price</code>改为6，期望<code>total</code>值也能自动计算更新为12。<br>
而这个自动计算更新，就是响应式。<br>
这一节我们先来谈论一下，如何触发计算更新。</p>
<h2 data-id="heading-1">如何实现更新计算结果</h2>
<pre><code class="copyable">let price = 5;
let quantity = 2;

let dep = new Set() // 相当于收集方法（依赖）的仓库

let effect = () => &#123; // 计算方法
  total = price * qunatity
&#125;
function track() &#123; // 添加计算方法到仓库中
  dep.add(effect)
&#125;
function trigger() &#123; // 触发仓库中的方法
  dep.forEach(effect => effect())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一步，我们需要把<code>effect</code>收集起来，以便于需要的时候再次调用。</p>
<pre><code class="copyable">track()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步，执行<code>effect</code>得到初始的结果</p>
<pre><code class="copyable">effect() // total = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步，当<code>price</code>发生改变时，再次触发已收集的方法。</p>
<pre><code class="copyable">price = 6 // 此时total还是10
trigger() // 此时得到total = 12
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">多个属性怎么办？</h2>
<p>上面我们实现了一个计算方法的存储。<br>
实际上，每个对象会有多个属性。<br>
而每个属性，也都有它们各自的dep，来存储一个或多个effect。</p>
<pre><code class="copyable">let product = &#123; price: 5, quantity: 2 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们建立起一个大的依赖仓库：<code>depsMap</code>。</p>
<pre><code class="copyable">const depsMap = new Map()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>depsMap</code>中，用属性名（如<code>price</code>或<code>qunatity</code>）作为<code>key</code>，用各自的<code>dep</code>作为<code>value</code>。<br>
那么，<code>track</code>方法应该这样写：</p>
<pre><code class="copyable">function track(key) &#123;
  let dep = depsMap.get(key)
  if (!dep) &#123; // 找不到就建一个
    depsMap.set(key, (dep = new Set()))
  &#125;
  dep.add(effect)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，<code>trigger</code>方法也要改写啦：</p>
<pre><code class="copyable">function trigger(key) &#123;
  let dep = depsMap.get(key)
  if (dep) &#123;
    dep.forEach(effect => effect())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来运行一下吧：</p>
<pre><code class="copyable">let product = &#123; price: 5, quantity: 2 &#125;
let total = 0

let effect = () => &#123; 
  total = product.price * product.quantity
&#125;

track('price')
effect() // total = 10

product.price = 6 // total = 10
trigger('price') // total = 12

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">多个对象怎么办？</h2>
<p>上面我们实现了一个对象的响应，接下来我们来探讨下多个对象的收集方法。<br>
我们需要创建一个更大的仓库来存储多个object，每个object都有属于自己的depsMap。</p>
<pre><code class="copyable">const targetMap = new WeakMap()
// 为什么用WeakMap我们暂时不讨论，目前只需要知道，它的key必须是object类型

function track(target, key) &#123;
  let depsMap = targetMap.get(target)
  if (!depsMap) &#123;  // 找不到就建一个
    targetMap.set(target, (depsMap = new Map()))
  &#125;
  let dep = depsMap.get(key)
  if (!dep) &#123;
    depsMap.set(key, (dep = new Set()))
  &#125;
  dep.add(effect)
&#125;

function trigger(target, key) &#123;
  const depsMap = targetMap.get(target)
  if (!depsMap) return // 如果没有任何依赖，直接返回
  let dep = depsMap.get(key)
  if (dep) &#123;
    dep.forEach(effect => effect())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来运行一下：</p>
<pre><code class="copyable">let product = &#123; price: 5, quantity: 2 &#125;
let total = 0
const depsMap = new Map()
let effect = () => &#123; 
  total = product.price * product.quantity
&#125;

track('product', 'price')
effect() // total = 10

product.price = 6  // total = 10
trigger('product', 'price') // total = 12
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<ul>
<li>targetMap</li>
</ul>
<p>用于存放每个响应式object（所有属性）的依赖</p>
<ul>
<li>depsMap</li>
</ul>
<p>用于存放响应式object每个属性对应的依赖</p>
<ul>
<li>dep</li>
</ul>
<p>用于存放某个属性对应的所有依赖，当属性发生变化时，会执行依赖
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2866968105a94938ab3a35baa1fb52d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            