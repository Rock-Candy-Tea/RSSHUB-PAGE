
---
title: 'Flutter简单实现手写瀑布流 第二篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6171055a4d834782b2747e2a3dfe199b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 03:36:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6171055a4d834782b2747e2a3dfe199b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前篇<a href="https://juejin.cn/post/6968786815448776718/" target="_blank">Flutter简单实现手写瀑布流  Widget部分</a>请看这。
封面为加载好图片后，快速滑动的帧数图。</p>
<h2 data-id="heading-0">RenderObject的实现</h2>
<p>前篇的Widget中有个createRenderObject的方法，这个方法即创建布局的信息并绘制使用。通过查阅RenderSliverList的源码，发现其是通过继承<a href="https://api.flutter.dev/flutter/rendering/RenderSliverMultiBoxAdaptor-class.html" target="_blank" rel="nofollow noopener noreferrer">RenderSliverMultiBoxAdaptor</a>类实现的布局，并重写了performLayout方法。该方法即为设置每个元素该放置的位置。</p>
<p>通过查阅源码，我们得知该类是抽象类，有3个mixin。</p>
<p>重要成员以及方法如下</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-comment">//本质是个管理布局中大量卡片的Element</span>
  <span class="hljs-keyword">final</span> RenderSliverBoxChildManager _childManager;
  
  <span class="hljs-comment">//设置每张卡片的布局信息，比如相对于滑动起点的偏移量</span>
  <span class="hljs-keyword">void</span> setupParentData(RenderObject child);
  
  <span class="hljs-comment">//初始化布局使用，稍后会谈及</span>
  <span class="hljs-built_in">bool</span> addInitialChild(&#123; <span class="hljs-built_in">int</span> index = <span class="hljs-number">0</span>, <span class="hljs-built_in">double</span> layoutOffset = <span class="hljs-number">0.0</span> &#125;) ;
  
  <span class="hljs-comment">//给定RenderBox的下标，即是第几张卡片</span>
  <span class="hljs-built_in">int</span> indexOf(RenderBox child);
  
  <span class="hljs-comment">//返回卡片的绘制高度</span>
  <span class="hljs-built_in">double</span> paintExtentOf(RenderBox child) ;
   
  <span class="hljs-comment">//返回给定卡片相对于滑动起点的偏移量</span>
  <span class="hljs-built_in">double?</span> childScrollOffset(RenderObject child);
   
  <span class="hljs-comment">//调用，绘制输出到屏幕上</span>
  <span class="hljs-keyword">void</span> paint(PaintingContext context, Offset offset);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">坑点提示(可以先跳过)</h3>
<p>1.RenderBox的layout方法的形参中，parentUsesSize属性一定要设置成true，不然父级元素无法访问其大小信息。</p>
<p>2.使用<a href="https://api.flutter.dev/flutter/widgets/SliverMultiBoxAdaptorElement/createChild.html" target="_blank" rel="nofollow noopener noreferrer">childManager.creatChild</a>创建新的卡片或者使用移除旧的卡片<a href="https://api.flutter.dev/flutter/widgets/SliverMultiBoxAdaptorElement/removeChild.html" target="_blank" rel="nofollow noopener noreferrer">childManager.removeChild</a>方法的时候，记得将其写在 <a href="https://api.flutter.dev/flutter/rendering/RenderObject/invokeLayoutCallback.html" target="_blank" rel="nofollow noopener noreferrer">invokeLayoutCallback((SliverConstraints constraints)&#123;&#125;)</a> 里边，来告知RenderObject要改变RenderTree，否则会出现红色报错页面，该调用在RenderObject的源码中有写到原因。</p>
<h2 data-id="heading-2">实现过程</h2>
<h3 data-id="heading-3">gridDelegate的实现</h3>
<p>首先，我们必须要有一个用于设置副轴上的应当放置几张卡片的类，这里我模仿了SliverGrid对应的<a href="https://api.flutter.dev/flutter/rendering/SliverGridDelegateWithFixedCrossAxisCount-class.html" target="_blank" rel="nofollow noopener noreferrer">SliverGridDelegateWithFixedCrossAxisCount</a>实现。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlowSliverDelegateWithFixedCrossAxisCount</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">FlowSliverDelegate</span> </span>&#123;
    <span class="hljs-keyword">const</span> FlowSliverDelegateWithFixedCrossAxisCount(&#123;
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.crossItemCount,
  &#125;);

  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> crossItemCount;   <span class="hljs-comment">//设置副轴能放几张卡片</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">ParentData的实现</h3>
<p>接着，我们的每张卡片应该有一个相对于主轴的偏移量，即记录在第几列的信息，供布局使用，这里继承了<a href="https://api.flutter.dev/flutter/rendering/SliverMultiBoxAdaptorParentData-class.html" target="_blank" rel="nofollow noopener noreferrer">SliverMultiBoxAdaptorParentData</a>，父类提供了index，keepAlive变量信息。<code>ParentData是RenderBox的一个属性，当坑点1中的属性为true时，父级才可以访问其信息！</code></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FlowSliverParentData</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SliverMultiBoxAdaptorParentData</span> </span>&#123;
  <span class="hljs-comment">//主轴偏移量  可以认为是距离手机屏幕左边几个像素</span>
  <span class="hljs-built_in">double</span> crossAxisPosition = <span class="hljs-number">0.0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">paint方法的重写</h3>
<p>paint是运行时最后被调用的，但我把它放在此处是因为内容不多。下面给出该方法里面的几个重要常量，其他的照葫芦画瓢即可。<code>注意，正真的绘制部分，是以屏幕为坐标系，左上角为零点。下面参数是描述绘制对象在该坐标轴的信息！</code></p>
<pre><code class="hljs language-dart copyable" lang="dart"> <span class="hljs-comment">//这里的child是RenderBox</span>
 
 <span class="hljs-comment">//应该绘制在离屏幕顶部多少像素</span>
 <span class="hljs-keyword">final</span> <span class="hljs-built_in">double</span> mainAxisDelta = childMainAxisPosition(child);
 
 <span class="hljs-comment">//应该绘制在离屏幕左边多少像素</span>
 <span class="hljs-keyword">final</span> <span class="hljs-built_in">double</span> crossAxisDelta = (child.parentData <span class="hljs-keyword">as</span> FlowSliverParentData).crossAxisPosition;
 
 <span class="hljs-comment">//好的，我开始画了</span>
 context.paintChild(child, childOffset);

 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">performLayout的重写。</h3>
<p><code>核心部分,也是最麻烦的部分</code></p>
<p>这个方法是对每张卡片对应的<code>RenderBox</code>的<code>parentData</code>进行参数设置，主要是设置parentData中<code>layoutOffset(相对滑动起点的偏移量)</code>,<code>crossAxisPosition(相对屏幕左边的偏移量)</code>，使其在待会<code>paint()</code>方法有正确的位置信息。</p>
<p>在这里，我们必须要做三件事。</p>
<p>1.使用父元素(viewPort)给的constraints信息进行布局设置。(不知道是啥的去翻翻第一篇文章的基础知识链接)</p>
<p>2.对出现在视窗范围内的RenderBox进行<code>layout()</code>调用，并且设置其parentData,使其有正确的位置信息。</p>
<p>3.输出布局信息给geometry变量。(不知道是啥的同上，这里是<code>SliverGeometry</code>)</p>
<p>布局算法会在<a href="https://juejin.cn/post/6968787097515884557">下篇</a>文章讲出，同时给出源码(太差劲了，得改改，暂时没写)。</p>
<h4 data-id="heading-7">用于performLayout的方法</h4>
<p>1.创建和销毁元素使用<a href="https://api.flutter.dev/flutter/widgets/SliverMultiBoxAdaptorElement-class.html" target="_blank" rel="nofollow noopener noreferrer">childManager</a>的提供的remove和create方法,注意坑点。</p>
<p>2.参照SliverList中使用childManager带有的输出geometry信息的<code>estimateMaxScrollOffset</code>,<code>calculatePaintOffset</code>,<code>calculateCacheOffset</code>三个方法。</p>
<h2 data-id="heading-8">来张最后效果图吧。</h2>
<p>评论和阅读多的话，我尽快写好下一篇文章。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6171055a4d834782b2747e2a3dfe199b~tplv-k3u1fbpfcp-watermark.image" alt="flow.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            