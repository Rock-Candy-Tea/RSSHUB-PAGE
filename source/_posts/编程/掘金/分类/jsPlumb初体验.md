
---
title: 'jsPlumb初体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c42e18104284d8ab246c246b8ebe135~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 04:23:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c42e18104284d8ab246c246b8ebe135~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h2 data-id="heading-0">一、什么是jsPlumb</h2>
<p>jsPlumb是一个功能强大，可以用来绘制DOM节点间连线的库，它提供了非常多的定制功能来设定DOM节点间的连线，你可以利用它来完成各种各样的流程图绘制。</p>
<h2 data-id="heading-1">二、安装</h2>
<p>jsPlumb分为免费（Community Edition）和付费（Toolkit Edition）两个版本，付费版本会有更多工鞥呢，我们只需要用免费版就可以了，这里我们使用的版本号是v2.15.6。有以下两种方式来引入jsPlumb</p>
<pre><code class="copyable">yarn add jsplumb 
import &#123; jsPlumb &#125; from 'jsplumb'; // yarn安装

https://cdn.bootcss.com/jsPlumb/2.15.3/js/jsplumb.min.js // cdn地址
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无论是哪种方式引入，最终我们都会得到一个JsPlumb对象。</p>
<h2 data-id="heading-2">三、名词解释</h2>
<ul>
<li>Source:连线的起始位置</li>
<li>Target:连线的结束位置</li>
<li>Endpoint:DOM节点上可以拖拽出连线的位置</li>
<li>Anchor:连线末端的位置</li>
<li>Connector：DOM节点间的连线</li>
<li>Overlay：连线相关的样式、信息等</li>
</ul>
<h2 data-id="heading-3">四、初始化&配置</h2>
<p>jsPlumb本身有自己的一套认配置，但是官方建议我们不要去修改，如果我们需要修改配置，可以先获取一个实例，再去做更改。后边我们所有的代码，也都基于这实例<strong>instance</strong>去做演示。这里注意：jsPlumb必须等到DOM初始化后才可以使用，所以我们调用<strong>ready</strong>方法来进行初始化。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> instance = jsPlumb.getInstance(); <span class="hljs-comment">// jsplumb实例</span>
instance.ready(<span class="hljs-function">()=></span> &#123;
    <span class="hljs-comment">//some code</span>
&#125;);<span class="hljs-comment">//</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<strong>importDefaults</strong>方法来更改默认配置，这里只列出了一部分。</p>
<pre><code class="hljs language-js copyable" lang="js">instance.importDefaults(&#123;
    <span class="hljs-attr">Container</span>: <span class="hljs-string">'editArea'</span>, <span class="hljs-comment">// 容器id</span>
    <span class="hljs-attr">PaintStyle</span>: &#123;
        <span class="hljs-attr">stroke</span>: <span class="hljs-string">'#E0E3E7'</span>, <span class="hljs-comment">// 线的颜色</span>
        <span class="hljs-attr">strokeWidth</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 线的粗细，值越大线越粗</span>
        <span class="hljs-attr">outlineStroke</span>: <span class="hljs-string">'transparent'</span>, <span class="hljs-comment">// 设置外边线的颜色，默认设置透明，这样别人就看不见了，点击线的时候可以不用精确点击</span>
        <span class="hljs-attr">outlineWidth</span>: <span class="hljs-number">10</span> <span class="hljs-comment">// 线外边的宽，值越大，线的点击范围越大</span>
    &#125;,
    <span class="hljs-attr">DeleteEndpointsOnDetach</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//删除连线同时是否删除端点</span>
    <span class="hljs-attr">HoverPaintStyle</span>: &#123;
        <span class="hljs-attr">stroke</span>: <span class="hljs-string">'#b0b2b5'</span>,
        <span class="hljs-attr">strokeWidth</span>: <span class="hljs-number">1</span>
    &#125;, <span class="hljs-comment">// 鼠标滑过线的样式</span>
    <span class="hljs-attr">Overlays</span>: [
      [
        <span class="hljs-string">'Arrow'</span>, <span class="hljs-comment">// 箭头样式</span>
            &#123;
                <span class="hljs-attr">width</span>: <span class="hljs-number">10</span>, <span class="hljs-comment">// 箭头尾部的宽度</span>
                <span class="hljs-attr">length</span>: <span class="hljs-number">8</span>, <span class="hljs-comment">// 从箭头的尾部到头部的距离</span>
                <span class="hljs-attr">location</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 位置，建议使用0～1之间</span>
                <span class="hljs-attr">direction</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 方向，默认值为1（表示向前），可选-1（表示向后）</span>
                <span class="hljs-attr">foldback</span>: <span class="hljs-number">0.623</span> <span class="hljs-comment">// 折回，也就是尾翼的角度，默认0.623，当为1时，为正三角</span>
        &#125;
      ],
      [
        <span class="hljs-string">'Label'</span>, <span class="hljs-comment">//条件样式</span>
            &#123;
                <span class="hljs-attr">label</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">location</span>: <span class="hljs-number">0.4</span>,
                <span class="hljs-attr">cssClass</span>: <span class="hljs-string">'aLabel'</span>
        &#125;
      ]
    ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">五、实战演练</h2>
<p>接下来，我们通过一些例子，来了解jsPlumb相关的功能</p>
<h4 data-id="heading-5">连接接两个Div</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"item1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"item2"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">instance.ready(<span class="hljs-function">() =></span> &#123;
  instance.connect(&#123;
    <span class="hljs-attr">source</span>: <span class="hljs-string">'item1'</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'item2'</span>,
    <span class="hljs-attr">endpoint</span>: <span class="hljs-string">'Dot'</span>
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图，几行代码，我们便得到了相连的两个div</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c42e18104284d8ab246c246b8ebe135~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">改变连线的样式</h4>
<p>jsPlumb提供了三种连线的形状可供选择，分别是Bezier（默认贝塞尔曲线）、Straight（直线）、Flowchart（流程图）、StateMachine（状态机）。我们通过<strong>connector</strong>属性来配置连线样式：</p>
<pre><code class="hljs language-js copyable" lang="js">instance.ready(<span class="hljs-function">() =></span> &#123;
  instance.connect(&#123;
    <span class="hljs-attr">source</span>: <span class="hljs-string">'item1'</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'item2'</span>,
    <span class="hljs-attr">endpoint</span>: <span class="hljs-string">'Dot'</span>
    <span class="hljs-attr">connector</span>: <span class="hljs-string">'Flowchart'</span>
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/523dd27e2cca4ef897e252f752b213c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67cca387e06d43f2b06915085889c1ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/189eac56983743a2b5c467491224be5a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">改变端点的样式</h4>
<p>我们发现，上边的几张图里，连线的端点都是底部的圆点。jsPlumb提供了很多参数，可以让我们来修改端点的样式，这里列出一部分看下效果：</p>
<pre><code class="hljs language-js copyable" lang="js">instance.ready(<span class="hljs-function">() =></span> &#123;
  instance.connect(&#123;
    <span class="hljs-attr">source</span>: <span class="hljs-string">'item1'</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'item2'</span>,
    <span class="hljs-attr">endpoint</span>: <span class="hljs-string">'Rect'</span>,<span class="hljs-comment">//端点的形状 Dot（默认圆点）、Rectangle（矩形）、Blank（空）</span>
    <span class="hljs-attr">connector</span>: <span class="hljs-string">'Straight'</span>,
    <span class="hljs-attr">anchors</span>: [<span class="hljs-string">'Right'</span>, <span class="hljs-string">'Left'</span>],<span class="hljs-comment">//分别对应source和target的端点位置,可选值Left、Right、Top、Bottom</span>
    <span class="hljs-attr">endpointStyle</span>: &#123;
      <span class="hljs-attr">fill</span>: <span class="hljs-string">'#1879ff'</span>,<span class="hljs-comment">//端点外圈颜色</span>
      <span class="hljs-attr">outlineStroke</span>: <span class="hljs-string">'#ff4400'</span><span class="hljs-comment">//端点填充颜色</span>
    &#125;
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ac87bee99f1496cba82799798b75cf4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">给连线加上方向&条件</h4>
<p>既然jsPlumb经常被用来绘制流程图，那么连线的方向和条件，当然是必不可少的了，下面我们通过<strong>overlay</strong>参数来给连线加上方向和条件：</p>
<pre><code class="hljs language-js copyable" lang="js">instance.ready(<span class="hljs-function">() =></span> &#123;
  instance.connect(&#123;
    <span class="hljs-attr">source</span>: <span class="hljs-string">'item1'</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'item2'</span>,
    <span class="hljs-attr">endpoint</span>: <span class="hljs-string">'Dot'</span>,
    <span class="hljs-attr">connector</span>: <span class="hljs-string">'Straight'</span>,
    <span class="hljs-attr">anchors</span>: [<span class="hljs-string">'Right'</span>, <span class="hljs-string">'Left'</span>],
    <span class="hljs-attr">overlays</span>: [
      [
        <span class="hljs-string">'Arrow'</span>,
        &#123;
          <span class="hljs-attr">width</span>: <span class="hljs-number">10</span>, <span class="hljs-comment">// 箭头尾部的宽度</span>
          <span class="hljs-attr">length</span>: <span class="hljs-number">8</span>, <span class="hljs-comment">// 从箭头的尾部到头部的距离</span>
          <span class="hljs-attr">location</span>: <span class="hljs-number">0.6</span>, <span class="hljs-comment">// 箭头位置，建议使用0～1之间</span>
          <span class="hljs-attr">direction</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 方向，默认值为1（表示向前），可选-1（表示向后）</span>
          <span class="hljs-attr">foldback</span>: <span class="hljs-number">0.623</span> <span class="hljs-comment">// 折回，也就是尾翼的角度，默认0.623，当为1时，为正三角</span>
        &#125;
      ],
      [
        <span class="hljs-string">'Label'</span>,
        &#123;
          <span class="hljs-attr">label</span>: <span class="hljs-string">'条件1'</span>,
          <span class="hljs-attr">location</span>: <span class="hljs-number">0.4</span>, <span class="hljs-comment">// label在连线上的位置，取0-1之间</span>
          <span class="hljs-attr">cssClass</span>: <span class="hljs-string">'aLabel'</span> <span class="hljs-comment">// 连线的类名，可以用来自定义样式</span>
        &#125;
      ]
    ]
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5eb67c423464c88a00e53e8cba45cdc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">设置节点可拖动</h4>
<p>jsPlumb提供了<strong>draggable</strong>方法，让我们可以把页面上的dom节点变得可以拖拽（这里注意，可拖拽的元素定位必须是<strong>absolute</strong>）</p>
<pre><code class="hljs language-js copyable" lang="js">instance.draggable(<span class="hljs-string">'item2'</span>, &#123;
    <span class="hljs-attr">containment</span>: <span class="hljs-string">'parent'</span>,<span class="hljs-comment">//拖拽元素的父级id</span>
    <span class="hljs-function"><span class="hljs-title">stop</span>(<span class="hljs-params">el</span>)</span> &#123;<span class="hljs-comment">//拖拽结束后的回调</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'拖拽结束: '</span>, el);
    &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56d56b5dd949448ea3217999083fb1bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">从元素上拖出一条连线</h4>
<p>上面我们描述了如何链接两个元素，接下来，我们来给已有的元素，增加一个端点，让它可以拖拽出一条连线
jsPlumb提供了两种方式来给元素增加端点，代码如下：</p>
<h5 data-id="heading-11">addEndpoint</h5>
<pre><code class="hljs language-js copyable" lang="js">instance.addEndpoint(<span class="hljs-string">'item1'</span>, &#123;
    <span class="hljs-attr">anchor</span>: <span class="hljs-string">'Top'</span>,
    <span class="hljs-attr">isSource</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">isTarget</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">maxConnections</span>: -<span class="hljs-number">1</span> <span class="hljs-comment">//最大的连线数量，-1为不限</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49a45abf7b1e4537a1dd7bc1283871c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-12">makeSource makeTarget</h5>
<pre><code class="hljs language-js copyable" lang="js">instance.makeSource(<span class="hljs-string">'item1'</span>, &#123;
    <span class="hljs-attr">anchor</span>: <span class="hljs-string">'Top'</span>,
    <span class="hljs-attr">isSource</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">isTarget</span>: <span class="hljs-literal">false</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d09962cb623a407ea8073aa974f60e38~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">总结</h3>
<p>文章里提及的功能仅仅是jsPlumb的一小部分，关于端点的自定义，事件绑定等等，在这里就不一一介绍了，大家可以参照官方文档(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.jsplumbtoolkit.com%2Ftoolkit%2Fcurrent%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.jsplumbtoolkit.com/toolkit/current/index.html" ref="nofollow noopener noreferrer">docs.jsplumbtoolkit.com/toolkit/cur…</a>) 去学习。</p></div>  
</div>
            