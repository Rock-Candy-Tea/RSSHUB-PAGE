
---
title: '一步一步，统一项目中的编码规范（vue, vscode, vetur, prettier, eslint）'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://user-gold-cdn.xitu.io/2019/4/24/16a4d7d10616b385?imageslim'
author: 掘金
comments: false
date: Wed, 24 Apr 2019 03:09:42 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2019/4/24/16a4d7d10616b385?imageslim'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>团队开发中，多人开发同一个项目，由于个人编码习惯不同，一个项目中最终的代码风格可能差别很大，所以需要通过工具进行约束来保证代码风格的统一。同时也希望通过工具尽可能的减少低级错误出现，并且能帮助修正，所以有了各种各样的 lint 和 formatter。</p>
<p>本篇的目标是使用 vscode 编辑器，使用 prettier 插件，结合使用 eslint 对代码进行校验和修正，并使用 eslint-config-airbnb-base 规则来实现代码风格的统一。</p>
<p>一般情况下，我们小公司、小 team 可能没有能力和精力来制订一套详尽规则，那么采用大厂已经制订好的规则就是很自然的选择（同时也必要争论你的好还是我的好了，人家大厂都这么干了，我们就按人家来吧！:)）</p>
<h2 data-id="heading-0">名词解释</h2>
<ul>
<li>vscode</li>
</ul>
<blockquote>
<p>一个文本编辑器 <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2F" title="https://code.visualstudio.com/" ref="nofollow noopener noreferrer">code.visualstudio.com/</a></p>
</blockquote>
<ul>
<li>prettier</li>
</ul>
<blockquote>
<p>vscode 插件，官方的说明是：Opinionated Code Formatter</p>
</blockquote>
<ul>
<li>eslint</li>
</ul>
<blockquote>
<p>代码校验和修复工具，官方说明是：The pluggable linting utility for JavaScript and JSX</p>
</blockquote>
<ul>
<li>eslint-config-airbnb-base</li>
</ul>
<blockquote>
<p>一组预先定义好的 eslint 规则，官方说明是：This package provides Airbnb's base JS .eslintrc (without React plugins) as an extensible shared config.</p>
</blockquote>
<p>下面一步一步，通过 vscode 的格式化的使用，到和 prettier 的结合，eslint 使用， prettier 结合 eslint 对 js 和 vue 文件校验，完成对项目代码校验和 fix，力求能以最简洁的方式把问题说清楚。</p>
<h2 data-id="heading-1">vscode 开箱即用的 code formatter 功能</h2>
<p>vscode 提供开箱即用的代码样式化功能（没有 css 格式化功能），下面在当前文件夹下创建测试文件：<code>./src/demo.html</code>、<code>./src/fun.js</code>、<code>./src/style.css</code>，格式化代码的快捷键是(win)：alt + shift + f</p>
<p>HTML 格式化前：</p>
<pre><code lang="html" class="copyable"><span><!DOCTYPE html></span>
<span><<span>html</span> <span>lang</span>=<span>"en"</span>></span>
<span><<span>head</span>></span>
<span><<span>meta</span> <span>charset</span>=<span>"UTF-8"</span>></span>
<span><<span>meta</span> <span>name</span>=<span>"viewport"</span> <span>content</span>=<span>"width=device-width, initial-scale=1.0"</span>></span>
<span><<span>meta</span> <span>http-equiv</span>=<span>"X-UA-Compatible"</span> <span>content</span>=<span>"ie=edge"</span>></span>
<span><<span>title</span>></span>Demo page<span></<span>title</span>></span>
<span></<span>head</span>></span>
<span><<span>body</span>></span><span><<span>h1</span>></span>This is a test page<span></<span>h1</span>></span>
<span><<span>p</span>></span>Page content<span></<span>p</span>></span>
<span></<span>body</span>></span>
<span></<span>html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre><p>格式化后：</p>
<pre><code lang="html" class="copyable"><span><!DOCTYPE html></span>
<span><<span>html</span> <span>lang</span>=<span>"en"</span>></span>

<span><<span>head</span>></span>
    <span><<span>meta</span> <span>charset</span>=<span>"UTF-8"</span>></span>
    <span><<span>meta</span> <span>name</span>=<span>"viewport"</span> <span>content</span>=<span>"width=device-width, initial-scale=1.0"</span>></span>
    <span><<span>meta</span> <span>http-equiv</span>=<span>"X-UA-Compatible"</span> <span>content</span>=<span>"ie=edge"</span>></span>
    <span><<span>title</span>></span>Demo page<span></<span>title</span>></span>
<span></<span>head</span>></span>

<span><<span>body</span>></span>
    <span><<span>h1</span>></span>This is a test page<span></<span>h1</span>></span>
    <span><<span>p</span>></span>Page content<span></<span>p</span>></span>
<span></<span>body</span>></span>

<span></<span>html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre><p>JS 格式化前：</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>getUserInfo</span>(<span>name</span>) </span>&#123;<span>let</span> HelloStr = <span>"Hello, your name is: "</span>
<span>return</span> HelloStr + name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>格式化后：</p>
<pre><code lang="javascript" class="copyable"><span><span>function</span> <span>getUserInfo</span>(<span>name</span>) </span>&#123;
    <span>let</span> HelloStr = <span>"Hello, your name is: "</span>
    <span>return</span> HelloStr + name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>CSS:</p>
<p></p><figure><img alt="CSS 文件的格式化" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4d7d10616b385?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>可以看到，CSS 文件默认情况下是不能被格式化的，这个时间轮到 prettier 登场~</p>
<h2 data-id="heading-2">用 prettier 对代码进行格式化</h2>
<p>prettier 的官方解释是：</p>
<ul>
<li>An opinionated code formatter</li>
<li>Supports many languages</li>
<li>Integrates with most editors</li>
<li>Has few options</li>
</ul>
<p>它能和多种编辑器结合，对多种语言进行 format，所以 css 也不是话下。</p>
<p>由于 vscode 默认有格式化的功能，安装了 prettier 插件后，prettier 也有格式化的功能以会造成冲突（对于html, js），这里编辑器会提示你，可以进行配置。</p>
<p></p><figure><img alt="Prettier 格式化 html" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4e2b56f9e97ab?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>需要注意的是，vscode 和 prettier 会有很多默认配置，可以通过 <code>CTRL + ,</code> 快捷键进入配置界面进行管理，所有修改后的结果会保存在 <code>settings.json</code> 文件里。</p>
<p>刚刚由于 vscode 默认的格式化程序和 prettier 冲突，经过选择后形成配置文件并写入 <code>settings.json</code>，如下：</p>
<pre><code lang="json" class="copyable">&#123;
    <span>"[html]"</span>: &#123;
        <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
    &#125;,
    <span>"[javascript]"</span>: &#123;
        <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
    &#125;,
    <span>"[jsonc]"</span>: &#123;
        <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>上面是指针不同类型的文件，分别指定 formatter，当然你也可以一次性指定<strong>所有类型</strong>文件的 formatter，修改后的配置文件 <code>settings.json</code> 如下：</p>
<pre><code lang="json" class="copyable">&#123;
    <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>经过如上配置， <code>css</code> 及其他类型的文件，拥有了通过 prettier 进行格式化的能力。</p>
<h2 data-id="heading-3">用 eslint 对 javascript 代码进行校验</h2>
<p>经过如上配置，可以对代码进行格式化了，但是如果要想去代码风格进行校验和修复，就要用到 eslint 了，下面分两步将 eslint 功能集成了项目中：</p>
<ol>
<li>在项目内安装 eslint 及相关的包</li>
<li>给 vscode 安装 eslint 插件</li>
</ol>
<p>下面分别来说</p>
<h3 data-id="heading-4">在项目内安装 eslint 及相关的包</h3>
<p></p><figure><img alt="安装 eslint" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4e2b56fc91f2a?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>经过上面的操作，将 eslint 及相关的包安装到项目里了 <code>package.json</code>如下：</p>
<pre><code lang="json" class="copyable">&#123;
  ...
  "dependencies": &#123;
    "eslint-plugin-vue": "^5.2.2"
  &#125;,
  "devDependencies": &#123;
    "eslint": "^5.16.0"
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>项目目录下多了一个 eslint 的配置文件 <code>.eslintrc.js</code> :</p>
<pre><code lang="javascript" class="copyable"><span>module</span>.exports = &#123;
    <span>"env"</span>: &#123;
        <span>"browser"</span>: <span>true</span>,
        <span>"es6"</span>: <span>true</span>
    &#125;,
    <span>"extends"</span>: [
        <span>"eslint:recommended"</span>,
        <span>"plugin:vue/essential"</span>
    ],
    <span>"globals"</span>: &#123;
        <span>"Atomics"</span>: <span>"readonly"</span>,
        <span>"SharedArrayBuffer"</span>: <span>"readonly"</span>
    &#125;,
    <span>"parserOptions"</span>: &#123;
        <span>"ecmaVersion"</span>: <span>2018</span>,
        <span>"sourceType"</span>: <span>"module"</span>
    &#125;,
    <span>"plugins"</span>: [
        <span>"vue"</span>
    ],
    <span>"rules"</span>: &#123;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre><p>这个配置文件的内容，是通过 <code>npx eslint --init</code> 自动生成的，当然你也可以手动配置，所有的选项这里都有中文说明：<a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Feslint.cn%2Fdocs%2Fuser-guide%2Fconfiguring" title="http://eslint.cn/docs/user-guide/configuring" ref="nofollow noopener noreferrer">eslint.cn/docs/user-g…</a></p>
<p>接下来就可以手动执行校验了：</p>
<p></p><figure><img alt="eslint lint" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4e2b56fa87b6a?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>在执行的时候可能会有包未安装的提示</p>
<blockquote>
<p>Failed to load plugin vue: Cannot find module 'eslint-plugin-vue'</p>
</blockquote>
<p>手动安装一下就好了，从执行结果来看，funs.js 文件有一个错误提示，说明校验程序已经能正常跑进来了。</p>
<p>现在采用的规则是 <code>eslint:recommended</code> ，我们的目标是采用 'eslint-config-airbnb-base'，所以再安装相应的包：</p>
<pre><code lang="bash" class="copyable">npm i -D eslint-config-airbnb-base eslint-plugin-import
<span class="copy-code-btn">复制代码</span></code></pre><p>然后对 <code>.eslintrc.js</code> 进行配置：</p>
<pre><code lang="javascript" class="copyable"><span>module</span>.exports = &#123;
  <span>env</span>: &#123;
    <span>browser</span>: <span>true</span>,
    <span>es6</span>: <span>true</span>,
  &#125;,
  <span>extends</span>: <span>'airbnb-base'</span>,
  <span>globals</span>: &#123;
    <span>Atomics</span>: <span>'readonly'</span>,
    <span>SharedArrayBuffer</span>: <span>'readonly'</span>,
  &#125;,
  <span>parserOptions</span>: &#123;
    <span>ecmaVersion</span>: <span>2018</span>,
    <span>sourceType</span>: <span>'module'</span>,
  &#125;,
  <span>plugins</span>: [
    <span>'vue'</span>,
  ],
  <span>rules</span>: &#123;
    <span>'linebreak-style'</span>: [<span>"error"</span>, <span>"windows"</span>]
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre><p>再进行校验：</p>
<pre><code lang="bash" class="copyable">D:\works\secoo\<span>test</span>\code-formatter> npx eslint .\src\funs.js

D:\works\secoo\<span>test</span>\code-formatter\src\funs.js
  1:10  error  <span>'getUserInfo'</span> is defined but never used              no-unused-vars
  2:7   error  <span>'HelloStr'</span> is never reassigned. Use <span>'const'</span> instead  prefer-const
  3:7   error  <span>'age'</span> is assigned a value but never used             no-unused-vars
  3:7   error  <span>'age'</span> is never reassigned. Use <span>'const'</span> instead       prefer-const
  3:15  error  Missing semicolon                                    semi

✖ 5 problems (5 errors, 0 warnings)
  3 errors and 0 warnings potentially fixable with the `--fix` option.
<span class="copy-code-btn">复制代码</span></code></pre><p>可以看到明显比之前的错误要多，Aribnb 的规则相对较为严格，可以规避很多低级错误。</p>
<p>这里要重点说一下的是，我们在 <code>.eslintrc.js</code> 的 <code>rules</code> 里加了 <code>'linebreak-style': ["error", "windows"]</code>，是由于不同系统间对换行的处理不同导致的，加这个规则来处理这个问题。</p>
<h3 data-id="heading-5">给 vscode 安装 eslint 插件</h3>
<p>走到这里我们已经可以校验 js 文件了，通过校验也发现了很多问题，但在 vscode里并没有错误提示，这就用到了 <strong><code>vscode</code></strong> 的另一个插件 <code>eslint</code>，安装完插件以后，在 vscode 里可以看到错误提示了：</p>
<p></p><figure><img alt="eslint lint" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4e2b56fb1182b?imageView2/0/w/1280/h/960/ignore-error/1" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>走到这里，我们离成功已经很近啦！</p>
<h2 data-id="heading-6">让 pretter 根据 eslint 校验结果，对代码进行样式化</h2>
<p>到目前为上，已经可以对 js 文件进行校验，甚至可以对 js 文件按规则进行修复了：</p>
<pre><code lang="bash" class="copyable">D:\works\secoo\<span>test</span>\code-formatter> npx eslint --fix .\src\funs.js

D:\works\secoo\<span>test</span>\code-formatter\src\funs.js
  1:10  error  <span>'getUserInfo'</span> is defined but never used   no-unused-vars
  3:9   error  <span>'age'</span> is assigned a value but never used  no-unused-vars

✖ 2 problems (2 errors, 0 warnings)
<span class="copy-code-btn">复制代码</span></code></pre><p>但是如果你用 vscode（如前述，vscode 使用 prettier） 进行修复，发现并没有应用 Airbnb 的规则，这里需要手动配置一下：</p>
<ul>
<li><code>CTRL + ,</code> 打开配置界面</li>
<li>扩展 -> Prettier 里打到 Eslint Integration 并勾选
得到 vscode 的配置文件 <code>settings.json</code> 如下</li>
</ul>
<pre><code lang="json" class="copyable">&#123;
    <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>,
    <span>"prettier.eslintIntegration"</span>: <span>true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>这时再对 js 文件进行格式化，就能按照指定的规则执行了，具体操作如下：</p>
<p></p><figure><img alt="prettier format follow eslint" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4ee945b11b14b?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h2 data-id="heading-7">校验并且格式化 vue 代码</h2>
<p>这部分是最麻烦的，很多同学都在这里翻车......</p>
<p>首先，要想 <code>vscode</code> 认识 <code>vue</code> 文件，需要安装插件 <code>vetur</code>，基本上安装好此插件后就可以开心的撸 vue 代码了，vetur 的默认配置如下：</p>
<pre><code lang="json" class="copyable">&#123;
  <span>"vetur.format.defaultFormatter.html"</span>: <span>"prettyhtml"</span>,
  <span>"vetur.format.defaultFormatter.css"</span>: <span>"prettier"</span>,
  <span>"vetur.format.defaultFormatter.postcss"</span>: <span>"prettier"</span>,
  <span>"vetur.format.defaultFormatter.scss"</span>: <span>"prettier"</span>,
  <span>"vetur.format.defaultFormatter.less"</span>: <span>"prettier"</span>,
  <span>"vetur.format.defaultFormatter.stylus"</span>: <span>"stylus-supremacy"</span>,
  <span>"vetur.format.defaultFormatter.js"</span>: <span>"prettier"</span>,
  <span>"vetur.format.defaultFormatter.ts"</span>: <span>"prettier"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>以上是默认配置，看着很开以的以为可以按着如下方式对代码进行格式化：</p>
<pre><code lang="bash" class="copyable">发出格式化命令
    |
    | next
    |
vetur 收到命令 将格式化任务转交给 prettier
    |
    | next
    |
prettier 收到命令 将格式化任务转交给 eslint
    |
    | next
    |
eslint 收到命令，将代码格式化
<span class="copy-code-btn">复制代码</span></code></pre><p>看似美好的结局被现实打破，当我们对 vue 文件进行格式化的时候，发它参考的规则是 prettier 规则，而非 eslint 规则。</p>
<p>如果想按着上述规则对 vue 进行格式化需要做两个事：
<code>settings.json</code></p>
<ul>
<li>将 vetur 中 js 的 formatter 设置为 prettier-eslint</li>
</ul>
<pre><code lang="json" class="copyable">&#123;
  ...
  "vetur.format.defaultFormatter.js": "prettier-eslint"
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>安装 prettier-eslint 包</li>
</ul>
<pre><code lang="bash" class="copyable">npm i -D prettier-eslint
<span class="copy-code-btn">复制代码</span></code></pre><p>对于这个问题，prettier-eslint <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprettier%2Fprettier-eslint" title="https://github.com/prettier/prettier-eslint" ref="nofollow noopener noreferrer">官网</a>上说的很清楚：</p>
<blockquote>
<p>This formats your code via prettier, and then passes the result of that to eslint --fix. This way you can get the benefits of prettier's superior formatting capabilities, but also benefit from the configuration capabilities of eslint.</p>
</blockquote>
<p>但就是这么一个问题，我在网上看把无数的同学绕进去了，确实直线理解的话会有两个坑：</p>
<ol>
<li>prettier 不是已经按着 eslint 来格式化 js 了吗，vetur 指给 prettier 按说没问题啊！现实是需要传递给 <code>prettier-eslint</code></li>
<li>很多同学跨过了第一道坎，但不曾想 <code>prettier-eslint</code> 需要手动安装一个包啊！</li>
</ol>
<p>所以导致在最后一步走不下去了。</p>
<p>至此配置基本已经完成，效果如下：</p>
<p></p><figure><img alt="eslint-vue-fix" src="https://user-gold-cdn.xitu.io/2019/4/24/16a4f08c6f302185?imageslim" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<h2 data-id="heading-8">最后总结</h2>
<p>最后总结一下，总共需要做那些工作</p>
<ol>
<li>安装 vscode 插件 <code>eslint</code>、 <code>prettier</code>、 <code>vetur</code></li>
<li>配置 eslint 规则</li>
<li>配置 prettier ，使其按着 eslint 工作</li>
<li>配置 vetur</li>
</ol>
<p>最终的配置文件如下：
settings.json</p>
<pre><code lang="json" class="copyable">&#123;
  <span>"extensions.autoUpdate"</span>: <span>false</span>,
  <span>"eslint.validate"</span>: [<span>"javascript"</span>, <span>"javascriptreact"</span>, <span>"vue"</span>],
  <span>"prettier.eslintIntegration"</span>: <span>true</span>,
  <span>"vetur.format.defaultFormatterOptions"</span>: &#123;
    <span>"prettier"</span>: &#123;
      <span>"eslintIntegration"</span>: <span>true</span>
    &#125;
  &#125;,
  <span>"vetur.format.defaultFormatter.js"</span>: <span>"prettier-eslint"</span>,
  <span>"[javascript]"</span>: &#123;
    <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
  &#125;,
  <span>"[jsonc]"</span>: &#123;
    <span>"editor.defaultFormatter"</span>: <span>"esbenp.prettier-vscode"</span>
  &#125;,
  <span>"vetur.format.defaultFormatter.html"</span>: <span>"prettier"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre><p>.eslintrc.js</p>
<pre><code lang="javascript" class="copyable"><span>module</span>.exports = &#123;
  <span>env</span>: &#123;
    <span>browser</span>: <span>true</span>,
    <span>es6</span>: <span>true</span>
  &#125;,
  <span>extends</span>: [<span>'airbnb-base'</span>, <span>'plugin:vue/recommended'</span>],
  <span>globals</span>: &#123;
    <span>Atomics</span>: <span>'readonly'</span>,
    <span>SharedArrayBuffer</span>: <span>'readonly'</span>
  &#125;,
  <span>parserOptions</span>: &#123;
    <span>ecmaVersion</span>: <span>2018</span>,
    <span>sourceType</span>: <span>'module'</span>
  &#125;,
  <span>plugins</span>: [<span>'vue'</span>],
  <span>rules</span>: &#123;
    <span>'linebreak-style'</span>: [<span>'error'</span>, <span>'windows'</span>],
    <span>'comma-dangle'</span>: [<span>'error'</span>, <span>'never'</span>], <span>// 修正 eslint-plugin-vue 带来的问题</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre><p>源代码在 <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwfzong%2Fvue-vscode-format" title="https://github.com/wfzong/vue-vscode-format" ref="nofollow noopener noreferrer">这里</a></p>
<p>参考文章：</p>
<ul>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.github.io%2Fvetur%2Fformatting.html" title="https://vuejs.github.io/vetur/formatting.html" ref="nofollow noopener noreferrer">Vetur 官方文档</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprettier%2Fprettier-eslint" title="https://github.com/prettier/prettier-eslint" ref="nofollow noopener noreferrer">prettier-eslint github rep</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Feslint.cn%2Fdocs%2Fuser-guide%2Fconfiguring" title="http://eslint.cn/docs/user-guide/configuring" ref="nofollow noopener noreferrer">eslint configuring</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Feslint.cn%2Fdocs%2Frules%2F" title="http://eslint.cn/docs/rules/" ref="nofollow noopener noreferrer">eslint rules</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fdocs%2Fgitignore" title="https://git-scm.com/docs/gitignore" ref="nofollow noopener noreferrer">gitignore</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fprettier.io%2Fdocs%2Fen%2Fintegrating-with-linters.html" title="https://prettier.io/docs/en/integrating-with-linters.html" ref="nofollow noopener noreferrer">Prettier Integrating with Linters</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=http%3A%2F%2Fstariveer.coding.me%2Ffe-doc%2F" title="http://stariveer.coding.me/fe-doc/" ref="nofollow noopener noreferrer">He Xing 的 blog</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.jongallant.com%2F2019%2F02%2Fvuejs-vetur-vscode-format-eslint-issues%2F" title="https://blog.jongallant.com/2019/02/vuejs-vetur-vscode-format-eslint-issues/" ref="nofollow noopener noreferrer">How I Resolved Vue.js, VSCode, Vetur, Prettyhtml, and Prettier Formatting and ES Lint Issues</a></li>
<li><a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbeautify-web%2Fjs-beautify" title="https://github.com/beautify-web/js-beautify" ref="nofollow noopener noreferrer">js-beautify github rep 及说明</a></li>
</ul>
<blockquote>
<p>Tips</p>
</blockquote>
<ul>
<li>由于 vetur 最新版本出现 bug，需要回退到  0.18.1 版本，具体信息见：<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvetur%2Fissues%2F1220" title="https://github.com/vuejs/vetur/issues/1220" ref="nofollow noopener noreferrer">github.com/vuejs/vetur…</a></li>
</ul>
</div>  
</div>
            