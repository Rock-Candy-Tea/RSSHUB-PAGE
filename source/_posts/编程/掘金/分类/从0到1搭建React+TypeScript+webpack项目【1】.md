
---
title: '从0到1搭建React+TypeScript+webpack项目【1】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7d363587e5040aeb12fef60990faeca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 22:27:18 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7d363587e5040aeb12fef60990faeca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">搭建项目结构</h1>
<h2 data-id="heading-1">下载脚手架</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install -g create-react-app
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">创建一个项目</h2>
<pre><code class="hljs language-js copyable" lang="js">create-react-app my-app --template typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该模版包含了全套正常运行 <code>React</code> 所需的包和配置，无需再额外手动安装 <code>typescript</code> 等，其中还包含了自动化测试文件以及PWA所需文件等，可自行根据需求增删。
创建结束后，项目结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js">my-app/
├─ .gitignore
├─ images.d.ts
├─ node_modules/
├─ public/
├─ src/
│  └─ ...
├─ package.json
├─ tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">安装eslint</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install eslint -dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">创建eslint的配置文件</h3>
<pre><code class="hljs language-js copyable" lang="js">./node_modules/.bin/eslint --init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据自身情况选择</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7d363587e5040aeb12fef60990faeca~tplv-k3u1fbpfcp-watermark.image" alt="eslint.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">安装相关包</h3>
<pre><code class="hljs language-js copyable" lang="js">yarn add eslint-plugin-react@latest @typescript-eslint/eslint-plugin@latest eslint-config-standard@latest eslint@^<span class="hljs-number">7.12</span><span class="hljs-number">.1</span> eslint-plugin-<span class="hljs-keyword">import</span>@^<span class="hljs-number">2.22</span><span class="hljs-number">.1</span> eslint-plugin-node@^<span class="hljs-number">11.1</span><span class="hljs-number">.0</span> eslint-plugin-promise@^<span class="hljs-number">4.2</span><span class="hljs-number">.1</span> @typescript-eslint/parser@latest  -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装<code>eslint-import-resolver-alias</code>，解决<code>import/unresolver</code> 的报错</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add eslint-<span class="hljs-keyword">import</span>-resolver-alias -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>补上一些esliint 官网推荐的扩展和插件及取消掉平常开发用起来很不舒服的一些规则</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-string">"env"</span>: &#123;
        <span class="hljs-string">"browser"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"es2021"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-string">"extends"</span>: [
       
        <span class="hljs-string">"plugin:react-hooks/recommended"</span>,
        <span class="hljs-string">"standard"</span>
    ],
    <span class="hljs-string">"parser"</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>,
    <span class="hljs-string">"parserOptions"</span>: &#123;
        <span class="hljs-string">"ecmaFeatures"</span>: &#123;
            <span class="hljs-string">"jsx"</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-string">"ecmaVersion"</span>: <span class="hljs-number">12</span>,
        <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span>
    &#125;,
    <span class="hljs-string">"plugins"</span>: [
        <span class="hljs-string">"react"</span>,
        <span class="hljs-string">"@typescript-eslint"</span>,
        <span class="hljs-string">"react-hooks"</span>
    ],
    <span class="hljs-string">"rules"</span>: &#123;
        <span class="hljs-string">"react-hooks/rules-of-hooks"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"react-hooks/exhaustive-deps"</span>: <span class="hljs-string">"warn"</span>,
        <span class="hljs-string">"react/no-unsafe"</span>: [
          <span class="hljs-string">"error"</span>,
          &#123;
            <span class="hljs-string">"checkAliases"</span>: <span class="hljs-literal">true</span>
          &#125;
        ],
        <span class="hljs-string">"react/self-closing-comp"</span>: <span class="hljs-string">"warn"</span>,
        <span class="hljs-string">"react/sort-comp"</span>: [
          <span class="hljs-string">"error"</span>,
          &#123;
            <span class="hljs-string">"order"</span>: [
              <span class="hljs-string">"static-methods"</span>,
              <span class="hljs-string">"instance-variables"</span>,
              <span class="hljs-string">"lifecycle"</span>,
              <span class="hljs-string">"everything-else"</span>,
              <span class="hljs-string">"rendering"</span>
            ]
          &#125;
        ],
        <span class="hljs-string">"react/prop-types"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"@typescript-eslint/no-useless-constructor"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"@typescript-eslint/array-type"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"@typescript-eslint/ban-types"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"@typescript-eslint/no-array-constructor"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"@typescript-eslint/naming-convention"</span>: [
          <span class="hljs-string">"error"</span>,
          &#123; <span class="hljs-string">"selector"</span>: <span class="hljs-string">"variable"</span>, <span class="hljs-string">"format"</span>: [<span class="hljs-string">"camelCase"</span>, <span class="hljs-string">"UPPER_CASE"</span>,<span class="hljs-string">"PascalCase"</span>] &#125;
        ],
        <span class="hljs-string">"@typescript-eslint/no-use-before-define"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"getter-return"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-dupe-args"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-dupe-keys"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-unreachable"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"valid-typeof"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-const-assign"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-new-symbol"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-this-before-super"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-undef"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-dupe-class-members"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-redeclare"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-unused-vars"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-var"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"no-use-before-define"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"no-console"</span>: <span class="hljs-string">"warn"</span>,
        <span class="hljs-string">"prefer-rest-params"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"prefer-spread"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"prefer-const"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"no-empty-function"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"eqeqeq"</span>: <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"array-callback-return"</span>: <span class="hljs-string">"warn"</span>,
        <span class="hljs-string">"default-case"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"no-shadow"</span>: <span class="hljs-string">"warn"</span>,
        <span class="hljs-string">"no-return-await"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"no-await-in-loop"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"require-await"</span>: <span class="hljs-string">"error"</span>,
        <span class="hljs-string">"generator-star-spacing"</span>: [<span class="hljs-string">"warn"</span>, <span class="hljs-string">"after"</span>],
        <span class="hljs-string">"yield-star-spacing"</span>: [<span class="hljs-string">"warn"</span>, <span class="hljs-string">"after"</span>],
        <span class="hljs-string">"spaced-comment"</span>: [<span class="hljs-string">"warn"</span>, <span class="hljs-string">"always"</span>, &#123; <span class="hljs-string">"markers"</span>: [<span class="hljs-string">"/"</span>] &#125;] ,
        <span class="hljs-string">"semi"</span>: [<span class="hljs-string">"error"</span>, <span class="hljs-string">"always"</span>, &#123; <span class="hljs-string">"omitLastInOneLineBlock"</span>: <span class="hljs-literal">true</span> &#125;] ,
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装对react-hooks 校验支持的插件eslint-plugin-react-hooks</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add eslint-plugin-react-hooks -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">安装 prettier</h2>
<pre><code class="hljs language-js copyable" lang="js">yarn add  prettier eslint-plugin-prettier eslint-config-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">配置代码格式的规则</h3>
<p>在根目录下面新建一个.prettierrc 的文件：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"trailingComma"</span>: <span class="hljs-string">"all"</span>,
    <span class="hljs-string">"tabWidth"</span>: <span class="hljs-number">2</span>,
    <span class="hljs-string">"semi"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"singleQuote"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"endOfLine"</span>: <span class="hljs-string">"auto"</span>,
    <span class="hljs-string">"printWidth"</span>: <span class="hljs-number">100</span>,
    <span class="hljs-string">"arrowParens"</span>: <span class="hljs-string">"always"</span>,
    <span class="hljs-string">"useTabs"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"overrides"</span>: [
        &#123;
            <span class="hljs-string">"files"</span>: <span class="hljs-string">"*.md"</span>,
            <span class="hljs-string">"options"</span>: &#123;
                <span class="hljs-string">"tabWidth"</span>: <span class="hljs-number">2</span>
            &#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">调整eslintrc.js 里面的插件配置</h3>
<p>修改extends、plugins、rules：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;

  <span class="hljs-attr">extends</span>: [..., <span class="hljs-string">"prettier"</span>],
  <span class="hljs-attr">plugins</span>: [..., <span class="hljs-string">"prettier"</span>],
  <span class="hljs-attr">rules</span>: &#123;
     ...,
    <span class="hljs-string">"prettier/prettier"</span>: <span class="hljs-string">"error"</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">安装stylelint</h2>
<h3 data-id="heading-10">安装相关依赖包</h3>
<pre><code class="hljs language-js copyable" lang="js">yarn add stylelint stylelint-config-standard stylelint-config-css-modules stylelint-config-rational-order stylelint-config-prettier  -D

yarn add stylelint-order stylelint-scss -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">根目录上新建.stylelintrc.json</h3>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"extends"</span>: [ <span class="hljs-string">"stylelint-config-standard"</span>,
      <span class="hljs-string">"stylelint-config-css-modules"</span>,
      <span class="hljs-string">"stylelint-config-rational-order"</span>,
      <span class="hljs-string">"stylelint-config-prettier"</span>],
    <span class="hljs-string">"plugins"</span>: [<span class="hljs-string">"stylelint-scss"</span>,<span class="hljs-string">"stylelint-order"</span>],
    <span class="hljs-string">"rules"</span>: &#123;
    <span class="hljs-string">"no-descending-specificity"</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">"at-rule-no-unknown"</span>: <span class="hljs-literal">null</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">安装 husky 和lint-staged</h2>
<pre><code class="hljs language-js copyable" lang="js">yarn add husky lint-staged -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">在package.json 配置对应的配置</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>
    &#125;
  &#125;,
  <span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-string">"**/*.&#123;scss,less,css&#125;"</span>: [
      <span class="hljs-string">"stylelint --fix"</span>,
      <span class="hljs-string">"git add"</span>
    ],
    <span class="hljs-string">"src/**/*.&#123;js,jsx,ts,tsx&#125;"</span>: [
      <span class="hljs-string">"eslint --fix"</span>,
      <span class="hljs-string">"git add"</span>
    ],
    <span class="hljs-string">"**/*.&#123;json,ts,tsx,js,jsx,md,scss,less,css,html&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>,
      <span class="hljs-string">"git add"</span>
    ]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">启动项目</h2>
<pre><code class="hljs language-js copyable" lang="js">yarn start
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">统一vscode的插件配置</h1>
<h3 data-id="heading-16">根目录创建.vscode 文件夹</h3>
<h3 data-id="heading-17">.vscode里创建extensions.json</h3>
<p>配置如下</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"recommendations"</span>: [
   <span class="hljs-string">"dbaeumer.vscode-eslint"</span>,
    <span class="hljs-string">"esbenp.prettier-vscode"</span>,
    <span class="hljs-string">"steoates.autoimport"</span>,
    <span class="hljs-string">"formulahendry.auto-close-tag"</span>,
    <span class="hljs-string">"formulahendry.auto-rename-tag"</span>,
    <span class="hljs-string">"clinyong.vscode-css-modules"</span>,
    <span class="hljs-string">"quicktype.quicktype"</span>
   ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">.vscode下面创建settings.json</h3>
<pre><code class="hljs language-js copyable" lang="js">&#123;
&#123;
  <span class="hljs-comment">// #每次保存的时候将代码按eslint格式进行修复</span>
  <span class="hljs-string">"editor.codeActionsOnSave"</span>: &#123;
    <span class="hljs-string">"source.fixAll"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"source.organizeImports"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">// 点击保存时，根据 eslint 规则自定修复，同时集成 prettier 到 eslint 中</span>
  <span class="hljs-string">"prettier.eslintIntegration"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>,
  <span class="hljs-comment">// 为了避免和 eslint 冲突，将编辑器默认的代码检查规则关闭（如果开启了）</span>
  <span class="hljs-string">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// stylelint 扩展自身的校验就够了</span>
  <span class="hljs-string">"css.validate"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"less.validate"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"scss.validate"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// 使用本地安装的 TypeScript 替代 VSCode 内置的来提供智能提示</span>
  <span class="hljs-string">"typescript.tsdk"</span>: <span class="hljs-string">"./node_modules/typescript/lib"</span>,
  <span class="hljs-comment">// 指定哪些文件不参与搜索</span>
  <span class="hljs-string">"search.exclude"</span>: &#123;
    <span class="hljs-string">"**/node_modules"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"dist"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"yarn.lock"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">// 指定哪些文件不被 VSCode 监听，预防启动 VSCode 时扫描的文件太多，导致 CPU 占用过高</span>
  <span class="hljs-string">"files.watcherExclude"</span>: &#123;
    <span class="hljs-string">"**/.git/objects/**"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"**/.git/subtree-cache/**"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"**/node_modules/*/**"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"**/dist/**"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-string">"eslint.options"</span>: &#123;
    <span class="hljs-string">"configFile"</span>: <span class="hljs-string">"./.eslintrc.js"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">.vscode 里新建一个xx.code-snippets 的文件</h3>
<p>把整个项目里面经常重复的代码配置成代码片段。这样只要敲关键字就能自动生成已经写好的代码。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
 <span class="hljs-string">"ts react function component"</span>: &#123;
    <span class="hljs-string">"scope"</span>: <span class="hljs-string">"typescriptreact"</span>,  <span class="hljs-comment">// 语言范围ts</span>
    <span class="hljs-string">"prefix"</span>: <span class="hljs-string">"tsrfc"</span>,    <span class="hljs-comment">//匹配的关键字</span>
    <span class="hljs-string">"body"</span>: [
      <span class="hljs-string">"import React from 'react';"</span>,
      <span class="hljs-string">"import styles from './$&#123;1:$&#123;TM_FILENAME_BASE&#125;&#125;.module.scss';"</span>,
      <span class="hljs-string">""</span>,
      <span class="hljs-string">"interface $&#123;1:$&#123;TM_FILENAME_BASE&#125;&#125;Props &#123;"</span>,
      <span class="hljs-string">"  [key: string]: any;"</span>,
      <span class="hljs-string">"&#125;"</span>,
      <span class="hljs-string">""</span>,
      <span class="hljs-string">"const $&#123;1:$&#123;TM_FILENAME_BASE&#125;&#125;: React.FC<$&#123;1:$&#123;TM_FILENAME_BASE&#125;&#125;Props> = () => &#123;"</span>,
      <span class="hljs-string">"  return ("</span>,
      <span class="hljs-string">"    <div className=&#123;styles.wrap&#125;>"</span>,
      <span class="hljs-string">"      $&#123;0&#125;"</span>,
      <span class="hljs-string">"    </div>"</span>,
      <span class="hljs-string">"  );"</span>,
      <span class="hljs-string">"&#125;;"</span>,
      <span class="hljs-string">""</span>,
      <span class="hljs-string">"export default $&#123;1:$&#123;TM_FILENAME_BASE&#125;&#125;;"</span>
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，在vscode的tsx 文件里面 敲tsrfc，就可以看到效果啦。</p></div>  
</div>
            