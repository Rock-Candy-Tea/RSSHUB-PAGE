
---
title: 'Flutter 动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=92'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:26:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=92'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">AnimatedWidget简化了什么？</h4>
<p>首先看一段不使用AnimatedWidget的代码：
给animation添加了Listener，动画执行的每一帧都会回调这个Listener，在这个Listener回调中，调用<code>setState()</code>来完成widget的更新（刷新）。</p>
<pre><code class="copyable">class ScaleAnimationRoute extends StatefulWidget &#123;
  @override
  _ScaleAnimationRouteState createState() => new _ScaleAnimationRouteState();
&#125;

//需要继承TickerProvider，如果有多个AnimationController，则应该使用TickerProviderStateMixin。
class _ScaleAnimationRouteState extends State<ScaleAnimationRoute>  with SingleTickerProviderStateMixin&#123; 
    
  Animation<double> animation;
  AnimationController controller;
    
  initState() &#123;
    super.initState();
    controller = new AnimationController(
        duration: const Duration(seconds: 3), vsync: this);
    //图片宽高从0变到300
    animation = new Tween(begin: 0.0, end: 300.0).animate(controller)
      ..addListener(() &#123;
        setState(()=>&#123;&#125;);
      &#125;);
    //启动动画(正向执行)
    controller.forward();
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return new Center(
       child: Image.asset("imgs/avatar.png",
          width: animation.value,
          height: animation.value
      ),
    );
  &#125;

  dispose() &#123;
    //路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样是不是很麻烦，还需要手动调用<code>setState()</code><br>
那么AnimatedWidget就是省略了setState()的步骤，<code>AnimatedWidget</code>类封装了调用<code>setState()</code>的细节,来看下面的代码：</p>
<pre><code class="copyable">class AnimatedImage extends AnimatedWidget &#123;
  AnimatedImage(&#123;Key key, Animation<double> animation&#125;)
      : super(key: key, listenable: animation);

  Widget build(BuildContext context) &#123;
    final Animation<double> animation = listenable;
    return new Center(
      child: Image.asset("imgs/avatar.png",
          width: animation.value,
          height: animation.value
      ),
    );
  &#125;
&#125;


class ScaleAnimationRoute1 extends StatefulWidget &#123;
  @override
  _ScaleAnimationRouteState createState() => new _ScaleAnimationRouteState();
&#125;

class _ScaleAnimationRouteState extends State<ScaleAnimationRoute1>
    with SingleTickerProviderStateMixin &#123;

  Animation<double> animation;
  AnimationController controller;

  initState() &#123;
    super.initState();
    controller = new AnimationController(
        duration: const Duration(seconds: 3), vsync: this);
    //图片宽高从0变到300
    animation = new Tween(begin: 0.0, end: 300.0).animate(controller);
    //启动动画
    controller.forward();
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return AnimatedImage(animation: animation,);
  &#125;

  dispose() &#123;
    //路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到不再需要添加Listener并手动调用<code>setState()</code>方法了。<code>AnimatedWidget</code> 自己会使用当前 <code>Animation</code> 的 <code>value</code> 来绘制自己。</p>
<h4 data-id="heading-1">AnimatedBuilder是干嘛的？</h4>
<p>我们可以看到上面的<code>AnimatedImage</code>, 用<code>AnimatedWidget</code>可以从动画中分离出<code>widget</code>，而动画的渲染过程（即设置宽高）仍然在<code>AnimatedWidget</code>中。也就是animation.value仍然设置在Image的width，height属性中。</p>
<pre><code class="copyable">class AnimatedImage extends AnimatedWidget &#123;
  AnimatedImage(&#123;Key key, Animation<double> animation&#125;)
      : super(key: key, listenable: animation);

  Widget build(BuildContext context) &#123;
    final Animation<double> animation = listenable;
    return new Center(
      child: Image.asset("imgs/avatar.png",
          width: animation.value,
          height: animation.value
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>AnimatedBuilder</code>是在<code>AnimatedWidget</code>的基础上将显示内容和动画拆分开来，更加方便的为特定的显示内容添加具体的动画。看下嘛的例子：<code>Image</code>和<code>Animation</code>就完美的分开了。</p>
<pre><code class="copyable">class GrowTransition extends StatelessWidget &#123;
  GrowTransition(&#123;this.child, this.animation&#125;);

  final Widget child;
  final Animation<double> animation;
    
  Widget build(BuildContext context) &#123;
    return new Center(
      child: new AnimatedBuilder(
          animation: animation,
          builder: (BuildContext context, Widget child) &#123;
            return new Container(
                height: animation.value, 
                width: animation.value, 
                child: child
            );
          &#125;,
          child: child
      ),
    );
  &#125;
&#125;

...
Widget build(BuildContext context) &#123;
    return GrowTransition(
    child: Image.asset("images/avatar.png"), 
    animation: animation,
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">AnimatedWidget和AnimatedBuilder就完美了吗？</h4>
<p>可以看到上面的代码，AnimationController依然暴露在外面，需要调用<code>controller.forward()</code>执行动画，能不能把AnimationController封装到动画widget的内部，答案是肯定的，直接看代码：</p>
<pre><code class="copyable">class AnimatedDecoratedExampleBox extends StatefulWidget &#123;
  @override
  State<StatefulWidget> createState() &#123;
    return _AnimatedDecoratedExampleBoxState();
  &#125;
&#125;

class _AnimatedDecoratedExampleBoxState
    extends State<AnimatedDecoratedExampleBox> &#123;
  Color _bgColor = Colors.blue;
  var duration = Duration(seconds: 1);

  @override
  Widget build(BuildContext context) &#123;
    return MaterialApp(
        home: Scaffold(
            backgroundColor: Colors.grey[200],
            appBar: AppBar(
              title: Text("AnimatedSwitcher"),
            ),
            body: Center(
                child: AnimatedDecoratedBox(
              duration: duration,
              decoration: BoxDecoration(color: _bgColor),
              child: FlatButton(
                onPressed: () &#123;
                  setState(() &#123;
                      _bgColor = _bgColor == Colors.blue
              ? Colors.red
              : Colors.blue;
                  &#125;);
                &#125;,
                child: Text(
                  "AnimatedDecoratedBox",
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ))));
  &#125;
&#125;

class AnimatedDecoratedBox extends StatefulWidget &#123;
  AnimatedDecoratedBox(&#123;
    Key key,
    @required this.decoration,
    this.child,
    this.curve = Curves.linear,
    @required this.duration,
    this.reverseDuration,
  &#125;);

  final BoxDecoration decoration;
  final Widget child;
  final Duration duration;
  final Curve curve;
  final Duration reverseDuration;

  @override
  _AnimatedDecoratedBoxState createState() => _AnimatedDecoratedBoxState();
&#125;

class _AnimatedDecoratedBoxState extends State<AnimatedDecoratedBox>
    with SingleTickerProviderStateMixin &#123;
  @protected
  AnimationController get controller => _controller;
  AnimationController _controller;

  Animation<double> get animation => _animation;
  Animation<double> _animation;

  DecorationTween _tween;

  @override
  Widget build(BuildContext context) &#123;
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) &#123;
        return DecoratedBox(
          decoration: _tween.animate(_animation).value,
          child: child,
        );
      &#125;,
      child: widget.child,
    );
  &#125;

  @override
  void initState() &#123;
    super.initState();
    _controller = AnimationController(
      duration: widget.duration,
      reverseDuration: widget.reverseDuration,
      vsync: this,
    );
    _tween = DecorationTween(begin: widget.decoration);
    _updateCurve();
  &#125;

  void _updateCurve() &#123;
    if (widget.curve != null)
      _animation = CurvedAnimation(parent: _controller, curve: widget.curve);
    else
      _animation = _controller;
  &#125;

  @override
  void didUpdateWidget(AnimatedDecoratedBox oldWidget) &#123;
    super.didUpdateWidget(oldWidget);
    if (widget.curve != oldWidget.curve) _updateCurve();
    _controller.duration = widget.duration;
    _controller.reverseDuration = widget.reverseDuration;
    if (widget.decoration != (_tween.end ?? _tween.begin)) &#123;
      _tween
        ..begin = _tween.evaluate(_animation)
        ..end = widget.decoration;
      _controller
        ..value = 0.0
        ..forward();
    &#125;
  &#125;

  @override
  void dispose() &#123;
    _controller.dispose();
    super.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>封装了<code>AnimatedDecoratedBox</code>这样一个动画组件，在内部管理<code>AnimationController</code>，那它的动画是何时执行的呢？</p>
<pre><code class="copyable">AnimatedDecoratedBox(
  duration: duration,
  decoration: BoxDecoration(color: _decorationColor),
  child: FlatButton(
    onPressed: () &#123;
      setState(() &#123;
        _decorationColor = Colors.red;
      &#125;);
    &#125;,
    child: Text(
      "AnimatedDecoratedBox",
      style: TextStyle(color: Colors.white),
    ),
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>外部，点击按钮时调用了<code>setState()</code>方法，那么<code>AnimatedDecoratedBox</code>内部的<code>didUpdateWidget()</code>方法就会被调用，在这个方法里面判断新旧属性不一样，就执行动画。</p>
<pre><code class="copyable">  @override
  void didUpdateWidget(AnimatedDecoratedBox1 oldWidget) &#123;
    super.didUpdateWidget(oldWidget);
    if (widget.curve != oldWidget.curve)
      _updateCurve();
    _controller.duration = widget.duration;
    _controller.reverseDuration = widget.reverseDuration;
    if(widget.decoration!= (_tween.end ?? _tween.begin))&#123;
      _tween
        ..begin = _tween.evaluate(_animation)
        ..end = widget.decoration;
      _controller
        ..value = 0.0
        ..forward();
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于<code>didUpdateWidget()</code>何时执行：</p>
<ul>
<li><code>didUpdateWidget()</code>：在widget重新构建时，Flutter framework会调用<code>Widget.canUpdate</code>来检测Widget树中同一位置的新旧节点，然后决定是否需要更新，如果<code>Widget.canUpdate</code>返回<code>true</code>则会调用此回调。正如之前所述，<code>Widget.canUpdate</code>会在新旧widget的key和runtimeType同时相等时会返回true，也就是说在在新旧widget的key和runtimeType同时相等时<code>didUpdateWidget()</code>就会被调用。如果key或runtime不一样，整个widget state都会重构，initState()方法会重新执行。详见我之前的文章：<a href="https://juejin.cn/post/6844904097699594254" target="_blank" title="https://juejin.cn/post/6844904097699594254">juejin.cn/post/684490…</a></li>
</ul>
<p>上面是在<code>didUpdateWidget()</code>方法中进行手动控制的，flutter提供了两个类简化了这种控制：
<code>ImplicitlyAnimatedWidget</code>和<code>ImplicitlyAnimatedWidgetState</code>，详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2Fchapter9%2Fanimated_widgets.html%23_9-7-1-%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589%25E5%258A%25A8%25E7%2594%25BB%25E8%25BF%2587%25E6%25B8%25A1%25E7%25BB%2584%25E4%25BB%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/chapter9/animated_widgets.html#_9-7-1-%E8%87%AA%E5%AE%9A%E4%B9%89%E5%8A%A8%E7%94%BB%E8%BF%87%E6%B8%A1%E7%BB%84%E4%BB%B6" ref="nofollow noopener noreferrer">book.flutterchina.club/chapter9/an…</a></p>
<h4 data-id="heading-3">AnimatedWidget,AnimatedBuilder同时执行多个动画</h4>
<p>同时执行大小和颜色透明度的动画</p>
<pre><code class="copyable">class AnimatedImage extends AnimatedWidget &#123;
  AnimatedImage(&#123;Key key, Animation<double> animation,this.animation_1, this.animation_2&#125;)
      : super(key: key, listenable: animation);

      final Animation<double> animation_1;
      final Animation<double> animation_2;

  Widget build(BuildContext context) &#123;
    final Animation<double> animation = listenable;
    return new Center(
      child: Container(
          width: animation_1.value,
          height: animation_1.value,
          color: Colors.orange.withOpacity(animation_2.value),
      ),
    );
  &#125;
&#125;


class ScaleAnimationRoute1 extends StatefulWidget &#123;
  @override
  _ScaleAnimationRouteState createState() => new _ScaleAnimationRouteState();
&#125;

class _ScaleAnimationRouteState extends State<ScaleAnimationRoute1>
    with SingleTickerProviderStateMixin &#123;

  Animation<double> animation;
  AnimationController controller;
  Animation<double> animation_1;

  initState() &#123;
    super.initState();
    controller = new AnimationController(
        duration: const Duration(seconds: 3), vsync: this);
    //图片宽高从0变到300
    animation = new Tween(begin: 0.0, end: 300.0).animate(controller);

    animation_1 = new Tween(begin: 0.0, end: 1.0).animate(controller);

    //启动动画
    controller.forward();
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return AnimatedImage(animation: controller, animation_1:animation, animation_2: animation_1);
  &#125;

  dispose() &#123;
    //路由销毁时需要释放动画资源
    controller.dispose();
    super.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">交织动画</h4>
<p>有些时候我们可能会需要一些复杂的动画，这些动画可能由一个动画序列或重叠的动画组成，比如：有一个柱状图，需要在高度增长的同时改变颜色，等到增长到最大高度后，我们需要在X轴上平移一段距离。可以发现上述场景在不同阶段包含了多种动画，要实现这种效果，使用交织动画（Stagger Animation）<br>
待续</p>
<h4 data-id="heading-5">通用“动画切换”组件（AnimatedSwitcher)</h4>
<p>待续</p>
<h4 data-id="heading-6">自定义路由切换动画</h4>
<p>待续</p>
<h4 data-id="heading-7">Hero动画</h4>
<p>待续</p>
<p>参考文档：<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2Fchapter9%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/chapter9/" ref="nofollow noopener noreferrer">book.flutterchina.club/chapter9/</a></p></div>  
</div>
            