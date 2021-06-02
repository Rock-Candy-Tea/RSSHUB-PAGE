
---
title: 'flutter 简单实现浏览器H5粒子动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b582a3d7b88f46e4a4ebbc08833bb78a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 22:56:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b582a3d7b88f46e4a4ebbc08833bb78a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">flutter 简单实现浏览器H5粒子动画</h1>
<p>我们常见H5炫酷的粒子动画，H5有的，flutter都想拥有。</p>
<h2 data-id="heading-1">1.老规矩先上图!</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b582a3d7b88f46e4a4ebbc08833bb78a~tplv-k3u1fbpfcp-watermark.image" alt="粒子动画2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2.大致思路分析</h2>
<p>1.先考虑画点</p>
<p>随机会在屏幕上产生相应的点，点会自己移动 ,x，y轴移动速度也是随机的</p>
<p>当点在碰到边缘时，速度变方向</p>
<p>2.画线</p>
<p>一个点和周围一定距离内的点相连，距离越远颜色透明度越低</p>
<p>应该要有最大连接数</p>
<p>3.鼠标移动</p>
<p>鼠标落下的点与周围一定距离的点相连</p>
<h2 data-id="heading-3">3.具体实现类</h2>
<p>1.鼠标监听事件：MouseRegion</p>
<p>2.重绘控件 ：CustomPainter</p>
<p>3.自定义view相关属性</p>
<pre><code class="hljs language-dart copyable" lang="dart"> LiziConfig(&#123;
    Key key,
    <span class="hljs-meta">@required</span> <span class="hljs-keyword">this</span>.context,
    <span class="hljs-keyword">this</span>.vx = <span class="hljs-number">4</span>,<span class="hljs-comment">//点x轴速度,正为右，负为左</span>
    <span class="hljs-keyword">this</span>.vy = <span class="hljs-number">4</span>,<span class="hljs-comment">//点球y轴速度</span>
    <span class="hljs-keyword">this</span>.radius = <span class="hljs-number">2</span>,<span class="hljs-comment">//点半径</span>
    <span class="hljs-keyword">this</span>.count = <span class="hljs-number">100</span>,<span class="hljs-comment">//点个数</span>
    <span class="hljs-keyword">this</span>.color = <span class="hljs-keyword">const</span> Color.fromRGBO(<span class="hljs-number">121</span>, <span class="hljs-number">162</span>, <span class="hljs-number">185</span>, <span class="hljs-number">1.0</span>),<span class="hljs-comment">//点颜色</span>
    <span class="hljs-keyword">this</span>.stroke = <span class="hljs-keyword">const</span> Color.fromRGBO(<span class="hljs-number">130</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">1.0</span>),<span class="hljs-comment">//线条颜色</span>
    <span class="hljs-keyword">this</span>.dist = <span class="hljs-number">100</span>,<span class="hljs-comment">//点吸附距离</span>
    <span class="hljs-keyword">this</span>.eDist = <span class="hljs-number">130</span>,<span class="hljs-comment">//鼠标吸附距离</span>
    <span class="hljs-keyword">this</span>.maxConn = <span class="hljs-number">10</span>,<span class="hljs-comment">//点到点最大连接数</span>
  &#125;) : <span class="hljs-keyword">super</span>(key: key);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.点相关属性</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span></span>&#123;
  <span class="hljs-built_in">double</span> x;<span class="hljs-comment">//x轴坐标</span>
  <span class="hljs-built_in">double</span> y;<span class="hljs-comment">//y轴坐标</span>
  <span class="hljs-built_in">double</span> vx;<span class="hljs-comment">//x轴移动速度</span>
  <span class="hljs-built_in">double</span> vy;<span class="hljs-comment">//y轴移动速度</span>
  <span class="hljs-built_in">int</span> conNum;<span class="hljs-comment">//点连接数量</span>
  Point(<span class="hljs-keyword">this</span>.x, <span class="hljs-keyword">this</span>.y, <span class="hljs-keyword">this</span>.vx, <span class="hljs-keyword">this</span>.vy,<span class="hljs-keyword">this</span>.conNum);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.详细代码</h2>
<p>1.先画出不同的点</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5e8f8c275f14ad48041d19b0a641835~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-02_144935.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">///<span class="markdown">初始化点的坐标</span></span>
<span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < count; i++) &#123;
      Point point=<span class="hljs-keyword">new</span> Point(
          Random().nextDouble()*MediaQuery.of(contextO).size.width,
          Random().nextDouble()*MediaQuery.of(contextO).size.height,
          vx / <span class="hljs-number">2</span> - Random().nextDouble() * vx,
          vy / <span class="hljs-number">2</span> - Random().nextDouble() * vy,<span class="hljs-number">0</span>);
      points.add(point);
    &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> paint(Canvas canvas, Size sizes) &#123;
    <span class="hljs-comment">///<span class="markdown">画点</span></span>
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < points.length; i++) &#123;
      canvas.drawCircle(Offset(points[i].x, points[i].y),
          radius.toDouble(),_paintPoint);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.移动点</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">///<span class="markdown">定时器去更改点位置</span></span>
<span class="hljs-keyword">const</span> oneSec = <span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">40</span>); <span class="hljs-comment">//间隔1秒</span>
    qrtimer = <span class="hljs-keyword">new</span> Timer.periodic(oneSec, (timer) &#123;
      _drawPoint();
    &#125;);

<span class="hljs-comment">///<span class="markdown">移动点</span></span>
  <span class="hljs-keyword">void</span> _drawPoint() &#123;
      setState(() &#123;
        <span class="hljs-keyword">if</span>(points.isNotEmpty) &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < count; i++) &#123;
            _borderPoint(points[i]);
            points[i].conNum=<span class="hljs-number">0</span>;
          &#125;
        &#125;
      &#125;);
  &#125;

  <span class="hljs-comment">///<span class="markdown">边界处理</span></span>
  <span class="hljs-keyword">void</span> _borderPoint(Point p) &#123;
    Size size=MediaQuery.of(context).size;
    <span class="hljs-keyword">if</span>(p.x<=<span class="hljs-number">0</span>||p.x>=size.width)&#123;
      p.vx=-p.vx;
      p.x+=p.vx;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(p.y<=<span class="hljs-number">0</span>||p.y>=size.height)&#123;
      p.vy = -p.vy;
      p.y += p.vy;
    &#125;<span class="hljs-keyword">else</span>&#123;
      p.x=p.x+p.vx;
      p.y=p.y+p.vy;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.画线</p>
<pre><code class="hljs language-dart copyable" lang="dart"> <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < points.length; i++) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> j = <span class="hljs-number">0</span>; j < points.length; j++) &#123;
        <span class="hljs-keyword">if</span>(i!=j)&#123;<span class="hljs-comment">///<span class="markdown">如果不是同一个点</span></span>
          <span class="hljs-comment">///<span class="markdown">算出两点间的距离</span></span>
          <span class="hljs-built_in">double</span> dx=points[i].x-points[j].x;
          <span class="hljs-built_in">double</span> dy=points[i].y-points[j].y;
          <span class="hljs-built_in">double</span> distp=sqrt(dx*dx+dy*dy);
          <span class="hljs-comment">// print("距离:"+distp.toString());</span>

          <span class="hljs-comment">/// <span class="markdown">两点距离小于吸附距离，而且小于最大连接数，则画线</span></span>
          <span class="hljs-keyword">if</span>(distp <= dist && points[i].conNum <maxConn)&#123;
              points[i].conNum++;
              _paintLine.strokeWidth=<span class="hljs-number">0.5</span>-distp/dist;
              _paintLine.color=Color.fromRGBO(stroke.red, stroke.green, stroke.blue, <span class="hljs-number">1</span>-distp/dist);

              canvas.drawLine(Offset(points[i].x, points[i].y), Offset(points[j].x, points[j].y), _paintLine);
          &#125;

          <span class="hljs-comment">///<span class="markdown">鼠标事件</span></span>
          <span class="hljs-keyword">if</span>(mouseY><span class="hljs-number">0</span>&&mouseX><span class="hljs-number">0</span>)&#123;
            <span class="hljs-built_in">double</span> dx=points[i].x-mouseX;
            <span class="hljs-built_in">double</span> dy=points[i].y-mouseY;
            <span class="hljs-built_in">double</span> distp=sqrt(dx*dx+dy*dy);
            <span class="hljs-comment">/// <span class="markdown">遇到鼠标吸附距离时加速，直接改变point的x，y值达到加速效果</span></span>
            <span class="hljs-keyword">if</span>(distp > dist && distp <= eDist)&#123;
              points[i].x = points[i].x + (mouseX - points[i].x) / <span class="hljs-number">20</span>;
              points[i].y = points[i].y + (mouseY - points[i].y) / <span class="hljs-number">20</span>;
            &#125;
            <span class="hljs-keyword">if</span>(distp <= eDist)&#123;
              _paintMouseLine.color=Color.fromRGBO(stroke.red, stroke.green, stroke.blue, <span class="hljs-number">1</span>-distp/eDist);
              canvas.drawLine(Offset(points[i].x, points[i].y), Offset(mouseX, mouseY), _paintMouseLine);
            &#125;
          &#125;
        &#125;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.鼠标事件</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement build</span>
    <span class="hljs-keyword">return</span> Container(
      child:  CustomPaint(
        child: MouseRegion(
          onEnter: (event)&#123;
            <span class="hljs-comment">//print("进入x:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(event.position.dx,event.position.dy);
          &#125;,
          onExit: (event)&#123;
            <span class="hljs-comment">//print("onExit:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(<span class="hljs-number">-1</span>,<span class="hljs-number">-1</span>);
          &#125;,
          onHover: (event)&#123;
            <span class="hljs-comment">// print("移动x:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(event.position.dx,event.position.dy);
          &#125;,
        ),
        painter: PaintLizi(
            <span class="hljs-keyword">this</span>.radius, <span class="hljs-keyword">this</span>.count, <span class="hljs-keyword">this</span>.color, <span class="hljs-keyword">this</span>.stroke,<span class="hljs-keyword">this</span>.maxConn,<span class="hljs-keyword">this</span>.dist,points,<span class="hljs-keyword">this</span>.mouseX,<span class="hljs-keyword">this</span>.mouseY,<span class="hljs-keyword">this</span>.eDist),
      ),
    );
  &#125;

  <span class="hljs-comment">///<span class="markdown">鼠标事件</span></span>
  <span class="hljs-keyword">void</span> _mouseEvent(<span class="hljs-built_in">double</span> x,<span class="hljs-built_in">double</span> y)&#123;
    setState(() &#123;
      mouseX=x;
      mouseY=y;
      Size size=MediaQuery.of(context).size;
      <span class="hljs-keyword">if</span>(mouseX>=size.width<span class="hljs-number">-10</span>||mouseX<=<span class="hljs-number">10</span>)&#123;
        mouseX=<span class="hljs-number">-1</span>;
      &#125;
      <span class="hljs-keyword">if</span>(mouseY>=size.height<span class="hljs-number">-10</span>||mouseY<=<span class="hljs-number">10</span>)&#123;
        mouseY=<span class="hljs-number">-1</span>;
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5.遇到的问题</h2>
<p>问题1：MouseRegion包裹CustomPaint，监听事件失效，如下</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">///<span class="markdown">监听事件失效</span></span>
<span class="hljs-keyword">return</span> MouseRegion(
      onEnter: (event)&#123;
        
      &#125;,
      child: CustomPaint(
        painter: PaintLizi(
            <span class="hljs-keyword">this</span>.radius, <span class="hljs-keyword">this</span>.count, <span class="hljs-keyword">this</span>.color, <span class="hljs-keyword">this</span>.stroke,<span class="hljs-keyword">this</span>.maxConn,<span class="hljs-keyword">this</span>.dist,points,<span class="hljs-keyword">this</span>.mouseX,<span class="hljs-keyword">this</span>.mouseY,<span class="hljs-keyword">this</span>.eDist),
          )
    );


<span class="hljs-comment">///<span class="markdown">正确方法 MouseRegion作为CustomPaint的child</span></span>
CustomPaint(
        child: MouseRegion(
          onEnter: (event)&#123;
            <span class="hljs-comment">//print("进入x:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(event.position.dx,event.position.dy);
          &#125;,
          onExit: (event)&#123;
            <span class="hljs-comment">//print("onExit:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(<span class="hljs-number">-1</span>,<span class="hljs-number">-1</span>);
          &#125;,
          onHover: (event)&#123;
            <span class="hljs-comment">// print("移动x:$&#123;event.position.dx&#125; y:$&#123;event.position.dy&#125;");</span>
            _mouseEvent(event.position.dx,event.position.dy);
          &#125;,
        ),
        painter: PaintLizi(
            <span class="hljs-keyword">this</span>.radius, <span class="hljs-keyword">this</span>.count, <span class="hljs-keyword">this</span>.color, <span class="hljs-keyword">this</span>.stroke,<span class="hljs-keyword">this</span>.maxConn,<span class="hljs-keyword">this</span>.dist,points,<span class="hljs-keyword">this</span>.mouseX,<span class="hljs-keyword">this</span>.mouseY,<span class="hljs-keyword">this</span>.eDist),
      ),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题2：onExit: (event)&#123;&#125;</p>
<p>鼠标移除事件在鼠标移到浏览器外并没有回调。</p></div>  
</div>
            