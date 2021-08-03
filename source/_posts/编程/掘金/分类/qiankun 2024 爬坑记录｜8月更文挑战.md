
---
title: 'qiankun 2.0.24 爬坑记录｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6930'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 07:51:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6930'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>由于本次开发项目需要嵌入之前的老项目，由于考虑到iframe速度慢、css/js需要额外请求、阻塞页面加载、浏览器前进/后退等缺点，遂打算踩坑qiankun，为了更早的爬坑，整理此文。</p>
</blockquote>
<h1 data-id="heading-0">简介</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fqiankun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/qiankun" ref="nofollow noopener noreferrer">qiankun</a> 是一个基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsingle-spa%2Fsingle-spa" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/single-spa/single-spa" ref="nofollow noopener noreferrer">single-spa</a> 的<code>微前端</code>实现库，旨在帮助大家能更简单、无痛的构建一个生产可用微前端架构系统。</p>
<p><strong>官方提供的资源：</strong></p>
<ul>
<li>官方提供了一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffengxianqi%2Fqiankun-example" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fengxianqi/qiankun-example" ref="nofollow noopener noreferrer">示例代码</a></li>
<li>示例代码的<a href="https://link.juejin.cn/?target=http%3A%2F%2Fqiankun.fengxianqi.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://qiankun.fengxianqi.com/" ref="nofollow noopener noreferrer">在线demo</a></li>
<li>单独访问在线<a href="https://link.juejin.cn/?target=http%3A%2F%2Fqiankun.fengxianqi.com%2Fsubapp%2Fsub-vue%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://qiankun.fengxianqi.com/subapp/sub-vue/" ref="nofollow noopener noreferrer">vue子应用</a></li>
<li>单独访问在线<a href="https://link.juejin.cn/?target=http%3A%2F%2Fqiankun.fengxianqi.com%2Fsubapp%2Fsub-react%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://qiankun.fengxianqi.com/subapp/sub-react/" ref="nofollow noopener noreferrer">react子应用</a></li>
</ul>
<p><strong>根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fqiankun.umijs.org%2Fzh%2Fguide%23%25E7%2589%25B9%25E6%2580%25A7" target="_blank" rel="nofollow noopener noreferrer" title="https://qiankun.umijs.org/zh/guide#%E7%89%B9%E6%80%A7" ref="nofollow noopener noreferrer">qiankun官方文档</a> 介绍，主要有以下七大特性：</strong></p>
<ul>
<li>📦 基于 single-spa 封装，提供了更加开箱即用的 API。</li>
<li>📱 技术栈无关，任意技术栈的应用均可 使用/接入，不论是 React/Vue/Angular/JQuery 还是其他等框架。</li>
<li>💪 HTML Entry 接入方式，让你接入微应用像使用 iframe 一样简单。</li>
<li>🛡​ 样式隔离，确保微应用之间样式互相不干扰。</li>
<li>🧳 JS 沙箱，确保微应用之间 全局变量/事件 不冲突。</li>
<li>⚡️ 资源预加载，在浏览器空闲时间预加载未打开的微应用资源，加速微应用打开速度。</li>
<li>🔌 umi 插件，提供了 @umijs/plugin-qiankun 供 umi 应用一键切换成微前端架构系统。</li>
</ul>
<p><strong>行业内其他前端团队对微前端的看法和实践：</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6844903943873675271" target="_blank" title="https://juejin.cn/post/6844903943873675271">每日优鲜供应链前端团队微前端改造</a></li>
<li><a href="https://juejin.cn/post/6844904073972432903" target="_blank" title="https://juejin.cn/post/6844904073972432903">微前端在美团外卖的实践</a></li>
<li><a href="https://juejin.cn/post/6844904046487142408" target="_blank" title="https://juejin.cn/post/6844904046487142408">前端微服务在字节跳动的打磨与应用</a></li>
<li><a href="https://juejin.cn/post/6844904112421765134" target="_blank" title="https://juejin.cn/post/6844904112421765134">微前端在小米 CRM 系统的实践</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.aliyun.com%2Farticle%2F742576" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.aliyun.com/article/742576" ref="nofollow noopener noreferrer">标准微前端架构在蚂蚁的落地实践</a></li>
</ul>
<h1 data-id="heading-1">API介绍</h1>
<p>此处只介绍api的简单功能描述，如想继续了解请移步<a href="https://link.juejin.cn/?target=https%3A%2F%2Fqiankun.umijs.org%2Fzh%2Fapi" target="_blank" rel="nofollow noopener noreferrer" title="https://qiankun.umijs.org/zh/api" ref="nofollow noopener noreferrer">官方文档</a></p>
<h2 data-id="heading-2">registerMicroApps(apps, lifeCycles?)</h2>
<p>注册微应用的基础配置信息。当浏览器 url 发生变化时，会自动检查每一个微应用注册的 activeRule 规则，符合规则的应用将会被自动激活。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; registerMicroApps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

registerMicroApps(
  [
    &#123;
      <span class="hljs-comment">// name - string - 必选，微应用的名称，微应用之间必须确保唯一</span>
      <span class="hljs-attr">name</span>: <span class="hljs-string">'apass-micro'</span>,
      <span class="hljs-comment">// entry - string - 必选，微应用的入口</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'localhost:8080'</span>,
      <span class="hljs-comment">// container - string | HTMLElement - 必选，微应用的容器节点的选择器或者 Element 实例</span>
      <span class="hljs-attr">container</span>: <span class="hljs-string">'#apassMicroTemplateConfig'</span>,
      <span class="hljs-comment">// activeRule - string - 必选，微应用的激活规则</span>
      <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/index/config/template/edit'</span>,
      <span class="hljs-comment">// props - object - 可选，主应用需要传递给微应用的数据</span>
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'kuitos'</span>,
        <span class="hljs-attr">routerPushFunc</span>: <span class="hljs-function">(<span class="hljs-params">that</span>) =></span> &#123;
          that.$router.push(<span class="hljs-string">'/713/5f4f65fabcb7c173/fields'</span>)
        &#125;,
        <span class="hljs-attr">data</span>: &#123;
          <span class="hljs-comment">// 已响应式的数据通信</span>
          <span class="hljs-attr">store</span>: microAppStore.getGlobalState
        &#125;,
      &#125;
    &#125;
  ],
  &#123;
    <span class="hljs-attr">beforeLoad</span>: <span class="hljs-function"><span class="hljs-params">app</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before load'</span>, app.name),
    <span class="hljs-attr">beforeMount</span>: [
      <span class="hljs-function"><span class="hljs-params">app</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before mount'</span>, app.name),
    ],
    <span class="hljs-attr">afterMount</span>: [
      <span class="hljs-function"><span class="hljs-params">app</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'after mount'</span>, app.name),
    ],
    <span class="hljs-attr">beforeUnmoun</span>: [
      <span class="hljs-function"><span class="hljs-params">app</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before unmount'</span>, app.name),
    ],
    <span class="hljs-attr">afterUnmount</span>: [
      <span class="hljs-function"><span class="hljs-params">app</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'after unmount'</span>, app.name),
    ]
  &#125;,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">start(opts?)</h2>
<p>启动 qiankun</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; start &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">setDefaultMountApp(appLink)</h2>
<p>设置主应用启动后默认进入的微应用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; setDefaultMountApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

setDefaultMountApp(<span class="hljs-string">'/homeApp'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">runAfterFirstMounted(effect)</h2>
<p>第一个微应用 mount 后需要调用的方法，比如开启一些监控或者埋点脚本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; runAfterFirstMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

runAfterFirstMounted(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一个子应用加载完后，该方法被调用'</span>)
  <span class="hljs-built_in">this</span>.otherFunction()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">loadMicroApp(app, configuration?)</h2>
<p>适用于需要手动 加载/卸载 一个微应用的场景。</p>
<p>通常这种场景下微应用是一个不带路由的可独立运行的业务组件。 微应用不宜拆分过细，建议按照业务域来做拆分。业务关联紧密的功能单元应该做成一个微应用，反之关联不紧密的可以考虑拆分成多个微应用。 一个判断业务关联是否紧密的标准：看这个微应用与其他微应用是否有频繁的通信需求。如果有可能说明这两个微应用本身就是服务于同一个业务场景，合并成一个微应用可能会更合适。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

<span class="hljs-comment">// 因为loadMicroApp()返回子应用的实例，拿一个全局变量接收后续可进行其他操作如：手动卸载子应用</span>
<span class="hljs-built_in">this</span>.microApp = loadMicroApp(
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'sub-vue'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'http://localhost:7777/subapp/sub-vue'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#apassMicroTemplateConfig'</span>,
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">routerBase</span>: <span class="hljs-string">'/index/config/template/edit'</span>,
      <span class="hljs-attr">getGlobalState</span>: microAppStore.getGlobalState,
      <span class="hljs-attr">sheetId</span>: <span class="hljs-string">'2133123123'</span>
    &#125;
  &#125;,
  &#123;
    <span class="hljs-comment">// sandbox - boolean | &#123; strictStyleIsolation?: boolean, experimentalStyleIsolation?: boolean &#125; - 可选，是否开启沙箱，默认为 true</span>
    <span class="hljs-attr">sandbox</span>: &#123; <span class="hljs-attr">strictStyleIsolation</span>: <span class="hljs-literal">true</span> &#125;,
    <span class="hljs-comment">// singular - boolean | ((app: RegistrableApp<any>) => Promise<boolean>); - 可选，是否为单实例场景，单实例指的是同一时间只会渲染一个微应用。默认为 false</span>
    <span class="hljs-attr">singular</span>: <span class="hljs-literal">true</span>
  &#125;
)

<span class="hljs-comment">// 封装卸载子应用的函数</span>
private unmountMicroApp () &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.microApp) &#123;
    <span class="hljs-built_in">this</span>.microApp.mountPromise.then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.microApp.unmount()
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">prefetchApps(apps, importEntryOpts?)</h2>
<p>手动预加载指定的微应用静态资源。仅<code>手动加载</code>微应用场景需要，基于路由自动激活场景直接配置 prefetch 属性即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; prefetchApps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

prefetchApps([ &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'app1'</span>, <span class="hljs-attr">entry</span>: <span class="hljs-string">'//locahost:7001'</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>, <span class="hljs-attr">entry</span>: <span class="hljs-string">'//locahost:7002'</span> &#125; ])
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">主应用配置</h1>
<h2 data-id="heading-9">安装qiankun</h2>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm i qiankun -S <span class="hljs-comment"># 或者 yarn add qiankun</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">调整main.js</h2>
<p>如果你需要在项目初始化的时候就加载这些子应用，那么需要修改main.js的一些配置；如果是在页面中手动加载可略过此步。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>

<span class="hljs-keyword">import</span> &#123; registerMicroApps, setDefaultMountApp, start &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"qiankun"</span>
Vue.config.productionTip = <span class="hljs-literal">false</span>
<span class="hljs-keyword">let</span> app = <span class="hljs-literal">null</span>;
<span class="hljs-comment">/**
 * 渲染函数
 * appContent 子应用html内容
 * loading 子应用加载效果，可选
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">&#123; appContent, loading &#125; = &#123;&#125;</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!app) &#123;
        app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">"#container"</span>,
            router,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">content</span>: appContent,
                    loading
                &#125;;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
                <span class="hljs-keyword">return</span> h(App, &#123;
                    <span class="hljs-attr">props</span>: &#123;
                        <span class="hljs-attr">content</span>: <span class="hljs-built_in">this</span>.content,
                        <span class="hljs-attr">loading</span>: <span class="hljs-built_in">this</span>.loading
                    &#125;
                &#125;);
            &#125;
        &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
        app.content = appContent;
        app.loading = loading;
    &#125;
&#125;

<span class="hljs-comment">/**
 * 路由监听
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>routerPrefix 前缀
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genActiveRule</span>(<span class="hljs-params">routerPrefix</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">location</span> =></span> location.pathname.startsWith(routerPrefix);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initApp</span>(<span class="hljs-params"></span>) </span>&#123;
    render(&#123; <span class="hljs-attr">appContent</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">loading</span>: <span class="hljs-literal">true</span> &#125;);
&#125;

initApp();

<span class="hljs-comment">// 传入子应用的数据</span>
<span class="hljs-keyword">let</span> msg = &#123;
    <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">auth</span>: <span class="hljs-literal">false</span>
    &#125;,
    <span class="hljs-attr">fns</span>: [
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"_LOGIN"</span>,
            <span class="hljs-function"><span class="hljs-title">_LOGIN</span>(<span class="hljs-params">data</span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`父应用返回信息<span class="hljs-subst">$&#123;data&#125;</span>`</span>);
            &#125;
        &#125;
    ]
&#125;;

<span class="hljs-comment">// 注册子应用</span>
registerMicroApps(
    [
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"sub-app-1"</span>,
            <span class="hljs-attr">entry</span>: <span class="hljs-string">"//localhost:8091"</span>,
            render,
            <span class="hljs-attr">activeRule</span>: genActiveRule(<span class="hljs-string">"/app1"</span>),
            <span class="hljs-attr">props</span>: msg
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"sub-app-2"</span>,
            <span class="hljs-attr">entry</span>: <span class="hljs-string">"//localhost:8092"</span>,
            render,
            <span class="hljs-attr">activeRule</span>: genActiveRule(<span class="hljs-string">"/app2"</span>),
        &#125;
    ],
    &#123;
        <span class="hljs-attr">beforeLoad</span>: [
            <span class="hljs-function"><span class="hljs-params">app</span> =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before load"</span>, app);
            &#125;
        ], <span class="hljs-comment">// 挂载前回调</span>
        <span class="hljs-attr">beforeMount</span>: [
            <span class="hljs-function"><span class="hljs-params">app</span> =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before mount"</span>, app);
            &#125;
        ], <span class="hljs-comment">// 挂载后回调</span>
        <span class="hljs-attr">afterUnmount</span>: [
            <span class="hljs-function"><span class="hljs-params">app</span> =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after unload"</span>, app);
            &#125;
        ] <span class="hljs-comment">// 卸载后回调</span>
    &#125;
);

<span class="hljs-comment">// 设置默认子应用,与 genActiveRule中的参数保持一致</span>
setDefaultMountApp(<span class="hljs-string">"/app1"</span>);

<span class="hljs-comment">// 启动</span>
start();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">修改App.vue中的id 或 增加渲染子应用的盒子</h2>
<p>因为一个主应用可能会嵌套多个子应用，所以App.vue难免会重名，所以最好加一个自己项目名称的前缀来做区分。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"main-root"</span>></span>
    <span class="hljs-comment"><!-- loading --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"loading"</span>></span>loading<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 子应用盒子 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root-view"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app-view-box"</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">loading</span>: <span class="hljs-built_in">Boolean</span>,
    <span class="hljs-attr">content</span>: <span class="hljs-built_in">String</span>
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">配置vue子应用</h1>
<p>因为子应用本身就是一个单独的应用，所以不必安装qiankun，只需要暴露被当做子应用嵌入时，qiankun所需的3个生命周期即可。</p>
<h2 data-id="heading-13">配置maim.js</h2>
<p>在支持被当做子应用嵌入的同时，需要支持项目独立运行，兼容之前配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./public-path'</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> router = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> instance = <span class="hljs-literal">null</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
    router = <span class="hljs-keyword">new</span> VueRouter(&#123;
        <span class="hljs-attr">base</span>: <span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? <span class="hljs-string">'/app1'</span> : <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
        routes,
    &#125;);

    instance = <span class="hljs-keyword">new</span> Vue(&#123;
        router,
        <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
        beforeMount () &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
                routerPushFunc(<span class="hljs-built_in">this</span>)
                AppModule.SET_CURRENT_ENV()
            &#125;
        &#125;
    &#125;).$mount(container ? container.querySelector(<span class="hljs-string">'#templateConfig'</span>) : <span class="hljs-string">'#templateConfig'</span>);
&#125;

<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
    render();
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue app bootstraped'</span>);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'props from main app'</span>, props);
    render();
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;
    (instance <span class="hljs-keyword">as</span> Vue).$destroy();
    (instance <span class="hljs-keyword">as</span> Vue).$el.innerHTML = <span class="hljs-string">''</span>; <span class="hljs-comment">// 防止内存泄漏，子项目销毁时清空dom</span>
    instance = <span class="hljs-literal">null</span>;
    router = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">public-path.js</h2>
<p>使用 webpack 静态 publicPath 配置：可以通过两种方式设置，一种是直接在 mian.js 中引入 public-path.js 文件，一种是在开发环境直接修改 vue.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
  <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
  __webpack_public_path__ = <span class="hljs-built_in">window</span>.__INJECTED_PUBLIC_PATH_BY_QIANKUN__
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">配置 vue.config.js</h2>
<p>子应用必须支持跨域：由于 qiankun 是通过 fetch 去获取子应用的引入的静态资源的，所以必须要求这些静态资源支持跨域</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> &#123; name &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./package'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">dir</span>) </span>&#123;
    <span class="hljs-keyword">return</span> path.join(__dirname, dir);
&#125;

<span class="hljs-keyword">const</span> pagesMicro = &#123;
  <span class="hljs-attr">templateConfig</span>: &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/microPage/templateConfig/main.ts'</span>,
    <span class="hljs-attr">template</span>: <span class="hljs-string">'src/microPage/templateConfig/index.html'</span>,
    <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'runtime~templateConfig'</span>, <span class="hljs-string">'chunk-vendors'</span>, <span class="hljs-string">'chunk-common'</span>, <span class="hljs-string">'templateConfig'</span>]
  &#125;,
&#125;

<span class="hljs-keyword">const</span> pagesMain = &#123;
  <span class="hljs-attr">index</span>: &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/main.ts'</span>,
    <span class="hljs-attr">template</span>: <span class="hljs-string">'/index.html'</span>
  &#125;
&#125;

<span class="hljs-keyword">const</span> pages = process.env.VUE_APP_ENTRY === <span class="hljs-string">'main'</span> ? pagesMain : pagesMicro

<span class="hljs-keyword">let</span> config = &#123;
  <span class="hljs-comment">/**
   * You will need to set publicPath if you plan to deploy your site under a sub path,
   * for example GitHub Pages. If you plan to deploy your site to https://foo.github.io/bar/,
   * then publicPath should be set to "/bar/".
   * In most cases please use '/' !!!
   * Detail: https://cli.vuejs.org/config/#publicpath
   */</span>
    <span class="hljs-attr">outputDir</span>: <span class="hljs-string">'dist'</span>,
    <span class="hljs-attr">assetsDir</span>: <span class="hljs-string">'static'</span>,
    <span class="hljs-attr">filenameHashing</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// tweak internal webpack configuration.</span>
    <span class="hljs-comment">// see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md</span>
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-comment">// host: '0.0.0.0',</span>
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">disableHostCheck</span>: <span class="hljs-literal">true</span>,
        port,
        <span class="hljs-attr">overlay</span>: &#123;
            <span class="hljs-attr">warnings</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">errors</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-attr">headers</span>: &#123;
            <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'*'</span>,
        &#125;,
    &#125;,
    <span class="hljs-comment">// 自定义webpack配置</span>
    <span class="hljs-attr">configureWebpack</span>: &#123;
        <span class="hljs-attr">resolve</span>: &#123;
            <span class="hljs-attr">alias</span>: &#123;
                <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'src'</span>),
            &#125;,
        &#125;,
        <span class="hljs-attr">output</span>: &#123;
            <span class="hljs-comment">// 把子应用打包成 umd 库格式</span>
            <span class="hljs-attr">library</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>-[name]`</span>,
            <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>,
            <span class="hljs-attr">jsonpFunction</span>: <span class="hljs-string">`webpackJsonp_<span class="hljs-subst">$&#123;name&#125;</span>`</span>,
        &#125;,
    &#125;,
&#125;;

<span class="hljs-keyword">if</span> (process.env.VUE_APP_ENTRY === <span class="hljs-string">'micro'</span>) &#123;
  config.pages = pagesMicro
&#125;

<span class="hljs-built_in">module</span>.exports = config
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">qiankun常见问题及解决方案</h1>
<h2 data-id="heading-17">避免 css 污染</h2>
<p>qiankun 只能解决子项目之间的样式相互污染，不能解决子项目的样式污染主项目的样式，技术与规范方面大约有这 5 种方案：</p>
<ul>
<li>vue自带的scope
<ul>
<li>只能解决一部分页面内的样式污染，但一般不会有这个问题</li>
</ul>
</li>
<li>BEM命名方式</li>
<li>css-in-js
<ul>
<li>学习曲线高；可读性差；借助前端堆栈消耗性能；</li>
</ul>
</li>
<li>css-loader
<ul>
<li>开启css-modules，类似于图片懒加载，替换attr</li>
<li>缺点：页面中需要把class写成css-modules的形式；样式多了之后都是hash的形式可读性不高；</li>
</ul>
</li>
<li>postcss-loader
<ul>
<li>利用postcss-modules插件的getJson()函数将所有css文件中的class转为json对象；利用postcss-html把json对象渲染回html页面的class</li>
<li>缺点：利用新的gulp，意义不大；每次修改都要编译，很慢；</li>
</ul>
</li>
</ul>
<p><strong>拿css-loader举例，开启css-modules，可参考以下文章：</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F06%2Fcss_modules.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2016/06/css_modules.html" ref="nofollow noopener noreferrer">阮一峰的 CSS Modules 用法教程</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_26733915%2Farticle%2Fdetails%2F54313492" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_26733915/article/details/54313492" ref="nofollow noopener noreferrer">CSS Modules 基本用法</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_44869002%2Farticle%2Fdetails%2F105806021" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_44869002/article/details/105806021" ref="nofollow noopener noreferrer">浅谈CSS Modules以及CSS Modules在Vue.js上的使用</a></li>
<li><a href="https://juejin.cn/post/6844903748926439431" target="_blank" title="https://juejin.cn/post/6844903748926439431">css 命名：BEM, scoped css, css modules 与 css-in-js</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fcss.html%23%25E5%25BC%2595%25E7%2594%25A8%25E9%259D%2599%25E6%2580%2581%25E8%25B5%2584%25E6%25BA%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/css.html#%E5%BC%95%E7%94%A8%E9%9D%99%E6%80%81%E8%B5%84%E6%BA%90" ref="nofollow noopener noreferrer">Vue CLI 的 CSS相关配置</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack-contrib%2Fcss-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack-contrib/css-loader" ref="nofollow noopener noreferrer">css-loader 的 github</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcss-modules%2Fcss-modules" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/css-modules/css-modules" ref="nofollow noopener noreferrer">css-modules 的 github</a></li>
<li><a href="https://juejin.cn/post/6844903497532473352" target="_blank" title="https://juejin.cn/post/6844903497532473352">TypeScript 中使用 CSS Modules</a></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 省略其他配置</span>
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-comment">// 是否使用css分离插件 ExtractTextPlugin</span>
    <span class="hljs-attr">extract</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 开启 CSS source maps?</span>
    <span class="hljs-attr">sourceMap</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// css预设器配置项</span>
    <span class="hljs-attr">loaderOptions</span>: &#123;
      <span class="hljs-attr">css</span>: &#123;
        <span class="hljs-comment">// These properties are valid:</span>
        <span class="hljs-comment">// object &#123; url?, import?, modules?, sourceMap?, importLoaders?, localsConvention?, onlyLocals?, esModule? &#125;</span>
        <span class="hljs-attr">modules</span>: &#123;
          <span class="hljs-comment">// These properties are valid:</span>
          <span class="hljs-comment">// object &#123; auto?, mode?, exportGlobals?, localIdentName?, localIdentRegExp?, context?, hashPrefix?, getLocalIdent? &#125;</span>
          <span class="hljs-attr">exportGlobals</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">'[path][name]__[local]--[hash:base64:5]'</span>
        &#125;,
        <span class="hljs-attr">localsConvention</span>: <span class="hljs-string">'asIs'</span> <span class="hljs-comment">// asIs camelCase camelCaseOnly dashes dashesOnly</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 启用 CSS modules for all css / pre-processor files.</span>
    <span class="hljs-attr">requireModuleExtension</span>: <span class="hljs-literal">true</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">谨慎使用 position：fixed</h2>
<p>在子项目中这个定位会出现问题，基本出现在模态框和抽屉的定位上，应尽量避免使用，确有相对于浏览器窗口定位需求，可以用 <code>position: sticky</code>，但是会有兼容性问题（IE不支持）。如果定位使用的是 bottom 和 right，则问题不大。
还有个办法，位置可以写成动态绑定 style 的形式:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; top: isQiankun ? '10px' : '0'&#125;"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">给 body 、 document 等绑定的事件，请在 unmount 周期清除</h2>
<p>js 沙箱只劫持了 window.addEventListener，使用 document.body.addEventListener 或者 document.body.onClick 添加的事件并不会被沙箱移除，会对其他的页面产生影响，请在 unmount 周期清除</p>
<h2 data-id="heading-20">报错：Uncaught Error application 'xxx' died in status LOADING_SOURCE_CODE: [qiankun] You need to export lifecycle functions in xxx entry</h2>
<p>一般就是打包姿势不对，可能原因：未打包成umd格式；所需的js文件虽然被整体打包了但没被加载，需要利用runtimeChunk单独打包出来</p>
<h2 data-id="heading-21">现刷新页面报错，容器找不到</h2>
<p>解决方案1：在组件 mounted 周期注册并启动 qiankun</p>
<p>解决方案2：new Vue() 之后，等 DOM 加载好了再注册并启动 qiankun</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vueApp = <span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">"#app"</span>);
vueApp.$nextTick(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">//在这里注册并启动 qiankun</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">主、子应用的路由，均可用 history 模式</h2>
<p>因为vue-router的history模式是全匹配的，所以如果当前子应用是被qiankun嵌入时，需要在子应用的一级路由前加上主应用除了<code>http://ip+port/</code>后的所有路由，即在主应用中初始子应用是定义的<code>activeRule</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    <span class="hljs-attr">base</span>: <span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? <span class="hljs-string">'/templateConfig'</span> : <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    <span class="hljs-attr">routes</span>: [
        &#123; ... &#125;
    ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">history模式下，主、子应用的路由配置问题</h2>
<p>如果主、子应用的vue-router都是history模式（即路由全匹配）时</p>
<ul>
<li>主应用中的route信息的path属性需要改为'index/edit*'的形式，即模糊全匹配，而且子应用的跟路由需要改为'index/edit/'的形式（上面说过了）。否则子应用改变路由后，主应用匹配不到当前页面，则会跳回登录页会调至404。</li>
<li>子应用中的route信息里最好不要有''或者'*'之类的判空。否则主应用（从嵌入子应用的那个页面）跳转到其他页面后，会触发子应用的路由匹配规则，进而跳转至子应用的登录页，而且导致主应用的路由跳转失败（也不能叫失败，实际上是跳转出去了又被redirect重定向回来了）。</li>
</ul>
<h2 data-id="heading-24">从一个子项目跳转到另一个子项目</h2>
<p>在子项目里面如何跳转到另一个子项目/主项目页面呢，直接写  或者用 router.push/router.replace 是不行的，原因是这个 router 是子项目的路由，所有的跳转都会基于子项目的 base 。写 <a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"> 链接可以跳转过去，但是会刷新页面，用户体验不好。</a></p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">
<p>解决办法也比较简单，在子项目注册时将主项目的路由实例对象传过去，子项目挂载到全局，用父项目的这个 router 跳转就可以了。</p>
<p>但是有一丢丢不完美，这样只能通过 js 来跳转，跳转的链接无法使用浏览器自带的右键菜单</p>
<h2 data-id="heading-25">图片资源报错404</h2>
<p>最好改为绝对路径</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./img/logo.jpg"</span>></span>
<span class="hljs-comment"><!-- 改为 --></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/img/logo.jpg"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者在主应用中配置nginx静态文件的代理（这里没有后台的nginx配置，所以拿webpack自带的proxyTable代理作示例）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (item === <span class="hljs-string">'/index/config/template/edit/static'</span>) &#123; <span class="hljs-comment">// 登录页img</span>
    proxyObj[item] = &#123;
      <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:8081'</span>,
      <span class="hljs-attr">ws</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">pathRewrite</span>: &#123; <span class="hljs-string">'^/index/config/template/edit/static'</span>: <span class="hljs-string">'/static'</span> &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (item === <span class="hljs-string">'/static/home'</span>) &#123; <span class="hljs-comment">// 首页img</span>
    proxyObj[item] = &#123;
      <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:8081'</span>,
      <span class="hljs-attr">ws</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">pathRewrite</span>: &#123; <span class="hljs-string">'^/static/home'</span>: <span class="hljs-string">'/static/home'</span> &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">手动加载子应用时，如果子应用的js文件太大会造成阻塞</h2>
<p>如果是手动加载子应用，即loadMicroApp()，推荐在页面初始化的时候就预加载资源，即prefetchApps()。避免请求的pending时间太长阻塞加载</p>
<h2 data-id="heading-27">ts项目与js项目文件加载的问题</h2>
<p>因为主项目是ts，默认加载的是ts文件；但子项目是js。所以在子项目中引入js文件的时候要标清楚后缀名，例如</p>
<pre><code class="copyable">// 会报错  Unknown custom element: <widget> - did you register the component correctly? For recursive components, make sure to provide the "name" option.
import &#123;widgetInRecord as widget&#125; from '@/views/sheetConfig/fieldConfig/widget/widget'

// 加上后缀名就不报错了
import &#123;widgetInRecord as widget&#125; from '@/views/sheetConfig/fieldConfig/widget/widget.js'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">在一个页面内以不同的初始化数据加载同一子应用（如：左侧是列表，右侧的详情是qiankun嵌入的子应用）</h2>
<p>重复加载问题、数据通信问题、请求响应问题</p>
<pre><code class="copyable"><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">主项目与子项目的数据通信</h2>
<p>项目之间的不要有太多的数据依赖，毕竟项目还是要独立运行的。通信操作需要判断是否 qiankun 模式，做兼容处理。</p>
<p>通过 props 传递父项目的 Vuex ，如果子项目是 vue 技术栈，则会很好用。假如子项目是 jQuery/react/angular ，就不能很好的监听到数据的变化。</p>
<p>qiakun 提供了一个全局的 GlobalState 来共享数据。主项目初始化之后，子项目可以监听到这个数据的变化，也能提交这个数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主项目初始化</span>
<span class="hljs-keyword">import</span> &#123; initGlobalState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

<span class="hljs-keyword">const</span> actions = initGlobalState(state);

<span class="hljs-comment">// 主项目项目监听和修改</span>
actions.onGlobalStateChange(<span class="hljs-function">(<span class="hljs-params">state, prev</span>) =></span> &#123;
  <span class="hljs-comment">// state: 变更后的状态; prev 变更前的状态</span>
  <span class="hljs-built_in">console</span>.log(state, prev);
&#125;);

actions.setGlobalState(state);

<span class="hljs-comment">// 子项目监听和修改</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props</span>) </span>&#123;
  props.onGlobalStateChange(<span class="hljs-function">(<span class="hljs-params">state, prev</span>) =></span> &#123;
    <span class="hljs-comment">// state: 变更后的状态; prev 变更前的状态</span>
    <span class="hljs-built_in">console</span>.log(state, prev);
  &#125;);
  props.setGlobalState(state);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">vue子项目内存泄露问题</h2>
<p>这个问题挺难发现的，是在 qiankun 的 issue 区看到的: github.com/umijs/qiank… ，排查过程我就不发了，解决方案挺简单。</p>
<p>子项目销毁时清空 dom 即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;
  instance.$destroy();
+ instance.$el.innerHTML = <span class="hljs-string">""</span>; <span class="hljs-comment">//新增这一行代码</span>
  instance = <span class="hljs-literal">null</span>;
  router = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是其实，来回切换子项目并不会使内存不断增加。也就是说，即使卸载子项目时，子项目占用的内存没有被释放，但是下次加载时会复用这块内存，那这样的话，子项目会不会加载更快？（还未考证）</p>
<h2 data-id="heading-31">安全和性能的问题</h2>
<p>qiankun 将每个子项目的 js/css 文件内容都记录在一个全局变量中，如果子项目过多，或者文件体积很大，可能会导致内存占用过多，导致页面卡顿。</p>
</a><p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">另外，qiankun 运行子项目的 js，并不是通过 script 标签插入的，而是通过 eval 函数实现的，eval 函数的安全和性能是有一些争议的：</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2Feval" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/eval" ref="nofollow noopener noreferrer">MDN的eval介绍</a></p>
<h1 data-id="heading-32">祝君无Bug~</h1></div>  
</div>
            