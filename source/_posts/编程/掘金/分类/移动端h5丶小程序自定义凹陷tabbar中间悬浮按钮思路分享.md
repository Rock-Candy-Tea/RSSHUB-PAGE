
---
title: '移动端h5丶小程序自定义凹陷tabbar中间悬浮按钮思路分享'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4ae1c0303fc4ceea839312a8b230fe1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 03:14:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4ae1c0303fc4ceea839312a8b230fe1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h2 data-id="heading-0">最近要开发一个微信小程序，然后看到了别的小程序的tabbar长这个样子👇</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4ae1c0303fc4ceea839312a8b230fe1~tplv-k3u1fbpfcp-watermark.image" alt="1627896129(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我就也想做这样凹陷的的<strong>tabbar</strong> (其实是领导叫的) ，那他这个凹陷的效果是怎么实现的呢，网上搜了很多也没找到实现的思路，后面自己研究后实现了，分享思路出来给需要的朋友。</p>
<p>我最后自己实现出来的效果是这样的👇</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1038fb1d09354719a21fce68ab19b981~tplv-k3u1fbpfcp-watermark.image" alt="1627899416(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">思路一：用 png 图片实现</h2>
<p>很简单，叫你们的UI设计师给你画一个类似这种的png图片👇</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ac30c3591a44d0a98f642e2610db217~tplv-k3u1fbpfcp-watermark.image" alt="tabbar.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>一定要png，凹陷的地方一定要透明。</p>
</blockquote>
<p>然后其他的就自己布局就好啦</p>
<h2 data-id="heading-2">思路二：用css的阴影属性来实现</h2>
<p>就这样说的话可能有些朋友不太明白，所以我将用代码写出来👇</p>
<h3 data-id="heading-3">首先看一下html和css代码结构</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex custom-tabbar"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex-1 h100 bg-white left-tabbar-wrapper"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h100 transparent-circle-wrapper"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"transparent-circle"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex-1 h100 bg-white right-tabbar-wrapper"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义css</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bg-white</span>&#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#FFFFFF</span>;
&#125;
<span class="hljs-selector-class">.u-flex-1</span>&#123;
    <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-class">.h100</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-class">.u-flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里的view你可以当作是html的div，小程序里面的是view，这里用了几个自定义的className。</p>
</blockquote>
<p>根据html结构我们可以看到我们是分成三个view来实现的，父级flex布局把他们排成一列，然后中间是一个透明的圆，两边就是白色背景的块级元素</p>
<h3 data-id="heading-4">那么重要的css来了，先固定在底部先 ( 我这里用的是 scss )</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.custom-tabbar</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-selector-class">.left-tabbar-wrapper</span> &#123;
<span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">21px</span>;
&#125;
    <span class="hljs-selector-class">.right-tabbar-wrapper</span> &#123;
        <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">21px</span>;
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两边的块级元素我们把对应的顶部给个圆角，然后效果就是这样👇</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed94648675974e22aa3e93a62f00a4d2~tplv-k3u1fbpfcp-watermark.image" alt="1627899708(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>中间的也是块级元素，设定了100px的宽度，并没有给背景颜色，所以中间是透明的</p>
<h3 data-id="heading-5">给中间的那个view设置相对定位，圆设置绝对定位，经典的子绝父相</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.transparent-circle-wrapper</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-selector-class">.transparent-circle</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">left</span>: -<span class="hljs-number">3px</span>;
        <span class="hljs-attribute">top</span>: -<span class="hljs-number">50px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">106px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里透明的圆top:-50px是为了悬浮，相信大家都能明白，其他的我就不过多阐述了，下面看核心实现的css属性</p>
<h3 data-id="heading-6">给圆设置一个<strong>白色</strong>阴影，把阴影扩大</h3>
<p>修改第三个参数，比如我这里设置100px</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">#ffffff</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改后效果是这样👇</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c22508d19ed4da2b0fb69ff4bc78684~tplv-k3u1fbpfcp-watermark.image" alt="1627900846(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">再修改圆的阴影偏移</h3>
<p>修改第二个参数，让阴影往下偏移</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">#ffffff</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改为100px的时候我们看到效果是这样的👇</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d34a8dd051740d99973156836c445f8~tplv-k3u1fbpfcp-watermark.image" alt="1627901087(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这里我估计你们应该懂了吧，最后我再修改偏移量为156px, 最后实现了，当然你们也许需要自己调节，毕竟宽高什么的跟我的不一样。大功告成👇</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1038fb1d09354719a21fce68ab19b981~tplv-k3u1fbpfcp-watermark.image" alt="1627899416(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">完整代码👇</h3>
<p>html</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex custom-tabbar"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex-1 h100 bg-white left-tabbar-wrapper"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h100 transparent-circle-wrapper"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"transparent-circle"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"u-flex-1 h100 bg-white right-tabbar-wrapper"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.bg-white</span>&#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#FFFFFF</span>;
&#125;
<span class="hljs-selector-class">.u-flex-1</span>&#123;
    <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-class">.h100</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-class">.u-flex</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
&#125;
<span class="hljs-selector-class">.custom-tabbar</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-selector-class">.left-tabbar-wrapper</span> &#123;
        <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">21px</span>;
    &#125;
    <span class="hljs-selector-class">.right-tabbar-wrapper</span> &#123;
        <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">21px</span>;
    &#125;
    <span class="hljs-selector-class">.transparent-circle-wrapper</span> &#123;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-selector-class">.transparent-circle</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: -<span class="hljs-number">3px</span>;
            <span class="hljs-attribute">top</span>: -<span class="hljs-number">50px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">106px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">156px</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">#ffffff</span>;
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p>这里两种思路都可以实现，第二种的话需要自行调节阴影编译、圆的宽高、left、top值等，来达到想要的效果，当然如果阴影超出外面了可以在父级给个overflow:hidden，我这里不需要。</p>
<blockquote>
<p>以上就是我的分享，希望能帮助到大家😀。</p>
</blockquote></div>  
</div>
            