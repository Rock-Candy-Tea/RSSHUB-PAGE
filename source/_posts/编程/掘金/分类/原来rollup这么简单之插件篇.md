
---
title: '原来rollup这么简单之插件篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2020/4/13/17173eb9fa4b986b?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Mon, 13 Apr 2020 06:26:57 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2020/4/13/17173eb9fa4b986b?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>大家好，我是小雨小雨，致力于分享有趣的、实用的技术文章。</p>
</blockquote>
<blockquote>
<p>内容分为翻译和原创，如果有问题，欢迎随时评论或私信，希望和大家一起进步。</p>
</blockquote>
<blockquote>
<p>大家的支持是我创作的动力。</p>
</blockquote>
<h4 data-id="heading-0">计划</h4>
<p>rollup系列打算一章一章的放出，内容更精简更专一更易于理解</p>
<p>这是rollup系列的最后一篇文章，以下是所有文章链接。</p>
<ul>
<li><a target="_blank" href="https://juejin.im/post/6844904094377705480">rollup.rollup</a></li>
<li><a target="_blank" href="https://juejin.im/post/6844904097171111949">rollup.generate + rollup.write</a></li>
<li><a target="_blank" href="https://juejin.im/post/6844904103550648333">rollup.watch</a></li>
<li><a target="_blank" href="https://juejin.im/post/6844904116414578701">tree shaking</a></li>
<li>plugins <==== 当前文章</li>
</ul>
<h4 data-id="heading-1">TL;DR</h4>
<p>rollup的插件和其他大型框架大同小异，都是提供统一的标准接口，通过约定大于配置定义公共配置，注入当前构建结果相关的属性与方法，供开发者进行增删改查操作。为稳定可持续增长提供了强而有力的铺垫！</p>
<p>但不想webpack区分loader和plugin，rollup的plugin既可以担任loader的角色，也可以胜任传统plugin的角色。rollup提供的钩子函数是核心，比如load、transform对chunk进行解析更改，resolveFileUrl可以对加载模块进行合法解析，options对配置进行动态更新等等~</p>
<h4 data-id="heading-2">注意点</h4>
<blockquote>
<p>所有的注释都在<a target="_blank" href="https://github.com/FoxDaxian/rollup-analysis">这里</a>，可自行阅读</p>
</blockquote>
<blockquote>
<p>!!!提示 => 标有TODO为具体实现细节，会视情况分析。</p>
</blockquote>
<blockquote>
<p>!!!注意 => 每一个子标题都是父标题(函数)内部实现</p>
</blockquote>
<blockquote>
<p>!!!强调 => rollup中模块(文件)的id就是文件地址，所以类似resolveID这种就是解析文件地址的意思，我们可以返回我们想返回的文件id(也就是地址，相对路径、决定路径)来让rollup加载</p>
</blockquote>
<blockquote>
<p>rollup是一个核心，只做最基础的事情，比如提供<a target="_blank" href="https://github.com/FoxDaxian/rollup-analysis/blob/master/src/utils/defaultPlugin.ts#L6">默认模块(文件)加载机制</a>, 比如打包成不同风格的内容，我们的插件中提供了加载文件路径，解析文件内容(处理ts，sass等)等操作，是一种插拔式的设计，和webpack类似
插拔式是一种非常灵活且可长期迭代更新的设计，这也是一个中大型框架的核心，人多力量大嘛~</p>
</blockquote>
<h4 data-id="heading-3">主要通用模块以及含义</h4>
<ol>
<li>Graph: 全局唯一的图，包含入口以及各种依赖的相互关系，操作方法，缓存等。是rollup的核心</li>
<li>PathTracker: 引用(调用)追踪器</li>
<li>PluginDriver: 插件驱动器，调用插件和提供插件环境上下文等</li>
<li>FileEmitter: 资源操作器</li>
<li>GlobalScope: 全局作用局，相对的还有局部的</li>
<li>ModuleLoader: 模块加载器</li>
<li>NodeBase: ast各语法(ArrayExpression、AwaitExpression等)的构造基类</li>
</ol>
<h4 data-id="heading-4">插件机制分析</h4>
<p>rollup的插件其实一个普通的函数，函数返回一个对象，该对象包含一些基础属性(如name)，和不同阶段的钩子函数，像这个样子:</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>plugin</span>(<span>options = &#123;&#125;</span>) </span>&#123;
  <span>return</span> &#123;
    <span>name</span>: <span>'rollup-plugin'</span>,
    transform() &#123;
      <span>return</span> &#123;
        <span>code</span>: <span>'code'</span>,
        <span>map</span>: &#123; <span>mappings</span>: <span>''</span> &#125;
      &#125;;
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>这里是官方建议遵守的<a target="_blank" href="https://rollupjs.org/guide/en/#conventions">约定</a>.</p>
<p>我们平常书写rollup插件的时候，最关注的就是钩子函数部分了，钩子函数的调用时机有三类:</p>
<ol>
<li>const chunks = rollup.rollup执行期间的<a target="_blank" href="https://rollupjs.org/guide/en/#build-hooks">Build Hooks</a></li>
<li>chunks.generator(write)执行期间的<a target="_blank" href="https://rollupjs.org/guide/en/#output-generation-hooks">Output Generation Hooks</a></li>
<li>监听文件变化并重新执行构建的rollup.watch执行期间的watchChange钩子函数</li>
</ol>
<p>除了类别不同，rollup也提供了几种<a target="_blank" href="https://github.com/FoxDaxian/rollup-analysis/blob/master/src/utils/PluginDriver.ts">钩子函数</a>的执行方式，每种方式都又分为同步或异步，方便内部使用：</p>
<ol>
<li>async: 处理promise的异步钩子，也有同步版本</li>
<li>first: 如果多个插件实现了相同的钩子函数，那么会串式执行，从头到尾，但是，如果其中某个的返回值不是null也不是undefined的话，会直接终止掉后续插件。</li>
<li>sequential: 如果多个插件实现了相同的钩子函数，那么会串式执行，按照使用插件的顺序从头到尾执行，如果是异步的，会等待之前处理完毕，在执行下一个插件。</li>
<li>parallel: 同上，不过如果某个插件是异步的，其后的插件不会等待，而是并行执行。</li>
</ol>
<p>文字表达比较苍白，咱们看几个实现：</p>
<ul>
<li>钩子函数: hookFirst
使用场景：resolveId、resolveAssetUrl等</li>
</ul>
<pre><code lang="ts" class="copyable"><span><span>function</span> <span>hookFirst</span><<span>H</span> <span>extends</span> <span>keyof</span> <span>PluginHooks</span>, <span>R</span> = <span>ReturnType</span><<span>PluginHooks</span>[<span>H</span>]>>(<span>
    hookName: H,
    args: Args<PluginHooks[H]>,
    replaceContext?: ReplaceContext | <span>null</span>,
    skip?: <span>number</span> | <span>null</span>
</span>): <span>EnsurePromise</span><<span>R</span>> </span>&#123;
    <span>// 初始化promise</span>
    <span>let</span> promise: <span>Promise</span><<span>any</span>> = <span>Promise</span>.resolve();
    <span>// this.plugins在初始化Graph的时候，进行了初始化</span>
    <span>for</span> (<span>let</span> i = <span>0</span>; i < <span>this</span>.plugins.length; i++) &#123;
        <span>if</span> (skip === i) <span>continue</span>;
        <span>// 覆盖之前的promise，换言之就是串行执行钩子函数</span>
        promise = promise.then(<span>(<span>result: <span>any</span></span>) =></span> &#123;
            <span>// 返回非null或undefined的时候，停止运行，返回结果</span>
            <span>if</span> (result != <span>null</span>) <span>return</span> result;
            <span>// 执行钩子函数</span>
            <span>return</span> <span>this</span>.runHook(hookName, args <span>as</span> <span>any</span>[], i, <span>false</span>, replaceContext);
        &#125;);
    &#125;
    <span>// 最后一个promise执行的结果</span>
    <span>return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>钩子函数: hookFirstSync
使用场景：resolveFileUrl、resolveImportMeta等</li>
</ul>
<pre><code lang="ts" class="copyable"><span>// hookFirst的同步版本，也就是并行执行</span>
<span><span>function</span> <span>hookFirstSync</span><<span>H</span> <span>extends</span> <span>keyof</span> <span>PluginHooks</span>, <span>R</span> = <span>ReturnType</span><<span>PluginHooks</span>[<span>H</span>]>>(<span>
    hookName: H,
    args: Args<PluginHooks[H]>,
    replaceContext?: ReplaceContext
</span>): <span>R</span> </span>&#123;
    <span>for</span> (<span>let</span> i = <span>0</span>; i < <span>this</span>.plugins.length; i++) &#123;
        <span>// runHook的同步版本</span>
        <span>const</span> result = <span>this</span>.runHookSync(hookName, args, i, replaceContext);
        <span>// 返回非null或undefined的时候，停止运行，返回结果</span>
        <span>if</span> (result != <span>null</span>) <span>return</span> result <span>as</span> <span>any</span>;
    &#125;
    <span>// 否则返回null</span>
    <span>return</span> <span>null</span> <span>as</span> <span>any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>钩子函数: hookSeq
使用场景：onwrite、generateBundle等</li>
</ul>
<pre><code lang="ts" class="copyable"><span>// 和hookFirst的区别就是不能中断</span>
<span>async</span> <span><span>function</span> <span>hookSeq</span><<span>H</span> <span>extends</span> <span>keyof</span> <span>PluginHooks</span>>(<span>
    hookName: H,
    args: Args<PluginHooks[H]>,
    replaceContext?: ReplaceContext
</span>): <span>Promise</span><<span>void</span>> </span>&#123;
    <span>let</span> promise: <span>Promise</span><<span>void</span>> = <span>Promise</span>.resolve();
    <span>for</span> (<span>let</span> i = <span>0</span>; i < <span>this</span>.plugins.length; i++)
        promise = promise.then(<span><span>()</span> =></span>
            <span>this</span>.runHook<<span>void</span>>(hookName, args <span>as</span> <span>any</span>[], i, <span>false</span>, replaceContext)
        );
    <span>return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>钩子函数: hookParallel
使用场景：buildStart、buildEnd、renderStart等</li>
</ul>
<pre><code lang="ts" class="copyable"><span>// 同步进行，利用的Promise.all</span>
<span><span>function</span> <span>hookParallel</span><<span>H</span> <span>extends</span> <span>keyof</span> <span>PluginHooks</span>>(<span>
    hookName: H,
    args: Args<PluginHooks[H]>,
    replaceContext?: ReplaceContext
</span>): <span>Promise</span><<span>void</span>> </span>&#123;
    <span>// 创建promise.all容器</span>
    <span>const</span> promises: <span>Promise</span><<span>void</span>>[] = [];
    <span>// 遍历每一个plugin</span>
    <span>for</span> (<span>let</span> i = <span>0</span>; i < <span>this</span>.plugins.length; i++) &#123;
        <span>// 执行hook返回promise</span>
        <span>const</span> hookPromise = <span>this</span>.runHook<<span>void</span>>(hookName, args <span>as</span> <span>any</span>[], i, <span>false</span>, replaceContext);
        <span>// 如果没有那么不push</span>
        <span>if</span> (!hookPromise) <span>continue</span>;
        promises.push(hookPromise);
    &#125;
    <span>// 返回promise</span>
    <span>return</span> <span>Promise</span>.all(promises).then(<span><span>()</span> =></span> &#123;&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>钩子函数: hookReduceArg0
使用场景: outputOptions、renderChunk等</li>
</ul>
<pre><code lang="ts" class="copyable"><span>// 对arg第一项进行reduce操作</span>
<span><span>function</span> <span>hookReduceArg0</span><<span>H</span> <span>extends</span> <span>keyof</span> <span>PluginHooks</span>, <span>V</span>, <span>R</span> = <span>ReturnType</span><<span>PluginHooks</span>[<span>H</span>]>>(<span>
    hookName: H,
    [arg0, ...args]: <span>any</span>[], <span>// 取出传入的数组的第一个参数，将剩余的置于一个数组中</span>
    reduce: Reduce<V, R>,
    replaceContext?: ReplaceContext <span>//  替换当前plugin调用时候的上下文环境</span>
</span>) </span>&#123;
    <span>let</span> promise = <span>Promise</span>.resolve(arg0); <span>// 默认返回source.code</span>
    <span>for</span> (<span>let</span> i = <span>0</span>; i < <span>this</span>.plugins.length; i++) &#123;
        <span>// 第一个promise的时候只会接收到上面传递的arg0</span>
        <span>// 之后每一次promise接受的都是上一个插件处理过后的source.code值</span>
        promise = promise.then(<span><span>arg0</span> =></span> &#123;
            <span>const</span> hookPromise = <span>this</span>.runHook(hookName, [arg0, ...args], i, <span>false</span>, replaceContext);
            <span>// 如果没有返回promise，那么直接返回arg0</span>
            <span>if</span> (!hookPromise) <span>return</span> arg0;
            <span>// result代表插件执行完成的返回值</span>
            <span>return</span> hookPromise.then(<span>(<span>result: <span>any</span></span>) =></span>
                reduce.call(<span>this</span>.pluginContexts[i], arg0, result, <span>this</span>.plugins[i])
            );
        &#125;);
    &#125;
    <span>return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>通过观察上面几种钩子函数的调用方式，我们可以发现，其内部有一个调用钩子函数的方法: runHook(Sync)，该函数执行插件中提供的钩子函数。</p>
<p>实现很简单:</p>
<pre><code lang="ts" class="copyable"><span><span>function</span> <span>runHook</span><<span>T</span>>(<span>
    hookName: <span>string</span>,
    args: <span>any</span>[],
    pluginIndex: <span>number</span>,
    permitValues: <span>boolean</span>,
    hookContext?: ReplaceContext | <span>null</span>
</span>): <span>Promise</span><<span>T</span>> </span>&#123;
    <span>this</span>.previousHooks.add(hookName);
    <span>// 找到当前plugin</span>
    <span>const</span> plugin = <span>this</span>.plugins[pluginIndex];
    <span>// 找到当前执行的在plugin中定义的hooks钩子函数</span>
    <span>const</span> hook = (plugin <span>as</span> <span>any</span>)[hookName];
    <span>if</span> (!hook) <span>return</span> <span>undefined</span> <span>as</span> <span>any</span>;

    <span>// pluginContexts在初始化plugin驱动器类的时候定义，是个数组，数组保存对应着每个插件的上下文环境</span>
    <span>let</span> context = <span>this</span>.pluginContexts[pluginIndex];
    <span>// 用于区分对待不同钩子函数的插件上下文</span>
    <span>if</span> (hookContext) &#123;
        context = hookContext(context, plugin);
    &#125;
    <span>return</span> <span>Promise</span>.resolve()
        .then(<span><span>()</span> =></span> &#123;
            <span>// permit values allows values to be returned instead of a functional hook</span>
            <span>if</span> (<span>typeof</span> hook !== <span>'function'</span>) &#123;
                <span>if</span> (permitValues) <span>return</span> hook;
                <span>return</span> error(&#123;
                    code: <span>'INVALID_PLUGIN_HOOK'</span>,
                    message: <span>`Error running plugin hook <span>$&#123;hookName&#125;</span> for <span>$&#123;plugin.name&#125;</span>, expected a function hook.`</span>
                &#125;);
            &#125;
            <span>// 传入插件上下文和参数，返回插件执行结果</span>
            <span>return</span> hook.apply(context, args);
        &#125;)
        .catch(<span><span>err</span> =></span> throwPluginError(err, plugin.name, &#123; hook: hookName &#125;));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>当然，并不是每个人刚开始都会使用插件，所以rollup本身也提供了几个必需的钩子函数供我们使用，在Graph实例化的时候与用户自定义插件进行concat操作:</p>
<pre><code lang="ts" class="copyable"><span>import</span> &#123; getRollupDefaultPlugin &#125; <span>from</span> <span>'./defaultPlugin'</span>;

<span>this</span>.plugins = userPlugins.concat(
    <span>// 采用内置默认插件或者graph的插件驱动器的插件，不管怎么样，内置默认插件是肯定有的</span>
    <span>// basePluginDriver是上一个PluginDriver初始化的插件</span>
    <span>// preserveSymlinks: 软连标志</span>
    basePluginDriver ? basePluginDriver.plugins : [getRollupDefaultPlugin(preserveSymlinks)]
);
<span class="copy-code-btn">复制代码</span></code></pre><p>那rollup提供了哪些必需的钩子函数呢:</p>
<pre><code lang="ts" class="copyable"><span>export</span> <span><span>function</span> <span>getRollupDefaultPlugin</span>(<span>preserveSymlinks: <span>boolean</span></span>): <span>Plugin</span> </span>&#123;
<span>return</span> &#123;
        <span>// 插件名</span>
name: <span>'Rollup Core'</span>,
<span>// 默认的模块(文件)加载机制，内部主要使用path.resolve</span>
resolveId: createResolveId(preserveSymlinks) <span>as</span> ResolveIdHook,
        <span>// this.pluginDriver.hookFirst('load', [id])为异步调用，readFile内部用promise包装了fs.readFile，并返回该promise</span>
load(id) &#123;
<span>return</span> readFile(id);
&#125;,
        <span>// 用来处理通过emitFile添加的urls或文件</span>
resolveFileUrl(&#123; relativePath, format &#125;) &#123;
<span>// 不同format会返回不同的文件解析地址</span>
<span>return</span> relativeUrlMechanisms[format](relativePath);
&#125;,
        <span>// 处理import.meta.url，参考地址:https://nodejs.org/api/esm.html#esm_import_meta)</span>
resolveImportMeta(prop, &#123; chunkId, format &#125;) &#123;
<span>// 改变 获取import.meta的信息 的行为</span>
<span>const</span> mechanism = importMetaMechanisms[format] && importMetaMechanisms[format](prop, chunkId);
<span>if</span> (mechanism) &#123;
<span>return</span> mechanism;
&#125;
&#125;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>过一眼发现都是最基本处理路径解析内容的钩子函数。</p>
<p>不仅如此，rollup给钩子函数注入了context，也就是上下文环境，用来方便对chunks和其他构建信息进行增删改查。</p>
<p><a target="_blank" href="https://rollupjs.org/guide/en/#plugin-context">文档</a>中也写得很清楚，比如：</p>
<ul>
<li>使用this.parse，调用rollup内部中的acron实例解析出ast</li>
<li>使用this.emitFile来增加产出的文件，看这个<a target="_blank" href="https://github.com/rollup/plugins/blob/371f4246068f3f469e046ecbe329b897eed9a692/packages/html/lib/index.js#L100">例子</a>.</li>
</ul>
<p>我们通过transform操作来简单看下，之前对ast进行transform的时候，调用了transform钩子：</p>
<pre><code lang="ts" class="copyable">
graph.pluginDriver
    .hookReduceArg0<<span>any</span>, <span>string</span>>(
        <span>'transform'</span>,
        [curSource, id], <span>// source.code 和 模块id</span>
        transformReducer,
    <span>// 第四个参数是一个函数，用来声明某些钩子上下文中需要的方法</span>
        (pluginContext, plugin) => &#123;
            <span>// 这一大堆是插件利用的，通过this.xxx调用</span>
            curPlugin = plugin;
            <span>if</span> (curPlugin.cacheKey) customTransformCache = <span>true</span>;
            <span>else</span> trackedPluginCache = getTrackedPluginCache(pluginContext.cache);
            <span>return</span> &#123;
                ...pluginContext,
                cache: trackedPluginCache ? trackedPluginCache.cache : pluginContext.cache,
                warn(warning: RollupWarning | <span>string</span>, pos?: <span>number</span> | &#123; column: <span>number</span>; line: <span>number</span> &#125;) &#123;
                    <span>if</span> (<span>typeof</span> warning === <span>'string'</span>) warning = &#123; message: warning &#125; <span>as</span> RollupWarning;
                    <span>if</span> (pos) augmentCodeLocation(warning, pos, curSource, id);
                    warning.id = id;
                    warning.hook = <span>'transform'</span>;
                    pluginContext.warn(warning);
                &#125;,
                error(err: RollupError | <span>string</span>, pos?: <span>number</span> | &#123; column: <span>number</span>; line: <span>number</span> &#125;): never &#123;
                    <span>if</span> (<span>typeof</span> err === <span>'string'</span>) err = &#123; message: err &#125;;
                    <span>if</span> (pos) augmentCodeLocation(err, pos, curSource, id);
                    err.id = id;
                    err.hook = <span>'transform'</span>;
                    <span>return</span> pluginContext.error(err);
                &#125;,
                emitAsset(name: <span>string</span>, source?: <span>string</span> | Buffer) &#123;
                    <span>const</span> emittedFile = &#123; <span>type</span>: <span>'asset'</span> <span>as</span> <span>const</span>, name, source &#125;;
                    emittedFiles.push(&#123; ...emittedFile &#125;);
                    <span>return</span> graph.pluginDriver.emitFile(emittedFile);
                &#125;,
                emitChunk(id, options) &#123;
                    <span>const</span> emittedFile = &#123; <span>type</span>: <span>'chunk'</span> <span>as</span> <span>const</span>, id, name: options && options.name &#125;;
                    emittedFiles.push(&#123; ...emittedFile &#125;);
                    <span>return</span> graph.pluginDriver.emitFile(emittedFile);
                &#125;,
                emitFile(emittedFile: EmittedFile) &#123;
                    emittedFiles.push(emittedFile);
                    <span>return</span> graph.pluginDriver.emitFile(emittedFile);
                &#125;,
                addWatchFile(id: <span>string</span>) &#123;
                    transformDependencies.push(id);
                    pluginContext.addWatchFile(id);
                &#125;,
                setAssetSource(assetReferenceId, source) &#123;
                    pluginContext.setAssetSource(assetReferenceId, source);
                    <span>if</span> (!customTransformCache && !setAssetSourceErr) &#123;
                        <span>try</span> &#123;
                            <span>return</span> <span>this</span>.error(&#123;
                                code: <span>'INVALID_SETASSETSOURCE'</span>,
                                message: <span>`setAssetSource cannot be called in transform for caching reasons. Use emitFile with a source, or call setAssetSource in another hook.`</span>
                            &#125;);
                        &#125; <span>catch</span> (err) &#123;
                            setAssetSourceErr = err;
                        &#125;
                    &#125;
                &#125;,
                getCombinedSourcemap() &#123;
                    <span>const</span> combinedMap = collapseSourcemap(
                        graph,
                        id,
                        originalCode,
                        originalSourcemap,
                        sourcemapChain
                    );
                    <span>if</span> (!combinedMap) &#123;
                        <span>const</span> magicString = <span>new</span> MagicString(originalCode);
                        <span>return</span> magicString.generateMap(&#123; includeContent: <span>true</span>, hires: <span>true</span>, source: id &#125;);
                    &#125;
                    <span>if</span> (originalSourcemap !== combinedMap) &#123;
                        originalSourcemap = combinedMap;
                        sourcemapChain.length = <span>0</span>;
                    &#125;
                    <span>return</span> <span>new</span> SourceMap(&#123;
                        ...combinedMap,
                        file: <span>null</span> <span>as</span> <span>any</span>,
                        sourcesContent: combinedMap.sourcesContent!
                    &#125;);
                &#125;
            &#125;;
        &#125;
    )
<span class="copy-code-btn">复制代码</span></code></pre><p>runHook中有一句判断，就是对上下文环境的使用：</p>
<pre><code lang="ts" class="copyable"><span><span>function</span> <span>runHook</span><<span>T</span>>(<span>
hookName: <span>string</span>,
args: <span>any</span>[],
pluginIndex: <span>number</span>,
permitValues: <span>boolean</span>,
hookContext?: ReplaceContext | <span>null</span>
</span>) </span>&#123;
    <span>// ...</span>
    <span>const</span> plugin = <span>this</span>.plugins[pluginIndex];
    <span>// 获取默认的上下文环境</span>
    <span>let</span> context = <span>this</span>.pluginContexts[pluginIndex];
    <span>// 如果提供了，就替换</span>
    <span>if</span> (hookContext) &#123;
        context = hookContext(context, plugin);
    &#125;
    <span>// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>至于rollup是什么时机调用插件提供的钩子函数的，这里就不啰嗦了，<a target="_blank" href="https://github.com/FoxDaxian/rollup-analysis">代码</a>中分布很清晰，一看便知.</p>
<p>还有 rollup 为了方便咱们变化插件，还提供了一个<a target="_blank" href="https://github.com/rollup/plugins/blob/master/packages/pluginutils/README.md">工具集</a>，可以非常方便的进行模块的操作以及判断，有兴趣的自行查看。</p>
<h4 data-id="heading-5">插件的缓存</h4>
<p>插件还提供缓存的能力，实现的非常巧妙：</p>
<pre><code lang="javascript" class="copyable"><span>export</span> <span><span>function</span> <span>createPluginCache</span>(<span>cache: SerializablePluginCache</span>): <span>PluginCache</span> </span>&#123;
<span>// 利用闭包将cache缓存</span>
<span>return</span> &#123;
has(id: string) &#123;
<span>const</span> item = cache[id];
<span>if</span> (!item) <span>return</span> <span>false</span>;
item[<span>0</span>] = <span>0</span>; <span>// 如果访问了，那么重置访问过期次数，猜测：就是说明用户有意向主动去使用</span>
<span>return</span> <span>true</span>;
&#125;,
get(id: string) &#123;
<span>const</span> item = cache[id];
<span>if</span> (!item) <span>return</span> <span>undefined</span>;
item[<span>0</span>] = <span>0</span>; <span>// 如果访问了，那么重置访问过期次数</span>
<span>return</span> item[<span>1</span>];
&#125;,
set(id: string, <span>value</span>: any) &#123;
            <span>// 存储单位是数组，第一项用来标记访问次数</span>
cache[id] = [<span>0</span>, value];
&#125;,
<span>delete</span>(id: string) &#123;
<span>return</span> <span>delete</span> cache[id];
&#125;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>然后创建缓存后，会添加在插件上下文中:</p>
<pre><code lang="javascript" class="copyable"><span>import</span> createPluginCache <span>from</span> <span>'createPluginCache'</span>;

<span>const</span> cacheInstance = createPluginCache(pluginCache[cacheKey] || (pluginCache[cacheKey] = <span>Object</span>.create(<span>null</span>)));

<span>const</span> context = &#123;
<span>// ...</span>
    cache: cacheInstance,
    <span>// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>之后我们就可以在插件中就可以使用cache进行插件环境下的缓存，进一步提升打包效率:</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>testPlugin</span>(<span></span>) </span>&#123;
  <span>return</span> &#123;
    <span>name</span>: <span>"test-plugin"</span>,
    buildStart() &#123;
      <span>if</span> (!<span>this</span>.cache.has(<span>"prev"</span>)) &#123;
        <span>this</span>.cache.set(<span>"prev"</span>, <span>"上一次插件执行的结果"</span>);
      &#125; <span>else</span> &#123;
        <span>// 第二次执行rollup的时候会执行</span>
        <span>console</span>.log(<span>this</span>.cache.get(<span>"prev"</span>));
      &#125;
    &#125;,
  &#125;;
&#125;
<span>let</span> cache;
<span>async</span> <span><span>function</span> <span>build</span>(<span></span>) </span>&#123;
  <span>const</span> chunks = <span>await</span> rollup.rollup(&#123;
    <span>input</span>: <span>"src/main.js"</span>,
    <span>plugins</span>: [testPlugin()],
    <span>// 需要传递上次的打包结果</span>
    cache,
  &#125;);
  cache = chunks.cache;
&#125;

build().then(<span><span>()</span> =></span> &#123;
  build();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre><p>不过需要注意的一点是<code>options</code>钩子函数是没有注入上下文环境的，它的调用方式也和其他钩子不一样:</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>applyOptionHook</span>(<span>inputOptions: InputOptions, plugin: Plugin</span>) </span>&#123;
<span>if</span> (plugin.options)&#123;
        <span>// 指定this和经过处理的input配置，并未传入context</span>
    <span>return</span> plugin.options.call(&#123; <span>meta</span>: &#123; rollupVersion &#125; &#125;, inputOptions) || inputOptions;
    &#125;

<span>return</span> inputOptions;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-6">总结</h4>
<p>rollup系列到此也就告一段落了，从开始阅读时的一脸懵逼，到读到依赖收集、各工具类的十脸懵逼，到现在的轻车熟路，真是一段难忘的经历~</p>
<p>学习大佬们的操作并取其精华，去其糟粕就像打怪升级一样，你品，你细品。哈哈</p>
<p>在这期间也是误导一些东西，看得多了，就会发现，其实套路都一样，摸索出它们的<code>核心框架</code>，再对功能缝缝补补，不断更新迭代，或许我们也可以成为开源大作的作者。</p>
<p>如果用几句话来描述rollup的话：</p>
<p>读取并合并配置 -> 创建依赖图 -> 读取入口模块内容 -> 借用开源estree规范解析器进行源码分析，获取依赖，递归此操作 -> 生成模块，挂载模块对应文件相关信息 -> 分析ast，构建各node实例 -> 生成chunks -> 调用各node重写的render -> 利用magic-string进行字符串拼接和wrap操作 -> 写入</p>
<p>精简一下就是:</p>
<p>字符串 -> AST -> 字符串</p>
<p></p><figure><img src="https://user-gold-cdn.xitu.io/2020/4/13/17173eb9fa4b986b?imageView2/0/w/1280/h/960/ignore-error/1" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>如果改系列能对你一丝丝帮忙，还请动动手指，鼓励一下~</p>
<p>拜了个拜~</p>
</div>  
</div>
            