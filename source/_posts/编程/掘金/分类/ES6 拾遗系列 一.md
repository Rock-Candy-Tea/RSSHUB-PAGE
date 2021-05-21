
---
title: 'ES6 拾遗系列 一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8514'
author: 掘金
comments: false
date: Thu, 20 May 2021 05:32:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=8514'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h1 data-id="heading-0">let 和 const</h1>
<h2 data-id="heading-1"><strong>问什么要引入 let 和 const ？</strong></h2>
<p>解决 var 声明变量带来的问题。</p>
<p>在 ES6 之前，声明变量只能通过 var ，使用var声明变量存在以下问题：</p>
<p>允许重复的变量声明：导致数据被覆盖</p>
<p>变量提升：怪异的数据访问、闭包问题</p>
<p>全局变量挂载到全局对象：全局对象成员污染问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 变量提升：怪异的数据访问</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.random() < <span class="hljs-number">0.5</span>) &#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-string">"abc"</span>;
    <span class="hljs-built_in">console</span>.log(a);
&#125;
<span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(a);
&#125;
<span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//<0.5 abc   >=0.5 undefined</span>

<span class="hljs-comment">// 变量提升：闭包问题</span>
<span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"divButtons"</span>)

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">10</span>; i++) &#123;
    <span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"button"</span>);
    btn.innerHTML = <span class="hljs-string">"按钮"</span> + i;
    div.appendChild(btn);
    btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">//输出11</span>
    &#125;
&#125;
<span class="hljs-comment">// 全局变量挂载到全局对象：全局对象成员污染问题</span>
<span class="hljs-keyword">var</span> abc = <span class="hljs-string">"123"</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.abc);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了解决上述问题，ES6 新增了 let 和 const</p>
<h2 data-id="heading-2"><strong>let 和 const 的特性 ？</strong></h2>
<p>块级作用域：代码执行时遇到花括号，会创建一个块级作用域，花括号结束，销毁块级作用域</p>
<p>变量赋值：在同一个作用域内，let 声明的变量能重新赋值，const 在声明变量的同时必须赋值 ，且值不可修改，在作用域外无法访问声明的变量</p>
<p>变量提升：let 和 const 均不会有变量提升，因此，不能在使用 let 和 const 声明变量之前使用它。底层实现上，let 声明的变量实际上也会有提升，但是，提升后会将其放入到“暂时性死区”，如果访问的变量位于暂时性死区，则会报错：“Cannot access 'a' before initialization”。当代码运行到该变量的声明语句时，会将其从暂时性死区中移除。</p>
<p>闭包问题处理：在循环中，用 let 声明的循环变量，会特殊处理，每次进入循环体，都会开启一个新的块级作用域，并且将循环变量绑定到该作用域（每次循环，使用的是一个全新的循环变量）。循环中使用let声明的循环变量，在循环结束后会销毁。</p>
<p>mdn文档链接：<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/let" target="_blank" rel="nofollow noopener noreferrer">let</a>  <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/const" target="_blank" rel="nofollow noopener noreferrer">const</a></p>
<h1 data-id="heading-3">解构赋值</h1>
<h2 data-id="heading-4"><strong>什么是解构赋值，它能做什么</strong></h2>
<p>解构赋值是 ES6 提供的一种语法糖，通过解构赋值，可以将属性/值从对象/数组中取出，并赋值给其他变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 取得对象的值</span>
<span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-keyword">let</span> a = obj.a;
<span class="hljs-keyword">let</span> b = obj.b;
<span class="hljs-built_in">console</span>.log(obj.a,obj.b);
<span class="hljs-comment">//取得数组的值</span>
<span class="hljs-keyword">const</span> arr =[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>];
<span class="hljs-keyword">let</span> num1 = arr[<span class="hljs-number">0</span>];
<span class="hljs-keyword">let</span> num2 = arr[<span class="hljs-number">1</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下的代码和上面的代码结果一致，区别是下面的用了解构赋值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 取得对象的值</span>
<span class="hljs-keyword">const</span> &#123;a,b&#125;=&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-comment">//取得数组的值</span>
<span class="hljs-keyword">const</span> [num1,num2]=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解构赋值在对象和数组解构赋值的时候会有差别，对象是按照属性取值，数组是按照index的顺序取值</p>
<p>另外对于解构赋值还提供了默认参数和变量重命名的语法糖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//默认参数</span>
<span class="hljs-keyword">let</span> &#123;a,b=<span class="hljs-number">5</span>,c=<span class="hljs-number">1</span>&#125;=&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-keyword">let</span> [num1,num2=<span class="hljs-number">10</span>,num3=<span class="hljs-number">1</span>]=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>];
<span class="hljs-comment">//变量重名名</span>
<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">a</span>:a1,b&#125;=&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">console</span>.log(a1)<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(a)<span class="hljs-comment">//报错 Uncaught ReferenceError: a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过解构赋值，快速实现两变量值交换</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a=<span class="hljs-number">11</span>,b=<span class="hljs-number">22</span>;
[b,a]=[a,b];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"><strong>解构赋值的原理（实现方式）</strong></h2>
<p>其内在是针对可迭代对象的Iterator接口，通过遍历器（for of）按顺序获取对应的值进行赋值</p>
<p>mdn文档链接：<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment" target="_blank" rel="nofollow noopener noreferrer">解构赋值</a></p>
<h1 data-id="heading-6">展开运算符</h1>
<h2 data-id="heading-7">怎么使用展开运算符偷懒</h2>
<p>展开运算符可以在函数调用/数组构造时, 将数组表达式或者string在语法层面展开；还可以在构造字面量对象时, 将对象表达式按key-value的方式展开</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//字符串展开</span>
<span class="hljs-keyword">let</span> str=<span class="hljs-string">'bar'</span>;
<span class="hljs-keyword">const</span> strArr = [...str]; <span class="hljs-comment">// ["b", "a", "r"]</span>


<span class="hljs-comment">//数组展开</span>
<span class="hljs-keyword">const</span> arr1 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">const</span> arr2 = [...arr1,<span class="hljs-number">4</span>]; <span class="hljs-comment">// [1,2,3,4]</span>

<span class="hljs-comment">//对象展开</span>
<span class="hljs-keyword">const</span> obj1 = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-keyword">const</span> obj2 = &#123;...obj1,<span class="hljs-attr">c</span>:<span class="hljs-number">3</span>&#125;; <span class="hljs-comment">// &#123;a: 1, b: 2, c: 3&#125;</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>偷懒操作：使用展开运算符，代替部分api功能，减少 api 的记忆</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//替换arr.concat()</span>
<span class="hljs-keyword">const</span> arr3 = [...arr1,...arr2]; <span class="hljs-comment">//等价 const arr3 = arr1.concat(arr2);</span>

<span class="hljs-comment">//替换arr.slice()</span>
<span class="hljs-keyword">const</span> arr3 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>].slice(<span class="hljs-number">2</span>) <span class="hljs-comment">//等价 [1,2,arr3]= [1,2,3,4]</span>
<span class="hljs-keyword">const</span> arr3 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>].slice(<span class="hljs-number">1</span>,<span class="hljs-number">3</span>) <span class="hljs-comment">//等价 [1,arr3,4]= [1,2,3,4]</span>

<span class="hljs-comment">//替换arr.push()</span>
<span class="hljs-keyword">const</span> arr3 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>].push(arr)<span class="hljs-comment">//等价 arr3 = [1,2,3,4,arr]</span>

<span class="hljs-comment">//替换 Object.assign() 相同</span>
<span class="hljs-keyword">const</span> obj3 = &#123;...obj1,...obj2&#125; <span class="hljs-comment">//等价 const obj3 = Object.assign(&#123;&#125;,obj1,obj2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>展开运算符除了能对字符串，数组，对象展开外，还能将剩余参数重新收集为数组和对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数调用时使用(剩余参数)</span>
<span class="hljs-keyword">let</span> a1=<span class="hljs-number">1</span>,a2=<span class="hljs-number">2</span>,a3=<span class="hljs-number">3</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a1,...arr</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(arr)<span class="hljs-comment">// [2,3]</span>
    <span class="hljs-keyword">return</span> a1*<span class="hljs-number">2</span> + arr.reduce(<span class="hljs-function">(<span class="hljs-params">a,b</span>)=></span>a+b) 
&#125;
sum(a1,a2,a3) <span class="hljs-comment">// 7</span>

<span class="hljs-comment">// 数组收集</span>
[<span class="hljs-number">1</span>, ...arr] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]  <span class="hljs-comment">// arr=[2,3,4]</span>
<span class="hljs-comment">//对象收集</span>
&#123; <span class="hljs-attr">a</span> : <span class="hljs-number">1</span> , ...obj &#125; = &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125; <span class="hljs-comment">//obj=&#123;b:2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mdn 文档：<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Spread_syntax" target="_blank" rel="nofollow noopener noreferrer">展开运算符</a>  <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/Rest_parameters" target="_blank" rel="nofollow noopener noreferrer">剩余参数</a></p></div>  
</div>
            