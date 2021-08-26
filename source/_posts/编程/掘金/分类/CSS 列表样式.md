
---
title: 'CSS 列表样式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9ed355597e4473dbdfe444ee131ed78~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:20:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9ed355597e4473dbdfe444ee131ed78~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 HTML 中，有序列表和无序列表的符号是用 type 属性来定义的，为了遵循结构和样式分离的原则，应该在 CSS 中定义列表样式。</p>
<h2 data-id="heading-0">一、列表项符号 list-style-type</h2>
<h3 data-id="heading-1">1、定义列表项符号</h3>
<p>列表项的符号针对 ol 或者 ul 元素，而不是 li 元素，在 ol 中，列表项符号的取值如下：</p>





























<table><thead><tr><th>属性值</th><th>说明</th></tr></thead><tbody><tr><td>decimal</td><td>阿拉伯数字 1、2、3……（默认）</td></tr><tr><td>lower-roman</td><td>小写罗马数字 i、ii、iii……</td></tr><tr><td>upper-roman</td><td>大写罗马数字 I、II、III……</td></tr><tr><td>lower-alpha</td><td>小写英文字母 a、b、c……</td></tr><tr><td>upper-alpha</td><td>大写英文字母 A、B、C……</td></tr></tbody></table>
<p>在 ul 中，列表项符号的取值如下：</p>





















<table><thead><tr><th>属性值</th><th>说明</th></tr></thead><tbody><tr><td>disc</td><td>实心圆（默认值）</td></tr><tr><td>circle</td><td>空心圆</td></tr><tr><td>square</td><td>正方形</td></tr></tbody></table>
<p>有如下示例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-tag">ol</span>&#123;
                <span class="hljs-attribute">list-style-type</span>: upper-roman;
            &#125;
            <span class="hljs-selector-tag">ul</span>&#123;
                <span class="hljs-attribute">list-style-type</span>: circle;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>有序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ol</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>无序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中显示为：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9ed355597e4473dbdfe444ee131ed78~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2、去除列表项的符号</h3>
<p>有时候并不想使用列表项的符号，可以使用 <code>list-style-type:none</code> 来去除列表项的符号，示例如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-tag">ol</span>,<span class="hljs-selector-tag">ul</span>&#123;
                <span class="hljs-attribute">list-style-type</span>: none;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>有序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ol</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>无序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd408ba8df63408d9e18008814c39e93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">二、列表项图片 list-style-image</h2>
<p>可以将列表项使用图片来代替，使网站更加美观，有如下示例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"个人主页，HTML学习笔记"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"Like_Frost"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"学习示例"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"版权所有，转载前请联系"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-tag">ol</span>,<span class="hljs-selector-tag">ul</span>&#123;
                <span class="hljs-attribute">list-style-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"cat.svg"</span>)
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>有序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ol</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>无序列表<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>列表项3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中效果为：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff3013fb3534471da4e0ba5cd927b8fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于列表项的符号，更多情况下是使用 iconfont 图标来实现，推荐一个好用的图标库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iconfont.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iconfont.cn/" ref="nofollow noopener noreferrer">www.iconfont.cn/</a></p></div>  
</div>
            