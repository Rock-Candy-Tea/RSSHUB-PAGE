
---
title: '实现Vue3中的响应式Api'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6003'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 00:57:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=6003'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue3响应式Api实现</h1>
<h2 data-id="heading-1">1. 前言</h2>
<blockquote>
<p>Vue3中的响应式Api中大量使用了ES6语法，在读本文之前请先了解以下知识点</p>
</blockquote>








































<table><thead><tr><th>预备知识点</th><th>简单介绍</th><th>MDN链接</th></tr></thead><tbody><tr><td>1. Proxy</td><td>Proxy 对象用于创建一个对象的代理，从而实现基本操作的拦截和自定义（如属性查找、赋值、枚举、函数调用等</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr><tr><td>2. Reflect</td><td>Reflect 是一个内置的对象，它提供拦截 JavaScript 操作的方法</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr><tr><td>3. WeakMap</td><td>WeakMap 对象是一组键/值对的集合，其中的键是弱引用的。其键必须是对象，而值可以是任意的,可以及时的被垃圾回收</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WeakMap" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr><tr><td>4. Set</td><td>值的集合，可以按照插入的顺序迭代它的元素。 Set中的元素只会出现一次，即 Set 中的元素是唯一的</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr><tr><td>5. Map</td><td>存键值对，并且能够记住键的原始插入顺序。任何值(对象或者原始值) 都可以作为一个键或一个值</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Map" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr><tr><td>6.Object.defineProperty</td><td>直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象。</td><td><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></td></tr></tbody></table>
<h2 data-id="heading-2">2. 介绍Vue3</h2>
<h3 data-id="heading-3">2.1 vue3介绍</h3>
<ul>
<li>Vue3.0 在去年 9 月正式发布了，随着时间的变化，现在Vue3.0生态已经趋向于稳定了</li>
<li>Vue3采用Typescript开发,增强类型检测。 Vue2 则采用flow</li>
<li>Vue3的性能优化，支持tree-shaking, 不使用就不会被打包</li>
<li>Vue3劫持数据采用Proxy,Vue2劫持数据采用Object.defineProperty。 defineProperty有性能问题和缺陷</li>
<li>Vue3 采用compositionApi进行组织功能，解决反复横跳，优化复用逻辑 （mixin带来的数据来源不清晰、命名冲突等）, 相比optionsApi 类型推断更加方便</li>
<li>源码采用 <code>monorepo</code> 方式进行管理，将模块拆分到package目录中</li>
<li>增加了 <code>Fragment</code>,<code>Teleport</code>，<code>Suspense</code>组件</li>
</ul>
<h3 data-id="heading-4">2.2 vue3架构分析</h3>
<h4 data-id="heading-5">2.2.1 Monorepo介绍</h4>
<ul>
<li><code>Monorepo</code> 是管理项目代码的一个方式，指在一个项目仓库(<code>repo</code>)中管理多个模块/包(package)</li>
<li>一个仓库可维护多个模块，不用到处找仓库</li>
<li>方便版本管理和依赖管理，模块之间的引用，调用都非常方便</li>
</ul>
<blockquote>
<p>缺点: 仓库体积会变大</p>
</blockquote>
<h4 data-id="heading-6">2.2.2 Vue3源码结构</h4>





























































<table><thead><tr><th>目录</th><th>说明</th></tr></thead><tbody><tr><td>reactivity</td><td>响应式系统</td></tr><tr><td>runtime-core</td><td>与平台无关的运行时核心 (可以创建针对特定平台的运行时 - 自定义渲染器)</td></tr><tr><td>runtime-dom</td><td>针对浏览器的运行时。包括<code>DOM API</code>，属性，事件处理等</td></tr><tr><td>runtime-test</td><td>用于测试</td></tr><tr><td>server-renderer</td><td>用于服务器端渲染</td></tr><tr><td>compiler-core</td><td>与平台无关的编译器核心</td></tr><tr><td>compiler-dom</td><td>针对浏览器的编译模块</td></tr><tr><td>compiler-ssr</td><td>针对服务端渲染的编译模块</td></tr><tr><td>compiler-sfc</td><td>针对单文件解析</td></tr><tr><td>size-check</td><td>用来测试代码体积</td></tr><tr><td>template-explorer</td><td>用于调试编译器输出的开发工具</td></tr><tr><td>shared</td><td>多个包之间共享的内容</td></tr><tr><td>vue</td><td>完整版本,包括运行时和编译器</td></tr></tbody></table>
<h2 data-id="heading-7">3. 响应式Api介绍</h2>
<blockquote>
<p>本文不会过多介绍具体用法，具体介绍和使用及完整Api请参考官方文档，下方为我们要去实现的响应式Api及简单介绍</p>
</blockquote>























































<table><thead><tr><th>Api</th><th>简单介绍</th><th>文档链接</th></tr></thead><tbody><tr><td>reactive</td><td>返回响应式的代理对象，深度递归懒代理，当取值时才会进行深度代理</td><td><a href="https://vue3js.cn/docs/zh/api/basic-reactivity.html#reactive" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>shallowReactive</td><td>返回响应式的代理对象，浅层代理，只代理第一层对象</td><td><a href="https://vue3js.cn/docs/zh/api/basic-reactivity.html#shallowreactive" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>readonly</td><td>返回响应式的代理对象，深度递归懒代理,代理的值不可被更改</td><td><a href="https://vue3js.cn/docs/zh/api/basic-reactivity.html#readonly" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>shallowReadonly</td><td>返回响应式的代理对象，浅层代理，代理的值不可被更改</td><td><a href="https://vue3js.cn/docs/zh/api/basic-reactivity.html#shallowreadonly" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>ref</td><td>接受一个内部值并返回一个响应式且可变的 ref 对象</td><td><a href="https://vue3js.cn/docs/zh/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>shallowRef</td><td>浅层代理内部值并返回一个响应式且可变的 ref 对象</td><td><a href="https://vue3js.cn/docs/zh/api/refs-api.html#shallowref" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>toRef</td><td>可以将 ref 传递出去，从而保持对其源 property 的响应式连接</td><td><a href="https://vue3js.cn/docs/zh/api/refs-api.html#toref" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>toRefs</td><td>可以将多个 ref 传递出去,从而保持对其源 property 的响应式连接</td><td><a href="https://vue3js.cn/docs/zh/api/refs-api.html#torefs" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr><tr><td>computed</td><td>计算属性，用法类似Vue2，原理不同</td><td><a href="https://vue3js.cn/docs/zh/api/computed-watch-api.html#computed" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/api…</a></td></tr></tbody></table>
<h2 data-id="heading-8">4. 响应式Api实现</h2>
<h3 data-id="heading-9">4.1 搭建开发环境</h3>
<h4 data-id="heading-10">4.1.0 说明</h4>
<blockquote>
<p>为了能保证1比1的还原及可阅读性，下方在实现过程中使用了极少的typescript语法</p>
</blockquote>
<h4 data-id="heading-11">4.1.1 安装依赖</h4>

































<table><thead><tr><th>依赖</th><th></th></tr></thead><tbody><tr><td>typescript</td><td>支持typescript</td></tr><tr><td>rollup</td><td>打包工具</td></tr><tr><td>rollup-plugin-typescript2</td><td>rollup 和 ts的 桥梁</td></tr><tr><td>@rollup/plugin-node-resolve</td><td>解析node第三方模块</td></tr><tr><td>@rollup/plugin-json</td><td>支持引入json</td></tr><tr><td>execa</td><td>开启子进程方便执行命令</td></tr></tbody></table>
<pre><code class="hljs language-bash copyable" lang="bash">npm install typescript rollup rollup-plugin-typescript2 @rollup/plugin-node-resolve @rollup/plugin-json execa -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">4.1.2 workspace配置</h4>
<pre><code class="hljs language-bash copyable" lang="bash">npm init -y && npx tsc --init
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"private"</span>:<span class="hljs-literal">true</span>,
  <span class="hljs-attr">"workspaces"</span>:[
    <span class="hljs-string">"packages/*"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>目录结构配置</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">C:.
│  package.json        <span class="hljs-comment"># 配置运行命令 </span>
│  rollup.config.js    <span class="hljs-comment"># rollup配置文件</span>
│  tsconfig.json       <span class="hljs-comment"># ts配置文件 更改为esnext</span>
│  yarn.lock
│  
├─packages             <span class="hljs-comment"># N个repo</span>
│  └─reactivity
│      │  package.json
│      └─src
│          index.ts
│              
└─scripts              <span class="hljs-comment"># 打包命令</span>
        build.js
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>配置模块名称及打包选项</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"@vue/reactivity"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"module"</span>: <span class="hljs-string">"dist/reactivity.esm-bundler.js"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"buildOptions"</span>:&#123;
    <span class="hljs-attr">"name"</span>:<span class="hljs-string">"VueReactivity"</span>,
    <span class="hljs-attr">"formats"</span>:[
      <span class="hljs-string">"esm-bundler"</span>,
      <span class="hljs-string">"cjs"</span>,
      <span class="hljs-string">"global"</span>
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>创建软链<code>yarn install</code></p>
</blockquote>
<h4 data-id="heading-13">4.1.3 对 packages 下模块进行打包</h4>
<blockquote>
<pre><code class="copyable">scripts/build.js
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>)
<span class="hljs-comment">// 过滤packages目录下所有模块</span>
<span class="hljs-keyword">const</span> targets = fs.readdirSync(<span class="hljs-string">'packages'</span>).filter(<span class="hljs-function"><span class="hljs-params">f</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (!fs.statSync(<span class="hljs-string">`packages/<span class="hljs-subst">$&#123;f&#125;</span>`</span>).isDirectory()) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;)
<span class="hljs-comment">// 开始并行打包</span>
runParallel(targets, build)
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runParallel</span>(<span class="hljs-params">source, iteratorFn</span>) </span>&#123;
    <span class="hljs-keyword">const</span> ret = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> source) &#123;
        <span class="hljs-keyword">const</span> p = iteratorFn(item)
        ret.push(p);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(ret);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">build</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-keyword">await</span> execa(
        <span class="hljs-string">'rollup'</span>,
        [
            <span class="hljs-string">'-c'</span>,
            <span class="hljs-string">'--environment'</span>,
            <span class="hljs-string">`TARGET:<span class="hljs-subst">$&#123;target&#125;</span>`</span>
        ], 
        &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span> &#125;
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">4.1.4 rollup配置</h4>
<blockquote>
<pre><code class="copyable">rollup.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> ts <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-typescript2'</span>
<span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span>
<span class="hljs-keyword">import</span> resolvePlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span>
<span class="hljs-keyword">const</span> packagesDir = path.resolve(__dirname, <span class="hljs-string">'packages'</span>); <span class="hljs-comment">// 获取packages目录</span>


<span class="hljs-keyword">const</span> packageDir = path.resolve(packagesDir, process.env.TARGET); <span class="hljs-comment">// 获取要打包的目标目录</span>
<span class="hljs-keyword">const</span> name = path.basename(packageDir); <span class="hljs-comment">// 获取打包的名字</span>

<span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">p</span> =></span> path.resolve(packageDir, p);
<span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(resolve(<span class="hljs-string">`package.json`</span>)) <span class="hljs-comment">// 获取目标对应的package.json</span>

<span class="hljs-keyword">const</span> packageOptions = pkg.buildOptions; <span class="hljs-comment">// 打包的选项</span>
<span class="hljs-keyword">const</span> outputConfigs = &#123;
    <span class="hljs-string">'esm-bundler'</span>: &#123;
        <span class="hljs-attr">file</span>: resolve(<span class="hljs-string">`dist/<span class="hljs-subst">$&#123;name&#125;</span>.esm-bundler.js`</span>), <span class="hljs-comment">// webpack打包用的</span>
        <span class="hljs-attr">format</span>: <span class="hljs-string">`es`</span>
    &#125;,
    <span class="hljs-string">'cjs'</span>: &#123;
        <span class="hljs-attr">file</span>: resolve(<span class="hljs-string">`dist/<span class="hljs-subst">$&#123;name&#125;</span>.cjs.js`</span>), <span class="hljs-comment">// node使用的</span>
        <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
    &#125;,
    <span class="hljs-string">'global'</span>: &#123;
        <span class="hljs-attr">file</span>: resolve(<span class="hljs-string">`dist/<span class="hljs-subst">$&#123;name&#125;</span>.global.js`</span>), <span class="hljs-comment">// 全局的</span>
        <span class="hljs-attr">format</span>: <span class="hljs-string">'iife'</span>
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createConfig</span>(<span class="hljs-params">format, output</span>) </span>&#123;
    output.name = packageOptions.name;
    output.sourcemap = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">input</span>: resolve(<span class="hljs-string">`src/index.ts`</span>), <span class="hljs-comment">// 入口</span>
        output,
        <span class="hljs-attr">plugins</span>:[
            json(),
            ts(&#123;
                <span class="hljs-attr">tsconfig</span>:path.resolve(__dirname,<span class="hljs-string">'tsconfig.json'</span>)
            &#125;),
            resolvePlugin(),
        ]
    &#125;
&#125;
<span class="hljs-comment">// 根据模块配置信息选择性打包</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> packageOptions.formats.map(<span class="hljs-function"><span class="hljs-params">format</span> =></span> createConfig(format, outputConfigs[format]));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.1.5 开发环境打包</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>)
<span class="hljs-keyword">const</span> target = <span class="hljs-string">'reactivity'</span>
execa(<span class="hljs-string">'rollup'</span>, [
        <span class="hljs-string">'-wc'</span>,
        <span class="hljs-string">'--environment'</span>,
        <span class="hljs-string">`TARGET:<span class="hljs-subst">$&#123;target&#125;</span>`</span>
    ], &#123;
        <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>
    &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">4.2 packages/reactivity/src 下文件说明</h3>

































<table><thead><tr><th>文件名</th><th>含义</th></tr></thead><tbody><tr><td>index.ts</td><td>入口文件,导入导出文件</td></tr><tr><td>reactive.ts</td><td>包含了reactive、shallowReactive、readonly、shallowReadonly等方法文件</td></tr><tr><td>basehandles.ts</td><td>公共的Proxy中的get和set方法文件</td></tr><tr><td>effect.ts</td><td>收集依赖和通知依赖更新文件</td></tr><tr><td>ref.ts</td><td>包含了ref、shallowRef、toRef、toRefs等方法文件</td></tr><tr><td>computed.ts</td><td>包含了computed等方法文件</td></tr></tbody></table>
<h3 data-id="heading-17">4.3 packages/shared/src 下文件说明</h3>

















<table><thead><tr><th>文件名</th><th>含义</th></tr></thead><tbody><tr><td>index.ts</td><td>公共的工具函数，判断对象，数组等等方法</td></tr><tr><td>opeartors.ts</td><td>公共的枚举常量，依赖收集和更新等等</td></tr></tbody></table>
<h3 data-id="heading-18">4.4 reactive 、shallowReactive、readonly、shallowReadonly 实现</h3>
<h4 data-id="heading-19">4.4.1 reactive.ts文件中</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; mutableHandles, shallowReadonlyHandles, shallowReactiveHandles, readonlyHandles &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./basehandles'</span>
<span class="hljs-keyword">import</span> &#123; isObject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/shared'</span>

<span class="hljs-comment">// 返回一个代理对象，深度代理，可修改</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createReactiveObject(target, <span class="hljs-literal">false</span>, mutableHandles)
&#125;
<span class="hljs-comment">// 返回一个代理对象，浅层代理，可修改</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowReactive</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createReactiveObject(target, <span class="hljs-literal">false</span>, shallowReactiveHandles)
&#125;
<span class="hljs-comment">// 返回一个代理对象，深度代理，不可被修改</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readonly</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createReactiveObject(target, <span class="hljs-literal">true</span>, shallowReadonlyHandles)
&#125;
<span class="hljs-comment">// 返回一个代理对象，浅层代理，未被代理的可以被修改</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowReadonly</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createReactiveObject(target, <span class="hljs-literal">true</span>, readonlyHandles)
&#125;
<span class="hljs-keyword">const</span> reactiveMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>;
<span class="hljs-keyword">const</span> readonlyMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>;

<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param </span>target 要被代理的对象
 * <span class="hljs-doctag">@param </span>isReadOnly 是否为只读
 * <span class="hljs-doctag">@param </span>handles proxy中的处理逻辑(get/set)
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">target, isReadOnly, handles</span>) </span>&#123;
  <span class="hljs-comment">// 如果要被代理的对象不是一个对象,那么返回原对象</span>
  <span class="hljs-keyword">if</span> (!isObject(target)) <span class="hljs-keyword">return</span> target
  <span class="hljs-comment">// 先从缓存中读取结果，如果已经被存过了，那么直接返回缓存的代理结果即可</span>
  <span class="hljs-keyword">const</span> proxyMap = isReadOnly ? readonlyMap : reactiveMap
  <span class="hljs-keyword">const</span> isExitsProxy = proxyMap.get(target)
  <span class="hljs-keyword">if</span> (isExitsProxy) &#123;
    <span class="hljs-keyword">return</span> isExitsProxy
  &#125;
  <span class="hljs-comment">// 对象如果被代理过，就不用再次代理，那么我们需要将代理过的结果缓存起来</span>
  <span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handles)
  <span class="hljs-comment">// 缓存代理结果，形成原目标和代理目标的映射关系</span>
  proxyMap.set(target, proxy)
  <span class="hljs-comment">// 返回代理对象</span>
  <span class="hljs-keyword">return</span> proxy
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">4.4.2 baseHandles.ts文件中</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; extend, stringify, isObject, isArray, IntegerKey, hasOwn, hasChanged &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-keyword">readonly</span>, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./reactive"</span>
<span class="hljs-keyword">import</span> &#123; OpeaTypes, TriggerTypes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"packages/shared/src/opeartors"</span>
<span class="hljs-keyword">import</span> &#123; track, trigger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./effect"</span>

<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param </span>readonly 是否为只读的，默认不是
 * <span class="hljs-doctag">@param </span>shallow 是否为浅层的，默认不是
 */</span>
<span class="hljs-keyword">const</span> createGetter = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">isReadonly = <span class="hljs-literal">false</span>, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-comment">// 真实的get函数，当读取代理对象中的值时，会触发此函数</span>
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@param </span>target 目标对象
   * <span class="hljs-doctag">@param </span>property 被获取的属性名
   * <span class="hljs-doctag">@param </span>receiver 代理对象
   */</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params">target, property, receiver</span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, property, receiver)
    <span class="hljs-comment">// 如果不是只读的，就说明要收集对应的依赖，因为只读的话不能被修改，所以不需要收集依赖，这些依赖后面会去更新我们对应的视图</span>
    <span class="hljs-keyword">if</span> (!isReadonly) &#123;
      <span class="hljs-comment">// 收集依赖...</span>
      track(target, OpeaTypes.GET, property)
    &#125;
    <span class="hljs-comment">// 如果是浅层代理，那么直接返回结果即可,不需要继续进行代理了</span>
    <span class="hljs-keyword">if</span> (shallow) &#123;
      <span class="hljs-keyword">return</span> res
    &#125;
    <span class="hljs-comment">// 如果取到的值还是一个对象,那么我们要递归进行代理</span>
    <span class="hljs-keyword">if</span> (isObject(res)) &#123;
      <span class="hljs-comment">// 看是否为只读的</span>
      <span class="hljs-keyword">return</span> isReadonly ? <span class="hljs-keyword">readonly</span>(res) : reactive(res)
    &#125;

    <span class="hljs-keyword">return</span> res
  &#125;
&#125;
<span class="hljs-keyword">const</span> createSetter = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@param </span>target 目标对象
   * <span class="hljs-doctag">@param </span>property 被获取的属性名
   * <span class="hljs-doctag">@param </span>value 新属性值
   * <span class="hljs-doctag">@param </span>receiver 代理对象
   */</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">target, property, value, receiver</span>) </span>&#123;
    <span class="hljs-comment">// 拿到老值,后面实现watch的时候会用到</span>
    <span class="hljs-keyword">let</span> oldValue = target[property]
    <span class="hljs-comment">// 判断是新增还是修改,可能是数组，可能是对象,因为reactive包裹的是一个对象</span>
    <span class="hljs-keyword">const</span> hadKey = isArray(target) && IntegerKey(property)
      ? <span class="hljs-built_in">Number</span>(property) < target.length
      : hasOwn(target, property)
    <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.set(target, property, value, receiver)
    <span class="hljs-keyword">if</span> (!hadKey) &#123;
      <span class="hljs-comment">// 新增</span>
      trigger(target, TriggerTypes.ADD, property, value)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasChanged(oldValue, value)) &#123;
      <span class="hljs-comment">// 修改</span>
      trigger(target, TriggerTypes.SET, property, value, oldValue)
    &#125;
    <span class="hljs-keyword">return</span> res
  &#125;
&#125;
<span class="hljs-keyword">const</span> readonlyObj = &#123;
  <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`set <span class="hljs-subst">$&#123;key&#125;</span> on <span class="hljs-subst">$&#123;stringify(target)&#125;</span> failed`</span>)
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mutableHandles = &#123;
  <span class="hljs-attr">get</span>: createGetter(),
  <span class="hljs-attr">set</span>: createSetter()
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> shallowReactiveHandles = &#123;
  <span class="hljs-attr">get</span>: createGetter(<span class="hljs-literal">false</span>, <span class="hljs-literal">true</span>),
  <span class="hljs-attr">set</span>: createSetter(<span class="hljs-literal">true</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> readonlyHandles = extend(&#123;
  <span class="hljs-attr">get</span>: createGetter(<span class="hljs-literal">true</span>, <span class="hljs-literal">false</span>),
&#125;, readonlyObj.set)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> shallowReadonlyHandles = extend(&#123;
  <span class="hljs-attr">get</span>: createGetter(<span class="hljs-literal">true</span>, <span class="hljs-literal">true</span>)
&#125;, readonlyObj.set)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">4.4.3 effect.ts文件中</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; isArray &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; TriggerTypes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"packages/shared/src/opeartors"</span>

<span class="hljs-comment">// effect(() =>&#123;&#125;,&#123;flush:'sync'&#125;) 立即执行一次</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, options: <span class="hljs-built_in">any</span> = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// 高阶函数返回新的effect函数</span>
  <span class="hljs-keyword">const</span> effect = createReactiveEffect(fn, options)
  <span class="hljs-keyword">if</span> (!options.lazy) &#123;
    <span class="hljs-comment">// 因为一上来就执行了一次，所以我们这里执行了effect调用就是相当于执行了createReactiveEffect中的effect函数</span>
    effect()
  &#125;
  <span class="hljs-keyword">return</span> effect
&#125;
<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>, activeEffect, effectStack = []
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span>(<span class="hljs-params">fn, options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">/**
     * 我们可能会写出这样的代码
     * effect(() =>&#123;  ---> effect1
     *    state.name
     *    effect(() =>&#123; ---> effect2
     *         state.age
     *    &#125;)
     *    state.address
     * &#125;)
     * 当我们进行第一次取值state.name时,name和effect1进行关联
     * 当我们进行第二次取值state.age时,age和effect2进行关联
     * 但是当我们进行第三次取值state.address时,此时的address和effect2关联了,就不对了
     * 因为effect的调用就是一个类似函数的调用栈，所以我们可以用一个栈形结构来维护key和effect的关系
     * 我们调用用户的函数可能会发生异常
     */</span>
    <span class="hljs-keyword">try</span> &#123;
      effectStack.push(effect)
      activeEffect = effect
      <span class="hljs-comment">// const fn = () => &#123;</span>
      <span class="hljs-comment">//   console.log(state.name + state.age)</span>
      <span class="hljs-comment">// &#125;</span>
      <span class="hljs-comment">// effect(fn)</span>
      <span class="hljs-comment">// 函数调用，会进行取值，我们需要收集对应的依赖关系，后续当状态发生改变，我们可以通知视图去更新，类似于Vue2中的 Dep / Watcher</span>
      <span class="hljs-comment">// effect的返回值就是函数调用的返回值</span>
      <span class="hljs-comment">// 取值走get</span>
      <span class="hljs-keyword">return</span> fn()
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// 调用完函数从栈中抛出</span>
      effectStack.pop()
      <span class="hljs-comment">// 让我们下一个的effect指向正确的effect</span>
      activeEffect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
    &#125;
  &#125;
  effect.uid = uid++ <span class="hljs-comment">// effect的唯一标识</span>
  effect._isEffect = <span class="hljs-literal">true</span> <span class="hljs-comment">// 标识是否为响应式effect</span>
  effect.raw = fn <span class="hljs-comment">// 将用户回调函数和effect做一个关联</span>
  effect.options = options <span class="hljs-comment">// 储存用户的配置选项</span>
  <span class="hljs-keyword">return</span> effect
&#125;
<span class="hljs-keyword">let</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>;
<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param </span>target 目标对象
 * <span class="hljs-doctag">@param </span>type 唯一标识
 * <span class="hljs-doctag">@param </span>key 对象的key
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target, <span class="hljs-keyword">type</span>, key</span>) </span>&#123;
  <span class="hljs-comment">// 要将key和对应的effect进行关联，我们用一个全局变量</span>
  <span class="hljs-comment">// 因为我们只有在effect中使用状态才会进行依赖收集,在外界使用我们是不管的,而每次get时都会触发此方法，所以我们需要判断一下activeEffect是否有值</span>
  <span class="hljs-comment">// 有值就说明是在effect中使用的状态</span>
  <span class="hljs-keyword">if</span> (activeEffect) &#123;
    <span class="hljs-comment">// 我们需要将key和effect进行关联，而key也应该和对应的目标对象进行关联，effect可能有多个，也有可能会重复，所以这里的关系是这样的</span>
    <span class="hljs-comment">// (WeakMap target) => (Map key => Set effect)</span>
    <span class="hljs-keyword">let</span> depsMap = targetMap.get(target)
    <span class="hljs-comment">// 第一次WeakMap中肯定没有target目标对象</span>
    <span class="hljs-keyword">if</span> (!depsMap) &#123;
      targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>))
    &#125;
    <span class="hljs-keyword">let</span> deps = depsMap.get(key)
    <span class="hljs-comment">// 第一次Map中肯定没有key</span>
    <span class="hljs-keyword">if</span> (!deps) &#123;
      depsMap.set(key, (deps = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>))
    &#125;
    <span class="hljs-comment">// 第一次Set中肯定没有effect</span>
    <span class="hljs-keyword">if</span> (!deps.has(key)) &#123;
      deps.add(activeEffect)
    &#125;
    <span class="hljs-comment">// 这样我们的关系就建立了,等到用户修改数据时，我们通知对应的effect重新执行即可</span>
  &#125;
&#125;
<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param </span>target 目标对象
 * <span class="hljs-doctag">@param </span>type 标识是新增还是修改,0新增,1修改
 * <span class="hljs-doctag">@param </span>key 要对哪个key进行操作
 * <span class="hljs-doctag">@param </span>value 操作后的结果值
 * <span class="hljs-doctag">@param </span>oldValue 操作前的结果值
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target, <span class="hljs-keyword">type</span>, key, value, oldValue?</span>) </span>&#123;
  <span class="hljs-comment">// 如果没有收集过对应的依赖，那么是不需要进行更新的</span>
  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target)
  <span class="hljs-keyword">if</span> (!depsMap) <span class="hljs-keyword">return</span>
  <span class="hljs-comment">// 用于存放要执行的effect函数集合</span>
  <span class="hljs-keyword">const</span> effects = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">deps</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (deps) &#123;
      deps.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> effects.add(effect))
    &#125;
  &#125;
  <span class="hljs-comment">// 说明改的是数组的length</span>
  <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> && isArray(target)) &#123;
    <span class="hljs-comment">// 我们需要循环depsMap,将要执行的effect全部添加到容器中</span>
    depsMap.forEach(<span class="hljs-function">(<span class="hljs-params">dep, key</span>) =></span> &#123;
      <span class="hljs-comment">// key > value 是这种情况</span>
      <span class="hljs-comment">/**
       * const state = reactive(&#123;arr:[1,2,3]&#125;)
      *  effect(() => console.log(state.arr[2]))
      *  setTimeout(() =>&#123; state.arr.length = 1 &#125;,1000)
      * 此时的key为2, value是1 ,也要进行更新
       */</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> key !== <span class="hljs-string">'symbol'</span>) &#123;
        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> || key > value) &#123;
          add(dep)
        &#125;
      &#125;
    &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 对象</span>
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-literal">undefined</span>) &#123;
      add(depsMap.get(key))
    &#125;
    <span class="hljs-comment">// 如果修改数组中的某一个索引，也要更新</span>
    <span class="hljs-keyword">switch</span> (<span class="hljs-keyword">type</span>) &#123;
      <span class="hljs-keyword">case</span> TriggerTypes.ADD:
        <span class="hljs-comment">// 表示是新增，通知length的effect去更新</span>
        add(depsMap.get(<span class="hljs-string">'length'</span>))
    &#125;
  &#125;
  <span class="hljs-comment">// 让effect更新</span>
  effects.forEach(<span class="hljs-function">(<span class="hljs-params">effect: <span class="hljs-built_in">any</span></span>) =></span> effect())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">4.4.4 shared/index.ts文件中</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 判断是否为对象类型</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> isObject = <span class="hljs-function"><span class="hljs-params">val</span> =></span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span> && val !== <span class="hljs-literal">null</span>
<span class="hljs-comment">// 合并方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> extend = <span class="hljs-built_in">Object</span>.assign
<span class="hljs-comment">// JSON.stringify</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> stringify = <span class="hljs-built_in">JSON</span>.stringify
<span class="hljs-comment">// 判断是否为数组</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> isArray = <span class="hljs-built_in">Array</span>.isArray
<span class="hljs-comment">// 判断是否为一个整型key</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> IntegerKey = <span class="hljs-function"><span class="hljs-params">key</span> =></span> <span class="hljs-built_in">parseInt</span>(key) + <span class="hljs-string">''</span> === key
<span class="hljs-comment">// 判断是否为一个函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> isFunc = <span class="hljs-function"><span class="hljs-params">val</span> =></span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'function'</span>
<span class="hljs-comment">// 判断是否是自身上的属性</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> hasOwn = <span class="hljs-function">(<span class="hljs-params">target, key</span>) =></span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(target, key)
<span class="hljs-comment">// 判断2个值是否不相等</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> hasChanged = <span class="hljs-function">(<span class="hljs-params">oldValue, value</span>) =></span> oldValue !== value
<span class="hljs-comment">// 打印</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> warn = <span class="hljs-function"><span class="hljs-params">val</span> =></span> <span class="hljs-built_in">console</span>.warn(val)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">4.5 ref 、shallowRef  实现</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; track, trigger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./effect"</span>
<span class="hljs-keyword">import</span> &#123; TrackTypes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"packages/shared/src/opeartors"</span>
<span class="hljs-keyword">import</span> &#123; hasChanged, isArray &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; isObject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./reactive"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRef</span>(<span class="hljs-params">rawValue, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> RefImpl(rawValue, shallow)
&#125;
<span class="hljs-keyword">const</span> convert = <span class="hljs-function"><span class="hljs-params">val</span> =></span> isObject(val) ? reactive(val) : val;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RefImpl</span> </span>&#123;
  <span class="hljs-comment">// 声明属性</span>
  <span class="hljs-keyword">public</span> _v_isRef = <span class="hljs-literal">true</span> <span class="hljs-comment">// 标识是一个ref属性</span>
  <span class="hljs-keyword">public</span> _value
  <span class="hljs-comment">// 简写:相当于在内部 this.rawValue = rawValue;this.shallow = shallow</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> rawValue, <span class="hljs-keyword">public</span> shallow</span>)</span> &#123;
    <span class="hljs-comment">// ref可以接收对象类型，如果接收的是对象类型，需要定义成响应式</span>
    <span class="hljs-built_in">this</span>._value = shallow ? rawValue : convert(rawValue)
  &#125;
  <span class="hljs-comment">// 类的属性访问器，编译后为Object.defineProperty</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-comment">// 外界: let r = ref(''); </span>
    <span class="hljs-comment">// 当外界去访问 r.value 时，要收集相关依赖 ==> track</span>
    <span class="hljs-comment">// 当外界去设置 r.value 时，要通知更新 ==> trigger</span>
    <span class="hljs-comment">// r.value 访问的是 this._value</span>
    <span class="hljs-comment">// 这样我们使用r.value时，value就会和对应的effect进行关联</span>
    <span class="hljs-comment">// 关联关系: RefImpl的实例 => value => [effect]</span>
    track(<span class="hljs-built_in">this</span>, TrackTypes.GET, <span class="hljs-string">'value'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newValue</span>) &#123;
    <span class="hljs-comment">// 通知更新</span>
    <span class="hljs-keyword">if</span> (hasChanged(<span class="hljs-built_in">this</span>.rawValue, newValue)) &#123;
      <span class="hljs-comment">// 这次的新值当成下一次的老值</span>
      <span class="hljs-built_in">this</span>._value = <span class="hljs-built_in">this</span>.shallow ? newValue : convert(newValue)
      <span class="hljs-built_in">this</span>.rawValue = newValue
      trigger(<span class="hljs-built_in">this</span>, TrackTypes.SET, <span class="hljs-string">'value'</span>, newValue, <span class="hljs-built_in">this</span>.rawValue)
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">rawValue</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createRef(rawValue)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowRef</span>(<span class="hljs-params">rawValue</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createRef(rawValue, <span class="hljs-literal">true</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">4.6 toRef、toRefs 实现</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; track, trigger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./effect"</span>
<span class="hljs-keyword">import</span> &#123; TrackTypes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"packages/shared/src/opeartors"</span>
<span class="hljs-keyword">import</span> &#123; hasChanged, isArray &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; isObject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./reactive"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRef</span>(<span class="hljs-params">rawValue, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> RefImpl(rawValue, shallow)
&#125;
<span class="hljs-keyword">const</span> convert = <span class="hljs-function"><span class="hljs-params">val</span> =></span> isObject(val) ? reactive(val) : val;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RefImpl</span> </span>&#123;
  <span class="hljs-comment">// 声明属性</span>
  <span class="hljs-keyword">public</span> _v_isRef = <span class="hljs-literal">true</span> <span class="hljs-comment">// 标识是一个ref属性</span>
  <span class="hljs-keyword">public</span> _value
  <span class="hljs-comment">// 简写:相当于在内部 this.rawValue = rawValue;this.shallow = shallow</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> rawValue, <span class="hljs-keyword">public</span> shallow</span>)</span> &#123;
    <span class="hljs-comment">// ref可以接收对象类型，如果接收的是对象类型，需要定义成响应式</span>
    <span class="hljs-built_in">this</span>._value = shallow ? rawValue : convert(rawValue)
  &#125;
  <span class="hljs-comment">// 类的属性访问器，编译后为Object.defineProperty</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-comment">// 外界: let r = ref(''); </span>
    <span class="hljs-comment">// 当外界去访问 r.value 时，要收集相关依赖 ==> track</span>
    <span class="hljs-comment">// 当外界去设置 r.value 时，要通知更新 ==> trigger</span>
    <span class="hljs-comment">// r.value 访问的是 this._value</span>
    <span class="hljs-comment">// 这样我们使用r.value时，value就会和对应的effect进行关联</span>
    <span class="hljs-comment">// 关联关系: RefImpl的实例 => value => [effect]</span>
    track(<span class="hljs-built_in">this</span>, TrackTypes.GET, <span class="hljs-string">'value'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newValue</span>) &#123;
    <span class="hljs-comment">// 通知更新</span>
    <span class="hljs-keyword">if</span> (hasChanged(<span class="hljs-built_in">this</span>.rawValue, newValue)) &#123;
      <span class="hljs-comment">// 这次的新值当成下一次的老值</span>
      <span class="hljs-built_in">this</span>._value = <span class="hljs-built_in">this</span>.shallow ? newValue : convert(newValue)
      <span class="hljs-built_in">this</span>.rawValue = newValue
      trigger(<span class="hljs-built_in">this</span>, TrackTypes.SET, <span class="hljs-string">'value'</span>, newValue, <span class="hljs-built_in">this</span>.rawValue)
    &#125;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObjectRefImpl</span> </span>&#123;
  <span class="hljs-keyword">public</span> _v_isRef = <span class="hljs-literal">true</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> target, <span class="hljs-keyword">public</span> key</span>)</span> &#123;

  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.target[<span class="hljs-built_in">this</span>.key]
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newValue</span>) &#123;
    <span class="hljs-built_in">this</span>.target[<span class="hljs-built_in">this</span>.key] = newValue
  &#125;
&#125;
<span class="hljs-comment">// 将一个值包装成ref对象，是否为响应式取决于原来的值是否是响应式</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRef</span>(<span class="hljs-params">target, key</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ObjectRefImpl(target, key)
&#125;
<span class="hljs-comment">// 将多个值包装成ref对象，是否为响应式取决于原来的值是否是响应式</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRefs</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-comment">// const r = toRefs(state)</span>
  <span class="hljs-comment">// target可能是数组，可能是对象</span>
  <span class="hljs-keyword">const</span> res = isArray(target) ? <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(target.length) : &#123;&#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> target) &#123;
    res[key] = toRef(target, key)
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">4.7 computed 实现</h3>
<h4 data-id="heading-26">4.7.1 computed.ts文件</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; isFunc, warn &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>
<span class="hljs-keyword">import</span> &#123; effect, track, trigger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./effect"</span>
<span class="hljs-keyword">import</span> &#123; TrackTypes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"packages/shared/src/opeartors"</span>

<span class="hljs-comment">/*
      计算属性特点:
        默认不会执行，当取值时才会执行
        有缓存，如果状态没有发生变化，不会重新执行函数，会返回上一次值
        可以传入一个函数，这个函数就是getter函数
        也可以传入一个配置项，配置项中包含get和set
        computed(() =>&#123;&#125;)
        computed(&#123;get()&#123;&#125;,set()&#123;&#125;&#125;)
*/</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span>(<span class="hljs-params">getterOrOptions</span>) </span>&#123;
  <span class="hljs-keyword">let</span> getter, setter
  <span class="hljs-keyword">if</span> (isFunc(getterOrOptions)) &#123;
    <span class="hljs-comment">// 是函数的情况</span>
    getter = getterOrOptions
    setter = <span class="hljs-function">() =></span> warn(<span class="hljs-string">'Write operation failed: computed value is readonly'</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 是配置项的情况</span>
    getter = getterOrOptions.get
    setter = getterOrOptions.set
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ComputedRefImpl(getter, setter)
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ComputedRefImpl</span> </span>&#123;
  <span class="hljs-comment">// 标识计算属性getter的返回值</span>
  <span class="hljs-keyword">public</span> _value
  <span class="hljs-comment">// 标识是一个Ref</span>
  <span class="hljs-keyword">public</span> _v_isRef = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// 默认是脏的，通过此变量来控制是否需要缓存</span>
  <span class="hljs-keyword">public</span> _dirty = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">public</span> effect
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> getter, <span class="hljs-keyword">public</span> setter</span>)</span> &#123;
    <span class="hljs-comment">// 默认getter不会执行,只有取值时才会执行</span>
    <span class="hljs-built_in">this</span>.effect = effect(getter, &#123;
      <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 默认不执行</span>
      <span class="hljs-attr">scheduler</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 说明变化过</span>
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>._dirty) &#123;
          <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">true</span>
          <span class="hljs-comment">// 通知更新</span>
          trigger(<span class="hljs-built_in">this</span>, TrackTypes.SET, <span class="hljs-string">'value'</span>)
        &#125;
      &#125;
    &#125;)
  &#125;
  <span class="hljs-comment">/**
   * 外界是这么访问的
   * const state = reactive(&#123;age:10&#125;)
   * const c = computed(() => state.age + 10)
   * c.value ==> 20
   */</span>
  <span class="hljs-comment">// 当读取c.value时，要调用我们的getter函数，函数的返回值作为我们的_value值</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-comment">// 要看一下依赖是否变化过，依赖变化过我们的dirty变量就为false</span>
    <span class="hljs-comment">// 计算属性中依赖的响应式数据如果发生变化了，当我们再次取值时会重新执行getter函数</span>
    <span class="hljs-comment">// 那么我们需要收集getter中的依赖</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._dirty) &#123;
      <span class="hljs-comment">// effect的返回值就是用户回调的返回值</span>
      <span class="hljs-built_in">this</span>._value = <span class="hljs-built_in">this</span>.effect()
      <span class="hljs-comment">// 缓存，下一次在取值就进入不到此判断中，会返回上一次的值</span>
      <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-comment">// 收集依赖</span>
    track(<span class="hljs-built_in">this</span>, TrackTypes.GET, <span class="hljs-string">'value'</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
    <span class="hljs-built_in">this</span>.setter(newVal)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">4.7.2 effect.ts文件中修改</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 让effect更新</span>
effects.forEach(<span class="hljs-function">(<span class="hljs-params">effect: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (effect.options.scheduler) &#123;
      <span class="hljs-keyword">return</span> effect.options.scheduler()
    &#125;
    <span class="hljs-keyword">return</span> effect()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">5. 总结</h2>
<blockquote>
<p>看了Vue2和Vue3源码中响应式处理这一部分，很明显的感觉到Vue3对于响应式数据处理这一块代码上简洁了很多，所有的功能都可以拆开然后单独使用，不需要反复横跳及切换文件。</p>
<p>个人去实现响应式Api并不是为了证明给谁看，而是去学习人家背后的设计思想，去学人家的编码设计，从而让我们在使用这些Api的过程中更加得心应手，在工作中，不可避免的会产生Bug，如果Bug的层次比较深，在相关的网站上查询不到这些问题，那么只能通过调试源码的方式去解决问题。</p>
<p>前端技术更新很快，我们在学习的过程中要以 知其所以然 的态度去对待，这样才能保证自己的核心竞争力及工作中较为不错的编码能力和架构思维</p>
<p>本文有写的不好的地方还请指出，多多包涵，不喜勿喷！</p>
</blockquote></div>  
</div>
            