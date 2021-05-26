
---
title: '6分钟实现CSS炫光倒影按钮'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/250c7b7773394e8c9f8614e45d552b13~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 22:30:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/250c7b7773394e8c9f8614e45d552b13~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">话不多，先看效果：</h2>
<p><strong> 回归老本行，继续分享简单有趣的CSS创意特效，放松放松心情~</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/250c7b7773394e8c9f8614e45d552b13~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">实现过程（完整源码在最后）：</h2>
<p><strong>1 老样子，定义基本样式：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   *&#123;
             <span class="hljs-attr">margin</span>: <span class="hljs-number">0</span>;
            padding: <span class="hljs-number">0</span>;
            box-sizing: border-box;
            font-family: <span class="hljs-string">'fangsong'</span>;
        &#125;
        body&#123;
            <span class="hljs-attr">height</span>: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: rgb(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>font-family: 'fangsong'; 仿宋字体。
display: flex;
align-items: center;
justify-content: center; flex布局，让按钮在屏幕居中。</p>
<p><strong>2.定义基本标签：</strong></p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item1"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item2"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item3"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3个a标签就对应3个按钮，每个按钮里4个span就是环绕按钮的4条边。
且都有个公共的选择器 .item 和 只属于自己的选择器。</p>
<p><strong>3.定义每个按钮的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.item</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">text-transform</span>: uppercase;
            <span class="hljs-attribute">text-decoration</span>: none;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">35px</span>;
            <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">5px</span>;
            <span class="hljs-attribute">color</span>: aqua;
            <span class="hljs-attribute">overflow</span>: hidden;
            -webkit-box-reflect: below <span class="hljs-number">1px</span> <span class="hljs-built_in">linear-gradient</span>( transparent,<span class="hljs-built_in">rgba</span>(<span class="hljs-number">6</span>, <span class="hljs-number">133</span>, <span class="hljs-number">133</span>,<span class="hljs-number">0.3</span>));
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>text-align: center;文字对齐方式。
line-height: 80px; 字行高。
text-transform: uppercase; 字母为大写。
text-decoration: none; 去掉a标签默认下划线。
letter-spacing: 5px; 每个字符间的距离。
overflow: hidden;溢出隐藏。
-webkit-box-reflect: below 1px linear-gradient( transparent,rgba(6, 133, 133,0.3)); 这个属性能实现倒影效果。</p>
<p><strong>4. 鼠标经过按钮样式改变：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">background-color</span>: aqua;
            <span class="hljs-attribute">box-shadow</span>:<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> aqua,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">75px</span> aqua,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">155px</span> aqua;
            <span class="hljs-attribute">color</span>: black;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>box-shadow:0 0 5px aqua,
0 0 75px aqua,
0 0 155px aqua; 阴影，写多行可以叠加更亮。</p>
<p><strong>5.设置环绕按钮的4根线上面那条的样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>; 
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to left,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: shang <span class="hljs-number">1s</span> linear infinite;
        &#125;
        <span class="hljs-keyword">@keyframes</span> shang&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">left</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: absolute;
left: -100%;  定位在对应位置。
background-image: linear-gradient(to left,aqua ,transparent); 线性渐变颜色。
animation: shang 1s linear infinite; 动画属性，让它动起来。</p>
<p><strong>5.以此类推，设置环绕按钮的其它3根样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to top,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: you <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.25s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> you&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">top</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">top</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">right</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: xia <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.5s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> xia&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">right</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">right</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">4</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to bottom,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: zuo <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.75s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> zuo&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">bottom</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">bottom</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>animation-delay: 0.75s; 动画延迟执行。每条线对应延迟一段时间，形成时间差，形成环绕效果。</p>
<p><strong>6.给第一，第三个按钮设置其它颜色：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.item1</span>&#123;
            <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">100deg</span>);
        &#125;
        <span class="hljs-selector-class">.item3</span>&#123;
            <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">250deg</span>);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>filter: hue-rotate(100deg); 用色相旋转，这样不管背景还是阴影颜色都变了。</p>
<h2 data-id="heading-2">完整代码：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"zh-CN"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        *&#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">box-sizing</span>: border-box;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'fangsong'</span>;
        &#125;
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
            <span class="hljs-attribute">display</span>: flex;
            <span class="hljs-attribute">align-items</span>: center;
            <span class="hljs-attribute">justify-content</span>: center;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-selector-class">.item</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">text-transform</span>: uppercase;
            <span class="hljs-attribute">text-decoration</span>: none;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">35px</span>;
            <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">5px</span>;
            <span class="hljs-attribute">color</span>: aqua;
            <span class="hljs-attribute">overflow</span>: hidden;
            -webkit-box-reflect: below <span class="hljs-number">1px</span> <span class="hljs-built_in">linear-gradient</span>( transparent,<span class="hljs-built_in">rgba</span>(<span class="hljs-number">6</span>, <span class="hljs-number">133</span>, <span class="hljs-number">133</span>,<span class="hljs-number">0.3</span>));
        &#125;
        <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">background-color</span>: aqua;
            <span class="hljs-attribute">box-shadow</span>:<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> aqua,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">75px</span> aqua,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">155px</span> aqua;
            <span class="hljs-attribute">color</span>: black;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>; 
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to left,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: shang <span class="hljs-number">1s</span> linear infinite;
        &#125;
        <span class="hljs-keyword">@keyframes</span> shang&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">left</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">left</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to top,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: you <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.25s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> you&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">top</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">top</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">right</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to right,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: xia <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.5s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> xia&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">right</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">right</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">4</span>)&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">100%</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">3px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to bottom,aqua ,transparent);
            <span class="hljs-attribute">animation</span>: zuo <span class="hljs-number">1s</span> linear infinite;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.75s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> zuo&#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">bottom</span>:-<span class="hljs-number">100%</span>;
            &#125;
            <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">bottom</span>:<span class="hljs-number">100%</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.item1</span>&#123;
            <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">100deg</span>);
        &#125;
        <span class="hljs-selector-class">.item3</span>&#123;
            <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">250deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
     
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item1"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item2"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item item3"</span>></span>
            aurora
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
 
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4602d128535d4481b21ce828b3a58f65~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>其它文章：</strong>
<a href="https://blog.csdn.net/luo1831251387/article/details/116452424" target="_blank" rel="nofollow noopener noreferrer">文字烟雾效果 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/115534417" target="_blank" rel="nofollow noopener noreferrer">环绕倒影加载特效 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113657124" target="_blank" rel="nofollow noopener noreferrer">气泡浮动背景特效 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113436552" target="_blank" rel="nofollow noopener noreferrer">简约时钟特效 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113360844" target="_blank" rel="nofollow noopener noreferrer">赛博朋克风格按钮 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/114393724" target="_blank" rel="nofollow noopener noreferrer">仿网易云官网轮播图 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111714413" target="_blank" rel="nofollow noopener noreferrer">水波加载动画 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111601962" target="_blank" rel="nofollow noopener noreferrer">导航栏滚动渐变效果 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111398881?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">书本翻页 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111032274?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">3D立体相册 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/114338506" target="_blank" rel="nofollow noopener noreferrer">霓虹灯绘画板效果 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111320280" target="_blank" rel="nofollow noopener noreferrer">记一些css属性总结（一）</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113179630" target="_blank" rel="nofollow noopener noreferrer">Sass总结笔记 </a>
......等等
<a href="https://blog.csdn.net/luo1831251387?spm=1000.2115.3001.5343" target="_blank" rel="nofollow noopener noreferrer">进我主页看更多~</a></p></div>  
</div>
            