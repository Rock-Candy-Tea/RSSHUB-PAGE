
---
title: '使用Flutter Widget开发游戏_是男人就坚持100秒_，一套代码横跨6端~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b941c3d9142d45fe92f1e6f7b9000bfe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 01:08:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b941c3d9142d45fe92f1e6f7b9000bfe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>之前使用Flutter里的游戏引擎Flare已经开发了一版这个游戏，原文地址：<a href="https://juejin.cn/post/6939065092965629983" target="_blank">juejin.cn/post/693906…</a> 。在文章里我说要用Widget再来做一次。现在兑现我的承诺，并且上周日在B站直播了整个开发过程</p>
<p><a href="https://www.bilibili.com/video/BV1JK411F7wi/" target="_blank" rel="nofollow noopener noreferrer">📺点击查看直播视频</a></p>
<h1 data-id="heading-1">在Flutter里展示Sprite动画</h1>
<p>请看这篇文章<a href="https://juejin.cn/post/6948604732822781966" target="_blank">《手写一个在Flutter里展示”精灵图“的Widget》</a></p>
<h1 data-id="heading-2">飞机的移动</h1>
<p>首先将飞机放置在画面正中，由于Widget的原点统一为左上角，所以要减去飞机图像宽和高的一半。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">//获得画布的宽高</span>
Size screenSize = <span class="hljs-built_in">window</span>.physicalSize/<span class="hljs-built_in">window</span>.devicePixelRatio;

<span class="hljs-comment">//将飞机的x,y坐标设定为画面中心</span>
playerLeft = screenSize.width/<span class="hljs-number">2</span><span class="hljs-number">-66</span>/<span class="hljs-number">2</span>;
playerTop = screenSize.height/<span class="hljs-number">2</span><span class="hljs-number">-82</span>/<span class="hljs-number">2</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>飞机我们需要捕获到用户的手势事件，使用GestureDetector这个Widget来拖动飞机。</p>
<pre><code class="hljs language-dart copyable" lang="dart">GestureDetector( 
  onPanUpdate: (DragUpdateDetails details) &#123;
    setState(() &#123;
      playerLeft += details.delta.dx;
      playerTop += details.delta.dy;
    &#125;);
  &#125;,
  child:<span class="hljs-comment">//飞机的Widget</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-04-12 16_29_13.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b941c3d9142d45fe92f1e6f7b9000bfe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">设定FPS</h1>
<p>由于没有使用游戏引擎，所以只好自己通过定时器来实现。比如我们要实现60FPS的刷新率，可以将定时器设置为17毫秒，这样的话刷新率约等于59fps。当然可以更精确一些，但没有那个必要。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Timer.periodic(<span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">17</span>), (timer) &#123;
  gameloop();
&#125;);

gameloop()&#123;
    setState(() &#123;
        <span class="hljs-comment">//触发build方法</span>
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过我这里建议设置为每<code>20</code>毫秒刷新一次，原因在后面会讲。</p>
<h1 data-id="heading-4">添加子弹</h1>
<p>我们建立一个子弹管理数组，将所有子弹的数据都放在数组中</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-built_in">List</span> bulletsData = [];

addBullet()&#123;
    <span class="hljs-built_in">double</span> bulletX;
    <span class="hljs-built_in">double</span> bulletY;

    <span class="hljs-keyword">if</span> (Random().nextBool()) &#123;
      bulletX = Random().nextDouble() * (screenSize.width + bulletSize.width) -
          bulletSize.width;
      bulletY = Random().nextBool() ? -bulletSize.height : screenSize.height;
    &#125; <span class="hljs-keyword">else</span> &#123;
      bulletX = Random().nextBool() ? -bulletSize.width : screenSize.width;
      bulletY = Random().nextDouble() * (screenSize.height + bulletSize.height) -
          bulletSize.height;
    &#125;

    bulletsData.add(&#123;
      <span class="hljs-string">"x"</span>:bulletX,
      <span class="hljs-string">"y"</span>:bulletY,
      <span class="hljs-string">"speed"</span>: (<span class="hljs-number">1</span>+gameTime/<span class="hljs-number">10</span>) + Random().nextDouble()*<span class="hljs-number">3</span>,
      <span class="hljs-string">"angle"</span>: atan2(((bulletY + bulletSize.height/<span class="hljs-number">2</span>) - (playerTop + playerHeight / <span class="hljs-number">2</span>)),
          ((bulletX + bulletSize.width) - (playerLeft + playerWidth / <span class="hljs-number">2</span>)))
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">子弹移动</h2>
<p>在<code>gameloop</code>中遍历数组对子弹进行移动。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = bulletsData.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
      <span class="hljs-keyword">var</span> bulletItem = bulletsData[i];

      <span class="hljs-built_in">double</span> angle = bulletItem[<span class="hljs-string">"angle"</span>];
      <span class="hljs-built_in">double</span> speed = bulletItem[<span class="hljs-string">"speed"</span>];

      bulletItem[<span class="hljs-string">"x"</span>] -= cos(angle) * speed;
      bulletItem[<span class="hljs-string">"y"</span>] -= sin(angle) * speed;

      <span class="hljs-keyword">if</span> (isHitPlayer(bulletItem[<span class="hljs-string">"x"</span>], bulletItem[<span class="hljs-string">"y"</span>])) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"gameOver"</span>);
        gameOver();
      &#125;

      <span class="hljs-keyword">if</span> (isNotInScreen(bulletItem[<span class="hljs-string">"x"</span>], bulletItem[<span class="hljs-string">"y"</span>])) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"bullet removed"</span>);
        bulletsData.removeAt(i);
        <span class="hljs-keyword">continue</span>;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">子弹展示</h2>
<p>上述代码完成后，我们的子弹在数据中就存在了。但是你看不见它们，因为他们没有被绘制到画面中。我们需要利用<code>Stack</code>和<code>Positioned</code>控件来展示它们。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Stack(
  children: getBulletsWidget(),
)

getBulletsWidget()&#123;
    <span class="hljs-built_in">List</span><Positioned> bullets = [];

    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>;i<bulletsData.length;i++)&#123;
      <span class="hljs-keyword">var</span> bulletItem = bulletsData[i];
      <span class="hljs-comment">// print(bulletItem);</span>
      <span class="hljs-keyword">var</span> bulletWidget = Positioned(
        left: bulletItem[<span class="hljs-string">"x"</span>],
        top: bulletItem[<span class="hljs-string">"y"</span>],
        child: bulletImage
      );

      bullets.add(bulletWidget);
    &#125;

    <span class="hljs-keyword">return</span> bullets;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-04-12 16_42_24.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f19a9bf4e364feba8eccc62e7846a2a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">按秒计时</h1>
<p>既然游戏标题叫“是男人就坚持100秒”，那游戏中肯定需要一个按秒的计时器。还记得前面为什么我建议将计时器的刷新频率设置为20毫秒吗？这样的话，我们每刷新50次是不是就是1秒钟呢？</p>
<pre><code class="hljs language-dart copyable" lang="dart">Timer.periodic(<span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">20</span>), (timer) &#123;
  <span class="hljs-keyword">if</span>(timer.tick%<span class="hljs-number">50</span>==<span class="hljs-number">0</span>)&#123;
    gameSeconds+=<span class="hljs-number">1</span>;
    <span class="hljs-comment">//seconds</span>
  &#125;

  loop();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Flutter里我们可以这样做，<code>timer</code>里的<code>tick</code>是一个计时器的执行计数，会不断累计，所以我们只需要对50取余，每次整除50的时候就是1秒钟啦~</p>
<h1 data-id="heading-8">跨端</h1>
<p>借助Flutter强大的跨端能力，这个游戏我们可以...</p>
<h2 data-id="heading-9">运行在Mac桌面</h2>
<pre><code class="hljs language-dart copyable" lang="dart">flutter run -d macOS
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-04-12 11_45_01.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce11d5dd7c040dd97ebe22012b32843~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">运行在浏览器</h2>
<pre><code class="hljs language-dart copyable" lang="dart">flutter run -d Chrome
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-04-12 16_54_04.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08328e8bcd46448d863f71c9dfc942d9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">运行在iOS</h2>
<pre><code class="hljs language-dart copyable" lang="dart">flutter run -d 模拟器ID
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2021-04-12 17_05_27.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a37bd4a6b024af4811089124cdaf821~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>还有Linux，Windows，Android我就不一一给大家截图了</p>
<p>项目已开源，请自行运行吧！</p>
<h1 data-id="heading-12">源码仓库</h1>
<p><a href="https://github.com/ezshine/fluttergame-keepalive100s" target="_blank" rel="nofollow noopener noreferrer">github.com/ezshine/flu…</a></p>
<h1 data-id="heading-13">关注大帅吧</h1>
<p>来一波赞和关注可好？</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            