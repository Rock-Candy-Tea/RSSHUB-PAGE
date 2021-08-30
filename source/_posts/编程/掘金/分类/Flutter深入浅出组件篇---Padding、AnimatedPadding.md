
---
title: 'Flutter深入浅出组件篇---Padding、AnimatedPadding'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19cda29c68124a549cd040e48385d58f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 20:05:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19cda29c68124a549cd040e48385d58f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Padding介绍</h2>
<p>​在应用程序中有许多<code>widget</code> 时，这个时候画面常常会变得很拥挤，这个时候如果想要在widget之间来保留一些间距，那就用 <code>Padding</code></p>
<h4 data-id="heading-1">为什么使用 <code>Padding</code> 而不使用 <code>Container.padding</code> 属性的 <code>Container</code>?</h4>
<p>​<code>Container</code> 是将许多更简单的 <code>widget</code> 组合在一个方便的包中，如果只需要设置 <code>padding</code> ，那我们最好使用 <code>Padding</code> 而不是 <code>Container</code></p>
<h2 data-id="heading-2">示例代码</h2>
<p>本文中很多效果都没有截图，可下载源代码运行项目 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJunAILiang%2Fflutter_code" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JunAILiang/flutter_code" ref="nofollow noopener noreferrer">源代码地址</a>，或者通过视频教程查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1BM4y1L71Z%3Fp%3D6" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1BM4y1L71Z?p=6" ref="nofollow noopener noreferrer">视频教程地址</a></p>
<h2 data-id="heading-3">Padding属性和说明</h2>
<blockquote>
<p>总共2个属性</p>
</blockquote>




















<table><thead><tr><th>字段</th><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>padding</td><td>EdgeInsetsGeometry</td><td>给子widget的间距</td></tr><tr><td>child</td><td>Widget</td><td>子widget</td></tr></tbody></table>
<h2 data-id="heading-4">Padding属性详细使用</h2>
<h3 data-id="heading-5">1、padding 、child</h3>
<p>​<code>padding</code> 给子<code>widget</code>的间距</p>
<p>​<code>child</code> 接收一个子 <code>Widget</code></p>
<h4 data-id="heading-6">完整代码</h4>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PaddingExample</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _PaddingExampleState createState() => _PaddingExampleState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_PaddingExampleState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">PaddingExample</span>> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"Padding example"</span>),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Padding(
              padding: EdgeInsets.all(<span class="hljs-number">0</span>),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.red,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(<span class="hljs-number">0</span>),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.green,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(<span class="hljs-number">0</span>),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.orange,
              ),
            )
          ],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">EdgeInsetsGeometry详解</h2>
<p>​<code>EdgeInsetsGeometry</code> 是一个描述边距的组件，一般都是使用它的子类 <code>EdgeInsets</code> 来进行设置。</p>
<h3 data-id="heading-8">1、fromLTRB</h3>
<p>​设置左、上、右、下的边距，可设定不同的值。</p>
<h3 data-id="heading-9">使用方法</h3>
<pre><code class="hljs language-dart copyable" lang="dart">Padding(
  padding: EdgeInsets.fromLTRB(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>, <span class="hljs-number">40</span>),
  child: Container(
    width: <span class="hljs-number">100</span>,
    height: <span class="hljs-number">100</span>,
    color: Colors.red,
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2、all</h3>
<p>​同时设置所有的边距为同一个值</p>
<h4 data-id="heading-11">使用方法</h4>
<pre><code class="hljs language-dart copyable" lang="dart">Padding(
  padding: EdgeInsets.all(<span class="hljs-number">10</span>),
  child: Container(
    width: <span class="hljs-number">100</span>,
    height: <span class="hljs-number">100</span>,
    color: Colors.green,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3、only</h3>
<p>​根据需要设置某一个边的间距</p>
<h4 data-id="heading-13">使用方法</h4>
<pre><code class="hljs language-dart copyable" lang="dart">Padding(
  padding: EdgeInsets.only(
    left: <span class="hljs-number">10</span>,
    right: <span class="hljs-number">10</span>
  ),
  child: Container(
    width: <span class="hljs-number">100</span>,
    height: <span class="hljs-number">100</span>,
    color: Colors.orange,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4、symmetric</h3>
<p>​设置水平（上下）、或者垂直（左右）的间距</p>
<h4 data-id="heading-15">使用方法</h4>
<pre><code class="hljs language-dart copyable" lang="dart">Padding(
  padding: EdgeInsets.symmetric(
    vertical: <span class="hljs-number">10</span>,
    horizontal: <span class="hljs-number">10</span>
  ),
  child: Container(
    width: <span class="hljs-number">100</span>,
    height: <span class="hljs-number">100</span>,
    color: Colors.orange,
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">完整代码</h3>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PaddingExample</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _PaddingExampleState createState() => _PaddingExampleState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_PaddingExampleState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">PaddingExample</span>> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"Padding example"</span>),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Padding(
              padding: EdgeInsets.fromLTRB(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>, <span class="hljs-number">40</span>),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.red,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(<span class="hljs-number">10</span>),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.green,
              ),
            ),
            Padding(
              padding: EdgeInsets.only(
                left: <span class="hljs-number">10</span>,
                right: <span class="hljs-number">10</span>
              ),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.orange,
              ),
            ),
            Padding(
              padding: EdgeInsets.symmetric(
                vertical: <span class="hljs-number">10</span>,
                horizontal: <span class="hljs-number">10</span>
              ),
              child: Container(
                width: <span class="hljs-number">100</span>,
                height: <span class="hljs-number">100</span>,
                color: Colors.orange,
              ),
            )
          ],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">AnimatedPadding介绍</h2>
<pre><code class="copyable">`Padding` 组件的动画版本，在设置的时间内缩放或放大到指定的padding
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">AnimatedPadding构造函数</h2>
<pre><code class="hljs language-dart copyable" lang="dart">  AnimatedPadding(&#123;
    Key? key,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.padding, <span class="hljs-comment">// 边距</span>
    <span class="hljs-keyword">this</span>.child,  <span class="hljs-comment">// 子Widget</span>
    Curve curve = Curves.linear,  <span class="hljs-comment">// 动画的运动速率</span>
    <span class="hljs-keyword">required</span> <span class="hljs-built_in">Duration</span> duration,  <span class="hljs-comment">// 动画的持续时间</span>
    VoidCallback? onEnd,   <span class="hljs-comment">// 动画结束时的回调</span>
  &#125;) : <span class="hljs-keyword">assert</span>(padding != <span class="hljs-keyword">null</span>),
       <span class="hljs-keyword">assert</span>(padding.isNonNegative),
       <span class="hljs-keyword">super</span>(key: key, curve: curve, duration: duration, onEnd: onEnd);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">AnimatedPadding完整示例代码</h2>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnimatedPaddingExample</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  _AnimatedPaddingExampleState createState() => _AnimatedPaddingExampleState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_AnimatedPaddingExampleState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">AnimatedPaddingExample</span>> </span>&#123;
  <span class="hljs-built_in">double</span> paddingAllValue = <span class="hljs-number">0.0</span>;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"AnimatedPaddingExample"</span>),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(<span class="hljs-string">'Padding: <span class="hljs-subst">$paddingAllValue</span>'</span>),
          AnimatedPadding(
            padding: EdgeInsets.all(paddingAllValue),
            duration: <span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">1000</span>),
            curve: Curves.easeInOut,
            child: Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height / <span class="hljs-number">4</span>,
              color: Colors.blue,
            ),
            onEnd: () &#123;
              <span class="hljs-built_in">print</span>(<span class="hljs-string">"动画结束时的回调"</span>);
            &#125;,
          ),
          ElevatedButton(
            child: Text(<span class="hljs-string">'改变padding的值'</span>),
            onPressed: () &#123;
              setState(() &#123;
                paddingAllValue = paddingAllValue == <span class="hljs-number">0.0</span> ? <span class="hljs-number">50.0</span> : <span class="hljs-number">0.0</span>;
              &#125;);
            &#125;),
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">AnimatedPadding效果展示</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19cda29c68124a549cd040e48385d58f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">总结</h2>
<p>​当只需要给组件之间增加一些间距时，使用<code>Padding</code> 是最好的选择。而如果的<code>Padding</code>在某种情况下需要改变其大小并且需要增加动画效果时，使用<code>AnimatedPadding</code> 最佳，而不需要花费大量时间去写动画。</p></div>  
</div>
            