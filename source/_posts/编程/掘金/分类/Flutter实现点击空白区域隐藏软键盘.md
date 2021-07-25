
---
title: 'Flutter实现点击空白区域隐藏软键盘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6274'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:43:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=6274'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>实现思路：
使用GestureDetector将最外层的MaterialApp包裹起来，监听onTap点击事件，使用FocusSocpe相关的api来控制软件的显示和隐藏。当键盘显示的时候，将键盘隐藏。</p>
<h1 data-id="heading-0">封装Widget</h1>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">/// <span class="markdown">因为不需要保持状态，所以这里继承的是StatelessWidget</span></span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HideKeyboard</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">final</span> Widget child;

  <span class="hljs-keyword">const</span> HideKeyboard(&#123;Key key, <span class="hljs-keyword">this</span>.child&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> GestureDetector(
      child: child,
      onTap: () &#123;
        FocusScopeNode currentFocus = FocusScope.of(context);
        <span class="hljs-keyword">if</span> (!currentFocus.hasPrimaryFocus &&
            currentFocus.focusedChild != <span class="hljs-keyword">null</span>) &#123;
          <span class="hljs-comment">/// <span class="markdown">取消焦点，相当于关闭键盘</span></span>
          FocusManager.instance.primaryFocus.unfocus();
        &#125;
      &#125;,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">使用</h1>
<pre><code class="hljs language-dart copyable" lang="dart">main() &#123;
  runApp(MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyApp(&#123;Key key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-comment">/// <span class="markdown">放在app最外层即可。</span></span>
    <span class="hljs-keyword">return</span> HideKeyboard(
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(
            title: Text(<span class="hljs-string">"Hide soft keyboard demo"</span>),
          ),
          body: Container(
            child: Text(<span class="hljs-string">"hello,world"</span>),
          ),
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            