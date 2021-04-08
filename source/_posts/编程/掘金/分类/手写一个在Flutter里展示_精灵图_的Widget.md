
---
title: '手写一个在Flutter里展示_精灵图_的Widget'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc8a48987fe4b27bcb48c2ceeeca36e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 18:16:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc8a48987fe4b27bcb48c2ceeeca36e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>之前用Flutter里的游戏引擎Flare做了一个“是男人就坚持100秒”的游戏，<a href="https://juejin.cn/post/6939065092965629983" target="_blank">文章请看这里</a></p>
<blockquote>
<p>使用Flare引擎之后，完全没有了<code>Flutter</code>应用特有的代码风格。虽然更适应我这类有过游戏开发经验的开发者，但并不利于我们学习<code>Flutter</code>框架。所以我在那篇文章最后也说了，要抽空用Widget重写一次这个游戏。</p>
</blockquote>
<p>首要任务，就是得有一个支持”精灵图“的<code>Widget</code>，既然是学习，那就不能用别人开发好的，必须得自己亲手造轮子。</p>
<h1 data-id="heading-1">什么是”精灵图“</h1>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc8a48987fe4b27bcb48c2ceeeca36e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>精灵图的英文是<code>spritesheet</code>（精灵表单），就是在一张图上放置多个图形，只需要加载到内存里一次。在展示的时候，仅展示单个图形的区域。一般多个图形多用来放置连续动画的多个关键帧。除了在游戏引擎里很常见以外，为了减少web请求，在前端领域也很常见。</p>
<h1 data-id="heading-2">原理拆解</h1>
<h2 data-id="heading-3">加载一张大图，但每次只展示图片的特定区域</h2>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57c7bac632c4b7cabe5a20ab7c766d0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>比如这张飞机的精灵图，尺寸是330x82（像素），横向排布5个画面，那么单个画面的尺寸就是<code>330/5 = 66</code>。我们每次展示的区域为<code>x=66*画面序号，y=0，width=66，height=82</code>。</p>
<h2 data-id="heading-4">可以设定横向排布或纵向排布</h2>
<p>精灵图可以横向或纵向排布，有些游戏引擎的贴图最大尺寸为4096x4096，所以还有些情况是需要我们换行切换的，但原理差异并不大，这里就不过多讨论了。</p>
<h2 data-id="heading-5">可以设定播放时间间隔，自动切换多个连续区域</h2>
<p><img alt="2021-04-08 09_45_16.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69bc23ab182d4b8990b13f9a490da777~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>大部分时候我们是需要用精灵图来展示动画的，比如这个飞机的精灵图。其中第1，2幅画面用于展示飞机飞行状态的动画，需要循环播放。</p>
<p><img alt="2021-04-08 09_48_43.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f26d972cbb8f43d58f46be9dab02dc94~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>第3，4，5幅画面用于展示飞机爆炸的动画，只需播放一次。</p>
<h1 data-id="heading-6">思考应该用哪些Widget来搭建</h1>
<p>通过一个动画演示来看看我们需要哪些Widget</p>
<p><img alt="2021-04-08 10_00_37.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75cb3e0259e745db9f6ee2ebbe65ca53~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>可以控制显示区域的Widget（Container）</li>
<li>需要可以指定坐标的Widget（Stack+Positioned）</li>
</ul>
<p>原理也清楚了，也知道该用什么Widget，那么接下来的代码就很容易了</p>
<h1 data-id="heading-7">将思路转变为代码</h1>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-meta">@override</span>
Widget build(BuildContext context) &#123;
<span class="hljs-keyword">return</span> Container(
    width: <span class="hljs-number">66</span>,
    height: <span class="hljs-number">82</span>,
    child: Stack(
      children: [
        Positioned(
          left: <span class="hljs-number">66</span>*currentIndex,
          top: <span class="hljs-number">0</span>,
          child: widget.image
        )
      ],
    ),
);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加入定时器，根据设定的时间间隔改变<code>currentIndex</code>，那么图片看上去就动起来了。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Timer.periodic(widget.duration, (timer) &#123; 
    setState(() &#123;
      <span class="hljs-keyword">if</span>(currentIndex>=<span class="hljs-number">4</span>)&#123;
        currentIndex=<span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-keyword">else</span> currentIndex++;
    &#125;);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再进一步封装成一个自己原创的<code>Widget</code>，下面是这个Widget的全部代码</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'dart:async'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/widgets.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnimatedSpriteImage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;

  <span class="hljs-keyword">final</span> Image image;
  <span class="hljs-keyword">final</span> Size spriteSize;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> startIndex;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> endIndex;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> playTimes;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">Duration</span> duration;
  <span class="hljs-keyword">final</span> Axis axis;

  AnimatedSpriteImage(&#123;
    Key? key,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.image,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.spriteSize,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.duration,
    <span class="hljs-keyword">this</span>.axis = Axis.horizontal,
    <span class="hljs-keyword">this</span>.startIndex = <span class="hljs-number">0</span>,
    <span class="hljs-keyword">this</span>.endIndex = <span class="hljs-number">0</span>,
    <span class="hljs-keyword">this</span>.playTimes = <span class="hljs-number">0</span>,<span class="hljs-comment">//0 = loop</span>
  &#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  _AnimatedSpriteImageState createState() => _AnimatedSpriteImageState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_AnimatedSpriteImageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">AnimatedSpriteImage</span>> </span>&#123;

  <span class="hljs-built_in">int</span> currentIndex = <span class="hljs-number">0</span>;
  <span class="hljs-built_in">int</span> currentTimes = <span class="hljs-number">0</span>;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;

    currentIndex = widget.startIndex;

    Timer.periodic(widget.duration, (timer) &#123; 
      <span class="hljs-keyword">if</span>(currentTimes<=widget.playTimes)&#123;
        setState(() &#123;
          <span class="hljs-keyword">if</span>(currentIndex>=widget.endIndex)&#123;
            <span class="hljs-keyword">if</span>(widget.playTimes!=<span class="hljs-number">0</span>)currentTimes++;
            <span class="hljs-keyword">if</span>(currentTimes<widget.playTimes||widget.playTimes==<span class="hljs-number">0</span>)currentIndex=widget.startIndex;
            <span class="hljs-keyword">else</span> currentIndex = widget.endIndex;
          &#125;
          <span class="hljs-keyword">else</span> currentIndex++;
        &#125;);
      &#125;
    &#125;);

    <span class="hljs-keyword">super</span>.initState();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Container(
        width: widget.spriteSize.width,
        height: widget.spriteSize.height,
        
        child: Stack(
          children: [
            Positioned(
              left: widget.axis==Axis.horizontal?-widget.spriteSize.width*currentIndex:<span class="hljs-number">0</span>,
              top: widget.axis==Axis.vertical?-widget.spriteSize.height*currentIndex:<span class="hljs-number">0</span>,
              child: widget.image
            )
          ],
        ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>封装得好，使用起来也尤其方便。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//播放飞机飞行状态动画</span>
AnimatedSpriteImage(
  duration: <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">200</span>),<span class="hljs-comment">//动画的间隔</span>
  image: Image.asset(<span class="hljs-string">"assets/images/player.png"</span>),<span class="hljs-comment">//精灵图</span>
  spriteSize: Size(<span class="hljs-number">66</span>, <span class="hljs-number">82</span>),<span class="hljs-comment">//单画面尺寸</span>
  startIndex: <span class="hljs-number">0</span>,<span class="hljs-comment">//动画起始画面序号</span>
  endIndex: <span class="hljs-number">1</span>,<span class="hljs-comment">//动画结束画面序号</span>
  playTimes: <span class="hljs-number">0</span>,<span class="hljs-comment">//播放次数，0为循环播放</span>
)

<span class="hljs-comment">//播放飞机爆炸动画</span>
AnimatedSpriteImage(
  duration: <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">200</span>),<span class="hljs-comment">//动画的间隔</span>
  image: Image.asset(<span class="hljs-string">"assets/images/player.png"</span>),<span class="hljs-comment">//精灵图</span>
  spriteSize: Size(<span class="hljs-number">66</span>, <span class="hljs-number">82</span>),<span class="hljs-comment">//单画面尺寸</span>
  startIndex: <span class="hljs-number">2</span>,<span class="hljs-comment">//动画起始画面序号</span>
  endIndex: <span class="hljs-number">4</span>,<span class="hljs-comment">//动画结束画面序号</span>
  playTimes: <span class="hljs-number">1</span>,<span class="hljs-comment">//播放次数，0为循环播放</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">关注大帅</h1>
<p>一个热爱前端开发的老程序猿，只在三个平台分享内容</p>
<ul>
<li>掘金</li>
<li>B站：<a href="https://space.bilibili.com/422646817" target="_blank" rel="nofollow noopener noreferrer">大帅老猿</a></li>
<li>微信公众号：大帅老猿</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            