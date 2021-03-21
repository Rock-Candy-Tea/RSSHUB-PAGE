
---
title: ​基于UmiJS的自动化Fetch请求生成插件
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 07:28:42 GMT
thumbnail: https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d8ce44ea6fe4b29be6dec3607e3028a~tplv-k3u1fbpfcp-watermark.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h2 data-id="heading-0">🔰 简介</h2>
<p>在<code>2021</code>年的今天，在大部分项目中已经抛弃了原先荒漠式的接口写法，很多项目都有意识的拆分成了很多个单独的<code>function</code>函数进行维护，每次写接口的时候不是在页面上套路一堆的<code>$axios</code>...等等与视图逻辑的代码。而是有意义的写成<code>Promise<R></code>返回值的函数，通过<code>export</code>往外导出。</p>
<p>诚然，目前的解决方案已经足够满足于我们当下的需求，虽然维护一份<code>export function</code>看起来很头疼。但是，为了以后，我忍了。只能不断的<code>CV</code>然后修改参数。那么，有没有更好的方式呢？</p>
<p>在之前的文章中，我分享了<code>约定式接口</code>，意思是将<code>接口函数</code>通过配置生成。那么我们在实际开发中就只需要编写配置就可以生产出一个<code>axios</code>，<code>fetch</code>的函数概念。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 配置 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> {
    <span class="hljs-attr">getUserInfo</span>: <span class="hljs-string">'POST /mall-app/v1/user'</span>
}

<span class="hljs-comment">/* 生成 */</span>
<span class="hljs-keyword">const</span> getUserInfo = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> {
    request(<span class="hljs-comment">//...todo)</span>
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今天就给大家分享下，聊聊在团队项目中是如何做<code>接口函数</code>自动生成的吧。</p>
<h2 data-id="heading-1">✅ 编译时  ❎ 运行时</h2>
<p>在之前的文章，提到的<code>约定式接口</code>是基于<code>运行时</code>产生的，有很多的缺点问题。具体可以去看我上一篇文章，在这里先开个传送门：<a href="https://juejin.cn/post/6873605885868916744" target="_blank">点击阅读</a></p>
<p>直观的缺点</p>
<ul>
<li>函数代码不可读</li>
<li>函数代码不可推导</li>
<li>逻辑执行是在项目运行去做的，需要开销。</li>
<li>函数代码错误无法检测</li>
<li>...</li>
</ul>
<p>当上述问题抛出的时候，对于使用<code>TypeScript</code>组织代码的项目简直是一种灾难，类型推导完全看运行时标注。 <code>TransForm</code>函数通过<code>Record<string, (data: Record<string, any>) => Promise<any>></code>的方式实现，虽然也可以实现基本的类型推导，但是对于代码维护者来说，是及其不友好的。</p>
<p><code># 上述类型推导默认为any</code></p>
<p>在纠结一段时间后，毅然决然的使用<code>微内核脚手架@umijs</code>的插件行为来做配置依赖管理。那么可以使用<code>插件</code>自带的能力见简便在<code>编译时</code>获得当前<code>配置文件</code>映射出来的函数文件。</p>
<p>那么，我们一起看看，映射插件是怎么练成的吧。</p>
<h2 data-id="heading-2">💦明确插件功能</h2>
<p>插件的功能核心就是自动映射<code>接口函数</code>，可供开发者在开发时调用，且获取来自于外部的数据。</p>
<p>那么我们根据运行时的开发思路相对来说实现起来逻辑是没有问题的。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d8ce44ea6fe4b29be6dec3607e3028a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">👍如何使用？</h2>
<h3 data-id="heading-4">install</h3>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> yarn</span>
yarn add plugin-transform-api -D
<span class="hljs-meta">
#</span><span class="bash"> npm</span>
npm install plugin-transform-api -D --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">创建接口配置文件路径</h3>
<p>确保当前的文件正确的存在于目录当中。</p>
<pre><code class="hljs language-tree copyable" lang="tree">.umi
│  ├─.cache
│  │  └─babel-loader
│  ├─core
│  ├─plugin-helmet
│  ├─plugin-initial-state
│  │  └─models
│  ├─plugin-interface
│  ├─plugin-model
│  └─plugin-request
├─pages
└─services
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">创建一个接口</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = {
    <span class="hljs-attr">fetchUserLogin</span>: <span class="hljs-string">'POST /service-app/v1/user/login'</span>
}
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">引入插件</h3>
<p>在<code>Umijs</code>的配置文件中引入插件，并且进行配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> { defineConfig } <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig({
  <span class="hljs-attr">nodeModulesTransform</span>: {
    <span class="hljs-attr">type</span>: <span class="hljs-string">'none'</span>,
  },
  <span class="hljs-attr">routes</span>: [
    { <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: <span class="hljs-string">'@/pages/index'</span> },
  ],
  <span class="hljs-attr">fastRefresh</span>: {},
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'plugin-transform-api'</span>],
  <span class="hljs-attr">interface</span>: {
    <span class="hljs-comment">// 指定api接口配置路径</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'services'</span>,

    <span class="hljs-comment">// 指定request接口请求配置</span>
    <span class="hljs-attr">requestPath</span>: <span class="hljs-string">'@/utils/fetch'</span>
  }
});

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">发送一个请求</h3>
<p>对<code>umi</code>进行一个接口引用。如下图，可以得到我们通过<code>fetchUserLogin: 'POST /service-app/v1/user/login'</code>生成后的一个请求函数。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a498c1c44f2a4d2f955cb049be2e4d22~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/888256a62c874158a316318f6750cea9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">🐱‍🐉资源</h2>
<ul>
<li><a href="https://github.com/wangly19/plugin-transform-api/tree/master" target="_blank" rel="nofollow noopener noreferrer">plugin-transform-api</a></li>
</ul>
<h2 data-id="heading-10">😒结语</h2>
<p>目前来说，当前插件属于一个测试版本，但是不妨碍我们继续进行一个完善。如果有好的建议欢迎加入<code>我的小窝</code>进行技术上的交流。</p>
<p>一个多月都没有写文章了，突然发现被业务牵扯了部分精力，慢慢的会恢复内容的创作。</p>
<p>当前内置请求模板：<code>umi-request</code>。基于<code>axios</code>的请求方式正在来的路上。目前来说，我个人比较推荐在支持<code>ES6</code>，而不需要进行<code>ES5</code>的适配项目中使用<code>fetch</code>来代替<code>xhr</code>。</p>
<p><em>如果你们后端爸爸好说话的话，完全可以直接下载一份接口文档当中的<code>JSON</code>文件复制到项目当中。QAQ</em></p>
<p>也是优先于我个人手头上的业务吧。</p>
<p><code>欠债文章数： 16 - 1</code></p>
<blockquote>
<p>有兴趣的朋友可以拉个群进行一些技术上的探讨。无广告</p>
</blockquote>
<p><img alt="88_785_bb9cce378efe1450897ff5734a3eb0a3_a423626931a68df99e84dc9ef79ca26d.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d756bf31f848aea0f5c6451215fc49~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            