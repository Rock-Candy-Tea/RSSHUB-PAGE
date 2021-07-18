
---
title: '_JS_【二】---基本数据类型之【Number篇】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=171'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:20:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=171'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h2 data-id="heading-0">核心知识点</h2>
<ol>
<li><strong>Number数字数据类型简述</strong></li>
<li><strong>isNaN（检测一个值是否为非有效数字）方法</strong></li>
<li><strong>自增及其特殊性</strong></li>
<li><strong>把其他类型值转换为数字类型</strong></li>
<li><strong>数组对象以及map方法回调函数的类型转换例子</strong></li>
</ol>
<h2 data-id="heading-1">Number数字类型</h2>
<ol>
<li>常规数字</li>
<li>NaN(NOT A NUMBER):不是一个数，但是隶属于数字类型</li>
<li>Infinity (无穷大值)</li>
</ol>
<h2 data-id="heading-2">NaN和isNaN（检测一个值是否为非有效数字）方法</h2>
<h3 data-id="heading-3">关于NaN</h3>
<p>1.【NaN和任何值都不相等，甚至和自己都不相等；】</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-literal">NaN</span> == <span class="hljs-literal">NaN</span>     <span class="hljs-comment">//false</span>
<span class="hljs-literal">NaN</span> === <span class="hljs-literal">NaN</span>    <span class="hljs-comment">//false</span>
<span class="hljs-literal">NaN</span> !== <span class="hljs-literal">NaN</span>    <span class="hljs-comment">//true  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.【但是用Object.is(NaN,NaN)判断两个值是否相等，结果是true】</p>
<h3 data-id="heading-4">isNaN:检测一个值是否是非有效数字</h3>
<ul>
<li>如果【不是有效数字】则返回true</li>
<li>反之【是有效数字】则返回false</li>
</ul>
<blockquote>
<p><strong>在使用isNaN进行检测的时候，其机制将首先会验证检测的值是否为数字类型，如果不是，先基于Number()这个方法，把值转换为数字类型，然后再检测。</strong></p>
</blockquote>
<ul>
<li>
<p>如isNaN('10');   //为false，因为在检测前由于此机制，自动转型了</p>
</li>
<li>
<p>凡是能够转成数字之后是有效数字的，都是有效数字</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">       <span class="hljs-comment">//isNaN([val])</span>
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-number">10</span>));<span class="hljs-comment">//false</span>
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-string">'AA'</span>));<span class="hljs-comment">//True</span>
       <span class="hljs-comment">/* 
           实际上在检测之前相当于发生了：
           Number('AA');  =>NaN 【转不成数字】
           isNaN(NaN);  =>TRUE
       */</span>
 <span class="hljs-comment">//</span>
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-string">'10'</span>));<span class="hljs-comment">//false</span>
       <span class="hljs-comment">/* 
         类型转换机制
           实际上在检测之前相当于发生了：
           Number('10');  =>10
           isNaN(10);  =>false
       */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">isNaN</span>(<span class="hljs-string">'123'</span>) <span class="hljs-comment">//false</span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-number">123</span>) <span class="hljs-comment">// false </span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-string">" "</span>) <span class="hljs-comment">//false </span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-string">'1.2.3'</span>) <span class="hljs-comment">// true </span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-string">"23px"</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">'"23px") = NaN 
isNaN（Number('</span>aaa<span class="hljs-string">')） //true Number('</span>aaa<span class="hljs-string">'") = NaN 
isNaN(Number(true)) // 输入1 =》false 
isNaN(Number(false)) // 输入0 =》false 
isNaN(Number(null)) // 输入0 =》false 
isNaN(Number(undefined)) // 输入NaN =》true
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">自增的特殊性</h2>
<blockquote>
<p>由于+号的特殊性质 <strong>【可代表数学运算】</strong>,<strong>【也可代表字符串拼接】</strong></p>
<p>所以在<strong>i++;</strong> <strong>i+=n;</strong> <strong>i=i+n;</strong> 这三种运算形式中也有些微的差别。</p>
<p><strong>i++;和其他两种不完全一样，其代表着纯粹的数学运算</strong></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> i = <span class="hljs-string">'10'</span>;
 i=i+<span class="hljs-number">1</span>;<span class="hljs-comment">//=>'10'+1=>'101'【结果为字符串拼接】</span>
 i+=<span class="hljs-number">1</span>;<span class="hljs-comment">//'10'+1=>'101'【结果为字符串拼接】</span>
 i++;<span class="hljs-comment">//=>10=>10+1=>11【结果为数字11，过程为数学运算】</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">把其他类型值转换为数字类型</h2>
<p><strong>两类方法：手动转换和隐式转换</strong></p>
<h3 data-id="heading-7">隐式转换：【浏览器内部默认要先转换为Number再进行计算的】</h3>
<blockquote>
<ol>
<li><strong>isNaN([val])</strong></li>
<li><strong>==数学运算</strong>（特殊情况：+在出现字符串或对象的情况下不是数学运算，而是字符串拼接）【只有前++/++后/+i的时候也可能是数学运算】</li>
<li><strong>==进行比较的时候</strong> 一些情况下会将数据类型进行转换为数字</li>
</ol>
</blockquote>
<h3 data-id="heading-8">手动转换</h3>
<h4 data-id="heading-9"><strong>Number([val])： 把所有有效数字字符都进行转换</strong>(一般用于浏览器的隐式转换中)</h4>
<p>+ 规则：</p>
<h5 data-id="heading-10">1 把字符串转换为数字：空字符串变为0，（第一个点除外，其作为小数点存在）如果出现任何一个非有效数字字符，结果都是NaN</h5>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-string">'12.5'</span>));<span class="hljs-comment">//12.5 </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-string">'12.5px'</span>));<span class="hljs-comment">//NaN </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-string">'12.5.5'</span>));<span class="hljs-comment">//NaN </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-string">''</span>));<span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">2 把布尔转换为数字：true->1 false->0</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-literal">true</span>));<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-literal">false</span>));<span class="hljs-comment">//0</span>
<span class="hljs-comment">//练习 </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">false</span>)); <span class="hljs-comment">//Number(false) =>0(是有效数字) =>false </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">true</span>));  <span class="hljs-comment">//Number(true) =>1(是有效数字) =>false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">3 null->0 undefined->NaN</h5>
<blockquote>
<p>null会转换为0</p>
<p>【null代表空对象指针，虽然代表没有，但是是有一个代表"空"的对象存在的，所以转换为Number应为0】undefined转换为NaN</p>
<p>【undefined代表未定义，未定义代表没有赋值，没有赋值就是"没有值"，"没有值"转换为Number的值就是NaN】</p>
</blockquote>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-literal">null</span>)); <span class="hljs-comment">//=>0 console.log(Number(undefined));//=>NaN </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">null</span>)); <span class="hljs-comment">//Number(null) =>0(是有效数字) =>false </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">undefined</span>)); <span class="hljs-comment">//Number(undefined) =>NaN(不是有效数字) =>true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">4 Symbol无法转换为数字，会报错：Uncaught TypeError: Cannot convert a Symbol value to a number</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"123"</span>))) 
<span class="hljs-comment">//=>Uncaught TypeError: Cannot convert a Symbol value to a number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">5 BigInt去除“n”（超过安全数字的，会按照科学计数法处理）</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>(<span class="hljs-number">231n</span>)) <span class="hljs-comment">//=>231</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">6 把对象转换为数字：</h5>
<blockquote>
<p><strong>普通对象、正则表达式对象、日期对象....转换为数字都是NaN</strong></p>
<p><strong>只有数组对象有可能转换为数字【数组也是对象类型的！】</strong></p>
<p><strong>【空数组转换为0】</strong> 只有一项值的数组才能最终转换为数值</p>
</blockquote>
<ul>
<li>
<p>先调用对象的 Symbol.toPrimitive 这个方法，如果不存在这个方法</p>
</li>
<li>
<p>再调用对象的 valueOf 获取原始值，如果获取的值不是原始值</p>
</li>
<li>
<p>再调用对象的 toString 把其变为字符串</p>
</li>
<li>
<p>最后再把字符串基于Number方法转换为数字</p>
</li>
</ul>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-built_in">Number</span>(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"xxx"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">5</span>&#125;) <span class="hljs-comment">//=>NaN</span>
<span class="hljs-number">1.</span>=>(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"xxx"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">5</span>&#125;)[<span class="hljs-built_in">Symbol</span>.toPrimitive] <span class="hljs-comment">//=>undefined</span>
<span class="hljs-number">2.</span>=>(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"xxx"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">5</span>&#125;).valueOf() <span class="hljs-comment">//=>&#123;name: "xxx", age: 5&#125;</span>
<span class="hljs-number">3.</span>=>(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"xxx"</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">5</span>&#125;).toString() <span class="hljs-comment">//=>"[object Object]"</span>
<span class="hljs-number">4.</span>=><span class="hljs-built_in">Number</span>(<span class="hljs-string">"[object Object]"</span>) <span class="hljs-comment">//=>NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>([]));<span class="hljs-comment">//=>0</span>
<span class="hljs-built_in">Number</span>([<span class="hljs-number">10</span>]) <span class="hljs-comment">//=>10</span>
<span class="hljs-number">1.</span>=>[<span class="hljs-number">10</span>][<span class="hljs-built_in">Symbol</span>.toPrimitive] <span class="hljs-comment">//=>undefined</span>
<span class="hljs-number">2.</span>=>[<span class="hljs-number">10</span>].valueOf() <span class="hljs-comment">//=>[10]</span>
<span class="hljs-number">3.</span>=>[<span class="hljs-number">10</span>].toString() <span class="hljs-comment">//=>"10"</span>
<span class="hljs-number">4.</span>=><span class="hljs-built_in">Number</span>(<span class="hljs-string">"10"</span>) <span class="hljs-comment">//=>10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-built_in">Number</span>([<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">30</span>]) <span class="hljs-comment">//=>NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">7 其他特殊转换的案例</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
<span class="hljs-built_in">Number</span>(time) <span class="hljs-comment">//=>1625126051393</span>
time[<span class="hljs-built_in">Symbol</span>.toPrimitive] <span class="hljs-comment">//=>ƒ [Symbol.toPrimitive]() &#123; [native code] &#125; 因为time有这个方法并且有3个参数 number / string / default 浏览器自己调用这个方法，会默认传递的实参值</span>
time[<span class="hljs-built_in">Symbol</span>.toPrimitive](<span class="hljs-string">'number'</span>) <span class="hljs-comment">//=>1625126051393</span>
dir(time)
<span class="hljs-attr">VM1101</span>:<span class="hljs-number">1</span> Thu Jul <span class="hljs-number">01</span> <span class="hljs-number">2021</span> <span class="hljs-number">15</span>:<span class="hljs-number">54</span>:<span class="hljs-number">11</span> GMT+<span class="hljs-number">0800</span> (中国标准时间)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>)) <span class="hljs-comment">//=>10</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>) <span class="hljs-comment">//=> Number &#123;10&#125; 输出一个对象 里面包含valueof()</span>
<span class="hljs-number">1.</span>=><span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>)[<span class="hljs-built_in">Symbol</span>.toPrimitive] <span class="hljs-comment">//=>undefined</span>
<span class="hljs-number">2.</span>=><span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>).valueOf() <span class="hljs-comment">//=>10  找到后不在往下走</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">parseInt([val],[进制])/parseFloat([val])的使用场景</h4>
<ul>
<li>
<p><strong>【注意：parseFloat不支持第二个参数！！！可以找浮点型数字】</strong></p>
</li>
<li>
<p><strong>【注意：parseInt可以识别各种整数（int）格式，如：8进制，10进制，16进制，所以可以接收第二个参数表示要转换为多少进制】</strong></p>
<blockquote>
<p><strong>规则：[val]值必须是一个字符串，如果不是则先<em>toString()</em> 转换为字符串；然后从字符串左侧第一个字符开始找，把找到的有效数字字符最后转换为数字「一个都没找到就是NaN」；遇到一个非有效数字字符，不论后面是否还有有效数字字符，都不再查找了；parseFloat可以多识别一个小数点</strong></p>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10"</span>) <span class="hljs-comment">//=> 10</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"010"</span>) <span class="hljs-comment">//=> 10</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10px"</span>) <span class="hljs-comment">//=> 10</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">'10px'</span>) <span class="hljs-comment">//=> NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10PX10"</span>) <span class="hljs-comment">//=> 10</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10.55px"</span>) <span class="hljs-comment">//=> 10</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">//=> NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">//=> NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-literal">false</span>);<span class="hljs-comment">//=>NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-literal">true</span>);<span class="hljs-comment">//=>NaN  如果是boolean，null，undefined类型值，则都会返回NaN</span>
<span class="hljs-built_in">parseInt</span>(&#123;&#125;) <span class="hljs-comment">//=>NaN </span>
<span class="hljs-built_in">parseInt</span>([]) <span class="hljs-comment">//=>NaN</span>
 <span class="hljs-comment">/* 
        parseInt/parseFloat
        如果是普通对象，则都会返回NaN
        (&#123;&#125;).toString() =>"[object object]"
        parseInt/parseFloat("[object object]") =>NaN
        ----------------------------
        [].toString() =>""//空字符串
        parseInt/parseFloat("") =>NaN
    */</span>
----------------------------
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">parseInt</span>([<span class="hljs-number">12</span>]));<span class="hljs-comment">//=>12</span>
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">parseFloat</span>([<span class="hljs-number">12.5</span>]));<span class="hljs-comment">//=>12.5</span>
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">parseInt</span>([<span class="hljs-number">12</span>,<span class="hljs-number">13</span>]));<span class="hljs-comment">//=>12</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">parseInt第二个参数 讲解---经典面试题</h4>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> arr = [<span class="hljs-number">27.2</span>, <span class="hljs-number">0</span>, <span class="hljs-string">'0013'</span>, <span class="hljs-string">'14px'</span>, <span class="hljs-number">123</span>];
 arr = arr.map(<span class="hljs-built_in">parseInt</span>);
<span class="hljs-comment">//array.map(function(currentValue,index,arr)&#123;&#125;) js中map函数会依次处理数组中的每一个元素  并返回一个新的数组 对原来的数组不会影响</span>
 <span class="hljs-built_in">console</span>.log(arr)
/!* 
  <span class="hljs-built_in">parseInt</span>(<span class="hljs-number">27.2</span>,<span class="hljs-number">0</span>)
    <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'27.2'</span>,<span class="hljs-number">10</span>)  ->  <span class="hljs-string">'27'</span>  ->  把<span class="hljs-string">'27'</span>看做<span class="hljs-number">10</span>进制，转换为<span class="hljs-number">10</span>进制  =><span class="hljs-number">27</span>
  <span class="hljs-built_in">parseInt</span>(<span class="hljs-number">0</span>,<span class="hljs-number">1</span>)  =><span class="hljs-literal">NaN</span>   -> 制不在取值范围内，=><span class="hljs-literal">NaN</span>
  <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'0013'</span>,<span class="hljs-number">2</span>)
    <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'0013'</span>,<span class="hljs-number">2</span>)  ->  <span class="hljs-string">'001'</span>  ->  把<span class="hljs-string">'001'</span>看做<span class="hljs-number">2</span>进制(<span class="hljs-number">2</span>以内的数)<span class="hljs-number">10</span>进制  =><span class="hljs-number">1</span>
      <span class="hljs-number">0</span>*<span class="hljs-number">2</span>^<span class="hljs-number">2</span> + <span class="hljs-number">0</span>*<span class="hljs-number">2</span>^<span class="hljs-number">1</span> + <span class="hljs-number">1</span>*<span class="hljs-number">2</span>^<span class="hljs-number">0</span>

  <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'14px'</span>,<span class="hljs-number">3</span>)
    <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'14px'</span>,<span class="hljs-number">3</span>)  ->  <span class="hljs-string">'1'</span>  ->  把<span class="hljs-string">'1'</span>看做<span class="hljs-number">3</span>进制(<span class="hljs-number">3</span>以内的数 <span class="hljs-number">4</span>超出三进制范围)，转换为<span class="hljs-number">10</span>进制  =><span class="hljs-number">1</span>
      <span class="hljs-number">1</span>*<span class="hljs-number">3</span>^<span class="hljs-number">0</span>   

  <span class="hljs-built_in">parseInt</span>(<span class="hljs-number">123</span>,<span class="hljs-number">4</span>)
    <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'123'</span>,<span class="hljs-number">4</span>)  ->  <span class="hljs-string">'123'</span>  ->  把<span class="hljs-string">'123'</span>看做<span class="hljs-number">4</span>进制(<span class="hljs-number">4</span>以内的数)，转换为<span class="hljs-number">10</span>进制  =><span class="hljs-number">27</span>
      <span class="hljs-number">1</span>*<span class="hljs-number">4</span>^<span class="hljs-number">2</span> + <span class="hljs-number">2</span>*<span class="hljs-number">4</span>^<span class="hljs-number">1</span> + <span class="hljs-number">3</span>*<span class="hljs-number">4</span>^<span class="hljs-number">0</span>

  <span class="hljs-built_in">parseInt</span>传递的第二个值是一个radix进制 
    + radix不写或者写<span class="hljs-number">0</span>，默认是<span class="hljs-number">10</span>进制「如果第一个传递的字符串是以“0x”开始的，那么默认是<span class="hljs-number">16</span>进制」
    + radix取值范围：<span class="hljs-number">2</span>~<span class="hljs-number">36</span>，不在这个范围内，处理的结果都是<span class="hljs-literal">NaN</span>
    + 在传递的字符串中，从左到右，找到符合radix进制的值&#123;遇到不符合的则结束查找&#125;，把找到的值，看做radix进制，最后转换为<span class="hljs-number">10</span>进制
    + 把其它进制的值转换为<span class="hljs-number">10</span>进制：“按权展开求和”
*!/

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            