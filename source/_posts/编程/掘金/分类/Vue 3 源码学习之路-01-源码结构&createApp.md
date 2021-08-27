
---
title: 'Vue 3 源码学习之路-01-源码结构&createApp'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30879aaab36947db86db93ba357601c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 01:56:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30879aaab36947db86db93ba357601c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Version: 3.0.11</p>
</blockquote>
<h2 data-id="heading-0">1.准备工作-源码结构</h2>
<h3 data-id="heading-1">1.1目录结构</h3>
<p>在正式学习源码之前，首先在Vue官方 github 官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next.git" ref="nofollow noopener noreferrer">下载源码</a> ，下载之后解压目录大概是这样的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30879aaab36947db86db93ba357601c3~tplv-k3u1fbpfcp-watermark.image" alt="vue-next.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>compiler-core</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dd54850b9004355903545cc9f2b6552~tplv-k3u1fbpfcp-watermark.image" alt="compiler-core.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>compiler-dom</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a425190931234c26aa6ae0f5f075e50b~tplv-k3u1fbpfcp-watermark.image" alt="compiler-dom.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>compiler-sfc</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d251e67ea4574ff58525477558e3a3d4~tplv-k3u1fbpfcp-watermark.image" alt="compiler-sfc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>compiler-ssr</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19eaca2e4d314512a93fbc8eaa34ce33~tplv-k3u1fbpfcp-watermark.image" alt="compiler-ssr.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>reactivity</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/084744b77e5341a4b4ad160c8fb0bbc6~tplv-k3u1fbpfcp-watermark.image" alt="reactivity.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>runtime-core 运行时核心</li>
</ul>
<p>先上一张图来看看runtime-core里面有啥东西。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d14cf23c30d409c820e37ff25fdc594~tplv-k3u1fbpfcp-watermark.image" alt="runtime-core.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图我们不难看出Vue的主要的核心api都在运行时核心里面，而且Vue3全部使用TypeScript作为开发语言。</p>
<p>在runtime-core中先说说主要的几个模块vnode、h、components、apiCreateApp、apiLifecycle，因为这个模块是实现Vue3 compositionApi功能的核心</p>
<ul>
<li>runtime-dom</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8ac2186ea943caac4815dbc85f86ba~tplv-k3u1fbpfcp-watermark.image" alt="runtime-dom.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>server-render</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4c8bcb4f7cc4a238b2c8f15e6ee6d39~tplv-k3u1fbpfcp-watermark.image" alt="server-render.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>sfc-playground</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eba0aca7b37c436aa68aef4d3c1b7a1b~tplv-k3u1fbpfcp-watermark.image" alt="sfc-playground.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>shared</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f17b1de62214d08b0af04bd6d094e81~tplv-k3u1fbpfcp-watermark.image" alt="shared.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>size-check</li>
<li>template-explorer</li>
<li>vue</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1e46f1920cd43eb96f343e593764513~tplv-k3u1fbpfcp-watermark.image" alt="vue.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1.2 源码编译后的样子</h3>
<p>大概就长成这个样子！不难发现每个功能模块有3个js文件和一个ts，首先说js文件，在平时使用dev模式开发的时候调用的是带有esm-bundler版本，项目打包
build的时候调用的是prod版本，剩余的一个版本暂时不清楚什么时候调用，ts文件里面定义了接口类型，并非真正意义上的运行代码，辅助开发的时候数据类型推断。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7931f488a634855a76e686be7dec041~tplv-k3u1fbpfcp-watermark.image" alt="vue-next-core01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228a2dc6a2ad4c118e81ef63f0feff9f~tplv-k3u1fbpfcp-watermark.image" alt="vue-next-core02.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2 createApp做了什么</h2>
<h3 data-id="heading-4">2.1 从main.js入手createApp</h3>
<p>首先我们看一下Vue3初始化代码，vue3初始化是通过执行createApp方法创建vue实例，而在vue2中使用new Vue()创建。那么下面我们来看一下createApp做了什么。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

createApp(App).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过浏览器devtool断点执行我们看到createApp方法里面，先执行下面这段代码。</p>
<p>这里主要干了三件事，第一创建renderer，第二创建app实例，第三重写mount函数。
首先通过ensureRenderer方法创建renderer渲染器，然后再通过createApp创建app实例，最后重写app.mount方法，返回proxy代理组件实例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> createApp = (<span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> app = ensureRenderer().createApp(...args);
    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
        injectNativeTagCheck(app);
        injectCustomElementCheck(app);
    &#125;
    <span class="hljs-keyword">const</span> &#123; mount &#125; = app;
    app.mount = <span class="hljs-function">(<span class="hljs-params">containerOrSelector</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> container = normalizeContainer(containerOrSelector);
        <span class="hljs-keyword">if</span> (!container)
            <span class="hljs-keyword">return</span>;
        <span class="hljs-keyword">const</span> component = app._component;
        <span class="hljs-keyword">if</span> (!isFunction(component) && !component.render && !component.template) &#123;
            component.template = container.innerHTML;
        &#125;
        <span class="hljs-comment">// clear content before mounting</span>
        container.innerHTML = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">const</span> proxy = mount(container, <span class="hljs-literal">false</span>, container <span class="hljs-keyword">instanceof</span> SVGElement);
        <span class="hljs-keyword">if</span> (container <span class="hljs-keyword">instanceof</span> Element) &#123;
            container.removeAttribute(<span class="hljs-string">'v-cloak'</span>);
            container.setAttribute(<span class="hljs-string">'data-v-app'</span>, <span class="hljs-string">''</span>);
        &#125;
        <span class="hljs-keyword">return</span> proxy;
    &#125;;
    <span class="hljs-keyword">return</span> app;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2 创建renderer</h3>
<p>那么看到第一个执行的方法是ensureRender()，通过源码注释了解到惰性创建渲染器renderer，这样做的原因是用户通过Vue只引入了reactivity时可以保证tree-shaking可用
如果renderer已经创建那么直接返回已经创建好的renderer，否则通过createRenderer创建新的渲染器renderer。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> rendererOptions = extend(&#123; patchProp, forcePatchProp &#125;, nodeOps);
<span class="hljs-comment">// lazy create the renderer - this makes core renderer logic tree-shakable</span>
<span class="hljs-comment">// in case the user only imports reactivity utilities from Vue.</span>
<span class="hljs-keyword">let</span> renderer;
<span class="hljs-keyword">let</span> enabledHydration = <span class="hljs-literal">false</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ensureRenderer</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> renderer || (renderer = createRenderer(rendererOptions));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createRenderer方法接收一个rendererOption参数，其中nodeOps里面封装的方法就是dom节点操作，当template模板数据变化的时候调用。</p>
<p>patchProp更新dom属性，包括style内敛样式，class类样式，以及patchEvent事件绑定</p>
<p>再看createRenderer方法，内执行baseCreateRenderer方法并将option参数传入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRenderer</span>(<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'%c调用 baseCreateRenderer >>>'</span>,<span class="hljs-string">'color:red'</span>)
    <span class="hljs-keyword">return</span> baseCreateRenderer(options);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着再看baseCreateRenderer方法，内部函数众多代码长先跳过，调用baseCreateRenderer方法是返回一个对象，包含三个元素：render，hydrate和createApp。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> count = <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">options, createHydrationFns</span>) </span>&#123;
    

    <span class="hljs-comment">// 代码过长省略N行 ...</span>
   
    <span class="hljs-keyword">return</span> &#123;
        render,
        hydrate,
        <span class="hljs-attr">createApp</span>: createAppAPI(render, hydrate)
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.3 创建app实例</h3>
<p>在返回参数里面看到调用了createAppAPI方法，也就是说在我们main.js里面执行createApp实际上调用的就是createAppAPI，返回一个app对象，我们再通过createAppAPI看app对象具体有哪些参数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppContext</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">app</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">config</span>: &#123;
            <span class="hljs-attr">isNativeTag</span>: NO,
            <span class="hljs-attr">performance</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">globalProperties</span>: &#123;&#125;,
            <span class="hljs-attr">optionMergeStrategies</span>: &#123;&#125;,
            <span class="hljs-attr">isCustomElement</span>: NO,
            <span class="hljs-attr">errorHandler</span>: <span class="hljs-literal">undefined</span>,
            <span class="hljs-attr">warnHandler</span>: <span class="hljs-literal">undefined</span>
        &#125;,
        <span class="hljs-attr">mixins</span>: [],
        <span class="hljs-attr">components</span>: &#123;&#125;,
        <span class="hljs-attr">directives</span>: &#123;&#125;,
        <span class="hljs-attr">provides</span>: <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    &#125;;
&#125;

<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppAPI</span>(<span class="hljs-params">render, hydrate</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">rootComponent, rootProps = <span class="hljs-literal">null</span></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (rootProps != <span class="hljs-literal">null</span> && !isObject(rootProps)) &#123;
            (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && warn(<span class="hljs-string">`root props passed to app.mount() must be an object.`</span>);
            rootProps = <span class="hljs-literal">null</span>;
        &#125;
        <span class="hljs-keyword">const</span> context = createAppContext();
        <span class="hljs-keyword">const</span> installedPlugins = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
        <span class="hljs-keyword">let</span> isMounted = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">const</span> app = (context.app = &#123;
            <span class="hljs-attr">_uid</span>: uid++,
            _component: rootComponent,
            <span class="hljs-attr">_props</span>: rootProps,
            <span class="hljs-attr">_container</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">_context</span>: context,
            version,
            <span class="hljs-keyword">get</span> <span class="hljs-title">config</span>() &#123;
                <span class="hljs-keyword">return</span> context.config;
            &#125;,
            <span class="hljs-keyword">set</span> <span class="hljs-title">config</span>(<span class="hljs-params">v</span>) &#123;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    warn(<span class="hljs-string">`app.config cannot be replaced. Modify individual options instead.`</span>);
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">plugin, ...options</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (installedPlugins.has(plugin)) &#123;
                    (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && warn(<span class="hljs-string">`Plugin has already been applied to target app.`</span>);
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (plugin && isFunction(plugin.install)) &#123;
                    installedPlugins.add(plugin);
                    plugin.install(app, ...options);
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(plugin)) &#123;
                    installedPlugins.add(plugin);
                    plugin(app, ...options);
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    warn(<span class="hljs-string">`A plugin must either be a function or an object with an "install" `</span> +
                        <span class="hljs-string">`function.`</span>);
                &#125;
                <span class="hljs-keyword">return</span> app;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">mixin</span>(<span class="hljs-params">mixin</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (__VUE_OPTIONS_API__) &#123;
                    <span class="hljs-keyword">if</span> (!context.mixins.includes(mixin)) &#123;
                        context.mixins.push(mixin);
                        <span class="hljs-comment">// global mixin with props/emits de-optimizes props/emits</span>
                        <span class="hljs-comment">// normalization caching.</span>
                        <span class="hljs-keyword">if</span> (mixin.props || mixin.emits) &#123;
                            context.deopt = <span class="hljs-literal">true</span>;
                        &#125;
                    &#125;
                    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                        warn(<span class="hljs-string">'Mixin has already been applied to target app'</span> +
                            (mixin.name ? <span class="hljs-string">`: <span class="hljs-subst">$&#123;mixin.name&#125;</span>`</span> : <span class="hljs-string">''</span>));
                    &#125;
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    warn(<span class="hljs-string">'Mixins are only available in builds supporting Options API'</span>);
                &#125;
                <span class="hljs-keyword">return</span> app;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">component</span>(<span class="hljs-params">name, component</span>)</span> &#123;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    validateComponentName(name, context.config);
                &#125;
                <span class="hljs-keyword">if</span> (!component) &#123;
                    <span class="hljs-keyword">return</span> context.components[name];
                &#125;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && context.components[name]) &#123;
                    warn(<span class="hljs-string">`Component "<span class="hljs-subst">$&#123;name&#125;</span>" has already been registered in target app.`</span>);
                &#125;
                context.components[name] = component;
                <span class="hljs-keyword">return</span> app;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">directive</span>(<span class="hljs-params">name, directive</span>)</span> &#123;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    validateDirectiveName(name);
                &#125;
                <span class="hljs-keyword">if</span> (!directive) &#123;
                    <span class="hljs-keyword">return</span> context.directives[name];
                &#125;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && context.directives[name]) &#123;
                    warn(<span class="hljs-string">`Directive "<span class="hljs-subst">$&#123;name&#125;</span>" has already been registered in target app.`</span>);
                &#125;
                context.directives[name] = directive;
                <span class="hljs-keyword">return</span> app;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">rootContainer, isHydrate, isSVG</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (!isMounted) &#123;
                    <span class="hljs-keyword">const</span> vnode = createVNode(rootComponent, rootProps);
                    <span class="hljs-comment">// store app context on the root VNode.</span>
                    <span class="hljs-comment">// this will be set on the root instance on initial mount.</span>
                    vnode.appContext = context;
                    <span class="hljs-comment">// HMR root reload</span>
                    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                        context.reload = <span class="hljs-function">() =></span> &#123;
                            render(cloneVNode(vnode), rootContainer, isSVG);
                        &#125;;
                    &#125;
                    <span class="hljs-keyword">if</span> (isHydrate && hydrate) &#123;
                        hydrate(vnode, rootContainer);
                    &#125;
                    <span class="hljs-keyword">else</span> &#123;
                        render(vnode, rootContainer, isSVG);
                    &#125;
                    isMounted = <span class="hljs-literal">true</span>;
                    app._container = rootContainer;
                    rootContainer.__vue_app__ = app;
                    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) || __VUE_PROD_DEVTOOLS__) &#123;
                        devtoolsInitApp(app, version);
                    &#125;
                    <span class="hljs-keyword">return</span> vnode.component.proxy;
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    warn(<span class="hljs-string">`App has already been mounted.\n`</span> +
                        <span class="hljs-string">`If you want to remount the same app, move your app creation logic `</span> +
                        <span class="hljs-string">`into a factory function and create fresh app instances for each `</span> +
                        <span class="hljs-string">`mount - e.g. \`const createMyApp = () => createApp(App)\``</span>);
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">if</span> (isMounted) &#123;
                    render(<span class="hljs-literal">null</span>, app._container);
                    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) || __VUE_PROD_DEVTOOLS__) &#123;
                        devtoolsUnmountApp(app);
                    &#125;
                    <span class="hljs-keyword">delete</span> app._container.__vue_app__;
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)) &#123;
                    warn(<span class="hljs-string">`Cannot unmount an app that is not mounted.`</span>);
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params">key, value</span>)</span> &#123;
                <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && key <span class="hljs-keyword">in</span> context.provides) &#123;
                    warn(<span class="hljs-string">`App already provides property with key "<span class="hljs-subst">$&#123;<span class="hljs-built_in">String</span>(key)&#125;</span>". `</span> +
                        <span class="hljs-string">`It will be overwritten with the new value.`</span>);
                &#125;
                <span class="hljs-comment">// TypeScript doesn't allow symbols as index type</span>
                <span class="hljs-comment">// https://github.com/Microsoft/TypeScript/issues/24587</span>
                context.provides[key] = value;
                <span class="hljs-keyword">return</span> app;
            &#125;
        &#125;);
        <span class="hljs-keyword">return</span> app;
    &#125;;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>createAppAPI的核心就是调用createAppContext 返回一个包含app、config、mixins、components、directives和provides基础参数对象，
然后再创建context.app对象，也就是vue的实例对象，包含内部参数和版本号，暴露出use、component、mount、mixin、directive、unmount、provide程序api给我们使用。</p>
<blockquote>
<p>本文作者：自如大前端研发中心-贾文莉</p>
</blockquote></div>  
</div>
            