
---
title: 'jQuery 都过时了，那我还学它干嘛？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4995'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 19:58:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=4995'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">jQuery 教你如何设计 API</h1>
<p>上文说到我一个不会 JS 的人居然能看懂 jQuery 的书，其实这不是因为我厉害，而是因为 jQuery 的 API 设计得太人性化了！</p>
<p>举几个例子给大家看看：</p>
<ul>
<li>第一个是 jQuery 对事件监听的简化</li>
</ul>
<pre><code class="copyable">// 那时，如果不用 jQuery，监听事件（兼容 IE 6）你要这么写
if (button.addEventListener)  
  button.addEventListener('click',fn);
else if (button.attachEvent) &#123; 
  button.attachEvent('onclick', fn);
&#125;else &#123;
  button.onclick = fn;
 &#125;
  
// 但是如果你用 jQuery，你只需要这么写
$(button).on('click', fn)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二个是 jQuery 对元素选择的简化</li>
</ul>
<pre><code class="copyable">// 如果你想获取 .nav > .navItem 对应的所有元素，用 jQuery 是这样写的
$('.nav > .navItem')

// 在 IE 6 上，你得这么写
var navItems = document.getElementsByClassName('navItem')
var result = []
for(var i = 0; i < navItems.length; i++)&#123;
  if(navItems[i].parentNode.className.match(/\bnav\b/)&#123;
    result.push(navItems[i])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有没有发现 jQuery 的代码一读就读懂了？可读性非常强！</p>
<p>当然我作为一个新人，每每看到 jQuery 那优雅的 API，都禁不住去思考 jQuery 到底是怎么实现的，我自己能不能实现出来（但我并不推荐看 jQuery 源码）。本着这样的想法，我学会了很多编程技巧。</p>
<p>为什么有些人代码水平老是提不高了，就是因为不会造轮子，不会设计优雅的 API，更不会实现优雅的 API，只会调用其他库或框架提供的功能（中枪的举手）。</p>
<p>而 jQuery 则提供了一个简单而又经典的范例供大家学习。</p>
<p>不信的话我们就来看看 jQuery 用到了哪些所谓的设计模式（其实就是编程套路）吧</p>
<h2 data-id="heading-1">1.发布订阅模式</h2>
<pre><code class="copyable">var eventHub = $(&#123;&#125;)
eventHub.on('xxx', function()&#123; console.log('收到') &#125;)
eventHub.trigger('xxx')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.用原型继承实现插件系统</h2>
<pre><code class="copyable">$.fn.modal = function()&#123; ... &#125;
$('#div1').modal()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3.事件委托</h2>
<pre><code class="copyable">$('div').on('click', 'span', function()&#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.链式调用</h2>
<pre><code class="copyable">$('div').text('hi').addClass('red').animate(&#123;left: 100&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5.函数重载（伪）</h2>
<pre><code class="copyable">$(fn)
$('div')
$(div)
$($(div))
$('span', '#scope1')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你会发现 $ 这个函数的参数可以是函数、字符串、元素和 jQuery 对象，甚至还能接受多个参数，这种重载是怎么做到的？</p>
<h2 data-id="heading-6">6.命名空间</h2>
<pre><code class="copyable">// 你的插件在一个 button 上绑定了很多事件
$button.on('click.plugin', function()&#123;...&#125;)
$button.on('mouseenter.plugin', function()&#123;...&#125;)
// 然后你想在某个时刻移除以上所有事件
$button.off('.plugin')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">7.高阶函数</h2>
<pre><code class="copyable"> var fn2 = $.proxy(fn1, asThis, param1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>$.proxy 接受一个函数，返回一个新的函数。</p>
<p>其他就不一一列举了。</p>
<h1 data-id="heading-8">jQuery 的 API 风格依然在流行</h1>
<p>我们把 jQuery.ajax 和 Axios 做一下对比：</p>
<pre><code class="copyable">    $.ajax(&#123;url:'/api', method:'get'&#125;)
    $.get('/api').then(fn1,fn2)
    axios(&#123; url: '/api', method: 'get'&#125;)
    axios.get('/api').then(fn1, fn2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么 2018 年流行的 axios 跟 jQuery.ajax 这么相像呢？</p>
<p>因为 jQuery 的 API 实在太好用了！搞得新库根本没法超越它，没有办法设计出更简洁的 API 了。毕竟 jQuery 也是在前端界流行近十年。</p>
<p>所以你学了 jQuery 很容易过渡其他类似的新库。</p>
<p><strong>AngularJS、Vue 1.x、Vue 2.x 其实都是顺着 Backbone MVC 的思路慢慢优化、改造得来的，如果你提前了解 Backbone 作为知识铺垫，那么理解 Vue 是非常容易的。如果面试官问你 MVC 和 MVVM 的区别，你也是很容易就可以答出来的。</strong></p></div>  
</div>
            