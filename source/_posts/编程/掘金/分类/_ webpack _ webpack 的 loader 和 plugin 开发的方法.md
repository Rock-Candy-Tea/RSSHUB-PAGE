
---
title: '_ webpack _ webpack 的 loader 和 plugin 开发的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44fadf45211245b0b7b41a7f6b01cbb9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 20:19:49 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44fadf45211245b0b7b41a7f6b01cbb9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>虽说不同构建工具在原理上是大同小异，但下一篇也应该写写 vite 了。</p>
</blockquote>
<h2 data-id="heading-0">Loader 和 Plugins 的区别</h2>
<p>loader 主要的是处理静态资源，而 plugins 是可以贯穿在整个 webpack 构建的周期中，他能做到 loader 做不到的事情。但是，loader 他可以用独立的运行环境，可以在本地使用一些库进行本地发发调制，而 plugins 不行，他必须编写好这个 plugin 之后在 webpack 构建中将 plugin 放在 plugins 的数组中执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44fadf45211245b0b7b41a7f6b01cbb9~tplv-k3u1fbpfcp-watermark.image" alt="web-webpack-loader-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">loader 开发的常用的开发方法</h2>
<h3 data-id="heading-2">webpack 文档 DEMO 结构分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; getOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'loader-utils'</span>;
<span class="hljs-keyword">import</span> &#123; validate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'schema-utils'</span>;
<span class="hljs-keyword">const</span> schema = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'object'</span>,
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">test</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>,
    &#125;,
  &#125;,
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = getOptions(<span class="hljs-built_in">this</span>);
  validate(schema, options, &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Example Loader'</span>,
    <span class="hljs-attr">baseDataPath</span>: <span class="hljs-string">'options'</span>,
  &#125;);
  <span class="hljs-comment">// Apply some transformations to the source...</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`export default <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(source)&#125;</span>`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>loader 实际上就是一个 js 模块，提供一个方法对原文件进行逻辑操作，处理完毕之后返回回去的一个过程。顺带提一点就是，loader 的链式调用是从后往前。</p>
<h3 data-id="heading-3">同步 loader 参数获取</h3>
<p>参数获取可以使用一个 叫 loader-utils 的 loader，使用其中的 getOptions 的方法就可以拿到传递的参数。
在 runLoaders 配置中 loaders 参照文档修改为带 options 的配置，举例加上一个对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">runLoaders(&#123;
    <span class="hljs-attr">loaders</span>: [
        <span class="hljs-comment">// path.join(__dirname, './loaders/raw-loader.js'),</span>
        &#123;
            <span class="hljs-attr">loader</span>: path.join(__dirname, <span class="hljs-string">'./loaders/raw-loader.js'</span>),
            <span class="hljs-attr">options</span>:&#123;
                <span class="hljs-attr">env</span>: <span class="hljs-string">'development'</span>,
                <span class="hljs-attr">version</span>: <span class="hljs-string">'1.0.0'</span>
            &#125;,
        &#125;
    ],
...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后使用 loader-utils 将传递的参数带出。注意，这里的 module.exports 不能使用箭头函数，否则，this 是指向了当前的作用域，就拿不到 runLoaders 里面的属性了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// npm install loader-utils -save-dev</span>
<span class="hljs-keyword">const</span> loaderUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>);

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">const</span> &#123; env, version &#125; = loaderUtils.getOptions(<span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">console</span>.log(env);
    <span class="hljs-built_in">console</span>.log(version);
    ...
&#125;;

<span class="hljs-comment">// npmjs -> https://www.npmjs.com/package/loader-utils </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">同步 loader  异常处理</h3>
<p>同步执行的情况下，处理异常错误打印的方式有两种：</p>
<p><strong>第一种</strong>：是直接使用 Error 输出错误，可以在信息内填写错误编号</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
   ...
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error:10001'</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第二种</strong>：是直接使用 this.callback ,根据参数的不同，再执行下一步或者是输出报错信息。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
...
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callback(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error:10001'</span>), source);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>this.callback 的第一个参数是 Error 时，表示异常直接报错，如果第一个参数是 null ，那就说明函数正常执行下一步返回数据, 同时也支持多个参数进行传递，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
...
<span class="hljs-keyword">const</span> params = &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">1</span> &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callback(<span class="hljs-literal">null</span>, source, params);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">异步 loader  处理</h3>
<p>使用异步获取结果需要使用 this.async() 这个方法，作为一个 callback 使用，第一个参数是判断是否错误，第二个直接传递参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
...
    <span class="hljs-keyword">const</span> callback = <span class="hljs-built_in">this</span>.async();
    fs.readFile(path.join(__dirname, <span class="hljs-string">'../src/number.txt'</span>), <span class="hljs-string">'utf-8'</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(err)&#123;
            callback(err,<span class="hljs-string">'error'</span>)
        &#125;
        callback(<span class="hljs-literal">null</span>, data);
    &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">loader 输出文件</h3>
<p>使用 emitFile 进行输出。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> loaderUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> url = loaderUtils.interpolateName(<span class="hljs-built_in">this</span>, <span class="hljs-string">'[name].[ext]'</span>, source);
    <span class="hljs-built_in">this</span>.emitFile(url, source)
    <span class="hljs-keyword">return</span> source;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">开发适用于活动的 CSS Sprites loader</h2>
<p>首先，需要使用 spritesmith 这个依赖，将多张图片和合并到一起。</p>
<h4 data-id="heading-8">第一步：读取图片 URL</h4>
<p>思路是先将 css 文件获取到，再使用正则匹配导出所有的图片地址</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> loaderUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
   <span class="hljs-keyword">const</span> images = source.match(<span class="hljs-regexp">/url\((\S*)/g</span>);
   <span class="hljs-keyword">const</span> matchedImages = [];
   <span class="hljs-keyword">if</span> (images && images.length > <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < images.length; i++) &#123;
     <span class="hljs-keyword">const</span> img = images[i].match(<span class="hljs-regexp">/url\(..(\S*)\'/</span>)[<span class="hljs-number">1</span>];
     matchedImages.push(path.join(__dirname, img));
    &#125;
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再把文件的目录提取出来，转换成一个绝对地址 push 到一个数组里面，打印出来的 matchedImages 如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  <span class="hljs-string">'/Users/../images/web-security-bg-1.jpeg'</span>,
  <span class="hljs-string">'/Users/../images/webpack-images-2.png'</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">第二步：使用 spritesmith 合并图片和 css 地址替换</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">Spritesmith.run(&#123; <span class="hljs-attr">src</span>: matchedImages&#125;, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
fs.writeFileSync(path.join(process.cwd(), <span class="hljs-string">'dist/sprite.png'</span>), result.image);
source = source.replace(<span class="hljs-regexp">/url\((\S*)/g</span>, <span class="hljs-function">(<span class="hljs-params">match</span>) =></span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">`url("dist/sprite.jpg")`</span>;
  &#125;);
  fs.writeFileSync(path.join(process.cwd(), <span class="hljs-string">'dist/index.css'</span>), source);
     callback(<span class="hljs-literal">null</span>,source); &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 dist 的目录中，就会出现一个合并好的图片同时 dist 里面还有一个已替换了 sprite 图的 css 文件 ，当然这里只是说明了一个思路，如果要完全的实现图片和样式的替换还需要考虑到背景大小，定位或者是一些边界问题，这里就不再细说了。</p>
<h2 data-id="heading-10">webpack 的 Plugin 的常用的开发方法</h2>
<h3 data-id="heading-11">webpack 文档 DEMO 结构分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack writting a plugin -> https://webpack.js.org/contribute/writing-a-plugin/</span>

<span class="hljs-comment">// A JavaScript class.</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorldPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.done.tap(<span class="hljs-string">'Hello World Plugin'</span>, <span class="hljs-function">(<span class="hljs-params">
      stats <span class="hljs-comment">/* stats is passed as an argument when done hook is tapped.  */</span>
    </span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World!'</span>);
    &#125;);
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = HelloWorldPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>plugin 实际上一个一个类，在 webpack 使用 plugin 的时候都会有 new XXplugin() 的操作，就是新建一个 plugin 的类。apply 是 plugin 在 webpack 是每一次构建的时候都会运行。</p>
<p>hooks 是 compiler 对象的一个钩子，也可以说是可以监听在某个阶段做一些什么样的事情。会掉的最后就是这个 plugin 的逻辑代码。</p>
<h3 data-id="heading-12">开发一个压缩构建资源为 zip 包的 plugin</h3>
<h4 data-id="heading-13">创建 zip 文件</h4>
<p>首先，还是先使用一个 jszip 它可以将文件压缩成一个 zip 包，使用 compiler 对象的 hooks 的 emit 钩子，生成一个文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> JSZip = <span class="hljs-built_in">require</span>(<span class="hljs-string">'jszip'</span>);
<span class="hljs-keyword">const</span> zip = <span class="hljs-keyword">new</span> JSZip();
compiler.hooks.emit.tapAsync(<span class="hljs-string">'ZipPlugin'</span>, <span class="hljs-function">(<span class="hljs-params">Compilation, callback</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> folder = zip.folder(<span class="hljs-built_in">this</span>.options.filename);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> filename <span class="hljs-keyword">in</span> Compilation.assets) &#123;
        <span class="hljs-keyword">const</span> source = Compilation.assets[filename].source();
        folder.file(filename, source)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 zip.folder 先设置 zip 包的名称， 在触发到了emit 的 tapAsunc 异步钩子的时候，处理 compilation 的内容填充到 folder 里面去。 compilation.assist 是一个目录名，遍历出文件名之后使用 source 拿到 source 在放回 folder 中。</p>
<h4 data-id="heading-14">第二步将文件输出为 zip</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">zip.generateAsync(&#123;
  <span class="hljs-attr">type</span>:<span class="hljs-string">'nodebuffer'</span>
  &#125;).then(<span class="hljs-function">(<span class="hljs-params">content</span>)=></span>&#123;
  <span class="hljs-keyword">const</span> outputPath = path.join(Compilation.options.output.path ,<span class="hljs-built_in">this</span>.options.filename + <span class="hljs-string">'.zip'</span>);
  <span class="hljs-keyword">const</span> outputRelativePath = path.relative(
    Compilation.options.output.path,
    outputPath
  )
  Compilation.assets[outputRelativePath] = <span class="hljs-keyword">new</span> RawSource(content);
    callback()
    <span class="hljs-built_in">console</span>.log(Compilation.options)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 zip.generateAsync 返回的 content 是一个 buffer ，需要使用 RawSource 将这个 buffer 转换挂到 compilation 的 assist 中 ，最后执行 callback 。</p></div>  
</div>
            