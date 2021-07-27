
---
title: '面试官：请手动实现一个Sass-loader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9355'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 20:40:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=9355'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">什么是Loader</h2>
<p>一个<code>loader</code>可以看做是一个<code>node</code>模块，也可以看做一个<code>loader</code>就是一个函数 (loader会导出一个函数)，众所周知<code>webpack</code>只能识别<code>js</code>文件，<code>loader</code>在<code>webpack</code>中担任的角色就是翻译工作，它可以让其它非<code>js</code>的资源（source）可以在<code>webpack</code>中通过<code>loader</code>顺利加载。</p>
<p><strong>Loader的方式</strong></p>
<ul>
<li>单一职责，一个loader只做一件事</li>
<li>调用方式，loader是从右向左执行，链式调用</li>
<li>统一原则，loader输入和输出都字符串</li>
</ul>
<p><strong>来看一下案例</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">343</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这种会报错，我们上面说过<code>laoder</code>的方式了，统一原则，输出输入必须是字符串。而我们上面代码则输出是数字，则报错。</p>
<blockquote>
<p>loader导出尽量别使用箭头函数，loader内部属性都是靠this来获取的，如this.callback，this.sync</p>
</blockquote>
<h2 data-id="heading-1">Webpack手写Loader</h2>
<p>为什么要手写<code>loader</code>呢，假如有一些<code>loader</code>插件不满足我们的需求时，我们会采用手写<code>loader</code>来定制化我们功能。</p>
<h3 data-id="heading-2">开始</h3>
<p>首先新建一个<code>js</code>文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第一个参数：是当前要处理的内容</li>
</ul>
<h4 data-id="heading-3">loader内置的方法</h4>
<p>函数里面暴露了一些方法，<code>this.query</code>获取<code>loader</code>传过来的参数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.query)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然里面还可以引入一个库，来处理参数，该情况用于有时候我们传给<code>loader</code>的参数不是一个对象，可能是一个字符串。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css/</span>,
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">"testLoader"</span>,
                <span class="hljs-attr">query</span>: <span class="hljs-string">"前端娱乐圈"</span>
            &#125;]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> loaderUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>)
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(loaderUtils.getOptions(<span class="hljs-built_in">this</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css/</span>,
            use: [
                <span class="hljs-string">"testLoader?name=前端娱乐圈"</span>
            ]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用上面<code>loaderUtils</code>内置库获取<code>loader</code>的参数。</p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="copyable">module: &#123;
    rules: [
        &#123;
            test: /\.css/,
            use: [&#123;
            loader: "testLoader?name=前端娱乐圈",
            options: &#123;
            name: "前端娱乐圈"
            &#125;
            
            // or
            
            query: &#123;
            name: "前端娱乐圈"
            &#125;
            &#125;]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这两种传参形式，如果<code>options</code>存在，行内参数拼接则无效。上面还写了一种传参形式，<code>query</code>也是可以传参的，那<code>options</code>和<code>query</code>有什么区别的。这俩没啥区别就是，<code>query</code>是<code>webpack</code>老版本之前的(2.5)，<code>options</code>是最新支持的方式</p>
<h4 data-id="heading-4">loader异步</h4>
<p>loader异步处理，假如说loader里面需要处理一些逻辑操作，但这个操作是异步的，那么loader就会编译失败，必须使用异步执行方法，来等待结果返回后，loader则才回执行成功</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.callback(<span class="hljs-number">1</span>, source)
    &#125;, <span class="hljs-number">3000</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方解释：this.callback参数</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">this</span>.callback(
  err: <span class="hljs-built_in">Error</span> | <span class="hljs-literal">null</span>, <span class="hljs-comment">// 错误信息</span>
  <span class="hljs-attr">content</span>: <span class="hljs-built_in">string</span> | Buffer, <span class="hljs-comment">// 最终生成的源码</span>
  sourceMap?: SourceMap, <span class="hljs-comment">// 对应的sourcemap</span>
  meta?: <span class="hljs-built_in">any</span> <span class="hljs-comment">// 其他额外的信息</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种方法是 <strong>this.async</strong>，async返回值也是一个callback所以这俩个是一样的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> callback = <span class="hljs-built_in">this</span>.async()
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        callback(<span class="hljs-number">1</span>, source)
    &#125;, <span class="hljs-number">3000</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Loader起别名</h4>
<h5 data-id="heading-6">resolveLoader - modules</h5>
<p>我们现在手写的loader都还是写绝对路径引入进来，那么怎么直接写loader名呢，有两种方法，我们来看一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">resolveLoader</span>: &#123;
        <span class="hljs-attr">modules</span>: [<span class="hljs-string">"node_modules"</span>, <span class="hljs-string">"./loaders"</span>]
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js/</span>
                use: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">"per-loader"</span>
            &#125;
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到上面，我们直接写的<code>per-loader</code>，我们是配置了解析<code>loader</code>路径，会先去<code>node_modules</code>里面查找，如果<code>node_modules</code>里面没有则会去<code>loaders</code>目录下查找。然后我们下面写<code>loader: per-loader</code>，<strong>注意：这里的<code>per-loader</code>就是当前<code>loader</code>的文件名</strong></p>
<h5 data-id="heading-7">resolveLoader - alias</h5>
<p>这种方法直接起别名，把路径引入过来就ok</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">resolveLoader</span>: &#123;
        <span class="hljs-string">"per-loader"</span>: path.resolve(__dirname, <span class="hljs-string">"./loaders/per-loader.js"</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js/</span>
                use: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">"per-loader"</span>
            &#125;
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">实现一个sass-loader && style-loader</h4>
<h5 data-id="heading-9">sass-loader</h5>
<p>首先安装一下<code>node-sass</code>插件，用于识别<code>scss</code>语法并编译为<code>css</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i node-sass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建<code>sassLoader.js</code>文件，并引入<code>node-sass</code>插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> nodeSass = <span class="hljs-built_in">require</span>(<span class="hljs-string">"node-sass"</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>)

<span class="hljs-keyword">let</span> result = nodeSass.renderSync(&#123;
    <span class="hljs-attr">file</span>: path.resolve(__dirname, <span class="hljs-string">"../src/scss/index.scss"</span>),
    <span class="hljs-attr">outputStyle</span>: <span class="hljs-string">'expanded'</span>,
&#125;);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> result.css.toString()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面采用<code>node-sass</code>官方配置，如异步解析<code>.scss</code>文件，上面对象中，<code>file</code>为当前要解析的文件地址，<code>outputStyle</code>为输出风格包含：<code>nested</code>(嵌套)、<code>expanded</code>(展开)、<code>compact</code>(紧凑，不换行)、<code>compressed</code>(压缩)。</p>
<p>导出<code>result.css.toString</code>, 这里为什么要<code>toString</code>，如果不<code>toString</code>的话返回的是一个<code>Buffer</code>数据。因为这里的返回值提供给下一个<code>loader</code>使用，为了下一个<code>loader</code>(style-loader)更好的使用我们这里直接处理一下。</p>
<blockquote>
<p>更多Api用法请参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fnode-sass" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/node-sass" ref="nofollow noopener noreferrer">node-sass</a></p>
</blockquote>
<h5 data-id="heading-10">style-loader</h5>
<p>新建<code>styleLoader.js</code>文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> style = <span class="hljs-string">`
        let style = document.createElement("style");
        style.innerHTML = <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(source)&#125;</span>;
        document.head.appendChild(style)
`</span>
    <span class="hljs-keyword">return</span> style
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面导出的函数第一参数(<code>source</code>)就是我们<code>sassLoader</code>的返回值，然后在字符串里面写上创建style元素逻辑代码，并最终返回。注意这里返回值必须是<code>字符串</code>上，刚开始我们就说过了，输入输出都必须是字符串。</p>
<h5 data-id="heading-11">完整配置</h5>
<p><strong>index.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"前端娱乐圈"</span>)
<span class="hljs-keyword">import</span> <span class="hljs-string">"./scss/index.scss"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>
    &#125;,
    <span class="hljs-attr">resolveLoader</span>: &#123;
       <span class="hljs-attr">alias</span>: &#123;
           <span class="hljs-string">"sassLoader"</span>: path.resolve(__dirname, <span class="hljs-string">"./loaders/sassLoader.js"</span>),
           <span class="hljs-string">"styleLoader"</span>: path.resolve(__dirname, <span class="hljs-string">"./loaders/styleLoader.js"</span>)
       &#125;
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.scss/</span>,
                use: [<span class="hljs-string">"styleLoader"</span>, <span class="hljs-string">"sassLoader"</span>]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中我们用到了解析<code>loader</code>路径配置(起别名)，loader是从右到左，从下到上解析执行。先是把<code>.scss</code>文件处理成<code>css</code>语法，然后在传递给<code>styleLoader</code>配置即可。以上一个简单完整的<code>loader</code>已实现完毕。如有帮助欢迎点赞+分享哦</p>
<blockquote>
<p>欢迎关注我的公众号：前端娱乐圈</p>
</blockquote>
<h2 data-id="heading-12">感谢</h2>
<p>谢谢你读完本篇文章，希望对你能有所帮助，如有问题欢迎各位指正。</p>
<p>我是蛙人(✿◡‿◡)，如果觉得写得可以的话，请点个赞吧❤。</p>
<p>感兴趣的小伙伴可以加入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fqinzhiying.github.io" target="_blank" rel="nofollow noopener noreferrer" title="https://qinzhiying.github.io" ref="nofollow noopener noreferrer">[ 前端娱乐圈交流群 ]</a> 欢迎大家一起来交流讨论</p>
<p>写作不易，<strong>「点赞」+「在看」+「转发」</strong> 谢谢支持❤</p>
<h2 data-id="heading-13">往期推荐</h2>
<p><a href="https://juejin.cn/post/6977237451660066853" target="_blank" title="https://juejin.cn/post/6977237451660066853">《什么场景下使用Render函数，如何配置JSX》</a></p>
<p><a href="https://juejin.cn/post/6944940506862485511" target="_blank" title="https://juejin.cn/post/6944940506862485511">《分享15个Webpack实用的插件！！！》</a></p>
<p><a href="https://juejin.cn/post/6943793273395740680" target="_blank" title="https://juejin.cn/post/6943793273395740680">《手把手教你写一个Vue组件发布到npm且可外链引入使用》</a></p>
<p><a href="https://juejin.cn/post/6942322281913778206" target="_blank" title="https://juejin.cn/post/6942322281913778206">《分享12个Webpack中常用的Loader》</a></p>
<p><a href="https://juejin.cn/post/6938581764432461854" target="_blank" title="https://juejin.cn/post/6938581764432461854">《聊聊什么是CommonJs和Es Module及它们的区别》</a></p>
<p><a href="https://juejin.cn/post/6937092511508725774" target="_blank" title="https://juejin.cn/post/6937092511508725774">《这些工作中用到的JavaScript小技巧你都知道吗？》</a></p>
<p><a href="https://juejin.cn/post/6934487656873082887" target="_blank" title="https://juejin.cn/post/6934487656873082887">《【建议收藏】分享一些工作中常用的Git命令及特殊问题场景怎么解决》</a></p></div>  
</div>
            