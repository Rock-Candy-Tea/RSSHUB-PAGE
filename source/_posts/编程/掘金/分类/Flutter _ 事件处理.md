
---
title: 'Flutter _ 事件处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8a7e943430479f8d11f01a208dccf8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 19:18:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8a7e943430479f8d11f01a208dccf8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">概述</h3>
<p>在移动端，各个平台或者 UI 系统的事件模型都是基本一致，即：一次完整的事件分为三个阶段，手指按下，移动，抬起，而其他的双击，拖动等都是基于这些事件的</p>
<p>当指针按下时，Flutter 会对应用程序执行<code>命中测试(Hit Test)</code> ，以确定指针与屏幕接触的位置存在哪些 Widget，指针按下事件(以及该指针的后续事件)会被分发到由命中测试发现的最内部的组件，然后从哪里开始，事件会在组件树中向上冒泡，这些事件会从最内部的组件分发的组件树的根路径上的所有组件，这个 Web 开发浏览器的事件冒泡机制相似，但是 Flutter 中没有机制取消或者停止冒泡过程，而浏览器是可以停止的。</p>
<blockquote>
<p>注意：只有通过命中测试的组件才能触发事件</p>
</blockquote>
<h3 data-id="heading-1">原始指针事件处理</h3>
<p>Flutter 中可以使用 Listener 来监听原始触摸事件，按照<Flutter实战> 中的分类，Listener 也是一个功能性组件，下面是 Listener 的构造函数定义：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Listener(&#123;
  Key key,
  <span class="hljs-keyword">this</span>.onPointerDown, <span class="hljs-comment">//手指按下回调</span>
  <span class="hljs-keyword">this</span>.onPointerMove, <span class="hljs-comment">//手指移动回调</span>
  <span class="hljs-keyword">this</span>.onPointerUp,<span class="hljs-comment">//手指抬起回调</span>
  <span class="hljs-keyword">this</span>.onPointerCancel,<span class="hljs-comment">//触摸事件取消回调</span>
  <span class="hljs-keyword">this</span>.behavior = HitTestBehavior.deferToChild, <span class="hljs-comment">//在命中测试期间如何表现</span>
  Widget child
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>behavior 在后面专门介绍</li>
</ul>
<p>示例：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventTest</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _EventTestState createState() => _EventTestState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_EventTestState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">EventTest</span>> </span>&#123;
  PointerEvent _event;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Listener(
      child: Container(
        margin: EdgeInsets.only(top: <span class="hljs-number">50</span>),
        color: Colors.blue,
        alignment: Alignment.center,
        child: Text(_event?.toString() ?? <span class="hljs-string">""</span>,
            style: TextStyle(color: Colors.white)),
      ),
      onPointerDown: (PointerDownEvent event) =>
          setState(() => &#123;_event = event&#125;),
      onPointerMove: (PointerMoveEvent event) =>
          setState(() => &#123;_event = event&#125;),
      onPointerUp: (PointerUpEvent event) => setState(() => &#123;_event = event&#125;),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img alt="image-20210330215620656" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8a7e943430479f8d11f01a208dccf8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>手指在蓝色区域内移动即可看到当前指针偏移，当触发指针事件时，参数 PointerDownEvent，PointerMoveEvent，PointerUpEvent 都是 <code>PointerEvent</code> 的子类，PointerEvent 包含当前指针的一些信息，如：</p>
<ul>
<li>position：他是鼠标相对于全局坐标的偏移</li>
<li>delta：两次指针移动事件的距离</li>
<li>pressure：按压力度，如果手机屏幕支持压力传感器，此属性才会有意义，如手机不支持，始终为 1。</li>
<li>orientation：指针移动方向，是一个角度值</li>
</ul>
<p>上面只是一些常用属性，除了这些还有很多其他属性，可自行查看 API</p>
<p><strong>behavior</strong></p>
<p>他决定子组件如何响应命中测试，他的值为 HitTestBehavior，是一个枚举类，有三个枚举值</p>
<ul>
<li>
<p>deferToChild：子组件会一个一个的进行命中测试，如果子组件中有测试通过的，则当前组件通过，这意味着指针事件作用于子组件时，其父级组件也肯定可以接收到事件</p>
</li>
<li>
<p>opaque：在命中测试时，将当前组件当初不透明处理(即使本身是透明的)，最终的效果相当于当前 Widget 的整个区域都是点击区域。栗子：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Listener(
    child: ConstrainedBox(
        constraints: BoxConstraints.tight(Size(<span class="hljs-number">300.0</span>, <span class="hljs-number">150.0</span>)),
        child: Center(child: Text(<span class="hljs-string">"Box A"</span>)),
    ),
    <span class="hljs-comment">//behavior: HitTestBehavior.opaque,</span>
    onPointerDown: (event) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"down A"</span>)
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例子，只有点击文本区域才会触发点击事件，因为 deferToChild 会去子组件判断是否命中测试，该例中子组件就是 Text("Box A") 。</p>
<p>如果想让整个 300x150 的区域都能点击，我们可以将 behavior 设为 HitTestBehavior.opaque。</p>
<blockquote>
<p>注意：该属性不能用于在组件树中拦截（忽略）事件，他只是决定命中测试时的组件大小</p>
</blockquote>
</li>
<li>
<p>translucent：当组件点击透明区域时，可以对自身边界及底部可视区域都进行命中测试。这意味着点击顶部组件透明区域时，顶部组件和底部组件都可以接收到事件，例如：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Stack(
  children: <Widget>[
    Listener(
      child: ConstrainedBox(
        constraints: BoxConstraints.tight(Size(<span class="hljs-number">300.0</span>, <span class="hljs-number">200.0</span>)),
        child: DecoratedBox(
            decoration: BoxDecoration(color: Colors.blue)),
      ),
      onPointerDown: (event) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"down0"</span>),
    ),
    Listener(
      child: ConstrainedBox(
        constraints: BoxConstraints.tight(Size(<span class="hljs-number">200.0</span>, <span class="hljs-number">100.0</span>)),
        child: Center(child: Text(<span class="hljs-string">"左上角200*100范围内非文本区域点击"</span>)),
      ),
      onPointerDown: (event) => <span class="hljs-built_in">print</span>(<span class="hljs-string">"down1"</span>),
      <span class="hljs-comment">//behavior: HitTestBehavior.translucent, //放开此行注释后可以"点透"</span>
    )
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上栗中，当注释掉最后一行代码，在左上角200x100 范围内非文本区域点击时(顶部组件透明区域)，控制台只会打印 down0，也就是说顶部没有接收到事件，只有底部接收到了</p>
<p>当放开注释后，再点击时顶部和底部都会接收到事件</p>
</li>
</ul>
<h4 data-id="heading-2">忽略 PinterEvent</h4>
<p>如果我们不想让某个子树响应 PointerEvent ，则可以使用 <code>IgnorePointer</code> 和 <code>AbsorbPointer</code>，这两个组件都能阻止子树接受指针事件，不同之处在于 <code>AbsorbPointer</code> 会参与命中测试，而 <code>IgnorePointer</code> 本身不会参与，这就意味着 <code>AbsorbPointer</code> 本身是可以接受指针事件的(但其子树不行)，而 <code>IngorePointer</code> 不可以，例：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Listener(
  child: AbsorbPointer(
    child: Listener(
      child: Container(
        color: Colors.red,
        width: <span class="hljs-number">200.0</span>,
        height: <span class="hljs-number">100.0</span>,
      ),
      onPointerDown: (event)=><span class="hljs-built_in">print</span>(<span class="hljs-string">"in"</span>),
    ),
  ),
  onPointerDown: (event)=><span class="hljs-built_in">print</span>(<span class="hljs-string">"up"</span>),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击 Container 时，由于他在 AbsorbPointer 子树上，所以不会响应指针事件，</p>
<p>但是 AbsorbPoniter 本身是可以接受指针事件的，所以会输出 up，如果将  <code>AbsorbPointer</code> 换成 <code>IgnorePointer</code>，那么两个都不会输出；</p>
<h3 data-id="heading-3">手势识别</h3>
<h4 data-id="heading-4">GestuerDetector</h4>
<p><code>GestureDetector</code> 是一个用于手势识别的功能性组件，我们可以通过它来识别各种手势</p>
<p><code>GestureDetector</code> 实际上是指针事件的语义化封装，下面我们来看一下各种手势识别。</p>
<h5 data-id="heading-5">点击，双击，长按</h5>
<p>我们通过 GestureDetector 对 Container 进行手势识别，触发相应事件后，在 Container 上显示事件名，如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_EventTestState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">EventTest</span>> </span>&#123;
  <span class="hljs-comment">//事件名称</span>
  <span class="hljs-built_in">String</span> _operation = <span class="hljs-string">""</span>;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Center(
      child: GestureDetector(
        child: Container(
          width: <span class="hljs-number">200</span>,
          color: Colors.blue,
          alignment: Alignment.center,
          height: <span class="hljs-number">100</span>,
          child: Text(_operation, style: TextStyle(color: Colors.white,fontSize: <span class="hljs-number">20</span>)),
        ),
        onTap: () => upDateText(<span class="hljs-string">"tap"</span>), <span class="hljs-comment">//单击</span>
        onDoubleTap: () => upDateText(<span class="hljs-string">"doubleTap"</span>), <span class="hljs-comment">//双击</span>
        onLongPress: () => upDateText(<span class="hljs-string">"longPress"</span>), <span class="hljs-comment">//长按</span>
      ),
    );
  &#125;

  <span class="hljs-keyword">void</span> upDateText(<span class="hljs-built_in">String</span> text) &#123;
    setState(() &#123;
      _operation = text;
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="345" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae13250f20d9475884ede903f2ad4faa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：当同时监听 onTop 和 onDoubleTap 时，当用户触发 tap 事件时，会有 200 毫秒的延时，这是因为可能会再次点击触发双击事件</p>
<p>如果只监听了 onTap，则不会有延时</p>
</blockquote>
<h5 data-id="heading-6">拖动，滑动</h5>
<p>一次完整的手势过程是指用户手指按下到抬起的整个过程，期间，用户按下后可能会移动，也可能不移动。</p>
<p>GestureDetector 对拖动和滑动事件时没有区分的，他们本质是一样的。</p>
<p>GestureDetector 会把要监听的组件的原点(左上角)作为本次手势的原点，当监听组件上手指按下时，手势识别就会开始。例：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_EventTestState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">EventTest</span>> <span class="hljs-title">with</span> <span class="hljs-title">SingleTickerProviderStateMixin</span> </span>&#123;

  <span class="hljs-built_in">double</span> _top = <span class="hljs-number">100.0</span>; <span class="hljs-comment">//距离顶部的偏移</span>
  <span class="hljs-built_in">double</span> _left = <span class="hljs-number">100.0</span>; <span class="hljs-comment">//距离左边的偏移</span>
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;

    <span class="hljs-keyword">return</span> Scaffold(
      body: Stack(
        children: <Widget>[
          Positioned(
            top: _top,
            left: _left,
            child: GestureDetector(
              child: CircleAvatar(child: Text(<span class="hljs-string">"A"</span>)),
              <span class="hljs-comment">//手指按下回调</span>
              onPanDown: (DragDownDetails e) &#123;
                <span class="hljs-built_in">print</span>(<span class="hljs-string">'用户手指按下 <span class="hljs-subst">$&#123;e.globalPosition&#125;</span>'</span>);
              &#125;,
              <span class="hljs-comment">//手指滑动回调</span>
              onPanUpdate: (DragUpdateDetails e) &#123;
                <span class="hljs-comment">//滑动时，更新偏移</span>
                <span class="hljs-built_in">print</span>(<span class="hljs-string">'滑动'</span>);
                setState(() &#123;
                  _left += e.delta.dx;
                  _top += e.delta.dy;
                &#125;);
              &#125;,
              onPanEnd: (DragEndDetails e) &#123;
                <span class="hljs-comment">//滑动结束，打印 x，y轴速度</span>
                <span class="hljs-built_in">print</span>(e.velocity);
              &#125;,
            ),
          )
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>globalPosition：此属性为用户按下时相对于屏幕(非父组件)原点的偏移</li>
<li>delta：当用户在屏幕上滑动时，会触发多次 Update 事件，dalta 指一次 Update 事件滑动的偏移量</li>
<li>velocity：该属性代表用户抬起时的滑动速度（包含x，y两个轴的），上例中没有处理抬起的速度，常见的效果是根据抬起手指的速度做一个减速动画</li>
</ul>
<p>效果如下：</p>
<img alt="345" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2fd9fe69aed40e99feafb2ea071c7f0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<pre><code class="hljs language-text copyable" lang="text">I/flutter ( 8239): 用户手指按下 Offset(134.9, 280.7)
I/flutter ( 8239): 滑动
I/chatty  ( 8239): uid=10152(com.flutter.flutter_study) 1.ui identical 302 lines
I/flutter ( 8239): 滑动
I/flutter ( 8239): Velocity(-59.6, 244.0)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">单一方向拖动</h5>
<p>在很多场景中，我们只需要沿着一个方向来拖动，如一个垂直方向的列表</p>
<p>GestureDetector 支持特定方向的手势事件，例如：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Positioned(
  top: _top,
  child: GestureDetector(
    child: CircleAvatar(child: Text(<span class="hljs-string">"A"</span>)),
    <span class="hljs-comment">//手指按下回调</span>
    onPanDown: (DragDownDetails e) &#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'用户手指按下 <span class="hljs-subst">$&#123;e.globalPosition&#125;</span>'</span>);
    &#125;,
    onVerticalDragUpdate: (DragUpdateDetails e) &#123;
      setState(() &#123;
        _top += e.delta.dy;
      &#125;);
    &#125;,
    onPanEnd: (DragEndDetails e) &#123;
      <span class="hljs-comment">//滑动结束，打印 x，y轴速度</span>
      <span class="hljs-built_in">print</span>(e.velocity);
    &#125;,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改滑动的那个例子如上即可</p>
<h5 data-id="heading-8">缩放</h5>
<p>GestureDetector 可以监听缩放事件，如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Center(
  child: GestureDetector(
    child: Image.asset(<span class="hljs-string">"./images/avatar.jpg"</span>, width: _width),
    onScaleUpdate: (ScaleUpdateDetails details) &#123;
      setState(() &#123;
        <span class="hljs-comment">//缩放倍数在 0.8 到 10 倍之间</span>
        _width = <span class="hljs-number">100</span> * details.scale.clamp(<span class="hljs-number">.8</span>, <span class="hljs-number">10.0</span>);
      &#125;);
    &#125;,
  ),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<img alt="345" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d0e92656aee4ce190697f874f46e0cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>上例比较简单，实际中我们可能还需要一些其他功能，如双击放大缩小，执行动画等，有兴趣的可以先尝试一下</p>
<h4 data-id="heading-9">GestureRecognizer</h4>
<p><code>getstureDetector</code> 内部是使用一个或者多个 <code>GestureRecognizer</code> 来识别各种手势的，而 GestureRecognizer 的作用就是通过 Listener 将原始指针转换为语义手势</p>
<p><code>GestureRecognizer</code> 是一个抽象类，一种手势对应一个子类，Flutter 实现了丰富的手势识别器，我们可以直接使用。</p>
<p>例如：</p>
<p>我们要给一段富文本 (RichText) ，的不同部分添加事件处理器，但是 TextSpan 并不是一个 widget，所以不能用 GestureDetector。但是 TextSpan 有一个 Recongizer 属性，他可以接收一个 GestureRecognizer。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-built_in">bool</span> _toggle = <span class="hljs-keyword">false</span>; <span class="hljs-comment">//变色开关</span>
TapGestureRecognizer _recognizer = TapGestureRecognizer();

Widget bothDirectionTest() &#123;
  <span class="hljs-keyword">return</span> Center(
    child: Text.rich(TextSpan(children: [
      TextSpan(text: <span class="hljs-string">"你好世界"</span>),
      TextSpan(
          text: <span class="hljs-string">"点击变色"</span>,
          style: TextStyle(
              fontSize: <span class="hljs-number">30</span>, color: _toggle ? Colors.red : Colors.yellow),
          recognizer: _recognizer
            ..onTap = () &#123;
              setState(() &#123;
                _toggle = !_toggle;
              &#125;);
            &#125;),
      TextSpan(text: <span class="hljs-string">"你好世界"</span>)
    ])),
  );
&#125;
<span class="hljs-meta">@override</span>
<span class="hljs-keyword">void</span> dispose() &#123;
    <span class="hljs-comment">//用到GestureRecognizer的话一定要调用其dispose方法释放资源</span>
    _recognizer.dispose();
    <span class="hljs-keyword">super</span>.dispose();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：使用 GestureRecognizer 之后，一定要调用其 dispose 方法来释放资源(主要是取消内部的计时器)，运行效果如下：</p>
<p><img alt="345" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cbdf19701c24ea7b5840cf59b279ec0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">手势竞争与冲突</h4>
<h5 data-id="heading-11">竞争</h5>
<p>如在上例中，同时监听水平方向和垂直方向的拖动事件，那么斜着滑动时那个方向会生效？ 实际上取决于第一次移动时两个轴上的位移分量，那个轴的大，那么哪个轴就会在本次滑动事件中胜出</p>
<p>实际上 Flutter 中引入了一个 Arenal 的概念，直译为 <strong>竞技场</strong> 的意思，每一个手势识别器(GestureRecognizer) 都是一个竞争者(GestureArenaMember)，当发生滑动事件时，他们都要在 <strong>竞技场</strong> 去竞争本次事件的处理权，而最终只有一个竞争者会胜出。</p>
<p>例如有一个 ListView，他的第一个子组件也是 ListView，如果滑动子 ListView，父 ListView 会动吗？答案肯定是不会动的，这时只有子 ListView 会动，这是因为子 LsitView 货到了滑动事件的处理权。</p>
<p><strong>示例</strong></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> _top1 = <span class="hljs-number">100.0</span>;
<span class="hljs-keyword">var</span> _left1 = <span class="hljs-number">100.0</span>;

Widget bothDirection() &#123;
  <span class="hljs-keyword">return</span> Stack(
    children: [
      Positioned(
        top: _top1,
        left: _left1,
        child: GestureDetector(
          child: CircleAvatar(child: Text(<span class="hljs-string">"A"</span>)),
          onVerticalDragUpdate: (DragUpdateDetails details) &#123;
            setState(() &#123;
              _top1 += details.delta.dy;
            &#125;);
          &#125;,
          onHorizontalDragUpdate: (DragUpdateDetails details) &#123;
            setState(() &#123;
              _left1 += details.delta.dx;
            &#125;);
          &#125;,
        ),
      )
    ],
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行之后，每次拖动只会沿着一个方向移动，而竞争者发生在手指按下后首次移动时</p>
<p>上例中获胜的条件是，首次移动时的位置在水平和垂直方向上分量大的一个获胜</p>
<h4 data-id="heading-12">手势冲突</h4>
<p>由于手势竞争最终只有一个胜出者，所以，当有多个手势识别器时，可能会产生冲突；</p>
<p>例如有一个 Widget，可以左右拖动，现在我们也想检测它上面手指按下和抬起的事件，如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> _left2 = <span class="hljs-number">100.0</span>;
Widget flictTest() &#123;
  <span class="hljs-keyword">return</span> Stack(
    children: [
      Positioned(
        left: _left2,
        top: <span class="hljs-number">100</span>,
        child: GestureDetector(
          child: CircleAvatar(child: Text(<span class="hljs-string">"A"</span>)),
          onHorizontalDragUpdate: (DragUpdateDetails details) &#123;
            setState(() &#123;
              _left2 += details.delta.dx;
            &#125;);
          &#125;,
          onHorizontalDragEnd: (details) &#123;
            <span class="hljs-built_in">print</span>(<span class="hljs-string">'onHorizontalDragEnd'</span>);
          &#125;,
          onTapDown: (details) &#123;
            <span class="hljs-built_in">print</span>(<span class="hljs-string">'down'</span>);
          &#125;,
          onTapUp: (details) &#123;
            <span class="hljs-built_in">print</span>(<span class="hljs-string">'up'</span>);
          &#125;,
        ),
      )
    ],
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拖动后，日志如下：</p>
<pre><code class="copyable">0I/flutter ( 4315): down
I/flutter ( 4315): onHorizontalDragEnd
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现没有打印 up，这是因为拖动时，在按下手指没有移动时，拖动手势还没有完整的语义，此时 TapDown 手势胜出，此时打印 down，而拖动时，拖动手势胜出，当抬起时， onHorizontalDragEnd 和 onTap 发生冲突，但是应为是在拖动的语义中，所以 onHorizeontalDragend 胜出，所以就会打印 onHorizontalDragEnd。</p>
<p>如果我们的逻辑代码中，对手指的按下和抬起时强依赖的，例如轮播组件，我们希望按下时暂停轮播，抬起时恢复轮播。但是由于轮播组件中本身可能已经处理了拖动手势，甚至支持了缩放手势，这时外部如果再用 onTapDown，onTap 来监听是不行的。</p>
<p>这个时候就可以同个 Listener 监听原始指针事件就行：</p>
<pre><code class="hljs language-dart copyable" lang="dart">Listener(
    child: GestureDetector(
      child: CircleAvatar(child: Text(<span class="hljs-string">"A"</span>)),
      onHorizontalDragUpdate: (DragUpdateDetails details) &#123;
        setState(() &#123;
          _left2 += details.delta.dx;
        &#125;);
      &#125;,
      onHorizontalDragEnd: (details) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">'onHorizontalDragEnd'</span>);
      &#125;,
    ),
    onPointerDown: (details)&#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'onPointerDown'</span>);
    &#125;,
    onPointerUp: (details)&#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'onPointerUp'</span>);
    &#125;,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>手势冲突只是手势级别的，而手势是对原始指针的语义化识别，所以在遇到复杂的冲突场景时，都可以通过 Listener 直接识别原始指针事件来解决冲突</p>
<h3 data-id="heading-13">事件总线</h3>
<p>在 App 中，我们经常需要一个广播机制，用以夸页面事件通知，例如注销登录时，某些页面可能需要进行状态更新。这个时候一个事件总线便会非常有用；</p>
<p>事件总线通常实现了订阅者模式，订阅者包含订阅者和发布者两个角色，可以通过事件总线来触发事件和监听事件；</p>
<p>代码如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">typedef</span> <span class="hljs-keyword">void</span> EventCallback(arg);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventBus</span> </span>&#123;
  <span class="hljs-comment">//私有构造</span>
  EventBus._internal();

  <span class="hljs-keyword">static</span> EventBus _singleton = <span class="hljs-keyword">new</span> EventBus._internal();

  <span class="hljs-comment">//工厂构造函数</span>
  <span class="hljs-keyword">factory</span> EventBus() => _singleton;

  <span class="hljs-comment">//保存时间订阅者队列，key：事件名(id)，value:对应的实际订阅者队列</span>
  <span class="hljs-keyword">var</span> _eMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span><<span class="hljs-built_in">Object</span>, <span class="hljs-built_in">List</span><EventCallback>>();

  <span class="hljs-comment">///<span class="markdown">添加订阅者</span></span>
  <span class="hljs-keyword">void</span> <span class="hljs-keyword">on</span>(eventName, EventCallback f) &#123;
    <span class="hljs-keyword">if</span> (eventName == <span class="hljs-keyword">null</span> || f == <span class="hljs-keyword">null</span>) <span class="hljs-keyword">return</span>;
    _eMap[eventName] ??= [];
    _eMap[eventName].add(f);
  &#125;

  <span class="hljs-comment">///<span class="markdown">移除订阅者</span></span>
  <span class="hljs-keyword">void</span> off(eventName, [EventCallback f]) &#123;
    <span class="hljs-keyword">var</span> list = _eMap[eventName];
    <span class="hljs-keyword">if</span> (eventName == <span class="hljs-keyword">null</span> || list == <span class="hljs-keyword">null</span>) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (f == <span class="hljs-keyword">null</span>) &#123;
      _eMap[eventName] = <span class="hljs-keyword">null</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      list.remove(f);
    &#125;
  &#125;

  <span class="hljs-comment">///<span class="markdown">触发订阅者</span></span>
  <span class="hljs-keyword">void</span> emit(eventName, [arg]) &#123;
    <span class="hljs-keyword">var</span> list = _eMap[eventName];
    <span class="hljs-keyword">if</span> (list == <span class="hljs-keyword">null</span>) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">int</span> len = list.length - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = len; i > <span class="hljs-number">-1</span>; i--) &#123;
      list[i](arg);
    &#125;
  &#125;
&#125;

<span class="hljs-comment">///<span class="markdown">定义一个 top-level,全局变量，页面引入该文件之后可以直接使用 bug</span></span>
<span class="hljs-keyword">var</span> bus = <span class="hljs-keyword">new</span> EventBus();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//监听登录失效</span>
bus.<span class="hljs-keyword">on</span>(Event.LOGIN_OUT, (arg) &#123;
  SpUtil.putString(Application.accessToken, <span class="hljs-keyword">null</span>);
  Application.router.navigateTo(context, Routes.login, clearStack: <span class="hljs-keyword">true</span>);
&#125;);

<span class="hljs-comment">//触发失效事件</span>
bus.emit(Event.LOGIN_OUT, <span class="hljs-keyword">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：Dart 中实现点了模式的标准做法就是使用 static 变量 + 工厂构造函数的方式，这样就可以保证 new EventBus() 始终返回都是同一个实例</p>
</blockquote>
<p>事件总线常用于组件之间的状态共享，但是关于组件之间的状态共享也有一些专门的包，如 redux，以及 Provider。</p>
<p>对于一些简单的应用，事件总线总是奏议满足业务需求，如果觉得使用状态管理包的话，一定要想清楚 APP 是否有必要使用它，防止化简为繁的过度设计。</p>
<hr>
<h3 data-id="heading-14">参考</h3>
<blockquote>
<p>参考自 Flutter实战</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            