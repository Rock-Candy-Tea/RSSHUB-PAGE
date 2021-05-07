
---
title: '转译器原理 parser 篇：新的 js 语法都是怎么实现的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14a066cc4c9b4e16a39c2ba164445607~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 03:07:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14a066cc4c9b4e16a39c2ba164445607~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>转译器原理分为 3 篇文章，分别对应 parse、transform、generate 3 个阶段，这篇是上篇。</p>
<p>我们会扩展一个 js 的新语法，探索下 js 新语法都是怎么实现的，然后再把这个新语法编译到 css。</p>
<p>具体会涉及到：</p>
<ul>
<li>js parser 的历史和标准</li>
<li>css parser 和 html parser</li>
<li>acorn 插件的写法</li>
<li>postcss 语法插件的写法</li>
</ul>
<h2 data-id="heading-0">转译器及其原理</h2>
<p><strong>我：</strong> 昊昊，你知道前端领域的转译器有哪些么？</p>
<p><strong>昊昊：</strong> 转译器（transpiler）是源码转源码，前端领域的太多了，比如 <a href="https://github.com/babel/babel" target="_blank" rel="nofollow noopener noreferrer">babel</a>、<a href="https://github.com/microsoft/TypeScript" target="_blank" rel="nofollow noopener noreferrer">typescript</a>、<a href="https://github.com/terser/terser" target="_blank" rel="nofollow noopener noreferrer">terser</a>、<a href="https://github.com/eslint/eslint" target="_blank" rel="nofollow noopener noreferrer">eslint</a>、<a href="https://github.com/prettier/prettier" target="_blank" rel="nofollow noopener noreferrer">prettier</a>、<a href="https://github.com/postcss/postcss" target="_blank" rel="nofollow noopener noreferrer">postcss</a>、<a href="https://github.com/posthtml/posthtml" target="_blank" rel="nofollow noopener noreferrer">posthtml</a>、<a href="https://github.com/vuejs/vue/tree/dev/packages/vue-template-compiler" target="_blank" rel="nofollow noopener noreferrer">vue template compiler</a> 等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14a066cc4c9b4e16a39c2ba164445607~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>babel 用于 es next、flow、typescript、jsx 等语法转目标环境支持的 js</li>
<li>typescript 用于处理 typescript 语法，并进行类型检查，然后转成 es5 或者 es3</li>
<li>terser 用于 parse es6 的代码，并进行压缩和混淆，输出处理后的代码</li>
<li>prettier 用于处理各种 css、js、html 等代码，进行格式化代码，然后输出格式化后的代码</li>
<li>eslint 是对代码风格和一些常见错误进行静态检查，通过 --fix 还可以自动修复</li>
<li>postcss 用于 css 的 parse，之后通过插件对 ast 进行各种处理，最后输出处理后的 css</li>
<li>posthtml 和 postcss 类似，不过是用于 html 处理的。</li>
<li>vue template compiler 是 vue 专用的，用于把 vue template 转成优化以后的 render 函数</li>
</ul>
<p><strong>我：</strong> 挺全面的了，前端领域主要的转译器差不多是这些，再加上 taro、uniapp 等基于上述转译器的小程序转译器。当然还有 rust 写的类似 babel 的 swc，或者 go 写的打包工具 esbuild 里自带的 js transpiler，这些不是 js 写的，就先不讨论了。</p>
<p><strong>昊昊：</strong> 光哥，这些转译器的实现原理是啥？</p>
<p><strong>我：</strong>  转译器是源码转源码，其实不管是啥转译器都分为三步。</p>
<p>第一步，<code>parse</code>，把源码 parse 成抽象语法树 AST，通过一棵树形的数据结构来记录源码中的信息，这样计算机才能理解源码。</p>
<p>第二步，<code>transform</code>，理解了源码之后，就是进行各种转换了，转译器全称转换编译器，主要工作就在于转换上，对 ast 进行不同目的的增删改。</p>
<p>第三步，<code>generate</code>，转换完的 ast 进行递归打印，生成新的代码，并且生成记录之前的源码和之后的源码的关联关系的 sourcemap。</p>
<p>虽然都是分为这三个阶段，但是具体的名字可能不同，比如 vue template compiler 中就把 transform 叫做 optimize，以为它主要是做优化后续渲染的一些转换；postcss 第三步叫做 stringifier。具体名字不用纠结。</p>
<p><strong>昊昊：</strong> 我对这三步都干了啥很好奇啊，光哥，你能给我讲讲不</p>
<p><strong>我：</strong> 可以啊。就像我说的，转译器都分为这三步，那么咱换个维度，分别分析 parse、transform、generate 这三个阶段，纵向对比各种转译器里面的实现。</p>
<p>不过内容有些多，分为三部分来讲吧，先讲 parse 部分。</p>
<h2 data-id="heading-1">JS Parser</h2>
<p><strong>我：</strong>  先从 JS Parser 开始吧。昊昊，你觉得为啥要用 JS 写 JS parser。</p>
<p><strong>昊昊：</strong> 是因为前端工程化吧，有了 node 之后可以用 js 写 js 代码的工具链，包括语法转换、压缩混淆，还有打包工具等，这些都需要 parser 的支持。</p>
<p><strong>我：</strong> 对，确实是工程化领域的工具链造成了对 parser 的需求。 最早的 JS 写的 JS parser 是  <a href="https://github.com/jquery/esprima" target="_blank" rel="nofollow noopener noreferrer">esprima</a>。当时 Mozilla 公布了它的 JS 引擎 SpiderMonkey 的 <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API" target="_blank" rel="nofollow noopener noreferrer">parser api 和 ast 标准</a>。于是 esprima 就基于它的 ast 标准实现了 parser。后来形成了 estree 标准，这个对其 SpiderMonkey 的 ast。 所以当听到 SpiderMonkey 的 ast 时，就是说 <a href="https://github.com/estree/estree" target="_blank" rel="nofollow noopener noreferrer">estree 标准</a>的 ast。比如 terser 的文档中就叫 SpiderMonkey ast。</p>
<p><strong>昊昊：</strong> 我知道了，SpiderMonkey 的 api 是参照物，estree 是对它的兼容和扩充，然后最早的实现是 esprima。</p>
<p><strong>我：</strong> 对，因为有了 esprima 这个 parser，很多 js 的转译工具就可以直接基于它做了，比如 eslint。 eslint 最早就是基于 esprima 的，前期一切都挺好。 但是当 js 到了 es6 以后，更新速度加快，而 esprima 的更新速度跟不上，这导致 eslint 的使用者经常抱怨这个问题。 所以 eslint 干脆 fork 了一份 esprima，自己扩展语法，这就是 <a href="https://github.com/eslint/espree" target="_blank" rel="nofollow noopener noreferrer">espree</a>。espree 自己单干了，但也是 estree 标准的实现。</p>
<p>后来社区迎来了更好的 JS parser，就是现在最常用的 <a href="https://github.com/acornjs/acorn" target="_blank" rel="nofollow noopener noreferrer">acorn</a>。它速度更快，支持新语法，而且支持插件扩展，全面超过了 esprima。所以大批之前基于 esprima 的就改为了基于 acorn。 其中当然包括 eslint，在 espree2.0 之后，底层的 parser 实现就改成了 acorn。</p>
<p>acorn 的插件机制使得开发者可以扩展一些新的语法，这样使得它能满足各种定制需求。我觉得一个好的插件机制很重要，webpack 不也是靠这些才成功的么。</p>
<p><strong>昊昊：</strong> acorn 可以扩展新的语法么，怎么做啊</p>
<p><strong>我：</strong> 比如我想扩展一个关键字，叫 ssh，这个 ssh 会生成一个新的 ast 节点，这样是不是就达到了扩展新语法的目的。那么该怎么做呢？</p>
<p>acorn 插件的形式是一个函数，接受旧 Parser，返回继承旧 Parser 的新 Parser，这个 Parser 通过重写一些方法，达到扩展的目的。这种基于继承和重写的扩展在面向对象领域还是挺常见的。</p>
<p>那重写啥方法呢？比如我想直接<code>ssh;</code>来使用，这样首先要注册一个关键字，用于分词的时候分出来，需要在构造器里面修改 this.keywords 的正则表达式，这个正则表达式就用于 keywords 的分词。</p>
<p>acorn Parser 的入口方法是 parse，我们要在 parse 方法里面设置 keywords。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">parse</span>(<span class="hljs-params">program</span>)</span> &#123;
    <span class="hljs-keyword">var</span> newKeywords = <span class="hljs-string">"break case catch continue debugger default do else finally for function if return switch throw try var while with null true false instanceof typeof void delete new in this const class extends export import super"</span>;
    newKeywords += <span class="hljs-string">" ssh"</span>;<span class="hljs-comment">// 增加一个关键字</span>
    <span class="hljs-built_in">this</span>.keywords = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"^(?:"</span> + newKeywords.replace(<span class="hljs-regexp">/ /g</span>, <span class="hljs-string">"|"</span>) + <span class="hljs-string">")$"</span>)

    <span class="hljs-keyword">return</span>(<span class="hljs-built_in">super</span>.parse(program));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后注册一个新的 token 类型来标识它</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Parser.acorn.keywordTypes[<span class="hljs-string">"ssh"</span>] = <span class="hljs-keyword">new</span> TokenType(<span class="hljs-string">"ssh"</span>,&#123;<span class="hljs-attr">keyword</span>: <span class="hljs-string">"ssh"</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样 acorn 就会在 parse 的时候分出 <code>ssh</code> 这个关键字</p>
<p>然后是语法阶段，acorn 会对不同的 AST 类型调用不同的 parseXxx 方法，我们这里要覆盖 parseStatement，因为 <code>ssh;</code> 是一个 statement。</p>
<p>this.type 是当前处理的 token 的类型，如果是新的 ssh 类型的话，就用 this.next() 消耗掉这个 token，然后组装成 AST。否则调用父类的 parse 逻辑。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">parseStatement</span>(<span class="hljs-params">context, topLevel, <span class="hljs-built_in">exports</span></span>)</span> &#123;
  <span class="hljs-keyword">var</span> starttype = <span class="hljs-built_in">this</span>.type;

  <span class="hljs-keyword">if</span> (starttype == Parser.acorn.keywordTypes[<span class="hljs-string">"ssh"</span>]) &#123;
    <span class="hljs-keyword">var</span> node = <span class="hljs-built_in">this</span>.startNode();
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.parseSshStatement(node);
  &#125;
  <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span>(<span class="hljs-built_in">super</span>.parseStatement(context, topLevel, <span class="hljs-built_in">exports</span>));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 this.startNode 创建新节点之后就是往这个节点填内容了，通过 this.next 把 ssh 这个单词消耗掉，然后返回一个对应的 ast</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">parseSshStatement</span>(<span class="hljs-params">node</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.next();
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.finishNode(&#123;<span class="hljs-attr">value</span>: <span class="hljs-string">'ssh'</span>&#125;,<span class="hljs-string">'sshStatement'</span>);<span class="hljs-comment">//新增加的ssh语句</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到了这里就大功告成了。 其实也不难：</p>
<ul>
<li>扩展词法分析阶段要修改对应的正则，注册对应的 tokenType。</li>
<li>扩展语法分析阶段，要重写对应的 parseXxx 方法，然后创建新节点，消耗掉 token，来产生新的 ast 节点返回。</li>
</ul>
<p>完整代码这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> acorn = <span class="hljs-built_in">require</span>(<span class="hljs-string">"acorn"</span>);

<span class="hljs-keyword">const</span> Parser = acorn.Parser;
<span class="hljs-keyword">const</span> tt = acorn.tokTypes; 
<span class="hljs-keyword">const</span> TokenType = acorn.TokenType;

<span class="hljs-comment">//添加一个ssh的关键字</span>
Parser.acorn.keywordTypes[<span class="hljs-string">"ssh"</span>] = <span class="hljs-keyword">new</span> TokenType(<span class="hljs-string">"ssh"</span>,&#123;<span class="hljs-attr">keyword</span>: <span class="hljs-string">"ssh"</span>&#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wordsRegexp</span>(<span class="hljs-params">words</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"^(?:"</span> + words.replace(<span class="hljs-regexp">/ /g</span>, <span class="hljs-string">"|"</span>) + <span class="hljs-string">")$"</span>)
&#125;

<span class="hljs-keyword">var</span> sshKeyword = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Parser</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parser</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">parse</span>(<span class="hljs-params">program</span>)</span> &#123;

      <span class="hljs-keyword">var</span> newKeywords = <span class="hljs-string">"break case catch continue debugger default do else finally for function if return switch throw try var while with null true false instanceof typeof void delete new in this const class extends export import super"</span>;
      newKeywords += <span class="hljs-string">" ssh"</span>;
      <span class="hljs-built_in">this</span>.keywords = wordsRegexp(newKeywords);<span class="hljs-comment">// 重新设置关键字</span>

      <span class="hljs-keyword">return</span>(<span class="hljs-built_in">super</span>.parse(program));
    &#125;

    <span class="hljs-function"><span class="hljs-title">parseStatement</span>(<span class="hljs-params">context, topLevel, <span class="hljs-built_in">exports</span></span>)</span> &#123;
      <span class="hljs-keyword">var</span> starttype = <span class="hljs-built_in">this</span>.type;

      <span class="hljs-keyword">if</span> (starttype == Parser.acorn.keywordTypes[<span class="hljs-string">"ssh"</span>]) &#123;
        <span class="hljs-keyword">var</span> node = <span class="hljs-built_in">this</span>.startNode();
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.parseSshStatement(node);
      &#125;
      <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span>(<span class="hljs-built_in">super</span>.parseStatement(context, topLevel, <span class="hljs-built_in">exports</span>));
      &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">parseSshStatement</span>(<span class="hljs-params">node</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.next();
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.finishNode(&#123;<span class="hljs-attr">value</span>: <span class="hljs-string">'ssh'</span>&#125;,<span class="hljs-string">'sshStatement'</span>);<span class="hljs-comment">//新增加的ssh语句</span>
    &#125;;
  &#125;
&#125;
<span class="hljs-keyword">const</span> newParser = Parser.extend(sshKeyword);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们调用一下我们定制的新 Parser，就可以发现他能处理 ssh 关键字了，我们成功的实现了新语法！就算 typescript、jsx、flow 等新语法的实现也是一样的方式，只不过那些更繁琐。将来你有什么好的扩展语法的想法，比如语言级别内置一个 dsl，像 jsx 那样，就可以这样来改 parser。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> program = 
<span class="hljs-string">`   
    ssh;
    const a = 1;
`</span>;

newParser.parse(program);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
 <span class="hljs-string">"type"</span>: <span class="hljs-string">"Program"</span>,
 <span class="hljs-string">"start"</span>: <span class="hljs-number">0</span>,
 <span class="hljs-string">"end"</span>: <span class="hljs-number">30</span>,
 <span class="hljs-string">"body"</span>: [
  &#123;
   <span class="hljs-string">"value"</span>: <span class="hljs-string">"ssh"</span>,
   <span class="hljs-string">"type"</span>: <span class="hljs-string">"sshStatement"</span>,
   <span class="hljs-string">"end"</span>: <span class="hljs-number">11</span>
  &#125;,
  &#123;
   <span class="hljs-string">"type"</span>: <span class="hljs-string">"EmptyStatement"</span>,
   <span class="hljs-string">"start"</span>: <span class="hljs-number">11</span>,
   <span class="hljs-string">"end"</span>: <span class="hljs-number">12</span>
  &#125;,
  &#123;
   <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>,
   <span class="hljs-string">"start"</span>: <span class="hljs-number">17</span>,
   <span class="hljs-string">"end"</span>: <span class="hljs-number">29</span>,
   <span class="hljs-string">"declarations"</span>: [
    &#123;
     <span class="hljs-string">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>,
     <span class="hljs-string">"start"</span>: <span class="hljs-number">23</span>,
     <span class="hljs-string">"end"</span>: <span class="hljs-number">28</span>,
     <span class="hljs-string">"id"</span>: &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,
      <span class="hljs-string">"start"</span>: <span class="hljs-number">23</span>,
      <span class="hljs-string">"end"</span>: <span class="hljs-number">24</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"a"</span>
     &#125;,
     <span class="hljs-string">"init"</span>: &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"Literal"</span>,
      <span class="hljs-string">"start"</span>: <span class="hljs-number">27</span>,
      <span class="hljs-string">"end"</span>: <span class="hljs-number">28</span>,
      <span class="hljs-string">"value"</span>: <span class="hljs-number">1</span>,
      <span class="hljs-string">"raw"</span>: <span class="hljs-string">"1"</span>
     &#125;
    &#125;
   ],
   <span class="hljs-string">"kind"</span>: <span class="hljs-string">"const"</span>
  &#125;
 ],
 <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"script"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>昊昊：</strong>  哇，好棒的插件机制，还能扩展新语法。除了 acorn，还有别的 js parser 有插件机制么？</p>
<p><strong>我：</strong>  我印象中没有，esprima、typescript等都没有语法的插件，这种只能等待官方去实现了。</p>
<p><strong>昊昊：</strong> 那 babel、espree 等都是基于 acorn 的，他们都做了哪些改动和扩充呢？</p>
<p><strong>我：</strong> espree 只是增加了一些属性，ast 保持 estree 兼容。 而 @babel/parser 除了在一些节点添加属性之外，也扩展了很多新节点，所以它是不兼容 estree 标准的。他做了这些修改：</p>
<ul>
<li>把 Literal 替换成了 StringLiteral、NumericLiteral, BigIntLiteral, BooleanLiteral, NullLiteral, RegExpLiteral</li>
<li>把 Property 替换成了 ObjectProperty 和 ObjectMethod</li>
<li>把 MethodDefinition 替换成了 ClassMethod</li>
<li>Program 和 BlockStatement 也支持 'use strict' 等指令的解析，对应的 ast 是 Directive 和 DirectiveLiteral</li>
<li>ChainExpression 替换为了 ObjectMemberExpression 和 OptionalCallExpression</li>
<li>ImportExpression 替换为了 CallExpression 并且 callee 属性设置为 Import 等</li>
</ul>
<p>它的 api 大概是这样的，plugins 就是它扩展的一些语法支持。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/parser"</span>).parse(<span class="hljs-string">"code"</span>, &#123;
  <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span>,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">"jsx"</span>,
    <span class="hljs-string">"typescript"</span>
  ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体可以在 <a href="https://babeljs.io/docs/en/babel-parser" target="_blank" rel="nofollow noopener noreferrer">@babel/parser</a> 的文档来查，整体基本是对 AST 的细化，其实也很好理解，比如一个数字类型，拆分为整数和浮点数显然方便更细粒度的处理啊，免去了各种判断。因为 babel 的 parser 是暴露 api 给开发者用来修改 ast 的，所以能省去很多判断的 ast 细化是很有必要的。</p>
<p>我们刚学会了写 acorn 的插件，可以实现 Literal 细化这个。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    parseLiteral (...args) &#123;
        <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">super</span>.parseLiteral(...args);
        <span class="hljs-keyword">switch</span>(<span class="hljs-keyword">typeof</span> node.value) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'number'</span>:
                node.type = <span class="hljs-string">'NumericLiteral'</span>;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'string'</span>:
                node.type = <span class="hljs-string">'StringLiteral'</span>;
                <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">return</span>  node;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实并不难，但是却能省去开发者很多判断，虽然失去了 estree 的兼容性，不得不说这是一种很不错的设计权衡。就像 hooks 明明可以用 map 实现，支持任意顺序，却最终选择了用数组实现，只能写在顶层，牺牲了一些灵活性换取了更简洁的写法。</p>
<p>这都是很棒的架构 treade off（权衡）。</p>
<p><strong>昊昊：</strong> 那其他的 JS 转译器呢，prettier、terser 等，他们的 parser 是啥？</p>
<p><strong>我：</strong></p>
<p>prettier 是基于 @babel/parser 和 typescript 等 parser 的， terser 是有自己的一套 ast 标准。你可能会问为什么 terser 是自己的一套，为什么不统一呢？</p>
<p>这个问题其实 terser 在 2012 年就回答过了，主要是是 terser 的 ast 上有很多方法，而且不同 ast 节点之间有继承关系，而 estree 标准的 ast 是纯粹的数据结构。也就是贫血模型和富血模型的区别。terser 觉得改动成本比较大，就一直没改。 可以搜 why not switching to SpiderMonkey AST 这篇文章，那里有官方解释。</p>
<p>其实我觉得改是可以改的，就是需要重写，terser 没改而已。</p>
<p>但这样我觉得是个需要去解决的问题，影响还是有的，主要是性能。 babel 是 estree 标准的细化也就是 SpiderMonkey 的 ast，而 terser 是自己的一套，这样用两个工具的时候就不能直接复用 ast，得转换一遍或者先打印成字符串再重新 parse，而且 sourcemap 也得关联上。不管哪种方式，性能都会有损耗。</p>
<p>terser 用自己的 parser 和 ast，最开始的 uglify 不支持 es6 的语法，后来有了 uglify-es，后来又放弃了，干脆重写了一遍，就是现在的 terser。 关键是它重写了依然用的自己的 ast...</p>
<p>这个问题在 js 的工具链中一直存在没解决，一般都会先用 babel 或者 typescript 来转一次源码，然后变成字符串后再用 terser 转一次，把 sourcemap 也做下关联。</p>
<p>现在一些别的语言写的 parser 解决了这个问题，比如 rust 写的 swc，他就实现了 parser 并且自己做了 minifier，这样不需要切换两套 ast，也不用 sourcemap 多一层映射，效率就会高一些。 再加上编译型语言比解释型语言做工具方面快很多。 所以性能差距挺明显的。</p>
<p>希望 JS 社区能出一个基于 estree 系列 parser 来做压缩的工具吧，替代掉 terser。babel-minify 是做这个的，但还在 0.x 阶段，希望尽快能够到 1.0 吧。</p>
<h2 data-id="heading-2">CSS Parser</h2>
<p><strong>昊昊：</strong> 光哥，JS parser 和一些转译器我大概知道了，那 css 呢</p>
<p><strong>我：</strong> css 的转译器流行的就 <a href="https://github.com/postcss/postcss" target="_blank" rel="nofollow noopener noreferrer">postcss</a> 一个，less、sass 等是为了增强 css 能力的 dsl，和 postcss 这种专用做转译器的工具定位上有不同。 而且更重要的是 postcss 的 parser 也支持插件机制，默认支持 css，但是可以通过插件支持各种语法。这里说的是 syntax parser，是用于扩展支持的语法的，一般我们说的 postcss插件是后面的 transform parser。</p>
<p>你看，流行的方案基本都是有好的插件机制的，这是规律，比如 acorn、postcss、webpack 等都是。因为这样才能利用社区的力量去弥补各方面的不足，才能形成生态。</p>
<p>我们上面写了一个 acorn 语法插件，接下来在 postcss 的语法插件里面用一下，现学现用嘛。让 postcss 支持 js 语法！ 是不是听起来听高大上的，其实怎么 parse 的 postcss 不关心，只要你输出给它的是 postcss 的 ast 就可以了。</p>
<p>分析一下思路： postcss 可以传入 parser 和 stringifier 来自己实现，其实 eslint、prettier 等也可以自定义 parser，文档中可以找到相关介绍。 我们这里只实现 parser。</p>
<p>目标是组装出 postcss 的 ast，这个分别调用 postcss.root、postcss.rule、postcss.decl 既可。源码封装成 Input 对象，然后对它进行 parse，之后返回组装好的 postcss 的 ast 就行了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> postcss = <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss'</span>);

(<span class="hljs-keyword">async</span> ()=> &#123;
 <span class="hljs-keyword">const</span> code = <span class="hljs-string">`ssh;`</span>;
 <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyParser</span> </span>&#123;
   <span class="hljs-function"><span class="hljs-title">parse</span>(<span class="hljs-params">input</span>)</span>&#123;
     <span class="hljs-keyword">const</span> root = postcss.root();

     <span class="hljs-keyword">const</span> ast = newParser.parse(input.css, &#123;<span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">6</span>&#125;);
     ast.body.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
       <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">'sshStatement'</span>) &#123;
         <span class="hljs-keyword">const</span> rule = postcss.rule();
         rule.selector = <span class="hljs-string">"ssh"</span>;

         <span class="hljs-keyword">const</span> decl = postcss.decl();
         decl.prop = <span class="hljs-string">'background'</span>;
         decl.value = <span class="hljs-string">'green;'</span>;

         rule.nodes.push(decl);
         root.nodes.push(rule);
       &#125;
     &#125;);
     <span class="hljs-keyword">return</span> root
  &#125;
&#125;
cosnt parser = <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
   <span class="hljs-keyword">let</span> input = <span class="hljs-keyword">new</span> postcss.Input(code)
   <span class="hljs-keyword">const</span> parser = <span class="hljs-keyword">new</span> MyParser(input);
   <span class="hljs-keyword">return</span> parser.parse(input);
&#125;
 <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> postcss().process(code, &#123; parser, <span class="hljs-attr">from</span>: <span class="hljs-string">''</span> &#125;);

 <span class="hljs-built_in">console</span>.log(result.content);
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<pre><code class="hljs language-css copyable" lang="css">ssh &#123;<span class="hljs-attribute">background</span>: green;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>昊昊：</strong> 哇，把 js 的新语法编译到 css，好酷哦。</p>
<p><strong>我：</strong> 而且不只是 parser 可以自定义，stringifier 也可以，比如打印的时候坐下语法高亮啥的。</p>
<h2 data-id="heading-3">HTML Parser</h2>
<p><strong>昊昊：</strong> 光哥，那还有 html 的 parser 呢？</p>
<p><strong>我：</strong> html 的也和 css 的差不多，有很多 dsl 也就是各种模版引擎，编译到 html。专门用作转译器的主要是 postcss，它的 parser 用的是 <a href="https://github.com/fb55/htmlparser2" target="_blank" rel="nofollow noopener noreferrer">htmlparser2</a>。流程和 postcss 差不多，但是他只支持 transform plugin，不支持 syntaxt plugin。区分这俩插件的方式很简单：</p>
<p>syntaxt plugin 是扩展语法的，所以输入的是字符串，输出的是 ast；</p>
<p>transform plugin 是对 ast 进行转换的，所以输入输出都是 ast。</p>
<p>虽然 <a href="https://github.com/posthtml/posthtml" target="_blank" rel="nofollow noopener noreferrer">posthtml</a> 不支持 syntaxt plugin，但你可以拿到某个节点之后取内容自己 parse 啊，然后生成 html 的 ast，比如 md 转 html、各种模版引擎转 html 等。</p>
<p><strong>昊昊：</strong> 感觉各种 parser 好多啊，有 acorn、htmlparser2、postcss 这些通用的 parser，也有各个转译器自己实现的 parser。</p>
<p><strong>我：</strong> 所以学习东西不要陷入到使用中啊，了解一下有哪些 parser 只是扩展下视野，学习怎么写 parser 要去了解词法分析语法分析这些东西，而不是学习某个 parser 的使用。但是一般情况下也不会手写复杂的 parser， html parser 还可以手写，比如 vue template compiler。但是复杂的就没必要了，可以用 antlr 这种 parser generator 来生成。</p>
<p>parse 只是转译的开始，重头戏在 parse 之后呢。</p></div>  
</div>
            