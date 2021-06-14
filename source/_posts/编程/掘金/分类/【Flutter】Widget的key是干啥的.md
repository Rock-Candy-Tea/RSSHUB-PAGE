
---
title: '【Flutter】Widget的key是干啥的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab4a2d3fd68640ce88df1d91efbb0d69~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 01:06:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab4a2d3fd68640ce88df1d91efbb0d69~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>之前入门一些Flutter应用的时候，总是会遇到<code>GlobalKey</code>这个类，当时我只从代码的语法上感知到这个东西肯定是用来绑定某些东西的，但至于key这东西是啥？为什么要绑定？不绑定的话会怎么样？为什么有的<code>Widget</code>实现需要绑定有有的不需要？这些统统都不知道。</p>
<p>于是趁着端午有时间，就认真翻了下官方文档，发现官方文档说得非常详细（前提是你对Flutter的控件树有一定理解），上面的问题基本都回答到，可惜的是官方是用视频（YouToBe）讲解的，这不便于忘记的时候速读翻阅，于是我就整理成这篇博客顺便加固下印象。</p>
<blockquote>
<ul>
<li>官方doc：<a href="https://api.flutter.dev/flutter/foundation/Key-class.html" target="_blank" rel="nofollow noopener noreferrer">api.flutter.dev/flutter/fou…</a></li>
<li>如果你不了解Flutter的控件树：<a href="https://juejin.cn/post/6844903837858283528" target="_blank">juejin.cn/post/684490…</a></li>
<li>本文demo代码：<a href="https://github.com/mimajiushi/flutter_key_demo" target="_blank" rel="nofollow noopener noreferrer">github.com/mimajiushi/…</a></li>
<li>强烈建议先了解Flutter的三颗树知识，不然有些逻辑你可能会觉得很绕。</li>
</ul>
</blockquote>
<hr>
<h1 data-id="heading-1">key是什么</h1>
<p>key的作用是：控制weidget树上的widget是否被替换（刷新）</p>
<p>如果两个weidget的<a href="https://api.flutter.dev/flutter/dart-core/Object/runtimeType.html" target="_blank" rel="nofollow noopener noreferrer">runtimeType</a>和<a href="https://api.flutter.dev/flutter/widgets/Widget/key.html" target="_blank" rel="nofollow noopener noreferrer">key</a>属性相等（用<a href="https://api.flutter.dev/flutter/widgets/Widget/operator_equals.html" target="_blank" rel="nofollow noopener noreferrer">==</a>比较），那么原本指向旧weidge的element，它的指针会指向新的widget上（通过<a href="https://api.flutter.dev/flutter/widgets/Element/update.html" target="_blank" rel="nofollow noopener noreferrer">Element.update方法</a>）。如果不相等，那么旧element会从树上移除，根据当前新的widget重新构建新element，并加到树上指向新widget。</p>
<p>我们可以看下代码是不是这么回事：
<code>Element.update</code></p>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-meta">@mustCallSuper</span>
  <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">update</span><span class="hljs-params">(covariant Widget newWidget)</span> </span>&#123;
    <span class="hljs-comment">// This code is hot when hot reloading, so we try to</span>
    <span class="hljs-comment">// only call _AssertionError._evaluateAssertion once.</span>
    <span class="hljs-keyword">assert</span>(_lifecycleState == _ElementLifecycle.active
        && widget != <span class="hljs-keyword">null</span>
        && newWidget != <span class="hljs-keyword">null</span>
        && newWidget != widget
        && depth != <span class="hljs-keyword">null</span>
        && Widget.canUpdate(widget, newWidget));
    <span class="hljs-comment">// This Element was told to update and we can now release all the global key</span>
    <span class="hljs-comment">// reservations of forgotten children. We cannot do this earlier because the</span>
    <span class="hljs-comment">// forgotten children still represent global key duplications if the element</span>
    <span class="hljs-comment">// never updates (the forgotten children are not removed from the tree</span>
    <span class="hljs-comment">// until the call to update happens)</span>
    <span class="hljs-keyword">assert</span>(() &#123;
      _debugForgottenChildrenWithGlobalKey.forEach(_debugRemoveGlobalKeyReservation);
      _debugForgottenChildrenWithGlobalKey.clear();
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;());
    _widget = newWidget;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入上面的<code>Widget.canUpdate</code></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">static</span> <span class="hljs-built_in">bool</span> canUpdate(Widget oldWidget, Widget newWidget) &#123;
    <span class="hljs-keyword">return</span> oldWidget.runtimeType == newWidget.runtimeType
        && oldWidget.key == newWidget.key;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到判断逻辑基本与文档一致，这里有个值得注意的是：<strong><span><code>Widget</code>本身不会调用<code>Widget.canUpdate</code>，这个方法是由<code>Element</code>负责调用的，也就是<code>Widget</code>能不能更新，最终还是<code>Element</code>说了算</span></strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab4a2d3fd68640ce88df1d91efbb0d69~tplv-k3u1fbpfcp-zoom-1.image" alt="相等时.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a245663012164527815a1bb8cd2fbfb2~tplv-k3u1fbpfcp-zoom-1.image" alt="不相等时.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相信看到这里你已经明白key是啥以及它的作用了，but <code>talk is cheap show me the code</code>，那么我们怎么证明这理论是对的呢？下面就给出了代码demo。</p>
<hr>
<h1 data-id="heading-2">什么时候会用到key</h1>
<h2 data-id="heading-3">建一个demo先</h2>
<p>下面先举一个不需要用key的例子，代码逻辑是，集合的元素顺序变更后，控件要跟着变化，代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'dart:math'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-keyword">void</span> main() &#123;
  runApp(<span class="hljs-keyword">new</span> MaterialApp(home: PositionedTiles()));
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PositionedTiles</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  State<StatefulWidget> createState() => PositionedTilesState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PositionedTilesState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">PositionedTiles</span>> </span>&#123;
  <span class="hljs-built_in">List</span><Widget> tiles;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    tiles = [
      <span class="hljs-comment">// StatefulColorfulTile(),</span>
      <span class="hljs-comment">// StatefulColorfulTile(),</span>
      <span class="hljs-comment">// StatefulColorfulTile(key: UniqueKey()),</span>
      <span class="hljs-comment">// StatefulColorfulTile(key: UniqueKey()),</span>
      StatelessColorfulTile(),
      StatelessColorfulTile(),
    ];
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      body: SafeArea(
        child: Row(
          children: tiles,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.sentiment_very_satisfied),
        <span class="hljs-comment">// child: Icon(Icons.sentiment_very_dissatisfied),</span>
        onPressed: swapTiles,
      ),
    );
  &#125;

  <span class="hljs-keyword">void</span> swapTiles() &#123;
    setState(() &#123;
      tiles.insert(<span class="hljs-number">1</span>, tiles.removeAt(<span class="hljs-number">0</span>));
    &#125;);
  &#125;
&#125;

<span class="hljs-comment">// ignore: must_be_immutable</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StatelessColorfulTile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  Color color = ColorUtil.randomColor();

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Container(
        color: color,
        child: Padding(padding: EdgeInsets.all(<span class="hljs-number">70.0</span>))
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StatefulColorfulTile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  StatefulColorfulTile(&#123;Key key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  State<StatefulWidget> createState() => StatefulColorfulTileState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StatefulColorfulTileState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">StatefulColorfulTile</span>> </span>&#123;
  Color color;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    color = ColorUtil.randomColor();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Container(
        color: color,
        child: Padding(padding: EdgeInsets.all(<span class="hljs-number">70.0</span>))
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ColorUtil</span> </span>&#123;
  <span class="hljs-keyword">static</span> Color randomColor() &#123;
    <span class="hljs-keyword">var</span> red = Random.secure().nextInt(<span class="hljs-number">255</span>);
    <span class="hljs-keyword">var</span> greed = Random.secure().nextInt(<span class="hljs-number">255</span>);
    <span class="hljs-keyword">var</span> blue = Random.secure().nextInt(<span class="hljs-number">255</span>);
    <span class="hljs-keyword">return</span> Color.fromARGB(<span class="hljs-number">255</span>, red, greed, blue);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码效果如下，可以看到使用<code>StatelessColorfulTile</code>时，点击按钮后两个色块能成功交换：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34043cfaa99f4873953fad8b77824423~tplv-k3u1fbpfcp-zoom-1.image" alt="QQ20210613173911HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>接下来我们把代码改成下面这样煮，重启：</p>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-meta">@override</span>
  <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initState</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">super</span>.initState();
    tiles = [
      StatefulColorfulTile(),
      StatefulColorfulTile(),
      <span class="hljs-comment">// StatefulColorfulTile(key: UniqueKey()),</span>
      <span class="hljs-comment">// StatefulColorfulTile(key: UniqueKey()),</span>
      <span class="hljs-comment">// StatelessColorfulTile(),</span>
      <span class="hljs-comment">// StatelessColorfulTile(),</span>
    ];
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>神奇的事情发生了，点击按钮后，色块不再发生交换：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fe61cf1adbb4ef7a23b17750859987e~tplv-k3u1fbpfcp-zoom-1.image" alt="QQ20210613174103HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那在使用<code>StatefulColorfulTile</code>的前提下，如何让色块再次点击按钮后能发生交换呢？我猜聪明的你已经想到了，就是设置key属性，即把代码改成下面这个样子，重启：</p>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-meta">@override</span>
  <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initState</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">super</span>.initState();
    tiles = [
      <span class="hljs-comment">// StatefulColorfulTile(),</span>
      <span class="hljs-comment">// StatefulColorfulTile(),</span>
      StatefulColorfulTile(key: UniqueKey()),
      StatefulColorfulTile(key: UniqueKey()),
      <span class="hljs-comment">// StatelessColorfulTile(),</span>
      <span class="hljs-comment">// StatelessColorfulTile(),</span>
    ];
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab8b71a28a8d4f2e9ddfd891786bec09~tplv-k3u1fbpfcp-zoom-1.image" alt="QQ20210613172343HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就是图解造成这些效果的原因了。</p>
<hr>
<h2 data-id="heading-4">为啥<code>StatelessColorfulTile</code>能交换</h2>
<p>我们先来看看<code>StatelessColorfulTile</code>交换的时候都发生了什么，先来看看交换前的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5dd2d84a14f445ab35b1fedc391c3a2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>交换后的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0abb68fc35eb42f0ad1f714dce60f6e5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当代码调用<code>PositionedTiles.setState</code>交换两个Widget后，flutter会从上到下逐一对比Widget树和Element树中的每个节点，如果发现节点的runtimeType和key一致的话（这里没有key，因此只对比runtimeType），那么就认为该Element仍然是有效的，可用复用，于是只需要更改Element的指针，就可以直接复用。</p>
<p>而由于<code>StatefulColorfulTile</code>的颜色信息是存储在widget中的：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StatelessColorfulTile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  Color color = ColorUtil.randomColor();
  
   ...（略）
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以即便色块Widget因为<code>Widget.canUpdate</code>返回不需要更新，内部没有回调到<code>setState</code>逻辑，也会成功交换。</p>
<blockquote>
<p>Element保存了Widget和RenderObject，Widget是负责描述控件样式，RenderObject则是布局渲染控制，当Element只更新了Widget，下一次渲染时就会变成新Widget的效果了。</p>
</blockquote>
<hr>
<h2 data-id="heading-5">为啥<code>StatefulColorfulTile</code>要加key才能交换</h2>
<p>先从代码的最表面说说<code>StatefulColorfulTile</code>和<code>StatelessColorfulTile</code>一个重大的区别，即Color的属性放的位置不一样。</p>
<p><code>StatelessColorfulTile</code>的Color属性是直接放置在Widget下的：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StatelessColorfulTile</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  Color color = ColorUtil.randomColor();
  
   ...（略）
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>StatefulColorfulTile</code>的Color属性是放在State下的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/599afea7ee804c2fb1a9ad0d601f366a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里补充一个基础知识，即<code>State</code>属性，最终都会被<code>Element</code>管理，下面可以简单追几段源码看看。</p>
<p>首先看看<code>StateFulWidget</code>的抽象方法：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c4211fc94b4d94b9262b46277644f6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了Flutter三棵树概念以后，我们应该明白每个Widget最终都会被创建出对应的Element，而创建的方法正是上面的<code>createElement</code>，它会调用<code>StatefulElement</code>构造函数来构造。</p>
<p>接着跟进<code>StatefulElement()</code>函数，我们就能清晰地看到<code>StatefulElement</code>管理了<code>State</code>，并且拿它来做各种各样的事了：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f60f1e59ad4a1ba708763aae8c0736~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>明确了<code>State</code>属性，最终都会被<code>Element</code>管理这个大前提后</strong>，接下来就好办了。</p>
<hr>
<p>我们先来看看<code>StatefulColorfulTile</code>不带key的时候，调用交换函数究竟发生了什么，依旧是先看<strong>交换前</strong>的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70bda6012a849a48302e18d124ad1f7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>交换后的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a15727f4d44931a5c33436fae83b35~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相信原因不用我多说了，首先还是Widget更新后，flutter会根据<code>runtimeType</code>和<code>key</code>比较Widget从而判断是否需要重新构建<code>Element</code>，这里<code>key</code>为空，只比较<code>runtimeType</code>，比较结果必然相等，所以<code>Element</code>直接复用。</p>
<p><code>StatefulColorfulTile</code>在重新渲染时，<code>Color</code>属性不再是从<code>Widget</code>对象（即自身）里获取，而是从<code>Element</code>的<code>State</code>里面获取，而<code>Element</code>根本没发生变化，所以取到的<code>Color</code>也没有变化，最终就算怎么渲染，颜色都是不变的，视觉效果上也就是两个色块没有交换了。</p>
<hr>
<p>接着看有了<code>key</code>之后，交换前：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23912fa9623e455e8e5b00794ad2d0bb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>交换后，发现两边<code>key</code>不相等，于是尝试匹配<code>Element</code>是否还有相同的id，发现有，于是重新排列<code>Element</code>让相同<code>key</code>的配对：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704459ee94ac4628970e92bc1cc25c72~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果Element这边没有key能与新Widget匹配得上，那么旧的Element会失效，后续根据新Widget重新构建一个Element。</p>
</blockquote>
<p>rebuild后，Element已改变，重新渲染后视觉上就看到两个色块交换位置了：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26c93d0322844292bbfca3143b4288c5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>熟悉三棵树原理的我们知道，<code>Element</code>就相当于设备上的真实控件，既然<code>Element</code>的位置变化了，那么最终屏幕上的控件也就跟着变化了，最终交换后重新渲染给视觉上就是两个色块交换了。</p>
<p>好了，本篇博客先到这里结束了，这里只是简单介绍了下Widget中key的作用，但实际上Key还有很多种实现，他们用处各有不同，这个因为和本篇目标没啥太大关系，所以不介绍了，有空自己翻翻官方文档其实很快也能搞懂了。</p></div>  
</div>
            