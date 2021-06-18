
---
title: 'TypeScript 基础（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f341bafdff94fea9014a1cd0e2c5f7c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 01:50:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f341bafdff94fea9014a1cd0e2c5f7c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、环境搭建与编译执行</h1>
<p>TypeScript 编写的程序并不能直接通过浏览器运行，我们需要先通过 TypeScript 编译器把 TypeScript 代码编译成 JavaScript 代码。</p>
<h2 data-id="heading-1">环境搭建</h2>
<h3 data-id="heading-2">安装 node.js</h3>
<p>TypeScript 的编译器是基于 Node.js 的，所以我们需要先安装 Node.js：<a href="https://nodejs.org/" target="_blank" rel="nofollow noopener noreferrer">node.js官网</a></p>
<p>安装完成以后，可以通过 <code>终端</code> 或者 <code>cmd</code> 等命令行工具来调用 node：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 查看当前 node 版本</span>
node -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">安装 TypeScript 编译器</h3>
<p>通过 <code>NPM</code> 包管理工具安装 TypeScript 编译器：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm i -g typescript
// 或
yarn add -g typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成以后，我们可以通过命令 <code>tsc</code> 来调用编译器：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 查看当前 tsc 编译器版本</span> 
tsc -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">win10 运行 <code>tsc</code> 报错</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f341bafdff94fea9014a1cd0e2c5f7c~tplv-k3u1fbpfcp-watermark.image" alt="ts 编译报错" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以<strong>管理员身份</strong>运行 <code>PowerShell</code>， 设置 <code>set-ExecutionPolicy RemoteSigned</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/333534b639ea4990ba126ac36472a0d8~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_202105232310253.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">编译代码</h2>
<p>默认情况下， TypeScript 的文件的后缀为 <code>.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ./src/test.ts</span>
<span class="hljs-keyword">let</span> str: <span class="hljs-built_in">string</span> = <span class="hljs-string">'una'</span>;

<span class="hljs-keyword">export</span> &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>TypeScript 与 ECMAScript 2015 一样，任何包含顶级 <code>import</code> 或者 <code>export</code> 的文件都被当成一个模块。相反地，<strong>如果一个文件不带有顶级的 <code>import</code> 或者 <code>export</code> 声明，那么它的内容被视为全局可见的</strong>。</p>
</blockquote>
<p>使用我们安装的 TypeScript 编译器 <code>tsc</code> 对 <code>.ts</code> 文件进行编译：<code>tsc ./src/test.ts</code>。<strong>默认情况下会在当前文件所在目录下生成同名的 js 文件</strong>。</p>
<pre><code class="hljs language-shell copyable" lang="shell">tsc ./src/test.ts
// 编译文件放在 src 文件夹
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/226428a818c942478fba6f891297b31e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">常用编译选项</h3>
<ul>
<li><strong><code>--outDir</code></strong>：<strong>指定编译文件输出目录</strong></li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">tsc --outDir ./dist ./src/test.ts
// 编译文件放在dist文件夹下
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7022bdb3243b48f79a951f1eb101d208~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong><code>--target</code></strong>：<strong>指定编译的代码版本目标，默认为 ES3</strong></li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">tsc --outDir ./dist --target ES6 ./src/test.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aead14874ed4f95a66fb89a0d2cc4e9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong><code>--watch</code></strong>：在监听模式下运行，<strong>当文件发生改变的时候自动编译</strong></li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">tsc --outDir ./dist --target ES6 --watch ./src/test.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面几个例子，我们基本可以了解 <code>tsc</code> 的使用了，但是大家应该也发现了，如果每次编译都输入这么一大堆的选项其实是很繁琐的，好在 TypeScript 编译为我们提供了一个更加强大且方便的方式，编译配置文件：<code>tsconfig.json</code> ，我们可以把上面的编译选项保存到这个配置文件中。</p>
<h3 data-id="heading-7">编译配置文件</h3>
<p>我们可以把编译的一些选项保存在一个指定的 json 文件中，默认情况下 <code>tsc</code> 命令运行的时候会自动
去加载运行命令所在的目录下的 <code>tsconfig.json</code> 文件，配置文件格式如下：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// ./tsconfig.json</span>
&#123;
    <span class="hljs-comment">// 编译选项</span>
    <span class="hljs-attr">"compilerOptions"</span>: &#123; 
        <span class="hljs-comment">// js 输出目录</span>
        <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"./dist"</span>, 
        <span class="hljs-comment">// 编译输出目标 ES 版本，默认ES3</span>
        <span class="hljs-attr">"target"</span>: <span class="hljs-string">"ES2015"</span>, 
        <span class="hljs-comment">// 监听改动</span>
        <span class="hljs-attr">"watch"</span>: <span class="hljs-literal">true</span>, 
    &#125;, 
    
    <span class="hljs-comment">// 需要编译的模块</span>
    <span class="hljs-comment">// ** : 所有目录（包括子目录） </span>
    <span class="hljs-comment">// * : 所有文件，也可以指定类型 *.ts </span>
    <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"./src/**/*"</span>] <span class="hljs-comment">// 相对路径</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了单独的配置文件，我们就可以直接运行：<code>tsc</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/081392fc378b4ffdb83b9a7671ba30a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">指定加载的配置文件</h4>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// ./configs/tsconfig.json</span>
&#123;
    <span class="hljs-comment">// 编译选项</span>
    <span class="hljs-attr">"compilerOptions"</span>: &#123; 
        <span class="hljs-comment">// js 输出目录</span>
        <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"../dist"</span>, 
        <span class="hljs-comment">// 编译输出目标 ES 版本，默认ES3</span>
        <span class="hljs-attr">"target"</span>: <span class="hljs-string">"ES2015"</span>, 
        <span class="hljs-comment">// 监听改动</span>
        <span class="hljs-attr">"watch"</span>: <span class="hljs-literal">true</span>, 
    &#125;, 
    
    <span class="hljs-comment">// 需要编译的模块</span>
    <span class="hljs-comment">// ** : 所有目录（包括子目录） </span>
    <span class="hljs-comment">// * : 所有文件，也可以指定类型 *.ts </span>
    <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"../src/**/*"</span>] <span class="hljs-comment">// 相对路径</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除 ./tsconfig.json 文件，重新创建新的配置文件，注意相对路径发生了改变。</p>
<p>使用 <code>--project</code> 或 <code>-p</code> 指定配置文件目录，会<strong>默认加载该目录下的 <code>tsconfig.json</code> 文件</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts">tsc -p ./configs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以指定某个具体的配置文件，把配置文件的文件名改为<code>ts.json</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts">tsc -p ./configs/ts.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f58b664004194c09939773b45570bad0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">二、类型系统初始</h1>
<h2 data-id="heading-10">类型系统组成</h2>
<p>类型系统包含两个重要组成部分：</p>
<ul>
<li>类型标注（定义、注解） - typing</li>
<li>类型检测（检查） - type-checking</li>
</ul>
<h3 data-id="heading-11">类型标注</h3>
<p>类型标注就是<strong>在代码中给数据（变量、函数（参数、返回值））添加类型说明</strong>，当一个变量或者函数（参数）等<strong>被标注后不能存储与标注类型不符合的类型</strong>。</p>
<p>有了标注， TypeScript 编译器就能按照标注对这些数据进行类型合法检测，各种编辑器、IDE 等就能进行智能提示。</p>
<h3 data-id="heading-12">类型检测</h3>
<p>顾名思义，就是<strong>对数据的类型进行检测</strong>。注意这里，重点是类型两字。</p>
<p><strong>类型系统检测的是类型，不是具体值</strong>（虽然，某些时候也可以检测值），比如某个参数的取值范围（1-100之间），我们不能依靠类型系统来完成这个检测，它应该是我们的业务层具体逻辑，类型系统检测的是它的值类型是否为数字！</p>
<h2 data-id="heading-13">类型标注</h2>
<p>在 TypeScript 中，类型标注的基本语法格式为：<strong><code>数据载体:类型</code></strong>。</p>
<h3 data-id="heading-14">基础类型（string，number，boolean）</h3>
<p>基础类型包含：<code>string</code>，<code>number</code>，<code>boolean</code>。</p>
<ul>
<li>
<p>布尔值 boolean</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> isDone: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>数字 number</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> decLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">6</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和 JavaScript 一样，TypeScript 里的<strong>所有数字都是浮点数</strong>。除了支持十进制和十六进制字面量，TypeScript 还支持 ECMAScript 2015 中引入的二进制和八进制字面量。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> hexLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0xf00d</span>;
<span class="hljs-keyword">let</span> binaryLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0b1010</span>;
<span class="hljs-keyword">let</span> octalLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0o744</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>字符串 string <code>let name: string = "bob";</code></p>
<blockquote>
<p><strong>模版字符串</strong>：被反引号包围（`），以$&#123; expr &#125;形式嵌入表达。可以定义多行文本和内嵌表达式。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> name: <span class="hljs-built_in">string</span> = <span class="hljs-string">`una`</span>;
<span class="hljs-keyword">let</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">23</span>;
<span class="hljs-keyword">let</span> sentence: <span class="hljs-built_in">string</span> = <span class="hljs-string">`Hello, my name is <span class="hljs-subst">$&#123; name &#125;</span>.

I'll be <span class="hljs-subst">$&#123; age + <span class="hljs-number">1</span> &#125;</span> years old next month.`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<blockquote>
<p>类型推断：变量初始化时如果没有标识，也会自动识别类型。</p>
</blockquote>
<h3 data-id="heading-15">空（null）和未定义（undefined）类型</h3>
<p>TypeScript 里，<strong>undefined 和 null 两者各自有自己的类型分别叫做 undefined 和 null</strong> 。这两种类型<strong>有且只有一个值</strong>，在标注一个变量为 Null 和 Undefined 类型，那就表示<strong>该变量不能修改了</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-literal">null</span>; 
a = <span class="hljs-literal">null</span>; <span class="hljs-comment">// ok </span>
a = <span class="hljs-number">1</span>; <span class="hljs-comment">// error Null类型一旦标准不能修改</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>默认情况下，null 和 undefined 是所有类型的子类型</strong>。 就是说你<strong>可以把 null 和 undefined 赋值给其它类型的变量</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">number</span>;
a = <span class="hljs-literal">null</span>; <span class="hljs-comment">// ok </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一个<strong>变量声明了，但是未赋值</strong>，那么该变量的<strong>值为 <code>undefined</code></strong> ，但是如果它<strong>同时也没有标注类型的话，默认类型为 <code>any</code></strong>。</p>
<p>因为 <code>null</code> 和 <code>undefined</code> 都是其它类型的子类型，所以默认情况下会有一些隐藏的问题：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a:<span class="hljs-built_in">number</span>; 
a = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 提示：不能将类型'null'分配给类型'number'</span>
a.toFixed(<span class="hljs-number">1</span>); <span class="hljs-comment">// ok（不报错，但实际运行是有问题的）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>然而，当你指定了 <code>--strictNullChecks</code> 标记，<code>null</code> 和 <code>undefined</code> 只能赋值给 <code>void</code> 和它们自己</strong>。 这能避免很多常见的问题。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// ./tsconfig.json</span>
&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123;
        <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"./dist"</span>,
        <span class="hljs-attr">"target"</span>: <span class="hljs-string">"es5"</span>,
        <span class="hljs-attr">"watch"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"strictNullChecks"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 严格的空值检查</span>
    &#125;,
    <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"./src/**/*"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">number</span>; 
a = <span class="hljs-literal">null</span>;
a.toFixed(<span class="hljs-number">1</span>); <span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：TypeScript 鼓励尽可能地使用 <code>--strictNullChecks</code>。</p>
</blockquote>
<h3 data-id="heading-16">数组类型</h3>
<p>TypeScript 中数组存储的类型必须一致，所以在标注数组类型的时候，同时要标注数组中存储的数据类型：</p>
<ul>
<li>
<p>泛型标注：<strong><code>Array<元素类型></code></strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// <number> 表示数组中存储的数据类型</span>
<span class="hljs-keyword">let</span> arr1: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = []; 
arr1.push(<span class="hljs-number">100</span>); <span class="hljs-comment">// ok </span>
arr1.push(<span class="hljs-string">'你好啊'</span>);<span class="hljs-comment">// error 字符串不能赋给类型'number'的参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>简单标注：<strong>在元素类型后面接上 []</strong>，表示<strong>由此类型元素组成的一个数组</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> arr2: <span class="hljs-built_in">string</span>[] = []; 
arr2.push(<span class="hljs-string">'una'</span>); <span class="hljs-comment">// ok </span>
arr2.push(<span class="hljs-number">1</span>); <span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-17">元组类型</h3>
<ul>
<li>元组表示一个 <strong><code>已知元素数量和类型的数组</code>，各元素的类型不必相同</strong>。</li>
<li><strong><code>初始化</code> 数据的个数 以及 <code>对应位置标注类型</code> 必须一致</strong></li>
<li><strong>当访问一个 <em><code>越界</code>（超过之前定义的数量）</em> 的元素，会使用<code>联合类型</code>替代，但必须是元组标注中的类型之一</strong>。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 1. 定义一对值分别为 string 和 number 类型的元组</span>
<span class="hljs-keyword">let</span> x: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>]; <span class="hljs-comment">// 声明一个元组类型</span>
x = [<span class="hljs-string">'hello'</span>, <span class="hljs-number">10</span>]; <span class="hljs-comment">// OK</span>
x = [<span class="hljs-number">10</span>, <span class="hljs-string">'hello'</span>]; <span class="hljs-comment">// Error 初始化 数据的个数 以及 对应位置标注类型 必须一致</span>

<span class="hljs-comment">// 2. 当访问一个已知索引的元素，会得到正确的类型</span>
<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">0</span>].substr(<span class="hljs-number">1</span>)); <span class="hljs-comment">// OK</span>
<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">1</span>].substr(<span class="hljs-number">1</span>)); <span class="hljs-comment">// Error, 'number' does not have 'substr'</span>

<span class="hljs-comment">// 3. 当访问一个越界的元素，会使用联合类型替代：</span>
x[<span class="hljs-number">3</span>] = <span class="hljs-string">'world'</span>; <span class="hljs-comment">// OK, 字符串可以赋值给(string | number)类型</span>
x[<span class="hljs-number">4</span>] = <span class="hljs-literal">true</span>; <span class="hljs-comment">// Error, 布尔不是(string | number)类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">枚举类型（enum）</h3>
<p>枚举的作用是 组织收集一组关联数据的方式，通过枚举我们可以<strong>给一组有关联意义的数据赋予一些友好的名字</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> HTTP_CODE &#123; 
    ERROR,
    OK = <span class="hljs-number">200</span>,
    NOT_FOUND = <span class="hljs-number">404</span>, 
    METHOD_NOT_ALLOWED 
&#125;;

HTTP_CODE.ERROR;<span class="hljs-comment">// 0 第一个枚举值默认为：0</span>
HTTP_CODE.OK;<span class="hljs-comment">// 200 </span>
HTTP_CODE.METHOD_NOT_ALLOWED;  <span class="hljs-comment">// 405 非第一个枚举值为上一个数字枚举值 + 1</span>
HTTP_CODE.OK = <span class="hljs-number">1</span>; <span class="hljs-comment">// error 枚举值为只读（常量），初始化后不可修改</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意事项：</p>
<ul>
<li>
<p><strong><code>key</code> 不能是数字</strong>；</p>
</li>
<li>
<p><strong><code>value</code></strong> 可以是<strong>数字</strong>，称为 数字类型枚举，也可以是<strong>字符串</strong>，称为 字符串类型枚举，但不能是其它值，<strong>默认为数字：0</strong>；</p>
</li>
<li>
<p>枚举值可以省略，如果省略，则：</p>
<ul>
<li><strong>第一个枚举值默认为：0</strong>；</li>
<li><strong>非第一个枚举值为上一个数字枚举值 + 1</strong>；</li>
</ul>
</li>
<li>
<p>枚举值为只读（常量），<strong>初始化后不可修改</strong>；</p>
</li>
<li>
<p>如果<strong>前一个枚举值类型为字符串，则后续枚举项必须手动赋值</strong>；</p>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> URLS &#123; 
    USER_REGISETER = <span class="hljs-string">'/user/register'</span>, 
    USER_LOGIN = <span class="hljs-string">'/user/login'</span>,
    <span class="hljs-comment">// 如果前一个枚举值类型为字符串，则后续枚举项必须手动赋值 </span>
    INDEX = <span class="hljs-number">0</span> 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>枚举名称可以是大写，也可以是小写，推荐使用全大写（通常使用<strong>全大写</strong>的命名方式来标注值为<strong>常量</strong>）。</p>
</blockquote>
<h3 data-id="heading-19">无值类型（void）</h3>
<p>表示<strong>没有任何数据</strong>的类型，通常用于<strong>标注无返回值函数的返回值类型</strong>，函数默认标注类型为： <code>void</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123; 
    <span class="hljs-comment">// 没有 return 或者 return undefined </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明一个 <code>void</code> 类型的变量没有什么大用，因为你只能为它赋予 <code>undefined</code> 和 <code>null</code> ：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> unusable: <span class="hljs-built_in">void</span> = <span class="hljs-literal">undefined</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在 <code>strictNullChecks</code> 为 false 的情况下， undefined 和 null 都可以赋值给 void ，但是<strong>当 <code>strictNullChecks</code> 为 <code>true</code> 的情况下，只有 <code>undefined</code> 才可以赋值给 <code>void</code></strong>。</p>
</blockquote>
<h3 data-id="heading-20">Never 类型</h3>
<p>never 类型表示的是那些<strong>永不存在的值</strong>的类型：</p>
<ul>
<li><strong>抛出异常</strong></li>
<li><strong>无返回值的函数</strong></li>
<li><strong>箭头函数</strong></li>
<li><strong>永不为真的变量</strong></li>
</ul>
<p><strong>never 类型是任何类型的子类型</strong>，也可以赋值给任何类型；然而，<strong>没有类型是 never 的子类型，即使 any 也不可以赋值给 never</strong>。</p>
<p>下面是一些返回 never 类型的函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 返回never的函数必须存在无法达到的终点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">error</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(message);
&#125;

<span class="hljs-comment">// 推断的返回值类型为 never</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fail</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> error(<span class="hljs-string">"Something failed"</span>);
&#125;

<span class="hljs-comment">// 返回 never 的函数必须存在无法达到的终点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">infiniteLoop</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">任意类型（any）</h3>
<p>有的时候，我们并<strong>不确定这个值到底是什么类型 或者 不需要对该值进行类型检测</strong>，就可以标注为 <strong><code>any</code></strong> 类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一个变量 <strong>声明未赋值 且 未标注类型</strong> 的情况下，默认为 <code>any</code> 类型；</li>
<li>任何类型值都可以赋值给 <code>any</code> 类型；</li>
<li><code>any</code> 类型也可以赋值给任意类型；</li>
<li><code>any</code> 类型有任意属性和方法；</li>
</ul>
<blockquote>
<p>标注为 <code>any</code> 类型，也意味着<strong>放弃对该值的类型检测</strong>，同时<strong>放弃 IDE 的智能提示</strong>。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a; <span class="hljs-comment">// 一个变量 声明未赋值 且 未标注类型，默认为 any 类型。当 noImplicitAny 为 true 时，报错。</span>
<span class="hljs-keyword">let</span> c: <span class="hljs-built_in">any</span> = <span class="hljs-string">'una'</span>; <span class="hljs-comment">// any 类型是任何类型的子类型</span>
<span class="hljs-keyword">let</span> d: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
d.toFixed(<span class="hljs-number">1</span>)

d = c; <span class="hljs-comment">// 把 c 赋值给 d，d 变成 any 类型</span>
d.toFixed(<span class="hljs-number">1</span>); <span class="hljs-comment">// d 变成字符串，不具备 toFixed 方法，虽然 IDE 没报错，但是一运行就会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>当指定 <code>noImplicitAny</code> 配置为 <code>true</code> ，当函数参数出现隐含的 <code>any</code> 类型时报错</strong>。</p>
</blockquote>
<h3 data-id="heading-22">未知类型（unknow）</h3>
<p><code>unknow</code>，3.0 版本中新增，属于<strong>安全版的 <code>any</code></strong>，但是与 <code>any</code> 不同的是：</p>
<ul>
<li><code>unknow</code> <strong>仅能赋值给 <code>unknow</code>、<code>any</code></strong>；</li>
<li><code>unknow</code> <strong>没有任何属性和方法</strong>；</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> c: unknow = <span class="hljs-string">'una'</span>; 
<span class="hljs-keyword">let</span> d: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
d.toFixed(<span class="hljs-number">1</span>)

d = c; <span class="hljs-comment">// error unknow 仅能赋值给 unknow、any </span>
d.toFixed(<span class="hljs-number">1</span>); <span class="hljs-comment">// error unknow 没有任何属性和方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">对象类型</h3>
<h4 data-id="heading-24">内置对象类型</h4>
<p>在 JavaScript 中，有许多的内置对象，比如：<code>Object</code>、<code>Array</code>、<code>Date</code> ……，我们可以通过对象的 <code>构造函数</code> 或者 <code>类</code> 来进行标注。</p>
<blockquote>
<p><code>object</code> 表示<strong>非原始类型</strong>，也就是除 <code>number</code>，<code>string</code>，<code>boolean</code>，<code>symbol</code>，<code>null</code> 或 <code>undefined</code> 之外的类型。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">object</span> = &#123;&#125;; 
<span class="hljs-keyword">let</span> arr: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]; 
<span class="hljs-keyword">let</span> d1: <span class="hljs-built_in">Date</span> = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">自定义对象类型</h4>
<p>许多时候，我们可能需要自定义结构的对象。这个时候，我们可以通过以下方式来自定义对象：</p>
<ul>
<li><strong>字面量标注</strong></li>
<li><strong>接口</strong></li>
<li>定义 <strong>类</strong> 或者 <strong>构造函数</strong></li>
</ul>
<h5 data-id="heading-26">字面量标注</h5>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: &#123;<span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span>; age: <span class="hljs-built_in">number</span>&#125; = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'una'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;

a.username; <span class="hljs-comment">// ok </span>
a.age; <span class="hljs-comment">// ok </span>
a.gender;<span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点: 方便、直接；</li>
<li>缺点: <strong>不利于复用和维护</strong>；</li>
</ul>
<h5 data-id="heading-27">接口</h5>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person &#123; username: <span class="hljs-built_in">string</span>; age: <span class="hljs-built_in">number</span>; &#125;;
<span class="hljs-keyword">let</span> a: Person = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'una'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;

a.username; <span class="hljs-comment">// ok </span>
a.age; <span class="hljs-comment">// ok </span>
a.gender;<span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点: 复用性高；</li>
<li>缺点: <strong>接口只能作为类型标注使用，不能作为具体值</strong>，它只是一种抽象的结构定义，并不是实体，没有具体功能实现；</li>
</ul>
<h5 data-id="heading-28">类 与 构造函数</h5>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123; 
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> username: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">public</span> age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    
    &#125; 
&#125;

a.username; <span class="hljs-comment">// ok </span>
a.age; <span class="hljs-comment">// ok </span>
a.gender;<span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点: 功能相对强大，<strong>定义实体的同时也定义了对应的类型</strong>；</li>
<li>缺点: 复杂，比如<strong>只想约束某个函数接收的参数结构，没有必要去定一个类，使用接口会更加简单</strong>。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> AjaxOptions &#123; 
    <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>; 
    method: <span class="hljs-built_in">string</span>; 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">options: AjaxOptions</span>) </span>&#123; &#125; 

ajax(&#123;<span class="hljs-attr">url</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-29">包装对象</h5>
<p>这里说的包装对象其实就是 JavaScript 中的 <code>String</code>、<code>Number</code>、<code>Boolean</code>，我们知道 <code>string</code> 类型 和 <code>String</code> 类型并不一样，在 TypeScript 中也是一样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 简单类型字符串</span>
a = <span class="hljs-string">'1'</span>; 
a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'1'</span>); <span class="hljs-comment">// error String有的，string不一定有（对象有的，基础类型不一定有） </span>

<span class="hljs-keyword">let</span> b: <span class="hljs-built_in">String</span>; <span class="hljs-comment">// 字符串对象</span>
b = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'2'</span>);
b = <span class="hljs-string">'2'</span>; <span class="hljs-comment">// ok 和上面正好相反 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>对象类型是可扩展的，但是简单类型不可扩展， <code>string</code> -> <code>String</code> 会丢失数据</strong>。</p>
</blockquote>
<h3 data-id="heading-30">函数类型</h3>
<p>在 JavaScript 函数是非常重要的，在 TypeScript 也是如此。同样的，函数也有自己的类型标注格式：<code>函数名称( 参数1: 类型, 参数2: 类型... ): 返回值类型;</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123; 
    <span class="hljs-keyword">return</span> x + y; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">类型断言：不再检查</h2>
<p>有时候你会遇到这样的情况，你会比 TypeScript 更了解某个值的详细信息。</p>
<p><strong>通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”</strong>。</p>
<p>类型断言好比其它语言里的类型转换，但是不进行特殊的数据检查和解构。它没有运行时的影响，<strong>只是在编译阶段起作用</strong>。TypeScript会假设你已经进行了必须的检查。</p>
<p>类型断言有两种形式：</p>
<ul>
<li><strong><code>尖括号</code>语法</strong>：</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>someValue).length; <span class="hljs-comment">// 尖括号语法：<string>someValue</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong><code>as</code> 语法</strong>：</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (someValue <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length; <span class="hljs-comment">// as语法：someValue as string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两种形式是等价的。 至于使用哪个大多数情况下是凭个人喜好；然而，<strong>当你在 TypeScript 里使用 JSX 时，只有 as 语法断言是被允许的</strong>。</p>
<h1 data-id="heading-32">三、接口详解</h1>
<h2 data-id="heading-33">接口定义</h2>
<p>接口：对复杂的<strong>对象</strong>类型进行标注的一种方式。</p>
<p>接口中<strong>多个属性</strong>之间可以使用 <strong>逗号</strong> 或者 <strong>分号</strong> 进行分隔。</p>
<p>接口的基础语法定义结构特别简单：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; x: <span class="hljs-built_in">number</span>; y: <span class="hljs-built_in">number</span>; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码定义了一个类型，该类型包含两个属性，一个 <code>number</code> 类型的 <code>x</code> 和一个 <code>number</code> 类型的
<code>y</code>。我们可以通过这个接口来给一个数据进行类型标注：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> p1: Point = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">100</span> &#125;;
p1.x = <span class="hljs-number">200</span>; <span class="hljs-comment">// ok</span>
p1.z = <span class="hljs-number">100</span>; <span class="hljs-comment">// error 类型“Point”上不存在属性“z”</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：接口是一种 <strong>类型</strong> ，不能作为 <strong>值</strong> 使用。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; x: <span class="hljs-built_in">number</span>; y: <span class="hljs-built_in">number</span>; &#125;
<span class="hljs-keyword">let</span> p1 = Point; <span class="hljs-comment">// error 接口是一种类型，不能作为值使用</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">接口属性</h2>
<h3 data-id="heading-35">可选属性</h3>
<p>接口也可以定义<strong>可选</strong>的属性，通过 <code>?</code> 来进行标注</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; 
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>; 
    y: <span class="hljs-built_in">number</span>; 
    color?: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 可选属性，等同于 string | undefined</span>
&#125;

<span class="hljs-keyword">let</span> p1: Point = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">100</span> &#125;; <span class="hljs-comment">// color 属性是可选的，没有也不报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：</p>
<ul>
<li><strong>对可能存在的属性进行预定义</strong></li>
<li>可以<strong>捕获引用了不存在的属性时的错误</strong></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> p2: Point = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span> &#125;;
<span class="hljs-keyword">let</span> p3: Point = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">col</span>: <span class="hljs-string">'red'</span> &#125;; <span class="hljs-comment">// error 类型“Point”上不存在属性“col”</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">只读属性</h3>
<p>我们还可以通过 <code>readonly</code> 来标注属性为<strong>只读</strong>，只读属性<strong>除了初始化以外，是不能被再次赋值的</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; 
    <span class="hljs-keyword">readonly</span> x: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 只读属性</span>
    <span class="hljs-keyword">readonly</span> y: <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-keyword">let</span> p1: Point = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">100</span> &#125;;
p1.x = <span class="hljs-number">200</span>; <span class="hljs-comment">// error 只读属性除了初始化以外，是不能被再次赋值的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37"><code>ReadonlyArray<T></code> 类型</h4>
<p>TypeScript 还具有 <code>ReadonlyArray<T></code> 类型，它与 <code>Array<T></code> 相似，只是<strong>把所有可变方法去掉了，确保数组创建后再也不能被修改</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">let</span> ro: ReadonlyArray<<span class="hljs-built_in">number</span>> = a;
ro[<span class="hljs-number">0</span>] = <span class="hljs-number">12</span>; <span class="hljs-comment">// error 类型“readonly number[]”中的索引签名仅允许读取</span>
ro.push(<span class="hljs-number">5</span>); <span class="hljs-comment">// error 类型“readonly number[]”上不存在属性“push”</span>
ro.length = <span class="hljs-number">100</span>; <span class="hljs-comment">// error 无法分配到 "length" ，因为它是只读属性</span>
a = ro; <span class="hljs-comment">// error 类型 "readonly number[]" 为 "readonly"，不能分配给可变类型 "number[]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的最后一行，可以看到就算<strong>把整个ReadonlyArray赋值到一个普通数组也不可以</strong>。但是你可以用类型断言重写：</p>
<pre><code class="hljs language-ts copyable" lang="ts">a = ro <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>[]; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>readonly</code> vs <code>const</code></p>
<p>最简单判断该用 <code>readonly</code> 还是 <code>const</code> 的方法是<strong>看要把它做为变量使用还是做为一个属性：变量 <code>const</code>，属性 <code>readonly</code></strong>。</p>
</blockquote>
<h3 data-id="heading-38">任意属性（额外属性）</h3>
<p>有的时候，我们希望给一个接口添加<strong>任意属性</strong>，可以通过<strong>索引类型</strong>来实现。</p>
<p>TypeScript 支持两种索引签名：<strong>字符串索引</strong>和<strong>数字索引</strong>。</p>
<p>数字索引类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; 
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>; 
    y: <span class="hljs-built_in">number</span>; 
    [prop: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 任意属性，数字索引</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串索引类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; 
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>; 
    y: <span class="hljs-built_in">number</span>; 
    [prop: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 任意属性，字符串索引</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：索引签名参数类型必须为 <strong><code>string</code> 或 <code>number</code></strong> 之一，但两者<strong>可同时出现</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123; 
    [prop1: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>; 
    [prop2: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>数字索引是字符串索引的子类型</strong>。</p>
</blockquote>
<p>注意：当<strong>同时存在数字类型索引和字符串类型索引</strong>时，<strong><em>数字索引的值类型</em> 必须是 <em>字符串索引的 值类型 或 子类型</em></strong>。</p>
<blockquote>
<p>这是因为当使用 <code>number</code> 来索引时，JavaScript 会将它转换成 <code>string</code> 然后再去索引对象。 也就是说用 100（number）去索引等同于使用"100"（string）去索引，因此两者需要保持一致。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point1 &#123; 
    [prop1: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>;
    [prop2: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// error 当 同时存在数字类型索引和字符串类型索引 时，数字类型的值类型必须是字符串类型的值类型或子类型</span>
&#125;

<span class="hljs-keyword">interface</span> Point2 &#123; 
    [prop1: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>;
    [prop2: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// ok</span>
&#125;

<span class="hljs-keyword">interface</span> Point3 &#123; 
    [prop1: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">Object</span>; 
    [prop2: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">Date</span>; <span class="hljs-comment">// ok</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体使用可看以下案例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123;
    <span class="hljs-keyword">readonly</span> x: <span class="hljs-built_in">number</span>;
    <span class="hljs-keyword">readonly</span> y: <span class="hljs-built_in">number</span>;
    color?: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 可选属性 string | undefined</span>
    <span class="hljs-comment">// [key: string]: number; // 这么设置的话 `color?: string` 会报错。</span>
    <span class="hljs-comment">// color 属性明显也符合 [key: string] 的设置，但是两者类型不同，一个是 string， 一个是 number</span>
    [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span> |<span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 兼容设置，扩展属性为3种类型即可</span>
&#125;

<span class="hljs-keyword">let</span> p1: Point = &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">100</span>
&#125;
<span class="hljs-comment">// p1.x = 200; // error 只读属性，仅能在初始化时赋值</span>

p1.z = <span class="hljs-number">100</span>; <span class="hljs-comment">// 扩展可选属性 [key: string]</span>
p1[<span class="hljs-number">0</span>] = <span class="hljs-number">100</span>; <span class="hljs-comment">// 虽然0是number类型与可选属性设置不同，但是数字索引是字符串索引的子类型，所以不报错。但是反过来不行</span>
<span class="hljs-comment">// 等同于</span>
<span class="hljs-comment">// p1['0'] = 100;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，你可以将索引签名设置为只读，这样就防止了给索引赋值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ReadonlyStringArray &#123;
    <span class="hljs-keyword">readonly</span> [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">let</span> myArray: ReadonlyStringArray = [<span class="hljs-string">"Alice"</span>, <span class="hljs-string">"Bob"</span>];
myArray[<span class="hljs-number">2</span>] = <span class="hljs-string">"Mallory"</span>; <span class="hljs-comment">// error 只读属性，仅能在初始化时赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">接口合并</h2>
<p><strong>多个同名的接口合并成一个接口</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Box &#123; 
    <span class="hljs-attr">height</span>: <span class="hljs-built_in">number</span>; 
    width: <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-keyword">interface</span> Box &#123; 
    <span class="hljs-attr">scale</span>: <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-keyword">let</span> box: Box = &#123;<span class="hljs-attr">height</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">width</span>: <span class="hljs-number">6</span>, <span class="hljs-attr">scale</span>: <span class="hljs-number">10</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果合并的接口存在<strong>同名</strong>的<strong>非函数成员</strong>，则必须保证他们<strong>类型一致</strong>，否则编译报错；</li>
<li>接口中的同名函数则是采用重载（后续会讲）；</li>
</ul>
<h2 data-id="heading-40">使用接口描述函数</h2>
<p>我们还可以使用接口来描述一个函数</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IFunc &#123; 
    (a: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 单独描述函数，没有 key</span>
&#125;

<span class="hljs-keyword">let</span> fn: IFunc = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，<strong>如果使用接口来单独描述一个函数，是没 key 的</strong>。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IEventFunc &#123;
    (e: MouseEvent): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">on</span>(<span class="hljs-params">el: HTMLElement, evname: <span class="hljs-built_in">string</span>, callback: IEventFunc</span>) </span>&#123;
&#125;

<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>);
<span class="hljs-keyword">if</span> (div) &#123;
    on(div, <span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        e.clientX <span class="hljs-comment">// HTMLElement 不存在 clientX 属性，MouseEvent 才存在 clientX 属性</span>
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">使用接口描述类</h2>
<p>与 C# 或 Java 里接口的基本作用一样，TypeScript 也能够用它来明确的强制一个类去符合某种契约，使用 <code>implements</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ClockInterface &#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>接口描述了类的公共部分</strong>，而不是公共和私有两部分。 它不会帮你检查类是否具有某些私有成员。</p>
<p>具体讲解在 ts-笔记 面向对象编程 模块。</p>
<h1 data-id="heading-42">四、高级类型</h1>
<h2 data-id="heading-43">联合类型</h2>
<p><strong>联合类型</strong>也可以称为<strong>多选类型</strong>，当我们希望<strong>标注一个变量为多个类型之一</strong>时可以选择联合类型标注（<strong>或</strong>）。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">css</span>(<span class="hljs-params">ele: Element, attr: <span class="hljs-built_in">string</span>, value: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) </span>&#123; 
    <span class="hljs-comment">// ... </span>
&#125;

<span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.box'</span>); 
<span class="hljs-comment">// document.querySelector 方法返回值就是一个联合类型 </span>

<span class="hljs-keyword">if</span> (box) &#123; <span class="hljs-comment">// ts 会提示有 null 的可能性，加上判断更严谨 </span>
    css(box, <span class="hljs-string">'width'</span>, <span class="hljs-string">'100px'</span>); 
    css(box, <span class="hljs-string">'opacity'</span>, <span class="hljs-number">1</span>); 
    css(box, <span class="hljs-string">'opacity'</span>, [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]); <span class="hljs-comment">// 错误 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-44">交叉类型</h2>
<p><strong>交叉类型</strong>也可以称为<strong>合并类型</strong>，可以<strong>把多种类型合并到一起成为一种新的类型</strong>，对一个对象进行扩展（<strong>与</strong>）：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> o1 &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>, 
    <span class="hljs-attr">y</span>: <span class="hljs-built_in">string</span>
&#125;; 

<span class="hljs-keyword">interface</span> o2 &#123;
    <span class="hljs-attr">z</span>: <span class="hljs-built_in">number</span>
&#125;; 

<span class="hljs-keyword">let</span> o: o1 & o2 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-string">'2'</span>&#125;, &#123;<span class="hljs-attr">z</span>: <span class="hljs-number">100</span>&#125;);
<span class="hljs-built_in">console</span>.log(o);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小技巧：</p>
<blockquote>
<p>TypeScript 在编译过程中只会转换语法（比如扩展运算符，箭头函数等语法进行转换，对于API 是不会进行转换的（也没必要转换，而是引入一些扩展库进行处理的），如果我们的代码中<strong>使用了 target 中没有的 API</strong> ，则需要<strong>手动进行引入</strong>，默认情况下 TypeScript 会根据target 载入核心的类型库</p>
<p>**target 为 es5 时: ["dom", "es5", "scripthost"] **</p>
<p><strong>target 为 es6 时: ["dom", "es6", "dom.iterable", "scripthost"]</strong></p>
<p>如果代码中使用了这些默认载入库以外的代码，则可以<strong>通过 lib 选项来进行设置</strong></p>
<p><a href="http://www.typescriptlang.org/docs/handbook/compiler-options.html" target="_blank" rel="nofollow noopener noreferrer">www.typescriptlang.org/docs/handbo…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4359a487e224442d893154cee5c536dd~tplv-k3u1fbpfcp-watermark.image" alt="通过 lib 设置类型库" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-45">字面量类型</h2>
<p>有的时候，我们希望<strong>标注的不是某个类型，而是一个固定值</strong>，就可以使用<strong>字面量类型</strong>，配合联合类型会更有用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setPosition</span>(<span class="hljs-params">ele: Element, direction: <span class="hljs-string">'left'</span> | <span class="hljs-string">'top'</span> | <span class="hljs-string">'right'</span> | <span class="hljs-string">'bottom'</span></span>) </span>&#123;
    <span class="hljs-comment">// ... </span>
&#125;

box && setDirection(box, <span class="hljs-string">'bottom'</span>); <span class="hljs-comment">// ok </span>
box && setDirection(box, <span class="hljs-string">'hehe'</span>); <span class="hljs-comment">// error </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-46">类型别名</h2>
<p>有的时候类型标注比较复杂，这个时候我们可以类型标注起一个相对简单的名字，我们称之为 <strong>类型别名</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> dir = <span class="hljs-string">'left'</span> | <span class="hljs-string">'top'</span> | <span class="hljs-string">'right'</span> | <span class="hljs-string">'bottom'</span>; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setPosition</span>(<span class="hljs-params">ele: Element, direction: dir</span>) </span>&#123; 
    <span class="hljs-comment">// ... </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">使用类型别名定义函数类型</h3>
<p>这里需要注意一下，如果使用 type 来定义函数类型，和接口有点不太相同</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 使用类型别名定义函数类型</span>
<span class="hljs-keyword">type</span> callback = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span>; 
<span class="hljs-keyword">let</span> fn: callback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>) </span>&#123;&#125;; 

<span class="hljs-comment">// 或者直接 </span>
<span class="hljs-keyword">let</span> fn: <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span> = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">interface 与 type 的区别</h2>
<ul>
<li><code>interface</code>
<ul>
<li><strong>只能描述 <code>object</code> / <code>class</code> / <code>function</code> 的类型</strong></li>
<li><strong>同名 <code>interface</code> 自动合并</strong>，利于扩展</li>
</ul>
</li>
<li><code>type</code>
<ul>
<li><strong>能描述所有数据</strong></li>
<li><strong>不能重名</strong></li>
</ul>
</li>
</ul>
<h2 data-id="heading-49">类型推导</h2>
<p>每次都显式标注类型会比较麻烦，TypeScript 提供了一种更加方便的特性：类型推导。TypeScript 编译器会<strong>根据当前上下文自动的推导出对应的类型标注</strong>，这个过程发生在：</p>
<ul>
<li><strong>初始化变量</strong>；</li>
<li><strong>设置函数默认参数值</strong>；</li>
<li><strong>返回函数值</strong>；</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>; <span class="hljs-comment">// 自动推断 x 为 number </span>
x = <span class="hljs-string">'a'</span>; <span class="hljs-comment">// 不能将类型“"a"”分配给类型“number” </span>

<span class="hljs-comment">// 函数参数类型、函数返回值会根据对应的默认值和返回值进行自动推断 </span>
<span class="hljs-comment">// 相当于 function fn(a?: number): number</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a = <span class="hljs-number">1</span></span>) </span>&#123; <span class="hljs-keyword">return</span> a * a &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">类型断言</h2>
<p>有的时候，我们可能标注一个<strong>更加精确的类型</strong>（缩小类型标注范围），比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> img = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#img'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到 img 的类型为 <code>Element</code>，而 <code>Element</code> 类型其实只是元素类型的通用类型，如果我们去访问 <code>src</code> 这个属性是有问题的，我们需要把它的类型标注得更为精确：<code>HTMLImageElement</code> 类型，这个时候，我们就可以使用<strong>类型断言，它类似于一种 <code>类型转换</code></strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> img = <HTMLImageElement><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#img'</span>);
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">let</span> img = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#img'</span>) <span class="hljs-keyword">as</span> HTMLImageElement;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：断言只是一种预判，并<strong>不会对数据本身产生实际的作用</strong>，即：类似转换，但并非真的转换了。</p>
</blockquote>
<h1 data-id="heading-51">五、函数详解</h1>
<p>一个函数的标注包含：</p>
<ul>
<li>参数</li>
<li>返回值（如果函数<strong>没有返回任何值</strong>，你也必须指定返回值类型为 <strong><code>void</code></strong> 而不能留空）</li>
</ul>
<p>对于<strong>返回值</strong>，我们在函数和返回值类型之前使用 <strong><code>=></code></strong> 符号，使之清晰明了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 1. 直接标注</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
&#125;

<span class="hljs-comment">// 2. type 类型别名 标注函数</span>
<span class="hljs-keyword">let</span> fn2: <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span> = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
&#125;

<span class="hljs-comment">// 在赋值语句的一边指定了类型但是另一边没有类型的话，TypeScript编译器会自动识别出类型</span>
<span class="hljs-keyword">let</span> fn3: <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span> = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
&#125;

<span class="hljs-comment">// 3. type 类型别名 标注函数，拆分类型变量</span>
<span class="hljs-keyword">type</span> callback = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span>;

<span class="hljs-comment">// 类型别名 使用的参数名为 a，函数使用的参数名为 b</span>
<span class="hljs-comment">// 只要参数类型是匹配的，那么就认为它是有效的函数类型，而不在乎参数名是否正确</span>
<span class="hljs-keyword">let</span> fn4: callback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
&#125;

<span class="hljs-comment">// 4. interface 接口标注函数</span>
<span class="hljs-keyword">interface</span> ICallBack &#123;
    (a: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 使用接口单独描述函数，是没 key 的</span>
&#125;

<span class="hljs-keyword">let</span> fn5: ICallBack = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">c</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-52">函数参数</h2>
<h3 data-id="heading-53">可选参数</h3>
<p>通过参数名后面添加 <code>?</code> 来标注该参数是可选的。可选参数必须跟在必须参数后面。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>); 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">css</span>(<span class="hljs-params">el: HTMLElement, attr: <span class="hljs-built_in">string</span>, val?: <span class="hljs-built_in">any</span></span>) </span>&#123;&#125;
<span class="hljs-comment">// 错误写法：</span>
<span class="hljs-comment">// function css(el?: HTMLElement, attr: string, val: any) &#123;&#125;</span>

div && css( div, <span class="hljs-string">'width'</span>, <span class="hljs-string">'100px'</span> ); <span class="hljs-comment">// 设置 </span>
div && css( div, <span class="hljs-string">'width'</span> ); <span class="hljs-comment">// 获取 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">默认参数</h3>
<p>我们还可以给参数设置默认值：</p>
<ul>
<li><strong>有默认值的参数也是可选的</strong></li>
<li>设置了默认值的参数可以根据值<strong>自动推导类型</strong></li>
</ul>
<p>带默认值的参数不需要放在必须参数的后面。 <strong>如果带默认值的参数出现在必须参数前面，用户必须明确的传入  <code>undefined</code> 值来获得默认值</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sort1</span>(<span class="hljs-params">items: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>>, order = <span class="hljs-string">'desc'</span></span>) </span>&#123;&#125; 

sort1([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]); 

<span class="hljs-comment">// 也可以通过联合类型来限制取值，并设置默认值</span>
<span class="hljs-comment">// 'desc'|'asc' 联合类型，限制取值 </span>
<span class="hljs-comment">// = 'desc' 设置默认值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sort2</span>(<span class="hljs-params">items: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>>, order: <span class="hljs-string">'desc'</span>|<span class="hljs-string">'asc'</span> = <span class="hljs-string">'desc'</span></span>) </span>&#123;&#125; 

sort2([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]); <span class="hljs-comment">// ok </span>
sort2([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>], <span class="hljs-string">'asc'</span>); <span class="hljs-comment">// ok </span>
sort2([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>], <span class="hljs-string">'abc'</span>); <span class="hljs-comment">// error </span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sort3</span>(<span class="hljs-params">order: <span class="hljs-string">'desc'</span>|<span class="hljs-string">'asc'</span> = <span class="hljs-string">'desc'</span>, items: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>></span>) </span>&#123;&#125; 

sort3([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]); <span class="hljs-comment">// error</span>
sort3(<span class="hljs-literal">undefined</span>, [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]); <span class="hljs-comment">// ok</span>
sort3(<span class="hljs-string">'asc'</span>, [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]); <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">剩余参数</h3>
<p>剩余参数是一个<strong>数组</strong>，所以标注的时候一定要注意</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IObj &#123; 
    [key:<span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>; 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">merge</span>(<span class="hljs-params">target: IObj, ...others: <span class="hljs-built_in">Array</span><IObj></span>) </span>&#123; 
    <span class="hljs-keyword">return</span> others.reduce( <span class="hljs-function">(<span class="hljs-params">prev, currnet</span>) =></span> &#123; 
        prev = <span class="hljs-built_in">Object</span>.assign(prev, currnet); <span class="hljs-comment">// 合并参数</span>
        <span class="hljs-keyword">return</span> prev; 
    &#125;, target ); 
&#125;

<span class="hljs-comment">// target => &#123;x: 1&#125;, others => &#123;y: 2&#125;, &#123;z: 3&#125;</span>
<span class="hljs-keyword">let</span> newObj = merge(&#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;, &#123;<span class="hljs-attr">y</span>: <span class="hljs-number">2</span>&#125;, &#123;<span class="hljs-attr">z</span>: <span class="hljs-number">3</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-56">函数中的this</h2>
<h3 data-id="heading-57">普通函数</h3>
<p>对于普通函数而言，<code>this</code> 是会随着调用环境的变化而变化的，所以默认情况下，普通函数中的 <code>this</code> 被标注为 <code>any</code> ，但我们可以在函数的<strong>第一个参数位（它不占据实际参数位置）</strong> 上显式的<strong>标注 <code>this</code> 的类型</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> T &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>; 
    fn: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>; 
&#125;

<span class="hljs-keyword">let</span> obj1: T = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, 
    <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>)</span> &#123; 
        <span class="hljs-comment">// 普调函数中的 this 为 any 类型 </span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); 
        <span class="hljs-comment">// this.d // any 无检测，this.d 也不会报错</span>
        (<T><span class="hljs-built_in">this</span>).d <span class="hljs-comment">// 类型断言</span>
    &#125; 
&#125;

<span class="hljs-keyword">let</span> obj2: T = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, 
    <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: T, x: <span class="hljs-built_in">number</span></span>)</span> &#123; 
        <span class="hljs-comment">// 通过第一个参数位标注 this 的类型，它对实际参数不会有影响</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// 有类型提示</span>
    &#125; 
&#125;
obj2.fn(<span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-58">箭头函数</h3>
<p>箭头函数的 <code>this</code> 不能像普通函数那样进行标注，它的 <code>this</code> 标注类型<strong>取决于它所在的作用域 <code>this</code> 的标注类型</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> T &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>; 
    fn: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>; 
&#125;

<span class="hljs-keyword">let</span> obj2: T = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>, 
    <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: T</span>)</span> &#123; <span class="hljs-comment">// 箭头函数的this是固定的，取决于它所在作用域 this 的标注类型</span>
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123; 
            <span class="hljs-comment">// T </span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); 
        &#125; 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-59">函数重载</h2>
<p>有的时候，同一个函数会接收不同类型的参数返回不同类型的返回值，我们可以使用函数重载来实现。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showOrHide</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-built_in">string</span>, value: <span class="hljs-string">'block'</span> | <span class="hljs-string">'none'</span> | <span class="hljs-built_in">number</span></span>) </span>&#123;&#125;

<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>); 
<span class="hljs-keyword">if</span> (div) &#123; 
    showOrHide( div, <span class="hljs-string">'display'</span>, <span class="hljs-string">'none'</span> ); 
    showOrHide( div, <span class="hljs-string">'opacity'</span>, <span class="hljs-number">1</span> ); 
    
    <span class="hljs-comment">// error，虽然通过了标注，但这里明显是有问题的</span>
    <span class="hljs-comment">// 虽然通过联合类型能够处理同时接收不同类型的参数，但是多个参数之间是一种组合的模式，我们需要的应该是一种对应的关系 </span>
    showOrHide( div, <span class="hljs-string">'display'</span>, <span class="hljs-number">1</span> ); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数重载：</p>
<ul>
<li>函数重载，是<strong>合并</strong>而不是覆盖</li>
<li><strong>通过函数重载可以设置不同的参数的对应关系</strong></li>
<li><strong>重载函数类型只需要定义结构，不需要实体，类似接口</strong></li>
<li><strong>查找重载列表，尝试使用第一个重载定义，如果匹配的话就使用该定义</strong>。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 通过函数重载可以设置不同的参数对应关系</span>
<span class="hljs-comment">// 重载函数类型只需要定义结构，不需要实体，类似接口</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showOrHide</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-string">'display'</span>, value: <span class="hljs-string">'block'</span> | <span class="hljs-string">'none'</span></span>)</span>; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showOrHide</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-string">'opacity'</span>, value: <span class="hljs-built_in">number</span></span>)</span>; 
<span class="hljs-comment">// 注意，function showOrHide(ele: HTMLElement, attr: string, value: any) 并不是重载列表的一部分，而是具体的函数实现。</span>
<span class="hljs-comment">// 这里只有两个重载，以其它参数调用 showOrHide 会产生错误。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showOrHide</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-built_in">string</span>, value: <span class="hljs-built_in">any</span></span>) </span>&#123; 
    ele.style[attr] = value; 
&#125;

<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>); 
<span class="hljs-keyword">if</span> (div) &#123; 
    showOrHide( div, <span class="hljs-string">'display'</span>, <span class="hljs-string">'none'</span> ); 
    showOrHide( div, <span class="hljs-string">'opacity'</span>, <span class="hljs-number">1</span> ); 
    showOrHide( div, <span class="hljs-string">'display'</span>, <span class="hljs-number">1</span> );  <span class="hljs-comment">// error</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> PlainObject &#123; 
    [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">css</span>(<span class="hljs-params">ele: HTMLElement, attr: PlainObject</span>)</span>; <span class="hljs-comment">// 对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">css</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-built_in">string</span>, value: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>)</span>; <span class="hljs-comment">// 字符串</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">css</span>(<span class="hljs-params">ele: HTMLElement, attr: <span class="hljs-built_in">any</span>, value?: <span class="hljs-built_in">any</span></span>) </span>&#123; 
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> attr === <span class="hljs-string">'string'</span> && value) &#123; 
        ele.style[attr] = value; 
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> attr === <span class="hljs-string">'object'</span>) &#123; 
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> attr) &#123; 
            ele.style[attr] = attr[key]; 
        &#125; 
    &#125; 
&#125;

<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>); 
<span class="hljs-keyword">if</span> (div) &#123; 
    css(div, <span class="hljs-string">'width'</span>, <span class="hljs-string">'100px'</span>); 
    css(div, &#123; <span class="hljs-attr">width</span>: <span class="hljs-string">'100px'</span>&#125;);
    css(div, <span class="hljs-string">'width'</span>); <span class="hljs-comment">// value? 如果不使用重载，这里就会有问题了 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了让编译器能够选择正确的检查类型，它与JavaScript里的处理流程相似。 它<strong>查找重载列表，尝试使用第一个重载定义，如果匹配的话就使用这个</strong>。 因此，<strong>在定义重载的时候，一定要把最精确的定义放在最前面</strong>。</p></div>  
</div>
            