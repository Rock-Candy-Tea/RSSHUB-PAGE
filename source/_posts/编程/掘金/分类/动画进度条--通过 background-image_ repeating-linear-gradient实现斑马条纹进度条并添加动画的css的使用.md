
---
title: '动画进度条--通过 background-image_ repeating-linear-gradient实现斑马条纹进度条并添加动画的css的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61db36eba4c4f70b1df27c30c001f88~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:46:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61db36eba4c4f70b1df27c30c001f88~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">动画进度条--通过 background-image: repeating-linear-gradient实现斑马条纹进度条并添加动画的css的使用</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61db36eba4c4f70b1df27c30c001f88~tplv-k3u1fbpfcp-watermark.image" alt="progress.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">效果</h2>
<p>codepen：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fczzonet%2Fpen%2FWNOeoNP" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/czzonet/pen/WNOeoNP" ref="nofollow noopener noreferrer">progress</a></p>
<h2 data-id="heading-2">原理</h2>
<p>通过 background-image: repeating-linear-gradient实现进度条斑马条纹并用background-position进行动画。</p>
<h2 data-id="heading-3">实现</h2>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.progress</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">300px</span> auto;

  <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;

  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">repeating-linear-gradient</span>(
    <span class="hljs-number">45deg</span>,
    <span class="hljs-number">#2ed573</span> <span class="hljs-number">0%</span>,
    <span class="hljs-number">#2ed573</span> <span class="hljs-number">1%</span>,
    <span class="hljs-number">#7bed9f</span> <span class="hljs-number">1%</span>,
    <span class="hljs-number">#7bed9f</span> <span class="hljs-number">2%</span>
  );

  <span class="hljs-attribute">background-position</span>: -<span class="hljs-number">2%</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background-size</span>: <span class="hljs-number">150%</span>;
  <span class="hljs-attribute">animation</span>: slider <span class="hljs-number">5s</span> linear infinite;
&#125;

<span class="hljs-keyword">@keyframes</span> slider &#123;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">background-position</span>: -<span class="hljs-number">100%</span> <span class="hljs-number">0</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">知识点</h2>
<h3 data-id="heading-5">repeating-linear-gradient()</h3>
<p>CSS函数 <strong><code>repeating-linear-gradient()</code></strong> 创建一个由重复线性渐变组成的<img src="https://juejin.cn/post/6998893926711033886" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#grad1</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-number">180deg</span>,
      <span class="hljs-built_in">rgb</span>(<span class="hljs-number">26</span>,<span class="hljs-number">198</span>,<span class="hljs-number">204</span>),
      <span class="hljs-built_in">rgb</span>(<span class="hljs-number">26</span>,<span class="hljs-number">198</span>,<span class="hljs-number">204</span>) <span class="hljs-number">7%</span>,
      <span class="hljs-built_in">rgb</span>(<span class="hljs-number">100</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>) <span class="hljs-number">10%</span>);
&#125;

<span class="hljs-selector-id">#grad2</span> &#123;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">repeating-linear-gradient</span>(-<span class="hljs-number">45deg</span>,
      transparent,
      transparent <span class="hljs-number">25px</span>,
      <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>,<span class="hljs-number">255</span>,<span class="hljs-number">255</span>,<span class="hljs-number">1</span>) <span class="hljs-number">25px</span>,
      <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>,<span class="hljs-number">255</span>,<span class="hljs-number">255</span>,<span class="hljs-number">1</span>) <span class="hljs-number">50px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：</p>
<ul>
<li>渐变：在指定位置切换颜色</li>
<li>斑马纹：只要指定渐变的开始和结束的位置是同一个颜色，就能实现纯色而不是渐变的色块了。</li>
</ul>
<h3 data-id="heading-6">background-position</h3>
<p><strong><code>background-position</code></strong> 为每一个背景图片设置初始位置。</p>
<p>百分比值的偏移指定图片的相对位置和容器的相对位置重合。值0%代表图片的左边界（或上边界）和容器的左边界（上边界）重合。值100%代表图片的右边界（或下边界）和容器的右边界（或下边界）重合。值50%则代表图片的中点和容器的中点重合。</p>
<p>因此，如果背景图片小，正百分比向右移动，图片大，正百分比向左移动。</p>
<p>另外需要注意，如果背景图片的大小和容器一样，那设置百分比的值将永远无效，因为“容器和图片的差”为0（图片永远填满容器，并且图片的相对位置和容器的相对位置永远重合）。在这种情况下，需要为偏移使用绝对值（例如px）。</p>
<h2 data-id="heading-7">总结</h2>
<p>简单介绍了repeating-linear-gradient和background-position的css知识，通过实际应用加深印象。另外如果需要控制动画的启停，只需要切换css即可。</p>
<p>如果本文对你有帮助，欢迎点赞关注，让更多的人看到。</p>
<h2 data-id="heading-8">Reference</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fgradient%2Frepeating-linear-gradient()" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient/repeating-linear-gradient()" ref="nofollow noopener noreferrer">repeating-linear-gradient() - CSS（层叠样式表） | MDN</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fbackground-position" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-position" ref="nofollow noopener noreferrer">background-position - CSS（层叠样式表） | MDN</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Do4y1U7pd" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1Do4y1U7pd" ref="nofollow noopener noreferrer">1分钟用CSS实现和bootstrap3一样的动画进度条_哔哩哔哩_bilibili</a></li>
</ol></div>  
</div>
            