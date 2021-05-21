
---
title: '从源码聊 postcss 和 babel 的 api 风格的不同'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41356a588c034f07a91b3b23b829be7f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 08:54:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41356a588c034f07a91b3b23b829be7f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>babel 是一个 js 到 js 的转译器，可以通过语法插件支持 es next、typescript、flow 等语法，支持 AST 转换插件，最后生成目标代码和 sourcemap。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41356a588c034f07a91b3b23b829be7f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>postcss 是一个 css 到 css 的转译器，可以通过语法插件支持 less、sass、stylus 等语法，也支持 AST 转换插件，最后生成目标代码和 sourcemap。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db247caabd1a4c38bd397b145126e700~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>postcss 之于 css，就像 babel 之于 js 一样，postcss 的插件体系也很繁荣，比如 autoprefixer、stylelint 等。</p>
<p>这俩工具在定位上类似，都是用于代码的转译和静态分析。但是在 api 设计上有所不同。</p>
<p>学完这篇文章你会了解到：</p>
<ul>
<li>babel、postcss 的 api 的简易使用</li>
<li>babel、postcss 的编译流程</li>
<li>postcss 的源码架构</li>
<li>postcss 和 babel 在 api 设计上的不同</li>
<li>链式和集中式的 api 风格各有什么好处</li>
</ul>
<h2 data-id="heading-0">babel api</h2>
<p>我们先从熟悉的 babel 开始，babel 7 的 api 一般这样用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> babel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/core'</span>);

<span class="hljs-keyword">const</span> code = <span class="hljs-string">`
    console.log('hello world');
`</span>;
<span class="hljs-keyword">const</span> &#123; code, map &#125; = babel.transformSync(code, &#123;
    <span class="hljs-attr">plugins</span>: [
        [
            pluginA,
            &#123;
                <span class="hljs-comment">// options</span>
            &#125;
        ]
    ],
    <span class="hljs-attr">sourceMaps</span>: <span class="hljs-literal">true</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 babel core 包的 transformSync 的 api，传入源码和转换插件。babel 会在内部完成<strong>源码到 AST 的 parse</strong>，<strong>AST 的 transform</strong>，以及<strong>目标代码和 sourcemap 的 generate</strong> 三个阶段。</p>
<p>我们可以用 babel3 的源码来了解下内部做了什么（babel3 的源码比较清晰，感兴趣可以去看看）：</p>
<p>首先，babel 通过 File 对象来保存处理的文件的源码等信息，然后调用 parse
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96dc8f091f82476db57a51bc6700aed2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>parse 方法里面会完成 parse、transform、generate 这 3 步：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed71cec08a3a4c92b9fdcb5cea93b8ce~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而 parse 在 babel 3 的时候还是直接使用了 acorn（babel 7 的 parser 是 fork 了 acorn 做的修改）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a049ca9de89451cab7bf632375cd898~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>transform 阶段会调用所有内置的 transformer 插件对 AST 进行转换：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41a24dd7a8de49619585a570ceec6a48~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而 generate 阶段会生成目标代码和 sourcemap：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7f220b93d0b4d17b8e316b5f2551d7f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>babel 后续做了很多的迭代，比如分成了很多包，但是这个流程是没有变的。</p>
<p>我们有的时候也会直接用更底层的包，而不使用 babel core：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>);
<span class="hljs-keyword">const</span> traverse = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/traverse'</span>).default;
<span class="hljs-keyword">const</span> generate = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/generator'</span>).default;

<span class="hljs-keyword">const</span> code = <span class="hljs-string">`
    console.log('hello world');
`</span>;

<span class="hljs-keyword">const</span> ast = parser.parse(code);

traverse(ast, &#123;
    <span class="hljs-attr">visitor</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-comment">//xxx</span>
        &#125;
    &#125;
&#125;);

<span class="hljs-keyword">const</span> &#123; code, map &#125; = generate(ast, &#123;
    <span class="hljs-attr">sourceMaps</span>: <span class="hljs-literal">true</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 @babel/core 是基于 @babel/parser、@babel/traverse、@babel/generator 等包做的封装，支持了插件能力。如果不需要插件，那么直接用这些包就行。</p>
<h3 data-id="heading-1">postcss api</h3>
<p>postcss 的 api 是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> postcss = <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss'</span>);
<span class="hljs-keyword">const</span> autoprefixer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)

<span class="hljs-keyword">const</span> css = <span class="hljs-string">`
@import "aaa";
a &#123;
   background: color;
&#125;`</span>;

postcss([autoprefixer]).process(css).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
 <span class="hljs-built_in">console</span>.log(result.css)
&#125;)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先调用 postcss 函数传入插件数组，然后调用 process 方法处理传入的 css，再调用 then 就可以在回调里面拿到结果（目标代码和 sourcemap）。</p>
<p>为什么会是这样的顺序呢，我们从源码角度看一下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32b253d14eb46a0a85526148e80e29a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先调用的 postcss 方法返回 Processor 对象，而 Processor 对象有 use（应用插件）、process（处理 css） 等方法，所以才是 postcss([]).process</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57b2049a37904ac8ab671e64c418de58~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们可以看到 process 返回的值是 LazyResult 对象，而 LazyResult 对象会调用 parser 对传入的 css 进行 parse，提供了 then 方法来返回结果，所以是 postcss([]).process(css).then(() => &#123;&#125;)。</p>
<p>then 里面会调用 aync，会应用插件，处理 AST（root），最终返回 stringifier 的结果。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a6640927ae3486883bf775f2a6c3e08~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>stringifier 里会调用 MapGenerator 把 AST 打印成目标 css，并生成 sourcemap。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00a75960014744e983c14106b870221c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是 postcss 的编译流程。</p>
<p>postcss 其实依然是 parse、transform、generate 3 步，只不过 api 不同。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5510ddeb0cc4c479974fe66bf1f3316~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>postcss 内部有这些类：</p>
<ul>
<li><code>Processor</code>：传入插件，返回 LazyResult，有 use（传入插件）、process（返回结果） 方法</li>
<li><code>LazyResult</code>：传入源码，调用 Parser 对源码进行 parse，有 then（异步获取结果）方法，会用插件对 AST 转换，然后调用 MapGenerator 打印 AST</li>
<li><code>Parser</code>：传入源码，返回 AST</li>
<li><code>MapGenerator</code>： 传入 AST，打印成目标代码，并生成 sourcemap。</li>
</ul>
<p>再回到开始，我们调用的方式是</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">postcss([autoprefixer]).process(css).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
 <span class="hljs-built_in">console</span>.log(result.css)
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 postcss 就是个工厂函数，用于创建 Processsor 对象，Processor 对象的 process 方法返回 LazyResult 对象，LazyResult 对象有 then 方法来返回结果。</p>
<h3 data-id="heading-2">链式和集中式的 api 风格</h3>
<p>postcss 和 babel 都是对代码（js、css）的转译，但是 api 却差别挺大，来对比下：</p>
<p>babel 是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; code, map &#125; = babel.transformSync(code, &#123;
    <span class="hljs-attr">plugins</span>: [
        [
            pluginA,
            &#123;
                <span class="hljs-comment">// options</span>
            &#125;
        ]
    ],
    <span class="hljs-attr">sourceMaps</span>: <span class="hljs-literal">true</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>postcss 是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">postcss([autoprefixer]).process(css).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
 <span class="hljs-built_in">console</span>.log(result.css)
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 babel 只有一个 api，一次性传入源码和插件，在内部完成 parse、transform、generate 3个阶段。</p>
<p>postcss 则是提供了链式的 api，分多步传入插件和源码。</p>
<p>postcss 这种链式的风格的好处是代码紧凑，每一步做了什么都比较明确。babel 这种一次性传入的好处是使用简单，但是 option 耦合在一块，复杂度高。</p>
<p>链式的多次传入，还是集中式的一次传入，都有自己的好处，比如 jquery、chalk、jest、webpack-chain 都是链式的，而 webpack、babel 等都是一次性传入的。</p>
<p>jest api 风格（链式）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test(<span class="hljs-string">`jest`</span>, <span class="hljs-function">() =></span> &#123;
    expect(a + b).not.toBeLessThan(expected);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chalk api 风格（链式）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">chalk.rgb(<span class="hljs-number">123</span>, <span class="hljs-number">45</span>, <span class="hljs-number">67</span>).underline(<span class="hljs-string">'Underlined reddish color'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack-chain api 风格（链式）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config
  .entry(<span class="hljs-string">'index'</span>)
    .add(<span class="hljs-string">'src/index.js'</span>)
    .end()
  .output
    .path(<span class="hljs-string">'dist'</span>)
    .filename(<span class="hljs-string">'[name].bundle.js'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack api 风格（集中式）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">webpack(&#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结</h2>
<p>本文我们通过 babel 和 postcss 的 api 用法分别探究了下内部的实现流程，知道了为什么 postcss 是 postcss([plugins]).process(css).then 的调用链。</p>
<p>之后分别梳理了 babel 的集中式风格 api、postcss 的链式风格 api 的优缺点，并且引申出了其他的一些库的 api 风格。知道了其实做同一件事情是可以设计出不同的 api 的。</p>
<p>希望这篇文章能够让你清楚 postcss 和 babel 内部的流程都是啥，为什么 postcss 的api 调用链条是那样的，它们都是什么 api 风格。链式和集中式都有什么优缺点。</p></div>  
</div>
            