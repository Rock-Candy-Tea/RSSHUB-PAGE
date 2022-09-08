
---
title: '手把手教你搭建规范的团队vue项目，包含commitlint，eslint，prettier，husky，commitizen等等'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80895e8689724b89be4785174104b7ad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Tue, 06 Sep 2022 17:27:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80895e8689724b89be4785174104b7ad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h1 data-id="heading-0">1，前言</h1>
<hr>
<p>本文主要分享一个项目的规范约束从0到1的流程，从通过vue-cli创建项目，到团队协作插件安装（<code>husky</code>、<code>eslint</code>、<code>commitlint</code>、<code>prettier</code>等）。</p>
<ul>
<li>本文vue-cli脚手架为5.x</li>
<li>本文webpack版本为5.x</li>
<li>本文vue版本为3.x</li>
</ul>
<h1 data-id="heading-1">2，创建项目</h1>
<hr>
<p>如果你的<code>vue-cli</code>不是5.x版本，并且不知道怎么创建<code>vue-cli</code>项目，请先查看该文章：<a href="https://juejin.cn/post/7135691704656478222" target="_blank" title="https://juejin.cn/post/7135691704656478222">传送门</a></p>
<p>首先进入一个空间足够的磁盘，比如楼主是进的L盘，输入以下命令：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">vue create demo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建完毕后，项目结构如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80895e8689724b89be4785174104b7ad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="初始目录" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时可以打开<code>package.json</code>，查看项目当前装的依赖。默认是已经安装了<code>eslint</code>、<code>babel</code>和<code>vue</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"dependencies"</span>: &#123;
   <span class="hljs-string">"core-js"</span>: <span class="hljs-string">"^3.8.3"</span>,
   <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^3.2.13"</span>
 &#125;,
 <span class="hljs-string">"devDependencies"</span>: &#123;
   <span class="hljs-string">"@babel/core"</span>: <span class="hljs-string">"^7.12.16"</span>,
   <span class="hljs-string">"@babel/eslint-parser"</span>: <span class="hljs-string">"^7.12.16"</span>,
   <span class="hljs-string">"@vue/cli-plugin-babel"</span>: <span class="hljs-string">"~5.0.0"</span>,
   <span class="hljs-string">"@vue/cli-plugin-eslint"</span>: <span class="hljs-string">"~5.0.0"</span>,
   <span class="hljs-string">"@vue/cli-service"</span>: <span class="hljs-string">"~5.0.0"</span>,
   <span class="hljs-string">"eslint"</span>: <span class="hljs-string">"^7.32.0"</span>,
   <span class="hljs-string">"eslint-plugin-vue"</span>: <span class="hljs-string">"^8.0.3"</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">2，安装vue全家桶</h1>
<hr>
<p>先安装一些常用的vue生态，包括<code>axios</code>，<code>vue-router</code>，<code>vuex</code>，<code>qs</code>，<code>element-plus</code>等，具体使用可看下方教程链接：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install axios vue-router vuex qs element-plus --save
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://juejin.cn/post/7025416249173606413" target="_blank" title="https://juejin.cn/post/7025416249173606413">助你上手Vue3全家桶之Vue3教程</a></li>
<li><a href="https://juejin.cn/post/7025416467826868231" target="_blank" title="https://juejin.cn/post/7025416467826868231">助你上手Vue3全家桶之VueX4教程</a></li>
<li><a href="https://juejin.cn/post/7025416356816240670" target="_blank" title="https://juejin.cn/post/7025416356816240670">助你上手Vue3全家桶之Vue-Router4教程</a></li>
</ul>
<p>再安装<code>typescript</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install typescript@<span class="hljs-number">4.7</span> --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">3，配置prettier</h1>
<hr>
<ol>
<li>
<p>首先在根目录创建<code>.prettierrc.js</code>文件，这个文件是项目的<code>prettier</code>规则，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// tab缩进大小,默认为2</span>
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 使用tab缩进，默认false</span>
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 使用分号, 默认true</span>
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 使用单引号, 默认false(在jsx中配置无效, 默认都是双引号)</span>
  <span class="hljs-attr">jsxBracketSameLine</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 在jsx中把'>' 是否单独放一行</span>
  <span class="hljs-attr">jsxSingleQuote</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 在jsx中使用单引号代替双引号</span>
  <span class="hljs-attr">proseWrap</span>: <span class="hljs-string">'preserve'</span>, <span class="hljs-comment">// "always" - 当超出print width（上面有这个参数）时就折行 "never" - 不折行 "perserve" - 按照文件原样折行</span>
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">'none'</span>, <span class="hljs-comment">// 对象最后一项默认格式化会加逗号</span>
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">'avoid'</span>, <span class="hljs-comment">// 箭头函数参数括号 默认avoid 可选 avoid(能省略括号的时候就省略)| always(总是有括号)</span>
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 对象中的空格 默认true&#123; foo: bar &#125; false:&#123;foo: bar&#125;</span>
  <span class="hljs-attr">printWidth</span>: <span class="hljs-number">100</span> <span class="hljs-comment">// 一行多长，超过的会换行</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>然后在根目录创建<code>.prettierignore</code>文件，这个是设置有那些文件需要忽略<code>eslint</code>的检查，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">node_modules
dist
public
.<span class="hljs-property">vscode</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装<code>prettier</code>的扩展。<code>eslint-plugin-prettier</code>，<code>eslint-config-prettier</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install eslint-config-prettier eslint-plugin-prettier --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h1 data-id="heading-4">4，配置eslint</h1>
<hr>
<ol>
<li>
<p>首先在根目录创建<code>.eslintrc.js</code>，这个文件是项目的<code>eslint</code>规则，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">commonjs</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es6</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">amd</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">globals</span>: &#123; <span class="hljs-comment">// 允许的全局变量</span>
    <span class="hljs-title class_">TAny</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-title class_">TAnyType</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-title class_">TAnyArray</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-title class_">TAnyFunc</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-title class_">TDictArray</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-title class_">TDictObject</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'plugin:vue/vue3-essential'</span>, <span class="hljs-string">'airbnb-base'</span>, <span class="hljs-string">'@vue/typescript/recommended'</span>], <span class="hljs-comment">// 扩展插件</span>
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">2020</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
    <span class="hljs-attr">ecmaFeatures</span>: &#123;
      <span class="hljs-attr">tsx</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 允许解析TSX</span>
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">settings</span>: &#123;
    <span class="hljs-string">'import/resolver'</span>: &#123;
      <span class="hljs-attr">node</span>: &#123; <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'vue'</span>] &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'prettier'</span>],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-comment">// 0表示不不处理，1表示警告，2表示错误并退出</span>
    <span class="hljs-string">'vue/multi-word-component-names'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 要求组件名称始终为多字</span>
    <span class="hljs-string">'@typescript-eslint/no-unused-vars'</span>: [
      <span class="hljs-string">'error'</span>,
      &#123; <span class="hljs-attr">varsIgnorePattern</span>: <span class="hljs-string">'.*'</span>, <span class="hljs-attr">args</span>: <span class="hljs-string">'none'</span> &#125;
    ],
    <span class="hljs-attr">camelcase</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 驼峰命名</span>
    <span class="hljs-string">'prettier/prettier'</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 会优先采用prettierrc.json的配置，不符合规则会提示错误</span>
    <span class="hljs-string">'no-console'</span>: process.<span class="hljs-property">env</span>.<span class="hljs-property">NODE_ENV</span> === <span class="hljs-string">'production'</span> ? <span class="hljs-string">'warn'</span> : <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'no-debugger'</span>: process.<span class="hljs-property">env</span>.<span class="hljs-property">NODE_ENV</span> === <span class="hljs-string">'production'</span> ? <span class="hljs-string">'warn'</span> : <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'comma-dangle'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'import/prefer-default-export'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 优先export default导出</span>
    <span class="hljs-string">'no-param-reassign'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 函数参数属性的赋值</span>
    <span class="hljs-attr">semi</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-explicit-any'</span>: <span class="hljs-string">'warn'</span>,
    <span class="hljs-string">'no-unused-expressions'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 联式调用使用?</span>
    <span class="hljs-string">'import/no-cycle'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 导入循环引用报错</span>
    <span class="hljs-string">'arrow-parens'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 箭头函数一个参数可以不要括号</span>
    <span class="hljs-string">'no-underscore-dangle'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 无下划线</span>
    <span class="hljs-string">'no-plusplus'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">//  使用一元运算符</span>
    <span class="hljs-string">'object-curly-newline'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'no-restricted-syntax'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 使用for of</span>
    <span class="hljs-string">'operator-linebreak'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// after</span>
    <span class="hljs-string">'arrow-body-style'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/explicit-module-boundary-types'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// ts每个函数都要显式声明返回值</span>
    <span class="hljs-comment">// 暂时屏蔽检测@别名</span>
    <span class="hljs-string">'import/no-useless-path-segments'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'import/no-unresolved'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'import/extensions'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'import/no-absolute-path'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'import/no-extraneous-dependencies'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'newline-per-chained-call'</span>: [<span class="hljs-string">'error'</span>, &#123; <span class="hljs-attr">ignoreChainWithDepth</span>: <span class="hljs-number">10</span> &#125;],
    <span class="hljs-string">'linebreak-style'</span>: [<span class="hljs-number">0</span>, <span class="hljs-string">'error'</span>, <span class="hljs-string">'windows'</span>],
    <span class="hljs-string">'no-shadow'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 注意你必须禁用基本规则，因为它可以报告不正确的错误</span>
    <span class="hljs-string">'@typescript-eslint/no-shadow'</span>: [<span class="hljs-string">'error'</span>],
    <span class="hljs-string">'@typescript-eslint/member-delimiter-style'</span>: [
      <span class="hljs-string">'error'</span>,
      &#123;
        <span class="hljs-attr">multiline</span>: &#123;
          <span class="hljs-attr">delimiter</span>: <span class="hljs-string">'none'</span>,
          <span class="hljs-attr">requireLast</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-attr">singleline</span>: &#123;
          <span class="hljs-attr">delimiter</span>: <span class="hljs-string">'semi'</span>,
          <span class="hljs-attr">requireLast</span>: <span class="hljs-literal">false</span>,
        &#125;,
      &#125;,
    ],
    <span class="hljs-string">'keyword-spacing'</span>: [
      <span class="hljs-number">2</span>,
      &#123;
        <span class="hljs-attr">before</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">after</span>: <span class="hljs-literal">true</span>,
      &#125;,
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>然后在根目录创建<code>.eslintignore</code>文件，这个是设置那些文件需要忽略<code>eslint</code>的检查，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">node_modules
dist
.<span class="hljs-property">vscode</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装<code>eslint</code>的扩展。<code>eslint-config-airbnb-base</code>，<code>@typescript-eslint/eslint-plugin</code>，<code>@typescript-eslint/parser</code>，<code>@vue/eslint-config-typescript</code>，<code>eslint-plugin-import</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install eslint-config-airbnb-base @typescript-eslint/eslint-plugin @vue/eslint-config-typescript @typescript-eslint/parser eslint-plugin-<span class="hljs-keyword">import</span> --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>到这一步，就可以在<code>package.json</code>文件里的<code>scripts</code>对象里添加一行自动修复文件的命令 <code>lint-fix</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"vue-cli-service build"</span>,
    <span class="hljs-string">"lint-fix"</span>: <span class="hljs-string">"vue-cli-service lint --fix ./src --ext .vue,.js,.ts"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录打开终端，输入<code>npm run lint-fix</code>，会按照你的<code>eslint</code>要求自动进行修复，部分修复不了的需要手动修改。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecc9cc27e62d4b678841c299d0bc6e6c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="自动修复" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">5，配置husky + git钩子</h1>
<hr>
<p><code>husky</code>是一个让配置<code>git</code>钩子变得更简单的工具，支持所有的<code>git</code>钩子。它可以将<code>git</code>内置的钩子暴露出来，很方便地进行钩子命令注入，而不需要在<code>.git/hooks</code>目录下自己写<code>shell</code>脚本了。您可以使用它来<code>lint</code>您的提交消息、运行测试、<code>lint</code>代码等。当你<code>commit</code>或<code>push</code>的时候。<code>husky</code>触发所有<code>git</code>钩子脚本。</p>
<ol>
<li>
<p>安装<code>husky</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install husky --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>启用<code>husky</code>，启用后，根目录会出现一个<code>.husky</code>的文件夹</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npx husky install
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>编辑<code>package.json</code>文件，在<code>scripts</code>中添加<code>"prepare": "husky install"</code>命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"vue-cli-service build"</span>,
    <span class="hljs-string">"lint-fix"</span>: <span class="hljs-string">"vue-cli-service lint --fix ./src --ext .vue,.js,.ts"</span>,
    <span class="hljs-string">"prepare"</span>: <span class="hljs-string">"husky install"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在<code>.husky</code>文件夹中，新建<code>pre-commit</code>文件，写入以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

npx lint-staged --allow-empty
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装<code>lint-staged</code>，这是本地暂存代码的检查工具，当你<code>git</code>提交代码时，会自动检查是否符合项目<code>eslint</code>和<code>prettier</code>规范</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install lint-staged --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在项目根目录创建<code>.lintstagedrc.json</code>文件，写入以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"*.&#123;ts,js,vue,tsx,jsx&#125;"</span>: [<span class="hljs-string">"npm run lint-fix"</span>, <span class="hljs-string">"prettier --write"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>到这一步，<code>git</code>提交的时候，会自动根据项目<code>eslint</code>和<code>prettier</code>规范修复代码并提交，如果碰到修复不了的，会取消提交。</p>
<h1 data-id="heading-6">6，配置commitlint</h1>
<hr>
<p>在<code>git</code>提交时，如果能找按照规范写好提交信息，能提高可读性以及项目维护效率，方便回溯。这里我们使用<code>commitlint</code>规范<code>git commit</code>提交的信息。</p>
<h2 data-id="heading-7">6.1，配置commitlint格式检查</h2>
<ol>
<li>
<p>首先安装<code>@commitlint/cli</code>和<code>@commitlint/config-conventional</code>（如果要自定义提交规范，就不用安装<code>@commitlint/config-conventional</code>）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install @commitlint/cli @commitlint/config-conventional --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在项目根目录的<code>.husky</code>文件夹中，新建<code>commit-msg</code>文件，写入以下内容：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

npx commitlint --edit $<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在项目根目录新建<code>commitlint.config.js</code>文件，写入以下内容：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
"off"或者0:关闭规则 "warn"或1:开启规则抛出警告 "error"或2:开启规则抛出错误
*/</span>
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'@commitlint/config-conventional'</span>],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'body-leading-blank'</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// body上面有换行</span>
    <span class="hljs-string">'footer-leading-blank'</span>: [<span class="hljs-number">1</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// footer上面有换行</span>
    <span class="hljs-string">'header-max-length'</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">'always'</span>, <span class="hljs-number">108</span>], <span class="hljs-comment">// header上最大108字符</span>
    <span class="hljs-string">'type-case'</span>: [<span class="hljs-number">0</span>],
    <span class="hljs-string">'type-empty'</span>: [<span class="hljs-number">0</span>],
    <span class="hljs-string">'scope-empty'</span>: [<span class="hljs-number">0</span>],
    <span class="hljs-string">'scope-case'</span>: [<span class="hljs-number">0</span>],
    <span class="hljs-string">'subject-full-stop'</span>: [<span class="hljs-number">0</span>, <span class="hljs-string">'never'</span>],
    <span class="hljs-string">'subject-case'</span>: [<span class="hljs-number">0</span>, <span class="hljs-string">'never'</span>],
    <span class="hljs-string">'type-enum'</span>: [
      <span class="hljs-number">2</span>,
      <span class="hljs-string">'always'</span>,
      [
        <span class="hljs-string">'feat'</span>, <span class="hljs-comment">// 新增功能、页面</span>
        <span class="hljs-string">'fix'</span>, <span class="hljs-comment">// 修补bug</span>
        <span class="hljs-string">'docs'</span>, <span class="hljs-comment">// 修改文档、注释</span>
        <span class="hljs-string">'style'</span>, <span class="hljs-comment">// 格式：不影响代码运行的变动、空格、格式化等等</span>
        <span class="hljs-string">'ui'</span>, <span class="hljs-comment">// ui修改：布局、css样式等等</span>
        <span class="hljs-string">'hotfix'</span>, <span class="hljs-comment">// 修复线上紧急bug</span>
        <span class="hljs-string">'build'</span>, <span class="hljs-comment">// 改变构建流程，新增依赖库、工具等（例如:修改webpack）</span>
        <span class="hljs-string">'refactor'</span>, <span class="hljs-comment">// 代码重构，未新增任何功能和修复任何bug</span>
        <span class="hljs-string">'revert'</span>, <span class="hljs-comment">// 回滚到上一个版本</span>
        <span class="hljs-string">'perf'</span>, <span class="hljs-comment">// 优化：提升性能、用户体验等</span>
        <span class="hljs-string">'ci'</span>, <span class="hljs-comment">// 对CI/CD配置文件和脚本的更改</span>
        <span class="hljs-string">'chore'</span>, <span class="hljs-comment">// 其他不修改src或测试文件的更改</span>
        <span class="hljs-string">'test'</span>, <span class="hljs-comment">// 测试用例：包括单元测试、集成测试</span>
    <span class="hljs-string">'update'</span> <span class="hljs-comment">// 更新：普通更新</span>
      ]
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在git提交时，填写的<code>commit</code>信息格式规范如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><type>(<scope>): <subject> <span class="hljs-comment">// 必填</span>
<span class="hljs-comment">// 空一行</span>
<body> <span class="hljs-comment">// 必填</span>
<span class="hljs-comment">// 空一行</span>
<footer> <span class="hljs-comment">// 可忽略不填</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">git commit -m <span class="hljs-string">'style(home.vue):修改样式

修改了home.vue的样式，添加了背景色'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-8">6.2，安装自定义的辅助提交依赖commitizen</h2>
<ol>
<li>
<p>首先需要安装<code>commitizen</code>和<code>commitlint-config-cz</code>和<code>cz-customizable</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install commitizen commitlint-config-cz cz-customizable --save -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>然后新建<code>.cz-config.js</code>文件，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">'use strict'</span>
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">types</span>: [
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'feat'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'新增：新增功能、页面'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'fix'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'bug：修复某个bug'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'docs'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'文档：修改增加文档、注释'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'style'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'格式：不影响代码运行的变动、空格、格式化等等'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'ui'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'ui修改：布局、css样式等等'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'hotfix'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'bug：修复线上紧急bug'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'build'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'测试：添加一个测试'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'refactor'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'重构：代码重构，未新增任何功能和修复任何bug'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'revert'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'回滚：代码回退到某个版本节点'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'perf'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'优化：提升性能、用户体验等'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'ci'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'自动化构建：对CI/CD配置文件和脚本的更改'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'chore'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'其他修改：不修改src目录或测试文件的修改'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'test'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'测试：包括单元测试、集成测试'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'update'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'更新：普通更新'</span> &#125;
  ],
  <span class="hljs-comment">// 交互提示信息</span>
  <span class="hljs-attr">messages</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'选择一种你的提交类型：'</span>,
    <span class="hljs-attr">scope</span>: <span class="hljs-string">'选择一个影响范围（可选）:'</span>,
    <span class="hljs-attr">customScope</span>: <span class="hljs-string">'表示此更改的范围：'</span>,
    <span class="hljs-attr">subject</span>: <span class="hljs-string">'短说明：\n'</span>,
    <span class="hljs-attr">body</span>: <span class="hljs-string">'长说明，使用"|"符号换行（可选）：\n'</span>,
    <span class="hljs-attr">breaking</span>: <span class="hljs-string">'非兼容性说明（可选）：\n'</span>,
    <span class="hljs-attr">footer</span>: <span class="hljs-string">'关闭的issue，例如：#31, #34（可选）：\n'</span>,
    <span class="hljs-attr">confirmCommit</span>: <span class="hljs-string">'确定提交说明?（yes/no）'</span>
  &#125;,
  <span class="hljs-attr">allowCustomScopes</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 设置选择了那些type，才询问 breaking message</span>
  <span class="hljs-attr">allowBreakingChanges</span>: [<span class="hljs-string">'feat'</span>, <span class="hljs-string">'fix'</span>, <span class="hljs-string">'ui'</span>, <span class="hljs-string">'hotfix'</span>, <span class="hljs-string">'update'</span>, <span class="hljs-string">'perf'</span>],
  <span class="hljs-attr">subjectLimit</span>: <span class="hljs-number">100</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>然后修改<code>commitlint.config.js</code>文件的<code>extends</code>选项，改成<code>['cz']</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
<span class="hljs-attr">extends</span>: [<span class="hljs-string">'cz'</span>],
......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>编辑<code>package.json</code>文件，在<code>scripts</code>中添加<code>"commit": "git-cz"</code>命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"vue-cli-service build"</span>,
    <span class="hljs-string">"lint-fix"</span>: <span class="hljs-string">"vue-cli-service lint --fix ./src --ext .vue,.js,.ts"</span>,
    <span class="hljs-string">"prepare"</span>: <span class="hljs-string">"husky install"</span>,
    <span class="hljs-string">"commit"</span>: <span class="hljs-string">"git-cz"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在根目录终端，运行以下命令初始化命令行的选项信息：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npx commitizen init cz-customizable --save-dev --save-exact
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>运行完成后，在<code>package.json</code>中会出现如下选项：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"config"</span>: &#123;
    <span class="hljs-string">"commitizen"</span>: &#123;
      <span class="hljs-string">"path"</span>: <span class="hljs-string">"./node_modules/cz-customizable"</span>
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>此时，代码提交过程就多了一个可选的规范提示，提交流程是先<code>git add .</code>，提交到暂存区，然后终端运行<code>npm run commit</code>，根据提示选择信息或者输入即可，最后<code>git push</code>推送，如下gif图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bad95e9e1d3438297d0d69b4e34d050~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="提交代码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>附几个我个人的项目模板：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FVite-H5-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/Vite-H5-Template" ref="nofollow noopener noreferrer">Vite-H5-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FVite-PC-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/Vite-PC-Template" ref="nofollow noopener noreferrer">Vite-PC-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FWebpack-PC-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/Webpack-PC-Template" ref="nofollow noopener noreferrer">Webpack-PC-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FH5-V2-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/H5-V2-Template" ref="nofollow noopener noreferrer">H5-V2-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FUniapp-Cli-V2-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/Uniapp-Cli-V2-Template" ref="nofollow noopener noreferrer">Uniapp-Cli-V2-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FUniapp-Cli-Ts-V3-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/Uniapp-Cli-Ts-V3-Template" ref="nofollow noopener noreferrer">Uniapp-Cli-Ts-V3-Template</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086%2FPC-V2-Template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086/PC-V2-Template" ref="nofollow noopener noreferrer">PC-V2-Template</a></li>
</ul>
<hr>
<p><strong>如果看了觉得有帮助的，我是@上进的鹏多多，欢迎 点赞 关注 评论；</strong></p>
<blockquote>
<p>PS：在本页按F12，在console中输入document.querySelectorAll('.like-btn')[0].click()，有惊喜哦</p>
</blockquote>
<p><code>往期文章</code></p>
<ul>
<li><a href="https://juejin.cn/post/7025416249173606413" target="_blank" title="https://juejin.cn/post/7025416249173606413">助你上手Vue3全家桶之Vue3教程</a></li>
<li><a href="https://juejin.cn/post/7025416467826868231" target="_blank" title="https://juejin.cn/post/7025416467826868231">助你上手Vue3全家桶之VueX4教程</a></li>
<li><a href="https://juejin.cn/post/7025416356816240670" target="_blank" title="https://juejin.cn/post/7025416356816240670">助你上手Vue3全家桶之Vue-Router4教程</a></li>
<li><a href="https://juejin.cn/post/6953803916484018206" target="_blank" title="https://juejin.cn/post/6953803916484018206">使用nvm管理node.js版本以及更换npm淘宝镜像源</a></li>
<li><a href="https://juejin.cn/post/6926773339411185671" target="_blank" title="https://juejin.cn/post/6926773339411185671">超详细！Vue的九种通信方式</a></li>
<li><a href="https://juejin.cn/post/6944950213538742279" target="_blank" title="https://juejin.cn/post/6944950213538742279">微信小程序实现搜索关键词高亮</a></li>
<li><a href="https://juejin.cn/post/6956491743537659941" target="_blank" title="https://juejin.cn/post/6956491743537659941">vue中利用.env文件存储全局环境变量，以及配置vue启动和打包命令</a></li>
<li><a href="https://juejin.cn/post/6989050898789957639" target="_blank" title="https://juejin.cn/post/6989050898789957639">超详细！Vuex手把手教程</a></li>
<li><a href="https://juejin.cn/post/6994259004318810120" target="_blank" title="https://juejin.cn/post/6994259004318810120">超详细！Vue-Router手把手教程</a></li>
</ul>
<p><code>个人主页</code></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fpdd11997110103%3Fspm%3D1010.2135.3001.5421" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/pdd11997110103?spm=1010.2135.3001.5421" ref="nofollow noopener noreferrer">CSDN</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwp993080086" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wp993080086" ref="nofollow noopener noreferrer">GitHub</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2Fb7a8536bff06" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/b7a8536bff06" ref="nofollow noopener noreferrer">简书</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2F-pdd%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/-pdd/" ref="nofollow noopener noreferrer">博客园</a></li>
<li><a href="https://juejin.cn/user/747323639737191" target="_blank" title="https://juejin.cn/user/747323639737191">掘金</a></li>
</ul></div>  
</div>
            