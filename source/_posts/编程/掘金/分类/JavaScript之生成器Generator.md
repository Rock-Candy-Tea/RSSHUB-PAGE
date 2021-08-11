
---
title: 'JavaScript之生成器Generator'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:13:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>微信公众号：  <strong>[大前端驿站]</strong><br>
关注大前端驿站。问题或建议，欢迎公众号留言。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">定义</h4>
<p>Generator 函数是 ECMAScript 6 新增的一个极为灵活的结构，拥有在一个函数块内暂停和恢复代码执行的能力。使用生成器可以自定义迭代器和实现协程。</p>
<p>函数名称前面加一个星号（*）表示它是一个生成器</p>
<pre><code class="copyable">function* generatorFnA() &#123;&#125;
function * generatorFnB() &#123;&#125;
function *generatorFnC() &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>标识生成器函数的星号不受两侧空格的影响,上面三种方式都是合理的定义。</p>
<p>生成器对象一开始处于暂停执行（suspended）的状态。与迭代器相似，生成器对象也实现了 Iterator 接口，因此具有 next()方法。调用这个方法会让生成器开始或恢复执行</p>
<pre><code class="copyable">function* generatorFn() &#123;&#125; 
const g = generatorFn(); 
console.log(g); // generatorFn &#123;<suspended>&#125; 
console.log(g.next); // f next() &#123; [native code] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成器函数只会在初次调用 next()方法后开始执行</p>
<pre><code class="copyable">function* generatorFn() &#123; 
 console.log('foo'); 
&#125; 
// 初次调用生成器函数并不会打印日志
let generatorObject = generatorFn(); 
generatorObject.next(); // foo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成器对象实现了 Iterable 接口，它们默认的迭代器是自引用的</p>
<pre><code class="copyable">function* generatorFn() &#123;&#125;
const g = generatorFn(); 
console.log(g === g[Symbol.iterator]()) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">yield 表达式</h4>
<p>yield 关键字可以让生成器停止和开始执行，也是生成器最有用的地方。生成器函数在遇到 yield关键字之前会正常执行。遇到这个关键字后，执行会停止，函数作用域的状态会被保留。停止执行的生成器函数只能通过在生成器对象上调用 next()方法来恢复执行</p>
<pre><code class="copyable">function* generatorFn() &#123; 
 yield 'foo'; 
 yield 'bar'; 
 return 'baz'; 
&#125; 
let generatorObject = generatorFn(); 
console.log(generatorObject.next()); // &#123; done: false, value: 'foo' &#125; 
console.log(generatorObject.next()); // &#123; done: false, value: 'bar' &#125; 
console.log(generatorObject.next()); // &#123; done: true, value: 'baz' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 yield 关键字退出的生成器函数会处在 done: false 状态；通过 return 关键字退出的生成器函数会处于 done: true 状态。</p>
<blockquote>
<p>yield 关键字只能在生成器函数内部使用，用在其他地方会抛出错误。</p>
</blockquote>
<p>可以使用星号增强 yield 的行为，让它能够迭代一个可迭代对象，从而一次产出一个值</p>
<pre><code class="copyable">function* generatorFn() &#123; 
 yield* [1, 2, 3]; 
&#125; 
let g = generatorFn(); 
for (const x of g) &#123; 
 console.log(x); 
&#125; 
// 1 
// 2 
// 3
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">提前终止生成器</h4>
<p>return()和 throw()方法都可以用于强制生成器进入关闭状态</p>
<pre><code class="copyable">function* generatorFn() &#123;&#125; 
const g = generatorFn(); 
console.log(g); // generatorFn &#123;<suspended>&#125; 
console.log(g.next); // f next() &#123; [native code] &#125; 
console.log(g.return); // f return() &#123; [native code] &#125; 
console.log(g.throw); // f throw() &#123; [native code] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>return方式终止生成器</li>
</ul>
<pre><code class="copyable">function* generatorFn() &#123; 
 for (const x of [1, 2, 3]) &#123; 
 yield x; 
 &#125; 
&#125; 
const g = generatorFn(); 
console.log(g); // generatorFn &#123;<suspended>&#125; 
console.log(g.return(4)); // &#123; done: true, value: 4 &#125; 
console.log(g); // generatorFn &#123;<closed>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成器对象使用return（）方法进入关闭状态后，就无法恢复了，如上所示，生成器是closed状态后再次调用next（）方法后会显示为done:true状态</p>
<ul>
<li>throw方式终止生成器</li>
</ul>
<pre><code class="copyable">function* generatorFn() &#123; 
 for (const x of [1, 2, 3]) &#123; 
 yield x; 
 &#125; 
&#125; 
const g = generatorFn(); 
console.log(g); // generatorFn &#123;<suspended>&#125; 
try &#123; 
 g.throw('foo'); 
&#125; catch (e) &#123; 
 console.log(e); // foo 
&#125; 
console.log(g); // generatorFn &#123;<closed>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>throw()方法会在暂停的时候将一个提供的错误注入到生成器对象中。如果错误未被处理，生成器就会关闭.不过，假如生成器函数内部处理了这个错误，那么生成器就不会关闭，而且还可以恢复执行。错误处理会跳过对应的 yield，因此在这个例子中会跳过一个值</p>
<pre><code class="copyable">function* generatorFn() &#123; 
 for (const x of [1, 2, 3]) &#123; 
 try &#123; 
 yield x; 
 &#125; catch(e) &#123;&#125; 
 &#125; 
&#125;
const g = generatorFn(); 
console.log(g.next()); // &#123; done: false, value: 1&#125; 
g.throw('foo'); 
console.log(g.next()); // &#123; done: false, value: 3&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果生成器对象还没有开始执行，那么调用 throw()抛出的错误不会在函数内部被捕获，因为这相当于在函数块外部抛出了错误。</p>
</blockquote>
<br>
<br>
<br>
~~ 感谢观看
<br>
<br>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<div align="center">关注下方【大前端驿站】</div>
<div align="center">让我们一起学，一起进步</div>
<p><strong>【分享、点赞、在看】三连吧，让更多的人加入我们</strong></p></div>  
</div>
            