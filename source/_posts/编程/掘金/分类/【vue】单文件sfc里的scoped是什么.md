
---
title: '【vue】单文件sfc里的scoped是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84825279d8294ad681fc3aa895d790fa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 22:36:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84825279d8294ad681fc3aa895d790fa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h3 data-id="heading-0">1、样式污染</h3>
<p>考虑这样的一个场景。有<code>组件A</code>和<code>组件B</code>的style中定义了同样的类<code>.h1</code>, 那么打包之后的css文件中就会有两个同样的<code>.h1</code>类， 当页面展示组件A或者组件B的时候样式都同时受到了定义的两个<code>.h1</code>的影响，造成样式错乱。为了更好说明，我写了A和B两个组件，代码如下：</p>
<ol>
<li>组件A</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"compA"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>A Hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">B</span>></span><span class="hljs-tag"></<span class="hljs-name">B</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> B <span class="hljs-keyword">from</span> <span class="hljs-string">"./B"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
  <span class="hljs-attr">components</span>: &#123;
    B
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.h1</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">40px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">color</span>: red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>组件B</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"compB"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>B<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.h1</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">40px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开页面，此时三个h1的颜色都是红色。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84825279d8294ad681fc3aa895d790fa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在组件B中<code>.h1</code>定义的<code>color: green;</code>被覆盖了。
打开浏览器控制台可以看到，下面的<code>.h1</code>将上面的<code>.h1</code>定义的<code>color</code>覆盖了。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c303ee1289544d10bdae5c114d8ed41c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2、使用scoped</h3>
<ol>
<li>A组件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"compA"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>A Hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">B</span>></span><span class="hljs-tag"></<span class="hljs-name">B</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> B <span class="hljs-keyword">from</span> <span class="hljs-string">"./B"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
  <span class="hljs-attr">components</span>: &#123;
    B
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.h1</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">40px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">color</span>: red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>B组件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"compB"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>B<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"h1"</span>></span>World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.h1</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">40px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  <span class="hljs-attribute">color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开页面后，是这样显示的：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3254c07bddc34452b6bc37bb07326a36~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这才是我们想要的效果。打开控制台，发现有下面两个变化：</p>
<ol>
<li>打包后的css选择器上多了<code>data-v-XXXXXX</code></li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f5adee6fb4b4ee4944029da3e64d78e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>dom元素上多了<code>data-v-XXXXXX</code></li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a9ad4f84d614348b0e94b5ddd9e4aa4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由此，我们大概能猜到<code>style</code>标签上加了<code>scoped</code>后编译后的css和页面中的dom元素都会加上<code>data-v-XXXXXX</code>。这样浏览器就能区分A组件的<code>.h1</code>和B组件的<code>.h1</code>。</p>
<p>上面讲的是使用<code>scoped</code>来解决样式污染的问题。当然这并不是我的目的，就像标题说的那样，我希望尝试把<code>scoped</code>是什么以及是怎么样生效的讲清楚。从一下几个问题作为切入点。</p>
<ol>
<li>什么是scopeId？scopeId是怎么生成的？</li>
<li>在sfc的<code>template</code>中我们并没有定义<code>data-v</code>这样的属性, 那为什么在页面的dom元素上会多出<code>data-v-XXXXXX</code>这个属性呢？</li>
<li>在sfc的<code>style</code>中我们写的选择器也没有加上<code>data-v-XXXXXX</code>，那这是怎么加上去的呢？</li>
</ol>
<h3 data-id="heading-2">2、什么是scopeId? scopeId是怎么生成的？</h3>
<p>每一个<code>sfc</code>组件都会有自己的唯一<code>scopeId</code>，类似<code>data-v-XXXXXX</code>中的<code>XXXXXX</code>就是scopeId。
我们都知道<code>.vue</code>单文件组件是需要经过<code>vue-loader</code>去处理的。既然每个vue文件的<code>scopeId</code>是唯一的，那么很容易联想到<code>scopeId</code>是不是<code>vue-loader</code>生成的。<code>vue-loader</code>里面的确有这样的逻辑。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> id = hash(
    isProduction
      ? (shortFilePath + <span class="hljs-string">'\n'</span> + source.replace(<span class="hljs-regexp">/\r\n/g</span>, <span class="hljs-string">'\n'</span>))
      : shortFilePath
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码就是生成<code>scopeId</code>执行的代码。</p>
<h3 data-id="heading-3">3、在sfc的<code>template</code>中我们并没有定义<code>data-v</code>这样的属性, 那为什么在页面的dom元素上会多出<code>data-v-XXXXXX</code>这个属性呢？</h3>
<p>不知道大家有没有仔细看过组件导出的对象是什么样的？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> B <span class="hljs-keyword">from</span> <span class="hljs-string">"./B"</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'组件B'</span>, B)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印的结果：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932384013fb24f05ae6637cf86055595~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>导出的组件配置上会多一个<code>_scopeId</code>属性，这个属性不是我们自己定义上去的, 属性值<code>data-v-5277df62</code>是不是很熟悉？</p>
<p>这个值是不是和上面的dom截图中组件B内部dom元素上的<code>scopeId</code>一样的？</p>
<p>很明显sfc组件只是在编译阶段往组件配置对象上加了<code>_scopeId</code>属性， 属性值也不是随便写的， 是由<code>vue-loader</code>生成的。生成逻辑上面已经讲过了。</p>
<p>那么dom元素是什么时候加上<code>scope</code>的呢？在<code>vue2</code>的<code>patch</code>逻辑中有这样一段代码，这段代码在<code>src/core/vdom/patch.js</code>中的<code>createElm</code>内。大概的逻辑就是在<code>createElm</code>内部创建真实的dom之后，调用<code>setScope</code>给dom元素添加<code>scopeId</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">  vnode.elm = vnode.ns
    ? nodeOps.createElementNS(vnode.ns, tag)
    : nodeOps.createElement(tag, vnode)
  setScope(vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setScope</code>的逻辑是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setScope</span> (<span class="hljs-params">vnode</span>) </span>&#123;
    <span class="hljs-keyword">let</span> i
    <span class="hljs-keyword">if</span> (isDef(i = vnode.fnScopeId)) &#123;
      nodeOps.setStyleScope(vnode.elm, i)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">let</span> ancestor = vnode
      <span class="hljs-keyword">while</span> (ancestor) &#123;
        <span class="hljs-keyword">if</span> (isDef(i = ancestor.context) && isDef(i = i.$options._scopeId)) &#123;
          nodeOps.setStyleScope(vnode.elm, i)
        &#125;
        ancestor = ancestor.parent
      &#125;
    &#125;
    <span class="hljs-comment">// for slot content they should also get the scopeId from the host instance.</span>
    <span class="hljs-keyword">if</span> (isDef(i = activeInstance) &&
      i !== vnode.context &&
      i !== vnode.fnContext &&
      isDef(i = i.$options._scopeId)
    ) &#123;
      nodeOps.setStyleScope(vnode.elm, i)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>dom元素上的<code>data-v-XXXXXX</code>是在运行时<code>patch</code>的过程中添加上去的。</p>
</blockquote>
<h3 data-id="heading-4">4、在sfc的<code>style</code>中我们写的选择器也没有加上<code>data-v-XXXXXX</code>，那这是怎么加上去的呢？</h3>
<p>这一切都是由一个叫<code>stylePostLoader</code>的loader来完成的。</p>
<ol>
<li>stylePostLoader处理css代码</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2df2266f850f4b238d25a1e26d278ef5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>compileStyle内部使用<code>postCss</code>对css代码进行转换。下面的截图中可以看到使用了<code>scoped</code>时会使用一个<code>scoped_1</code>插件。</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b044e913789e4ba58e23fea4c9b950d0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>查看<code>scoped_1</code>插件的代码，发现有这样一段代码。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> selector.insertAfter(node, selectorParser.attribute(&#123;
    <span class="hljs-attr">attribute</span>: id
 &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>css代码上的<code>data-v-XXXXXX</code>是通过<code>stylePostLoader</code>加上去的。</p>
</blockquote>
<h3 data-id="heading-5">5、/deep/的作用？</h3>
<p><code>scopedId</code>默认是加在选择器的最后一级上的。比如说下面的例子中有<code>组件A</code>和<code>组件B</code>。在<code>组件A</code>中使用了<code>组件B</code>, 当在组件A中修改组件B的内部<code>.el-autocomplete</code>样式时：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.compA</span> <span class="hljs-selector-class">.el-autocomplete</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">280px</span>;
&#125;

<span class="hljs-comment">/* 编译后的代码 */</span>
<span class="hljs-selector-class">.compA</span> <span class="hljs-selector-class">.el-autocomplete</span><span class="hljs-selector-attr">[data-v-19388c91]</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">280px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>/deep/</code>后</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.compA</span> /deep/<span class="hljs-selector-class">.el-autocomplete</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">280px</span>;
&#125;

<span class="hljs-comment">/* 编译后的代码 */</span>
<span class="hljs-selector-class">.compA</span><span class="hljs-selector-attr">[data-v-19388c91]</span> <span class="hljs-selector-class">.el-autocomplete</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">280px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比下面的dom结构图， 很明显知道了deep之后起作用的原因了。</p>
<p><img alt="210322-1536.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8e2d10c04bd474e8a176881df31c0f6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>使用<code>/deep/</code>之前我们想要修改<code>组件B</code>内部带有<code>.el-autocomplete</code>的元素的样式，打包后使用的选择器是<code>.compA .el-autocomplete[data-v-19388c91]</code>，很明显带有<code>.el-autocomplete</code>的元素上是不存在<code>data-v-19388c91</code>属性的，所以样式不起作用。</li>
<li>使用<code>/deep/</code>之后呢？打包后的css是这样的<code>.compA[data-v-19388c91] .el-autocomplete</code>, 将<code>scopedId</code>移动到了<code>.compA</code>上， 此时样式是起作用的。</li>
</ul>
<blockquote>
<p>总结</p>
</blockquote>
<ol>
<li>当在父组件内给子组件的根节点修改样式时，其实是不用加<code>/deep/</code>的， 因为在子组件的根节点上同时有父组件和子组件的<code>scopeId</code>。</li>
<li>当在父组件内给子组件的非根节点修改样式时需要带上<code>/deep/</code>，因为在父组件定义选择器的最后一级使用的是父组件的<code>scopeId</code>，而子组件中需要选择的元素却使用的是子组件的<code>scopeId</code>，所以是不会匹配上的，样式也不会生效。</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            