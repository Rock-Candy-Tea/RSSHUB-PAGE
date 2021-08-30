
---
title: 'vue3 release 源码解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=664'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 20:32:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=664'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>若川源码解读源地址：<a href="https://juejin.cn/post/6997943192851054606" target="_blank" title="https://juejin.cn/post/6997943192851054606">juejin.cn/post/699794…</a></p>
</blockquote>
<p>感谢若川哥组织的阅读源码活动，收获很大，想加入的小伙伴看过来: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fruochuan12%2Ffnfzu7" title="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fruochuan12%2Ffnfzu7" target="_blank">公告</a></p>
<h2 data-id="heading-0">1. 相关依赖包</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> args = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>))
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>)
<span class="hljs-keyword">const</span> semver = <span class="hljs-built_in">require</span>(<span class="hljs-string">'semver'</span>)
<span class="hljs-keyword">const</span> currentVersion = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).version
<span class="hljs-keyword">const</span> &#123; prompt &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>)
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">minimist</h3>
<p>minimist轻量级的命令行参数解析引擎</p>
<p>解析过程中，minimist会依次匹配不同的模式，从long options到short options，匹配之后再进行相应的解析工作。</p>
<p>其中process.argv的第一和第二个元素是Node可执行文件和被执行JavaScript文件的完全限定的文件系统路径，无论你是否这样输入他们。</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> node example/parse.js -a beep -b boop</span>
&#123; _: [], a: 'beep', b: 'boop' &#125;
<span class="hljs-meta">
$</span><span class="bash"> node example/parse.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz</span>
&#123; _: [ 'foo', 'bar', 'baz' ],
  x: 3,
  y: 4,
  n: 5,
  a: true,
  b: true,
  c: true,
  beep: 'boop' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">chalk</h3>
<p>chalk 包的作用是修改控制台中字符串的样式，包括：</p>
<ol>
<li>字体样式(加粗、隐藏等)</li>
<li>字体颜色</li>
</ol>

<ol start="3">
<li>背景颜色</li>
</ol>
<h3 data-id="heading-3">semver</h3>
<p>语义化版本的nodejs实现，用于版本校验比较等。</p>
<p>semver 定义了两种概念：</p>
<ul>
<li>版本是指例如 0.4.1、1.2.7、1.2.4-beta.0 这样表示包的特定版本的字符串。</li>
<li>范围则是对满足特定规则的版本的一种表示，例如 1.2.3-2.3.4、1.x、^0.2、>1.4.</li>
</ul>
<p>在这两种概念上可以进行很多种计算，例如比较两个版本的大小、判断一个版本是否满足一个范围、判断一个版本是否比范围中的任何版本都大等。</p>
<p>版本格式：主版本号.次版本号.修订号，版本号递增规则如下：<br>
主版本号：当你做了不兼容的 API 修改，<br>
次版本号：当你做了向下兼容的功能性新增，<br>
修订号：当你做了向下兼容的问题修正。<br>
先行版本号及版本编译信息可以加到“主版本号.次版本号.修订号”的后面，作为延伸。</p>
<h3 data-id="heading-4">enquirer</h3>
<p>命令行交互工具，例如发布时选择相关版本号</p>
<h3 data-id="heading-5">execa</h3>
<p>execa是可以调用shell和本地外部程序的javascript封装。会启动子进程执行。支持多操作系统，包括windows。如果父进程退出，则生成的全部子进程都被杀死。</p>
<h2 data-id="heading-6">2. 主要流程解读</h2>
<p>运行下面的命令 <code>yarn release --dry</code>，会控制台会显示发布的整套流程</p>
<pre><code class="hljs language-shell copyable" lang="shell">// 执行测试用例
Running tests...
(skipped)

// 更新依赖版本
Updating cross dependencies...

// 打包编译所有包
Building all packages...

// 生成CHANGELOG.md文件描述
<span class="hljs-meta">$</span><span class="bash"> conventional-changelog -p angular -i CHANGELOG.md -s</span>

// commit代码
Committing changes...

// 发布包
Publishing packages...
Publishing compiler-core...

// 提交到github
Pushing to GitHub...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3. main函数</h2>
<h3 data-id="heading-8">3.1 取版本号</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 根据上文 mini 这句代码意思是 yarn run release 3.2.4 </span>
<span class="hljs-comment">// 取到参数 3.2.4</span>
<span class="hljs-keyword">let</span> targetVersion = args._[<span class="hljs-number">0</span>]

<span class="hljs-comment">// 如果不存在版本号就手动选择相关版本</span>
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
    targetVersion = release.match(<span class="hljs-regexp">/((.*))/</span>)[<span class="hljs-number">1</span>]
  &#125;
&#125;

<span class="hljs-comment">// 校验版本是否符合规范</span>
<span class="hljs-keyword">if</span> (!semver.valid(targetVersion)) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`invalid target version: <span class="hljs-subst">$&#123;targetVersion&#125;</span>`</span>)
&#125;

<span class="hljs-comment">// 确认要 release</span>
<span class="hljs-keyword">const</span> &#123; yes &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'confirm'</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'yes'</span>,
  <span class="hljs-attr">message</span>: <span class="hljs-string">`Releasing v<span class="hljs-subst">$&#123;targetVersion&#125;</span>. Confirm?`</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">运行测试用例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// run tests before release</span>
  step(<span class="hljs-string">'\nRunning tests...'</span>)
  <span class="hljs-keyword">if</span> (!skipTests && !isDryRun) &#123;
    <span class="hljs-keyword">await</span> run(bin(<span class="hljs-string">'jest'</span>), [<span class="hljs-string">'--clearCache'</span>])
    <span class="hljs-keyword">await</span> run(<span class="hljs-string">'yarn'</span>, [<span class="hljs-string">'test'</span>, <span class="hljs-string">'--bail'</span>])
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`(skipped)`</span>)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">更新依赖版本号</h3>
<p>流程：</p>
<ol>
<li>自己本身 package.json 的版本号</li>
<li>packages.json 中 dependencies 中 vue 相关的依赖修改</li>
<li>packages.json 中 peerDependencies 中 vue 相关的依赖修改</li>
</ol>
<pre><code class="copyable">step('\nUpdating cross dependencies...')
updateVersions(targetVersion)

//更新根目录版本号和更新所有依赖package版本
function updateVersions(version) &#123;
  // 1. update root package.json
  updatePackage(path.resolve(__dirname, '..'), version)
  // 2. update all packages
  packages.forEach(p => updatePackage(getPkgRoot(p), version))
&#125;

// 更新版本
function updatePackage(pkgRoot, version) &#123;
  const pkgPath = path.resolve(pkgRoot, 'package.json')
  const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf-8'))
  pkg.version = version
  updateDeps(pkg, 'dependencies', version)
  updateDeps(pkg, 'peerDependencies', version)
  fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2) + '\n')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">打包和编译</h3>
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
<h3 data-id="heading-12">最后流程</h3>
<pre><code class="copyable">// 生成changelog
await run(`yarn`, ['changelog'])

// 运行查看差异，有版本差异就提交
const &#123; stdout &#125; = await run('git', ['diff'], &#123; stdio: 'pipe' &#125;)
if (stdout) &#123;
  step('\nCommitting changes...')
  await runIfNotDry('git', ['add', '-A'])
  await runIfNotDry('git', ['commit', '-m', `release: v$&#123;targetVersion&#125;`])
&#125; else &#123;
  console.log('No changes to commit.')
&#125;

// publish packages
step('\nPublishing packages...')
for (const pkg of packages) &#123;
  await publishPackage(pkg, targetVersion, runIfNotDry)
&#125;

// 发布到github
step('\nPushing to GitHub...')
await runIfNotDry('git', ['tag', `v$&#123;targetVersion&#125;`])
await runIfNotDry('git', ['push', 'origin', `refs/tags/v$&#123;targetVersion&#125;`])
await runIfNotDry('git', ['push'])


// 如果传了这个参数则输出 可以用 git diff 看看更改

// const isDryRun = args.dry
if (isDryRun) &#123;
  console.log(`\nDry run finished - run git diff to see package changes.`)
&#125;

// 如果 跳过的包，则输出以下这些包没有发布。不过代码 `skippedPackages` 里是没有包。
// 所以这段代码也不会执行。
// 我们习惯写 arr.length !== 0 其实 0 就是 false 。可以不写。
if (skippedPackages.length) &#123;
  console.log(
    chalk.yellow(
      `The following packages are skipped and NOT published:\n- $&#123;skippedPackages.join(
        '\n- '
      )&#125;`
    )
  )
&#125;
console.log()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">总结</h2>
<p>通过这次学习:</p>
<ol>
<li>熟悉vue的发布</li>
<li>会调试部分node</li>
<li>学习到一些依赖库的功能作用</li>
</ol></div>  
</div>
            