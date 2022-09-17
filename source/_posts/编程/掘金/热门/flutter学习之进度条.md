
---
title: 'flutter学习之进度条'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b96baab3d124bcf93728b51f766baa6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Tue, 30 Aug 2022 05:39:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b96baab3d124bcf93728b51f766baa6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第30天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>本文主要介绍下flutter中进度条的使用</p>
</blockquote>
<h2 data-id="heading-0">LinearProgressIndicator</h2>
<p><code>LinearProgressIndicator</code>线性进度指示器，也称为进度条。继承<code>ProgressIndicator</code></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> LinearProgressIndicator(&#123;
  Key? key,
  <span class="hljs-built_in">double?</span> value,
  Color? backgroundColor,
  Color? color,
  Animation<Color?>? valueColor,
  <span class="hljs-keyword">this</span>.minHeight,
  <span class="hljs-built_in">String?</span> semanticsLabel,
  <span class="hljs-built_in">String?</span> semanticsValue,
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>水平进度指示器，基本用法如下</p>
<pre><code class="hljs language-dart copyable" lang="dart">Scaffold(
  appBar: AppBar(title: Text(<span class="hljs-string">'Indicator'</span>),),
  body:LinearProgressIndicator(),
  floatingActionButton: FloatingActionButton(
    child: <span class="hljs-keyword">const</span> Icon(Icons.navigate_next),
    onPressed: () &#123;
    &#125;,),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b96baab3d124bcf93728b51f766baa6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-29_21.32.18.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>value</code>设置具体</p>
<pre><code class="hljs language-dart copyable" lang="dart">LinearProgressIndicator(
  value: <span class="hljs-number">0.4</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>value</code>的值范围是0-1，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996c5b4820c542a191cdc4e4f2fe230f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
设置背景颜色及进度值：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> LinearProgressIndicator(
  value: <span class="hljs-number">0.4</span>,
    backgroundColor: Colors.yellowAccent,
    valueColor: AlwaysStoppedAnimation<Color>(Colors.black)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c8da62e77fc40e9970e9b85fb1abba4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">CircularProgressIndicator</h2>
<p><code>CircularProgressIndicator</code> 是圆形进度条，和<code>LinearProgressIndicator</code>用法一样：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> CircularProgressIndicator(&#123;
  Key? key,
  <span class="hljs-built_in">double?</span> value,
  Color? backgroundColor,
  Color? color,
  Animation<Color?>? valueColor,
  <span class="hljs-keyword">this</span>.strokeWidth = <span class="hljs-number">4.0</span>,
  <span class="hljs-built_in">String?</span> semanticsLabel,
  <span class="hljs-built_in">String?</span> semanticsValue,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单使用：</p>
<pre><code class="hljs language-dart copyable" lang="dart">CircularProgressIndicator()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b57a9e38bb74d45a310107fba51ef75~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-29_21.45.12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置进度值及颜色值：</p>
<pre><code class="hljs language-dart copyable" lang="dart">CircularProgressIndicator(
  value: <span class="hljs-number">0.3</span>,
  backgroundColor: Colors.blue,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.redAccent),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aa54a19a81a4e20b76a9ac9788ca7d9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">CupertinoActivityIndicator</h2>
<p><code>CupertinoActivityIndicator</code>是我们iOS中加载风格的指示器，CupertinoActivityIndicator不能设置进度，只能一直转“菊花”</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">const</span> CupertinoActivityIndicator(&#123;
  Key? key,
  <span class="hljs-keyword">this</span>.color,
  <span class="hljs-keyword">this</span>.animating = <span class="hljs-literal">true</span>,
  <span class="hljs-keyword">this</span>.radius = _kDefaultIndicatorRadius,
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用默认</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-built_in">CupertinoActivityIndicator</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f4289c801de46db9c199882e5ada329~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-29_21.53.27.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>radius</code>参数是半径，值越大，控件越大。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"> CupertinoActivityIndicator(
  radius: <span class="hljs-number">60</span>,
  color: Colors.redAccent,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe6edc9c9826484ab25c1d38175dff6d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-29_21.56.10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">flutter_progress_hud</h2>
<p>覆盖加载屏幕显示一个进度指示器，也称为模态进度 HUD 或平视显示，这通常意味着应用程序正在加载或执行一些工作。
我们也可以使用一些三方的加载f<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fflutter_progress_hud" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/flutter_progress_hud" ref="nofollow noopener noreferrer">lutter_progress_hud:</a></p>
<pre><code class="hljs language-Dart copyable" lang="Dart">ProgressHUD(
  borderColor:Colors.orange,
  backgroundColor:Colors.blue.,
  child:Builder(
    builder:(context)=>Container(
      height:DeviceSize.height(context),
      width:DeviceSize.width(context),
      padding:EdgeInsets.only(left:<span class="hljs-number">20</span>,right:<span class="hljs-number">20</span>,top:<span class="hljs-number">20</span>),
    ),
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以根据context 初始化</p>
<pre><code class="hljs language-ini copyable" lang="ini">final <span class="hljs-attr">progress</span> = ProgressHUD.of(context)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>show</p>
<pre><code class="hljs language-scss copyable" lang="scss">progress<span class="hljs-selector-class">.show</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加提示语</p>
<pre><code class="hljs language-scss copyable" lang="scss">progress<span class="hljs-selector-class">.showWithText</span>('Loading...');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>消失</p>
<pre><code class="hljs language-scss copyable" lang="scss">progress<span class="hljs-selector-class">.dismiss</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/873ffe138f1e4cf2a141962108c58ce7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="demo.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            