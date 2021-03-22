
---
title: '一键生成基于Vue3+Webpack5开箱即用的管理台'
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 20:31:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92df1d7384614244897f2cb0e22eaff3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>互联网时代，形形色色的<code>H5</code>应用、小程序……各种C端B端业务都少不了中后台管理系统，市面上有<code>antd</code>、<code>iview</code>等各种<code>UI</code>框架组件库，但是一个管理台往往涉及到公司统一的登录、权限管理、统一的请求处理、数据管理、自动化测试、甚至还有国际化等场景，如果从零搭建，这些都是我们需要考虑的，但是这些其实是和业务解耦的，所以本着以后再次创建管理台时不想复制粘贴，于是选用了新鲜出炉的<code>Fes.js 2.0</code>来构建。</p>
<h2 data-id="heading-0">关于Fes.js</h2>
<p><code>Fes.js</code>是基于最新 <code>Vue3 + webpack5</code> 的前端应用框架，通过插件化提供了统一的布局、登录、权限管理、<code>Vuex</code>、国际化等能力，关于<code>fes.js</code>更多了解可以参考<a href="https://winixt.gitee.io/fesjs/zh/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>。话不多说，下面就来带你从零搭建一个开箱即用的中后台管理系统。</p>
<h2 data-id="heading-1">准备</h2>
<p>首先确保本地<strong>Node</strong>版本是<code>12.0.0</code>以上（也别12了，都1202年了，秦朝都灭亡了，升级最新吧）~</p>
<p>如果你喜欢用<code>yarn</code>，那就用以下三部曲：</p>
<h3 data-id="heading-2">1.创建模板</h3>
<pre><code class="hljs language-shell copyable" lang="shell">yarn create @fesjs/fes-app fes-demo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据自己的需求选择创建<strong>PC</strong>或<strong>H5</strong>项目，创建完项目后<code>cd</code>到刚刚创建的目录：<code>cd fes-demo</code>，然后继续下一步。</p>
<h3 data-id="heading-3">2.安装依赖</h3>
<pre><code class="hljs language-shell copyable" lang="shell">yarn
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.运行开发环境</h3>
<pre><code class="hljs language-shell copyable" lang="shell">yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你喜欢用<code>npm</code>（你怕毛），那就用以下三部曲：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 创建模板</span>
npx @fesjs/create-fes-app fes-demo
<span class="hljs-meta">
#</span><span class="bash"> 安装依赖</span>
npm install
<span class="hljs-meta">
#</span><span class="bash"> 运行</span>
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">初见</h2>
<p>执行完以上操作之后，在浏览器访问：<a href="http://127.0.0.1:8080%EF%BC%8C" target="_blank" rel="nofollow noopener noreferrer">http://127.0.0.1:8080，</a> 我们就可以看到初始的系统界面了，如下图：</p>
<p><img alt="fes-demo-init" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92df1d7384614244897f2cb0e22eaff3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">开干</h2>
<h3 data-id="heading-7">新建页面</h3>
<p>接下来我们试着新建几个页面，在<code>pages</code>目录下新建以下目录和文件：</p>
<pre><code class="copyable">├─pages
│  ├─order
|    └─ list.vue
|     └─ detail.vue
│  └─product
|     └─ list.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>fes</code>会根据我们的目录结构自动生成<code>Vue</code>的<code>routes</code>，如果想知道生成的路由具体结构可以在<code>src\.fes\core\routes\routes.js</code> 文件中查看。</p>
<h3 data-id="heading-8">页面配置</h3>
<p>页面新建之后，我们来配置一下页面的<code>name</code>及<code>title</code>等相关信息，这里我们以<code>pages/product/list.vue</code> 文件为例，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/pages/product/list.vue</span>

<template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">config</span>></span>
&#123;
    "name": "productManage",
    "title": "产品管理"
&#125;
<span class="hljs-tag"></<span class="hljs-name">config</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, reactive, toRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
...
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">配置菜单和权限</h3>
<p>页面配置好了之后，在根目录的<code>.fes.js</code>文件中配置一下<strong>菜单</strong>和<strong>权限</strong>，<code>.fes.js</code> 文件为项目基础配置文件，详情可参考<a href="https://winixt.gitee.io/fesjs/zh/guide/config.html" target="_blank" rel="nofollow noopener noreferrer">官网文档</a>，这里我们修改内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    ... <span class="hljs-comment">// 其他配置略</span>
    <span class="hljs-attr">access</span>: &#123;
        <span class="hljs-attr">roles</span>: &#123;
            <span class="hljs-attr">superAdmin</span>: [<span class="hljs-string">"/"</span>, <span class="hljs-string">"/product/list"</span>, <span class="hljs-string">"/order/list"</span>, <span class="hljs-string">"/order/detail"</span>],
            <span class="hljs-attr">admin</span>: [<span class="hljs-string">"/"</span>, <span class="hljs-string">"/product/list"</span>]
        &#125;
    &#125;,
    <span class="hljs-attr">layout</span>: &#123;
        ...
        <span class="hljs-attr">menus</span>: [
            &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>
            &#125;,
            &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'productManage'</span><span class="hljs-comment">// 产品管理</span>
            &#125;,
            &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'orderManage'</span>,<span class="hljs-comment">// 订单管理</span>
                <span class="hljs-attr">title</span>: <span class="hljs-string">'订单管理'</span>,
                <span class="hljs-attr">children</span>: [
                    &#123;
                        <span class="hljs-attr">name</span>: <span class="hljs-string">'orderList'</span><span class="hljs-comment">// 订单列表</span>
                    &#125;
                ]
            &#125;
        ]
    &#125;
    ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，这里我们设置了两个角色，超级管理员（<code>superAdmin</code>）和普通管理员（<code>admin</code>），超级管理员比普通管理员可以访问更多的页面，在页面渲染前通过<code>setRole</code>这个方法设定角色为<code>superAdmin</code>（超级管理员），这里参考<code>app.js</code>的代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; access &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@fesjs/fes'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> beforeRender = &#123;
    <span class="hljs-attr">loading</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">PageLoading</span> /></span></span>,
    <span class="hljs-function"><span class="hljs-title">action</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; setRole &#125; = access;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                setRole(<span class="hljs-string">'superAdmin'</span>);<span class="hljs-comment">// 设定角色</span>
                resolve(&#123;
                    <span class="hljs-attr">userName</span>: <span class="hljs-string">'Hello, World!'</span>
                &#125;);
            &#125;, <span class="hljs-number">1000</span>);
        &#125;);
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，<code>menus</code>中的<code>name</code>要与页面配置的<code>name</code>相匹配，比如<code>menus</code>中【产品管理】那一项配置的<code>name: 'productManage'</code> 需要和具体页面文件<code>src/pages/product/list.vue</code>文件中<code><config></config></code> 的<code>name</code>相匹配。</p>
<p>根据配置好的<code>menus</code>，以及设置对应的权限后我们就可以看到以下界面：</p>
<p><img alt="fes-demo-01" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ad9c46760e74fdaa669efeff1232dcc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>到这里我们完成了常见的新建页面、菜单、权限等场景的开发，是不是觉得很简单？</p>
<p>接下来我们简单看看其他一些常见的开发配置场景~</p>
<h2 data-id="heading-10">常见配置问题FAQ</h2>
<h3 data-id="heading-11">1.UI组件库按需加载怎么配？</h3>
<p>这里以<code>ant-design-vue</code> 为例，在 <code>.fes.js</code> 中增加如下配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    ...
    <span class="hljs-attr">extraBabelPlugins</span>: [
        [<span class="hljs-string">'import'</span>, &#123; <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'ant-design-vue'</span>, <span class="hljs-attr">libraryDirectory</span>: <span class="hljs-string">'es'</span>, <span class="hljs-attr">style</span>: <span class="hljs-string">'css'</span> &#125;]
    ],
    ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>babel</code>的配置Copy过来就行，简单So easy~</p>
<h3 data-id="heading-12">2.HTTP请求怎么玩？</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; request &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@fesjs/fes'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">add</span>: <span class="hljs-function">(<span class="hljs-params">data, option</span>) =></span> request(<span class="hljs-string">'/api/product/add'</span>, data, option),
    <span class="hljs-attr">getList</span>: <span class="hljs-function">(<span class="hljs-params">data, option</span>) =></span> request(<span class="hljs-string">'/api/product/list'</span>, data, option)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多玩法可参考<a href="https://winixt.gitee.io/fesjs/zh/reference/plugin/plugins/request.html" target="_blank" rel="nofollow noopener noreferrer">request插件</a>文档。</p>
<h3 data-id="heading-13">3.统一的请求处理在哪配置？</h3>
<p>比如想要对接口相应的数据做统一处理，可以添加<code>responseDataAdaptor</code>这个钩子函数，参数<code>data</code>就是接口返回的报文部分，又比如对接口的<code>code</code>进行统一处理，可以添加<code>errorHandler</code>。</p>
<h4 data-id="heading-14">示例：</h4>
<p>假如后端返回的<code>JSON</code>数据如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
<span class="hljs-attr">"code"</span>: <span class="hljs-string">"8888"</span>,
<span class="hljs-attr">"msg"</span>: <span class="hljs-string">"未登录或登录态过期，请重新登录"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么在<code>app.js</code>中做如下配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; getRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@fesjs/fes'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> request = &#123;
    <span class="hljs-attr">responseDataAdaptor</span>: <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        <span class="hljs-comment">// data.code = data.retCode;</span>
        <span class="hljs-keyword">return</span> data;
    &#125;,
    <span class="hljs-attr">errorHandler</span>: &#123;
        <span class="hljs-number">8888</span>: <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> router = getRouter();
            alert(<span class="hljs-string">'登录态过期，请重新登录'</span>);
            router.push(<span class="hljs-string">'/account/login'</span>);
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置中<code>8888</code>对应的是接口<code>code</code>字段返回的值，如果接口返回的<code>code</code>字段叫别的名称，比如叫<code>retCode</code>，可以在<code>responseDataAdaptor </code>进行转换，如：<code>data.code = data.retCode;</code>。</p>
<h3 data-id="heading-15">4.支持移动端应用的开发吗？</h3>
<p><code>Fes.js</code> 同时支持 PC 和移动端的开发，同时为 PC 和移动端提供了一些标配的能力。例如 PC 端的布局、权限管理、国际化等；移动端的屏幕适配、1px 问题、hover 态等，相信在初始化应用的时候你已经看到了，<strong>PC</strong> or <strong>H5</strong> 任你选~</p>
<h3 data-id="heading-16">5.文件引入别名配置</h3>
<p>在<code>.fes.js</code>中添加如下配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">alias: &#123;
    <span class="hljs-string">'@common'</span>: <span class="hljs-string">'src/common/'</span>,
    <span class="hljs-string">'@utils'</span>: <span class="hljs-string">'src/utils/'</span>,
    <span class="hljs-string">'@images'</span>: <span class="hljs-string">'src/images/'</span>,
    <span class="hljs-string">'@services'</span>: <span class="hljs-string">'src/services/'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件中导入方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> xxx <span class="hljs-keyword">from</span> <span class="hljs-string">'@/common/xxx.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">6.换个Logo？</h3>
<p>在<code>.fes.js</code>文件中添加Logo字段，换成你的图片路径（可以是一个完整的图片链接）就行了，<strong>需要注意的是如果这个Logo是本地的，需要将Logo文件拷贝到<code>public</code>目录下</strong>（如果没有，自行在项目根目录建立一个<code>public</code>目录），<code>public</code>目录可以放置一些其他不需要经过<code>webpack</code>打包的文件。</p>
<p>这里在<code>public</code>目录中新建了一个<code>img</code>目录，并将Logo图片放入，那么Logo路径配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    ...
    <span class="hljs-attr">layout</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'xx管理系统'</span>,
        <span class="hljs-attr">logo</span>: <span class="hljs-string">'./img/logo.png'</span>,
        ...
    &#125;,
    ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，如果还想了解更多的开发场景配置，可以自己参考<a href="https://winixt.gitee.io/fesjs/zh/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>一点点体验。</p>
<h2 data-id="heading-18">结语</h2>
<p>经过在一个新的内部管理系统实践<code>fes.js</code>，整体下来感觉还是能够提升很大的开发效率，很多常见的开发场景都可以通过插件化添加，省去自己一点点编码的时间。不过<code>fes 2.0</code> 刚刚新鲜出炉，还有很多的开发场景待支持，希望后续能够出更多的插件，提供更多的能力。</p>
<h2 data-id="heading-19">参考链接</h2>
<ul>
<li>Fes.js官网文档：<a href="https://winixt.gitee.io/fesjs/zh/" target="_blank" rel="nofollow noopener noreferrer">winixt.gitee.io/fesjs/zh/</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            