
---
title: 'Vue 3.2 发布了，那尤雨溪是怎么发布 Vue.js 的？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa09101a1f0743489e905c2b5560ff90~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 17:14:36 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa09101a1f0743489e905c2b5560ff90~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<p>大家好，我是<a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank" rel="nofollow noopener noreferrer" title="https://lxchuan12.gitee.io" ref="nofollow noopener noreferrer">若川</a>。欢迎关注我的<a href="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" title="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" target="_blank">公众号若川视野</a>，最近组织了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fruochuan12" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/ruochuan12" ref="nofollow noopener noreferrer"><strong>源码共读</strong></a>活动，感兴趣的可以加我微信 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FW6Su8znRL8Vsj6ZayY_UAg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/W6Su8znRL8Vsj6ZayY_UAg" ref="nofollow noopener noreferrer">ruochuan12</a>，长期交流学习。</p>
<p>之前写的<a href="https://juejin.cn/column/6960551178908205093" target="_blank" title="https://juejin.cn/column/6960551178908205093">《学习源码整体架构系列》</a> 包含<code>jQuery</code>、<code>underscore</code>、<code>lodash</code>、<code>vuex</code>、<code>sentry</code>、<code>axios</code>、<code>redux</code>、<code>koa</code>、<code>vue-devtools</code>、<code>vuex4</code>十篇源码文章。</p>
<p>写相对很难的源码，耗费了自己的时间和精力，也没收获多少阅读点赞，其实是一件挺受打击的事情。从阅读量和读者受益方面来看，不能促进作者持续输出文章。</p>
<p>所以转变思路，写一些相对通俗易懂的文章。<strong>其实源码也不是想象的那么难，至少有很多看得懂</strong>。</p>
<p>最近尤雨溪发布了3.2版本。小版本已经是<code>3.2.4</code>了。本文来学习下尤大是怎么发布<code>vuejs</code>的，学习源码为自己所用。</p>
<p>本文涉及到的 <code>vue-next/scripts/release.js</code>文件，整个文件代码行数虽然只有 <code>200</code> 余行，但非常值得我们学习。</p>
<p>歌德曾说：读一本好书，就是在和高尚的人谈话。 同理可得：读源码，也算是和作者的一种学习交流的方式。</p>
<p>阅读本文，你将学到：</p>
<pre><code class="hljs language-bash copyable" lang="bash">1. 熟悉 vuejs 发布流程
2. 学会调试 nodejs 代码
3. 动手优化公司项目发布流程
<span class="copy-code-btn">复制代码</span></code></pre>
<p>环境准备之前，我们先预览下<code>vuejs</code>的发布流程。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa09101a1f0743489e905c2b5560ff90~tplv-k3u1fbpfcp-watermark.image" alt="vue 发布流程" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2. 环境准备</h2>
<p>打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next" ref="nofollow noopener noreferrer">vue-next</a>，
开源项目一般都能在 <code>README.md</code> 或者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2F.github%2Fcontributing.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/.github/contributing.md" ref="nofollow noopener noreferrer">.github/contributing.md</a> 找到贡献指南。</p>
<p>而贡献指南写了很多关于参与项目开发的信息。比如怎么跑起来，项目目录结构是怎样的。怎么投入开发，需要哪些知识储备等。</p>
<p>你需要确保 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.org/" ref="nofollow noopener noreferrer">Node.js</a> 版本是 <code>10+</code>, 而且 <code>yarn</code> 的版本是 <code>1.x</code> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarnpkg.com%2Fen%2Fdocs%2Finstall" target="_blank" rel="nofollow noopener noreferrer" title="https://yarnpkg.com/en/docs/install" ref="nofollow noopener noreferrer">Yarn 1.x</a>。</p>
<p>你安装的 <code>Node.js</code> 版本很可能是低于 <code>10</code>。最简单的办法就是去官网重新安装。也可以使用 <code>nvm</code>等管理<code>Node.js</code>版本。</p>
<pre><code class="hljs language-bash copyable" lang="bash">node -v
<span class="hljs-comment"># v14.16.0</span>
<span class="hljs-comment"># 全局安装 yarn</span>
<span class="hljs-comment"># 克隆项目</span>
git <span class="hljs-built_in">clone</span> https://github.com/vuejs/vue-next.git
<span class="hljs-built_in">cd</span> vue-next

<span class="hljs-comment"># 或者克隆我的项目</span>
git <span class="hljs-built_in">clone</span> https://github.com/lxchuan12/vue-next-analysis.git
<span class="hljs-built_in">cd</span> vue-next-analysis/vue-next

<span class="hljs-comment"># 安装 yarn</span>
npm install --global yarn
<span class="hljs-comment"># 安装依赖</span>
yarn <span class="hljs-comment"># install the dependencies of the project</span>
<span class="hljs-comment"># yarn release</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.1 严格校验使用 yarn 安装依赖</h3>
<p>接着我们来看下 <code>vue-next/package.json</code> 文件。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// vue-next/package.json</span>
&#123;
    <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"3.2.4"</span>,
    <span class="hljs-attr">"workspaces"</span>: [
        <span class="hljs-string">"packages/*"</span>
    ],
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-comment">// --dry 参数是我加的，如果你是调试 代码也建议加</span>
        <span class="hljs-comment">// 不执行测试和编译 、不执行 推送git等操作</span>
        <span class="hljs-comment">// 也就是说空跑，只是打印，后文再详细讲述</span>
        <span class="hljs-attr">"release"</span>: <span class="hljs-string">"node scripts/release.js --dry"</span>,
        <span class="hljs-attr">"preinstall"</span>: <span class="hljs-string">"node ./scripts/checkYarn.js"</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你尝试使用 <code>npm</code> 安装依赖，应该是会报错的。为啥会报错呢。
因为 <code>package.json</code> 有个前置 <code>preinstall</code>  <code>node ./scripts/checkYarn.js</code> 判断强制要求是使用<code>yarn</code>安装。</p>
<p><code>scripts/checkYarn.js</code>文件如下，也就是在<code>process.env</code>环境变量中找执行路径<code>npm_execpath</code>，如果不是<code>yarn</code>就输出警告，且进程结束。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// scripts/checkYarn.js</span>
<span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/yarn\.js$/</span>.test(process.env.npm_execpath || <span class="hljs-string">''</span>)) &#123;
  <span class="hljs-built_in">console</span>.warn(
    <span class="hljs-string">'\u001b[33mThis repository requires Yarn 1.x for scripts to work properly.\u001b[39m\n'</span>
  )
  process.exit(<span class="hljs-number">1</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想忽略这个前置的钩子判断，可以使用<code>yarn --ignore-scripts</code> 命令。也有后置的钩子<code>post</code>。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.npmjs.com%2Fcli%2Fv6%2Fusing-npm%2Fscripts" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.npmjs.com/cli/v6/using-npm/scripts" ref="nofollow noopener noreferrer">更多详细的可以查看 npm 文档</a></p>
<h3 data-id="heading-3">2.2 调试  vue-next/scripts/release.js 文件</h3>
<p>接着我们来学习如何调试 <code>vue-next/scripts/release.js</code>文件。</p>
<p>这里声明下我的 <code>VSCode</code> 版本 是 <code>1.59.0</code> 应该 <code>1.50.0</code> 起就可以按以下步骤调试了。</p>
<pre><code class="hljs language-bash copyable" lang="bash">code -v
<span class="hljs-comment"># 1.59.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到 <code>vue-next/package.json</code> 文件打开，然后在 <code>scripts</code> 上方，会有<code>debug</code>（调试）按钮，点击后，选择 <code>release</code>。即可进入调试模式。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5474fafa63ee4ad1aada507be7b1d9d1~tplv-k3u1fbpfcp-watermark.image" alt="debugger" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时终端会如下图所示，有 <code>Debugger attached.</code> 输出。这时放张图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c77dec9a4eb4e1cbc3bc9139a902e91~tplv-k3u1fbpfcp-watermark.image" alt="terminal" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Fnodejs%2Fnodejs-debugging" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/docs/nodejs/nodejs-debugging" ref="nofollow noopener noreferrer"> 更多 nodejs 调试相关  可以查看官方文档</a></p>
<p>学会调试后，先大致走一遍流程，在关键地方多打上几个断点多走几遍，就能猜测到源码意图了。</p>
<h2 data-id="heading-4">3 文件开头的一些依赖引入和函数声明</h2>
<p>我们可以跟着断点来，先看文件开头的一些依赖引入和函数声明</p>
<h3 data-id="heading-5">3.1 第一部分</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue-next/scripts/release.js</span>
<span class="hljs-keyword">const</span> args = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>))
<span class="hljs-comment">// 文件模块</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-comment">// 路径</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-comment">// 控制台</span>
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>)
<span class="hljs-keyword">const</span> semver = <span class="hljs-built_in">require</span>(<span class="hljs-string">'semver'</span>)
<span class="hljs-keyword">const</span> currentVersion = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).version
<span class="hljs-keyword">const</span> &#123; prompt &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>)

<span class="hljs-comment">// 执行子进程命令   简单说 就是在终端命令行执行 命令</span>
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过依赖，我们可以在 <code>node_modules</code> 找到对应安装的依赖。也可以找到其<code>README</code>和<code>github</code>仓库。</p>
<h4 data-id="heading-6">3.1.1 minimist  命令行参数解析</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsubstack%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/substack/minimist" ref="nofollow noopener noreferrer">minimist</a></p>
<p>简单说，这个库，就是解析命令行参数的。看例子，我们比较容易看懂传参和解析结果。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ node example/parse.js -a beep -b boop
&#123; _: [], a: <span class="hljs-string">'beep'</span>, b: <span class="hljs-string">'boop'</span> &#125;

$ node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
&#123; _: [ <span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-string">'baz'</span> ],
  x: 3,
  y: 4,
  n: 5,
  a: <span class="hljs-literal">true</span>,
  b: <span class="hljs-literal">true</span>,
  c: <span class="hljs-literal">true</span>,
  beep: <span class="hljs-string">'boop'</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> args = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>process.argv</code>的第一和第二个元素是<code>Node</code>可执行文件和被执行JavaScript文件的完全限定的文件系统路径，无论你是否这样输入他们。</p>
<h4 data-id="heading-7">3.1.2 chalk 终端多色彩输出</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchalk%2Fchalk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chalk/chalk" ref="nofollow noopener noreferrer">chalk</a></p>
<p>简单说，这个是用于终端显示多色彩输出。</p>
<h4 data-id="heading-8">3.1.3 semver  语义化版本</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnpm%2Fnode-semver" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/npm/node-semver" ref="nofollow noopener noreferrer">semver</a></p>
<p>语义化版本的nodejs实现，用于版本校验比较等。关于语义化版本可以看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2Flang%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/lang/zh-CN/" ref="nofollow noopener noreferrer">语义化版本 2.0.0 文档</a></p>
<blockquote>
<p>版本格式：主版本号.次版本号.修订号，版本号递增规则如下：<br>
主版本号：当你做了不兼容的 API 修改，<br>
次版本号：当你做了向下兼容的功能性新增，<br>
修订号：当你做了向下兼容的问题修正。<br>
先行版本号及版本编译信息可以加到“主版本号.次版本号.修订号”的后面，作为延伸。<br></p>
</blockquote>
<h4 data-id="heading-9">3.1.4 enquirer 交互式询问 CLI</h4>
<p>简单说就是交互式询问用户输入。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fenquirer%2Fenquirer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/enquirer/enquirer" ref="nofollow noopener noreferrer">enquirer</a></p>
<h4 data-id="heading-10">3.1.5 execa 执行命令</h4>
<p>简单说就是执行命令的，类似我们自己在终端输入命令，比如 <code>echo 若川</code>。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fexeca" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/execa" ref="nofollow noopener noreferrer">execa</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 例子</span>
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>);

(<span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">const</span> &#123;stdout&#125; = <span class="hljs-keyword">await</span> execa(<span class="hljs-string">'echo'</span>, [<span class="hljs-string">'unicorns'</span>]);
<span class="hljs-built_in">console</span>.log(stdout);
<span class="hljs-comment">//=> 'unicorns'</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完了第一部分，接着我们来看第二部分。</p>
<h3 data-id="heading-11">3.2 第二部分</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue-next/scripts/release.js</span>

<span class="hljs-comment">// 对应 yarn run release --preid=beta</span>
<span class="hljs-comment">// beta</span>
<span class="hljs-keyword">const</span> preId =
  args.preid ||
  (semver.prerelease(currentVersion) && semver.prerelease(currentVersion)[<span class="hljs-number">0</span>])
<span class="hljs-comment">// 对应 yarn run release --dry</span>
<span class="hljs-comment">// true</span>
<span class="hljs-keyword">const</span> isDryRun = args.dry
<span class="hljs-comment">// 对应 yarn run release --skipTests</span>
<span class="hljs-comment">// true 跳过测试</span>
<span class="hljs-keyword">const</span> skipTests = args.skipTests
<span class="hljs-comment">// 对应 yarn run release --skipBuild </span>
<span class="hljs-comment">// true</span>
<span class="hljs-keyword">const</span> skipBuild = args.skipBuild

<span class="hljs-comment">// 读取 packages 文件夹，过滤掉 不是 .ts文件 结尾 并且不是 . 开头的文件夹</span>
<span class="hljs-keyword">const</span> packages = fs
  .readdirSync(path.resolve(__dirname, <span class="hljs-string">'../packages'</span>))
  .filter(<span class="hljs-function"><span class="hljs-params">p</span> =></span> !p.endsWith(<span class="hljs-string">'.ts'</span>) && !p.startsWith(<span class="hljs-string">'.'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二部分相对简单，继续看第三部分。</p>
<h3 data-id="heading-12">3.3 第三部分</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue-next/scripts/release.js</span>

<span class="hljs-comment">// 跳过的包</span>
<span class="hljs-keyword">const</span> skippedPackages = []

<span class="hljs-comment">// 版本递增</span>
<span class="hljs-keyword">const</span> versionIncrements = [
  <span class="hljs-string">'patch'</span>,
  <span class="hljs-string">'minor'</span>,
  <span class="hljs-string">'major'</span>,
  ...(preId ? [<span class="hljs-string">'prepatch'</span>, <span class="hljs-string">'preminor'</span>, <span class="hljs-string">'premajor'</span>, <span class="hljs-string">'prerelease'</span>] : [])
]

<span class="hljs-keyword">const</span> inc = <span class="hljs-function"><span class="hljs-params">i</span> =></span> semver.inc(currentVersion, i, preId)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一块可能不是很好理解。<code>inc</code>是生成一个版本。更多可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnpm%2Fnode-semver%23prerelease-identifiers" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/npm/node-semver#prerelease-identifiers" ref="nofollow noopener noreferrer">semver文档</a></p>
<pre><code class="hljs language-js copyable" lang="js">semver.inc(<span class="hljs-string">'3.2.4'</span>, <span class="hljs-string">'prerelease'</span>, <span class="hljs-string">'beta'</span>)
<span class="hljs-comment">// 3.2.5-beta.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3.4 第四部分</h3>
<p>第四部分声明了一些执行脚本函数等</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue-next/scripts/release.js</span>

<span class="hljs-comment">// 获取 bin 命令</span>
<span class="hljs-keyword">const</span> bin = <span class="hljs-function"><span class="hljs-params">name</span> =></span> path.resolve(__dirname, <span class="hljs-string">'../node_modules/.bin/'</span> + name)
<span class="hljs-keyword">const</span> run = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  execa(bin, args, &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>, ...opts &#125;)
<span class="hljs-keyword">const</span> dryRun = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  <span class="hljs-built_in">console</span>.log(chalk.blue(<span class="hljs-string">`[dryrun] <span class="hljs-subst">$&#123;bin&#125;</span> <span class="hljs-subst">$&#123;args.join(<span class="hljs-string">' '</span>)&#125;</span>`</span>), opts)
<span class="hljs-keyword">const</span> runIfNotDry = isDryRun ? dryRun : run

<span class="hljs-comment">// 获取包的路径</span>
<span class="hljs-keyword">const</span> getPkgRoot = <span class="hljs-function"><span class="hljs-params">pkg</span> =></span> path.resolve(__dirname, <span class="hljs-string">'../packages/'</span> + pkg)

<span class="hljs-comment">// 控制台输出</span>
<span class="hljs-keyword">const</span> step = <span class="hljs-function"><span class="hljs-params">msg</span> =></span> <span class="hljs-built_in">console</span>.log(chalk.cyan(msg))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">3.4.1 bin 函数</h4>
<p>获取 <code>node_modules/.bin/</code> 目录下的命令，整个文件就用了一次。</p>
<pre><code class="hljs language-js copyable" lang="js">bin(<span class="hljs-string">'jest'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于在命令终端，项目根目录 运行 <code>./node_modules/.bin/jest</code> 命令。</p>
<h4 data-id="heading-15">3.4.2 run、dryRun、runIfNotDry</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> run = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  execa(bin, args, &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>, ...opts &#125;)
<span class="hljs-keyword">const</span> dryRun = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  <span class="hljs-built_in">console</span>.log(chalk.blue(<span class="hljs-string">`[dryrun] <span class="hljs-subst">$&#123;bin&#125;</span> <span class="hljs-subst">$&#123;args.join(<span class="hljs-string">' '</span>)&#125;</span>`</span>), opts)
<span class="hljs-keyword">const</span> runIfNotDry = isDryRun ? dryRun : run
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>run</code> 真实在终端跑命令，比如 <code>yarn build --release</code></p>
<p><code>dryRun</code> 则是不跑，只是 <code>console.log();</code> 打印 'yarn build --release'</p>
<p><code>runIfNotDry</code> 如果不是空跑就执行命令。isDryRun 参数是通过控制台输入的。<code>yarn run release --dry</code>这样就是<code>true</code>。<code>runIfNotDry</code>就是只是打印，不执行命令。这样设计的好处在于，可以有时不想直接提交，要先看看执行命令的结果。不得不说，尤大就是会玩。</p>
<p>在 <code>main</code> 函数末尾，也可以看到类似的提示。可以用<code>git diff</code>先看看文件修改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isDryRun) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`\nDry run finished - run git diff to see package changes.`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完了文件开头的一些依赖引入和函数声明等，我们接着来看<code>main</code>主入口函数。</p>
<h2 data-id="heading-16">4 main 主流程</h2>
<p>第4节，主要都是<code>main</code> 函数拆解分析。</p>
<h3 data-id="heading-17">4.1 流程梳理 main 函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>)
<span class="hljs-keyword">const</span> step = <span class="hljs-function"><span class="hljs-params">msg</span> =></span> <span class="hljs-built_in">console</span>.log(chalk.cyan(msg))
<span class="hljs-comment">// 前面一堆依赖引入和函数定义等</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 版本校验</span>

  <span class="hljs-comment">// run tests before release</span>
  step(<span class="hljs-string">'\nRunning tests...'</span>)
  <span class="hljs-comment">// update all package versions and inter-dependencies</span>
  step(<span class="hljs-string">'\nUpdating cross dependencies...'</span>)
  <span class="hljs-comment">// build all packages with types</span>
  step(<span class="hljs-string">'\nBuilding all packages...'</span>)

  <span class="hljs-comment">// generate changelog</span>
  step(<span class="hljs-string">'\nCommitting changes...'</span>)

  <span class="hljs-comment">// publish packages</span>
  step(<span class="hljs-string">'\nPublishing packages...'</span>)

  <span class="hljs-comment">// push to GitHub</span>
  step(<span class="hljs-string">'\nPushing to GitHub...'</span>)
&#125;

main().catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.error(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的<code>main</code>函数省略了很多具体函数实现。接下来我们拆解 <code>main</code> 函数。</p>
<h3 data-id="heading-18">4.2 确认要发布的版本</h3>
<p>第一段代码虽然比较长，但是还好理解。
主要就是确认要发布的版本。</p>
<p>调试时，我们看下这段的两张截图，就好理解啦。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69b61d4df8ad4687ad99600a9220bc84~tplv-k3u1fbpfcp-watermark.image" alt="终端输出选择版本号" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84ee1c3af54a49b8bf4ae383e1e8c783~tplv-k3u1fbpfcp-watermark.image" alt="终端输入确认版本号" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 根据上文 mini 这句代码意思是 yarn run release 3.2.4 </span>
<span class="hljs-comment">// 取到参数 3.2.4</span>
<span class="hljs-keyword">let</span> targetVersion = args._[<span class="hljs-number">0</span>]

<span class="hljs-keyword">if</span> (!targetVersion) &#123;
  <span class="hljs-comment">// no explicit version, offer suggestions</span>
  <span class="hljs-keyword">const</span> &#123; release &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'select'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'release'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'Select release type'</span>,
    <span class="hljs-attr">choices</span>: versionIncrements.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;i&#125;</span> (<span class="hljs-subst">$&#123;inc(i)&#125;</span>)`</span>).concat([<span class="hljs-string">'custom'</span>])
  &#125;)

<span class="hljs-comment">// 选自定义</span>
  <span class="hljs-keyword">if</span> (release === <span class="hljs-string">'custom'</span>) &#123;
    targetVersion = (
      <span class="hljs-keyword">await</span> prompt(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'version'</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Input custom version'</span>,
        <span class="hljs-attr">initial</span>: currentVersion
      &#125;)
    ).version
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 取到括号里的版本号</span>
    targetVersion = release.match(<span class="hljs-regexp">/\((.*)\)/</span>)[<span class="hljs-number">1</span>]
  &#125;
&#125;

<span class="hljs-comment">// 校验 版本是否符合 规范</span>
<span class="hljs-keyword">if</span> (!semver.valid(targetVersion)) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`invalid target version: <span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>)
&#125;

<span class="hljs-comment">// 确认要 release</span>
<span class="hljs-keyword">const</span> &#123; yes &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'confirm'</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'yes'</span>,
  <span class="hljs-attr">message</span>: <span class="hljs-string">`Releasing v<span class="hljs-subst">$&#123;targetVersion&#125;</span>. Confirm?`</span>
&#125;)

<span class="hljs-comment">// false 直接返回</span>
<span class="hljs-keyword">if</span> (!yes) &#123;
  <span class="hljs-keyword">return</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">4.3 执行测试用例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// run tests before release</span>
step(<span class="hljs-string">'\nRunning tests...'</span>)
<span class="hljs-keyword">if</span> (!skipTests && !isDryRun) &#123;
  <span class="hljs-keyword">await</span> run(bin(<span class="hljs-string">'jest'</span>), [<span class="hljs-string">'--clearCache'</span>])
  <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'test'</span>, <span class="hljs-string">'--bail'</span>])
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`(skipped)`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">4.4 更新依赖版本</h3>
<p>这一部分，就是更新根目录下<code>package.json</code> 的版本号和所有 <code>packages</code> 的版本号。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// update all package versions and inter-dependencies</span>
step(<span class="hljs-string">'\nUpdating cross dependencies...'</span>)
updateVersions(targetVersion)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateVersions</span>(<span class="hljs-params">version</span>) </span>&#123;
  <span class="hljs-comment">// 1. update root package.json</span>
  updatePackage(path.resolve(__dirname, <span class="hljs-string">'..'</span>), version)
  <span class="hljs-comment">// 2. update all packages</span>
  packages.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> updatePackage(getPkgRoot(p), version))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">4.4.1 updatePackage 更新包</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updatePackage</span>(<span class="hljs-params">pkgRoot, version</span>) </span>&#123;
  <span class="hljs-keyword">const</span> pkgPath = path.resolve(pkgRoot, <span class="hljs-string">'package.json'</span>)
  <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(pkgPath, <span class="hljs-string">'utf-8'</span>))
  pkg.version = version
  updateDeps(pkg, <span class="hljs-string">'dependencies'</span>, version)
  updateDeps(pkg, <span class="hljs-string">'peerDependencies'</span>, version)
  fs.writeFileSync(pkgPath, <span class="hljs-built_in">JSON</span>.stringify(pkg, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>) + <span class="hljs-string">'\n'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">4.4.2 updateDeps 更新依赖版本号</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDeps</span>(<span class="hljs-params">pkg, depType, version</span>) </span>&#123;
  <span class="hljs-keyword">const</span> deps = pkg[depType]
  <span class="hljs-keyword">if</span> (!deps) <span class="hljs-keyword">return</span>
  <span class="hljs-built_in">Object</span>.keys(deps).forEach(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (
      dep === <span class="hljs-string">'vue'</span> ||
      (dep.startsWith(<span class="hljs-string">'@vue'</span>) && packages.includes(dep.replace(<span class="hljs-regexp">/^@vue\//</span>, <span class="hljs-string">''</span>)))
    ) &#123;
      <span class="hljs-built_in">console</span>.log(
        chalk.yellow(<span class="hljs-string">`<span class="hljs-subst">$&#123;pkg.name&#125;</span> -> <span class="hljs-subst">$&#123;depType&#125;</span> -> <span class="hljs-subst">$&#123;dep&#125;</span>@<span class="hljs-subst">$&#123;version&#125;</span>`</span>)
      )
      deps[dep] = version
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">4.5 打包编译所有包</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// build all packages with types</span>
step(<span class="hljs-string">'\nBuilding all packages...'</span>)
<span class="hljs-keyword">if</span> (!skipBuild && !isDryRun) &#123;
  <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'build'</span>, <span class="hljs-string">'--release'</span>])
  <span class="hljs-comment">// test generated dts files</span>
  step(<span class="hljs-string">'\nVerifying type declarations...'</span>)
  <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'test-dts-only'</span>])
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`(skipped)`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">4.6 生成 changelog</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// generate changelog</span>
<span class="hljs-keyword">await</span> run(<span class="hljs-string">`yarn`</span>, [<span class="hljs-string">'changelog'</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>yarn changelog</code> 对应的脚本是<code>conventional-changelog -p angular -i CHANGELOG.md -s</code>。</p>
<h3 data-id="heading-25">4.7 提交代码</h3>
<p>经过更新版本号后，有文件改动，于是<code>git diff</code>。
是否有文件改动，如果有提交。</p>
<p><code>git add -A</code>
<code>git  commit -m 'release: v$&#123;targetVersion&#125;'</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; stdout &#125; = <span class="hljs-keyword">await</span> run(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'diff'</span>], &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'pipe'</span> &#125;)
<span class="hljs-keyword">if</span> (stdout) &#123;
  step(<span class="hljs-string">'\nCommitting changes...'</span>)
  <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'add'</span>, <span class="hljs-string">'-A'</span>])
  <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'commit'</span>, <span class="hljs-string">'-m'</span>, <span class="hljs-string">`release: v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'No changes to commit.'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">4.8 发布包</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// publish packages</span>
step(<span class="hljs-string">'\nPublishing packages...'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pkg <span class="hljs-keyword">of</span> packages) &#123;
  <span class="hljs-keyword">await</span> publishPackage(pkg, targetVersion, runIfNotDry)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段函数比较长，可以不用细看，简单说就是 <code>yarn publish</code> 发布包。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">publishPackage</span>(<span class="hljs-params">pkgName, version, runIfNotDry</span>) </span>&#123;
  <span class="hljs-comment">// 如果在 跳过包里 则跳过</span>
  <span class="hljs-keyword">if</span> (skippedPackages.includes(pkgName)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">const</span> pkgRoot = getPkgRoot(pkgName)
  <span class="hljs-keyword">const</span> pkgPath = path.resolve(pkgRoot, <span class="hljs-string">'package.json'</span>)
  <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(pkgPath, <span class="hljs-string">'utf-8'</span>))
  <span class="hljs-keyword">if</span> (pkg.private) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// For now, all 3.x packages except "vue" can be published as</span>
  <span class="hljs-comment">// `latest`, whereas "vue" will be published under the "next" tag.</span>
  <span class="hljs-keyword">let</span> releaseTag = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">if</span> (args.tag) &#123;
    releaseTag = args.tag
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (version.includes(<span class="hljs-string">'alpha'</span>)) &#123;
    releaseTag = <span class="hljs-string">'alpha'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (version.includes(<span class="hljs-string">'beta'</span>)) &#123;
    releaseTag = <span class="hljs-string">'beta'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (version.includes(<span class="hljs-string">'rc'</span>)) &#123;
    releaseTag = <span class="hljs-string">'rc'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (pkgName === <span class="hljs-string">'vue'</span>) &#123;
    <span class="hljs-comment">// TODO remove when 3.x becomes default</span>
    releaseTag = <span class="hljs-string">'next'</span>
  &#125;

  <span class="hljs-comment">// TODO use inferred release channel after official 3.0 release</span>
  <span class="hljs-comment">// const releaseTag = semver.prerelease(version)[0] || null</span>

  step(<span class="hljs-string">`Publishing <span class="hljs-subst">$&#123;pkgName&#125;</span>...`</span>)
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> runIfNotDry(
      <span class="hljs-string">'yarn'</span>,
      [
        <span class="hljs-string">'publish'</span>,
        <span class="hljs-string">'--new-version'</span>,
        version,
        ...(releaseTag ? [<span class="hljs-string">'--tag'</span>, releaseTag] : []),
        <span class="hljs-string">'--access'</span>,
        <span class="hljs-string">'public'</span>
      ],
      &#123;
        <span class="hljs-attr">cwd</span>: pkgRoot,
        <span class="hljs-attr">stdio</span>: <span class="hljs-string">'pipe'</span>
      &#125;
    )
    <span class="hljs-built_in">console</span>.log(chalk.green(<span class="hljs-string">`Successfully published <span class="hljs-subst">$&#123;pkgName&#125;</span>@<span class="hljs-subst">$&#123;version&#125;</span>`</span>))
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-keyword">if</span> (e.stderr.match(<span class="hljs-regexp">/previously published/</span>)) &#123;
      <span class="hljs-built_in">console</span>.log(chalk.red(<span class="hljs-string">`Skipping already published: <span class="hljs-subst">$&#123;pkgName&#125;</span>`</span>))
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> e
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">4.9 推送到 github</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// push to GitHub</span>
step(<span class="hljs-string">'\nPushing to GitHub...'</span>)
<span class="hljs-comment">// 打 tag</span>
<span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'tag'</span>, <span class="hljs-string">`v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
<span class="hljs-comment">// 推送 tag</span>
<span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'push'</span>, <span class="hljs-string">'origin'</span>, <span class="hljs-string">`refs/tags/v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
<span class="hljs-comment">// git push 所有改动到 远程  - github</span>
<span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'push'</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// yarn run release --dry</span>

<span class="hljs-comment">// 如果传了这个参数则输出 可以用 git diff 看看更改</span>

<span class="hljs-comment">// const isDryRun = args.dry</span>
<span class="hljs-keyword">if</span> (isDryRun) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`\nDry run finished - run git diff to see package changes.`</span>)
&#125;

<span class="hljs-comment">// 如果 跳过的包，则输出以下这些包没有发布。不过代码 `skippedPackages` 里是没有包。</span>
<span class="hljs-comment">// 所以这段代码也不会执行。</span>
<span class="hljs-comment">// 我们习惯写 arr.length !== 0 其实 0 就是 false 。可以不写。</span>
<span class="hljs-keyword">if</span> (skippedPackages.length) &#123;
  <span class="hljs-built_in">console</span>.log(
    chalk.yellow(
      <span class="hljs-string">`The following packages are skipped and NOT published:\n- <span class="hljs-subst">$&#123;skippedPackages.join(
        <span class="hljs-string">'\n- '</span>
      )&#125;</span>`</span>
    )
  )
&#125;
<span class="hljs-built_in">console</span>.log()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里我们就拆解分析完 <code>main</code> 函数了。</p>
<p>整个流程很清晰。</p>
<pre><code class="hljs language-bash copyable" lang="bash">1. 确认要发布的版本
2. 执行测试用例
3. 更新依赖版本
    3.1 updatePackage 更新包
    3.2 updateDeps 更新依赖版本号
4. 打包编译所有包
5. 生成 changelog
6. 提交代码
7. 发布包
8. 推送到 github
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用一张图总结则是：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa09101a1f0743489e905c2b5560ff90~tplv-k3u1fbpfcp-watermark.image" alt="vue 发布流程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看完<code>vue-next/scripts/release.js</code>，感兴趣还可以看<code>vue-next/scripts</code>文件夹下其他代码，相对行数不多，但收益较大。</p>
<h2 data-id="heading-28">5. 总结</h2>
<p><code>vuejs</code>发布的文件很多代码我们可以直接复制粘贴修改，优化我们自己发布的流程。比如写小程序，相对可能发布频繁，完全可以使用这套代码，配合<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fdevtools%2Fci.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html" ref="nofollow noopener noreferrer">miniprogram-ci</a>，再加上一些自定义，加以优化。</p>
<p>当然也可以用开源的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frelease-it%2Frelease-it" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/release-it/release-it" ref="nofollow noopener noreferrer">release-it</a>。</p>
<p>同时，我们可以：</p>
<p>引入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.atlassian.com%2Fgit%2Ftutorials%2Fcomparing-workflows%2Fgitflow-workflow" target="_blank" rel="nofollow noopener noreferrer" title="https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow" ref="nofollow noopener noreferrer">git flow</a>，管理<code>git</code>分支。估计很多人不知道<code>windows</code> <code>git bash</code>已经默认支持 <code>git flow </code>命令。</p>
<p>引入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftypicode%2Fhusky" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/typicode/husky" ref="nofollow noopener noreferrer">husky</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fokonet%2Flint-staged" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/okonet/lint-staged" ref="nofollow noopener noreferrer">lint-staged</a> 提交<code>commit</code>时用<code>ESLint</code>等校验代码提交是否能够通过检测。</p>
<p>引入 单元测试 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fjest" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/jest" ref="nofollow noopener noreferrer">jest</a>，测试关键的工具函数等。</p>
<p>引入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fconventional-changelog%2Fconventional-changelog" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/conventional-changelog/conventional-changelog" ref="nofollow noopener noreferrer">conventional-changelog</a></p>
<p>引入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstreamich%2Fgit-cz" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/streamich/git-cz" ref="nofollow noopener noreferrer">git-cz</a> 交互式<code>git commit</code>。</p>
<p>等等规范自己项目的流程。如果一个候选人，通过看<code>vuejs</code>发布的源码，积极主动优化自己项目。我觉得面试官会认为这个候选人比较加分。</p>
<p>看开源项目源码的好处在于：一方面可以拓展视野，另外一方面可以为自己所用，收益相对较高。</p>
<hr>
<h2 data-id="heading-29">关于</h2>
<p>作者：常以<strong>若川</strong>为名混迹于江湖。前端路上 | PPT爱好者 | 所知甚少，唯善学。<br>
<a href="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" title="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" target="_blank">公众号若川视野</a>，致力于帮助5年内前端成长<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" title="https://link.juejin.cn?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank">若川的博客</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fblog%2Flxchuan12" title="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fblog%2Flxchuan12" target="_blank"><code>segmentfault</code>若川视野专栏</a>，开通了<strong>若川视野</strong>专栏，欢迎关注~<br>
<a href="https://juejin.im/user/1415826704971918/posts" title="https://juejin.im/user/1415826704971918/posts" target="_blank">掘金专栏</a>，欢迎关注~<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Flxchuan12" title="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Flxchuan12" target="_blank">知乎若川视野专栏</a>，开通了<strong>若川视野</strong>专栏，欢迎关注~<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flxchuan12%2Fblog" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flxchuan12%2Fblog" target="_blank">github blog</a>，求个<code>star</code>^_^~</p></div>  
</div>
            