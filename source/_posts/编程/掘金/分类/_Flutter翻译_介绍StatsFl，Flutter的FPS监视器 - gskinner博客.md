
---
title: '_Flutter翻译_介绍StatsFl，Flutter的FPS监视器 - gskinner博客'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1266c65873ba4c66ad884f4338a2765b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:19:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1266c65873ba4c66ad884f4338a2765b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://medium.com/flutter-community/introducing-statsfl-an-fps-monitor-for-flutter-gskinner-blog-aed95eb9f68f" target="_blank" rel="nofollow noopener noreferrer">medium.com/flutter-com…</a></p>
<p>原文作者：<a href="https://medium.com/@gskinner_team" target="_blank" rel="nofollow noopener noreferrer">medium.com/@gskinner_t…</a></p>
<p>发布时间：2020年4月14日 - 2分钟阅读</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1266c65873ba4c66ad884f4338a2765b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>随着我们开始将Flutter推向更多的平台，如桌面和网络，快速和轻松地测量你的应用程序的性能变得越来越重要。虽然内置的性能监控器可以完成工作，但它在可读性方面还有很多不足之处。</p>
<p>为了帮助缓解这个问题，我们创建了StatsFl：<a href="https://pub.dev/packages/statsfl" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/st…</a></p>
<p>使用时，只需将你的根视图包裹在StatsFl小组件中。</p>
<pre><code class="hljs language-dart copyable" lang="dart">StatsFl(child: MyApp());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个简单的改变，你将在你的应用程序的左上方得到一个离散的FPS历史图表</p>
<p>在大多数情况下，默认的选项应该是你所需要的，但为了以防万一，我们已经使它变得相当可配置。下图显示了3种配置下的StatsFl。正如你所看到的，对齐方式、宽度和高度都可以调整。你甚至可以关掉showText，以获得一个简约的模式（底部）。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59d112d87daa4e25b47736c67d446307~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外，你可以根据你的需要调整sampleTime和totalTime的长度。在这个例子中，我们每0.5秒计算一次，在15秒的时间内，总共有30个样本。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">return</span> StatsFl( 
   sampleTime: <span class="hljs-number">.5</span>, <span class="hljs-comment">//Interval between fps calculations, in seconds.</span>
   totalTime: <span class="hljs-number">15</span>, <span class="hljs-comment">//Total length of timeline, in seconds. </span>
   child: MyApp()
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你喜欢这个包，请抛出一个大拇指，以帮助增加人气!</p>
<hr>
<p>原文发表于2020年4月14日<a href="https://blog.gskinner.com/" target="_blank" rel="nofollow noopener noreferrer">blog.gskinner.com</a></p>
<hr>
<p><a href="http://www.deepl.com/" target="_blank" rel="nofollow noopener noreferrer">www.deepl.com</a> 翻译</p></div>  
</div>
            