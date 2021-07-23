
---
title: '如何优雅的在flutter中使用logger'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67c2fbdb1f8648c8bab81ab53b226c7c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 02:00:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67c2fbdb1f8648c8bab81ab53b226c7c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">flutter中的logger</h1>
<p>flutter中的日志使用print实现，但是print只能显示一种颜色，这样我们调试起来比较麻烦。所以，我在ansicolor的基础上实现了一个可以控制颜色的日志记录框架。</p>
<h1 data-id="heading-1">如何使用</h1>
<p>已发布pub，直接引用即可</p>
<p><code>colorize_logger: ^[last version]</code></p>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fcolorize_logger" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/colorize_logger" ref="nofollow noopener noreferrer">pub.dev/packages/co…</a></p>
<p>github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTaleAi%2Fflutter_colorize_logger" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TaleAi/flutter_colorize_logger" ref="nofollow noopener noreferrer">github.com/TaleAi/flut…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67c2fbdb1f8648c8bab81ab53b226c7c~tplv-k3u1fbpfcp-watermark.image" alt="screenshot.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">优点</h1>
<ul>
<li>有 info、warning、error、fatal四种日志类型及颜色</li>
<li>release模式自动关闭日志</li>
<li>可自定义输出风格</li>
</ul>
<h1 data-id="heading-3">简单用法</h1>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:colorize_logger/colorize_logger.dart'</span>;

<span class="hljs-comment">// 初始化</span>
Logger.client = ColorizeLoggerClient();

Logger.info(<span class="hljs-string">'info'</span>);
Logger.warning(<span class="hljs-string">'waring'</span>, tag: <span class="hljs-string">'_MyHomePageState'</span>);<span class="hljs-comment">/// <span class="markdown">可以设置tag</span></span>
Logger.fatal(<span class="hljs-string">'fatal'</span>);
Logger.error(<span class="hljs-string">'error'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">自定义扩展</h1>
<p>先来看看基类</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoggerClient</span> </span>&#123;
  <span class="hljs-keyword">void</span> info(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;);
  <span class="hljs-keyword">void</span> warning(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;);
  <span class="hljs-keyword">void</span> error(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;);
  <span class="hljs-keyword">void</span> fatal(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要继承并实现LoggerClient的方法就可以自定义了</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:ansicolor/ansicolor.dart'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'client.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomLoggerClient</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LoggerClient</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> error(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;) &#123;
    <span class="hljs-keyword">final</span> error = AnsiPen()
      ..white(bold: <span class="hljs-keyword">true</span>)
      ..xterm(<span class="hljs-number">88</span>, bg: <span class="hljs-keyword">true</span>);
    <span class="hljs-built_in">print</span>(error(_format(tag ?? <span class="hljs-string">'ERROR'</span>, message)));
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> fatal(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;) &#123;
    <span class="hljs-keyword">final</span> fatal = AnsiPen()
      ..white()
      ..red(bg: <span class="hljs-keyword">true</span>);
    <span class="hljs-built_in">print</span>(fatal(_format(tag ?? <span class="hljs-string">'FATAL'</span>, message)));
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> info(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;) &#123;
    <span class="hljs-keyword">final</span> info = AnsiPen()
      ..black()
      ..green(bg: <span class="hljs-keyword">true</span>);
    <span class="hljs-built_in">print</span>(info(_format(tag ?? <span class="hljs-string">'INFO'</span>, message)));
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> warning(<span class="hljs-built_in">String</span> message, &#123;<span class="hljs-built_in">String?</span> tag&#125;) &#123;
    <span class="hljs-keyword">final</span> info = AnsiPen()
      ..black()
      ..yellow(bg: <span class="hljs-keyword">true</span>);
    <span class="hljs-built_in">print</span>(info(_format(tag ?? <span class="hljs-string">'WARNING'</span>, message)));
  &#125;

  <span class="hljs-built_in">String</span> _format(<span class="hljs-built_in">String</span> tag, <span class="hljs-built_in">String</span> message) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'[<span class="hljs-subst">$tag</span>] <span class="hljs-subst">$message</span>'</span>;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来只要在初始化的地方替换就可以实现自定义日志</p>
<pre><code class="hljs language-dart copyable" lang="dart">Logger.client = CustomLoggerClient();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">下一步计划</h1>
<p>考虑到在实际应用中，给测试的包是release的版本，这样有问题的时候我们无法看到日志，所以下一步的计划是</p>
<ul>
<li>实现一个基于文件的日志记录，可以存储在手机中，这样有问题可以导出日志给开发看</li>
</ul></div>  
</div>
            