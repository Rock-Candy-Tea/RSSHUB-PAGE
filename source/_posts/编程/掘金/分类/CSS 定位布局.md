
---
title: 'CSS 定位布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a66b3cd7a6142efbc8110db9bfd0628~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:55:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a66b3cd7a6142efbc8110db9bfd0628~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>虽然浮动布局比较灵活，但是不容易控制，定位布局的出现，使得用户精准定位页面中的元素成为可能，页面布局也随心所欲。但定位布局缺乏灵活性，给空间大小和位置不确定的版面布局带来困惑，所以在实际开发中，要灵活使用这两种布局。</p>
<p>定位布局使用 position 属性来实现，属性值如下：</p>

























<table><thead><tr><th>属性值</th><th>说明</th></tr></thead><tbody><tr><td>fixed</td><td>固定定位</td></tr><tr><td>relative</td><td>相对定位</td></tr><tr><td>absolute</td><td>绝对定位</td></tr><tr><td>static</td><td>静态定位（默认值）</td></tr></tbody></table>
<h2 data-id="heading-0">一、固定定位</h2>
<p>固定定位的实现方式：<code>position:fixed;</code>，固定的元素不会随着滚动条的拖动而改变位置，要结合 top、bottom、left、right 属性一起使用，用来规定元素相对于浏览器的位置，这四个属性一般只用到两个，参考值是浏览器的四条边。</p>
<p>有如下示例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-class">.div1</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">2000px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">141</span>, <span class="hljs-number">212</span>, <span class="hljs-number">120</span>);
                <span class="hljs-attribute">display</span>: table-cell;
                <span class="hljs-attribute">vertical-align</span>: middle;
            &#125;
            <span class="hljs-selector-class">.div2</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">position</span>: fixed;
                <span class="hljs-attribute">background-color</span>: darkseagreen;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">300px</span>;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div1"</span>></span>没有设置定位的元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div2"</span>></span>设置了定位的元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>右边 div 在滚动条滚动时位置不变，左边变化：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a66b3cd7a6142efbc8110db9bfd0628~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3137c3b0f84e13a9965a801f78f1e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>固定定位最常见的一个应用：回顶部按钮。</p>
<h2 data-id="heading-1">二、相对定位</h2>
<p>相对定位的实现方式：<code>position:relative;</code>，相对定位是指元素的位置相对于原始位置计算而来的，也要搭配 top、bottom、left、right 四个属性使用，通常使用两个即可。</p>
<p><strong>固定定位是相对于浏览器的位置，绝对定位是相对于元素本身的位置。</strong></p>
<p>当两个 div 均没有设置定位时：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f77511e6af464f06b30228cf1e178a00~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，使第一个 div 不变，为第二个 div 设置相对定位：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-class">.div1</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">141</span>, <span class="hljs-number">212</span>, <span class="hljs-number">120</span>);
            &#125;
            <span class="hljs-selector-class">.div2</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: darkseagreen;
                <span class="hljs-attribute">position</span>: relative;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">20px</span>;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div1"</span>></span>div1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div2"</span>></span>div2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，元素相对于它原来的位置偏移了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84e2e4aa3e7c4cb5968dcd117f3f3bf0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再加一个不设置定位的 div3：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-class">.div1</span>, <span class="hljs-selector-class">.div3</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">141</span>, <span class="hljs-number">212</span>, <span class="hljs-number">120</span>);
            &#125;
            <span class="hljs-selector-class">.div2</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: darkseagreen;
                <span class="hljs-attribute">position</span>: relative;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">20px</span>;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div1"</span>></span>div1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div2"</span>></span>div2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div3"</span>></span>div3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09302a44e0d74b3aa51333ca3c0896f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可见，虽然第二个 div 较原来的位置偏移了，但它仍然占据未偏移时的位置，并不影响文档流，其后的元素仍按原始文档流排列。</p>
<h2 data-id="heading-2">三、绝对定位</h2>
<p>使用方式：<code>position:absolute;</code> ，当使用绝对定位时，此元素脱离文档流，其他元素会当这个元素不存在。此属性也要结合 top、bottom、left、right 属性一起使用，通常只需要两个，参考对象是浏览器的四条边。</p>
<p>有如下示例，div2 为绝对定位：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-class">.div1</span>, <span class="hljs-selector-class">.div3</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">141</span>, <span class="hljs-number">212</span>, <span class="hljs-number">120</span>);
                <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
            &#125;
            <span class="hljs-selector-class">.div2</span>&#123;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
                <span class="hljs-attribute">background-color</span>: azure;
                <span class="hljs-attribute">position</span>: absolute;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">50px</span>;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">50px</span>;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div1"</span>></span>div1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div2"</span>></span>div2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div3"</span>></span>div3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d19962878f74bb3a166cba8418eda3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可见，绝对定位的 div2 已经脱离文档流，不影响其他元素的排列。</p>
<h2 data-id="heading-3">四、静态定位</h2>
<p>在默认情况下，元素是静态定位的，即正常出现在标准文档流中，对其的 top、bottom、left、right 不生效。</p></div>  
</div>
            