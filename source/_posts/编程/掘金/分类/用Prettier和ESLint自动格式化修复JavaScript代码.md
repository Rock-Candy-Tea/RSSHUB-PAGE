
---
title: '用Prettier和ESLint自动格式化修复JavaScript代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab508a30d8944c15915a48f83c9ff498~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 19:45:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab508a30d8944c15915a48f83c9ff498~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>打出JavaScript代码可以帮助你及早发现错误，使你的代码更加清晰，并提高代码质量。然而，当你同时使用格式化器（用于pretty-printing）和linter时，可能会有一些问题。衬托者可以覆盖来自格式化器的样式变化。它们会朝不同的方向发展。</p>
<p>为了顺利的使用，需要让它们站在同一起跑线上。本文将讨论如何将最流行的格式化器<a href="https://prettier.io/" target="_blank" rel="nofollow noopener noreferrer">Prettier</a>与最流行的linter<a href="https://eslint.org/" target="_blank" rel="nofollow noopener noreferrer">ESLint</a>一起使用。本文将阐述如何设置它们，并在命令行和<a href="https://code.visualstudio.com/" target="_blank" rel="nofollow noopener noreferrer">Visual Studio Code (VS Code)</a>中一起使用它们，以自动修正和格式化你的代码。</p>
<p>目前已经有很多方法解决这个问题，但有些是黑客的的解决方案。我将讨论其中一些的优点和缺点。可以自行决定选择用哪种方式。</p>
<p>首先，让我们广泛地了解一下提示规则，这样我们就可以理解提示器和格式化器之间的分界线是什么。</p>
<h2 data-id="heading-0">润色规则</h2>
<p>有两大类提示规则。</p>
<ol>
<li><strong>格式化规则</strong>。这些规则影响代码的风格。这些规则不涉及bug。例如，ESLint中的<a href="https://eslint.org/docs/rules/no-mixed-spaces-and-tabs" target="_blank" rel="nofollow noopener noreferrer">'no-mixed-spaces-and-tabs'</a>规则确保缩进时只使用制表符或空格。Prettier有一个<a href="https://prettier.io/docs/en/options.html#tabs" target="_blank" rel="nofollow noopener noreferrer">'tabs'选项</a>用于同样的事情。</li>
<li><strong>代码质量规则</strong>。这些规则可以提高代码质量，并有可能防止或捕获错误。例如，ESLint中的<a href="https://eslint.org/docs/rules/no-implicit-globals" target="_blank" rel="nofollow noopener noreferrer">'no-implicit-globals'</a>规则不允许全局范围变量。从其他脚本创建的全局变量可能会发生名称冲突。这通常会导致运行时错误或意外行为。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab508a30d8944c15915a48f83c9ff498~tplv-k3u1fbpfcp-zoom-1.image" alt="Prettier的格式化规则和ESLint的代码质量规则在linting规则维恩图上重叠" loading="lazy" referrerpolicy="no-referrer"></p>
<p>问题是，Prettier和ESLint的规则重叠了，但我们希望它们不重叠。</p>
<p>一般来说，我们希望<a href="https://prettier.io/" target="_blank" rel="nofollow noopener noreferrer">Prettier</a>能处理第一类，而ESLint能处理第二类。有一些规则可能很难被归类为其中之一。我们不需要纠结于它们属于哪个类别。我们的兴趣在于确保Prettier或ESLint执行一个特定的动作，并且不会相互碰撞。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6811f80283da4d52859a3a7461b4dc45~tplv-k3u1fbpfcp-zoom-1.image" alt="Prettier的格式化规则和ESLint的代码质量规则之间的分离" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于运行它们的顺序，最好是在ESLint之前运行Prettier。Prettier通过以一致的方式重新打印整个程序来格式化文件，以消除任何格式化错误的可能性。因此，如果你想让ESLint加入格式化的行动，你应该在Prettier之后运行它，以防止更改被覆盖掉。</p>
<p>如果你对ESLint和Prettier不熟悉，我会在下一节介绍如何对它们进行初始配置。如果你熟悉，你可以跳到【方法】部分。</p>
<h2 data-id="heading-1">ESLint和Prettier的初始配置</h2>
<p>ESLint和Prettier都可以从<a href="https://juejin.cn/post/undefined">npm</a>和<a href="https://juejin.cn/post/undefined">Yarn</a>下载。对于每一个项目，你都要创建一个<code>package.json</code>，并把它们作为<code>devDependencies</code>加入。</p>
<pre><code class="copyable">npm install --save-dev eslint
npm install --save-dev --save-exact prettier

<span class="copy-code-btn">复制代码</span></code></pre>
<p>ESLint开始时是一张白纸。在你创建一个包含一些规则的配置之前，它不会做任何事情。把你的配置文件（<code>.eslintrc.&#123;js,yml,json&#125;</code>）放到你的项目目录下，你就可以进行lint了。你可以设置一个全局配置，但我不鼓励使用ESLint，我仍然使用一个全局配置。</p>
<p>有了配置，你可以从命令行中运行ESLint。你可以阅读ESLint的<a href="https://eslint.org/docs/user-guide/getting-started" target="_blank" rel="nofollow noopener noreferrer">Getting Started Guide</a>了解更多细节。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f060b22b28464fcab1da89f4e31e6986~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210609114941.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另一方面，Prettier有一个默认配置。它可以在不创建你自己的配置文件的情况下运行，所以你可以直接开始使用它。建议在大项目上使用特定版本的Prettier，否则更新可能会导致许多文件的改变，并给你的git提交增加噪音。你可能应该使用一个<code>[.prettierignore](https://prettier.io/docs/en/ignore.html)</code>文件来忽略那些不应该被格式化的东西也。你可以阅读Prettier的<a href="https://prettier.io/docs/en/install.html" target="_blank" rel="nofollow noopener noreferrer">安装指南</a>了解更多信息。</p>
<p><img src="https://blog.logrocket.com/wp-content/uploads/2021/05/prettier-cli.png" alt="插入Prettier代码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个典型的<code>package.json</code>会像我下面的样子。我把<code>src</code>和<code>test</code>文件夹中的文件作为我的npm脚本的目标。如果可能的话，我喜欢跳过<code>.eslintignore</code>和<code>.prettierignore</code>文件--更简单的才是最好的！</p>
<pre><code class="copyable">&#123;
  "name": "basic-project",
  "版本": "1.0.0",
  "main": "index.js",
  "scripts": &#123;
    "lint": "npx eslint src test",
    "lint:fix": "npm run lint -- -- -- fix",
    "prettier": "npx prettier src test --check",
    "prettier:fix": "npm run prettier -- -- write"。
  &#125;,
  "author": "Rob o'leary",
  "license": "ISC"。
  "devDependencies": &#123;
    "eslint": "^7.25.0",
    "prettier": "^2.2.1"
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有主要的代码编辑器都有ESLint和Prettier的扩展。对于VS Code，官方的扩展是<a href="https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode" target="_blank" rel="nofollow noopener noreferrer">Prettier - Code formatter</a>和<a href="https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint" target="_blank" rel="nofollow noopener noreferrer">ESLint</a>。</p>
<p><img src="https://blog.logrocket.com/wp-content/uploads/2021/05/vscode-eslint.png" alt="在VS Code中插入ESLint" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">为你的代码提供提示和pret-print的各种方法</h2>
<p>我推荐下面的第一种方法。</p>
<h3 data-id="heading-3">1. 删除冲突的规则并连续运行</h3>
<p>在ESLint中，通过使用以下配置，很容易关闭与Prettier冲突的规则。</p>
<ul>
<li><a href="https://github.com/prettier/eslint-config-prettier" target="_blank" rel="nofollow noopener noreferrer">eslint-config-prettier</a> for JavaScript</li>
<li><a href="https://github.com/alexjoverm/tslint-config-prettier" target="_blank" rel="nofollow noopener noreferrer">tslint-config-prettier</a> 如果你使用TypeScript的话</li>
</ul>
<p>首先，安装该配置。这只是针对JavaScript的。</p>
<pre><code class="copyable">$ npm install --save-dev eslint-config-prettier

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在你的本地<code>.stylelintrc.*</code>ESLint配置文件中，将该配置名称追加到<code>[extends](https://stylelint.io/user-guide/configuration/#extends)</code>数组中。确保把更漂亮的配置放在最后，这样它将覆盖其他配置的设置。</p>
<p>例如 <code>.eslintrc.json</code>:</p>
<pre><code class="copyable">&#123;
  // ...
  延伸。[
    // ...
    'eslint:recommended',
    "prettier" // 确保这是最后一个
  ],
  // ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，你可以自由地将Prettier和ESLint一起运行而没有任何副作用。</p>
<p>你可以像在命令行中那样，通过将它们定义为npm脚本，一个接一个地运行prettier和ESLint。以下是在<code>package.json</code>中的样子。</p>
<pre><code class="copyable">&#123;
   "name": "no-worries-setup",   
   "版本": "1.0.0",
   "脚本": &#123;
    "lint": "npx eslint src test",
    "lint:fix": "npm run lint -- -- -- fix",
    "prettier": "npx prettier src test --check",
    "prettier:fix": "npm run prettier -- -- write",
    "format": "npm run prettier:fix && npm run lint:fix"。
  &#125;
  // ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">在VS代码中的配置</h4>
<ol>
<li>
<p>安装扩展程序。<a href="https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint" target="_blank" rel="nofollow noopener noreferrer">ESLint</a>, <a href="https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode" target="_blank" rel="nofollow noopener noreferrer">Prettier</a>, 和 <a href="https://marketplace.visualstudio.com/items?itemName=rohit-gohri.format-code-action&ssr=false#review-details" target="_blank" rel="nofollow noopener noreferrer">Format Code Action</a>.</p>
</li>
<li>
<p>更新你的用户设置（<code>settings.json</code>），如下。</p>
<pre><code class="copyable">&#123;
  //...
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "eslint.probe": [
      "javascript",
      "javascriptreact",
      "vue"
  ],
  "editor.formatOnSave": false,
  // 运行Prettier，然后运行ESLint
  "editor.codeActionsOnSave": [
    "source.formatDocument",
    "source.fixAll.eslint"
  ],
  "vetur.validation.template": false
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>首先，你需要禁用保存时的编辑器格式（<code>editor.formatOnSave</code>）。我们希望通过代码动作来处理一切。</p>
<p>在<a href="https://code.visualstudio.com/updates/v1_44#_explicit-ordering-for-code-actions-on-save&quot" target="_blank" rel="nofollow noopener noreferrer">March 2020 (v1.44)</a>中，<code>editor.codeActionsOnSave</code>属性被更新为接受一个代码动作的数组，这允许有序的代码动作。如果我们安装了<a href="https://marketplace.visualstudio.com/items?itemName=rohit-gohri.format-code-action&ssr=false#review-details" target="_blank" rel="nofollow noopener noreferrer">Format Code Action</a>扩展，我们可以使格式化作为一个代码动作来使用。所以我们可以以我们喜欢的任何顺序运行Prettier和ESLint作为代码动作。</p>
<p>在这个例子中，我们先用<code>source.formatDocument</code>动作运行Prettier（它使用默认格式），然后用<code>source.fixAll.eslint</code>动作运行<code>eslint --fix</code>。</p>
<p><code>slint.probe</code>属性是用来锁定ESLint应该验证的语言。如果你想看到弹出信息，你可以使用<code>eslint.validate</code>来代替。</p>
<p>如果你使用Vetur扩展，确保它不做自己的验证。有一个设置<code>vetur.validation.template</code>，你不应该启用它。</p>
<h3 data-id="heading-5">2. 以编程方式运行Prettier和ESLint</h3>
<p>下面的应用程序提供了一个统一的方式来运行<code>prettier</code>，然后立即对文件进行<code>eslint --fix</code>。</p>
<ul>
<li><a href="https://github.com/prettier/prettier-eslint" target="_blank" rel="nofollow noopener noreferrer">prettier-eslint</a> 用于JavaScript</li>
<li><a href="https://github.com/azz/prettier-tslint" target="_blank" rel="nofollow noopener noreferrer">prettier-tslint</a> for TypeScript</li>
</ul>
<p>首先，安装该软件包。这只是针对JavaScript的。</p>
<pre><code class="copyable">$ npm install --save-dev prettier-eslint

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，你需要编写你自己的实现，来针对你的文件并运行格式化。</p>
<p>下面是一个格式化字符串的基本例子。</p>
<pre><code class="copyable">const format = require("prettier-eslint")。

// 注意，原文中没有分号
const sourceCode = "const &#123;foo&#125; = bar"。

const options = &#123;
  text: sourceCode,
  eslintConfig: &#123;
    parserOptions: &#123;
      ecmaVersion: 7,
    &#125;,
    规则。&#123;
      semi: ["error", "never"],
    &#125;,
  &#125;,
  prettierOptions: &#123;
    bracketSpacing: true,
  &#125;,
  fallbackPrettierOptions: &#123;
    singleQuote: false,
  &#125;,
&#125;;

const formatted = format(options);

// 注意格式化的文本中没有分号
formatted; // const &#123; foo &#125; = bar

<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，这个方法需要更多的工作来锁定文件，读取内容，并写入输出。</p>
<h4 data-id="heading-6">在VS代码中的配置</h4>
<p>你可以安装和使用<a href="https://marketplace.visualstudio.com/items?itemName=rvest.vs-code-prettier-eslint" target="_blank" rel="nofollow noopener noreferrer">Prettier ESLint</a>扩展，阅读README中的说明。</p>
<h3 data-id="heading-7">3. 运行Prettier，就像它是一个ESLint规则一样</h3>
<p>通常不建议这样做，因为</p>
<ol>
<li>你会被ESLint报告为格式化问题。你想让Prettier为你自动修复的东西划上红线吗？</li>
<li>它比直接运行Prettier要慢一些。</li>
<li>你有了另一个可以引入错误的层面。</li>
</ol>
<p>你可以使用ESLint插件，让你把Prettier当做一个linter规则来运行。</p>
<ul>
<li><a href="https://github.com/prettier/eslint-plugin-prettier" target="_blank" rel="nofollow noopener noreferrer">eslint-plugin-prettier</a> 用于JavaScript</li>
<li><a href="https://github.com/ikatyang/tslint-plugin-prettier" target="_blank" rel="nofollow noopener noreferrer">tslint-plugin-prettier</a> 用于TypeScript</li>
</ul>
<p>首先，安装该插件。这只是针对JavaScript的。</p>
<pre><code class="copyable">$ npm install --save-dev eslint-plugin-prettier

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在你的".stylelintrc.*"文件中的<a href="https://stylelint.io/user-guide/configuration/#extends" target="_blank" rel="nofollow noopener noreferrer"><code>plugins</code></a>数组中追加该插件。</p>
<p>例子 <strong>.eslintrc.json</strong>:****</p>
<pre><code class="copyable">&#123;
  "plugins": ["prettier"]。
  "规则": &#123;
    "prettier/prettier": "错误"
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>韦斯-博斯几年前推荐过这种<a href="https://juejin.cn/post/undefined">方法</a>，在当时是一个合理的选择，但现在有了更多的选择。</p>
<h4 data-id="heading-8">在VS代码中配置</h4>
<ol>
<li>
<p>安装扩展程序。<a href="https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint" target="_blank" rel="nofollow noopener noreferrer">ESLint</a>和<a href="https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode" target="_blank" rel="nofollow noopener noreferrer">Prettier</a>。</p>
</li>
<li>
<p>更新你的用户设置（<code>settings.json</code>），如下。</p>
<pre><code class="copyable">"eslint.alwaysShowStatus": true,
"editor.formatOnSave": true,
//对JS和JJSX关闭，我们将通过eslint来做这件事
"[javascript, javascriptreact]": &#123;
  "editor.formatOnSave": false
&#125;,
//告诉ESLint插件在保存时运行
"editor.codeActionsOnSave": &#123;
  "source.fixAll": true
&#125;,
// 可选但重要的是：如果你为其他语言（如CSS和HTML）启用了prettier扩展，请关闭JS的扩展，因为我们已经通过ESLint做了。
"prettier.disableLanguages": ["javascript", "javascriptreact"],

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-9">结论</h2>
<p>Prettier和ESLint可以非常有效地一起使用。它需要一些配置，但在读完这篇文章后，这应该是很简单的！这样的设置很好，可以把一些任务从你的手上拿开，重新获得一些头脑空间。它可以帮助你提高你的代码质量，让你的代码库更有可读性，而无需人工干预。</p>
<p>原文链接；<a href="https://blog.logrocket.com/automate-formatting-and-fixing-javascript-code-with-prettier-and-eslint/" target="_blank" rel="nofollow noopener noreferrer">blog.logrocket.com/automate-fo…</a></p></div>  
</div>
            