
---
title: 'React基础概念一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a6c61027b864c2baf60d7be95e860b0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 00:02:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a6c61027b864c2baf60d7be95e860b0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">安装脚手架</h1>
<blockquote>
<ol>
<li>npm install -g create-react-app</li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li>npm config set registry <a href="https://link.juejin.cn/?target=https%3A%2F%2Fregistry.npm.taobao.org" target="_blank" rel="nofollow noopener noreferrer" title="https://registry.npm.taobao.org" ref="nofollow noopener noreferrer">registry.npm.taobao.org</a></li>
</ol>
</blockquote>
<blockquote>
<ol start="3">
<li>创建项⽬:npx create-react-app my-app</li>
</ol>
</blockquote>
<blockquote>
<ol start="4">
<li>启动项⽬:npm start</li>
</ol>
</blockquote>
<blockquote>
<ol start="5">
<li>暴露配置项:npm run eject</li>
</ol>
</blockquote>
<h1 data-id="heading-1">cra文件结构</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a6c61027b864c2baf60d7be95e860b0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">隐藏的index</h1>
<blockquote>
<p>1.基础结构</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a921b88bdf81475e9c3508899f327e82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>2.两个入口</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e1396a50743432c9a6661f9e83aee7c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">vscode插件</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cec67bbe78324151b0d4bcef945f8a97~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>可愉快的使用rcc rfc imp快捷键...</li>
</ul>
<h1 data-id="heading-4">jsx</h1>
<blockquote>
<p>1.基本使⽤</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0cb22c7de75410a98e17bcbd2a96fdf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>2.&#123;&#125;</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1d716c4eba41c4b6e118ba5ab67f9f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>3.函数</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2c3c7e5a29241cfa21b06a899dd0619~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>4.对象</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c585ede5c99e4743b584f1121144aa3e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>5.条件语句</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fe71747fcbc4ded9553d42ba456aaf3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>6.数组</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/280469206ac24dc999174e65df25ca7f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>7.属性的使⽤</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e6b43b327d46b2b40a1dcd4b6061f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>8.模块化(index.module.css后缀名是固定的)</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af77fe6370dc40cab0aabcbd4fe51792~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="9">
<li>本质</li>
</ol>
</blockquote>
<p>jsx仅仅只是React.createElement(component,props,...children)函数的语法糖,所有的jsx最终都会转换成React.createElement()的函数调用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7320f1461db44bc839f7478f8b6eb30~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>看下源码：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c681fec71043435eb20a5ff0452754f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d0690e2380648d09240563397edf0b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>引申虚拟DOM的创建过程</li>
</ul>
<p>通过React.createElement最终创建出来一个ReactElement对象</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e1025e2aa2a48fbba7d36ba447accdf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终利用ReactElement对象组成一个js的对象树，这棵树就叫虚拟DOM。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/383fe6bae4184275aa7e7ee8debc869b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ReactDOM.render -> 让虚拟DOM转换为真实DOM（这个过程叫做协调Reconciliation）。</p>
<ul>
<li>为啥使用虚拟DOM</li>
</ul>
<p>1.document.createElement本身创建出来的就是一个非常复杂的对象。</p>
<p>2.DOM操作会引起浏览器的重绘与回流。</p>
<p>3.真实dom很难跟踪状态的改变，不方便调试。</p>
<h1 data-id="heading-5">组件</h1>
<h2 data-id="heading-6">类式组件</h2>
<ul>
<li>class组件通常拥有状态和⽣命周期，组件名称大写字符开头，继承于Component，必须实现render⽅法。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db807e39cf22464db4e73540bbfd8102~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>state最基本写法</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/882bde416f454129a8d371200f5fa78d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>props最基本写法</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddf441d2a6064ddd9892983ba3b86e2c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">函数式组件</h2>
<ul>
<li>从React16.8开始引⼊了hooks，函数组件也能够拥有状态(这里先知道有这么一个东西 后面细说)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a77584af6f249f4ab5ec41af5d60590~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">事件处理(this问题的三大方案)</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ff1275d5f8468489aa9aa2a9afdc12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7427ad2dcf3843688a754df721d765c8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">生命周期</h1>
<blockquote>
<p>旧(16版本前)</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3800b4957e946a0ad98adc9b1fac117~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1218408e1495411c836d8b85780e4d87~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>新(16版本后)</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dedca1e77d84c509711e44eace1fbe2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39deec0392f14379838e58569a17a0da~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>getDerivedStateFromProps</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b03550331f477f979a078945dab1a7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>getSnapshotBeforeUpdate</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd2c99d044ba4efbba9afe528b7e8a23~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">通信</h1>
<h2 data-id="heading-11">父子通信</h2>
<ul>
<li>父传值给子(就是通过props)</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a62b5c31cd04f8d82c8ec6205b0f6ed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>子传值给父(通过调用父事件回传参数)</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ba602ac9f01480c91aeb9e2e1db937f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">兄弟通信</h2>
<blockquote>
<ol>
<li>上面的写法Home 与 About就完成了一次兄弟间的通信(也就是给到上级，通过上级获取)</li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li>消息发布订阅方式-任意组件通信(插件)</li>
</ol>
</blockquote>
<ul>
<li>npm i pubsub-js -D / npm i events -D</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36575dce3bc8427bb1c1d8d773f6d555~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff83e3f5d0e44680b0810ac4f2597fcf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">跨组件通信-context(非hooks写法)</h2>
<blockquote>
<p>一种组件间通信方式, 常用于【祖组件】与【后代组件】间通信,相当于注入在封装库中基本用到。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3b2687b3cff44eeb2e8c69d9ceca0c3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>函数式组件如何声明接受context</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a937ab93ac14fca82efa985cf41d86b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">setState</h1>
<blockquote>
<ol>
<li>正确使⽤setState</li>
</ol>
</blockquote>
<pre><code class="copyable">setState(partialState, callback)
partialState : object|function //⽤于产⽣与当前state合并的⼦集。
callback : function //state更新之后被调⽤。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ae62078827242238b50b3762dee0c47~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="2">
<li>不要直接修改 State</li>
</ol>
</blockquote>
<pre><code class="copyable">this.state.name = 'Hello'; //此代码不会重新渲染组件
this.setState(&#123;name: 'Hello'&#125;);//正确使⽤
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol start="3">
<li>State的更新可能是异步的</li>
</ol>
</blockquote>
<ul>
<li>setState在生命周期中是异步的</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f8a562fe47421891747cfde717d814~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>setState在合成事件是异步的</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e493563d9be417287ab907108e113e1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>让setState输出同步的结果(callback/componentDidUpdate)</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c827d06319e48c8a8c187badbb4b6b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="4">
<li>State的更新可能是同步的</li>
</ol>
</blockquote>
<ul>
<li>setState在setTimeout中是同步的</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda5ebfbc6034a59b11a4d36217828c6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>setState在原生事件中是同步的</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3b3b09e3da40c49914c1dcfe48f0db~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="5">
<li>State的更新数据合并</li>
</ol>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0a0067a7fc9461f88667748eb7913d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc01af4a2ea64c519f89eccae16ec380~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="5">
<li>State的更新本身被合并</li>
</ol>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c53884d8e1647b1b4b4760d2b93d4fd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b54ccc22ae04e6ea28b16cb62e06a85~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>6.为什么设计setState为异步</p>
</blockquote>
<ul>
<li>显著提升性能</li>
</ul>
<p>1.如果每次调用setState都进行一次更新，那么意味着render函数或被频繁调用,界面重新渲染,效率较低。</p>
<p>2.最好的方法应该是获取多个更新的操作，之后进行批量更新。</p>
<ul>
<li>如果同步更新了state,但是还没有执行render函数，那么stste和props不能保持同步，会在开发中产生很多问题，如父组件的state改变了而render还未完成导致子组件props的值未能同步。</li>
</ul>
<blockquote>
<p>7.总结</p>
</blockquote>
<pre><code class="copyable">(1). setState(stateChange, [callback])------对象式的setState
     1.stateChange为状态改变对象(该对象可以体现出状态的更改)
     2.callback是可选的回调函数, 它在状态更新完毕、界面也更新后(render调用后)才被调用
     
(2). setState(updater, [callback])------函数式的setState
     1.updater为返回stateChange对象的函数。
     2.updater可以接收到state和props。
     3.callback是可选的回调函数, 它在状态更新、界面也更新后(render调用后)才被调用。
     
总结:
    1.对象式的setState是函数式的setState的简写方式(语法糖)
    2.使用原则：
(1).如果新状态不依赖于原状态 ===> 使用对象方式
(2).如果新状态依赖于原状态 ===> 使用函数方式
(3).如果需要在setState()执行后获取最新的状态数据, 要在第二个callback函数中读取
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">react更新机制</h1>
<ul>
<li>props/state改变</li>
<li>render函数重新执行</li>
<li>生产新的虚拟DOM树</li>
<li>新旧虚拟DOM树进行Diff</li>
<li>计算出差异进行更新</li>
<li>更新到真实的DOM</li>
</ul>
<blockquote>
<p>1.同层节点之间相互比较;</p>
</blockquote>
<blockquote>
<p>2.不同类型的节点，产生不同的树结构然后直接删除替换;</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3065360f60fb44b2b6e6e388f20b14ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>3.同一类型节点：className修改只会更新className，style中某个属性修改只会更新某个属性;</p>
</blockquote>
<blockquote>
<p>4.同类型组件：更新该组件的Props,调用组件render函数，继续Diff递归比较;</p>
</blockquote>
<blockquote>
<p>5.开发中，可以通过key来指定哪些节点在不同渲染下保持稳定;</p>
</blockquote>
<blockquote>
<p>6.对于列表修改数据往最后添加一条数据，最后的数据会生成一个mutation，最终将其插入DOM树即可。此时添加key意义不是很大。</p>
</blockquote>
<blockquote>
<p>7.对于列表修改数据往前面或中间添加一条数据，React会对每一个子元素产生一个mutation，此时key的意义就重大了，存在key时会进行key的匹配，会产生位移的操作，可以减少不必要的更新。</p>
</blockquote>
<h1 data-id="heading-16">组件优化</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb0a6ee3f49d40f89ad1aab86f77cc2a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">两个问题</h2>
<blockquote>
<ol>
<li>只要执行setState(),即使不改变状态数据, 组件也会重新render() ==> 效率低</li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li>只要当前组件重新render(), 就会自动重新render子组件，纵使子组件没有用到父组件的任何数据 ==> 效率低</li>
</ol>
</blockquote>
<ul>
<li>出现问题的原因就是上面react更新机制第四点提到的，当执行了setState()，就会执行render，render时发现有组件执行组件的render,导致不必要的更新。</li>
</ul>
<h2 data-id="heading-18">效率高的做法</h2>
<blockquote>
<p>只有当组件的state或props数据发生改变时才重新render()</p>
</blockquote>
<h2 data-id="heading-19">原因</h2>
<blockquote>
<p>Component中的shouldComponentUpdate()总是返回true</p>
</blockquote>
<h2 data-id="heading-20">方案一</h2>
<blockquote>
<p>重写shouldComponentUpdate()方法</p>
</blockquote>
<blockquote>
<p>比较新旧state或props数据, 如果有变化才返回true, 如果没有返回false,如果state数据多的话这个方案是不可行的</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bf2595c063d4d72a74430ecdd5adda4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a0fca8296d3421c9c881e4854eb84f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">方案二</h2>
<blockquote>
<p>使用PureComponent</p>
</blockquote>
<blockquote>
<p>PureComponent重写了shouldComponentUpdate(), 只有state或props数据有变化才返回true</p>
</blockquote>
<blockquote>
<p>解决不了函数式组件(使用memo解决)</p>
</blockquote>
<blockquote>
<p>注意:</p>
</blockquote>
<ul>
<li>只是进行state和props数据的浅比较, 如果只是数据对象内部数据变了, 返回false</li>
<li>不要直接修改state数据, 而是要产生新数据</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/547b0b491cf64d439f435393a428b673~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe381b4445114073ab7877c143c40b34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ac8ac2a7d93468f94034c892683947d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/476ec5ea4a674abcb37031820427c79d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">函数式组件的优化-memo</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63db0a0ad62e44eab4aed935a4b3b868~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a62101b8b0f0446691fe2247a688c901~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-23">setState不可变数据的力量</h1>
<p>简单的说就是传入新的值的时候必须使用新的值而不是修改原来state中的值。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a572d80734fb4cedb546b4b4f4bdf200~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef12720f68004c35981cc551666ea4c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当使用SCU,PureComponent优化时必须传入新的数据，如果不适用优化可以直接修改原数据,一般来说都使用的是优化的开发写法。</p></div>  
</div>
            