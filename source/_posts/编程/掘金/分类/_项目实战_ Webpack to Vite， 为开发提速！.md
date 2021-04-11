
---
title: '_项目实战_ Webpack to Vite， 为开发提速！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f8eec2e02040298737ced7b9e1eb2e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 04:34:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f8eec2e02040298737ced7b9e1eb2e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="Webpack to Vite" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f8eec2e02040298737ced7b9e1eb2e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">背景</h1>
<p>最近，就 <code>前端开发过程中的痛点及可优化项</code> 做了一次收集。  其中，<code>构建耗时、项目编译速度慢</code> 的字眼出现了好几次。</p>
<p>随着业务的快速发展，我们很多项目的体积也快速膨胀。 随之而来的， 就是打包变慢等问题。</p>
<p><code>提升研发效率</code>，是技术人永恒的追求。</p>
<p>我们项目也有启动慢的问题，同事也提到过几次。 刚好我之前也做过类似的探索和优化， 于是就借这个机会，改造一下项目， <code>解决启动耗时的问题</code>。</p>
<p>于昨天下午(2021.4.7 23:00)， 成功嵌入 Vite, 项目启动时间由约 <code>190s => 20s</code>, 热更新时间缩短为 <code>2s</code>。</p>
<p>中间踩了一些坑， 好在最后爬出来了， 相关技术要点都会在下文中呈现。</p>
<blockquote>
<p>FBI Warning： 以下文字，只是我结合自己的实际项目, 总结出来的一些浅薄的经验， 如有错误，欢迎指正 :)</p>
</blockquote>
<p>今天的主要内容：</p>
<ul>
<li><code>为什么 Vite 启动这么快</code></li>
<li><code>我的项目如何植入 Vite</code></li>
<li><code>我在改造过程中遇到的问题</code></li>
<li><code>关于 Vite 开发、打包上线的一些思考</code></li>
<li><code>相关代码和结论</code></li>
</ul>
<h1 data-id="heading-1">正文</h1>
<h2 data-id="heading-2">为什么 Vite 启动这么快</h2>
<p>底层实现上， Vite 是基于 esbuild 预构建依赖的。</p>
<p>esbuild 使用 go 编写，并且比以 js 编写的打包器预构建依赖, 快 10 - 100 倍。</p>
<p>因为 js 跟 go 相比实在是太慢了，js 的一般操作都是毫秒计，go 则是纳秒。</p>
<p>另外， 两者的<code>启动方式</code>也有所差异。</p>
<h3 data-id="heading-3">webpack 启动方式</h3>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baf656258c7d49ab8bfd8134c9852041~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">Vite 启动方式</h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0905f21e382a4b07aa87ff0820dcd75d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Webpack 会<code>先打包</code>，然后启动开发服务器，请求服务器时直接给予打包结果。</p>
<p>而 Vite 是<code>直接启动</code>开发服务器，请求哪个模块再对该模块进行<code>实时编译</code>。</p>
<p>由于现代浏览器本身就支持 ES Module，会自动向依赖的 Module 发出请求。</p>
<p>Vite 充分利用了这一点，将开发环境下的模块文件，就作为浏览器要执行的文件，而不是像 W ebpack 那样进行<code>打包合并</code>。</p>
<p>由于 Vite 在启动的时候<code>不需要打包</code>，也就意味着<code>不需要分析模块的依赖</code>、<code>不需要编译</code>。
因此启动速度非常快。当浏览器请求某个模块时，再根据需要对模块内容进行编译。</p>
<p>这种按需动态编译的方式，极大的缩减了编译时间，项目越复杂、模块越多，vite 的优势越明显。</p>
<p>在 HMR（热更新）方面，当改动了一个模块后，仅需让浏览器重新请求该模块即可，不像webpack那样需要把该模块的相关依赖模块全部编译一次，效率更高。</p>
<p>从实际的开发体验来看， 在 Vite 模式下， 开发环境可以瞬间启动， 但是等到页面出来， 要等一段时间。</p>
<h2 data-id="heading-5">我的项目如何植入 Vite</h2>
<h3 data-id="heading-6">新项目</h3>
<p>创建一个 Vite 新项目就比较简单：</p>
<pre><code class="hljs language-css copyable" lang="css">yarn create <span class="hljs-keyword">@vitejs</span>/app
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/236d7f06dd6d4559a26180bf84baaf7f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9c258d397e453cbb390a7b16bb456b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>生成好之后， 直接启动就可以了：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1de5ccd6b4d04d39b6789fcb6e30d674~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">已有项目</h3>
<p>已有项目的迁移， 稍微繁琐一些。</p>
<p>首先， 加入 Vite 的相关配置。 这里我使用了一个 cli 工具： <code>wp2vite</code>.</p>
<p>安装好之后， 直接执行：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dc2126cc943cdb9c2d9da5cf0beff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这一步， 会自动生成 Vite 的配置文件，并引入相关的依赖。</p>
<p>把依赖安装一下， 启动就可以了。</p>
<p>如果没有意外的话， 你会<code>收获一堆报错</code>。</p>
<p>恭喜你，进入开心愉快的踩坑环节。</p>
<h2 data-id="heading-8">我在改造过程中遇到的问题</h2>
<h3 data-id="heading-9">1. alias 错误</h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ea59f7ea41140a1892845cfa520feef~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>项目代码里配置了一些别名，vite 无法识别，所以需要在vite 里面也配置 alias：</p>
<pre><code class="hljs language-js copyable" lang="js">  resolve: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(__dirname, <span class="hljs-string">'src'</span>),
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2. 无法识别 less 全局变量</h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e5b3baee6140aa9209737c64eacbb3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>解决办法：</p>
<p>把自定义的全局变量从外部注入即可， 直接在 <code>vite.config.js</code> 的 css 选项中加入：</p>
<pre><code class="hljs language-js copyable" lang="js">  css: &#123;
    <span class="hljs-attr">preprocessorOptions</span>: &#123;
      <span class="hljs-attr">less</span>: &#123;
        <span class="hljs-attr">modifyVars</span>: &#123;
          <span class="hljs-attr">hack</span>: <span class="hljs-string">`true;@import '<span class="hljs-subst">$&#123;resolve(<span class="hljs-string">'./src/vars.less'</span>)&#125;</span>';`</span>,
          ...themeVariables,
        &#125;,
        <span class="hljs-attr">javascriptEnabled</span>: <span class="hljs-literal">true</span>,
      &#125;,
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3. Uncaught Error: Target container is not a DOM element.</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e89bca499b614357ba709372d3691404~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根元素未找到。</p>
<p>原因是： 默认生成的 index.html 中：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>id 是 root, 而逻辑中的是<code>#app</code>, 这里直接改成 <code>id=app</code> 即可。</p>
<h3 data-id="heading-12">4. typings 文件找不到</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/006cfc91a1e34d38b2d7bba9e1be4a1b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>typings 文件未找到</code>。</p>
<p>这个错误， 乍一看， 一头雾水。</p>
<p>进去看一下源代码和编译后的代码：</p>
<p>源代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fda34d1914ff4b6fb7ea8cb854c13e1c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>编译后：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6b150dc4294db8a7ef803419a1ba49~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/891217cab1ec4c219668e2d380db335a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>typings 文件这不是好好的在这吗， 怎么就找不到？</p>
<p>想了一下： Vite 不知道 typeings 文件是不需要被编译的，需要告诉编译器不编译这个文件。</p>
<p>最后在 TS 官方文档里找到了答案：</p>
<p><a href="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html" target="_blank" rel="nofollow noopener noreferrer">www.typescriptlang.org/docs/handbo…</a></p>
<blockquote>
<p>Type-Only Imports and Export</p>
</blockquote>
<blockquote>
<p>This feature is something most users may never have to think about; however, if you’ve hit issues under --isolatedModules, TypeScript’s transpileModule API, or Babel, this feature might be relevant.</p>
</blockquote>
<blockquote>
<p>TypeScript 3.8 adds a new syntax for type-only imports and exports.</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> type &#123; SomeThing &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./some-module.js"</span>;
<span class="hljs-keyword">export</span> type &#123; SomeThing &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要单独引入types, 于是把代码改为：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f89636e60294ce69486a3d52e9ca802~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>同时要注意， 如果一个文件有有多个导出， 也要分开引入：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/185aaabae8e944c7a464182bbe69fb55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>唯一痛苦的是: 全局都需要改一遍， 体力活。</p>
<p>至此，typeings 问题完美解决。</p>
<h3 data-id="heading-13">5. 无法识别 svg</h3>
<p>我们在使用 svg 作为图标组件的时候， 一般是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Icon <span class="hljs-keyword">from</span> <span class="hljs-string">'@ant-design/icons'</span>;
<span class="hljs-keyword">import</span> ErrorSvg <span class="hljs-keyword">from</span> <span class="hljs-string">'@/assets/ico_error.svg'</span>;

<span class="hljs-keyword">const</span> ErrorIcon = <span class="hljs-function">(<span class="hljs-params">props: any</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Icon</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;ErrorSvg&#125;</span> /></span></span>;

<span class="hljs-comment">// ...</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ErrorIcon</span> /></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器报错：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2dcfd5638a245bc9eb2af2f19f1206c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">error occurred <span class="hljs-keyword">in</span> the <<span class="hljs-regexp">/src/</span>assets/ico_error.svg> component
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显的看到， 这里是把<code>文件路径</code>作为组件了。</p>
<p>现在要做的是：把这个文件路径， 换成可以识别的组件。</p>
<p>搜索一番， 找到了个插件： <code>vite-plugin-react-svg</code></p>
<p>加入配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reactSvgPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vite-plugin-react-svg'</span>);

plugins: [
  reactSvgPlugin(),
],
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> MyIcon <span class="hljs-keyword">from</span> <span class="hljs-string">'./svgs/my-icon.svg?component'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">MyIcon</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是： 引入的 svg 文件需要加 <code>?component</code> 作为后缀。</p>
<p>看了一下源码， 这个后缀是用来作为标识符的，</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6b655272a34cbcbeb2a37ed05292bf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果后缀匹配上是<code>component</code>,  就解析文件， 并缓存， 最后返回结果：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/109b28b0d8f7487cb98a7c72be8de8ee~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>知道原理之后， 就需要把全部的 <code>.svg</code> => <code>.svg?component</code>。</p>
<p>vscode 一键替换就可以， 不过注意别把 node_module 里面的也替换了。</p>
<h3 data-id="heading-14">6. global 未定义</h3>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce4986a5ff944839249519ad620c8c6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>global</code> 是 Node里面的变量， 会在客户端报错 ？</p>
<p>一层层看下去， 原来是引入的第三方包使用了global。</p>
<p>看 vite 文档里提到了 Client Types:</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c53c90dcb484c9dae84d0deae966116~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>追加到 <code>tsconfig</code> 里面：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"types"</span>: [<span class="hljs-string">"node"</span>, <span class="hljs-string">"jest"</span>, <span class="hljs-string">"vite/client"</span>],
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后， 并没有什么乱用。。。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e3b386674954a878e9addbc0517986e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>没办法， 只得祭出 <code>window</code> 大法。</p>
<p>在入口index.tsx 里面加上：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> any).global = <span class="hljs-built_in">window</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新， 好了。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ab31292dce4ef99e64dab43e371d08~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">7. [未解决] 替代HtmlWebpackPlugin</h3>
<p>还需要注入一些外部变量， 修改入口html, favicon, title 之类。</p>
<p>找到一个插件： <code>vite-plugin-singlefile</code></p>
<p>不过并没有什么用。</p>
<p>有了解的同学请留言赐教。</p>
<p>至此， 整个app 已经能在本地跑起来了， build 也没问题。</p>
<h3 data-id="heading-16">7. 线上打包构建时， 内存溢出</h3>
<p>本地能跑起来， 打包也没问题， 后面当然是放到线上跑一跑啦。</p>
<p>立刻安排！</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b15302c6592f4279825996ca12604502~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>内存不足， 我就给你加点：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbb437268fc84268ae6e341ac4791701~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/422e0c059733436ba9edc22d54858666~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>搞定！</p>
<p><img alt="unnamed.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bafe5b855ee46baaaf5e053f6f09bf4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">关于 Vite 开发、打包上线的一些思考</h2>
<p>从实际使用来看， vite 在一些功能上还是无法完全替代 webpack。</p>
<p>毕竟是后起之秀， 相关的生态还需要持续完善。</p>
<p>个人认为，目前一种比较稳妥的方式是：</p>
<ul>
<li>保留 webpack dev & build 的能力， <code>vite 仅作为开发的辅助</code></li>
</ul>
<p>等相关工具再完善一些， 再考虑完全迁移过来。</p>
<h2 data-id="heading-18">相关代码和结论</h2>
<h3 data-id="heading-19">一个完整的 Vite demo</h3>
<p>仓库地址： <a href="https://github.com/beMySun/react-hooks-i18n-template/tree/test-wp2vite" target="_blank" rel="nofollow noopener noreferrer">github.com/beMySun/rea…</a></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19b62826179243d88aeaf5d5e5fbda77~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">业务项目的 vite.config.js 完整配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>;
<span class="hljs-keyword">import</span> legacyPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-legacy'</span>;
<span class="hljs-keyword">import</span> &#123; resolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> lessToJS = <span class="hljs-built_in">require</span>(<span class="hljs-string">'less-vars-to-js'</span>);
<span class="hljs-keyword">const</span> themeVariables = lessToJS(fs.readFileSync(resolve(__dirname, <span class="hljs-string">'./src/antd-custom.less'</span>), <span class="hljs-string">'utf8'</span>));
<span class="hljs-keyword">const</span> reactSvgPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vite-plugin-react-svg'</span>);

<span class="hljs-comment">// https://cn.vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">base</span>: <span class="hljs-string">'./'</span>,
  <span class="hljs-attr">root</span>: <span class="hljs-string">'./'</span>,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'react-native'</span>: <span class="hljs-string">'react-native-web'</span>,
      <span class="hljs-string">'@'</span>: resolve(__dirname, <span class="hljs-string">'src'</span>),
    &#125;,
  &#125;,
  <span class="hljs-attr">define</span>: &#123;
    <span class="hljs-string">'process.env.REACT_APP_IS_LOCAL'</span>: <span class="hljs-string">'\'true\''</span>,
    <span class="hljs-string">'window.__CID__'</span>: <span class="hljs-built_in">JSON</span>.stringify(process.env.cid || <span class="hljs-string">'id'</span>),
  &#125;,
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">8080</span>,
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'https://stoku.test.shopee.co.id/'</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">cookieDomainRewrite</span>: &#123;
          <span class="hljs-string">'stoku.test.shopee.co.id'</span>: <span class="hljs-string">'localhost'</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-attr">build</span>: &#123;
    <span class="hljs-attr">target</span>: <span class="hljs-string">'es2015'</span>,
    <span class="hljs-attr">minify</span>: <span class="hljs-string">'terser'</span>,
    <span class="hljs-attr">manifest</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">outDir</span>: <span class="hljs-string">'build'</span>,
    <span class="hljs-attr">rollupOptions</span>: &#123;&#125;,
  &#125;,
  <span class="hljs-attr">esbuild</span>: &#123;&#125;,
  <span class="hljs-attr">optimizeDeps</span>: &#123;&#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// viteSingleFile(&#123;</span>
    <span class="hljs-comment">//   title: 'dynamic title', // doesn't work</span>
    <span class="hljs-comment">// &#125;),</span>
    reactSvgPlugin(),
    reactRefresh(),
    legacyPlugin(&#123;
      <span class="hljs-attr">targets</span>: [
        <span class="hljs-string">'Android > 39'</span>,
        <span class="hljs-string">'Chrome >= 60'</span>,
        <span class="hljs-string">'Safari >= 10.1'</span>,
        <span class="hljs-string">'iOS >= 10.3'</span>,
        <span class="hljs-string">'Firefox >= 54'</span>,
        <span class="hljs-string">'Edge >= 15'</span>,
      ],
    &#125;),
    <span class="hljs-comment">// vitePluginImp(&#123;</span>
    <span class="hljs-comment">//   libList: [</span>
    <span class="hljs-comment">//     &#123;</span>
    <span class="hljs-comment">//       libName: 'antd',</span>
    <span class="hljs-comment">//       style: (name) => `antd/es/$&#123;name&#125;/style`,</span>
    <span class="hljs-comment">//     &#125;,</span>
    <span class="hljs-comment">//   ],</span>
    <span class="hljs-comment">// &#125;),</span>
  ],
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">preprocessorOptions</span>: &#123;
      <span class="hljs-attr">less</span>: &#123;
        <span class="hljs-attr">modifyVars</span>: &#123;
          <span class="hljs-attr">hack</span>: <span class="hljs-string">`true;@import '<span class="hljs-subst">$&#123;resolve(<span class="hljs-string">'./src/vars.less'</span>)&#125;</span>';`</span>,
          ...themeVariables,
        &#125;,
        <span class="hljs-attr">javascriptEnabled</span>: <span class="hljs-literal">true</span>,
      &#125;,
    &#125;,
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">最后</h1>
<p>使用 Vite 能大幅缩短项目构建时间，提升开发效率。</p>
<p>不过也要结合项目的实际情况，合理取舍。</p>
<p>对于我的这个项目而言，把 Vite 作为辅助开发的一种方式，还是挺有用的。</p>
<p>期待 Vite 能继续完善，为研发提效。</p>
<p>好了， 内容大概就这么多， 希望对大家有所帮助。</p>
<p>才疏学浅，如有错误， 欢迎指正。</p>
<p>谢谢。</p>
<p>最后，如果觉得内容有帮助， 可以关注下我的公众号（前端皮小蛋），掌握最新动态，一起学习！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            