
---
title: 'rollup - 构建原理及简易实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402951b5fad2494086a3a2e604c84e88~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 17:28:58 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402951b5fad2494086a3a2e604c84e88~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402951b5fad2494086a3a2e604c84e88~tplv-k3u1fbpfcp-watermark.image" alt="56.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>黄丹丹，微医前端技术部医疗支撑组。一个资深猫奴，爱静亦爱动无痕切换的精分程序媛.</p>
</blockquote>
<h2 data-id="heading-0">一、Rollup 概述</h2>
<p>官网地址：<a href="https://rollupjs.org/guide/en/" target="_blank" rel="nofollow noopener noreferrer">rollupjs.org/guide/en/</a></p>
<h3 data-id="heading-1">Rollup 是什么</h3>
<p><strong>我们先看看 Rollup 的作者 Rich Harris 是怎么讲的？</strong>
Rollup 是一个模块化的打包工具。本质上，它会合并 JavaScript 文件。而且你不需要去手动指定它们的顺序，或者去担心文件之间的变量名冲突。它的内部实现会比说的复杂一点，但是它就是这么做的 —— <strong>合并</strong>。</p>
<h3 data-id="heading-2">对比 Webpack</h3>
<p><a href="https://webpack.js.org/" target="_blank" rel="nofollow noopener noreferrer">webpack</a> 对前端来说是再熟悉不过的工具了，它提供了强大的功能来构建前端的资源，包括 html/js/ts/css/less/scss ... 等语言脚本，也包括 images/fonts ... 等二进制文件。正是因为 webpack 拥有如此强大的功能，所以 webpack 在进行资源打包的时候，就会产生很多冗余的代码（如果你有查看过 webpack 的 bundle 文件，便会发现）。
​</p>
<p>而对于一些项目（特别是类库）只有 js，而没有其他的静态资源文件，使用 webpack 就有点大才小用了，因为 webpack bundle 文件的体积略大，运行略慢，可读性略低。这个时候就可以选择 Rollup
​</p>
<p><a href="https://rollupjs.org/guide/en/" target="_blank" rel="nofollow noopener noreferrer">Rollup</a>是一个模块打包器，支持 ES6 模块，支持 Tree-shaking，但不支持 webpack 的 code-splitting、模块热更新等，这意味着它更适合用来做类库项目的打包器而不是应用程序项目的打包器。</p>
<h3 data-id="heading-3">简单总结</h3>
<p><strong>对于应用适用于 webpack，对于类库更适用于 Rollup，react/vue/anngular 都在用</strong>Rollup<strong>作为打包工具</strong></p>
<h2 data-id="heading-4">二、Rollup 前置知识</h2>
<p>在阐述 Rollup 的构建原理之前，我们需要了解一些<strong>前置知识</strong></p>
<h3 data-id="heading-5">magic-string</h3>
<p>magic-string 是 Rollup 作者写的一个关于字符串操作的库，这个库主要是对字符串一些常用方法进行了封装</p>
<pre><code class="copyable">var MagicString = require('magic-string')
var magicString = new MagicString('export var name = "zhangsan"')
// 以下所有操作都是基于原生字符串
// 类似于截取字符串
console.log(magicString.snip(0, 6).toString()) // export
// 从开始到结束删除
console.log(magicString.remove(0, 7).toString()) //  var name = "zhangsan"

// 多个模块，把他们打包在一个文件里，需要把很多文件的源代码合并在一起
let bundleString = new MagicString.Bundle();
bundleString.addSource(&#123;
    content: 'console.log(hello)',
    separator: '\n'
&#125;)
bundleString.addSource(&#123;
    content: 'console.log(world)',
    separator: '\n'
&#125;)
// // 原理类似
// let str = ''
// str += 'console.log(hello);\n'
// str += 'console.log(world);\n'
console.log(bundleString.toString()) 
// hello
// world
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">AST</h3>
<p>通过 javascript parse 可以把代码转化为一颗抽象语法树 AST，这颗树定义了代码的结构，通过操纵这个树，我们可以精确的定位到声明语句、赋值语句、运算符语句等等，实现对代码的分析、优化、变更等操作
源代码：main.js</p>
<pre><code class="copyable">// main.js
import &#123; a &#125; from './a'
console.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转化为 AST 是长这样子的，如下：</p>
<pre><code class="copyable">&#123;
  "type": "Program", // 这个 AST 类型为 Program，表明是一个程序
  "start": 0,
  "end": 40,
  "body": [ // body 是一个数组，每一条语句都对应 body 下的一个语句
    &#123;
      "type": "ImportDeclaration", // 导入声明类型
      "start": 0,
      "end": 23,
      "specifiers": [
        &#123;
          "type": "ImportSpecifier",
          "start": 9,
          "end": 10,
          "imported": &#123;
            "type": "Identifier",
            "start": 9,
            "end": 10,
            "name": "a" // 导入模块命名 name 'a'
          &#125;,
          "local": &#123;
            "type": "Identifier",
            "start": 9,
            "end": 10,
            "name": "a" // 本地模块命名，同 imported.name
          &#125;
        &#125;
      ],
      "source": &#123;
        "type": "Literal",
        "start": 18,
        "end": 23,
        "value": "./a", // 导入路径 './a'
        "raw": "'./a'"
      &#125;
    &#125;,
    &#123;
      "type": "ExpressionStatement", // 表达式类型
      "start": 24,
      "end": 38,
      "expression": &#123;
        "type": "CallExpression", // 调用表达式类型
        "start": 24,
        "end": 38,
        "callee": &#123;
          "type": "MemberExpression",
          "start": 24,
          "end": 35,
          "object": &#123;
            "type": "Identifier",
            "start": 24,
            "end": 31,
            "name": "console"
          &#125;,
          "property": &#123;
            "type": "Identifier",
            "start": 32,
            "end": 35,
            "name": "log"
          &#125;,
          "computed": false,
          "optional": false
        &#125;,
        "arguments": [
          &#123;
            "type": "Identifier",
            "start": 36,
            "end": 37,
            "name": "a"
          &#125;
        ],
        "optional": false
      &#125;
    &#125;
  ],
  "sourceType": "module"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<h3 data-id="heading-7">AST 工作流</h3>
<p>Parse（解析）将代码转化成抽象语法树，树上有很多的 estree 节点
Transform(转换) 对抽象语法树进行转换
Generate（代码生成） 将上一步经过转换过的抽象语法树生成新的代码</p>
<h3 data-id="heading-8">acorn</h3>
<p>acorn 是一个 JavaScript 语法解析器，它将 JavaScript 字符串解析成语法抽象树 AST
如果想了解 AST 语法树可以点下这个网址<a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer.net/</a>
​</p>
<h3 data-id="heading-9">作用域/作用域链</h3>
<p>在 js 中，作用域是用来规定变量访问范围的规则，
作用域链是由当前执行环境和上层执行环境的一系列变量对象组成的，它保证了当前执行环境对符合访问权限的变量和函数的有序访问</p>
<h2 data-id="heading-10">三、Rollup</h2>
<h3 data-id="heading-11">Rollup 是怎样工作的呢？</h3>
<p>你给它一个入口文件 —— 通常是 index.js。Rollup 将使用 Acorn 读取解析文件 —— 将返回给我们一种叫抽象语法树（AST）的东西。 一旦有了 AST ，你就可以发现许多关于代码的东西，比如它包含哪些 import 声明。
​</p>
<p>假设 index.js 文件头部有这样一行：</p>
<pre><code class="copyable">import foo from './foo.js';
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这就意味着 Rollup 需要去加载，解析，分析在 index.js 中引入的 ./foo.js。重复解析直到没有更多的模块被加载进来。更重要的是，所有的这些操作都是可插拔的，所以您可以从 node_modules 中导入或者使用 sourcemap-aware 的方式将 ES2015 编译成 ES5 代码。</strong></p>
<p>在 Rollup 中，一个文件就是一个模块，每个模块都会根据文件的代码生成一个 AST 抽象语法树。
​</p>
<p>分析 AST 节点，就是看这个节点有没有调用函数方法，有没有读到变量，有，就查看是否在当前作用域，如果不在就往上找，直到找到模块顶级作用域为止。如果本模块都没找到，说明这个函数、方法依赖于其他模块，需要从其他模块引入。如果发现其他模块中有方法依赖其他模块，就会递归读取其他模块，如此循环直到没有依赖的模块为止
找到这些变量或着方法是在哪里定义的，把定义语句包含进来即可
其他无关代码一律不要
​</p>
<p>看如下代码，我们先实际操作一下：</p>
<pre><code class="copyable">// index.js
import &#123; foo &#125; from "./foo";
foo()
var city = 'hangzhou'

function test() &#123;
    console.log('test')
&#125;

console.log(test())
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// foo.js
import &#123; bar &#125; from "./bar";
export function foo() &#123;
    console.log('foo')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// bar.js
export function bar() &#123;
    console.log('bar')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// rollup.config.js
export default &#123;
    input: './src/index.js',
    output: &#123;
        file: './dist/bundle.js', // 打包后的存放文件
        format: 'cjs', //输出格式 amd es6 life umd cjs
        name: 'bundleName', //如果输出格式 life，umd 需要指定一个全局变量
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 npm run build,会得到如下结果：</p>
<pre><code class="copyable">'use strict';

function foo() &#123;
    console.log('foo');
&#125;

foo();

function test() &#123;
    console.log('test');
&#125;

console.log(test());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上，我们可以看到
<strong>Rollup 只是会合并你的代码 —— 没有任何浪费</strong>。所产生的包也可以更好的缩小。有人称之为 “作用域提升（scope hoisting）”。
其次，它把你导入的模块中的未使用代码移除。这被称为“（摇树优化）treeshaking”。
总之，Rollup 就是一个模块化的打包工具。
​</p>
<p>接下来我们进入源码，具体分析下 Rollup 的构建流程</p>
<h2 data-id="heading-12">Rollup 构建流程分析</h2>
<h3 data-id="heading-13">Rollup 源码结构</h3>
<pre><code class="copyable">
│  bundle.js // Bundle 打包器，在打包过程中会生成一个 bundle 实例，用于收集其他模块的代码，最后再将收集的代码打包到一起。
│  external-module.js // ExternalModule 外部模块，例如引入了 'path' 模块，就会生成一个 ExternalModule 实例。
│  module.js // Module 模块，module 实例。
│  rollup.js // rollup 函数，一切的开始，调用它进行打包。
│
├─ast // ast 目录，包含了和 AST 相关的类和函数
│      analyse.js // 主要用于分析 AST 节点的作用域和依赖项。
│      Scope.js // 在分析 AST 节点时为每一个节点生成对应的 Scope 实例，主要是记录每个 AST 节点对应的作用域。
│      walk.js // walk 就是递归调用 AST 节点进行分析。
│
├─finalisers
│      cjs.js
│      index.js
│
└─utils // 一些帮助函数
        map-helpers.js
        object.js
        promise.js
        replaceIdentifiers.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"></h3>
<h3 data-id="heading-15">Rollup 构建流程</h3>
<p><strong>我们以 index.js 入口文件，index 依赖了 foo.js,foo 依赖了 bar.js</strong></p>
<pre><code class="copyable">// index.js
import &#123; foo &#125; from "./foo";
foo()
var city = 'hangzhou'

function test() &#123;
    console.log('test')
&#125;

console.log(test())
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// foo.js
import &#123; bar &#125; from "./bar";
export function foo() &#123;
    console.log('foo')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// bar.js
export function bar() &#123;
    console.log('bar')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>debug 起来!!!</strong></p>
<pre><code class="copyable">// debug.js
const path = require('path')
const rollup = require('./lib/rollup')
// 入口文件的绝对路径
let entry = path.resolve(__dirname, 'src/main.js')
// 和源码有所不同，这里使用的是同步，增加可读性
rollup(entry, 'bundle.js')
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">1.new Bundle(), build()</h4>
<p>首先生成一个 Bundle 实例，也就是打包器。
然后执行 build 打包编译</p>
<pre><code class="copyable">// rollup.js
let Bundle = require('./bundle')
function rollup(entry, outputFileName) &#123;
    // Bundle 代表打包对象，里面包含所有的模块信息
    const bundle = new Bundle(&#123; entry &#125;)
    // 调用 build 方法开始进行编译
    bundle.build(outputFileName)
&#125;
module.exports = rollup
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>lib/bundle.js</strong>
根据入口路径出发（在 bundle 中，我们会首先统一处理下入口文件的后缀），去找到他的模块定义，在 fetchModule 中，会生成一个 module 实例
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae907bac3e54ce6b5a6db65f422dae1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们关注红框中的代码，会发现返回了一个 module
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6ee3482e5594042807654d47ca93ff9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">2.new Module()</h4>
<p>每个文件都是一个模块，每个模块都会有一个 Module 实例。
在 Module 实例中，会调用 acorn 库的 parse() 方法将代码解析成 AST。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae87d16f6921472f972d34bddbf93c3f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
对生成的 AST 进行分析<strong>analyse</strong>
我们先看一下入口文件 index.js 生成的 AST
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e498fbda3d4b2192d5c3c9912f68c9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e718a351ba6d42758ccbbe54ebb1dd7b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到 ast.body 是一个数组，分别对应 index.js 的五条语句
展开这个 ast 树如下：</p>
<pre><code class="copyable">&#123;
  "type": "Program",
  "start": 0,
  "end": 128,
  "body": [
    &#123;
      "type": "ImportDeclaration", // 导入声明
      "start": 0,
      "end": 31,
      "specifiers": [
        &#123;
          "type": "ImportSpecifier",
          "start": 9,
          "end": 12,
          "imported": &#123;
            "type": "Identifier",
            "start": 9,
            "end": 12,
            "name": "foo"
          &#125;,
          "local": &#123;
            "type": "Identifier",
            "start": 9,
            "end": 12,
            "name": "foo"
          &#125;
        &#125;
      ],
      "source": &#123;
        "type": "Literal",
        "start": 20,
        "end": 30,
        "value": "./foo.js",
        "raw": "\"./foo.js\""
      &#125;
    &#125;,
    &#123;
      "type": "ExpressionStatement",
      "start": 32,
      "end": 37,
      "expression": &#123;
        "type": "CallExpression",
        "start": 32,
        "end": 37,
        "callee": &#123;
          "type": "Identifier",
          "start": 32,
          "end": 35,
          "name": "foo"
        &#125;,
        "arguments": [],
        "optional": false
      &#125;
    &#125;,
    &#123;
      "type": "VariableDeclaration",
      "start": 38,
      "end": 59,
      "declarations": [
        &#123;
          "type": "VariableDeclarator",
          "start": 42,
          "end": 59,
          "id": &#123;
            "type": "Identifier",
            "start": 42,
            "end": 46,
            "name": "city"
          &#125;,
          "init": &#123;
            "type": "Literal",
            "start": 49,
            "end": 59,
            "value": "hangzhou",
            "raw": "'hangzhou'"
          &#125;
        &#125;
      ],
      "kind": "var"
    &#125;,
    &#123;
      "type": "FunctionDeclaration",
      "start": 61,
      "end": 104,
      "id": &#123;
        "type": "Identifier",
        "start": 70,
        "end": 74,
        "name": "test"
      &#125;,
      "expression": false,
      "generator": false,
      "async": false,
      "params": [],
      "body": &#123;
        "type": "BlockStatement",
        "start": 77,
        "end": 104,
        "body": [
          &#123;
            "type": "ExpressionStatement",
            "start": 83,
            "end": 102,
            "expression": &#123;
              "type": "CallExpression",
              "start": 83,
              "end": 102,
              "callee": &#123;
                "type": "MemberExpression",
                "start": 83,
                "end": 94,
                "object": &#123;
                  "type": "Identifier",
                  "start": 83,
                  "end": 90,
                  "name": "console"
                &#125;,
                "property": &#123;
                  "type": "Identifier",
                  "start": 91,
                  "end": 94,
                  "name": "log"
                &#125;,
                "computed": false,
                "optional": false
              &#125;,
              "arguments": [
                &#123;
                  "type": "Literal",
                  "start": 95,
                  "end": 101,
                  "value": "test",
                  "raw": "'test'"
                &#125;
              ],
              "optional": false
            &#125;
          &#125;
        ]
      &#125;
    &#125;,
    &#123;
      "type": "ExpressionStatement",
      "start": 106,
      "end": 125,
      "expression": &#123;
        "type": "CallExpression",
        "start": 106,
        "end": 125,
        "callee": &#123;
          "type": "MemberExpression",
          "start": 106,
          "end": 117,
          "object": &#123;
            "type": "Identifier",
            "start": 106,
            "end": 113,
            "name": "console"
          &#125;,
          "property": &#123;
            "type": "Identifier",
            "start": 114,
            "end": 117,
            "name": "log"
          &#125;,
          "computed": false,
          "optional": false
        &#125;,
        "arguments": [
          &#123;
            "type": "CallExpression",
            "start": 118,
            "end": 124,
            "callee": &#123;
              "type": "Identifier",
              "start": 118,
              "end": 122,
              "name": "test"
            &#125;,
            "arguments": [],
            "optional": false
          &#125;
        ],
        "optional": false
      &#125;
    &#125;
  ],
  "sourceType": "module"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过这个 AST 树，分析 **analyse **具体做了什么???
​</p>
<p><strong>第一步：分析当前模块导入【import】和导出【exports】模块，将引入的模块和导出的模块存储起来</strong>
this.imports = &#123;&#125;;//存放着当前模块所有的导入<br>
this.exports = &#123;&#125;;//存放着当前模块所有的导出</p>
<pre><code class="copyable">    this.imports = &#123;&#125;;//存放着当前模块所有的导入
    this.exports = &#123;&#125;;//存放着当前模块所有的导出
    this.ast.body.forEach(node => &#123;
      if (node.type === 'ImportDeclaration') &#123;// 说明这是一个 import 语句
        let source = node.source.value; // 从哪个模块导入的
        let specifiers = node.specifiers; // 导入标识符
        specifiers.forEach(specifier => &#123;
          const name = specifier.imported.name; //name
          const localName = specifier.local.name; //name
          //本地的哪个变量，是从哪个模块的的哪个变量导出的
          this.imports[localName] = &#123; name, localName, source &#125;
        &#125;);
        //&#125;else if(/^Export/.test(node.type))&#123; // 导出方法有很多
      &#125; else if (node.type === 'ExportNamedDeclaration') &#123; // 说明这是一个 exports 语句
        let declaration = node.declaration;//VariableDeclaration
        if (declaration.type === 'VariableDeclaration') &#123;
          let name = declaration.declarations[0].id.name;
          this.exports[name] = &#123;
            node, localName: name, expression: declaration
          &#125;
        &#125;
      &#125;
    &#125;);
    analyse(this.ast, this.code, this);//找到了_defines 和 _dependsOn
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打断点可以看到，foo 已经被存入 imports  =》** import &#123; foo &#125; from "./foo";  **
exports:&#123;&#125; 表示没有导出语句
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/550e6485d4124999a1ab6a7023d01ace~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第二步：analyse(this.ast, this.code, this); //找到_defines 和 _dependsOn</strong>
​</p>
<p>找出当前模块使用到了哪些变量
标记哪些变量时当前模块声明的，哪些变量是导入别的模块的变量
我们定义以下字段用来存放：
<strong>_defines: &#123; value: &#123;&#125; &#125;</strong>,//存放当前模块定义的所有的全局变量<br>
<strong>_dependsOn: &#123; value: &#123;&#125; &#125;,/</strong>/当前模块没有定义但是使用到的变量，也就是依赖的外部变量
<strong>_included: &#123; value: false, writable: true &#125;</strong>,//此语句是否已经被包含到打包结果中，防止重复打包
<strong>_source:</strong> &#123; value: magicString.snip(statement.start, statement.end) &#125; //magicString.snip 返回的还是 magicString 实例 clone
​</p>
<p>分析每个 AST 节点之间的作用域，构建 scope tree，</p>
<pre><code class="copyable">function analyse(ast, magicString, module) &#123;
    let scope = new Scope();//先创建一个模块内的全局作用域
    //遍历当前的所有的语法树的所有的顶级节点
    ast.body.forEach(statement => &#123;
    
        //给作用域添加变量 var function const let 变量声明
        function addToScope(declaration) &#123;
            var name = declaration.id.name;//获得这个声明的变量
            scope.add(name);
            if (!scope.parent) &#123;//如果当前是全局作用域的话
                statement._defines[name] = true;
            &#125;
        &#125;

        Object.defineProperties(statement, &#123;
            _defines: &#123; value: &#123;&#125; &#125;,//存放当前模块定义的所有的全局变量
            _dependsOn: &#123; value: &#123;&#125; &#125;,//当前模块没有定义但是使用到的变量，也就是依赖的外部变量
            _included: &#123; value: false, writable: true &#125;,//此语句是否已经 被包含到打包结果中了
            //start 指的是此节点在源代码中的起始索引,end 就是结束索引
            //magicString.snip 返回的还是 magicString 实例 clone
            _source: &#123; value: magicString.snip(statement.start, statement.end) &#125;
        &#125;);
        
        //这一步在构建我们的作用域链
        walk(statement, &#123;
            enter(node) &#123;
                let newScope;
                if (!node) return
                switch (node.type) &#123;
                    case 'FunctionDeclaration':
                        const params = node.params.map(x => x.name);
                        if (node.type === 'FunctionDeclaration') &#123;
                            addToScope(node);
                        &#125;
                        //如果遍历到的是一个函数声明，我会创建一个新的作用域对象
                        newScope = new Scope(&#123;
                            parent: scope,//父作用域就是当前的作用域
                            params
                        &#125;);
                        break;
                    case 'VariableDeclaration': //并不会生成一个新的作用域
                        node.declarations.forEach(addToScope);
                        break;
                &#125;
                if (newScope) &#123;//当前节点声明一个新的作用域
                    //如果此节点生成一个新的作用域，那么会在这个节点放一个_scope，指向新的作用域
                    Object.defineProperty(node, '_scope', &#123; value: newScope &#125;);
                    scope = newScope;
                &#125;
            &#125;,
            leave(node) &#123;
                if (node._scope) &#123;//如果此节点产出了一个新的作用域，那等离开这个节点，scope 回到父作用法域
                    scope = scope.parent;
                &#125;
            &#125;
        &#125;);
    &#125;);
    ast._scope = scope;
    //找出外部依赖_dependsOn
    ast.body.forEach(statement => &#123;
        walk(statement, &#123;
            enter(node) &#123;
                if (node._scope) &#123;
                    scope = node._scope;
                &#125; //如果这个节点放有一个 scope 属性，说明这个节点产生了一个新的作用域
                if (node.type === 'Identifier') &#123;
                    //从当前的作用域向上递归，找这个变量在哪个作用域中定义
                    const definingScope = scope.findDefiningScope(node.name);
                    if (!definingScope) &#123;
                        statement._dependsOn[node.name] = true;//表示这是一个外部依赖的变量
                    &#125;
                &#125;

            &#125;,
            leave(node) &#123;
                if (node._scope) &#123;
                    scope = scope.parent;
                &#125;

            &#125;
        &#125;);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断点可以看到**_defines 和 _dependsOn **分别存入了当前变量和引入的变量
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e3c7ea7496649a89e06458ab4c0762c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e32eb18e1f6242f8b31c9e240a1dd552~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>第三步：this.definitions = &#123;&#125;;</strong>
<strong>把全局变量的定义语句存放到 definitions 里</strong></p>
<pre><code class="copyable">// module.js
this.definitions = &#123;&#125;;//存放着所有的全局变量的定义语句
    this.ast.body.forEach(statement => &#123;
      Object.keys(statement._defines).forEach(name => &#123;
        //key 是全局变量名，值是定义这个全局变量的语句
        this.definitions[name] = statement;
      &#125;);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第四步：展开语句，展开当前模块的所有语句，把这些语句中定义的变量的语句都放到结果里</strong>
​</p>
<p>if (statement.type === 'ImportDeclaration') &#123;return&#125; 如果是导入声明语句，既 import &#123; foo &#125; from "./foo";这条语句我们是不需要的，return 掉</p>
<pre><code class="copyable">//展开这个模块里的语句，把些语句中定义的变量的语句都放到结果里
  expandAllStatements() &#123;
    let allStatements = [];
    this.ast.body.forEach(statement => &#123;
      if (statement.type === 'ImportDeclaration') &#123;return&#125;
      let statements = this.expandStatement(statement);
      allStatements.push(...statements);
    &#125;);
    return allStatements;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>**expandStatement：**找到当前节点依赖的变量，找到这些变量的声明语句。
这些语句可能是在当前模块声明的，也也可能是在导入的模块的声明的
然后放入结果里</p>
<pre><code class="copyable">
  expandStatement(statement) &#123;
    let result = [];
    const dependencies = Object.keys(statement._dependsOn);//外部依赖 [name]
    dependencies.forEach(name => &#123;
      //找到定义这个变量的声明节点，这个节点可以有在当前模块内，也可能在依赖的模块里
      let definition = this.define(name);
      result.push(...definition);
    &#125;);
    if (!statement._included) &#123;
      statement._included = true;//表示这个节点已经确定被纳入结果里了，以后就不需要重复添加了
      result.push(statement);
    &#125;
    return result;
  &#125;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>define: 找到定义这个变量的声明节点，这个节点可以有在当前模块内，也可能在依赖的模块里</strong>
<strong>const module = this.bundle.fetchModule(importData.source, this.path);</strong>
获取导入变量的模块</p>
<pre><code class="copyable">   define(name) &#123;
    //查找一下导入变量里有没有 name
    if (hasOwnProperty(this.imports, name)) &#123;
      const importData = this.imports[name];
      // 获取导入变量的模块
      const module = this.bundle.fetchModule(importData.source, this.path);
      // 这个 module 模块也有导入导出
      const exportData = module.exports[importData.name];
      // 返回这个导入模块变量的声明语句
      return module.define(exportData.localName);
    &#125; else &#123;
      //definitions 是对象,key 当前模块的变量名，值是定义这个变量的语句
      let statement = this.definitions[name];
      if (statement && !statement._included) &#123;
        return this.expandStatement(statement);
      &#125; else &#123;
        return [];
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/029457f6e6494618ac9eb26ec0ab34cf~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
​</p>
<p>this.statements 里就是所有我们分析标记之后返回的数组
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5aa46ecb2f54c2f9ca0d84c1577b739~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
​</p>
<p><strong>以上分析了很多，但总结来就是做了以下事情：</strong></p>
<ul>
<li>收集导入和导出变量</li>
<li>建立映射关系，方便后续使用</li>
<li>收集所有语句定义的变量</li>
<li>建立变量和声明语句之间的对应关系，方便后续使用</li>
<li>过滤 import 语句</li>
<li>删除关键词</li>
<li>输出语句时，判断变量是否为 import</li>
<li>如是需要递归再次收集依赖文件的变量</li>
<li>否则直接输出</li>
<li>构建依赖关系，创建作用域链，交由./src/ast/analyse.js 文件处理</li>
<li>在抽象语法树的每一条语句上挂载_source(源代码)、_defines(当前模块定义的变量)、_dependsOn(外部依赖的变量)、_included(是否已经包含在输出语句中)</li>
<li>收集每个语句上定义的变量，创建作用域链</li>
</ul>
<h4 data-id="heading-18">3.generate（）</h4>
<p>第一步：移除额外代码
例如从 foo.js 中引入的 foo() 函数代码是这样的：export function foo() &#123;&#125;。rollup 会移除掉 export，变    成 function foo() &#123;&#125;。因为它们就要打包在一起了，所以就不需要 export 了。
​</p>
<p>第二步：把 AST 节点的源码 addSource 到 magicString,这个操作本质上相当于拼字符串,
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/356d227e90c546b88424fd85937ce7e6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
第三步：**return magicString.toString() **。
返回合并后源代码</p>
<pre><code class="copyable">generate() &#123;
    let magicString = new MagicString.Bundle();
    this.statements.forEach(statement => &#123;
      const source = statement._source;
      if (statement.type === 'ExportNamedDeclaration') &#123;
        source.remove(statement.start, statement.declaration.start);
      &#125; 
      magicString.addSource(&#123;
        content: source,
        separator: '\n'
      &#125;);
    &#125;);
    return &#123; code: magicString.toString() &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后输出到'dist/bundle.js'中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6f17545de45400482e01a543faff851~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">小结</h3>
<p>简单来说，Rollup 构建其实就是做了以下几件事：</p>
<ul>
<li>获取入口文件的内容，包装成 module，生成抽象语法树</li>
<li>对入口文件抽象语法树进行依赖解析</li>
<li>生成最终代码</li>
<li>写入目标文件</li>
</ul>
<h2 data-id="heading-20">四、总结</h2>
<p>以上代码实现过程可以帮你简单的实现一个 rollup 打包流程，但也仅仅是对 rollup 源码进行了抽象，方便大家理解 rollup 打包的原理，其中很多细节没有写出来，如果感兴趣的话，可以深入阅读一下源码。</p>
<h2 data-id="heading-21">五、参考资料</h2>
<p><a href="https://zhuanlan.zhihu.com/p/372808332" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/372808332</a></p>
<p><a href="https://github.com/xitu/gold-miner/blob/master/TODO/rollup-interview.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></p>
<p><a href="https://blog.csdn.net/q411020382/article/details/108302906" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/q411020382/…</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3b384a65e13483294525d060b030453~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            