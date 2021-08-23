
---
title: '团队DevOps之Commitlint配置篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c6189c5d1b4ac9bca638a9b80ad975~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 20:40:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c6189c5d1b4ac9bca638a9b80ad975~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h3 data-id="heading-0">DevOps简介</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c6189c5d1b4ac9bca638a9b80ad975~tplv-k3u1fbpfcp-watermark.image" alt="819128-20190103143926138-1118094955[1].png" loading="lazy" referrerpolicy="no-referrer">
DevOps（Development和Operations的组合词）是一组过程、方法与系统的统称，用于促进开发（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25BA%2594%25E7%2594%25A8%25E7%25A8%258B%25E5%25BA%258F%2F5985445" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F/5985445" ref="nofollow noopener noreferrer">应用程序</a>/软件工程）、技术运营和质量保障（QA）部门之间的沟通、协作与整合，来使得构建、测试、发布软件能够更加地快捷、频繁和可靠。</p>
<h3 data-id="heading-1">DevOps流程步骤</h3>
<p>DevOps的应用场景往往是一个庞大复杂的背景和流程的场景，，以 IT 自动化以及持续集成（CI）、持续部署（CD）为基础，来优化程式开发、测试、系统运维等所有环节，大都包含一个<code>持续交付流水线</code>。</p>
<ul>
<li>开发人员：<code>IDE</code>、<code>Git</code>等开发和编译工具</li>
<li>版本控制系统：<code>分支策略</code>、<code>语义化版本</code></li>
<li>构建服务器：<code>持续集成</code>、<code>代码质量检查</code></li>
<li>工件库：存放浏览器可以直接运行的二进制包</li>
<li>系统的包管理器：编译或测试环境系统上管理二进制包</li>
<li>环境一致性，依赖包的版本，操作系统，浏览器兼容</li>
<li>预发布或生产：预发布环境与生产环境互换（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fnulige%2Farticles%2F10929182.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/nulige/articles/10929182.html" ref="nofollow noopener noreferrer">蓝绿发布</a>，<code>灰度发布</code>，<code>滚动发布</code>）</li>
<li>发布管理：在高程度自动化测试的基础上实践自动化或半自动化（人工介入）部署</li>
<li>开发和生产环境问题管理系统</li>
</ul>
<p>上述每一步骤都是软件开发中的必要环节，每一步都有重要的意义，下图是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Flearn%2Fpaths%2Fevolve-your-devops-practices%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/zh-cn/learn/paths/evolve-your-devops-practices/" ref="nofollow noopener noreferrer">微软开发者Azure DevOps</a>学习的进阶概要图。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1962c8899e4ebe8de58dfecf886332~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">DevOps之Commitlint配置</h3>
<p>为了便于团队开发协同工作，更好的维护项目，Commitlint便油然而生，本文会对目前流行的配置方法进行详细的说明，文中的项目是基于<code>Commitlint</code> + <code>husky</code> + <code>eslint</code>的基础上搭建的，直接上代码。</p>
<h4 data-id="heading-3">查看本地的Node版本号</h4>
<p>原因：<strong>@commitlint</strong>最新版本仅支持<code>Node>=12</code>，husky最新版本也仅支持<code>Node>=12</code>。</p>
<pre><code class="hljs language-command.js copyable" lang="command.js">PS C:\Windows\system32> node -v
v14.15.0
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">初始化项目</h4>
<pre><code class="hljs language-command.js copyable" lang="command.js">E:\组件库\demo\devops>git clone https://gitee.com/zhaotao27/commitlint-husky-demo.git
Cloning into 'commitlint-husky-demo'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Or 这样创建项目</p>
<pre><code class="hljs language-command.js copyable" lang="command.js">E:\组件库\demo\devops>npm init -y
Wrote to E:\组件库\demo\devops\package.json:
&#123;
  "name": "commitlint-husky-demo",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "repository": &#123;
    "type": "git",
    "url": "https://gitee.com/zhaotao27/commitlint-husky-demo.git"
  &#125;,
  "keywords": [],
  "author": "",
  "license": "ISC"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">在项目中安装@commitlint/config-conventional @commitlint/cli</h4>
<pre><code class="hljs language-npm.js copyable" lang="npm.js">npm install --save-dev @commitlint/config-conventional @commitlint/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">在项目根目录生成项目配置的commitlint.config.js</h4>
<pre><code class="hljs language-bash.sh copyable" lang="bash.sh">echo module.exports = &#123;extends: ['@commitlint/config-conventional']&#125; > commitlint.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">默认的commitlint.config</h4>
<pre><code class="hljs language-commitlint.config.js copyable" lang="commitlint.config.js">module.exports = &#123;
  extends: ['@commitlint/config-conventional']
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">安装其他依赖包</h4>
<p>作用：<code>commitizen</code>规范化提交标准 <code>cz-conventional-changelog-zh</code>中文版的提交规范提示</p>
<pre><code class="copyable">npm install husky commitizen cz-conventional-changelog-zh conventional-changelog-cli --save-dev 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">package.json 配置</h4>
<pre><code class="hljs language-package.json copyable" lang="package.json">"config": &#123;
    "commitizen": &#123;
      "path": "./node_modules/cz-conventional-changelog-zh"
    &#125;
  &#125;,
"scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "prepare": "npx husky install",
    "lint": "lint-staged",
    "release": "standard-version",
    "commit": "git add . && npm lint && git cz",
    "genlog": "conventional-changelog -p angular -i CHANGELOG.md -s"
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">激活husky配置</h4>
<pre><code class="copyable">E:\组件库\demo\devops\commitlint-husky-demo>npm run prepare
> commitlint-husky-demo@1.0.0 prepare E:\组件库\demo\devops\commitlint-husky-demo
> npx husky install
husky - Git hooks installed
E:\组件库\demo\devops\commitlint-husky-demo>yarn husky add .husky/commit-msg 'npm yarn commitlint --edit $1'
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">commit-msg配置</h5>
<p>说明：<code>npm run lint</code>在代码提交后进行代码格式校验</p>
<pre><code class="hljs language-commit-msg.sh copyable" lang="commit-msg.sh">#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npm run lint && npx --no-install commitlint --edit $1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">执行命令<code>npm run commit</code></h4>
<pre><code class="copyable">E:\组件库\demo\devops\commitlint-husky-demo>npm run commit
> commitlint-husky-demo@1.0.0 commit E:\组件库\demo\devops\commitlint-husky-demo
> git add . && git cz
warning: LF will be replaced by CRLF in package.json.
The file will have its original line endings in your working directory.
cz-cli@4.2.4, cz-conventional-changelog-zh@0.0.2
? 选择您要提交的更改类型: (Use arrow keys)
> feat:     一个新功能
  fix:      一个bug
  docs:     文档增删改
  style:    样式修改(空白、格式、缺少分号等)
  refactor: 既不修复bug也不添加新功能的更改
  perf:     性能优化
  test:     增加测试
(Move up and down to reveal more choices)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">安装代码检测依赖</h3>
<p>说明：<code>eslint</code> 代码校验， <code>prettier</code> 格式化代码， <code>stylelint</code> 样式解析 ，<code>standard-version</code>版本发布规范</p>
<pre><code class="hljs language-npm.js copyable" lang="npm.js">npm install --save-dev eslint lint-staged prettier standard-version stylelint stylelint-config-standard
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">激活项目的Eslint代码检测</h5>
<pre><code class="copyable">E:\组件库\demo\devops\commitlint-husky-demo>npx eslint --init
√ How would you like to use ESLint? · problems # 代码检测和问题警告
√ What type of modules does your project use? · esm #js模块解析
√ Which framework does your project use? · react # 应用React框架
√ Does your project use TypeScript? · No / Yes # 是否用TS
√ Where does your code run? · browser # 浏览器环境
√ What format do you want your config file to be in? · JavaScript # 语言
The config that you've selected requires the following dependencies:
eslint-plugin-react@latest
√ Would you like to install them now with npm? · No / Yes
Installing eslint-plugin-react@latest
+ eslint-plugin-react@7.24.0
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">添加<code>stylelint.config.js</code>文件</h5>
<pre><code class="copyable">module.exports = &#123;
  extends: 'stylelint-config-standard',
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">版本发布命令</h5>
<p>说明： 默认是<code>patch</code>小版本迭代，（<strong>feature</strong> 会更新 <strong>minor</strong>, <strong>bug fix</strong> 会更新 <strong>patch</strong>, <strong>BREAKING CHANGES</strong> 会更新 <strong>major</strong>）</p>
<pre><code class="copyable">E:\组件库\demo\devops\commitlint-husky-demo>npm run release
> commitlint-husky-demo@1.0.1 release E:\组件库\demo\devops\commitlint-husky-demo
> standard-version
√ bumping version in package.json from 1.0.1 to 1.0.2
√ bumping version in package-lock.json from 1.0.1 to 1.0.2
√ outputting changes to CHANGELOG.md
√ committing package-lock.json and package.json and CHANGELOG.md
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">普通Git提交Hooks</h5>
<pre><code class="copyable">E:\组件库\demo\devops\commitlint-husky-demo>git add .
E:\组件库\demo\devops\commitlint-husky-demo>git commit -m "chore: 添加测试脚本文件"
> commitlint-husky-demo@1.0.1 lint E:\组件库\demo\devops\commitlint-husky-demo
> lint-staged
[STARTED] Preparing...
[SUCCESS] Preparing...
[STARTED] Running tasks...
[STARTED] Running tasks for **/*.less
[STARTED] Running tasks for src/**/*.&#123;js,vue&#125;
[SKIPPED] No staged files match **/*.less
[STARTED] prettier --write
[SUCCESS] prettier --write
[SUCCESS] Running tasks for src/**/*.&#123;js,vue&#125;
[SUCCESS] Running tasks...
[STARTED] Applying modifications...
[SUCCESS] Applying modifications...
[STARTED] Cleaning up...
[SUCCESS] Cleaning up...
[master 5f984bb] chore: 添加测试脚本文件
 1 file changed, 3 insertions(+)
 create mode 100644 src/example/test.demo.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">总结</h3>
<p>以上代码均可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fzhaotao27%2Fcommitlint-husky-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/zhaotao27/commitlint-husky-demo" ref="nofollow noopener noreferrer">Gitee</a>代码仓库中查看，如果文中有不对的地方或者没考虑到的请在评论区指出，我会及时的进行补充说明；总的来说进行还是很顺利的，就是在安装<code>Commitlint</code>依赖的时候有版本的问题，前期的<code>Commitlint</code>提交规范也算结束了，后面就开始组件库的正式编码了，<code>Devops</code>的路还很长，<strong>希望和大家一起每次进步一点点，每天都有新收获！</strong></p></div>  
</div>
            