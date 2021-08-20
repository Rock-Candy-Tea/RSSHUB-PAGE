
---
title: '13个JavaScript 一行程序，让你看起来像个专家'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5482'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 16:24:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=5482'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：Shadeed
译者：前端小智
来源：medium</p>
</blockquote>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>JavaScript 可以做很多好玩的事， 从复杂的框架到处理API，有太多的东西需要学习。但是，它也能让我们只用一行就能做一些了不起的事情。</p>
<h3 data-id="heading-0">1. 获得一个随机的布尔值（<code>true</code>/<code>false</code>）</h3>
<p>该函数使用<code>Math.random()</code>方法返回一个布尔值（<code>true</code> 或者 <code>false</code>）。<code>Math.random</code>创建一个<code>0</code>到<code>1</code>之间的随机数，我们只要检查它是否高于或低于<code>0.5</code>，就有50%机会得到<code>true</code>或<code>false</code>。</p>
<pre><code class="copyable">const randomBoolean = () => Math.random() >= 0.5;
console.log(randomBoolean());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 检查所提供的日期是否为工作日</h3>
<p>使用这种方法，我们能够检查在函数中提供的日期是否是工作日或周末的日子。</p>
<pre><code class="copyable">const isWeekday = (date) => date.getDay() % 6 !== 0;

console.log(isWeekday(new Date(2021, 7, 6)));
// true  因为是周五

console.log(isWeekday(new Date(2021, 7, 7)));
// false 因为是周六
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.反转字符串</h3>
<p>有几种不同的方法来反转一个字符串。这是最简单的一种，使用<code>split()</code>、<code>reverse()</code>和<code>join()</code>方法。</p>
<pre><code class="copyable">const reverse = str => str.split('').reverse().join('');
reverse('hello world');     
// 'dlrow olleh'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.检查当前标签是否隐藏</h3>
<p><code>Document.hidden</code> （只读属性）返回布尔值，表示页面是（<code>true</code>）否（<code>false</code>）隐藏。</p>
<pre><code class="copyable">const isBrowserTabInView = () => document.hidden;
isBrowserTabInView();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>场外：无意间发现爱奇艺广告播放时间居然是在当前标签页激活的时候才会进行倒计时，离开当前标签页的时候，倒计时停止，百度一下发现<code>document.hidden</code>这个东东。</p>
<p><code>document.hidden</code>是<code>h5</code>新增加<code>api</code>使用的时候有兼容性问题。</p>
<pre><code class="copyable">var hidden
if (typeof document.hidden !== "undefined") &#123;
    hidden = "hidden";
&#125; else if (typeof document.mozHidden !== "undefined") &#123;
    hidden = "mozHidden";
&#125; else if (typeof document.msHidden !== "undefined") &#123;
    hidden = "msHidden";
&#125; else if (typeof document.webkitHidden !== "undefined") &#123;
    hidden = "webkitHidden";
&#125;
console.log("当前页面是否被隐藏：" + document[hidden])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. 检查一个数字是偶数还是奇数</h3>
<pre><code class="copyable">const isEven = num => num % 2 === 0;
console.log(isEven(2));
// true
console.log(isEven(3));
// false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 从一个日期获取时间</h3>
<pre><code class="copyable">const timeFromDate = date => date.toTimeString().slice(0, 8);

console.log(timeFromDate(new Date(2021, 0, 10, 17, 30, 0))); 
// "17:30:00"

console.log(timeFromDate(new Date()));
// 打印当前的时间
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7. 保留 n 位小数</h3>
<pre><code class="copyable">const toFixed = (n, fixed) => ~~(Math.pow(10, fixed) * n) / Math.pow(10, fixed);
// 事例
toFixed(25.198726354, 1);       // 25.1
toFixed(25.198726354, 2);       // 25.19
toFixed(25.198726354, 3);       // 25.198
toFixed(25.198726354, 4);       // 25.1987
toFixed(25.198726354, 5);       // 25.19872
toFixed(25.198726354, 6);       // 25.198726
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8. 检查当前是否有元素处于焦点中</h3>
<p>我们可以使用<code>document.activeElement</code>属性检查一个元素是否当前处于焦点。</p>
<pre><code class="copyable">const elementIsInFocus = (el) => (el === document.activeElement);
elementIsInFocus(anyElement)
// 如果在焦点中返回true，如果不在焦点中返回 false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9. 检查当前浏览器是否支持触摸事件</h3>
<pre><code class="copyable">const touchSupported = () => &#123;
  ('ontouchstart' in window || window.DocumentTouch && document instanceof window.DocumentTouch);
&#125;
console.log(touchSupported());
// 如果支持触摸事件，将返回true，如果不支持则返回false。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10. 检查当前浏览器是否在苹果设备上</h3>
<pre><code class="copyable">const isAppleDevice = /Mac|iPod|iPhone|iPad/.test(navigator.platform);
console.log(isAppleDevice);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">11. 滚动到页面顶部</h3>
<pre><code class="copyable">const goToTop = () => window.scrollTo(0, 0);
goToTop();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">12. 获取参数的平均数值</h3>
<pre><code class="copyable">const average = (...args) => args.reduce((a, b) => a + b) / args.length;
average(1, 2, 3, 4);
// 2.5
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">13.华氏/摄氏转换</h3>
<pre><code class="copyable">const celsiusToFahrenheit = (celsius) => celsius * 9/5 + 32;
const fahrenheitToCelsius = (fahrenheit) => (fahrenheit - 32) * 5/9;
// 事例
celsiusToFahrenheit(15);    // 59
celsiusToFahrenheit(0);     // 32
celsiusToFahrenheit(-20);   // -4
fahrenheitToCelsius(59);    // 15
fahrenheitToCelsius(32);    // 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>~完，我是刷碗智，会所按摩走起！</p>
<hr>
<p>原文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Fdailyjs%2F13-javascript-one-liners-thatll-make-you-look-like-a-pro-29a27b6f51cb" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/dailyjs/13-javascript-one-liners-thatll-make-you-look-like-a-pro-29a27b6f51cb" ref="nofollow noopener noreferrer">medium.com/dailyjs/13-…</a></p>
<h2 data-id="heading-13">交流</h2>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div>  
</div>
            