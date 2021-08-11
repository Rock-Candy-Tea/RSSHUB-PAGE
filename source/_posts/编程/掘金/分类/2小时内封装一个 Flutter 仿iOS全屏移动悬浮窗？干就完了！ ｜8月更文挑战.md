
---
title: '2小时内封装一个 Flutter 仿iOS全屏移动悬浮窗？干就完了！ ｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/087098eef85d4e0c872e840ccffe96e9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 19:10:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/087098eef85d4e0c872e840ccffe96e9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><em>废话开篇：大家都知道在苹果手机设置里面有“辅助触控”这样的一个开关，它其实就相当于一个屏幕软键盘，可以拖动到屏幕内的任意位置。闲置的时候为半透明状，用户操作的时候为不透明，在iOS原生上面可以将自定义view加载到keyWindow上，这样就view就处在所有的view最上面，那么，下面来具体在flutter上实现这样的功能。</em></p>
<p>效果展示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/087098eef85d4e0c872e840ccffe96e9~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-08-10 上午11.05.52.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>步骤一、封装自定义全屏浮动组件，将app内全部组件以child形式展示</strong></p>
</blockquote>
<p>其实，这里写的有点浮夸了，大致的意思就是封装一个组件，内部采用帧布局的形式进行排列。将app全部的内容作为主要组件进行展示，这时再简单的封装一下悬浮框组件作为帧布局上层组件即可，再利用 GestureDetector 进行拖拽手势监听，随即移动悬浮组件，那么，大体上的布局就完成了。</p>
<p>下面展示一下主要布局代码：</p>
<p>GeneralFloatOnScreenView 代码：</p>
<pre><code class="copyable">class GeneralFloatOnScreenView extends StatefulWidget &#123;
  Widget child;
  GeneralFloatOnScreenView(&#123;required this.child&#125;);
  @override
  State<StatefulWidget> createState() &#123;
    return new GeneralFloatOnScreenViewState();
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>GeneralFloatOnScreenViewState 代码</p>
<p>属性声明</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">//帧布局顶部距离
double _top = 0;
//帧布局左侧距离
double _left = 0;
//悬浮组件宽度，这里设置为宽高一直，因此height并没有声明
double _width = 50;
//记录屏幕或者父类组件宽度，用来判断拖拽听指挥后回归左右边缘判断
double _parentWidth = 0;
bool _isInitData = false;
//悬浮组件透明度
double _opacity = 0.3;
//动画控制器
late AnimationController _controller;
//动画
late Animation<double> _animation;
//这里的浮动组件声明成了属性，目的就是防止多次刷新当此组件内部有一些单独的逻辑的情况下。
late Widget _contentWidget;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化，在widget初始化里面去创建组件，这样只要当前组件不在屏幕上消失，那么即使不进行 wantKeepAlive 设置也不会重新初始。在悬浮组件上嵌套了一层 GestureDetector 手势来进行拖拽的移动。</p>
<pre><code class="hljs language-flutter copyable" lang="flutter">@override
void initState() &#123;
  // TODO: implement initState
  super.initState();
  _contentWidget = new GestureDetector(
    onPanUpdate: (DragUpdateDetails details)&#123;
      _left += details.delta.dx;
      _top += details.delta.dy;
      _changePosition();
    &#125;,
    onPanEnd: (DragEndDetails details)&#123;
      _changePosition();
      //判断悬浮组件左右回归操作
      _animateMoveBackAction();
    &#125;,
    onPanCancel: ()&#123;
      //当取消手势时进行边缘判断
      _changePosition();
    &#125;,
    onPanStart: (DragStartDetails details)&#123;
      //开始拖拽时将悬浮框透明度设置为1.0
      setState(() &#123;
        _opacity = 1.0;
      &#125;);
    &#125;,
    child: new Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.all(Radius.circular(_width / 2.0)),
        color: Colors.red,
      ),
      width: _width,
      height: _width,
    ),
  );
  
  //这里初始化动画类
  _controller =
      AnimationController(duration: Duration(milliseconds: 0), vsync: this);
  _animation =
      Tween(begin: _left, end: _left).animate(_controller);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>build 方法，这里没有什么特别要注意的，里面只是添加了帧布局进行包裹。</p>
<pre><code class="copyable">@override
Widget build(BuildContext context) &#123;
  //对于必要属性只进行一次计算
  if(_isInitData == false) &#123;
    _top = MediaQuery.of(context).size.height - 200;
    _left = 15;
    _parentWidth = MediaQuery.of(context).size.width;
    _isInitData = true;
  &#125;
  return new Stack(
    fit: StackFit.passthrough,
    children: <Widget>[
      this.widget.child,
      Positioned(
          top: _top,
          left: _left,
          child: new Opacity(
              child: _contentWidget,
              opacity: _opacity
          ),
      )
    ],
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>步骤二，如何进行手势的拖拽移动及边缘判断？</strong></p>
</blockquote>
<p>当 GestureDetector 手势监听 onPanUpdate 方法里进行悬浮组件的位置移动，直接修改属性 _left、_top值即可，这里注意进行一下屏幕边缘判断。</p>
<pre><code class="copyable">//位置边界判断
void _changePosition()&#123;
  if(_left < 0) &#123;
    _left = 0;
  &#125;

  if(_left >= MediaQuery.of(context).size.width - _width)&#123;
    _left = MediaQuery.of(context).size.width - _width;
  &#125;

  if(_top < 0) &#123;
    _top = 0;
  &#125;

  if(_top >= MediaQuery.of(context).size.height - _width) &#123;
    _top = MediaQuery.of(context).size.height - _width;
  &#125;
  //刷新界面
  setState(() &#123;

  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>步骤三、如何进行拖拽手势结束悬浮组件回归边缘动画？</strong></p>
</blockquote>
<p>当GestureDetector 手势监听 onPanEnd 方法执行的时候判断当前悬浮组件中轴线停留的位置与屏幕（或者父组件中轴线）的位置关系，偏左向左边缘靠，偏右向有边缘靠。这里的动画并没有添加到某个动画组件上，而是直接执行，监听animation的值的变化进行悬浮组件的回归移动。当动画直接状态为结束后再将悬浮组件的透明度设置为半透明状态。</p>
<pre><code class="copyable">//中轴线回弹动画
void _animateMoveBackAction()&#123;
  double centerX = _left + _width / 2.0;
  double toPositionX = 0;
  double needMoveLength = 0;
  if(centerX <= _parentWidth / 2.0) &#123;
    needMoveLength = _left;
  &#125; else &#123;
    needMoveLength = (_parentWidth - _left - _width);
  &#125;
  double precent = (needMoveLength / (_parentWidth / 2.0));
  int time = (600 * precent).ceil();
  if(centerX <= _parentWidth / 2.0)&#123;
    //回到左边缘
    toPositionX = 0;
  &#125; else &#123;
    //回到右边缘
    toPositionX = _parentWidth - _width;
  &#125;
  //这里由于根据需要偏移的距离需要重新设置动画执行时长，那么之前的动画控制器就先销毁再创建。
  _controller.dispose();
  _controller =
      AnimationController(duration: Duration(milliseconds: time), vsync: this);
  //这里对监听 animation 执行过程进行监听，重新绘制悬浮组件位置
  _animation =
      Tween(begin: _left, end: toPositionX * 1.0).animate(_controller);
  _animation.addListener(() &#123;
    _left = _animation.value.toDouble();
    setState(() &#123;

    &#125;);
  &#125;);
  _animation.addStatusListener((status) &#123;
    if(status == AnimationStatus.completed)&#123;
      Future.delayed(Duration(microseconds: 200),()&#123;
        setState(() &#123;
          _opacity = 0.3;
        &#125;);
      &#125;);
    &#125;
  &#125;);
  _controller.forward();

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意组件销毁时进行动画控制器的销毁操作，注意先执行自身的相关操作后执行super.dispos()</p>
<pre><code class="copyable">@override
void dispose() &#123;
  // TODO: implement dispose
  _controller.dispose();
  super.dispose();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>步骤四、如何用这个封装好的组件？</strong></p>
</blockquote>
<p>将之前 app 的全部组件用 GeneralFloatOnScreenView 包裹起来，将它作为child传给自定义组件即可</p>
<pre><code class="copyable">home: new Scaffold(
  //这里的 new BottomTabbarWidget() 是 app 的全部组件，将它作为child传给自定义组件即可
  body: new GeneralFloatOnScreenView(child: new BottomTabbarWidget()),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，简单的仿iOS全屏悬浮窗就实现好了，代码拙劣，大神勿喷，如果对大家有帮助，更是深感欣慰。</p></div>  
</div>
            