
---
title: '「笔记」基于 lerna 的多包 JavaScript 项目搭建维护'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2792'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 04:33:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=2792'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<blockquote>
<p>这是一篇笔记，审核大大不要推荐到首页！</p>
</blockquote>
<h2 data-id="heading-0">全局安装 lerna</h2>
<pre><code class="hljs language-sh copyable" lang="sh">$ npm install lerna -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">新建一个 git 仓库</h2>
<pre><code class="hljs language-sh copyable" lang="sh">$ git init lerna-repo && <span class="hljs-built_in">cd</span> lerna-repo
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">初始化 lerna 项目</h2>
<pre><code class="hljs language-sh copyable" lang="sh">$ lerna init --independent
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你的代码仓库目前应该是如下结构：</p>
<pre><code class="copyable">lerna-repo/
  packages/
  package.json
  lerna.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">创建 package</h2>
<pre><code class="hljs language-sh copyable" lang="sh">$ lerna create module-1
$ lerna create module-2
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">yarn workspaces & Lerna Hoisting</h2>
<p>使用 <a href="https://yarnpkg.com/lang/zh-Hans/docs/workspaces/" target="_blank" rel="nofollow noopener noreferrer">yarn workspaces</a> 结合 Lerna useWorkspaces 可以实现 <a href="https://github.com/lerna/lerna/blob/main/doc/hoist.md" target="_blank" rel="nofollow noopener noreferrer">Lerna Hoisting</a>。这并不是多此一举，这可以让你在统一的地方（根目录）管理依赖，这即节省时间又节省空间。</p>
<p>配置 lerna.json:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  ...
  <span class="hljs-attr">"npmClient"</span>: <span class="hljs-string">"yarn"</span>,
  <span class="hljs-attr">"useWorkspaces"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顶级 package.json 必须包含一个 workspaces 数组:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
  ...
  <span class="hljs-attr">"workspaces"</span>: [<span class="hljs-string">"packages/*"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">npm registry</h2>
<h3 data-id="heading-6">搭建 verdaccio</h3>
<blockquote>
<p>verdaccio 是一个开源轻量的 npm 私服</p>
</blockquote>
<p>全局安装：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ npm install verdaccio -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置 <code>~/.config/verdaccio/config.yaml</code> uplinks:</p>
<pre><code class="copyable">...
# a list of other known repositories we can talk to
uplinks:
  npmjs:
    url: https://registry.npmjs.org/
  taobao:
    url: https://registry.npm.taobao.org/
  tuya:
    url: https://registry-npm.tuya-inc.top/
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">设置开机自启动</h3>
<p>0、run <code>sudo npm i -g pm2</code></p>
<p>1、run <code>pm2 start verdaccio</code> & <code>pm2 startup</code></p>
<p>outputs:</p>
<pre><code class="hljs language-sh copyable" lang="sh">[PM2] Init System found: launchd
[PM2] To setup the Startup Script, copy/paste the following <span class="hljs-built_in">command</span>:
sudo env PATH=<span class="hljs-variable">$PATH</span>:/usr/<span class="hljs-built_in">local</span>/bin /usr/<span class="hljs-built_in">local</span>/lib/node_modules/pm2/bin/pm2 startup launchd -u luozhu --hp /Users/luozhu
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、run <code>sudo env PATH=$PATH:/usr/local/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup launchd -u luozhu --hp /Users/luozhu</code></p>
<p>outputs:</p>
<pre><code class="hljs language-sh copyable" lang="sh">[PM2] Freeze a process list on reboot via:
$ pm2 save

[PM2] Remove init script via:
$ pm2 unstartup launchd
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">修改 lerna publishConfig</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// lerna.json</span>
&#123;
  <span class="hljs-attr">"command"</span>: &#123;
    <span class="hljs-attr">"publish"</span>: &#123;
      <span class="hljs-attr">"ignoreChanges"</span>: [<span class="hljs-string">"ignored-file"</span>, <span class="hljs-string">"*.md"</span>],
      <span class="hljs-attr">"message"</span>: <span class="hljs-string">"chore(release): publish %s"</span>,
      <span class="hljs-attr">"registry"</span>: <span class="hljs-string">"http://localhost:4873"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 各 package 的 package.json</span>
&#123;
  <span class="hljs-attr">"publishConfig"</span>: &#123;
    <span class="hljs-attr">"registry"</span>: <span class="hljs-string">"http://localhost:4873"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">commitlint & commitizen</h2>
<blockquote>
<p>请参考我之前的文章 <a href="https://juejin.im/post/6877462747631026190" target="_blank" rel="nofollow noopener noreferrer">一文搞定规范化 Git Commit</a></p>
</blockquote>
<h2 data-id="heading-10">开发流程</h2>
<h3 data-id="heading-11">install</h3>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn install
<span class="hljs-comment"># or</span>
$ lerna bootstrap
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">package 依赖</h3>
<p>给指定 package 安装依赖：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn workspace module-1 add lodash
<span class="hljs-comment"># or</span>
$ lerna add lodash --scope module-1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给所有 package 安装依赖：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn workspaces add dayjs
<span class="hljs-comment"># or</span>
$ lerna add dayjs
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">workspace 依赖</h3>
<pre><code class="hljs language-sh copyable" lang="sh">$ lerna add module-2 --scope module-1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">共用的工具依赖</h3>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn add -W -D typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">lerna.json</h2>
<ul>
<li>version: 当前仓库的版本，Independent mode 请设置为 <code>independent</code></li>
<li>npmClient: 指定运行命令的客户端程序（默认是 npm）</li>
<li>ignoreChanges: 一个不包含在 <code>lerna changed/publish</code> 的 glob 数组。使用这个去阻止发布不必要的更新，比如修复 <code>README.md</code></li>
<li>command
<ul>
<li>publish
<ul>
<li>message: 一个 publish 时的自定义 commit 信息。详情请查看<a href="https://github.com/lerna/lerna/blob/main/commands/version#--message-msg" target="_blank" rel="nofollow noopener noreferrer">@lerna/version</a></li>
<li>registry: 设置自定义的 npm 代理（比如使用 verdaccio 搭建的私服）</li>
</ul>
</li>
<li>version
<ul>
<li>conventionalCommits: <code>lerna version</code> 会自动决定 version bump 和生成 CHANGELOG 文件</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-16">npm scripts</h2>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"release:beta"</span>: <span class="hljs-string">"lerna publish --canary --pre-dist-tag=beta --preid=beta --yes"</span>,
    <span class="hljs-attr">"release:rc"</span>: <span class="hljs-string">"lerna publish prerelease --pre-dist-tag=rc --preid=rc"</span>,
    <span class="hljs-attr">"release:next"</span>: <span class="hljs-string">"lerna publish prerelease --pre-dist-tag=next --preid=next"</span>,
    <span class="hljs-attr">"release:preminor"</span>: <span class="hljs-string">"lerna publish preminor --pre-dist-tag=next --preid=next"</span>,
    <span class="hljs-attr">"release:premajor"</span>: <span class="hljs-string">"lerna publish premajor --pre-dist-tag=next --preid=next"</span>,
    <span class="hljs-attr">"release"</span>: <span class="hljs-string">"lerna publish"</span>,
    <span class="hljs-attr">"release:minor"</span>: <span class="hljs-string">"lerna publish minor"</span>,
    <span class="hljs-attr">"release:major"</span>: <span class="hljs-string">"lerna publish major"</span>,
    <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"git cz"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            