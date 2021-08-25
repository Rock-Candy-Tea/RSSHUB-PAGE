
---
title: 'DIff算法看不懂就一起来砍我(带图)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03196dcfcce243b0bf69780250b39086~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 23:29:49 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03196dcfcce243b0bf69780250b39086~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>面试官:"你了解<code>虚拟DOM(Virtual DOM)</code>跟<code>Diff算法</code>吗,请描述一下它们";</p>
<p>我:"额,...鹅,那个",完了😰,突然智商不在线,没组织好语言没答好或者压根就答不出来;</p>
<p>所以这次我总结一下相关的知识点,让你可以有一个清晰的认知之余也会让你在今后遇到这种情况可以<strong>坦然自若,应付自如,游刃有余</strong>:</p>
<hr>
<h2 data-id="heading-1">相关知识点:</h2>
<ul>
<li>虚拟DOM(Virtual DOM):
<ul>
<li>
<p><strong>什么是虚拟dom</strong></p>
</li>
<li>
<p><strong>为什么要使用虚拟dom</strong></p>
</li>
<li>
<p>虚拟DOM库</p>
</li>
</ul>
</li>
<li>DIFF算法:
<ul>
<li>snabbDom源码
<ul>
<li>init函数</li>
<li>h函数</li>
<li><strong>patch函数</strong></li>
<li><strong>patchVnode函数</strong></li>
<li><strong>updateChildren函数</strong></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr>
<h2 data-id="heading-2">虚拟DOM(Virtual DOM)</h2>
<h3 data-id="heading-3">什么是虚拟DOM</h3>
<p>一句话总结虚拟DOM就是一个用来描述真实DOM的<strong>javaScript对象</strong>,这样说可能不够形象,那我们来举个🌰:分别用代码来描述<code>真实DOM</code>以及<code>虚拟DOM</code></p>
<p><code>真实DOM</code>:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>a<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>b<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>c<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>对应的虚拟DOM</code>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">let</span> vnode = h(<span class="hljs-string">'ul.list'</span>, [
  h(<span class="hljs-string">'li'</span>,<span class="hljs-string">'a'</span>),
  h(<span class="hljs-string">'li'</span>,<span class="hljs-string">'b'</span>),
  h(<span class="hljs-string">'li'</span>,<span class="hljs-string">'c'</span>),
])

<span class="hljs-built_in">console</span>.log(vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">控制台打印出来的<strong>Vnode</strong>:</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03196dcfcce243b0bf69780250b39086~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">h函数生成的虚拟DOM这个JS对象(Vnode)的源码:</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> VNodeData &#123;
    props?: Props
    attrs?: Attrs
    <span class="hljs-class"><span class="hljs-keyword">class</span>?: <span class="hljs-title">Classes</span>
    <span class="hljs-title">style</span>?: <span class="hljs-title">VNodeStyle</span>
    <span class="hljs-title">dataset</span>?: <span class="hljs-title">Dataset</span>
    <span class="hljs-title">on</span>?: <span class="hljs-title">On</span>
    <span class="hljs-title">hero</span>?: <span class="hljs-title">Hero</span>
    <span class="hljs-title">attachData</span>?: <span class="hljs-title">AttachData</span>
    <span class="hljs-title">hook</span>?: <span class="hljs-title">Hooks</span>
    <span class="hljs-title">key</span>?: <span class="hljs-title">Key</span>
    <span class="hljs-title">ns</span>?: <span class="hljs-title">string</span> // <span class="hljs-title">for</span> <span class="hljs-title">SVGs</span>
    <span class="hljs-title">fn</span>?: () </span>=> VNode <span class="hljs-comment">// for thunks</span>
    args?: <span class="hljs-built_in">any</span>[] <span class="hljs-comment">// for thunks</span>
    [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> <span class="hljs-comment">// for any other 3rd party module</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> Key = <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>

<span class="hljs-keyword">const</span> <span class="hljs-keyword">interface</span> VNode = &#123;
    <span class="hljs-attr">sel</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 选择器</span>
    <span class="hljs-attr">data</span>: VNodeData | <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// VNodeData上面定义的VNodeData</span>
    <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span><VNode | <span class="hljs-built_in">string</span>> | <span class="hljs-literal">undefined</span>, <span class="hljs-comment">//子节点,与text互斥</span>
    <span class="hljs-attr">text</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 标签中间的文本内容</span>
    <span class="hljs-attr">elm</span>: Node | <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 转换而成的真实DOM</span>
    <span class="hljs-attr">key</span>: Key | <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 字符串或者数字</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">补充:</h5>
<p>上面的h函数大家可能有点熟悉的感觉但是一时间也没想起来,没关系我来帮大伙回忆;
<code>开发中常见的现实场景,render函数渲染</code>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 案例1 vue项目中的main.js的创建vue实例</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">"#app"</span>);

<span class="hljs-comment">//案例2 列表中使用render渲染</span>
columns: [
    &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">"操作"</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">"action"</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-number">150</span>,
        <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h, params</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, [
                h(<span class="hljs-string">'Button'</span>, &#123;
                    <span class="hljs-attr">props</span>: &#123;
                        <span class="hljs-attr">size</span>: <span class="hljs-string">'small'</span>
                    &#125;,
                    <span class="hljs-attr">style</span>: &#123;
                        <span class="hljs-attr">marginRight</span>: <span class="hljs-string">'5px'</span>,
                        <span class="hljs-attr">marginBottom</span>: <span class="hljs-string">'5px'</span>,
                    &#125;,
                    <span class="hljs-attr">on</span>: &#123;
                        <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> &#123;
                            <span class="hljs-built_in">this</span>.toEdit(params.row.uuid);
                        &#125;
                    &#125;
                &#125;, <span class="hljs-string">'编辑'</span>)
            ]);
        &#125;
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-7">为什么要使用虚拟DOM</h3>
<ul>
<li>MVVM框架解决视图和状态同步问题</li>
<li>模板引擎可以简化视图操作,没办法跟踪状态</li>
<li>虚拟DOM跟踪状态变化</li>
<li>参考github上<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMatt-Esch%2Fvirtual-dom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Matt-Esch/virtual-dom" ref="nofollow noopener noreferrer">virtual-dom</a>的动机描述
<ul>
<li>虚拟DOM可以维护程序的状态,跟踪上一次的状态</li>
<li>通过比较前后两次状态差异更新真实DOM</li>
</ul>
</li>
<li>跨平台使用
<ul>
<li>浏览器平台渲染DOM</li>
<li>服务端渲染SSR(Nuxt.js/Next.js),前端是vue向,后者是react向</li>
<li>原生应用(Weex/React Native)</li>
<li>小程序(mpvue/uni-app)等</li>
</ul>
</li>
<li>真实DOM的属性很多，创建DOM节点开销很大</li>
<li>虚拟DOM只是普通JavaScript对象，描述属性并不需要很多，创建开销很小</li>
<li><strong>复杂视图情况下提升渲染性能</strong>(操作dom性能消耗大,减少操作dom的范围可以提升性能)</li>
</ul>
<p><strong>灵魂发问</strong>:使用了虚拟DOM就一定会比直接渲染真实DOM快吗?答案当然是<code>否定</code>的,且听我说:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bd4d26c0f154fc1adff6a6ed8346909~tplv-k3u1fbpfcp-watermark.image" alt="2c3559e204c5aae6a1c6bfdc8557efcd.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>举例</strong>:当一个节点变更时DOMA->DOMB</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea61542e0dfb449e9cf506f0901aafe1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上述情况:
<code>示例1</code>是创建一个<code>DOMB</code>然后替换掉<code>DOMA</code>;
<code>示例2</code>去<code>创建虚拟DOM+DIFF算法</code>比对发现<code>DOMB</code>跟<code>DOMA</code>不是相同的节点,最后还是创建一个<code>DOMB</code>然后替换掉<code>DOMA</code>;
可以明显看出1是更快的,同样的结果,2还要去创建虚拟DOM+DIFF算啊对比
所以说使用虚拟DOM比直接操作真实DOM就一定要快这个说法是<code>错误的,不严谨的</code></p>
<p><strong>举例</strong>:当DOM树里面的某个子节点的内容变更时:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d4fdab03fc4cc583c3ca60a1f4e20e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当一些复杂的节点,比如说一个父节点里面有多个子节点,当只是一个子节点的内容发生了改变,那么我们没有必要像<code>示例1</code>重新去渲染这个<code>DOM树</code>,这个时候<code>虚拟DOM+DIFF算法</code>就能够得到很好的体现,我们通过<code>示例2</code>使用<code>虚拟DOM+Diff算法</code>去找出改变了的子节点更新它的内容就可以了</p>
<p>总结:<strong>复杂视图情况下提升渲染性能</strong>,因为<code>虚拟DOM+Diff算法</code>可以精准找到DOM树变更的地方,减少DOM的操作(重排重绘)</p>
<hr>
<h3 data-id="heading-8">虚拟dom库</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom" ref="nofollow noopener noreferrer">Snabbdom</a>
<ul>
<li>Vue.js2.x内部使用的虚拟DOM就是改造的Snabbdom</li>
<li>大约200SLOC(single line of code)</li>
<li>通过模块可扩展</li>
<li>源码使用TypeScript开发</li>
<li>最快的Virtual DOM之一</li>
</ul>
</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMatt-Esch%2Fvirtual-dom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Matt-Esch/virtual-dom" ref="nofollow noopener noreferrer">virtual-dom</a></li>
</ul>
<hr>
<h2 data-id="heading-9">Diff算法</h2>
<p>在看完上述的文章之后相信大家已经对Diff算法有一个初步的概念,没错,Diff算法其实就是找出两者之间的差异;</p>
<blockquote>
<p>diff 算法首先要明确一个概念就是 Diff 的对象是虚拟DOM（virtual dom），更新真实 DOM 是 Diff 算法的结果。</p>
</blockquote>
<p>下面我将会手撕<code>snabbdom</code>源码核心部分为大家打开<code>Diff</code>的心,给点耐心,别关网页,我知道你们都是这样:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98b1ea6928a942afb2e9d5b056ed320e~tplv-k3u1fbpfcp-watermark.image" alt="src=http___img.wxcha.com_file_201905_17_f5a4d33d48.jpg&refer=http___img.wxcha.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-10">snabbdom的核心</h2>
<ul>
<li><code>init()</code>设置模块.创建<code>patch()</code>函数</li>
<li>使用<code>h()</code>函数创建JavaScript对象<code>(Vnode)</code>描述<code>真实DOM</code></li>
<li><code>patch()</code>比较<code>新旧两个Vnode</code></li>
<li>把变化的内容更新到<code>真实DOM树</code></li>
</ul>
<h3 data-id="heading-11">init函数</h3>
<p>init函数时设置模块,然后创建patch()函数,我们先通过场景案例来有一个直观的体现:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;init&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'snabbdom/build/package/init.js'</span>
<span class="hljs-keyword">import</span> &#123;h&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'snabbdom/build/package/h.js'</span>

<span class="hljs-comment">// 1.导入模块</span>
<span class="hljs-keyword">import</span> &#123;styleModule&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"snabbdom/build/package/modules/style"</span>;
<span class="hljs-keyword">import</span> &#123;eventListenersModule&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"snabbdom/build/package/modules/eventListeners"</span>;

<span class="hljs-comment">// 2.注册模块</span>
<span class="hljs-keyword">const</span> patch = init([
  styleModule,
  eventListenersModule
])

<span class="hljs-comment">// 3.使用h()函数的第二个参数传入模块中使用的数据(对象)</span>
<span class="hljs-keyword">let</span> vnode = h(<span class="hljs-string">'div'</span>, [
  h(<span class="hljs-string">'h1'</span>, &#123;<span class="hljs-attr">style</span>: &#123;<span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'red'</span>&#125;&#125;, <span class="hljs-string">'Hello world'</span>),
  h(<span class="hljs-string">'p'</span>, &#123;<span class="hljs-attr">on</span>: &#123;<span class="hljs-attr">click</span>: eventHandler&#125;&#125;, <span class="hljs-string">'Hello P'</span>)
])

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eventHandler</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-string">'疼,别摸我'</span>)
&#125;

<span class="hljs-keyword">const</span> app = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>)

patch(app,vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当init使用了导入的模块就能够在h函数中用这些模块提供的api去创建<code>虚拟DOM(Vnode)对象</code>;在上文中就使用了<code>样式模块</code>以及<code>事件模块</code>让创建的这个虚拟DOM具备样式属性以及事件属性,最终通过<code>patch函数</code>对比<code>两个虚拟dom</code>(会先把app转换成虚拟dom),更新视图;</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d327c27f5214fbda311f4d8ca09ad9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再简单看看init的源码部分:</p>
<pre><code class="hljs language-javaScript copyable" lang="javaScript"><span class="hljs-comment">// src/package/init.ts</span>
<span class="hljs-comment">/* 第一参数就是各个模块
   第二参数就是DOMAPI,可以把DOM转换成别的平台的API,
也就是说支持跨平台使用,当不传的时候默认是htmlDOMApi,见下文
   init是一个高阶函数,一个函数返回另外一个函数,可以缓存modules,与domApi两个参数,
那么以后直接只传oldValue跟newValue(vnode)就可以了*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span> (<span class="hljs-params">modules: <span class="hljs-built_in">Array</span><Partial<Module>>, domApi?: DOMAPI</span>) </span>&#123;

...

<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span> (<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-12">h函数</h3>
<p>些地方也会用<code>createElement</code>来命名,它们是一样的东西,都是创建<code>虚拟DOM</code>的,在上述文章中相信大伙已经对h函数有一个初步的了解并且已经联想了使用场景,就不作场景案例介绍了,直接上源码部分:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// h函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: string</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: string, data: VNodeData | <span class="hljs-literal">null</span></span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: string, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: string, data: VNodeData | <span class="hljs-literal">null</span>, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: any, b?: any, c?: any</span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-title">var</span> <span class="hljs-title">data</span>: <span class="hljs-title">VNodeData</span> = </span>&#123;&#125;
  <span class="hljs-title">var</span> <span class="hljs-title">children</span>: <span class="hljs-title">any</span>
  <span class="hljs-title">var</span> <span class="hljs-title">text</span>: <span class="hljs-title">any</span>
  <span class="hljs-title">var</span> <span class="hljs-title">i</span>: <span class="hljs-title">number</span>
    ...
  <span class="hljs-title">return</span> <span class="hljs-title">vnode</span>(<span class="hljs-params">sel, data, children, text, <span class="hljs-literal">undefined</span></span>) //最终返回一个<span class="hljs-title">vnode</span>函数
&#125;</span>;
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vnode函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span> (<span class="hljs-params">sel: string | <span class="hljs-literal">undefined</span>,
  data: any | <span class="hljs-literal">undefined</span>,
  children: <span class="hljs-built_in">Array</span><VNode | string> | <span class="hljs-literal">undefined</span>,
  text: string | <span class="hljs-literal">undefined</span>,
  elm: Element | Text | <span class="hljs-literal">undefined</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key
  <span class="hljs-keyword">return</span> &#123; sel, data, children, text, elm, key &#125; <span class="hljs-comment">//最终生成Vnode对象</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结</strong>:<code>h函数</code>先生成一个<code>vnode</code>函数,然后<code>vnode</code>函数再生成一个<code>Vnode</code>对象(虚拟DOM对象)</p>
<h4 data-id="heading-13">补充:</h4>
<p>在h函数源码部分涉及一个<code>函数重载</code>的概念,简单说明一下:</p>
<ul>
<li>参数个数或参数类型不同的函数()</li>
<li>JavaScript中没有重载的概念</li>
<li>TypeScript中有重载,不过重载的实现还是通过代码调整参数</li>
</ul>
<blockquote>
<p>重载这个概念个参数相关,和返回值无关</p>
</blockquote>
<ul>
<li>实例1(函数重载-参数个数)</li>
</ul>
<pre><code class="hljs language-typeScript copyable" lang="typeScript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a:<span class="hljs-built_in">number</span>,b:<span class="hljs-built_in">number</span></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(a+b)

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a:<span class="hljs-built_in">number</span>,b:<span class="hljs-built_in">number</span>,c:<span class="hljs-built_in">number</span></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(a+b+c)

&#125;

add(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)

add(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实例2(函数重载-参数类型)</li>
</ul>
<pre><code class="hljs language-typeScript copyable" lang="typeScript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a:<span class="hljs-built_in">number</span>,b:<span class="hljs-built_in">number</span></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(a+b)

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a:<span class="hljs-built_in">number</span>,b:<span class="hljs-built_in">string</span></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(a+b)

&#125;

add(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)

add(<span class="hljs-number">1</span>,<span class="hljs-string">'2'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-14">patch函数(核心)</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a4b29be73d343dea8d37d902e642eec~tplv-k3u1fbpfcp-watermark.image" alt="src=http___shp.qpic.cn_qqvideo_ori_0_e3012t7v643_496_280_0&refer=http___shp.qpic.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要是看完前面的铺垫,看到这里你可能走神了,<code>醒醒啊,这是核心啊,上高地了兄弟</code>;</p>
<ul>
<li>pactch(oldVnode,newVnode)</li>
<li>把新节点中变化的内容渲染到真实DOM,最后返回新节点作为下一次处理的旧节点(核心)</li>
<li>对比新旧<code>VNode</code>是否相同节点(节点的key和sel相同)</li>
<li>如果不是相同节点,删除之前的内容,重新渲染</li>
<li>如果是相同节点,再判断新的<code>VNode</code>是否有<code>text</code>,如果有并且和<code>oldVnode</code>的<code>text</code>不同直接更新文本内容<code>(patchVnode)</code></li>
<li>如果新的VNode有children,判断子节点是否有变化<code>(updateChildren,最麻烦,最难实现)</code></li>
</ul>
<p>源码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;    
    <span class="hljs-keyword">let</span> i: number, <span class="hljs-attr">elm</span>: Node, <span class="hljs-attr">parent</span>: Node
    <span class="hljs-keyword">const</span> insertedVnodeQueue: VNodeQueue = []
    <span class="hljs-comment">// cbs.pre就是所有模块的pre钩子函数集合</span>
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.pre.length; ++i) cbs.pre[i]()
    <span class="hljs-comment">// isVnode函数时判断oldVnode是否是一个虚拟DOM对象</span>
    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
        <span class="hljs-comment">// 若不是即把Element转换成一个虚拟DOM对象</span>
        oldVnode = emptyNodeAt(oldVnode)
    &#125;
    <span class="hljs-comment">// sameVnode函数用于判断两个虚拟DOM是否是相同的,源码见补充1;</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
        <span class="hljs-comment">// 相同则运行patchVnode对比两个节点,关于patchVnode后面会重点说明(核心)</span>
        patchVnode(oldVnode, vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
        elm = oldVnode.elm! <span class="hljs-comment">// !是ts的一种写法代码oldVnode.elm肯定有值</span>
        <span class="hljs-comment">// parentNode就是获取父元素</span>
        parent = api.parentNode(elm) <span class="hljs-keyword">as</span> Node

        <span class="hljs-comment">// createElm是用于创建一个dom元素插入到vnode中(新的虚拟DOM)</span>
        createElm(vnode, insertedVnodeQueue)

        <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// 把dom元素插入到父元素中,并且把旧的dom删除</span>
            api.insertBefore(parent, vnode.elm!, api.nextSibling(elm))<span class="hljs-comment">// 把新创建的元素放在旧的dom后面</span>
            removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
        &#125;
    &#125;

    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < insertedVnodeQueue.length; ++i) &#123;
        insertedVnodeQueue[i].data!.hook!.insert!(insertedVnodeQueue[i])
    &#125;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.post.length; ++i) cbs.post[i]()
    <span class="hljs-keyword">return</span> vnode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">补充1: sameVnode函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1: VNode, vnode2: VNode</span>): <span class="hljs-title">boolean</span> </span>&#123; 通过key和sel选择器判断是否是相同节点
    <span class="hljs-keyword">return</span> vnode1.key === vnode2.key && vnode1.sel === vnode2.sel
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-16">patchVnode</h3>
<ul>
<li>第一阶段触发<code>prepatch</code>函数以及<code>update</code>函数(都会触发prepatch函数,两者不完全相同才会触发update函数)</li>
<li>第二阶段,真正对比新旧<code>vnode</code>差异的地方</li>
<li>第三阶段,触发<code>postpatch</code>函数更新节点</li>
</ul>
<p>源码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode: VNode, vnode: VNode, insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">const</span> hook = vnode.data?.hook
    hook?.prepatch?.(oldVnode, vnode)
    <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm!
    <span class="hljs-keyword">const</span> oldCh = oldVnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-keyword">const</span> ch = vnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (vnode.data !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
        vnode.data.hook?.update?.(oldVnode, vnode)
    &#125;
    <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123; <span class="hljs-comment">// 新节点的text属性是undefined</span>
        <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123; <span class="hljs-comment">// 当新旧节点都存在子节点</span>
            <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue) <span class="hljs-comment">//并且他们的子节点不相同执行updateChildren函数,后续会重点说明(核心)</span>
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123; <span class="hljs-comment">// 只有新节点有子节点</span>
            <span class="hljs-comment">// 当旧节点有text属性就会把''赋予给真实dom的text属性</span>
            <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) api.setTextContent(elm, <span class="hljs-string">''</span>) 
            <span class="hljs-comment">// 并且把新节点的所有子节点插入到真实dom中</span>
            addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123; <span class="hljs-comment">// 清除真实dom的所有子节点</span>
            removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123; <span class="hljs-comment">// 把''赋予给真实dom的text属性</span>
            api.setTextContent(elm, <span class="hljs-string">''</span>)
        &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123; <span class="hljs-comment">//若旧节点的text与新节点的text不相同</span>
        <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123; <span class="hljs-comment">// 若旧节点有子节点,就把所有的子节点删除</span>
            removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
        &#125;
        api.setTextContent(elm, vnode.text!) <span class="hljs-comment">// 把新节点的text赋予给真实dom</span>
    &#125;
    hook?.postpatch?.(oldVnode, vnode) <span class="hljs-comment">// 更新视图</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看得可能有点蒙蔽,下面再上一副思维导图:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10b1affc940944fbb104690244932283~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-17">题外话:diff算法简介</h3>
<p><strong>传统diff算法</strong></p>
<ul>
<li>虚拟DOM中的Diff算法</li>
<li><code>传统算法</code>查找两颗树每一个节点的差异</li>
<li>会运行n1(dom1的节点数)*n2(dom2的节点数)次方去对比,找到差异的部分再去更新</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55d7da430d3d4bdf8d5a12a146f7bf59~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>snabbdom的diff算法优化</strong></p>
<ul>
<li>Snbbdom根据DOM的特点对传统的diff算法做了<code>优化</code></li>
<li>DOM操作时候很少会跨级别操作节点</li>
<li>只比较<code>同级别</code>的节点</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d06c2b90434b444d9bb8dc4d582de342~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/929562921ff94914bbe60647ad891104~tplv-k3u1fbpfcp-watermark.image" alt="src=http___img.wxcha.com_file_202004_03_1ed2e19e4f.jpg&refer=http___img.wxcha.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们就会介绍<code>updateChildren</code>函数怎么去对比子节点的<code>异同</code>,也是<code>Diff算法</code>里面的一个核心以及难点;</p>
<hr>
<h3 data-id="heading-18">updateChildren(核中核:判断子节点的差异)</h3>
<ul>
<li>这个函数我分为三个部分,<code>部分1:声明变量</code>,<code>部分2:同级别节点比较</code>,<code>部分3:循环结束的收尾工作</code>(见下图);</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f17a869ef82e434ba4bdeb11a7c54e55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>同级别节点比较</code>的<code>五种</code>情况:
<ol>
<li><code>oldStartVnode/newStartVnode</code>(旧开始节点/新开始节点)相同</li>
<li><code>oldEndVnode/newEndVnode</code>(旧结束节点/新结束节点)相同</li>
<li><code>oldStartVnode/newEndVnode</code>(旧开始节点/新结束节点)相同</li>
<li><code>oldEndVnode/newStartVnode</code>(旧结束节点/新开始节点)相同</li>
<li><code>特殊情况当1,2,3,4的情况都不符合</code>的时候就会执行,在<code>oldVnodes</code>里面寻找跟<code>newStartVnode</code>一样的节点然后位移到<code>oldStartVnode</code>,若没有找到在就<code>oldStartVnode</code>创建一个</li>
</ol>
</li>
<li>执行过程是一个循环,在每次循环里,只要执行了上述的情况的五种之一就会结束一次循环</li>
<li><code>循环结束的收尾工作</code>:直到oldStartIdx>oldEndIdx || newStartIdx>newEndIdx(代表旧节点或者新节点已经遍历完)</li>
</ul>
<p>为了更加直观的了解,我们再来看看<code>同级别节点比较</code>的<code>五种</code>情况的实现细节:</p>
<h4 data-id="heading-19">新开始节点和旧开始节点(情况1)</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffcab05bd82243eca7db4c759d8e1c2f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>若<code>情况1符合:(从新旧节点的开始节点开始对比</code>,<code>oldCh[oldStartIdx]和newCh[newStartIdx]</code>进行<code>sameVnode(key和sel相同)</code>判断是否相同节点)</li>
<li>则执行<code>patchVnode</code>找出两者之间的差异,更新图;如没有差异则什么都不操作,结束一次循环</li>
<li><code>oldStartIdx++/newStartIdx++</code></li>
</ul>
<h4 data-id="heading-20">新结束节点和旧结束节点(情况2)</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97bcd272a2bf47e9b027daa9408641dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>若<code>情况1不符合</code>就判断<code>情况2</code>,若符合:(从新旧节点的结束节点开始对比,<code>oldCh[oldEndIdx]和newCh[newEndIdx]</code>对比,执行<code>sameVnode(key和sel相同)</code>判断是否相同节点)</li>
<li>执行<code>patchVnode</code>找出两者之间的差异,更新视图,;如没有差异则什么都不操作,结束一次循环</li>
<li><code>oldEndIdx--/newEndIdx--</code></li>
</ul>
<h4 data-id="heading-21">旧开始节点/新结束节点(情况3)</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043575e806d04e37aca08b3bafdd006b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>若<code>情况1,2</code>都不符合,就会尝试情况3:(旧节点的开始节点与新节点的结束节点开始对比,<code>oldCh[oldStartIdx]和newCh[newEndIdx]</code>对比,执行<code>sameVnode(key和sel相同)</code>判断是否相同节点)</li>
<li>执行<code>patchVnode</code>找出两者之间的差异,更新视图,如没有差异则什么都不操作,结束一次循环</li>
<li><code>oldCh[oldStartIdx]对应的真实dom</code>位移到<code>oldCh[oldEndIdx]对应的真实dom</code>后</li>
<li><code>oldStartIdx++/newEndIdx--</code>;</li>
</ul>
<h4 data-id="heading-22">旧结束节点/新开始节点(情况4)</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c70a031047848baacc349c4ea36de7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>若<code>情况1,2,3</code>都不符合,就会尝试情况4:(旧节点的结束节点与新节点的开始节点开始对比,<code>oldCh[oldEndIdx]和newCh[newStartIdx]</code>对比,执行<code>sameVnode(key和sel相同)</code>判断是否相同节点)</li>
<li>执行<code>patchVnode</code>找出两者之间的差异,更新视图,如没有差异则什么都不操作,结束一次循环</li>
<li><code>oldCh[oldEndIdx]对应的真实dom</code>位移到<code>oldCh[oldStartIdx]对应的真实dom</code>前</li>
<li><code>oldEndIdx--/newStartIdx++</code>;</li>
</ul>
<h4 data-id="heading-23">新开始节点/旧节点数组中寻找节点(情况5)</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23c6682b562a4a7096b5e89364cc62e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>从旧节点里面寻找,若寻找到与<code>newCh[newStartIdx]</code>相同的节点(且叫<code>对应节点[1]</code>),执行<code>patchVnode</code>找出两者之间的差异,更新视图,如没有差异则什么都不操作,结束一次循环</li>
<li><code>对应节点[1]对应的真实dom</code>位移到<code>oldCh[oldStartIdx]对应的真实dom</code>前</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c2c1e87841c4693836dd6f45e8abdd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>若没有寻找到相同的节点</code>,则创建一个与<code>newCh[newStartIdx]</code>节点对应的<code>真实dom</code>插入到<code>oldCh[oldStartIdx]对应的真实dom</code>前</li>
<li><code>newStartIdx++</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd371150ce274b59a978f5301c57b79a~tplv-k3u1fbpfcp-watermark.image" alt="379426071b8130075b11ba142f9468e2.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>下面我们再介绍一下<code>结束循环</code>的收尾工作<code>(oldStartIdx>oldEndIdx || newStartIdx>newEndIdx)</code>:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e38af32ad3cc4e8381a6e7606056015f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>新节点的所有子节点</code>先遍历完(<code>newStartIdx>newEndIdx</code>),循环结束</li>
<li><code>新节点的所有子节点</code>遍历结束就是把没有对应相同节点的<code>子节点</code>删除</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84b09cb6e4bc4d68bb7d0615c58047f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>旧节点的所有子节点</code>先遍历完(<code>oldStartIdx>oldEndIdx</code>),循环结束</li>
<li><code>旧节点的所有子节点</code>遍历结束就是在多出来的<code>子节点</code>插入到<code>旧节点结束节点</code>前;(源码:<code>newCh[newEndIdx + 1].elm)</code>,就是对应的<code>旧结束节点的真实dom</code>,newEndIdx+1是因为在匹配到相同的节点需要-1,所以需要加回来就是结束节点</li>
</ul>
<p>最后附上源码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh, insertedVnodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>;                <span class="hljs-comment">// 旧节点开始节点索引</span>
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>;                <span class="hljs-comment">// 新节点开始节点索引</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>;   <span class="hljs-comment">// 旧节点结束节点索引</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>];       <span class="hljs-comment">// 旧节点开始节点</span>
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]; <span class="hljs-comment">// 旧节点结束节点</span>
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>;   <span class="hljs-comment">// 新节点结束节点索引</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>];       <span class="hljs-comment">// 新节点开始节点</span>
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]; <span class="hljs-comment">// 新节点结束节点</span>
    <span class="hljs-keyword">let</span> oldKeyToIdx;                    <span class="hljs-comment">// 节点移动相关</span>
    <span class="hljs-keyword">let</span> idxInOld;                       <span class="hljs-comment">// 节点移动相关</span>
    <span class="hljs-keyword">let</span> elmToMove;                      <span class="hljs-comment">// 节点移动相关</span>
    <span class="hljs-keyword">let</span> before;


    <span class="hljs-comment">// 同级别节点比较</span>
    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
        <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
            oldStartVnode = oldCh[++oldStartIdx]; <span class="hljs-comment">// Vnode might have been moved left</span>
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
            oldEndVnode = oldCh[--oldEndIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
            newStartVnode = newCh[++newStartIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
            newEndVnode = newCh[--newEndIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123; <span class="hljs-comment">// 判断情况1</span>
            patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue);
            oldStartVnode = oldCh[++oldStartIdx];
            newStartVnode = newCh[++newStartIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;   <span class="hljs-comment">// 情况2</span>
            patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue);
            oldEndVnode = oldCh[--oldEndIdx];
            newEndVnode = newCh[--newEndIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; <span class="hljs-comment">// Vnode moved right情况3</span>
            patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue);
            api.insertBefore(parentElm, oldStartVnode.elm, api.nextSibling(oldEndVnode.elm));
            oldStartVnode = oldCh[++oldStartIdx];
            newEndVnode = newCh[--newEndIdx];
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left情况4</span>
            patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue);
            api.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm);
            oldEndVnode = oldCh[--oldEndIdx];
            newStartVnode = newCh[++newStartIdx];
        &#125;
        <span class="hljs-keyword">else</span> &#123;                                             <span class="hljs-comment">// 情况5</span>
            <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
                oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx);
            &#125;
            idxInOld = oldKeyToIdx[newStartVnode.key];
            <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element        // 创建新的节点在旧节点的新节点前</span>
                api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm);
            &#125;
            <span class="hljs-keyword">else</span> &#123;
                elmToMove = oldCh[idxInOld];
                <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123; <span class="hljs-comment">// 创建新的节点在旧节点的新节点前</span>
                    api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm);
                &#125;
                <span class="hljs-keyword">else</span> &#123;
                                                           <span class="hljs-comment">// 在旧节点数组中找到相同的节点就对比差异更新视图,然后移动位置</span>
                    patchVnode(elmToMove, newStartVnode, insertedVnodeQueue);
                    oldCh[idxInOld] = <span class="hljs-literal">undefined</span>;
                    api.insertBefore(parentElm, elmToMove.elm, oldStartVnode.elm);
                &#125;
            &#125;
            newStartVnode = newCh[++newStartIdx];
        &#125;
    &#125;
    <span class="hljs-comment">// 循环结束的收尾工作</span>
    <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
        <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
            <span class="hljs-comment">// newCh[newEndIdx + 1].elm就是旧节点数组中的结束节点对应的dom元素</span>
            <span class="hljs-comment">// newEndIdx+1是因为在之前成功匹配了newEndIdx需要-1</span>
            <span class="hljs-comment">// newCh[newEndIdx + 1].elm,因为已经匹配过有相同的节点了,它就是等于旧节点数组中的结束节点对应的dom元素(oldCh[oldEndIdx + 1].elm)</span>
            before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm;
            <span class="hljs-comment">// 把新节点数组中多出来的节点插入到before前</span>
            addVnodes(parentElm, before, newCh, newStartIdx, newEndIdx, insertedVnodeQueue);
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 这里就是把没有匹配到相同节点的节点删除掉</span>
            removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-24">key的作用</h4>
<ul>
<li>Diff操作可以<code>更加快速</code>;</li>
<li>Diff操作可以更加准确;<code>(避免渲染错误)</code></li>
<li><code>不推荐使用索引</code>作为key</li>
</ul>
<p>以下我们看看这些作用的实例:</p>
<h5 data-id="heading-25">Diff操作可以更加准确;<code>(避免渲染错误)</code>:</h5>
<p>实例:a,b,c三个dom元素中的b,c间插入一个z元素</p>
<p>没有设置key
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc841403d3874843adeb339feb901215~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当设置了key:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf9ebd75b8ed4d85a2e015420c20c7e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-26">Diff操作可以更加准确;<code>(避免渲染错误)</code></h5>
<p>实例:a,b,c三个dom元素,修改了a元素的某个属性再去在a元素前新增一个z元素</p>
<p>没有设置key:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00cd0de9dd140b184b3dd0d10200d3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25a742557b014b7685dc7ecc2b5d941a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为没有设置key,默认都是undefined,所以节点都是相同的,更新了text的内容但还是沿用了之前的dom,所以实际上<code>a->z(a原本打勾的状态保留了,只改变了text),b->a,c->b,d->c</code>,遍历完毕发现还要增加一个dom,在最后新增一个text为d的dom元素</p>
<p>设置了key:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c94fa1135b4d6a8aaa74ecd53f515a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af7ab3ff46724f6b8f836fb5c0860644~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当设置了key,a,b,c,d都有对应的key,<code>a->a,b->b,c->c,d->d</code>,内容相同无需更新,遍历结束,新增一个text为z的dom元素</p>
<h5 data-id="heading-27"><code>不推荐使用索引</code>作为key:</h5>
<p>设置索引为key:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df0109381ef04b9c90d35be0dcf9f0dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这明显效率不高,我们只希望找出不同的节点更新,而使用索引作为key会增加运算时间,我们可以把key设置为与节点text为一致就可以解决这个问题:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/803ebdd0db5b40f8b6cfb8dfc6721ebe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-28">最后</h2>
<p>如有描述错误或者不明的地方请在下方评论联系我,我会立刻更新,如有收获,请为我点个赞👍这是对我的莫大的支持,谢谢各位</p></div>  
</div>
            