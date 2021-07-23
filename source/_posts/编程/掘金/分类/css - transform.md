
---
title: 'css - transform'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=462'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:31:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=462'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对元素进行变形。</p>
<p><strong>相关样式：</strong></p>
<ol>
<li>transform-origin</li>
</ol>
<p>设置一个元素变形的原点</p>
<pre><code class="copyable">transform-origin: center; // 默认
transform-origin: top left;
transform-origin: 50px 50px;
transform-origin: bottom right 60px; // 60 -》 z
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<h1 data-id="heading-0">transform-style</h1>
</li>
</ol>
<p>设置元素的子元素是位于 3D 空间中还是平面中。</p>
<pre><code class="copyable">transform-style: flat;
transform-style: preserve-3d;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>transform-box</li>
</ol>
<pre><code class="copyable">transform-box: border-box; // 使用边框作为参考框。表的参考框是包裹着该表的边框，而不是其表框。
transform-box: fill-box; // 使用对象边界框作为参考框。
transform-box: view-box; // 使用最近的SVG视口作为参考框
transform-box: content-box;
transform-box: stroke-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>perspective</li>
</ol>
<p>指定了观察者与 z=0 平面的距离，使具有三维位置变换的元素产生透视效果。 z>0 的三维元素比正常大，而 z<0 时则比正常小，大小程度由该属性的值决定。</p>
<pre><code class="copyable">perspective: 800px;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>perspective-origin</li>
</ol>
<p>指定了观察者的位置，用作 perspective 属性的消失点。</p>
<pre><code class="copyable">perspective-origin: top left;
perspective-origin: 50% 50%;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>backface-visibility</li>
</ol>
<p>指定当元素背面朝向观察者时是否可见</p>
<pre><code class="copyable">backface-visibility: visible;
backface-visibility: hidden;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法有：</strong></p>
<ol>
<li>移动：translate</li>
</ol>
<pre><code class="copyable">transform: translateX(50px);
transform: translateY(30px);
transform: translate(20px, 40px);
transform: translate3d(5px, 22px, 3px);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>缩放：scale</li>
</ol>
<pre><code class="copyable">transform: scaleX(3.5);
transform: scaleY(0.5);
transform: scale(1.5, 0.3);
transform: scale3d(3.5, 0.5, 3.5);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>旋转：rotate</li>
</ol>
<pre><code class="copyable">transform: rotateX(80deg);
transform: rotateY(20deg);
transform: rotate(30deg);
transform: rotate3d(5, -25, 11, 32deg);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>skew：倾斜</li>
</ol>
<pre><code class="copyable">transform: skewX(20deg);
transform: skewY(50deg);
transform: skew(10deg, 40deg);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>matrix：矩阵</li>
</ol>
<p>matrix( scaleX(), skewY(), skewX(), scaleY(), translateX(), translateY() ) 3 x 3
matrix3d(scalex,0,0,0,skewx,scaley,0,0,0,0,scalez,0,translatex,translatey,translatez,1) 4 x 4
可以省略单位</p>
<pre><code class="copyable">/* 2D 默认 */
transform: matrix(1, 0, 0, 1, 0, 0);
/* 3D 默认 */
transform: matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);

matrix(1,0,0,1,30,30) === translate(30,30)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>参考：<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangxinxu.com%2Fwordpress%2F2012%2F06%2Fcss3-transform-matrix-%25E7%259F%25A9%25E9%2598%25B5%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangxinxu.com/wordpress/2012/06/css3-transform-matrix-%E7%9F%A9%E9%98%B5/" ref="nofollow noopener noreferrer">www.zhangxinxu.com/wordpress/2…</a> <br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FZtachi%2Flearn-matrix3d" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Ztachi/learn-matrix3d" ref="nofollow noopener noreferrer">github.com/Ztachi/lear…</a> <br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F52e0018e6ce2" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/52e0018e6ce2" ref="nofollow noopener noreferrer">www.jianshu.com/p/52e0018e6…</a> <br></p>
</blockquote></div>  
</div>
            