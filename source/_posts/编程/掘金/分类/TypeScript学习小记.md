
---
title: 'TypeScript学习小记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69219d266a3a4fb0a148e3c58dc5ed46~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 03:13:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69219d266a3a4fb0a148e3c58dc5ed46~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69219d266a3a4fb0a148e3c58dc5ed46~tplv-k3u1fbpfcp-watermark.image" alt="Typescript.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">一、TypeScript简介</h1>
<h2 data-id="heading-1">1.TypeScript简介</h2>
<p>1.TypeScript是JavaScript的超集。</p>
<p>2.TypeScript 其实就是类型化的 JavaScript，它不仅支持 JavaScript 的所有特性，还在 JavaScript 的基础上添加了静态类型注解扩展。</p>
<p>3.相较于JS而言，TS拥有了静态类型，更加严格的语法，更强大的功能；TS可以在代码执行前就完成代码的检查，减小了运行时异常的出现的几率；TS代码可以编译为任意版本的JS代码，可有效解决不同JS运行环境的兼容问题；同样的功能，TS的代码量要大于JS，但由于TS的代码结构更加清晰，变量类型更加明确，在后期代码的维护中TS却远远胜于JS。</p>
<p>4.TS代码需要通过编译器编译为JS，然后再交由JS解析器执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d438c771ddf04350be6e2ef24371592f~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2.TypeScript 开发环境搭建</h2>
<p>1.下载Node.js</p>
<ul>
<li>官网下载：<a href="https://nodejs.org/zh-cn/" target="_blank" rel="nofollow noopener noreferrer">nodejs.org/zh-cn/</a></li>
</ul>
<p>2.安装Node.js</p>
<ul>
<li>安装后输入 node -v 查看版本信息</li>
</ul>
<p>3.使用npm / yarn全局安装typescript</p>
<ul>
<li>
<p>打开命令行输入：npm install -g typescript / yarn global add typescript</p>
</li>
<li>
<p>安装后输入 tsc -v 查看版本信息</p>
</li>
</ul>
<p>4.创建一个ts文件</p>
<p>5.使用tsc对ts文件进行编译</p>
<ul>
<li>
<p>打开命令行，再进入ts文件所在目录</p>
</li>
<li>
<p>执行命令：tsc xxx.ts</p>
</li>
</ul>
<p>6.使用node命令运行ts编译后的js的文件</p>
<ul>
<li>node xxx.js</li>
</ul>
<p>7.全局安装直接在node端直接运行ts代码的ts-node，简化开发操作</p>
<ul>
<li>
<p>npm install -g ts-node / yarn global add ts-node</p>
</li>
<li>
<p>打开命令行，再进入ts文件所在目录</p>
</li>
<li>
<p>执行命令：ts-node xxx.ts</p>
</li>
</ul>
<h2 data-id="heading-3">3.VS Code开发TS的注意事项</h2>
<p>1.因为 VS Code 中内置了特定版本的 TypeScript 语言服务，所以它天然支持 TypeScript 语法解析和类型检测，且这个内置的服务与手动安装的 TypeScript 完全隔离。因此，<strong>VS Code 支持在内置和手动安装版本之间动态切换语言服务，从而实现对不同版本的 TypeScript 的支持</strong>。</p>
<p>2.如果当前应用目录中安装了与内置服务不同版本的 TypeScript，我们就可以点击 VS Code 底部工具栏的版本号信息，从而实现 “use VS Code's Version” 和 “use Workspace's Version” 两者之间的随意切换。</p>
<p>3.<strong>特别注意！</strong>：VS Code 默认使用自身内置的 TypeScript 语言服务版本，而在应用构建过程中，构建工具使用的却是应用路径下 node_modules/typescript 里的 TypeScript 版本。如果两个版本之间存在不兼容的特性，就会造成开发阶段和构建阶段静态类型检测结论不一致的情况，因此，我们务必将 VS Code 语言服务配置成使用当前工作区的 TypeScript 版本。</p>
<ul>
<li>工作区局部安装 typescript ：npm install typescript / yarn add typescript</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ea63a8050dc4bc7a110095f25563cb4~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">4.TypeScript初体验</h2>
<p>1.初始化typescript项目，生成配置文件</p>
<ul>
<li>
<p>打开命令行输入：tsc --init</p>
</li>
<li>
<p>生成tsconfg.json<strong>配置 TypeScript 的行为</strong></p>
</li>
<li>
<p>该配置将决定了 VS Code 语言服务如何对当前应用下的 TypeScript 代码进行类型检测。</p>
</li>
</ul>
<p>2.编写HelloWorld.ts文件</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">word: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(word);
&#125;
say(<span class="hljs-string">'Hello, World'</span>);

<span class="hljs-keyword">let</span> str1: <span class="hljs-built_in">string</span>
str1 = <span class="hljs-string">'hello'</span>
<span class="hljs-built_in">console</span>.log(str1);

<span class="hljs-keyword">let</span> str2: <span class="hljs-built_in">string</span> = <span class="hljs-string">'hello2'</span>
<span class="hljs-built_in">console</span>.log(str2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.执行tsc转译命令</p>
<ul>
<li>tsc HelloWorld.ts</li>
</ul>
<p><strong>注意：</strong> 指定转译的目标文件后，tsc 将<strong>忽略</strong>当前应用路径下的 tsconfig.json 配置，因此我们需要通过显式设定如下所示的参数，让 tsc 以严格模式检测并转译 TypeScript 代码。同时，我们可以给 tsc 设定一个 watch 参数监听文件内容变更，实时进行类型检测和代码转译。</p>
<ul>
<li>tsc HelloWorld.ts --strict --alwaysStrict false --watch</li>
</ul>
<p>4.直接使用 ts-node 运行 HelloWorld.ts</p>
<ul>
<li>ts-node HelloWorld.ts</li>
</ul>
<p>输出结果：</p>
<p>Hello, World</p>
<p>hello</p>
<p>hello2</p>
<p>5.<strong>注意：</strong> TypeScript 的类型注解旨在约束函数或者变量，在上面的例子中，我们就是通过约束一个示例函数来接收一个字符串类型（string）的参数。如果按如下写法，传入的参数不是string类型，则vscode会标红这个错误，并在问题（Problems）面板中显示错误信息</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">word: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(word);
&#125;
say(<span class="hljs-number">1</span>); <span class="hljs-comment">//变量类型不匹配错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">二、数据类型</h1>
<h2 data-id="heading-6">1.基本语法</h2>
<p>1.在语法层面，缺省类型注解（类型声明）的 TypeScript 与 JavaScript 完全一致。因此，我们可以把 TypeScript 代码的编写看作是为 JavaScript 代码添加类型注解（类型声明）。</p>
<ul>
<li>
<p>类型声明是TS非常重要的一个特点</p>
</li>
<li>
<p>通过类型声明可以指定TS中变量（参数、形参）的类型</p>
</li>
<li>
<p>指定类型后，当为变量赋值时，TS编译器会自动检查值是否符合类型声明，符合则赋值，否则报错</p>
</li>
<li>
<p>简而言之，类型声明给变量设置了类型，使得变量只能存储某种类型的值</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//1.缺省类型声明</span>
<span class="hljs-keyword">let</span> num = <span class="hljs-number">1</span>;
<span class="hljs-comment">//2.添加了类型声明</span>
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.语法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//1.字面量定义</span>
<span class="hljs-keyword">let</span> 变量名: 变量类型 = 初始化值;
<span class="hljs-comment">//2.先声明，后赋值</span>
<span class="hljs-keyword">let</span> 变量名: 变量类型;
变量名 = 变量值;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.<strong>自动类型判断</strong></p>
<ul>
<li>
<p>TS拥有自动的类型判断机制</p>
</li>
<li>
<p>当对变量的声明和赋值是同时进行时，TS编译器会自动判断变量的类型</p>
</li>
<li>
<p>所以如果你的变量的声明和赋值时同时进行的，可以省略掉类型声明</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//1.缺省类型声明</span>
<span class="hljs-keyword">let</span> num = <span class="hljs-number">1</span>;

简化写法：

<span class="hljs-comment">//2.添加了类型声明</span>
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在以下代码中，x1 的类型被推断为 number，将变量赋值给 number 类型的变量 x2 后，不会出现任何错误。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> x1 = <span class="hljs-number">42</span>; <span class="hljs-comment">// 推断出 x1 的类型是 number</span>
<span class="hljs-keyword">let</span> x2: <span class="hljs-built_in">number</span> = x1; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 TypeScript 中，具有初始化值的变量、有默认值的函数参数、函数返回的类型都可以根据<strong>上下文推断</strong>出来。比如我们能根据 return 语句推断函数返回的类型，如下代码所示：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** 根据参数的类型，推断出返回值的类型也是 number */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add1</span>(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-keyword">const</span> x1= add1(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// 推断出 x1 的类型也是 number</span>

<span class="hljs-comment">/** 推断参数 b 的类型是数字或者 undefined，返回值的类型也是数字 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add2</span>(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b = <span class="hljs-number">1</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-keyword">const</span> x2 = add2(<span class="hljs-number">1</span>);
<span class="hljs-keyword">const</span> x3 = add2(<span class="hljs-number">1</span>, <span class="hljs-string">'1'</span>); <span class="hljs-comment">// ts(2345) Argument of type '"1"' is not assignable to parameter of type 'number | undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述 add1 函数中，我们 return 了变量 a + b 的结果，因为 a 和 b 的类型为 number，所以函数返回类型被推断为 number。</p>
<p>当然，拥有默认值的函数参数的类型也能被推断出来。比如上述 add2 函数中，b 参数被推断为 number | undefined 类型，如果我们给 b 参数传入一个字符串类型的值，由于函数参数类型不一致，此时编译器就会抛出一个 ts(2345) 错误。</p>
<h2 data-id="heading-7">2.类型种类</h2>
















































































<table><thead><tr><th align="center">类型</th><th align="center">例子</th><th align="center">描述</th></tr></thead><tbody><tr><td align="center">number</td><td align="center">1, -33, 2.5</td><td align="center">任意数字</td></tr><tr><td align="center">string</td><td align="center">'hi', "hi", 模板字符串</td><td align="center">任意字符串</td></tr><tr><td align="center">boolean</td><td align="center">true、false</td><td align="center">布尔值true或false</td></tr><tr><td align="center">any</td><td align="center">*</td><td align="center">TS新增类型，任意类型</td></tr><tr><td align="center">unknown</td><td align="center">*</td><td align="center">TS新增类型，类型安全的any</td></tr><tr><td align="center">void</td><td align="center">空值（undefined）</td><td align="center">TS新增类型，没有值（或undefined）</td></tr><tr><td align="center">never</td><td align="center">没有值</td><td align="center">TS新增类型，不能是任何值</td></tr><tr><td align="center">object</td><td align="center">&#123;name:'孙悟空'&#125;</td><td align="center">任意的JS对象</td></tr><tr><td align="center">array</td><td align="center">[1,2,3]</td><td align="center">任意JS数组</td></tr><tr><td align="center">tuple</td><td align="center">[4,5]</td><td align="center">TS新增类型，元素，固定长度数组</td></tr><tr><td align="center">enum</td><td align="center">enum&#123;A, B&#125;</td><td align="center">TS中新增类型，枚举</td></tr><tr><td align="center">联合类型</td><td align="center">boolean | string</td><td align="center">TS中新增类型，为变量指定多个类型，可以是其中一种类型</td></tr><tr><td align="center">字面量声明</td><td align="center">let a: 10</td><td align="center">使用字面量代表类型</td></tr><tr><td align="center">交叉类型</td><td align="center">Colors & Rectangle</td><td align="center">通过&将两个或多个类型合并到一起</td></tr></tbody></table>
<h2 data-id="heading-8">3.字符串（string）</h2>
<p>1.使用<code>string</code>表示 JavaScript 中任意的字符串（包括模板字符串），且<strong>所有 JavaScript 支持的定义字符串的方法，我们都可以直接在 TypeScript 中使用。</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//先声明，后赋值</span>
<span class="hljs-keyword">let</span> firstname1: <span class="hljs-built_in">string</span>;
firstname1 = <span class="hljs-string">'Captain'</span>;
<span class="hljs-comment">//字符串字面量</span>
<span class="hljs-keyword">let</span> firstname: <span class="hljs-built_in">string</span> = <span class="hljs-string">'Captain'</span>;
<span class="hljs-comment">//显式类型转换</span>
<span class="hljs-keyword">let</span> familyname: <span class="hljs-built_in">string</span> = <span class="hljs-built_in">String</span>(<span class="hljs-string">'S'</span>);
<span class="hljs-comment">//模板字符串</span>
<span class="hljs-keyword">let</span> fullname: <span class="hljs-built_in">string</span> = <span class="hljs-string">`my name is <span class="hljs-subst">$&#123;firstname&#125;</span>.<span class="hljs-subst">$&#123;familyname&#125;</span>`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">4.数字（number）</h2>
<p>1.使用<code>number</code>类型表示 JavaScript 已经支持或者即将支持的十进制整数、浮点数，以及二进制数、八进制数、十六进制数。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** 十进制整数 */</span>
<span class="hljs-keyword">let</span> integer: <span class="hljs-built_in">number</span> = <span class="hljs-number">6</span>;
<span class="hljs-comment">/** 十进制整数 */</span>
<span class="hljs-keyword">let</span> integer2: <span class="hljs-built_in">number</span> = <span class="hljs-built_in">Number</span>(<span class="hljs-number">42</span>);
<span class="hljs-comment">/** 十进制浮点数 */</span>
<span class="hljs-keyword">let</span> decimal: <span class="hljs-built_in">number</span> = <span class="hljs-number">3.14</span>;
<span class="hljs-comment">/** 二进制整数 */</span>
<span class="hljs-keyword">let</span> binary: <span class="hljs-built_in">number</span> = <span class="hljs-number">0b1010</span>;
<span class="hljs-comment">/** 八进制整数 */</span>
<span class="hljs-keyword">let</span> octal: <span class="hljs-built_in">number</span> = <span class="hljs-number">0o744</span>;
<span class="hljs-comment">/** 十六进制整数 */</span>
<span class="hljs-keyword">let</span> hex: <span class="hljs-built_in">number</span> = <span class="hljs-number">0xf00d</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">5.布尔值（boolean）</h2>
<p>1.使用<code>boolean</code>表示 True 或者 False</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** TypeScript 真香 为 真 */</span>
<span class="hljs-keyword">let</span> TypeScriptIsGreat: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">true</span>;
 <span class="hljs-comment">/** TypeScript 太糟糕了 为 否 */</span>
<span class="hljs-keyword">let</span> TypeScriptIsBad: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">6.Symbol（ES6新增）</h2>
<p>1.可以通过<code>Symbol</code>构造函数，创建一个独一无二的标记；同时，还可以使用<code>symbol</code>表示如下代码所示的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> sym1: symbol = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">let</span> sym2: symbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'42'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">7.any</h2>
<p>1.any 指的是一个任意类型，它是官方提供的一个选择性绕过静态类型检测的作弊方式。</p>
<p>2.我们可以对被注解为 any 类型的变量进行任何操作，包括获取事实上并不存在的属性、方法，并且 TypeScript 还无法检测其属性是否存在、类型是否正确。</p>
<p>3.比如我们可以把任何类型的值赋值给 any 类型的变量，也可以把 any 类型的值赋值给任意类型（除 never 以外）的变量，如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> anything: <span class="hljs-built_in">any</span> = &#123;&#125;;
anything.doAnything(); <span class="hljs-comment">// 不会提示错误</span>
anything = <span class="hljs-number">1</span>; <span class="hljs-comment">// 不会提示错误</span>
anything = <span class="hljs-string">'x'</span>; <span class="hljs-comment">// 不会提示错误</span>
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = anything; <span class="hljs-comment">// 不会提示错误</span>
<span class="hljs-keyword">let</span> str: <span class="hljs-built_in">string</span> = anything; <span class="hljs-comment">// 不会提示错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.如果我们不想花费过高的成本为复杂的数据添加类型注解，或者已经引入了缺少类型注解的第三方组件库，这时就可以把这些值全部注解为 any 类型，并告诉 TypeScript 选择性地忽略静态类型检测。</p>
<p>5.尤其是在将一个基于 JavaScript 的应用改造成 TypeScript 的过程中，我们不得不借助 any 来选择性添加和忽略对某些 JavaScript 模块的静态类型检测，直至逐步替换掉所有的 JavaScript。</p>
<p>6.any 类型会在对象的调用链中进行传导，即所有 any 类型的任意属性的类型都是 any，如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> anything: <span class="hljs-built_in">any</span> = &#123;&#125;;
<span class="hljs-keyword">let</span> z = anything.x.y.z; <span class="hljs-comment">// z 类型是 any，不会提示错误</span>
z(); <span class="hljs-comment">// 不会提示错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从长远来看，使用 any 绝对是一个坏习惯。如果一个 TypeScript 应用中充满了 any，此时静态类型检测基本起不到任何作用，也就是说与直接使用 JavaScript 没有任何区别。<strong>因此，除非有充足的理由，否则我们应该尽量避免使用 any ，并且开启禁用隐式 any 的设置。</strong></p>
<h2 data-id="heading-13">8.unknown（类型安全的any）</h2>
<p>1.主要用来描述类型并不确定的变量</p>
<p>2.比如在多个 if else 条件分支场景下，它可以用来接收不同条件下类型各异的返回值的临时变量，如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> result: unknown;
<span class="hljs-keyword">if</span> (x) &#123;
  result = x();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (y) &#123;
  result = y();
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.与 any 不同的是，unknown 在类型上更安全。比如我们可以将任意类型的值赋值给 unknown，但 unknown 类型的值只能赋值给 unknown 或 any，如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> result: unknown;
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = result; <span class="hljs-comment">// 提示 ts(2322)</span>
<span class="hljs-keyword">let</span> anything: <span class="hljs-built_in">any</span> = result; <span class="hljs-comment">// 不会提示错误</span>
<span class="hljs-keyword">let</span> notSure: unknown = <span class="hljs-number">4</span>;
notSure = <span class="hljs-string">'hello'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.使用 unknown 后，TypeScript 会对它做类型检测。但是，如果不缩小类型（Type Narrowing），我们对 unknown 执行的任何操作都会出现如下所示错误：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> result: unknown;
result.toFixed(); <span class="hljs-comment">// 提示 ts(2571)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.<strong>而所有的类型缩小手段对 unknown 都有效</strong>，如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> result: unknown;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> result === <span class="hljs-string">'number'</span>) &#123; <span class="hljs-comment">//类型守卫</span>
  result.toFixed(); <span class="hljs-comment">// 此处 hover result 提示类型是 number，不会提示错误</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">9.void、undefined、null（用的少）</h2>
<p>1.它仅适用于表示没有返回值的函数。即如果该函数没有返回值，那它的类型就是 void。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span></span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.在 strict 模式下，声明一个 void 类型的变量几乎没有任何实际用处，因为我们不能把 void 类型的变量值再赋值给除了 any 和 unkown 之外的任何类型变量。</p>
<p>3.undefined 类型 和 null 类型，它们是 TypeScript 值与类型关键字同名的唯二例外。</p>
<p>undefined 的最大价值主要体现在接口类型上，它表示一个可缺省、未定义的属性。</p>
<p>4.我们可以把 undefined 值或类型是 undefined 的变量赋值给 void 类型变量，反过来，类型是 void 但值是 undefined 的变量不能赋值给 undefined 类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> undeclared: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">let</span> unusable: <span class="hljs-built_in">void</span> = <span class="hljs-literal">undefined</span>;
unusable = undeclared; <span class="hljs-comment">// ok</span>
undeclared = unusable; <span class="hljs-comment">// ts(2322)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">10.never（用的少）</h2>
<p>1.never 表示永远不会发生值的类型，这里我们举一个实际的场景进行说明。</p>
<p>2.首先，我们定义一个统一抛出错误的函数，代码示例如下（圆括号后 : + 类型注解 ，表示函数返回值的类型）</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ThrowError</span>(<span class="hljs-params">msg: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(msg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上函数因为永远不会有返回值，所以它的返回值类型就是 never。</p>
<p>3.同样，如果函数代码中是一个死循环，那么这个函数的返回值类型也是 never，如下代码所示。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">InfiniteLoop</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.never 是所有类型的子类型，它可以给所有类型赋值，但是反过来，除了 never 自身以外，其他类型（包括 any 在内的类型）都不能为 never 类型赋值。如下代码所示。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> Unreachable: <span class="hljs-built_in">never</span>;
Unreachable = <span class="hljs-number">1</span>; <span class="hljs-comment">// ts(2322)</span>
Unreachable = <span class="hljs-string">'string'</span>; <span class="hljs-comment">// ts(2322)</span>
Unreachable = <span class="hljs-literal">true</span>; <span class="hljs-comment">// ts(2322)</span>
<span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> = Unreachable; <span class="hljs-comment">// ok</span>
<span class="hljs-keyword">let</span> str: <span class="hljs-built_in">string</span> = Unreachable; <span class="hljs-comment">// ok</span>
<span class="hljs-keyword">let</span> bool: <span class="hljs-built_in">boolean</span> = Unreachable; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">11.object（用的少）</h2>
<p>1.object 类型表示非原始类型的类型，即非 number、string、boolean、bigint、symbol、null、undefined 的类型。</p>
<p>示例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> obj: <span class="hljs-built_in">object</span> = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.一个应用场景是用来表示 Object.create 的类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">o: <span class="hljs-built_in">object</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">any</span></span>;
create(&#123;&#125;); <span class="hljs-comment">// ok</span>
create(<span class="hljs-function">() =></span> <span class="hljs-literal">null</span>); <span class="hljs-comment">// ok</span>
create(<span class="hljs-number">2</span>); <span class="hljs-comment">// ts(2345)</span>
create(<span class="hljs-string">'string'</span>); <span class="hljs-comment">// ts(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">12.数组类型（Array）</h2>
<p>1.第一种定义方式：直接使用 [] 的形式定义数组类型，语法：类型[]</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** 子元素是数字类型的数组 */</span>
<span class="hljs-keyword">let</span> arrayOfNumber: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-comment">/** 子元素是字符串类型的数组 */</span>
<span class="hljs-keyword">let</span> arrayOfString: <span class="hljs-built_in">string</span>[] = [<span class="hljs-string">'x'</span>, <span class="hljs-string">'y'</span>, <span class="hljs-string">'z'</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.第二种定义方式：使用 Array 泛型定义数组类型，语法：Array<类型></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** 子元素是数字类型的数组 */</span>
<span class="hljs-keyword">let</span> arrayOfNumber: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-comment">/** 子元素是字符串类型的数组 */</span>
<span class="hljs-keyword">let</span> arrayOfString: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">string</span>> = [<span class="hljs-string">'x'</span>, <span class="hljs-string">'y'</span>, <span class="hljs-string">'z'</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两种定义数组类型的方式虽然本质上没有任何区别，但是更推荐使用 [] 这种形式来定义。<strong>一方面可以避免与 JSX 的语法冲突，另一方面可以减少不少代码量</strong>。</p>
<p>3.如果我们明确指定了数组元素的类型，以下所有操作都将因为不符合类型约定而提示错误。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> arrayOfNumber: <span class="hljs-built_in">number</span>[] = [<span class="hljs-string">'x'</span>, <span class="hljs-string">'y'</span>, <span class="hljs-string">'z'</span>]; <span class="hljs-comment">// 提示 ts(2322)</span>
arrayOfNumber[<span class="hljs-number">3</span>] = <span class="hljs-string">'a'</span>; <span class="hljs-comment">// 提示 ts(2322)</span>
arrayOfNumber.push(<span class="hljs-string">'b'</span>); <span class="hljs-comment">// 提示 ts(2345)</span>
<span class="hljs-keyword">let</span> arrayOfString: <span class="hljs-built_in">string</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]; <span class="hljs-comment">// 提示 ts(2322)</span>
arrayOfString[<span class="hljs-number">3</span>] = <span class="hljs-number">1</span>; <span class="hljs-comment">// 提示 ts(2322)</span>
arrayOfString.push(<span class="hljs-number">2</span>); <span class="hljs-comment">// 提示 ts(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">13.元组类型（Tuple）</h2>
<p>1.元组就是固定长度的数组，它最重要的特性是可以限制数组元素的个数和类型，它特别适合用来实现多值返回。应用场景如react hooks的useState。</p>
<p>2.语法：[类型, 类型, 类型]</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> h: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>];
h = [<span class="hljs-string">'hello'</span>, <span class="hljs-number">123</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">14.联合类型</h2>
<p>1.TypeScript 中支持一个变量可以赋予多种不同的变量类型，多个变量类型使用 <code>|</code> 分隔。</p>
<p>2.联合类型作为函数参数时，在函数内vscode可以直接提示出共有属性，但不能提示出私有属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> num: <span class="hljs-built_in">number</span> | <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span>;
num = <span class="hljs-number">3</span>;
<span class="hljs-built_in">console</span>.log(num);
num = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">console</span>.log(num);
num = <span class="hljs-literal">undefined</span>;
<span class="hljs-built_in">console</span>.log(num);
num = <span class="hljs-string">'ff'</span> <span class="hljs-comment">//报错</span>


<span class="hljs-keyword">interface</span> Bird &#123;
    <span class="hljs-attr">fly</span>: <span class="hljs-built_in">Boolean</span>;
    sing: <span class="hljs-function">() =></span> &#123;&#125;
&#125;

<span class="hljs-keyword">interface</span> Dog &#123;
    <span class="hljs-attr">fly</span>: <span class="hljs-built_in">Boolean</span>;
    dark: <span class="hljs-function">() =></span> &#123;&#125;
&#125;

<span class="hljs-comment">// animal 参数可以是 Bird 或 Dog，语法提示可以直接提示出共有属性 fly，但是不能直接提示出 sing 和 dark。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trainAnimal</span>(<span class="hljs-params">animal: Bird | Dog</span>) </span>&#123;
    animal.fly
    <span class="hljs-comment">// animal.dark() 这里直接报错，因为不能确保 animal 包含 dark 方法。</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">15.交叉类型</h2>
<p>1.通过<code>'&'</code> 将两个或多个类型合并到一起</p>
<p>2.交叉类型作为函数参数时，在函数内可以获取合并类型的所有属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 交叉类型</span>
<span class="hljs-keyword">interface</span> Colors &#123;
    <span class="hljs-attr">red</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">interface</span> Rectangle &#123;
    <span class="hljs-attr">height</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">width</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">area</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">// param 参数可以访问类型 Colors 和 Rectangle 所有属性</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">param: Colors & Rectangle</span>) </span>&#123;
    param.height = <span class="hljs-number">2</span>
    param.width = <span class="hljs-number">3</span>
    param.red = <span class="hljs-string">'red'</span>
    param.area = (): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
        <span class="hljs-keyword">return</span> param.height * param.width
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">16.字面量声明（限制变量的范围）</h2>
<p>1.使用字面量去指定变量的类型，通过字面量可以确定变量的取值范围</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> a: <span class="hljs-number">10</span>;
a = <span class="hljs-number">10</span>;
a = <span class="hljs-number">11</span>; <span class="hljs-comment">//报错</span>

<span class="hljs-keyword">let</span> color: <span class="hljs-string">'red'</span> | <span class="hljs-string">'blue'</span> | <span class="hljs-string">'black'</span>;
color = <span class="hljs-string">'red'</span>;
color = <span class="hljs-string">'yellow'</span>; <span class="hljs-comment">//报错</span>

<span class="hljs-keyword">let</span> num: <span class="hljs-number">1</span> | <span class="hljs-number">2</span> | <span class="hljs-number">3</span> | <span class="hljs-number">4</span> | <span class="hljs-number">5</span>;
num = <span class="hljs-number">1</span>;
num = <span class="hljs-number">22</span>; <span class="hljs-comment">//报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.&#123;&#125; 用来指定对象中可以包含哪些属性</p>
<ul>
<li>
<p>语法：&#123;属性名:属性值,属性名:属性值&#125;</p>
</li>
<li>
<p>在属性名后边加上?，表示属性是可选的</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> b: &#123;<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, age?: <span class="hljs-built_in">number</span>&#125;;
b = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'孙悟空'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;;
b = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'孙悟空'</span>&#125;;
<span class="hljs-built_in">console</span>.log(b);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.[propName: string]: any 表示任意类型的属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> c: &#123;<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>&#125;;
c = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'猪八戒'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">'男'</span>&#125;;
<span class="hljs-built_in">console</span>.log(c);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">17.enum 枚举</h2>
<p>1.事先考虑到某一变量可能取的值，尽量用自然语言中含义清楚的单词来表示它的每一个值，这种方法称为枚举方法，用这种方法定义的类型称枚举类型。</p>
<p>2.语法</p>
<pre><code class="copyable">enum 枚举名 &#123;
    标识符[= 整型常数/字符串],
    标识符[= 整型常数/字符串], 
    ...
    标识符[= 整型常数/字符串],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.示例1：如果标识符没有赋值，它的值就是下标。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">enum</span> Flag &#123;
    success,
    error,
    overtime
&#125;;
<span class="hljs-keyword">let</span> s: Flag = Flag.overtime;
<span class="hljs-built_in">console</span>.log(s); <span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.示例2：如果标识符已经赋值，它的值就是被赋的值。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">enum</span> Flag &#123;
    success = <span class="hljs-number">200</span>,
    error = <span class="hljs-number">404</span>,
    overtime = <span class="hljs-number">500</span>
&#125;;
<span class="hljs-keyword">let</span> s: Flag = Flag.overtime;
<span class="hljs-built_in">console</span>.log(s); <span class="hljs-comment">//500</span>

<span class="hljs-built_in">enum</span> Direction &#123;
    Up = <span class="hljs-string">"UP"</span>,
    Down = <span class="hljs-string">"DOWN"</span>,
    Left = <span class="hljs-string">"LEFT"</span>,
    Right = <span class="hljs-string">"RIGHT"</span>
&#125;
<span class="hljs-keyword">let</span> d: Direction = Direction.Up;
<span class="hljs-built_in">console</span>.log(d); <span class="hljs-comment">//UP</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.示例3：如果标识符没有赋值，它的值就是下标，如果从中间突然指定了一个值，那么它之后的值都会从当前值开始重新计算。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">enum</span> Flag &#123;
    success,
    error = <span class="hljs-number">100</span>,
    overtime
&#125;;
<span class="hljs-keyword">let</span> s: Flag = Flag.overtime;
<span class="hljs-built_in">console</span>.log(s); <span class="hljs-comment">//101</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">18.类型断言（Type Assertion）</h2>
<p>1.有些情况下，变量的类型对于我们来说是很明确，但是TS编译器却并不清楚，此时，可以通过类型断言来告诉编译器变量的类型，断言有两种形式：</p>
<ul>
<li>第一种：语法：变量 as 类型</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> someValue: unknown = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (someValue <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二种：语法：<类型>变量</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> someValue: unknown = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>someValue).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.示例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> arrayNumber: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> greaterThan2: <span class="hljs-built_in">number</span> = arrayNumber.find(<span class="hljs-function"><span class="hljs-params">num</span> =></span> num > <span class="hljs-number">2</span>); <span class="hljs-comment">// 提示 ts(2322)</span>

<span class="hljs-keyword">const</span> arrayNumber: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> greaterThan2: <span class="hljs-built_in">number</span> = arrayNumber.find(<span class="hljs-function"><span class="hljs-params">num</span> =></span> num > <span class="hljs-number">2</span>) <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两种方式虽然没有任何区别，但是尖括号格式会与 JSX 产生语法冲突，因此我们更推荐使用 as 语法。</p>
<p>3.<strong>非空断言</strong>，即在值（变量、属性）的后边添加 '!' 断言操作符，它可以用来排除值为 null、undefined 的情况，具体示例如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> mayNullOrUndefinedOrString: <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span> | <span class="hljs-built_in">string</span>;
mayNullOrUndefinedOrString!.toString(); <span class="hljs-comment">// ok</span>
mayNullOrUndefinedOrString.toString(); <span class="hljs-comment">// ts(2531)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对于非空断言来说，我们同样应该把它视作和 any 一样危险的选择。</strong></p>
<p>在复杂应用场景中，如果我们使用非空断言，就无法保证之前一定非空的值，比如页面中一定存在 id 为 feedback 的元素，数组中一定有满足 > 2 条件的数字，这些都不会被其他人改变。而一旦保证被改变，错误只会在运行环境中抛出，而静态类型检测是发现不了这些错误的。</p>
<p>所以，我们建议使用<strong>类型守卫来代替非空断言</strong>，比如如下所示的条件判断：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> mayNullOrUndefinedOrString: <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span> | <span class="hljs-built_in">string</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> mayNullOrUndefinedOrString === <span class="hljs-string">'string'</span>) &#123; <span class="hljs-comment">//类型守卫</span>
  mayNullOrUndefinedOrString.toString(); <span class="hljs-comment">// ok</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">19.类型别名</h2>
<p>1.类型别名用来给一个类型起个新名字。</p>
<p>2.类型别名常用于联合类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//声明一个联合类型的别名</span>
<span class="hljs-keyword">type</span> myType = <span class="hljs-number">1</span> | <span class="hljs-number">2</span> | <span class="hljs-number">3</span> | <span class="hljs-number">4</span> | <span class="hljs-number">5</span>;
<span class="hljs-keyword">let</span> k: myType;
k = <span class="hljs-number">2</span>;

<span class="hljs-comment">//声明一个字符串和函数的别名</span>
<span class="hljs-keyword">type</span> Name = <span class="hljs-built_in">string</span>;
<span class="hljs-keyword">type</span> NameResolver = <span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>;
<span class="hljs-keyword">type</span> NameOrResolver = Name | NameResolver;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">n: NameOrResolver</span>): <span class="hljs-title">Name</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> n === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> n;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> n();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25">二、函数（function）</h1>
<h2 data-id="heading-26">1.函数定义</h2>
<p>函数定义的形式有2种：</p>
<p>1.函数声明式</p>
<p>2.函数表达式</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//函数声明式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> 函数名(<span class="hljs-params">参数列表</span>): 返回值类型 </span>&#123;
    函数体 ...
    [<span class="hljs-keyword">return</span> 返回值;]
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> x + y;
&#125;

<span class="hljs-comment">//函数表达式</span>
<span class="hljs-keyword">let</span> 函数名 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">参数列表</span>): 返回值类型 </span>&#123;
    函数体 ...
    [<span class="hljs-keyword">return</span> 返回值;]
&#125;;
<span class="hljs-keyword">let</span> sum2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> x + y;
&#125;;
<span class="hljs-comment">//类型推断-箭头函数写法</span>
<span class="hljs-keyword">const</span> add = (a: <span class="hljs-built_in">number</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注：</strong> TS中的函数是考虑参数的类型和个数的！如下代码，多传与少传参数，传的参数类型不匹配都会报错！</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> x + y;
&#125;
sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">//报错</span>
sum(<span class="hljs-number">1</span>); <span class="hljs-comment">//报错</span>
sum(<span class="hljs-number">1</span>, <span class="hljs-string">'a'</span>); <span class="hljs-comment">//报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">2.函数返回值类型</h2>
<p>TS 中，如果显式声明函数的返回值类型为 undfined，将会报错。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">undefined</span> </span>&#123; <span class="hljs-comment">// ts(2355) </span>
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时需要使用 void 类型来表示函数没有返回值的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
&#125;
fn1().doSomething(); <span class="hljs-comment">// ts(2339)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">3.函数类型先声明，再定义</h2>
<p>1.一般写法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//一般写法</span>
<span class="hljs-keyword">let</span> add: (a: <span class="hljs-built_in">number</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 函数类型声明</span>
add = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>&#123;
<span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.使用类似定义<strong>箭头函数</strong>的语法，来表示函数类型的参数和返回值类型，此时<code>=></code><strong>用来表示函数的声明，其左侧是函数的参数类型，右侧是函数的返回值类型；而 ES6 中的</strong><code>=></code>是函数的实现。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//1.简写+箭头函数</span>
<span class="hljs-keyword">let</span> add: <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span> = (a: <span class="hljs-built_in">number</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
<span class="hljs-keyword">return</span> a + b;
&#125;

<span class="hljs-comment">//2.类型别名+箭头函数+缺省类型类型声明</span>
<span class="hljs-keyword">type</span> Adder = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 函数类型声明</span>
<span class="hljs-keyword">const</span> add: Adder = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a + b; <span class="hljs-comment">// ES6 箭头函数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">4.可缺省和可推断的返回值类型</h2>
<p>一般情况下，TypeScript 中的函数返回值类型是可以缺省和推断出来的。如下示例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computeTypes</span>(<span class="hljs-params">one: <span class="hljs-built_in">string</span>, two: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> nums = [two];
  <span class="hljs-keyword">const</span> strs = [one];
  <span class="hljs-keyword">return</span> &#123;
    nums,
    strs
  &#125; <span class="hljs-comment">// 返回 &#123; nums: number[]; strs: string[] &#125; 的类型 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">5.可选参数</h2>
<p>1.使用 <code>?</code> 表示可选的参数</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">firstName: <span class="hljs-built_in">string</span>, lastName?: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (lastName) &#123;
        <span class="hljs-keyword">return</span> firstName + <span class="hljs-string">' '</span> + lastName;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> firstName;
    &#125;
&#125;
<span class="hljs-keyword">let</span> tomcat = buildName(<span class="hljs-string">'Tom'</span>, <span class="hljs-string">'Cat'</span>);
<span class="hljs-keyword">let</span> tom = buildName(<span class="hljs-string">'Tom'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> 可选参数必须接在必需参数后面，即可选参数必须配置到参数的最后面。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">firstName?: <span class="hljs-built_in">string</span>, lastName: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (firstName) &#123;
        <span class="hljs-keyword">return</span> firstName + <span class="hljs-string">' '</span> + lastName;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> lastName;
    &#125;
&#125;
<span class="hljs-keyword">let</span> tomcat = buildName(<span class="hljs-string">'Tom'</span>, <span class="hljs-string">'Cat'</span>);
<span class="hljs-keyword">let</span> tom = buildName(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'Tom'</span>);
error TS1016: A required parameter cannot follow an optional parameter.
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">6.默认参数</h2>
<p>1.TS 会将添加了默认值的参数识别为可选参数，显式声明参数的类型，不过，此时的默认参数只起到参数默认值的作用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">firstName: <span class="hljs-built_in">string</span>, lastName: <span class="hljs-built_in">string</span> = <span class="hljs-string">'Cat'</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> firstName + <span class="hljs-string">' '</span> + lastName;
&#125;
<span class="hljs-keyword">let</span> tomcat = buildName(<span class="hljs-string">'Tom'</span>, <span class="hljs-string">'Cat'</span>);
<span class="hljs-keyword">let</span> tom = buildName(<span class="hljs-string">'Tom'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时就不受「可选参数必须接在必需参数后面」的限制了：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">firstName: <span class="hljs-built_in">string</span> = <span class="hljs-string">'Tom'</span>, lastName: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> firstName + <span class="hljs-string">' '</span> + lastName;
&#125;
<span class="hljs-keyword">let</span> tomcat = buildName(<span class="hljs-string">'Tom'</span>, <span class="hljs-string">'Cat'</span>);
<span class="hljs-keyword">let</span> cat = buildName(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'Cat'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.缺省声明参数的类型，TS 会根据函数的默认参数的类型来推断函数参数的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log</span>(<span class="hljs-params">x = <span class="hljs-string">'hello'</span></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(x);
&#125;
log(); <span class="hljs-comment">//'hello'</span>
log(<span class="hljs-string">'hi'</span>); <span class="hljs-comment">//'hi'</span>
log(<span class="hljs-number">1</span>); <span class="hljs-comment">//报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据函数的默认参数 'hello' ，TS 推断出了x 的类型为 string | undefined。</p>
<h2 data-id="heading-32">7.剩余参数</h2>
<p>1.使用 <code>...</code> 将接收到的参数传到一个指定类型的数组中。</p>
<p><strong>注：</strong> rest 参数只能是最后一个参数，</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">push</span>(<span class="hljs-params">array: <span class="hljs-built_in">any</span>[], ...items: <span class="hljs-built_in">any</span>[]</span>) </span>&#123;
    items.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>) </span>&#123;
        array.push(item);
    &#125;);
&#125;
<span class="hljs-keyword">let</span> a = [];
push(a, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">8.函数重载</h2>
<p>1.重载指的是两个或者两个以上同名函数，但它们的参数不一样，这时会出现函数重载的情况。</p>
<p>即重载允许一个函数接受不同数量或类型的参数时，作出不同的处理。</p>
<p>2.TS 中的重载是通过为同一个函数提供多个函数类型声明来实现函数重载的功能的。</p>
<p>比如，我们需要实现一个函数 <code>reverse</code>，输入数字 <code>123</code> 的时候，输出反转的数字 <code>321</code>，输入字符串 <code>'hello'</code> 的时候，输出反转的字符串 <code>'olleh'</code>。</p>
<p>利用联合类型，我们可以这么实现：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span></span>): <span class="hljs-title">number</span> | <span class="hljs-title">string</span> | <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(x.toString().split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>));
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> x.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>然而这样有一个缺点，就是不能够精确的表达，输入为数字的时候，输出也应该为数字，输入为字符串的时候，输出也应该为字符串。</strong></p>
<p>这时，我们可以使用重载定义多个 <code>reverse</code> 的函数类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//重载声明</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span></span>;
<span class="hljs-comment">//重载实现：声明中出现的参数都写出来，且类型合并，返回值类型合并</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span></span>): <span class="hljs-title">number</span> | <span class="hljs-title">string</span> | <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(x.toString().split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>));
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> x.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>);
    &#125;
&#125;
reverse(<span class="hljs-number">123</span>)
reverse(<span class="hljs-string">"abc"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们重复定义了多次函数 <code>reverse</code>，前几次都是重载声明，最后一次是重载实现。<strong>函数重载声明的各个成员必须是函数实现的子集</strong>，例如 "function reverse(x: number): number;"是"function reverse(x: number | string): number | string | void"的子集。</p>
<h1 data-id="heading-34">三、类（class）</h1>
<h2 data-id="heading-35">1.类的定义与使用</h2>
<p>1.定义类：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> 类名 </span>&#123;
属性名: 类型;

<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">参数: 类型</span>)</span>&#123;
<span class="hljs-built_in">this</span>.属性名 = 参数;
&#125;

方法名()&#123;
....
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.示例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span></span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = age;
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`大家好，我是<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.使用类：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'孙悟空'</span>, <span class="hljs-number">18</span>);
p.sayHello();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.this</p>
<ul>
<li>在类中，使用this表示当前对象</li>
</ul>
<h2 data-id="heading-36">2.类属性与方法的权限设置</h2>
<p>1.默认情况下，对象的属性是可以任意的修改的，为了确保数据的安全性，在TS中可以对属性的权限进行设置</p>
<p>2.只读属性（readonly）：</p>
<ul>
<li>如果在声明属性时添加一个readonly，则属性便成了只读属性无法修改</li>
<li>注意：如果 <code>readonly</code> 和其他访问修饰符同时存在的话，需要写在其后面。</li>
</ul>
<p>3.使用static开头的属性是静态属性（类属性），可以直接通过类去访问</p>
<ul>
<li>Person.age</li>
</ul>
<p>4.直接定义的属性是实例属性，需要通过对象的实例去访问：</p>
<ul>
<li>
<p>const per = new Person();</p>
</li>
<li>
<p>per.name</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span></span>&#123;
    <span class="hljs-comment">// 定义实例属性</span>
    <span class="hljs-keyword">readonly</span> name: <span class="hljs-built_in">string</span> = <span class="hljs-string">'孙悟空'</span>;
    <span class="hljs-comment">// name = '孙悟空';</span>

    <span class="hljs-comment">// 在属性前使用static关键字可以定义类属性（静态属性）</span>
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">readonly</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">18</span>;
    <span class="hljs-comment">// age = 18;</span>

    <span class="hljs-comment">// 定义方法</span>
<span class="hljs-comment">//如果方法以static开头则方法就是类方法，可以直接通过类去调用</span>
    <span class="hljs-comment">// static sayHello()&#123;</span>
    <span class="hljs-comment">//    console.log('Hello 大家好！');</span>
    <span class="hljs-comment">// &#125;</span>
    
    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 在方法中可以通过this来表示当前调用方法的对象</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello 大家好！'</span>);
    &#125;
&#125;

<span class="hljs-keyword">const</span> per = <span class="hljs-keyword">new</span> Person();
<span class="hljs-built_in">console</span>.log(per);
<span class="hljs-built_in">console</span>.log(per.name, per.age);

<span class="hljs-comment">// console.log(Person.age);</span>

<span class="hljs-comment">// console.log(per.name);</span>
<span class="hljs-comment">// per.name = 'tom';</span>
<span class="hljs-comment">// console.log(per.name);</span>

per.sayHello();
<span class="hljs-comment">// Person.sayHello();</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">3.继承</h2>
<ul>
<li>
<p>实现继承使用 <code>extends</code> 关键字</p>
</li>
<li>
<p>使用继承后，子类将会拥有父类所有的方法和属性</p>
<ul>
<li>
<p>通过继承可以将多个类中共有的代码写在一个父类中，</p>
</li>
<li>
<p>这样只需要写一次即可让所有的子类都同时拥有父类中的属性和方法</p>
</li>
<li>
<p>如果希望在子类中添加一些父类中没有的属性或方法直接加就行</p>
</li>
</ul>
</li>
<li>
<p>通过继承可以在不修改类的情况下完成对类的扩展</p>
</li>
<li>
<p>方法重写</p>
<ul>
<li>如果在子类中添加了和父类同名的方法，则子类方法会覆盖掉父类的方法</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 定义一个Animal类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;

    <span class="hljs-comment">// constructor 被称为构造函数</span>
    <span class="hljs-comment">//  构造函数会在对象创建时调用</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = age;
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'动物在叫~'</span>);
    &#125;
&#125;

<span class="hljs-comment">// 定义一个表示狗的类</span>
<span class="hljs-comment">// 使Dog类继承Animal类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;

    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>在跑~~~`</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'汪汪汪汪！'</span>);
    &#125;

&#125;

<span class="hljs-comment">// 定义一个表示猫的类</span>
<span class="hljs-comment">// 使Cat类继承Animal类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'喵喵喵喵！'</span>);
    &#125;
&#125;

<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'旺财'</span>, <span class="hljs-number">5</span>);
<span class="hljs-keyword">const</span> cat = <span class="hljs-keyword">new</span> Cat(<span class="hljs-string">'咪咪'</span>, <span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(dog);
dog.sayHello();
dog.run();
<span class="hljs-built_in">console</span>.log(cat);
cat.sayHello();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>在子类中可以使用super来完成对父类的引用</p>
</li>
<li>
<p>如果在子类中写了构造函数，在子类构造函数中必须对父类的构造函数进行调用</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'动物在叫~'</span>);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-comment">// 如果在子类中写了构造函数，在子类构造函数中必须对父类的构造函数进行调用</span>
        <span class="hljs-built_in">super</span>(name); <span class="hljs-comment">// 调用父类的构造函数</span>
        <span class="hljs-built_in">this</span>.age = age;
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 在类的方法中 super就表示当前类的父类</span>
        <span class="hljs-built_in">super</span>.sayHello();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'汪汪汪汪！'</span>);
    &#125;

&#125;

<span class="hljs-keyword">const</span> dog = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'旺财'</span>, <span class="hljs-number">3</span>);
dog.sayHello();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">4.TS中属性具有三种修饰符：</h2>
<ul>
<li>
<p>public（默认值），可以在类、子类和对象中读取与修改</p>
</li>
<li>
<p>protected ，可以在类、子类中读取与修改</p>
</li>
<li>
<p>private ，可以在类中读取与修改</p>
<ul>
<li>通过在类中添加方法使得私有属性可以被外部访问</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span></span>&#123;
    <span class="hljs-keyword">protected</span> num: <span class="hljs-built_in">number</span>;
    
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">num: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.num = num;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.num);
    &#125;
&#125;

<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> B(<span class="hljs-number">123</span>);
<span class="hljs-comment">//b.num = 33; //不能修改</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">5.属性的存取器</h2>
<ul>
<li>
<p>getter方法用来读取属性</p>
</li>
<li>
<p>setter方法用来设置属性</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-keyword">private</span> _name: <span class="hljs-built_in">string</span>;
    <span class="hljs-keyword">private</span> _age: <span class="hljs-built_in">number</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>._name = name;
        <span class="hljs-built_in">this</span>._age = age;
    &#125;

    <span class="hljs-comment">// 自定义访问接口</span>
    <span class="hljs-comment">// 定义方法，用来获取name属性</span>
    <span class="hljs-comment">// getName()&#123;</span>
    <span class="hljs-comment">//     return this._name;</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// 定义方法，用来设置name属性</span>
    <span class="hljs-comment">// setName(value: string)&#123;</span>
    <span class="hljs-comment">//     this._name = value;</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// getAge()&#123;</span>
    <span class="hljs-comment">//     return this._age;</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// setAge(value: number)&#123;</span>
    <span class="hljs-comment">//     // 判断年龄是否合法</span>
    <span class="hljs-comment">//     if(value >= 0)&#123;</span>
    <span class="hljs-comment">//         this._age = value;</span>
    <span class="hljs-comment">//     &#125;</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-comment">// TS中设置getter方法的方式</span>
    <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>()&#123;
        <span class="hljs-comment">// console.log('get name()执行了！！');</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._name;
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">value</span>)&#123;
        <span class="hljs-built_in">this</span>._name = value;
    &#125;

    <span class="hljs-keyword">get</span> <span class="hljs-title">age</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._age;
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">age</span>(<span class="hljs-params">value</span>)&#123;
        <span class="hljs-keyword">if</span>(value >= <span class="hljs-number">0</span>)&#123;
            <span class="hljs-built_in">this</span>._age = value
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">const</span> per = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'孙悟空'</span>, <span class="hljs-number">18</span>);

<span class="hljs-comment">// per.setName('猪八戒');</span>
<span class="hljs-comment">// per.setAge(-33);</span>

per.name = <span class="hljs-string">'猪八戒'</span>;
per.age = -<span class="hljs-number">33</span>;
<span class="hljs-built_in">console</span>.log(per.name, per.age);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">6.参数属性</h2>
<p>1.可以直接将属性定义在构造函数中，等同于类中定义该属性同时给该属性赋值，使代码更简洁。</p>
<p>2.修饰符和<code>readonly</code>也可以使用在构造函数参数中，</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/* class C&#123;

    name: string;
    age: number

    // 可以直接将属性定义在构造函数中
    constructor(name: string, age: number) &#123;
        this.name = name;
        this.age = age;
    &#125;

&#125;*/</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span></span>&#123;
    <span class="hljs-comment">// 可以直接将属性定义在构造函数中</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">public</span> age: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = age;
    &#125;
&#125;

<span class="hljs-keyword">const</span> c = <span class="hljs-keyword">new</span> C(<span class="hljs-string">'xxx'</span>, <span class="hljs-number">111</span>);
<span class="hljs-built_in">console</span>.log(c);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">7.抽象类（abstract class）</h2>
<p>1.以abstract开头的类是抽象类</p>
<p>2.抽象类就是专门用来被继承的类</p>
<p>3.抽象类和其他类区别不大，只是不能用来创建对象</p>
<p>4.使用abstract开头的方法叫做抽象方法，抽象方法没有方法体只能定义在抽象类中，继承抽象类时抽象方法必须要实现</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;
    
    <span class="hljs-keyword">abstract</span> run(): <span class="hljs-built_in">void</span>;
    
    <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'动物在叫~'</span>);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'狗在跑~'</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> d = <span class="hljs-keyword">new</span> Dog(<span class="hljs-string">'dd'</span>)
<span class="hljs-built_in">console</span>.log(d.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-42">8.类类型</h2>
<p>1.给对象加上 TypeScript 的类型注解</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  sayHi(): <span class="hljs-built_in">string</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`My name is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>;
  &#125;
&#125;

<span class="hljs-keyword">let</span> a: Animal = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'Jack'</span>);
<span class="hljs-built_in">console</span>.log(a.sayHi()); <span class="hljs-comment">// My name is Jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-43">四、接口（Interface）</h1>
<h2 data-id="heading-44">1.接口的概念与作用</h2>
<p>1.在面向对象的编程中，接口是一种规范的定义，它定义了行为和动作的规范，在程序设计里面，接口起到一种限制和规范的作用。接口定义了某一批类所需要遵守的规范，接口不关心这些类的内部状态数据，也不关心这些类里方法的实现细节，它只规定这批类里必须提供某些方法，提供这些方法的类就可以满足实际需要。 typescrip中的接口类似于java，同时还增加了更灵活的接口类型，包括属性、函数、可索引和类等。</p>
<p>2.接口的作用就是对行为和动作进行规范和约束，跟抽象类类似，但是，接口中不能有方法体，只允许有方法定义。</p>
<h2 data-id="heading-45">2.接口当成类型使用 - 定义对象的类型</h2>
<ul>
<li>使用接口（Interfaces）来定义对象的类型。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> myInterface &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
    gender: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">const</span> obj: myInterface = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'sss'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">111</span>,
    <span class="hljs-attr">gender</span>: <span class="hljs-string">'男'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-46">3.类实现接口</h2>
<ul>
<li>类使用implements实现接口</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> myInter&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    sayHello(): <span class="hljs-built_in">void</span>;
&#125;

   <span class="hljs-comment">/*
    * 定义类时，可以使类去实现一个接口,
    *   实现接口就是使类满足接口的要求
    * */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">myInter</span></span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'大家好~~'</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> my = <span class="hljs-keyword">new</span> MyClass(<span class="hljs-string">'Jack'</span>);
my.sayHello()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一个类可以实现多个接口</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Alarm &#123;
    alert(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> Light &#123;
    lightOn(): <span class="hljs-built_in">void</span>;
    lightOff(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-title">implements</span> <span class="hljs-title">Alarm</span>, <span class="hljs-title">Light</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">alert</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Car alert'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">lightOn</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Car light on'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">lightOff</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Car light off'</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> Car = <span class="hljs-keyword">new</span> Car();
car.alert();
car.lightOn();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">4.可选属性</h2>
<ul>
<li>使用?设置可选属性</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> tom: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Tom'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">5.任意属性</h2>
<ul>
<li>使用[propName: string]: any;</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age?: <span class="hljs-built_in">number</span>;
    [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-keyword">let</span> tom: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Tom'</span>,
    <span class="hljs-attr">gender</span>: <span class="hljs-string">'male'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-49">6.可索引型接口</h2>
<ul>
<li>可索引接口就是对数组、对象的约束，不常用！</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//可索引接口，对数组的约束</span>
<span class="hljs-keyword">interface</span> UserArr &#123;
    [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">var</span> arr1: UserArr = [<span class="hljs-string">"aaa"</span>, <span class="hljs-string">"bbb"</span>];
<span class="hljs-built_in">console</span>.log(arr1[<span class="hljs-number">0</span>]);

<span class="hljs-comment">//可索引接口，对对象的约束</span>
<span class="hljs-keyword">interface</span> UserObj &#123;
    [index: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">var</span> arr2: UserObj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">'21'</span> &#125;;
<span class="hljs-built_in">console</span>.log(arr2);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">7.只读属性</h2>
<ul>
<li>有时候我们希望对象中的一些字段只能在创建的时候被赋值，那么可以用 <code>readonly</code> 定义只读属性：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-keyword">readonly</span> id: <span class="hljs-built_in">number</span>;
    name: <span class="hljs-built_in">string</span>;
    age?: <span class="hljs-built_in">number</span>;
    [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-keyword">let</span> tom: Person = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">89757</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Tom'</span>,
    <span class="hljs-attr">gender</span>: <span class="hljs-string">'male'</span>
&#125;;

tom.id = <span class="hljs-number">9527</span>; <span class="hljs-comment">//error TS2540</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-51">8.接口继承接口</h2>
<ul>
<li>对于类、抽象类、接口继承只能单继承，但接口却可以被多实现。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//人这个接口</span>
<span class="hljs-keyword">interface</span> Person &#123;
    eat(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">//程序员接口</span>
<span class="hljs-keyword">interface</span> Programmer <span class="hljs-keyword">extends</span> Person &#123;
    code(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">//小程序接口</span>
<span class="hljs-keyword">interface</span> Web &#123;
    app(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">//前端工程师</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WebProgrammer</span> <span class="hljs-title">implements</span> <span class="hljs-title">Person</span>, <span class="hljs-title">Web</span> </span>&#123;
    <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;
    <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">"下班吃饭饭"</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">code</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">"上班敲代码"</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">app</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">"开发小程序"</span>);
    &#125;
&#125;

<span class="hljs-keyword">var</span> w = <span class="hljs-keyword">new</span> WebProgrammer(<span class="hljs-string">"小李"</span>);
w.eat();
w.code();
w.app();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-52">9.接口合并</h2>
<p>1.接口中的属性在合并时会简单的合并到一个接口中：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">weight</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
    weight: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.注意：<strong>合并的属性的类型必须是唯一的</strong>：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;  <span class="hljs-comment">// 虽然重复了，但是类型都是 `number`，所以不会报错</span>
    weight: <span class="hljs-built_in">number</span>;
&#125;


<span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">string</span>;  <span class="hljs-comment">// 类型不一致，会报错</span>
    weight: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-comment">// index.ts(5,3): error TS2403</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.接口中方法的合并，与函数的合并一样：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
    alert(s: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">weight</span>: <span class="hljs-built_in">number</span>;
    alert(s: <span class="hljs-built_in">string</span>, <span class="hljs-attr">n</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Alarm &#123;
    <span class="hljs-attr">price</span>: <span class="hljs-built_in">number</span>;
    weight: <span class="hljs-built_in">number</span>;
    alert(s: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>;
    alert(s: <span class="hljs-built_in">string</span>, <span class="hljs-attr">n</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-53">10.接口继承类（了解）</h2>
<p>常见的面向对象语言中，接口是不能继承类的，但是在 TypeScript 中却是可以的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
&#125;

<span class="hljs-keyword">interface</span> Point3d <span class="hljs-keyword">extends</span> Point &#123;
    <span class="hljs-attr">z</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> point3d: Point3d = &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">z</span>: <span class="hljs-number">3</span>&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么 TypeScript 会支持接口继承类呢？</p>
<p>实际上，当我们在声明 <code>class Point</code> 时，除了会创建一个名为 <code>Point</code> 的类之外，同时也创建了一个名为 <code>Point</code> 的类型（实例的类型）。</p>
<p>所以我们既可以将 <code>Point</code> 当做一个类来用（使用 <code>new Point</code> 创建它的实例）：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
&#125;

<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以将 <code>Point</code> 当做一个类型来用（使用 <code>: Point</code> 表示参数的类型）：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printPoint</span>(<span class="hljs-params">p: Point</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(p.x, p.y);
&#125;

printPoint(<span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子实际上可以等价于：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
&#125;

<span class="hljs-keyword">interface</span> PointInstanceType &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printPoint</span>(<span class="hljs-params">p: PointInstanceType</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(p.x, p.y);
&#125;

printPoint(<span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中我们新声明的 <code>PointInstanceType</code> 类型，与声明 <code>class Point</code> 时创建的 <code>Point</code> 类型是等价的。</p>
<p>所以回到 <code>Point3d</code> 的例子中，我们就能很容易的理解为什么 TypeScript 会支持接口继承类了：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
&#125;

<span class="hljs-keyword">interface</span> PointInstanceType &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-comment">// 等价于 interface Point3d extends PointInstanceType</span>
<span class="hljs-keyword">interface</span> Point3d <span class="hljs-keyword">extends</span> Point &#123;
    <span class="hljs-attr">z</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> point3d: Point3d = &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">z</span>: <span class="hljs-number">3</span>&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们声明 <code>interface Point3d extends Point</code> 时，<code>Point3d</code> 继承的实际上是类 <code>Point</code> 的实例的类型。</p>
<p>换句话说，可以理解为定义了一个接口 <code>Point3d</code> 继承另一个接口 <code>PointInstanceType</code>。</p>
<p>所以「接口继承类」和「接口继承接口」没有什么本质的区别。</p>
<p>值得注意的是，<code>PointInstanceType</code> 相比于 <code>Point</code>，缺少了 <code>constructor</code> 方法，这是因为声明 <code>Point</code> 类时创建的 <code>Point</code> 类型是不包含构造函数的。另外，除了构造函数是不包含的，静态属性或静态方法也是不包含的（实例的类型当然不应该包括构造函数、静态属性或静态方法）。</p>
<p>换句话说，声明 <code>Point</code> 类时创建的 <code>Point</code> 类型只包含其中的实例属性和实例方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
    <span class="hljs-comment">/** 静态属性，坐标系原点 */</span>
    <span class="hljs-keyword">static</span> origin = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    <span class="hljs-comment">/** 静态方法，计算与原点距离 */</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">distanceToOrigin</span>(<span class="hljs-params">p: Point</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.sqrt(p.x * p.x + p.y * p.y);
    &#125;
    <span class="hljs-comment">/** 实例属性，x 轴的值 */</span>
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    <span class="hljs-comment">/** 实例属性，y 轴的值 */</span>
    y: <span class="hljs-built_in">number</span>;
    <span class="hljs-comment">/** 构造函数 */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.x = x;
        <span class="hljs-built_in">this</span>.y = y;
    &#125;
    <span class="hljs-comment">/** 实例方法，打印此点 */</span>
    <span class="hljs-function"><span class="hljs-title">printPoint</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.x, <span class="hljs-built_in">this</span>.y);
    &#125;
&#125;

<span class="hljs-keyword">interface</span> PointInstanceType &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
    printPoint(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">let</span> p1: Point;
<span class="hljs-keyword">let</span> p2: PointInstanceType;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中最后的类型 <code>Point</code> 和类型 <code>PointInstanceType</code> 是等价的。</p>
<p>同样的，在接口继承类的时候，也只会继承它的实例属性和实例方法。</p>
<h1 data-id="heading-54">五、泛型</h1>
<h2 data-id="heading-55">1.泛型的简介</h2>
<p>1.泛型（Generics）是指在定义函数、接口或类的时候，不预先指定具体的类型（返回值、参数、属性的类型不能确定），而在使用的时候再指定类型的一种特性。</p>
<p>2.泛型就是解决类、接口、方法的复用性、以及对不特定数据类型的支持。</p>
<h2 data-id="heading-56">2.泛型基本使用举例</h2>
<p>实现一个函数 <code>createArray</code>，它可以创建一个指定长度的数组，同时将每一项都填充一个默认值：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">Array</span><<span class="hljs-title">any</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

createArray(<span class="hljs-number">3</span>, <span class="hljs-string">'x'</span>); <span class="hljs-comment">// ['x', 'x', 'x']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们使用了数组泛型来定义返回值的类型。</p>
<p>这段代码编译不会报错，但是一个显而易见的缺陷是：它并没有准确的定义返回值的类型：</p>
<ul>
<li>
<p>首先使用any会关闭TS的类型检查</p>
</li>
<li>
<p>其次<code>Array<any></code> 允许数组的每一项都为任意类型。但是我们预期的是，数组中每一项都应该是输入的 <code>value</code> 的类型。</p>
</li>
</ul>
<p>使用泛型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span><<span class="hljs-title">T</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result: T[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

createArray<<span class="hljs-built_in">string</span>>(<span class="hljs-number">3</span>, <span class="hljs-string">'x'</span>); <span class="hljs-comment">// ['x', 'x', 'x']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们在函数名后添加了 <code><T></code>，其中 <code>T</code> 用来指代任意输入的类型，在后面的输入 <code>value: T</code> 和输出 <code>Array<T></code> 中即可使用了。</p>
<p>接着在调用的时候，可以指定它具体的类型为 <code>string</code>。当然，也可以不手动指定，而让TS类型推断自动推算出来：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span><<span class="hljs-title">T</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result: T[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

createArray(<span class="hljs-number">3</span>, <span class="hljs-string">'x'</span>); <span class="hljs-comment">// ['x', 'x', 'x']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-57">3.多个类型参数</h2>
<p>定义泛型的时候，可以一次定义多个类型参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swap</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">tuple: [T, U]</span>): [<span class="hljs-title">U</span>, <span class="hljs-title">T</span>] </span>&#123;
    <span class="hljs-keyword">return</span> [tuple[<span class="hljs-number">1</span>], tuple[<span class="hljs-number">0</span>]];
&#125;

swap([<span class="hljs-number">7</span>, <span class="hljs-string">'seven'</span>]); <span class="hljs-comment">// ['seven', 7]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们定义了一个 <code>swap</code> 函数，用来交换输入的元组。</p>
<h2 data-id="heading-58">4.泛型约束</h2>
<p>使用泛型时，可以将泛型当成是一个普通的类去使用，也可以对泛型的范围进行约束</p>
<p>1.泛型继承接口</p>
<p>在函数内部使用泛型变量的时候，由于事先不知道它是哪种类型，所以不能随意的操作它的属性或方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length); <span class="hljs-comment">// error TS2339</span>
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，泛型 <code>T</code> 不一定包含属性 <code>length</code>，所以编译的时候报错了。</p>
<p>这时，我们可以对泛型进行约束，只允许这个函数传入那些包含 <code>length</code> 属性的变量。这就是泛型约束：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Lengthwise &#123;
    <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Lengthwise</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们使用了 <code>extends</code> 约束了泛型 <code>T</code> 必须符合接口 <code>Lengthwise</code> 的形状，也就是必须包含 <code>length</code> 属性。</p>
<p>此时如果调用 <code>loggingIdentity</code> 的时候，传入的 <code>arg</code> 不包含 <code>length</code>，那么在编译阶段就会报错了：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Lengthwise &#123;
    <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Lengthwise</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);
    <span class="hljs-keyword">return</span> arg;
&#125;

loggingIdentity(<span class="hljs-number">7</span>); <span class="hljs-comment">// error TS2345</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.多个类型参数之间也可以互相约束：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyFields</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">U</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">target: T, source: U</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id <span class="hljs-keyword">in</span> source) &#123;
        target[id] = (<T>source)[id];
    &#125;
    <span class="hljs-keyword">return</span> target;
&#125;

<span class="hljs-keyword">let</span> x = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">d</span>: <span class="hljs-number">4</span> &#125;;

<span class="hljs-built_in">console</span>.log(copyFields(x, &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">d</span>: <span class="hljs-number">20</span> &#125;)); <span class="hljs-comment">// &#123; a: 1, b: 10, c: 3, d: 20 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，我们使用了两个类型参数，其中要求 <code>T</code> 继承 <code>U</code>，这样就保证了 <code>U</code> 上不会出现 <code>T</code> 中不存在的字段。</p>
<h2 data-id="heading-59">5.泛型接口</h2>
<ul>
<li>使用接口的方式来定义一个函数的基本结构（参数、返回值）</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//泛型接口</span>
<span class="hljs-keyword">interface</span> ConfigFn<T> &#123;
    (value: T): T;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> value;
&#125;

<span class="hljs-keyword">var</span> myGetData: ConfigFn<<span class="hljs-built_in">string</span>> = getData;
<span class="hljs-built_in">console</span>.log(myGetData(<span class="hljs-string">'20'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-60">6.泛型类</h2>
<ul>
<li>与泛型接口类似，泛型也可以用于类的类型定义中</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GenericNumber</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-attr">zeroValue</span>: T;
    add: <span class="hljs-function">(<span class="hljs-params">x: T, y: T</span>) =></span> T;
&#125;

<span class="hljs-keyword">let</span> myGenericNumber = <span class="hljs-keyword">new</span> GenericNumber<<span class="hljs-built_in">number</span>>();
myGenericNumber.zeroValue = <span class="hljs-number">0</span>;
myGenericNumber.add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x, y</span>) </span>&#123; <span class="hljs-keyword">return</span> x + y; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-61">7.泛型类进阶</h2>
<ul>
<li>把一个类当做泛型用于另一个类的类型定义中</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//定义操作数据库的泛型类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MysqlDb</span><<span class="hljs-title">T</span>></span>&#123;
    add(info: T): <span class="hljs-built_in">boolean</span> &#123;
        <span class="hljs-built_in">console</span>.log(info);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
&#125;

<span class="hljs-comment">//想给User表增加数据，定义一个User类和数据库进行映射</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
    <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    pasword: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
&#125;

<span class="hljs-keyword">var</span> user = <span class="hljs-keyword">new</span> User();
user.username = <span class="hljs-string">"张三"</span>;
user.pasword = <span class="hljs-string">"123456"</span>;
<span class="hljs-keyword">var</span> md1 = <span class="hljs-keyword">new</span> MysqlDb<User>();
md1.add(user);

<span class="hljs-comment">//想给ArticleCate增加数据，定义一个ArticleCate类和数据库进行映射</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ArticleCate</span> </span>&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    desc: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    status: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">params: &#123;
        title: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
        desc: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
        status?: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>
    &#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.title = params.title;
        <span class="hljs-built_in">this</span>.desc = params.desc;
        <span class="hljs-built_in">this</span>.status = params.status;
    &#125;
&#125;

<span class="hljs-keyword">var</span> article = <span class="hljs-keyword">new</span> ArticleCate(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"这是标题"</span>,
    <span class="hljs-attr">desc</span>: <span class="hljs-string">"这是描述"</span>,
    <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>
&#125;);
<span class="hljs-keyword">var</span> md2 = <span class="hljs-keyword">new</span> MysqlDb<ArticleCate>();
md2.add(article);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-62">8.泛型参数的默认类型（了解）</h2>
<p>在 TypeScript 2.3 以后，我们可以为泛型中的类型参数指定默认类型。当使用泛型时没有在代码中直接指定类型参数，从实际值参数中也无法推测出时，这个默认类型就会起作用。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span><<span class="hljs-title">T</span> = <span class="hljs-title">string</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result: T[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            