
---
title: '使用 Angular Schematics 快速生成模板代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1205'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 17:56:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=1205'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">准备</h2>
<ol>
<li>全局安装 <code>@angular-devkit/schematics-cli</code> 以使用 <code>schematics</code> 命令</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install -g @angular-devkit/schematics-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建新的<code>Schematics</code>项目</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ schematics blank <schematic-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在已生成的Schematics工程根目录下调用该命令会快速添加一个以填写的<code><schematic-name></code>命名的schematic空白模板，并在<code>collection.json</code>中添加相应基础信息。</p>
<h2 data-id="heading-1">步骤</h2>
<p>创建一个Schematics初始工程</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ schematics blank my-schematics
$ <span class="hljs-built_in">cd</span> my-schematics
$ npm i
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-2">1. Schematics文件构成</h3>
<h4 data-id="heading-3"><strong><code>/src/collection.json</code></strong></h4>
<p><code>collection.json</code> 文件是整个Schematics的主要定义文件，并且包含该库中所有可用schematic模板的定义。</p>
<blockquote>
<p>如果你查看过 Angular CLI 生成的项目中默认提供的 <code>@schematics/angular</code> 包，会发现它的 <code>collection.json</code> 中包含了常用的生成<code>component</code>或<code>service</code>的命令。换句话说，我们可以用Schematics生成任何东西。</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"../node_modules/@angular-devkit/schematics/collection-schema.json"</span>,
  <span class="hljs-attr">"schematics"</span>: &#123;
    <span class="hljs-attr">"my-schematics"</span>: &#123;
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"A blank schematic."</span>,
      <span class="hljs-attr">"factory"</span>: <span class="hljs-string">"./my-schematics/index#mySchematics"</span>
       
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>description</code>：描述该Schematic模板</li>
<li><code>factory</code>：指明该Schematic模板入口。从该文件可以看出，生成的Schematics初始工程默认提供了一个同名的<code>my-schematics</code>模板，指向<code>./my-schematics/index</code>文件并特别指向<code>mySchematics</code>函数。也可以仅使用 <code>"factory": "./my-schematics/index"</code>, 需要将<code>index.ts</code>中<code>export function mySchematics()&#123;&#125;</code>更改为<code>export default function()&#123;&#125;</code>。</li>
</ul>
<p>附加属性：</p>
<ul>
<li><code>aliases</code>（可选）：指定该Schematic模板的一个或多个别名，以string数组表示。</li>
<li><code>schema</code>（可选）：指明每个Schematic模板单独的schema和所有的可用的命令行选项参数。</li>
</ul>
<p>另外，注意Schematics工程中<code>package.json</code>有一个<code>schematic</code>属性指向 <code>collection.json</code> 文件。</p>
<h4 data-id="heading-4"><strong><code>index.ts</code></strong></h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Rule, SchematicContext, Tree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics'</span>;
<span class="hljs-comment">// 可以不用将本函数设置为默认导出，同一文件中可以有多个 rule factory</span>
<span class="hljs-comment">// 这是一个 schematic 工厂函数，最终返回一个 rule</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mySchematics</span>(<span class="hljs-params">_options: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, _context: SchematicContext</span>) =></span> &#123;
    <span class="hljs-comment">// schematic rule 会被 Tree 和 Schematic context 调用</span>
    <span class="hljs-comment">// rule 会把对文件的变换处理添加到 Tree 上，返回处理后的 Tree 给下一条 rule，这就是说，schematic rule 是可组合的</span>
    <span class="hljs-keyword">return</span> tree;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><strong><code>schema.json</code></strong> （需要时手动创建）</h4>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"http://json-schema.org/schema"</span>,
  <span class="hljs-attr">"$id"</span>: <span class="hljs-string">"MyFirstSchematic"</span>,
  <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Hello Option Schema"</span>,
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"object"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"My First Schematic"</span>,
  <span class="hljs-attr">"properties"</span>: &#123;
    <span class="hljs-attr">"name"</span>: &#123;                               <span class="hljs-comment">// 参数名</span>
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,                     <span class="hljs-comment">// 参数类型</span>
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"The name of file"</span>,    <span class="hljs-comment">// 参数描述</span>
      <span class="hljs-attr">"$default"</span>: &#123;                         <span class="hljs-comment">// 设为默认参数</span>
        <span class="hljs-attr">"$source"</span>: <span class="hljs-string">"argv"</span>,                  <span class="hljs-comment">// 从命令行命令传入</span>
        <span class="hljs-attr">"index"</span>: <span class="hljs-number">0</span>                          <span class="hljs-comment">// 在命令中的默认位置。</span>
        <span class="hljs-comment">// 例如：schematics .:my-schematics Mirai (默认位置) </span>
        <span class="hljs-comment">// 对比 schematics .:my-schematics --name=Mirai (标准传入形式)</span>
      &#125;,
      <span class="hljs-attr">"x-prompt"</span>: <span class="hljs-string">"Who do we want to greet?"</span> <span class="hljs-comment">// 未传入该位置参数时的交互提示</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"required"</span>: [
    <span class="hljs-string">"name"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-6">2. Schematics 相关基本概念</h3>
<h4 data-id="heading-7"><strong>factory</strong></h4>
<p>工厂函数将接受一些自定义的参数 <code>_options</code> 并返回一条规则。</p>
<blockquote>
<p>为什么需要工厂函数而不是直接实施一条规则：我们希望 schematic 模板能灵活调整规则以适应一定范围内的需求，所以需要一个函数接收自定义参数 <code>_options</code></p>
</blockquote>
<h4 data-id="heading-8"><strong>Rule</strong></h4>
<p>规则是通过Tree和SchematicContext调用的，并且可以调用其他已经实现的规则。一旦被调用，规则将对树进行调整，并将其返回以供进一步处理。</p>
<h3 data-id="heading-9"><strong>Tree</strong></h3>
<blockquote>
<p>Schematics都是关于代码生成和现有文件的更改。</p>
</blockquote>
<p>Tree 是工作空间中每个文件的虚拟表示。使用虚拟树而不是直接操作文件有以下一些优势：1）只有在每个 schematic 都成功运行的情况下，我们才会提交对树的更改。 2）在 debug 模式下（使用 <code>--dry-run</code> 标识），可以预览文件的改动而不影响实际的文件系统。 3）I/O 操作仅发生在整个处理过程结束后。</p>
<hr>
<h3 data-id="heading-10">3. 从一个简单的例子体验Schematics</h3>
<p>让我们从默认生成的 <code>/src/my-schematics</code> 模板开始体验。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//index.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mySchematics</span>(<span class="hljs-params">_options: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, _context: SchematicContext</span>) =></span> &#123;
    tree.create(<span class="hljs-string">'hello.js'</span>, <span class="hljs-string">`console.log('Hello Schematics');`</span>);
    <span class="hljs-keyword">return</span> tree;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建并在当前工程根目录下运行：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm run build
$ schematics .:my-schematics
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：显示 <code>CREATE hello.js (32 bytes)</code> 但没有实际文件生成。</p>
<p>原因：在使用相对路径调用schematics时默认为调试模式，每次使用时需要添加 <code>--debug=false</code> 或 <code>--dry-run=false</code> 关闭调试模式。</p>
<p>再次调用 <code>schematics .:my-schematics --debug=false</code>，至此，成功生成一个 <code>hello.js</code> 文件，其内容为 <code>console.log('Hello Schematics');</code> 。</p>
<hr>
<h3 data-id="heading-11">4. 向schematics传入自定义选项</h3>
<p>在<code>/src/my-schematics</code>下创建<code>schema.json</code>，添加以下代码。这里我们以自定义一个<code>name</code>参数为例。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"http://json-schema.org/schema"</span>,
  <span class="hljs-attr">"$id"</span>: <span class="hljs-string">"MyFirstSchematic"</span>,
  <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Hello Option Schema"</span>,
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"object"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"My First Schematic"</span>,
  <span class="hljs-attr">"properties"</span>: &#123;
    <span class="hljs-attr">"name"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"The name of file"</span>,
      <span class="hljs-attr">"$default"</span>: &#123;
        <span class="hljs-attr">"$source"</span>: <span class="hljs-string">"argv"</span>,
        <span class="hljs-attr">"index"</span>: <span class="hljs-number">0</span>
      &#125;,
      <span class="hljs-attr">"x-prompt"</span>: <span class="hljs-string">"Who do we want to greet?"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"required"</span>: [
    <span class="hljs-string">"name"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>collection.json</code> 中引入创建的 <code>schema.json</code> 。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"$schema"</span>: <span class="hljs-string">"../node_modules/@angular-devkit/schematics/collection-schema.json"</span>,
  <span class="hljs-attr">"schematics"</span>: &#123;
    <span class="hljs-attr">"my-schematics"</span>: &#123;
      <span class="hljs-attr">"description"</span>: <span class="hljs-string">"A blank schematic."</span>,
      <span class="hljs-attr">"factory"</span>: <span class="hljs-string">"./my-schematics/index#mySchematics"</span>,
      <span class="hljs-attr">"schema"</span>: <span class="hljs-string">"./my-schematics/schema.json"</span>           <span class="hljs-comment">// add this</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，也可以创建一个 <code>schema.d.ts</code> 来为我们的原理图提供代码及类型的检查。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> Schema&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后于 <code>index.ts</code> 中引入并使用定义的<code>Schema</code>类型（<code>function mySchematics(_options: Schema): Rule</code>）。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Rule, SchematicContext, Tree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics'</span>;
<span class="hljs-keyword">import</span> &#123; Schema &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./schema'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mySchematics</span>(<span class="hljs-params">_options: Schema</span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, _context: SchematicContext</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; name &#125; = _options;
    tree.create(<span class="hljs-string">'hello.js'</span>, <span class="hljs-string">`console.log('Hello <span class="hljs-subst">$&#123;name&#125;</span>');`</span>);
    <span class="hljs-keyword">return</span> tree;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调试（每次调试前将上次生成的<code>hello.js</code>删除）：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm run build
$ schematics .:my-schematics Mirai --debug=<span class="hljs-literal">false</span>
or
$ schematics .:my-schematics --name=Mirai --debug=<span class="hljs-literal">false</span>
or
$ schematics .:my-schematics --debug=<span class="hljs-literal">false</span> 
未传入name参数会提示： ? Who <span class="hljs-keyword">do</span> we want to greet? 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示生成<code>hello.js</code>文件（<code>CREATE hello.js (27 bytes)</code>），内容：<code>console.log('Hello Mirai');</code>，参数传入成功！</p>
<hr>
<h3 data-id="heading-12">5. 生成更复杂的schematic模板</h3>
<p>创建一个新的模板<code>component</code>来体验类似<code>ng g c <component-name></code>命令生成的<code><component-name>.component.ts</code>文件。</p>
<p>在根目录下调用<code>schematics blank component</code>，在生成<code>/src/component/</code>文件夹下创建<code>files</code>文件夹，并在里面创建<code>__name@dasherize__.component.ts.template</code>文件。（另外需要在<code>/src/component/</code>文件夹下创建<code>schema.json</code> <code>schema.d.ts</code>，在<code>collection.json</code>中添加<code>schema</code>属性等，见上一步）</p>
<blockquote>
<p>__(双下划线)是分隔符，将name变量与其他普通字符串分隔开。dasherize是一个辅助函数，它将接收name变量的值并将其转换为kebab case字符串，@是将变量应用到辅助函数的方法。</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// __name@dasherize__.component.ts.template</span>
<span class="hljs-keyword">import</span> &#123; Component, OnInit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'my-<%= dasherize(name) %>'</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">'./<%= dasherize(name) %>.component.html'</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">'./<%= dasherize(name) %>.component.css'</span>]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <%</span>= classify(name) %>Component <span class="hljs-keyword">implements</span> OnInit &#123;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-function"><span class="hljs-title">ngOnInit</span>(<span class="hljs-params"></span>)</span> &#123;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模板文件书写：</p>
<ul>
<li>模板语言使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fejs.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ejs.bootcss.com/" ref="nofollow noopener noreferrer">EJS</a></li>
<li>从 <code>@angular-devkit/core</code> 中引入 <code>strings</code> ，使用其中的 <code>dasherize / classify / underscore</code> 等方法对 <code>name</code> 进行处理。</li>
</ul>
<p>EJS标签含义：</p>
<ul>
<li><% '脚本' 标签，用于流程控制，无输出。</li>
<li><%_ 删除其前面的空格符</li>
<li><%= 输出数据到模板（输出是转义 HTML 标签）</li>
<li><%- 输出非转义的数据到模板</li>
<li><%# 注释标签，不执行、不输出内容</li>
<li><%% 输出字符串 '<%'</li>
<li>%> 一般结束标签</li>
<li>-%> 删除紧随其后的换行符</li>
<li>_%> 将结束标签后面的空格符删除</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// index.ts</span>
<span class="hljs-keyword">import</span> &#123; Rule, SchematicContext, Tree, mergeWith, applyTemplates, apply, url &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/schematics'</span>;
<span class="hljs-keyword">import</span> &#123; Schema &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./schema'</span>;
<span class="hljs-keyword">import</span> &#123; strings &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular-devkit/core'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">component</span>(<span class="hljs-params">_options: Schema</span>): <span class="hljs-title">Rule</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">tree: Tree, _context: SchematicContext</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> mergeWith(apply(url(<span class="hljs-string">'./files'</span>), [
      applyTemplates(&#123;
        ...strings,
        <span class="hljs-attr">name</span>: _options.name
      &#125;)
    ]))(tree, _context);      <span class="hljs-comment">//(tree, _context)防止TS编译器报警 "tree 未使用"</span>
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>index.ts</code>中的转换规则：</p>
<ul>
<li><code>url()</code> 指定模板文件路径。</li>
<li><code>applyTemplate()</code> 接受向模板文件嵌入的参数及处理函数，转换文件同时删去 <code>.template</code> 后缀。</li>
<li><code>apply()</code> 对模板源应用多个规则，并返回转换后的模板。</li>
<li>从<code>@angular-devkit/schematics</code>中引入以上方法。</li>
</ul>
<p>在当前工程根路径下执行：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm run build
$ schematics .:component --name=UserList --debug=<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功生成<code>user-list.component</code>文件，可以看到，内容中<code>name</code>参数被修改为传入的<code>UserList</code>的对应格式。</p>
<p>最后发布至NPM，就可以在项目中快速生成自定义的模板代码啦。</p>
<h2 data-id="heading-13">总结</h2>
<p>以上是一个基本的模板生成例子，<code>Schematics</code> 运行在一个 Node 容器内，所以其可玩性非常强，可以操作文件并修改文件内容，绝大多数文件类型都可以找到相对应的现有类库来支持。</p>
<p>参考<code>@schematics/angular</code>包，可以封装一些类似其<code>utility</code>下的公用方法，来指定生成文件的路径或验证所填参数等。</p>
<hr>
<h2 data-id="heading-14">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40tomastrajan%2Ftotal-guide-to-custom-angular-schematics-5c50cf90cdb4" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@tomastrajan/total-guide-to-custom-angular-schematics-5c50cf90cdb4" ref="nofollow noopener noreferrer">Total Guide To Custom Angular Schematics</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fqiita.com%2Fpuku0x%2Fitems%2F462a038133e7233dfaed" target="_blank" rel="nofollow noopener noreferrer" title="https://qiita.com/puku0x/items/462a038133e7233dfaed" ref="nofollow noopener noreferrer">Schematicsを作ってみよう</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fangular%2Fangular-cli%2Fblob%2Fmaster%2Fpackages%2Fangular_devkit%2Fschematics%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/angular/angular-cli/blob/master/packages/angular_devkit/schematics/README.md" ref="nofollow noopener noreferrer">angular-cli/packages/angular_devkit/schematics</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.okta.com%2Fblog%2F2019%2F02%2F13%2Fangular-schematics" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.okta.com/blog/2019/02/13/angular-schematics" ref="nofollow noopener noreferrer">Use Angular Schematics to Simplify Your Life</a></p></div>  
</div>
            