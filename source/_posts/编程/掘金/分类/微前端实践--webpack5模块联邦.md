
---
title: '微前端实践--webpack5模块联邦'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b58df968ca94842be6656a28744f087~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 10:28:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b58df968ca94842be6656a28744f087~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>webpack5推出一个非常令人惊艳的功能叫<code>module federation</code>,中文叫<code>模块联邦</code>，它提供了一套在不同项目构建之间的调度、运行机制。它很像<code>微前端</code>，但又不限于此。本文结合案例介绍一下该特性的基本应用和原理。</p>
</blockquote>
<h2 data-id="heading-0">类似微前端</h2>
<p>微前端的概念相信大家都不陌生，其本质是服务的拆分与隔离，最大程度地减少服务之间的冲突与碰撞。webpack的模块联邦做的事情与此差不多。</p>
<p>不过，webpack模块联邦有更多的优点：</p>
<ul>
<li>基于webpack生态，学习成本、实施成本低。毕竟大多数项目都在webpack</li>
<li>天生的工程化，npm各种包任你发挥</li>
<li>相关概念脉络清晰易懂</li>
<li>配置简单易上手，官方也提供了基于各种框架的版本</li>
</ul>
<p>那么，如果你之前有过在前端实践微服务的念头，又由于这样那样的原因没有实施，现在，你的机会来了！</p>
<h2 data-id="heading-1">三个概念</h2>
<p>首先，要理解三个重要的概念：</p>
<ul>
<li><strong>webpack构建</strong>。一个独立项目通过webpack打包编译而产生资源包。</li>
<li><strong>remote</strong>。一个暴露模块供其他<code>webpakc构建</code>消费的<code>webpack构建</code>。</li>
<li><strong>host</strong>。一个消费其他<code>remote</code>模块的<code>webpack构建</code>。</li>
</ul>
<p>一言以蔽之，一个<strong>webpack构建</strong>可以是remote--即服务的提供方，也可以是host--即服务的消费方，也可以同时扮演服务提供者和服务消费者，完全看项目的架构。</p>
<p>host与remote两个角色的依赖关系可用下图表示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b58df968ca94842be6656a28744f087~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要指出的是，<strong>任何一个webpack构建既可以作为host消费方，也可以作为remote提供方</strong>，区别在于职责和webpack配置的不同。</p>
<h2 data-id="heading-2">案例实操</h2>
<h3 data-id="heading-3">项目依赖关系介绍</h3>
<p>一共有三个微应用:<code>lib-app</code>、<code>component-app</code>、<code>main-app</code>，角色分别是：</p>
<ul>
<li><code>lib-app</code>as remote,暴露了两个模块<code>react</code>和<code>react-dom</code></li>
<li><code>component-app</code> as remote and host,依赖<code>lib-app</code>,暴露了一些组件供<code>main-app</code>消费</li>
<li><code>main-app</code> as host,依赖<code>lib-app</code>和<code>component-app</code></li>
</ul>
<h3 data-id="heading-4">lib-app暴露模块</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...省略</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> ModuleFederationPlugin(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"lib_app"</span>,
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"remoteEntry.js"</span>,
            <span class="hljs-attr">exposes</span>: &#123;
                <span class="hljs-string">"./react"</span>:<span class="hljs-string">"react"</span>,
                <span class="hljs-string">"./react-dom"</span>:<span class="hljs-string">"react-dom"</span>
            &#125;
        &#125;)
    ],
    <span class="hljs-comment">//...省略</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e46632795274b96acb7105d3fb5ae95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
除去生成的map文件，有四个文件：<code>main.js</code>、<code>remoteEntry.js</code>、<code>...react_index.js</code>、<code>...react-dom_index.js</code>；</p>
<ul>
<li>第一个是本项目的入口文件（该项目只是暴露接口，所以该文件为空）</li>
<li>第二个是远程入口文件，其他webpack构建使用、访问本项目暴露的模块时，须通过它来加载</li>
<li>第三个和第四个是暴露的模块，供其他项目消费</li>
</ul>
<h3 data-id="heading-5">component-app的配置</h3>
<p>依赖<code>lib-app</code>,暴露三个模块组件<code>Button</code>、<code>Dialog</code>、<code>Logo</code></p>
<pre><code class="copyable">//webpack.config.js
module.exports = &#123;
    //...省略
    plugins:[
        new ModuleFederationPlugin(&#123;
            name: "component_app",
            filename: "remoteEntry.js",
            exposes: &#123;
              "./Button":"./src/Button.jsx",
              "./Dialog":"./src/Dialog.jsx",
              "./Logo":"./src/Logo.jsx"
            &#125;,
            remotes:&#123;
                "lib-app":"lib_app@http://localhost:3000/remoteEntry.js"
            &#125;
        &#125;),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三个暴露的组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Button.jsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;color:</span> "#<span class="hljs-attr">fff</span>",<span class="hljs-attr">backgroundColor:</span> "#<span class="hljs-attr">409eff</span>",<span class="hljs-attr">borderColor:</span> "#<span class="hljs-attr">409eff</span>"&#125;&#125;></span>按钮组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Dialog.jsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dialog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.props.visible)&#123;
            <span class="hljs-keyword">return</span> (
                <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;position:</span>"<span class="hljs-attr">fixed</span>",<span class="hljs-attr">left:0</span>,<span class="hljs-attr">right:0</span>,<span class="hljs-attr">top:0</span>,<span class="hljs-attr">bottom:0</span>,<span class="hljs-attr">backgroundColor:</span>"<span class="hljs-attr">rgba</span>(<span class="hljs-attr">0</span>,<span class="hljs-attr">0</span>,<span class="hljs-attr">0</span>,<span class="hljs-attr">.3</span>)"&#125;&#125;></span>
                    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>this.props.switchVisible(false)&#125; style=&#123;&#123;position:"absolute",top:"10px",right:"10px"&#125;&#125;>X<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span>"<span class="hljs-attr">20</span>%",<span class="hljs-attr">textAlign:</span>"<span class="hljs-attr">center</span>"&#125;&#125;></span>
                        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>
                            What is your name ?
                        <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;fontSize:</span>"<span class="hljs-attr">18px</span>",<span class="hljs-attr">lineHeight:2</span>&#125;&#125; <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> /></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                    
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
                );
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Logo.jsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react'</span>;
<span class="hljs-keyword">import</span> pictureData <span class="hljs-keyword">from</span> <span class="hljs-string">'./MF.jpeg'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;pictureData&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;width:</span>"<span class="hljs-attr">500px</span>",<span class="hljs-attr">borderRadius:</span>"<span class="hljs-attr">10px</span>"&#125;&#125;/></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建结果基本跟上一个类似。
需要说明的是，为了保证暴露的组件可以正常工作，需要在本地做测试，main.js 是测试的入口函数。该子项目下运行<code>npm run start</code>打开浏览器：<code>localhost:3001</code>可以看到组件正常工作：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a14ca5da10334a07862e0b6a30c25285~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
并且打开控制台网络，<code>react</code>、<code>react-dom</code>模块已经从本项目中分离：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ce71a9c40624111baf66ff80dc61509~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">main-app的配置</h3>
<p>main-app依赖两个项目<code>lin-app</code>、<code>component-app</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">///webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//省略...</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> ModuleFederationPlugin(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"main_app"</span>,
            <span class="hljs-attr">remotes</span>:&#123;
                <span class="hljs-string">"lib-app"</span>:<span class="hljs-string">"lib_app@http://localhost:3000/remoteEntry.js"</span>,
                <span class="hljs-string">"component-app"</span>:<span class="hljs-string">"component_app@http://localhost:3001/remoteEntry.js"</span>
            &#125;,
        &#125;),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
          <span class="hljs-attr">template</span>: <span class="hljs-string">"./public/index.html"</span>,
        &#125;)
    ]
    <span class="hljs-comment">//省略...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于需要等待基础模块加载完毕，所以需要配置懒加载入口bootstrap.js.</p>
<ul>
<li>webpack打包入口文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>(<span class="hljs-string">"./bootstrap.js"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>bootstrap.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.jsx'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react-dom'</span>;
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react'</span>
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"app"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>根组件App.jsx</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'lib-app/react'</span>;
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'component-app/Button'</span>
<span class="hljs-keyword">import</span> Dialog <span class="hljs-keyword">from</span> <span class="hljs-string">'component-app/Dialog'</span>
<span class="hljs-keyword">import</span> Logo <span class="hljs-keyword">from</span> <span class="hljs-string">'component-app/Logo'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-comment">//省略...</span>
  &#125;
  <span class="hljs-comment">//省略...</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      //省略...
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行并打开浏览器<code>http://localhost:3002</code>:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/385f112113064157929ddac36707ba4d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看控制台，资源进行了很好的分离：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3905e8951f4b4c899ce7d2aaa83eb584~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">基本原理</h2>
<p>这一节，我们从host的代码着手，简单分析这一切是如何交互、工作的。</p>
<p>程序从main.js里的一段代码开始：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__webpack_require__.e(<span class="hljs-string">"bootstrap_js"</span>).then(__webpack_require__.bind(__webpack_require__,<span class="hljs-string">"./bootstrap.js"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>__webpack_require__.e("bootstrap_js")</code>是加载id为<code>bootstrap_js</code>的chunk的所有依赖，返回一个<code>promise</code>.等一切依赖就绪，再获取<code>./bootstrap.js</code>模块并执行</p>
<p>这里是<code>__webpack_require__.e</code>的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__webpack_require__.e = <span class="hljs-function">(<span class="hljs-params">chunkId</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(<span class="hljs-built_in">Object</span>.keys(__webpack_require__.f).reduce(<span class="hljs-function">(<span class="hljs-params">promises, key</span>) =></span> &#123;
__webpack_require__.f[key](chunkId, promises);
<span class="hljs-keyword">return</span> promises;
&#125;, []));
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面一段代码做了一件事，遍历<code>__webpack_require__.f</code>对象并依次执行对象里的成员函数，此时该对象有两个成员：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
<span class="hljs-attr">remotes</span>:<span class="hljs-function">(<span class="hljs-params">chunkId, promises</span>) =></span> &#123;
<span class="hljs-comment">//查找chunkId bootstrap_js对应的所有远程模块并加载</span>
<span class="hljs-keyword">var</span> chunkMapping = &#123;
                    <span class="hljs-string">"bootstrap_js"</span>: [
                        <span class="hljs-string">"webpack/container/remote/lib-app/react"</span>,
                        <span class="hljs-string">"webpack/container/remote/component-app/Button"</span>,
                        <span class="hljs-comment">//省略...</span>
                    ]
                &#125;;
                <span class="hljs-keyword">var</span> idToExternalAndNameMapping = &#123;
                    <span class="hljs-string">"webpack/container/remote/lib-app/react"</span>: [
                        <span class="hljs-string">"default"</span>,
                        <span class="hljs-string">"./react"</span>,
                        <span class="hljs-string">"webpack/container/reference/lib-app"</span>
                    ],
                    <span class="hljs-string">"webpack/container/remote/component-app/Button"</span>: [
                        <span class="hljs-string">"default"</span>,
                        <span class="hljs-string">"./Button"</span>,
                        <span class="hljs-string">"webpack/container/reference/component-app"</span>
                    ],
                    <span class="hljs-comment">//...省略</span>
                &#125;;
&#125;,
<span class="hljs-attr">j</span>:<span class="hljs-function">(<span class="hljs-params">chunkId,promises</span>)=></span>&#123;
<span class="hljs-comment">//负责加载chunkId对应的本地模块</span>
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上，<code>bootstrap_js</code>对应了两个promises：</p>
<ul>
<li>一个负责远程依赖加载</li>
<li>另一个负责本地加载</li>
</ul>
<p>等到所有依赖模块加载完准备就绪，才会require模块并执行。</p>
<p>当然，细节远不止此。源码里还有一些比较有趣的模块，如<code>__webpack_require__.l</code>负责以script标签的方式加载脚本、<code>webpackJsonpCallback</code>负责更新本地模块的promsie状态、<code>__webpack_require__.f.j</code>里远程模块的层级调用等，
囿于篇幅有限，无法作做过多深入介绍，有兴趣的朋友，欢迎留言讨论！</p>
<h2 data-id="heading-8">最后</h2>
<p>本文所涉及的案例已经托管到<a href="https://github.com/anderlaw/react-webpack-MF" target="_blank" rel="nofollow noopener noreferrer">Github</a>。</p>
<p>如有任何疑惑，欢迎留言讨论，如果本文对你有所帮助，可以点赞转发给更多的人哦。</p></div>  
</div>
            