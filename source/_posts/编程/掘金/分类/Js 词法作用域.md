
---
title: 'Js 词法作用域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92238891adcf4dbf9d2e89e78abd53d4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 05:04:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92238891adcf4dbf9d2e89e78abd53d4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h2 data-id="heading-0">词法作用域(Lexical Scope)</h2>
<p><strong>词法作用域(Lexical Scope)是 JavaScript 所采用的作用域模型</strong> . 词法作用域也称为静态作用域.</p>
<h3 data-id="heading-1">相应定义:</h3>
<p>1."functions are executed using the variable scope that was in effect when they were defined, not the variable scope that is in effect when they are invoked" - according to JavaScript Definition Guide.</p>
<p>​函数的执行依赖于函数定义的时候所产生的变量作用域， 而不是函数调用的时候产生的。</p>
<p>2.<strong>Lexical Scoping</strong> defines how variable names are resolved in nested functions: <strong>inner functions contain the scope of parent functions even if the parent function has returned</strong>(closure). - according to stackoverflow answer</p>
<p>​词法作用域定义了如何在嵌套函数中解析变量名：即使父函数已返回，内部函数仍包含父函数的作用域。</p>
<p>3.programming ("static scope") In a lexically scoped language, the &#123;scope&#125; of an &#123;identifier&#125; is fixed at &#123;compile time&#125; to some region in the &#123;source code&#125; containing the identifier's declaration. This means that an identifier is only accessible within that region (including procedures declared within it).</p>
<p>程序（“静态范围”）在词法作用域语言中，&#123;identifier&#125; 的 &#123;scope&#125; 在 &#123;compile time&#125; 就固定到 &#123;source code&#125; 中，包含标识符声明的某个区域。这意味着标识符只能在该区域内访问（包括在其中声明的过程）。</p>
<p>4.In lexical scoping (and if you're the interpreter), you search in the local function (the function which is running now), then you search in the function (or scope) in which that function was <em>defined,</em> then you search in the function (scope) in which <em>that</em> function was defined, and so forth.</p>
<p>"Lexical" here refers to <em>text,</em> in that you can find out what variable is being referred to by looking at the nesting of scopes in the program text.</p>
<p>在词法范围（如果你是解释器）中，你在当前函数（现在正在运行的函数）中搜索，然后在定义该函数的函数（或作用域）中搜索，然后在定义该函数的函数（作用域）中搜索，依此类推。</p>
<p>“词法”在这里指的是上下文，因为您可以通过查看程序上下文中作用域的嵌套来找出所引用的变量。</p>
<p>​</p>
<h3 data-id="heading-2">静态作用域:</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">// 输出 2 静态作用域</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
    foo();
&#125;
bar();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 foo 函数，先从 foo 函数内部查找是否有局部变量 a，如果没有，就查找全局变量，也就是 a 等于 2，所以结果会打印 2。</p>
<h3 data-id="heading-3">动态作用域:</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 伪代码</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    print a;<span class="hljs-comment">// 输出 3 而不是2 ！动态作用域关注函数从何处调用，其作用域链是基于运行时的调用栈的。</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
    foo();
&#125;

bar();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 foo 函数，依然是从 foo 函数内部查找是否有局部变量 a。如果没有，就从调用函数的作用域链，也就是 bar 函数内部查找 a 变量，所以结果会打印 3。</p>
<h3 data-id="heading-4">作用域查询:</h3>
<p><em>Lexical scope</em> means that in a nested group of functions, <strong>the inner functions have access to the variables and other resources of their parent scope</strong>. This means that the child's functions are lexically bound to the execution context of their parents.</p>
<p>词法作用域意味着在一组嵌套的函数中，内部函数可以访问其父作用域的变量和其他资源。 这意味着子函数在词法上绑定到其父函数的执行上下文。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">"outer"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">one</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> name = <span class="hljs-string">"middle"</span>;
  <span class="hljs-keyword">var</span> other = <span class="hljs-string">"findme"</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">two</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">"inner"</span>;
    <span class="hljs-comment">// Here `name` is "inner" and `other` is "findme"</span>
    <span class="hljs-built_in">console</span>.dir(&#123;<span class="hljs-attr">name</span>: name, <span class="hljs-attr">other</span>: other&#125;);
  &#125;
  two();
  <span class="hljs-comment">// Here `name` is "middle" and `other` is "findme"</span>
  <span class="hljs-built_in">console</span>.dir(&#123;<span class="hljs-attr">name</span>: name, <span class="hljs-attr">other</span>: other&#125;);
&#125;

one();
<span class="hljs-comment">// Here `name` is "outer" and `other` is not defined.</span>
<span class="hljs-built_in">console</span>.dir(&#123;<span class="hljs-attr">name</span>: name&#125;);
<span class="hljs-built_in">console</span>.dir(&#123;<span class="hljs-attr">other</span>: other&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92238891adcf4dbf9d2e89e78abd53d4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529195849061" loading="lazy" referrerpolicy="no-referrer">
<p><strong>一旦找到第一个匹配，作用域查询就停止了</strong>。相同的标识符名称可以在嵌套作用域的多个层中被指定，这称为“遮蔽（shadowing）”（内部的标识符“遮蔽”了外部的标识符）。无论如何遮蔽，作用域查询总是从当前被执行的最内侧的作用域开始，向外/向上不断查找，直到第一个匹配才停止。但是<strong>从外部看</strong>，<strong>内部的变量是未被定义的</strong>。</p>
<p>在不同执行上下文中具有相同名称的变量从执行堆栈的顶部到底部依次获得优先级。<strong>最内层函数</strong>中（执行堆栈的最顶层上下文）相同的名称将具有<strong>更高的优先级</strong>。</p>
<p>Another:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">grandfather</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">'Hammad'</span>;
    <span class="hljs-comment">// 'likes' is not accessible here</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parent</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 'name' is accessible here</span>
        <span class="hljs-comment">// 'likes' is not accessible here</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">child</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-comment">// Innermost level of the scope chain</span>
            <span class="hljs-comment">// 'name' is also accessible here</span>
            <span class="hljs-keyword">var</span> likes = <span class="hljs-string">'Coding'</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>词法作用域是<strong>向前工作</strong>的，这意味着 <code>name</code> 可以通过其子级的执行上下文访问。</p>
<p>但它不会<strong>向后返回</strong>到其父项，这意味着<strong>它的父项无法访问变量 likes</strong>。</p>
<h3 data-id="heading-5">AST直观理解</h3>
<h4 data-id="heading-6">back to the example of static scope</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
    foo();
&#125;
bar(); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0a500e1cafa42edb61a0804de2dc1da~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529202708712" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由图可知, 程序由四部分组成. 全局作用域下包含了变量声明 VariableDeclaration, 函数function foo(), 函数function bar(), 和执行语句 ExpreesionStatement( bar() ).</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bf4d344a0994b1eac704c380b4739ec~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529203132281" loading="lazy" referrerpolicy="no-referrer">
<p>变量声明部分, 在全局作用域中声明变量 identifier(a),  并将 2 赋值于a.</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b833c53304f840c2a4b4522a7bfb33b8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529203319338" loading="lazy" referrerpolicy="no-referrer">
<p>函数function foo() 部分. 其中执行 console.log(a)</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce4df00d9c714034aaaa9ee5c039bd41~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529203438150" loading="lazy" referrerpolicy="no-referrer">
<p>函数function bar()部分.</p>
<p>注意到在bar的函数作用域中, 又有一个新的 变量声明 identifier(a) , 并将 3 赋值于 a.</p>
<p>执行 foo()</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de79a25f5d4544dfb81364769e5b3459~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529203637661" loading="lazy" referrerpolicy="no-referrer">
<p>最后执行语句 ExpreesionStatement(bar () )</p>
<p>由于foo函数并不是在bar函数的嵌套函数内, 所以变量 a 在<strong>foo函数作用域</strong>中找不到此变量, 接着便直接从<strong>全局变量</strong>中寻找, 并找到2.</p>
<h4 data-id="heading-7">嵌套函数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> value = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> value = <span class="hljs-number">2</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(value);
    &#125;
    foo()
&#125;
bar() <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果为嵌套函数的话, 则将从当前子作用域依次向父作用域查找, 直到找到第一个<code>value</code>值(2)结束.</p>
<p>function bar() 部分的AST 如下:</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5561667d35984193bafadb2ef9be617c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529204421976" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-8">变量污染</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    a = <span class="hljs-number">3</span>;
    foo()
&#125;
bar() <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是重点注意 function bar() 部分的AST:</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e04eccd014e4a349ed76429cb602983~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210529205948750" loading="lazy" referrerpolicy="no-referrer">
<p>在这里并不再是变量声明 (VariableDeclaration)了, 而是 执行语句(ExpressionStatement). 因此执行bar函数的时候, 首先根据上下文顺序将 3 赋值于全局变量 a, 并通过foo函数 查找到全局变量 a = 3, 打印出了3. 局部变量修改了全局变量, 造成了<strong>变量污染</strong>.
这段代码也可以看作是在 function bar()函数作用域中再次(用var)声明了 a , 并将 3 赋值于 a, 而var 声明并没有块作用域的概念, 结果便是在全局作用域中创建了 a 变量. 如图所示:</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b1d4b5980a6441ab76f8a7afbac3513~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210617203816758" loading="lazy" referrerpolicy="no-referrer">
<p>这句 a = 3 具有神秘感 ! 让我验证了1个小时, 它究竟是什么, 还得不出结论..</p>
<p>REF：
​Lexical Scope:</p>
<p>​<a href="https://stackoverflow.com/questions/1047454/what-is-lexical-scope" target="_blank" rel="nofollow noopener noreferrer">stackoverflow.com/questions/1…</a></p>
<p>​<a href="http://howtonode.org/what-is-this" target="_blank" rel="nofollow noopener noreferrer">howtonode.org/what-is-thi…</a></p>
<p>​<a href="http://www.gnu.org/software/guile/manual/html_node/Lexical-Scope.html" target="_blank" rel="nofollow noopener noreferrer">www.gnu.org/software/gu…</a></p>
<p>​<a href="http://wiki.c2.com/?LexicalScoping" target="_blank" rel="nofollow noopener noreferrer">wiki.c2.com/?LexicalSco…</a></p>
<p>​<a href="http://wiki.c2.com/?DynamicScoping" target="_blank" rel="nofollow noopener noreferrer">wiki.c2.com/?DynamicSco…</a></p></div>  
</div>
            