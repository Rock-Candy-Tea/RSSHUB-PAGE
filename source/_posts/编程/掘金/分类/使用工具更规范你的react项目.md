
---
title: '使用工具更规范你的react项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fff9dfa783488281274c55fae57857~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 04:49:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fff9dfa783488281274c55fae57857~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、配置<code>prettier</code></h2>
<ul>
<li>
<p>1、使用<code>npx</code>初始化一个项目，这里我使用<code>typescript</code>模板的方式构建项目</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npx</span> <span class="hljs-string">create-react-app react-demo1 --template typescript</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2、参考官方的方式配置，<a href="https://prettier.io/docs/en/install.html" target="_blank" rel="nofollow noopener noreferrer">官方地址</a></p>
</li>
<li>
<p>3、安装插件包</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npm</span> <span class="hljs-string">install --save-dev --save-exact prettier</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、在根目录下创建一个<code>.prettierrc</code>和<code>.prettierignore</code>的文件</p>
<ul>
<li><code>prettierr</code>文件是配置<code>prettierr</code>规则的</li>
<li><code>.prettierignore</code>是配置不需要<code>prettierr</code>的文件，有点类似<code>.gitignore</code>的作用</li>
</ul>
</li>
<li>
<p>5、在<code>.prettierignore</code>配置</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">build</span>
<span class="hljs-attr">coverage</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>6、在<code>.prettierr</code>中配置，以下是我自己项目中配置的，仅供参考</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">&#123;</span>
  <span class="hljs-meta">"prettier.semi"</span>: <span class="hljs-string">true,</span>
  <span class="hljs-meta">"singleQuote"</span>: <span class="hljs-string">true,</span>
  <span class="hljs-meta">"trailingComma"</span>: <span class="hljs-string">"es5",</span>
  <span class="hljs-meta">"printWidth"</span>: <span class="hljs-string">100,</span>
  <span class="hljs-meta">"tabWidth"</span>: <span class="hljs-string">2,</span>
  <span class="hljs-meta">"endOfLine"</span>: <span class="hljs-string">"auto",</span>
  <span class="hljs-meta">"arrowParens"</span>: <span class="hljs-string">"always"</span>
<span class="hljs-attr">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多配置可以参考官方，<a href="https://prettier.io/docs/en/options.html" target="_blank" rel="nofollow noopener noreferrer">官网地址</a>，以下是我提供的文字说明</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">&#123;</span>
    <span class="hljs-meta">"printWidth"</span>: <span class="hljs-string">100, // 超过最大值换行</span>
    <span class="hljs-meta">"tabWidth"</span>: <span class="hljs-string">4, // 缩进字节数</span>
    <span class="hljs-meta">"useTabs"</span>: <span class="hljs-string">false, // 缩进不使用tab，使用空格</span>
    <span class="hljs-meta">"semi"</span>: <span class="hljs-string">true, // 句尾添加分号</span>
    <span class="hljs-meta">"singleQuote"</span>: <span class="hljs-string">true, // 使用单引号代替双引号</span>
    <span class="hljs-meta">"proseWrap"</span>: <span class="hljs-string">"preserve", // 默认值。因为使用了一些折行敏感型的渲染器（如GitHub comment）而按照markdown文本样式进行折行</span>
    <span class="hljs-meta">"arrowParens"</span>: <span class="hljs-string">"avoid", //  (x) => &#123;&#125; 箭头函数参数只有一个时是否要有小括号。avoid：省略括号</span>
    <span class="hljs-meta">"bracketSpacing"</span>: <span class="hljs-string">true, // 在对象，数组括号与文字之间加空格 "&#123; foo: bar &#125;"</span>
    <span class="hljs-meta">"disableLanguages"</span>: <span class="hljs-string">["vue"], // 不格式化vue文件，vue文件的格式化单独设置</span>
    <span class="hljs-meta">"endOfLine"</span>: <span class="hljs-string">"auto", // 结尾是 \n \r \n\r auto</span>
    <span class="hljs-meta">"eslintIntegration"</span>: <span class="hljs-string">false, //不让prettier使用eslint的代码格式进行校验</span>
    <span class="hljs-meta">"htmlWhitespaceSensitivity"</span>: <span class="hljs-string">"ignore",</span>
    <span class="hljs-meta">"ignorePath"</span>: <span class="hljs-string">".prettierignore", // 不使用prettier格式化的文件填写在项目的.prettierignore文件中</span>
    <span class="hljs-meta">"jsxBracketSameLine"</span>: <span class="hljs-string">false, // 在jsx中把'>' 是否单独放一行</span>
    <span class="hljs-meta">"jsxSingleQuote"</span>: <span class="hljs-string">false, // 在jsx中使用单引号代替双引号</span>
    <span class="hljs-meta">"parser"</span>: <span class="hljs-string">"babylon", // 格式化的解析器，默认是babylon</span>
    <span class="hljs-meta">"requireConfig"</span>: <span class="hljs-string">false, // Require a 'prettierconfig' to format prettier</span>
    <span class="hljs-meta">"stylelintIntegration"</span>: <span class="hljs-string">false, //不让prettier使用stylelint的代码格式进行校验</span>
    <span class="hljs-meta">"trailingComma"</span>: <span class="hljs-string">"es5", // 在对象或数组最后一个元素后面是否加逗号（在ES5中加尾逗号）</span>
    <span class="hljs-meta">"tslintIntegration"</span>: <span class="hljs-string">false // 不让prettier使用tslint的代码格式进行校验</span>
<span class="hljs-attr">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ul>
<li>
<p>7、由于<code>create-react-app</code>创建的项目自带了<code>eslint</code>的规范，我们又加一个<code>prettierr</code>，自然会出现有冲突的时候，这时候我们就要告知使用谁的规范。可以简单的理解为优先级吧，<a href="https://prettier.io/docs/en/install.html#eslint-and-other-linters" target="_blank" rel="nofollow noopener noreferrer">参考官网</a></p>
<ul>
<li>
<p>安装依赖包</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npm</span> <span class="hljs-string">install eslint-config-prettier -D</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在<code>package.json</code>中配置下</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
   ...
    <span class="hljs-attr">"eslintConfig"</span>: &#123;
    <span class="hljs-attr">"extends"</span>: [
      <span class="hljs-string">"react-app"</span>,
      <span class="hljs-string">"react-app/jest"</span>,
      <span class="hljs-comment">// 添加这行代码</span>
      <span class="hljs-string">"prettier"</span>
    ]
  &#125;,
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">二、配置<code>git</code>的钩子函数，对每次<code>commit</code>的时候就使用<code>prettierr</code>格式化代码</h2>
<ul>
<li>
<p>1、<a href="https://prettier.io/docs/en/precommit.html" target="_blank" rel="nofollow noopener noreferrer">参考地址</a></p>
</li>
<li>
<p>2、使用<code>npx</code>生成文件</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npx</span> <span class="hljs-string">mrm lint-staged</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>3、运行上面的命令会自动在<code>package.json</code>中添加配置</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"lint-staged"</span>:
    <span class="hljs-comment">// 默认生成的</span>
    <span class="hljs-comment">// "*.&#123;js,css,md&#125;": "prettier --write"</span>
    <span class="hljs-comment">// 项目是要使用ts的话就要添加下</span>
    <span class="hljs-string">"*.&#123;ts,tsx,css,md&#125;"</span>: <span class="hljs-string">"prettier --write"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、在<code>package.json</code>中添加<code>husky</code>的提交钩子</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  ...
  <span class="hljs-attr">"husky"</span>: &#123;
    <span class="hljs-attr">"hooks"</span>: &#123;
      <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"lint-staged"</span>: &#123;
    <span class="hljs-attr">"*.&#123;js,ts,tsx&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>,
      <span class="hljs-comment">// 添加这行表示修复后会自动执行git add操作</span>
      <span class="hljs-string">"git add"</span>
    ]
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ul>
<li>5、修改下<code>index.ts</code>文件,将单引号改为双引号，把分号去掉，然后使用<code>git</code>提交代码查看文件是不是自动格式化了</li>
</ul>
<h2 data-id="heading-2">三、配置<code>git</code>的提交规范</h2>
<ul>
<li>
<p>1、<a href="https://github.com/conventional-changelog/commitlint" target="_blank" rel="nofollow noopener noreferrer">参考文档</a></p>
</li>
<li>
<p>2、安装依赖包</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npm</span> <span class="hljs-string">install --save-dev @commitlint/config-conventional @commitlint/cli</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>3、生产一个<code>commitlint.config.js</code>文件</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">echo</span> <span class="hljs-string">"module.exports = &#123;extends: ['@commitlint/config-conventional']&#125;" > commitlint.config.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是我自己根据网上的修改了下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'@commitlint/config-conventional'</span>],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'type-enum'</span>: [
      <span class="hljs-number">2</span>,
      <span class="hljs-string">'always'</span>,
      [<span class="hljs-string">'upd'</span>, <span class="hljs-string">'feat'</span>, <span class="hljs-string">'fix'</span>, <span class="hljs-string">'docs'</span>, <span class="hljs-string">'style'</span>, <span class="hljs-string">'refactor'</span>, <span class="hljs-string">'test'</span>, <span class="hljs-string">'chore'</span>],
    ],
  &#125;,
&#125;;

<span class="hljs-comment">/**
 * https://segmentfault.com/a/1190000017790694
 * upd: 更新
 * feat: 新增
 * fix: 修复
 * docs: 文档
 * style: 样式
 * refactor: 重构代码
 * test: 单元测试
 * chore: 构建过程或辅助工具的变动
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、生成提示信息的</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npx</span> <span class="hljs-string">husky add .husky/commit-msg 'npx --no-install commitlint --edit "$1"'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>5、测试提交</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42fff9dfa783488281274c55fae57857~tplv-k3u1fbpfcp-watermark.image" alt="image-20210604201407638.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>6、每次提交代码的时候必须带上说明</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">git</span> <span class="hljs-string">add .</span>
<span class="hljs-attr">git</span> <span class="hljs-string">commit -m 'feat: 新增代码'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-3">四、配置<code>eslint</code>的</h2>
<p>也许你会说上面每次提交代码都会自动帮我们格式化，但是我们更加希望在我们写代码的时候，每次保存代码的时候就能发现哪里不规范，这样提交代码的时候直接提交，不需要再来一个一个修改。</p>
<ul>
<li>
<p>1、初始化<code>eslint</code>，等待一瞬间会在项目的根目录下生成一个<code>.eslintrc.js</code>的文件</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npx</span> <span class="hljs-string">eslint --init</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70d97a74cb3345438668d8de0c670e1c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210604202306849.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>2、相对于的在项目的根目录下创建<code>.eslintignore</code>来忽视不需要检查的文件</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-comment"># 注释，忽略文件</span>
<span class="hljs-attr">node_modules</span>
<span class="hljs-attr">src/serviceWorker.ts</span>
<span class="hljs-attr">src/react-app-env.d.ts</span>
<span class="hljs-attr">*.lock</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>3、我们配置的<code>prettier</code>那么我们就要对<code>eslint</code>和<code>prettier</code>兼容，<a href="https://www.npmjs.com/package/eslint-plugin-prettier" target="_blank" rel="nofollow noopener noreferrer">参的地址</a></p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npm</span> <span class="hljs-string">install eslint-plugin-prettier -D</span>
<span class="hljs-attr">npm</span> <span class="hljs-string">install eslint-config-prettier -D</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、根据文档来配置</p>
</li>
<li>
<p>5、现在<code>react</code>都是使用<code>hooks</code>开发了，自然也要配置这个规则，<a href="https://www.npmjs.com/package/eslint-plugin-react-hooks" target="_blank" rel="nofollow noopener noreferrer">参考地址</a></p>
</li>
<li>
<p>6、运行项目，手动删除一个分号或者单引号改为双引号</p>
</li>
<li>
<p>7、付一份我自己的<code>.eslintrc.js</code>的配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'react-app'</span>,
    <span class="hljs-string">'eslint:recommended'</span>,
    <span class="hljs-string">'plugin:react/recommended'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>,
    <span class="hljs-string">'plugin:prettier/recommended'</span>,
    <span class="hljs-string">'plugin:react-hooks/recommended'</span>,
  ],
  <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaFeatures</span>: &#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'react'</span>, <span class="hljs-string">'@typescript-eslint'</span>, <span class="hljs-string">'prettier'</span>, <span class="hljs-string">'react-hooks'</span>],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'prettier/prettier'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-string">'arrow-body-style'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'prefer-arrow-callback'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'react-hooks/rules-of-hooks'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-string">'react-hooks/exhaustive-deps'</span>: <span class="hljs-string">'warn'</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-4">五、配置样式格式化</h2>
<ul>
<li>
<p>1、安装依赖包</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">npm</span> <span class="hljs-string">install --save-dev stylelint stylelint-config-standard</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2、项目的根目录下创建文件<code>.stylelintrc</code></p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">&#123;</span>
  <span class="hljs-meta">"extends"</span>: <span class="hljs-string">["stylelint-config-standard"],</span>
  <span class="hljs-meta">"rules"</span>: <span class="hljs-string">&#123;&#125;</span>
<span class="hljs-attr">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>3、在<code>package.json</code>中配置<code>git</code>钩子来格式化样式</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  ...
  <span class="hljs-attr">"lint-staged"</span>: &#123;
    <span class="hljs-attr">"*.&#123;js,ts,tsx&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>,
      <span class="hljs-string">"git add"</span>
    ],
    <span class="hljs-comment">// 针对css或者scss的样式格式化，如果你用less就继续加上</span>
    <span class="hljs-attr">"*.&#123;css,scss&#125;"</span>: [
      <span class="hljs-string">"stylelint src/**/*.css --fix"</span>,
      <span class="hljs-string">"stylelint src/**/*.scss --fix"</span>
    ]
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、在<code>index.css</code>中随便写点样式，然后使用<code>git</code>提交代码查看样式否格式化</p>
</li>
<li>
<p>5、使用<code>git</code>提交代码的时候会比较慢，似乎还在拉取什么包，这时候建议删除<code>node_modules</code>然后重新安装</p>
</li>
</ul>
<h2 data-id="heading-5">六、编辑器规范</h2>
<ul>
<li>
<p>1、在项目下创建一个<code>.editorconfig</code>文件</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-comment"># http://editorconfig.org</span>
<span class="hljs-attr">root</span> = <span class="hljs-string">true</span>

<span class="hljs-attr">[*]</span>
<span class="hljs-attr">indent_style</span> = <span class="hljs-string">space</span>
<span class="hljs-attr">indent_size</span> = <span class="hljs-string">2</span>
<span class="hljs-attr">end_of_line</span> = <span class="hljs-string">lf</span>
<span class="hljs-attr">charset</span> = <span class="hljs-string">utf-8</span>
<span class="hljs-attr">trim_trailing_whitespace</span> = <span class="hljs-string">true</span>
<span class="hljs-attr">insert_final_newline</span> = <span class="hljs-string">true</span>

<span class="hljs-attr">[*.md]</span>
<span class="hljs-attr">trim_trailing_whitespace</span> = <span class="hljs-string">false</span>

<span class="hljs-attr">[Makefile]</span>
<span class="hljs-attr">indent_style</span> = <span class="hljs-string">tab</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            