
---
title: 'Flutter学习之 动画核心'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fea2aa840e4c5e95d03c95bf354cdf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Sat, 27 Aug 2022 05:27:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fea2aa840e4c5e95d03c95bf354cdf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第28天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>本文主要介绍下flutter中动画核心</p>
</blockquote>
<h2 data-id="heading-0">1. Tween（映射）</h2>
<p><code>AnimationController </code>之前设置的最小/大值类型是 double，如果动画的变化是颜色要如何处理？</p>
<p><code>AnimationController</code> 在执行动画期间返回的值是 0 到 1，颜色从红色变为黑色方法如下：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_AnimationPageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">AnimationPage</span>> <span class="hljs-title">with</span> <span class="hljs-title">SingleTickerProviderStateMixin</span></span>&#123;
  <span class="hljs-keyword">late</span> AnimationController _controller;
  <span class="hljs-keyword">final</span> _startColor = Colors.black;
  <span class="hljs-keyword">final</span> _endColor = Colors.red;

  Color? _color;
  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    _controller = AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">1000</span>));
    _controller.addListener(() &#123;
      setState(() &#123;
        _color = Color.lerp(_startColor, _endColor, _controller.value);

      &#125;);
    &#125;);

  &#125;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(title: <span class="hljs-keyword">const</span> Text(<span class="hljs-string">'core'</span>),),
      body: Center(
        child: ElevatedButton(
          onPressed: ()&#123;
            _controller.forward();
          &#125;,
          child: Icon(Icons.change_circle,color:_color ?? Colors.red ,size: <span class="hljs-number">100</span>,),

        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fea2aa840e4c5e95d03c95bf354cdf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-27_20.23.47.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里使用的是<code>Color.lerp</code>表示一个渐变色两个颜色之间的线性插值。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">static</span> Color? lerp(Color? a, Color? b, <span class="hljs-built_in">double</span> t)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>' t '参数表示时间轴上的位置，0表示0 插值还没有开始，返回' a '(或其他东西)相当于' a ')， 1.0意味着插值已经完成，返回' b '(或等于' b '的值)，以及介于两者之间的值表示插值在时间轴上的相关点。</p>
<p>Flutter 中把这种从 0 -> 1 转换为 蓝色 -> 红色 行为称之为 <strong>Tween（映射）</strong> 。</p>
<p>使用 Tween 完成动画</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_AnimationPageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">AnimationPage</span>> <span class="hljs-title">with</span> <span class="hljs-title">SingleTickerProviderStateMixin</span></span>&#123;
  <span class="hljs-keyword">late</span> AnimationController _controller;
  <span class="hljs-keyword">final</span> _startColor = Colors.black;
  <span class="hljs-keyword">final</span> _endColor = Colors.red;
  <span class="hljs-keyword">late</span> Animation<Color?> _animation;


  Color? _color;
  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    _controller = AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">1000</span>));
    _controller.addListener(() &#123;
      setState(() &#123;&#125;);

    &#125;);
    _animation = ColorTween(begin: Colors.black, end: Colors.red).animate(_controller);



  &#125;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(title: <span class="hljs-keyword">const</span> Text(<span class="hljs-string">'core'</span>),),
      body: Center(
        child: ElevatedButton(
          onPressed: ()&#123;
            _controller.forward();
          &#125;,
          child: Icon(Icons.change_circle,color: _animation.value  ,size: <span class="hljs-number">100</span>,),

        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b92210f2ae3e4dda9fbc329cff566175~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-27_20.58.46.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本质上也是使用 <strong>Color.lerp</strong> 实现的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a523db1aa4f4a0c86c734eecc05880e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2. Curve（曲线）</h2>
<p>Curve曲线简单的使用</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_CurveAnimationPageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">CurveAnimationPage</span>>
    <span class="hljs-title">with</span> <span class="hljs-title">SingleTickerProviderStateMixin</span> </span>&#123;
  <span class="hljs-keyword">late</span> AnimationController _controller;
  <span class="hljs-keyword">late</span> Animation _animation;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    _controller =
    AnimationController(vsync: <span class="hljs-keyword">this</span>, duration: <span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">1000</span>))
      ..addListener(() &#123;
        setState(() &#123;&#125;);
      &#125;);

    _animation = Tween(begin: <span class="hljs-number">100.0</span>, end: <span class="hljs-number">200.0</span>)
        .chain(CurveTween(curve: Curves.bounceIn))
        .animate(_controller);
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(title: <span class="hljs-keyword">const</span> Text(<span class="hljs-string">"core"</span>),),
      body: Center(
          child: ElevatedButton(
            onPressed: ()&#123;
              _controller.forward();
            &#125;,
            child: Icon(Icons.add,size: _animation.value,),
          )),
    );
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    <span class="hljs-keyword">super</span>.dispose();
    _controller.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大小 100 变大到 200，动画曲线设置为 <strong>bounceIn（弹簧效果）</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eacca06aed2b4caf994f480960741134~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-27_21.17.28.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>动画效果中系统已经提供了几十种种常用到动画曲线：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2b4f04aaa204a71a6dce5f0e0952b99~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们使用linear</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/287f469b4afe4569bd6dbe23e3a01d43~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-27_21.23.18.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其余动画效果可以官方文档查看。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.github.io%2Fassets-for-api-docs%2Fassets%2Fanimation%2Fcurve_fast_linear_to_slow_ease_in.mp4" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.github.io/assets-for-api-docs/assets/animation/curve_fast_linear_to_slow_ease_in.mp4" ref="nofollow noopener noreferrer">fastLinearToSlowEaseIn
</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a276b1409f42a3a39d3a93760d5486~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们也可以仿照系统进行自定义。</p></div>  
</div>
            