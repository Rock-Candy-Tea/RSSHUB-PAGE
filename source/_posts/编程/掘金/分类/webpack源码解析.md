
---
title: 'webpack源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3acb30d4dce445c8e0386c8dfab6471~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 02:16:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3acb30d4dce445c8e0386c8dfab6471~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言</strong>：
webpack作为一个打包工具，它的入参是各种静态文件和配置参数，可以实现灵活的可扩展性的插件配置和loaders加载，最后输出打包后的bundle文件。下图是官网中的webpack打包示意图，webpack可以打包全世界！
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3acb30d4dce445c8e0386c8dfab6471~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在使用webpack的过程中，一直有几个疑问萦绕脑海：</p>
<ul>
<li>webpack中间的处理流程究竟做了些什么？</li>
<li>我们平时配置的loaders、plugins都在哪个阶段起作用？</li>
<li>webpack是如何支持如此复杂的配置而又不影响性能的？</li>
</ul>
<p>在分析源码之前，我们必须要先了解一下Tapable这个东西（第3个问题的答案）。
Webpack本质上是事件驱动的，从一个事件，走向下一个事件。它的整个编译过程中暴露出来大量的 Hook 供内部/外部插件使用，而实现这一切的核心就是Tapable。Tapable 类似于发布订阅模式，但是它提供了更加复杂的钩子类型，我们可以理解为webpack打包流程是由打包阶段的各个事件组成的，而插件的实现就是在这些事件钩子上绑定属于自己的回调函数，这样就实现了webpack的可扩展性。</p>
<p>可参考这篇文章：
<a href="https://blog.csdn.net/weixin_38208314/article/details/115166713" target="_blank" rel="nofollow noopener noreferrer">webpack tapable啥玩意？</a></p>
<p>我们一起来看一下吧，首先举个🌰说明webpack在做什么？</p>
<h2 data-id="heading-0">一.举例说明webpack在做什么？</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// a.js (webpack config 入口文件)</span>
<span class="hljs-keyword">import</span> add <span class="hljs-keyword">from</span> <span class="hljs-string">'./b.js'</span>

add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)

<span class="hljs-keyword">import</span>(<span class="hljs-string">'./c'</span>).then(<span class="hljs-function"><span class="hljs-params">del</span> =></span> del(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>))

-----

<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">import</span> mod <span class="hljs-keyword">from</span> <span class="hljs-string">'./d.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n1 + n2
&#125;

mod(<span class="hljs-number">100</span>, <span class="hljs-number">11</span>)

-----

<span class="hljs-comment">// c.js</span>
<span class="hljs-keyword">import</span> mod <span class="hljs-keyword">from</span> <span class="hljs-string">'./d.js'</span>

mod(<span class="hljs-number">100</span>, <span class="hljs-number">11</span>)

<span class="hljs-keyword">import</span>(<span class="hljs-string">'./b.js'</span>).then(<span class="hljs-function"><span class="hljs-params">add</span> =></span> add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>))

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">del</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n1 - n2
&#125;
-----

<span class="hljs-comment">// d.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mod</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n1 % n2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>各个文件的依赖关系如下：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc148858faeb4938a2ffdd6fc07915ea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">app</span>: <span class="hljs-string">'a.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash:8].js'</span>,
    <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'[name].bundle.[chunkhash:8].js'</span>,
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/'</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码经过webpack打包之后，最终会输出2个打包文件：</p>
<ul>
<li>app.js - 包含了 a.j、b.js、d.js 的代码</li>
<li>0.bundle.js - 包含了 c.js 的代码</li>
</ul>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f98b28e09a9c4abc8e34ca066f2e1f52~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
看到这里，我们看到webpack将我们的文件按照某种规则进行打包输出（当然目前为止我们还没有用到插件和loaders），如果不知道这两个包是如何输出的也没关系，后面会再解释。</p>
<p><strong>webpack到底怎么做到的</strong>？我们开始进入正题吧，本文只解析部分核心webpack源码，抛砖引玉，让大家对webpack的运行流程有一个大致的了解。</p>
<p>在打包的时候我们会在命令行执行以下打包命令：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">webpack --config webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该命令在webpack-cli中相当于执行以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用，这里模仿webpack-cli中的代码，相当于在命令行里输入webpack。</span>
<span class="hljs-keyword">const</span> options = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./webpack.config.js"</span>);
<span class="hljs-keyword">const</span> compiler = webpack(options);

compiler.run();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单解释：加载webpack配置文件，传给webpack文件，返回一个编译器compiler，运行编译器。
so，我们先来看看webpack入口---webpack.js做了什么？</p>
<h2 data-id="heading-1">一 .webpack.js</h2>
<p>下面这段代码是webpack.js的主要部分：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> webpack = <span class="hljs-function">(<span class="hljs-params">options, callback</span>) =></span> &#123;
...
<span class="hljs-comment">// 用我们自定义的配置覆盖webpack默认的配置 返回综合配置</span>
    options = <span class="hljs-keyword">new</span> WebpackOptionsDefaulter().process(options);
    <span class="hljs-comment">// 将代码入口传入编译器，实例化编译器</span>
    compiler = <span class="hljs-keyword">new</span> Compiler(options.context);
    <span class="hljs-comment">// Node环境插件 挂载在编译器的钩子上</span>
    <span class="hljs-keyword">new</span> NodeEnvironmentPlugin(&#123;...&#125;).apply(compiler);
    <span class="hljs-comment">// 自定义插件 挂载在编译器的钩子上</span>
    options.plugin.apply(compiler);
   ...
    <span class="hljs-comment">// 将webpack配置的其他属性所用到的插件，都挂载在compiler上</span>
    compiler.options = <span class="hljs-keyword">new</span> WebpackOptionsApply().process(options, compiler);
...
<span class="hljs-keyword">return</span> compiler;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里解释几件事情：</p>
<ul>
<li>webpack4.0可以实现零配置，没有用户配置的情况下，它会采用默认的配置将src文件夹下的index.js打包到dist文件夹下的main.js中（其他很多默认配置不赘述）。</li>
<li>new Compiler(options.context)这句代码的意思是将当前文件夹的绝对路径传给编译器。</li>
</ul>
<p>举例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodeEnvironmentPlugin</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
compiler.inputFileSystem = <span class="hljs-keyword">new</span> CachedInputFileSystem(
<span class="hljs-keyword">new</span> NodeJsInputFileSystem(),
<span class="hljs-number">60000</span>
);
<span class="hljs-comment">//....</span>
compiler.hooks.beforeRun.tap(<span class="hljs-string">"NodeEnvironmentPlugin"</span>, <span class="hljs-function"><span class="hljs-params">compiler</span> =></span> &#123;
<span class="hljs-keyword">if</span> (compiler.inputFileSystem === inputFileSystem) inputFileSystem.purge();
&#125;);
&#125;
&#125;
<span class="hljs-built_in">module</span>.exports = NodeEnvironmentPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上图中，是node环境下的一个插件的代码核心。比如我们在解析文件(resolver)的时候，需要用到的文件系统，这个插件就是在compiler的beforeRun钩子上挂载了自己的事件，将文件读取系统挂载在compiler上，使得compiler中的其他插件可以使用文件读取系统。</p>
<p>webpack.js主要做了几件事：
1.整合配置参数（用户配置和默认配置）
2.将node环境的插件和用户配置的插件挂载在compiler各个钩子上，使得各个插件可以在编译的不同阶段执行自己的逻辑。
3.返回compiler</p>
<p>开始执行compiler.run();操作：</p>
<h2 data-id="heading-2">二. compiler.js</h2>
<p>compiler.js是用来控制编译流程的文件。run方法逻辑如下：
beforeRun钩子-->run钩子-->编译compile方法-->编译结束回调onCompiled
run方法核心代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params">callback</span>)</span> &#123;
<span class="hljs-keyword">const</span> onCompiled = <span class="hljs-function">(<span class="hljs-params">err, compilation</span>) =></span> &#123;
<span class="hljs-comment">// 编译结束后的回调函数</span>
<span class="hljs-comment">// 文件输出</span>
&#125;
...
    <span class="hljs-comment">// 触发beforeRun钩子，增加文件存取的功能 </span>
    <span class="hljs-built_in">this</span>.hooks.beforeRun.callAsync(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
      <span class="hljs-comment">// 触发run钩子，处理缓存的模块 减少编译的模块 加快编译速度</span>
      <span class="hljs-built_in">this</span>.hooks.run.callAsync(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
       ...
          <span class="hljs-built_in">this</span>.compile(onCompiled);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这里各种钩子嵌套执行，并没有添加任何功能，但其实插件已经在各种钩子上绑定了自己的事件，webpack实现了功能与实现的解耦，代码逻辑清晰。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.hooks.beforeCompile.callAsync(params, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
      <span class="hljs-comment">// 编译</span>
      <span class="hljs-built_in">this</span>.hooks.compile.call(params);
      <span class="hljs-comment">// newCompilation是webpack使用的编译器</span>
      <span class="hljs-keyword">const</span> compilation = <span class="hljs-built_in">this</span>.newCompilation(params);
      <span class="hljs-comment">// 正式启动编译 </span>
      <span class="hljs-built_in">this</span>.hooks.make.callAsync(compilation, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
      ...
        <span class="hljs-comment">// 编译结束</span>
        compilation.finish(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          ...
          <span class="hljs-comment">// 封装 执行优化的钩子 chunk构建和打包优化</span>
          compilation.seal(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            ...

            <span class="hljs-built_in">this</span>.hooks.afterCompile.callAsync(compilation, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            ...
            <span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, compilation);
            &#125;);
          &#125;);
        &#125;);
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compile函数的逻辑如下：
beforeCompile钩子-->compile钩子-->实例化编译器compilation对象-->make钩子(转换模块)-->编译结束-->seal封装-->afterCompile钩子-->执行compile回调函数</p>
<p>compiler.js文件做的几件事：</p>
<ul>
<li>启动编译。通过实例化编译对象并执行make钩子，编译开始，真正的核心编译工作是由compilation对象做的。</li>
<li>管理输出。编译结束后会执行onCompiled这个回调函数，整理输出数据。</li>
<li>通过钩子控制整个编译流程。</li>
</ul>
<p>下方表格中，分别是compiler的几个钩子，插件就是挂载在编译的不同阶段，在不同的阶段执行不同的插件。</p>







































































<table><thead><tr><th>关键钩子</th><th>钩子类型</th><th>钩子参数</th><th>作用</th></tr></thead><tbody><tr><td>beforeRun</td><td>AsyncSeriesHook</td><td>Compiler</td><td>运行前的准备活动，主要启用了文件读取的功能。</td></tr><tr><td>run</td><td>AsyncSeriesHook</td><td>Compiler</td><td>“机器”已经跑起来了，在编译之前有缓存，则启用缓存，这样可以提高效率。</td></tr><tr><td>beforeCompile</td><td>AsyncSeriesHook</td><td>params</td><td>开始编译前的准备，创建的ModuleFactory，创建Compilation，并绑定ModuleFactory到Compilation上。</td></tr><tr><td>compile</td><td>SyncHook</td><td>params</td><td>编译了</td></tr><tr><td>make</td><td>AsyncParallelHook</td><td>compilation</td><td>从Compilation的addEntry函数，开始构建模块</td></tr><tr><td>afterCompile</td><td>AsyncSeriesHook</td><td>compilation</td><td>编译结束了</td></tr><tr><td>shouldEmit</td><td>SyncBailHook</td><td>compilation</td><td>获取compilation发来的电报，确定编译时候成功，是否可以开始输出了。</td></tr><tr><td>emit</td><td>AsyncSeriesHook</td><td>compilation</td><td>输出文件了</td></tr><tr><td>afterEmit</td><td>AsyncSeriesHook</td><td>compilation</td><td>输出完毕</td></tr><tr><td>done</td><td>AsyncSeriesHook</td><td>Status</td><td>无论成功与否，一切已尘埃落定。</td></tr></tbody></table>
<p>编译回调函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> onCompiled = <span class="hljs-function">(<span class="hljs-params">err, compilation</span>) =></span> &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hooks.shouldEmit.call(compilation) === <span class="hljs-literal">false</span>) &#123;
...
<span class="hljs-built_in">this</span>.hooks.done.callAsync(stats, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
...
    &#125;
    <span class="hljs-keyword">return</span>

&#125;
<span class="hljs-built_in">this</span>.emitAssets(compilation, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    ...
    <span class="hljs-keyword">if</span> (compilation.hooks.needAdditionalPass.call()) &#123;
    ...
    <span class="hljs-built_in">this</span>.hooks.done.callAsync(stats, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;&#125;);
    &#125;;
&#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数的作用就是将编译后的内容生成文件。先调用shouldEmit判断是否编译成功，成功之后就调用Compiler.emitAssets方法打包文件。我们可以看到compiler文件通过各种钩子控制了整个编译流程。但是真正的编译是在compilation.js文件中。</p>
<p>so?我们来看一下最核心的编译函数：compilation</p>
<h2 data-id="heading-3">三. compilation.js</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 正式启动编译 </span>
  <span class="hljs-built_in">this</span>.hooks.make.callAsync(compilation, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-comment">// 编译结束</span>
    compilation.finish(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在compiler.js中，我们发现，在执行了make钩子之后，并没有执行任何的compilation对象的方法，而是在它的回调函数中直接执行了compilation.finish方法。那编译到底是如何做到的？其实，在关于入口的插件中，在make这个钩子上绑定了事件，其中执行了addEntry这个添加入口的操作，从这里就开始了真正的编译过程。</p>
<p><strong>插播</strong>：在执行添加入口addEntry操作之前，入口插件做了哪些准备工作呢？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// WebpackOptionsApply.js</span>
<span class="hljs-keyword">new</span> EntryOptionPlugin().apply(compiler);
compiler.hooks.entryOption.call(options.context, options.entry);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，在EntryOptionsPlugin中注册了compiler.hooks.entryOption钩子的事件处理函数，它会根据入口值entry的类型不同，区分单入口/多入口，实例化不同的插件类型。（<code>SingleEntryPlugin</code>，<code>MultiEntryPlugin</code>等）
<strong>插播结束！</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//SingleEntryPlugin.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SingleEntryPlugin</span> </span>&#123;
...
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
compiler.hooks.compilation.tap(
      <span class="hljs-string">"SingleEntryPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        <span class="hljs-comment">// 存储键值对 将 SingleEntryDependency 和 normalModuleFactory关联起来</span>
        compilation.dependencyFactories.set(
          SingleEntryDependency,
          normalModuleFactory
        );
      &#125;
    );
    compiler.hooks.make.tapAsync(
      <span class="hljs-string">"SingleEntryPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, callback</span>) =></span> &#123;
        ...
        compilation.addEntry(context, dep, name, callback);
      &#125;
    );
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们以单入口为例，看一下SingleEntryPlugin做了些什么事情？</p>
<ol>
<li>注册了 compilation 事件回调。</li>
<li>注册了 make 事件回调。</li>
</ol>
<ul>
<li>compilation事件是在实例化编译器的时候触发的，在make动作执行之前，绑定这个钩子的插件可以获得两个参数，一个是编译器本身，一个是模块工厂。该回调函数的作用是将SingleEntryDependency和normalModuleFactory关联起来。</li>
<li>在make阶段的时候调用addEntry 方法，然后进入 _addModuleChain 进入正式的编译阶段。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// compiler.js</span>
<span class="hljs-function"><span class="hljs-title">addEntry</span>(<span class="hljs-params">context, entry, name, callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.hooks.addEntry.call(entry, name);
...
    <span class="hljs-built_in">this</span>._addModuleChain(
      ...
      <span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>addEntry方法做了两件事：
1.调用addEntry钩子
2.调用_addModuleChain方法，执行结束后，将执行make钩子携带过来的回调函数，告知compiler编译结束。
_addModuleChain做了几件事（重点）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">_addModuleChain</span>(<span class="hljs-params">context, dependency, onModule, callback</span>)</span> &#123;
...
    <span class="hljs-comment">// 获取模块工厂类型</span>
    <span class="hljs-keyword">const</span> moduleFactory = <span class="hljs-built_in">this</span>.dependencyFactories.get(Dep);
   ...
    <span class="hljs-built_in">this</span>.semaphore.acquire(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 创建新模块 module</span>
      moduleFactory.create(
    ...
    <span class="hljs-comment">// 将模块加入到compilation.modules中</span>
          <span class="hljs-keyword">const</span> addModuleResult = <span class="hljs-built_in">this</span>.addModule(<span class="hljs-built_in">module</span>);
          <span class="hljs-built_in">module</span> = addModuleResult.module;
          <span class="hljs-comment">// 入口模块加入compilation.entries</span>
          onModule(<span class="hljs-built_in">module</span>);
          
          <span class="hljs-comment">// 处理模块的依赖 再转换依赖 组成模块链</span>
          <span class="hljs-keyword">const</span> afterBuild = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span> (addModuleResult.dependencies) &#123;
              <span class="hljs-built_in">this</span>.processModuleDependencies(<span class="hljs-built_in">module</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                ...
              &#125;);
            &#125; 
          &#125;;

          <span class="hljs-keyword">if</span> (addModuleResult.build) &#123;
            <span class="hljs-comment">// 构建 转换模块代码（parse loader generate）</span>
            <span class="hljs-built_in">this</span>.buildModule(<span class="hljs-built_in">module</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
              ...
              <span class="hljs-comment">// 判断依赖</span>
              afterBuild();
            &#125;);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_addModuleChain流程分析：</p>
<p>1）<strong>获取入口对应的模块工厂类型</strong></p>
<p>根据不同 dependency 类型，获取 multiModuleFactory（多入口模块的生产工厂） 或者normalModuleFacotry（单入口模块的工厂）
2)  <strong>调用moduleFactory.create创建入口模块</strong></p>
<p>对于单入口来说，moduleFactory.create调用的是normalModuleFacotry的create方法。该方法主要作用就是获取文件和loaders对应的绝对路径，并实例化模块工厂创建模块。
<strong>插播</strong>：moduleFactory.create做了什么？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">data, callback</span>)</span> &#123;
<span class="hljs-comment">//...省略部分逻辑</span>
<span class="hljs-built_in">this</span>.hooks.beforeResolve.callAsync(
&#123;
contextInfo,
resolveOptions,
context,
request,
dependencies
&#125;,
<span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
<span class="hljs-comment">//...</span>
<span class="hljs-comment">// 触发 normalModuleFactory 中的 factory 事件。</span>
<span class="hljs-keyword">const</span> factory = <span class="hljs-built_in">this</span>.hooks.factory.call(<span class="hljs-literal">null</span>);
<span class="hljs-comment">// Ignored</span>
<span class="hljs-keyword">if</span> (!factory) <span class="hljs-keyword">return</span> callback();
factory(result, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
<span class="hljs-comment">//...</span>
callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
&#125;);
&#125;
);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>触发 beforeResolve 事件</li>
<li>触发 NormalModuleFactory 中的 factory 事件。在 NormalModuleFactory 的 constructor 中有一段注册 factory 事件的逻辑。</li>
<li>执行 factory 方法，主要流程如下：</li>
</ul>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a19741bd7b0f41ba943baeaac95170a5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
factory 方法做了两件事情：获取文件的绝对路径及其对应的loaders的绝对路径，生成normalModule实例，并将文件路径和loaders路径存放到该实例中。</p>
<p><strong>插播结束</strong></p>
<p>3）<strong>addModule</strong>
得到模块实例之后，将其存放于全局的 Compilation.modules 数组中和 _modules 对象中。
这个阶段可以看成add阶段，他会将module的所有信息都存于Compilation 中，以便于在最后打包成 chunk 的时候使用。</p>
<p>4）<strong>调用buildModule解析模块，输出依赖列表</strong>
该阶段做了以下几件事情：</p>
<ul>
<li>运行Loader</li>
<li>Parser解析出AST</li>
<li>walkStatements解析出依赖</li>
</ul>
<p><strong>插播</strong>：buildModule做了什么事情？
moduleNormalModule 的实例，Compilation.buildModule实际上调用的是NormalModule.build 方法：build方法逻辑如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// NormalModule.build 方法</span>
<span class="hljs-function"><span class="hljs-title">build</span>(<span class="hljs-params">options, compilation, resolver, fs, callback</span>)</span> &#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.doBuild(options, compilation, resolver, fs, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-keyword">try</span> &#123;
       <span class="hljs-comment">// 这里会将 source 转为 AST，分析出所有的依赖</span>
<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.parser.parse(<span class="hljs-comment">/*参数*/</span>);
<span class="hljs-keyword">if</span> (result !== <span class="hljs-literal">undefined</span>) &#123;
<span class="hljs-comment">// parse is sync</span>
handleParseResult(result);
&#125;
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
handleParseError(e);
&#125;
  &#125;)
&#125;

<span class="hljs-comment">// NormalModule.doBuild 方法</span>
<span class="hljs-function"><span class="hljs-title">doBuild</span>(<span class="hljs-params">options, compilation, resolver, fs, callback</span>)</span> &#123;
<span class="hljs-comment">//...</span>
<span class="hljs-comment">// 执行各种 loader</span>
runLoaders(
&#123;
<span class="hljs-attr">resource</span>: <span class="hljs-built_in">this</span>.resource,
<span class="hljs-attr">loaders</span>: <span class="hljs-built_in">this</span>.loaders,
<span class="hljs-attr">context</span>: loaderContext,
<span class="hljs-attr">readResource</span>: fs.readFile.bind(fs)
&#125;,
<span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
<span class="hljs-comment">//...</span>
<span class="hljs-comment">// createSource 会将 runLoader 得到的结果转为字符串以便后续处理</span>
<span class="hljs-built_in">this</span>._source = <span class="hljs-built_in">this</span>.createSource(
<span class="hljs-built_in">this</span>.binary ? asBuffer(source) : asString(source),
resourceBuffer,
sourceMap
);
<span class="hljs-comment">//...</span>
&#125;
);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分为两部分：</p>
<ul>
<li>doBuild函数：对源文件执行loaders，doBuild方法才是真正取到了文件的内容，并用loaders对其进行处理。</li>
<li>doBuild函数回调：使用acorn将代码转换为ast抽象语法树，遍历ast找出该文件的所有依赖，为该module增加依赖（dependency 实例），每一个dependency 实例都有一个template方法，template中保存着源代码中该依赖的字符位置range，在最后生成文件的时候，会将该range替换成依赖文件的内容。</li>
</ul>
<p>4）<strong>执行buildModule的回调函数afterBuild</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> afterBuild = <span class="hljs-function">() =></span> &#123;
...
<span class="hljs-comment">// 如果有依赖，则进入 processModuleDependencies</span>
<span class="hljs-keyword">if</span> (addModuleResult.dependencies) &#123;
<span class="hljs-built_in">this</span>.processModuleDependencies(<span class="hljs-built_in">module</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> callback(err);
callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
&#125;);
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行processModuleDependencies方法，处理模块依赖</li>
<li>处理依赖的方式与主文件类似，会重复执行reate-->build-->add-->processDep整个流程，构建完整的模块链。</li>
</ul>
<p>完成编译过程生成模块链之后，执行make事件的回调函数，告知compiler编译完毕。开始执行seall封装操作。</p>
<h2 data-id="heading-4">四.seal封装</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.hooks.make.callAsync(compilation, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        ...
          compilation.seal(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          ...
            <span class="hljs-built_in">this</span>.hooks.afterCompile.callAsync(compilation, err
             ...
            &#125;);
          &#125;);
        &#125;);
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>make编译过程结束后，开始执行compilation的seal钩子，开始chunk的构建和优化打包过程。
此过程会根据入口文件、配置中关于优化分包的参数去合并生成多个chunk。
因为这部分代码过于冗长，且嵌套很多，这里就不粘贴代码进行解析了，接下来，我们以文章开头的代码为例说明chunk形成的过程，便于理解：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea4e41eac8c04f0f9d7aa1096e90d84f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>首先，webpack会为所有的module生成<strong>module graph</strong>（模块图谱，如上图）。模块图谱的形成过程就是从入口文件开始，分析每一个模块的同步依赖modules和异步依赖blocks，对于同步依赖，再执行以上步骤。对于异步依赖，会单独拿出来进行分析，便于后面将异步依赖单独进行打包。
<img alt="图2" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/181e7ab3f6d84d8e9f43c9298a9e3ba4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其次，上图是根据<strong>module graph</strong> 生成<strong>basic chunk graph</strong>的结果，生成了3个chunkGroup。basic chunk graph的生成过程是：入口文件和异步文件，webpack会为它们单独生成一个chunk，从入口文件开始，遍历它的同步依赖modules以及依赖modules的依赖...，同时将该模块与入口文件的chunk相关联，直到没有找到同步依赖为止（得到上图第一个chunkGroup）。在遍历的过程中，如果遇到异步依赖，就单独创建一个chunk，再执行以上过程，关联modules和chunk，这样就完成了最后两个chunkGroup的形成。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c33ae07fd7241e6a90ec3f5d065a4bf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
最后一步，得到<strong>优化chunk graph</strong>。观察basic chunk graph的结果：发现三个包中都有d.js，这样打包之后会造成重复打包。后两个异步加载的包中需要的d.js已经在入口包中进行了同步加载，同步加载的优先级大于异步加载，所以后两个chunkGroup需要的d.js可以去掉。再看第三个包中需要的b.js，也已经在入口包中以同步的形式加载过了，所以也不需要，将第三个包删掉，就得到了最终的chunk。</p>
<h2 data-id="heading-5">五.输出打包文件</h2>
<p>整合chunk完毕之后，最后要输出打包文件。我们得到的module、chunk文件都是通过require进行聚合的代码，不可以在浏览器中运行，webpack会提供template模版产生带有_webpack_require()格式的代码（实质上是webpack实现了简单的require函数），这样打包之后的代码就可以在浏览器中运行了。</p>
<p><a href="https://blog.csdn.net/weixin_38208314/article/details/114978932" target="_blank" rel="nofollow noopener noreferrer">关于webpack模块化可参考这篇文章</a></p>
<p>最后，通过emitAssets将最终的js输出到output的path中。</p>
<p>附上一张webpack打包流程图。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b30640cfd3b4f6dbf92a06788161833~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
参考博客：
<a href="https://juejin.cn/post/6844903728735059976#heading-25" target="_blank">juejin.cn/post/684490…</a>
<a href="https://juejin.cn/post/6844903903675285511#heading-4" target="_blank">juejin.cn/post/684490…</a>
<a href="https://juejin.cn/post/6844903864592760845" target="_blank">juejin.cn/post/684490…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            