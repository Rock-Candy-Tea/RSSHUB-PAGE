
---
title: 'npm file方式引入公共包遇到的几个坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc4ece8125d43029a3d1c0c2e0bf7f9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 01:52:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc4ece8125d43029a3d1c0c2e0bf7f9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fmilugloomy%2Farticle%2Fdetails%2F103187370" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/milugloomy/article/details/103187370" ref="nofollow noopener noreferrer">《前端多个vue项目公共组件的三种方法（推荐npm file引入）》</a>这一篇里讲了npm通过file方式引入公共包的方法，但在实际运用中，会遇到不少坑，这里就讲述笔者遇到的2个问题并给出解决方案。</p>
<h3 data-id="heading-1">问题一</h3>
<p>通过file方式引入的包，npm不会自动安装该包的依赖。
例：项目A通过file方式引入了包B，如下所示。在
<strong>项目A的package.json：</strong></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"A"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"B"</span>: <span class="hljs-string">"file:../B"</span>
  &#125;
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>项目B的package.json：</strong></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"B"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"axios"</span>: <span class="hljs-string">"^0.19.2"</span>
  &#125;
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此在项目A中执行npm install时，不会安装axios包，node_modules中只有一个通过软链接引入的B。</p>
<h4 data-id="heading-2">解决方案</h4>
<p>主要思路：</p>
<ul>
<li>增加一个webpack插件，DepPlugin，在entryOption hook，也就是webpack刚处理完配置项之后，执行插件。</li>
<li>读取主项目package.json中dependencies中所有依赖，读取所有file引入npm包中dependencies中的依赖和版本号，两者取差集，也就是在file引入npm包中依赖的但主项目中没有的。</li>
<li>一次性安装上述所得的所有依赖，执行<code>npm install a@1.0 b@2.1 c@3.2 --no-save</code>（a b c为依赖包名）。</li>
</ul>
<p>以下是代码：
<strong>vue.config.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js">chainWebpack: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
  <span class="hljs-keyword">const</span> depPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./plugin/DepPlugin'</span>)
  config.plugin(<span class="hljs-string">'DepPlugin'</span>).use(depPlugin).tap(<span class="hljs-function"><span class="hljs-params">args</span> =></span> args)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>DepPlugin.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> sep = path.sep
<span class="hljs-keyword">let</span> cwd = process.cwd()
<span class="hljs-keyword">const</span> execSync = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>).execSync

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DepPlugin</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.options = options || &#123;&#125;
  <span class="hljs-built_in">this</span>.done = <span class="hljs-literal">false</span>
&#125;
DepPlugin.prototype.apply = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">compiler</span>) </span>&#123;
  <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
  compiler.hooks.entryOption.tap(<span class="hljs-string">'DepPlugin'</span>, <span class="hljs-function"><span class="hljs-params">compiler</span> =></span> &#123;
    <span class="hljs-keyword">if</span>(that.done) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">const</span> mainDependency = getDependency(<span class="hljs-string">'.'</span> + sep + <span class="hljs-string">'package.json'</span>)
    <span class="hljs-comment">// 假设有file引入了2个项目，baqi和baqi-chat</span>
    <span class="hljs-keyword">let</span> subDependency = &#123;
      ...getSubDependency(<span class="hljs-string">'baqi'</span>),
      ...getSubDependency(<span class="hljs-string">'baqi-chat'</span>)
    &#125;
    <span class="hljs-keyword">const</span> subDependencyKey = <span class="hljs-built_in">Object</span>.keys(subDependency)
    <span class="hljs-keyword">const</span> mainDependencyKey = <span class="hljs-built_in">Object</span>.keys(mainDependency)
    <span class="hljs-comment">// 获取当前包中的依赖</span>
    <span class="hljs-comment">// 查找baqi，baqi-chat包中有的依赖，但主包中没有的</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < subDependencyKey.length; i++) &#123;
      <span class="hljs-keyword">if</span> (mainDependencyKey.includes(subDependencyKey[i])) &#123;
        <span class="hljs-keyword">delete</span> subDependency[subDependencyKey[i]]
      &#125;
    &#125;
    <span class="hljs-comment">// 安装这些依赖</span>
    execCmdSync(<span class="hljs-string">'cd '</span> + cwd)
    <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> dep <span class="hljs-keyword">in</span> subDependency) &#123;
      <span class="hljs-comment">// node_modules中没有这些包就安装</span>
      <span class="hljs-keyword">if</span> (fs.existsSync(path.join(cwd, <span class="hljs-string">'node_modules'</span> + sep + dep)) === <span class="hljs-literal">false</span>) &#123;
        str += dep + <span class="hljs-string">'@'</span> + subDependency[dep].replace(<span class="hljs-regexp">/\"|\^|\~/g</span>, <span class="hljs-string">''</span>) + <span class="hljs-string">' '</span>
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (str) &#123;
      execCmdSync(<span class="hljs-string">'npm install '</span> + str + <span class="hljs-string">'--no-save'</span>)
    &#125;
  &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSubDependency</span> (<span class="hljs-params">moduleName</span>) </span>&#123;
  <span class="hljs-keyword">const</span> filePath = path.join(cwd, <span class="hljs-string">'..'</span> + sep + moduleName + sep + <span class="hljs-string">'package.json'</span>)
  <span class="hljs-keyword">const</span> dependencies = getDependency(filePath)
  <span class="hljs-keyword">return</span> dependencies
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDependency</span> (<span class="hljs-params">packageJsonPath</span>) </span>&#123;
  <span class="hljs-keyword">const</span> fileObj = <span class="hljs-built_in">JSON</span>.parse(readPackageJson(packageJsonPath))
  <span class="hljs-keyword">const</span> dependency = fileObj.dependencies
  <span class="hljs-keyword">return</span> dependency
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readPackageJson</span> (<span class="hljs-params">packageJsonPath</span>) </span>&#123;
  <span class="hljs-keyword">const</span> fileStr = fs.readFileSync(packageJsonPath, <span class="hljs-string">'utf8'</span>)
  <span class="hljs-keyword">return</span> fileStr
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">execCmdSync</span> (<span class="hljs-params">cmdStr</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行：'</span> + cmdStr)
  <span class="hljs-keyword">const</span> out = execSync(cmdStr, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;)
  <span class="hljs-keyword">return</span> out
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">问题二</h3>
<p>babel不会自动转义file引入的包，也就是子包中若有ES6写法，在低版本的浏览器中运行时会报错。</p>
<h5 data-id="heading-4">解决方案</h5>
<p>vue官网这么描述的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc4ece8125d43029a3d1c0c2e0bf7f9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
所以，可以在vue.config.js中添加</p>
<pre><code class="hljs language-js copyable" lang="js">transpileDependencies: [ 
  <span class="hljs-regexp">/[/\\]node_modules[/\\]baqi[/\\]/</span>,
  <span class="hljs-regexp">/[/\\]node_modules[/\\]baqi-chat[/\\]/</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此问题同样适用与npm link</p></div>  
</div>
            