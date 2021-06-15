
---
title: '5分钟实现炫彩流光按钮 html+css'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3de8116b0f4478c8a135d486d16e455~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 19:59:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3de8116b0f4478c8a135d486d16e455~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天</p>
<h2 data-id="heading-0">话不多，先上效果：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3de8116b0f4478c8a135d486d16e455~tplv-k3u1fbpfcp-zoom-1.image" alt="1" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">简介：</h2>
<p>用基础css做一个有一点炫酷的流光按钮，不止按钮，只要是盒子就行。</p>
<h2 data-id="heading-2">具体步骤：</h2>
<p><strong>1.先定义一个盒子当做按钮，如我就用a标签：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"guang"</span>></span>button<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.先给a标签写基础的样式，比如长宽等等...：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"> .guang&#123;
        position: relative;
        display: inline-block;
        width: 220px;
        height: 80px;
        color: rgb(255, 255, 255);
        line-height: 80px;
        font-size: 35px;
        font-family: sans-serif;
        text-decoration: none;
        text-transform: uppercase;
        text-align: center;
        border-radius: 30px;
        background: linear-gradient(90deg,rgb(39, 122, 218),rgb(74, 230, 121),rgb(201, 214, 13),rgb(226, 20, 233),rgb(16, 172, 219));
        background-size: 400%;
        z-index: 1;
        text-shadow: 0 0 5px white,
                     0 0 5px white;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：其中一些属性用处：</strong>
text-transform: uppercase;  全部换成大写字母。
background: linear-gradient(.......);  <strong>线性</strong>颜色渐变，可以改成自己要的颜色。
text-shadow: 0 0 5px white,
0 0 5px white;
写两行是为了让字体更亮。</p>
<p><strong>3.鼠标经过盒子产生流光的动画：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"> .guang:hover&#123;
        animation: move 5s linear alternate infinite;
    &#125;
    @keyframes move&#123;
        0%&#123;
           background-position: 0%;
        &#125;
        100%&#123;
            background-position: 100%;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.定义盒子周围的光晕阴影：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"> .guang::before&#123;
        content: '';
        position: absolute;
        top: -10px;
        left: -10px;
        width: 240px;
        height: 100px;
        background: linear-gradient(90deg,rgb(39, 122, 218),rgb(74, 230, 121),rgb(243, 169, 10),rgb(226, 20, 233),rgb(16, 172, 219));
        background-size: 400%;
        opacity: 0;
        z-index: -1;
        border-radius: 45px;
        transition: 0.6s;
       
    &#125;
  .guang:hover::before&#123;
        filter: blur(15px);
        opacity: 1;
        animation: move 8s linear alternate infinite;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：其中一些属性用处：</strong>
filter: blur 滤镜，就是让其模糊</p>
<h2 data-id="heading-3">完整代码：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    *&#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">box-sizing</span>: border-box;
    &#125;
    <span class="hljs-selector-tag">body</span>&#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">background-color</span>: black;
    &#125;
    <span class="hljs-selector-class">.guang</span>&#123;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">display</span>: inline-block;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">220px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>);
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">35px</span>;
        <span class="hljs-attribute">font-family</span>: sans-serif;
        <span class="hljs-attribute">text-decoration</span>: none;
        <span class="hljs-attribute">text-transform</span>: uppercase;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">90deg</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">39</span>, <span class="hljs-number">122</span>, <span class="hljs-number">218</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">74</span>, <span class="hljs-number">230</span>, <span class="hljs-number">121</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">201</span>, <span class="hljs-number">214</span>, <span class="hljs-number">13</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">226</span>, <span class="hljs-number">20</span>, <span class="hljs-number">233</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">16</span>, <span class="hljs-number">172</span>, <span class="hljs-number">219</span>));
        <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span>;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> white,
                     <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> white;
    &#125;
    <span class="hljs-selector-class">.guang</span><span class="hljs-selector-pseudo">:hover</span>&#123;
        <span class="hljs-attribute">animation</span>: move <span class="hljs-number">5s</span> linear alternate infinite;
    &#125;
    <span class="hljs-keyword">@keyframes</span> move&#123;
        <span class="hljs-number">0%</span>&#123;
           <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0%</span>;
        &#125;
        <span class="hljs-number">100%</span>&#123;
            <span class="hljs-attribute">background-position</span>: <span class="hljs-number">100%</span>;
        &#125;
    &#125;
    <span class="hljs-selector-class">.guang</span><span class="hljs-selector-pseudo">::before</span>&#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: -<span class="hljs-number">10px</span>;
        <span class="hljs-attribute">left</span>: -<span class="hljs-number">10px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">240px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">90deg</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">39</span>, <span class="hljs-number">122</span>, <span class="hljs-number">218</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">74</span>, <span class="hljs-number">230</span>, <span class="hljs-number">121</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">243</span>, <span class="hljs-number">169</span>, <span class="hljs-number">10</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">226</span>, <span class="hljs-number">20</span>, <span class="hljs-number">233</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">16</span>, <span class="hljs-number">172</span>, <span class="hljs-number">219</span>));
        <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span>;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">45px</span>;
        <span class="hljs-attribute">transition</span>: <span class="hljs-number">0.6s</span>;
       
    &#125;
    <span class="hljs-selector-class">.guang</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::before</span>&#123;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">15px</span>);
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">animation</span>: move <span class="hljs-number">8s</span> linear alternate infinite;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"guang"</span>></span>button<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<p>哈哈~
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d7f688c128b43bbb5130fc9239a2702~tplv-k3u1fbpfcp-zoom-1.image" alt="1" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            