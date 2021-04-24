
---
title: 'TS 编译工具！从 ts-loader 到 Babel'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=211'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 02:52:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=211'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ts-loader</h2>
<p>这是用于 <code>webpack</code> 的 <code>TypeScript</code> 加载器，将 <code>TypeScript</code> 编译成 <code>JavaScript</code>。</p>
<p><code>ts-loader</code> 在内部是调用了 <code>TypeScript</code> 的官方编译器 -- <code>tsc</code>。所以，<code>ts-loader</code> 和 <code>tsc</code> 是共享 <code>tsconfig.json</code>。</p>
<h3 data-id="heading-1">安装</h3>
<pre><code class="copyable">yarn add ts-loader --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>or</p>
<pre><code class="copyable">npm install ts-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果还没有安装 <code>TypeScript</code>，你需要先安装一下：</p>
<pre><code class="copyable">yarn add typescript --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>or</p>
<pre><code class="copyable">npm install typescript --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">开始</h3>
<p>正常使用 <code>webpack</code> 即可。</p>
<h3 data-id="heading-3">Options</h3>
<p>有两种类型的 <code>Options</code>：<code>TypeScript options</code>（也称为 “编译器 options” ）和 <code>loader options</code>。<code>TypeScript options</code> 应该通过 <code>tsconfig.json</code> 文件设置。<code>loader options</code> 可以通过 webpack 配置中的 options 属性指定：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.tsx?$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'ts-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">transpileOnly</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 只做语言转换，而不做类型检查</span>
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>transpileOnly</code> 快速构建一个项目。</p>
<ul>
<li>
<p><code>transpileOnly: false</code>
语言转换 + 类型检查 = 3290 ms</p>
<pre><code class="copyable">> webpack --mode production --config ./build/webpack.config.js

clean-webpack-plugin: options.output.path not defined. Plugin disabled...
asset index.html 327 bytes [emitted]
asset app.js 89 bytes [emitted] [minimized] (name: main)
./src/index.ts 102 bytes [built] [code generated]
webpack 5.27.2 compiled successfully in 3290 ms
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>transpileOnly: true</code>
only 语言转换 = 598 ms</p>
<pre><code class="copyable">> webpack --mode production --config ./build/webpack.config.js

clean-webpack-plugin: options.output.path not defined. Plugin disabled...
asset index.html 327 bytes [compared for emit]
asset app.js 89 bytes [compared for emit] [minimized] (name: main)
./src/index.ts 102 bytes [built] [code generated]
webpack 5.27.2 compiled successfully in 598 ms
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>transpileOnly: true</code> + <code>fork-ts-checker-webpack-plugin</code>
<code>transpileOnly: true</code> 配合插件 <code>fork-ts-checker-webpack-plugin</code>，可以补全类型检查的功能。</p>
<pre><code class="copyable">npm i fork-ts-checker-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ForkTsCheckerWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fork-ts-checker-webpack-plugin"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">plugins</span>:[
    ...
    <span class="hljs-keyword">new</span> ForkTsCheckerWebpackPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，你的项目中有类型错误，编译就会报错。</p>
<p>编译通过耗时：2289 ms。</p>
<pre><code class="copyable">> webpack --mode production --config ./build/webpack.config.js

clean-webpack-plugin: options.output.path not defined. Plugin disabled...
asset index.html 327 bytes [compared for emit]
asset app.js 89 bytes [emitted] [minimized] (name: main)
./src/index.ts 102 bytes [built] [code generated]
webpack 5.27.2 compiled successfully in 2289 ms
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-4">awesome-typescript-loader</h2>
<p><code>awesome-typescript-loader</code> 的创建主要是为了加快项目中的编译速度。</p>
<p>与<code>ts-loader</code>的主要区别：</p>
<ul>
<li>更适合与 <code>Babel</code> 集成，使用 <code>Babel</code> 的转义和缓存。</li>
<li>不需要安装独立的插件，就可以把类型检查放在独立进程中。</li>
</ul>
<h3 data-id="heading-5">安装</h3>
<pre><code class="copyable">npm install awesome-typescript-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.tsx?$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'awesome-typesscript-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">transpileOnly</span>: <span class="hljs-literal">false</span>
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">跑一下</h3>
<ul>
<li>
<p><code>transpileOnly: false</code></p>
<pre><code class="copyable">webpack 5.27.2 compiled successfully in 3392 ms
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>transpileOnly: true</code></p>
<pre><code class="copyable">webpack 5.27.2 compiled successfully in 2411 ms

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>transpileOnly: true</code> + 自带插件 <code>CheckerPlugin</code></p>
<pre><code class="copyable">webpack 5.27.2 compiled successfully in 2529 ms
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-7">ts-loader 与 awesome-typescript-loader 编译时间对比</h3>























<table><thead><tr><th align="center">loader</th><th align="center">默认配置</th><th align="center">transpileOnly</th><th align="center">transpileObly + 类型检查进程</th></tr></thead><tbody><tr><td align="center">ts-loader</td><td align="center">3200+</td><td align="center">600</td><td align="center">2200+</td></tr><tr><td align="center">awesome-typescript-loader</td><td align="center">3300+</td><td align="center">2400+</td><td align="center">2500+ (类型检查有疏漏)</td></tr></tbody></table>
<h2 data-id="heading-8">Babel</h2>
<p>为什么有了 <code>Typescript</code>，还需要 <code>Babel</code>？看一下对比：</p>























<table><thead><tr><th align="center"></th><th align="center">编译能力</th><th align="center">类型检查</th><th align="center">插件</th></tr></thead><tbody><tr><td align="center">tsc</td><td align="center">ts(x),js(x) --> es 3/5/6...</td><td align="center">有</td><td align="center">无</td></tr><tr><td align="center">Babel</td><td align="center">ts(x),js(x) --> es 3/5/6...</td><td align="center">无</td><td align="center">丰富</td></tr></tbody></table>
<ul>
<li>
<p>Babel 7 之前，是不支持 TS 的</p>
<p>编译流程是这样的：<code>TS > TS 编译器 > JS > Babel > JS (再次)</code></p>
</li>
<li>
<p>Babel 7</p>
<p>实现了“只有一个 Javascript 编译器” 的梦想！通过允许 Babel 作为唯一的编译器来工作，就再也没必要利用一些复杂的 Webpack 魔法来管理、配置或者合并两个编译器。</p>
</li>
</ul>
<h3 data-id="heading-9">Babel 是如何处理 TypeScript 的？</h3>
<p>它移除了 <code>TypeScript</code>。</p>
<p>是的，它将 <code>TypeScript</code> 全部转换为常规 <code>JavaScript</code>，然后再一如既往的操作。</p>
<p><code>Babel</code> 为什么在编译过程中剥离 <code>TypeScript</code>？</p>
<ol>
<li>
<p>基于 <code>Babel</code> 的优秀的缓存和单文件散发架构，<code>Babel</code> + <code>TypeScript</code> 的组合套餐会提供了更快的编译。</p>
</li>
<li>
<p><strong>而 类型检查 呢？</strong> 那只在当你准备好的时候进行。</p>
</li>
</ol>
<h3 data-id="heading-10">创建一个 babel 工程</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  ...
  <span class="hljs-comment">// 指定输出文件 dist，指定扩展名 "ts,tsx"</span>
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"babel src --out-dir dist --extensions \".ts,.tsx\""</span>
  &#125;,
  ...
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@babel/cli"</span>: <span class="hljs-string">"^7.13.16"</span>,
    <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.13.16"</span>,
    <span class="hljs-attr">"@babel/plugin-proposal-class-properties"</span>: <span class="hljs-string">"^7.13.0"</span>,  <span class="hljs-comment">// 支持类属性</span>
    <span class="hljs-attr">"@babel/plugin-proposal-object-rest-spread"</span>: <span class="hljs-string">"^7.13.8"</span>, <span class="hljs-comment">// 支持剩余扩展操作符</span>
    <span class="hljs-attr">"@babel/preset-env"</span>: <span class="hljs-string">"^7.13.15"</span>,
    <span class="hljs-attr">"@babel/preset-typescript"</span>: <span class="hljs-string">"^7.13.0"</span> <span class="hljs-comment">// 编译 ts 文件</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .babellrc</span>
&#123;
  <span class="hljs-attr">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>, <span class="hljs-string">"@babel/preset-typescript"</span>],
  <span class="hljs-attr">"plugins"</span>: [
    <span class="hljs-string">"@babel/plugin-proposal-class-properties"</span>,
    <span class="hljs-string">"@babel/plugin-proposal-object-rest-spread"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/index.ts</span>
<span class="hljs-comment">// 类的属性、剩余扩展操作符，正好对应两个插件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-keyword">let</span> &#123; x, y, ...z &#125; = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">a</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">5</span> &#125;;
<span class="hljs-keyword">let</span> obj = &#123; x, y, ...z &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm run build

> babel src --out-dir dist --extensions ".ts,.tsx"

Successfully compiled 1 file with Babel (632ms).
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">结合 <code>TypeScript</code></h4>
<p>此时，只具备编译功能，再安装 <code>Typescript</code> 补全类型检查功能。</p>
<pre><code class="copyable">npm i typescript -D
tsc --init
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// tsconfig.json</span>
&#123;
  ...
  <span class="hljs-attr">"compilerOptions"</span>:&#123;
    <span class="hljs-attr">"noEmit"</span>:<span class="hljs-literal">true</span> <span class="hljs-comment">// 不输出文件，只做类型检查</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置一下脚本</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  ...
  <span class="hljs-attr">"script"</span>:&#123;
    ...
    <span class="hljs-attr">"check-type"</span>: <span class="hljs-string">"tsc --watch"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要新开一个 terminal，跑 <code>npm run check-type</code>，就 ok 。</p>
<h3 data-id="heading-12"><del>有四种语法</del>，有两种语法，Babel 无法编译</h3>
<ul>
<li>
<p>常量枚举</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> <span class="hljs-built_in">enum</span> A &#123;
  X,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>历史遗留风格的 <code>import/export</code> 语法</p>
<p><code>import foo = require(...)</code> 和 <code>export = foo</code>。</p>
</li>
<li>
<p><del><code>namespace</code> 命名空间</del>:</p>
<p>从 v7.6.0 起，支持 TypeScript 命名空间的编译。</p>
</li>
<li>
<p><del>类型断言</del></p>
<p>支持 <code>as</code> 方式</p>
</li>
</ul>
<h2 data-id="heading-13">如何选择 TypeScript 编译工具</h2>
<ul>
<li>如果没有使用 <code>Babel</code>，首选 <code>TypeScript</code> 自带编译器（配合 <code>ts-loader</code> 使用）</li>
<li>如果项目中有 <code>Babel</code>，安装 <code>@babel/preset-typescript</code>，配合 <code>tsc</code> 做类型检查。</li>
<li>两种编译器不要混用。</li>
</ul>
<p>End.</p></div>  
</div>
            