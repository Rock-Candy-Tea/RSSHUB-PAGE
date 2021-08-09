
---
title: 'Yarn 2的Monorepo开发实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7409'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 21:06:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=7409'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Monorepo是指单仓库多包管理，目前是比较常见的一种包管理方式，比如<code>React</code>、<code>Vue</code>、<code>Babel</code>都是采用的这种管理方式。</p>
<p>使用<code>yarn</code>的workspace来管理多包仓库，相对<code>lerna</code>管理来说配置会简单一些。</p>
<p><code>yarn</code>的workspace会将仓库里的依赖通通放在根目录的<code>node_modules</code>里，这样比如<code>eslint</code>、<code>tsconfig</code>，<code>prettier</code>都能作用于子仓库。</p>
<p>我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangyu1818%2Ftikka" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangyu1818/tikka" ref="nofollow noopener noreferrer">仓库地址</a></p>
<h2 data-id="heading-0">yarn2的安装</h2>
<p><code>yarn2</code>增加了无<code>node_modules</code>的功能，额外增加了一些命令和插件机制，在Monorepo仓库中，<code>yarn2</code>可以自动替换各个子包相互依赖的版本号。</p>
<p>在项目目录中执行</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn <span class="hljs-built_in">set</span> version berry
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>berry</code>是<code>yarn2</code>的代，执行这个命令后项目会切换到<code>yarn2</code>管理。</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn <span class="hljs-built_in">set</span> version latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更新<code>yarn2</code>版本。</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn plugin import workspace-tools
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装<code>yarn2</code>的workspace插件，这个插件可以增加对workspace的命令操作。</p>
<p>因为<code>yarn2</code>多了一个无<code>node_modules</code>的功能，但是这个感觉不是很好用，所以还是需要<code>node_modules</code>。</p>
<p>修改<code>.yarnrc.yml</code>。</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">nodeLinker:</span> <span class="hljs-string">node-modules</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时<code>yanr2</code>会多一些额外的文件，我们需要把它们放进<code>.gitignore</code>。</p>
<pre><code class="copyable">.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">设置workspace</h2>
<p>根目录创建<code>packages</code>文件夹放置子包。</p>
<p><code>package.json</code>中配置workspace的目录为<code>packages</code>目录下的所有包。</p>
<pre><code class="copyable">"workspaces": [
    "packages/*"
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">子包的操作</h2>
<p>在<code>packages</code>目录中新建一个目录，比如叫<code>components</code>。</p>
<pre><code class="copyable">packages
├── components
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>packages/components</code>目录下执行<code>yarn init -y</code>来初始化。</p>
<p>根路径执行<code> yarn workspaces list</code>，会输出当前包的列表。</p>
<h3 data-id="heading-3">添加依赖</h3>
<p>项目根目录执行</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn workspace components add -D react
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>React</code>作为依赖添加到<code>components</code>的<code>package.json</code>中，但是实际依赖是装在根目录的<code>node_modules</code>里。</p>
<h2 data-id="heading-4">子包间的相互依赖</h2>
<p>子包间可能会存在依赖关系。</p>
<pre><code class="copyable">packages
├── components
├── shared
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在<code>components</code>包会依赖<code>shared</code>包，我们需要在<code>components</code>包中的<code>package.json</code>中添加配置。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"components"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"shared"</span>: <span class="hljs-string">"workspace:*"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>workspace:*</code>表示在<code>components</code>包执行<code>npm publish</code>的时候，会自动将<code>shared</code>的版本更换为<code>shared</code>包的版本。</p>
<h2 data-id="heading-5">tsconfig的配置</h2>
<p>只需要用一个<code>tscofnig</code>配置文件，就能管理所有子包的ts配置，额外需要配置的是<code>paths</code>字段，这样开发的时候ts才不会报找不到包的错。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"components"</span>: [<span class="hljs-string">"packages/components/src"</span>],
      <span class="hljs-attr">"shared"</span>: [<span class="hljs-string">"packages/shared/src"</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你的子包命名是像<code>vue</code>一样，就简写配置。</p>
<pre><code class="copyable">"paths":&#123;
  "@vue/*": ["packages/*/src"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">版本管理</h2>
<p>我没有找到yarn2 有自带的多包版本管理，所以我还是根据<code>vue</code>的<code>release</code>脚本来做的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// scripts/release.js</span>

<span class="hljs-comment">// 找到所有的包</span>
<span class="hljs-keyword">const</span> packages = fs
  .readdirSync(path.resolve(__dirname, <span class="hljs-string">'../packages'</span>))
  .filter(<span class="hljs-function">(<span class="hljs-params">p</span>) =></span> !p.startsWith(<span class="hljs-string">'.'</span>))

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateVersions</span>(<span class="hljs-params">version</span>) </span>&#123;
  <span class="hljs-comment">// 更新root package.json version</span>
  updatePackage(path.resolve(__dirname, <span class="hljs-string">'..'</span>), version)
  packages.forEach(<span class="hljs-function">(<span class="hljs-params">p</span>) =></span> updatePackage(getPkgRoot(p), version))
&#125;

<span class="hljs-comment">// 更新每个子包的package.json version</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updatePackage</span>(<span class="hljs-params">pkgRoot, version</span>) </span>&#123;
  <span class="hljs-keyword">const</span> pkgPath = path.resolve(pkgRoot, <span class="hljs-string">'package.json'</span>)
  <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(pkgPath, <span class="hljs-string">'utf-8'</span>))
  pkg.version = version
  fs.writeFileSync(pkgPath, <span class="hljs-built_in">JSON</span>.stringify(pkg, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>) + <span class="hljs-string">'\n'</span>)
&#125;

updateVersions(<span class="hljs-string">'1.0.0'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">打包📦</h2>
<p>打包会相对复杂一些，像<code>vue</code>是使用的<code>rollup</code>来自己写的配置打包，并且需要找到包路径循环执行命令。</p>
<p>yarn2可以省略循环操作，如果每一个子包都有<code>build</code>命令，则根目录执行<code>yarn workspaces foreach run build</code>，yarn会帮我们在每一个包路径执行<code>build</code>命令。</p>
<p>需要注意的是由于包之间有相互依赖关系，我们在根目录执行<code>yarn</code>后，子包会自动被<code>link</code>进<code>node_modules</code>，打包的时候，可能会找到<code>node_modules</code>里对应<code>link</code>后的包<code>main</code>字段的文件。</p>
<p>如果我们的子包<code>main</code>字段都为<code>lib/index.js</code>，<code>a</code>包依赖<code>b</code>包，打包时则会找到<code>node_modules/b/lib/index.js</code>，但是如果这时候<code>b</code>包没有执行打包就会找不到入口文件报错，所以在打包过程中也是有先后顺序的，需要先打<code>b</code>包，再打<code>a</code>包。</p>
<p>我写了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangyu1818%2Fcjsb" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangyu1818/cjsb" ref="nofollow noopener noreferrer">简单的CLI工具</a>来打包<code>commonjs</code>的代码。</p>
<pre><code class="hljs language-sh copyable" lang="sh">cjsb --packages packages/b packages/a
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录执行后，会先对<code>packages/b</code>打包，再对<code>packages/a</code>打包，也不需要每个包都有<code>build</code>命令了。</p>
<h2 data-id="heading-8">结语</h2>
<p>这是我使用yarn2 workspace的一次简单实践。</p>
<p>如果觉得麻烦其实也可以用一些现有的工具，比如<code>lerna</code>管理+<code>father</code>打包。</p></div>  
</div>
            