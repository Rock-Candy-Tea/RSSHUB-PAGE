
---
title: '你知道 Vue 3 是如何发布新版本的吗？Vue 3 release 源码解析带你了解 Vue 3 发布流程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68e599b7dfa8488099198cb8bcaacdfc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 19:58:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68e599b7dfa8488099198cb8bcaacdfc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue.js 是如何发布的</h1>
<p>原文链接: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fupupming%2Fvue-next-analysis%2Fblob%2Fmaster%2Fmd%2Frelease%2FREADME-upupming.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/upupming/vue-next-analysis/blob/master/md/release/README-upupming.md" ref="nofollow noopener noreferrer">github.com/upupming/vu…</a></p>
<h2 data-id="heading-1">准备工作</h2>
<p>第一次阅读参与源码共读活动，看了上期的工具函数的总结，学习到很多，感觉跟着<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fruochuan12%2Ffnfzu7" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/ruochuan12/fnfzu7" ref="nofollow noopener noreferrer">若川大哥</a>学下去肯定会收获满满。</p>
<p>这次要阅读的源码在: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub1s.com%2Fvuejs%2Fvue-next%2Fblob%2FHEAD%2Fscripts%2Frelease.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github1s.com/vuejs/vue-next/blob/HEAD/scripts/release.js" ref="nofollow noopener noreferrer">github1s.com/vuejs/vue-n…</a> 。</p>
<p>仓库克隆下来，运行 <code>yarn</code> 安装好依赖。</p>
<p>在 <code>package.json</code> 中有一个 <code>release</code> script 用来运行这个文件：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"release"</span>: <span class="hljs-string">"node scripts/release.js"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照川哥的说明，可以加个 <code>--dry</code>（空跑） 参数，不执行测试和编译，不执行 git 推送等操作。</p>
<p>然后就可以直接在 <code>package.json</code> 文件的 <code>scripts</code> 上方按 Debug 按钮开始调试。</p>
<p>首先运行一遍看看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68e599b7dfa8488099198cb8bcaacdfc~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43526f80a96c4287a99872b9ab97c325~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c13e622d5ba24377a9842c4ff496e716~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到测试和 build 直接跳过了，commit 和 push 部分都是 <code>[dryrun]</code>，说明也是直接跳过了（只打印了一下如果不是 dryrun 会运行啥）。</p>
<p>运行完之后，会发现 <code>CHANGELOG.md</code> 加上了自上一个 release 以来所有的 commit （但是 chore 这种用户不关心的 commit 的被忽略掉了）:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b548fbe6d174fb2ab93752b1a65212c~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为整个项目是一个是 monorepo，所有 package 的 <code>package.json</code> 中自身的版本号和其依赖的内部包的版本号都被正确更新了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b56a085e89b842a59642f27c1f2bf8e8~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们来分析源代码。</p>
<h2 data-id="heading-2">依赖包</h2>
<p>前面几行是脚本依赖的所有包，下面分别详细了解一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> args = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>))
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>)
<span class="hljs-keyword">const</span> semver = <span class="hljs-built_in">require</span>(<span class="hljs-string">'semver'</span>)
<span class="hljs-keyword">const</span> currentVersion = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).version
<span class="hljs-keyword">const</span> &#123; prompt &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>)
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">minimist</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/minimist" ref="nofollow noopener noreferrer">www.npmjs.com/package/min…</a></p>
<p>主要用来解析命令行参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> argv = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>));
<span class="hljs-built_in">console</span>.log(argv);
<span class="copy-code-btn">复制代码</span></code></pre>
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
<p>可以看到返回值 <code>argv</code> 中，<code>_</code> 为所有不是 option 的输入组成的数组，而 option 的输入都是用 <code>argv['option']=value</code> 的形式保存。</p>
<p>类似的包还有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fyargs" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/yargs" ref="nofollow noopener noreferrer">yargs</a></p>
<h3 data-id="heading-4">chalk</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fchalk" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/chalk" ref="nofollow noopener noreferrer">www.npmjs.com/package/cha…</a></p>
<p>主要用来给字符串加上颜色修饰。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>);

<span class="hljs-comment">// 套一个 chalk.blue 打印出来就是蓝色的了</span>
<span class="hljs-built_in">console</span>.log(chalk.blue(<span class="hljs-string">'Hello world!'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">semver</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fsemver" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/semver" ref="nofollow noopener noreferrer">www.npmjs.com/package/sem…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/" ref="nofollow noopener noreferrer">语义化版本（Semantic Versioning）</a>辅助包，有一些版本号的一些判断和处理逻辑。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> semver = <span class="hljs-built_in">require</span>(<span class="hljs-string">'semver'</span>)

semver.valid(<span class="hljs-string">'1.2.3'</span>) <span class="hljs-comment">// '1.2.3'</span>
semver.valid(<span class="hljs-string">'a.b.c'</span>) <span class="hljs-comment">// null</span>
semver.clean(<span class="hljs-string">'  =v1.2.3   '</span>) <span class="hljs-comment">// '1.2.3'</span>
semver.satisfies(<span class="hljs-string">'1.2.3'</span>, <span class="hljs-string">'1.x || >=2.5.0 || 5.0.0 - 7.2.3'</span>) <span class="hljs-comment">// true</span>
semver.gt(<span class="hljs-string">'1.2.3'</span>, <span class="hljs-string">'9.8.7'</span>) <span class="hljs-comment">// false</span>
semver.lt(<span class="hljs-string">'1.2.3'</span>, <span class="hljs-string">'9.8.7'</span>) <span class="hljs-comment">// true</span>
semver.minVersion(<span class="hljs-string">'>=1.0.0'</span>) <span class="hljs-comment">// '1.0.0'</span>
<span class="hljs-comment">// coerce 用来将输入强制转换为 semver 对象</span>
semver.valid(semver.coerce(<span class="hljs-string">'v2'</span>)) <span class="hljs-comment">// '2.0.0'</span>
semver.valid(semver.coerce(<span class="hljs-string">'42.6.7.9.3-alpha'</span>)) <span class="hljs-comment">// '42.6.7'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">enquirer</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fenquirer" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/enquirer" ref="nofollow noopener noreferrer">www.npmjs.com/package/enq…</a></p>
<p>主要用来进行命令行的交互式输入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; prompt &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>);

<span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> prompt(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'username'</span>,
  <span class="hljs-attr">message</span>: <span class="hljs-string">'What is your username?'</span>
&#125;);

<span class="hljs-built_in">console</span>.log(response); <span class="hljs-comment">// &#123; username: 'jonschlinkert' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">execa</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fexeca" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/execa" ref="nofollow noopener noreferrer">www.npmjs.com/package/exe…</a></p>
<p>跟 nodejs 自带的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fchild_process.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/child_process.html" ref="nofollow noopener noreferrer"><code>child_process</code></a> 包功能差不多，但是更加易用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>);

(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> &#123;stdout&#125; = <span class="hljs-keyword">await</span> execa(<span class="hljs-string">'echo'</span>, [<span class="hljs-string">'unicorns'</span>]);
    <span class="hljs-built_in">console</span>.log(stdout);
    <span class="hljs-comment">//=> 'unicorns'</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">获取配置信息</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> currentVersion = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).version
<span class="hljs-comment">// semver.prerelease('1.2.3-alpha.1') -> ['alpha', 1]</span>
<span class="hljs-keyword">const</span> preId =
  args.preid ||
  (semver.prerelease(currentVersion) && semver.prerelease(currentVersion)[<span class="hljs-number">0</span>])
<span class="hljs-keyword">const</span> isDryRun = args.dry
<span class="hljs-keyword">const</span> skipTests = args.skipTests
<span class="hljs-keyword">const</span> skipBuild = args.skipBuild
<span class="hljs-comment">// 获取所有子 package 的名称，过滤掉 .ts 文件和隐藏文件</span>
<span class="hljs-keyword">const</span> packages = fs
  .readdirSync(path.resolve(__dirname, <span class="hljs-string">'../packages'</span>))
  .filter(<span class="hljs-function"><span class="hljs-params">p</span> =></span> !p.endsWith(<span class="hljs-string">'.ts'</span>) && !p.startsWith(<span class="hljs-string">'.'</span>))

<span class="hljs-comment">// 跳过的包，这里写死成了空数组，后面也没有增加，应该没用</span>
<span class="hljs-keyword">const</span> skippedPackages = []

<span class="hljs-comment">// 后续交互式输入的时候可供选择的升级选项</span>
<span class="hljs-keyword">const</span> versionIncrements = [
  <span class="hljs-string">'patch'</span>,
  <span class="hljs-string">'minor'</span>,
  <span class="hljs-string">'major'</span>,
  ...(preId ? [<span class="hljs-string">'prepatch'</span>, <span class="hljs-string">'preminor'</span>, <span class="hljs-string">'premajor'</span>, <span class="hljs-string">'prerelease'</span>] : [])
]

<span class="hljs-comment">// 下面都是一些辅助函数了</span>
<span class="hljs-comment">// inc 函数给定发布类型，返回新的版本号</span>
<span class="hljs-comment">// semver.inc('1.2.3', 'prerelease', 'beta') -> '1.2.4-beta.0'</span>
<span class="hljs-keyword">const</span> inc = <span class="hljs-function"><span class="hljs-params">i</span> =></span> semver.inc(currentVersion, i, preId)
<span class="hljs-keyword">const</span> bin = <span class="hljs-function"><span class="hljs-params">name</span> =></span> path.resolve(__dirname, <span class="hljs-string">'../node_modules/.bin/'</span> + name)
<span class="hljs-comment">// 运行任意可执行文件</span>
<span class="hljs-keyword">const</span> run = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  execa(bin, args, &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>, ...opts &#125;)
<span class="hljs-comment">// 空跑：打印一下运行参数，不实际运行</span>
<span class="hljs-keyword">const</span> dryRun = <span class="hljs-function">(<span class="hljs-params">bin, args, opts = &#123;&#125;</span>) =></span>
  <span class="hljs-built_in">console</span>.log(chalk.blue(<span class="hljs-string">`[dryrun] <span class="hljs-subst">$&#123;bin&#125;</span> <span class="hljs-subst">$&#123;args.join(<span class="hljs-string">' '</span>)&#125;</span>`</span>), opts)
<span class="hljs-keyword">const</span> runIfNotDry = isDryRun ? dryRun : run
<span class="hljs-keyword">const</span> getPkgRoot = <span class="hljs-function"><span class="hljs-params">pkg</span> =></span> path.resolve(__dirname, <span class="hljs-string">'../packages/'</span> + pkg)
<span class="hljs-keyword">const</span> step = <span class="hljs-function"><span class="hljs-params">msg</span> =></span> <span class="hljs-built_in">console</span>.log(chalk.cyan(msg))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">main 主流程</h3>
<p>主流程分为以下步骤：</p>
<ul>
<li>确定要发布的新版本号 <code>targetVersion</code>
<ul>
<li>命令行指定</li>
<li>用户选择 <code>versionIncrements</code> 中的一种得到新版本号</li>
<li>用户自行输入</li>
</ul>
</li>
<li>运行测试</li>
<li>调用 <code>updateVersions</code> 函数更新所有子 package 的版本号，以及相互依赖关系</li>
<li>build 所有 package</li>
<li>运行 <code>yarn changelog</code> 生成 changelog</li>
<li>如果文件有改动，git commit 所有更改</li>
<li>对每个 package 分别调用 <code>publishPackage</code> 函数进行发布
<ul>
<li>另外可以注意到项目根目录对应的包不会被发布，而且其 <code>package.json</code> 根本也没有 <code>name</code> 字段，可以认为它只是一个 monorepo 配置</li>
</ul>
</li>
<li>推送到 GitHub</li>
</ul>
<p>这里调用了两个函数 <code>updateVersions</code> 和 <code>publishPackage</code>，我们后面可以看看具体逻辑。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> targetVersion = args._[<span class="hljs-number">0</span>]

  <span class="hljs-keyword">if</span> (!targetVersion) &#123;
    <span class="hljs-comment">// no explicit version, offer suggestions</span>
    <span class="hljs-keyword">const</span> &#123; release &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'select'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'release'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'Select release type'</span>,
      <span class="hljs-attr">choices</span>: versionIncrements.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;i&#125;</span> (<span class="hljs-subst">$&#123;inc(i)&#125;</span>)`</span>).concat([<span class="hljs-string">'custom'</span>])
    &#125;)

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
      targetVersion = release.match(<span class="hljs-regexp">/\((.*)\)/</span>)[<span class="hljs-number">1</span>]
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (!semver.valid(targetVersion)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`invalid target version: <span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>)
  &#125;

  <span class="hljs-keyword">const</span> &#123; yes &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'confirm'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'yes'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">`Releasing v<span class="hljs-subst">$&#123;targetVersion&#125;</span>. Confirm?`</span>
  &#125;)

  <span class="hljs-keyword">if</span> (!yes) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// run tests before release</span>
  step(<span class="hljs-string">'\nRunning tests...'</span>)
  <span class="hljs-keyword">if</span> (!skipTests && !isDryRun) &#123;
    <span class="hljs-keyword">await</span> run(bin(<span class="hljs-string">'jest'</span>), [<span class="hljs-string">'--clearCache'</span>])
    <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'test'</span>, <span class="hljs-string">'--bail'</span>])
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`(skipped)`</span>)
  &#125;

  <span class="hljs-comment">// update all package versions and inter-dependencies</span>
  step(<span class="hljs-string">'\nUpdating cross dependencies...'</span>)
  updateVersions(targetVersion)

  <span class="hljs-comment">// build all packages with types</span>
  step(<span class="hljs-string">'\nBuilding all packages...'</span>)
  <span class="hljs-keyword">if</span> (!skipBuild && !isDryRun) &#123;
    <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'build'</span>, <span class="hljs-string">'--release'</span>])
    <span class="hljs-comment">// test generated dts files</span>
    step(<span class="hljs-string">'\nVerifying type declarations...'</span>)
    <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'test-dts-only'</span>])
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`(skipped)`</span>)
  &#125;

  <span class="hljs-comment">// generate changelog</span>
  <span class="hljs-keyword">await</span> run(<span class="hljs-string">`yarn`</span>, [<span class="hljs-string">'changelog'</span>])

  <span class="hljs-keyword">const</span> &#123; stdout &#125; = <span class="hljs-keyword">await</span> run(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'diff'</span>], &#123; <span class="hljs-attr">stdio</span>: <span class="hljs-string">'pipe'</span> &#125;)
  <span class="hljs-keyword">if</span> (stdout) &#123;
    step(<span class="hljs-string">'\nCommitting changes...'</span>)
    <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'add'</span>, <span class="hljs-string">'-A'</span>])
    <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'commit'</span>, <span class="hljs-string">'-m'</span>, <span class="hljs-string">`release: v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'No changes to commit.'</span>)
  &#125;

  <span class="hljs-comment">// publish packages</span>
  step(<span class="hljs-string">'\nPublishing packages...'</span>)
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pkg <span class="hljs-keyword">of</span> packages) &#123;
    <span class="hljs-keyword">await</span> publishPackage(pkg, targetVersion, runIfNotDry)
  &#125;

  <span class="hljs-comment">// push to GitHub</span>
  step(<span class="hljs-string">'\nPushing to GitHub...'</span>)
  <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'tag'</span>, <span class="hljs-string">`v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
  <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'push'</span>, <span class="hljs-string">'origin'</span>, <span class="hljs-string">`refs/tags/v<span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>])
  <span class="hljs-keyword">await</span> runIfNotDry(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'push'</span>])

  <span class="hljs-keyword">if</span> (isDryRun) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`\nDry run finished - run git diff to see package changes.`</span>)
  &#125;

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
&#125;

main().catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.error(err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><code>updateVersions</code> 函数</h3>
<p><code>updateVersions</code> 只接收一个 <code>version</code> 参数，因为每一次发布所有 package 的版本号都保持一致，这样简化了处理逻辑，不过即使某个包没有任何更新，也会被更新版本号而发布。</p>
<p>对于根目录和所有的子 package，均使用 <code>updatePackage</code> 函数更新 <code>package.json</code> 文件，会更新 <code>version</code>, <code>dependencies</code> 和 <code>peerDependencies</code> 字段。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateVersions</span>(<span class="hljs-params">version</span>) </span>&#123;
  <span class="hljs-comment">// 1. update root package.json</span>
  updatePackage(path.resolve(__dirname, <span class="hljs-string">'..'</span>), version)
  <span class="hljs-comment">// 2. update all packages</span>
  packages.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> updatePackage(getPkgRoot(p), version))
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updatePackage</span>(<span class="hljs-params">pkgRoot, version</span>) </span>&#123;
  <span class="hljs-keyword">const</span> pkgPath = path.resolve(pkgRoot, <span class="hljs-string">'package.json'</span>)
  <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(pkgPath, <span class="hljs-string">'utf-8'</span>))
  pkg.version = version
  updateDeps(pkg, <span class="hljs-string">'dependencies'</span>, version)
  updateDeps(pkg, <span class="hljs-string">'peerDependencies'</span>, version)
  fs.writeFileSync(pkgPath, <span class="hljs-built_in">JSON</span>.stringify(pkg, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>) + <span class="hljs-string">'\n'</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDeps</span>(<span class="hljs-params">pkg, depType, version</span>) </span>&#123;
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
<h3 data-id="heading-11"><code>publishPackage</code> 函数</h3>
<p><code>publishPackage</code> 用来发布单个 package。</p>
<p>现在 <code>npm i vue</code> 的时候还是默认安装 vue 2，因为从这里可以看到 vue 3 是用的 <code>next</code> 标签来发布的，需要 <code>npm i vue@next</code>。</p>
<p>如果报错已经发过同版本号的包，就跳过。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">publishPackage</span>(<span class="hljs-params">pkgName, version, runIfNotDry</span>) </span>&#123;
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
<h3 data-id="heading-12">自动生成 GitHub Release</h3>
<p>在 git push 之后，根据项目的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2F4d9b651d82d240b5b521b478bb3aabe6b30e37f5%2F.github%2Fworkflows%2Frelease-tag.yml" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/4d9b651d82d240b5b521b478bb3aabe6b30e37f5/.github/workflows/release-tag.yml" ref="nofollow noopener noreferrer">GitHub Action 配置</a>，还会自动根据 tag 标签生成对应的 release 出来，例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fruns%2F3352769524%3Fcheck_suite_focus%3Dtrue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/runs/3352769524?check_suite_focus=true" ref="nofollow noopener noreferrer">release: v3.2.4</a> 得到的 GitHub Release 如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c9a5711a014ae090702ec9b641adb5~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-20" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">总结</h3>
<ul>
<li>感觉代码逻辑非常清晰，善于抽取工具函数，例如 <code>runIfNotDry</code>, <code>getPkgRoot</code> 这些，可以减少代码量</li>
<li>学会了如何使用 <code>semver</code> 包自动生成新的版本号，以后尽量不要再手动地取版本号名称了。</li>
<li>一个 monorepo 下所有子 package 保持统一版本号，操作起来更加简单</li>
</ul></div>  
</div>
            