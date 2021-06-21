
---
title: 'Babel polyfill 常见配置对比'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/576e7807b99e49ff99c841b086a2ba81~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 09:30:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/576e7807b99e49ff99c841b086a2ba81~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>在解决了使用core-js@2的旧项目中，项目打包后使用 ES 新 api 报错的问题之后。对比了解 <code>@babel/preset-env 、core-js@3 、@babel/runtime</code> 三者的使用场景和区别，总结出如下内容。内容中如有不当之处，还望不吝指正，理性交流。</p>
<h3 data-id="heading-1">Babel 是什么</h3>
<ul>
<li>Babel 是一个 JS 编译器，通过 Babel 我们可以把按最新标准编写的 JS 代码向下编译成兼容浏览器或其他环境的通用版本。</li>
<li>虽然 Babel 开箱即用，但是如果不做任何配置，输入原始代码，则会输出同样的原始代码。如果想要做一些实际工作，需要添加<code>插件（plugins）</code>。一个个手动引入需要的插件过于繁琐，所以通常会使用官方提供的<code>预设（presets）</code>，预设是插件的集合。</li>
<li>官方提供的预设：@babel/preset-env</li>
</ul>
<h3 data-id="heading-2">插件和预设的执行顺序</h3>
<ul>
<li>插件先执行，预设后执行</li>
<li>插件集从前往后执行</li>
<li>预设集从后往前执行</li>
</ul>
<h3 data-id="heading-3">Babel 转译代码，会将代码分成两部分</h3>
<ul>
<li><code>syntax</code>（语法）：箭头函数、let、const、展开运算符等</li>
<li><code>api</code>：Promise、includes、map等</li>
<li>Babel 默认不转换 syntax 和 api ，使用 @babel/preset-env 或 babel-runtime 后转换 syntax，但不会转换 api 。需要使用垫片（polyfill）转换 api，polyfill 可以让新的内置函数、实例方法等在低版本环境中也可以使用。</li>
</ul>
<h3 data-id="heading-4">官方给出了两种 polyfill 方案</h3>
<ul>
<li><code>babel-polyfill</code>：会污染全局适合在业务项目中使用。（Babel7.4.0版本开始，babel/polyfill 已经被废弃，推荐直接使用core-js）</li>
<li><code>babel-runtime</code>：不污染全局适合在组件或类库项目中使用。</li>
</ul>
<h3 data-id="heading-5">创建一个项目目录，来比较几种常见的 polyfill 配置</h3>
<pre><code class="hljs language-js copyable" lang="js"># 创建demo文件夹，进入并新建src文件夹和里面的index.js文件
mkdir demo && cd $_ && mkdir src && cd $_ && touch index.js

# 以默认配置初始化package.json
npm init -y            

# 安装 Babel核心库和命令行支持
npm install --save-dev @babel/core @babel/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">src/index.js的待编译代码</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/576e7807b99e49ff99c841b086a2ba81~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">1.不做任何配置</h3>
<p>配置 package.json 的 NPM Scripts 后，运行<code>npm run build</code></p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"babel src --out-dir lib"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>NPM 版本5.2以上，也可以直接运行编译命令：<code>npx babel src --out-dir lib</code></p>
<p><strong>会发现输出的 lib/index.js 文件，与编译之前没有区别，输出了原始代码。</strong></p>
<p><strong>在根目录添加文件：</strong></p>
<ul>
<li>babel.config.json（Babel配置文件）</li>
<li>.browserslistrc（声明了一段浏览器集合，根据这段集合描述，针对性的输出兼容性代码）</li>
</ul>
<p>看看使用了配置和浏览器策略之后，会有哪些改变。</p>
<h3 data-id="heading-8">2.@babel/preset-env</h3>
<ul>
<li>只转换syntax（class，typeof，箭头函数），不转换api（map，includes）</li>
<li>syntax的转换策略会根据浏览器策略（.browserslistrc文件的配置）改变</li>
<li>安装：npm i @babel/preset-env -D</li>
</ul>
<p>在 babel.config.json 文件中添加如下代码</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置兼容较低版本的浏览器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .browserslistrc</span>
><span class="hljs-number">0.25</span>%
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译之后的代码如下
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5ccb29e548e4e8ba8098af0a0083e35~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer">
设置兼容较高版本的浏览器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//.browserslistrc</span>
Chrome > <span class="hljs-number">75</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0af0e750653746b3a8856693b9b7ed42~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">3.@babel/preset-env + core-js@3</h3>
<ul>
<li>转换 syntax 和 api。</li>
<li>syntax 和 api 的转换策略会根据浏览器策略改变。</li>
<li>polyfill 从core-js@3 引入。</li>
<li>安装：npm i core-js@3 -S</li>
<li>使用 Webpack 打包后的文件体积约 23kb。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单介绍一下配置项 <strong>useBuiltIns</strong> ：默认为 false，可以使用的值有 usage 和 entry</p>
<ul>
<li><code>usage</code>：不需要手动 import '@babel/polyfill'，会根据 browserlist + 业务代码使用到的新 API 按需自动加上 polyfill</li>
<li><code>entry</code>：需要手动 import '@babel/polyfill'，根据 browserlist 中浏览器版本的支持，将 polyfill 拆分引入浏览器不支持的 polyfill。这样会导致实际用不到的 polyfill 也会被打包到输出文件，导致文件比较大。</li>
<li><code>false</code>：不启用 polyfill，如果 import '@babel/polyfill', 会无视 browserlist 将所有的 polyfill 加载进来。</li>
<li>新版本的 Babel，会提示直接引入 core-js 或者 regenerator-runtime/runtime 来代替@babel/polyfill。</li>
</ul>
<p>目标浏览器：>0.25%</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d479003c439144e3b4c3e8fadc3ef5dc~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer">
目标浏览器：Chrome > 75</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abcf2513b5484282a982bf59c3d550c1~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">4.@babel/preset-env + @babel/runtime-corejs3 + @babel/plugin-transform-runtime</h3>
<ul>
<li>api转换会根据策略改变。</li>
<li>syntax转换会根据策略改变。</li>
<li>安装：npm i @babel/plugin-transform-runtime -D   @babel/runtime-corejs3 -S</li>
<li>使用 Webpack 打包后的文件体积约 26kb。</li>
</ul>
<p><strong>@babel/runtime 和 @babel/plugin-transform-runtime 的关系：</strong></p>
<ul>
<li>plugin-transform-runtime 用于<code>编译时</code>转译代码，真正的polyfill在代码<code>运行时</code>从babel/runtime里引入，所以plugin-transform-runtime 需要安装在<code>开发环境</code>，而babel/runtime安装在<code>生产环境</code>。</li>
</ul>
<p><strong>@babel/runtime 和 @babel/runtime-corejs3：</strong></p>
<ul>
<li>@babel/runtime包含：helpers、regenerator-runtime。只能处理语法。</li>
<li>@babel/runtime-corejs3包含：helpers、regenerator-runtime、core-js@3。引入core-js@3处理api。</li>
</ul>
<p><strong>根据 corejs 的选项，来选择对应的包即可：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7f01162ab014e398fd8413a28efa83f~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer">
Babel 在每个需要转换的代码前面都会插入一些 helpers 代码，这可能会导致多个文件都会有重复的 helpers 代码。@babel/plugin-transform-runtime 的 helpers: true 选项就可以把这些代码抽离出来。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"plugins"</span>: [
        [
            <span class="hljs-string">"@babel/plugin-transform-runtime"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">"helpers"</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">"regenerator"</span>: <span class="hljs-literal">false</span>
            &#125;
        ]yu
    ],
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目标浏览器：>0.25%</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2400e1114010486e98c8db4392e3b81c~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目标浏览器：Chrome > 75</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e492adc159440c84169f234e71254a~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">5.组合使用@babel/preset-env + core-js@3 + @babel/plugin-transform-runtime + @babel/runtime-corejs3</h3>
<ul>
<li>core-js 设置转译api， runtime 设置 false 不转译api。</li>
<li>runtime 转换了语法，没有转 api，core-js 转了api。</li>
<li>runtime 提取 helper 代码，减少重复代码，core-js 使用最新版本按需引入。</li>
<li>使用 Webpack 打包后的文件体积约 12kb，<code>体积最小</code>。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"plugins"</span>: [
        [
            <span class="hljs-string">"@babel/plugin-transform-runtime"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-literal">false</span>,
                <span class="hljs-attr">"helpers"</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">"regenerator"</span>: <span class="hljs-literal">false</span>
            &#125;
        ]
    ],
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目标浏览器：>0.25%</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bebc755f95fd4b31a9a3482266d52013~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目标浏览器：Chrome > 75</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792ab21dc54a4810a1045e707b6ac63a~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">6.组合使用@babel/preset-env + core-js@3 + @babel/plugin-transform-runtime + @babel/runtime-corejs3，core-js和runtime都设置转译api</h3>
<ul>
<li>runtime转了语法和api，两者不会重复转译，输出结果与配置4一致。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"plugins"</span>: [
        [
            <span class="hljs-string">"@babel/plugin-transform-runtime"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">"helpers"</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">"regenerator"</span>: <span class="hljs-literal">false</span>
            &#125;
        ]
    ],
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>,
                <span class="hljs-attr">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">总结：</h3>
<ul>
<li>个人测试的编译后体积最小的代码是配置5：使用 core-js 的 useBuiltIns 设置按需引入 polyfill 结合 @babel/plugin-transform-runtime 提取重复代码的 helper 代码。</li>
<li>官方建议的使用方式是：根据使用场景，useBuiltIns 的 polyfill 全局范围添加，@babel/plugin-transform-runtime 的 polyfill 非全局范围添加，采用一种配置即可。</li>
</ul></div>  
</div>
            