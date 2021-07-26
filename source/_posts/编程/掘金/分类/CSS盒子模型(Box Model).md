
---
title: 'CSS盒子模型(Box Model)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50f628b348a4b619409cc3a29fe3b2b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 23:57:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50f628b348a4b619409cc3a29fe3b2b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>所有HTML元素可以看作盒子，在CSS中，"box model"这一术语是用来设计和布局时使用。</p>
<p>CSS盒模型本质上是一个盒子，封装周围的HTML元素，它包括：边距，边框，填充，和实际内容。</p>
<p>盒模型允许我们在其它元素和周围元素边框之间的空间放置元素。</p>
<p>下面的图片说明了盒子模型(Box Model)：</p>
<p><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50f628b348a4b619409cc3a29fe3b2b~tplv-k3u1fbpfcp-zoom-1.image" alt="CSS box-model" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不同部分的说明：</p>
<ul>
<li><strong>Margin(外边距)</strong>  - 清除边框外的区域，外边距是透明的。</li>
<li><strong>Border(边框)</strong>  - 围绕在内边距和内容外的边框。</li>
<li><strong>Padding(内边距)</strong>  - 清除内容周围的区域，内边距是透明的。</li>
<li><strong>Content(内容)</strong>  - 盒子的内容，显示文本和图像。</li>
</ul>
<p>为了正确设置元素在所有浏览器中的宽度和高度，你需要知道的盒模型是如何工作的。</p>
<hr>
<h2 data-id="heading-0">元素的宽度和高度</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8e87cff01904807ab7c8a9b9806a516~tplv-k3u1fbpfcp-zoom-1.image" alt="Remark" loading="lazy" referrerpolicy="no-referrer"><strong>重要:</strong>  当您指定一个 CSS 元素的宽度和高度属性时，你只是设置内容区域的宽度和高度。要知道，完整大小的元素，你还必须添加内边距，边框和外边距。</p>
<p>下面的例子中的元素的总宽度为500px：</p>
<h2 data-id="heading-1">实例</h2>
<p>div &#123; width: 500px; border: 25px solid green; padding: 25px; margin: 25px; &#125;</p>
<p><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Ftry%2Ftry.php%3Ffilename%3Dtrycss_boxmodel" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/try/try.php?filename=trycss_boxmodel" ref="nofollow noopener noreferrer">尝试一下 »</a></p>
<p>让我们自己算算：<br>
500px (宽)\</p>
<ul>
<li>50px (左 + 右填充)\</li>
<li>50px (左 + 右边框)\</li>
<li>50px (左 + 右边距)\</li>
</ul>
<p>= 650px</p>
<p>总结：### 盒子中的区域</p>
<p>一个盒子中主要的属性就5个：width、height、padding、border、margin。如下：</p>
<ul>
<li>width和height：<strong>内容</strong>的宽度、高度（不是盒子的宽度、高度）。</li>
<li>padding：内边距。</li>
<li>border：边框。</li>
<li>margin：外边距。</li>
</ul></div>  
</div>
            