
---
title: '死磕系列之——Vue.js 核心原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3e0fecfffa34c1f9e8d34572f52e7e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 02:12:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3e0fecfffa34c1f9e8d34572f52e7e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<ul>
<li>前端三大框架对比</li>
</ul>

































<table><thead><tr><th>框架</th><th>发布年份</th><th>出自</th><th>star数</th><th>特性</th></tr></thead><tbody><tr><td>Angular</td><td>2010年</td><td>Google</td><td>73.7k</td><td>双向数据绑定</td></tr><tr><td>React</td><td>2013年</td><td>Facebook</td><td>169k</td><td>VirtualDOM、Redux</td></tr><tr><td>Vue</td><td>2014年</td><td>尤雨溪EvanYou</td><td>184k</td><td>更轻量、易于上手、中文文档友好</td></tr></tbody></table>
<ul>
<li>
<p>框架趋同/互相借鉴</p>
<ul>
<li>Vue借鉴knockout模板引擎、借鉴Angular双向数据绑定、借鉴React虚拟dom/redux/JSX</li>
<li>跨端开发（Ionic/ReactNative/Weex）</li>
<li>桌面开发（electron支持vue/react）</li>
<li>总之，你有我有全都有，大家好才是真的好</li>
</ul>
</li>
<li>
<p>类vue的开发模式（新赛道）：小程序、uniapp</p>
</li>
</ul>
<p>阅读本文后你将了解到：</p>
<ul>
<li>Vue是什么？解决了什么问题？</li>
<li>MVVM架构</li>
<li>三要素（响应式、模板编译、vdom/diff算法）</li>
<li>组件渲染/更新过程</li>
</ul>
<p>PS：本文内容主要针对Vue2，涉及少量vue3.0内容</p>
<h3 data-id="heading-1">一、Vue是什么？</h3>
<p><strong>vue是什么？</strong></p>
<blockquote>
<p>Vue (读音 /vjuː/，类似于 <strong>view</strong>) 是一套用于<strong>构建用户界面的渐进式框架</strong>。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与<strong>现代化的工具链以及各种支持类库</strong>结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。</p>
</blockquote>
<ul>
<li>轻量级渐进式框架（便于与第三方库或既有项目整合）</li>
<li>生态丰富（vue-cli、vue-router、vuex、社区UI组件库...）</li>
<li>易于上手（入门简单、中文文档友好）</li>
</ul>
<p><strong>vue解决了什么问题？</strong></p>
<ul>
<li><strong>HTML</strong>：从0到1</li>
<li><strong>CSS</strong>：提供装饰</li>
<li><strong>JavaScript(DOM)</strong>：支持页面动态化（例如倒计时）</li>
<li><strong>jQuery</strong>：解决浏览器兼容问题、优雅API（解放前端，造轮子）</li>
<li><strong>Vue</strong>：<strong>数据驱动视图</strong>，让开发者从DOM操作中解放（如倒计时，自加器）</li>
</ul>
<p><strong>疑问：数据驱动视图是怎么做到的？（数据变化 -> 视图更新）</strong></p>
<h4 data-id="heading-2">1、如何理解MVVM</h4>
<blockquote>
<p>MVVM是一种软件架构模式，MVVM是MVP的变体，MVP模式和MVVM模式都是MVC模式的变体。<a href="http://www.ruanyifeng.com/blog/2015/02/mvcmvp_mvvm.html" target="_blank" rel="nofollow noopener noreferrer">MVC，MVP 和 MVVM 的图示</a></p>
</blockquote>
<blockquote>
<p>软件构架对代码进行解耦分层，各层互不影响，有效降低了开发复杂度。我们可以通过调整MVC三者之前的通信模式，来达到一定的架构目的。</p>
</blockquote>
<p>MVVM对视图更新模式的影响</p>
<ul>
<li>静态渲染：更新需要进行DOM操作，如ASP/JSP/PHP，适合业务简单的场景</li>
<li>数据驱动视图：通过数据即可更新视图，如Vue/React/Angular，适合业务复杂的场景</li>
</ul>
<p>MVVM包含3部分：</p>
<ul>
<li><strong>View</strong>：用户看到屏幕的结构、布局和外观，也称UI</li>
<li><strong>ViewModel</strong>：是一个绑定器，能和 <code>View</code> 和 <code>Model</code> 层进行通信</li>
<li><strong>Model</strong>：是数据和逻辑</li>
</ul>
<h4 data-id="heading-3">2、MVVM在Vue中的体现</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3e0fecfffa34c1f9e8d34572f52e7e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"reverse"</span>></span>reverse<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
</template
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">"Hello Vue123!!"</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">reverse</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.message = <span class="hljs-built_in">this</span>.message.split(<span class="hljs-string">""</span>).reverse().join(<span class="hljs-string">""</span>);
      &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>View: template模板</li>
<li>Model: data数据</li>
<li>ViewModel: Vue实例</li>
</ul>
<p>PS：Vue没有严格遵循 MVVM 模式：严格的MVVM要求View不能和Model直接通信，而Vue在组件中提供了$refs这个属性，让Model可以直接操作View，违反了这一规定。</p>
<p><strong>疑问：vue是如何实现MVVM的？</strong></p>
<h4 data-id="heading-4">3、Vue三要素</h4>
<ul>
<li>响应式：vue如何监听到 data 的每个属性变化？</li>
<li>模板引擎：vue的模板如何被解析？</li>
<li>渲染：vue的模板如何被渲染成html？以及渲染过程</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa6b219179c14b13abd1d436703e2099~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">二、Vue三要素-响应式</h3>
<blockquote>
<p>响应式：组件 data 的数据一旦变化，立刻触发视图的更新。</p>
</blockquote>
<p>响应式如何实现？</p>
<h4 data-id="heading-6">Object.defineProperty（IE9+）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;&#125;;
<span class="hljs-keyword">let</span> value = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">'a'</span>, &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger get'</span>);
        <span class="hljs-comment">// 收集依赖 todo...</span>
        <span class="hljs-keyword">return</span> value;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger set'</span>);
        <span class="hljs-keyword">if</span> (val !== value) &#123;
            value = val;
            <span class="hljs-comment">// 数据变更，需要重新渲染 todo...</span>
        &#125;
        
    &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(obj.a);
obj.a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点</p>
<ul>
<li>深度监听需要递归到底，一次性计算量大</li>
<li>无法监听新增属性/删除属性（Vue.$set）</li>
<li>无法原生监听数组，需要特殊处理</li>
</ul>
<h4 data-id="heading-7">proxy（Vue3.0，IE11+）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;&#125;
<span class="hljs-keyword">let</span> reactiveObj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, prop</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger get'</span>);
        <span class="hljs-comment">// 收集依赖 todo...</span>
        <span class="hljs-keyword">return</span> obj[prop];
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, prop, value</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger set'</span>);
        obj[prop] = value;
        <span class="hljs-keyword">if</span> (obj[prop] !== value) &#123;
            <span class="hljs-comment">// 数据变更，需要重新渲染 todo...</span>
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<ul>
<li>有兼容性的问题，caniuse 95%</li>
<li>它会修改JavaScript的一些底层代码的执行方式，所以它是无法被完全polyfill的</li>
</ul>
<p>响应式带来的问题：</p>
<ul>
<li>jQuery可以自行控制DOM操作的时机，手动调整，而响应式的DOM操作则在内部进行；</li>
<li>DOM 操作非常耗费性能</li>
</ul>
<p><strong>疑问：如何有效控制DOM操作？</strong></p>
<h3 data-id="heading-8">三、Vue三要素-渲染：虚拟DOM（Virtual DOM）</h3>
<blockquote>
<p>Vue是数据驱动视图，如何有效控制DOM操作？</p>
</blockquote>
<ul>
<li>解决方案：<code>vdom</code>
<ul>
<li>JS执行速度快</li>
<li>用JS模拟DOM结构，计算出最小的变更，操作DOM</li>
</ul>
</li>
<li><code>vdom</code> 是优化方案，不是响应式必须
<ul>
<li><code>vdom</code> 是实现 <code>vue</code> 和 <code>react</code> 的重要基石</li>
<li><code>diff算法</code> 是 <code>vdom</code> 中最核心、最关键的部分</li>
</ul>
</li>
<li>用JS模拟DOM结构：<code>vnode</code></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>vdom<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"font-size: 20px;"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>a<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">tag</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">classname</span>: <span class="hljs-string">'container'</span>,
        <span class="hljs-attr">id</span>: <span class="hljs-string">'div1'</span>
    &#125;,
    <span class="hljs-attr">children</span>: [
        &#123;
            <span class="hljs-attr">tag</span>: <span class="hljs-string">'p'</span>,
            <span class="hljs-attr">children</span>: <span class="hljs-string">'vdom'</span>
        &#125;,
        &#123;
            <span class="hljs-attr">tag</span>: <span class="hljs-string">'ul'</span>,
            <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">style</span>: <span class="hljs-string">'font-size: 20px;'</span> &#125;,
            <span class="hljs-attr">children</span>: [
                &#123;
                    <span class="hljs-attr">tag</span>: <span class="hljs-string">'li'</span>,
                    <span class="hljs-attr">children</span>: <span class="hljs-string">'a'</span>
                &#125;
            ]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>vdom</code> 小结：数据驱动视图的模式下，有效控制DOM操作
<ul>
<li><code>vnode</code>：用JS模拟DOM结构</li>
<li><code>diff算法</code>：新旧vnode对比，得出最小更新范围，最后更新DOM</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">四、diff算法-vdom核心部分</h3>
<blockquote>
<p>diff 算法是一种通过同层的树节点进行比较的高效算法，避免了对树进行逐层搜索遍历，所以时间复杂度只有 O(n)</p>
</blockquote>
<h4 data-id="heading-10">概述：</h4>
<ul>
<li>diff即对比，是一个广泛的概念（非独创），如linux diff命令，git diff等</li>
<li>两个js对象也可以做diff</li>
<li>两棵树做diff，如这里的vdom diff</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/286a4362483c4cafb3fb8615cefe94bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">树diff的时间复杂度O(n^3)</h4>
<ul>
<li>1、遍历tree1，2、遍历tree2，3、排序</li>
<li>1000个节点，要计算1亿次，算法不可用</li>
</ul>
<h4 data-id="heading-12">优化时间复杂度到O(n)</h4>
<ul>
<li>只比较同一层级，不跨级比较</li>
<li>tag不相同，则直接删掉重建，不再深度比较</li>
<li>tag和key，两者都相同，则认为是相同节点，更新dom，并继续比较节点的子元素</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39a203ea582649f5aba9bf27f86aada7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68ef124893964d349a15fa4f32759b2d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">diff算法流程</h4>
<p>1、首次渲染，取vnode进行渲染即可</p>
<p>2、数据更新后，将vnode和oldVnode进行对比</p>
<ul>
<li>从根节点开始遍历，判断当前的旧节点和新节点是否同一节点（sel和key相同）</li>
<li>若不是同一节点，则删掉重建；</li>
<li>若是同一节点，则更新当前节点dom，继续处理子元素children</li>
</ul>
<p>3、<strong>子元素children的对比算法</strong>（尽可能多地复用真实DOM,尽可能少的添加删除真实DOM）
思路：添加4个指针，分别指向新旧children的开始和结束比较的过程中，循环从两边向中间收拢；</p>
<ul>
<li>第一步：分别进行开始开始、结束结束、开始结束、结束开始对比，若匹配成功，则指针向中间收拢；</li>
<li>第二步：若第一步未匹配，则在旧children中遍历查找是否匹配新children的开始节点，若匹配成功，则移动旧节点到对应位置；</li>
<li>第三步：循环结束后，根据新老节点的数目不同做相应的添加或者删除节点操作</li>
</ul>
<p>各场景图示（这里看动画 👉  <a href="https://www.bilibili.com/video/BV1b5411V7i3?from=search&seid=4125072074822008044" target="_blank" rel="nofollow noopener noreferrer">diff算法图解动画</a>）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0d8dca6afe24cd795af2edc2be7e049~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5295957102da4ba2b13eb6c8c65b4f73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ee3dec92df84644982cfb237166e12c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e62d8912026f4bbf9f1975de26b8de73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad12f271b8484572b14e32048fbba20f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>删除节点
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f94f32ebd3040c9bec27350e554f8cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增节点
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bdb95ad733f414f9542a5ebb4ec9175~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>未设置key
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/027885ad98f7446d8eefa107c481c6a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置key
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50d9e7701ad14f779de617fb3368fc3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">五、Vue三要素-模板编译</h3>
<ul>
<li>概览
<ul>
<li>前置知识：JS的with语法
<ul>
<li>改变&#123;&#125;内自由变量的查找规则，当做obj属性来查找</li>
<li>如果找不到匹配的obj属性，就会报错</li>
<li>with要慎用，它打破了作用域规则，易读性变差</li>
</ul>
</li>
<li>vue模板(不是html，有指令、插值、JS表达式)到底是什么？</li>
<li>vue如何处理模板？组件渲染和更新过程？</li>
</ul>
</li>
<li>步骤：
<ol>
<li><strong>vue-template-complier将模板</strong></li></ol></li></ul></div>  
</div>
            