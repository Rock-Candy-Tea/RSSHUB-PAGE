
---
title: '小程序动态tabBar菜单，根据条件渲染不同的tabBar'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e53380cd44e74742b479d1d415653b99~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:21:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e53380cd44e74742b479d1d415653b99~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>这次的项目需求是用户存在两种身份，普通用户和师傅用户，那么要根据不同的身份展示不同的tabBar菜单，看了下官方文档，难度不大，但是由于我用的框架是Taro，用官方文档的方法试了几次wxApi调不通就放弃了，转为JS通用大法写，但是配置方面还是得按照小程序文档来。</p>
<p><strong>做成效果</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e53380cd44e74742b479d1d415653b99~tplv-k3u1fbpfcp-zoom-1.image" alt="用户菜单" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dc5c11f13b0416aafdb37a82bccbf26~tplv-k3u1fbpfcp-zoom-1.image" alt="师傅菜单" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">说明</h2>
<p>此文是Taro版，非原生，思路可供参考，毕竟JS是互通的。</p>
<h2 data-id="heading-2">1. 配置信息</h2>
<ul>
<li>在 app.json 中的 tabBar 项指定 custom 字段，同时其余 tabBar 相关配置也补充完整。</li>
</ul>
<ul>
<li>所有 tab 页的 json 里需声明 usingComponents 项，也可以在 app.json 全局开启。</li>
</ul>
<p>由于Taro没有单目录json，所以只配了第一条就生效了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  tabBar: &#123;
      <span class="hljs-attr">custom</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">list</span>: [&#123;
        <span class="hljs-string">'pagePath'</span>: <span class="hljs-string">'pages/home/index'</span>,
        <span class="hljs-string">'text'</span>: <span class="hljs-string">'首页'</span>,
      &#125;, ...]
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2. 添加 tabBar 代码文件</h2>
<ul>
<li>在代码根目录下添加入口文件:</li>
</ul>
<pre><code class="copyable">  custom-tab-bar/index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此文件编写的组件会作为自定义的tabBar展示出来</p>
<h2 data-id="heading-4">主要步骤</h2>
<ol>
<li>custom-tab-bar/index.js里编写组件（此组件即是新的tabBar组件）</li>
<li>比如用户端有4个菜单，师傅端有3个菜单，这里我做好了标识type区分身份</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> nav = [&#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/home/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">1</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'首页'</span>,
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/user1/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">1</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'用户菜单1'</span>
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/user2/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">1</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'用户菜单2'</span>
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/user3/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">1</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'用户菜单3'</span>
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/masterhome/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">2</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'师傅首页'</span>
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/master1/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">2</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'师傅菜单1'</span>
    &#125;, &#123;
      <span class="hljs-string">'url'</span>: <span class="hljs-string">'/pages/master2/index'</span>,
      <span class="hljs-string">'type'</span>: <span class="hljs-number">2</span>,
      <span class="hljs-string">'text'</span>: <span class="hljs-string">'师傅菜单2'</span>
    &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>登录后拿到后端返回的身份信息，这里定义一个变量isMaster存储起来</li>
<li>然后在 custom-tab-bar/index.js里拿到isMaster，根据isMaster处理得到navList来渲染需要对应的tabBar 列表</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">const</span> navList = isMaster ? nav.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.type === <span class="hljs-number">2</span>) : data.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.type === <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>当isMaster 为true 时，tabBar显示</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c52f6fc089a14d6ab42501e2ac970a94~tplv-k3u1fbpfcp-zoom-1.image" alt="师傅菜单" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>当isMaster 为false 时，tabBar显示</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f061133f2c488bad10cb10b24c7701~tplv-k3u1fbpfcp-zoom-1.image" alt="用户菜单" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7315335578a84c928d8ce1f9f2139cce~tplv-k3u1fbpfcp-zoom-1.image" alt="觉得还不错记得点个赞，与君加油" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            