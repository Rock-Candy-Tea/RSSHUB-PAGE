
---
title: 'husky 7 + lint-staged 11+ prettier 2 + eslint 7 配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39ed2462b64d425e9fc61efa89a143a5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 02:35:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39ed2462b64d425e9fc61efa89a143a5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>基于最新的一些库来规范项目，<br>比如格式化和提交预处理等～<br>
<br>一些库的最新版的配置更加独立了，<br>对于工程化来说，其实更加直观了～<br>
围绕react技术栈加入相关门禁来开展文章～</p>
<h2 data-id="heading-1">效果图</h2>
<h3 data-id="heading-2">git commit 限定</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39ed2462b64d425e9fc61efa89a143a5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3324544c991047128838f59f2c9cb728~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">pre-commit 门禁</h3>
<p>一般用于拦截提交之前的暂存区变动，进行相关的门禁检测<br></p>
<h3 data-id="heading-4">prettier</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53693d1339a04ddab4b059746e7fc3bf~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">ESLint</h3>
<p>主要就是代码规范化<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a95a17ed3c44c97982ac84ade34b052~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<h2 data-id="heading-6">配置姿势</h2>
<h3 data-id="heading-7">安装相关依赖</h3>
<p>对于我们真实的业务的，一般来说都有沉淀出自己的一套封装；<br>不管是eslint还是commitizen，不过此处我们直接说一个全新没有任何沉淀的；<br>
<br>下面的devDependencies涵盖了我们这次教程的所有依赖，这是最重要的一步～</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"ones-frontend-publish-platform"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"prepare"</span>: <span class="hljs-string">"husky install; node check-esbuild.js"</span>,
    <span class="hljs-string">"lint:fix"</span>: <span class="hljs-string">"eslint ./src --ext .jsx,.js,.ts,.tsx --fix --quiet  --ignore-path .gitignore"</span>,
    <span class="hljs-string">"lint:format"</span>: <span class="hljs-string">"prettier  --loglevel warn --write \"./**/*.&#123;js,jsx,ts,tsx,css,md,json&#125;\" "</span>,
    <span class="hljs-string">"lint:style"</span>: <span class="hljs-string">"stylelint src/**/*.&#123;css,less,scss&#125; --fix "</span>,
    <span class="hljs-string">"commit"</span>: <span class="hljs-string">"cz"</span>,
    <span class="hljs-string">"type-check"</span>: <span class="hljs-string">"tsc"</span>
  &#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"@commitlint/cli"</span>: <span class="hljs-string">"^12.1.4"</span>,
    <span class="hljs-string">"@commitlint/config-conventional"</span>: <span class="hljs-string">"^12.1.4"</span>,
    <span class="hljs-string">"commitizen"</span>: <span class="hljs-string">"^4.2.4"</span>,
    <span class="hljs-string">"cz-conventional-changelog"</span>: <span class="hljs-string">"^3.3.0"</span>,
    <span class="hljs-string">"eslint"</span>: <span class="hljs-string">"^7.30.0"</span>,
    <span class="hljs-string">"eslint-config-prettier"</span>: <span class="hljs-string">"^8.3.0"</span>,
    <span class="hljs-string">"eslint-plugin-import"</span>: <span class="hljs-string">"^2.23.4"</span>,
    <span class="hljs-string">"eslint-plugin-jsx-a11y"</span>: <span class="hljs-string">"^6.4.1"</span>,
    <span class="hljs-string">"eslint-plugin-prettier"</span>: <span class="hljs-string">"^3.4.0"</span>,
    <span class="hljs-string">"eslint-plugin-react"</span>: <span class="hljs-string">"^7.24.0"</span>,
    <span class="hljs-string">"eslint-plugin-react-hooks"</span>: <span class="hljs-string">"^4.2.0"</span>,
    <span class="hljs-string">"eslint-plugin-simple-import-sort"</span>: <span class="hljs-string">"^7.0.0"</span>,
    <span class="hljs-string">"husky"</span>: <span class="hljs-string">"^7.0.1"</span>,
    <span class="hljs-string">"lint-staged"</span>: <span class="hljs-string">"^11.0.1"</span>,
    <span class="hljs-string">"prettier"</span>: <span class="hljs-string">"^2.3.2"</span>,
  &#125;,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">husky初始化及钩子配置</h3>
<p>husky 7的初始化推荐用他们官方提供的姿势，放到prepare，<br>在安装依赖的时候去执行～～初始化过的会自动跳过～</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"prepare"</span>: <span class="hljs-string">"husky install"</span>,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功执行的化，功能根目录会存在一个.husky的目录；<br>最新版的husky走的是标准的shell脚本（推荐姿势）<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923acaf49e2746d29247e20f9fc5031a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>commit-msg和pre-commit都是对应的钩子；</p>
<ul>
<li>commit-msg: 就是git commit msg的时候去触发对应的逻辑
<ul>
<li>一般我们在这里验证commit msg的验证</li>
</ul>
</li>
<li>pre-commit: 就是git commit 之前走的钩子
<ul>
<li>一般我们在这里去处理暂存区的文件，比如格式化代码，eslint fix代码等</li>
</ul>
</li>
</ul>
<h4 data-id="heading-9">commit-msg</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/sh</span>
. <span class="hljs-string">"<span class="hljs-subst">$(dirname <span class="hljs-string">"<span class="hljs-variable">$0</span>"</span>)</span>/_/husky.sh"</span>

<span class="hljs-comment"># npx 是npm的一个免安装工具，</span>
<span class="hljs-comment"># 本质就是可以临时download执行某个二进制</span>
npx --no-install commitlint --edit <span class="hljs-variable">$1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">pre-commit</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/sh</span>
. <span class="hljs-string">"<span class="hljs-subst">$(dirname <span class="hljs-string">"<span class="hljs-variable">$0</span>"</span>)</span>/_/husky.sh"</span>

<span class="hljs-comment"># 这里就是唤醒lint-staged</span>
npx lint-staged 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">commitlint配置</h3>
<h4 data-id="heading-12">package.json</h4>
<p>这里就是读取那个规范commitlint的规则包，若是要自定义可以在这个基础上用<br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fleoforfree%2Fcz-customizable" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/leoforfree/cz-customizable" ref="nofollow noopener noreferrer">github.com/leoforfree/…</a></p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"config"</span>: &#123;
  <span class="hljs-attr">"commitizen"</span>: &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./node_modules/cz-conventional-changelog"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">eslint配置（.eslintrc.js)</h3>
<p>采用社区主流的推荐配置，唯一考虑的点<br>就是需要考虑和prettier的冲突</p>
<pre><code class="hljs language-bash copyable" lang="bash">module.exports = &#123;
  root: <span class="hljs-literal">true</span>,
  parser: <span class="hljs-string">'@typescript-eslint/parser'</span>,
  parserOptions: &#123;
    ecmaVersion: 2020,
    sourceType: <span class="hljs-string">'module'</span>,
    ecmaFeatures: &#123;
      jsx: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
  settings: &#123;
    react: &#123;
      version: <span class="hljs-string">'detect'</span>,
    &#125;,
  &#125;,
  env: &#123;
    browser: <span class="hljs-literal">true</span>,
    amd: <span class="hljs-literal">true</span>,
    node: <span class="hljs-literal">true</span>,
  &#125;,
  extends: [
    <span class="hljs-string">'eslint:recommended'</span>,
    <span class="hljs-string">'plugin:react/recommended'</span>,
    <span class="hljs-string">'plugin:react-hooks/recommended'</span>,
    <span class="hljs-string">'plugin:jsx-a11y/recommended'</span>,
    <span class="hljs-string">'prettier'</span>, // eslint-config-prettier的标准用法，必须放在最后一个，用于关闭和eslint冲突规则
  ],
  plugins: [<span class="hljs-string">'simple-import-sort'</span>, <span class="hljs-string">'prettier'</span>, <span class="hljs-string">'@typescript-eslint'</span>],
  rules: &#123;
    <span class="hljs-string">'prettier/prettier'</span>: [<span class="hljs-string">'error'</span>, &#123;&#125;, &#123; usePrettierrc: <span class="hljs-literal">true</span> &#125;],
    <span class="hljs-string">'react/react-in-jsx-scope'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'jsx-a11y/accessible-emoji'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'no-unused-vars'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-unused-vars'</span>: [<span class="hljs-string">'error'</span>],
    <span class="hljs-string">'react/display-name'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'jsx-a11y/no-static-element-interactions'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'jsx-a11y/click-events-have-key-events'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'react/prop-types'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'react-hooks/exhaustive-deps'</span>: <span class="hljs-string">'off'</span>, // <--- THIS IS THE NEW RULE
    <span class="hljs-string">'@typescript-eslint/explicit-function-return-type'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'simple-import-sort/imports'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-string">'simple-import-sort/exports'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-string">'jsx-a11y/anchor-is-valid'</span>: [
      <span class="hljs-string">'error'</span>,
      &#123;
        components: [<span class="hljs-string">'Link'</span>],
        specialLink: [<span class="hljs-string">'hrefLeft'</span>, <span class="hljs-string">'hrefRight'</span>],
        aspects: [<span class="hljs-string">'invalidHref'</span>, <span class="hljs-string">'preferButton'</span>],
      &#125;,
    ],
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">prettier配置（.prettierrc.json）</h3>
<p>哇哈哈，是不是很简陋，我完整的过了一边v2的文档；<br>发现默认的配置其实就是社区推荐的主流配置；</p>
<pre><code class="hljs language-bash copyable" lang="bash">&#123;
  <span class="hljs-string">"singleQuote"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">lint-staged（.lintstagedrc.json）</h3>
<p>非常好理解，就是暂存区内所有符合对应后缀的走对应的规则；<br>比如代码的走了eslint和prettier，先规范，后格式化～<br>比如样式的只走格式化～～<br>比如其他prettier支持的必要文件也走一下格式化～</p>
<pre><code class="hljs language-bash copyable" lang="bash">&#123;
  <span class="hljs-string">"*.&#123;js,jsx,ts,tsx&#125;"</span>: [<span class="hljs-string">"eslint"</span>, <span class="hljs-string">"prettier --write"</span>],
  <span class="hljs-string">"*.&#123;less,scss&#125;"</span>: <span class="hljs-string">"prettier --write"</span>,
  <span class="hljs-string">"*.&#123;js,css,json,md&#125;"</span>: [<span class="hljs-string">"prettier --write"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">总结</h2>
<p>其实总体的配置还是挺清晰的，各个工具的都相对独立，<br>也有自己的专属配置文件～～<br>
<br>前端的工程化也越来越直观了</p></div>  
</div>
            