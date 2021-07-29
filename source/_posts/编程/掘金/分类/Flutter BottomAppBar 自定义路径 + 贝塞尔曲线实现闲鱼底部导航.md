
---
title: 'Flutter BottomAppBar 自定义路径 + 贝塞尔曲线实现闲鱼底部导航'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab66307a9e49f19a0232d4d6eb8a22~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 07:26:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab66307a9e49f19a0232d4d6eb8a22~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>网上已经有不少文章展示如何使用 <code>CircularNotchedRectangle</code> 或 <code>AutomaticNotchedShape</code> 实现带凹陷效果的 BottomAppBar，但是都没有提到如何自定义 NotchedShape 实现任意形状的 BottomAppBar，本文以闲鱼底部导航为例展示如何自定义 NotchedShape。</p>
<p>首先假设你已经知道如何使用 <code>CircularNotchedRectangle</code> 创建凹陷效果，我们主要做的就是写一个新的 class 继承 <code>NotchedShape</code> 来实现我们想要的效果。</p>
<p>在开始写 <code>NotchedShape</code> 之前我们先准备好一个正常的 BottomAppBar，因为不是重点，具体的实现就不展开说了，看起来像是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab66307a9e49f19a0232d4d6eb8a22~tplv-k3u1fbpfcp-zoom-1.image" alt="Screenshot_20210728-172230" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>唯一值得一提的是，中间的按钮是一个正常的 <code>FloatingActionButton</code>，为了让它比原来大并能超出 BottomAppBar 而使用了 <code>Transform.scale</code>。</em></p>
<p>接下来，我们创建新的 class <code>CustomNotchedShape</code> 继承 <code>NotchedShape</code> 并 override <code>getOuterPath</code>：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomNotchedShape</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">NotchedShape</span> </span>&#123;
  <span class="hljs-keyword">final</span> BuildContext context;
  <span class="hljs-keyword">const</span> CustomNotchedShape(<span class="hljs-keyword">this</span>.context);

  <span class="hljs-meta">@override</span>
  Path getOuterPath(Rect host, Rect? guest) &#123;
    <span class="hljs-keyword">return</span> Path();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>NotchedShape</code> 和 <code>CustomClipper<Path></code> 很像，都是通过创建一个 path 来定义我们想要的形状，如果你有 <code>CustomClipper<Path></code> 的经验，那 <code>NotchedShape</code> 也就差不多了。唯一不一样的是 <code>Path getOuterPath(Rect host, Rect? guest)</code> 有两个参数，<code>host</code> 在这里就是 BottomAppBar 本身的矩形边界，<code>guest</code> 则是嵌入 BottomAppBar 的矩形边界。由于我们并不需要嵌入 guest，第二个参数可以忽略掉。</p>
<p>我们可以先简单写一个梯形 path 来验证。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Path getOuterPath(Rect host, Rect? guest) &#123;
  <span class="hljs-keyword">return</span> Path()
    ..moveTo(host.left + <span class="hljs-number">20</span>, host.top)
    ..lineTo(host.right - <span class="hljs-number">20</span>, host.top)
    ..lineTo(host.right, host.bottom)
    ..lineTo(host.left, host.bottom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f831d81f1fcc481b9d15baa166ed024e~tplv-k3u1fbpfcp-zoom-1.image" alt="Screenshot_20210728-180335" loading="lazy" referrerpolicy="no-referrer"></p>
<p>知道怎么使用 path 创建自定义形状之后就可以思考如何实现闲鱼底部导航的效果了，经过观察，这样的效果可以由圆弧或贝塞尔曲线组合而成，使用贝塞尔曲线可能是最简单的，而且只需要一个控制点的贝塞尔曲线。</p>
<p>我们可以先画轮廓直线，然后再换成单个控制点的贝塞尔曲线即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1f8f83887704efa884c4f40246ed0b0~tplv-k3u1fbpfcp-zoom-1.image" alt="Screenshot_20210728-174420" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart">Path getOuterPath(Rect host, Rect? guest) &#123;
  <span class="hljs-keyword">const</span> radius = <span class="hljs-number">40.0</span>;
  <span class="hljs-keyword">const</span> lx = <span class="hljs-number">20.0</span>;
  <span class="hljs-keyword">const</span> ly = <span class="hljs-number">8</span>;
  <span class="hljs-keyword">var</span> x = (MediaQuery.of(context).size.width - radius) / <span class="hljs-number">2</span> - lx;
  <span class="hljs-keyword">return</span> Path()
    ..moveTo(host.left, host.top)
    ..lineTo(x, host.top)
    ..lineTo(x += lx, host.top - ly)
    ..lineTo(x += radius, host.top - ly)
    ..lineTo(x += lx, host.top)
    ..lineTo(host.right, host.top)
    ..lineTo(host.right, host.bottom)
    ..lineTo(host.left, host.bottom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lx 和 ly 是旁边两条斜线的 x、y，radius 是顶部横线的长度。</p>
<p>然后我们替换成贝塞尔曲线以及选择合适的控制点，再引入两个变量 bx、by 作为控制点的 x、y 偏移量，所有参数调整到合适到值之后即可实现最终效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96d4b3a5780140379f159b62735ba494~tplv-k3u1fbpfcp-zoom-1.image" alt="Screenshot_20210728-164125" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart">Path getOuterPath(Rect host, Rect? guest) &#123;
  <span class="hljs-keyword">const</span> radius = <span class="hljs-number">40.0</span>;
  <span class="hljs-keyword">const</span> lx = <span class="hljs-number">20.0</span>;
  <span class="hljs-keyword">const</span> ly = <span class="hljs-number">8</span>;
  <span class="hljs-keyword">const</span> bx = <span class="hljs-number">10.0</span>;
  <span class="hljs-keyword">const</span> by = <span class="hljs-number">20.0</span>;
  <span class="hljs-keyword">var</span> x = (MediaQuery.of(context).size.width - radius) / <span class="hljs-number">2</span> - lx;
  <span class="hljs-keyword">return</span> Path()
    ..moveTo(host.left, host.top)
    ..lineTo(x, host.top)
    ..quadraticBezierTo(x + bx, host.top, x += lx, host.top - ly)
    ..quadraticBezierTo(
        x + radius / <span class="hljs-number">2</span>, host.top - by, x += radius, host.top - ly)
    ..quadraticBezierTo((x += lx) - bx, host.top, x, host.top)
    ..lineTo(host.right, host.top)
    ..lineTo(host.right, host.bottom)
    ..lineTo(host.left, host.bottom);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqiuxiang%2Fcustom_notched_shape" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qiuxiang/custom_notched_shape" ref="nofollow noopener noreferrer">github.com/qiuxiang/cu…</a></p>
<p>DartPad 在线演示：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdartpad.dev%2F%3Fnull_safety%3Dtrue%26id%3Da976bbb3961a8c5f5998a54c8d2ed7aa" target="_blank" rel="nofollow noopener noreferrer" title="https://dartpad.dev/?null_safety=true&id=a976bbb3961a8c5f5998a54c8d2ed7aa" ref="nofollow noopener noreferrer">dartpad.dev/?null_safet…</a></p></div>  
</div>
            