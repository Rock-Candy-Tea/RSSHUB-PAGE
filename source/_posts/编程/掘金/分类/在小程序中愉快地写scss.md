
---
title: '在小程序中愉快地写scss'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9729'
author: 掘金
comments: false
date: Sat, 08 May 2021 03:00:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=9729'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>利用webpack将sass编译成wxss插入小程序页面</p>
</blockquote>
<blockquote>
<p>公司的电商小程序项目有点年头了，一直用的原生写法，由于种种原因，没法用其他技术栈重构，每次写wxss都是很难受的，所以有了这个想法</p>
</blockquote>
<h2 data-id="heading-0">问题点1：小程序每个页面都有一个wxss文件，所以webpack打包编译如何输出多个wxss文件</h2>
<p>wepback设置多入口配置，会对应输出多出口文件。
所以项目中有多少个scss文件，就对应多少个入口。</p>
<ol>
<li>在<code>app.json</code>中定义了主包和分包的页面路径，直接遍历获取他们的目录名</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// pages and subPackages</span>
<span class="hljs-keyword">const</span> &#123; pages, subPackages &#125; = appJson

<span class="hljs-comment">// 提取主包目录名</span>
<span class="hljs-comment">// "pages/homeDelivery/index" => "pages/homeDelivery"</span>
<span class="hljs-comment">// /[^/]+(?!.*\/)/ 把最后一个斜杠后的内容去掉</span>
<span class="hljs-keyword">const</span> dirList = pages.map(<span class="hljs-function"><span class="hljs-params">page</span> =></span> page.replace(<span class="hljs-regexp">/[^/]+(?!.*\/)/</span>, <span class="hljs-string">''</span>))

<span class="hljs-comment">// 提取分包目录名</span>
<span class="hljs-comment">// "pages/paySuccess/index" => "fightGroups/pages/paySuccess/index" => "fightGroups/pages/paySuccess"</span>
subPackages.forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; pages, root &#125; = sub
  dirList.push(...pages.map(<span class="hljs-function"><span class="hljs-params">subPage</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;root&#125;</span>/<span class="hljs-subst">$&#123;subPage&#125;</span>`</span>.replace(<span class="hljs-regexp">/[^/]+(?!.*\/)/</span>, <span class="hljs-string">''</span>)))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再通过遍历目录下的文件获取所有<code>scss/sass</code>文件</p>
<ol start="2">
<li>
<p>再加上<code>components</code>组件目录，递归遍历此目录下所有文件，如果是<code>scss/sass</code>就返回</p>
</li>
<li>
<p>提取wxss文件: <code>MiniCssExtractPlugin</code></p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">plugins: [
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
    <span class="hljs-comment">// 重新定义后缀名</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].wxss'</span>
  &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">问题点2： webpack打包会默认输出一个 [name].js文件，但我们不需要</h2>
<p><code>FixStyleOnlyEntriesPlugin</code>利用这个插件，会删除webpack打包出来的<code>[name].js</code>，并且不会影响原有的js文件</p>
<h2 data-id="heading-2">问题点3：热更新</h2>
<p>开启webpack的watch功能</p>
<pre><code class="hljs language-js copyable" lang="js">watchOptions: &#123;
  <span class="hljs-comment">// 忽略除scss之外的所有文件，减轻监听压力</span>
  <span class="hljs-attr">ignored</span>: [<span class="hljs-regexp">/node_modules/</span>, <span class="hljs-string">'*.js'</span>, <span class="hljs-string">'*.css'</span>, <span class="hljs-string">'*.wxml'</span>, <span class="hljs-string">'*.wxss'</span>, <span class="hljs-string">'*.wxs'</span>, <span class="hljs-string">'*.json'</span>]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时修改scss文件，就会重新打包编译，实现热更新。
提供两个shell命令，分别用于一次性构建和热更新</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"build"</span>: <span class="hljs-string">"cross-env build_type=buildOnce webpack --config webpack.config.js"</span>,
<span class="hljs-string">"watch"</span>: <span class="hljs-string">"cross-env build_type=buildConstantly webpack --config webpack.config.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">问题点4：小程序的打包编译</h2>
<ol>
<li>添加<code>.gitignore</code>忽略<code>node_modules</code></li>
<li><code>project.config.json</code>通过<code>packOptions</code>设置打包配置，我们需要忽略<code>node_modules</code>,<code>webpack.config.js</code>,<code>package.json</code>,<code>package-lock.json</code></li>
<li><code>project.config.json</code>通过<code>packOptions</code>设置热更新，设置同上</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"packOptions"</span>: &#123;
    <span class="hljs-attr">"ignore"</span>: [
        &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"folder"</span>,
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"node_modules"</span>
        &#125;,
        &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"file"</span>,
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"webpack.config.js"</span>
        &#125;,
        &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"file"</span>,
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"package.json"</span>
        &#125;,
        &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"file"</span>,
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"package-lock.json"</span>
        &#125;
    ]
&#125;,
<span class="hljs-string">"watchOptions"</span>: &#123;
    <span class="hljs-attr">"ignore"</span>: [
        <span class="hljs-string">"webpack.config.js"</span>,
        <span class="hljs-string">"package.json"</span>,
        <span class="hljs-string">"package-lock.json"</span>,
        <span class="hljs-string">"node_modules/**/**"</span>
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">完整webpack配置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> FixStyleOnlyEntriesPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-fix-style-only-entries"</span>);
<span class="hljs-keyword">const</span> appJson = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./app.json'</span>)

<span class="hljs-keyword">const</span> baseConfig = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">watch</span>: process.env.build_type === <span class="hljs-string">'buildConstantly'</span>,
  <span class="hljs-attr">watchOptions</span>: &#123;
    <span class="hljs-comment">// 忽略除scss之外的所有文件</span>
    <span class="hljs-attr">ignored</span>: [<span class="hljs-regexp">/node_modules/</span>, <span class="hljs-string">'*.js'</span>, <span class="hljs-string">'*.css'</span>, <span class="hljs-string">'*.wxml'</span>, <span class="hljs-string">'*.wxss'</span>, <span class="hljs-string">'*.wxs'</span>, <span class="hljs-string">'*.json'</span>]
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.s(a|c)ss$/</span>,
        use: [
          MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'sass-loader'</span>
        ],
      &#125;
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> FixStyleOnlyEntriesPlugin(),
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].wxss'</span>
    &#125;)
  ]
&#125;

<span class="hljs-keyword">const</span> genExportInfo = <span class="hljs-function">(<span class="hljs-params">parseFileList</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!parseFileList.length) <span class="hljs-keyword">return</span> []
  <span class="hljs-keyword">return</span> parseFileList.map(<span class="hljs-function"><span class="hljs-params">pathInfo</span> =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">index</span>: path.resolve(__dirname, pathInfo),
      &#125;,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, path.dirname(pathInfo))
      &#125;,
      ...baseConfig,
    &#125;
  &#125;)
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>递归获取目录下的所有文件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;String&#125;</span> </span>dir 指定目录路径
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;RegExp&#125;</span> </span>suffixReg 指定后缀名正则,/^.*$/表示匹配全通过
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> </span>list 
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Array&#125;</span> </span>返回文件路径
 */</span>
<span class="hljs-keyword">const</span> recursiveFile = <span class="hljs-function">(<span class="hljs-params">dir, suffixReg = <span class="hljs-regexp">/^.*$/</span>, list = []</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> readList = fs.readdirSync(dir)
  readList.forEach(<span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
    <span class="hljs-keyword">const</span> filePath = path.join(dir, r)
    <span class="hljs-keyword">if</span> (fs.statSync(filePath).isFile()) &#123;
      <span class="hljs-keyword">const</span> fileSuffix = path.extname(filePath).slice(<span class="hljs-number">1</span>)
      suffixReg.test(fileSuffix) && list.push(filePath)
    &#125; <span class="hljs-keyword">else</span> &#123;
      recursiveFile(filePath, suffixReg, list)
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> list
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>css文件路径来源: app.json里的pages和subPackages,还有components
 */</span>
<span class="hljs-keyword">const</span> genCssPathList = <span class="hljs-function">(<span class="hljs-params">appJson</span>) =></span> &#123;
  <span class="hljs-comment">// pages and subPackages</span>
  <span class="hljs-keyword">const</span> &#123; pages, subPackages &#125; = appJson

  <span class="hljs-comment">// 提取主包目录名</span>
  <span class="hljs-comment">// "pages/homeDelivery/index" => "pages/homeDelivery"</span>
  <span class="hljs-comment">// /[^/]+(?!.*\/)/ 把最后一个斜杠后的内容去掉</span>
  <span class="hljs-keyword">const</span> dirList = pages.map(<span class="hljs-function"><span class="hljs-params">page</span> =></span> page.replace(<span class="hljs-regexp">/[^/]+(?!.*\/)/</span>, <span class="hljs-string">''</span>))

  <span class="hljs-comment">// 提取分包目录名</span>
  <span class="hljs-comment">// "pages/paySuccess/index" => "fightGroups/pages/paySuccess/index" => "fightGroups/pages/paySuccess"</span>
  subPackages.forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; pages, root &#125; = sub
    dirList.push(...pages.map(<span class="hljs-function"><span class="hljs-params">subPage</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;root&#125;</span>/<span class="hljs-subst">$&#123;subPage&#125;</span>`</span>.replace(<span class="hljs-regexp">/[^/]+(?!.*\/)/</span>, <span class="hljs-string">''</span>)))
  &#125;)

  <span class="hljs-keyword">const</span> needToParseList = []

  <span class="hljs-comment">// 提取components所有文件</span>
  needToParseList.push(...recursiveFile(path.resolve(__dirname, <span class="hljs-string">'./components'</span>), <span class="hljs-regexp">/s(a|c)ss/</span>))
  
  dirList.forEach(<span class="hljs-function"><span class="hljs-params">dir</span> =></span> &#123;
    needToParseList.push(...recursiveFile(path.resolve(__dirname, dir), <span class="hljs-regexp">/s(a|c)ss/</span>))
  &#125;)

  <span class="hljs-keyword">return</span> needToParseList
&#125;

<span class="hljs-built_in">module</span>.exports = genExportInfo(genCssPathList(appJson))

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            