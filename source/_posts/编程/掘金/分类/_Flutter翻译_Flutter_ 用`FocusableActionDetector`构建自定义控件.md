
---
title: '_Flutter翻译_Flutter_ 用`FocusableActionDetector`构建自定义控件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9285'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 17:38:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=9285'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://blog.gskinner.com/archives/2021/06/flutter-building-custom-components-with-focusableactiondetector.html" target="_blank" rel="nofollow noopener noreferrer">blog.gskinner.com/archives/20…</a></p>
<p>原文作者：<a href="https://blog.gskinner.com/archives/author/shawnblais" target="_blank" rel="nofollow noopener noreferrer">blog.gskinner.com/archives/au…</a></p>
<p>发布时间：2021年6月11日</p>
</blockquote>
<p>当在Flutter中构建一个自定义的UI控件时，很有可能只是使用一个GestureDetector就结束了，但这样做将是一个错误！尤其是当您打算支持用户使用鼠标或键盘等其他输入方式时。尤其是当您打算支持用户使用鼠标或键盘等其他输入方式时。</p>
<p>事实证明，制作一个对各种输入都表现 "正确 "的UI控件要比仅仅检测敲击动作复杂得多。一般来说，你创建的每个控件都需要以下功能。</p>
<ul>
<li>悬停状态</li>
<li>一个焦点状态（用于TAB键或箭头键的遍历）。</li>
<li>一个可以改变鼠标光标的区域</li>
<li>用于[空格]和[回车]键（或者其他键）的处理程序</li>
</ul>
<p>传统上，你可以通过组成一个大的部件块来创建，包括Focus、Actions、Shortcuts和MouseRegion。这很有效，但有很多模板和缩进。幸运的是，Flutter为这个目的提供了一个专门的小部件。<a href="https://api.flutter.dev/flutter/widgets/FocusableActionDetector-class.html" target="_blank" rel="nofollow noopener noreferrer">FocusableActionDetector</a>。</p>
<p>FocusableActionDetector将Focus、Actions、Shortcuts和MouseRegion融为一体，在Flutter SDK中被大量使用，包括Material DatePicker、Switch、Checkbox、Radio和Slider控件。</p>
<p>自己使用它是相当简单的。让我们来看看我们如何使用这个小部件建立一个完全自定义的按钮。</p>
<p>注意：要跟上代码，请查看这里的gist：<a href="https://gist.github.com/esDotDev/04a6301a3858769d4baf5ab1230f7fa2" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/esDotDev/04…</a></p>
<h1 data-id="heading-0">MyCustomButton</h1>
<p>首先，创建一个StatefulWidget，它可以保存你的_isFocused和_isHovered状态。我们还将创建一个FocusNode，我们可以用它来请求按下时的焦点，这是按钮的一个常见行为。还要创建一些典型的onPressed和标签字段来配置按钮。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyCustomButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  State<MyCustomButton> createState() => _MyCustomButtonState();
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyCustomButtonState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyCustomButton</span>> </span>&#123;
  <span class="hljs-built_in">bool</span> _isHovered = <span class="hljs-keyword">false</span>;
  <span class="hljs-built_in">bool</span> _isFocused = <span class="hljs-keyword">false</span>;
  FocusNode _focusNode = FocusNode();
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
     <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span></span>
  &#125;
  <span class="hljs-keyword">void</span> _handlePressed() &#123;
    _focusNode.requestFocus();
    widget.onPressed();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们正在制作一个按钮，所以我们将添加一些基本的配置选项。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">const</span> MyCustomButton(&#123;Key? key, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.onPressed, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.label&#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> VoidCallback onPressed;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> label;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在剩下的就是填写build()方法了。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Widget build(BuildContext context) &#123;
<span class="hljs-comment">// Change visuals based on focus/hover state</span>
Color outlineColor = _isFocused ? Colors.black : Colors.transparent;
Color bgColor = _isHovered ? Colors.blue.shade100 : Colors.white;
<span class="hljs-comment">// Use `GestureDetector` to handle taps</span>
<span class="hljs-keyword">return</span> GestureDetector(
  onTap: _handlePressed,
  <span class="hljs-comment">// Focus Actionable Detector</span>
  child: FocusableActionDetector(
    focusNode: _focusNode,
    <span class="hljs-comment">// Set mouse cursor</span>
    mouseCursor: SystemMouseCursors.click,
    <span class="hljs-comment">// Rebuild with hover/focus changes</span>
    onShowFocusHighlight: (v) => setState(() => _isFocused = v),
    onShowHoverHighlight: (v) => setState(() => _isHovered = v),
    <span class="hljs-comment">// Button Content</span>
    child: Container(
      padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">8</span>),
      child: Text(widget.label),
      decoration: BoxDecoration(
        color: bgColor,
        border: Border.all(color: outlineColor, width: <span class="hljs-number">1</span>),
      ),
    ),
  ),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，注意你仍然需要包裹一个GestureDetector来检测轻触。此外，注意你如何根据悬停/焦点状态来改变你的ui的外观。</p>
<h1 data-id="heading-1">键盘动作</h1>
<p>任何控件的最后一步是键盘绑定。默认情况下，大多数操作系统控件支持[Space]和[Enter]来 "提交"。你可以通过在.actions字段中连接内置的ActivateIntent来做到这一点。</p>
<pre><code class="hljs language-dart copyable" lang="dart">FocusableActionDetector(
  <span class="hljs-comment">// Hook up the built-in `ActivateIntent` to submit on [Enter] and [Space]</span>
  actions: &#123;
    ActivateIntent: CallbackAction<Intent>(onInvoke: (_) => _handlePressed()),
  &#125;,
  child: ...
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：你可以创建你自己的自定义<a href="https://api.flutter.dev/flutter/widgets/Action-class.html" target="_blank" rel="nofollow noopener noreferrer">动作和意图</a>，但大多数时候，默认的ActivateIntent已经足够了。</p>
<p>你也可以使用.shortcuts参数添加额外的键绑定。这里我们将[Ctrl + X]绑定到同一个ActivateIntent上。现在，我们的控件将在[Enter]、[Space]和[Ctrl + X]时提交!</p>
<pre><code class="hljs language-dart copyable" lang="dart">FocusableActionDetector(
  <span class="hljs-comment">// Add 'Ctrl + X' key to the default [Enter] and [Space]</span>
  shortcuts: &#123;
    SingleActivator(LogicalKeyboardKey.keyX, control: <span class="hljs-keyword">true</span>): ActivateIntent(),
  &#125;,
  child: ...
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这些，你就有了一个完成的控件，它在桌面、网页和手机上都能完全按照你的期望工作</p>
<blockquote>
<p><a href="https://blog.gskinner.com/wp-content/uploads/2021/06/QkwRw94d3L1.mp4" target="_blank" rel="nofollow noopener noreferrer">blog.gskinner.com/wp-content/…</a></p>
<p>Tab键、回车键、空格键、轻击键都能如期工作!</p>
</blockquote>
<p>下面是你的新自定义按钮的完整代码。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyCustomButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyCustomButton(&#123;Key? key, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.onPressed, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.label&#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> VoidCallback onPressed;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> label;
  <span class="hljs-meta">@override</span>
  State<MyCustomButton> createState() => _MyCustomButtonState();
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyCustomButtonState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyCustomButton</span>> </span>&#123;
  <span class="hljs-built_in">bool</span> _isHovered = <span class="hljs-keyword">false</span>;
  <span class="hljs-built_in">bool</span> _isFocused = <span class="hljs-keyword">false</span>;
  FocusNode _focusNode = FocusNode();
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
<span class="hljs-comment">// Change visuals based on focus/hover state</span>
    Color outlineColor = _isFocused ? Colors.black : Colors.transparent;
    Color bgColor = _isHovered ? Colors.blue.shade100 : Colors.white;
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: _handlePressed,
      child: FocusableActionDetector(
        actions: &#123;
          ActivateIntent: CallbackAction<Intent>(onInvoke: (_) => _handlePressed()),
        &#125;,
        shortcuts: &#123;
          SingleActivator(LogicalKeyboardKey.keyX, control: <span class="hljs-keyword">true</span>): ActivateIntent(),
        &#125;,
        child: Container(
          padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">8</span>),
          child: Text(widget.label),
          decoration: BoxDecoration(
            color: bgColor,
            border: Border.all(color: outlineColor, width: <span class="hljs-number">1</span>),
          ),
        ),
      ),
    );
  &#125;
  <span class="hljs-keyword">void</span> _handlePressed() &#123;
    _focusNode.requestFocus();
    widget.onPressed();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要查看一个运行中的例子，以及一个自定义复选框的例子，请查看这里：<a href="https://gist.github.com/esDotDev/04a6301a3858769d4baf5ab1230f7fa2%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/esDotDev/04…</a></p>
<h1 data-id="heading-2">更进一步...</h1>
<p>虽然FocusableActionDetector处理了一些模板，但对于像按钮、复选框、开关等常见的用例来说，它仍然留下了很多东西。具体来说。</p>
<ul>
<li>添加GestureDetector</li>
<li>添加ActivateIntent映射</li>
<li>维护isHovered和isFocused状态</li>
<li>管理提交时的焦点请求</li>
</ul>
<p>在我们看来，所有这些常见的行为都可以用某种构建器来处理。所以我们继续做了一个</p>
<p>它被称为<a href="https://pub.dev/packages/focusable_control_builder" target="_blank" rel="nofollow noopener noreferrer">FocusableControlBuilder</a>，在这里有一个软件包：<a href="https://pub.dev/packages/focusable_control_builder" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/fo…</a></p>
<p>FocusableControlBuilder支持GestureDetector，管理FocusNode，为键盘支持添加了一个ActivateIntent，并提供了一个构建方法，可以访问control.isFocused和control.isHovered，以便在视图的构建中使用。呵!</p>
<p>对于大多数使用情况，这将消除大部分的模板。按钮、复选框、切换器、滑块等都可以以这个构建器为基础，用不同的手势或状态对其进行扩展。</p>
<p>如果我们转换前面的例子，它看起来像。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyCustomButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyCustomButton(<span class="hljs-keyword">this</span>.label, &#123;Key? key, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.onPressed&#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> label;
  <span class="hljs-keyword">final</span> VoidCallback onPressed;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> FocusableControlBuilder(
        onPressed: onPressed,
        builder: (_, FocusableControlState control) &#123;
          Color outlineColor = control.isFocused ? Colors.black : Colors.transparent;
          Color bgColor = control.isHovered ? Colors.blue.shade100 : Colors.grey.shade200;
          <span class="hljs-keyword">return</span> Container(
            padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">8</span>),
            child: Text(label),
            decoration: BoxDecoration(
              color: bgColor,
              border: Border.all(color: outlineColor, width: <span class="hljs-number">1</span>),
            ),
          );
        &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不错啊! 我们希望你觉得这个包有用，如果你觉得有用，请在下面告诉我们</p>
<hr>
<p><a href="http://www.deepl.com/" target="_blank" rel="nofollow noopener noreferrer">www.deepl.com</a> 翻译</p></div>  
</div>
            