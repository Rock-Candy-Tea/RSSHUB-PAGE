
---
title: '使用css3绘制github章鱼猫'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad077f128f84feaa1d80ccf1501f376~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 18:05:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad077f128f84feaa1d80ccf1501f376~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 概述</h2>
<p>最近整理<code>CSS</code>和大家分享一下使用 <code>CSS3</code> 绘制<code>github</code> 的章鱼猫 <code>Logo</code> 的过程。</p>
<p>网上经常能看到一些通过<code>border</code>属性实现的圆形，椭圆形，三角形。这里主要用到的就是<code>CSS</code>的<code>border</code>属性。通过<code>border-radius</code>来设置矩形的圆角。</p>
<p><code>border-radius</code>最多可指定四个值，分别是左上角，右上角，右下角和左下角。也可以分别设置每个角的值，而且可以精确到角度的<code>X</code>，<code>Y</code>轴的值。</p>
<pre><code class="hljs language-css copyable" lang="css">// 左上角
<span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">40px</span> <span class="hljs-number">80px</span>;
// 右上角
<span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">40px</span> <span class="hljs-number">80px</span>;
// 左下角
<span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">40px</span> <span class="hljs-number">80px</span>;
// 右下角
<span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">40px</span> <span class="hljs-number">80px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>40px</code>和<code>80px</code>分别表示<code>X</code>轴参与弯曲弧度的部分为<code>40px</code>，<code>Y</code>轴参与弯曲的弧度为<code>80px</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad077f128f84feaa1d80ccf1501f376~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.36.48.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2. 开始绘制</h2>
<p>章鱼猫的所有部位都是通过<code>div</code>元素标签绘制再通过定位进行组合，首先绘制出头部的轮廓。通过设置四个角度的圆角画出大饼脸。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
<span class="hljs-attribute">width</span>: <span class="hljs-number">268px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">204px</span>;
<span class="hljs-attribute">left</span>: <span class="hljs-number">116px</span>;
<span class="hljs-attribute">top</span>: <span class="hljs-number">77px</span>;
<span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">137px</span> <span class="hljs-number">94px</span>;
<span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">137px</span> <span class="hljs-number">94px</span>;
<span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">105px</span> <span class="hljs-number">95px</span>;
<span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">104px</span> <span class="hljs-number">82px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5905e9ac4d9042578193f71a560107b0~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.42.46.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>加上耳朵。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
<span class="hljs-attribute">width</span>: <span class="hljs-number">60px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">12deg</span>);
<span class="hljs-attribute">top</span>: <span class="hljs-number">66px</span>;
<span class="hljs-attribute">left</span>: <span class="hljs-number">133px</span>;
<span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">150px</span> <span class="hljs-number">36px</span>;
<span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">43px</span> <span class="hljs-number">95px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8efe07cde2354a938ccf513e1f7ca85e~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.44.37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>五官</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9610ca9fa26419bbb1291e9102db27c~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.45.01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>胡须</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">position</span>: absolute; 
<span class="hljs-attribute">height</span>: <span class="hljs-number">8px</span>;
<span class="hljs-attribute">width</span>: <span class="hljs-number">98px</span>;
<span class="hljs-attribute">top</span>: <span class="hljs-number">222px</span>;
<span class="hljs-attribute">left</span>: <span class="hljs-number">26px</span>;
<span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">98px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">border-top</span>: <span class="hljs-number">1px</span> solid red;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/661e9a060e394bdda3e45f97179e1d66~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.45.18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>四只脚和小尾巴，可以使用<code>border</code>属性来设置。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">border-right</span>: <span class="hljs-number">6px</span> solid red;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">70px</span>;
<span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">70px</span> <span class="hljs-number">70px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过这里偷懒了，直接使用模块绘制的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4139a8e9dee441b7a94f7a90cd6f1496~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 19.45.38.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3. 填充颜色</h2>
<p>整体完成之后添加上颜色。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30fe8a0ce20a40549c50567643d8a34a~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 20.14.00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>已经变得有模有样了，继续~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfbe1e94ce714b48b7d94b91d01a478a~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 20.20.10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后装饰一下小尾巴！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4804dcf1ea5d476ab25fc965c6e03913~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-08-17 20.29.35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成！</p></div>  
</div>
            