
---
title: 'VUE SSR常见问题，优化及异常处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4317'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:12:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=4317'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>ssr的意思是服务端渲染，前端还没有流行的时候，之前的网站是在服务端拼接HTML字符串，将其返回呈现在页面
vue ssr优点：<br>
vue ssr做的是在页面中请求url的时候，会从服务端渲染返回一个渲染好的html字符串，将首屏所需要的数据异步请求，填充发到前端展示，而不是发一个壳子，ssr是一份代码运行在两个环境里面（服务端、客户端），服务端先运行好之后，把模板渲染成html页面，然后返回给前端，前端再载入js文件，完成激活，后续的操作就是spa了，这样第一个页面是服务端渲染的带数据的，seo爬虫就能获取到数据，同时因为首屏只渲染一个页面，后续激活spa是发生在浏览器端，首屏渲染问题也得到解决。</p>
<p>vue ssr缺点：<br>
在配置过程中比较复杂，需要配置两个入口文件，一个是服务端首屏渲染所需要的，第二个是前端激活所需要的，有nuxt.js可以更容易实现ssr</p>
<p>相比于单纯的spa，服务端渲染加重了服务器的负担，当用户量多的时候，因为需要在后端创建全新的vue实例，所以比单纯请求数据浪费性能。<br>
虽然 Vue 的服务器端渲染(SSR)相当快速，但是由于创建组件实例和虚拟 DOM 节点的开销，无法与纯基于字符串拼接的模板的性能相当。在 SSR 性能至关重要的情况下，明智地利用缓存策略，可以极大改善响应时间并减少服务器负载，对组件页面接口进行缓存。</p>
<p>前后端同构，在后端就需要写前端vue的代码，与前后端分离相违背，这个可以通过webpack打包实现，只需要配置入口文件以及相应的逻辑就可以。</p>
<p>缓存和运维的问题。</p>
<p><br>
应用场景：<br>
并不是所有的网站都需要SEO，比如企业内部网站，后天管理系统等。<br>
一些vue老项目，重构成本太大，首屏渲染可以通过路由懒加载，按需加载的方式，修改对应的问题，不全盘扳倒重写。<br>
在服务器返回结果之前，可以做处理判断是否是爬虫，来决定进行预渲染</p>
<h3 data-id="heading-0">SSR的应用场景</h3>
<h4 data-id="heading-1">1.SEO需求</h4>
<p>SEO（Search Engine Optimization，搜索引擎优化），是一种利用搜索引擎规则，提高网站在搜索引擎内自然排名的技术。通常这需要页面内容在页面加载完成时便已经存在。SEO需求的存在与互联网技术的发展历程密不可分。在互联网产生之初，网页使用超文本链接协议，将服务器的信息传递给客户端。而后出现了专门为人们检索信息的搜索引擎。随着前端技术的不断发展，出现了前后端分离的纯前端项目，由于这类项目需要页面加载完成后再异步获取数据渲染，因此大部分搜索引擎无法获取到这类项目的内容。Vue SSR正是基于此类需求而给出的一种技术方案。利用nodejs搭建页面渲染服务，在服务端完成之前需要在客户端完成的页面渲染工作，输出给SEO更友好的页面。</p>
<p>除Vue SSR方案外，也可以选择Prerender（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprerender%2Fprerender%25EF%25BC%2589%25E4%25BD%259C%25E4%25B8%25BA%25E6%259B%25BF%25E4%25BB%25A3%25E6%2596%25B9%25E6%25A1%2588%25E3%2580%2582Prerender%25E5%2592%258CVue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/prerender/prerender%EF%BC%89%E4%BD%9C%E4%B8%BA%E6%9B%BF%E4%BB%A3%E6%96%B9%E6%A1%88%E3%80%82Prerender%E5%92%8CVue" ref="nofollow noopener noreferrer">github.com/prerender/p…</a> SSR的相同点是都需要在服务端完成页面的渲染，不同点在于Prerender采用无界面虚拟浏览器Phantomjs去渲染输出页面，而Vue SSR是基于vue组件的渲染。相比来说Prerender的通用性更强，任何页面都适用，而Vue SSR则只适用于vue项目，但由于Vue SSR是基于代码层面的直接渲染，不需要像Prerender那样再去拉取静态资源，因此速度更快。</p>
<p>至于应该使用哪一种技术方案，就要视需求和实际情况取舍了。</p>
<h4 data-id="heading-2">2.首屏渲染速度</h4>
<p>如在上面SEO需求中提到的，目前前后端的分离的前端项目需要先加载静态资源，再异步获取数据，最后渲染页面，在这个过程中的前两部页面都是没有数据的，影响了首屏的渲染速度，也就影响了用户的体验。 目前对于首屏渲染速度的提升有许多方案，在ssr之外还有龙骨，墓碑，数据直出。相比于这些方案ssr方案实现是最复杂的，但效果也是最好的。</p>
<h4 data-id="heading-3">3.Vue SSR方案的选择</h4>
<p>目前Vue SSR的实现有两种实现，一种是基于官方Vue SSR指南文档的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fssr.html%23SSR-%25E5%25AE%258C%25E5%2585%25A8%25E6%258C%2587%25E5%258D%2597" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/ssr.html#SSR-%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97" ref="nofollow noopener noreferrer">官方方案</a>，一种是vue.js通用应用框架--NUXT。 官方方案具有更直接的控制应用程序的结构，更深入底层，更加灵活，同时在使用官方方案的过程中，也会对Vue SSR有更加深入的了解。 而NUXT提供了平滑的开箱即用的体验，它建立在同等的Vue技术栈之上，但抽象出很多模板，并提供了一些额外的功能，例如静态站点生成。通过NUXT可以根据约定的规则，快速的实现Vue SSR。</p>
<h3 data-id="heading-4">开发中容易遇到的一些问题</h3>
<h5 data-id="heading-5">1.一套代码两套执行环境</h5>
<p>vue的生命周期钩子函数中， 只有 <strong>beforeCreate</strong>和 <strong>created</strong> 会在服务器端渲染(SSR)过程中被调用，这就是说在这两个钩子函数中的代码以及除了vue生命周期钩子函数的全局代码，都将会在<strong>服务端和客户端两套环境</strong>下执行。如果在两套环境的代码中加入具有副作用的代码或访问特定平台的API，将出现各种问题。比如服务端没有window、document对象， 如果加了对这个对象的引用和操作，将在服务端引起报错中断。</p>
<p>因此，总结起来，最容易犯的错误就是不判断环境就去使用window、document对象。</p>
<p>解决方案：</p>
<p>（1）在beforeCreate，created生命周期以及全局的执行环境中调用特定的api前需要<strong>判断执行环境</strong>；</p>
<p>（2）使用adapter模式，写一套adapter<strong>兼容不同环境的api</strong>。</p>
<h5 data-id="heading-6">2.服务端数据的预获取</h5>
<p>官方方案使用<strong>Vuex</strong>在服务端预获取数据。 在服务端添加vue钩子函数，获取数据后，将数据保存在vuex的store结构中，同时渲染页面。</p>
<p>在数据预获取阶段注册的钩子函数中，最好只进行数据的获取和保存，不进行其他任何涉及this的操作。因为此时的this是服务端的this，是所有用户共享的this，进行操作将发生一些不可预知的错误。</p>
<p>举个例子，比如想在数据预获取的钩子函数中操作data数据。 首先，数据预获取的钩子函数在运行时还没有vue的实例，因此根本拿不到关于vue实例的任何东西；其次，进行的存取操作都是在所有用户的公共变量下进行的，一旦成功进行了存取操作，必然是所有用户的存取操作。</p>
<p>同时需要注意的是，vuex在Vue SSR方案下，应使用<strong>惰性注册</strong>的方案。如果不使用惰性注册方案，而是在一开始vuex初始化实例的时候就把所有的模块统一注册，将会出现多个页面共用许多模块的问题。</p>
<p>如我们有store模块如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-comment">// store/modules/foo.js</span>
 <span class="hljs-number">2</span> <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-number">3</span>  namespaced: <span class="hljs-literal">true</span>,
 <span class="hljs-number">4</span>  <span class="hljs-comment">// 重要信息：state 必须是一个函数，</span>
 <span class="hljs-number">5</span>  <span class="hljs-comment">// 因此可以创建多个实例化该模块</span>
 <span class="hljs-number">6</span>  state: <span class="hljs-function">() =></span> (&#123;
 <span class="hljs-number">7</span>    count: <span class="hljs-number">0</span>
 <span class="hljs-number">8</span>  &#125;),
 <span class="hljs-number">9</span>  actions: &#123;
<span class="hljs-number">10</span>    inc: <span class="hljs-function">(<span class="hljs-params">&#123; commit &#125;</span>) =></span> commit(<span class="hljs-string">'inc'</span>)
<span class="hljs-number">11</span>  &#125;,
<span class="hljs-number">12</span>  mutations: &#123;
<span class="hljs-number">13</span>    inc: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count++
<span class="hljs-number">14</span>  &#125;
<span class="hljs-number">15</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则在路由组件内，需要按如下代码惰性注册vuex模块</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-comment">// 在路由组件内</span>
 <span class="hljs-number">2</span> <template>
 <span class="hljs-number">3</span>  <div>&#123;&#123; fooCount &#125;&#125;</div>
 <span class="hljs-number">4</span> </template>
 <span class="hljs-number">5</span> <script>
 <span class="hljs-number">6</span> <span class="hljs-comment">// 在这里导入模块，而不是在 `store/index.js` 中</span>
 <span class="hljs-number">7</span> <span class="hljs-keyword">import</span> fooStoreModule <span class="hljs-keyword">from</span> <span class="hljs-string">'../store/modules/foo'</span>
 <span class="hljs-number">8</span> <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-number">9</span>  <span class="hljs-comment">// 数据预获取生命周期，在服务端运行</span>
<span class="hljs-number">10</span>  asyncData (&#123; store &#125;) &#123;
<span class="hljs-number">11</span>    <span class="hljs-comment">//惰性注册store模块</span>
<span class="hljs-number">12</span>    store.registerModule(<span class="hljs-string">'foo'</span>, fooStoreModule)
<span class="hljs-number">13</span>    <span class="hljs-comment">//执行foo命名空间下名为inc的action操作</span>
<span class="hljs-number">14</span>    <span class="hljs-keyword">return</span> store.dispatch(<span class="hljs-string">'foo/inc'</span>)
<span class="hljs-number">15</span>  &#125;,
<span class="hljs-number">16</span>  <span class="hljs-comment">// 重要信息：当多次访问路由时，</span>
<span class="hljs-number">17</span>  <span class="hljs-comment">// 避免在客户端重复注册模块。</span>
<span class="hljs-number">18</span>  destroyed () &#123;
<span class="hljs-number">19</span>    <span class="hljs-built_in">this</span>.$store.unregisterModule(<span class="hljs-string">'foo'</span>)
<span class="hljs-number">20</span>  &#125;,
<span class="hljs-number">21</span>  computed: &#123;
<span class="hljs-number">22</span>    fooCount () &#123;
<span class="hljs-number">23</span>      <span class="hljs-comment">//获取store数据</span>
<span class="hljs-number">24</span>      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.foo.count
<span class="hljs-number">25</span>    &#125;
<span class="hljs-number">26</span>  &#125;
<span class="hljs-number">27</span> &#125;
<span class="hljs-number">28</span> </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结起来就是，在服务端预获取数据的钩子函数中，不要进行额外的操作，任何对于数据的额外操作都要在vuex的体系下进行，vuex在Vue SSR方案下，应使用惰性注册的方案。</p>
<h5 data-id="heading-7">3.接口代理的问题</h5>
<p>由于前端平时开发时的接口很多都是线下的，因此需要对于接口的地址进行代理切换。我们平时用的最多的是fiddler和charles等端口代理软件。但是ssr在数据预获取时走的是服务端，不是浏览器，因此不能通过这两个工具进行代理。</p>
<p>办法有两个，一个是修改服务器的host地址，这个方法在开发阶段只需要更改本机的host就好，但是在提测阶段需要修改服务器的host，如果两个项目在同一个机器上测试，将不可避免的造成冲突。 第二个方法是使用axios的代理功能，因为axios对于ssr有天然的适配性，因此99%的项目都会用它。而它自带的proxy功能，可以帮助我们方便的做接口代理。</p>
<p>代理配置文件如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-comment">// config/dev-host</span>
 <span class="hljs-number">2</span> <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-number">3</span>   https: <span class="hljs-string">'192.168.183.80'</span>,
 <span class="hljs-number">4</span>   http: <span class="hljs-string">'192.168.183.80'</span>
 <span class="hljs-number">5</span> &#125;
 <span class="hljs-number">6</span> 代理设置代码如下：
 <span class="hljs-number">7</span> <span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
 <span class="hljs-number">8</span> <span class="hljs-keyword">import</span> https <span class="hljs-keyword">from</span> <span class="hljs-string">'https'</span>;
 <span class="hljs-number">9</span> <span class="hljs-keyword">import</span> devHost <span class="hljs-keyword">from</span> <span class="hljs-string">'../config/dev-host'</span>;
<span class="hljs-number">10</span> 
<span class="hljs-number">11</span> <span class="hljs-keyword">let</span> proxy = <span class="hljs-function">(<span class="hljs-params">isDev</span>) =></span> &#123;
<span class="hljs-number">12</span>  <span class="hljs-keyword">if</span> (!isDev) &#123;
<span class="hljs-number">13</span>    <span class="hljs-keyword">return</span>;
<span class="hljs-number">14</span>  &#125;
<span class="hljs-number">15</span>  <span class="hljs-keyword">let</span> proxy = <span class="hljs-literal">null</span>;
<span class="hljs-number">16</span>  <span class="hljs-keyword">if</span> (devHost.https) &#123;
<span class="hljs-number">17</span>    <span class="hljs-comment">//如果存在https的代理，则设置https的代理</span>
<span class="hljs-number">18</span>    proxy = &#123;
<span class="hljs-number">19</span>      host: devHost.https,
<span class="hljs-number">20</span>      port: <span class="hljs-number">443</span>
<span class="hljs-number">21</span>    &#125;;
<span class="hljs-number">22</span>    <span class="hljs-comment">//可以配置忽略https的证书认证</span>
<span class="hljs-number">23</span>    Axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
<span class="hljs-number">24</span>      config.httpsAgent = <span class="hljs-keyword">new</span> https.Agent(&#123;<span class="hljs-attr">rejectUnauthorized</span>: <span class="hljs-literal">false</span>&#125;);
<span class="hljs-number">25</span>      <span class="hljs-keyword">return</span> config;
<span class="hljs-number">26</span>    &#125;);
<span class="hljs-number">27</span>    Axios.defaults.proxy = proxy;
<span class="hljs-number">28</span>  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (devHost.http) &#123;
<span class="hljs-number">29</span>    <span class="hljs-comment">//如果存在http的代理，则设置http的代理</span>
<span class="hljs-number">30</span>    proxy = &#123;
<span class="hljs-number">31</span>      host: devHost.http,
<span class="hljs-number">32</span>      port: <span class="hljs-number">80</span>
<span class="hljs-number">33</span>    &#125;;
<span class="hljs-number">34</span>    Axios.defaults.proxy = proxy;
<span class="hljs-number">35</span>  &#125;
<span class="hljs-number">36</span> &#125;
<span class="hljs-number">37</span> <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> proxy
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">4.cookie穿透</h5>
<p>由于客户端的http请求首先达到SSR服务器，再由SSR服务器去后端服务器获取相应的接口数据。在客户端到SSR服务器的请求中，客户端是携带有cookie数据的。但是在SSR服务器请求后端接口的过程中，却是没有相应的cookie数据的。因此在SSR服务器进行接口请求的时候，我们需要手动拿到客户端的cookie传给后端服务器。这里如果使用是axios，就可以手动设置axios请求的headers字段，达到cookie穿透的目的。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-keyword">let</span> addCookie = <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
 <span class="hljs-number">2</span>    <span class="hljs-comment">// 判断客户端请求中是否携带cookie</span>
 <span class="hljs-number">3</span>    <span class="hljs-keyword">if</span>(!process.browser && config.req && config.req.headers && config.req.headers.cookie)&#123;
 <span class="hljs-number">4</span>        <span class="hljs-comment">//将客户端请求携带的cookie添加到SSR服务端请求的header中</span>
 <span class="hljs-number">5</span>        config.headers =  config.headers || &#123;&#125;;
 <span class="hljs-number">6</span>        config.headers.cookie = config.req.headers.cookie;
 <span class="hljs-number">7</span>        <span class="hljs-keyword">delete</span> config.req;
 <span class="hljs-number">8</span>    &#125;
 <span class="hljs-number">9</span>    <span class="hljs-keyword">return</span> config;
<span class="hljs-number">10</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">5.路由模式</h5>
<p>vue有两种路由模式，一种是hash模式，就是我们经常用的#/hasha/hashb这种，还有一种是history模式，就是/historya/historyb这种。因为hash模式的路由提交不到服务器上，因此ssr的路由需要采用history的方式。</p>
<h3 data-id="heading-10">异常处理问题</h3>
<h5 data-id="heading-11">1.异常来自哪里？</h5>
<p>（1）服务端数据预获取过程中的异常，如接口请求的各种异常，获取到数据后对数据进行操作的过程中出现的错误异常。</p>
<p>（2）在服务端数据预获取的生命周期结束后的渲染页面过程中出现的异常，包括各种操作数据的语法错误等，如对undefined取属性。</p>
<h5 data-id="heading-12">2.怎么处理异常</h5>
<p>（1）官方处理方法</p>
<p>抛出500错误页面，体验不友好，产品不接受。</p>
<p>（2）目前采用的方法</p>
<p>a.服务端数据预获取过程中出现的异常，让页面继续渲染，不抛出500异常页面，打错误日志，接入监控。同时，在页面加入标志，让前端页面再次进行一次数据获取页面渲染的尝试。</p>
<p>b.页面渲染过程的异常。由于目前渲染过程是vue提供的一个插件进行的，异常不好捕获，同时出现问题的概率不是很大，因此还没有做专门的处理。</p>
<p>代码如下：</p>
<p>entry-server.js服务端部分：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-built_in">Promise</span>.all(matchedComponents.map(<span class="hljs-function"><span class="hljs-params">component</span> =></span> &#123;
 <span class="hljs-number">2</span>    <span class="hljs-comment">//代码略，参见官方文档</span>
 <span class="hljs-number">3</span> &#125;)).then(<span class="hljs-function">() =></span> &#123;
 <span class="hljs-number">4</span>    <span class="hljs-comment">//代码略，参见官方文档</span>
 <span class="hljs-number">5</span> &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
 <span class="hljs-number">6</span>    <span class="hljs-comment">//官方代码在这里直接抛出异常，从而走500错误页面</span>
 <span class="hljs-number">7</span>    <span class="hljs-comment">//我们做如下处理，首先打印错误日志，将日志加入监控报警，监控异常</span>
 <span class="hljs-number">8</span>    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rendererror'</span>,<span class="hljs-string">'entry-server'</span>,err);
 <span class="hljs-number">9</span>    <span class="hljs-comment">// 其次，增加服务端预渲染错误标识，前端拿到标志后重新渲染</span>
<span class="hljs-number">10</span>    context.serverError = <span class="hljs-literal">true</span>;
<span class="hljs-number">11</span>    <span class="hljs-comment">//最后，将服务端vue实例正常返回，避免抛500</span>
<span class="hljs-number">12</span>    resolve(app)
<span class="hljs-number">13</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.template.html页面模板部分增加如下js代码：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-number">1</span> <span class="hljs-comment">// 服务端渲染错误标识</span>
 <span class="hljs-number">2</span> <span class="hljs-built_in">window</span>.__serverRenderError = &#123;&#123;serverError || <span class="hljs-literal">false</span>&#125;&#125;;    
 <span class="hljs-number">3</span> entry-client.js客户端部分：
 <span class="hljs-number">4</span> <span class="hljs-comment">// ...忽略无关代码</span>
 <span class="hljs-number">5</span> router.onReady(<span class="hljs-function">(<span class="hljs-params">currentRoute</span>) =></span> &#123;
 <span class="hljs-number">6</span>    <span class="hljs-comment">// ...忽略无关代码</span>
 <span class="hljs-number">7</span>    <span class="hljs-comment">//如果拿到服务端的错误状态，则执行客户端渲染程序</span>
 <span class="hljs-number">8</span>    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.__serverRenderError)&#123;
 <span class="hljs-number">9</span>        feCompatibleRende(currentRoute);
<span class="hljs-number">10</span>    &#125;
<span class="hljs-number">11</span>    app.$mount(<span class="hljs-string">'#app'</span>);
<span class="hljs-number">12</span> &#125;)    
<span class="hljs-number">13</span> 
<span class="hljs-number">14</span> <span class="hljs-comment">// node报错时前端路由重渲染</span>
<span class="hljs-number">15</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">feCompatibleRende</span>(<span class="hljs-params">route</span>)</span>&#123;
<span class="hljs-number">16</span>    <span class="hljs-keyword">let</span> matched = router.getMatchedComponents(route);
<span class="hljs-number">17</span>    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'前端兼容渲染执行'</span>);
<span class="hljs-number">18</span>    <span class="hljs-built_in">Promise</span>.all(matched.map(<span class="hljs-function"><span class="hljs-params">c</span> =></span> &#123;
<span class="hljs-number">19</span>        <span class="hljs-keyword">if</span> (c.preFetch) &#123;
<span class="hljs-number">20</span>            <span class="hljs-keyword">return</span> c.preFetch(&#123;
<span class="hljs-number">21</span>                store,
<span class="hljs-number">22</span>                route,
<span class="hljs-number">23</span>                req: &#123;
<span class="hljs-number">24</span>                    headers: &#123;
<span class="hljs-number">25</span>                        cookie: <span class="hljs-built_in">document</span>.cookie
<span class="hljs-number">26</span>                    &#125;
<span class="hljs-number">27</span>                &#125;
<span class="hljs-number">28</span>            &#125;)
<span class="hljs-number">29</span>        &#125;
<span class="hljs-number">30</span>    &#125;)).then(<span class="hljs-function">() =></span> &#123;
<span class="hljs-number">31</span>        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ok'</span>);
<span class="hljs-number">32</span>    &#125;).catch(<span class="hljs-function">(<span class="hljs-params">e</span>)=></span>&#123;
<span class="hljs-number">33</span>        <span class="hljs-built_in">console</span>.error(e);
<span class="hljs-number">34</span>    &#125;)
<span class="hljs-number">35</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：总结起来一句话，为了更好的体验，不要出现500。</p>
<h3 data-id="heading-13">性能</h3>
<p>ssr可以提高首屏加载的速度，减少白屏时间，通过以下设置可以提高性能，减少服务器资源的占用，加快访问速度。</p>
<p>（1）页面级别的缓存 将渲染完成的页面缓存到内存中，同时设置最大缓存数量和缓存时间。 优势：大幅度提高页面的访问速度 代价：增加服务器内存的使用</p>
<p>**</p>
<pre><code class="copyable"> 1 const LRU = require('lru-cache');//删除最近最少使用条目的缓存对象
 2 // 实例化配置缓存对象
 3 const microCache = LRU(&#123;
 4  max: 100,//最大存储100条
 5  maxAge: 1000 // 存储在 1 秒后过期
 6 &#125;)
 7 //http请求处理
 8 server.get('*', (req, res) => &#123;
 9  //根据url获取缓存页面    
10  const hit = microCache.get(req.url)
11  //如果有缓存则直接返回缓存数据
12  if (hit) &#123;
13    return res.end(hit)
14  &#125;
15  renderer.renderToString((err, html) => &#123;
16    res.end(html)
17    //将页面缓存到缓存对象中
18    microCache.set(req.url, html)
19  &#125;)
20 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2）组件级别的缓存 适用：纯静态组件，v-for中循环的子组件</p>
<ol>
<li><code>在大多数情况下，你不应该也不需要缓存单一实例组</code></li>
</ol>
<p>（3）接口级别的缓存</p>
<p>**</p>
<pre><code class="copyable"> 1 适用：通用性强的接口
 2 
 3  将通用的接口缓存到内存，减少服务端接口请求的时间
 4 代码如下：
 5 import axios from 'axios'
 6 import qs from 'qs'
 7 import md5 from 'md5'
 8 
 9 const LRU = require('lru-cache');//删除最近最少使用条目的缓存对象
10 const microCache = LRU(&#123;
11  max: 100,//最大存储100条
12  maxAge: 1000 // 存储在 1 秒后过期
13 &#125;)
14 
15 export default &#123;
16  get(url, data) &#123;
17    //通过 url 和参数, 生成一个唯一的 key
18    const key = md5(url + JSON.stringify(data))
19    //如果命中缓存则返回缓存
20    if (microCache.has(key)) &#123;
21      return Promise.resolve(microCache.get(key))
22    &#125;
23    return axios.get(url,&#123;params:data&#125;).then(res => &#123;
24      //如果需要缓存，则缓存
25      if (data.cache) microCache.set(key, res)
26      return res
27    &#125;)
28  &#125;
29 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">安全</h3>
<p>因为做了node服务，因此安全方面也需要考虑。</p>
<p>(1)DDOS攻击</p>
<p>最基本的DDOS攻击就是利用合理的服务请求来占用过多的服务资源，从而使合法用户无法得到服务的响应</p>
<p>应对：</p>
<p>1.提升硬件设备</p>
<p>硬件性能越好，提供的服务并发能力越强，这样即使有小量的DDOS攻击也可以不影响正常用户的访问。</p>
<p>2.在服务端只做最基本的处理</p>
<p>在服务端不做过多复杂的数据处理，可以有效的提高ssr的性能。</p>
<p>3.日志只打印关键部位的关键信息</p>
<p>打印日志过多将耗费服务器资源，影响服务器的性能。</p>
<p>4.DDOS流量清洗</p>
<p>部署流量清洗相关设备，可以对网络中的DDoS攻击流量进行清除，同时保证正常流量的通过。</p>
<p>5.DDOS软硬件防火墙</p>
<p>软件防火墙解决方案为将软件防火墙部署到被保护的服务器上，优点是成本低、方便、灵活，缺点是作用有限、占用资源。</p>
<p>硬件防火墙解决方案为安装防火墙硬件，优点是效果好，缺点是成本高。</p>
<p>(2)sql注入</p>
<p>就是通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令 例如： 游戏pc详情页的代码为<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgame.zhuanzhuan.com%2Fdetail%2F1001306437923405830%3Fmetric%3De32aeb1b742c27af0ec80cef4b51b65" target="_blank" rel="nofollow noopener noreferrer" title="http://game.zhuanzhuan.com/detail/1001306437923405830?metric=e32aeb1b742c27af0ec80cef4b51b65" ref="nofollow noopener noreferrer">game.zhuanzhuan.com/detail/1001…</a></p>
<p>而攻击者将url替换为<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgame.zhuanzhuan.com%2Fdetail%2Fselect%2520*%2520from%2520user%3Fmetric%3De32aeb1b742c27af0ec80cef4b51b65" target="_blank" rel="nofollow noopener noreferrer" title="http://game.zhuanzhuan.com/detail/select%20*%20from%20user?metric=e32aeb1b742c27af0ec80cef4b51b65" ref="nofollow noopener noreferrer">game.zhuanzhuan.com/detail/sele…</a></p>
<p>应对：
1.对参数进行校验</p>
<p>在服务端的entry文件中添加校验代码，执行组件的校验规则</p>
<p>**</p>
<pre><code class="copyable"> 1  // 执行组件的校验方法
 2  let isValid = true
 3  Components.forEach((Component) => &#123;
 4    if (!isValid) return
 5    if (typeof Component.options.validate !== 'function') return
 6    isValid = Component.options.validate(app.context)
 7  &#125;)
 8  //验证不通过则返回404
 9  if (!isValid) &#123;
10    // Render a 404 error page
11    return render404Page()
12  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3)数据泄露</p>
<p>使用vuex的情况下，如果不使用惰性加载，容易造成数据泄露的情况发生。</p>
<p>关于任何需要登录获取数据的情况，建议不在服务端进行，只在客户端进行</p></div>  
</div>
            