
---
title: 'Angular Schematics在DevUI Admin中的实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ed3e64daf9e4be99a054b73b2770db6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 15:37:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ed3e64daf9e4be99a054b73b2770db6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ed3e64daf9e4be99a054b73b2770db6~tplv-k3u1fbpfcp-watermark.image" alt="汤汤Tang.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">引言</h1>
<p>Angular Schematics 是基于模板(Template-based)的，Angular 特有的代码生成器，当然它不仅仅是生成代码，也可以修改我们的代码，它使得我们可以基于 Angular CLI 去实现我们自己的一些自动化操作。</p>
<p>相信在平时开发 Angular 项目的同时，大家都用过 <code>ng generate component component-name</code>, <code>ng add @angular/materials</code>, <code>ng generate module module-name</code>，这些都是 Angular 中已经为我们实现的一些 CLI，那么我们应该如何在自己的项目中去实现基于自己项目的 CLI 呢？本文将会基于我们在 <a href="https://github.com/DevCloudFE/ng-devui-admin" target="_blank" rel="nofollow noopener noreferrer">ng-devui-admin</a> 中的实践来进行介绍。欢迎大家持续的关注，后续我们将会推出更加丰富的 CLI 帮助大家更快搭建一个 <code>Admin</code> 页面。</p>
<h1 data-id="heading-1">如何在本地开发你的 Angular Schematics</h1>
<p>在本地开发你需要先安装 <code>schematics</code> 脚手架</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g @angular-devkit/schematics-cli

<span class="hljs-comment"># 安装完成之后新建一个schematics项目</span>
schematics blank --name=your-schematics
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建项目之后你会看到如下目录结构，代表你已经成功创建一个 <code>shematics</code> 项目。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da5287665d64d54b5404d52d3991768~tplv-k3u1fbpfcp-watermark.image" alt="project.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">重要文件介绍</h1>
<ul>
<li>
<p><code>tsconfig.json</code>： 主要与项目打包编译相关，在这不做具体介绍</p>
</li>
<li>
<p><code>collection.json</code>：与你的 CLI 命令相关，用于定义你的相关命令</p>
</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"../node_modules/@angular-devkit/schematics/collection-schema.json"</span>,
  <span class="hljs-attr">"schematics"</span>: &#123;
    <span class="hljs-attr">"first-schematics"</span>: &#123;
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"A blank schematic."</span>,
      <span class="hljs-attr">"factory"</span>: <span class="hljs-string">"./first-schematics/index#firstSchematics"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>first-schematics</code>: 命令的名字，可以在项目中通过 <code>ng g first-schematics:first-schematics</code> 来运行该命令。
<code>description</code>: 对该条命令的描述。
<code>factory</code>: 命令执行的入口函数
通常还会有另外一个属性 <code>schema</code>，我们将在后面进行讲解。</p>
<ul>
<li><code>index.ts</code>：在该文件中实现你命令的相关逻辑</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Rule, SchematicContext, Tree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">firstSchematics</span>(<span class="hljs-params">_options: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, _context: SchematicContext</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> tree;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我们先看几个需要了解的参数：
<code>tree</code>：在这里你可以将 tree 理解为我们整个的 angular 项目，你可以通过 tree 新增文件，修改文件，以及删除文件。
<code>_context</code>：该参数为 <code>schematics</code> 运行的上下文，比如你可以通过 <code>context</code> 执行 <code>npm install</code>。
<code>Rule</code>：为我们制定的操作逻辑。</p>
<h1 data-id="heading-3">实现一个 ng-add 指令</h1>
<p>现在我们通过实现一个 <code>ng-add</code> 指令来更好的熟悉。</p>
<p>同样是基于以上我们已经创建好的项目。</p>
<h2 data-id="heading-4">新建命令相关的文件</h2>
<p>首先我们在 <code>src</code> 目录下新建一个目录 <code>ng-add</code>，然后在该目录下添加三个文件 <code>index.ts</code>, <code>schema.json</code>, <code>schema.ts</code>，之后你的目录结构应该如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f7bad77b99b44d18046713e3dfd47e4~tplv-k3u1fbpfcp-watermark.image" alt="ng-add.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">配置 <code>collection.json</code></h2>
<p>之后我们在 <code>collection.json</code> 中配置该条命令：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"../node_modules/@angular-devkit/schematics/collection-schema.json"</span>,
  <span class="hljs-attr">"schematics"</span>: &#123;
    ...,
    <span class="hljs-attr">"ng-add"</span>: &#123;
      <span class="hljs-attr">"factory"</span>: <span class="hljs-string">"./ng-add/index"</span>,
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Some description about your schematics"</span>,
      <span class="hljs-attr">"schema"</span>: <span class="hljs-string">"./ng-add/schema.json"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">在 <code>files</code> 目录中加入我们想要插入的文件</h2>
<p>关于 <code>template</code> 的语法可以参考 <a href="https://ejs.bootcss.com/#install" target="_blank" rel="nofollow noopener noreferrer">ejs 语法</a></p>
<p><code>app.component.html.template</code></p>
<pre><code class="hljs language-template copyable" lang="template"><div class="my-app">
  <% if (defaultLanguage === 'zh-cn') &#123; %>你好，Angular Schematics!<% &#125; else &#123; %>Hello, My First Angular Schematics!<% &#125; %>
  <h1>&#123;&#123; title &#125;&#125;</h1>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>app.component.scss.template</code></p>
<pre><code class="hljs language-template copyable" lang="template">.app &#123;
  display: flex;
  justify-content: center;
  align-item: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>app.component.ts.template</code></p>
<pre><code class="hljs language-template copyable" lang="template">import &#123; Component &#125; from '@angular/core';

@Component(&#123;
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
&#125;)
export class AppComponent &#123;
  title = <% if (defaultLanguage === 'zh-cn') &#123; %>'你好'<% &#125; else &#123; %>'Hello'<% &#125; %>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">开始实现命令逻辑</h2>
<ul>
<li><code>schema.json</code>：在该文件中定义与用户的交互</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"http://json-schema.org/schema"</span>,
  <span class="hljs-attr">"id"</span>: <span class="hljs-string">"SchematicsDevUI"</span>,
  <span class="hljs-attr">"title"</span>: <span class="hljs-string">"DevUI Options Schema"</span>,
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"object"</span>,
  <span class="hljs-attr">"properties"</span>: &#123;
    <span class="hljs-attr">"defaultLanguage"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Choose the default language"</span>,
      <span class="hljs-attr">"default"</span>: <span class="hljs-string">"zh-cn"</span>,
      <span class="hljs-attr">"x-prompt"</span>: &#123;
        <span class="hljs-attr">"message"</span>: <span class="hljs-string">"Please choose the default language you want to use: "</span>,
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"list"</span>,
        <span class="hljs-attr">"items"</span>: [
          &#123;
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"zh-cn"</span>,
            <span class="hljs-attr">"label"</span>: <span class="hljs-string">"简体中文 (zh-ch)"</span>
          &#125;,
          &#123;
            <span class="hljs-attr">"value"</span>: <span class="hljs-string">"en-us"</span>,
            <span class="hljs-attr">"label"</span>: <span class="hljs-string">"English (en-us)"</span>
          &#125;
        ]
      &#125;
    &#125;,
    <span class="hljs-attr">"i18n"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"boolean"</span>,
      <span class="hljs-attr">"default"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Config i18n for the project"</span>,
      <span class="hljs-attr">"x-prompt"</span>: <span class="hljs-string">"Would you like to add i18n? (default: Y)"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"required"</span>: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上的定义中，我们的命令将会接收两个参数分别为 <code>defaultLanguage</code>，<code>i18n</code>，我们以 <code>defaultLanguage</code> 为例讲解对参数的相关配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"defaultLanguage"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Choose the default language"</span>,
    <span class="hljs-attr">"default"</span>: <span class="hljs-string">"zh-cn"</span>,
    <span class="hljs-attr">"x-prompt"</span>: &#123;
      <span class="hljs-attr">"message"</span>: <span class="hljs-string">"Please choose the default language you want to use: "</span>,
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"list"</span>,
      <span class="hljs-attr">"items"</span>: [
        &#123;
          <span class="hljs-attr">"value"</span>: <span class="hljs-string">"zh-cn"</span>,
          <span class="hljs-attr">"label"</span>: <span class="hljs-string">"简体中文 (zh-ch)"</span>
        &#125;,
        &#123;
          <span class="hljs-attr">"value"</span>: <span class="hljs-string">"en-us"</span>,
          <span class="hljs-attr">"label"</span>: <span class="hljs-string">"English (en-us)"</span>
        &#125;
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>type</code> 代表该参数的类型是 <code>string</code>。
<code>default</code> 为该参数的默认值为 <code>zh-cn</code>。
<code>x-prompt</code> 定义与用户的交互，<code>message</code> 为我们对用户进行的相关提问，在这里我们的 <code>type</code> 为 <code>list</code> 代表我们会为用户提供 <code>items</code> 中列出的选项供用户进行选择。</p>
<ul>
<li><code>schema.ts</code>：在该文件中定义我们接收到的参数类型</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> Schema &#123;
  <span class="hljs-attr">defaultLanguage</span>: <span class="hljs-built_in">string</span>;
  i18n: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>index.ts</code>：在该文件中实现我们的操作逻辑，假设在此次 <code>ng-add</code> 操作中，我们根据用户输入的 <code>defaultLanguage</code>, <code>i18n</code> 来对用户的项目进行相应的更改，并且插入相关的 npm 包，再进行安装。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123;
  apply,
  applyTemplates,
  chain,
  mergeWith,
  move,
  Rule,
  SchematicContext,
  SchematicsException,
  Tree,
  url
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics'</span>;
<span class="hljs-keyword">import</span> &#123; NodePackageInstallTask &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics/tasks'</span>;
<span class="hljs-keyword">import</span> &#123; Schema <span class="hljs-keyword">as</span> AddOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./schema'</span>;

<span class="hljs-keyword">let</span> projectWorkspace: &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-built_in">string</span>;
  sourceRoot: <span class="hljs-built_in">string</span>;
  defaultProject: <span class="hljs-built_in">string</span>;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> packgeType = <span class="hljs-string">'dependencies'</span> | <span class="hljs-string">'devDependencies'</span> | <span class="hljs-string">'scripts'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> PACKAGES_I18N = [
  <span class="hljs-string">'@devui-design/icons@^1.2.0'</span>,
  <span class="hljs-string">'@ngx-translate/core@^13.0.0'</span>,
  <span class="hljs-string">'@ngx-translate/http-loader@^6.0.0'</span>,
  <span class="hljs-string">'ng-devui@^11.1.0'</span>
];
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> PACKAGES = [<span class="hljs-string">'@devui-design/icons@^1.2.0'</span>, <span class="hljs-string">'ng-devui@^11.1.0'</span>];
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> PACKAGE_JSON_PATH = <span class="hljs-string">'package.json'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ANGULAR_JSON_PATH = <span class="hljs-string">'angular.json'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options: AddOptions</span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, context: SchematicContext</span>) =></span> &#123;
    <span class="hljs-comment">// 获取项目空间中我们需要的相关变量</span>
    getWorkSpace(tree);

    <span class="hljs-comment">// 根据是否选择i18n插入不同的packages</span>
    <span class="hljs-keyword">const</span> packages = options.i18n ? PACKAGES_I18N : PACKAGES;
    addPackage(tree, packages, <span class="hljs-string">'dependencies'</span>);

    <span class="hljs-comment">// 执行 npm install</span>
    context.addTask(<span class="hljs-keyword">new</span> NodePackageInstallTask());

    <span class="hljs-comment">// 自定义的一系列 Rules</span>
    <span class="hljs-keyword">return</span> chain([removeOriginalFiles(), addSourceFiles(options)]);
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面时使用到的函数的具体实现：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// getWorkSpace</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getWorkSpace</span>(<span class="hljs-params">tree: Tree</span>) </span>&#123;
  <span class="hljs-keyword">let</span> angularJSON;
  <span class="hljs-keyword">let</span> buffer = tree.read(ANGULAR_JSON_PATH);
  <span class="hljs-keyword">if</span> (buffer) &#123;
    angularJSON = <span class="hljs-built_in">JSON</span>.parse(buffer.toString());
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> SchematicsException(
      <span class="hljs-string">'Please make sure the project is an Angular project.'</span>
    );
  &#125;

  <span class="hljs-keyword">let</span> defaultProject = angularJSON.defaultProject;
  projectWorkspace = &#123;
    <span class="hljs-attr">root</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">sourceRoot</span>: angularJSON.projects[defaultProject].sourceRoot,
    defaultProject
  &#125;;

  <span class="hljs-keyword">return</span> projectWorkspace;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// removeOriginalFiles</span>
<span class="hljs-comment">// 根据自己的需要选择需要删除的文件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeOriginalFiles</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree</span>) =></span> &#123;
    [
      <span class="hljs-string">`<span class="hljs-subst">$&#123;projectWorkspace.sourceRoot&#125;</span>/app/app.component.ts`</span>,
      <span class="hljs-string">`<span class="hljs-subst">$&#123;projectWorkspace.sourceRoot&#125;</span>/app/app.component.html`</span>,
      <span class="hljs-string">`<span class="hljs-subst">$&#123;projectWorkspace.sourceRoot&#125;</span>/app/app.component.scss`</span>,
      <span class="hljs-string">`<span class="hljs-subst">$&#123;projectWorkspace.sourceRoot&#125;</span>/app/app.component.css`</span>
    ]
      .filter(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> tree.exists(f))
      .forEach(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> tree.delete(f));
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 files 下的文件拷贝到指定的路径下，关于 <code>chain</code>, <code>mergeWith</code>, <code>apply</code>, <code>template</code> 的详细使用方法可以参考 <a href="https://github.com/angular/angular-cli/blob/master/packages/angular_devkit/schematics/README.md" target="_blank" rel="nofollow noopener noreferrer">Schematics</a></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// addSourceFiles</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addSourceFiles</span>(<span class="hljs-params">options: AddOptions</span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> chain([
    mergeWith(
      apply(url(<span class="hljs-string">'./files'</span>), [
        applyTemplates(&#123;
          <span class="hljs-attr">defaultLanguage</span>: options.defaultLanguage
        &#125;),
        move(<span class="hljs-string">`<span class="hljs-subst">$&#123;projectWorkspace.sourceRoot&#125;</span>/app`</span>)
      ])
    )
  ]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// readJson</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readJson</span>(<span class="hljs-params">tree: Tree, file: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">type</span>?: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-keyword">if</span> (!tree.exists(file)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-keyword">const</span> sourceFile = tree.read(file)!.toString(<span class="hljs-string">'utf-8'</span>);
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> json = <span class="hljs-built_in">JSON</span>.parse(sourceFile);
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">type</span> && !json[<span class="hljs-keyword">type</span>]) &#123;
      json[<span class="hljs-keyword">type</span>] = &#123;&#125;;
    &#125;
    <span class="hljs-keyword">return</span> json;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Failed when parsing file <span class="hljs-subst">$&#123;file&#125;</span>.`</span>);
    <span class="hljs-keyword">throw</span> error;
  &#125;
&#125;

<span class="hljs-comment">// writeJson</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeJson</span>(<span class="hljs-params">tree: Tree, file: <span class="hljs-built_in">string</span>, source: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">void</span> </span>&#123;
  tree.overwrite(file, <span class="hljs-built_in">JSON</span>.stringify(source, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));
&#125;

<span class="hljs-comment">// readPackageJson</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readPackageJson</span>(<span class="hljs-params">tree: Tree, <span class="hljs-keyword">type</span>?: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-keyword">return</span> readJson(tree, PACKAGE_JSON_PATH, <span class="hljs-keyword">type</span>);
&#125;

<span class="hljs-comment">// writePackageJson</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writePackageJson</span>(<span class="hljs-params">tree: Tree, json: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-keyword">return</span> writeJson(tree, PACKAGE_JSON_PATH, json);
&#125;

<span class="hljs-comment">// addPackage</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addPackage</span>(<span class="hljs-params">
  tree: Tree,
  packages: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">string</span>[],
  <span class="hljs-keyword">type</span>: packgeType = <span class="hljs-string">'dependencies'</span>
</span>): <span class="hljs-title">Tree</span> </span>&#123;
  <span class="hljs-keyword">const</span> packageJson = readPackageJson(tree, <span class="hljs-keyword">type</span>);

  <span class="hljs-keyword">if</span> (packageJson == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> tree;
  &#125;

  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(packages)) &#123;
    packages = [packages];
  &#125;
  packages.forEach(<span class="hljs-function">(<span class="hljs-params">pck</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> splitPosition = pck.lastIndexOf(<span class="hljs-string">'@'</span>);
    packageJson[<span class="hljs-keyword">type</span>][pck.substr(<span class="hljs-number">0</span>, splitPosition)] = pck.substr(
      splitPosition + <span class="hljs-number">1</span>
    );
  &#125;);

  writePackageJson(tree, packageJson);
  <span class="hljs-keyword">return</span> tree;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了保持 <code>index.ts</code> 文件的简洁，可以将相关操作的方法抽取到一个新的文件中进行引用。</p>
<h2 data-id="heading-8">测试 <code>ng-add</code></h2>
<p>至此我们已经完成了 <code>ng-add</code> 命令，现在我们对该命令进行测试：</p>
<ul>
<li><code>ng new test</code> 初始化一个 Angular 项目</li>
<li><code>cd test && mkdir libs</code> 在项目中添加一个 libs 文件夹，将图中标蓝的文件拷贝到其中</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/103251f35b7f4e32a74a9355b8dcf183~tplv-k3u1fbpfcp-watermark.image" alt="files.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>之后在命令行中执行 <code>npm link libs/</code></li>
<li>link 完成之后 <code>cd libs && npm run build && cd ..</code></li>
<li>现在执行 <code>ng add first-schematics</code> 之后会看到如下提示</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af7c8eef11ed44f58ac108f57a21e8e8~tplv-k3u1fbpfcp-watermark.image" alt="result.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>最后我们通过 <code>npm start</code> 来查看执行的结果如下</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e758d48910d942dfbd3a08ec6bd80388~tplv-k3u1fbpfcp-watermark.image" alt="pages.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">结语</h1>
<p>综上简单介绍了一个 <code>Schematics</code> 的实现，更多的一些应用欢迎大家查看 <a href="https://github.com/DevCloudFE/ng-devui-admin" target="_blank" rel="nofollow noopener noreferrer">ng-devui-admin</a> 中的实现。</p>
<p>欢迎加DevUI小助手微信：devui-official，一起讨论Angular技术和前端技术。</p>
<p>欢迎关注我们<a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://github.com/devcloudfe/ng-devui" target="_blank" rel="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://devui.design/admin/" target="_blank" rel="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-10">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6956155033410863134" target="_blank">《号外号外！DevUI Admin V1.0 发布啦！》</a></p>
<p><a href="https://juejin.cn/post/6970840860158066702" target="_blank">Monorepo初体验：将现有的NG CLI工程改造成Monorepo方式</a></p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p></div>  
</div>
            