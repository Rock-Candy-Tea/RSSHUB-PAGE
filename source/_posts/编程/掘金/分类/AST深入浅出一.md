
---
title: 'AST深入浅出一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10c12c574d3f4393bad8215148795796~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 01:06:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10c12c574d3f4393bad8215148795796~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是AST(抽象语法树)</h2>
<p>AST是一种分层的程序表示，根据编程语言的语法来呈现源代码结构，每个 AST 节点对应一个源代码项。</p>
<p>上面说法的确很抽象，可以看下面的代码表示，可以看出来源码和下面树中的节点是一一对应的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a,b</span>)</span>&#123;
<span class="hljs-keyword">return</span> a+b
&#125;
add(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 转换成语法树</span>
&#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Program"</span>,
    <span class="hljs-attr">"body"</span>: [
      &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"FunctionDeclaration"</span>,
        <span class="hljs-attr">"id"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
          <span class="hljs-attr">"start"</span>: <span class="hljs-number">9</span>,
          <span class="hljs-attr">"end"</span>: <span class="hljs-number">12</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"add"</span>
        &#125;,
        <span class="hljs-attr">"params"</span>: [
          &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
          &#125;,
          &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
          &#125;
        ],
        <span class="hljs-attr">"body"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"BlockStatement"</span>,
          <span class="hljs-attr">"body"</span>: [
            &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ReturnStatement"</span>,
              <span class="hljs-attr">"argument"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"BinaryExpression"</span>,
                <span class="hljs-attr">"left"</span>: &#123;
                  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
                &#125;,
                <span class="hljs-attr">"operator"</span>: <span class="hljs-string">"+"</span>,
                <span class="hljs-attr">"right"</span>: &#123;
                  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
                &#125;
              &#125;
            &#125;
          ]
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ExpressionStatement"</span>,
        <span class="hljs-attr">"expression"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
          <span class="hljs-attr">"callee"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"add"</span>
          &#125;,
          <span class="hljs-attr">"arguments"</span>: [
            &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Literal"</span>,
              <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>,
              <span class="hljs-attr">"raw"</span>: <span class="hljs-string">"1"</span>
            &#125;,
            &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Literal"</span>,
              <span class="hljs-attr">"value"</span>: <span class="hljs-number">2</span>,
              <span class="hljs-attr">"raw"</span>: <span class="hljs-string">"2"</span>
            &#125;
          ],
          <span class="hljs-attr">"optional"</span>: <span class="hljs-literal">false</span>
        &#125;
      &#125;
    ]
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">在线js转ast语法</a> 的网站，感兴趣可以体验下。</p>
<h2 data-id="heading-1">编译原理</h2>
<p>首先来看下浏览器的编译原理如下，可以看出来浏览器对js的编译和解释都需要源代码通过<strong>词法分析</strong>和<strong>语法分析</strong>转换成AST</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10c12c574d3f4393bad8215148795796~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">词法分析Tokenize</h3>
<p>词法分析：是计算机科学中将字符序列转换为单词（Token）序列的过程。进行词法分析的程序或者函数叫作词法分析器（Lexical analyzer，简称Lexer），也叫扫描器（Scanner）。</p>
<p>其作用是将一行行的源码拆解成一个个 token。所谓 token，指的是语法上不可能再分的、最小的单个字符或字符串。以上面代码为例子，以下就是生成的token序列：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31265a5c54544694900894056f299314~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">语法分析parse</h3>
<p>语法分析是编译过程的一个逻辑阶段。语法分析的任务是在词法分析的基础上将单词序列组合成各类语法短语，如“程序”，“语句”，“表达式”等等.语法分析程序判断源程序在结构上是否正确.</p>
<p>其作用是将上一步生成的 token 数据，根据<strong>语法规则</strong>转为 AST。同时也会去验证语法，语法有错的话会抛出语法错误</p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Mozilla/Projects/SpiderMonkey/Parser_API" target="_blank" rel="nofollow noopener noreferrer">parseApi</a></p>
<p>可以通过安装插件recast生成AST语法树</p>
<p><code>npm i recast -S </code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// c创建parse.js</span>
<span class="hljs-keyword">const</span> recast = <span class="hljs-built_in">require</span>(<span class="hljs-string">"recast"</span>);
<span class="hljs-keyword">const</span> code =
  <span class="hljs-string">`
  function add(a, b) &#123;
    return a + b
  &#125;
  add(1,2)
  `</span>
<span class="hljs-keyword">const</span> ast = recast.parse(code);
<span class="hljs-keyword">const</span> add  = ast.program.body
<span class="hljs-built_in">console</span>.log(add)
<span class="hljs-comment">// 运行 node parse.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/494bd5dbbfad483fba5b7d8ff7ce0dba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">AST用途</h2>
<ul>
<li>
<p>打包编译：webpack、rollup、babel等</p>
</li>
<li>
<p>语法检查：JSLint、JSHint、Prettier</p>
</li>
<li>
<p>IDE的错误提示、格式化、高亮、自动补全等</p>
</li>
<li>
<p>代码混淆压缩：UglifyJS2</p>
</li>
<li>
<p>多端开发框架：Mpvue、Taro等</p>
</li>
<li>
<p>...</p>
</li>
</ul></div>  
</div>
            