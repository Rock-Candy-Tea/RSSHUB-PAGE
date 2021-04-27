
---
title: '【DoKit&北大专题】-DoKit For 小程序源码分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12247d5492db4973825666efa58cbf61~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 01:29:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12247d5492db4973825666efa58cbf61~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">专题背景</h1>
<blockquote>
<p>近几年随着开源在国内的蓬勃发展，一些高校也开始探索让开源走进校园，让同学们在学生时期就感受到开源的魅力，这也是高校和国内的头部互联网企业共同尝试的全新教学模式。本专题会记录这段时间内学生们的学习成果。</p>
<p>更多专题背景参考:<a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
</blockquote>
<h1 data-id="heading-1">系列文章</h1>
<p><a href="https://juejin.cn/post/6948247882172629005" target="_blank">【DoKit&北大专题】缘起</a></p>
<p><a href="https://juejin.cn/post/6948257290654842916" target="_blank">【DoKit&北大专题】-读小程序源代码（一）</a></p>
<p><a href="https://juejin.cn/post/6948300642767077412" target="_blank">【DoKit&北大专题】-读小程序源代码（二）</a></p>
<p><a href="https://juejin.cn/post/6955347254567764005/" target="_blank">【DoKit&北大专题】-读小程序源代码（三）</a></p>
<p><a href="https://juejin.cn/post/6955363977404612621/" target="_blank">【DoKit&北大专题】-实现DoKit For Web请求捕获工具（一）产品调研</a></p>
<p><strong><a href="https://juejin.cn/post/6955767193929777182/" target="_blank">【DoKit&北大专题】-DoKit For 小程序源码分析</a></strong></p>
<h1 data-id="heading-2">原文</h1>
<h2 data-id="heading-3">DoKit简介</h2>
<p>DoKit是一款面向泛前端产品研发全生命周期的效率平台，其作为DiDi旗下Stars最多的项目，现已拥有17k+Stars。<a href="https://github.com/didi/DoraemonKit" target="_blank" rel="nofollow noopener noreferrer">Github地址</a>
本文的目的是对DoKit小程序方向的源码进行分析。</p>
<h2 data-id="heading-4">项目引入及使用</h2>
<p><a href="https://github.com/didi/DoraemonKit/tree/master/miniapp" target="_blank" rel="nofollow noopener noreferrer">快速上手</a>
<a href="https://www.dokit.cn/#/index/home" target="_blank" rel="nofollow noopener noreferrer">Mock平台</a>
注意：读源码或对DoKit进行开发时用的是src/，使用DoKit时应该引入dist/
src和dist目录的区别：src是源代码，dist是将src里的js文件打包输出后的</p>
<h2 data-id="heading-5">写在前面</h2>
<p>关于<code>DoKit for miniapp</code>的整体设计思想，在这里放两张DoKit老师们的PPT。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12247d5492db4973825666efa58cbf61~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a65f6f11c28a44bd9816e8fa96141f3a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我觉得“在框架中跳舞”这句话描述得非常恰当，小程序依托于微信客户端，在开发过程中有着诸多限制，如果想要开发一些辅助功能，大概率是通过对微信小程序官方API进行一定的改造来实现，下文对源码的分析中也一直在体现这种思想。</p>
<h2 data-id="heading-6">DoKit项目结构</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d0d3b60b2d54dfd94a85586885f83b3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">``</p>
<blockquote>
<p><code>assets</code> ——资源文件夹，目前存放了一些图标文件
<code>components</code> ——Dokit最核心的部分，包括了八个自定义组件</p>
<ol>
<li>apimock —— 数据Mock功能组件</li>
<li>appinformation —— App信息查看功能组件</li>
<li>back —— 用来返回的自定义组件，该组件并不是Dokit的功能组件，在其他功能页面通过该组件进行返回</li>
<li>debug —— 主菜单组件，罗列了Dokit的各种功能</li>
<li>h5door —— h5任意门功能组件</li>
<li>httpinjector ——请求注射功能组件</li>
<li>positionsimulation —— 位置模拟功能组件</li>
<li>storage —— 存储管理功能组件</li>
</ol>
</blockquote>
<p><code>index</code> —— Dokit入口的自定义组件，将Dokit引入项目中时，就是在目标page页面中引入这个component</p>
<blockquote>
<p><code>logs</code> —— 与微信小程序样例项目中的<code>logs内容</code>相同，貌似没什么用
<code>utils</code> —— <code>imgbase64.js</code>将Dokit各种图标转换成base64格式；<code>util.js</code>内存储了一些常用工具函数，包括时间输出、跳转页面、深拷贝等</p>
</blockquote>
<blockquote>
<p>参考文章：<a href="https://juejin.cn/post/6948076833673838600" target="_blank">juejin.cn/post/694807…</a>，亦庄亦谐</p>
</blockquote>
<h2 data-id="heading-7">index组件</h2>
<p>DoKit工具集的入口，该组件起到一个外壳的作用，其他功能组件就是展示在index组件页面上的。</p>
<h2 data-id="heading-8">代码分析</h2>
<ul>
<li>index.json</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"component"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"navigationBarTitleText"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"usingComponents"</span>: &#123;
    <span class="hljs-attr">"debug"</span>: <span class="hljs-string">"../components/debug/debug"</span>,
    <span class="hljs-attr">"appinformation"</span>: <span class="hljs-string">"../components/appinformation/appinformation"</span>,
    <span class="hljs-attr">"positionsimulation"</span>: <span class="hljs-string">"../components/positionsimulation/positionsimulation"</span>,
    <span class="hljs-attr">"storage"</span>: <span class="hljs-string">"../components/storage/storage"</span>,
    <span class="hljs-attr">"h5door"</span>: <span class="hljs-string">"../components/h5door/h5door"</span>,
    <span class="hljs-attr">"httpinjector"</span>: <span class="hljs-string">"../components/httpinjector/httpinjector"</span>,
    <span class="hljs-attr">"apimock"</span>: <span class="hljs-string">"../components/apimock/apimock"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见index本身是一个自定义组件，同时引入了DoKit所有其他的功能组件
什么是自定义组件？</p>
<blockquote>
<p>开发者可以将页面内的功能模块抽象成自定义组件，以便在不同的页面中重复使用；也可以将复杂的页面拆分成多个低耦合的模块，有助于代码维护。自定义组件在使用时与基础组件非常相似。</p>
</blockquote>
<ul>
<li>index.wxml</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">block</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom!= 'dokit' &#125;&#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">debug</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'debug' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">debug</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">appinformation</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'appinformation' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">appinformation</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">positionsimulation</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'positionsimulation' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">positionsimulation</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">storage</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'storage' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">storage</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h5door</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'h5door' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">h5door</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">httpinjector</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'httpinjector' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">httpinjector</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">apimock</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'apimock' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span> <span class="hljs-attr">projectId</span>=<span class="hljs-string">"&#123;&#123; projectId &#125;&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">apimock</span>></span>
<span class="hljs-tag"></<span class="hljs-name">block</span>></span>
<span class="hljs-tag"><<span class="hljs-name">block</span> <span class="hljs-attr">wx:else</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">cover-image</span>
        <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"tooggleComponent"</span>
        <span class="hljs-attr">data-type</span>=<span class="hljs-string">"debug"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-entrance"</span>
        <span class="hljs-attr">src</span>=<span class="hljs-string">"//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">cover-image</span>></span>
<span class="hljs-tag"></<span class="hljs-name">block</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>wx:if</code>是wxml文件的列表渲染语法，可见index页面是根据 <code>&#123;&#123;curCom&#125;&#125;</code> 的值来展示不同的功能组件。</p>
<ul>
<li>index.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">Component(&#123;
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">projectId</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">curCom</span>: <span class="hljs-string">'dokit'</span>,
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">tooggleComponent</span>(<span class="hljs-params">e</span>)</span> &#123;
        <span class="hljs-keyword">const</span> componentType = e.currentTarget.dataset.type || e.detail.componentType
          <span class="hljs-built_in">this</span>.setData(&#123;
            <span class="hljs-attr">curCom</span>: componentType
          &#125;)
      &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始情况下<code>&#123;&#123;curCom&#125;&#125;</code> 的值为 <code>'dokit'</code> ，因此显示的是 <code>wx:else</code> 块，页面上只有一个图标</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b84ad27cdc148f39b7edbab31107cf6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>bindtap</code> 是监听点击事件，点击图标会调用js文件中的 <code>tooggleComponent</code> 方法，传入事件e。该方法会获取 <code>e.currentTarget.dataset.type || e.detail.componentType</code> 这两个值并更新 <code>curCom</code> 值，可以打印出来进行验证，第一个值是debug，第二个值未定义。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c635a1208d874d028032fd33861626da~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca068eed75cb441ca969c575831e5451~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>curCom</code> 值的更改会影响到页面上显示的组件，因此点击图标后页面显示的是debug组件，上图控制台中第三行输出就是debug组件进入页面节点树的标志。尝试在wxml文件中更改<code>data-type="debug"</code> 的值为其他组件的名称，再次点击会相应显示出新的组件，因此也证明了<code>e.currentTarget.dataset.type</code>的值由 <code>data-type</code> 属性决定。</p>
<p>进一步观察，当点击debug组件上的其他功能图标如App信息时，外壳index里的debug组件就会发生更换，控制台的输出如下图所示，说明的确是<code>curCom</code> 值决定了index页面上显示的组件，注意到此时<code>tooggleComponent</code> 方法又被触发了，根据代码，触发的来源应该只有 <code>bindtoogle</code> 了，观察到这次 <code>e.currentTarget.dataset.type || e.detail.componentType</code> 中第一个值变成了未定义，第二个值为appinformation。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/782cc4862e3e4484ae59e0dcd7dbd165~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">目前的疑惑</h3>
<p>我知道bindtap是监听点击事件，但bindtoggle是用来做什么的，以及它们与 <code>e.currentTarget.dataset.type || e.detail.componentType</code>的关系是什么？（下文分析）</p>
<h2 data-id="heading-10">back组件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99dd1fff16bc4d8eb41ab9ce5292f571~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e96c17516a47c8b75fa9e80a6f2efc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
该组件被除index外的其他组件引用，在其他组件的页面中表现为一个dokit的logo，点击logo都会返回到最原始的index页面。
back组件工作原理简单，正好可以用来学习<strong>组件间通信和自定义事件</strong>。</p>
<h3 data-id="heading-11">原理分析</h3>
<p>DoKit中点击各个按钮后进行相应组件的切换，是由组件中的自定义事件实现的。要使用自定义组件，就要有监听和触发。其中由子组件对事件进行触发，父组件对事件进行监听。
以每个功能组件都引用的back组件为例
back.wxml中代码如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">cover-image</span>
    <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"onbackDokitEntry"</span>
    <span class="hljs-attr">data-type</span>=<span class="hljs-string">"debug"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-back"</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">"top: &#123;&#123; top &#125;&#125;"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">cover-image</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明back组件表现为一张图片，图片监听了点击事件，当事件触发后会调用<code>onbackDokitEntry</code>方法。
（此外，我认为源码中的<code>data-type="debug"</code>并没有用，通过下文的分析可知，事件的触发并没带上这个数据）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> onbackDokitEntry (e) &#123;
      <span class="hljs-comment">// console.log(e)</span>
      <span class="hljs-built_in">this</span>.triggerEvent(<span class="hljs-string">'return'</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，<code>onbackDokitEntry</code>方法触发了一个return事件。
在其他组件的wxml中，这里以appinformation组件为例，对back组件的使用如下</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">back</span> <span class="hljs-attr">bindreturn</span>=<span class="hljs-string">"onGoBack"</span>></span><span class="hljs-tag"></<span class="hljs-name">back</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这句话表明，appinformation组件里的back组件正是在监听一个名为<code>return</code>的自定义事件，如果监听到了，就会调用<code>onGoBack</code>方法，在js文件中其定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> onGoBack () &#123;
   <span class="hljs-comment">//触发事件，携带detail对象</span>
   <span class="hljs-built_in">this</span>.triggerEvent(<span class="hljs-string">'toggle'</span>, &#123; <span class="hljs-attr">componentType</span>: <span class="hljs-string">'dokit'</span>&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处说明，<code>onGoBack</code>方法又触发了名为<code>toggle</code>的事件，并携带了一个detail对象<code>&#123;componentType: 'dokit'&#125;</code>。
再回到最外面装载其他组件的index外壳页面，可以看到对appinformation组件的使用方式为：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">appinformation</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'appinformation' &#125;&#125;"</span> 
                <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">appinformation</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，此处正是在监听名为<code>toggle</code>的事件，并调用<code>tooggleComponent</code>方法，其定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">tooggleComponent</span>(<span class="hljs-params">e</span>)</span> &#123;      
        <span class="hljs-keyword">const</span> componentType = e.currentTarget.dataset.type || e.detail.componentType
          <span class="hljs-built_in">this</span>.setData(&#123;
            <span class="hljs-attr">curCom</span>: componentType,        
          &#125;)
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到此处就明白了，根据<code>toogle</code>事件携带的detail对象中的componentType值，<code>curCom</code>值变更为<code>'dokit'</code>，前文对index组件的分析中已经提到，<code>curCom</code>值直接影响到index里组件的显示，当其值为<code>'dokit'</code>时，index页面就会变成最原始的只有一个logo的样子。因此，这样就解释了back组件的工作原理——通过监听对logo图标的点击事件，从里到外触发了一系列的自定义返回事件，最终体现在index页面中；同时也解释了上文中提到的<code>bindtoggle</code>的部分作用（该事件不只是用于返回，还有一个功能是从debug组件进入其他功能组件，下文分析）。</p>
<p><strong>back组件工作流程图如下</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bdcf1f3c44c41bb8a8aea83317cc9d1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">debug组件</h2>
<p>该组件起到一个功能菜单的作用，展示了dokit当前具备的所有功能，点击每个图标会进入相应的功能组件。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1704887019904449aaa3d3916bc17865~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">功能展示</h3>
<p>debug.wxml</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;tools&#125;&#125;"</span> <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"index"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-collections card"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>debug.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">lifetimes: &#123;
  attached () &#123;
    <span class="hljs-built_in">this</span>.setData(&#123;
      <span class="hljs-attr">tools</span>: <span class="hljs-built_in">this</span>.getTools()
    &#125;);
  &#125;
&#125;,
  
 <span class="hljs-function"><span class="hljs-title">getTools</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> [
      &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"common"</span>,
        <span class="hljs-string">"title"</span>: <span class="hljs-string">"常用工具"</span>,
        <span class="hljs-string">"tools"</span>: [
          &#123;
            <span class="hljs-string">"title"</span>: <span class="hljs-string">"App信息"</span>,
            <span class="hljs-string">"image"</span>: img.appinfoicon,
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"appinformation"</span>
          &#125;,
          <span class="hljs-comment">//此处省略。。。</span>
        ]
      &#125;
    ]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>attached</code>是一个组件生命周期方法，在组件实例进入页面节点树时执行，由代码可知，每次debug组件进入index页面时，会通过<code>getTools</code>方法为组件的<code>tools</code>变量赋值，<code>getTools</code>方法返回的就是其他功能组件的信息，之后在wxml中，利用<code>wx:for="&#123;&#123;tools&#125;&#125;"</code>进行列表渲染，从而循环展示出所有的功能。</p>
<h3 data-id="heading-14">功能选择</h3>
<p>debug.wxml</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;item.tools&#125;&#125;"</span>
              <span class="hljs-attr">wx:for-index</span>=<span class="hljs-string">"idx"</span>
              <span class="hljs-attr">wx:for-item</span>=<span class="hljs-string">"tool"</span>
              <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"idx"</span>
              <span class="hljs-attr">data-type</span>=<span class="hljs-string">"&#123;&#123;tool.type&#125;&#125;"</span>
              <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"onToggle"</span>
              <span class="hljs-attr">class</span>=<span class="hljs-string">"card-item"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在列表循环中，每个图标在监听点击事件，点击发生后调用<code>onToggle</code>方法，使用<code>data-type</code>属性可以给事件带上信息，以此判断用户点击的具体是哪个功能。</p>
<blockquote>
<p>在组件节点中可以附加一些自定义数据。这样，在事件中可以获取这些自定义的节点数据，用于事件的逻辑处理。
在 WXML 中，这些自定义数据以data-开头，多个单词由连字符-连接。这种写法中，连字符写法会转换成驼峰写法，而大写字符会自动转成小写字符。如：</p>
<ul>
<li>data-element-type，最终会呈现为event.currentTarget.dataset.elementType；</li>
<li>data-elementType，最终会呈现为event.currentTarget.dataset.elementtype。</li>
</ul>
<p>微信开发文档，<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p>
</blockquote>
<p>degub.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">onToggle (event) &#123;
  <span class="hljs-keyword">const</span> type = event.currentTarget.dataset.type;
  <span class="hljs-keyword">if</span>(type === <span class="hljs-string">'onUpdate'</span>) &#123;
    <span class="hljs-built_in">this</span>[type]();
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//触发事件，携带detail对象</span>
    <span class="hljs-built_in">this</span>.triggerEvent(<span class="hljs-string">'toggle'</span>, &#123; <span class="hljs-attr">componentType</span>: type &#125;)
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由官方文档和代码可知，<code>event.currentTarget.dataset.type</code>就是wxml中的<code>data-type</code>属性值。如果用户点击的是更新版本功能，则会调用在此js文件中定义的<code>onUpdate</code>方法（此方法下文分析）；如果是其他功能，则会触发<code>toggle</code>事件，并带上一个detail对象，再之后就如上文已经分析的那样，会被index页面中的<code>bindtoggle</code>监听，并根据detail对象更新<code>curCom</code>值，从而实现页面中相应功能组件的切换。
<strong>流程图如下</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6de760a510924c209052646f4f9cdb3e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上文back组件部分的最后，我提到<code>bindtoggle</code>有两个作用，现在可以做一个总结：</p>
<ul>
<li>监听所有组件中的点击logo返回事件</li>
<li>监听debug组件中的功能选择事件</li>
</ul>
<p>可以发现，这些层层嵌套的自定义事件的最底层触发条件都是<code>tap</code>，即点击操作。</p>
<h3 data-id="heading-15">版本更新功能</h3>
<p>此功能用来检查小程序最新发布的版本是否比当前设备中的版本高</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">onUpdate () &#123;
  <span class="hljs-keyword">const</span> updateManager = wx.getUpdateManager();
  updateManager.onCheckForUpdate(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!res.hasUpdate) &#123;
      <span class="hljs-comment">// 请求完新版本信息的回调</span>
      wx.showModal(&#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
        <span class="hljs-attr">content</span>: <span class="hljs-string">'当前已经是最新版本'</span>
      &#125;)
    &#125;
  &#125;);
  updateManager.onUpdateReady(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//新版本下载成功</span>
    wx.showModal(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'新版本已经准备好，是否重启应用？'</span>,
      <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (res.confirm) &#123;
          <span class="hljs-comment">// 新的版本已经下载好，调用 applyUpdate 应用新版本并重启</span>
          updateManager.applyUpdate()
        &#125;
      &#125;
    &#125;)
  &#125;);
  updateManager.onUpdateFailed(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 新版本下载失败</span>
     wx.showModal(&#123;
       <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
       <span class="hljs-attr">content</span>: <span class="hljs-string">'下载失败'</span>,
       <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
       &#125;
     &#125;)
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前文已经提到，在debug菜单组件中如果点击了更新版本功能，则会调用上述<code>onUpdate</code>方法。
<code>wx.getUpdateManager</code>是微信官方接口，用来获取小程序<strong>全局唯一</strong>的版本更新管理器<code>UpdateManager</code>对象，以此来管理小程序的更新，该对象有四个方法。</p>
<blockquote>
<ul>
<li>UpdateManager.applyUpdate()</li>
</ul>
<p>强制小程序重启并使用新版本。在小程序新版本下载完成后（即收到 onUpdateReady 回调）调用。</p>
<ul>
<li>UpdateManager.onCheckForUpdate(function callback)</li>
</ul>
<p>监听向微信后台请求检查更新结果事件。微信在小程序冷启动时自动检查更新，不需由开发者主动触发。</p>
<ul>
<li>UpdateManager.onUpdateReady(function callback)</li>
</ul>
<p>监听小程序有版本更新事件。客户端主动触发下载（无需开发者触发），下载成功后回调</p>
<ul>
<li>UpdateManager.onUpdateFailed(function callback)</li>
</ul>
<p>监听小程序更新失败事件。小程序有新版本，客户端主动触发下载（无需开发者触发），下载失败（可能是网络原因等）后回调</p>
<p>微信开发文档，
<a href="https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.html" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p>
</blockquote>
<p>所以<code>onUpdate</code>方法的整体逻辑是先检查是否存在更新版本，若不存在则使用<code>wx.showModal</code>显示模态对话框提示当前已是最新版本，若存在则由微信客户端自动进行小程序的新版本下载，如果下载成功将调用<code>onUpdateReady</code>里的回调——提醒用户重启应用新版本，如果下载失败则调用<code>onUpdateFailed</code>里的回调（源码中该回调函数内容为空，这里我模仿<code>onUpdateReady</code>里的回调也加了一个对话框）。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb1ba0a30e714d10a66689af4c8d7a09~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c84b3df3650c450e9754fd4f69f1b9e4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04c79716ac504f45b5c6e6443a0e2490~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-16">positionsimulation组件</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/455bb00249814d8aac8fab37e64c2d41~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/275f324d52154b98aa0ca5e933cb1034~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>用于小程序端位置模拟，包括位置授权，位置查看，位置模拟，恢复位置设置等几大功能，可以通过简单的点击操作实现任意位置模拟和位置还原，该功能的实现原理是通过对wx.getLocation进行方法重写，进而进行位置模拟，位置模拟后，在小程序内所有调用位置查询的方法内都将返回你设定的位置，还原后将恢复原生方法
DoKit文档，<a href="https://github.com/didi/DoraemonKit/tree/master/miniapp" target="_blank" rel="nofollow noopener noreferrer">github.com/didi/Doraem…</a></p>
</blockquote>
<h3 data-id="heading-17">快速授权</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fast-authorization"</span> <span class="hljs-attr">open-type</span>=<span class="hljs-string">"openSetting"</span>></span>快速授权<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>open-type</code>微信开放能力，点击button后会打开小程序授权设置页面</p>
<h3 data-id="heading-18">查看位置</h3>
<p>使用自定义的<code>openMyPosition</code>方法，定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> openMyPosition ()&#123;
   wx.getLocation(&#123;
     <span class="hljs-attr">type</span>: <span class="hljs-string">'gcj02'</span>,
     success (res) &#123;
       wx.openLocation(&#123;
         <span class="hljs-attr">latitude</span>:res.latitude,
         <span class="hljs-attr">longitude</span>:res.longitude,
         <span class="hljs-attr">scale</span>: <span class="hljs-number">18</span>
       &#125;)
     &#125;
   &#125;)
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，该方法直接调用了微信官方的<code>wx.getLocation</code>接口来获取当前位置数据，<code>type</code>属性为<code>'gcj02'</code>，这是一种可用于<code>wx.openLocation</code>的坐标，接口调用成功则将坐标传给<code>wx.openLocation</code>方法，使用微信内置地图查看当前位置。</p>
<h3 data-id="heading-19">选择位置</h3>
<p><strong>预备知识：</strong></p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63a0332fe3284b68b5f8073c81c46c1a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
</blockquote>
<blockquote>
<p>**Object.defineProperty()**方法会直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象。
参考：<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
</blockquote>
<p>使用自定义的<code>choosePosition</code>方法，定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">choosePosition ()&#123;
  wx.chooseLocation(&#123;
    <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setData(&#123; <span class="hljs-attr">currentLatitude</span>: res.latitude &#125;);
      <span class="hljs-built_in">this</span>.setData(&#123; <span class="hljs-attr">currentLongitude</span>: res.longitude &#125;)
      <span class="hljs-built_in">Object</span>.defineProperty(wx, <span class="hljs-string">'getLocation'</span>, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">val</span>)</span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
            obj.success(&#123;<span class="hljs-attr">latitude</span>: res.latitude, <span class="hljs-attr">longitude</span>: res.longitude&#125;)
          &#125;
        &#125;
      &#125;)
    &#125;
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先调用微信官方的<code>wx.chooseLocation</code>方法，以实现打开微信内置地图选择位置，调用成功后，使用<code>Object.defineProperty</code>方法改写了<code>wx.getLocation</code>方法。通过预备知识我们知道，<code>getLocation</code>可以看作对象<code>wx</code>的一个属性，属性值为一个函数定义，那么当我们修改该属性的<code>get</code>函数时，其实就相当于重写了<code>getLocation</code>里的函数定义，在新的函数定义里，我们接收一个对象参数，调用其<code>success</code>方法，方法参数中传入我们之前选择的坐标数据，从而实现了今后每次调用<code>wx.getLocation</code>方法时，给<code>success</code>回调函数传入的都是我们选择的坐标数据。（<code>get</code>函数中不需要参数，源码这里应该是误写）</p>
<p><strong>总结一下就是，改写了</strong><code>**wx.getLocation**</code><strong>方法，使其给其回调函数传入的是我们设定的值。</strong></p>
<h3 data-id="heading-20">还原</h3>
<p>使用自定义的<code>resetPosition</code>方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> app = getApp()
app.originGetLocation = wx.getLocation


<span class="hljs-comment">//省略...</span>

resetPosition ()&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(wx, <span class="hljs-string">'getLocation'</span>,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">return</span> app.originGetLocation
    &#125;
  &#125;);
  wx.showToast(&#123;<span class="hljs-attr">title</span>:<span class="hljs-string">'还原成功！'</span>&#125;)
  <span class="hljs-built_in">this</span>.getMyPosition()
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在最开始，使用<code>app.originGetLocation</code>保存了<code>wx.getLocation</code>中原始的函数定义，以方便后面恢复。之后，相似的原理，利用<code>Object.defineProperty</code>方法将<code>wx.getLocation</code>改写回来，从而实现还原。</p>
<h3 data-id="heading-21">总结</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/608302d8cd974c1ea2bb5179d29d1157~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">apimock组件</h2>
<h3 data-id="heading-23">mock是什么</h3>
<p>mock可以拦截网络请求，并返回一个模拟的服务器响应，使开发人员在后端接口还未实现时也能够完成前端的开发。</p>
<h3 data-id="heading-24">效果演示</h3>
<ol>
<li>在平台端新建一条数据mock</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6df3012f8cf84c15a11f3636b8dc6e57~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
设定接口名称为test，接口分类为测试，请求路径为<code>/test</code>
在详情页面，还可以增加多个场景，并设定不同场景下的返回值，这里我设定了2个场景，<code>Default</code>和<code>场景1</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd8b75842a6b4377b0b2bc79c2910879~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>小程序上查看mock功能</li>
</ol>
<p>首先要确保在引入dokit的组件页面上传入了<code>projectId</code>属性，projectId可以在平台端找到</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">dokit</span> <span class="hljs-attr">projectId</span>=<span class="hljs-string">"5fcd3ef4b4f88839cd7bff5848bfe3ca"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">dokit</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开apimock（数据模拟）组件，可以看到我们之前注册的test接口
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e946770f61d9499b96b6d97615a648cf~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>模拟一个网络请求</li>
</ol>
<p>在首页加了一个button，当点击按钮时，向<code>/test</code>接口发送一个GET请求，如果请求成功的话，打印返回结果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26b2c141253e4467ae7d3e28d52cbb1a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">mock_test</span>(<span class="hljs-params"></span>)</span>&#123;
    wx.request(&#123;
      <span class="hljs-attr">url</span>: <span class="hljs-string">'https://localhost/test'</span>,
      <span class="hljs-attr">method</span>:<span class="hljs-string">"GET"</span>,
      <span class="hljs-attr">success</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(res)
      &#125;
    &#125;)
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>测试结果</li>
</ol>
<p>打开mock开关，设定场景值为<code>Default</code>，点击按钮发送请求，观察控制台，可以看到是我们之前设定的返回值
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b98ab87b32c740d7811939ea579e06d7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
设定场景值为<code>场景值1</code>，再次测试，发现返回值的确发生了相应的改变
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1e6be30ba0435897b58d7ce50ae43c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>模板功能</li>
</ol>
<p>对mock接口请求成功后，返回的数据会作为模板数据保存下来，方便上传
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e8889e0023a42c4b56e3ecc14d581a9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d8e2992f63f47b0a9fb660fa9e207f3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">代码分析</h2>
<p>视图层的原理很简单，之前其他组件的分析中均有涉及，故在此不作赘述，直接分析逻辑层
按照自上而下的方法，首先看一下该组件的生命周期</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">lifetimes: &#123;
  created () &#123;
  &#125;,
  attached () &#123;
    <span class="hljs-built_in">this</span>.pageInit()
  &#125;,
  detached () &#123;
    wx.setStorageSync(<span class="hljs-string">'dokit-mocklist'</span>, <span class="hljs-built_in">this</span>.data.mockList)
    wx.setStorageSync(<span class="hljs-string">'dokit-tpllist'</span>, <span class="hljs-built_in">this</span>.data.tplList)
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当该组件进入页面即开始使用时，调用了<code>pageInit</code>方法，从名字上看这应该是一个关于初始化的方法。</li>
<li>当该组件从页面中移除即退出该功能时，调用了<code>wx.setStorageSync</code>方法，该方法的作用是同步设置本地缓存，从key的名字上看是缓存了mock接口和模板的数据。</li>
</ul>
<p><code>pageInit</code>方法定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//页面初始化</span>
pageInit () &#123;
  <span class="hljs-comment">//初始化mock列表</span>
  <span class="hljs-built_in">this</span>.initList()
  <span class="hljs-comment">//添加RequestHooks</span>
  <span class="hljs-built_in">this</span>.addRequestHooks()
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法做了两件事，一个是初始化mock列表，另一个是添加RequestHooks，下面依次进行分析</p>
<h4 data-id="heading-26">initList()</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//初始化mock列表</span>
initList () &#123;
  <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">const</span> opt = &#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;mockBaseUrl&#125;</span>/api/app/interface`</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
    <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">projectId</span>: <span class="hljs-built_in">this</span>.getProjectId(), <span class="hljs-attr">isfull</span>: <span class="hljs-number">1</span> &#125;
  &#125;
  that.request(opt).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; data &#125; = res.data
    <span class="hljs-keyword">if</span> (data && data.datalist && data.datalist.length) &#123;
      that.updateMockList(data.datalist)
      that.updateTplList(data.datalist)
    &#125;
  &#125;).catch()
&#125;,
  
 <span class="hljs-comment">//获取projectId</span>
 getProjectId () &#123;
   <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.projectId) &#123;
     <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"您还没有设置 projectId，去快平台端体验吧：https://www.dokit.cn"</span>)
     <span class="hljs-keyword">return</span>
   &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.data.projectId
   &#125;
 &#125;,

<span class="hljs-comment">//构造promise对象 </span>
request (options) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    app.originRequest(&#123;
      ...options,
      <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-params">res</span> =></span> resolve(res),
      <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err)
    &#125;)
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第4-8行设置了一个对象常量<code>opt</code>，属性<code>url</code>是一个反引号包起来的模板字符串，其中<code>$&#123;mockBaseUrl&#125;</code>在前面已经设置成一个值为"<a href="https://mock.dokit.cn/" target="_blank" rel="nofollow noopener noreferrer">mock.dokit.cn</a>"的常量，这正是dokit平台端的网址。
属性<code>data</code>的初始化里调用了<code>getProjectId</code>方法，该方法的定义在第18行，虽然<code>projectId</code>是组件的属性，但也通过<code>this.data</code>访问，其值是在我们引入dokit工具的页面中传入的，在这里首先检测是否已传入<code>projectId</code>，若未传入则控制台输出警告后返回；若已传入则返回该属性值。
从<code>opt</code>对象的构造来看，非常像我们在使用<code>wx.request</code>方法时传入的对象，下文的分析也会印证这个猜想。</p>
<p>第9-15行调用了一个<code>request</code>方法，该方法的定义在第28行，用来构造并返回一个promise对象。在继续分析之前，有必要简单介绍一下什么是promise，在我看来promise是用来控制异步操作实现同步的一种手段，其避免了层层嵌套的回调函数，将一系列异步操作按照我们期望的顺序执行。</p>
<blockquote>
<p>想了解更多关于promise的内容请浏览</p>
<p><a href="https://blog.csdn.net/zzh990822/article/details/109573797?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-0&spm=1001.2101.3001.4242" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/zzh990822/a…</a></p>
<p><a href="https://www.liaoxuefeng.com/wiki/1022910821149312/1023024413276544" target="_blank" rel="nofollow noopener noreferrer">www.liaoxuefeng.com/wiki/102291…</a></p>
<p>Promise中的then第二个参数和catch有什么区别<a href="https://blog.csdn.net/gogo_steven/article/details/103352762" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/gogo_steven…</a></p>
</blockquote>
<p>第31行的<code>app.originRequest</code>是在该js文件最前面被设置的（本文未显示），设置的值为<code>wx.request</code>，为什么这里不直接使用<code>wx.request</code>呢？
因为apimock组件的实现原理就是通过改写<code>wx.request</code>方法，如果想确保任何时候都还能使用到正常的<code>wx.request</code>方法，就得事先将其另存起来。</p>
<p>回到第9-15行，如果已经明白promise工作原理的话，我们就可分析出这段代码的意思——带上我们的projectId向dokit平台端接口发送请求，该接口的作用应该是根据projectId返回我们在平台端设定的mock信息，<strong>在确保请求成功并返回后，检验返回数据，如果合法则调用相关方法对mocklist数据进行更新</strong>，这里的执行顺序非常重要，而promise的作用就体现在这。值得一提的是，第15行的<code>catch</code>方法里没有传入异常处理的回调函数，我认为最好有一个，从而使程序更加健壮。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.catch(<span class="hljs-function">(<span class="hljs-params">err</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">addRequestHooks()</h4>
<p>首先，什么是Hooks，根据网络上的解释，是在已经可以正常运作的程序中额外添加流程控制，通俗来说就是拦截指定的消息，用自己的方式处理一下，然后再放出去。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">addRequestHooks () &#123;
  <span class="hljs-built_in">Object</span>.defineProperty(wx,  <span class="hljs-string">"request"</span> , &#123; <span class="hljs-attr">writable</span>:  <span class="hljs-literal">true</span> &#125;);
  <span class="hljs-built_in">console</span>.group(<span class="hljs-string">'addRequestHooks success'</span>)
  <span class="hljs-keyword">const</span> matchUrlRequest = <span class="hljs-built_in">this</span>.matchUrlRequest.bind(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">const</span> matchUrlTpl = <span class="hljs-built_in">this</span>.matchUrlTpl.bind(<span class="hljs-built_in">this</span>)
  wx.request = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> opt = util.deepClone(options)
    <span class="hljs-keyword">const</span> originSuccessFn = options.success
    <span class="hljs-keyword">const</span> sceneId = matchUrlRequest(options)
    <span class="hljs-keyword">if</span> (sceneId) &#123;
      options.url = <span class="hljs-string">`<span class="hljs-subst">$&#123;mockBaseUrl&#125;</span>/api/app/scene/<span class="hljs-subst">$&#123;sceneId&#125;</span>`</span>
      <span class="hljs-built_in">console</span>.group(<span class="hljs-string">'request options'</span>, options)
      <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'被拦截了~'</span>)
    &#125;
    options.success = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
      originSuccessFn(matchUrlTpl(opt, res))
    &#125;
    app.originRequest(options)
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第2行的<code>Object.defineProperty</code>之前我们已经分析过，它的作用是为对象新增或修改一个属性，这里是将<code>wx.request</code>设置为允许被赋值运算符改变。
观察到第4、5行的方法后都有一个<code>.bind(this)</code>，这里是为了确保之后调用两个方法时，其函数体内的this指向的是当前这个组件对象。</p>
<blockquote>
<p>bind()会创建一个函数，函数体内的this对象的值会被绑定到传入bind()第一个参数的值，例如，f.bind(obj)，实际上可以理解为obj.f()，这时，f函数体内的this自然指向的是obj。</p>
</blockquote>
<p>第6-19行是对<code>wx.request</code>的重写，第9行是将请求<code>options</code>传入<code>matchUrlRequest</code>中，返回一个<code>sceneId</code>，如果该值非空的话，改写请求<code>options</code>里的URL为dokit平台端一个与<code>sceneId</code>相关的接口，并在控制台输出改写后的<code>options</code>信息，第15-17行改写了请求<code>options</code>里的<code>success</code>回调函数（下文分析），第18行调用之前保存的原始的微信请求方法，此时传入的是已修改后的<code>options</code>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61a8a8d8a3e4c569e8fcc8ec835a723~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里可以推测，<code>matchUrlRequest</code>方法的作用应该是将我们原本要发送的请求与mock接口列表相匹配，如果匹配成功就返回之前为该mock接口选定的场景的Id。观察改写后的新URL我们可以确定dokit平台端就是根据场景Id来确定应该响应什么数据。
具体来看，<code>matchUrlRequest</code>方法的定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//匹配URL请求</span>
matchUrlRequest (options) &#123;
  <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">false</span>, curMockItem, sceneId;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.mockList.length) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>,len = <span class="hljs-built_in">this</span>.data.mockList.length; i < len; i++) &#123;
    curMockItem = <span class="hljs-built_in">this</span>.data.mockList[i]
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.requestIsmatch(options, curMockItem)) &#123;
      flag = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">break</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (curMockItem.sceneList && curMockItem.sceneList.length) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j=<span class="hljs-number">0</span>,jLen=curMockItem.sceneList.length; j<jLen; j++) &#123;
      <span class="hljs-keyword">const</span> curSceneItem = curMockItem.sceneList[j]
      <span class="hljs-keyword">if</span> (curSceneItem.checked) &#123;
        sceneId = curSceneItem._id
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    sceneId = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-keyword">return</span> flag && curMockItem.checked && sceneId
&#125;,
  
<span class="hljs-comment">// judge url is match</span>
requestIsmatch (options, mockItem) &#123;
  <span class="hljs-keyword">const</span> path = util.getPartUrlByParam(options.url, <span class="hljs-string">'path'</span>)
  <span class="hljs-keyword">const</span> query = util.getPartUrlByParam(options.url, <span class="hljs-string">'query'</span>)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.urlMethodIsEqual(path, options.method, mockItem.path, mockItem.method) 
  && <span class="hljs-built_in">this</span>.requestParamsIsEqual(query, options.data, mockItem.query, mockItem.body)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第3行声明了3个变量，<code>flag</code>记录是否匹配成功，<code>curMockItem</code>记录mock接口信息，<code>sceneId</code>记录场景Id。第5-11行是在循环遍历mock列表，其中真正用来匹配的是第7行的<code>requestIsmatch</code>方法，其定义在26行，通过观察里面调用的方法名大致可以推断用来匹配的依据是：请求路径、请求方法、query参数、请求体。回到第12-24行，若成功匹配到mock信息，则继续检查该mock接口下的哪一个场景被勾选，选中的场景Id存入<code>sceneId</code>中，第23行的写法表示若<code>flag</code>和<code>curMockItem.checked</code>都为true的话，返回<code>sceneId</code>的值，否则返回false。</p>
<p>现在对<code>addRequestHooks</code>方法的分析中还剩下一点，就是第15-17行对原有请求<code>options</code>里的success回调函数的修改，结合第8行来看，好像就是多做了一件事<code>matchUrlTpl(opt, res)</code>，该方法的定义如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">matchUrlTpl (options, res) &#123;
  <span class="hljs-keyword">let</span> curTplItem,that = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">if</span> (!that.data.tplList.length) &#123; <span class="hljs-keyword">return</span> res &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>,len=that.data.tplList.length;i<len;i++) &#123;
    curTplItem = that.data.tplList[i]
    <span class="hljs-keyword">if</span> (that.requestIsmatch(options, curTplItem) && curTplItem.checked && res.statusCode == <span class="hljs-number">200</span>) &#123;
      that.data.tplList[i].templateData = res.data
    &#125;
  &#125;
  wx.setStorageSync(<span class="hljs-string">'dokit-tpllist'</span>, that.data.tplList)
  <span class="hljs-keyword">return</span> res
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来说，该方法的作用就是，如果本次请求与mock接口列表匹配，则将请求成功返回的数据<code>res</code>作为模板保存在本地存储中，然后正常返回<code>res</code>以便继续执行原来的success回调。</p>
<h3 data-id="heading-28">总结</h3>
<p>至此，数据mock功能最核心的代码已经分析完毕，其原理简单概括就是，重写<code>wx.request</code>方法，在发送请求前，将请求与用户设置的mock接口进行匹配，若匹配成功则修改请求信息（URL和请求成功的回调函数），之后才真正发送请求。</p>
<h2 data-id="heading-29">结语</h2>
<p>这是本人第一次尝试阅读并分析开源项目的代码，在此过程中感觉收获良多，感谢指导和帮助过我的DoKit项目老师们和同学们。由于我对小程序和JavaScript的理解也只是入门阶段，文中若有分析不当之处，欢迎指正。</p>
<p>2021/4/27</p>
<h1 data-id="heading-30">作者信息</h1>
<p>作者：<a href="https://juejin.cn/user/4416075175560327" target="_blank">七省文状元</a></p>
<p>原文链接：<a href="https://juejin.cn/post/6955782379952668679/" target="_blank">juejin.cn/post/695578…</a></p>
<p>来源：掘金</p></div>  
</div>
            