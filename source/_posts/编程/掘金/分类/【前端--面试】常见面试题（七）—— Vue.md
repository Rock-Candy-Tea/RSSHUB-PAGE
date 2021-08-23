
---
title: '【前端--面试】常见面试题（七）—— Vue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9860'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 01:44:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=9860'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>又迎来了新的一周，八月就要快过去了，金九银十的季节仿佛近在咫尺，不知道要跳槽的同学准备的如何了，今天就整理Vue的知识点吧~</p>
</blockquote>
<h3 data-id="heading-0">说一下Vue的双向绑定数据的原理</h3>
<p>采用数据劫持结合发布者-订阅者模式的方式，通过 <code>Object.defineProperty()</code> 来劫持各个属性的 <code>setter</code>，<code>getter</code>，在数据变动时发布消息给订阅者，触发相应监听回调。</p>
<h3 data-id="heading-1">Vue 如何去除url中的 <code>#</code></h3>
<p><code>vue-router</code> 默认使用 <code>hash</code> 模式，所以在路由加载的时候，项目中的 <code>url</code> 会自带 <code>#</code>。如果不想使用 <code>#</code>， 可以使用 <code>vue-router</code> 的另一种模式 <code>history</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">routes</span>: [ ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">v-if 和 v-show 区别</h3>
<p>使用了 <code>v-if</code> 的时候，如果值为 <code>false</code> ，那么页面将不会有这个 <code>html</code> 标签生成。<code>v-show</code> 则是不管值为 <code>true</code> 还是 <code>false</code> ，<code>html</code> 元素都会存在，只是 <code>CSS</code> 中的 <code>display</code> 显示或隐藏。</p>
<h3 data-id="heading-3"><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">route和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">和</span></span></span></span></span>router的区别</h3>
<p><code>$router</code> 为 <code>VueRouter</code> 实例，想要导航到不同 <code>URL</code>，则使用 <code>$router.push</code> 方法<code>$route</code> 为当前 <code>router</code> 跳转对象里面可以获取 <code>name</code> 、 <code>path</code> 、 <code>query</code> 、 <code>params</code> 等。</p>
<h3 data-id="heading-4">NextTick的作用</h3>
<p><code>$nextTick</code> 是在下次 <code>DOM</code> 更新循环结束之后执行延迟回调，在修改数据之后使用 <code>$nextTick</code>，则可以在回调中获取更新后的 <code>DOM</code>。</p>
<h3 data-id="heading-5">Vue 组件 data 为什么必须是函数</h3>
<p>因为js本身的特性带来的，如果 <code>data</code> 是一个对象，那么由于对象本身属于引用类型，当我们修改其中的一个属性时，会影响到所有Vue实例的数据。如果将 <code>data</code> 作为一个函数返回一个对象，那么每一个实例的 <code>data</code> 属性都是独立的，就不会相互影响了。</p>
<h3 data-id="heading-6">Vue 中怎么自定义指令</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 注册一个全局自定义指令 `v-focus`</span>
Vue.directive(<span class="hljs-string">'focus'</span>, &#123;
  <span class="hljs-comment">// 当被绑定的元素插入到 DOM 中时……</span>
  <span class="hljs-attr">inserted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-comment">// 聚焦元素</span>
    el.focus()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在局部注册：</p>
<pre><code class="hljs language-js copyable" lang="js">directives: &#123;
  <span class="hljs-attr">focus</span>: &#123;
    <span class="hljs-comment">// 指令的定义</span>
    <span class="hljs-attr">inserted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
      el.focus()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">keep-alive 的作用</h3>
<p><code>keep-alive</code> 是 <code>Vue</code> 内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染，还可以使用API提供的props，实现组件的动态缓存</p>
<pre><code class="hljs language-Vue copyable" lang="Vue"><keep-alive>
  <component>
    <!-- 该组件将被缓存！ -->
  </component>
</keep-alive>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Vue 的核心是什么</h3>
<p>数据驱动 组件系统</p>
<h3 data-id="heading-9"> vue 等单页面应用的优缺点</h3>
<p><strong>优点：</strong></p>
<ul>
<li>良好的交互体验</li>
<li>良好的前后端工作分离模式</li>
<li>减轻服务器压力</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>SEO难度较高</li>
<li>前进、后退管理</li>
<li>初次加载耗时多</li>
</ul></div>  
</div>
            