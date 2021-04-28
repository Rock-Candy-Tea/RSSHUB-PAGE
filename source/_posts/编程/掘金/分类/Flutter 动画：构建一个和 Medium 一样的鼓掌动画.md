
---
title: 'Flutter 动画：构建一个和 Medium 一样的鼓掌动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b33a769017849ec81a80b0594f9c108~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 05:21:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b33a769017849ec81a80b0594f9c108~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://proandroiddev.com/flutter-animation-creating-mediums-clap-animation-in-flutter-3168f047421e" target="_blank" rel="nofollow noopener noreferrer">Flutter Animation : Creating medium’s clap animation in flutter</a></li>
<li>原文作者：<a href="https://medium.com/@Kartik1607" target="_blank" rel="nofollow noopener noreferrer">Kartik Sharma</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/flutter-animation-creating-mediums-clap-animation-in-flutter.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/Hoarfroster" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/greycodee" target="_blank" rel="nofollow noopener noreferrer">greycodee</a>、<a href="https://github.com/HumanBeingXenon" target="_blank" rel="nofollow noopener noreferrer">HumanBeingXenon</a></li>
</ul>
</blockquote>
<p>在这篇文章中，我们将从零开始探索 Flutter 动画。我们将通过在 Flutter 中模仿制作 Medium 的鼓掌动画，学习一些关于动画的核心概念。</p>
<p>正如标题所说，这篇文章将更多地关注动画，而不是 Flutter 的基础知识。</p>
<h2 data-id="heading-0">入门</h2>
<p>我们会从新建一个 Flutter 项目开始。每当我们新建一个 Flutter 项目，我们就会看到这段代码：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// main.dart</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-keyword">void</span> main() => runApp(<span class="hljs-keyword">new</span> MyApp());

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MaterialApp(
      title: <span class="hljs-string">'Flutter Demo'</span>,
      theme: <span class="hljs-keyword">new</span> ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: <span class="hljs-keyword">new</span> MyHomePage(title: <span class="hljs-string">'Flutter Demo Home Page'</span>),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyHomePage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  MyHomePage(&#123;Key key, <span class="hljs-keyword">this</span>.title&#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> title;

  <span class="hljs-meta">@override</span>
  _MyHomePageState createState() => <span class="hljs-keyword">new</span> _MyHomePageState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-built_in">int</span> _counter = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">void</span> _incrementCounter() &#123;
    setState(() &#123;
      _counter++;
    &#125;);
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Scaffold(
      appBar: <span class="hljs-keyword">new</span> AppBar(
        title: <span class="hljs-keyword">new</span> Text(widget.title),
      ),
      body: <span class="hljs-keyword">new</span> Center(
        child: <span class="hljs-keyword">new</span> Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            <span class="hljs-keyword">new</span> Text(
              <span class="hljs-string">'You have pushed the button this many times:'</span>,
            ),
            <span class="hljs-keyword">new</span> Text(
              <span class="hljs-string">'<span class="hljs-subst">$_counter</span>'</span>,
              style: Theme.of(context).textTheme.display1,
            ),
          ],
        ),
      ),
      floatingActionButton: <span class="hljs-keyword">new</span> FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: <span class="hljs-string">'Increment'</span>,
        child: <span class="hljs-keyword">new</span> Icon(Icons.add),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Flutter 为我们提供了一份免费的入门代码午餐～它已经管理了点击次数的状态，并为我们创建了一个浮动的动作按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b33a769017849ec81a80b0594f9c108~tplv-k3u1fbpfcp-zoom-1.image" alt="我们目前有的按钮" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是我们想要达到的最终效果：</p>
<p>// 等待上传 // <a href="https://miro.medium.com/max/1600/1*Hnkdb5BSXFmjVitdYQiirQ.gif" target="_blank" rel="nofollow noopener noreferrer">miro.medium.com/max/1600/1*…</a></p>
<p>我们将会创建的动画。作者：<a href="https://dribbble.com/shots/4294768-Medium-Claps-Made-in-Flinto" target="_blank" rel="nofollow noopener noreferrer"><strong>Thuy Gia Nguyen</strong></a></p>
<p>在添加动画之前，我们先来快速浏览并解决一些简单的问题。</p>
<ol>
<li>改变按钮图标和背景。</li>
<li>当我们按住按钮时，按钮应该继续添加计数。</li>
</ol>
<p>让我们添加这 2 个快速修复，然后开始制作动画：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// main.dart</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-built_in">int</span> _counter = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">final</span> duration = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">300</span>);
  Timer timer;


  initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
  &#125;

  dispose() &#123;
   <span class="hljs-keyword">super</span>.dispose();
  &#125;

  <span class="hljs-keyword">void</span> increment(Timer t) &#123;
    setState(() &#123;
      _counter++;
    &#125;);
  &#125;

  <span class="hljs-keyword">void</span> onTapDown(TapDownDetails tap) &#123;
    <span class="hljs-comment">// User pressed the button. This can be a tap or a hold.</span>
    increment(<span class="hljs-keyword">null</span>); <span class="hljs-comment">// Take care of tap</span>
    timer = <span class="hljs-keyword">new</span> Timer.periodic(duration, increment); <span class="hljs-comment">// Takes care of hold</span>
  &#125;

  <span class="hljs-keyword">void</span> onTapUp(TapUpDetails tap) &#123;
    <span class="hljs-comment">// User removed his finger from button.</span>
    timer.cancel();
  &#125;

  Widget getScoreButton() &#123;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Positioned(
        child: <span class="hljs-keyword">new</span> Opacity(opacity: <span class="hljs-number">1.0</span>, child: <span class="hljs-keyword">new</span> Container(
            height: <span class="hljs-number">50.0</span> ,
            width: <span class="hljs-number">50.0</span> ,
            decoration: <span class="hljs-keyword">new</span> ShapeDecoration(
              shape: <span class="hljs-keyword">new</span> CircleBorder(
                  side: BorderSide.none
              ),
              color: Colors.pink,
            ),
            child: <span class="hljs-keyword">new</span> Center(child:
            <span class="hljs-keyword">new</span> Text(<span class="hljs-string">"+"</span> + _counter.toString(),
              style: <span class="hljs-keyword">new</span> TextStyle(color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: <span class="hljs-number">15.0</span>),))
        )),
        bottom: <span class="hljs-number">100.0</span>
    );
  &#125;

  Widget getClapButton() &#123;
    <span class="hljs-comment">// Using custom gesture detector because we want to keep increasing the claps</span>
    <span class="hljs-comment">// when user holds the button.</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> GestureDetector(
        onTapUp: onTapUp,
        onTapDown: onTapDown,
        child: <span class="hljs-keyword">new</span> Container(
          height: <span class="hljs-number">60.0</span> ,
          width: <span class="hljs-number">60.0</span> ,
          padding: <span class="hljs-keyword">new</span> EdgeInsets.all(<span class="hljs-number">10.0</span>),
          decoration: <span class="hljs-keyword">new</span> BoxDecoration(
              border: <span class="hljs-keyword">new</span> Border.all(color: Colors.pink, width: <span class="hljs-number">1.0</span>),
              borderRadius: <span class="hljs-keyword">new</span> BorderRadius.circular(<span class="hljs-number">50.0</span>),
              color: Colors.white,
              boxShadow: [
                <span class="hljs-keyword">new</span> BoxShadow(color: Colors.pink, blurRadius: <span class="hljs-number">8.0</span>)
              ]
          ),
          child: <span class="hljs-keyword">new</span> ImageIcon(
              <span class="hljs-keyword">new</span> AssetImage(<span class="hljs-string">"images/clap.png"</span>), color: Colors.pink,
              size: <span class="hljs-number">40.0</span>),
        )
    );
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Scaffold(
      appBar: <span class="hljs-keyword">new</span> AppBar(
        title: <span class="hljs-keyword">new</span> Text(widget.title),
      ),
      body: <span class="hljs-keyword">new</span> Center(
        child: <span class="hljs-keyword">new</span> Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            <span class="hljs-keyword">new</span> Text(
              <span class="hljs-string">'You have pushed the button this many times:'</span>,
            ),
            <span class="hljs-keyword">new</span> Text(
              <span class="hljs-string">'<span class="hljs-subst">$_counter</span>'</span>,
              style: Theme
                  .of(context)
                  .textTheme
                  .display1,
            ),
          ],
        ),
      ),
      floatingActionButton: <span class="hljs-keyword">new</span> Padding(
          padding: <span class="hljs-keyword">new</span> EdgeInsets.only(right: <span class="hljs-number">20.0</span>),
          child: <span class="hljs-keyword">new</span> Stack(
            alignment: FractionalOffset.center,
            overflow: Overflow.visible,
            children: <Widget>[
              getScoreButton(),
              getClapButton(),
            ],
          )
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从最终的产品来看，我们需要补充 3 点。</p>
<ol>
<li>改变 Widget 的大小</li>
<li>当按钮被按下时，显示那个展示鼓掌次数的 Widget，并在按钮释放时隐藏这个 Widget</li>
<li>添加那些很小的向四周撒花的 Widget，并将它们做成动画</li>
</ol>
<p>让我们一个一个来，慢慢推进学习进度。开始之前，我们需要了解 Flutter 中一些关于动画的基本知识。</p>
<h2 data-id="heading-1">了解 Flutter 中基本动画的 Widget</h2>
<p>一个动画无非是一些随时间变化的数值。例如，当我们点击按钮时，我们想让显示鼓掌次数的 Widget 从底部逐步上移。当按钮释放的时候它应该已经上移了不少，这时候我们应该把它隐藏起来。</p>
<p>将焦点关注在显示鼓掌次数的 Widget 上，我们需要<strong>在一段时间内改变</strong>它的位置和不透明度。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 显示鼓掌次数的 Widget</span>

<span class="hljs-keyword">new</span> Positioned(
  child: <span class="hljs-keyword">new</span> Opacity(opacity: <span class="hljs-number">1.0</span>, 
    child: <span class="hljs-keyword">new</span> Container(
      <span class="hljs-comment">// ……</span>
    )),
  bottom: <span class="hljs-number">100.0</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比方说，我们想让显示鼓掌次数的 Widget 在 150 毫秒后才从底部向上淡入。让我们在时间轴上思索一下，如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c00964cdd4d4c99a61b414c9b78fc48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一幅简单的二维图像，位置随着时间推移而改变。</p>
<p>请注意这是一条斜线，不过如果你喜欢的话，这其实也可以是一条曲线。</p>
<p>你可以让位置随着时间慢慢增加，然后越来越快。或者你也可以让它以超高速进来，然后在最后慢下来。</p>
<p>这就是我们要介绍的第一个 Widget <code>AnimationController</code>。</p>
<p><code>AnimationController</code> 构造器是这样的：</p>
<pre><code class="hljs language-dart copyable" lang="dart">scoreInAnimationController = <span class="hljs-keyword">new</span> AnimationController(duration: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">150</span>), vsync: <span class="hljs-keyword">this</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们已经为动画创建了一个简单的控制器，并指定了要运行动画的持续时间为 150ms。不过那个 <code>vsync</code> 是什么？</p>
<p>移动设备每隔几毫秒就会刷新一次屏幕。这就是我们如何将一组图像感知为一个连续的流或一部影片。</p>
<p>屏幕刷新的速度可以因设备而异。比方说，手机每秒刷新屏幕 60 次（60 帧/秒），那就是每隔 16.67 毫秒之后设备会绘制一个新的界面。有时图像可能会发生错位（我们在屏幕刷新时发送了不同的图像），我们就会看到屏幕撕裂。<code>vsync</code> 可以解决这个问题。</p>
<p>让我们在控制器上添加一个监听器然后运行动画：</p>
<pre><code class="hljs language-dart copyable" lang="dart">scoreInAnimationController.addListener(() &#123;
  <span class="hljs-built_in">print</span>(scoreInAnimationController.value);
&#125;);
scoreInAnimationController.forward(from: <span class="hljs-number">0.0</span>);

<span class="hljs-comment">/* OUTPUT
I/flutter ( 1913): 0.0
I/flutter ( 1913): 0.0
I/flutter ( 1913): 0.22297333333333333
I/flutter ( 1913): 0.3344533333333333
I/flutter ( 1913): 0.4459333333333334
I/flutter ( 1913): 0.5574133333333334
I/flutter ( 1913): 0.6688933333333335
I/flutter ( 1913): 0.7803666666666668
I/flutter ( 1913): 0.8918466666666668
I/flutter ( 1913): 1.0
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>控制器在 150 毫秒内产生了从 0.0 到 1.0 的数字</strong> —— 请注意，产生的数值几乎是线性的（0.2, 0.3, 0.4……）。我们如何改变这种行为？这将由第二个 Widget <code>CurvedAnimation</code> 来完成：</p>
<pre><code class="hljs language-dart copyable" lang="dart">bounceInAnimation = <span class="hljs-keyword">new</span> CurvedAnimation(parent: scoreInAnimationController, curve: Curves.bounceIn);
bounceInAnimation.addListener(() &#123;
  <span class="hljs-built_in">print</span>(bounceInAnimation.value);
&#125;);

<span class="hljs-comment">/* OUTPUT
I/flutter ( 5221): 0.0
I/flutter ( 5221): 0.0
I/flutter ( 5221): 0.24945376519722218
I/flutter ( 5221): 0.16975716286388898
I/flutter ( 5221): 0.17177866222222238
I/flutter ( 5221): 0.6359024059750003
I/flutter ( 5221): 0.9119433941222221
I/flutter ( 5221): 1.0
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过将 <code>parent</code> 设置为我们的控制器并提供我们想要跟随的曲线，创建了一个曲线动画。在 <a href="https://docs.flutter.io/flutter/animation/Curves-class.html" target="_blank" rel="nofollow noopener noreferrer">Flutter Curves 类参考文档页面</a>我们可以看到一系列我们可以使用的曲线。控制器在 150 毫秒的时间内向曲线动画 Widget 提供 0.0 到 1.0 的数值，而曲线动画 Widget 就会按照我们设置的曲线对这些值进行插值。</p>
<p>现在我们得到了从 0.0 到 1.0 的值，而我们希望我们的展示点赞次数的 Widget 的动画值的范围是 <code>[0.0, 100.0]</code>。我们可以简单地将上一步得到的值乘以 100 来得到结果。或者我们可以使用第三种部件 <code>Tween</code> 类。</p>
<pre><code class="hljs language-dart copyable" lang="dart">tweenAnimation = <span class="hljs-keyword">new</span> Tween(begin: <span class="hljs-number">0.0</span>, end: <span class="hljs-number">100.0</span>).animate(scoreInAnimationController);
tweenAnimation.addListener(() &#123;
  <span class="hljs-built_in">print</span>(tweenAnimation.value);
&#125;);

<span class="hljs-comment">/* Output 
I/flutter ( 2639): 0.0
I/flutter ( 2639): 0.0
I/flutter ( 2639): 33.452000000000005
I/flutter ( 2639): 44.602000000000004
I/flutter ( 2639): 55.75133333333334
I/flutter ( 2639): 66.90133333333334
I/flutter ( 2639): 78.05133333333333
I/flutter ( 2639): 89.20066666666668
I/flutter ( 2639): 100.0
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Tween</code> 类生成了从 <code>begin</code> 到 <code>end</code> 的值。我们使用了前面的 <code>scoreInAnimationController</code> ，它使用了一条线性曲线。（当然我们也可以使用我们的反弹曲线来获得不同的值）。<code>Tween</code> 的优势并不止于此 —— 你还可以 <code>Tween</code> 其他东西。<a href="https://docs.flutter.io/flutter/animation/Tween-class.html" target="_blank" rel="nofollow noopener noreferrer">你可以直接 <code>Tween</code> 颜色、偏移、位置以及其他继承了 <code>Tween</code> 基类的 Widget 属性</a>。</p>
<p><strong>展示鼓掌次数的 Widget 的位置动画</strong></p>
<p>在这一点上，我们已经有足够的知识让我们的展示鼓掌次数的 Widget 在我们按下按钮时从底部弹出，而在我们释放按钮的时候隐藏。</p>
<pre><code class="hljs language-dart copyable" lang="dart">initState() &#123;
  <span class="hljs-keyword">super</span>.initState();
  scoreInAnimationController = <span class="hljs-keyword">new</span> AnimationController(duration: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">150</span>), vsync: <span class="hljs-keyword">this</span>);
  scoreInAnimationController.addListener(()&#123;
    setState(() &#123;&#125;); <span class="hljs-comment">// 调用渲染函数（译者注：其实是更新状态）</span>
  &#125;);
&#125;

<span class="hljs-keyword">void</span> onTapDown(TapDownDetails tap) &#123;
  scoreInAnimationController.forward(from: <span class="hljs-number">0.0</span>);
  ...    
&#125;
Widget getScoreButton() &#123;
  <span class="hljs-keyword">var</span> scorePosition = scoreInAnimationController.value * <span class="hljs-number">100</span>;
  <span class="hljs-keyword">var</span> scoreOpacity = scoreInAnimationController.value;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Positioned(
    child: <span class="hljs-keyword">new</span> Opacity(opacity: scoreOpacity, 
      child: <span class="hljs-keyword">new</span> Container(<span class="hljs-comment">/* …… */</span>)
    ),
    bottom: scorePosition
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc52dfc826424877969fc845de309b7f~tplv-k3u1fbpfcp-zoom-1.image" alt="动画的现状" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点开后弹出展示鼓掌次数的 Widget，不过还是有一个问题：</p>
<p>当我们多次点击按钮时，展示鼓掌次数的 Widget 会不断地弹出。这是因为上面代码中的一个小错误。我们告诉控制器在每次点击按钮时从 0 开始前进。</p>
<p>现在，让我们为展示鼓掌次数的 Widget 添加输出动画。</p>
<p>首先，我们添加一个枚举来更容易地管理展示鼓掌次数的 Widget 的状态。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">enum</span> ScoreWidgetStatus &#123;
  HIDDEN,
  BECOMING_VISIBLE,
  BECOMING_INVISIBLE
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们创建一个动画控制器，对 Widget 的位置值在 <code>[100, 150]</code> 范围内进行非线性动画。我们还为动画添加了一个状态监听器，一旦动画结束，我们就将展示鼓掌次数的 Widget 的状态设置为隐藏。</p>
<pre><code class="hljs language-dart copyable" lang="dart">scoreOutAnimationController = <span class="hljs-keyword">new</span> AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: duration);
scoreOutPositionAnimation = <span class="hljs-keyword">new</span> Tween(begin: <span class="hljs-number">100.0</span>, end: <span class="hljs-number">150.0</span>).animate(
  <span class="hljs-keyword">new</span> CurvedAnimation(parent: scoreOutAnimationController, curve: Curves.easeOut)
);
scoreOutPositionAnimation.addListener(()&#123;
  setState(() &#123;&#125;);
&#125;);
scoreOutAnimationController.addStatusListener((status) &#123;
  <span class="hljs-keyword">if</span> (status == AnimationStatus.completed) &#123;
    _scoreWidgetStatus = ScoreWidgetStatus.HIDDEN;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当用户将手指从 Widget 上移开时，我们将设置相应的状态，并启动一个 300 毫秒的计时器。300 毫秒后，我们将对 Widget 的位置和不透明度进行动画处理：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> onTapUp(TapUpDetails tap) &#123;
  <span class="hljs-comment">// 用户移开了他的手指</span>
  scoreOutETA = <span class="hljs-keyword">new</span> Timer(duration, () &#123;
    scoreOutAnimationController.forward(from: <span class="hljs-number">0.0</span>);
    _scoreWidgetStatus = ScoreWidgetStatus.BECOMING_INVISIBLE;
  &#125;);
  holdTimer.cancel();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当用户将手指点按 Widget 时，我们将设置相应的状态，并启动一个 300 毫秒的计时器：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> onTapDown(TapDownDetails tap) &#123;
  <span class="hljs-comment">// 用户点按了按钮 —— 不管是长按还是点按</span>
  <span class="hljs-keyword">if</span> (scoreOutETA != <span class="hljs-keyword">null</span>) scoreOutETA.cancel(); <span class="hljs-comment">// 我们不希望次数消失！</span>
  <span class="hljs-keyword">if</span> (_scoreWidgetStatus == ScoreWidgetStatus.HIDDEN) &#123;
    scoreInAnimationController.forward(from: <span class="hljs-number">0.0</span>);
    _scoreWidgetStatus = ScoreWidgetStatus.BECOMING_VISIBLE;
  &#125;
  increment(<span class="hljs-keyword">null</span>); <span class="hljs-comment">// 关注点按</span>
  holdTimer = <span class="hljs-keyword">new</span> Timer.periodic(duration, increment); <span class="hljs-comment">// 关注长按</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还修改了 <code>TapDown</code> 事件，以处理一些特殊情况。最后，我们需要选择我们需要使用哪个控制器的值来处理我们的展示鼓掌次数的 Widget 的位置和不透明度。一个简单的 <code>switch</code> 就可以完成这项工作：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Widget getScoreButton() &#123;
  <span class="hljs-keyword">var</span> scorePosition = <span class="hljs-number">0.0</span>;
  <span class="hljs-keyword">var</span> scoreOpacity = <span class="hljs-number">0.0</span>;
  <span class="hljs-keyword">switch</span>(_scoreWidgetStatus) &#123;
    <span class="hljs-keyword">case</span> ScoreWidgetStatus.HIDDEN:
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> ScoreWidgetStatus.BECOMING_VISIBLE:
      scorePosition = scoreInAnimationController.value * <span class="hljs-number">100</span>;
      scoreOpacity = scoreInAnimationController.value;
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> ScoreWidgetStatus.BECOMING_INVISIBLE:
      scorePosition = scoreOutPositionAnimation.value;
      scoreOpacity = <span class="hljs-number">1.0</span> - scoreOutAnimationController.value;
  &#125;
  <span class="hljs-keyword">return</span> ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前输出：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf49b170823d4c6e9aa8de871ed3f276~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，我们需要选择我们需要使用哪个控制器的值来设置展示鼓掌次数的 Widget 的位置和不透明度 —— 它应该弹出+淡出。</p>
<p><strong>展示鼓掌次数的 Widget 大小动画</strong></p>
<p>在这一点上，当次数增加时我们也知道如何改变大小。让我们快速添加大小动画，然后我们转到撒花动画上。</p>
<p>我更新了 <code>ScoreWidgetStatus</code> 枚举，以持有一个额外的 <code>VISIBLE</code> 值。现在，我们为大小属性添加一个新的控制器。</p>
<pre><code class="hljs language-dart copyable" lang="dart">scoreSizeAnimationController = <span class="hljs-keyword">new</span> AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">150</span>));
scoreSizeAnimationController.addStatusListener((status) &#123;
  <span class="hljs-keyword">if</span>(status == AnimationStatus.completed) &#123;
    scoreSizeAnimationController.reverse();
  &#125;
&#125;);
scoreSizeAnimationController.addListener(()&#123;
  setState(() &#123;&#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制器在 150 毫秒内产生从 0 到 1 的数值，一旦完成，我们就产生从 1 到 0 的数值，这样就有了很好的放大和缩小的效果。</p>
<p>我们还更新了我们的 <code>increment</code> 函数 —— 当数字递增时就会开始动画。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> increment(Timer t) &#123;
  scoreSizeAnimationController.forward(from: <span class="hljs-number">0.0</span>);
  setState(() &#123;
    _counter++;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要处理枚举的 <code>Visible</code> 属性的情况。为此，我们需要在 <code>TouchDown</code> 事件中添加一些判断：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> onTapDown(TapDownDetails tap) &#123;
  <span class="hljs-comment">// 用户点按了按钮 —— 不管是长按还是点按</span>
  <span class="hljs-keyword">if</span> (scoreOutETA != <span class="hljs-keyword">null</span>) scoreOutETA.cancel(); <span class="hljs-comment">// 我们不希望次数消失！</span>
  <span class="hljs-keyword">if</span>(_scoreWidgetStatus == ScoreWidgetStatus.BECOMING_INVISIBLE) &#123;
    <span class="hljs-comment">// 在 Widget 向上飞入的时候点击了按钮，把那玩意暂停掉！</span>
    scoreOutAnimationController.stop(canceled: <span class="hljs-keyword">true</span>);
    _scoreWidgetStatus = ScoreWidgetStatus.VISIBLE;
  &#125;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (_scoreWidgetStatus == ScoreWidgetStatus.HIDDEN ) &#123;
    _scoreWidgetStatus = ScoreWidgetStatus.BECOMING_VISIBLE;
    scoreInAnimationController.forward(from: <span class="hljs-number">0.0</span>);
  &#125;
  increment(<span class="hljs-keyword">null</span>); <span class="hljs-comment">// 关注点按</span>
  holdTimer = <span class="hljs-keyword">new</span> Timer.periodic(duration, increment); <span class="hljs-comment">// 关注长按</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们在 Widget 中使用控制器的值。</p>
<pre><code class="hljs language-dart copyable" lang="dart">extraSize = scoreSizeAnimationController.value * <span class="hljs-number">10</span>;
...
height: <span class="hljs-number">50.0</span> + extraSize,
width: <span class="hljs-number">50.0</span>  + extraSize,
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整的代码可以在 <a href="https://gist.github.com/Kartik1607/52c882194e3119e0d176fb15e6c6b913" target="_blank" rel="nofollow noopener noreferrer">GitHub Gist</a> 处找到。这里我们同时运行的大小和位置的动画。尺寸放缩动画还需要一点点调整，最后再说。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d096308c9b24b7a9462c33343c30304~tplv-k3u1fbpfcp-zoom-1.image" alt="尺寸和位置动画一起工作" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">撒花动画</h2>
<p>在做撒花动画之前，我们需要对尺寸放缩动画做一些调整。目前来看，按钮的放大幅度太大。解决方法很简单，将 <code>extrasize</code> 系数从 <code>10</code> 改为小一点的数字。</p>
<p>现在来看撒花动画。我们可以观察到，<strong>撒出来的花只是 5 个变化着位置的图像。</strong></p>
<p>我在微软的 Paint 软件中制作了一个三角形和一个圆形的图像，并将其保存到 Flutter 资源中。现在我们就可以将该图像作为 Image Asset 素材。</p>
<p>在制作动画之前，我们先来思考一下定位和一些我们需要完成的任务。</p>
<ol>
<li>我们需要定位 5 张图片，每张图片呈现不同角度，围成一个完整的圆。</li>
<li>我们需要根据角度旋转图像。</li>
<li>我们需要随着时间增加圆的半径。</li>
<li>我们需要根据角度和半径找到坐标。</li>
</ol>
<p>简单的三角学给我们提供了根据角度的正弦和余弦得到 x 和 y 坐标的公式。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> sparklesWidget =
  <span class="hljs-keyword">new</span> Positioned(child: <span class="hljs-keyword">new</span> Transform.rotate(
    angle: currentAngle - pi/<span class="hljs-number">2</span>,
    child: <span class="hljs-keyword">new</span> Opacity(opacity: sparklesOpacity,
      child : <span class="hljs-keyword">new</span> Image.asset(<span class="hljs-string">"images/sparkles.png"</span>, width: <span class="hljs-number">14.0</span>, height: <span class="hljs-number">14.0</span>, ))
    ),
    left:(sparkleRadius*cos(currentAngle)) + <span class="hljs-number">20</span>,
    top: (sparkleRadius* sin(currentAngle)) + <span class="hljs-number">20</span> ,
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们需要创建 5 个这样的 Widget，而每个 Widget 都应该有不同的角度。一个简单的 <code>for</code> 循环就可以了。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">for</span>(<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>;i < <span class="hljs-number">5</span>; ++i) &#123;
  <span class="hljs-keyword">var</span> currentAngle = (firstAngle + ((<span class="hljs-number">2</span>*pi)/<span class="hljs-number">5</span>)*(i));
  <span class="hljs-keyword">var</span> sparklesWidget = ...
  stackChildren.add(sparklesWidget);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需将 <code>2*pi</code>（360 度）分成 5 份，并据此创建一个 Widget。然后，我们将这些 Widget 添加到一个数组中，这个数组将作为栈的孩子。</p>
<p>现在，在这一点上，大部分的工作已经完成。我们只需要对 <code>sparkleRadius</code> 进行动画处理，并在分数递增时生成一个新的 <code>firstAngle</code>。</p>
<pre><code class="hljs language-dart copyable" lang="dart">sparklesAnimationController = <span class="hljs-keyword">new</span> AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: duration);
sparklesAnimation = <span class="hljs-keyword">new</span> CurvedAnimation(parent: sparklesAnimationController, curve: Curves.easeIn);
sparklesAnimation.addListener(()&#123;
  setState(() &#123; &#125;);
&#125;);

<span class="hljs-keyword">void</span> increment(Timer t) &#123;
  sparklesAnimationController.forward(from: <span class="hljs-number">0.0</span>);
  ...
  setState(() &#123;
  ...
  _sparklesAngle = random.nextDouble() * (<span class="hljs-number">2</span>*pi);
&#125;);
     
Widget getScoreButton() &#123;
  ...
  <span class="hljs-keyword">var</span> firstAngle = _sparklesAngle;
  <span class="hljs-keyword">var</span> sparkleRadius = (sparklesAnimationController.value * <span class="hljs-number">50</span>) ;
  <span class="hljs-keyword">var</span> sparklesOpacity = (<span class="hljs-number">1</span> - sparklesAnimation.value);
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd18e17f978a43c382f8f1a9f6ab85a8~tplv-k3u1fbpfcp-zoom-1.image" alt="最终结果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是我们对 Flutter 中<strong>基本动画的介绍</strong>。我们未来还会继续探索更多的 Flutter 知识，以学习创建更高级的 UI。</p>
<p>你可以在我的 <a href="https://github.com/Kartik1607/FlutterUI/tree/master/MediumClapAnimation/medium_clap" target="_blank" rel="nofollow noopener noreferrer">Git 仓库</a>找到完整的代码。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            