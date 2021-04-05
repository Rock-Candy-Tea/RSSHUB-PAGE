
---
title: 'Flutter Getx 01 - 路由、中间件、鉴权、传值、跳转'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94e4168674040e0b59021ba5df75b2d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 02:20:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94e4168674040e0b59021ba5df75b2d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94e4168674040e0b59021ba5df75b2d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">Getx</h1>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19b2de245e55497a886cdc0cdcc79569~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f4aeb35d7b341e5b4b614e6adf4ea90~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><a href="https://pub.flutter-io.cn/packages/get" target="_blank" rel="nofollow noopener noreferrer">pub.flutter-io.cn/packages/ge…</a></p>
<p><a href="https://marketplace.visualstudio.com/items?itemName=get-snippets.get-snippets" target="_blank" rel="nofollow noopener noreferrer">vscode 插件</a></p>
<p><a href="https://plugins.jetbrains.com/plugin/14975-getx-snippets" target="_blank" rel="nofollow noopener noreferrer">Android Studio/Intellij 插件</a></p>
<h1 data-id="heading-1">本节目标</h1>
<ul>
<li>GetPage 对象</li>
<li>路由层级控制</li>
<li>路由中间件、鉴权</li>
<li>404 处理</li>
<li>路由跳转、替换、清除</li>
<li>路由传值、返回值</li>
<li>路由转场动画</li>
</ul>
<h2 data-id="heading-2">开发环境</h2>
<ul>
<li>Flutter 2.1.0-12.1.pre</li>
<li>Dart 2.13.0</li>
<li>get: ^3.26.0</li>
</ul>
<h2 data-id="heading-3">参考</h2>
<ul>
<li><a href="https://github.com/jonataslaw/getx/tree/master/example" target="_blank" rel="nofollow noopener noreferrer">getx example</a></li>
<li><a href="https://kauemurakami.github.io/getx_pattern/" target="_blank" rel="nofollow noopener noreferrer">getx_pattern</a></li>
<li><a href="https://marketplace.visualstudio.com/items?itemName=get-snippets.get-snippets" target="_blank" rel="nofollow noopener noreferrer">GetX Snippets</a></li>
</ul>
<h2 data-id="heading-4">视频</h2>
<p><a href="https://www.bilibili.com/video/BV1yU4y1876r/" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1yU…</a></p>
<h2 data-id="heading-5">代码</h2>
<p><a href="https://github.com/ducafecat/getx_quick_start" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/g…</a></p>
<h2 data-id="heading-6">正文</h2>
<h3 data-id="heading-7">初始 getx 项目</h3>
<ul>
<li>pubspec.yaml</li>
</ul>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">dependencies:</span>
  <span class="hljs-string">...</span>
  <span class="hljs-attr">get:</span> <span class="hljs-string">^3.26.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:get/get.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomeView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> HomeView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"首页"</span>),
      ),
      body: ListView(
        children: [
          <span class="hljs-comment">// 路由&导航</span>
          Divider(),

        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_routes.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">part</span> of <span class="hljs-string">'app_pages.dart'</span>;

<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppRoutes</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> Home = <span class="hljs-string">'/home'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:get/get.dart'</span>;

<span class="hljs-keyword">part</span> <span class="hljs-string">'app_routes.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppPages</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> INITIAL = AppRoutes.Home;

  <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> routes = [
    GetPage(
      name: AppRoutes.Home,
      page: () => HomeView(),
    ),
  ];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/main.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">Future<<span class="hljs-keyword">void</span>> main() <span class="hljs-keyword">async</span> &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyApp(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> GetMaterialApp(
      debugShowCheckedModeBanner: <span class="hljs-keyword">false</span>,
      initialRoute: AppPages.INITIAL,
      getPages: AppPages.routes,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">编写 GetPage 定义</h3>
<ul>
<li>lib/pages/list/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ListView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> ListView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"列表页"</span>),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/list_detail/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DetailView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> DetailView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"详情页"</span>),
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text(<span class="hljs-string">"导航-返回"</span>),
            subtitle: Text(<span class="hljs-string">'Get.back()'</span>),
            onTap: () => Get.back(),
          ),
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_routes.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppRoutes</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> Home = <span class="hljs-string">'/home'</span>;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> <span class="hljs-built_in">List</span> = <span class="hljs-string">'/list'</span>;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> Detail = <span class="hljs-string">'/detail'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">    GetPage(
      name: AppRoutes.Home,
      page: () => HomeView(),
      children: [
        GetPage(
          name: AppRoutes.<span class="hljs-built_in">List</span>,
          page: () => ListView(),
          children: [
            GetPage(
              name: AppRoutes.Detail,
              page: () => DetailView(),
            ),
          ],
        ),
      ],
    ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">导航操作 命名、视图对象</h3>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-命名路由 home > list"</span>),
    subtitle: Text(<span class="hljs-string">'Get.toNamed("/home/list")'</span>),
    onTap: () => Get.toNamed(<span class="hljs-string">"/home/list"</span>),
  ),
  ListTile(
    title: Text(<span class="hljs-string">"导航-命名路由 home > list > detail"</span>),
    subtitle: Text(<span class="hljs-string">'Get.toNamed("/home/list/detail")'</span>),
    onTap: () => Get.toNamed(<span class="hljs-string">"/home/list/detail"</span>),
  ),
  ListTile(
    title: Text(<span class="hljs-string">"导航-类对象"</span>),
    subtitle: Text(<span class="hljs-string">"Get.to(DetailView())"</span>),
    onTap: () => Get.to(DetailView()),
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">导航-清除上一个</h3>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-清除上一个"</span>),
    subtitle: Text(<span class="hljs-string">"Get.off(DetailView())"</span>),
    onTap: () => Get.off(DetailView()),
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">导航-清除所有</h3>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-清除所有"</span>),
    subtitle: Text(<span class="hljs-string">"Get.offAll(DetailView())"</span>),
    onTap: () => Get.offAll(DetailView()),
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">导航-arguments 传值+返回值</h3>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-arguments传值+返回值"</span>),
    subtitle: Text(
        <span class="hljs-string">'Get.toNamed("/home/list/detail", arguments: &#123;"id": 999&#125;)'</span>),
    onTap: () <span class="hljs-keyword">async</span> &#123;
      <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">await</span> Get.toNamed(<span class="hljs-string">"/home/list/detail"</span>,
          arguments: &#123;<span class="hljs-string">"id"</span>: <span class="hljs-number">999</span>&#125;);
      Get.snackbar(<span class="hljs-string">"返回值"</span>, <span class="hljs-string">"success -> "</span> + result[<span class="hljs-string">"success"</span>].toString());
    &#125;,
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/list_detail/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  _buildBackListTileRow(<span class="hljs-built_in">Map?</span> val) &#123;
    <span class="hljs-keyword">return</span> val == <span class="hljs-keyword">null</span>
        ? Container()
        : ListTile(
            title: Text(<span class="hljs-string">"传值 id = "</span> + val[<span class="hljs-string">"id"</span>].toString()),
            subtitle: Text(<span class="hljs-string">'Get.back(result: &#123;"success": true&#125;'</span>),
            onTap: () => Get.back(result: &#123;<span class="hljs-string">"success"</span>: <span class="hljs-keyword">true</span>&#125;),
          );
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">final</span> details = Get.arguments <span class="hljs-keyword">as</span> <span class="hljs-built_in">Map</span>;
    <span class="hljs-keyword">final</span> parameters = Get.parameters;

    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"详情页"</span>),
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text(<span class="hljs-string">"导航-返回"</span>),
            subtitle: Text(<span class="hljs-string">'Get.back()'</span>),
            onTap: () => Get.back(),
          ),
          _buildBackListTileRow(details),
          _buildBackListTileRow(parameters),
        ],
      ),
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">导航-parameters 传值+返回值</h3>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-parameters传值+返回值"</span>),
    subtitle: Text(<span class="hljs-string">'Get.toNamed("/home/list/detail?id=666")'</span>),
    onTap: () <span class="hljs-keyword">async</span> &#123;
      <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">await</span> Get.toNamed(<span class="hljs-string">"/home/list/detail?id=666"</span>);
      Get.snackbar(<span class="hljs-string">"返回值"</span>, <span class="hljs-string">"success -> "</span> + result[<span class="hljs-string">"success"</span>].toString());
    &#125;,
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/list_detail/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">final</span> parameters = Get.parameters;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">导航-参数传值+返回值</h3>
<ul>
<li>lib/common/routes/app_routes.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> Detail_ID = <span class="hljs-string">'/detail/:id'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ...
  GetPage(
    name: AppRoutes.Detail_ID,
    page: () => DetailView(),
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-参数传值+返回值"</span>),
    subtitle: Text(<span class="hljs-string">'Get.toNamed("/home/list/detail/777")'</span>),
    onTap: () <span class="hljs-keyword">async</span> &#123;
      <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">await</span> Get.toNamed(<span class="hljs-string">"/home/list/detail/777"</span>);
      Get.snackbar(<span class="hljs-string">"返回值"</span>, <span class="hljs-string">"success -> "</span> + result[<span class="hljs-string">"success"</span>].toString());
    &#125;,
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">导航-not found</h3>
<ul>
<li>lib/pages/notfound/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NotfoundView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> NotfoundView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"路由没有找到"</span>),
      ),
      body: ListTile(
        title: Text(<span class="hljs-string">"返回首页"</span>),
        subtitle: Text(<span class="hljs-string">'Get.offAllNamed(AppRoutes.Home)'</span>),
        onTap: () => Get.offAllNamed(AppRoutes.Home),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_routes.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> NotFound = <span class="hljs-string">'/notfound'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> unknownRoute = GetPage(
    name: AppRoutes.NotFound,
    page: () => NotfoundView(),
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/main.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> GetMaterialApp(
      ...
      unknownRoute: AppPages.unknownRoute,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">导航-中间件-认证 Auth</h3>
<ul>
<li>lib/pages/login/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> LoginView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"登录"</span>),
      ),
      body: ListTile(
        title: Text(<span class="hljs-string">"返回首页"</span>),
        subtitle: Text(<span class="hljs-string">'Get.offAllNamed(AppRoutes.Home)'</span>),
        onTap: () => Get.offAllNamed(AppRoutes.Home),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/my/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyView(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"我的"</span>),
      ),
      body: ListTile(
        title: Text(<span class="hljs-string">"返回首页"</span>),
        subtitle: Text(<span class="hljs-string">'Get.offAllNamed(AppRoutes.Home)'</span>),
        onTap: () => Get.offAllNamed(AppRoutes.Home),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_routes.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> Login = <span class="hljs-string">'/login'</span>;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> My = <span class="hljs-string">'/my'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/middleware/router_auth.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RouteAuthMiddleware</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">GetMiddleware</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">int</span> priority = <span class="hljs-number">0</span>;

  RouteAuthMiddleware(&#123;<span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.priority&#125;);

  <span class="hljs-meta">@override</span>
  RouteSettings? redirect(<span class="hljs-built_in">String</span> route) &#123;
    Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">1</span>), () => Get.snackbar(<span class="hljs-string">"提示"</span>, <span class="hljs-string">"请先登录APP"</span>));
    <span class="hljs-keyword">return</span> RouteSettings(name: AppRoutes.Login);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">    <span class="hljs-comment">// 白名单</span>
    GetPage(
      name: AppRoutes.Login,
      page: () => LoginView(),
    ),

    GetPage(
      name: AppRoutes.My,
      page: () => MyView(),
      middlewares: [
        RouteAuthMiddleware(priority: <span class="hljs-number">1</span>),
      ],
    ),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lib/pages/home/index.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  ListTile(
    title: Text(<span class="hljs-string">"导航-中间件-认证Auth"</span>),
    subtitle: Text(<span class="hljs-string">'Get.toNamed(AppRoutes.My)'</span>),
    onTap: () => Get.toNamed(AppRoutes.My),
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Transition 转场动画</h3>
<ul>
<li>lib/common/routes/app_pages.dart</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  GetPage(
    name: AppRoutes.Detail_ID,
    page: () => DetailView(),
    transition: Transition.downToUp,
  ),
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>© 猫哥</p>
<p><a href="https://ducafecat.tech/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech</a></p>
<p><a href="https://ducafecat.gitee.io/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.gitee.io</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            