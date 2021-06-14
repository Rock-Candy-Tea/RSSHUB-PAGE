
---
title: '【Vue2.x 源码学习】第十一篇 - Vue 的数据渲染流程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6342742f0b4db9bdd588bc724e4e32~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 04:25:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6342742f0b4db9bdd588bc724e4e32~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一，前言</h2>
<p>上篇，主要介绍了数组数据变化的观测情况，涉及以下几个点：</p>
<ul>
<li>实现了数组数据变化被劫持后，已重写原型方法的具体逻辑；</li>
<li>数组各种数据变化时的观测情况分析；</li>
</ul>
<p>目前为止，数据劫持的各种情况就全部分析完了</p>
<p>本篇，Vue的数据渲染流程</p>
<hr>
<h2 data-id="heading-1">二，如何渲染</h2>
<h3 data-id="heading-2">1，代码回顾</h3>
<p>数据初始化完成后，将开始进行视图渲染</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    vm.$options = options;
    
    initState(vm);

    <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      <span class="hljs-comment">// todo...</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>el 为 dom 挂载处，如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">app</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2，问题分析</h3>
<p>Vue 不会直接操作字符串，可以想象一下：</p>
<ul>
<li>从字符串中解析出指令，以及进行值更新是比较困难的</li>
<li>再考虑到节点复用的场景，更是无法通过对比字符串来完成</li>
</ul>
<h3 data-id="heading-4">3，Vue 视图渲染</h3>
<p>vue 支持 template 和 jsx：</p>
<ul>
<li>日常开发中，大部分会采用 template 完成模板的编写，因为 template 即简单又方便；</li>
<li>而相比 template来讲，jsx 则加更灵活。写法上也显得稍微复杂一些；</li>
</ul>
<hr>
<h2 data-id="heading-5">三，渲染流程分析</h2>
<h3 data-id="heading-6">1，流程分析</h3>
<p>Vue 需要对 template 进行解析，从而将 template 模板语法转变为 javascript 语法；</p>
<p>而这个转化的过程，就需要用到 ast 语法树（可描述 css、js、html 等语法）</p>
<p>使用 ast 语法树来对 html 的语法结构进行描述，根据 ast 树形结构将代码重组为 js 语法</p>
<p>即后续对 html 模板的操作，就都可以通过 js 来完成，而不必考虑解析字符串了</p>
<h3 data-id="heading-7">2，Vue 模板编译原理</h3>
<ol>
<li>将 template 模板编译为 render 函数</li>
<li>通过 rander 函数再返回虚拟 dom</li>
<li>再通过 diff 算法比对虚拟 dom</li>
</ol>
<p>流程：template模板 -> render 函数 -> 虚拟dom -> diff 算法</p>
<hr>
<h2 data-id="heading-8">四，简单分析</h2>
<p><a href="https://template-explorer.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">template-explorer.vuejs.org/</a>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6342742f0b4db9bdd588bc724e4e32~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>div 模板：最终被编译成为一个 render 方法，即 render 函数；</li>
<li>_c 函数：相当于 createElement，创建div，内部包含属性 id ，值为 app；</li>
<li>_v 函数：创建文本，即将_s(msg)创建为一个文本；</li>
<li>_s 函数：相当于 JSON.stringify，如果吗模板参数msg为对象，通过 _s 使其转为 string</li>
</ul>
<hr>
<h2 data-id="heading-9">五，Vue 数据渲染的核心流程</h2>
<h3 data-id="heading-10">1，初次渲染时</h3>
<ol>
<li>template 模板被编译为 ast 语法树；</li>
<li>通过 ast 语法树生成 render 函数；</li>
<li>通过 render 函数返回 vnode 虚拟节点；</li>
<li>使用 vnode 虚拟节点生成真实 dom 并进行渲染；</li>
</ol>
<h3 data-id="heading-11">2，视图更新时</h3>
<ol>
<li>调用 render 函数生成新的 vnode 虚拟节点；</li>
<li>通过 diff 算法对新老 vnode 虚拟节点进行对比；</li>
<li>根据虚拟节点比对结果，更新真实 dom；</li>
</ol>
<hr>
<h2 data-id="heading-12">六，结尾</h2>
<p>本篇，主要介绍了 vue 数据渲染核心流程</p>
<p>下一篇，template 模板生成 ast 语法树</p></div>  
</div>
            