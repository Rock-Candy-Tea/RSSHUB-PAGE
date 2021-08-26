
---
title: '纯CSS绘制曲线 _ radial-gradient'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c198657dd21b41e9b08d2f3854624759~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 07:01:40 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c198657dd21b41e9b08d2f3854624759~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>在昨天的文章中：<a href="https://juejin.cn/post/7000006806911057956" target="_blank" title="https://juejin.cn/post/7000006806911057956">clip-path的一个重要的函数path所引入的曲线绘制问题</a>我们提到，可以通过<code>radial-gradient</code>绘制曲线，那么如何实现这一目的的，今天我们来扩展阐述学习一下。</p>
<h2 data-id="heading-0">初步认识<code>radial-gradient</code></h2>
<p><code>radial-gradient</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fgradient%2Fradial-gradient()" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient/radial-gradient()" ref="nofollow noopener noreferrer">MDN官方释义</a>：</p>
<blockquote>
<p><code>radial-gradient()</code> CSS函数创建了一个图像，该图像是由从原点发出的两种或者多种颜色之间的逐步过渡组成。它的形状可以是圆形（circle）或椭圆形（ellipse）。这个方法得到的是一个CSS<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fgradient" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient" ref="nofollow noopener noreferrer"><code><gradient></code></a>数据类型的对象，其是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fimage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/image" ref="nofollow noopener noreferrer"><code><image></code></a> 的一种。</p>
</blockquote>
<p>语法规则：</p>
<blockquote>
<p>radial-gradient(circle at center, red 0, blue, green 100%)</p>
<p>表示：
A gradient at the center of its container,
starting red, changing to blue, and finishing green</p>
</blockquote>
<p>TALK IS CHEAP, SHOW ME THE CODE!</p>
<p>话不多说，上代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<title>radial-gradient学习</title>
<body>
    <div class="box">
        radial-gradient(circle at center, red 0, blue, green 100%);
    </div>
</body>
<style>
    .box &#123;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;

        font-size: 16px;
        font-weight: bold;

        width: 500px;
        height: 500px;
        background: radial-gradient(circle at center, red 0, blue, green 100%);
    &#125;
</style>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码为基础代码，后续我们的变化也会基于此进行绘制。</p>
<p>初步效果如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c198657dd21b41e9b08d2f3854624759~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>几个参数的变换效果如下列的图：</p>
<ol>
<li>(1)圆心位置变化</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afc63f6b6e9e4767a36beeeeb9a1ba78~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(2)圆心位置变化：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d9d041687d547848d1a01a218c6b78c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><code>size</code>参数变化：</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc2754c4b79547e3a440ce8bda431869~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>颜色变化：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/586a051180b4436a81a079bd773ae309~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">回忆另外一个渐变函数<code>linear-gradient</code></h2>
<p>记得我们阐述过另外一个与颜色过渡有关的函数，<code>linear-gradient</code>：<a href="https://juejin.cn/post/6995500195337207822" target="_blank" title="https://juejin.cn/post/6995500195337207822">纯CSS输出渐变色背景图案 | linear-gradient</a>，
类似<code>linear-gradient</code>可以绘制某个颜色的直线，我们也可以通过<code>radial-gradient</code>绘制曲线。</p>
<h2 data-id="heading-2">曲线绘制</h2>
<p>先来一个简单的：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50a360acc4454ba4be6ede45619a7e1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，我们通过调节圆心位置，尺寸大小，过渡颜色，就可以绘制曲线了。并且background允许多个<code>radial-gradient</code>参数，即可以绘制多条曲线。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ffb9486996c4352b67173517400ec22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="copyable"><!DOCTYPE html>
<title>radial-gradient学习</title>
<body>
    <div class="box1">
        background: radial-gradient(circle at center, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%),
                    radial-gradient(circle at top 0 left 0, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%),
                    radial-gradient(circle at top 0 left 100px, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%);
    </div>
</body>
<style>
    body &#123;
        display: flex;
        flex-direction: row;
        
        font-weight: bold;
    &#125;

    div &#123;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        width: 500px;
        height: 500px;
        margin: 20px;
        border: 1px solid black;
    &#125;

    .box1 &#123;
        
        background: radial-gradient(circle at center, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%),
                    radial-gradient(circle at top 0 left 0, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%),
                    radial-gradient(circle at top 0 left 100px, transparent 0%, transparent 30%, black 30%, black 31%,  transparent 31%, transparent 100%);
    &#125;
</style>
</html>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            