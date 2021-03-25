
---
title: 'fabric.js实现可视化签章以及遮罩打印的功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bedff2d79944f609285d764ed47d5e9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 18:47:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bedff2d79944f609285d764ed47d5e9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h1 data-id="heading-0">前言</h1>
<h2 data-id="heading-1">业务场景</h2>
<p>首先，是因为这样一个需求，我开始尝试使用<strong>fabric.js</strong></p>
<p>公司有个项目，是<strong>可信电子凭证可视化签章</strong>。</p>
<blockquote>
<p>支持在打开的PDF文件上能随意拖动一个图片到PDF文档的任意位置。能获取当前拖动的图片在PDF文档的x，y坐标。</p>
</blockquote>
<p>后来，又一次用到了fabric.js是<strong>档案管理平台的项目</strong>。</p>
<blockquote>
<p>文件在线预览的页面，需要增加一个遮罩打印的功能，就是在pdf文件上打上马赛克，遮罩一些内容。不通过安装插件，纯前端技术来解决。在PDF文件的预览区域上，按住鼠标左键然后拖着，可生成马赛克的遮罩打印区域。</p>
</blockquote>
<p><img alt="图片1.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bedff2d79944f609285d764ed47d5e9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="图片2.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b642a283f5b46198bac7f97898cc7be~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">了解一门新技术，直接看官网和相关文档。</h2>
<p>**fabricjs官网在此：**<a href="http://fabricjs.com/" target="_blank" rel="nofollow noopener noreferrer">fabricjs.com/</a></p>
<p>官网首页，写在这样一段话：</p>
<blockquote>
<p>Fabric.js is a powerful and simple Javascript HTML5 canvas library</p>
</blockquote>
<p><strong>Fabric.js是一个强大而简单的Javascript HTML5 Canvas库</strong></p>
<p>然后看了相关文档，了解到我们能通过使用它实现在canvas上创建，填充图形，给图形填充渐变颜色。组合图形（包括组合图形，图形文字，图片等）等一系列功能。</p>
<p>简单来说，我们可以通过使用Fabric从而以较为简单的方式，实现较为复杂的Canvas功能。</p>
<p><strong>知道和做到之间，有一条天然的鸿沟。</strong></p>
<p><strong>有时，人们了解到前人的经验踩过的坑，但是仍然不可避免的掉进这些坑里。自己掉进这些坑里，再爬出来，才最终学习到这些经验，最终避开这些坑。</strong></p>
<h2 data-id="heading-3">快速上手</h2>
<p>了解到其基础概览，和应用场景之后，准备快速上手。</p>
<p><strong>在vue项目中引入服务</strong></p>
<pre><code class="hljs language-js copyable" lang="js">npm install fabric
<span class="hljs-keyword">import</span> &#123; fabric &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'fabric'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先做了一个demo用来实现在pdf预览的区域上拖拽图片。</p>
<p>关于pdf文件预览，之前用的pdf.js基于html的pdf阅读器，从官网下载静态资源，放到项目的static静态资源文件夹里面。</p>
<p>使用pdf.js已经写好的viewer.html页面来预览。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span>/pdf/web/viewer.html?file=<span class="hljs-string">' + encodeURIComponent(pdf)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>使用iframe标签去显示。然后，封装成一个公共工作，在需要的地方，直接调用。</p>
<p>组件代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pdf"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-card pdf-viewer"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">iframe</span>
        <span class="hljs-attr">:src</span>=<span class="hljs-string">"'static/pdf/web/viewer.html?file=' + encodeURIComponent(pdf)"</span>
        <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span>
        <span class="hljs-attr">frameborder</span>=<span class="hljs-string">"0"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"PdfDetail"</span>,
  <span class="hljs-attr">components</span>: &#123;&#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">pdf</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">""</span>,
    &#125;,
    <span class="hljs-attr">height</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">560</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;&#125;,
  <span class="hljs-attr">computed</span>: &#123;&#125;,
  <span class="hljs-attr">methods</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
.wrapper &#123;
&#125;
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只是顺带说了一下pdf.js预览的方法，我并没有采用这种方法去实现pdf预览功能。</p>
<p>因为，不仅要预览，还需要将pdf预览区域转换成canvas画布，然后在画布上实现图片拖拽位置的功能，并获取坐标。</p>
<p>我采用的是vue-pdf组件</p>
<p>GitHub地址：</p>
<p><a href="https://github.com/FranckFreiburger/vue-pdf#readme" target="_blank" rel="nofollow noopener noreferrer">github.com/FranckFreib…</a></p>
<pre><code class="hljs language-js copyable" lang="js">npm install --save vue-pdf
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">pdf</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./static/relativity.pdf"</span>></span><span class="hljs-tag"></<span class="hljs-name">pdf</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> pdf <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-pdf'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    pdf
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">核心代码</h1>
<p><strong>以下是demo的核心代码</strong></p>
<h2 data-id="heading-5">基础方法</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化画布对象</span>
<span class="hljs-keyword">new</span> fabric.Canvas(<span class="hljs-string">'canvas'</span>)
<span class="hljs-comment">//赋予一个变量，并且添加了双击事件，通过双击事件删除canvas画布上添加的内容</span>
<span class="hljs-built_in">this</span>.canvas = <span class="hljs-keyword">new</span> fabric.Canvas(<span class="hljs-string">'canvas'</span>)
<span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">'mouse:dblclick'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> items = <span class="hljs-built_in">this</span>.canvas.getObjects()
    items = items.filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.width > <span class="hljs-number">1</span> && item.height > <span class="hljs-number">1</span>)
    <span class="hljs-keyword">let</span> itemIdx = items.indexOf(e.target)
    <span class="hljs-built_in">this</span>.canvas.remove(<span class="hljs-built_in">this</span>.canvas.item(itemIdx));
    <span class="hljs-built_in">this</span>.canvas.renderAll();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在created钩子函数中，设置fabric的对象拖拽框</strong></p>
<pre><code class="hljs language-js copyable" lang="js">fabric.Object.prototype.setControlsVisibility(&#123;
      <span class="hljs-attr">bl</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 左下</span>
      <span class="hljs-attr">br</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 右下</span>
      <span class="hljs-attr">mb</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 下中</span>
      <span class="hljs-attr">ml</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 中左</span>
      <span class="hljs-attr">mr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 中右</span>
      <span class="hljs-attr">mt</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上中</span>
      <span class="hljs-attr">tl</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上左</span>
      <span class="hljs-attr">tr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上右</span>
      <span class="hljs-attr">mtr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 旋转控制键</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过图片路径，往画布上添加图片的方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> imgCoord = fabric.Image.fromURL(imgUrl, <span class="hljs-function">(<span class="hljs-params">img</span>) =></span> &#123;
    img.scale(<span class="hljs-number">1</span>).set(&#123;
        <span class="hljs-attr">crossOrigin</span>: <span class="hljs-string">'anonymous'</span>,
        <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>,
    &#125;)
<span class="hljs-built_in">this</span>.canvas.add(img).setActiveObject(img)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过图片对象，往画布上添加图片的方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> image= <span class="hljs-keyword">new</span> Image()
image.src = imgUrl
image.crossOrigin = <span class="hljs-string">'Anonymous'</span>;
image.onload = <span class="hljs-function">() =></span> &#123;
      fabric.Image.fromObject(imgl,<span class="hljs-function">(<span class="hljs-params">img</span>) =></span> &#123;
          img.scale(<span class="hljs-number">1</span>).set(&#123;
              <span class="hljs-attr">crossOrigin</span>: <span class="hljs-string">'anonymous'</span>,
              left,
              top,
              width,
              height,
              scaleX,
              scaleY,
          &#125;)
        <span class="hljs-built_in">this</span>.canvas.add(img).setActiveObject(img)
          <span class="hljs-built_in">this</span>.canvas.renderAll()
      &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>除了添加图片，还可以添加文本框，并且设置文字的颜色字体大小等等。</strong></p>
<p><strong>需要注意的是fontSize参数必须为Number类型。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> attributeObject = &#123;
    fill,
    fontFamily,
    fontWeight,
    textAlign,
    lineHeight,
    width,
    <span class="hljs-attr">splitByGrapheme</span>:<span class="hljs-literal">true</span>,
    height,
    <span class="hljs-attr">fontSize</span>:,
    originX: <span class="hljs-string">'center'</span>,
    <span class="hljs-attr">originY</span>: <span class="hljs-string">'center'</span>,
&#125;
<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> fabric.Textbox(text, attributeObject)
<span class="hljs-keyword">var</span> group = <span class="hljs-keyword">new</span> fabric.Group([obj], &#123;
    left,
    top,
&#125;)
<span class="hljs-built_in">this</span>.canvas.add(group)
<span class="hljs-built_in">this</span>.canvas.renderAll()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>为了最终拿到画布上所有对象的属性，以及坐标。我将这些属性和坐标，放到了一个json对象数组里面，保存起来。</li>
<li>图片和文字，除了能够拖拽，文字框还要求，能够改变字体颜色大小等等。</li>
<li>我加了字体颜色大小等属性的选择框，做了数据双向绑定。</li>
<li>每当json对象数组改变的时候，我就清空画布上的所有对象，然后从json对象数组里面拿到保存的属性和坐标，在画布上重新渲染。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//清空画布</span>
<span class="hljs-built_in">this</span>.canvas.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>获取画布上所有对象的坐标</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getImgPosition</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.canvas) <span class="hljs-keyword">return</span>
    <span class="hljs-built_in">this</span>.imgcoordinate = []
    <span class="hljs-keyword">let</span> items = <span class="hljs-built_in">this</span>.canvas.getObjects()
    items = items.filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.width > <span class="hljs-number">1</span> && item.height > <span class="hljs-number">1</span>)
    items.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> itemcoord = &#123;
            <span class="hljs-attr">floorIndex</span>: index,
            <span class="hljs-attr">tl</span>: &#123;
                <span class="hljs-attr">x</span>: item.aCoords.tl.x,
                <span class="hljs-attr">y</span>: item.aCoords.tl.y,
            &#125;,
            <span class="hljs-attr">tr</span>: &#123;
                <span class="hljs-attr">x</span>: item.aCoords.tr.x,
                <span class="hljs-attr">y</span>: item.aCoords.tr.y,
            &#125;,
            <span class="hljs-attr">bl</span>: &#123;
                <span class="hljs-attr">x</span>: item.aCoords.bl.x,
                <span class="hljs-attr">y</span>: item.aCoords.bl.y,
            &#125;,
            <span class="hljs-attr">br</span>: &#123;
                <span class="hljs-attr">x</span>: item.aCoords.br.x,
                <span class="hljs-attr">y</span>: item.aCoords.br.y,
            &#125;,
        &#125;
        <span class="hljs-built_in">this</span>.imgcoordinate.push(itemcoord)
    &#125;)
    <span class="hljs-built_in">this</span>.xycoordinate = <span class="hljs-built_in">this</span>.imgcoordinate.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.tl)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">添加马赛克</h2>
<p><strong>最后说一下，在canvas画布通过fabric.js添加马赛克的方法</strong></p>
<p>首先，初始化canvas画布对象的时候，增加鼠标事件监听的方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.canvas = <span class="hljs-keyword">new</span> fabric.Canvas(<span class="hljs-string">"canvas"</span>);
<span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:down"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  that.mousedown(e);
&#125;);
<span class="hljs-comment">//鼠标抬起事件</span>
<span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:up"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  that.mouseup(e);
&#125;);
<span class="hljs-comment">// 移动画布事件</span>
<span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:move"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  that.mousemove(e);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>鼠标点击mousedown事件时，记录下画布上点的位置，</li>
<li>鼠标移动后抬起mouseup事件时，记录下画布上点的最终位置，</li>
<li>这样，就可以算出鼠标拖拽的矩形的初始位置x，y坐标，以及矩形的宽高。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> mouse = <span class="hljs-built_in">this</span>.canvas.getPointer(e.e);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>接下来是最关键的，实现马赛克的方法，这个花了很长时间。</strong></p>
<ul>
<li>在初始化canvas画布对象的时候，需要通过getContext() 方法返回一个用于在画布上绘图的环境。</li>
<li>然后传一个图片路径imgUrl，通过drawImage画出底图。</li>
<li>具体生成马赛克的方法，在setColor中，是通过context对象的getImageData方法，获取图片数据。根据设置的马赛克方块大小，通过rgb的颜色设置，模糊掉底图上的图片，实现遮罩的效果。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Img = <span class="hljs-keyword">new</span> Image();
Img.src = imgUrl;
that.bgImage = Img;
Img.onload = <span class="hljs-function">() =></span> &#123;
    that.context.drawImage(Img, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    that.context.save();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>以下，是画矩形方框，并且填充马赛克，最终实现马赛克的方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">drawMake</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.canvas)<span class="hljs-keyword">return</span>;
  <span class="hljs-built_in">this</span>.context.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.canvas.width, <span class="hljs-built_in">this</span>.canvas.height);
  <span class="hljs-built_in">this</span>.context.drawImage(<span class="hljs-built_in">this</span>.bgImage, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
  <span class="hljs-built_in">this</span>.context.save();
  <span class="hljs-comment">// if (this.canvas) this.canvas.clear();</span>
  <span class="hljs-built_in">this</span>.makeList.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> &#123; beginX, beginY, w, h &#125; = item;
    <span class="hljs-built_in">this</span>.makeGrid(beginX, beginY, w, h);
  &#125;);
&#125;,
<span class="hljs-function"><span class="hljs-title">makeGrid</span>(<span class="hljs-params">beginX, beginY, rectWidth, rectHight</span>)</span> &#123;
  <span class="hljs-keyword">const</span> row = <span class="hljs-built_in">Math</span>.round(rectWidth / <span class="hljs-built_in">this</span>.squareEdgeLength) + <span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> column = <span class="hljs-built_in">Math</span>.round(rectHight / <span class="hljs-built_in">this</span>.squareEdgeLength) + <span class="hljs-number">1</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < row * column; i++) &#123;
    <span class="hljs-keyword">let</span> x = (i % row) * <span class="hljs-built_in">this</span>.squareEdgeLength + beginX;
    <span class="hljs-keyword">let</span> y = <span class="hljs-built_in">parseInt</span>(i / row) * <span class="hljs-built_in">this</span>.squareEdgeLength + beginY;
    <span class="hljs-built_in">this</span>.setColor(x, y);
  &#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">setColor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
  <span class="hljs-keyword">const</span> imgData = <span class="hljs-built_in">this</span>.context.getImageData(
    x,
    y,
    <span class="hljs-built_in">this</span>.squareEdgeLength,
    <span class="hljs-built_in">this</span>.squareEdgeLength
  ).data;
  <span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>,
    g = <span class="hljs-number">0</span>,
    b = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < imgData.length; i += <span class="hljs-number">4</span>) &#123;
    r += imgData[i];
    g += imgData[i + <span class="hljs-number">1</span>];
    b += imgData[i + <span class="hljs-number">2</span>];
  &#125;
  r = <span class="hljs-built_in">Math</span>.round(r / (imgData.length / <span class="hljs-number">4</span>));
  g = <span class="hljs-built_in">Math</span>.round(g / (imgData.length / <span class="hljs-number">4</span>));
  b = <span class="hljs-built_in">Math</span>.round(b / (imgData.length / <span class="hljs-number">4</span>));
  <span class="hljs-built_in">this</span>.drawRect(
    x,
    y,
    <span class="hljs-built_in">this</span>.squareEdgeLength,
    <span class="hljs-built_in">this</span>.squareEdgeLength,
    <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;g&#125;</span>, <span class="hljs-subst">$&#123;b&#125;</span>)`</span>,
    <span class="hljs-number">2</span>,
    <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;g&#125;</span>, <span class="hljs-subst">$&#123;b&#125;</span>)`</span>
  );
&#125;,
<span class="hljs-function"><span class="hljs-title">drawRect</span>(<span class="hljs-params">
  x,
  y,
  width,
  height,
  fillStyle,
  lineWidth,
  strokeStyle,
  globalAlpha
</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.context.beginPath();
    <span class="hljs-built_in">this</span>.context.rect(x, y, width, height);
    <span class="hljs-built_in">this</span>.context.lineWidth = lineWidth;
    <span class="hljs-built_in">this</span>.context.strokeStyle = strokeStyle;
    fillStyle && (<span class="hljs-built_in">this</span>.context.fillStyle = fillStyle);
    globalAlpha && (<span class="hljs-built_in">this</span>.context.globalAlpha = globalAlpha);
    <span class="hljs-built_in">this</span>.context.fill();
    <span class="hljs-built_in">this</span>.context.stroke();
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了fabric.js之外，为了实现遮罩打印的功能。还用到了 html2canvas 和 jsPDF的方法，在此不一一赘述，直接放出遮罩打印的组件完整代码。</p>
<p>实现了基本的业务需求之后，我还做了一些优化，譬如撤销和回退的功能。增加了属性设置弹框，通过拖动滑块选择马赛克方块的大小。通过driver.js实现帮助提示，操作指引。</p>
<p>这里，主要是记录了实现业务需求的解决思路，以及踩坑指南。</p>
<h1 data-id="heading-7">参考文章</h1>
<p><strong>参考了博客园的两篇文章：</strong></p>
<p>Canvas实用库Fabric.js使用手册</p>
<p><a href="https://www.cnblogs.com/aaron911/p/11949928.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/aaron911/p/…</a></p>
<p>Vue PDF文件预览vue-pdf</p>
<p><a href="https://www.cnblogs.com/steamed-twisted-roll/p/9648255.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/steamed-twi…</a></p>
<h1 data-id="heading-8">完整代码</h1>
<p><strong>遮罩打印的组件，完整代码</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"web-file"</span>></span>
      <span class="hljs-comment"><!-- 操作栏 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"operate-box nowrap flex justify-between"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex btn-list"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"page-btn"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span>
              <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changePdfPage(0)"</span>
              <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"currentPage == 1"</span>
              <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
            ></span>
              上一页
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"page-count"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"pageCount"</span>></span>&#123;&#123; currentPage &#125;&#125; / &#123;&#123; pageCount &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span>
              <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changePdfPage(1)"</span>
              <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"currentPage == pageCount"</span>
              <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
            ></span>
              下一页
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask-print"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"printPdf"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-printer"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span>
              打印
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask-setting"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span>
              <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"attributeEdit"</span>
              <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-setting"</span>
              <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
            ></span>
              遮罩属性设置
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask-add"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addMask"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span>添加遮罩<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"guide"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-info"</span>></span>
            帮助
          <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex btn-list"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask-back"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span>
              <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"stepBack"</span>
              <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-arrow-left"</span>
              <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
            ></span>
              回退
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask-clear"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-button</span>
              <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"clearClean"</span>
              <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-refresh-left"</span>
              <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
            ></span>
              撤销
            <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"goBack"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span>返回原文页<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!-- pdf翻页 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"pageCount && pageCount > 0"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pdf-box"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"pdf"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"baseMap"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showPdfBoxFlag"</span>></span>
        <span class="hljs-comment"><!-- pdf预览 --></span>
        <span class="hljs-tag"><<span class="hljs-name">pdf</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"pdf"</span>
          <span class="hljs-attr">:src</span>=<span class="hljs-string">"pdfsrc"</span>
          <span class="hljs-attr">:page</span>=<span class="hljs-string">"currentPage"</span>
          @<span class="hljs-attr">num-pages</span>=<span class="hljs-string">"pageCount = $event"</span>
          @<span class="hljs-attr">page-loaded</span>=<span class="hljs-string">"pageLoaded"</span>
          @<span class="hljs-attr">loaded</span>=<span class="hljs-string">"loadPdfHandler"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">pdf</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">class</span>=<span class="hljs-string">"manager_detail"</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"manager_detail"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123; 'accurate-choice': accurateChoiceFlag &#125;"</span>
        ></span>
          <span class="hljs-comment"><!-- 画布 --></span>
          <span class="hljs-tag"><<span class="hljs-name">canvas</span>
            <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>
            <span class="hljs-attr">ref</span>=<span class="hljs-string">"imgContent"</span>
            <span class="hljs-attr">:width</span>=<span class="hljs-string">"canvasObj.width"</span>
            <span class="hljs-attr">:height</span>=<span class="hljs-string">"canvasObj.height"</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">"
              position: absolute;
              width: 100%;
              height: 100%;
              left: 0;
              top: 0;
              cursor: crosshair;
            "</span>
          ></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">attribute-set</span>
      <span class="hljs-attr">:title</span>=<span class="hljs-string">"attribute.title"</span>
      @<span class="hljs-attr">close</span>=<span class="hljs-string">"attribute.show = false"</span>
      @<span class="hljs-attr">ok</span>=<span class="hljs-string">"setAttribute"</span>
      <span class="hljs-attr">v-if</span>=<span class="hljs-string">"attribute.show"</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"attribute"</span>
    /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fabric &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"fabric"</span>;
<span class="hljs-keyword">import</span> pdf <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-pdf"</span>;
<span class="hljs-keyword">import</span> html2canvas <span class="hljs-keyword">from</span> <span class="hljs-string">"html2canvas"</span>;
<span class="hljs-keyword">import</span> jsPDF <span class="hljs-keyword">from</span> <span class="hljs-string">"jspdf"</span>;
<span class="hljs-keyword">import</span> AttributeSet <span class="hljs-keyword">from</span> <span class="hljs-string">"./AttributeSet"</span>;
<span class="hljs-comment">// 引导页的功能</span>
<span class="hljs-keyword">import</span> Driver <span class="hljs-keyword">from</span> <span class="hljs-string">"driver.js"</span>; <span class="hljs-comment">// import driver.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"driver.js/dist/driver.min.css"</span>; <span class="hljs-comment">// import driver.js css</span>
<span class="hljs-keyword">import</span> steps <span class="hljs-keyword">from</span> <span class="hljs-string">"./steps"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    pdf,
    AttributeSet,
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">pdfsrc</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">""</span>,
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">canvas</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">context</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">bgImage</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">pageCount</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// pdf文件总页数</span>
      <span class="hljs-attr">currentPage</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">clickFlag</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">clickTimer</span>: -<span class="hljs-number">1</span>,
      <span class="hljs-attr">canvasObj</span>: &#123;
        <span class="hljs-attr">width</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-number">0</span>,
      &#125;,
      <span class="hljs-attr">json</span>: [],
      <span class="hljs-attr">basecoordinate</span>: [], <span class="hljs-comment">//基础坐标数组</span>
      <span class="hljs-attr">xycoordinate</span>: [], <span class="hljs-comment">// 左上角的坐标数组</span>
      <span class="hljs-attr">isMasic</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">squareEdgeLength</span>: <span class="hljs-number">20</span>, <span class="hljs-comment">//马赛克大小</span>
      <span class="hljs-attr">mouse</span>: &#123;
        <span class="hljs-attr">started</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
      &#125;,
      <span class="hljs-attr">accurateChoiceFlag</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">imgUrl</span>: <span class="hljs-string">""</span>,
      <span class="hljs-comment">// maskPic: "/static/img/fabric/mask.png",</span>
      <span class="hljs-attr">makeGridObject</span>: &#123;
        <span class="hljs-attr">beginX</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">beginY</span>: <span class="hljs-number">0</span>,
      &#125;,
      <span class="hljs-attr">makeList</span>: [],
      <span class="hljs-attr">fillColor</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">attribute</span>: &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">"属性设置"</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">style</span>: <span class="hljs-string">"1"</span>, <span class="hljs-comment">//0代表颜色，1代表马赛克</span>
      &#125;,
      <span class="hljs-attr">driver</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">showPdfBoxFlag</span>: <span class="hljs-literal">false</span>,
    &#125;;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    fabric.Object.prototype.setControlsVisibility(&#123;
      <span class="hljs-attr">bl</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 左下</span>
      <span class="hljs-attr">br</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 右下</span>
      <span class="hljs-attr">mb</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 下中</span>
      <span class="hljs-attr">ml</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 中左</span>
      <span class="hljs-attr">mr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 中右</span>
      <span class="hljs-attr">mt</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上中</span>
      <span class="hljs-attr">tl</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上左</span>
      <span class="hljs-attr">tr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 上右</span>
      <span class="hljs-attr">mtr</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 旋转控制键</span>
    &#125;);
    <span class="hljs-built_in">this</span>.showPdfBoxFlag = <span class="hljs-literal">true</span>;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.driver = <span class="hljs-keyword">new</span> Driver(&#123;
      <span class="hljs-comment">//此处为api</span>
      <span class="hljs-attr">animate</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.5</span>,
      <span class="hljs-attr">allowClose</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">doneBtnText</span>: <span class="hljs-string">"完成"</span>,
      <span class="hljs-attr">closeBtnText</span>: <span class="hljs-string">"关闭"</span>,
      <span class="hljs-attr">nextBtnText</span>: <span class="hljs-string">"下一步"</span>,
      <span class="hljs-attr">prevBtnText</span>: <span class="hljs-string">"上一步"</span>,
      <span class="hljs-attr">onReset</span>: <span class="hljs-function">(<span class="hljs-params">Element</span>) =></span> &#123;
        <span class="hljs-comment">//这里写逻辑回调</span>
      &#125;,
    &#125;);
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">goBack</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'back'</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">guide</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.driver.defineSteps(steps);
      <span class="hljs-built_in">this</span>.driver.start();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setAttribute</span>(<span class="hljs-params">item</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.attribute.style = item.styleValue;
      <span class="hljs-built_in">this</span>.fillColor = item.styleValue == <span class="hljs-string">"0"</span> ? <span class="hljs-string">"#fff"</span> : <span class="hljs-string">""</span>;
      <span class="hljs-built_in">this</span>.squareEdgeLength = item.maskValue;
      <span class="hljs-built_in">this</span>.drawMake();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">attributeEdit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.attribute.show = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">let</span> item = &#123;
          <span class="hljs-attr">styleValue</span>: <span class="hljs-built_in">this</span>.attribute.style,
          <span class="hljs-attr">maskValue</span>: <span class="hljs-built_in">this</span>.squareEdgeLength,
        &#125;;
        <span class="hljs-built_in">this</span>.$refs.attribute.initData(item);
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">addMask</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.mouse.started = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.initCanvasObjAndEvent();
      <span class="hljs-built_in">this</span>.accurateChoiceFlag = <span class="hljs-literal">true</span>;
    &#125;,
    <span class="hljs-comment">// 返回上一步</span>
    <span class="hljs-function"><span class="hljs-title">stepBack</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.makeList.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.makeList.splice(<span class="hljs-built_in">this</span>.makeList.length - <span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
        <span class="hljs-built_in">this</span>.drawMake();
      &#125;
    &#125;,
    <span class="hljs-comment">// 初始化画布对象</span>
    <span class="hljs-function"><span class="hljs-title">initCanvasObjAndEvent</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.canvas) &#123;
        <span class="hljs-built_in">this</span>.canvas = <span class="hljs-keyword">new</span> fabric.Canvas(<span class="hljs-string">"canvas"</span>);
        <span class="hljs-keyword">let</span> imgContent = <span class="hljs-built_in">this</span>.$refs.imgContent;
        <span class="hljs-built_in">this</span>.context = imgContent.getContext(<span class="hljs-string">"2d"</span>);
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">this</span>.pageTransformedIntoCanvas(<span class="hljs-function">(<span class="hljs-params">pageData, PDF</span>) =></span> &#123;
          <span class="hljs-keyword">let</span> Img = <span class="hljs-keyword">new</span> Image();
          Img.src = pageData;
          that.bgImage = Img;
          Img.onload = <span class="hljs-function">() =></span> &#123;
            that.context.drawImage(Img, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
            that.context.save();
          &#125;;
        &#125;);
        <span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:down"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          that.mousedown(e);
        &#125;);
        <span class="hljs-comment">//鼠标抬起事件</span>
        <span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:up"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          that.mouseup(e);
        &#125;);
        <span class="hljs-comment">// 移动画布事件</span>
        <span class="hljs-built_in">this</span>.canvas.on(<span class="hljs-string">"mouse:move"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          that.mousemove(e);
        &#125;);
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">pageLoaded</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.currentPage = e;
      <span class="hljs-built_in">this</span>.canvasObj.width = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"pdf"</span>).offsetWidth;
      <span class="hljs-built_in">this</span>.canvasObj.height = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"pdf"</span>).offsetHeight;
    &#125;,
    <span class="hljs-comment">// pdf加载时</span>
    <span class="hljs-function"><span class="hljs-title">loadPdfHandler</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-comment">// this.currentPage = 1; // 加载的时候先加载第一页</span>
    &#125;,
    <span class="hljs-comment">// 改变PDF页码,val传过来区分上一页下一页的值,0上一页,1下一页</span>
    <span class="hljs-function"><span class="hljs-title">changePdfPage</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.clickFlag) <span class="hljs-keyword">return</span>;
      <span class="hljs-built_in">this</span>.clickFlag = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.clickTimer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.clickFlag = <span class="hljs-literal">false</span>;
      &#125;, <span class="hljs-number">500</span>);
      <span class="hljs-keyword">if</span> (val === <span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.currentPage > <span class="hljs-number">1</span>) &#123;
        <span class="hljs-built_in">this</span>.currentPage--;
      &#125;
      <span class="hljs-keyword">if</span> (val === <span class="hljs-number">1</span> && <span class="hljs-built_in">this</span>.currentPage < <span class="hljs-built_in">this</span>.pageCount) &#123;
        <span class="hljs-built_in">this</span>.currentPage++;
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.canvas)<span class="hljs-built_in">this</span>.canvas.clear();
      <span class="hljs-built_in">this</span>.canvas = <span class="hljs-literal">null</span>;
      <span class="hljs-built_in">this</span>.showPdfBoxFlag = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span>&#123;
        <span class="hljs-built_in">this</span>.showPdfBoxFlag = <span class="hljs-literal">true</span>;
      &#125;)
    &#125;,
    <span class="hljs-comment">// 鼠标事件</span>
    <span class="hljs-function"><span class="hljs-title">mousedown</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.mouse.started) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
      <span class="hljs-keyword">let</span> mouse = <span class="hljs-built_in">this</span>.canvas.getPointer(e.e);
      <span class="hljs-comment">// this.mouse.started = true;</span>
      <span class="hljs-keyword">let</span> x = mouse.x;
      <span class="hljs-keyword">let</span> y = mouse.y;
      <span class="hljs-built_in">this</span>.mouse = &#123;
        ...this.mouse,
        x,
        y,
      &#125;;
      <span class="hljs-built_in">this</span>.makeGridObject = &#123;
        <span class="hljs-attr">beginX</span>: x,
        <span class="hljs-attr">beginY</span>: y,
      &#125;;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mousemove</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.mouse.started) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
      <span class="hljs-keyword">var</span> mouse = <span class="hljs-built_in">this</span>.canvas.getPointer(e.e);
      <span class="hljs-keyword">var</span> w = <span class="hljs-built_in">Math</span>.abs(mouse.x - <span class="hljs-built_in">this</span>.mouse.x),
        h = <span class="hljs-built_in">Math</span>.abs(mouse.y - <span class="hljs-built_in">this</span>.mouse.y);
      <span class="hljs-keyword">if</span> (!w || !h) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mouseup</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.mouse.started) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
      <span class="hljs-built_in">this</span>.mouse.started = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>.accurateChoiceFlag = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">let</span> endX = e.offsetX;
      <span class="hljs-keyword">let</span> endY = e.offsetY;
      <span class="hljs-comment">// 马赛克遮罩</span>
      <span class="hljs-keyword">let</span> &#123; beginX, beginY &#125; = <span class="hljs-built_in">this</span>.makeGridObject;
      <span class="hljs-keyword">var</span> mouse = <span class="hljs-built_in">this</span>.canvas.getPointer(e.e);
      <span class="hljs-keyword">var</span> w = <span class="hljs-built_in">Math</span>.abs(mouse.x - beginX),
        h = <span class="hljs-built_in">Math</span>.abs(mouse.y - beginY);
      <span class="hljs-keyword">let</span> obj = &#123;
        beginX,
        beginY,
        w,
        h,
      &#125;;
      <span class="hljs-built_in">this</span>.makeList.push(obj);
      <span class="hljs-built_in">this</span>.drawMake();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">pageTransformedIntoCanvas</span>(<span class="hljs-params">callback</span>)</span> &#123;
      <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
      html2canvas(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"pdf"</span>), &#123;
        <span class="hljs-attr">allowTaint</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">useCORS</span>: <span class="hljs-literal">true</span>,
      &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">canvas</span>) </span>&#123;
        <span class="hljs-keyword">let</span> contentWidth = canvas.width;
        <span class="hljs-keyword">let</span> contentHeight = canvas.height;
        <span class="hljs-comment">//竖向打印</span>
        <span class="hljs-keyword">let</span> imgWidth = <span class="hljs-number">595.28</span>;
        <span class="hljs-keyword">let</span> imgHeight = (<span class="hljs-number">592.28</span> / contentWidth) * contentHeight;
        <span class="hljs-keyword">let</span> pageHeight = (contentWidth / <span class="hljs-number">592.28</span>) * <span class="hljs-number">841.89</span>;
        <span class="hljs-keyword">let</span> leftHeight = contentHeight;
        <span class="hljs-keyword">let</span> position = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">if</span> (contentWidth > contentHeight) &#123;
          <span class="hljs-comment">//横向打印</span>
          imgWidth = <span class="hljs-number">841.89</span>;
          imgHeight = (<span class="hljs-number">841.89</span> / contentWidth) * contentHeight;
        &#125;
        <span class="hljs-keyword">let</span> pageData = canvas.toDataURL(<span class="hljs-string">"image/jpeg"</span>, <span class="hljs-number">1.0</span>);
        <span class="hljs-keyword">let</span> PDF;
        <span class="hljs-keyword">if</span> (contentWidth <= contentHeight) &#123;
          <span class="hljs-comment">//竖向打印</span>
          PDF = <span class="hljs-keyword">new</span> jsPDF(<span class="hljs-string">""</span>, <span class="hljs-string">"pt"</span>, <span class="hljs-string">"a4"</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">//    横向打印</span>
          PDF = <span class="hljs-keyword">new</span> jsPDF(<span class="hljs-string">"l"</span>, <span class="hljs-string">"pt"</span>, <span class="hljs-string">"a4"</span>);
        &#125;
        <span class="hljs-keyword">if</span> (leftHeight < pageHeight) &#123;
          PDF.addImage(pageData, <span class="hljs-string">"JPEG"</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, imgWidth, imgHeight);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-keyword">while</span> (leftHeight > <span class="hljs-number">0</span>) &#123;
            PDF.addImage(pageData, <span class="hljs-string">"JPEG"</span>, <span class="hljs-number">0</span>, position, imgWidth, imgHeight);
            leftHeight -= pageHeight;
            position -= <span class="hljs-number">841.89</span>;
            <span class="hljs-keyword">if</span> (leftHeight > <span class="hljs-number">0</span>) &#123;
              PDF.addPage();
            &#125;
          &#125;
        &#125;
        <span class="hljs-keyword">let</span> datauri = PDF.output(<span class="hljs-string">"dataurlstring"</span>);
        <span class="hljs-keyword">let</span> base64 = datauri.split(<span class="hljs-string">"base64,"</span>)[<span class="hljs-number">1</span>];
        callback(pageData, PDF);
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">drawMake</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.canvas)<span class="hljs-keyword">return</span>;
      <span class="hljs-built_in">this</span>.context.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.canvas.width, <span class="hljs-built_in">this</span>.canvas.height);
      <span class="hljs-built_in">this</span>.context.drawImage(<span class="hljs-built_in">this</span>.bgImage, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      <span class="hljs-built_in">this</span>.context.save();
      <span class="hljs-comment">// if (this.canvas) this.canvas.clear();</span>
      <span class="hljs-built_in">this</span>.makeList.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> &#123; beginX, beginY, w, h &#125; = item;
        <span class="hljs-built_in">this</span>.makeGrid(beginX, beginY, w, h);
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">clearClean</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.canvas) <span class="hljs-built_in">this</span>.canvas.clear();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">printPdf</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> base64 = <span class="hljs-string">""</span>;
      <span class="hljs-keyword">let</span> datauri = <span class="hljs-string">""</span>;
      <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
      <span class="hljs-built_in">this</span>.pageTransformedIntoCanvas(<span class="hljs-function">(<span class="hljs-params">pageData, PDF</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> blob = PDF.output(<span class="hljs-string">"blob"</span>);
        that.print(blob);
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">print</span>(<span class="hljs-params">blob</span>)</span> &#123;
      <span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
      <span class="hljs-keyword">var</span> ifr = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"iframe"</span>);
      ifr.style.frameborder = <span class="hljs-string">"no"</span>;
      ifr.style.display = <span class="hljs-string">"none"</span>;
      ifr.style.pageBreakBefore = <span class="hljs-string">"always"</span>;
      ifr.setAttribute(<span class="hljs-string">"id"</span>, <span class="hljs-string">"printPdf"</span> + date);
      ifr.setAttribute(<span class="hljs-string">"name"</span>, <span class="hljs-string">"printPdf"</span> + date);
      ifr.src = <span class="hljs-built_in">window</span>.URL.createObjectURL(blob);
      <span class="hljs-built_in">document</span>.body.appendChild(ifr);
      <span class="hljs-built_in">this</span>.doPrint(<span class="hljs-string">"printPdf"</span> + date);
      <span class="hljs-built_in">window</span>.URL.revokeObjectURL(ifr.src); <span class="hljs-comment">// 释放URL 对象</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">doPrint</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">var</span> ordonnance = <span class="hljs-built_in">document</span>.getElementById(val).contentWindow;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        ordonnance.print();
      &#125;, <span class="hljs-number">100</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">makeGrid</span>(<span class="hljs-params">beginX, beginY, rectWidth, rectHight</span>)</span> &#123;
      <span class="hljs-keyword">const</span> row = <span class="hljs-built_in">Math</span>.round(rectWidth / <span class="hljs-built_in">this</span>.squareEdgeLength) + <span class="hljs-number">1</span>;
      <span class="hljs-keyword">const</span> column = <span class="hljs-built_in">Math</span>.round(rectHight / <span class="hljs-built_in">this</span>.squareEdgeLength) + <span class="hljs-number">1</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < row * column; i++) &#123;
        <span class="hljs-keyword">let</span> x = (i % row) * <span class="hljs-built_in">this</span>.squareEdgeLength + beginX;
        <span class="hljs-keyword">let</span> y = <span class="hljs-built_in">parseInt</span>(i / row) * <span class="hljs-built_in">this</span>.squareEdgeLength + beginY;
        <span class="hljs-built_in">this</span>.setColor(x, y);
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setColor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
      <span class="hljs-keyword">const</span> imgData = <span class="hljs-built_in">this</span>.context.getImageData(
        x,
        y,
        <span class="hljs-built_in">this</span>.squareEdgeLength,
        <span class="hljs-built_in">this</span>.squareEdgeLength
      ).data;
      <span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>,
        g = <span class="hljs-number">0</span>,
        b = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < imgData.length; i += <span class="hljs-number">4</span>) &#123;
        r += imgData[i];
        g += imgData[i + <span class="hljs-number">1</span>];
        b += imgData[i + <span class="hljs-number">2</span>];
      &#125;
      r = <span class="hljs-built_in">Math</span>.round(r / (imgData.length / <span class="hljs-number">4</span>));
      g = <span class="hljs-built_in">Math</span>.round(g / (imgData.length / <span class="hljs-number">4</span>));
      b = <span class="hljs-built_in">Math</span>.round(b / (imgData.length / <span class="hljs-number">4</span>));
      <span class="hljs-built_in">this</span>.drawRect(
        x,
        y,
        <span class="hljs-built_in">this</span>.squareEdgeLength,
        <span class="hljs-built_in">this</span>.squareEdgeLength,
        <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;g&#125;</span>, <span class="hljs-subst">$&#123;b&#125;</span>)`</span>,
        <span class="hljs-number">2</span>,
        <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;g&#125;</span>, <span class="hljs-subst">$&#123;b&#125;</span>)`</span>
      );
    &#125;,
    <span class="hljs-function"><span class="hljs-title">drawRect</span>(<span class="hljs-params">
      x,
      y,
      width,
      height,
      fillStyle,
      lineWidth,
      strokeStyle,
      globalAlpha
    </span>)</span> &#123;
      <span class="hljs-built_in">this</span>.context.beginPath();
      <span class="hljs-built_in">this</span>.context.rect(x, y, width, height);
      <span class="hljs-built_in">this</span>.context.lineWidth = lineWidth;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fillColor) &#123;
        fillStyle = <span class="hljs-built_in">this</span>.fillColor;
        strokeStyle = <span class="hljs-built_in">this</span>.fillColor;
      &#125;
      <span class="hljs-built_in">this</span>.context.strokeStyle = strokeStyle;
      fillStyle && (<span class="hljs-built_in">this</span>.context.fillStyle = fillStyle);
      globalAlpha && (<span class="hljs-built_in">this</span>.context.globalAlpha = globalAlpha);
      <span class="hljs-built_in">this</span>.context.fill();
      <span class="hljs-built_in">this</span>.context.stroke();
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.btn-list</span> &#123;
  & > <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
  &#125;
  & > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">0</span>;
  &#125;
&#125;
<span class="hljs-selector-class">.page-btn</span> &#123;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-selector-class">.page-count</span> &#123;
    <span class="hljs-attribute">min-width</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
  &#125;
&#125;
<span class="hljs-selector-class">.pdf-box</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.manager_detail</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.web-file</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">65%</span>;
  <span class="hljs-attribute">min-width</span>: <span class="hljs-number">900px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
  <span class="hljs-selector-class">.pdf-box</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>; // <span class="hljs-attribute">height</span>: <span class="hljs-number">55vh</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
  &#125;
&#125;
<span class="hljs-selector-class">.accurate-choice</span> &#123;
  <span class="hljs-attribute">cursor</span>: crosshair;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            