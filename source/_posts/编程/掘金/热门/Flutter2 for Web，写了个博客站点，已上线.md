
---
title: 'Flutter2 for Web，写了个博客站点，已上线'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f6cbdcf4e0405f80924414b2025eda~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 18 Mar 2021 03:59:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f6cbdcf4e0405f80924414b2025eda~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Flutter 迎来了它的的第二个大版本 <code>Flutter2</code>，其中最大变更之一就是对 Web 的生产质量有了新的支持，已经从 Beta 测试顺利转正。</p>
<p>常言道“是骡是马，拉出来溜溜”，写个项目验证下是非常有必要的。</p>
<blockquote>
<p>因在写本文时，已完成项目编写，可优先体验项目成果：<a href="http://webdemo.loveli.site/" target="_blank" rel="nofollow noopener noreferrer">webdemo.loveli.site</a></p>
<p>项目源码：<a href="https://github.com/swiftdo/web-demo" target="_blank" rel="nofollow noopener noreferrer">swiftdo/web-demo</a></p>
</blockquote>
<p>本项目将参照我的微信小程序 <code>OldBirds</code> 的功能，实现文章列表、文章详情、分类文章列表等页面，数据是通过 api 动态获取的。</p>
<blockquote>
<p>OldBirds 小程序里除了更新自己的博客外，也会推荐一些优质文章供大家阅读，欢迎体验</p>
</blockquote>
<p>那么下面将从零开始讲解这个项目的实现过程。因为从 0 到 1 也不是件容易的事情，所以会分 N 篇文章讲解。大体有以下内容：</p>
<ul>
<li>项目搭建</li>
<li>网络请求的封装</li>
<li>项目环境的封装</li>
<li>实现首页，请求跨域问题</li>
<li>状态管理封装</li>
<li>页面适配</li>
<li>路由2.0的封装</li>
<li>url 策略</li>
<li>项目打包、部署上线</li>
</ul>
<h2 data-id="heading-0">搭建环境，创建初始项目</h2>
<p>因本人习惯每个 Flutter 项目对应各自的 Flutter 版本，所以采用 <a href="https://github.com/leoafarias/fvm" target="_blank" rel="nofollow noopener noreferrer">fvm</a> 进行 Flutter 的版本管理。如果您不熟悉如何使用 fvm，不防阅读下我之前写的文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6935631938673721381" target="_blank">Flutter 2.0 顺滑撤回， web 初体验</a></li>
<li><a href="https://github.com/leoafarias/fvm" target="_blank" rel="nofollow noopener noreferrer">FVM 愉快的切换 Flutter 版本，强烈推荐！</a></li>
</ul>
<p>创建项目的大致命令如下：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ mkdir web-demo <span class="hljs-comment"># 创建目录</span>
$ <span class="hljs-built_in">cd</span> web-demo <span class="hljs-comment"># 进入目录</span>
$ fvm install stable  <span class="hljs-comment"># 安装flutter stable channel 的版本</span>
$ fvm use stable --force <span class="hljs-comment"># web-demo 使用 stable 版本</span>
$ fvm flutter create .  <span class="hljs-comment"># 生成以 web-demo 为项目名的工程</span>
$ fvm flutter run -d Chrome <span class="hljs-comment"># 运行到 Chrome 上</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当项目成功运行，自动打开浏览器显示页面的时候，说明我们成功的创建了 web-demo 工程。后面就是往项目中添砖加瓦，补充血液了。</p>
<h2 data-id="heading-1">项目结构规划</h2>
<p>那么接下来，我们一起搭建项目的基本骨架：</p>
<p><img alt="-w402" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f6cbdcf4e0405f80924414b2025eda~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>assets：images、files、fonts 等资源文件</li>
<li>components：存放的是公共组件，重业务型</li>
<li>config：项目的环境配置，比如 debug，product，preview 各环境的配置</li>
<li>core：轻业务型工具类，或者公共组件，可以方便移植到其他项目</li>
<li>models：模型类，json 数据解析</li>
<li>pages：页面</li>
<li>router：路由</li>
<li>services：一些第三方库的封装、网络请求等</li>
<li>style：公共的样式，颜色，字体，尺寸等</li>
</ul>
<p>以上的目录规划，是根据自己的经验总结划分的，你也可以按自己项目结构的来。但组件、页面、路由、资源、环境、服务基本上是达成了行业共识，很多项目都这么划分。</p>
<p>完成基本划分后，接下来，我们从哪里下手？</p>
<p>通常在开发的时候，我们会先有UI设计稿和需求文档，然后我们开始编写静态UI，待后端同学接口完成，继续对接接口，然后测试，改bug，发版。</p>
<p>本项目比较特殊，已有 API 接口和数据，所以我们可以优先封装网络请求。</p>
<h2 data-id="heading-2">网络封装</h2>
<p>Flutter 网络请求，通常会使用 <code>dio</code> 插件。</p>
<p>那么首先在 servers 目录下创建文件<code>api.dart</code>，定义一个接口 <code>Api</code>：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Api</span> </span>&#123;
  
  <span class="hljs-comment">/// <span class="markdown">获取文章列表</span></span>
  <span class="hljs-comment">/// <span class="markdown">[categoryId] 是文章分类id</span></span>
  Future<<span class="hljs-built_in">Map</span>> fetchArticleList(&#123;<span class="hljs-built_in">int</span> pageNo, <span class="hljs-built_in">int</span> pageSize = <span class="hljs-number">20</span>, <span class="hljs-built_in">String</span> categoryId&#125;);
  
  <span class="hljs-comment">/// <span class="markdown">获取文章详情</span></span>
  Future<<span class="hljs-built_in">Map</span>> fetchArticleDetail(&#123;<span class="hljs-built_in">String</span> articleId&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在定义一个实现类：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ApiImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Api</span> </span>&#123;
  Dio _dio;

  ApiImpl() &#123;
    _dio = Dio(
      BaseOptions(baseUrl: <span class="hljs-string">'baseurl.com'</span>, connectTimeout: <span class="hljs-number">20000</span>, receiveTimeout: <span class="hljs-number">20000</span>),
    );
  &#125;

  <span class="hljs-comment">/// <span class="markdown">接口请求</span></span>
  Future<<span class="hljs-built_in">Map</span>> fetchArticleList(&#123;<span class="hljs-built_in">int</span> pageNo, <span class="hljs-built_in">int</span> pageSize = <span class="hljs-number">20</span>, <span class="hljs-built_in">String</span> categoryId&#125;) <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> response = <span class="hljs-keyword">await</span> _dio.<span class="hljs-keyword">get</span>(<span class="hljs-string">'list'</span>, queryParameters: &#123;
      <span class="hljs-string">'pageNo'</span>: pageNo,
      <span class="hljs-string">'pageSize'</span>: pageSize,
      <span class="hljs-string">"category_id"</span>: categoryId,
    &#125;);
    <span class="hljs-built_in">Map</span> data = response.data;
    <span class="hljs-keyword">return</span> data;
  &#125;

  Future<<span class="hljs-built_in">Map</span>> fetchArticleDetail(&#123;<span class="hljs-built_in">String</span> articleId&#125;) <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> response = <span class="hljs-keyword">await</span> _dio.<span class="hljs-keyword">get</span>(<span class="hljs-string">'detail'</span>, queryParameters: &#123;
      <span class="hljs-string">'article_id'</span>: articleId,
    &#125;);
    <span class="hljs-built_in">Map</span> data = response.data;
    <span class="hljs-keyword">return</span> ValueUtil.toMap(data[<span class="hljs-string">'data'</span>]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是我们完成 dio 的二次封装。抽出 Api 基类，ApiImpl 进行实现，这样封装的好处是在调用 Api 的地方不需要 dio 的细节，然后如果你哪天不用 dio，用其他的请求库，那么你只需要改 <code>ApiImpl</code> 的实现即可。</p>
<p>那么上面的代码有没有比较突出的问题呢？我们一起来分析下</p>
<h2 data-id="heading-3">问题分析</h2>
<h3 data-id="heading-4">baseurl 问题</h3>
<p>代码中 ApiImpl 的 <code>baseurl.com</code> 是有问题的。因为在开发环境，我们可能用的是 <code>localhost</code>，在线上环境才是 <code>baseurl.com</code>。</p>
<p>那么很快有人会说可以通过 <code>kDebugMode</code> 区分正式环境或者是开发环境。</p>
<pre><code class="hljs language-dart copyable" lang="dart">BaseOptions(baseUrl: kDebugMode ? <span class="hljs-string">'localhost'</span>: <span class="hljs-string">'baseurl.com'</span>, connectTimeout: <span class="hljs-number">20000</span>, receiveTimeout: <span class="hljs-number">20000</span>),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果只有两个环境，确实可以这么干。但是如果有一天，新增了个预发布环境，那么这个时候 kDebugMode 就不受用了，无法通过 bool 类型去区分 3 种情况。</p>
<p>还有一种情况是，各环境除了 baseUrl 不一样，其他的一些配置如 <code>connectTimeout</code> 也可能需要不同的值，那么就会有很多<code>kDebugMode?:</code>的判断。</p>
<p>该如何解决？</p>
<p>对于 baseurl 的分析我们引出了2个问题：</p>
<ul>
<li>baseurl 的值跟环境有关</li>
<li>如果有多个值都跟环境有关，需要进行很多判断</li>
</ul>
<p>假设我们现在的 baseurl 有三个：</p>
<ol>
<li>在 debug 环境的时候，是 a.com</li>
<li>在 preview 环境的时候，是 b.com</li>
<li>在 product 环境的时候，是 c.com</li>
</ol>
<p>我们一开始的关注点在 baseurl，这次我们换个思考对象：环境。如果环境确定了，那么 baseurl 也就定了。我们可以沿着这个方向思考。</p>
<p><strong>那么我们如何确认环境？</strong></p>
<p>通常，有很多人是这么做的：</p>
<ul>
<li>env == 1, debug 环境</li>
<li>env == 2, preivew 环境</li>
<li>env == 3, product 环境</li>
</ul>
<p>然后通过设置 <code>env</code> 的值来确定环境（也有些人会使用枚举）。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">if</span> (env == <span class="hljs-number">1</span>) &#123;
    baseurl = <span class="hljs-string">"a.com"</span>;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (env == <span class="hljs-number">2</span>) &#123;
    baseurl = <span class="hljs-string">"b.com"</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (env == <span class="hljs-number">3</span>) &#123;
    baseurl = <span class="hljs-string">"c.com"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确实这样实现了我们的目的，但是跟环境有关的地方，就会充斥着各种 <code>if else</code> 判断，不是很优雅。傲娇的我们不喜欢。</p>
<p>既然变量不喜欢，那我们就整一个类吧，不就是要一个 baseurl，我们给你：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Config</span> </span>&#123;
    <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl; <span class="hljs-comment">/// <span class="markdown">这就是我们想要的</span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为整个应用只有一个环境，我们可以把它作为一个全局变量：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Config config = Config();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是 Config 是抽象类，所以我们不能直接赋值。我们需要 Config 的实现类，因为有三个环境，所以就实现三个 Config 子类：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConfigDebug</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Config</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl => <span class="hljs-string">"a.com"</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConfigPreview</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Config</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl => <span class="hljs-string">"b.com"</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConfigProduct</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Config</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl => <span class="hljs-string">"c.com"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果现在是 debug 环境，那么：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Config config = ConfigDebug();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在需要使用 <code>baseurl</code> 的地方，直接调用 <code>config.baseurl</code>，这个时候我们不再需要任何条件判断。如果我们还需要个客户环境，我们直接创建个 Config 的实现类即可。</p>
<p>还有刚上面说到的 <code>connectTimeout</code> 也跟环境有关系，那么可以在 Config 添加 <code>connectTimeout</code>：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Config</span> </span>&#123;
    <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl; <span class="hljs-comment">/// <span class="markdown">这就是我们想要的</span></span>
    <span class="hljs-built_in">int</span> <span class="hljs-keyword">get</span> connectTimeout = <span class="hljs-number">2000</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConfigProduct</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Config</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> baseurl => <span class="hljs-string">"c.com"</span>;
  
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">int</span> <span class="hljs-keyword">get</span> connectTimeout = <span class="hljs-number">6000</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码实现 debug 和 preview 环境的时候 connectTimeout 为 2000，在 product 环境的时候为 6000。</p>
<p>这样封装下来，是不是比全局 env 变量控制优雅多了？</p>
<h3 data-id="heading-5">调用问题</h3>
<p>对于我们封装好的 <code>ApiImpl</code> 该如何使用？相信你也看过或者写过类似代码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>
getList() <span class="hljs-keyword">async</span>&#123;
    <span class="hljs-keyword">var</span> res = <span class="hljs-keyword">await</span> ApiImpl().fetchArticleList(pageNo: pageNo);
    <span class="hljs-comment">//....</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样调用，确实可以完成接口的请求，项目完美跑起来。但是有想过更优雅的解决方案么？难道 <code>Api</code> 这个东西抽出成接口就没啥作用么？很多人会回答，<code>Api</code> 抽象类有啥作用，我就没有这个类，没啥卵用，直接 <code>class ApiImpl &#123;&#125;</code>。</p>
<p>真的没有价值么，一起来看看下面代码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> </span>&#123;
    Home(&#123;<span class="hljs-keyword">this</span>.api&#125;)
    <span class="hljs-keyword">final</span> Api api;    
    getList() <span class="hljs-keyword">async</span>&#123;
        <span class="hljs-keyword">var</span> res = <span class="hljs-keyword">await</span> api.fetchArticleList(pageNo: pageNo);
        <span class="hljs-comment">//....</span>
    &#125;
&#125;

Home(api: ApiImpl())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Home 只依赖了 Api，不需要跟 ApiImpl 产生关联。如果A在开发的时候，需要完成一个功能，但是这个功能又依赖了 B 写的代码，但 B 又还没时间实现。这个时候，我们需要将我们需要的功能抽象成接口，然后依赖这个抽象基类，这样，即使不提供实现，代码也可以正常编译。当然我们也可以写个临时的实现，让代码能够运行起来。待别人有时间，或者别人的模块已写好，对接相应的接口实现即可。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ApiMockImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Api</span> </span>&#123;&#125;

<span class="hljs-comment">// Home(api: ApiMockImpl())</span>
Home(api: ApiImpl())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写代码就不怕被别人耽误，同时代码的灵活度也提升了。</p>
<p>对于上面的代码，如果只有 Home 这一个类，改起来还是挺容易的，但是像网络请求这种，可能就会散落在 N 处，那么我们就需要将 N 处 <code>ApiMockImpl</code> 替换为 <code>ApiImpl</code>，是不是很蛋疼。要是能只改一个地方就好了，接下来我们就这个问题给出了实现方案。</p>
<h3 data-id="heading-6">依赖注入</h3>
<pre><code class="hljs language-dart copyable" lang="dart">Config config = ConfigDebug();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局变量对于我们来说，是程序数据 “同步” 的最方便最快捷的方式。</p>
<ul>
<li>内存地址固定，读写效率比较高。</li>
<li>全局可见，任何一个函数或线程都可以读写全局变量</li>
</ul>
<p>非常简单灵活，然后太过自由，修改的风险性就越高。全局变量破坏了函数的封装性能，由于多个函数都可能使用全局变量，函数执行时全局变量的值可能随时发生变化，那么同样的输入就不一定有同样的输出。对于程序的查错和调试都非常不利，可靠性大打折扣。</p>
<pre><code class="hljs language-sh copyable" lang="sh">如果不是万不得已，最好不要使用全局变量
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以怎么办？可以采用单例。但是我们 Config 不适合作为一个单例。所以我们需要一个单例对象，然后 Config 作为其一个属性。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SomeSharedInstance</span> </span>&#123;
    <span class="hljs-comment">// 单例公开访问点</span>
  <span class="hljs-keyword">factory</span> SomeSharedInstance() =>_sharedInstance()
  
  <span class="hljs-comment">// 静态私有成员，没有初始化</span>
  <span class="hljs-keyword">static</span> SomeSharedInstance _instance;
  
  <span class="hljs-comment">// 私有构造函数</span>
  SomeSharedInstance._() &#123;
    <span class="hljs-comment">// 具体初始化代码</span>
  &#125;

  <span class="hljs-comment">// 静态、同步、私有访问点</span>
  <span class="hljs-keyword">static</span> SomeSharedInstance _sharedInstance() &#123;
    <span class="hljs-keyword">if</span> (_instance == <span class="hljs-keyword">null</span>) &#123;
      _instance = SomeSharedInstance._();
    &#125;
    <span class="hljs-keyword">return</span> _instance;
  &#125;  
  
  Config config;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在使用config 的时候，我们需要做类似操作：</p>
<pre><code class="hljs language-dart copyable" lang="dart">SomeSharedInstance()
    ..config = ConfigDebug();
    
<span class="hljs-comment">// SomeSharedInstance().config.baseurl;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我个人觉得一个普通应用就一个单例基本够用。</p>
</blockquote>
<p>写到这里，强烈推荐一个插件 <a href="https://github.com/fluttercommunity/get_it" target="_blank" rel="nofollow noopener noreferrer">get_it</a>，非常适合我们现在这个场景。将创建的代码解耦。</p>
<blockquote>
<p>服务定位模式（Service Locator Pattern）是一种软件开发中的设计模式，通过应用强大的抽象层，可对涉及尝试获取一个服务的过程进行封装。该模式使用一个称为"Service Locator"的中心注册表来处理请求并返回处理特定任务所需的必要信息.
来自: <a href="https://www.cnblogs.com/gaochundong/archive/2013/04/12/service_locator_pattern.html" target="_blank" rel="nofollow noopener noreferrer">Service Locator 模式</a></p>
</blockquote>
<p>在 lib 目录下创建 <code>locator.dart</code>：</p>
<pre><code class="hljs language-dart copyable" lang="dart">
GetIt locator = GetIt.instance;

setupLocator() &#123;
  <span class="hljs-comment">// 配置项目环境</span>
  <span class="hljs-keyword">if</span> (kDebugMode) &#123;
    locator.registerSingleton<Config>(ConfigDebug());
  &#125; <span class="hljs-keyword">else</span> &#123;
    locator.registerSingleton<Config>(ConfigProduct());
  &#125;
  <span class="hljs-comment">/// <span class="markdown">这里就实现了改一处实现全局替换</span></span>
  locator.registerLazySingleton<Api>(() => ApiImpl());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了服务的注册。然后在 <code>main.dart</code> 中调用 <code>setupLocator()</code>:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() <span class="hljs-keyword">async</span> &#123;
  WidgetsFlutterBinding.ensureInitialized();
  <span class="hljs-keyword">await</span> setupLocator();
  runApp(MyApp());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在需要使用服务的时候，如需要获取 Config 的配置，直接调用 <code>locator<Config>()</code> 即可：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ApiImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Api</span> </span>&#123;
  Dio _dio;

  ApiImpl() &#123;
    _dio = Dio(
      BaseOptions(baseUrl: locator<Config>().baseUrl, connectTimeout: <span class="hljs-number">20000</span>, receiveTimeout: <span class="hljs-number">20000</span>),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有也顺带解决了 <code>ApiImpl</code> 的调用可能多处修改的问题。</p>
<pre><code class="hljs language-dart copyable" lang="dart">getList() <span class="hljs-keyword">async</span>&#123;
    <span class="hljs-keyword">var</span> res = <span class="hljs-keyword">await</span> locator<Api>().fetchArticleList(pageNo: pageNo);
    <span class="hljs-comment">//....</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多 get_it 的使用，可以参考其<a href="https://pub.dev/packages/get_it" target="_blank" rel="nofollow noopener noreferrer">文档</a>。</p>
<h2 data-id="heading-7">章节总结</h2>
<p>本文我们带大家实现了：</p>
<ul>
<li>网络请求的封装</li>
<li>项目环境的封装</li>
</ul>
<p>在封装过程中，我们不断的让代码变得优雅些、灵活些。设计是个不断迭代的过程，不断的优化，思考就能离目标越来越近。</p>
<p>总之，切记：以抽象为基准比以细节为基准搭建起来的架构要稳定得多，因此在拿到需求后，要面相接口编程，先顶层设计再细节地设计代码结构。</p>
<p>最后本项目的源码已上传到 github 中：<a href="https://github.com/swiftdo/web-demo" target="_blank" rel="nofollow noopener noreferrer">swiftdo/web-demo</a></p>
<p>如果想加入微信交流群的话，请关注微信公众号：<strong>OldBirds</strong></p>
<p>当然文章可能有理解不当的地方，欢迎大牛们指出。下一章节我们将会讲状态管理的内容，敬请期待！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            