
---
title: '基于 monorepo 的架构实践总结： vscode 插件及其相关 packages 开发'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0823e275094647a580b5faec3a87d13e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 19:35:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0823e275094647a580b5faec3a87d13e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>GithubBlog：<a href="https://github.com/Nealyang/PersonalBlog/issues/99" target="_blank" rel="nofollow noopener noreferrer">github.com/Nealyang/Pe…</a></p>
<p>背景如是：</p>
<ul>
<li><a href="https://mp.weixin.qq.com/s/JRF4GjYqXw1f6jGqcYofnQ" target="_blank" rel="nofollow noopener noreferrer">pmlci 源码脚手架：https://mp.weixin.qq.com/s/JRF4GjYqXw1f6jGqcYofnQ</a></li>
</ul>
<p>随着脚手架的提供，以及新增页面和模块的功能封装。</p>
<p>毕竟 <strong>多提供一层规范，就多了一层约束。</strong> 而架构的本质是为了让开发者能够将精力更加的focus 到业务的开发中，无需关心其他。比如上述脚手架初始化出来的一些模块配置、异步加载甚至一些已定义并且保留在初始化架构中的一些业务 <code>hooks</code> 等。</p>
<p>如上原因，我希望能够提供一套可视化的操作（创建项目、选择依赖、添加页面，选择所需物料、配置物料属性等），一言以蔽之就是让用户对于源码开发而言，只需要编写对应的业务模块组件，而不需管理架构是如何组织模块和状态分发的，<strong>除了业务模块编码，其他都是可视化操作</strong>。</p>
<p>因为团队里 100%的同学都是以 <code>vscode</code> 作为饭碗，所以自然而然的 <code>vscode extinction</code> 就是我的第一选择了。计划中会提供创建项目、新增页面、模块配置、页面配置、新增模块等一系列插件。后续阶段性进展，再发文总结。咳咳，是的，这将是一个<strong>源码工作台</strong>的赶脚~</p>
<p>截止目前，已经将项目的脚手架基本搭建了个 90% ，此处作为第一阶段性总结。</p>
<h2 data-id="heading-1">成果展示</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0823e275094647a580b5faec3a87d13e~tplv-k3u1fbpfcp-zoom-1.image" alt="demo" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8de1d7417454ef493432df406e5a57f~tplv-k3u1fbpfcp-zoom-1.image" alt="项目目录" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>extensions</code> 文件夹为 <code>vscode</code> 插件的文件夹、<code>packages</code> 文件夹是存放公共的组件、<code>scripts</code> 为发布、构建、开发的脚本，其他就是一些工程配置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea4bd35662344697a392408cce2f1cc2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当然，这里最主要不是产品功能的展示，嘎嘎~</p>
</blockquote>
<h3 data-id="heading-2">packages.json scripts</h3>
<pre><code class="hljs language-json copyable" lang="json">
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"publish"</span>: <span class="hljs-string">"lerna list && publish:package"</span>,
    <span class="hljs-attr">"publish-beta"</span>: <span class="hljs-string">"lerna list && npm run publish-beta:package"</span>,
    <span class="hljs-attr">"start"</span>:<span class="hljs-string">"tnpm run start:packages && tnpm run start:extensions"</span>,
    <span class="hljs-attr">"start:packages"</span>: <span class="hljs-string">"tnpm run setup:packages && tnpm run packages:watch"</span>,
    <span class="hljs-attr">"start:extensions"</span>:<span class="hljs-string">"tnpm run extensions:link"</span>,
    <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"git-cz"</span>,
    <span class="hljs-attr">"env"</span>: <span class="hljs-string">"node ./scripts/env.js"</span>,
    <span class="hljs-attr">"packages:link"</span>: <span class="hljs-string">"lerna link"</span>,
    <span class="hljs-attr">"packages:install"</span>: <span class="hljs-string">"rm -rf node_modules && rm -rf ./packages/*/node_modules && rm -rf ./packages/*/package-lock.json && SASS_BINARY_SITE=https://npm.taobao.org/mirrors/node-sass/ yarn install --registry=http://registry.npm.taobao.org"</span>,
    <span class="hljs-attr">"packages:clean"</span>: <span class="hljs-string">"rm -rf ./packages/*/lib"</span>,
    <span class="hljs-attr">"packages:watch"</span>: <span class="hljs-string">"ts-node ./scripts/watch.ts"</span>,
    <span class="hljs-attr">"packages:build"</span>: <span class="hljs-string">"npm run packages:clean && ts-node ./scripts/build.ts"</span>,
    <span class="hljs-attr">"setup:packages"</span>: <span class="hljs-string">"npm run packages:install && lerna clean --yes && npm run packages:build && npm run packages:link "</span>,
    <span class="hljs-attr">"publish-beta:package"</span>: <span class="hljs-string">"ts-node ./scripts/publish-beta-package.ts"</span>,
    <span class="hljs-attr">"publish:package"</span>: <span class="hljs-string">"ts-node ./scripts/publish-package.ts"</span>,
    <span class="hljs-attr">"extensions:install"</span>: <span class="hljs-string">" rm -rf ./extensions/*/node_modules && rm -rf ./extensions/*/package-lock.json && rm -rf ./extensions/*/web/node_modules && rm -rf ./extensions/*/web/package-lock.json && ts-node ./scripts/extension-deps-install.ts"</span>,
    <span class="hljs-attr">"extensions:link"</span>: <span class="hljs-string">"ts-node ./scripts/extension-link-package.ts"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>scripts</code> 没有添加完全，目前开发直接 <code>npm start</code> 发布 <code>packages</code> 分别为 <code>npm run publish-beta:package</code> 、 <code>npm run publish:package</code> ,上面也有 <code>publish</code> 的命令汇总。</p>
<h2 data-id="heading-3">架构选型</h2>
<p>目前是为了将 <code>pmCli</code> 功能全部封装成插件，然后通过可视化替代掉编码过程中关于架构配置的相关操作。所以插件必然不会只有一个，而是一个基于源码架构的一个<strong>操作集</strong>：多 <code>extensions</code>。插件中有非常多的相似功能封装。比如从 <code>gitlab</code> 上读取基础文件、<code>vscode</code> 和 <code>WebView</code> 的通信、<code>AST</code> 的基本封装等，所以必然需要依赖非常多的 <code>packages</code> ，为了开发提效和集合的统一管理，必然想到基于 <code>lerna</code> 的<code>monorepo</code> 的项目结构。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8938508ef7904e6d8288a65e09dbaa7e~tplv-k3u1fbpfcp-zoom-1.image" alt="网图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中关于 lerna 的一些采坑就不多说了，主要是我也只是看了市面上大部分的实践文章和官方文档，缺乏一些自己实践（毕竟感觉研究多也解决不了多大的痛点，就不想花精力了）最终的 <code>monorepo</code> 是基于 <code>yarn workspace</code> 实现的，通过 <code>lerna link</code> 来软链<code>package</code>、<code>lerna</code> 的发布 <code>package</code> 比较鸡肋，就参考 <code>App works</code> 自己写了一些打包发布到预发、线上的脚本。</p>
<p>项目工作流以及编码约束通过<code>husky</code>、<code>lint-staged</code>、<code>git-cz</code>、 <code>eslint</code>、<code>prettier</code>等常规配置。</p>
<p>编码采用 <code>ts</code> 编码，所以对于 <code>extensions</code> 以及 <code>packages</code> 中都有很多公共的配置，这里可以提取出来公共部分放置到项目根目录下（如上项目目录截图）。</p>
<h2 data-id="heading-4">实践</h2>
<p>通过 <code>lerna init</code>、<code>lerna create xxx</code> 来初始化这里就不说了。反正完事以后就是带有一个<code>packages</code> 和 <code>package.json</code> 文件的一个目录结构。</p>
<h3 data-id="heading-5">项目架构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7762ce2172b5424a8c0e7098219dea75~tplv-k3u1fbpfcp-zoom-1.image" alt="项目结构" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">package结构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/774133835c0f42eda90610a831d1ff92~tplv-k3u1fbpfcp-zoom-1.image" alt="package" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>以上结构说明都在图片里了</p>
</blockquote>
<h3 data-id="heading-7">脚本封装</h3>
<p>在项目的根目录下放置了一个 <code>scripts</code> 文件夹，存放着一些发布、开发以及依赖的安装的脚本啥的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/294d6566912b474ebfca0c489f602648~tplv-k3u1fbpfcp-zoom-1.image" alt="scripts" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">getPakcageInfo.ts</h4>
<blockquote>
<p>用于从 <code>packages</code> 中获取相关 <code>publish</code> 信息。其中<code>shouldPublish</code>是将本地 <code>version</code> 和线上 <code>version</code> 对比，判断师傅需要执行 <code>publish</code> 的</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/*
 * @Author: 一凨
 * @Date: 2021-06-07 18:47:32
 * @Last Modified by: 一凨
 * @Last Modified time: 2021-06-07 19:12:28
 */</span>
<span class="hljs-keyword">import</span> &#123; existsSync, readdirSync, readFileSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> &#123; join &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> &#123; getLatestVersion &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ice-npm-utils'</span>;

<span class="hljs-keyword">const</span> TARGET_DIRECTORY = join(__dirname, <span class="hljs-string">'../../packages'</span>);
<span class="hljs-comment">// 定义需要获取到的信息结构</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> IPackageInfo &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  directory: <span class="hljs-built_in">string</span>;
  localVersion: <span class="hljs-built_in">string</span>;
  mainFile: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// package.json main file</span>
  shouldPublish: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="hljs-comment">// 检查 package 是否 build 成功</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkBuildSuccess</span>(<span class="hljs-params">directory: <span class="hljs-built_in">string</span>, mainFile: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> existsSync(join(directory, mainFile));
&#125;
<span class="hljs-comment">// 判断线上最新version是否和本地 version 相同</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkVersionExists</span>(<span class="hljs-params">pkg: <span class="hljs-built_in">string</span>, version: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">boolean</span>> </span>&#123;
  <span class="hljs-keyword">return</span> getLatestVersion(pkg)
    .then(<span class="hljs-function">(<span class="hljs-params">latestVersion</span>) =></span> version === latestVersion)
    .catch(<span class="hljs-function">() =></span> <span class="hljs-literal">false</span>);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPackageInfos</span> (<span class="hljs-params"></span>):<span class="hljs-title">Promise</span><<span class="hljs-title">IPackageInfo</span>[]></span>&#123;
  <span class="hljs-keyword">const</span> packageInfos: IPackageInfo[] = [];
  <span class="hljs-keyword">if</span> (!existsSync(TARGET_DIRECTORY)) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[ERROR] Directory <span class="hljs-subst">$&#123;TARGET_DIRECTORY&#125;</span> not exist!`</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 拿到所有packages 目录，再去遍历其 package.json</span>
    <span class="hljs-keyword">const</span> packageFolders: <span class="hljs-built_in">string</span>[] = readdirSync(TARGET_DIRECTORY).filter(<span class="hljs-function">(<span class="hljs-params">filename</span>) =></span> filename[<span class="hljs-number">0</span>] !== <span class="hljs-string">'.'</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[PUBLISH] Start check with following packages:'</span>);
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(
      packageFolders.map(<span class="hljs-keyword">async</span> (packageFolder) => &#123;
        <span class="hljs-keyword">const</span> directory = join(TARGET_DIRECTORY, packageFolder);
        <span class="hljs-keyword">const</span> packageInfoPath = join(directory, <span class="hljs-string">'package.json'</span>);

        <span class="hljs-comment">// Process package info.</span>
        <span class="hljs-keyword">if</span> (existsSync(packageInfoPath)) &#123;
          <span class="hljs-keyword">const</span> packageInfo = <span class="hljs-built_in">JSON</span>.parse(readFileSync(packageInfoPath, <span class="hljs-string">'utf8'</span>));
          <span class="hljs-keyword">const</span> packageName = packageInfo.name || packageFolder;

          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`- <span class="hljs-subst">$&#123;packageName&#125;</span>`</span>);
<span class="hljs-comment">// 从 package.json 中取信息 返回</span>
          <span class="hljs-keyword">try</span> &#123;
            packageInfos.push(&#123;
              <span class="hljs-attr">name</span>: packageName,
              directory,
              <span class="hljs-attr">localVersion</span>: packageInfo.version,
              <span class="hljs-attr">mainFile</span>: packageInfo.main,
              <span class="hljs-comment">// If localVersion not exist, publish it</span>
              <span class="hljs-attr">shouldPublish</span>:
                checkBuildSuccess(directory, packageInfo.main) &&
                !(<span class="hljs-keyword">await</span> checkVersionExists(packageName, packageInfo.version)),
            &#125;);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[ERROR] get <span class="hljs-subst">$&#123;packageName&#125;</span> information failed: `</span>, e);
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[ERROR] <span class="hljs-subst">$&#123;packageFolder&#125;</span>'s package.json not found.`</span>);
        &#125;
      &#125;),
    );
  &#125;
  <span class="hljs-keyword">return</span> packageInfos;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码的解释都在注释里了，核心做的事情就是，从 <code>packages</code> 中读取每一个 <code>package</code> 的 <code>package.json</code> 中的信息，然后组成需要的格式返回出去，用于发布。</p>
<h4 data-id="heading-9">publish-beta-package</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/*
 * @Author: 一凨
 * @Date: 2021-06-07 18:45:51
 * @Last Modified by: 一凨
 * @Last Modified time: 2021-06-07 19:29:26
 */</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;
<span class="hljs-keyword">import</span> &#123; spawnSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'child_process'</span>;
<span class="hljs-keyword">import</span> &#123; IPackageInfo, getPackageInfos &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./fn/getPackageInfos'</span>;

<span class="hljs-keyword">const</span> BETA_REG = <span class="hljs-regexp">/([^-]+)-beta\.(\d+)/</span>; <span class="hljs-comment">// '1.0.0-beta.1'</span>

<span class="hljs-keyword">interface</span> IBetaPackageInfo <span class="hljs-keyword">extends</span> IPackageInfo &#123;
  <span class="hljs-attr">betaVersion</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setBetaVersionInfo</span>(<span class="hljs-params">packageInfo: IPackageInfo</span>): <span class="hljs-title">IBetaPackageInfo</span> </span>&#123;
  <span class="hljs-keyword">const</span> &#123; name, localVersion &#125; = packageInfo;

  <span class="hljs-keyword">let</span> version = localVersion;

  <span class="hljs-keyword">if</span> (!BETA_REG.test(localVersion)) &#123;
    <span class="hljs-comment">// 如果 localVersion 不是 beta version，则盘他！</span>
    <span class="hljs-keyword">let</span> betaVersion = <span class="hljs-number">1</span>;
    <span class="hljs-comment">// 获取package 的 dist-tag 相关信息</span>
    <span class="hljs-keyword">const</span> childProcess = spawnSync(<span class="hljs-string">'npm'</span>, [<span class="hljs-string">'show'</span>, name, <span class="hljs-string">'dist-tags'</span>, <span class="hljs-string">'--json'</span>], &#123;
      <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>,
    &#125;);

    <span class="hljs-keyword">const</span> distTags = <span class="hljs-built_in">JSON</span>.parse(childProcess.stdout || <span class="hljs-string">"&#123;&#125;"</span>) || &#123;&#125;;
    <span class="hljs-keyword">const</span> matched = (distTags.beta || <span class="hljs-string">''</span>).match(BETA_REG);

    <span class="hljs-comment">// 1.0.0-beta.1 -> ["1.0.0-beta.1", "1.0.0", "1"] -> 1.0.0-beta.2</span>
    <span class="hljs-keyword">if</span> (matched && matched[<span class="hljs-number">1</span>] === localVersion && matched[<span class="hljs-number">2</span>]) &#123;
      <span class="hljs-comment">// 盘 version，+1</span>
      betaVersion = <span class="hljs-built_in">Number</span>(matched[<span class="hljs-number">2</span>]) + <span class="hljs-number">1</span>;
    &#125;
    version += <span class="hljs-string">`-beta.<span class="hljs-subst">$&#123;betaVersion&#125;</span>`</span>;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, packageInfo, &#123; <span class="hljs-attr">betaVersion</span>: version &#125;);
&#125;

<span class="hljs-comment">// 将矫正后的 betaVersion 写到对应 package.json 中</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updatePackageJson</span>(<span class="hljs-params">betaPackageInfos: IBetaPackageInfo[]</span>): <span class="hljs-title">void</span> </span>&#123;
  betaPackageInfos.forEach(<span class="hljs-function">(<span class="hljs-params">betaPackageInfo: IBetaPackageInfo</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; directory, betaVersion &#125; = betaPackageInfo;

    <span class="hljs-keyword">const</span> packageFile = path.join(directory, <span class="hljs-string">'package.json'</span>);
    <span class="hljs-keyword">const</span> packageData = fs.readJsonSync(packageFile);

    packageData.version = betaVersion;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < betaPackageInfos.length; i++) &#123;
      <span class="hljs-keyword">const</span> dependenceName = betaPackageInfos[i].name;
      <span class="hljs-keyword">const</span> dependenceVersion = betaPackageInfos[i].betaVersion;

      <span class="hljs-keyword">if</span> (packageData.dependencies && packageData.dependencies[dependenceName]) &#123;
        packageData.dependencies[dependenceName] = dependenceVersion;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (packageData.devDependencies && packageData.devDependencies[dependenceName]) &#123;
        packageData.devDependencies[dependenceName] = dependenceVersion;
      &#125;
    &#125;

    fs.writeFileSync(packageFile, <span class="hljs-built_in">JSON</span>.stringify(packageData, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));
  &#125;);
&#125;
<span class="hljs-comment">// npm publish --tag=beta 发布</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">publish</span>(<span class="hljs-params">pkg: <span class="hljs-built_in">string</span>, betaVersion: <span class="hljs-built_in">string</span>, directory: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[PUBLISH BETA]'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;pkg&#125;</span>@<span class="hljs-subst">$&#123;betaVersion&#125;</span>`</span>);
  spawnSync(<span class="hljs-string">'npm'</span>, [<span class="hljs-string">'publish'</span>, <span class="hljs-string">'--tag=beta'</span>], &#123;
    <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>,
    <span class="hljs-attr">cwd</span>: directory,
  &#125;);
&#125;

<span class="hljs-comment">// 入口文件</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[PUBLISH BETA] Start:'</span>);
getPackageInfos().then(<span class="hljs-function">(<span class="hljs-params">packageInfos: IPackageInfo[]</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> shouldPublishPackages = packageInfos
    .filter(<span class="hljs-function">(<span class="hljs-params">packageInfo</span>) =></span> packageInfo.shouldPublish)
    .map(<span class="hljs-function">(<span class="hljs-params">packageInfo</span>) =></span> setBetaVersionInfo(packageInfo));

  updatePackageJson(shouldPublishPackages);

  <span class="hljs-comment">// Publish</span>
  <span class="hljs-keyword">let</span> publishedCount = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> publishedPackages = [];


  shouldPublishPackages.forEach(<span class="hljs-function">(<span class="hljs-params">packageInfo</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; name, directory, betaVersion &#125; = packageInfo;
    publishedCount++;
    <span class="hljs-comment">// 打印此次发布的相关信息</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`--- <span class="hljs-subst">$&#123;name&#125;</span>@<span class="hljs-subst">$&#123;betaVersion&#125;</span> ---`</span>);
    publish(name, betaVersion, directory);
    publishedPackages.push(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>:<span class="hljs-subst">$&#123;betaVersion&#125;</span>`</span>);
  &#125;);

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[PUBLISH PACKAGE BETA] Complete (count=<span class="hljs-subst">$&#123;publishedCount&#125;</span>):`</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;publishedPackages.join(<span class="hljs-string">'\n'</span>)&#125;</span>`</span>);

&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本功能都在注释里了（这句话后面不赘述了），总结次脚本作用：</p>
<ul>
<li>拿到所有的本地 packageInfo 信息</li>
<li>对比线上（已发布）信息，纠正此次发布需要的版本信息</li>
<li>将纠正的版本信息补充道（写入）本地对应的 package 中的 package.json 中</li>
<li>调用脚本，执行发布</li>
</ul>
<blockquote>
<p><code>publish-package</code> 就非常简单了，写的也比较简单，就是调用 <code>npm publish</code> ，当然，也需要一些基本的线上校验，比如上述的 <code>shouldPublish</code>。不赘述了！</p>
<p>需要注意的是，发布的时候，需要注意登陆（<code>npm whoami</code>）以及如果你也是采用<code>@xxx/</code>的命名方式的话，注意对应 <code>organization</code>的权限</p>
</blockquote>
<h4 data-id="heading-10">watch</h4>
<p>主要借助 nsfw 的能力对本地文件进行监听。<strong>有变动，咱编译就完事了！</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"> <span class="hljs-comment">/*
 * @Author: 一凨
 * @Date: 2021-06-07 20:16:09
 * @Last Modified by: 一凨
 * @Last Modified time: 2021-06-10 17:19:05
 */</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> glob <span class="hljs-keyword">from</span> <span class="hljs-string">'glob'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;
<span class="hljs-keyword">import</span> &#123; run &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./fn/shell'</span>;


<span class="hljs-comment">// eslint-disable-next-line @typescript-eslint/no-var-requires</span>
<span class="hljs-keyword">const</span> nsfw = <span class="hljs-built_in">require</span>(<span class="hljs-string">'nsfw'</span>);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watchFiles</span>(<span class="hljs-params">cwd, ext</span>) </span>&#123;
  <span class="hljs-keyword">const</span> files = glob.sync(ext, &#123; cwd, <span class="hljs-attr">nodir</span>: <span class="hljs-literal">true</span> &#125;);

  <span class="hljs-keyword">const</span> fileSet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
  <span class="hljs-comment">/* eslint no-restricted-syntax:0 */</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> file <span class="hljs-keyword">of</span> files) &#123;
    <span class="hljs-comment">/* eslint no-await-in-loop:0 */</span>
    <span class="hljs-keyword">await</span> copyOneFile(file, cwd);
    fileSet.add(path.join(cwd, file));
  &#125;

  <span class="hljs-keyword">const</span> watcher = <span class="hljs-keyword">await</span> nsfw(cwd, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
    event.forEach(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (
        e.action === nsfw.actions.CREATED ||
        e.action === nsfw.actions.MODIFIED ||
        e.action === nsfw.actions.RENAMED
      ) &#123;
        <span class="hljs-keyword">const</span> filePath = e.newFile ? path.join(e.directory, e.newFile!) : path.join(e.directory, e.file!);
        <span class="hljs-keyword">if</span> (fileSet.has(filePath)) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'non-ts change detected:'</span>, filePath);
          copyOneFile(path.relative(cwd, filePath), cwd);
        &#125;
      &#125;
    &#125;);
  &#125;);
  watcher.start();
&#125;

watchFiles(path.join(__dirname, <span class="hljs-string">'../packages'</span>), <span class="hljs-string">'*/src/**/!(*.ts|*.tsx)'</span>).catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.trace(e);
  process.exit(<span class="hljs-number">128</span>);
&#125;);

<span class="hljs-comment">// 在这之上的代码都是为了解决 tsc 不支持 copy 非 .ts/.tsx 文件的问题</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tscWatcher</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> run(<span class="hljs-string">'npx tsc --build ./tsconfig.json -w'</span>);
&#125;

tscWatcher();

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyOneFile</span>(<span class="hljs-params">file, cwd</span>) </span>&#123;
  <span class="hljs-keyword">const</span> <span class="hljs-keyword">from</span> = path.join(cwd, file);
  <span class="hljs-keyword">const</span> to = path.join(cwd, file.replace(<span class="hljs-regexp">/src\//</span>, <span class="hljs-string">'/lib/'</span>));
  <span class="hljs-keyword">await</span> fs.copy(<span class="hljs-keyword">from</span>, to);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">extensions-deps-install</h4>
<p>因为我们的 <code>workspace</code> 是 <code>packages</code> 目录下，所以针对于 <code>extensions</code> 下的插件以及 <code>web</code> 页面，我们没有办法通过 <code>yarn</code> 直接<code>install</code> 所有依赖，随意提供了一个插件安装依赖的脚本。<strong>其实就是跑到项目目录下，去执行 <code>npm i</code></strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> fse <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> spawn <span class="hljs-keyword">from</span> <span class="hljs-string">'cross-spawn'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> extensionsPath = path.join(__dirname, <span class="hljs-string">'..'</span>, <span class="hljs-string">'..'</span>, <span class="hljs-string">'extensions'</span>);
  <span class="hljs-keyword">const</span> extensionFiles = fse.readdirSync(extensionsPath);
  <span class="hljs-keyword">const</span> installCommonds = [<span class="hljs-string">'install'</span>];
  <span class="hljs-keyword">if</span> (!process.env.CI) &#123; <span class="hljs-comment">// 拼接参数</span>
    installCommonds.push(<span class="hljs-string">'--no-package-lock'</span>);
    installCommonds.push(<span class="hljs-string">'--registry'</span>);
    installCommonds.push(process.env.REGISTRY ? process.env.REGISTRY : <span class="hljs-string">'http://registry.npm.taobao.org'</span>);
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < extensionFiles.length; i++) &#123;
    <span class="hljs-comment">// 遍历安装，如果有 web 目录，则继续安装 web 页面里的依赖</span>
    <span class="hljs-keyword">const</span> cwd = path.join(extensionsPath, extensionFiles[i]);
    <span class="hljs-comment">// eslint-disable-next-line quotes</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Installing extension's dependencies"</span>, cwd);

    spawn.sync(<span class="hljs-string">'tnpm'</span>, installCommonds, &#123;
      <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>,
      cwd,
    &#125;);
    <span class="hljs-keyword">const</span> webviewPath = path.join(cwd, <span class="hljs-string">'web'</span>);
    <span class="hljs-keyword">if</span> (fse.existsSync(webviewPath)) &#123;
      <span class="hljs-comment">// eslint-disable-next-line quotes</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Installing extension webview's dependencies"</span>, webviewPath);
      spawn.sync(<span class="hljs-string">'tnpm'</span>, installCommonds, &#123;
        <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>,
        <span class="hljs-attr">cwd</span>: webviewPath,
      &#125;);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意 <code>scripts</code> 都是 ts 编码，所以在 <code>npmScripts</code> 中采用 <code>ts-node</code> 去执行</p>
</blockquote>
<h4 data-id="heading-12">extension-link-package</h4>
<p>删除本地相关的 package，让其递归向上（应用级）查找到对应软链后的 package</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> fse <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;
<span class="hljs-keyword">import</span> &#123; run &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./fn/shell'</span>;

(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> extensionsPath = path.join(__dirname, <span class="hljs-string">'../extensions'</span>);
  <span class="hljs-keyword">const</span> extensionFiles = <span class="hljs-keyword">await</span> fse.readdir(extensionsPath);
<span class="hljs-comment">// 获取 extensions 下的插件列表，挨个遍历执行 remove</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(
    extensionFiles.map(<span class="hljs-keyword">async</span> (extensionFile) => &#123;
      <span class="hljs-keyword">const</span> cwd = path.join(extensionsPath, extensionFile);
      <span class="hljs-keyword">if</span> (fse.existsSync(cwd)) &#123;
        <span class="hljs-comment">// link packages to extension</span>
        <span class="hljs-keyword">if</span> (!process.env.CI) &#123;
          <span class="hljs-keyword">await</span> removePmworks(cwd);
        &#125;
        <span class="hljs-keyword">const</span> webviewPath = path.join(cwd, <span class="hljs-string">'web'</span>);
        <span class="hljs-keyword">if</span> (fse.existsSync(webviewPath)) &#123;
          <span class="hljs-comment">// link packages to extension webview</span>
          <span class="hljs-keyword">if</span> (!process.env.CI) &#123;
            <span class="hljs-keyword">await</span> removePmworks(webviewPath);
          &#125;
        &#125;
      &#125;
    &#125;),
  );
&#125;)().catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.trace(e);
  process.exit(<span class="hljs-number">128</span>);
&#125;);

<span class="hljs-comment">// 删除 @pmworks 下的依赖</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removePmworks</span>(<span class="hljs-params">cwd: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> cwdStat = <span class="hljs-keyword">await</span> fse.stat(cwd);
  <span class="hljs-keyword">if</span> (cwdStat.isDirectory()) &#123;
    <span class="hljs-keyword">await</span> run(<span class="hljs-string">`rm -rf <span class="hljs-subst">$&#123;path.join(cwd, <span class="hljs-string">'node_modules'</span>, <span class="hljs-string">'@pmworks'</span>)&#125;</span>`</span>);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">小小总结</h4>
<p>核心脚本目前就如上吧，其实都是比较简单直接的功能。关于 extensions 的发布啥的还没有写，其实也可以从 appworks 中借（抄）鉴（袭）到的。等后续发布插件了再补充吧。</p>
<p>一个项目完成基建以后，基本就可以开工了。这里我拿创建项目来举例子吧（着重说基建部分，对插件功能和实现不展开具体的解释，第二阶段再总结吧）。</p>
<h3 data-id="heading-14">vscode extensions（vscode-webview 封装举例）</h3>
<p>我们通过 <code>yo code</code> 在 <code>extensions</code> 文件夹中去初始化一下我们要写的插件。具体的基础知识，参考官方文档：<a href="https://code.visualstudio.com/api" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api</a></p>
<p>如上以后，我们有了一个项目的基本架构，包的一系列管理，就已经可以进入到我们的开发阶段了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83bd8d97cd79469680412e750b7d2c6a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>毕竟我们插件是为了可视化的一系列操作，那么<code>vscode</code> 的按钮和命令必然满足不了我们，需要一个操作界面：<code>webView</code>。 如上图是一个带有 <code>webView</code> 插件的整体交互过程：</p>
<ul>
<li><code>Common-xxx(utils)</code> 是负责整个项目级别一些通用功能封装</li>
<li><code>Extension-utils</code> 是针对某一个插件提取的一些方法库，比如 <code>project-utils</code> 是 <code>createProject</code> 初始化项目时候用到的方法库，类似于一个 <code>controller</code></li>
<li><code>extension-service</code> 是承载 <code>vscode</code> 和 <code>webView</code> 通信的一些方法提取，顾名思义：<code>service</code></li>
</ul>
<p>上面说的有些绕，与传统 <code>MVC</code> 不同的是这里的 view 有两个：<code>vscode-extension</code> 和 <code>extension-webview</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472a30fc9f674fb5a848f8f5a1a19b99~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>举个栗子！ 这里以初始化一个项目教授架为例子吧~</p>
<blockquote>
<p>关于 vscode  extension with WebView相关基础概念可以看这里：<a href="https://code.visualstudio.com/api/extension-guides/webview" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api/extensi…</a></p>
</blockquote>
<h4 data-id="heading-15">WebView</h4>
<p>WebView 其实没有太多要准备的，就是准备 HTML、JavaScript 和 css 前端三大件就行了。</p>
<p>这里我使用的 ice 的脚手架初始化出来的项目：<code>npm init ice</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f6004b1058b43d799852ba5318a43cf~tplv-k3u1fbpfcp-zoom-1.image" alt="web" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后修改 <code>build.json</code> 中的<code>outputDir</code>配置，以及指定为 <code>mpa</code> 模式</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"mpa"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"vendor"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"publicPath"</span>: <span class="hljs-string">"./"</span>,
  <span class="hljs-attr">"outputDir"</span>: <span class="hljs-string">"../build"</span>,
  <span class="hljs-attr">"plugins"</span>: [
    [
      <span class="hljs-string">"build-plugin-fusion"</span>,
      &#123;
        <span class="hljs-attr">"themePackage"</span>: <span class="hljs-string">"@alifd/theme-design-pro"</span>
      &#125;
    ],
    [
      <span class="hljs-string">"build-plugin-moment-locales"</span>,
      &#123;
        <span class="hljs-attr">"locales"</span>: [
          <span class="hljs-string">"zh-cn"</span>
        ]
      &#125;
    ],
    <span class="hljs-string">"@ali/build-plugin-ice-def"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>码完代码以后得到我们的三大件即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58d657c3ff8846bbad44055a84372e05~tplv-k3u1fbpfcp-zoom-1.image" alt="build 后的文件输出" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>更多关于 ice 的文档，请移步官方文档</p>
</blockquote>
<h4 data-id="heading-16">Extensions</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="hljs-keyword">import</span> &#123; getHtmlFroWebview, connectService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@pmworks/vscode-webview"</span>;
<span class="hljs-keyword">import</span> &#123; DEV_WORKS_ICON &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@pmworks/constants"</span>;
<span class="hljs-keyword">import</span> services <span class="hljs-keyword">from</span> <span class="hljs-string">'./services'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: vscode.ExtensionContext</span>) </span>&#123;
<span class="hljs-keyword">const</span> &#123; extensionPath &#125; = context;

<span class="hljs-keyword">let</span> projectCreatorPanel: vscode.WebviewPanel | <span class="hljs-literal">undefined</span>;

<span class="hljs-keyword">const</span> activeProjectCreator = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> columnToShowIn = vscode.window.activeTextEditor ? vscode.window.activeTextEditor.viewColumn : <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">if</span> (projectCreatorPanel) &#123;
projectCreatorPanel.reveal(columnToShowIn)
&#125; <span class="hljs-keyword">else</span> &#123;
projectCreatorPanel = vscode.window.createWebviewPanel(<span class="hljs-string">'BeeDev'</span>, <span class="hljs-string">'初始化源码架构'</span>, columnToShowIn || vscode.ViewColumn.One, &#123;
<span class="hljs-attr">enableScripts</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">retainContextWhenHidden</span>: <span class="hljs-literal">true</span>,
&#125;);
&#125;
projectCreatorPanel.webview.html = getHtmlFroWebview(extensionPath, <span class="hljs-string">'projectcreator'</span>, <span class="hljs-literal">false</span>);
projectCreatorPanel.iconPath = vscode.Uri.parse(DEV_WORKS_ICON);
projectCreatorPanel.onDidDispose(
<span class="hljs-function">() =></span> &#123;
projectCreatorPanel = <span class="hljs-literal">undefined</span>;
&#125;,
<span class="hljs-literal">null</span>,
context.subscriptions,
);
connectService(projectCreatorPanel, context, &#123; services &#125;);
&#125;

<span class="hljs-keyword">let</span> disposable = vscode.commands.registerCommand(<span class="hljs-string">'devworks-project-creator.createProject.start'</span>, activeProjectCreator);

context.subscriptions.push(disposable);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deactivate</span>(<span class="hljs-params"></span>) </span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里也都是常规操作，注册命令和相关回调，初始化 <code>WebView</code> 。这里说下<code>getHtmlFroWebview</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-comment">/**
 * 给本地资源带上安全协议
 * <span class="hljs-doctag">@param </span>url 本地资源路径
 * <span class="hljs-doctag">@returns </span>带有 vscode-resource 协议的安全路径
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">originResourceProcess</span>(<span class="hljs-params">url: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> vscode.Uri.file(url).with(&#123; <span class="hljs-attr">scheme</span>: <span class="hljs-string">'vscode-resource'</span> &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getHtmlFroWebview = (
  extensionPath: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">entryName</span>: <span class="hljs-built_in">string</span>,
  needVendor?: <span class="hljs-built_in">boolean</span>,
  cdnBasePath?: <span class="hljs-built_in">string</span>,
  extraHtml?: <span class="hljs-built_in">string</span>,
  resourceProcess?: <span class="hljs-function">(<span class="hljs-params">url: <span class="hljs-built_in">string</span></span>) =></span> vscode.Uri,): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  resourceProcess = resourceProcess || originResourceProcess;
  <span class="hljs-keyword">const</span> localBasePath = path.join(extensionPath, <span class="hljs-string">'build'</span>);
  <span class="hljs-keyword">const</span> rootPath = cdnBasePath || localBasePath;
  <span class="hljs-keyword">const</span> scriptPath = path.join(rootPath, <span class="hljs-string">`js/<span class="hljs-subst">$&#123;entryName&#125;</span>.js`</span>);
  <span class="hljs-keyword">const</span> scriptUri = cdnBasePath ?
    scriptPath :
    resourceProcess(scriptPath);
  <span class="hljs-keyword">const</span> stylePath = path.join(rootPath, <span class="hljs-string">`css/<span class="hljs-subst">$&#123;entryName&#125;</span>.css`</span>);
  <span class="hljs-keyword">const</span> styleUri = cdnBasePath ?
    stylePath :
    resourceProcess(stylePath);
  <span class="hljs-comment">// vendor for MPA</span>
  <span class="hljs-keyword">const</span> vendorStylePath = path.join(rootPath, <span class="hljs-string">'css/vendor.css'</span>);
  <span class="hljs-keyword">const</span> vendorStyleUri = cdnBasePath
    ? vendorStylePath
    : resourceProcess(vendorStylePath);
  <span class="hljs-keyword">const</span> vendorScriptPath = path.join(rootPath, <span class="hljs-string">'js/vendor.js'</span>);
  <span class="hljs-keyword">const</span> vendorScriptUri = cdnBasePath
    ? vendorScriptPath
    : resourceProcess(vendorScriptPath);

  <span class="hljs-comment">// Use a nonce to whitelist which scripts can be run</span>
  <span class="hljs-keyword">const</span> nonce = getNonce();
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <meta name="theme-color" content="#000000">
    <title>Iceworks</title>
    <link rel="stylesheet" type="text/css" href="<span class="hljs-subst">$&#123;styleUri&#125;</span>">
    <span class="hljs-subst">$&#123;extraHtml || <span class="hljs-string">''</span>&#125;</span>
    `</span> +
    (needVendor ? <span class="hljs-string">`<link rel="stylesheet" type="text/css" href="<span class="hljs-subst">$&#123;vendorStyleUri&#125;</span>" />`</span> : <span class="hljs-string">''</span>) +
    <span class="hljs-string">`
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="ice-container"></div>
    `</span> +
    (needVendor ? <span class="hljs-string">`<script nonce="<span class="hljs-subst">$&#123;nonce&#125;</span>" src="<span class="hljs-subst">$&#123;vendorScriptUri&#125;</span>"></script>`</span> : <span class="hljs-string">''</span>) +
    <span class="hljs-string">`<script nonce="<span class="hljs-subst">$&#123;nonce&#125;</span>" src="<span class="hljs-subst">$&#123;scriptUri&#125;</span>"></script>
  </body>
</html>`</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNonce</span>(<span class="hljs-params"></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">let</span> text = <span class="hljs-string">''</span>;
  <span class="hljs-keyword">const</span> possible = <span class="hljs-string">'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">32</span>; i++) &#123;
    text += possible.charAt(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * possible.length));
  &#125;
  <span class="hljs-keyword">return</span> text;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法位于 <code>packages/vscode-webview/vscode.ts</code> ，其实<strong>就是获取一段 html</strong>，将本地资源添加 <code>vscode</code> 协议。支持 <code>vendor</code>、<code>extraHtml</code>等</p>
<p>截止目前，我们已经可以在 vscode 中唤起我们的 WebView 了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adfeced540f44ff7b457eff21e6a9cb3~tplv-k3u1fbpfcp-zoom-1.image" alt="webview" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">通信</h4>
<p>然后就是解决 vscode 和 WebView 通信的问题了。这里的通信跟 pubSub 非常的类似：</p>
<ul>
<li>
<p>插件给 WebView 发消息</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">panel.webview.postMessage(&#123;<span class="hljs-attr">text</span>:<span class="hljs-string">"你好，这里是 vscode 发送过来的消息"</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>webview 端接受消息</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>,<span class="hljs-function"><span class="hljs-params">event</span>=></span>&#123;
<span class="hljs-keyword">const</span> message = event.data;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`WebView 接受到的消息：<span class="hljs-subst">$&#123;message&#125;</span>`</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>webview 给插件发消息</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">vscode.postMessage(&#123;<span class="hljs-attr">text</span>:<span class="hljs-string">"你好，这是 webView 发送过来的消息"</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>插件端接受</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">panel.webview.onDidReceiveMessage(<span class="hljs-function"><span class="hljs-params">msg</span>=></span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`插件接受到的消息：<span class="hljs-subst">$&#123;msg&#125;</span>`</span>)
&#125;,<span class="hljs-literal">undefined</span>,context.subscriptions);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这种通信机制太零散了，在实际项目中，<code>webView</code> 更加的类似于我们的 <code>view</code> 层。所以<strong>理论上它只要通过 <code>service</code> 去调用 <code>controller</code> 接口去完成底层操作告诉我结果就可以</strong>：</p>
<p>比如在创建项目的时候需要让用户选择创建目录，在 HTML 页面点击选择按钮的 click handle 应该如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-keyword">const</span> getAppPath = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> projectPath = <span class="hljs-keyword">await</span> callService(<span class="hljs-string">'project'</span>, <span class="hljs-string">'getFolderPath'</span>, <span class="hljs-string">'ok'</span>);
    setAppPath(projectPath);
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>callService</code>的形参第一个作为 <code>service</code> 类、第二个作为类里面所需要调用的方法名，后续的为其对应方法的参数。</p>
<p>正对如上，我们封装一个 <code>callService</code> 方法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages/vscode-webview/webview.ts</span>

<span class="hljs-comment">// @ts-ignore</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> vscode = <span class="hljs-keyword">typeof</span> acquireVsCodeApi === <span class="hljs-string">'function'</span> ? acquireVsCodeApi() : <span class="hljs-literal">null</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> callService = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">service: <span class="hljs-built_in">string</span>, method: <span class="hljs-built_in">string</span>, ...args</span>) </span>&#123;
  <span class="hljs-comment">// 统一 return promise，统一调用方式</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 生成对应的 eventId</span>
    <span class="hljs-keyword">const</span> eventId = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; &#125;);

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`WebView call vscode extension service：<span class="hljs-subst">$&#123;service&#125;</span> <span class="hljs-subst">$&#123;method&#125;</span> <span class="hljs-subst">$&#123;eventId&#125;</span> <span class="hljs-subst">$&#123;args&#125;</span>`</span>);

    <span class="hljs-comment">// 收到 vscode 发来消息，一般为处理后 webView 的需求后</span>
    <span class="hljs-keyword">const</span> handler = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
      <span class="hljs-keyword">const</span> msg = event.data;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`webview receive vscode message:&#125;`</span>, msg);
      <span class="hljs-keyword">if</span> (msg.eventId === eventId) &#123;<span class="hljs-comment">// 去定时对应的 eventID，说明此次通信结束，可以移除（结束）此次通信了</span>
        <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'message'</span>, handler);
        msg.errorMessage ? reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(msg.errorMessage)) : resolve(msg.result);
      &#125;
    &#125;

    <span class="hljs-comment">// webview 接受 vscode 发来的消息</span>
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, handler);

    <span class="hljs-comment">// WebView 向 vscode 发送消息</span>
    vscode.postMessage(&#123;
      service,
      method,
      eventId,
      args
    &#125;);

  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webview</code> 层完成了对发送时间请求、接受时间请求以及接受后取消完成（<code>removeListener</code>）此次时间请求的封装。那么我们在来给 <code>extension</code> 添加上对应的<code>webView</code> 需要的 <code>service.methodName</code> 才行。</p>
<p>这里我们再封装了一个叫做 connectService 的方法。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">connectService(projectCreatorPanel, context, &#123; services &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的<code>projectCreatorPanel</code> 就是create 出来的 <code>WebviewPanel</code> 的“实例”，而 services 可以理解为含有多个类的对象</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> services = &#123;
<span class="hljs-attr">project</span>:&#123;
<span class="hljs-function"><span class="hljs-title">getFolderPath</span>(<span class="hljs-params">...args</span>)</span>&#123;
<span class="hljs-comment">//xxx</span>
&#125;,
xxx
&#125;,
<span class="hljs-attr">xxx</span>:&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的 connectService 方法如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">connectService</span>(<span class="hljs-params">
  webviewPanel: vscode.WebviewPanel,
  context: vscode.ExtensionContext,
  options: IConnectServiceOptions
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; subscriptions &#125; = context;
  <span class="hljs-keyword">const</span> &#123; webview &#125; = webviewPanel;
  <span class="hljs-keyword">const</span> &#123; services &#125; = options;
  webview.onDidReceiveMessage(<span class="hljs-keyword">async</span> (message: IMessage) => &#123;
    <span class="hljs-keyword">const</span> &#123; service, method, eventId, args &#125; = message;
    <span class="hljs-keyword">const</span> api = services && services[service] && services[service][method];
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onDidReceiveMessage'</span>, message);
    <span class="hljs-keyword">if</span> (api) &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> fillApiArgLength = api.length - args.length;
        <span class="hljs-keyword">const</span> newArgs = fillApiArgLength > <span class="hljs-number">0</span> ? args.concat(<span class="hljs-built_in">Array</span>(fillApiArgLength).fill(<span class="hljs-literal">undefined</span>)) : args;
        <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> api(...newArgs, context, webviewPanel);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'invoke service result'</span>, result);
        webview.postMessage(&#123; eventId, result &#125;);
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'invoke service error'</span>, err);
        webview.postMessage(&#123; eventId, <span class="hljs-attr">errorMessage</span>: err.message &#125;);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      vscode.window.showErrorMessage(<span class="hljs-string">`invalid command <span class="hljs-subst">$&#123;message&#125;</span>`</span>);
    &#125;
  &#125;, <span class="hljs-literal">undefined</span>, subscriptions);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码也比较简单，就是<strong>注册监听函数，然后只要监听到<code>WebView</code> <code>post</code> 过来的 <code>message</code>，就去取对应 <code>services</code> 下的某个 <code>service</code> 的 <code>method</code> 去执行，并且传入 <code>WebView</code> 传过来的参数</strong>。</p>
<p>extension 的 services 是在这里引入的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a71c22c49754315bf67e0613fd2635b~tplv-k3u1fbpfcp-zoom-1.image" alt="services" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而<code>@pmworks/project-service</code>这个 package 里面也只是封装一些基本的方法调用。核心的处理逻辑比如下载对应<code>gitRpo</code>、解析本地文件等都是在对应的<code>extension-utils</code> 里面进行。<strong>service只管调用即可。</strong></p>
<h4 data-id="heading-18">小小问题</h4>
<p>如上已经完成了基本的流程封装，剩下就是具体逻辑的编写了。但是在实际开发中，web 页面需要拿到 vscode 传入的参数才行，而在 web 页面开发中，vscode 插件又没法读取未编译后的代码。如何解决呢？</p>
<p><strong>在 webView 里面在封装一层 callService 用于本地 web 页面开发所需</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f04a6b7dcab45619e7aaead1cadf5a5~tplv-k3u1fbpfcp-zoom-1.image" alt="封装 callService" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">后续展望</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7845971c90f4ef68112969d8428f1e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>截止目前，基本介绍完了这两周除业务工作外的一些开发总结了。接下来需要恶补一下 vscode 插件的相关 api 准备开始操刀了。当然，在这之前，另一个非常非常紧急的任务就是还需要再升级下去年整理的源码架构，对齐下集团内现在 rax 体系的一些能力。</p>
<p>在回到这个插件体系（BeeDev源码工作台）的开发中，后续还需要：</p>
<ul>
<li>初始化源码架构</li>
<li>创建页面、拖拉拽相关 H5 源码物料（需要整个物料后台）生成初始化页面</li>
<li>创建模块、可视化配置模块加载类别等</li>
</ul>
<p>如果精力有余，其实还需要个<code>node</code> 后台，这样才能打通服务端和本地的能力（就是个桌面应用了呀~）</p>
<p>好吧，不 YY，先酱紫吧~ 下一个里程碑了再总结下~~</p>
<p>至于项目源码。。。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce931943fd9d4f5c90b409f4f460f8e1~tplv-k3u1fbpfcp-zoom-1.image" alt="参考以开源的 appworks" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">参考文献</h2>
<ul>
<li>appworks：<a href="https://appworks.site/" target="_blank" rel="nofollow noopener noreferrer">appworks.site/</a></li>
<li>vscode  extension api：<a href="https://code.visualstudio.com/api" target="_blank" rel="nofollow noopener noreferrer">code.visualstudio.com/api</a></li>
<li>monorepo&leran：<a href="https://github.com/lerna/lerna" target="_blank" rel="nofollow noopener noreferrer">github.com/lerna/lerna</a></li>
</ul>
<h2 data-id="heading-21">其他</h2>
<p>关注微信公众号【全栈前端精选】，每天推送精选文章~</p></div>  
</div>
            