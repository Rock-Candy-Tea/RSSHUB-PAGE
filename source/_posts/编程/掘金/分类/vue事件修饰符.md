
---
title: 'vue事件修饰符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8758'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 03:18:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=8758'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在vue组件中经常会用到事件修饰符，今天用到修饰符发现又有些忘了，记录总结一下vue中的事件修饰符。</p>
<h2 data-id="heading-0">事件修饰符</h2>
<ul>
<li><a href="https://juejin.cn/post/6976203863346905124#self">.self</a></li>
<li><a href="https://juejin.cn/post/6976203863346905124#stop">.stop</a></li>
<li><a href="https://juejin.cn/post/6976203863346905124#capture">.capture</a></li>
<li><a href="https://juejin.cn/post/6976203863346905124#prevent">.prevent</a></li>
<li><a href="https://juejin.cn/post/6976203863346905124#once">.once</a></li>
<li><a href="https://juejin.cn/post/6976203863346905124#passive">.passive</a></li>
</ul>
<h2 data-id="heading-1"><a id="user-content-self" href="https://juejin.cn/post/undefined">.self</a></h2>
<p>含义： 只当在 event.target 是当前元素自身时触发处理函数，即事件不是从内部元素触发的<br>
用途： 点击弹窗蒙层关闭弹窗，可以在最外层蒙层的点击事件上添加.self修饰符，这样弹窗内部的点击就不会触发蒙版的点击事件了，内部点击事件上添加.stop同样也可以阻止蒙层的点击事件被触发。</p>
<h2 data-id="heading-2"><a id="user-content-stop" href="https://juejin.cn/post/undefined">.stop</a></h2>
<p>含义：阻止事件冒泡<br>
用途：阻止事件向外层冒泡，触发外层事件</p>
<h2 data-id="heading-3"><a id="user-content-capture" href="https://juejin.cn/post/undefined">.capture</a></h2>
<p>含义：添加事件监听器时使用事件捕获模式，即内部元素触发的事件先在此处理，然后才交由内部元素进行处理<br>
用途：内部元素触发的事件先在此处理</p>
<pre><code class="hljs language-js copyable" lang="js"><div v-on:click.capture=<span class="hljs-string">"clickEvent"</span>>...</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><a id="user-content-prevent" href="https://juejin.cn/post/undefined">.prevent</a></h2>
<p>含义：阻止默认事件<br>
用途：如form的submit事件默认提交会刷新页面，.prevent修饰符可以阻止该默认事件</p>
<pre><code class="hljs language-js copyable" lang="js"><form v-on:submit.prevent=<span class="hljs-string">"onSubmit"</span>></form>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用 v-on:click.prevent.self 会阻止所有的点击的默认行为，而 v-on:click.self.prevent 只会阻止对元素自身的点击的默认行为。</p>
</blockquote>
<h2 data-id="heading-5"><a id="user-content-once" href="https://juejin.cn/post/undefined">.once</a></h2>
<p>版本： 2.1.4 新增<br>
含义：该事件只执行一次<br>
用途：对于只执行一次的事件<br></p>
<blockquote>
<p>注意：不像其它修饰符只能对原生的 DOM 事件起作用的修饰符，.once 修饰符还能被用到自定义的组件事件上。</p>
</blockquote>
<h2 data-id="heading-6"><a id="user-content-passive" href="https://juejin.cn/post/undefined">.passive</a></h2>
<p>版本：2.3.0 新增<br>
含义：不会等监听器执行完后onScroll再去执行默认行为 (监听器执行是要耗时的，有些甚至耗时很明显，这样就会导致页面卡顿)<br>
用途：.passive 修饰符尤其能够提升移动端的性能。</p>
<pre><code class="hljs language-js copyable" lang="js"><!-- 滚动事件的默认行为 (即滚动行为) 将会立即触发 -->
<!-- 而不会等待 <span class="hljs-string">`onScroll`</span> 完成  -->
<!-- 这其中包含 <span class="hljs-string">`event.preventDefault()`</span> 的情况 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-on:scroll.passive</span>=<span class="hljs-string">"onScroll"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>不要把 .passive 和 .prevent 一起使用，因为 .prevent 将会被忽略，同时浏览器可能会向你展示一个警告。请记住，.passive 会告诉浏览器你不想阻止事件的默认行为。</p>
</blockquote>
<p>如果对passive还是不理解，另一篇文章会对passive详细讲解。</p></div>  
</div>
            