
---
title: '为什么说用 babel 编译 typescript 是更好的选择'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a42373db7cc74793b8b36d4952931a6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 12:05:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a42373db7cc74793b8b36d4952931a6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<p>typescript 给 javascript 扩展了类型的语法和语义，让 js 代码达到了静态类型语言级别的类型安全，之前只能在运行时发现的类型不安全的问题，现在能在编译期间发现了，所以大项目越来越多的选择用 typescript 来写。除此之外，typescript 还能够配合 ide 做更好的智能提示，这也是用 typescript 的一个理由。</p>
<blockquote>
<p>类型安全： 如果一个类型的变量赋值给它不兼容类型的值，这就是类型不安全，如果一个类型的对象，调用了它没有的方法，这也是类型不安全。反之，就是类型安全。类型安全就是变量的赋值、对象的函数调用都是在类型支持的范围内。</p>
</blockquote>
<p>最开始 typescript 代码只有自带的 tyepscript compiler（tsc）能编译，编译不同版本的 typescript 代码需要用不同版本的 tsc，通过配置 tsconfig.json 来指定如何编译。</p>
<p>但是 tsc 编译 ts 代码为 js 是有问题的：</p>
<p>tsc 不支持很多还在草案阶段的语法，这些语法都是通过 babel 插件来支持的，所以很多项目的工具链是用 tsc 编译一遍 ts 代码，之后再由 babel 编译一遍。这样编译链路长，而且生成的代码也不够精简。</p>
<p>所以，typescript 找 babel 团队合作，在 babel7 中支持了 typescript 的编译，可以通过插件来指定 ts 语法的编译。比如 api 中是这样用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>);

parser.parse(sourceCode, &#123;
    <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'typescript'</span>]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个插件是 typescript 团队与 babel 团队合作了一年的成果。</p>
<p>但是，这个插件真的能支持所有 typescript 代码么？ 答案是否定的。</p>
<p>我们来看一下 babel 不支持哪些 ts 语法，为什么不支持。</p>
<h2 data-id="heading-0">babel 能编译所有 typescript 代码么？</h2>
<p>babel 的编译流程是这样的：</p>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a42373db7cc74793b8b36d4952931a6c~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>parser: 把源码 parse 成 ast</li>
<li>traverse：遍历 ast，生成作用域信息和 path，调用各种插件来对 ast 进行转换</li>
<li>generator：把转换以后的 ast 打印成目标代码，并生成 sourcemap</li>
</ul>
<p>而 typescript compiler 的编译流程是这样的：</p>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c3ad31d14c3497c9cda1203c17855b9~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>scanner + parser： 分词和组装 ast，从源码到 ast 的过程</li>
<li>binder + checker： 生成作用域信息，进行类型推导和检查</li>
<li>transform：对经过类型检查之后的 ast 进行转换</li>
<li>emitter： 打印 ast 成目标代码，生成 sourcemap 和类型声明文件（根据配置）</li>
</ul>
<p>其实 babel 的编译阶段和 tsc 的编译阶段是类似的，只是 tsc 多了一个 checker，其余的部分没什么区别。</p>
<ul>
<li>babel 的 parser 对应 tsc 的 scanner + parser</li>
<li>babel 的 traverse 阶段 对应 tsc 的 binder + transform</li>
<li>babel 的 generator 对应 tsc 的 emitter</li>
</ul>
<p>那么能不能基于 babel 的插件在 traverse 的时候实现 checker 呢？</p>
<p>答案是不可以。</p>
<p>因为 tsc 的类型检查是需要拿到整个工程的类型信息，需要做类型的引入、多个文件的 namespace、enum、interface 等的合并，而 babel 是单个文件编译的，不会解析其他文件的信息。所以做不到和 tsc 一样的类型检查。</p>
<p><strong>一个是在编译过程中解析多个文件，一个是编译过程只针对单个文件，流程上的不同，导致 babel 无法做 tsc 的类型检查。</strong></p>
<p>那么 babel 是怎么编译 typescript 的呢？</p>
<p>其实 babel 只是能够 parse ts 代码成 ast，不会做类型检查，会直接把类型信息去掉，然后打印成目标代码。</p>
<p>这导致了有一些 ts 语法是 babel 所不支持的：</p>
<ul>
<li>
<p>const enum 不支持。const enum 是在编译期间把 enum 的引用替换成具体的值，需要解析类型信息，而 babel 并不会解析，所以不支持。可以用相应的插件把 const enum 转成 enum。</p>
</li>
<li>
<p>namespace 部分支持。不支持 namespace 的跨文件合并，不支持导出非 const 的值。这也是因为 babel 不会解析类型信息且是单文件编译。</p>
</li>
</ul>
<p>上面两种两个是因为编译方式的不同导致的不支持。</p>
<ul>
<li>
<p>export = import = 这种 ts 特有语法不支持，可以通过插件转为 esm</p>
</li>
<li>
<p>如果开启了 jsx 编译，那么 <string> aa 这种类型断言不支持，通过 aa as string 来替代。这是因为这两种语法有冲突，在两个语法插件(jsx、typescript)里，解决冲突的方式就是用 as 代替。</p>
</li>
</ul>
<p>这四种就是 babel 不支持的 ts 语法，其实影响并不大，这几个特性不用就好了。</p>
<p><strong>结论：babel 不能编译所有 typescript 代码，但是除了 namespace 的两个特性外，其余的都可以做编译。</strong></p>
<p>babel 是可以编译 typescript 代码，那么为什么要用 babel 编译呢？</p>
<h2 data-id="heading-1">为什么要用 babel 编译 typescript 代码？</h2>
<p>babel 编译 typescript 代码有 3 个主要的优点：</p>
<h3 data-id="heading-2">产物体积更小</h3>
<h4 data-id="heading-3">tsc</h4>
<p>tsc 如何配置编译目标呢？</p>
<p>在 compilerOptions 里面配置 target，target 设置目标语言版本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">compilerOptions</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">"es5"</span> <span class="hljs-comment">// es3、es2015</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>typescript 如何引入 polyfill 呢？</p>
<p>在入口文件里面引入 core-js.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'core-js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">babel7</h4>
<p>babel7 是如何配置编译目标呢？</p>
<p>在 preset-env 里面指定 targets，直接指定目标运行环境（浏览器、node）版本，或者指定 query 字符串，由 browserslist 查出具体的版本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">presets</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">targets</span>: &#123;
                    <span class="hljs-attr">chrome</span>: <span class="hljs-number">45</span>
                &#125;
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">presets</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">targets</span>: <span class="hljs-string">"last 1 version,> 1%,not dead"</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel7 如何引入 polyfill 呢？</p>
<p>也是在 @babel/preset-env 里面配置，除了指定 targets 之外，还要指定 polyfill 用哪个（corejs2 还是 corejs3），如何引入（entry 在入口引入 ，usage 每个模块单独引入用到的）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">presets</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">targets</span>: <span class="hljs-string">"last 1 version,> 1%,not dead"</span>,
                <span class="hljs-attr">corejs</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样可以根据 @babel/compat-data 的数据来针对的做语法转换和 api 的 polyfill：</p>
<p><strong>先根据 targets 查出支持的目标环境的版本，再根据目标环境的版本来从所有特性中过滤支持的，剩下的就是不支持的特性。只对这些特性做转换和 polyfill 即可。</strong></p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c646b073afa9487d9204adc63445a283~tplv-k3u1fbpfcp-watermark.image" width="50%" loading="lazy" referrerpolicy="no-referrer">
<p>而且 babel 还可以通过 @babel/plugin-transform-runtime 来把全局的 corejs 的 import 转成模块化引入的方式。</p>
<p>显然，用 babel 编译 typescript 从产物上看有两个优点：</p>
<ul>
<li>能够做更精准的按需编译和 polyfill，产物体积更小</li>
<li>能够通过插件来把 polyfill 变成模块化的引入，不污染全局环境</li>
</ul>
<p>从产物来看，babel 胜。</p>
<h3 data-id="heading-5">支持的语言特性</h3>
<p>typescript 默认支持很多 es 的特性，但是不支持还在草案阶段的特性，babel 的 preset-env 支持所有标准特性，还可以通过 proposal 来支持更多还未进入标准的特性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'@babel/proposal-xxx'</span>],
    <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/presets-env'</span>, &#123;...&#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从支持的语言特性来看，babel 胜。</p>
<h3 data-id="heading-6">编译速度</h3>
<p>tsc 会在编译过程中进行类型检查，类型检查需要综合多个文件的类型信息，要对 AST 做类型推导，比较耗时，而 babel 不做类型检查，所以编译速度会快很多。</p>
<p>从编译速度来看， babel 胜。</p>
<p>总之，从编译产物大小（主要）、支持的语言特性、编译速度来看，babel 完胜。</p>
<p>但是，babel 不做类型检查，那怎么类型检查呢？</p>
<h2 data-id="heading-7">babel 和 tsc 的结合</h2>
<p>babel 可以编译生成更小的产物，有更快的编译速度和更多的特性支持，所以我们选择用 babel 编译 typescript 代码。但是类型检查也是需要的，可以在 npm scripts 中配一个命令：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"scripts"</span>: &#123;
        <span class="hljs-string">"typeCheck"</span>: <span class="hljs-string">"tsc --noEmit"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在需要进行类型检查的时候单独执行一下 npm run typeCheck 就行了，但最好在 git commit 的 hook 里（通过 husky 配置）再执行一次强制的类型检查。</p>
<h2 data-id="heading-8">总结</h2>
<p>typescript 给 js 扩展了静态类型的支持，使得代码能够在编译期间检查出赋值类型不匹配、调用了没有的方法等错误，保证类型安全。</p>
<p>除了 tsc 之外，babel7 也能编译 typescript 代码了，这是两个团队合作一年的结果。</p>
<p>但是 babel 因为单文件编译的特点，做不了和 tsc 的多文件类型编译一样的效果，有几个特性不支持（主要是 namespace 的跨文件合并、导出非 const 的值），不过影响不大，整体是可用的。</p>
<p>babel 做代码编译，还是需要用 tsc 来进行类型检查，单独执行 tsc --noEmit 即可。</p>
<p>babel 编译 ts 代码，相比 tsc 有很多优点：产物体积更小，支持更多特性，编译速度更快。所以用 babel 编译 typescript 是一个更好的选择。</p>
<p>更多内容，见掘金小册<a href="https://juejin.cn/book/6946117847848321055" target="_blank">《babel 插件通关秘籍》</a>。</p></div>  
</div>
            