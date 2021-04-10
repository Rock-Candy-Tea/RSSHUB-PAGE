
---
title: '【Typescript小手册】配置文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4210'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 16:16:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=4210'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>Typescript 会根据配置文件来设定编译编译方式和细节，这篇文章来讲讲 Typescript 编译配置文件<strong>常用</strong>的选项的含义。它的编译选项非常多，更多内容可参考官方文档<a href="https://www.typescriptlang.org/tsconfig" target="_blank" rel="nofollow noopener noreferrer">Intro to the TSConfig Reference</a>。</p>
<p><em>对于初学者而言，不需要一开始就掌握这一部分内容，可以选择先跳过本章节。</em></p>
<p>我们可以通过<code>tsc --init</code>命令来让 Typescript 帮你生成一个配置文件，里面也所有配置项及相应的说明。</p>
<hr>
<h2 data-id="heading-1">配置</h2>
<p>按照功能，配置可以分为 9 类：</p>
<ul>
<li>文件</li>
<li>项目</li>
<li>约束</li>
<li>模块解析</li>
<li>代码映射</li>
<li>风格检查</li>
<li>命令行</li>
<li>观察</li>
<li>高级</li>
</ul>
<p>其中后 8 类属性编写在<code>compilerOptions</code>对象中。</p>
<hr>
<h3 data-id="heading-2">文件</h3>
<h4 data-id="heading-3">files</h4>
<p>类型：数组。</p>
<p>控制需要进行编译的文件路径，可以省略后缀名 ts。</p>
<p>示例：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"files"</span>: [<span class="hljs-string">"src/a.ts"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">include</h4>
<p>类型：数组。</p>
<p>控制需要进行编译的文件路径，与 files 不同的是可以使用通配符<code>*</code>（表示文件）、<code>**</code>（比较目录）和<code>?</code>（表示字符）。</p>
<p>示例：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"src/**/*"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表示编辑 src 目录下的所有 ts 文件。</p>
<p>如果没有配置 include，则编译工作目录下的所有 ts 文件，相当于设置为<code>["**/*"]</code>。</p>
<h4 data-id="heading-5">exclude</h4>
<p>类型：数组。默认值为：<code>["node_modules", "bower_components", "jspm_packages"]</code>和配置 outDir 指定的文件夹。</p>
<p>用于排除不需要编译的文件，可以使用与 include 相同的通配符。</p>
<p>exclude 只是对 include 的修饰，如果一个文件处在 files 列表、被<code>import</code>语句导入、被<code>/// <reference></code>语句指定或是类型文件的，exclude 配置无法将其排除。</p>
<h4 data-id="heading-6">extends</h4>
<p>类型：字符串。</p>
<p>值含义是另一个配置文件的路径，本配置文件会在继承被引入的配置文件的基础上融合。files、include、exclude 直接覆盖，references 无法继承。</p>
<h3 data-id="heading-7">项目</h3>
<h4 data-id="heading-8">target</h4>
<p>类型：字符串。默认：<code>ES3</code>。</p>
<p>控制生成的 js 文件所使用的 ES 版本。可选值可参考：<a href="https://www.typescriptlang.org/tsconfig/#target" target="_blank" rel="nofollow noopener noreferrer">tsconfig#target</a>，其中<code>ESNEXT</code>是个比较特殊的值，它表示使用当前 Typescript 版本支持的最新的 ES 版本。</p>
<h4 data-id="heading-9">lib</h4>
<p>类型：字符串数组。</p>
<p>不同的 Javascript 运行环境和 ES 版本有不同 API，lib 控制哪些 API 可以被使用，本质上是引入相对应的类型声明文件。</p>
<p>target 选项会影响 lib 的默认值，对应目标环境的 API 会被自动引入。</p>
<p>示例：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"lib"</span>: [<span class="hljs-string">"ES2015"</span>, <span class="hljs-string">"DOM"</span>]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样配置之后，在代码中就可以使用 ES2015 和 DOM 中的 API。如果想要查询 Typescript 内置对象的 API，可以查询 node_modules/typescript/lib 中的声明文件。</p>
<p>更多可配置的选项可见：<a href="https://www.typescriptlang.org/tsconfig#lib" target="_blank" rel="nofollow noopener noreferrer">tsconfig#lib</a></p>
<h4 data-id="heading-10">module</h4>
<p>类型：字符串。</p>
<p>控制编译结果的模块系统，常用的有：<code>CommonJS</code>和<code>ES6</code>。</p>
<p>target 选项会影响 module 的默认值。</p>
<h4 data-id="heading-11">outDir</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>默认情况下，生成的文件（包括 js 文件、d.ts 文件和代码映射文件）与 ts 源文件在同一目录下。设置了 outDir 后，输出文件被转移至对应目录，且目录结构仍然保留。输出目录中的第一层目录有选项 rootDir 控制。</p>
<h4 data-id="heading-12">rootDir</h4>
<p>类型：字符串。</p>
<p>当设置了 outDir，控制输出文件目录结构的根目录。默认值是所有非声明文件的 ts 文件的最长公共路径。</p>
<p>比如，如果源代码目录结构是这样的，设置了<code>"outDir": "out"</code>：</p>
<pre><code class="copyable">Workspace
├── tsconfig.json
├── src
│   ├── a.ts
│   ├── b.ts
│   ├── sub
│   │   ├── c.ts
├── types.d.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么输出结构为。</p>
<pre><code class="copyable">Workspace
├── out
│   ├── a.js
│   ├── b.js
│   ├── sub
│   │   ├── c.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果设置了 rootDir，那么输出文件夹中的第一层目录就是指定的目录。比如设置<code>"outDir": "./"</code>，那么输出结构为。</p>
<pre><code class="copyable">Workspace
├── out
│   ├── src
│   │    ├── a.js
│   │    ├── b.js
│   │    ├── sub
│   │    │   ├── c.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">outFile</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>设置一个文件路径，将所有代码打包到一个文件内。</p>
<p><em>要求 module 设置为<code>System</code>或<code>AMD</code>。</em></p>
<h4 data-id="heading-14">noEmit</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>设置为<code>true</code>后不会产生输出文件，结果值保存在内容中，通常在其它编译工具（入 Babel）中使用。</p>
<h4 data-id="heading-15">declaration</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>自动生成声明文件（.d.ts）。</p>
<h4 data-id="heading-16">sourceMap</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>生成代码映射文件。</p>
<h4 data-id="heading-17">importHelpers</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>在运行时引入辅助库。</p>
<p>Typescript 在编译<strong>模块文件</strong>中的新语法为旧语法（比如从 ES6 到 ES5）时，需要引入一些辅助函数。默认情况下，这些辅助函数被硬编码到使用处。为了压缩代码，开启 importHelpers 会使得辅助函数在运行时被引用，这样可以减少代码量。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copy</span>(<span class="hljs-params">arg: <span class="hljs-built_in">string</span>[]</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [...arg]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 ts 文件中使用了 ES6 的扩展运算符。当不使用 importHelpers 时，被编译成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-keyword">var</span> __spreadArrays =
  (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span>.__spreadArrays) ||
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> s = <span class="hljs-number">0</span>, i = <span class="hljs-number">0</span>, il = <span class="hljs-built_in">arguments</span>.length; i < il; i++) s += <span class="hljs-built_in">arguments</span>[i].length
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> r = <span class="hljs-built_in">Array</span>(s), k = <span class="hljs-number">0</span>, i = <span class="hljs-number">0</span>; i < il; i++) <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> a = <span class="hljs-built_in">arguments</span>[i], j = <span class="hljs-number">0</span>, jl = a.length; j < jl; j++, k++) r[k] = a[j]
    <span class="hljs-keyword">return</span> r
  &#125;
<span class="hljs-built_in">exports</span>.__esModule = <span class="hljs-literal">true</span>
<span class="hljs-built_in">exports</span>.copy = <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copy</span>(<span class="hljs-params">arg</span>) </span>&#123;
  <span class="hljs-keyword">return</span> __spreadArrays(arg)
&#125;
<span class="hljs-built_in">exports</span>.copy = copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果开启了<code>importHelpers</code>，被编译成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-built_in">exports</span>.__esModule = <span class="hljs-literal">true</span>
<span class="hljs-built_in">exports</span>.copy = <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
<span class="hljs-keyword">var</span> tslib_1 = <span class="hljs-built_in">require</span>(<span class="hljs-string">'tslib'</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copy</span>(<span class="hljs-params">arg</span>) </span>&#123;
  <span class="hljs-keyword">return</span> tslib_1.__spreadArrays(arg)
&#125;
<span class="hljs-built_in">exports</span>.copy = copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注意：使用此功能时，编译时和运行时环境都需要 tslib 库（NPM 安装）。</em></p>
<h4 data-id="heading-18">allowJs</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>允许在 ts 文件中引入 js 文件。</p>
<h4 data-id="heading-19">checkJs</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>检查在 ts 文件中引入的 js 文件的语法。</p>
<h4 data-id="heading-20">removeComments</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>删除注释。</p>
<h3 data-id="heading-21">约束</h3>
<h4 data-id="heading-22">strict</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>代码检查时遵循严格模式，同时开启：</p>
<ul>
<li>alwaysStrict</li>
<li>strictNullChecks</li>
<li>strictBindCallApply</li>
<li>strictFunctionTypes</li>
<li>strictPropertyInitialization</li>
<li>noImplicitAny</li>
<li>noImplicitThis</li>
</ul>
<h4 data-id="heading-23">alwaysStrict</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>使用严格模式编译 ts 文件，在生成的 js 文件中使用<code>'use strict'</code>。</p>
<h4 data-id="heading-24">onImplicitAny</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>禁止使用不明确的<code>any</code>类型。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">slice</span>(<span class="hljs-params">arg</span>) </span>&#123;
  <span class="hljs-keyword">return</span> arg.slice(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一段代码中，由于没有声明参数<code>arg</code>的类型，编译器推测<code>arg</code>为<code>any</code>类型。如果设置了<code>"noImplicit": true</code>，那就会报错，必须显示声明为<code>any</code>类型，即：<code>function slice(arg: any)</code>。</p>
<h4 data-id="heading-25">onImplicitThis</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>禁止<code>this</code>具有不明确的类型。</p>
<p>这种情况通常发生在高等函数中，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GetLog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>log</code>函数不是<code>GetLog</code>类的对象，而是由<code>GetLog</code>类方法生成的函数，其 this 指向并不是<code>GetLog</code>类的实例，而是全局对象或<code>undefined</code>，可能会违背这个函数的设计目的。</p>
<h4 data-id="heading-26">strictBindCallApply</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>限制函数的<code>call</code>，<code>apply</code>和<code>bind</code>方法的传参为函数的参数类型。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parse</span>(<span class="hljs-params">arg: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseInt</span>(arg)
&#125;

parse.call(<span class="hljs-literal">undefined</span>, <span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为<code>true</code>不是<code>string</code>类型值，所以编译器报错提示类型错误。</p>
<p>如果没有开启这个选项，那么编译器不会报错，且<code>call</code>，<code>apply</code>和<code>bind</code>方法的返回值为<code>any</code>类型。</p>
<h4 data-id="heading-27">strictFunctionTypes</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>严格的函数类型检查。</p>
<p>在未开启这个选项时，编译器会包容一些可能发生的联合类型错误，将错误的报告延迟到运行时。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log</span>(<span class="hljs-params">arg: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(arg.toLowerCase())
&#125;

<span class="hljs-keyword">type</span> StringOrNumberFunc = <span class="hljs-function">(<span class="hljs-params">arg: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>

<span class="hljs-keyword">let</span> f: StringOrNumberFunc = log
f(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于<code>log</code>只接受字符串类型的参数，但是<code>f</code>可以接受字符串或数字的参数，所以两者之间的参数类型没有完全匹配，如果将数字传入<code>f</code>函数就会报错。</p>
<p>设置了<code>"strictFunctionTypes": true</code>后可以避免这个问题，在编译阶段编译器会报告这一可能发生的错误。</p>
<p><em>注意：这一特性仅适用于<code>function</code>函数，不适用对象或类方法。</em></p>
<h4 data-id="heading-28">strictNullChecks</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>严格检查<code>null</code>和<code>undefined</code>。</p>
<p>在未开启这个选项时，<code>null</code>和<code>undefined</code>可以被其它类型的变量兼容，进而在运行时可能出错。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> array = []
<span class="hljs-keyword">let</span> target = array.find(<span class="hljs-function"><span class="hljs-params">a</span> =></span> a.name === <span class="hljs-string">'a'</span>)
<span class="hljs-built_in">console</span>.log(target.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>array</code>是空数组，<code>target</code>必定为<code>undefined</code>，所以在执行<code>target.name</code>时会报错。</p>
<p>如果设置了<code>"strictNullChecks": true</code>，这一问题在编译阶段会被报告出来。</p>
<h4 data-id="heading-29">strictPropertyInitialization</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>禁止在<code>class</code>声明中，类属性被声明但是没有被初始化（声明初始化或构造函数初始化）。</p>
<h3 data-id="heading-30">模块解析</h3>
<h4 data-id="heading-31">baseUrl</h4>
<p>类型：字符串。</p>
<p>引入非绝对地址模块的基地址。</p>
<h4 data-id="heading-32">moduleResolution</h4>
<p>类型：字符串。</p>
<p>控制模块的搜索策略，即对于引入 ts 的其它 ts 文件或模块，编译其如何找到其源文件。</p>
<p>可选值有<code>node</code>和<code>classic</code>，其中<code>classic</code>主要用于向后兼容，一般常用<code>node</code>。</p>
<p>可多细节可查看 Typescript 文档：<a href="https://www.typescriptlang.org/docs/handbook/module-resolution.html" target="_blank" rel="nofollow noopener noreferrer">module-resolution</a>。</p>
<h4 data-id="heading-33">esModuleInterop</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>辅助解决 ES 模块中引入 CommonJs 模块时的问题，主要针对 ESM 中有默认导出而 CommonJs 没有。</p>
<p>开启后 allowSyntheticDefaultImports 会被默认开启。</p>
<p>更多细节可查看 Typescript 文档：<a href="https://www.typescriptlang.org/tsconfig#esModuleInterop" target="_blank" rel="nofollow noopener noreferrer">tsconfig#esModuleInterop</a>。</p>
<h4 data-id="heading-34">allowSyntheticDefaultImports</h4>
<p>类型：布尔。默认：<code>false</code>。</p>
<p>将全部导出转换为默认导出。</p>
<p>如果一个模块，没有默认导出，那我们需要已这样的方式引入全部变量：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置了<code>"allowSyntheticDefaultImports": true</code>后，我们可以以默认导出的方式引入模块：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">paths</h4>
<p>类型：对象。</p>
<p>控制模块路径的重映射，也可以理解为路径别名。</p>
<p>示例：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"."</span>
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>:[<span class="hljs-string">"src/*"</span>],
      <span class="hljs-attr">"jquery"</span>: [<span class="hljs-string">"node_modules/jquery/dist/jquery"</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，一个条配置使得无论当前编写的文件在目录结构中的什么位置，或是与 src 中目标文件的相对关系如何，都可以直接使用<code>@</code>前缀且相对于 baseUrl 的路径来访问；第二条配置，显示的设置了 jquery 的位置。</p>
<p>使用这个选项前必须设置 baseUrl。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            