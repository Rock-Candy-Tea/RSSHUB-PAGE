
---
title: '理解SSR以及实践于Vue（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40d94bc76b374df19b76bc099bd9251b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:11:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40d94bc76b374df19b76bc099bd9251b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>今天我们的主题是：<strong>Vue SSR</strong>，这个名词相信我们大家都不陌生，但是现在我们做的一些项目并不会都去使用，那SSR具体是怎么实现呢？又什么时候用才好呢？今天我们就从Vue中的SSR的实现来入手，完整的走一遍流程，一起来吧～</p>
<p>PS：Vue-SSR将会分为三部分完成：理解SSR以及实践于Vue（上）、Vue中同构开发SSR应用（中）、Nuxt.js实践（下）</p>
<h2 data-id="heading-1">什么是SSR</h2>
<p>SSR全称为服务端渲染（Server Side Render），ennnn，那我们又该问了？什么又是服务端渲染呢？先别急，我们来从web开发的一步步发展开始讲起～</p>
<h2 data-id="heading-2">传统web开发</h2>
<p>我们都知道，web的开发工作在开始之初其实基本都是后端开发者完成的，那时候甚至来说都还没有前端开发工程师这个职位，那时候都是前后端不分离（如jsp这种），也就是说网页内容是在服务端渲染完成之后，再一次性传输到浏览器。</p>
<p>我们画一张图来大概表示一下这个过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40d94bc76b374df19b76bc099bd9251b~tplv-k3u1fbpfcp-watermark.image" alt="传统web开发.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图我们应该可以了解到传统的web开发的模式，接下来我们就使用node来构建简单的服务端来模拟一下以前的方式：</p>
<p>node服务端的代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">"express"</span>)
<span class="hljs-keyword">const</span> app = express()

app.get(<span class="hljs-string">"/"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.send(<span class="hljs-string">`<h3>hello,guangying</h3>`</span>);
&#125;);

app.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"server running..."</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将其运行起来然后右键显示网页源代码，我们可以看到结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/516b6db27f0242ffba72adea4c54888d~tplv-k3u1fbpfcp-watermark.image" alt="传统web开发的结果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么结合上面的描述，我们发现这种方式浏览器拿到的是全部完整的DOM结构</p>
<h2 data-id="heading-3">单页应用SPA（Single Page App）</h2>
<p>由于传统的开发模式导致的结果是用户体验不是太好，而单页应用的优秀用户体验，让其逐渐发展为主流，页面内容由JS渲染出来，这种方式我们也称为<strong>客户端渲染</strong></p>
<p>我们同样也画一张图来展示一下大概过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64c0a7a1be6040c7b431ef402653b9e8~tplv-k3u1fbpfcp-watermark.image" alt="SPA开发.png" loading="lazy" referrerpolicy="no-referrer">
通过上图我们发现：相较于传统web开发，SPA的方式如果要完整的呈现在用户面前，那么最少都需要经历两次网络请求，因为第一次的时候服务器返回给客户端的只是页面骨架，并没有实际的内容，真正的内容是要等到客户端执行js代码之后才会生成的</p>
<p>这里我们以Vue为例，通过node来模拟一下该种方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()

app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> html = <span class="hljs-string">`
    <div id="app">
      <h3>hello, &#123;&#123;name&#125;&#125;</h3>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue(&#123;
        el: '#app',
        data:&#123;
          name: 'guangying'
        &#125;
      &#125;)
    </script>
  `</span>
  res.send(html)
&#125;)

app.listen(<span class="hljs-number">3030</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'server running2...'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们同样来通过查看网页源代码的方式检查一下，如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7513b3d05aa04799bc2c018e6504e33c~tplv-k3u1fbpfcp-watermark.image" alt="SPA开发结果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过分析，我们基本上能够得出SPA方式的优缺点：</p>
<p>优点：</p>
<ul>
<li>渲染计算放到客户端，这样减轻了服务端的压力</li>
<li>由于是单页面应用，会节省一部分流量</li>
</ul>
<p>缺点：</p>
<ul>
<li>首屏加载速度慢，尤其是网络环境不好的情况下</li>
<li>不利于搜索引擎的SEO</li>
</ul>
<h2 data-id="heading-4">服务端渲染SSR（Server Side Render）</h2>
<p>由于前两种方式存在的缺陷，于是便有了SSR，它相当于是位于前两者之间，SSR解决方案是：服务端渲染出完整的首屏DOM结构返回，前端能拿到的内容包括首屏以及完整的SPA结构，应用激活后仍然按照SPA方式运行，这种渲染方式就是SSR</p>
<p>PS：</p>
<ul>
<li>简单点说那就是前两者之间的结合和改善</li>
<li>这里要提及一个概念——首屏！首屏！首屏！重要的事情说三遍，不是单纯的首页，这里感觉很容易混淆</li>
</ul>
<p>同样我们也来画一个图来展示一下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202837a907024bbfbf395bcb32d739ea~tplv-k3u1fbpfcp-watermark.image" alt="SSR开发.png" loading="lazy" referrerpolicy="no-referrer">
我们通过学习SSR的过程，我们发现他解决了前两者的问题，因为首屏是在服务端进行渲染的，SEO是可以正确拿到结果的；同时首屏在渲染完成传回客户端的时候，SSR同样也能携带如路由信息，状态管理信息等等到前端，简单点说就是传回来前端的就是首屏全部的结构以及SPA方式该有的结构，这样首屏渲染也就得到了改善</p>
<p>接下来我们就以Vue为例，进行Vue SSR的实践：</p>
<p>1、安装依赖：Vue中的服务端渲染模块：vue-server-renderer</p>
<p>PS:注意安装依赖的时候要保证Vue和vue-server-renderer的版本一致</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install vue-server-renderer@<span class="hljs-number">2.6</span><span class="hljs-number">.10</span> -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、运行脚本：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()

<span class="hljs-comment">// 1、导入Vue</span>
<span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue'</span>)

<span class="hljs-comment">// 2、导入createRenderer并且获取渲染器</span>
<span class="hljs-keyword">const</span> &#123;createRenderer&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-server-renderer'</span>)
<span class="hljs-keyword">const</span> renderer = createRenderer()

app.get(<span class="hljs-string">'*'</span>, <span class="hljs-keyword">async</span> (req, res) => &#123;
  <span class="hljs-comment">// 3、创建一个待渲染的Vue实例</span>
  <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <h1>hello,&#123;&#123;name&#125;&#125;</h1>
    `</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'guangying'</span>
      &#125;
    &#125;,
  &#125;)
  <span class="hljs-keyword">try</span> &#123;   
    <span class="hljs-comment">// renderToString将vue实例渲染为html字符串，它返回⼀个Promise</span>
    <span class="hljs-keyword">const</span> html = <span class="hljs-keyword">await</span> renderer.renderToString(vm)
    <span class="hljs-comment">// 返回html给客户端</span>
    res.send(html)
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(error)
  &#125;
&#125;)

app.listen(<span class="hljs-number">3333</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sever running3'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写完之后我们运行，同样查看网页源代码，如图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1b10782861e4cd49995e718b19bd405~tplv-k3u1fbpfcp-watermark.image" alt="SSR开发结果.png" loading="lazy" referrerpolicy="no-referrer">
我们可以发现这时候我们得到了完整的DOM结构，但是我们注意红框中的属性，这是给Vue的，有了这个信息，Vue就知道这是服务端渲染的内容，将来在做激活的时候就有了凭证</p>
<p>我们现在这个例子是最基本的一个SSR例子，接下来我们来看看接入Vue-router之后的情况：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()

<span class="hljs-comment">// 1、导入Vue</span>
<span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue'</span>)
<span class="hljs-comment">// 引⼊vue-router</span>
<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-router'</span>)
Vue.use(Router)

<span class="hljs-keyword">const</span> &#123;createRenderer&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-server-renderer'</span>)
<span class="hljs-keyword">const</span> renderer = createRenderer()

<span class="hljs-comment">// path修改为通配符</span>
app.get(<span class="hljs-string">'*'</span>, <span class="hljs-keyword">async</span> (req, res) => &#123;
  <span class="hljs-comment">// 每次创建⼀个路由实例</span>
  <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> Router(&#123;
    <span class="hljs-attr">routes</span>: [
      &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: &#123;<span class="hljs-attr">template</span>: <span class="hljs-string">'<h1>这是首页</h1>'</span>&#125;&#125;,
      &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/detail'</span>, <span class="hljs-attr">component</span>: &#123;<span class="hljs-attr">template</span>: <span class="hljs-string">'<h1>这是详情</h1>'</span>&#125;&#125;
    ]
  &#125;)
  <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-comment">// 添加router-view显示内容</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h1>hello,&#123;&#123;name&#125;&#125;</h1>
      <router-link to="/">首页</router-link>
      <router-link to="/detail">详情</router-link>
      <router-view></router-view>
      </div>
    `</span>,
    router,    <span class="hljs-comment">// 挂载</span>
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'guangying'</span>
      &#125;
    &#125;,
  &#125;)
  <span class="hljs-keyword">try</span> &#123;   
    <span class="hljs-comment">// 跳转⾄对应路由</span>
    router.push(req.url)
    <span class="hljs-keyword">const</span> html = <span class="hljs-keyword">await</span> renderer.renderToString(vm)
    res.send(html)
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(error)
  &#125;
&#125;)

app.listen(<span class="hljs-number">3333</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sever running3'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实讲到这里，我们关于Vue SSR的基本实践已经差不多了，但是我们想一想我们现在这样的写法会有哪些问题呢？</p>
<p>比如我们这么写是将服务端和前端混合在了一起，这样我们的开发负担会增加，同时代码不美观不容易维护，能不能让我们按照以前熟悉的Vue方式开发呢？</p>
<p>再比如如果我们想添加用户事件怎么让其生效呢？因为现在就是返回HTML字符串，直接按照熟悉的Vue方式写是无效的，换句话说那就是怎么激活后续的客户端呢？</p>
<p>这一篇我们主要就是介绍SSR的基本定义和基本实践，我们要先弄明白他的实现原理和实现的过程，下一篇我们继续学习如何使用同构的方式来完成<strong>服务端渲染</strong>和<strong>客户端激活</strong></p>
<h2 data-id="heading-5">文末</h2>
<p>欢迎关注「<strong>前端光影</strong>」公众号，公众号都是以系统专题模块的形式来展示的，这样看起来就会比较方便，系统，让我们一起持续学习各种前端知识，加油！</p></div>  
</div>
            