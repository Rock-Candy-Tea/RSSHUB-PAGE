
---
title: 'Flutter适配安卓刘海、水滴屏显示全屏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2280'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 23:56:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2280'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>配置Android</li>
</ul>
<p>找到android/app/src/main/res/values目录,打开styles.xml
将shortEdges放到style标签内。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-meta"><?xml version="1.0" encoding="utf-8"?></span>
<span class="hljs-tag"><<span class="hljs-name">resources</span>></span>
    <span class="hljs-comment"><!-- Theme applied to the Android Window while the process is starting --></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"LaunchTheme"</span> <span class="hljs-attr">parent</span>=<span class="hljs-string">"@android:style/Theme.Black.NoTitleBar"</span>></span><span class="xml">
        <span class="hljs-comment"><!-- Show a splash screen on the activity. Automatically removed when
             Flutter draws its first frame --></span>
        <span class="hljs-tag"><<span class="hljs-name">item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"android:windowBackground"</span>></span>@drawable/launch_background<span class="hljs-tag"></<span class="hljs-name">item</span>></span>
        /// 放这里
        <span class="hljs-tag"><<span class="hljs-name">item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"android:windowLayoutInDisplayCutoutMode"</span>></span>shortEdges<span class="hljs-tag"></<span class="hljs-name">item</span>></span>
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-comment"><!-- Theme applied to the Android Window as soon as the process has started.
         This theme determines the color of the Android Window while your
         Flutter UI initializes, as well as behind your Flutter UI while its
         running.
         
         This Theme is only used starting with V2 of Flutter's Android embedding. --></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"NormalTheme"</span> <span class="hljs-attr">parent</span>=<span class="hljs-string">"@android:style/Theme.Black.NoTitleBar"</span>></span><span class="xml">
        <span class="hljs-tag"><<span class="hljs-name">item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"android:windowBackground"</span>></span>@android:color/white<span class="hljs-tag"></<span class="hljs-name">item</span>></span>
        /// 放这里
        <span class="hljs-tag"><<span class="hljs-name">item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"android:windowLayoutInDisplayCutoutMode"</span>></span>shortEdges<span class="hljs-tag"></<span class="hljs-name">item</span>></span>
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">resources</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LaunchTheme指的是启动页的主题，也就是我们常说的Splah页面。如果需要启动页全屏就放在里面。
NormalTheme代表正常页面的主题。
根据需求，我们可以放在2个不同的地方。</p>
<ul>
<li>Flutter中设置SystemChrome.setEnabledSystemUIOverlays([])，隐藏状态栏和底部导航栏</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@override</span>
initState() &#123;
  <span class="hljs-comment">/// 初始化时隐藏</span>
      SystemChrome.setEnabledSystemUIOverlays([]);
      <span class="hljs-keyword">super</span>.initState();
&#125;

<span class="hljs-meta">@override</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">dispose</span><span class="hljs-params">()</span> </span>&#123; 
<span class="hljs-comment">/// 页面关闭时恢复正常设置</span>
  SystemChrome.setEnabledSystemUIOverlays(SystemUiOverlay.values);
    <span class="hljs-keyword">super</span>.dispose();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            