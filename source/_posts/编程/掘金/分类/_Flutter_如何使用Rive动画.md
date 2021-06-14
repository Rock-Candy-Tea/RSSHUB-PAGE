
---
title: '_Flutter_如何使用Rive动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78f9d94677204c429c6f03ec789cceaa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 20:25:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78f9d94677204c429c6f03ec789cceaa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Rive2动画效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78f9d94677204c429c6f03ec789cceaa~tplv-k3u1fbpfcp-watermark.image" alt="ezgif-4-3e0e6218bced.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>预览网站:<a href="https://rive-nav.liugl.cn/" target="_blank" rel="nofollow noopener noreferrer">rive-nav.liugl.cn/</a></p>
<h3 data-id="heading-1">开始使用</h3>
<p>Rive2文件的后缀为<code>.riv</code>，将文件拖到<a href="https://rive.app/preview/" target="_blank" rel="nofollow noopener noreferrer">Rive预览工具</a>可以查看文件内提供的动画和状态</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05dddae5c82e4c52bdab37bcbc7edc2b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">有了<code>动画列表</code>就可以开始准备使用了</h4>
<p>添加依赖<br>
<code>rive: ^0.7.17</code></p>
<p>将<code>.riv</code>文件放到指定目录并引用</p>
<pre><code class="hljs language-dart copyable" lang="dart">assets:
    - riv_files/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入依赖<br>
<code>import 'package:rive/rive.dart';</code></p>
<p>这里我们制作的是一个简单的动画图标，所以只有两个动画：<code>idle</code>、<code>active</code></p>
<h4 data-id="heading-3">针对该图标的属性进行简单的封装：</h4>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/services.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:rive/rive.dart'</span>;

<span class="hljs-comment">///<span class="markdown">rive图标封装</span></span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RiveIcon</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> RiveIcon(&#123;
    Key? key,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.isSelected,
    <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.rivPath,
    <span class="hljs-keyword">this</span>.idle = <span class="hljs-string">'idle'</span>,
    <span class="hljs-keyword">this</span>.active = <span class="hljs-string">'active'</span>,
  &#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-comment">///<span class="markdown">是否选中</span></span>
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">bool</span> isSelected;

  <span class="hljs-comment">///<span class="markdown">文件路径</span></span>
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> rivPath;

  <span class="hljs-comment">///<span class="markdown">闲置状态</span></span>
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> idle;

  <span class="hljs-comment">///<span class="markdown">激活状态</span></span>
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> active;

  <span class="hljs-meta">@override</span>
  _RiveIconState createState() => _RiveIconState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_RiveIconState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">RiveIcon</span>> </span>&#123;
  <span class="hljs-comment">///<span class="markdown">画布</span></span>
  Artboard? _riveArtboard;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    _init();
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> setState(VoidCallback fn) &#123;
    <span class="hljs-keyword">if</span> (mounted) <span class="hljs-keyword">super</span>.setState(fn);
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> didUpdateWidget(<span class="hljs-keyword">covariant</span> RiveIcon oldWidget) &#123;
    <span class="hljs-keyword">if</span> (oldWidget.isSelected != widget.isSelected) &#123;
      widget.isSelected ? _select() : _unSelect();
    &#125;

    <span class="hljs-keyword">super</span>.didUpdateWidget(oldWidget);
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    _riveArtboard?.remove();
    <span class="hljs-keyword">super</span>.dispose();
  &#125;

  <span class="hljs-comment">///<span class="markdown">选中</span></span>
  <span class="hljs-keyword">void</span> _select() &#123;
    _riveArtboard?.removeController(SimpleAnimation(widget.idle));
    _riveArtboard?.addController(SimpleAnimation(widget.active));
  &#125;

  <span class="hljs-comment">///<span class="markdown">未选中</span></span>
  <span class="hljs-keyword">void</span> _unSelect() &#123;
    _riveArtboard?.removeController(SimpleAnimation(widget.active));
    _riveArtboard?.addController(SimpleAnimation(widget.idle));
  &#125;

  <span class="hljs-comment">///<span class="markdown">初始化</span></span>
  Future<<span class="hljs-keyword">void</span>> _init() <span class="hljs-keyword">async</span> &#123;
    _riveArtboard =
        RiveFile.<span class="hljs-keyword">import</span>(<span class="hljs-keyword">await</span> rootBundle.load(widget.rivPath)).mainArtboard;

    setState(() &#123;&#125;);

    widget.isSelected ? _select() : _unSelect();
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> _riveArtboard == <span class="hljs-keyword">null</span>
        ? <span class="hljs-keyword">const</span> SizedBox.shrink()
        : Rive(artboard: _riveArtboard!);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做封装是为了更好地控制动画的状态，<code>非循环</code>的rive动画在被添加时<code>只会播放一次</code>，想重新从头开始播放需要<code>移除该动画并重新添加</code>：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">///<span class="markdown">选中</span></span>
<span class="hljs-keyword">void</span> _select() &#123;
    _riveArtboard?.removeController(SimpleAnimation(widget.idle));
    _riveArtboard?.addController(SimpleAnimation(widget.active));
&#125;

<span class="hljs-comment">///<span class="markdown">未选中</span></span>
<span class="hljs-keyword">void</span> _unSelect() &#123;
    _riveArtboard?.removeController(SimpleAnimation(widget.active));
    _riveArtboard?.addController(SimpleAnimation(widget.idle));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">如何使用？</h4>
<pre><code class="hljs language-dart copyable" lang="dart">RiveIcon(
    rivPath: <span class="hljs-string">'riv_files/test.riv'</span>,
    isSelected: <span class="hljs-keyword">true</span>,
    idle: <span class="hljs-string">'idle'</span>,
    active: <span class="hljs-string">'active'</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rivPath</code>为文件路径<br>
修改<code>isSelected</code>以控制动画状态<br>
<code>idle</code>和<code>active</code>的值可根据图标内的动画名自定义</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2e5059f918d49e4a808758928ac33c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">为什么不推荐使用官方提供的<code>.asset</code>或者<code>.network</code>构造函数?</h4>
<p>官方提供的构造函数不包含状态管理，难以切换动画，只适合<code>循环动画</code>或者<code>一次性动画</code></p>
<h4 data-id="heading-6">PS:</h4>
<p><a href="https://github.com/xSILENCEx/rive_nav" target="_blank" rel="nofollow noopener noreferrer">Demo地址</a><br>
rive文件也在demo里面，感兴趣的朋友可以尝试使用<br>
如果对rive动画的制作也感兴趣可以看一下：<a href="https://juejin.cn/post/6973478894275919908" target="_blank">[Flutter] Rive2（新版Flare）编辑工具简介</a></p></div>  
</div>
            