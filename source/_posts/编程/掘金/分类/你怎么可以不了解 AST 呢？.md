
---
title: '你怎么可以不了解 AST 呢？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 17:17:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank" title="https://juejin.cn/post/6963056815420473357#heading-0">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>周世铁，微医前端技术部医疗支撑组前端乱构师</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在我们编写业务代码的时候，可能很少人会使用到<code>AST</code>，以至于大多数同学都不大了解<code>AST</code>。有的同学曾经学过，但是不去实践的话，过段时间又忘的差不多了。看到这里，你会发现说的就是你。听说贵圈现在写文章都要编故事，时不时还要整点表情包。这是真的吗？作为公司最头铁的前端，我就不放。</p>
<blockquote>
<p>本文将通过以下几个方面对<code>AST</code>进行学习</p>
</blockquote>
<ol>
<li>
<p>基础知识</p>
<ul>
<li>
<p><code>AST</code>是什么</p>
</li>
<li>
<p><code>AST</code>有什么用</p>
</li>
<li>
<p><code>AST</code>如何生成</p>
</li>
</ul>
</li>
<li>
<p>实战小例子</p>
<ul>
<li>
<p>去掉<code>debugger</code></p>
</li>
<li>
<p>修改函数中执行的<code>console.log</code>参数</p>
</li>
</ul>
</li>
<li>
<p>总结</p>
</li>
</ol>
<h2 data-id="heading-1">基础知识</h2>
<h3 data-id="heading-2"><code>AST</code>是什么</h3>
<p>先贴下官方的解释</p>
<blockquote>
<p>在计算机科学中，抽象语法树（abstract syntax tree 或者缩写为 AST），或者语法树（syntax tree），是源代码的抽象语法结构的树状表现形式，这里特指编程语言的源代码。</p>
</blockquote>
<p>为了方便大家理解抽象语法树，来看看具体的例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> tree = <span class="hljs-string">'this is tree'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js 源代码将会被转化成下面的抽象语法树</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-string">"end"</span>: <span class="hljs-number">25</span>,
  <span class="hljs-string">"body"</span>: [
    &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>,
      <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-string">"end"</span>: <span class="hljs-number">25</span>,
      <span class="hljs-string">"declarations"</span>: [
        &#123;
          <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>,
          <span class="hljs-string">"start"</span>: <span class="hljs-number">4</span>,
          <span class="hljs-string">"end"</span>: <span class="hljs-number">25</span>,
          <span class="hljs-string">"id"</span>: &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-string">"start"</span>: <span class="hljs-number">4</span>,
            <span class="hljs-string">"end"</span>: <span class="hljs-number">8</span>,
            <span class="hljs-string">"name"</span>: <span class="hljs-string">"tree"</span>
          &#125;,
          <span class="hljs-string">"init"</span>: &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"Literal"</span>,
            <span class="hljs-string">"start"</span>: <span class="hljs-number">11</span>,
            <span class="hljs-string">"end"</span>: <span class="hljs-number">25</span>,
            <span class="hljs-string">"value"</span>: <span class="hljs-string">"this is tree"</span>,
            <span class="hljs-string">"raw"</span>: <span class="hljs-string">"'this is tree'"</span>
          &#125;
        &#125;
      ],
      <span class="hljs-string">"kind"</span>: <span class="hljs-string">"var"</span>
    &#125;
  ],
  <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到一条语句由若干个词法单元组成。这个词法单元就像 26 个字母。创造出个十几万的单词，通过不同单词的组合又能写出不同内容的文章。</p>
<blockquote>
<p>至于有哪些词法单元可点击查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FMozilla%2FProjects%2FSpiderMonkey%2FParser_API%23node_objects" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API#node_objects" ref="nofollow noopener noreferrer">AST 对象文档</a> 或者 参考掘金大佬的文章<a href="https://juejin.cn/post/6844903798347939853#heading-12" target="_blank" title="https://juejin.cn/post/6844903798347939853#heading-12">高级前端基础-JavaScript 抽象语法树 AST</a>里面列举了语法树节点与解释。</p>
</blockquote>
<p>推荐一个工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">在线 ast 转换器</a>。可以在这个网站上，亲自尝试下转换。<strong>点击语句中的词，右边的抽象语法树节点便会被选中</strong>，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e1143afa0d402ca10e81e5daf4fceb~tplv-k3u1fbpfcp-zoom-1.image" alt="tree.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">AST 有什么用</h3>
<ul>
<li>IDE 的错误提示、代码格式化、代码高亮、代码自动补全等</li>
<li>JSLint、JSHint 对代码错误或风格的检查等</li>
<li>webpack、rollup 进行代码打包等</li>
<li>CoffeeScript、TypeScript、JSX 等转化为原生 Javascript.</li>
<li>vue 模板编译、react 模板编译</li>
</ul>
<h3 data-id="heading-4">AST 如何生成</h3>
<p>看到这里，你应该已经知道抽象语法树大致长什么样了。那么<code>AST</code>又是如何生成的呢？</p>
<p>AST 整个解析过程分为两个步骤</p>
<ul>
<li>词法分析 (Lexical Analysis)：扫描输入的源代码字符串，生成一系列的词法单元 (tokens)。这些词法单元包括数字，标点符号，运算符等。词法单元之间都是独立的，也即在该阶段我们并不关心每一行代码是通过什么方式组合在一起的。</li>
<li>语法分析 (Syntax Analysis)：建立分析语法单元之间的关系</li>
</ul>
<p>还是以上面<code>var tree = 'this is tree'</code>为例</p>
<h4 data-id="heading-5">正规理解</h4>
<h5 data-id="heading-6">词法分析</h5>
<p>先经过词法分析，扫描输入的源代码字符串，生成一系列的词法单元 (<code>tokens</code>)。这些词法单元包括数字，标点符号，运算符等</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e638e3157f3a47eeaea9973bb7b39599~tplv-k3u1fbpfcp-zoom-1.image" alt="tokens.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">语法分析</h5>
<p>语法分析阶段就会将上一阶段生成的 <code>tokens</code> 列表转换为如下图所示的 <code>AST</code>(我把<code>start</code>、<code>end</code>字段去掉了不用在意)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a33b85c3c512429ea14410e8d3606530~tplv-k3u1fbpfcp-zoom-1.image" alt="ast.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">非正规理解</h4>
<p><strong>郑重声明：我周某人语文很少及格，大致意思能理解就好。</strong></p>
<p>例子："它是猪。"</p>
<h5 data-id="heading-9">词法分析</h5>
<p>先经过词法分析，扫描输入的源代码字符串，生成一系列的词法单元 (<code>tokens</code>)。这些词法单元包括数字，标点符号，运算符等</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceda725db0674ae2b85727a3df1a44d9~tplv-k3u1fbpfcp-zoom-1.image" alt="chinese_tokens.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-10">语法分析</h5>
<p>语法分析阶段就会将上一阶段生成的 <code>tokens</code> 列表转换为如下图所示的 <code>AST</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de0b4faef4c5459ca829238c7c528a0b~tplv-k3u1fbpfcp-zoom-1.image" alt="chinese_ast.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">JsParser</h3>
<p>JavaScript Parser，把 js 源码转化为抽象语法树的解析器。</p>
<ul>
<li><code>acorn</code></li>
<li><code>esprima</code></li>
<li><code>traceur</code></li>
<li><code>@babel/parser</code></li>
</ul>
<h2 data-id="heading-12">实战小例子</h2>
<h4 data-id="heading-13">例子 1：去 debugger</h4>
<p>源代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'debugger'</span>)
  <span class="hljs-keyword">debugger</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据前面学过的知识点，我们先脑海中意淫下如何去掉这个<code>debugger</code></p>
<ol>
<li>先将源代码转化成<code>AST</code></li>
<li><strong>遍历</strong><code>**AST**</code><strong>上的节点，找到</strong><code>**debugger**</code><strong>节点，并删除</strong></li>
<li>将转换过的<code>AST</code>再生成<code>JS</code>代码</li>
</ol>
<p>将源代码拷贝到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">在线 ast 转换器</a> 中，并点击左边区域的<code>debugger</code>，可以看到左边的<code>debugger</code>节点就被选中了。所以只要把图中选中的<code>debugger</code>抽象语法树节点<strong>删除</strong>就行了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb9b92cbd7054332aabd0919ae398964~tplv-k3u1fbpfcp-zoom-1.image" alt="debugger.jpg" loading="lazy" referrerpolicy="no-referrer">
​</p>
<p>这个例子比较简单，直接上代码。
​</p>
<p>这个例子我使用<code>@babel/parser</code>、<code>@babel/traverse</code>、<code>@babel/generator</code>，它们的作用分别是解析、转换、生成。</p>
<p>​</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>);
<span class="hljs-keyword">const</span> traverse = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/traverse"</span>);
<span class="hljs-keyword">const</span> generator = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/generator"</span>);

<span class="hljs-comment">// 源代码</span>
<span class="hljs-keyword">const</span> code = <span class="hljs-string">`
function fn() &#123;
  console.log('debugger')
  debugger;
&#125;
`</span>;

<span class="hljs-comment">// 1. 源代码解析成 ast</span>
<span class="hljs-keyword">const</span> ast = parser.parse(code);


<span class="hljs-comment">// 2. 转换</span>
<span class="hljs-keyword">const</span> visitor = &#123;
  <span class="hljs-comment">// traverse 会遍历树节点，只要节点的 type 在 visitor 对象中出现，变化调用该方法</span>
  <span class="hljs-function"><span class="hljs-title">DebuggerStatement</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-comment">// 删除该抽象语法树节点</span>
    path.remove();
  &#125;
&#125;
traverse.default(ast, visitor);

<span class="hljs-comment">// 3. 生成</span>
<span class="hljs-keyword">const</span> result = generator.default(ast, &#123;&#125;, code);

<span class="hljs-built_in">console</span>.log(result.code)

<span class="hljs-comment">// 4. 日志输出</span>

<span class="hljs-comment">// function fn() &#123;</span>
<span class="hljs-comment">//   console.log('debugger');</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>babel</code>核心逻辑处理都在<code>visitor</code>里。<code>traverse</code>会遍历树节点，只要节点的<code>type</code>在<code>visitor</code>对象中出现，便会调用该<code>type</code>对应的方法，在方法中调用<code>path.remove()</code>将当前节点删除。<code>demo</code>中使用到的<code>path</code>的一些<code>api</code>可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fplugin-handbook.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md" ref="nofollow noopener noreferrer">babel-handbook</a>。</p>
<h4 data-id="heading-14">例子 2：修改函数中执行的 console.log 参数</h4>
<p>我们有时候在函数里打了日志，但是又想在控制台直观的看出是哪个函数中打的日志，这个时候就可以使用<code>AST</code>，去解析、转换、生成最后想要的代码。</p>
<p>源代码：</p>
<pre><code class="copyable">function funA() &#123;
console.log(1)
&#125;

// 转换成

function funA() &#123;
console.log('from function funA:', 1)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编码之前，我们先理清思路，再下手也不迟。这个时候就需要借助 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">在线 ast 转换器</a>来分析了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db857be6f58d4392a882817d839f4c0f~tplv-k3u1fbpfcp-zoom-1.image" alt="funA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过工具发现想要实现这个案例只需要往<code>arguments</code>前面插入段节点就可以了。</p>
<p>这里也像例子 1 一样先梳理下思路</p>
<ol>
<li>使用 <code>@babel/parser</code> 将源代码解析成 <code>ast</code></li>
<li>监听 <code>@babel/traverse</code> 遍历到 <code>CallExpression</code></li>
<li>触发后，判断如果执行的方法是 <code>console.log</code> 时，往 <code>arguments</code> <code>unshift</code>一个 <code>StringLiteral</code></li>
<li>将转换后的 <code>ast</code> 生成代码</li>
</ol>
<p>将 <code>js</code> 代码解析成 <code>ast</code> 与 将 <code>ast</code> 生成 <code>js</code> 代码与去 <code>debugger</code> 例子一致，这里将不再描述。</p>
<p>首先监听<code>CallExpression</code>遍历</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> visitor = &#123;
  <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-comment">// console.log(path)</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>观察 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">在线 ast 转换器</a> 解析后的树，我们只要判断<code>path</code> 的 <code>callee</code>中存在对象 <code>console</code> 及属性 <code>property</code> 。就可以往当前的 <code>path</code> 的 <code>arguments</code> <code>unshift</code> 一个 <code>StringLiteral</code></p>
<p>这里的 <code>types</code> 对象是使用了一个新包 <code>@babel/types</code> , 用来判断类型。</p>
<p>上面用到的<code>isMemberExpression,isIdentifier,getFunctionParent,stringLiteral</code>都可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fplugin-handbook.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md" ref="nofollow noopener noreferrer">babel-handbook</a>文档中找到，本文就不解释了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> visitor = &#123;
  <span class="hljs-comment">// 当遍历到 CallExpression 时候触发</span>
  <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-keyword">const</span> callee = path.node.callee;
    <span class="hljs-comment">// 判断当前当前执行的函数是否是组合表达式</span>
    <span class="hljs-keyword">if</span> (types.isMemberExpression(callee)) &#123;
      <span class="hljs-keyword">const</span> &#123; object, property &#125; = callee;
      <span class="hljs-keyword">if</span> (types.isIdentifier(object, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'console'</span> &#125;) && types.isIdentifier(property, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'log'</span> &#125;)) &#123;
        <span class="hljs-comment">// 查找最接近的父函数或程序</span>
        <span class="hljs-keyword">const</span> parent = path.getFunctionParent();
        <span class="hljs-keyword">const</span> parentFunName = parent.node.id.name;
        path.node.arguments.unshift(types.stringLiteral(<span class="hljs-string">`from function <span class="hljs-subst">$&#123;parentFunName&#125;</span>`</span>))
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">总结</h2>
<p>就像前言所说的，我们的日常工作中很少会去使用<code>AST</code>，以至于大多数同学都不大了解<code>AST</code>。但了解了 <code>AST</code> 可以帮助我们更好地理解开发工具、编译器的原理，并产出提高代码效率的工具。还记得我在之前的前端小组遇到一个问题，我们项目是<code>ssr</code>项目，在服务端执行的生命周期不允许出现客户端才能执行的代码。但是小组成员有时候无意的写了，导致服务端渲染降级。在学习<code>AST</code>之前，我为了解决这个问题，写了个<code>loader</code>通过正则去匹配校验，当时可真是逼死我了，正则需要去适配各种场景。后面我学习了<code>AST</code>了之后，编写了个<code>eslint</code>插件实现了客户端代码校验。</p>
<h3 data-id="heading-16">参考</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fplugin-handbook.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md" ref="nofollow noopener noreferrer">babel-handbook</a>
<a href="https://juejin.im/post/6844903746804137991" target="_blank" title="https://juejin.im/post/6844903746804137991">深入 Babel，这一篇就够了</a>
<a href="https://juejin.cn/post/6844903798347939853#heading-12" target="_blank" title="https://juejin.cn/post/6844903798347939853#heading-12">高级前端基础-JavaScript 抽象语法树 AST</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83a145c3f8d44e71bcc4172d32f48190~tplv-k3u1fbpfcp-watermark.image" alt="未命名_自定义px_2021-07-11-0.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            