
---
title: 'Flutter FractionallySizedBox 按比例设置Widget的尺寸'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2390bb784549c3ae2a5643299f3b92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 01:48:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2390bb784549c3ae2a5643299f3b92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">FractionallySizedBox 按比例设置Widget的尺寸</h1>
<p>有时候,应用的设计是按照比例给出的 , 例如这种情况:
有一个按钮,它的宽度应该占应用父级宽度的70%
或者
页面的边距是整体控件的10%</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2390bb784549c3ae2a5643299f3b92~tplv-k3u1fbpfcp-watermark.image" alt="image-20200822151426410" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时可以使用FractionallySizedBox来实现.</p>
<h2 data-id="heading-1">构造方法</h2>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> FractionallySizedBox(&#123;
  Key key,
  <span class="hljs-keyword">this</span>.alignment = Alignment.center,
  <span class="hljs-keyword">this</span>.widthFactor,
  <span class="hljs-keyword">this</span>.heightFactor,
  Widget child,
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先看一下构造方法 :</p>
<ul>
<li>alignment: 对齐方式, 用来控制FractionallySizedBox在父组件中的位置 , 默认是中间Alignment.center</li>
<li>widthFactor: 宽度系数,取0-1之间. 如0.8,代表宽度为可用尺寸的80%.</li>
<li>heightFactor: 高度系数,取0-1之间.</li>
<li>child: 需要设置的widget</li>
</ul>
<p><strong>关于heightFactor/widthFactor , 其所占的比例为可用尺寸的比例,一般为父组件的尺寸,并非屏幕的尺寸</strong></p>
<h2 data-id="heading-2">使用</h2>
<ol>
<li>设置控件尺寸</li>
</ol>
<p>使用FractionallySizedBox来包裹你想要设置的Widget,给它一个高度或宽度系数 , 例如 0.5表示可用尺寸的50%,即一半.</p>
<p>然后使用<code>alignment</code>来控制<code>FractionallySizedBox</code>应该显示在哪.</p>
<p>例如:</p>
<pre><code class="hljs language-dart copyable" lang="dart">FractionallySizedBox(
            alignment: Alignment.bottomRight,
            heightFactor: <span class="hljs-number">0.5</span>,
            widthFactor: <span class="hljs-number">0.5</span>,
            child: YourWidget
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f171a19e6024ad99e844603cca8ade0~tplv-k3u1fbpfcp-watermark.image" alt="image-20200822153005763" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>填充空白部分</li>
</ol>
<p>假如有一行组件,比如一个左侧有一个图片, 右侧有一个文本,而中间相距10dp,</p>
<p>可能我们会使用SizedBox来填充:</p>
<pre><code class="hljs language-dart copyable" lang="dart">          Row(
            children: [
              Image.network(<span class="hljs-string">'imgurl'</span>),
              SizedBox(width: <span class="hljs-number">10</span>),
              Text(<span class="hljs-string">'文字'</span>),
            ],
          )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果二者之间的距离是按比例来的呢?</p>
<p>这时可以使用没有child的FractionallySizedBox来替代SizedBox()来填充空白区域.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6c41c7e91d041e78c5d45274e64dc87~tplv-k3u1fbpfcp-watermark.image" alt="image-20200822153229372" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart">FractionallySizedBox(
              heightFactor: <span class="hljs-number">0.1</span>,
            )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是在Row或者Column中使用, 可以将这个<code>FractionallySizedBox</code>包裹在<code>Flexible</code>中 :</p>
<pre><code class="hljs language-dart copyable" lang="dart">Flexible(
            child: FractionallySizedBox(
              heightFactor: <span class="hljs-number">0.1</span>,
            ),
          )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码地址:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizhuoyuan%2Fflutter_study%2Fblob%2Fmaster%2Flib%2Fpage%2Ffractionally_sized_box_page.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lizhuoyuan/flutter_study/blob/master/lib/page/fractionally_sized_box_page.dart" ref="nofollow noopener noreferrer">github</a></p>
<h3 data-id="heading-3">扩展</h3></div>  
</div>
            