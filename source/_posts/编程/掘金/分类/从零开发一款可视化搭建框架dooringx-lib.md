
---
title: '从零开发一款可视化搭建框架dooringx-lib'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85b658a896c46afb042f64a622b347f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 18:00:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85b658a896c46afb042f64a622b347f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>dooringx演示地址: <a href="https://link.juejin.cn/?target=http%3A%2F%2Fx.dooring.cn" target="_blank" rel="nofollow noopener noreferrer" title="http://x.dooring.cn" ref="nofollow noopener noreferrer">dooringx可视化搭建平台</a> <br> 注: ⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<p>去年上线的可视化编辑器 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fh5.dooring.cn%2Fh5_plus" target="_blank" rel="nofollow noopener noreferrer" title="http://h5.dooring.cn/h5_plus" ref="nofollow noopener noreferrer"><strong>H5-dooring</strong></a> 至今已有一年的时间，期间有很多热心的网友和大佬提出了非常多宝贵的建议，我们也在一步步实现中，以下是几个比较典型的低代码可视化平台需求:</p>
<ul>
<li><strong>出码能力</strong>(即源码下载功能)</li>
<li><strong>组件交互</strong>(即组件支持业务中常用的链接跳转，弹窗交互，自定义事件等)</li>
<li><strong>数据源管理</strong>(即用户创建的不同页面拥有共享数据的能力，不同组件之间也有共享数据的能力)</li>
<li><strong>组件商店</strong>(即用户可以自主生产组件，定义组件，接入组件数据的能力)</li>
<li><strong>布局能力</strong>(即用户可以选择不同的布局方案来设计页面)</li>
<li><strong>常用功能集成</strong>(页面截图，微信分享，debug能力)</li>
</ul>
<p>上面的这些功需求已经在 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fh5.dooring.cn%2Fh5_plus" target="_blank" rel="nofollow noopener noreferrer" title="http://h5.dooring.cn/h5_plus" ref="nofollow noopener noreferrer"><strong>H5-dooring</strong></a> 陆续实现了，在我之前的文章中也有对应的技术分享。但是为了让更多的人能低成本的拥有自己的可视化搭建系统，我们团队的大佬花了非常多的时间研究和沉淀，最近也开源了一款可视化搭建框架 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fdooringx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/dooringx" ref="nofollow noopener noreferrer"><strong>dooringx-lib</strong></a>，我们可以基于它轻松制作可视化编辑器，而无需考虑内部的实现细节，接下来我就和大家分享一下这款可视化框架的使用方式和实现思路，同时也非常感谢 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring" ref="nofollow noopener noreferrer"><strong>dooring可视化团队</strong></a> 各位大佬们的辛勤付出。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85b658a896c46afb042f64a622b347f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">可视化搭建框架基本使用和技术实现</h2>
<p>为了让大家更好的理解可视化搭建框架，我这里举几个形象的例子:</p>
<ol>
<li><strong>antd</strong> —— <strong>antd-pro</strong></li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96d9d90953dc40dfb496dc12bcfd6d6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们都知道 <strong>antd</strong> 是流行的前端组件库，那么基于它上层封装的管理后台 <strong>antd-pro</strong> 就是它的上层应用。</p>
<ol start="2">
<li><strong>GrapesJS</strong> —— <strong>craft.js</strong></li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16c4ed95ad04409c80ef755e5828a4ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>GrapesJS</strong> 是一款国外的页面编辑器框架(详细介绍可参考我之前的文章 <a href="https://juejin.cn/post/6994335252508311565" target="_blank" title="https://juejin.cn/post/6994335252508311565">这款国外开源框架, 让你轻松构建自己的页面编辑器</a>) ，那么 <strong>craft.js</strong> 就是它的上层应用框架。</p>
<ol start="3">
<li><strong>dooringx-lib</strong> —— <strong>dooringx</strong></li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42f9050035c54f80919b90f8c47da3f8~tplv-k3u1fbpfcp-watermark.image" alt="chrome-capture.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>dooringx-lib</strong> 是一款可视化搭建框架，同理 <strong>dooringx</strong> 就是基于 <strong>dooringx-lib</strong> 的可视化编辑器。</p>
<p>之所以要介绍它们的区别，是因为之前有很多朋友对这块概念理解的不是很清晰，在了解了<strong>可视化搭建框架</strong> 的 “内涵” 之后，我们开始今天的核心内容。</p>
<h3 data-id="heading-1">1.技术栈</h3>
<p>在分享框架实现思路之前当然要自报家门，框架实现上我们还是采用熟悉的 <strong>React</strong> 生态，移动端组件库采用的众安团队的 <strong>zarm</strong>，编辑器应用层采用的 <strong>antd</strong>，至于其他的比如<strong>拖拽</strong>，<strong>参考线</strong>，<strong>状态管理</strong>，<strong>插件机制</strong>等都是我们团队大佬自研的方案。如果你是 <strong>vue</strong> 或者其他技术栈为主的团队，也可以参考实现思路，相信也会对你有一定的启发。</p>
<h3 data-id="heading-2">2.基本使用方式</h3>
<p>在开始深入之前我们先看看如何使用这款框架，我们只需要按照如下方式即可安装使用:</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm/yarn  install dooringx-lib
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时我们还提供了基础的使用demo，方便大家在自己的工程中快速上手:</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 克隆项目</span>
<span class="hljs-comment"># cnpmjs</span>
git <span class="hljs-built_in">clone</span> https://github.com.cnpmjs.org/H5-Dooring/dooringx.git

<span class="hljs-comment"># or</span>
git <span class="hljs-built_in">clone</span> https://github.com/H5-Dooring/dooringx.git


<span class="hljs-comment"># 进入项目目录</span>
<span class="hljs-built_in">cd</span> dooringx

<span class="hljs-comment"># 安装依赖</span>
yarn install

<span class="hljs-comment"># 启动基础示例</span>
yarn start:example

<span class="hljs-comment"># 启动 dooringx-lib</span>
yarn start

<span class="hljs-comment"># 启动 dooringx doc 文档</span>
yarn start:doc

yarn build
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>demo</strong> 的 <strong>github</strong> 项目如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97baea81b0334f2e9d0e1eac3b8b0009~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>github地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fdooringx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/dooringx" ref="nofollow noopener noreferrer">github.com/H5-Dooring/…</a></p>
<p>在了解完使用方式之后，我们来看看基本架构和实现思路。</p>
<h3 data-id="heading-3">3.dooringx-lib基础架构和工作机制</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5b30e8590614803af0961c29a3cfa03~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图就是我根据目前 <strong>dooringx-lib</strong> 的项目架构梳理的架构图，基本包含了搭建化编辑框架的大部分必备模块。为了保证框架的灵活性，我们还可以按需安装对应的功能组件，开发自定义的组件等。如下是一个基本的导入案例:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
    RightConfig,
    Container,
    useStoreState,
    innerContainerDragUp,
    LeftConfig,
    ContainerWrapper,
    Control,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dooringx-lib'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将整个框架拆分成了不同的模块，这些模块既相互独立又可以相互关联。完整的工作流程如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e999388399194dcf842fa4ec8089ea74~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可以看出，我们只需要拥有基础的业务研发能力，就可以借助 <strong>dooringx-lib</strong> 构建一个属于自己的搭建平台，就好比任何程序的本质: <strong>数据</strong>和<strong>逻辑</strong>。</p>
<h3 data-id="heading-4">4.dooringx-lib插件开发</h3>
<p>接下来我会和大家分享 <strong>dooringx-lib</strong> 的插件开发方式和具体实现(如何导入插件，如何编写组件，如何注册函数等)，如果大家感兴趣的话也可以跟着下面的方式实践一下。</p>
<h4 data-id="heading-5">4.1 如何导入组件</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c86c86f65f7d472c9394a92904ea9196~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们在上图可以看到左侧是我们的组件物料区，分为<strong>基础组件</strong>，<strong>媒体组件</strong>，<strong>可视化组件</strong>，它们的添加会统一放在 <strong>LeftRegistMap</strong> 数组中来管理，其基本结构如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> LeftRegistMap: LeftRegistComponentMapItem[] = [
  &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'basic'</span>, <span class="hljs-comment">// 组件类别</span>
      <span class="hljs-attr">component</span>: <span class="hljs-string">'button'</span>, <span class="hljs-comment">// 组件名称</span>
      <span class="hljs-attr">img</span>: <span class="hljs-string">'icon-anniu'</span>, <span class="hljs-comment">// 组件icon</span>
      <span class="hljs-attr">displayName</span>: <span class="hljs-string">'按钮'</span>, <span class="hljs-comment">// 组件中文名</span>
      <span class="hljs-attr">urlFn</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./registComponents/button'</span>),  <span class="hljs-comment">// 注册回调</span>
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>左侧组件支持同步导入或者异步导入。</p>
<p>如果需要异步导入组件，则需要填写 <strong>urlFn</strong>，需要一个返回 <strong>promise</strong> 的函数。也可以支持远程载入组件，只要 <strong>webpack</strong> 配上即可。</p>
<p>如果需要同步导入组件，则需要将组件放入配置项的 <strong>initComponentCache</strong> 中，这样在载入时便会注册进 <strong>componentRegister</strong> 里。</p>
<pre><code class="hljs language-js copyable" lang="js">initComponentCache: &#123;
  <span class="hljs-attr">modalMask</span>: &#123; <span class="hljs-attr">component</span>: MmodalMask &#125;,  
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">4.2 如何定制左侧面板</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d678455db7144830960e9c68470f6dcb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>左侧面板传入 <strong>leftRenderListCategory</strong> 即可。</p>
<pre><code class="hljs language-js copyable" lang="js">leftRenderListCategory: [
  &#123;
<span class="hljs-attr">type</span>: <span class="hljs-string">'basic'</span>,
<span class="hljs-attr">icon</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">HighlightOutlined</span> /></span></span>,
displayName: <span class="hljs-string">'基础组件'</span>,
  &#125;,
  &#123;
<span class="hljs-attr">type</span>: <span class="hljs-string">'xxc'</span>,
<span class="hljs-attr">icon</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ContainerOutlined</span> /></span></span>,
custom: <span class="hljs-literal">true</span>,
<span class="hljs-attr">customRender</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是自定义渲染<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>,
  &#125;,
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>type</strong> 是分类，左侧组件显示在哪个分类由该字段决定。<strong>icon</strong> 则是左侧分类小图标(如上图所示)。当 <strong>custom</strong> 为 <strong>true</strong> 时，可以使用 <strong>customRender</strong> 自定义渲染。</p>
<h4 data-id="heading-7">4.3 开发一个自定义的可视化组件</h4>
<p>组件需要导出一个由 <strong>ComponentItemFactory</strong> 生成的对象:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MButton = <span class="hljs-keyword">new</span> ComponentItemFactory(
<span class="hljs-string">'button'</span>,
<span class="hljs-string">'按钮'</span>,
&#123;
<span class="hljs-attr">style</span>: [
createPannelOptions<FormMap, <span class="hljs-string">'input'</span>>(<span class="hljs-string">'input'</span>, &#123;
<span class="hljs-attr">receive</span>: <span class="hljs-string">'text'</span>, 
<span class="hljs-attr">label</span>: <span class="hljs-string">'文字'</span>,
&#125;),
],
<span class="hljs-attr">animate</span>: [createPannelOptions<FormMap, <span class="hljs-string">'animateControl'</span>>(<span class="hljs-string">'animateControl'</span>, &#123;&#125;)],
<span class="hljs-attr">actions</span>: [createPannelOptions<FormMap, <span class="hljs-string">'actionButton'</span>>(<span class="hljs-string">'actionButton'</span>, &#123;&#125;)],
&#125;,
&#123;
<span class="hljs-attr">props</span>: &#123;
...
<span class="hljs-attr">text</span>:<span class="hljs-string">'x.dooring'</span><span class="hljs-comment">// input配置项组件接收的初始值</span>
&#125;,
&#125;,
<span class="hljs-function">(<span class="hljs-params">data, context, store, config</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ButtonTemp</span> <span class="hljs-attr">data</span>=<span class="hljs-string">&#123;data&#125;</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span> <span class="hljs-attr">context</span>=<span class="hljs-string">&#123;context&#125;</span> <span class="hljs-attr">config</span>=<span class="hljs-string">&#123;config&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">ButtonTemp</span>></span></span>;
&#125;,
<span class="hljs-literal">true</span>
);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MButton;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中第一个参数为组件注册名，第二个参数用来展示使用。</p>
<p>第三个参数用来配置右侧面板的配置项组件。其中键为右侧面板的分类，值为配置项组件数组。</p>
<p>第四个参数会配置组件的初始值，特别注意的是，制作组件必须要有初始宽度高度（非由内容撑开），否则会在适配时全选时产生问题。</p>
<p>这个初始值里有很多有用的属性，比如fixed代表使用固定定位，可以结合配置项更改该值，使得组件可以fixed定位。</p>
<p>还有 <strong>canDrag</strong> 类似于锁定命令，锁定的元素不可拖拽。</p>
<p>初始值里的 <strong>rotate</strong> 需要个对象，<strong>value</strong> 代表旋转角度，<strong>canRotate</strong> 代表是否可以操作旋转。（0.7.0版本开始支持）</p>
<p>第五个参数是个函数，你将获得配置项中的 <strong>receive</strong> 属性（暂且都默认该配置为<strong>receive</strong>）传来的配置，比如上例中 <strong>receive</strong> 的是 <strong>text</strong>，则该函数中 <strong>data</strong> 里会收到该字段。</p>
<p><strong>context</strong> 一般只有 <strong>preview</strong> 和 <strong>edit</strong>，用来进行环境判断。</p>
<p><strong>config</strong> 可以拿到所有数据，用来制作事件时使用。</p>
<p>第六个参数 <strong>resize</strong> 是为了判断是否能进行缩放，当为 <strong>false</strong> 时，无法进行缩放。</p>
<p>第七个参数 <strong>needPosition</strong>，某些组件移入画布后会默认采取拖拽的落点，该配置项默认为 <strong>true</strong>, 就是需要拖拽的位置，为 <strong>false</strong> 时将使用组件自身 <strong>top</strong> 和 <strong>left</strong> 定位来放置。</p>
<h4 data-id="heading-8">4.4 事件注册</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7855ffac84a43c39478522c06cf755c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>注册时机</li>
</ol>
<p>事件可以细分为 <strong>注册时机</strong> 和 <strong>函数</strong>，组件内可以通过 <strong>hook</strong> 的方式来实现注册时机：</p>
<pre><code class="hljs language-js copyable" lang="js">useDynamicAddEventCenter(pr, <span class="hljs-string">`<span class="hljs-subst">$&#123;pr.data.id&#125;</span>-init`</span>, <span class="hljs-string">'初始渲染时机'</span>); <span class="hljs-comment">//注册名必须带id 约定！</span>
useDynamicAddEventCenter(pr, <span class="hljs-string">`<span class="hljs-subst">$&#123;pr.data.id&#125;</span>-click`</span>, <span class="hljs-string">'点击执行时机'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>useDynamicAddEventCenter</strong> 第一个参数是 <strong>render</strong> 的四个参数组成的对象。第二个参数是注册的时机名，必须跟 <strong>id</strong> 相关，这是约定，否则多个组件可能会导致名称冲突，并且方便查找该时机。</p>
<p>注册完时机后，我们需要将时机放入对应的触发位置上，比如这个 <strong>button</strong> 的点击执行时机就放到 <strong>onclick</strong> 中：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Button</span>
    <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
eventCenter.runEventQueue(`$&#123;pr.data.id&#125;-click`, pr.config);
    &#125;&#125;
>
    x.dooring
<span class="hljs-tag"></<span class="hljs-name">Button</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中第一个参数则为注册的时机名，第二个为 <strong>render</strong> 函数中最后一个参数 <strong>config</strong></p>
<ol start="2">
<li>函数注册</li>
</ol>
<p>函数由组件抛出，可以加载到事件链上。比如，注册个改变文本函数，那么我可以在任意组件的时机中去调用该函数，从而触发该组件改变文本。</p>
<p>函数注册需要放入 <strong>useEffect</strong> 中，在组件卸载时需要卸载函数！否则会导致函数越来越多。</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> functionCenter = eventCenter.getFunctionCenter();
<span class="hljs-keyword">const</span> unregist = functionCenter.register(
<span class="hljs-string">`<span class="hljs-subst">$&#123;pr.data.id&#125;</span>+改变文本函数`</span>,
<span class="hljs-keyword">async</span> (ctx, next, config, args, _eventList, iname) => &#123;
<span class="hljs-keyword">const</span> userSelect = iname.data;
<span class="hljs-keyword">const</span> ctxVal = changeUserValue(
userSelect[<span class="hljs-string">'改变文本数据源'</span>],
args,
<span class="hljs-string">'_changeval'</span>,
config,
ctx
);
<span class="hljs-keyword">const</span> text = ctxVal[<span class="hljs-number">0</span>];
setText(text);
next();
&#125;,
[
&#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'改变文本数据源'</span>,
<span class="hljs-attr">data</span>: [<span class="hljs-string">'ctx'</span>, <span class="hljs-string">'input'</span>, <span class="hljs-string">'dataSource'</span>],
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">receive</span>: <span class="hljs-string">'_changeval'</span>,
<span class="hljs-attr">multi</span>: <span class="hljs-literal">false</span>,
&#125;,
&#125;,
]
);
<span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
unregist();
&#125;;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数中参数与配置见后面的函数开发。</p>
<h4 data-id="heading-9">4.5 右侧面板开发</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93d3f6c00b9445698c0c757702d9099c~tplv-k3u1fbpfcp-watermark.image" alt="chrome-capture (2).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了开发自定义的右侧属性面板，我们只要将开发的组件配成一个对象放入 <strong>initFormComponents</strong> 即可。为了良好的开发体验，需要定义个 <strong>formMap</strong> 类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FormBaseType &#123;
    receive?: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FormInputType <span class="hljs-keyword">extends</span> FormBaseType &#123;
    <span class="hljs-attr">label</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FormActionButtonType &#123;&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FormAnimateControlType &#123;&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> FormMap &#123;
    <span class="hljs-attr">input</span>: FormInputType;
    actionButton: FormActionButtonType;
    animateControl: FormAnimateControlType;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>formMap</strong> 的键名就是 <strong>initFormComponents</strong> 键名，<strong>formMap</strong> 的值对应组件需要收到的值。</p>
<p>以 <strong>input</strong> 组件为例，<strong>FormInputType</strong> 此时有2个属性: <strong>label</strong>, <strong>receive</strong>。</p>
<p>那么在开发该组件时，<strong>props</strong> 会收到：</p>
<pre><code class="hljs language-js copyable" lang="js">interface MInputProps &#123;
    <span class="hljs-attr">data</span>: CreateOptionsRes<FormMap, <span class="hljs-string">'input'</span>>;
    current: IBlockType;
    config: UserConfig;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是 <strong>data</strong> 是 <strong>formMap</strong> 类型，而 <strong>current</strong> 是当前点击的组件，<strong>config</strong> 就不用说了。</p>
<p>还记得在左侧组件开发中的第三个参数吗？这样就都关联起来了：</p>
<pre><code class="hljs language-js copyable" lang="js">style: [
    createPannelOptions<FormMap, <span class="hljs-string">'input'</span>>(<span class="hljs-string">'input'</span>, &#123;
        <span class="hljs-attr">receive</span>: <span class="hljs-string">'text'</span>,  
        <span class="hljs-attr">label</span>: <span class="hljs-string">'文字'</span>
    &#125;)
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>createPannelOptions</strong> 这个函数的泛型里填入对应的组件，将会给收到的配置项良好的提示。</p>
<p>在配置项组件里所要做的就是接收组件传来的配置项，然后去修改 <strong>current</strong> 的属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MInput</span>(<span class="hljs-params">props: MInputProps</span>) </span>&#123;
<span class="hljs-keyword">const</span> option = useMemo(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">return</span> props.data?.option || &#123;&#125;;
&#125;, [props.data]);
<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Row</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">padding:</span> '<span class="hljs-attr">10px</span> <span class="hljs-attr">20px</span>' &#125;&#125;></span>
<span class="hljs-tag"><<span class="hljs-name">Col</span> <span class="hljs-attr">span</span>=<span class="hljs-string">&#123;6&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">lineHeight:</span> '<span class="hljs-attr">30px</span>' &#125;&#125;></span>
&#123;(option as any)?.label || '文字'&#125;：
<span class="hljs-tag"></<span class="hljs-name">Col</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Col</span> <span class="hljs-attr">span</span>=<span class="hljs-string">&#123;18&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Input</span>
                <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;props.current.props[(option</span> <span class="hljs-attr">as</span> <span class="hljs-attr">any</span>)<span class="hljs-attr">.receive</span>] || ''&#125;
                <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> &#123;
                        const receive = (option as any).receive;
                        const clonedata = deepCopy(store.getData());
                        const newblock = clonedata.block.map((v: IBlockType) => &#123;
                                if (v.id === props.current.id) &#123;
                                        v.props[receive] = e.target.value;
                                &#125;
                                return v;
                        &#125;);
                        store.setData(&#123; ...clonedata, block: [...newblock] &#125;);
                &#125;&#125;
            ><span class="hljs-tag"></<span class="hljs-name">Input</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Col</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Row</span>></span></span>
);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于可以很轻松的拿到 <strong>store</strong>，所以可以在任意地方进行修改数据。</p>
<p>将组件的 <strong>value</strong> 关联 <strong>current</strong> 的属性，<strong>onChange</strong> 去修改 <strong>store</strong>，这样就完成了个双向绑定。</p>
<p>注意：如果你的右侧组件需要用到 <strong>block</strong> 以外的属性，可能需要去判断是否处于弹窗模式。</p>
<h4 data-id="heading-10">4.6 自定义右键菜单</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5f48b994d594b3693c727c2dd59dfe8~tplv-k3u1fbpfcp-watermark.image" alt="chrome-capture (3).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>右键菜单可以进行自定义：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 自定义右键</span>
<span class="hljs-keyword">const</span> contextMenuState = config.getContextMenuState();
<span class="hljs-keyword">const</span> unmountContextMenu = contextMenuState.unmountContextMenu;
<span class="hljs-keyword">const</span> commander = config.getCommanderRegister();
<span class="hljs-keyword">const</span> ContextMenu = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> handleclick = <span class="hljs-function">() =></span> &#123;
unmountContextMenu();
&#125;;
<span class="hljs-keyword">const</span> forceUpdate = useState(<span class="hljs-number">0</span>)[<span class="hljs-number">1</span>];
contextMenuState.forceUpdate = <span class="hljs-function">() =></span> &#123;
forceUpdate(<span class="hljs-function">(<span class="hljs-params">pre</span>) =></span> pre + <span class="hljs-number">1</span>);
&#125;;
<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
<span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
            <span class="hljs-attr">left:</span> <span class="hljs-attr">contextMenuState.left</span>,
            <span class="hljs-attr">top:</span> <span class="hljs-attr">contextMenuState.top</span>,
            <span class="hljs-attr">position:</span> '<span class="hljs-attr">fixed</span>',
            <span class="hljs-attr">background:</span> '<span class="hljs-attr">rgb</span>(<span class="hljs-attr">24</span>, <span class="hljs-attr">23</span>, <span class="hljs-attr">23</span>)',
&#125;&#125;
></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> '<span class="hljs-attr">100</span>%' &#125;&#125;
            <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
                    commander.exec('redo');
                    handleclick();
            &#125;&#125;
        >
            <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>自定义<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
);
&#125;;
contextMenuState.contextMenu = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ContextMenu</span>></span><span class="hljs-tag"></<span class="hljs-name">ContextMenu</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先拿到 <strong>contextMenuState</strong>，<strong>contextMenuState</strong> 上有个 <strong>unmountContextMenu</strong> 是关闭右键菜单方法。所以在点击后需要调用关闭。同时上面的 <strong>left</strong> 和 <strong>top</strong> 是右键的位置。另外，我们还需要在组件内增加强刷，赋值给 <strong>forceUpdate</strong>，用于在组件移动时进行跟随。</p>
<h4 data-id="heading-11">4.7 表单验证提交思路</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b29a21055e8b42f2ba61c62c2faa1963~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>表单验证提交有非常多的做法，因为数据全部是联通的，或者直接写个表单组件也可以。在不使用表单组件时，简单的做法是为每个输入组件做个验证函数与提交函数。这样是否验证就取决于用户的选取，而抛出的输入可以让用户选择放到哪，并由用户去命名变量。</p>
<p>在点击提交按钮时，调用所有组件的验证函数与提交函数，使其抛给上下文，再通过上下文聚合函数聚合成对象，最后可以通过发送函数发送给对应后端，从而完成整个流程。我们可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fdooringx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/dooringx" ref="nofollow noopener noreferrer"><strong>dooringx</strong></a> 中试下这个<strong>demo</strong>。</p>
<p>另一种方式是可以专门写个提交按钮，固定了参数，以及部分规则，比如规定在页面中的所有表单都会被收集提交。</p>
<p>那么我们可以利用数据源，将所有表单输出内容自动提交给数据源，最后的提交按钮按数据源规定格式的<strong>key</strong> 提取，发送给后端。</p>
<h2 data-id="heading-12">后期规划</h2>
<p>后期我们还会在产品功能方面持续迭代优化，如果大家有好的建议, 也可以随时和我们交流, 也欢迎在 github 上积极提 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fdooringx%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/dooringx/issues" ref="nofollow noopener noreferrer"><strong>issue</strong></a>。</p>
<p>如果大家对可视化搭建或者低代码/零代码感兴趣，也可以参考我往期的文章或者在评论区交流你的想法和心得，欢迎一起探索前端真正的技术。</p>
<blockquote>
<p>github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fdooringx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/dooringx" ref="nofollow noopener noreferrer">dooringx | 快速高效搭建可视化拖拽平台</a> <br> 首发：<a href="https://juejin.cn/" target="_blank" title="https://juejin.cn">掘金技术社区</a> <br> 团队：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring" ref="nofollow noopener noreferrer">Dooring可视化团队</a><br> 专栏：<a href="https://juejin.cn/column/6963455443528056839" target="_blank" title="https://juejin.cn/column/6963455443528056839">低代码可视化</a> <br> 公众号: 趣谈前端</p>
</blockquote>
<h2 data-id="heading-13">更多推荐</h2>
<ul>
<li><a href="https://juejin.cn/post/6986824393653485605" target="_blank" title="https://juejin.cn/post/6986824393653485605">如何设计可视化搭建平台的组件商店？</a></li>
<li><a href="https://juejin.cn/post/6981257575425654792" target="_blank" title="https://juejin.cn/post/6981257575425654792">从零设计可视化大屏搭建引擎</a></li>
<li><a href="https://juejin.cn/post/6976476731662139428" target="_blank" title="https://juejin.cn/post/6976476731662139428">从零使用electron搭建桌面端可视化编辑器Dooring</a></li>
<li><a href="https://juejin.cn/post/6973946702235615269" target="_blank" title="https://juejin.cn/post/6973946702235615269">(低代码)可视化搭建平台数据源设计剖析</a></li>
<li><a href="https://juejin.cn/post/6950075140906418213" target="_blank" title="https://juejin.cn/post/6950075140906418213">从零搭建一款PC页面编辑器PC-Dooring</a></li>
<li><a href="https://juejin.cn/post/6904878119724056584" target="_blank" title="https://juejin.cn/post/6904878119724056584">如何搭积木式的快速开发H5页面?</a></li>
</ul></div>  
</div>
            