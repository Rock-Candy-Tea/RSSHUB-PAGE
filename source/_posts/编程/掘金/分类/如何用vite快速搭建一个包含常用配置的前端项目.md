
---
title: '如何用vite快速搭建一个包含常用配置的前端项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=761'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:26:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=761'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与新手入门的第1篇文章</p>
<p>vite 一个由 vue 作者尤雨溪开发的 web 开发工具，它具有以下特点：</p>
<ol>
<li>快速的冷启动</li>
<li>即时的模块热更新</li>
<li>真正的按需编译</li>
</ol>
<p>至于为什么选择vite，官网上介绍的很详细，可点击查看<a href="https://cn.vitejs.dev/guide/why.html" target="_blank" rel="nofollow noopener noreferrer">为什么选择vite</a>，这里主要介绍一下如何用vite搭建一个包含前端开发常用配置的前端项目</p>
<h3 data-id="heading-0">初始化项目</h3>
<p>查看<a href="https://cn.vitejs.dev/guide/#scaffolding-your-first-vite-project" target="_blank" rel="nofollow noopener noreferrer">vite官网</a>可知
<code>yarn create @vitejs/app </code>
这里选择vue框架，再选择vue-ts模板，然后根据提示操作即可</p>
<p>初始化项目也可以采用快捷方式，在命令中写好项目名称和模板
<code>yarn create @vitejs/app project-name --template vue-ts</code></p>
<h3 data-id="heading-1">安装eslint及相关plugin</h3>
<pre><code class="copyable">yarn add eslint eslint-plugin-vue @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-plugin-simple-import-sort -D  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释说明下相关plugin:</p>
<p>eslint-plugin-vue：Vue.js的官方ESLint插件<br>
@typescript-eslint/parser：ESLint的解析器，用于解析typescript，从而检查和规范Typescript代码<br>
@typescript-eslint/eslint-plugin：ESLint插件，包含了各类定义好的检测Typescript代码的规范<br>
eslint-plugin-simple-import-sort：自动排序 import 的插件</p>
<p>新建.eslintrc.js文件</p>
<pre><code class="hljs language-json copyable" lang="json">module.exports = &#123;
  root: <span class="hljs-literal">true</span>,
  env: &#123;
    browser: <span class="hljs-literal">true</span>,
    node: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">//定义eslint依赖的插件</span>
  plugins: [<span class="hljs-string">"@typescript-eslint"</span>, <span class="hljs-string">"prettier"</span>, <span class="hljs-string">"simple-import-sort"</span>],
  <span class="hljs-comment">//定义文件继承的代码规范</span>
  extends: [<span class="hljs-string">"plugin:vue/vue3-recommended"</span>, <span class="hljs-string">"prettier"</span>],
  parserOptions: &#123;
    <span class="hljs-comment">//解析ts文件</span>
    parser: <span class="hljs-string">"@typescript-eslint/parser"</span>,
    sourceType: <span class="hljs-string">"module"</span>,
    ecmaVersion: <span class="hljs-number">2020</span>,
    ecmaFeatures: &#123;
      tsx: <span class="hljs-literal">true</span> <span class="hljs-comment">// 允许解析TSX</span>
    &#125;
  &#125;,
  rules: &#123;
    <span class="hljs-attr">"prettier/prettier"</span>: <span class="hljs-string">"error"</span>,
    <span class="hljs-attr">"@typescript-eslint/explicit-module-boundary-types"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"@typescript-eslint/interface-name-prefix"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"@typescript-eslint/no-empty-function"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"@typescript-eslint/no-explicit-any"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"@typescript-eslint/no-var-requires"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"@typescript-eslint/camelcase"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"no-console"</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"warn"</span> : <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"no-debugger"</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"warn"</span> : <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"vue/html-self-closing"</span>: [
      <span class="hljs-string">"error"</span>,
      &#123;
        html: &#123;
          component: <span class="hljs-string">"always"</span>,
          normal: <span class="hljs-string">"always"</span>,
          void: <span class="hljs-string">"any"</span>
        &#125;,
        math: <span class="hljs-string">"always"</span>,
        svg: <span class="hljs-string">"always"</span>
      &#125;
    ],
    <span class="hljs-attr">"vue/require-default-prop"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"vue/no-v-html"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"sort-imports"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"import/order"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-attr">"simple-import-sort/imports"</span>: <span class="hljs-string">"error"</span>,
    <span class="hljs-attr">"simple-import-sort/exports"</span>: <span class="hljs-string">"error"</span>
  &#125;,
  overrides: [
    &#123;
      files: [<span class="hljs-string">"**/__tests__/*.&#123;j,t&#125;s?(x)"</span>, <span class="hljs-string">"**/tests/unit/**/*.spec.&#123;j,t&#125;s?(x)"</span>],
      env: &#123;
        jest: <span class="hljs-literal">true</span>
      &#125;
    &#125;
  ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">安装prettier 用于代码格式化</h3>
<pre><code class="copyable">yarn add prettier eslint-config-prettier eslint-plugin-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">eslint-config-prettier</h4>
<p>解决ESLint中的样式规范和prettier中样式规范的冲突，以prettier的样式规范为准，使ESLint中的样式规范自动失效</p>
<h4 data-id="heading-4">eslint-plugin-prettier</h4>
<p>将prettier作为ESLint规范来使用</p>
<p>新建.prettierrc文件</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"printWidth"</span>: <span class="hljs-number">120</span>,
  <span class="hljs-attr">"proseWrap"</span>: <span class="hljs-string">"preserve"</span>,
  <span class="hljs-attr">"tabWidth"</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">"semi"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"singleQuote"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"trailingComma"</span>: <span class="hljs-string">"none"</span>,
  <span class="hljs-attr">"bracketSpacing"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"jsxBracketSameLine"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"arrowParens"</span>: <span class="hljs-string">"avoid"</span>,
  <span class="hljs-attr">"rangeStart"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">"endOfLine"</span>: <span class="hljs-string">"lf"</span>,
  <span class="hljs-attr">"insertPragma"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"requirePragma"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"useTabs"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想在保存时编辑器自动规范代码还需要在vscode的配置文件中添加
<code>"editor.formatOnSave": true</code></p>
<h3 data-id="heading-5">安装stylelint 规范style</h3>
<pre><code class="copyable">yarn add stylelint stylelint-prettier stylelint-config-prettier stylelint-config-recess-order -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建.stylelintrc.js</p>
<pre><code class="hljs language-json copyable" lang="json">module.exports = &#123;
  defaultSeverity: <span class="hljs-string">"error"</span>,
  plugins: [<span class="hljs-string">"stylelint-prettier"</span>],
  extends: [<span class="hljs-string">"stylelint-prettier/recommended"</span>, <span class="hljs-string">"stylelint-config-recess-order"</span>],
  rules: &#123;&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">安装commit-message 用于规范git message</h3>
<p><code>yarn add @commitlint/cli @commitlint/config-conventional -D</code></p>
<p>新建.commitlintrc.js文件</p>
<pre><code class="hljs language-json copyable" lang="json">module.exports = &#123;
  extends: [<span class="hljs-string">"@commitlint/config-conventional"</span>],
  rules: &#123;
    <span class="hljs-attr">"type-enum"</span>: [
      <span class="hljs-number">2</span>,
      <span class="hljs-string">"always"</span>,
      [
        <span class="hljs-string">"release"</span>,
        <span class="hljs-string">"wip"</span>,
        <span class="hljs-string">"build"</span>,
        <span class="hljs-string">"chore"</span>,
        <span class="hljs-string">"ci"</span>,
        <span class="hljs-string">"docs"</span>,
        <span class="hljs-string">"feat"</span>,
        <span class="hljs-string">"fix"</span>,
        <span class="hljs-string">"perf"</span>,
        <span class="hljs-string">"refactor"</span>,
        <span class="hljs-string">"revert"</span>,
        <span class="hljs-string">"style"</span>,
        <span class="hljs-string">"test"</span>,
        <span class="hljs-string">"merge"</span>]
    ]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">安装ls-lint 用于规范文件夹命名</h3>
<p><code>yarn add @ls-lint/ls-lint -D</code></p>
<p>新建.ls-lint.yml文件</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-comment"># 文件名及文件夹名命名规则</span>
<span class="hljs-attr">ls:</span>
  <span class="hljs-string">src/components/*:</span>
    <span class="hljs-string">.dir:</span> <span class="hljs-string">PascalCase</span> <span class="hljs-comment"># 组件文件夹名命名模式</span>
  <span class="hljs-attr">src/views:</span>
    <span class="hljs-string">.dir:</span> <span class="hljs-string">camelCase</span> <span class="hljs-string">|</span> <span class="hljs-string">snake_case</span>
  <span class="hljs-attr">src/store:</span>
    <span class="hljs-string">.dir:</span> <span class="hljs-string">camelCase</span> <span class="hljs-string">|</span> <span class="hljs-string">kebab-case</span>
  <span class="hljs-attr">src/router:</span>
    <span class="hljs-string">.dir:</span> <span class="hljs-string">camelCase</span> <span class="hljs-string">|</span> <span class="hljs-string">kebab-case</span> <span class="hljs-string">|</span> <span class="hljs-string">regex:^__.+$</span>
  <span class="hljs-attr">src:</span>
    <span class="hljs-string">.ts:</span> <span class="hljs-string">camelCase</span>
    <span class="hljs-string">.d.ts:</span> <span class="hljs-string">camelCase</span> <span class="hljs-string">|</span> <span class="hljs-string">kebab-case</span>
<span class="hljs-attr">ignore:</span>
  <span class="hljs-string">-</span> <span class="hljs-string">.git</span>
  <span class="hljs-string">-</span> <span class="hljs-string">node_modules</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">安装husky和lint-staged</h3>
<p>用于对要提交的文件代码检查及格式化
<code>yarn add husky lint-staged -D</code>
修改package.json</p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-attr">"hooks"</span>: &#123;
      <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>,
      <span class="hljs-attr">"commit-msg"</span>: <span class="hljs-string">"commitlint -e $HUSKY_GIT_PARAMS"</span>
    &#125;
  &#125;,
  <span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-attr">"*.&#123;vue,ts,js,scss&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>,
      <span class="hljs-string">"git add"</span>
    ]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">配置项目运行任务</h3>
<p>在vscode中选择终端->配置默认生成任务即可在.vscode文件夹下生成tasks.json文件，内容如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"2.0.0"</span>,
  <span class="hljs-attr">"tasks"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"npm"</span>,
      <span class="hljs-attr">"script"</span>: <span class="hljs-string">"dev"</span>,
      <span class="hljs-attr">"problemMatcher"</span>: [],
      <span class="hljs-attr">"label"</span>: <span class="hljs-string">"npm: dev"</span>,
      <span class="hljs-attr">"detail"</span>: <span class="hljs-string">"vite"</span>,
      <span class="hljs-attr">"group"</span>: &#123;
        <span class="hljs-attr">"kind"</span>: <span class="hljs-string">"build"</span>,
        <span class="hljs-attr">"isDefault"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 设置成默认任务</span>
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行默认任务的快捷键是ctrl+shift+b，这样每次开发时不用在命令行输入命令 yarn dev，直接按快捷键就行</p>
<h3 data-id="heading-10">配置项目中需要的vscode扩展</h3>
<p>在项目根目录中的.vscode文件夹下新建extensions.json文件
将下面内容填写到extensions.json文件中</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"recommendations"</span>: [
    <span class="hljs-string">"shenjiaolong.vue-helper"</span>,
    <span class="hljs-string">"octref.vetur"</span>,
    <span class="hljs-string">"esbenp.prettier-vscode"</span>,
    <span class="hljs-string">"dbaeumer.vscode-eslint"</span>,
    <span class="hljs-string">"stylelint.vscode-stylelint"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果参与该项目的同事vscode中没有安装所列插件，则会在右下角提示是否安装</p></div>  
</div>
            