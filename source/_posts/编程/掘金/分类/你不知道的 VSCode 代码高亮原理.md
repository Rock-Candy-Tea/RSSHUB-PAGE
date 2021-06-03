
---
title: '你不知道的 VSCode 代码高亮原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccf8c3497c82473182529a9b334a0024~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 03:01:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccf8c3497c82473182529a9b334a0024~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><blockquote>
<p>全文5000字，解读 vscode 背后的代码高亮实现原理，欢迎点赞关注转发。</p>
</blockquote>
<p>Vscode 的代码高亮、代码补齐、错误诊断、跳转定义等语言功能由两种扩展方案协同实现，包括：</p>
<ul>
<li>基于词法分析技术，识别分词 token 并应用高亮样式</li>
<li>基于可编程语言特性接口，识别代码语义并应用高亮样式，此外还能实现错误诊断、智能提示、格式化等功能</li>
</ul>
<p>两种方案的功能范畴逐级递增，相应地技术复杂度与实现成本也逐级升高，本文将概要介绍两种方案的工作过程与特点，各自完成什么工作，互相这么写作，并结合实际案例一步步揭开 vscode 代码高亮功能的实现原理：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccf8c3497c82473182529a9b334a0024~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">Vscode 插件基础</h1>
<p>介绍 vscode 代码高亮原理之前，有必要先熟悉一下 vscode 的底层架构。与 Webpack 相似，vscode 本身只是实现了一套架子，架子内部的命令、样式、状态、调试等功能都以插件形式提供，vscode 对外提供了五种拓展能力：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22da5f25b7dc430d9837437e2e198aae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中，代码高亮功能由 <strong>语言扩展</strong> 类插件实现，根据实现方式又可以细分为：</p>
<ul>
<li><strong>声明式</strong> ：以特定 JSON 结构声明一堆匹配词法的正则，无需编写逻辑代码即可添加如块级匹配、自动缩进、语法高亮等语言特性，vscode 内置的 extendsions/css、extendsions/html 等插件都是基于声明式接口实现的</li>
<li><strong>编程式</strong> ：vscode 运行过程中会监听用户行为，在特定行为发生后触发事件回调，编程式语言扩展需要监听这些事件，动态分析文本内容并按特定格式返回代码信息</li>
</ul>
<p>声明式性能高，能力弱；编程式性能低，能力强。语言插件开发者通常可以混用，用声明式接口在最短时间内识别出词法 token，提供基本的语法高亮功能；之后用编程式接口动态分析内容，提供更高级特性比如错误诊断、智能提示等。</p>
<p>Vscode 中的声明式语言扩展基于 TextMate 词法分析引擎实现；编程式语言扩展则基于语义分析接口、<code>vscode.language.*</code> 接口、Language Server Protocol 协议三种方式实现，下面展开介绍每种技术方案的基本逻辑。</p>
<h1 data-id="heading-1">词法高亮</h1>
<p><strong>词法分析(Lexical Analysis)</strong> 是计算机学科中将字符序列转换为 <strong>标记(token)</strong> 序列的过程，而 <strong>标记(token)</strong> 是构成源代码的最小单位，词法分析技术在编译、IDE等领域有非常广泛的应用。</p>
<p>比如 vscode 的词法引擎分析出 token 序列后再根据 token 的类型应用高亮样式，这个过程可以简单划分为分词、样式应用两个步骤。</p>
<blockquote>
<p>参考资料：</p>
<ul>
<li><a href="https://macromates.com/manual/en/language%5C_grammars" target="_blank" rel="nofollow noopener noreferrer">macromates.com/manual/en/l…</a></li>
<li><a href="https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/languag…</a></li>
</ul>
</blockquote>
<h2 data-id="heading-2">分词</h2>
<p>分词过程本质上将一长串代码递归地拆解为具有特定含义、分类的字符串片段，比如 <code>+-*/%</code> 等操作符；<code>var/const</code> 等关键字；<code>1234</code> 或 <code>"tecvan"</code> 类型的常量值等，简单说就是从一段文本中识别出，什么地方有一个什么词。</p>
<p>Vscode 的词法分析基于 <a href="https://macromates.com/" target="_blank" rel="nofollow noopener noreferrer">TextMate</a> 引擎实现，功能比较复杂，可以简单划分为三个方面：基于正则的分词、复合分词规则、嵌套分词规则。</p>
<h3 data-id="heading-3">基本规则</h3>
<p>Vscode 底层的 <a href="https://macromates.com/" target="_blank" rel="nofollow noopener noreferrer">TextMate</a> 引擎基于 <a href="https://macromates.com/manual/en/regular_expressions" target="_blank" rel="nofollow noopener noreferrer">正则</a> 匹配实现分词功能，运行时逐行扫描文本内容，用预定义的 <a href="https://macromates.com/manual/en/language_grammars#language_rules" target="_blank" rel="nofollow noopener noreferrer">rule</a> 集合测试文本行中是否包含匹配特定正则的内容，例如对于下面的规则配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"patterns"</span>: [
        &#123;
            <span class="hljs-string">"name"</span>: <span class="hljs-string">"keyword.control"</span>,
            <span class="hljs-string">"match"</span>: <span class="hljs-string">"\b(if|while|for|return)\b"</span>
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例中，<code>patterns</code> 用于定义规则集合， <code>match</code> 属性定于用于匹配 token 的正则，<code>name</code> 属性声明该 token 的分类(scope)，TextMate 分词过程遇到匹配 <code>match</code> 正则的内容时，会将其看作单独 token 处理并分类为 <code>name</code> 声明的 <code>keyword.control</code> 类型。</p>
<p>上述示例会将 <code>if/while/for/return</code> 关键词识别为 <code>keyword.control</code> 类型，但无法识别其它关键字：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6026c626ee214ae79e49cee0e6ce51dc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 TextMate 语境中，scope 是一种 <code>.</code> 分割的层级结构，例如 <code>keyword</code> 与 <code>keyword.control</code> 形成父子层级，这种层级结构在样式处理逻辑中能实现一种类似 css 选择器的匹配，后面会讲到细节。</p>
<h3 data-id="heading-4">复合分词</h3>
<p>上述示例配置对象在 TextMate 语境下被称作 Language Rule，除了 <code>match</code> 用于匹配单行内容，还可以使用 <code>begin + end</code> 属性对匹配更复杂的跨行场景。从 <code>begin</code> 到 <code>end</code> 所识别到的范围内，都认为是 <code>name</code> 类型的 token，比如在 <a href="https://github.com/vuejs/vetur" target="_blank" rel="nofollow noopener noreferrer">vuejs/vetur</a> 插件的 <code>syntaxes/vue.tmLanguage.json</code> 文件中有这么一段配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"Vue"</span>,
    <span class="hljs-string">"scopeName"</span>: <span class="hljs-string">"source.vue"</span>,
    <span class="hljs-string">"patterns"</span>: [
        &#123;
          <span class="hljs-string">"begin"</span>: <span class="hljs-string">"(<)(style)(?![^/>]*/>\\s*$)"</span>,
          <span class="hljs-comment">// 虚构字段，方便解释</span>
          <span class="hljs-string">"name"</span>: <span class="hljs-string">"tag.style.vue"</span>,
          <span class="hljs-string">"beginCaptures"</span>: &#123;
            <span class="hljs-string">"1"</span>: &#123;
              <span class="hljs-string">"name"</span>: <span class="hljs-string">"punctuation.definition.tag.begin.html"</span>
            &#125;,
            <span class="hljs-string">"2"</span>: &#123;
              <span class="hljs-string">"name"</span>: <span class="hljs-string">"entity.name.tag.style.html"</span>
            &#125;
          &#125;,
          <span class="hljs-string">"end"</span>: <span class="hljs-string">"(</)(style)(>)"</span>,
          <span class="hljs-string">"endCaptures"</span>: &#123;
            <span class="hljs-string">"1"</span>: &#123;
              <span class="hljs-string">"name"</span>: <span class="hljs-string">"punctuation.definition.tag.begin.html"</span>
            &#125;,
            <span class="hljs-string">"2"</span>: &#123;
              <span class="hljs-string">"name"</span>: <span class="hljs-string">"entity.name.tag.style.html"</span>
            &#125;,
            <span class="hljs-string">"3"</span>: &#123;
              <span class="hljs-string">"name"</span>: <span class="hljs-string">"punctuation.definition.tag.end.html"</span>
            &#125;
          &#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置中，<code>begin</code> 用于匹配 <code><style></code> 语句，<code>end</code> 用于匹配 <code></style></code> 语句，且 <code><style></style></code> 整个语句被赋予 scope 为 <code>tag.style.vue</code> 。此外，语句中字符被 <code>beginCaptures</code> 、<code>endCaptures</code> 属性分配成不同的 scope 类型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8ec645ae2e6469f83cbc45c95da7a48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里从 <code>begin</code> 到 <code>beginCaptures</code> ，从 <code>end</code> 到 <code>endCaptures</code> 形成了某种程度的复合结构，从而实现一次匹配多行内容。</p>
<h3 data-id="heading-5">规则嵌套</h3>
<p>在上述 <code>begin + end</code> 基础上，TextMate 还支持以子 <code>patterns</code> 方式定义嵌套的语言规则，例如：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"lng"</span>,
    <span class="hljs-attr">"patterns"</span>: [
        &#123;
            <span class="hljs-attr">"begin"</span>: <span class="hljs-string">"^lng`"</span>,
            <span class="hljs-attr">"end"</span>: <span class="hljs-string">"`"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"tecvan.lng.outline"</span>,
            <span class="hljs-attr">"patterns"</span>: [
                &#123;
                    <span class="hljs-attr">"match"</span>: <span class="hljs-string">"tec"</span>,
                    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"tecvan.lng.prefix"</span>
                &#125;,
                &#123;
                    <span class="hljs-attr">"match"</span>: <span class="hljs-string">"van"</span>,
                    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"tecvan.lng.name"</span>
                &#125;
            ]
        &#125;
    ],
    <span class="hljs-attr">"scopeName"</span>: <span class="hljs-string">"tecvan"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置识别 <code>lng` </code> 到 <code>`</code> 之间的字符串，并分类为 <code>tecvan.lng.outline</code> 。之后，递归处理两者之间的内容并按照子 <code>patterns</code> 规则匹配出更具体的 token ，例如对于：</p>
<pre><code class="copyable">lng`awesome tecvan`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可识别出分词：</p>
<ul>
<li><code>lng`awesome tecvan` </code> ，scope 为 <code>tecvan.lng.outline</code></li>
<li><code>tec</code> ，scope 为 <code>tecvan.lng.prefix</code></li>
<li><code>van</code> ，scope 为 <code>tecvan.lng.name</code></li>
</ul>
<p>TextMate 还支持语言级别的嵌套，例如：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"lng"</span>,
    <span class="hljs-attr">"patterns"</span>: [
        &#123;
            <span class="hljs-attr">"begin"</span>: <span class="hljs-string">"^lng`"</span>,
            <span class="hljs-attr">"end"</span>: <span class="hljs-string">"`"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"tecvan.lng.outline"</span>,
            <span class="hljs-attr">"contentName"</span>: <span class="hljs-string">"source.js"</span>
        &#125;
    ],
    <span class="hljs-attr">"scopeName"</span>: <span class="hljs-string">"tecvan"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于上述配置， <code>lng` </code> 到 <code>`</code> 之间的内容都会识别为 <code>contentName</code> 指定的 <code>source.js</code> 语句。</p>
<h2 data-id="heading-6">样式</h2>
<p>词法高亮本质上就是先按上述规则将原始文本拆解成多个具类的 token 序列，之后按照 token 的类型适配不同的样式。TextMate 在分词基础上提供了一套按照 token 类型字段 scope 配置样式的功能结构，例如：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"tokenColors"</span>: [
        &#123;
            <span class="hljs-attr">"scope"</span>: <span class="hljs-string">"tecvan"</span>,
            <span class="hljs-attr">"settings"</span>: &#123;
                <span class="hljs-attr">"foreground"</span>: <span class="hljs-string">"#eee"</span>
            &#125;
        &#125;,
        &#123;
            <span class="hljs-attr">"scope"</span>: <span class="hljs-string">"tecvan.lng.prefix"</span>,
            <span class="hljs-attr">"settings"</span>: &#123;
                <span class="hljs-attr">"foreground"</span>: <span class="hljs-string">"#F44747"</span>
            &#125;
        &#125;,
        &#123;
            <span class="hljs-attr">"scope"</span>: <span class="hljs-string">"tecvan.lng.name"</span>,
            <span class="hljs-attr">"settings"</span>: &#123;
                <span class="hljs-attr">"foreground"</span>: <span class="hljs-string">"#007acc"</span>,
            &#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例中，<code>scope</code> 属性支持一种被称作 <strong>Scope Selectors</strong> 的匹配模式，这种模式与 css 选择器类似，支持：</p>
<ul>
<li>元素选择，例如 <code>scope = tecvan.lng.prefix</code> 能够匹配 <code>tecvan.lng.prefix</code> 类型的token；特别的 <code>scope = tecvan</code> 能够匹配 <code>tecvan.lng</code> 、<code>tecvan.lng.prefix</code> 等子类型的 token</li>
<li>后代选择，例如 <code>scope = text.html source.js</code> 用于匹配 html 文档中的 JavaScript 代码</li>
<li>分组选择，例如 <code>scope = string, comment</code> 用于匹配字符串或备注</li>
</ul>
<p>插件开发者可以自定义 scope 也可以选择复用 TextMate 内置的许多 scope ，包括 comment、constant、entity、invalid、keyword 等，完整列表请查阅 <a href="https://macromates.com/manual/en/language_grammars#naming_conventions" target="_blank" rel="nofollow noopener noreferrer">官网</a>。</p>
<p><code>settings</code> 属性则用于设置该 token 的表现样式，支持foreground、background、bold、italic、underline 等样式属性。</p>
<h2 data-id="heading-7">实例解析</h2>
<p>看完原理我们来拆解一个实际案例： <a href="https://github.com/mrmlnc/vscode-json5" target="_blank" rel="nofollow noopener noreferrer">github.com/mrmlnc/vsco…</a> ，<a href="https://json5.org/" target="_blank" rel="nofollow noopener noreferrer">json5</a> 是 JSON 扩展协议，旨在使人类更易于手动编写和维护，支持备注、单引号、十六进制数字等特性，这些拓展特性需要使用 vscode-json5 插件实现高亮效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f97fe4041000429e9800d0dad66b3901~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中，左边是没有启动 vscode-json5 的效果，右边是启动后的效果。</p>
<p>vscode-json5 插件源码很简单，两个关键点：</p>
<ul>
<li>在 <code>package.json</code> 文件中声明插件的 <code>contributes</code> 属性，可以理解为插件的入口：</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"contributes"</span>: &#123;
    <span class="hljs-comment">// 语言配置</span>
    <span class="hljs-attr">"languages"</span>: [&#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-string">"json5"</span>,
      <span class="hljs-attr">"aliases"</span>: [<span class="hljs-string">"JSON5"</span>, <span class="hljs-string">"json5"</span>],
      <span class="hljs-attr">"extensions"</span>: [<span class="hljs-string">".json5"</span>],
      <span class="hljs-attr">"configuration"</span>: <span class="hljs-string">"./json5.configuration.json"</span>
    &#125;],
    <span class="hljs-comment">// 语法配置</span>
    <span class="hljs-attr">"grammars"</span>: [&#123;
      <span class="hljs-attr">"language"</span>: <span class="hljs-string">"json5"</span>,
      <span class="hljs-attr">"scopeName"</span>: <span class="hljs-string">"source.json5"</span>,
      <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./syntaxes/json5.json"</span>
    &#125;]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在语法配置文件 <code>./syntaxes/json5.json</code> 中按照 TextMate 的要求定义 Language Rule：</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"scopeName"</span>: <span class="hljs-string">"source.json5"</span>,
    <span class="hljs-attr">"fileTypes"</span>: [<span class="hljs-string">"json5"</span>],
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"JSON5"</span>,
    <span class="hljs-attr">"patterns"</span>: [
        &#123; <span class="hljs-attr">"include"</span>: <span class="hljs-string">"#array"</span> &#125;,
        &#123; <span class="hljs-attr">"include"</span>: <span class="hljs-string">"#constant"</span> &#125;
        <span class="hljs-comment">// ...</span>
    ],
    <span class="hljs-attr">"repository"</span>: &#123;
        <span class="hljs-attr">"array"</span>: &#123;
            <span class="hljs-attr">"begin"</span>: <span class="hljs-string">"\\["</span>,
            <span class="hljs-attr">"beginCaptures"</span>: &#123;
                <span class="hljs-attr">"0"</span>: &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"punctuation.definition.array.begin.json5"</span> &#125;
            &#125;,
            <span class="hljs-attr">"end"</span>: <span class="hljs-string">"\\]"</span>,
            <span class="hljs-attr">"endCaptures"</span>: &#123;
                <span class="hljs-attr">"0"</span>: &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"punctuation.definition.array.end.json5"</span> &#125;
            &#125;,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"meta.structure.array.json5"</span>
            <span class="hljs-comment">// ...</span>
        &#125;,
        <span class="hljs-attr">"constant"</span>: &#123;
            <span class="hljs-attr">"match"</span>: <span class="hljs-string">"\\b(?:true|false|null|Infinity|NaN)\\b"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"constant.language.json5"</span>
        &#125; 
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，结束了，没了，就是这么简单，之后 vscode 就可以根据这份配置适配 json5 的语法高亮规则。</p>
<h2 data-id="heading-8">调试工具</h2>
<p>Vscode 内置了一套 scope inspect 工具，用于调试 TextMate 检测出的 token、scope 信息，使用时只需要将编辑器光标 focus 到特定 token 上，快捷键 <code>ctrl + shift + p</code> 打开 vscode 命令面板后输出 <code>Developer: Inspect Editor Tokens and Scopes</code> 命令并回车：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/805fed9202ab47f0bda86c1685c8fdcd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>命令运行后就可以看到分词 token 的语言、scope、样式等信息。</p>
<h1 data-id="heading-9">编程式语言扩展</h1>
<p>词法分析引擎 TextMate 本质上是一种基于正则的静态词法分析器，优点是接入方式标准化，成本低且运行效率较高，缺点是静态代码分析很难实现某些上下文相关的 IDE 功能，例如对于下面的代码：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b67d720dfa94c42b62dabb701b77e96~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意代码第一行函数参数 <code>languageModes</code> 与第二行函数体内的 <code>languageModes</code> 是同一实体但是没有实现相同的样式，视觉上没有形成联动。</p>
<p>为此，vscode 在 TextMate 引擎之外提供了三种更强大也更复杂的语言特性扩展机制：</p>
<ul>
<li>使用 <code>DocumentSemanticTokensProvider</code> 实现可编程的语义分析</li>
<li>使用 <code>vscode.languages.*</code> 下的接口监听各类编程行为事件，在特定时间节点实现语义分析</li>
<li>根据 <a href="https://microsoft.github.io/language-server-protocol/" target="_blank" rel="nofollow noopener noreferrer">Language Server Protocol</a> 协议实现一套完备的语言特性分析服务器</li>
</ul>
<p>相比于上面介绍的声明式的词法高亮，语言特性接口更灵活，能够实现诸如错误诊断、候选词、智能提示、定义跳转等高级功能。</p>
<blockquote>
<p>参考资料：</p>
<ul>
<li><a href="https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/languag…</a></li>
<li><a href="https://code.visualstudio.com/api/language-extensions/programmatic-language-features" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/languag…</a></li>
<li><a href="https://code.visualstudio.com/api/language-extensions/language-server-extension-guide" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/languag…</a></li>
</ul>
</blockquote>
<h2 data-id="heading-10">DocumentSemanticTokensProvider 分词</h2>
<h3 data-id="heading-11">简介</h3>
<p><strong>Sematic Tokens Provider</strong> 是 vscode 内置的一种对象协议，它需要自行扫描代码文件内容，然后以整数数组形式返回语义 token 序列，告诉 vscode 在文件的哪一行、那一列、多长的区间内是一个什么类型的 token。</p>
<p>注意区分一下，TextMate 中的扫描是引擎驱动的，逐行匹配正则，而 <strong>Sematic Tokens Provider</strong> 场景下扫描规则、匹配规则都交由插件开发者自行实现，灵活性增强但相对的开发成本也会更高。</p>
<p>实现上，<strong>Sematic Tokens Provider</strong> 以 <code>vscode.DocumentSemanticTokensProvider</code> 接口定义，开发者可以按需实现两个方法：</p>
<ul>
<li><code>provideDocumentSemanticTokens</code> ：全量分析代码文件语义</li>
<li><code>provideDocumentSemanticTokensEdits</code> ：增量分析正在编辑模块的语义</li>
</ul>
<p>我们来看个完整的示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;

<span class="hljs-keyword">const</span> tokenTypes = [<span class="hljs-string">'class'</span>, <span class="hljs-string">'interface'</span>, <span class="hljs-string">'enum'</span>, <span class="hljs-string">'function'</span>, <span class="hljs-string">'variable'</span>];
<span class="hljs-keyword">const</span> tokenModifiers = [<span class="hljs-string">'declaration'</span>, <span class="hljs-string">'documentation'</span>];
<span class="hljs-keyword">const</span> legend = <span class="hljs-keyword">new</span> vscode.SemanticTokensLegend(tokenTypes, tokenModifiers);

<span class="hljs-keyword">const</span> provider: vscode.DocumentSemanticTokensProvider = &#123;
  provideDocumentSemanticTokens(
    <span class="hljs-built_in">document</span>: vscode.TextDocument
  ): vscode.ProviderResult<vscode.SemanticTokens> &#123;
    <span class="hljs-keyword">const</span> tokensBuilder = <span class="hljs-keyword">new</span> vscode.SemanticTokensBuilder(legend);
    tokensBuilder.push(      
      <span class="hljs-keyword">new</span> vscode.Range(<span class="hljs-keyword">new</span> vscode.Position(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>), <span class="hljs-keyword">new</span> vscode.Position(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>)),
      tokenTypes[<span class="hljs-number">0</span>],
      [tokenModifiers[<span class="hljs-number">0</span>]]
    );
    <span class="hljs-keyword">return</span> tokensBuilder.build();
  &#125;
&#125;;

<span class="hljs-keyword">const</span> selector = &#123; <span class="hljs-attr">language</span>: <span class="hljs-string">'javascript'</span>, <span class="hljs-attr">scheme</span>: <span class="hljs-string">'file'</span> &#125;;

vscode.languages.registerDocumentSemanticTokensProvider(selector, provider, legend);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信大多数读者对这段代码都会觉得陌生，我想了很久，觉得还是从函数输出的角度开始讲起比较容易理解，也就是上例代码第 17 行 <code>tokensBuilder.build()</code>。</p>
<h3 data-id="heading-12">输出结构</h3>
<p><code>provideDocumentSemanticTokens</code> 函数要求返回一个整数数组，数组项按 5 位为一组分别表示：</p>
<ul>
<li>第 <code>5 * i</code> 位，token 所在行相对于上一个 token 的偏移</li>
<li>第 <code>5 * i + 1</code> 位，token 所在列相对于上一个 token 的偏移</li>
<li>第 <code>5 * i + 2</code> 位，token 长度</li>
<li>第 <code>5 * i + 3</code> 位，token 的 type 值</li>
<li>第 <code>5 * i + 4</code> 位，token 的 modifier 值</li>
</ul>
<p>我们需要理解这是一个位置强相关的整数数组，数组中每 5 个项描述一个 token 的位置、类型。token 位置由所在行、列、长度三个数字组成，而为了压缩数据的大小 vscode 有意设计成相对位移的形式，例如对于这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name <span class="hljs-keyword">as</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如只是简单地按空格分割，那么这里可以解析出三个 token：<code>const</code> 、 <code>name</code> 、<code>as</code> ，对应的描述数组为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
<span class="hljs-comment">// 对应第一个 token：const</span>
<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">5</span>, x, x,
<span class="hljs-comment">// 对应第二个 token： name</span>
<span class="hljs-number">0</span>, <span class="hljs-number">6</span>, <span class="hljs-number">4</span>, x, x,
<span class="hljs-comment">// 第三个 token：as</span>
<span class="hljs-number">0</span>, <span class="hljs-number">5</span>, <span class="hljs-number">2</span>, x, x
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里是以相对前一个 token 位置的形式描述的，比如 <code>as</code> 字符对应的 5 个数字的语义为：相对前一个 token 偏移 0 行、5 列，长度为 2 ，类型为 xx。</p>
<p>剩下的第 <code>5 * i + 3</code> 位与第 <code>5 * i + 4</code> 位分别描述 token 的 type 与 modifier，其中 type 指示 token 的类型，例如 comment、class、function、namespace 等等；modifier 是类型基础上的修饰器，可以近似理解为子类型，比如对于 class 有可能是 abstract 的，也有可能是从标准库导出 defaultLibrary。</p>
<p>type、modifier 的具体数值需要开发者自行定义，例如上例中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tokenTypes = [<span class="hljs-string">'class'</span>, <span class="hljs-string">'interface'</span>, <span class="hljs-string">'enum'</span>, <span class="hljs-string">'function'</span>, <span class="hljs-string">'variable'</span>];
<span class="hljs-keyword">const</span> tokenModifiers = [<span class="hljs-string">'declaration'</span>, <span class="hljs-string">'documentation'</span>];
<span class="hljs-keyword">const</span> legend = <span class="hljs-keyword">new</span> vscode.SemanticTokensLegend(tokenTypes, tokenModifiers);

<span class="hljs-comment">// ...</span>

vscode.languages.registerDocumentSemanticTokensProvider(selector, provider, legend);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过 <code>vscode. SemanticTokensLegend</code> 类构建 type、modifier 的内部表示 <code>legend</code> 对象，之后使用 <code>vscode.languages.registerDocumentSemanticTokensProvider</code> 接口与 provider 一起注册到 vscode 中。</p>
<h3 data-id="heading-13">语义分析</h3>
<p>上例中 <code>provider</code> 的主要作用就是遍历分析文件内容，返回符合上述规则的整数数组，vscode 对具体的分析方法并没有做限定，只是提供了用于构建 token 描述数组的工具 <code>SemanticTokensBuilder</code>，例如上例中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> provider: vscode.DocumentSemanticTokensProvider = &#123;
  provideDocumentSemanticTokens(
    <span class="hljs-built_in">document</span>: vscode.TextDocument
  ): vscode.ProviderResult<vscode.SemanticTokens> &#123;
    <span class="hljs-keyword">const</span> tokensBuilder = <span class="hljs-keyword">new</span> vscode.SemanticTokensBuilder(legend);
    tokensBuilder.push(      
      <span class="hljs-keyword">new</span> vscode.Range(<span class="hljs-keyword">new</span> vscode.Position(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>), <span class="hljs-keyword">new</span> vscode.Position(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>)),
      tokenTypes[<span class="hljs-number">0</span>],
      [tokenModifiers[<span class="hljs-number">0</span>]]
    );
    <span class="hljs-keyword">return</span> tokensBuilder.build();
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码使用 SemanticTokensBuilder 接口构建并返回了一个 <code>[0, 3, 5, 0, 0]</code> 的数组，即第 0 行，第 3 列，长度为 5 的字符串，type =0，modifier = 0，运行效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd75ac102c44251bee74ee981226e76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了这一段被识别出的 token 外，其它字符都被认为不可识别。</p>
<h3 data-id="heading-14">小结</h3>
<p>本质上，<code>DocumentSemanticTokensProvider</code> 只是提供了一套粗糙的 IOC 接口，开发者能做的事情比较有限，所以现在大多数插件都没有采用这种方案，读者理解即可，不必深究。</p>
<h2 data-id="heading-15">Language API</h2>
<h3 data-id="heading-16">简介</h3>
<p>相对而言，<code>vscode.languages.*</code> 系列 API 所提供的语言扩展能力可能更符合前端开发者的思维习惯。<code>vscode.languages.*</code> 托管了一系列用户交互行为的处理、归类逻辑，并以事件接口方式开放出来，插件开发者只需监听这些事件，根据参数推断语言特性，并按规则返回结果即可。</p>
<p>Vscode Language API 提供了很多事件接口，比如说：</p>
<ul>
<li>registerCompletionItemProvider： 提供代码补齐提示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/603340cdc4204c0ab738eb5796b45080~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>registerHoverProvider：光标停留在 token 上时触发</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e3ff096d98042d6a39f45ef444f543d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>registerSignatureHelpProvider：提供函数签名提示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40ac6f0746234036930d537c3d191559~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整的列表请查阅 <a href="https://code.visualstudio.com/api/language-extensions/programmatic-language-features#show-hovers" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/languag…</a> 一文。</p>
<h3 data-id="heading-17">Hover 示例</h3>
<p>Hover 功能实现分两步，首先需要在 <code>package.json</code> 中声明 hover 特性：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    ...
    <span class="hljs-attr">"main"</span>: <span class="hljs-string">"out/extensions.js"</span>,
    <span class="hljs-attr">"capabilities"</span> : &#123;
        <span class="hljs-attr">"hoverProvider"</span> : <span class="hljs-string">"true"</span>,
        ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，需要在 <code>activate</code> 函数中调用 <code>registerHoverProvider</code> 注册 hover 回调：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">ctx: vscode.ExtensionContext</span>): <span class="hljs-title">void</span> </span>&#123;
    ...
    vscode.languages.registerHoverProvider(<span class="hljs-string">'language name'</span>, &#123;
        <span class="hljs-function"><span class="hljs-title">provideHover</span>(<span class="hljs-params"><span class="hljs-built_in">document</span>, position, token</span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">contents</span>: [<span class="hljs-string">'aweome tecvan'</span>] &#125;;
        &#125;
    &#125;);
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05a9897b07b14371b3025e84df934111~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其它特性功能的写法与此相似，感兴趣的同学建议到官网自行查阅。</p>
<h2 data-id="heading-18">Language Server Protocol</h2>
<h3 data-id="heading-19">简介</h3>
<p>上述基于语言扩展插件的代码高亮方法有一个相似的问题：难以在编辑器间复用，同一个语言，需要根据编辑器环境、语言重复编写功能相似的支持插件，那么对于 n 种语言，m 中编辑器，这里面的开发成本就是 <code>n * m</code>。</p>
<p>为了解决这个问题，微软提出了一种叫做 Language Server Protocol 的标准协议，语言功能插件与编辑器之间不再直接通讯，而是通过 LSP 做一层隔离：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04486a22ede94b378053cf02d4f5c8d6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>增加 LSP 层带来两个好处：</p>
<ul>
<li>LSP 层的开发语言、环境等与具体 IDE 所提供的 host 环境脱耦</li>
<li>语言插件的核心功能只需要编写一次，就可以复用到支持 LSP 协议的 IDE 中</li>
</ul>
<p>虽然 LSP 与上述 Language API 能力上几乎相同，但借助这两个优点大大提升了插件的开发效率，目前很多 vscode 语言类插件都已经迁移到 LSP 实现，包括 vetur、eslint、Python for VSCode 等知名插件。</p>
<p>Vscode 中的 LSP 架构包含两部分：</p>
<ul>
<li>Language Client: 一个标准 vscode 插件，实现与 vscode 环境的交互，例如 hover 事件首先会传递到 client，再由 client 传递到背后的 server</li>
<li>Language Server: 语言特性的核心实现，通过 LSP 协议与 Language Client 通讯，注意 Server 实例会以单独进程方式运行</li>
</ul>
<p>做个类比，LSP 就是经过架构优化的 Language API，原来由单个 provider 函数实现的功能拆解为 Client + Server 两端跨语言架构，Client 与 vscode 交互并实现请求转发；Server 执行代码分析动作，并提供高亮、补全、提示等功能，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f791e3553ca403cab7ecc1ac71506e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">简单示例</h3>
<p>LSP 稍微有一点点复杂，建议读者先拉下 vscode 官方示例对比学习：</p>
<pre><code class="hljs language-sh copyable" lang="sh">git <span class="hljs-built_in">clone</span> https://github.com/microsoft/vscode-extension-samples.git
<span class="hljs-built_in">cd</span> vscode-extension-samples/lsp-sample
yarn
yarn compile
code .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vscode-extension-samples/lsp-sample 的主要代码文件有：</p>
<pre><code class="hljs language-sh copyable" lang="sh">.
├── client // Language Client
│   ├── src
│   │   └── extension.ts // Language Client 入口文件
├── package.json 
└── server // Language Server
    └── src
        └── server.ts // Language Server 入口文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样例代码中有几个关键点：</p>
<ol>
<li>在 <code>package.json</code> 中声明激活条件与插件入口</li>
<li>编写入口文件 <code>client/src/extension.ts</code>，启动 LSP 服务</li>
<li>编写 LSP 服务即 <code>server/src/server.ts</code> ，实现 LSP 协议</li>
</ol>
<p>逻辑上，vscode 会在加载插件时根据 <code>package.json</code> 的配置判断激活条件，之后加载、运行插件入口，启动 LSP 服务器。插件启动后，后续用户在 vscode 的交互行为会以标准事件，如 hover、completion、signature help 等方式触发插件的 client ，client 再按照 LSP 协议转发到 server 层。</p>
<p>下面我们拆开看看三个模块的细节。</p>
<h4 data-id="heading-21">入口配置</h4>
<p>示例 vscode-extension-samples/lsp-sample 中的 <code>package.json</code> 有两个关键配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"activationEvents"</span>: [
        <span class="hljs-string">"onLanguage:plaintext"</span>
    ],
    <span class="hljs-attr">"main"</span>: <span class="hljs-string">"./client/out/extension"</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中：</p>
<ul>
<li><code>activationEvents</code>： 声明插件的激活条件，代码中的 <code>onLanguage:plaintext</code> 意为打开 txt 文本文件时激活</li>
<li><code>main</code>： 插件的入口文件</li>
</ul>
<h4 data-id="heading-22">Client 样例</h4>
<p>示例 vscode-extension-samples/lsp-sample 中的 Client 入口代码，关键部分如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: ExtensionContext</span>) </span>&#123;
    <span class="hljs-comment">// Server 配置信息</span>
    <span class="hljs-keyword">const</span> serverOptions: ServerOptions = &#123;
        <span class="hljs-attr">run</span>: &#123; 
            <span class="hljs-comment">// Server 模块的入口文件</span>
            <span class="hljs-attr">module</span>: context.asAbsolutePath(
                path.join(<span class="hljs-string">'server'</span>, <span class="hljs-string">'out'</span>, <span class="hljs-string">'server.js'</span>)
            ), 
            <span class="hljs-comment">// 通讯协议，支持 stdio、ipc、pipe、socket</span>
            <span class="hljs-attr">transport</span>: TransportKind.ipc 
        &#125;,
    &#125;;

    <span class="hljs-comment">// Client 配置</span>
    <span class="hljs-keyword">const</span> clientOptions: LanguageClientOptions = &#123;
        <span class="hljs-comment">// 与 packages.json 文件的 activationEvents 类似</span>
        <span class="hljs-comment">// 插件的激活条件</span>
        <span class="hljs-attr">documentSelector</span>: [&#123; <span class="hljs-attr">scheme</span>: <span class="hljs-string">'file'</span>, <span class="hljs-attr">language</span>: <span class="hljs-string">'plaintext'</span> &#125;],
        <span class="hljs-comment">// ...</span>
    &#125;;

    <span class="hljs-comment">// 使用 Server、Client 配置创建代理对象</span>
    <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> LanguageClient(
        <span class="hljs-string">'languageServerExample'</span>,
        <span class="hljs-string">'Language Server Example'</span>,
        serverOptions,
        clientOptions
    );

    client.start();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码脉络很清晰，先是定义 Server、Client 配置对象，之后创建并启动了 <code>LanguageClient</code> 实例。从实例可以看到，Client 这一层可以做的很薄，在 Node 环境下大部分转发逻辑都被封装在 <code>LanguageClient</code> 类中，开发者无需关心细节。</p>
<h4 data-id="heading-23">Server 样例</h4>
<p>示例 vscode-extension-samples/lsp-sample 中的 Server 代码实现了错误诊断、代码补全功能，作为学习样例来说稍显复杂，所以我只摘抄出错误诊断部分的代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Server 层所有通讯都使用 createConnection 创建的 connection 对象实现</span>
<span class="hljs-keyword">const</span> connection = createConnection(ProposedFeatures.all);

<span class="hljs-comment">// 文档对象管理器，提供文档操作、监听接口</span>
<span class="hljs-comment">// 匹配 Client 激活规则的文档对象都会自动添加到 documents 对象中</span>
<span class="hljs-keyword">const</span> documents: TextDocuments<TextDocument> = <span class="hljs-keyword">new</span> TextDocuments(TextDocument);

<span class="hljs-comment">// 监听文档内容变更事件</span>
documents.onDidChangeContent(<span class="hljs-function"><span class="hljs-params">change</span> =></span> &#123;
    validateTextDocument(change.document);
&#125;);

<span class="hljs-comment">// 校验</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">validateTextDocument</span>(<span class="hljs-params">textDocument: TextDocument</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">void</span>> </span>&#123;
    <span class="hljs-keyword">const</span> text = textDocument.getText();
    <span class="hljs-comment">// 匹配全大写的单词</span>
    <span class="hljs-keyword">const</span> pattern = <span class="hljs-regexp">/\b[A-Z]&#123;2,&#125;\b/g</span>;
    <span class="hljs-keyword">let</span> m: RegExpExecArray | <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 这里判断，如果一个单词里面全都是大写字符，则报错</span>
    <span class="hljs-keyword">const</span> diagnostics: Diagnostic[] = [];
    <span class="hljs-keyword">while</span> ((m = pattern.exec(text))) &#123;
        <span class="hljs-keyword">const</span> diagnostic: Diagnostic = &#123;
            <span class="hljs-attr">severity</span>: DiagnosticSeverity.Warning,
            <span class="hljs-attr">range</span>: &#123;
                <span class="hljs-attr">start</span>: textDocument.positionAt(m.index),
                <span class="hljs-attr">end</span>: textDocument.positionAt(m.index + m[<span class="hljs-number">0</span>].length)
            &#125;,
            <span class="hljs-attr">message</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;m[<span class="hljs-number">0</span>]&#125;</span> is all uppercase.`</span>,
            <span class="hljs-attr">source</span>: <span class="hljs-string">'ex'</span>
        &#125;;
        diagnostics.push(diagnostic);
    &#125;

    <span class="hljs-comment">// 发送错误诊断信息</span>
    <span class="hljs-comment">// vscode 会自动完成错误提示渲染</span>
    connection.sendDiagnostics(&#123; <span class="hljs-attr">uri</span>: textDocument.uri, diagnostics &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LSP Server 代码的主要流程：</p>
<ul>
<li>调用 <code>createConnection</code> 建立与 vscode 主进程的通讯链路，后续所有的信息交互都基于 connection 对象实现。</li>
<li>创建 <code>documents</code> 对象，并根据需要监听文档事件如上例中的 <code>onDidChangeContent</code></li>
<li>在事件回调中分析代码内容，根据语言规则返回错误诊断信息，例如示例中使用正则判断单词是否全部为大写字母，是的话使用 <code>connection.sendDiagnostics</code> 接口发送错误提示信息</li>
</ul>
<p>运行效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/016fe2d4154d4d2392ea5daed9d93eb8~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-06-02 at 16.14.59.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-24">小结</h4>
<p>通览样例代码，LSP 客户端服务器之间的通讯过程都已经封装在 <code>LanguageClient</code> 、<code>connection</code> 等对象中，插件开发者并不需要关心底层实现细节，也不需要深入理解 LSP 协议即可基于这些对象暴露的接口、事件等实现简单的代码高亮效果。</p>
<h1 data-id="heading-25">总结</h1>
<p>Vscode 用插件方式提供了多种语言扩展接口，分声明式、编程式两类，在实际项目中通常会混合使用这两种技术，用基于 TextMate 的声明式接口迅速识别出代码中的词法；再用编程式接口如 LSP 补充提供诸如错误提示、代码补齐、跳转定义等高级功能。</p>
<p>这段时间看了不少开源 vscode 插件，其中 Vue 官方提供的 Vetur 插件学习是这方面的典型案例，学习价值极高，建议对这方面有兴趣的读者可以自行前往分析学习 vscode 语言扩展类插件的写法。</p>
<blockquote>
<p>往期文章</p>
<ul>
<li><a href="https://mp.weixin.qq.com/s/A0udBhvNoA0o-kX1B0rt9A" target="_blank" rel="nofollow noopener noreferrer">分享几个 Webpack 实用分析工具</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/372721645" target="_blank" rel="nofollow noopener noreferrer">[建议收藏] Webpack 4+ 优秀学习资料合集</a></li>
<li><a href="https://mp.weixin.qq.com/s/SbJNbSVzSPSKBe2YStn2Zw" target="_blank" rel="nofollow noopener noreferrer">[万字总结] 一文吃透 Webpack 核心原理</a></li>
<li><a href="https://mp.weixin.qq.com/s/tXkGx6Ckt9ucT2o8tNM-8w" target="_blank" rel="nofollow noopener noreferrer">[源码解读] Webpack 插件架构深度讲解</a></li>
<li><a href="https://mp.weixin.qq.com/s/QkXFOHNpL0PRQtCcWIaX-g" target="_blank" rel="nofollow noopener noreferrer">十分钟精进 Webpack：module.issuer 属性详解</a></li>
<li><a href="https://mp.weixin.qq.com/s/kr73Epnn6wAx9DH7KRVUaA" target="_blank" rel="nofollow noopener noreferrer">有点难的 webpack 知识点：Dependency Graph 深度解析</a></li>
<li><a href="https://mp.weixin.qq.com/s/dFrRY_ntUwmIOXzs8TYcFQ" target="_blank" rel="nofollow noopener noreferrer">有点难的知识点： Webpack Chunk 分包规则详解</a></li>
<li><a href="https://mp.weixin.qq.com/s/nkBvbwpzeb0fzG02HXta8A" target="_blank" rel="nofollow noopener noreferrer">Webpack 原理系列六： 彻底理解 Webpack 运行时</a></li>
<li><a href="https://mp.weixin.qq.com/s/TPWcB4MfVrTgFtVxsShNFA" target="_blank" rel="nofollow noopener noreferrer">Webpack 原理系列七：如何编写loader</a></li>
</ul>
</blockquote></div>  
</div>
            