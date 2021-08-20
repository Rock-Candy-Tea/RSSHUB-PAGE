
---
title: '【代码校验】ESlint回顾 and  JS标准编码风格standard｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a12917f694f4cf9b5a0192aadc38c8e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:44:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a12917f694f4cf9b5a0192aadc38c8e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Eslint 是什么</h1>
<h2 data-id="heading-1">编码规范</h2>
<p>每个程序员都有自己的编码习惯，最常见的莫过于：</p>
<ul>
<li>有的人写代码一行代码结尾必须加分号 <code>;</code>，有的人觉得不加分号 <code>;</code> 更好看；</li>
<li>有的人写代码一行代码不会超过 80 个字符，认为这样看起来简洁明了，有的人喜欢把所有逻辑都写在一行代码上，觉得别人看不懂的代码很牛逼；</li>
<li>有的人使用变量必然会先定义 <code>var a = 10;</code>，而粗心的人写变量可能没有定义过就直接使用 <code>b = 10;</code>；</li>
</ul>
<h2 data-id="heading-2">Lint 的含义</h2>
<p>如果你写自己的项目怎么折腾都没关系，但是在公司中老板希望每个人写出的代码都要符合一个统一的规则，这样别人看源码就能够看得懂，因为源码是符合统一的编码规范制定的。</p>
<p>那么问题来了，总不能每个人写的代码老板都要一行行代码去检查吧，这是一件很蠢的事情。凡是重复性的工作，都应该被制作成工具来节约成本。这个工具应该做两件事情：</p>
<ul>
<li>提供编码规范；</li>
<li>提供自动检验代码的程序，并打印检验结果：告诉你哪一个文件哪一行代码不符合哪一条编码规范，方便你去修改代码。</li>
</ul>
<p>Lint 因此而诞生。</p>
<h2 data-id="heading-3">Eslint 的含义</h2>
<p>Lint 是检验代码格式工具的一个统称，具体的工具有 <code>Jslint</code> 、 <code>Eslint</code> 等等 ...........</p>
<h1 data-id="heading-4">二、使用 Eslint</h1>
<blockquote>
<p>确保你的电脑安装了 node 和 npm 环境</p>
</blockquote>
<h2 data-id="heading-5">创建项目</h2>
<p><code>npm init</code> 指令会在项目根目录下生成 <code>package.json</code> 文件。</p>
<p>**</p>
<pre><code class="copyable">$ d:
$ cd d:
$ mkdir test-eslint
$ cd test-eslint
$ npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">安装依赖包</h2>
<p><code>--save-dev</code> 会把 eslint 安装到 package.json 文件中的 devDependencies 属性中，意思是只是开发阶段用到这个包，上线时就不需要这个包了。</p>
<p>**</p>
<pre><code class="copyable">$ npm install eslint --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">设置 package.json 文件</h2>
<p>打开 package.json 文件，修改 script 属性如下：</p>
<p>**</p>
<pre><code class="copyable">"scripts": &#123;
    "test": "react-scripts test --env=jsdom",
    "lint": "eslint src",
    "lint:create": "eslint --init"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>script 属性的意思是脚本，使用方法是在 cmd 窗口中输入 <code>npm run 指令</code> 的形式，如：<code>npm run lint:create</code>；</li>
<li><code>"lint:create": "eslint --init"</code> 这个脚本是为了生成 .eslintrc.js 文件，在介绍 Lint 的时候说到 Lint 应该提供编码规范，规范写在哪里，就写在这个文件，所以我们需要创建它；</li>
<li><code>"lint": "eslint src"</code> 在介绍 Lint 的时候也说到 Lint 应该提供自动校验代码的程序，这个脚本是让 Lint 自动检验 src 目录下所有的 .js 文件。</li>
</ul>
<h2 data-id="heading-8">创建 .eslint.js 文件</h2>
<pre><code class="hljs language-js copyable" lang="js">

$ npm run lint:create

> <span class="hljs-number">20170811</span>@<span class="hljs-number">0.1</span><span class="hljs-number">.0</span> lint:create D:\code\test\<span class="hljs-number">20170811</span>
> eslint --init

? How would you like to configure ESLint? Answer questions about your style <span class="hljs-comment">// 以问答的形式创建配置文件</span>
? Are you using ECMAScript <span class="hljs-number">6</span> features? Yes      <span class="hljs-comment">// 是否校验 Es6 语法</span>
? Are you using ES6 modules? Yes                <span class="hljs-comment">// 是否校验 Es6 模块语法</span>
? Where will your code run? Browser             <span class="hljs-comment">// 代码运行环境，Browser 指浏览器</span>
? Do you use CommonJS? Yes                      <span class="hljs-comment">// 是否校验 CommonJs 语法</span>
? Do you use JSX? Yes                           <span class="hljs-comment">// 是否校验 JSX 语法</span>
? Do you use React? Yes                         <span class="hljs-comment">// 是否校验 React 语法</span>
? What style <span class="hljs-keyword">of</span> indentation <span class="hljs-keyword">do</span> you use? Tabs    <span class="hljs-comment">// 首行空白选择 Tab 键还是 Space</span>
? What quotes <span class="hljs-keyword">do</span> you use <span class="hljs-keyword">for</span> strings? Double    <span class="hljs-comment">// 字符串使用单引号 'string' 还是双引号 "string"</span>
? What line endings <span class="hljs-keyword">do</span> you use? Windows         <span class="hljs-comment">// 操作系统</span>
? Do you <span class="hljs-built_in">require</span> semicolons? Yes                <span class="hljs-comment">// 每行代码结尾是否校验加分号 ;</span>
? What format <span class="hljs-keyword">do</span> you want your config file to be <span class="hljs-keyword">in</span>? JavaScript     <span class="hljs-comment">// 以 .js 格式生成配置文件</span>
Installing eslint-plugin-react@latest   <span class="hljs-comment">// 因为要校验 Reac 语法，所以这里需要下载一个 React 语法规则的包</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">创建 index.js 文件</h2>
<p>在根目录下创建 src/index.js 文件，内容如下，接下来就使用 Eslint 来检验这个 .js 文件是否符合编码规范。</p>
<pre><code class="copyable">const lint = 'eslint'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的目录结构应该为：</p>
<pre><code class="copyable">- test-eslint
    + .eslintrc.js
    + package.json
    - src
        + index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">校验代码</h2>
<pre><code class="copyable">$ npm run lint

    1:7   error  'lint' is assigned a value but never used  no-unused-vars
    1:14  error  Strings must use doublequote               quotes
    1:22  error  Missing semicolon                          semi

    3 problems (3 errors, 0 warnings)
    2 errors, 0 warnings potentially fixable with the `--fix` option.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里报了三个错误，分别是：</p>
<ul>
<li>index.js 第1行第7个字符，报错编码规则为 <code>no-unused-vars</code>：变量 lint 只定义了，但是未使用；</li>
<li>index.js 第1行第14个字符，报错编码规则为 <code>quotes</code>：编码规范字符串只能使用双引号，这里却使用了单引号；</li>
<li>index.js 第1行第22个字符，报错编码规则为 <code>semi</code>：编码规范每行代码结尾必须加分号，这里没有加分号。</li>
</ul>
<p>当我们熟悉了编码规范之后，只需进行响应的修改就可以使代码形成统一的风格。刚开始如果对编码规范具体某一条规则不了解的话，可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Frules%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" ref="nofollow noopener noreferrer">eslint规则表</a> 查看用法。（不建议去背规则表，而是用到什么查什么，把它当成字典来用，不那么累）</p>
<h2 data-id="heading-11">设置 --fix 参数</h2>
<p>打开 package.json 文件，修改 script 属性如下：</p>
<p>**</p>
<pre><code class="copyable">"scripts": &#123;
    "test": "react-scripts test --env=jsdom",
    "lint": "eslint src --fix",
    "lint:create": "eslint --init"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：这里给 <code>"lint": "eslint src --fix",</code> 加上 <code>--fix</code> 参数，是 Eslint 提供的自动修复基础错误的功能。</p>
<p>此时运行 <code>npm run lint</code> 会看到少了两条报错信息，并不是说编码规范变了，而是 Eslint 自动修复了基础错误，打开 index.js 文件，可看到字符串自动变成了双引号，并且代码末尾也加上了分号。可惜的是 --fix 只能修复基础的不影响代码逻辑的错误，像 no-unused-vars 这种错误只能手动修改。</p>
<h2 data-id="heading-12">配置文件讲解</h2>
<p>按照上述操作，会生成默认 <code>.eslintrc.js</code> 配置文件，内容如下：</p>
<pre><code class="copyable">// .eslintrc.js 
module.exports = &#123;
    "env": &#123;
        "browser": true,
        "commonjs": true,
        "es6": true
    &#125;,
    "extends": "eslint:recommended",
    "parserOptions": &#123;
        "ecmaFeatures": &#123;
            "experimentalObjectRestSpread": true,
            "jsx": true
        &#125;,
        "sourceType": "module"
    &#125;,
    "plugins": [
        "react"
    ],
    "rules": &#123;
        "indent": [
            "error",
            "tab"
        ],
        "linebreak-style": [
            "error",
            "windows"
        ],
        "quotes": [
            "error",
            "double"
        ],
        "semi": [
            "error",
            "always"
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该文件导出一个对象，对象包含属性 <code>env</code>、<code>extends</code>、<code>parserOptions</code>、<code>plugins</code>、<code>rules</code> 五个属性，作为刚学习 Eslint 的新手，我们总是想要竭尽所能的详细了解每一个属性是什么，干嘛用的，以获取小小的安全感。</p>
<h2 data-id="heading-13">env、parserOptions、plugins</h2>
<p>这三个放在一起将是因为你只需要知道它们是干嘛的：我的程序里要用到 ES6 、React 、JSX 语法，这几个属性就是让 Eslint 能够检验到这些语法的。其余的你不需要知道更多的哪怕一丢丢的东东了。</p>
<p>作者在学习之初在这块浪费了很多时间，官方文档看了很多遍，大多不能理解什么意思，后来想它既然提供这么一个自动生成配置文件的工具，并且是命令行交互的方式，我只需要告诉它我要用 ES6 、React 、JSX 语法，它会自动进行相关配置满足我的要求即可。</p>
<h2 data-id="heading-14">extends</h2>
<p>前面一直说检验代码遵循编码规范，那到底是什么规范呢。</p>
<p>值为 "eslint:recommended" 的 extends 属性启用一系列核心规则，这些规则是经过前人验证的最佳实践（所谓最佳实践，就是大家伙都觉得应该遵循的编码规范），<strong>想知道最佳实践具体有哪些编码规范</strong>，可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Frules%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" ref="nofollow noopener noreferrer">eslint规则表</a> 中查看被标记为 √ 的规则项。</p>
<p>如果觉得官方提供的默认规则不好用，可以自定义规则配置文件，然后发布成 Npm 包，eslint-config-airbnb 就是别人自定义的编码规范，使用 npm 安装后，在我们自己的 .eslintrc.js 中进行配置 "extends": "airbnb"，eslint-config 这个前缀可以省略不写，这样我们就使用了 eslint-config-airbnb 中的规则，而不是官方的规则 "extends":"eslint:recommended" 了。关于如何创建自定义规则配置并共享可以参考： <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Fdeveloper-guide%252Fshareable-configs" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Fdeveloper-guide%2Fshareable-configs" ref="nofollow noopener noreferrer">如何自定义规则配置</a></p>
<p>关于 "airbnb" 编码规范说两句，在接触到大多数开源项目中，大多数的作者都会使用 "airbnb" 编码规范而不是 官方的 "extends": "eslint:recommended" 编码规范。</p>
<p>如果我们觉得 eslint-config-airbnb 规则配置中个别规则并不符合当前项目的要求，可以直接在 .eslintrc.js 配置 rules 属性，优先级高于共享规则 airbnb。</p>
<h2 data-id="heading-15">rules</h2>
<p>配置文件也生成了，我们怎么知道我们的系统会遵循什么规则呢？？</p>
<p>在前面的列子中，使用 <code>npm run lint</code> 校验出了三处错误，假如我们的项目中字符串就是要使用单引号而不是双引号，代码结尾就是要不加分号才好看，变量就是定义了可能不会使用，我们可以通过设置 rules 来定义我们自己的编码规范，即规则。</p>
<p>ESLint 附带有大量的规则，修改规则应遵循如下要求：</p>
<ul>
<li>"off" 或 0 - 关闭规则</li>
<li>"warn" 或 1 - 开启规则，使用警告级别的错误：warn (不会导致程序退出)</li>
<li>"error" 或 2 - 开启规则，使用错误级别的错误：error (当被触发的时候，程序会退出)</li>
</ul>
<p>有的规则没有属性，只需控制是开启还是关闭，像这样："eqeqeq": "off"，有的规则有自己的属性，使用起来像这样："quotes": ["error", "double"]，具体有没有自带属性，可查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Frules%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" ref="nofollow noopener noreferrer">eslint规则表</a>。</p>
<p>修改 .eslintrc.js 文件中的 rules 属性：</p>
<pre><code class="copyable">"rules": &#123;
    "indent": [
        "error",
        "tab"
    ],
    "linebreak-style": [
        "error",
        "windows"
    ],
    "quotes": [
        "error",
        "single"        // 改成字符串必须由单引号括起来而不是双引号，'string'不报错，"string"报错
    ],
    "semi": [
        "error",
        "never"         // 改成代码结尾不再加分号，加了分号报错，不加分号不报错
    ],
    "no-unused-vars": 0 // 0 相当于 off，表示关闭规则，相当于不再校验这条规则：变量定义了必须使用
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再使用 <code>npm run lint</code> 进行代码校验，没有报错就说明校验通过，代码符合统一编码规范。</p>
<pre><code class="copyable">D:\code\test\20170811>npm run lint

> 20170811@0.1.0 lint D:\code\test\20170811
> eslint src


D:\code\test\20170811>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">可能存在的疑问</h2>
<p>刚接触 ESlint ，并不清楚有哪些规则怎么办，要去 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Frules%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" ref="nofollow noopener noreferrer">eslint规则表</a> 一条条记忆吗？答案是 no。</p>
<p>个人认为 ESlint 的配置文件并不是一次性完成的，而是在项目过程中慢慢完善的。你可以放心大胆的先进行编码，然后使用 <code>npm run lint</code> 校验代码的编码规范，如果这时候报错，可以在报错信息中知道是哪一条编码规范报错了，你可能并不认识它们，此时去 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttp%253A%252F%252Feslint.cn%252Fdocs%252Frules%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" ref="nofollow noopener noreferrer">eslint规则表</a> 查询相应规则的使用方法，如：<code>no-unused-vars</code>，从而进一步确定项目中是否需要这条编码规范，如果需要，进行局部调整即可。</p>
<pre><code class="copyable">$ npm run lint

    1:7   error  'lint' is assigned a value but never used  no-unused-vars
    1:14  error  Strings must use doublequote               quotes
    1:22  error  Missing semicolon                          semi

    3 problems (3 errors, 0 warnings)
    2 errors, 0 warnings potentially fixable with the `--fix` option.
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">常用的几个规则</h2>
<pre><code class="copyable">"quotes": [1, "single"],            # 单引号
"quote-props":[2, "as-needed"],     # 双引号自动变单引号
"semi": [2, "never"],               # 一行结尾不要写分号
"comma-dangle": [1,"always-multiline"]  # 对象或数组多行写法时，最后一个值加逗号
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">三、使用场景</h1>
<h3 data-id="heading-19">1. vscode的ESLint插件，能帮助我们自动整理代码格式</h3>
<blockquote>
<p>VScode中保存时使用ESlint进行代码检查</p>
</blockquote>
<h4 data-id="heading-20">1.1 启用ESLint</h4>
<blockquote>
<p>ESLint插件安装 与 插件的扩展设置, 选择vs code左下角的“设置”， 打开 VSCode 配置文件,添加如下配置</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a12917f694f4cf9b5a0192aadc38c8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-21">settings.json中添加如下配置</h5>
<blockquote>
<p><strong>eslint.autoFixOnSave</strong> 用来进行保存时自动格式化，但是默认只支持js 文件。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39d3dc13f7044f368730341ad8e8cd4b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这样每次保存的时候就可以根据根目录下 .eslintrc.js 你配置的ESLint规则来检查和做一些简单的fix</p>
</blockquote>
<h3 data-id="heading-22">2. react、vue项目中安装eslint包，配置在.exlintrc.js中引入npm包中公司规定的eslint规则或者直接规定自已的规则，来覆盖node-modules中引入的规则。</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02feba5e1a0c42ef9d2d78b79d885d3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-23">四、参考</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstandard%2Fstandard" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/standard/standard" ref="nofollow noopener noreferrer">github.com/standard/st…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/" ref="nofollow noopener noreferrer">eslint.org/</a></li>
</ul>
<h1 data-id="heading-24">五、总结一</h1>
<h3 data-id="heading-25">1. 【语法规则】 一般包括：</h3>
<ul>
<li>两个字符缩进</li>
<li>使用单引号</li>
<li>语句后不可以写分号</li>
<li>等等</li>
</ul>
<h3 data-id="heading-26">2. Lint 是检验代码格式工具的一个统称</h3>
<ul>
<li>具体的工具有 <code>Jslint</code> 、 <code>Eslint</code> 等</li>
</ul>
<h3 data-id="heading-27">3. VSCode的ESLint插件，能帮助我们自动整理代码格式</h3>
<ul>
<li>直接安装eslint插件即可，每次保存，vscode就能标红不符合ESLint规则的地方，同时还会做一些简单的自我修正。</li>
</ul>
<h3 data-id="heading-28">4. ESLint 是一个开源的JavaScript验证工具，相比<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.oschina.net%2Fp%2Fjslint" target="_blank" rel="nofollow noopener noreferrer" title="http://www.oschina.net/p/jslint" ref="nofollow noopener noreferrer">JSLint</a>，ESLint具有可配置性</h3>
<p>其他跟 JSLint 的不同之处：</p>
<ul>
<li>ESLint 使用 Esprima 来进行 javascript 解析</li>
<li>ESLint 使用 AST 来修改代码模式</li>
<li>ESLint 是完全插件化的，每个规则都是一个插件，用户可以在运行时增加更多的插件</li>
</ul>
<h3 data-id="heading-29">5. JavaScript 校验 对比</h3>
<blockquote>
<p>JavaScript 校验：JSLint、JSHint、JSCS、ESLint</p>
</blockquote>
<ul>
<li>
<p>JSLint，古老，不可配置，不可扩展，不可禁用许多特性的校验</p>
</li>
<li>
<p>JSHint，可配置的JSLint版本</p>
</li>
<li>
<p>JSCS，代码样式检查，只捕获与代码格式化相关的问题，而不是潜在的bug或错误。已经与 ESLint 合并。</p>
</li>
<li>
<p>ESLint，易于扩展，可自定义规则，可以插件形式安装更多的规则。</p>
</li>
</ul>
<blockquote>
<p>一个 linting 工具是解决问题的一个很好的步骤，但是它基于一定的规则发现错误，具有一定的局限性。</p>
</blockquote>
<blockquote>
<p>要采用更安全的bug自动收集，建议使用单元测试(unit tests)，代码评审(code reviews)</p>
</blockquote>
<h1 data-id="heading-30">六、【最佳配置】 JavaScript 的推荐编码规范</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8af853b9e8ed4fc980f43c048ab5436c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
业界有许多 JavaScript 的推荐编码规范，较为出名的就是下面两个：</p>
<ol>
<li>airbnb style</li>
<li>javascript standard</li>
</ol>
<p>同时这里也推荐 AlloyTeam 的 eslint-config-alloy。</p>
<p>但是代码规范这个东西，最好是团队成员之间一起来制定，确保大家都能够接受，如果实在是有人有异议，就只能少数服从多数了。虽然这节的标题叫最佳配置，但是软件行业并有没有什么方案是最佳方案，即使 javascript standard 也不是 javascript 标准的编码规范，它仅仅只是叫这个名字而已，只有适合的才是最好的。</p>
<p>安利一下，将 ESLint 和 Prettier 结合使用，不仅统一编码规范，也能统一代码风格。</p>
<h1 data-id="heading-31">七、 我为什么使用 JavaScript Standard Style(JavaScript 标准编码风格)</h1>
<p>请参考
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu012207345%2Farticle%2Fdetails%2F78407787" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u012207345/article/details/78407787" ref="nofollow noopener noreferrer">blog.csdn.net/u012207345/…</a></p>
<p>安利一下
良好的程序层次结构</p>
<p>程序员应该重视：</p>
<ul>
<li>正确性</li>
<li>可读性</li>
<li>幸福感</li>
<li>高效率</li>
</ul>
<blockquote>
<p>事实证明，采用 JavaScript Standard Style(JavaScript 标准编码风格)，对以上每一条都有好处。</p>
</blockquote>
<h1 data-id="heading-32">八、【ESlint原理】</h1>
<blockquote>
<p>ast 抽象语法树</p>
</blockquote>
<blockquote>
<p>JavaScript 的 linter 工具发展历史其实也不算短，ESLint 之所以能够后来者居上，主要原因还是 JSLint 和 JSHint 采用自顶向下的方式来解析代码，并且早期 JavaScript 语法万年不更新，能这种方式够以较快的速度来解析代码，找到可能存在的语法错误和不规范的代码。但是 ES6 发布之后，JavaScript 语法发生了很多的改动，比如：箭头函数、模板字符串、扩展运算符……，这些语法的发布，导致 JSLint 和 JSHint 如果不更新解析器就没法检测 ES6 的代码。而 ESLint 另辟蹊径，采用 AST 的方式对代码进行静态分析，并保留了强大的可扩展性和灵活的配置能力。这也告诉我们，在日常的编码过程中，一定要考虑到后续的扩展能力。</p>
</blockquote>
<blockquote>
<p>正是因为这个强大扩展能力，让业界的很多 JavaScript 编码规范能够在各个团队进行快速的落地，并且团队自己定制的代码规范也可以对外共享。</p>
</blockquote>
<blockquote>
<p>最后，希望你通过上面的学习已经理解了 ESLint 带来的好处，同时掌握了 ESLint 的用法，并可以为现有的项目引入 ESLint 改善项目的代码质量。</p>
</blockquote>
<h1 data-id="heading-33">九、 使用/编写 ESLint插件</h1>
<p>虽然官方提供了上百种的规则可供选择，但是这还不够，因为官方的规则只能检查标准的 JavaScript 语法，如果你写的是 JSX 或者 Vue 单文件组件，ESLint 的规则就开始束手无策了。</p>
<p>这个时候就需要安装 ESLint 的插件，来定制一些特定的规则进行检查。ESLint 的插件与扩展一样有固定的命名格式，以 eslint-plugin- 开头，使用的时候也可以省略这个头。</p>
<pre><code class="copyable">npm install --save-dev eslint-plugin-vue eslint-plugin-react
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">&#123;
  "plugins": [
    "react", // eslint-plugin-react
    "vue",   // eslint-plugin-vue  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者是在扩展中引入插件，前面有提到 plugin: 开头的是扩展是进行插件的加载。</p>
<pre><code class="copyable">&#123;
  "extends": [
    "plugin:react/recommended",  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-34">十、总结二</h1>
<h5 data-id="heading-35">1. Vue/react项目 vscode 安装eslint插件的方法(代码自动修复)</h5>
<h5 data-id="heading-36">2. npm run script对象中 执行npm lint命令时 加上自动修复 -fix参数</h5>
<h5 data-id="heading-37">3. 【eslint两处安装有何区别】Vue/react项目中安装了eslint，vscode安装eslint插件？</h5>
<blockquote>
<p>webpack 里面的是在编译期给你报错用的，报错了会停止编译，直到你修复。
vscode中的是提示给你看的，方便你直接看到错误。顺便会帮你修复简单的错误。</p>
</blockquote>
<blockquote>
<p>准确的说应该是webpack中的eslint是加载器，全名是eslint-loader。是为了处理某些文件的加载器而已,因此<code>它本质是loader</code>。
vscode是一个编辑器，vscode中的eslint<code>本质上是一个vscode插件</code>，
他会调用eslint，然后将eslint的报错反馈给vscode，仅此而已。
webpack和webpack-cli有什么区别？ 你可以对比理解一下</p>
</blockquote></div>  
</div>
            