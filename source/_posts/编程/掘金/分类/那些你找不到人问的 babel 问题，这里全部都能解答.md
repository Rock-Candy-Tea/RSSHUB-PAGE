
---
title: '那些你找不到人问的 babel 问题，这里全部都能解答'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673328522fd140da8aa53b459bfcaf4e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 08:08:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673328522fd140da8aa53b459bfcaf4e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.cn/book/6946117847848321055" target="_blank">《babel 插件通关秘籍》</a>的小册除了本身规划好的内容会写完之外，也会持续服务好读者，在微信群中会解答所有 babel 问题。</p>
<p>为了把一些回答积累下来，我决定在小册后加入一些 Q&A 的章节，来维护这些回答过的问题。（以下问题皆来自小册微信群内的真实提问）</p>
<h2 data-id="heading-0">问：分不清 esnext 中哪些是语法，哪些是 api 怎么办？怎么快速区分？</h2>
<p><strong>答：</strong> esnext 分为两部分，语法和 api。</p>
<h3 data-id="heading-1">api</h3>
<p>api 主要是对象和函数的形式，这是 js 一直以来就支持的语法。我们可以用 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer.net</a> 看一下他们的 AST。</p>
<p>比如这两个 api：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
[].includes();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new Map();</code> 是 NewExpression （new 表达式） 节点，它的 callee 属性是 Identifier （标识符）节点，（对于表达式和标识符不清楚的建议去看小册的第二节的 AST 详解），这两种 AST 都是早就支持的，不是新语法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673328522fd140da8aa53b459bfcaf4e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>[].includes()</code> 是 CallExpression（函数调用表达式）节点，其中 callee 属性是一个 MemberExpression（成员表达式），object 和 property 分别为 ArrayExpression（数组表达式） 和 Identifier（标识符），也都是早就支持的 AST，不是新语法。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bf4b7336104c7da40d634a17583587~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那什么是新语法呢？</p>
<h3 data-id="heading-2">语法</h3>
<p>新语法是新的代码结构，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">aaa::b() <span class="hljs-comment">// bind 表达式</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Aaa</span> </span>&#123;&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 class 声明语句 和 bind 表达式都是新语法，因为他们结构和已有的语法不同，所以也会用新的 AST 来表示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e01bcfcc8fd4406d9642914630b03843~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一条语句的 CallExpression 是早就支持的，但是 callee 属性的 BindExpression 却是新的 AST，这就是新语法。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cba5a72ee0f4f7eb9fd10521a9ff379~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的 ClassDeclaration 也是新的 AST，所以是新语法。</p>
<p><strong>api 一般是 polyfill 也就是 corejs 和 regenerator 来实现的，而语法则通过 helper 来实现。这三部分都是 runtime 包的组成部分。</strong></p>
<h3 data-id="heading-3">小结</h3>
<p>问问题的同学分不清什么是新语法什么是新 api，建议多用下 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer.net</a> 这个网站，从 AST 的类型上就可以看出来，如果是新的 AST，那么就是新语法，如果是早就支持的 AST，那么一般都是 api 的扩充。</p>
<p>当然，不用 AST 分析也同样应该能够分清楚。但是 AST 能够帮助你更好的理解代码结构。同学们多多用 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer.net</a>。</p>
<h2 data-id="heading-4">问：我引入了 polyfill 但是污染了全局，导致项目报错了，怎么解决？</h2>
<p><strong>答：</strong> 其实这个问题在小册的 “babel 的内置功能（下）” 中讲过了，可以去翻一翻。</p>
<p>@babel/preset-env 如果配置了 useBuiltIns 并指定了 corejs 版本的话会自动引入 polyfill，方式是设置到全局。</p>
<p>如果觉得全局的方式不符合需求，那么可以使用 @babel/plugin-transform-runtime 来解决，它会把全局注入的方式改成模块化引入的方式。</p>
<p>比如只引入 @babel/preset-env 时是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"@babel/preset-env"</span>, &#123; 
        <span class="hljs-string">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span>,
        <span class="hljs-string">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>,<span class="hljs-comment">// or "entry" or "false"</span>
        <span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>
    &#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec9dd003a7704245bb4b332edac65f1b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是加上 @babel/plugin-transform-runtime 插件之后就变成了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"plugins"</span>:[
        [<span class="hljs-string">"@babel/plugin-transform-runtime"</span>, &#123;
            <span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>
        &#125;]
    ],
    <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"@babel/preset-env"</span>, &#123; 
        <span class="hljs-string">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span>,
        <span class="hljs-string">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>,<span class="hljs-comment">// or "entry" or "false"</span>
        <span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>
    &#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fd9e6e2e2e74228a69ecbcdc82005bf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就不会再污染全局环境了。</p>
<h3 data-id="heading-5">彩蛋</h3>
<p>放个小彩蛋，上面的代码可以简写为 @babel/transform-runtime、@babel/env，有同学记得为什么么？可以在小册的评论区留言。</p>
<h2 data-id="heading-6">问：自动埋点的案例里面没有获取参数，是不是能完善一些呢？</h2>
<p><strong>答：</strong> 能问出这个问题的同学说明已经掌握了自动埋点的实现思路了。确实，案例中的代码不是标准答案，是为了帮大家理清思路，所以写的简单一些。</p>
<p>但是同学们完全可以根据自己的需求扩展，比如如果埋点需要参数，那是不是可以通过 scope 的 api 从作用域中取，是不是能做一些 AST 的静态分析呢？ 同学们完全可以做的更完善，根据自己的需求做修改。</p>
<p>所有的案例都是简化版，目的都是为了帮大家理清思路，希望大家能够在掌握 babel 的 api 和修改、分析 AST 的思路以后，自己去做一些有意义的自动化的东西，这才是目的。</p>
<h2 data-id="heading-7">总结</h2>
<p>我们梳理了通过 AST 来识别新语法还是 api 的思路，知道了如何把注入的 api 抽离出来，还思考了下自动注入埋点的扩展思路。这些都是同学们问的问题。</p>
<p><a href="https://juejin.cn/book/6946117847848321055" target="_blank">小册</a>的目的有两个，一个是把小册中原本的内容讲清楚，让同学们能吸收，另一个是解答大家的问题，根据大家的需求去完善小册。这样最终的小册一定是能够对大家有所帮助的。大家有问题可以加微信群问，那些你找不到人问的 babel 问题，在群里都可以得到解答。</p></div>  
</div>
            