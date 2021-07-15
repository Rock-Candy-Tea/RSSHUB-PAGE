
---
title: 'webpack试练03'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=599'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 07:48:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=599'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、tree shaking</h3>
<ul>
<li>提到tree shaking就要说到mode</li>
<li>当mode为develoment|none时，未使用到的模块也会被被打包进来</li>
<li>当mode为production时，未使用到的模块则不会被打包进了</li>
<li>当然希望打包进来的也是有方法的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">在package.json文件中添加副作用列表，列表内的不管用没用到，都会打包进来
<span class="hljs-string">"sideEffects"</span>: [
  <span class="hljs-string">"**/*.css"</span>,
  <span class="hljs-string">"**/*.scss"</span>,
  <span class="hljs-string">"./esnext/index.js"</span>,
  <span class="hljs-string">"./esnext/configure.js"</span>
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2、Scope Hoisting</h3>
<ul>
<li>未开启时存在的问题：打包后的代码存在大量的闭包代码，导致体积增大，作用域变多，内存开销大</li>
<li>开启后：会被webpack加上一层包裹 import会被编译成__webpack_require，打包出IIFE(匿名闭包)</li>
<li>原理：将所有模块的代码按顺序放在一个函数的作用域里，然后适当的重命名一些变量以防止变量名冲突，以此来减少函数的声明和内存的开销</li>
<li>当mode为develoment|none时</li>
</ul>
<pre><code class="copyable">// 可以手动开启
new webpack.optimize.ModuleConcatenationPlugin(),
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当mode为production时，默认开启</li>
<li>仅支持es6语法</li>
</ul>
<h3 data-id="heading-2">3、代码分割及动态import</h3>
<ul>
<li>动态引入import需babel插件的支持</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"@babel/preset-env"</span>], <span class="hljs-string">"@babel/preset-react"</span>],
  <span class="hljs-string">"plugins"</span>: [<span class="hljs-string">"@babel/plugin-syntax-dynamic-import"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> logo <span class="hljs-keyword">from</span> <span class="hljs-string">"../../../images/loaders.png"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">Text</span>: <span class="hljs-literal">null</span>,
    &#125;;
  &#125;
  loadComponent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 在这里就可以动态引入了，这一个text组件也会单独被打包出来，当点击时则会动态加载</span>
    <span class="hljs-keyword">import</span>(<span class="hljs-string">"./text.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">Text</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">Text</span>: Text.default,
      &#125;);
    &#125;);
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; Text &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"search"</span>></span>
        &#123;Text ? <span class="hljs-tag"><<span class="hljs-name">Text</span> /></span> : "11"&#125;
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.loadComponent&#125;</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;logo&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4、在webpack中使用ESLint</h3>
<ul>
<li>创建.eslintrc.js文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 所使用的及继承的lint包都需要安装 </span>
  <span class="hljs-string">"parser"</span>: <span class="hljs-string">"babel-eslint"</span>,
  <span class="hljs-string">"extends"</span>: <span class="hljs-string">"airbnb"</span>,
  <span class="hljs-comment">// "rules": &#123;</span>
  <span class="hljs-comment">//     "semi": "error"</span>
  <span class="hljs-comment">// &#125;,</span>
  <span class="hljs-string">"env"</span>: &#123;
    <span class="hljs-string">"browser"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"node"</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack配置修改</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
        use: [
          <span class="hljs-string">"babel-loader"</span>,
          <span class="hljs-string">"eslint-loader"</span>
        ],
      &#125;,
    ]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>想要详细了解请看官网配置：<a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.bootcss.com/" ref="nofollow noopener noreferrer">eslint.bootcss.com/</a></li>
</ul>
<h3 data-id="heading-4">5、webpack打包组件或基础库</h3>
<p>说来惭愧，入行两年多了，竟然没注册过npm，自己连个简单的组件库都没有</p>
<ul>
<li>看代码吧</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">--webpack 配置
<span class="hljs-keyword">const</span> TerserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"terser-webpack-plugin"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-string">"larger-number"</span>: <span class="hljs-string">"./src/index.js"</span>,
    <span class="hljs-string">"larger-number.min"</span>: <span class="hljs-string">"./src/index.js"</span>,
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].js"</span>,
    <span class="hljs-comment">// 打包库的名字</span>
    <span class="hljs-attr">library</span>: <span class="hljs-string">"largeNumber"</span>,
    <span class="hljs-comment">// 支持  amd cmd es6 script标签引入</span>
    <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">"umd"</span>,
    <span class="hljs-attr">libraryExport</span>: <span class="hljs-string">"default"</span>,
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-comment">// mode: production 时默认使用的压缩插件,</span>
      <span class="hljs-keyword">new</span> TerserPlugin(&#123;
        <span class="hljs-attr">include</span>: <span class="hljs-regexp">/\.min\.js$/</span>,
      &#125;),
    ],
  &#125;,
&#125;;

--index 使用打包文件
<span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">"production"</span>) &#123;
  <span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./dist/larger-number.min.js"</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./dist/larger-number.js"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>github地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F838216870%2Fwebpack_study" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/838216870/webpack_study" ref="nofollow noopener noreferrer">github.com/838216870/w…</a></p>
<p>不断学习中，有想沟通交流的欢迎评论留言；</p></div>  
</div>
            