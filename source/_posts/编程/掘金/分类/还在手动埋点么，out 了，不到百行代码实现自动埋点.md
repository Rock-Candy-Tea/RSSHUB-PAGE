
---
title: '还在手动埋点么，out 了，不到百行代码实现自动埋点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d17966f33ad9476aaf39e05d110b013a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 05:33:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d17966f33ad9476aaf39e05d110b013a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>埋点是一个常见的需求，就是在函数里面上报一些信息。像一些性能的埋点，每个函数都要处理，很繁琐。能不能自动埋点呢？</p>
<p>答案是可以的。埋点只是在函数里面插入了一段代码，这段代码不影响其他逻辑，这种函数插入不影响逻辑的代码的手段叫做函数插桩。</p>
<p>我们可以基于 babel 来实现自动的函数插桩，在这里就是自动的埋点。</p>
<h2 data-id="heading-0">思路分析</h2>
<p>比如这样一段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> aa <span class="hljs-keyword">from</span> <span class="hljs-string">'aa'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> bb <span class="hljs-keyword">from</span> <span class="hljs-string">'bb'</span>;
<span class="hljs-keyword">import</span> &#123;cc&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'cc'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'dd'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'aaa'</span>);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">bb</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'bbb'</span>;
    &#125;
&#125;

<span class="hljs-keyword">const</span> c = <span class="hljs-function">() =></span> <span class="hljs-string">'ccc'</span>;

<span class="hljs-keyword">const</span> d = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ddd'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们要实现埋点就是要转成这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> _tracker2 <span class="hljs-keyword">from</span> <span class="hljs-string">"tracker"</span>;
<span class="hljs-keyword">import</span> aa <span class="hljs-keyword">from</span> <span class="hljs-string">'aa'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> bb <span class="hljs-keyword">from</span> <span class="hljs-string">'bb'</span>;
<span class="hljs-keyword">import</span> &#123; cc &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'cc'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'dd'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  _tracker2();

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'aaa'</span>);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">bb</span>(<span class="hljs-params"></span>)</span> &#123;
    _tracker2();

    <span class="hljs-keyword">return</span> <span class="hljs-string">'bbb'</span>;
  &#125;

&#125;

<span class="hljs-keyword">const</span> c = <span class="hljs-function">() =></span> &#123;
  _tracker2();

  <span class="hljs-keyword">return</span> <span class="hljs-string">'ccc'</span>;
&#125;;

<span class="hljs-keyword">const</span> d = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  _tracker2();

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ddd'</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有两方面的事情要做：</p>
<ul>
<li>引入 tracker 模块。如果已经引入过就不引入，没有的话就引入，并且生成个唯一 id 作为标识符</li>
<li>对所有函数在函数体开始插入 tracker 的代码</li>
</ul>
<h2 data-id="heading-1">代码实现</h2>
<p>掘金小册<a href="https://juejin.cn/book/6946117847848321055" target="_blank">《babel 插件通关秘籍》</a>中有具体 api 的详细介绍。</p>
<h3 data-id="heading-2">模块引入</h3>
<p>引入模块这种功能显然很多插件都需要，这种插件之间的公共函数会放在 helper，这里我们使用 @babel/helper-module-imports。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> importModule = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/helper-module-imports'</span>);

<span class="hljs-comment">// 省略一些代码</span>
importModule.addDefault(path, <span class="hljs-string">'tracker'</span>,&#123;
    <span class="hljs-attr">nameHint</span>: path.scope.generateUid(<span class="hljs-string">'tracker'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先要判断是否被引入过：在 Program 根结点里通过 path.traverse 来遍历 ImportDeclaration，如果引入了 tracker 模块，就记录 id 到 state，并用 path.stop 来终止后续遍历；没有就引入 tracker 模块，用 generateUid 生成唯一 id，然后放到 state。</p>
<p>当然 default import 和 namespace import 取 id 的方式不一样，需要分别处理下。</p>
<p>我们把 tracker 模块名作为参数传入，通过 options.trackerPath 来取。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Program: &#123;
    enter (path, state) &#123;
        path.traverse(&#123;
            ImportDeclaration (curPath) &#123;
                <span class="hljs-keyword">const</span> requirePath = curPath.get(<span class="hljs-string">'source'</span>).node.value;
                <span class="hljs-keyword">if</span> (requirePath === options.trackerPath) &#123;<span class="hljs-comment">// 如果已经引入了</span>
                    <span class="hljs-keyword">const</span> specifierPath = curPath.get(<span class="hljs-string">'specifiers.0'</span>);
                    <span class="hljs-keyword">if</span> (specifierPath.isImportSpecifier()) &#123; 
                        state.trackerImportId = specifierPath.toString();
                    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(specifierPath.isImportNamespaceSpecifier()) &#123;
                        state.trackerImportId = specifierPath.get(<span class="hljs-string">'local'</span>).toString();<span class="hljs-comment">// tracker 模块的 id</span>
                    &#125;
                    path.stop();<span class="hljs-comment">// 找到了就终止遍历</span>
                &#125;
            &#125;
        &#125;);
        <span class="hljs-keyword">if</span> (!state.trackerImportId) &#123;
            state.trackerImportId  = importModule.addDefault(path, <span class="hljs-string">'tracker'</span>,&#123;
                <span class="hljs-attr">nameHint</span>: path.scope.generateUid(<span class="hljs-string">'tracker'</span>)
            &#125;).name; <span class="hljs-comment">// tracker 模块的 id</span>
            state.trackerAST = api.template.statement(<span class="hljs-string">`<span class="hljs-subst">$&#123;state.trackerImportId&#125;</span>()`</span>)();<span class="hljs-comment">// 埋点代码的 AST</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在记录 tracker 模块的 id 的时候，也生成调用 tracker 模块的 AST，使用 template.statement.</p>
<h3 data-id="heading-3">函数插桩</h3>
<p>函数插桩要找到对应的函数，这里要处理的有：ClassMethod、ArrowFunctionExpression、FunctionExpression、FunctionDeclaration 这些节点。</p>
<p>当然有的函数没有函数体，这种要包装一下，然后修改下 return 值。如果有函数体，就直接在开始插入就行了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'ClassMethod|ArrowFunctionExpression|FunctionExpression|FunctionDeclaration'</span>(path, state) &#123;
    <span class="hljs-keyword">const</span> bodyPath = path.get(<span class="hljs-string">'body'</span>);
    <span class="hljs-keyword">if</span> (bodyPath.isBlockStatement()) &#123; <span class="hljs-comment">// 有函数体就在开始插入埋点代码</span>
        bodyPath.node.body.unshift(state.trackerAST);
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 没有函数体要包裹一下，处理下返回值</span>
        <span class="hljs-keyword">const</span> ast = api.template.statement(<span class="hljs-string">`&#123;<span class="hljs-subst">$&#123;state.trackerImportId&#125;</span>();return PREV_BODY;&#125;`</span>)(&#123;<span class="hljs-attr">PREV_BODY</span>: bodyPath.node&#125;);
        bodyPath.replaceWith(ast);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就实现了自动埋点。</p>
<h2 data-id="heading-4">效果演示</h2>
<p>我们来试下效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; transformFromAstSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/core'</span>);
<span class="hljs-keyword">const</span>  parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>);
<span class="hljs-keyword">const</span> autoTrackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./plugin/auto-track-plugin'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-keyword">const</span> sourceCode = fs.readFileSync(path.join(__dirname, <span class="hljs-string">'./sourceCode.js'</span>), &#123;
    <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>
&#125;);

<span class="hljs-keyword">const</span> ast = parser.parse(sourceCode, &#123;
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'unambiguous'</span>
&#125;);

<span class="hljs-keyword">const</span> &#123; code &#125; = transformFromAstSync(ast, sourceCode, &#123;
    <span class="hljs-attr">plugins</span>: [[autoTrackPlugin, &#123;
        <span class="hljs-attr">trackerPath</span>: <span class="hljs-string">'tracker'</span>
    &#125;]]
&#125;);

<span class="hljs-built_in">console</span>.log(code);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d17966f33ad9476aaf39e05d110b013a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们实现了自动埋点！</p>
<h2 data-id="heading-5">扩展思考</h2>
<p>上面实现的是一种情况，实际上可能有的函数不需要埋点，这种可以自己做一下过滤，或者在函数上写上注释，然后根据注释来过滤，就像 eslint 支持 /* eslint-disable */ 的设置一样。关于注释的操作，可以看另一个案例《自动生成 API 文档》。</p>
<h2 data-id="heading-6">总结</h2>
<p>函数插桩是在函数中插入一段逻辑但不影响函数原本逻辑，埋点就是一种常见的函数插桩，我们完全可以用 babel 来自动做。</p>
<p>实现思路分为引入 tracker 模块和函数插桩两部分：</p>
<p>引入 tracker 模块需要判断 ImportDeclaration 是否包含了 tracker 模块，没有的话就用 @babel/helper-module-import 来引入。</p>
<p>函数插桩就是在函数体开始插入一段代码，如果没有函数体，需要包装一层，并且处理下返回值。、</p>
<p>代码在<a href="https://github.com/QuarkGluonPlasma/babel-plugin-exercize#babel-plugin-exercize" target="_blank" rel="nofollow noopener noreferrer">这里</a>，建议自己实现一遍。</p>
<p>详见掘金小册<a href="https://juejin.cn/book/6946117847848321055" target="_blank">《babel 插件通关秘籍》</a>。</p></div>  
</div>
            