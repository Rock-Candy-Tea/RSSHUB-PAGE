
---
title: '使用 Flutter 构建一个名言名句应用程序'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e689da1f5594b379ba11464ed16f3f3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 05:24:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e689da1f5594b379ba11464ed16f3f3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://medium.com/flutterdevs/flutter-quotes-app-bb30ef27b255" target="_blank" rel="nofollow noopener noreferrer">Flutter Quotes App</a></li>
<li>原文作者：<a href="https://medium.com/@danubhav" target="_blank" rel="nofollow noopener noreferrer">Anubhav Gupta</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/flutter-quotes-app.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/Hoarfroster" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/5Reasons" target="_blank" rel="nofollow noopener noreferrer">5Reasons</a>、<a href="https://github.com/greycodee" target="_blank" rel="nofollow noopener noreferrer">greycodee</a></li>
</ul>
</blockquote>
<h2 data-id="heading-0">引言</h2>
<p>在过去的 8 个月里，我一直在探索 Flutter。今天我将带着大家开始一段旅程，制作一个属于自己的简单而又漂亮的应用，并同时学会进行 API 请求。</p>
<h2 data-id="heading-1">目录 TOC</h2>
<blockquote>
<p>从互联网上获取数据。
设计应用程序的用户界面。
为文本设计样式。</p>
</blockquote>
<p>让我们开始……</p>
<h2 data-id="heading-2">初步设置</h2>
<p>在我们深入研究之前，不要忘记将这些包添加到你的项目中：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">animated_text_kit:</span> <span class="hljs-string">^3.1.0</span>
<span class="hljs-attr">google_fonts:</span> <span class="hljs-string">^1.1.1</span>
<span class="hljs-attr">http:</span> <span class="hljs-string">^0.12.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">创建一个新的 Flutter 项目</h2>
<p>打开你最喜欢的 IDE（VScode 或 Android Studio），创建一个新的 Flutter 应用，并给它取一个你喜欢的名字，保存在本地磁盘的某个地方。</p>
<p>首先我们删除掉默认生成的计数器应用代码，并创建一个主函数来运行我们的 Material 应用程序。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// main.dart</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter_quote_app/screens/home.dart'</span>;

<span class="hljs-keyword">void</span> main() &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-comment">// 你的应用程序 Widget 树的根 Widget</span>
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> MaterialApp(
        title: <span class="hljs-string">'名言名句应用程序'</span>,
        theme: ThemeData(
          primarySwatch: Colors.amber,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        debugShowCheckedModeBanner: <span class="hljs-keyword">false</span>,
        home: HomeScreen());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">通过 API 获取数据</h2>
<p>为了获得数据，我们需要一个 API 以获得名言名句的 JSON 格式的原始数据。</p>
<p>获取数据的 API 是 <a href="https://zenquotes.io/api/quotes" target="_blank" rel="nofollow noopener noreferrer"><strong>https://zenquotes.io/api/quotes</strong></a>。当你打开这个链接时，它会向你显示名言名句的原始数据。选择所有的文本复制一下，然后在另一个标签页中打开 <a href="https://app.quicktype.io/" target="_blank" rel="nofollow noopener noreferrer"><strong>quicktype</strong></a> 并粘贴进去，我们就可以立即生成我们的<strong>Dart Model</strong>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e689da1f5594b379ba11464ed16f3f3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将原始数据复制到左侧栏中，并给模型类命名：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// quotesmodel.dart</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'dart:convert'</span>;

<span class="hljs-built_in">List</span><Quotes> quotesFromJson(<span class="hljs-built_in">String</span> str) =>
  <span class="hljs-built_in">List</span><Quotes>.from(json.decode(str).map((x) => Quotes.fromJson(x)));

<span class="hljs-built_in">String</span> quotesToJson(<span class="hljs-built_in">List</span><Quotes> data) =>
  json.encode(<span class="hljs-built_in">List</span><<span class="hljs-built_in">dynamic</span>>.from(data.map((x) => x.toJson())));

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Quotes</span> </span>&#123;
  Quotes(&#123;
    <span class="hljs-keyword">this</span>.q,
    <span class="hljs-keyword">this</span>.a,
    <span class="hljs-keyword">this</span>.h,
  &#125;);

  <span class="hljs-built_in">String</span> q;
  <span class="hljs-built_in">String</span> a;
  <span class="hljs-built_in">String</span> h;

  <span class="hljs-keyword">factory</span> Quotes.fromJson(<span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">dynamic</span>> json) => Quotes(
      q: json[<span class="hljs-string">"q"</span>],
      a: json[<span class="hljs-string">"a"</span>],
      h: json[<span class="hljs-string">"h"</span>],
    );

  <span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">dynamic</span>> toJson() => &#123;
      <span class="hljs-string">"q"</span>: q,
      <span class="hljs-string">"a"</span>: a,
      <span class="hljs-string">"h"</span>: h,
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是生成的 Dart 模型类。</p>
<h3 data-id="heading-5">让我们创建一个函数来请求 API 获取数据</h3>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>

<span class="hljs-keyword">static</span> Future<<span class="hljs-built_in">List</span><Quotes>> fetchQuotes() <span class="hljs-keyword">async</span> &#123;
  <span class="hljs-keyword">final</span> response = <span class="hljs-keyword">await</span> http.<span class="hljs-keyword">get</span>(<span class="hljs-string">'https://zenquotes.io/api/quotes'</span>);
  <span class="hljs-keyword">if</span> (response.statusCode == <span class="hljs-number">200</span>) &#123;
    <span class="hljs-built_in">print</span>(quotesFromJson(response.body).length);
    <span class="hljs-keyword">return</span> quotesFromJson(response.body);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">throw</span> Exception(<span class="hljs-string">'失败加载名言名句'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，我们有一个异步方法，作出一个 GET 请求。如果响应的状态码是 <code>200</code>，它就会返回<strong>名言名句</strong>的列表，否则就抛出一个异常。</p>
<h2 data-id="heading-6">设计 UI</h2>
<p>现在我们已经准备好了所有的东西，让我们做一个漂亮的 UI 来显示我们的名言名句。</p>
<p>所以，首先要创建一个有状态的 Widget 作为 <strong>HomeScreen</strong> 界面。它将有一个 <strong>Widget</strong> 构建方法（返回一个 <code>Scaffold</code>）。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:animated_text_kit/animated_text_kit.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter_quote_app/models/qoutemodel.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:google_fonts/google_fonts.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:http/http.dart'</span> <span class="hljs-keyword">as</span> http;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomeScreen</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _HomeScreenState createState() => _HomeScreenState();
&#125;

PageController pageController = PageController(keepPage: <span class="hljs-keyword">true</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_HomeScreenState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">HomeScreen</span>> </span>&#123;
  <span class="hljs-comment">// 调用 API 并获取数据</span>
  <span class="hljs-keyword">static</span> Future<<span class="hljs-built_in">List</span><Quotes>> fetchQuotes() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> response = <span class="hljs-keyword">await</span> http.<span class="hljs-keyword">get</span>(<span class="hljs-string">'https://zenquotes.io/api/quotes'</span>);
    <span class="hljs-keyword">if</span> (response.statusCode == <span class="hljs-number">200</span>) &#123;
      <span class="hljs-built_in">print</span>(quotesFromJson(response.body).length);
      <span class="hljs-keyword">return</span> quotesFromJson(response.body);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> Exception(<span class="hljs-string">'获取名言名句失败'</span>);
    &#125;
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    fetchQuotes();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      body: Column(
        children: [
          Expanded(
            flex: <span class="hljs-number">8</span>,
            child: <span class="hljs-comment">/* TODO */</span>
          ),
          Expanded(
            child: Container(
              alignment: Alignment.center,
            ),
          ),
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们使用 <code>Column</code> 作为 <code>Scaffold</code> 的 <code>body</code> 属性值，包含两个 <code>Expanded</code> 子 Widget，一个有 <code>flex: 8</code>，另一个没有 <code>flex</code> 不过有一个 <code>Container</code> 作为子 Widget。</p>
<p>另外，如果你看到上面的代码，我们有一个 <code>void</code> 返回值的 <code>initState</code>。它将在我们导航到 <code>HomeScreen</code> 时运行。它有我们的 <code>fetchQuotes</code> 方法，在 Widget 被插入到树中之前被调用。</p>
<blockquote>
<p>由于我们使用的是API，所以我们将使用 <code>FutureBuilder</code>。</p>
</blockquote>
<blockquote>
<p>为什么要用这个东西呢？</p>
</blockquote>
<p>由于我们的 UI 会在应用运行后立即构建，但我们却无法立刻获取到来自 API 的<em><strong>响应</strong></em>，因此如果你的 UI 依赖于 API 响应值，那么它将会抛出很多的 <code>null</code> 错误。</p>
<h3 data-id="heading-7">让我们投奔 Future</h3>
<p><code>FutureBuilder</code> 也是一个 Widget，因此我们可以直接在我们的 <code>Scaffold</code> 上使用它，或者也可以把它作为一个子 Widget 连接到任何你喜欢的 Widget 上。在这里我将使用 <code>Expanded</code> Widget 作为 <code>FutureBuilder</code> 的父 Widget。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:animated_text_kit/animated_text_kit.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter_quote_app/models/qoutemodel.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:google_fonts/google_fonts.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:http/http.dart'</span> <span class="hljs-keyword">as</span> http;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomeScreen</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _HomeScreenState createState() => _HomeScreenState();
&#125;

PageController pageController = PageController(keepPage: <span class="hljs-keyword">true</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_HomeScreenState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">HomeScreen</span>> </span>&#123;
  <span class="hljs-comment">// 调用 API 并获取数据</span>
  <span class="hljs-keyword">static</span> Future<<span class="hljs-built_in">List</span><Quotes>> fetchQuotes() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> response = <span class="hljs-keyword">await</span> http.<span class="hljs-keyword">get</span>(<span class="hljs-string">'https://zenquotes.io/api/quotes'</span>);
    <span class="hljs-keyword">if</span> (response.statusCode == <span class="hljs-number">200</span>) &#123;
      <span class="hljs-built_in">print</span>(quotesFromJson(response.body).length);
      <span class="hljs-keyword">return</span> quotesFromJson(response.body);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> Exception(<span class="hljs-string">'失败加载名言名句'</span>);
    &#125;
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    fetchQuotes();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      body: Column(
        children: [
          Expanded(
            flex: <span class="hljs-number">8</span>,
            child: FutureBuilder<<span class="hljs-built_in">List</span><Quotes>>(
              future: fetchQuotes(),
              builder:
                  (BuildContext context, AsyncSnapshot<<span class="hljs-built_in">List</span><Quotes>> snapshot) &#123;
                <span class="hljs-keyword">if</span> (snapshot.connectionState == ConnectionState.done &&
                    snapshot.hasData) &#123;
                  <span class="hljs-keyword">return</span> buildPageView(snapshot);
                &#125; <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-keyword">return</span> Center(child: CircularProgressIndicator());
                &#125;
              &#125;,
            ),
          ),
          Expanded(
            child: Container(
              alignment: Alignment.center,
            ),
          ),
        ],
      ),
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FutureBuilder</code> 有两个主要属性：<code>future</code> 和 <code>builder</code>。这里我们将 <code>future</code> 赋值为 <code>fetchQuotes()</code> 方法以运行获取数据的函数并将结果返回给 <code>builder</code> 的 <code>snapshot</code>。现在只要用给出的结果创建任何你喜欢的 Widget 即可。</p>
<p>现在我想要的是这样的行为：当我在等待结果的时候，我想向用户显示一个 <code>CircularProgressIndicator</code>。而一旦有了返回的数据就立即显示名言名句页面。</p>
<p><code>FutureBuilder</code> 能帮助我们轻松实现：</p>
<pre><code class="hljs language-dart copyable" lang="dart">future: fetchQuotes(),          
builder: (BuildContext context, AsyncSnapshot<<span class="hljs-built_in">List</span><Quotes>> snapshot) &#123;
    <span class="hljs-keyword">if</span> (snapshot.connectionState == ConnectionState.done && snapshot.hasData) &#123;
       <span class="hljs-keyword">return</span> buildPageView(snapshot);
    &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-keyword">return</span> Center(child: CircularProgressIndicator());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们已经创建了我的 <code>PageView</code> Widget 构造器 <code>buildPageView()</code>，并将其传递给子 Widget。</p>
<h2 data-id="heading-8">样式化文本</h2>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// home.dart</span>

PageView buildPageView(AsyncSnapshot<<span class="hljs-built_in">List</span><Quotes>> snapshot) &#123;
    <span class="hljs-keyword">return</span> PageView.builder(
      controller: pageController,
      itemCount: snapshot.data.length,
      scrollDirection: Axis.vertical,
      itemBuilder: (BuildContext context, <span class="hljs-built_in">int</span> index) &#123;
        <span class="hljs-keyword">return</span> Container(
          <span class="hljs-comment">// height: MediaQuery.of(context).size.height * 0.87,</span>
          width: <span class="hljs-built_in">double</span>.infinity,
          decoration: BoxDecoration(
            color: Colors.amberAccent[<span class="hljs-number">700</span>],
            borderRadius: BorderRadius.only(
              topLeft: Radius.circular(<span class="hljs-number">20</span>),
              bottomLeft: Radius.circular(<span class="hljs-number">60</span>),
            ),
          ),
          padding: EdgeInsets.symmetric(horizontal: <span class="hljs-number">20</span>, vertical: <span class="hljs-number">30</span>),
          margin: EdgeInsets.only(bottom: <span class="hljs-number">10</span>),

          child: Stack(
            children: [
              Text(
                <span class="hljs-string">'名言名句应用程序'</span>,
                style: GoogleFonts.lobster(fontSize: <span class="hljs-number">45</span>, color: Colors.white),
              ),
              Align(
                alignment: Alignment.center,
                child: TyperAnimatedTextKit(
                  isRepeatingAnimation: <span class="hljs-keyword">false</span>,
                  repeatForever: <span class="hljs-keyword">false</span>,
                  displayFullTextOnTap: <span class="hljs-keyword">true</span>,
                  speed: <span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">150</span>),
                  onFinished: () &#123;
                    pageController.nextPage(
                      duration: <span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">1</span>),
                      curve: Curves.easeInOutCirc,
                    );
                  &#125;,
                  text: [<span class="hljs-string">'"'</span> + snapshot.data[index].q + <span class="hljs-string">'"'</span>],
                  textStyle: GoogleFonts.montserratAlternates(
                      fontSize: <span class="hljs-number">30.0</span>, color: Colors.white),
                ),
              ),
              Align(
                alignment: Alignment.bottomRight,
                child: Text(
                  snapshot.data[index].a,
                  style: GoogleFonts.lora(fontSize: <span class="hljs-number">14</span>),
                ),
              ),
            ],
          ),
        );
      &#125;,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 PageView 构造器中，我们使用了 <code>TyperAnimatedTextKit</code>，而你也需要导入这个包。在 <code>TyperAnimatedTextKit</code> 里面有一个函数，可以帮助我们在屏幕上输入完整的字符串时跳到下一页。另外，我们使用了 <strong>Google Fonts</strong>，你也需要导入同样的包。</p>
<p>// 等待上传 // <a href="https://miro.medium.com/max/1200/1*PvXgGVrBtx31_HFm_mcWtg.gif" target="_blank" rel="nofollow noopener noreferrer">miro.medium.com/max/1200/1*…</a></p>
<p>瞧! 您已经创建了第一个名言名句应用程序。</p>
<p>本文代码：<a href="https://github.com/flutter-devs/flutter_quote_app.git" target="_blank" rel="nofollow noopener noreferrer"><strong>flutter-devs/flutter_quote_app</strong></a></p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            