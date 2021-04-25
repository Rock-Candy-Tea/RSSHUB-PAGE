
---
title: '代码检查工具！从 TSLint  到 ESLint'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60f4aead025d41bd8984999a41ff584d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 01:29:37 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60f4aead025d41bd8984999a41ff584d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60f4aead025d41bd8984999a41ff584d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2019 年 1 月，<code>TypeScript</code> 官方决定全面采用 <code>ESLint</code>，之后也发布 <code>typescript-eslint</code> 项目，以集中解决 <code>TypeScript</code> 和 <code>ESLint</code> 兼容性问题。而之前的两个 <code>lint</code> 解决方案都将弃用：</p>
<ul>
<li><code>typescript-eslint-parser</code> 已停止维护</li>
<li>在完成 <code>ESLint</code> 功能后，将弃用 <code>TSLint</code> 并帮助用户迁移到 <code>ESLint</code></li>
</ul>
<h3 data-id="heading-0">TS 官方转向 ESLint 的原因:</h3>
<ol>
<li>TSLint 执行规则的方式存在一些框架问题，从而<strong>影响性能</strong>，而修复这些问题会破坏现有的规则。</li>
<li>ESLint 的<strong>性能更好</strong>，并且社区用户通常拥有 ESLint 的规则配置（比如 React 和 Vue 的配置），而不会拥有 TSLint 的规则配置。</li>
</ol>
<h2 data-id="heading-1">已经有 TypeScript，为什么需要 ESLint ？</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/399beef1cf5741fdb5da5a5e1ddff59c~tplv-k3u1fbpfcp-watermark.image" alt="ts.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>ts</code> 编译器主要做类型检查和语言转换，<code>ESLint</code> 则可以保持代码风格的统一；两者的功能有部分重合，但也各有职责。</p>
<p>但是，<code>ESLint</code> 处理 <code>ts</code> 代码会遇到一些问题？因为 <code>ts</code> 编译器和 <code>ESLint</code> 在开始各自的工作之前都会将代码转换成 <code>AST</code>（抽象语法树），而两种语法树是不兼容的。这时，我们可以使用 <code>typescript-eslint</code> 项目，它为 <code>ESLint</code> 提供了专门解析 ts 代码的编译器，来解决 <code>TypeScript</code> 和 <code>ESLint</code> 兼容性问题。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1969849afea428b953718cb9c7a411d~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件 (3).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">在 TypeScript 中使用 ESLint</h2>
<h3 data-id="heading-3">安装</h3>
<pre><code class="copyable">npm i eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@typescript-eslint/parser</code>为 <code>ESLint</code> 提供解析器。（别忘了同时安装 <code>typescript</code>）
<code>@typescript-eslint/eslint-plugin</code> 它作为 <code>ESLint</code> 默认规则的补充，提供了一些额外的适用于 <code>ts</code> 语法的规则。</p>
<h3 data-id="heading-4">创建配置文件</h3>
<p><code>ESLint</code> 需要一个配置文件来决定对哪些规则进行检查，配置文件的名称一般是 .<code>eslintrc.js</code> 或 <code>.eslintrc.json</code>。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .eslintrc.json</span>
&#123;
  <span class="hljs-attr">"parser"</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>,
  <span class="hljs-attr">"plugins"</span>: [<span class="hljs-string">"@typescript-eslint"</span>],
  <span class="hljs-attr">"parserOptions"</span>: &#123;
    <span class="hljs-attr">"project"</span>: <span class="hljs-string">"./tsconfig.json"</span>
  &#125;,
  <span class="hljs-attr">"extends"</span>: [<span class="hljs-string">"plugin:@typescript-eslint/recommended"</span>],
  <span class="hljs-attr">"rules"</span>: &#123; <span class="hljs-attr">"@typescript-eslint/no-inferrable-types"</span>: <span class="hljs-string">"off"</span> &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rules</code> 的取值一般是一个数组，其中第一项是 <code>off</code>、<code>warn</code> 或 <code>error</code> 中的一个，表示关闭、警告和报错。后面的项都是该规则的其他配置。</p>
<p>如果没有其他配置的话，则可以将规则的取值简写为数组中的第一项（上例中的 <code>@typescript-eslint/no-inferrable-types</code>）。</p>
<p><code>off</code>、<code>warn</code> 和 <code>error</code>的含义如下：</p>
<ul>
<li><code>off</code>：禁用此规则</li>
<li><code>warn</code>：代码检查时输出错误信息，但是不会影响到 <code>exit code</code></li>
<li><code>error</code>：发现错误时，不仅会输出错误信息，而且 <code>exit code</code> 将被设为 <code>1</code>（一般 <code>exit code</code> 不为 <code>0</code> 则表示执行出现错误）</li>
</ul>
<h3 data-id="heading-5">检查整个项目的 ts/js 文件</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  ...
  <span class="hljs-attr">"script"</span>: &#123;
    ...
    <span class="hljs-attr">"lint"</span>: <span class="hljs-string">"eslint src --ext .js,.ts"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm run lint
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">在 VSCode 中集成 ESLint 检查</h3>
<p>安装 <code>ESLint</code> 插件，点击「扩展」按钮，搜索 <code>ESLint</code>，然后安装即可。</p>
<p><code>VSCode</code> 中的 <code>ESLint</code> 插件默认是不会检查 <code>.ts</code> 后缀的，需要在「文件 => 首选项 => 设置 => 工作区」中（也可以在项目根目录下创建一个配置文件 <code>.vscode/settings.json</code>），添加以下配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  ...
  <span class="hljs-attr">"eslint.validate"</span>: [
    <span class="hljs-string">"javascript"</span>,
    <span class="hljs-string">"javascriptreact"</span>,
    <span class="hljs-string">"vue"</span>,
    <span class="hljs-string">"html"</span>,
    <span class="hljs-string">"typescript"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">比较 babel-eslint 和 typescript-eslint</h2>
<ul>
<li><strong>babel-eslint:</strong> 支持 <code>TypeScript</code> 没有的额外的语法检查，抛弃 <code>TypeScript</code>，不支持类型检查。</li>
<li><strong>typescript-eslint:</strong> 基于 <code>TypeScript</code> 的 <code>AST</code>，支持创建基于类型信息的规则（<code>tsconfig.json</code>）</li>
</ul>
<p>两者底层机制不一样，不要一起用。<code>Babel</code> 体系建议用 <code>babel-eslint</code>，否则可以用 <code>typescript-eslint</code>。</p>
<h2 data-id="heading-8">TypeScript 工程系列</h2>
<ul>
<li><a href="https://juejin.cn/post/6951674686639964168/" target="_blank">不用的 TypeScript？命名空间。</a></li>
<li><a href="https://juejin.cn/post/6952488541255368741/" target="_blank">TS 的努力：声明合并</a></li>
<li><a href="https://juejin.cn/post/6952821026950479886" target="_blank">如何在 TypeScript 中引入外部类库？</a></li>
<li><a href="https://juejin.cn/post/6953553286657998879/" target="_blank">快速上手，tsconfig（文件选项）</a></li>
<li><a href="https://juejin.cn/post/6953554051879403534" target="_blank">快速上手，tsconfig （编译选项）</a></li>
<li><a href="https://juejin.cn/post/6953892137175875597" target="_blank">要不要学一下更高效的 TS 构建方式（工程引入）</a></li>
<li><a href="https://juejin.cn/post/6954304242093932557" target="_blank">TS 编译工具！从 ts-loader 到 Babel</a></li>
<li><a href="https://juejin.cn/post/6955025103507849223/" target="_blank">代码检查工具！从 TSLint  到 ESLint</a></li>
</ul></div>  
</div>
            