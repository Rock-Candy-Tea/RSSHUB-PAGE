
---
title: '一起来看看Vite原理吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9020'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 19:17:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=9020'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vite是一个面向现代浏览器的一个更轻，更快的web应用开发工具，他基于ECMAScript标准原生模块系统ES Module实现。</p>
<p>他的出现是为了解决webpack冷启动时间过长，另外Webpack HMR热更新反应速度慢的问题。</p>
<p>使用Vite创建的项目就是一个普通的Vue3应用，相比基于Vue-cli创建的应用少了很多配置文件和依赖。Vite创建的项目开发依赖非常简单，只有Vite和@vue/compiler-sfc, Vite是一个运行工具，compiler-sfc是为了编译.vue结尾的单文件组件。</p>
<p>Vite目前仅支持Vue3.0的版本，在创建项目的时候通过制定不同的模板也支持使用其他框架，Vite提供了两个子命令。</p>
<pre><code class="hljs language-s copyable" lang="s"># 开启服务器
vite serve
# 打包
vite build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开启服务的时候不需要打包，所以启动速度特别快。在生产环境打包和webpack类似会将所有文件进行编译打包到一起。对于代码切割的需求Vite采用的是原生的动态导入来实现的，所以打包结果只能支持现代浏览器，如果老版本浏览器需要使用可以引入Polyfill。</p>
<p>之前我们使用Webpack打包是因为浏览器环境并不支持模块化，还有就是模块文件会产生大量的http请求。在现代浏览器模块坏已经被支持了，http2也解决了多文件请求的问题。当然你过你的应用需要支持IE浏览器，那么还是需要打包的。因为IE并不支持ES Module</p>
<p>Vite创建的项目几乎不需要额外的配置，默认支持TS、Less, Sass，Stylus，postcss等，但是需要单独安装对应的编译器。同时还支持jsx和web assembly。</p>
<p>Vite带来的好处是提升开发者在开发过程中的体验，web开发服务器不需要等待可以立即启动，模块热更新几乎是实时的，所需的文件按需编译，避免编译用不到的文件，开箱即用，避免loader及plugins的配置。</p>
<p>Vite的核心功能包括开启一个静态的web服务器，并且能够编译单文件组件，并且提供HMR功能。</p>
<p>当启动vite的时候首先会将当前项目目录作为静态服务器的跟目录，静态服务器会拦截部分请求，当请求单文件的时候会实时编译，以及处理其他浏览器不能识别的模块，通过websocket实现hmr。</p>
<p>我们自己来实现一下这个功能从而来学习其实现原理。</p>
<h4 data-id="heading-0">搭建静态测试服务器</h4>
<p>我们首先实现一个能够开启静态web服务器的命令行工具。vite内部使用的是KOA来实现静态服务器。(ps：node命令行工具可以查看我之前的文章，这里就不介绍了，直接贴代码)。</p>
<pre><code class="hljs language-s copyable" lang="s">npm init
npm install koa koa-send -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工具bin的入口文件设置为本地的index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>)
<span class="hljs-keyword">const</span> send = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-send'</span>)

<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa()

<span class="hljs-comment">// 开启静态文件服务器</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-comment">// 加载静态文件</span>
    <span class="hljs-keyword">await</span> send(ctx, ctx.path, &#123; <span class="hljs-attr">root</span>: process.cwd(), <span class="hljs-attr">index</span>: <span class="hljs-string">'index.html'</span>&#125;)
    <span class="hljs-keyword">await</span> next()
&#125;)

app.listen(<span class="hljs-number">5000</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器已经启动 http://localhost:5000'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就编写好了一个node静态服务器的工具。</p>
<h4 data-id="heading-1">处理第三方模块</h4>
<p>我们的做法是当代码中使用了第三方模块，我们可以通过修改第三方模块的路径，给他一个标识，然后再服务器中拿到这个标识来处理这个模块。</p>
<p>首先我们需要修改第三方模块的路径，这里我们需要一个新的中间件来实现。</p>
<p>需要判断一下当前返回给浏览器的文件是否是javascript，只需要看响应头中的content-type。</p>
<p>如果是javascript，需要找到这个文件中引入的模块路径。ctx.body就是返回给浏览器的内容文件。这里的数据是一个stream，需要转换成字符串来处理。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> stream2string = <span class="hljs-function">(<span class="hljs-params">stream</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Promse(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> chunks = [];
        stream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-params">chunk</span> =></span> &#123;chunks.push(chunk)&#125;)
        stream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123; resolve(Buffer.concat(chunks).toString(<span class="hljs-string">'utf-8'</span>))&#125;)
        stream.on(<span class="hljs-string">'error'</span>, reject)
    &#125;)
&#125;

<span class="hljs-comment">// 修改第三方模块路径</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-keyword">if</span> (ctx.type === <span class="hljs-string">'application/javascript'</span>) &#123;
        <span class="hljs-keyword">const</span> contents = <span class="hljs-keyword">await</span> stream2string(ctx.body);
        <span class="hljs-comment">// 将body中导入的路径修改一下，重新赋值给body返回给浏览器</span>
        <span class="hljs-comment">// import vue from 'vue', 匹配到from '修改为from '@modules/</span>
        ctx.body = contents.replace(<span class="hljs-regexp">/(from\s+['"])(?![\.\/])/g</span>, <span class="hljs-string">'$1/@modules/'</span>);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们开始加载第三方模块, 这里同样需要一个中间件，判断请求路径是否是我们修改过的@module开头，如果是的话就去node_modules里面加载对应的模块返回给浏览器。</p>
<p>这个中间件要放在静态服务器之前。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 加载第三方模块</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-keyword">if</span> (ctx.path.startsWith(<span class="hljs-string">'/@modules/'</span>)) &#123;
        <span class="hljs-comment">// 截取模块名称</span>
        <span class="hljs-keyword">const</span> moduleName = ctx.path.substr(<span class="hljs-number">10</span>);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到模块名称之后需要获取模块的入口文件，这里要获取的是ES Module模块的入口文件，需要先找到这个模块的package.json然后再获取这个package.json中的module字段的值也就是入口文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 找到模块路径</span>
<span class="hljs-keyword">const</span> pkgPath = path.join(process.pwd(), <span class="hljs-string">'node_modules'</span>, moduleName, <span class="hljs-string">'package.json'</span>);
<span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(pkgPath);
<span class="hljs-comment">// 重新给ctx.path赋值，需要重新设置一个存在的路径，因为之前的路径是不存在的</span>
ctx.path = path.join(<span class="hljs-string">'/node_modules'</span>, moduleName, pkg.module);
<span class="hljs-comment">// 执行下一个中间件</span>
awiat next();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样浏览器请求进来的时候虽然是@modules路径，但是我们在加载之前将path路径修改为了node_modules中的路径，这样在加载的时候就回去node_modules中获取文件，将加载的内容响应给浏览器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 加载第三方模块</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-keyword">if</span> (ctx.path.startsWith(<span class="hljs-string">'/@modules/'</span>)) &#123;
        <span class="hljs-comment">// 截取模块名称</span>
        <span class="hljs-keyword">const</span> moduleName = ctx.path.substr(<span class="hljs-number">10</span>);
        <span class="hljs-comment">// 找到模块路径</span>
        <span class="hljs-keyword">const</span> pkgPath = path.join(process.pwd(), <span class="hljs-string">'node_modules'</span>, moduleName, <span class="hljs-string">'package.json'</span>);
        <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(pkgPath);
        <span class="hljs-comment">// 重新给ctx.path赋值，需要重新设置一个存在的路径，因为之前的路径是不存在的</span>
        ctx.path = path.join(<span class="hljs-string">'/node_modules'</span>, moduleName, pkg.module);
        <span class="hljs-comment">// 执行下一个中间件</span>
        awiat next();
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">单文件组件处理</h4>
<p>之前我们说过浏览器是没办法处理.vue资源的, 浏览器只能识别js,css等常用资源，所以其他类型的资源都需要在服务端处理。当请求单文件组件的时候需要在服务器将单文件组件编译成js模块返回给浏览器。</p>
<p>当浏览器第一次请求文件(App.vue)的时候，服务器会把单文件组件编译成一个对象，先加载这个组件，然后再创建一个对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Hello <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/components/Hello.vue'</span>
<span class="hljs-keyword">const</span> __script = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
    <span class="hljs-attr">components</span>: &#123;
        Hello
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着再去加载入口文件，这次会告诉服务器编译一下这个单文件组件的模板，返回一个render函数。然后将render函数挂载到刚创建的组件选项对象上，最后导出选项对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; render <span class="hljs-keyword">as</span> __render &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'/src/App.vue?type=template'</span>
__script.rener = __render
__script.__hmrId = <span class="hljs-string">'/src/App.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> __script
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说vite会发送两次请求，第一次请求会编译单文件文件，第二次请求是编译单文件模板返回一个render函数。</p>
<ol>
<li>编译单文件选项</li>
</ol>
<p>我们首先来实现一下第一次请求单文件的情况。需要把单文件组件编译成一个选项，这里同样用一个中间件来实现。这个功能要在处理静态服务器只有，处理第三方模块路径之前。</p>
<p>我们首先需要对单文件组件进行编译。这里需要借助compiler-sfc。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 处理单文件组件</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-keyword">if</span> (ctx.path.endsWith(<span class="hljs-string">'.vue'</span>)) &#123;
        <span class="hljs-comment">// 获取响应文件内容，转换成字符串</span>
        <span class="hljs-keyword">const</span> contents = <span class="hljs-keyword">await</span> streamToString(ctx.body);
        <span class="hljs-comment">// 编译文件内容</span>
        <span class="hljs-keyword">const</span> &#123; descriptor &#125; = compilerSFC.parse(contents);
        <span class="hljs-comment">// 定义状态码</span>
        <span class="hljs-keyword">let</span> code;
        <span class="hljs-comment">// 不存在type就是第一次请求</span>
        <span class="hljs-keyword">if</span> (!ctx.query.type) &#123;
            code = descriptor.script.content;
            <span class="hljs-comment">// 这里的code格式是, 需要改造成我们前面贴出来的vite中的样子</span>
            <span class="hljs-comment">// import Hello from './components/Hello.vue'</span>
            <span class="hljs-comment">// export default &#123;</span>
            <span class="hljs-comment">//      name: 'App',</span>
            <span class="hljs-comment">//      components: &#123;</span>
            <span class="hljs-comment">//          Hello</span>
            <span class="hljs-comment">//      &#125;</span>
            <span class="hljs-comment">//  &#125;</span>
            <span class="hljs-comment">// 改造code的格式，将export default 替换为const __script =</span>
            code = code.relace(<span class="hljs-regexp">/export\s+default\s+/g</span>, <span class="hljs-string">'const __script = '</span>)
            code += <span class="hljs-string">`
                import &#123; render as __render &#125; from '<span class="hljs-subst">$&#123;ctx.path&#125;</span>?type=template'
                __script.rener = __render
                export default __script
            `</span>
        &#125;
        <span class="hljs-comment">// 设置浏览器响应头为js</span>
        ctx.type = <span class="hljs-string">'application/javascript'</span>
        <span class="hljs-comment">// 将字符串转换成数据流传给下一个中间件。</span>
        ctx.body = stringToStream(code);
    &#125;
    <span class="hljs-keyword">await</span> next()
&#125;)

<span class="hljs-keyword">const</span> stringToStream = <span class="hljs-function"><span class="hljs-params">text</span> =></span> &#123;
    <span class="hljs-keyword">const</span> stream = <span class="hljs-keyword">new</span> Readable();
    stream.push(text);
    stream.push(<span class="hljs-literal">null</span>);
    <span class="hljs-keyword">return</span> stream;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-s copyable" lang="s">npm install @vue/compiler-sfc -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们再来处理单文件组件的第二次请求，第二次请求url会带上type=template参数，我们需要将单文件组件模板编译成render函数。</p>
<p>我们首先要判断当前请求中有没有type=template</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!ctx.query.type) &#123;
    ...
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ctx.query.type === <span class="hljs-string">'template'</span>) &#123;
    <span class="hljs-comment">// 获取编译后的对象 code就是render函数</span>
    <span class="hljs-keyword">const</span> templateRender = compilerSFC.compileTemplate(&#123; <span class="hljs-attr">source</span>: descriptor.template.content &#125;)
    <span class="hljs-comment">// 将render函数赋值给code返回给浏览器</span>
    code = templateRender.code
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们还要处理一下工具中的process.env，因为这些代码会返回到浏览器中运行，如果不处理会默认为node，导致运行失败。可以在修改第三方模块路径的中间件中修改，修改完路径之后再添加一条修改process.env</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改第三方模块路径</span>
app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-keyword">if</span> (ctx.type === <span class="hljs-string">'application/javascript'</span>) &#123;
        <span class="hljs-keyword">const</span> contents = <span class="hljs-keyword">await</span> stream2string(ctx.body);
        <span class="hljs-comment">// 将body中导入的路径修改一下，重新赋值给body返回给浏览器</span>
        <span class="hljs-comment">// import vue from 'vue', 匹配到from '修改为from '@modules/</span>
        ctx.body = contents.replace(<span class="hljs-regexp">/(from\s+['"])(?![\.\/])/g</span>, <span class="hljs-string">'$1/@modules/'</span>).replace(<span class="hljs-regexp">/process\.env\.NODE_ENV/g</span>, <span class="hljs-string">'"development"'</span>);
    &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们就实现了一个简版的vite，当然这里我们只演示了.vue文件，对于css，less，其他资源都没有处理，不过方法都是类似的，感兴趣的同学可以自行实现。HRM也没有实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> &#123; Readable &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream)
const Koa = require('</span>koa<span class="hljs-string">')
const send = require('</span>koa-send<span class="hljs-string">')
const compilerSFC = require('</span>@vue/compiler-sfc<span class="hljs-string">')

const app = new Koa()

const stream2string = (stream) => &#123;
    return new Promse((resolve, reject) => &#123;
        const chunks = [];
        stream.on('</span>data<span class="hljs-string">', chunk => &#123;chunks.push(chunk)&#125;)
        stream.on('</span>end<span class="hljs-string">', () => &#123; resolve(Buffer.concat(chunks).toString('</span>utf-<span class="hljs-number">8</span><span class="hljs-string">'))&#125;)
        stream.on('</span>error<span class="hljs-string">', reject)
    &#125;)
&#125;

const stringToStream = text => &#123;
    const stream = new Readable();
    stream.push(text);
    stream.push(null);
    return stream;
&#125;

// 加载第三方模块
app.use(async (ctx, next) => &#123;
    if (ctx.path.startsWith('</span>/@modules/<span class="hljs-string">')) &#123;
        // 截取模块名称
        const moduleName = ctx.path.substr(10);
        // 找到模块路径
        const pkgPath = path.join(process.pwd(), '</span>node_modules<span class="hljs-string">', moduleName, '</span>package.json<span class="hljs-string">');
        const pkg = require(pkgPath);
        // 重新给ctx.path赋值，需要重新设置一个存在的路径，因为之前的路径是不存在的
        ctx.path = path.join('</span>/node_modules<span class="hljs-string">', moduleName, pkg.module);
        // 执行下一个中间件
        awiat next();
    &#125;
&#125;)

// 开启静态文件服务器
app.use(async (ctx, next) => &#123;
    // 加载静态文件
    await send(ctx, ctx.path, &#123; root: process.cwd(), index: '</span>index.html<span class="hljs-string">'&#125;)
    await next()
&#125;)

// 处理单文件组件
app.use(async (ctx, next) => &#123;
    if (ctx.path.endsWith('</span>.vue<span class="hljs-string">')) &#123;
        // 获取响应文件内容，转换成字符串
        const contents = await streamToString(ctx.body);
        // 编译文件内容
        const &#123; descriptor &#125; = compilerSFC.parse(contents);
        // 定义状态码
        let code;
        // 不存在type就是第一次请求
        if (!ctx.query.type) &#123;
            code = descriptor.script.content;
            // 这里的code格式是, 需要改造成我们前面贴出来的vite中的样子
            // import Hello from '</span>./components/Hello.vue<span class="hljs-string">'
            // export default &#123;
            //      name: '</span>App<span class="hljs-string">',
            //      components: &#123;
            //          Hello
            //      &#125;
            //  &#125;
            // 改造code的格式，将export default 替换为const __script =
            code = code.relace(/export\s+default\s+/g, '</span><span class="hljs-keyword">const</span> __script = <span class="hljs-string">')
            code += `
                import &#123; render as __render &#125; from '</span>$&#123;ctx.path&#125;?type=template<span class="hljs-string">'
                __script.rener = __render
                export default __script
            `
        &#125; else if (ctx.query.type === '</span>template<span class="hljs-string">') &#123;
            // 获取编译后的对象 code就是render函数
            const templateRender = compilerSFC.compileTemplate(&#123; source: descriptor.template.content &#125;)
            // 将render函数赋值给code返回给浏览器
            code = templateRender.code
        &#125;
        // 设置浏览器响应头为js
        ctx.type = '</span>application/javascript<span class="hljs-string">'
        // 将字符串转换成数据流传给下一个中间件。
        ctx.body = stringToStream(code);
    &#125;
    await next()
&#125;)

// 修改第三方模块路径
app.use(async (ctx, next) => &#123;
    if (ctx.type === '</span>application/javascript<span class="hljs-string">') &#123;
        const contents = await stream2string(ctx.body);
        // 将body中导入的路径修改一下，重新赋值给body返回给浏览器
        // import vue from '</span>vue<span class="hljs-string">', 匹配到from '</span>修改为<span class="hljs-keyword">from</span> <span class="hljs-string">'@modules/
        ctx.body = contents.replace(/(from\s+['</span><span class="hljs-string">"])(?![\.\/])/g, '$1/@modules/').replace(/process\.env\.NODE_ENV/g, '"</span>development<span class="hljs-string">"');
    &#125;
&#125;)

app.listen(5000)

console.log('服务器已经启动 http://localhost:5000')

</span><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            