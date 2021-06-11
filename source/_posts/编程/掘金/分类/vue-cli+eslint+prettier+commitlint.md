
---
title: 'vue-cli+eslint+prettier+commitlint'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2037bde8a2b4206aa5b314386429d95~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 03:46:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2037bde8a2b4206aa5b314386429d95~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">查看vue-cli版本</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2037bde8a2b4206aa5b314386429d95~tplv-k3u1fbpfcp-zoom-1.image" alt="查看vue-cli版本" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">vue-cli创建项目</h2>
<p>vue create demo 或 如下图 （解决window下光标无法上下选择问题）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/153347c2ef37438692de349eab74bdc9~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-cli创建项目" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81a581ca30424733af1a0ce36e195d13~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-cli创建项目" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择 Manually select features</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2b0fd5d5ab4f309eaf3acc9eaf84b2~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-cli创建项目" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择Lint / Formatter 其他根据自己情况选择，vue的版本我选择2.0</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50387ea81c7e43fe8e111f63650cceb6~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-cli创建项目" loading="lazy" referrerpolicy="no-referrer">
选择dart-sass，查了资料说dart-sass比node-sass性能要好，回车，就自动安装依赖</p>
<h2 data-id="heading-2">Prettier配置</h2>
<p>根目录下创建prettierrc.config.js文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// tab缩进大小，默认为2</span>
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>,
  <span class="hljs-comment">// 使用tab缩进，默认false</span>
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 使用分号，默认true</span>
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 使用单引号, 默认false，(在jsx中配置无效, 默认都是双引号)</span>
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 行尾逗号，默认none，可选（none|es5|all），es5 包括es5中的数组、对象，all 包括函数对象等所有可选</span>
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">"all"</span>,
  <span class="hljs-comment">// 对象中的空格 默认true，true: &#123; foo: bar &#125;，false: &#123;foo: bar&#125;</span>
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// JSX标签闭合位置 默认false</span>
  <span class="hljs-attr">jsxBracketSameLine</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// 箭头函数参数括号 默认avoid 可选（avoid|always），avoid 能省略括号的时候就省略 例如x => x ，always 总是有括号</span>
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">"avoid"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改package.json</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>,
      <span class="hljs-string">"commit-msg"</span>: <span class="hljs-string">"commitlint -E HUSKY_GIT_PARAMS"</span>
    &#125;
  &#125;,
  <span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-string">"*.&#123;js,jsx,vue&#125;"</span>: [
      <span class="hljs-string">"vue-cli-service lint ./src --fix"</span>,
      <span class="hljs-string">"prettier --write ./src"</span>,
      <span class="hljs-string">"git add"</span>
    ]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Eslint配置</h2>
<p>修改.eslintrc.js里rules字段，添加如下配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">rules: &#123;
    <span class="hljs-string">"prettier/prettier"</span>: <span class="hljs-string">"off"</span>,

    <span class="hljs-string">"no-console"</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"warn"</span> : <span class="hljs-string">"off"</span>,
    <span class="hljs-string">"no-debugger"</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"warn"</span> : <span class="hljs-string">"off"</span>,

    <span class="hljs-comment">/**
     * 代码中可能的错误或逻辑错误
     */</span>
    <span class="hljs-string">"no-cond-assign"</span>: [<span class="hljs-string">"error"</span>, <span class="hljs-string">"always"</span>], <span class="hljs-comment">// 禁止条件表达式中出现赋值操作符</span>
    <span class="hljs-string">"no-constant-condition"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">checkLoops</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 禁止在条件中使用常量表达式</span>
    <span class="hljs-string">"no-control-regex"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在正则表达式中使用控制字符</span>
    <span class="hljs-string">"no-debugger"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用 debugger</span>
    <span class="hljs-string">"no-dupe-args"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止 function 定义中出现重名参数</span>
    <span class="hljs-string">"no-dupe-keys"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止对象字面量中出现重复的 key</span>
    <span class="hljs-string">"no-duplicate-case"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止出现重复的 case 标签</span>
    <span class="hljs-string">"no-empty"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">allowEmptyCatch</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 禁止出现空语句块</span>
    <span class="hljs-string">"no-empty-character-class"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在正则表达式中使用空字符集</span>
    <span class="hljs-string">"no-ex-assign"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止对 catch 子句的参数重新赋值</span>
    <span class="hljs-string">"no-extra-boolean-cast"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止不必要的布尔转换</span>
    <span class="hljs-string">"no-extra-semi"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止不必要的分号</span>
    <span class="hljs-string">"no-func-assign"</span>: [<span class="hljs-string">"warn"</span>], <span class="hljs-comment">// 禁止对 function 声明重新赋值</span>
    <span class="hljs-string">"no-inner-declarations"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在嵌套的块中出现变量声明或 function 声明</span>
    <span class="hljs-string">"no-invalid-regexp"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">allowConstructorFlags</span>: [] &#125;], <span class="hljs-comment">// 禁止 RegExp 构造函数中存在无效的正则表达式字符串</span>
    <span class="hljs-string">"no-irregular-whitespace"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在字符串和注释之外不规则的空白</span>
    <span class="hljs-string">"no-obj-calls"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止把全局对象作为函数调用</span>
    <span class="hljs-string">"no-regex-spaces"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止正则表达式字面量中出现多个空格</span>
    <span class="hljs-string">"no-sparse-arrays"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用稀疏数组</span>
    <span class="hljs-string">"no-unexpected-multiline"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止出现令人困惑的多行表达式</span>
    <span class="hljs-string">"no-unsafe-finally"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在 finally 语句块中出现控制流语句</span>
    <span class="hljs-string">"no-unsafe-negation"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止对关系运算符的左操作数使用否定操作符</span>
    <span class="hljs-string">"use-isnan"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 要求使用 isNaN() 检查 NaN</span>

    <span class="hljs-comment">/**
     * 最佳实践
     */</span>
    <span class="hljs-string">"default-case"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 要求 switch 语句中有 default 分支</span>
    <span class="hljs-string">"dot-notation"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 强制尽可能地使用点号</span>
    <span class="hljs-attr">eqeqeq</span>: [<span class="hljs-string">"warn"</span>], <span class="hljs-comment">// 要求使用 === 和 !==</span>
    <span class="hljs-string">"no-caller"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用 arguments.caller 或 arguments.callee</span>
    <span class="hljs-string">"no-case-declarations"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 不允许在 case 子句中使用词法声明</span>
    <span class="hljs-string">"no-empty-function"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止出现空函数</span>
    <span class="hljs-string">"no-empty-pattern"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止使用空解构模式</span>
    <span class="hljs-string">"no-eval"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用 eval()</span>
    <span class="hljs-string">"no-global-assign"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止对原生对象或只读的全局对象进行赋值</span>
    <span class="hljs-string">"no-magic-numbers"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">ignoreArrayIndexes</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 禁用魔术数字</span>
    <span class="hljs-string">"no-redeclare"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">builtinGlobals</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 禁止重新声明变量</span>
    <span class="hljs-string">"no-self-assign"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">props</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 禁止自我赋值</span>
    <span class="hljs-string">"no-unused-labels"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用出现未使用过的标</span>
    <span class="hljs-string">"no-useless-escape"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用不必要的转义字符</span>
    <span class="hljs-attr">radix</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 强制在parseInt()使用基数参数</span>

    <span class="hljs-comment">/**
     * 变量声明
     */</span>
    <span class="hljs-string">"no-delete-var"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止删除变量</span>
    <span class="hljs-string">"no-undef"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁用未声明的变量，除非它们在 /*global */ 注释中被提到</span>
    <span class="hljs-string">"no-unused-vars"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止出现未使用过的变量</span>
    <span class="hljs-string">"no-use-before-define"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 禁止在变量定义之前使用它们</span>

    <span class="hljs-comment">/**
     * ECMAScript 6
     */</span>
    <span class="hljs-string">"arrow-spacing"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">before</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">after</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 强制箭头函数的箭头前后使用一致的空格</span>
    <span class="hljs-string">"no-var"</span>: [<span class="hljs-string">"error"</span>], <span class="hljs-comment">// 要求使用 let 或 const 而不是 var</span>
    <span class="hljs-string">"object-shorthand"</span>: [<span class="hljs-string">"error"</span>, <span class="hljs-string">"always"</span>], <span class="hljs-comment">// 要求或禁止对象字面量中方法和属性使用简写语法</span>
    <span class="hljs-string">"prefer-arrow-callback"</span>: [<span class="hljs-string">"error"</span>, &#123; <span class="hljs-attr">allowNamedFunctions</span>: <span class="hljs-literal">false</span> &#125;], <span class="hljs-comment">// 要求回调函数使用箭头函数</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">安装commitlint</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac3cf178883439f925a66f361583825~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">commit规范</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span> 提交格式
git commit -m <type>[optional scope]: <description>

<span class="hljs-number">2.</span> 常用的type类别
type ：用于表明我们这次提交的改动类型，是新增了功能？还是修改了测试代码？又或者是更新了文档？总结以下 <span class="hljs-number">11</span> 种类型：
• build：主要目的是修改项目构建系统(例如 glup，webpack，rollup 的配置等)的提交
• ci：主要目的是修改项目继续集成流程(例如 Travis，Jenkins，GitLab CI，Circle等)的提交
• docs：文档更新
• feat：新增功能
• fix：bug 修复
• perf：性能优化
• refactor：重构代码(既没有新增功能，也没有修复 bug)
• style：不影响程序逻辑的代码修改(修改空白字符，补全缺失的分号等)
• test：新增测试用例或是更新现有测试
• revert：回滚某个更早之前的提交
• chore：不属于以上类型的其他类型(日常事务)
optional scope：一个可选的修改范围。用于标识此次提交主要涉及到代码中哪个模块。
description：一句话描述此次提交的主要内容，做到言简意赅。

例如：
git commit -m <span class="hljs-string">'feat: 增加 xxx 功能'</span>
git commit -m <span class="hljs-string">'bug: 修复 xxx 功能'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">效果如图</h2>
<p>eslint校验失败</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2840f6ca7d5d4bff8d9a066b0f6d05cc~tplv-k3u1fbpfcp-zoom-1.image" alt="eslint校验失败" loading="lazy" referrerpolicy="no-referrer"></p>
<p>commitlint校验失败</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e2d8bb2a9d846babc1a454cf97a9839~tplv-k3u1fbpfcp-zoom-1.image" alt="commitlint校验失败" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功提交</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4c948ad559e46cdb9844b665c346503~tplv-k3u1fbpfcp-zoom-1.image" alt="成功提交" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            