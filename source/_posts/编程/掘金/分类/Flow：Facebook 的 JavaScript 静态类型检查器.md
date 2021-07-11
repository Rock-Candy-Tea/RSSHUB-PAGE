
---
title: 'Flow：Facebook 的 JavaScript 静态类型检查器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://i.loli.net/2021/07/10/2vg9mucboQanZiW.jpg'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 07:38:49 GMT
thumbnail: 'https://i.loli.net/2021/07/10/2vg9mucboQanZiW.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>记某年的一次团队分享，主要目的：优化又臭又长维护噩梦的JavaScript老项目</p>
</blockquote>
<p><img src="https://i.loli.net/2021/07/10/2vg9mucboQanZiW.jpg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript写起来，<code>行云流水、挥洒自如、无拘无束、笔走龙蛇、为所欲为</code></p>
<p>金主粑粑，每天抓狂，小修小补的<code>hotfix从未停止</code>，<code>脆弱的代码</code>经不住半点风浪</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c0bd336de34431ab89ff28776404441~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Flow是JavaScript代码的<code>静态类型检查器</code>。 它可以帮助您<code>提高工作效率</code>。 让您的代码<code>更快，更智能，更自信，更大规模</code>。</p>
<p>Flow通过静态类型注释检查代码是否存在错误。 这些类型允许您告诉Flow您希望代码如何工作，Flow将确保它以这种方式工作。</p>
<h3 data-id="heading-0">1.从demo开始认识flow</h3>
<h3 data-id="heading-1">2.安装，配置</h3>
<h3 data-id="heading-2">3.flow总结及使用</h3>
<h3 data-id="heading-3">前言</h3>
<p>我们知道<code>react</code>源码现在还是采用<code>flow + js</code>的方式，下图截取一小段<code>react Fiber源码</code>，先混个脸熟</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * <span class="hljs-doctag">@flow</span>
 */</span>
<span class="hljs-keyword">import</span> type &#123;ReactElement&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'shared/ReactElementType'</span>;
<span class="hljs-keyword">import</span> type &#123;ReactFragment, ReactPortal, ReactScope&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'shared/ReactTypes'</span>;
<span class="hljs-keyword">import</span> type &#123;Fiber&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactInternalTypes'</span>;
<span class="hljs-keyword">import</span> type &#123;RootTag&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactRootTags'</span>;
<span class="hljs-keyword">import</span> type &#123;WorkTag&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactWorkTags'</span>;
<span class="hljs-keyword">import</span> type &#123;TypeOfMode&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactTypeOfMode'</span>;
<span class="hljs-keyword">import</span> type &#123;Lanes&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactFiberLane.new'</span>;
<span class="hljs-keyword">import</span> type &#123;SuspenseInstance&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactFiberHostConfig'</span>;
<span class="hljs-keyword">import</span> type &#123;OffscreenProps&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./ReactFiberOffscreenComponent'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.从demo开始认识flow</h3>
<h4 data-id="heading-5">1.1 出入参静态类型注释</h4>
<pre><code class="copyable">// @flow
function square(n: number): number &#123;
  return n * n;
&#125;

square("2"); // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错信息：</p>
<p>Error ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ common/globFile.js:26:8</p>
<p>Cannot call square with '2' bound to n because string [1] is incompatible with number [2].</p>
<h4 data-id="heading-6">1.2.运算结果类型检查</h4>
<p>因为Flow很好地理解JavaScript，所以它不需要很多这些类型。 你应该只需要做很少的工作来描述你的Flow代码，它将推断其余部分。 在很多时候，Flow可以完全理解您的代码而不需要任何类型</p>
<pre><code class="copyable">// @flow
function square(n) &#123;
  return n * n; // Error!
&#125;

square("2");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错信息：
Cannot perform arithmetic operation because string [1] is not a number.</p>
<h3 data-id="heading-7">2.安装</h3>
<h4 data-id="heading-8">2.1 安装编译器</h4>
<p>官方推荐<code>babel</code>或<code>flow-remove-types</code></p>
<pre><code class="copyable">npm install --save-dev @babel/cli @babel/preset-flow
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目增加<code>babel.config.js</code>文件</p>
<pre><code class="copyable">module.exports = function() &#123;
  return &#123;
    presets: [
      "@babel/preset-flow"
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>package.json</code>中添加scripts</p>
<pre><code class="copyable">&#123;
  "devDependencies": &#123;
    "@babel/cli": "^7.4.4",
    "@babel/preset-flow": "^7.0.0",
  &#125;,
  "scripts": &#123;
    "build": "babel src/ -d lib/",
    "prepublish": "npm run build"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">2.2 安装flow</h4>
<pre><code class="copyable">npm install --save-dev flow-bin
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>package.json</code>中添加scripts</p>
<pre><code class="copyable">&#123;
  "devDependencies": &#123;
    "flow-bin": "^0.99.0"
  &#125;,
  "scripts": &#123;
    "flow": "flow"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成<code>flowconfig</code>配置文件</p>
<pre><code class="copyable">npm run flow init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行<code>flow</code></p>
<pre><code class="copyable">npm run flow
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.flow总结及使用</h3>
<ul>
<li>3.1 使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org%2Fen%2Fdocs%2Fusage%2F%23toc-initialize-your-project" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org/en/docs/usage/#toc-initialize-your-project" ref="nofollow noopener noreferrer">flow init初始化项目</a></li>
<li>3.2 使用flow启动Flow后台进程<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org%2Fen%2Fdocs%2Fusage%2F%23toc-run-the-flow-background-process" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org/en/docs/usage/#toc-run-the-flow-background-process" ref="nofollow noopener noreferrer">flow status</a></li>
<li>3.3 使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org%2Fen%2Fdocs%2Fusage%2F%23toc-prepare-your-code-for-flow" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org/en/docs/usage/#toc-prepare-your-code-for-flow" ref="nofollow noopener noreferrer">// @flow</a>确定Flow将监视哪些文件</li>
<li>3.4 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org%2Fen%2Fdocs%2Fusage%2F%23toc-write-flow-code" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org/en/docs/usage/#toc-write-flow-code" ref="nofollow noopener noreferrer">编写flow代码</a></li>
<li>3.5 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org%2Fen%2Fdocs%2Fusage%2F%23toc-check-your-code" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org/en/docs/usage/#toc-check-your-code" ref="nofollow noopener noreferrer">检查代码</a>是否存在类型错误</li>
<li>3.6 如何在代码中添加类型注释</li>
</ul>
<h4 data-id="heading-11">3.1 使用 flow init 初始化项目</h4>
<p>生成类似INI格式，项目.flowconfig配置文件</p>
<p>3.1.1 <code>.flowconfig</code>由6个部分组成</p>
<pre><code class="copyable">; 忽略匹配文件
[ignore]
<PROJECT_ROOT>/__tests__/.*
<PROJECT_ROOT>/lib/.*

; 包含指定的文件或目录
[include]
<PROJECT_ROOT>/src/.*

; 在类型检查代码时包含指定的库定义
[libs]

; lint
[lints]
all=warn
untyped-type-import=error
sketchy-null-bool=off

; 选项
[options]
all=true
esproposal.decorators=ignore
experimental.const_params=true
module.file_ext=.bar
module.use_strict=true

; 严格
[strict]
nonstrict-import
unclear-type
unsafe-getters-setters
untyped-import
untyped-type-import


; none
; 在声明模式下，代码没有进行类型检查，会检查文件内容
[declarations]
<PROJECT_ROOT>/third_party/.*

; 不检查文件内容，不匹配指定正则表达式的类型文件，丢弃类型并将模块视为任何模块
[untyped]
<PROJECT_ROOT>/third_party/.*

; 指定flow使用的版本
[version]
0.98.1

<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.1.2 # or ; or 💩 are ignored</p>
<pre><code class="copyable"># This is a comment
  # This is a comment
; This is a comment
  ; This is a comment
💩 This is a comment
  💩 This is a comment
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.1.3 .flowconfig放置位置</p>
<p>.flowconfig的位置非常重要。Flow将包含.flowconfig的目录视为项目根目录。 默认情况下，Flow包含项目根目录下的所有源代码</p>
<h4 data-id="heading-12">3.2 使用flow启动flow后台进程</h4>
<p><code>vscode</code>推荐安装<code>Flow Language Support</code></p>
<pre><code class="copyable">flow status // 启动flow后台进程
flow stop   // 终止flow后台进程
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack</code>热加载，使用<code>flow-webpack-plugin</code></p>
<pre><code class="copyable">'use strict';

const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const FlowWebpackPlugin = require('flow-webpack-plugin');

module.exports = &#123;
  mode: 'development',
  devtool: 'source-map',
  entry:  './example/app.js',
  output: &#123;
      filename: 'bundle.js',
      path: path.resolve(__dirname, './dist'),
  &#125;,
  devServer: &#123;
      hot: true,
      disableHostCheck: true,
      historyApiFallback: true
  &#125;,
  plugins: [
      new HtmlWebpackPlugin(&#123; template: 'example/index.html' &#125;),
      new FlowWebpackPlugin(&#123;
        flowArgs: ['check']
      &#125;)
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">3.3 使用// @flow确定Flow将监视哪些文件</h4>
<p>Flow后台进程使用此标志收集所有文件，并使用所有这些文件中提供的类型信息来确保一致性和无错误编程</p>
<p>使用JavaScript注释的形式，注释<code>@flow</code></p>
<pre><code class="copyable">// @flow

或

/* @flow */
<span class="copy-code-btn">复制代码</span></code></pre>
<p>忽略<code>//@flow</code>，检查所有文件</p>
<pre><code class="copyable">flow check --all
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">3.4 编写flow代码</h4>
<p>Flow后台进程将会捕获此错误</p>
<pre><code class="copyable">// @flow

function foo(x: ?number): string &#123;
  if (x) &#123;
    return x;
  &#125;
  return "default string";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3.5 检查代码是否存在类型错误</h4>
<pre><code class="copyable"># equivalent to `flow status`
flow
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行flow检查</p>
<pre><code class="copyable">// @flow

function foo(x: ?number): string &#123;
  if (x) &#123;
    return x;  // Cannot return `x` because  number [1] is incompatible with  string [2].
  &#125;
  return "default string";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">3.6 如何在代码中添加类型注释</h4>
<p>类型注释符号</p>
<pre><code class="copyable">|       // 或
&       // 且 
?       // 可选
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型注释中包括的类型</p>
<pre><code class="copyable">boolean                                 // true or new Boolean(false)
string                                  // "hello" or new String("world")
number                                  // 3.14 or new Number(42)
null                                    // null
undefined (void in Flow types)          // undefined
Array (其中T用来描述数组中值的类型)     // Array<T>
Object                                  // &#123;&#125;
Function                                // function
class                                   // class
Symbols (not yet supported in Flow)     // Symbol("foo")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小写</p>
<pre><code class="copyable">// @flow
function method(x: number, y: string, z: boolean) &#123;
  // ...
&#125;

method(3.14, "hello", true);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大写</p>
<pre><code class="copyable">// @flow
function method(x: Number, y: String, z: Boolean) &#123;
  // ...
&#125;

method(new Number(42), new String("world"), new Boolean(false));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>boolean</p>
<pre><code class="copyable">// @flow
function acceptsBoolean(value: boolean) &#123;
  // ...
&#125;

acceptsBoolean(true);  // Works!
acceptsBoolean(false); // Works!
acceptsBoolean("foo"); // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript可以隐式地将其他类型的值转换为布尔值</p>
<pre><code class="copyable">if (42) &#123;&#125; // 42 => true
if ("") &#123;&#125; // "" => false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非布尔值需要显式转换为布尔类型</p>
<pre><code class="copyable">// @flow
function acceptsBoolean(value: boolean) &#123;
  // ...
&#125;

acceptsBoolean(0);          // Error!
acceptsBoolean(Boolean(0)); // Works!
acceptsBoolean(!!0);        // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>string</p>
<pre><code class="copyable">// @flow
function acceptsString(value: string) &#123;
  // ...
&#125;

acceptsString("foo"); // Works!
acceptsString(false); // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript可以隐式地将其他类型的值转换为字符</p>
<pre><code class="copyable">"foo" + 42; // "foo42"
"foo" + &#123;&#125;; // "foo[object Object]"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Flow连接到字符串时只接受字符串和数字。</p>
<pre><code class="copyable">// @flow
"foo" + "foo"; // Works!
"foo" + 42;    // Works!
"foo" + &#123;&#125;;    // Error!
"foo" + [];    // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>必须明确并将其他类型转换为字符串</p>
<pre><code class="copyable">// @flow
"foo" + String(&#123;&#125;);     // Works!
"foo" + [].toString();  // Works!
"" + JSON.stringify(&#123;&#125;) // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>number</p>
<pre><code class="copyable">// @flow
function acceptsNumber(value: number) &#123;
  // ...
&#125;

acceptsNumber(42);       // Works!
acceptsNumber(3.14);     // Works!
acceptsNumber(NaN);      // Works!
acceptsNumber(Infinity); // Works!
acceptsNumber("foo");    // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>null and void</p>
<pre><code class="copyable">// @flow
function acceptsNull(value: null) &#123;
  /* ... */
&#125;

function acceptsUndefined(value: void) &#123;
  /* ... */
&#125;

acceptsNull(null);           // Works!
acceptsNull(undefined);      // Error!
acceptsUndefined(null);      // Error!
acceptsUndefined(undefined); // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Array</p>
<pre><code class="copyable">let arr: Array<number> = [1, 2, 3];
let arr1: Array<boolean> = [true, false, true];
let arr2: Array<string> = ["A", "B", "C"];
let arr3: Array<mixed> = [1, true, "three"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object</p>
<pre><code class="copyable">// @flow
var obj1: &#123; foo: boolean &#125; = &#123; foo: true &#125;;
var obj2: &#123;
  foo: number,
  bar: boolean,
  baz: string,
&#125; = &#123;
  foo: 1,
  bar: true,
  baz: 'three',
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Function</p>
<pre><code class="copyable">// @flow
function concat(a: string, b: string): string &#123;
  return a + b;
&#125;

concat("foo", "bar"); // Works!
// $ExpectError
concat(true, false);  // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头Function</p>
<pre><code class="copyable">let method = (str, bool, ...nums) => &#123;
  // ...
&#125;;

let method = (str: string, bool?: boolean, ...nums: Array<number>): void => &#123;
  // ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回调Function</p>
<pre><code class="copyable">function method(callback: (error: Error | null, value: string | null) => void) &#123;
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>class</p>
<pre><code class="copyable">// @flow
class MyClass<A, B, C> &#123;
  constructor(arg1: A, arg2: B, arg3: C) &#123;
    // ...
  &#125;
&#125;

var val: MyClass<number, boolean, string> = new MyClass(1, true, 'three');


class Foo &#123;
  serialize() &#123; return '[Foo]'; &#125;
&#125;

class Bar &#123;
  serialize() &#123; return '[Bar]'; &#125;
&#125;

// $ExpectError
const foo: Foo = new Bar(); // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Maybe Types</p>
<pre><code class="copyable">// @flow
function acceptsMaybeString(value: ?string) &#123;
  // ...
&#125;

acceptsMaybeString("bar");     // Works!
acceptsMaybeString(undefined); // Works!
acceptsMaybeString(null);      // Works!
acceptsMaybeString();          // Works!
acceptsMaybeString(12345);     // Error!

// value: string null or undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象属性可选</p>
<pre><code class="copyable">// @flow
function acceptsObject(value: &#123; foo?: string &#125;) &#123;
  // ...
&#125;

acceptsObject(&#123; foo: "bar" &#125;);     // Works!
acceptsObject(&#123; foo: undefined &#125;); // Works!
acceptsObject(&#123; foo: null &#125;);      // Error!问号放在string前不报错
acceptsObject(&#123;&#125;);                 // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数参数可选</p>
<pre><code class="copyable">// @flow
function acceptsOptionalString(value?: string) &#123;
  // ...
&#125;

acceptsOptionalString("bar");     // Works!
acceptsOptionalString(undefined); // Works!
acceptsOptionalString(null);      // Error!问号放在string前不报错
acceptsOptionalString();          // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带默认值的函数参数</p>
<pre><code class="copyable">// @flow
function acceptsOptionalString(value: string = "foo") &#123;
  // ...
&#125;

acceptsOptionalString("bar");     // Works!
acceptsOptionalString(undefined); // Works!
acceptsOptionalString(null);      // Error!
acceptsOptionalString();          // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用字面文字作为类型</p>
<pre><code class="copyable">// @flow
function acceptsTwo(value: 2) &#123;
  // ...
&#125;

acceptsTwo(2);   // Works!
// $ExpectError
acceptsTwo(3);   // Error!
// $ExpectError
acceptsTwo("2"); // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Union Types</p>
<pre><code class="copyable">// @flow
function getColor(name: "success" | "warning" | "danger") &#123;
  switch (name) &#123;
    case "success" : return "green";
    case "warning" : return "yellow";
    case "danger"  : return "red";
  &#125;
&#125;

getColor("success"); // Works!
getColor("danger");  // Works!
// $ExpectError
getColor("error");   // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mixed Types</p>
<pre><code class="copyable">function stringifyBasicValue(value: string | number) &#123;
  return '' + value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>A type based on another type</p>
<pre><code class="copyable">function identity<T>(value: T): T &#123;
  return value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>An arbitrary type that could be anything</p>
<pre><code class="copyable">function getTypeOf(value: mixed): string &#123;
  return typeof value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Any Types</p>
<pre><code class="copyable">// @flow
function add(one: any, two: any): number &#123;
  return one + two;
&#125;

add(1, 2);     // Works.
add("1", "2"); // Works.
add(&#123;&#125;, []);   // Works.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量类型
将类型添加到变量声明
const let var</p>
<pre><code class="copyable">// @flow
const foo /* : number */ = 1;
const bar: number = 2;

var fooVar /* : number */ = 1;
let fooLet /* : number */ = 1;
var barVar: number = 2;
let barLet: number = 2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let</p>
<pre><code class="copyable">let foo: number = 1;
foo = 2;   // Works!
// $ExpectError
foo = "3"; // Error!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新分配变量</p>
<pre><code class="copyable">let foo = 42;

if (Math.random()) foo = true;
if (Math.random()) foo = "hello";

let isOneOf: number | boolean | string = foo; // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新分配变量确定变量类型</p>
<pre><code class="copyable">// @flow
let foo = 42;
let isNumber: number = foo; // Works!

foo = true;
let isBoolean: boolean = foo; // Works!

foo = "hello";
let isString: string = foo; // Works!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>react</p>
<pre><code class="copyable">import * as React from 'react';

type Props = &#123;
  foo: number,
  bar?: string,
&#125;;

type State = &#123;
  count: number,
&#125;;


class MyComponent extends React.Component<Props> &#123;
  state = &#123;
    count: 0,
  &#125;;
  render() &#123;
    this.props.doesNotExist; // Error! You did not define a `doesNotExist` prop.

    return <div>&#123;this.props.bar&#125;</div>;
  &#125;
&#125;

<MyComponent foo=&#123;42&#125; />;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想了解更多用法，可移步<code>flow官方文档</code>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflow.org" target="_blank" rel="nofollow noopener noreferrer" title="https://flow.org" ref="nofollow noopener noreferrer">flow.org</a></p>
<p>此篇笔记已收录 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fniexq%2Fniexq.github.io" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/niexq/niexq.github.io" ref="nofollow noopener noreferrer">个人笔记</a>，感谢阅读，欢迎<code>star</code>鼓励</p></div>  
</div>
            