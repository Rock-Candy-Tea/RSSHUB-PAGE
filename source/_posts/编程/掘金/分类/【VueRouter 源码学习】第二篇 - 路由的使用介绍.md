
---
title: '【VueRouter 源码学习】第二篇 - 路由的使用介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/575ad0507ee545aebbeba40623b27ca5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 07:55:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/575ad0507ee545aebbeba40623b27ca5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<h2 data-id="heading-0">一，前言</h2>
<p>上篇，介绍了源码环境搭建与路由模式，主要涉及以下几个点：</p>
<ul>
<li>完成了 VueRouter 源码项目开发环境的搭建；</li>
<li>介绍了 Hash 和 History 两种路由模式;</li>
</ul>
<p>本篇，路由的使用介绍；</p>
<hr>
<h2 data-id="heading-1">二，VueRouter 的使用</h2>
<h3 data-id="heading-2">安装依赖</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue-router
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">路由插件的配置</h3>
<p>创建 router.js 进行路由插件配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'./vue-router'</span>;

<span class="hljs-comment">// 通过 Vue.use 使用 Router 插件：</span>
<span class="hljs-comment">// 全局注册两个组件：router-link、router-view；</span>
<span class="hljs-comment">// 为实例提供两个原型属性：$router，$route；</span>
Vue.use(Router); 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">备注：
Vue.use()内部会调用 install 方法
注册全局组件：router-link 和 router-view；
同时，为实例提供两个原型上的属性：$router，$route；
<span class="copy-code-btn">复制代码</span></code></pre>
<p>router-link 组件：内部会对路由的 Hash 模式和 History 模式做兼容处理；</p>
<p>创建 Router 实例并导出：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'./vue-router'</span>;

Vue.use(Router);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>:<span class="hljs-string">'hash'</span>,
  <span class="hljs-attr">routes</span>:[
    &#123;
      <span class="hljs-attr">path</span>:<span class="hljs-string">'/'</span>,      <span class="hljs-comment">// 路径</span>
      <span class="hljs-attr">name</span>:<span class="hljs-string">''</span>,       <span class="hljs-comment">// 名字</span>
      <span class="hljs-attr">component</span>:ABC  <span class="hljs-comment">// 路径显示的组件</span>
    &#125;
  ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">创建视图组件</h3>
<p>创建 2 个视图组件 Home 和 Mine：</p>
<pre><code class="hljs language-html copyable" lang="html">// views/Home.vue
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

// views/Mine.vue
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我的<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">配置路由和页面的关系</h3>
<p>引入两个视图组件，配置路由和页面的关系</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'./vue-router'</span>;
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'./node_modules/vue-router'</span>;
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'./views/Home'</span>;
<span class="hljs-keyword">import</span> Mine <span class="hljs-keyword">from</span> <span class="hljs-string">'./views/Mine'</span>;

Vue.use(Router);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>:<span class="hljs-string">'hash'</span>,
  <span class="hljs-attr">routes</span>:[
    &#123;
      <span class="hljs-attr">path</span>:<span class="hljs-string">'/'</span>,       <span class="hljs-comment">// 路径</span>
      <span class="hljs-attr">name</span>:<span class="hljs-string">''</span>,        <span class="hljs-comment">// 名字</span>
      <span class="hljs-attr">component</span>: Home <span class="hljs-comment">// 路径显示的组件</span>
    &#125;,&#123;
      <span class="hljs-attr">path</span>:<span class="hljs-string">'/'</span>,
      <span class="hljs-attr">name</span>:<span class="hljs-string">''</span>,
      <span class="hljs-attr">component</span>: Mine
    &#125;
  ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">路由注册到 Vue</h3>
<p>注册路由到 Vue 实例中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>

<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;  <span class="hljs-comment">// 导入路由配置</span>

<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
  router, <span class="hljs-comment">// 将路由注册到 Vue 实例中</span>
  <span class="hljs-attr">render</span>:<span class="hljs-function">(<span class="hljs-params">h</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'h1'</span>, &#123;&#125;, <span class="hljs-string">'Hello Vue Router'</span>);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">配置路由组件的渲染位置</h3>
<p>创建根组件 App.vue 用于显示视图渲染后的结果：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 显示页面渲染的内容 --></span>
        <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，需要 h 方法渲染 App.vue：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;

<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
  router,
  <span class="hljs-attr">render</span>:<span class="hljs-function">(<span class="hljs-params">h</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> h(App);<span class="hljs-comment">// 使用 h 方法渲染 App 组件</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">启动服务</h3>
<pre><code class="hljs language-bash copyable" lang="bash">vue serve
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">查看视图组件</h3>
<p>访问路由查看视图组件显示：</p>
<p>首页：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/575ad0507ee545aebbeba40623b27ca5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我的：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fa85b99681d4837b8ec3f317ce76551~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>备注：由于使用了 hash 模式，URL 默认会被添加 '/#/'</p>
<hr>
<h3 data-id="heading-10">添加路由的切换</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!-- 添加路由切换 --></span>
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>跳转至首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
        &nbsp
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/mine"</span>></span>跳转至我的<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
        <span class="hljs-comment"><!-- 显示页面渲染的内容 --></span>
        <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">测试路由切换效果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c909166945b45d0a40877c44d19c57c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/542eabfc50314e72b0174f6c539447cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-12">三，结尾</h2>
<p>本篇，介绍了路由的配置和使用；</p>
<p>下篇，路由 install 的实现；</p></div>  
</div>
            