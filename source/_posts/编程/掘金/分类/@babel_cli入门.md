
---
title: '@babel_cli入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2593'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 17:45:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=2593'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">初始化一个项目</h2>
<pre><code class="hljs language-bash copyable" lang="bash">mkdir babeljs
<span class="hljs-built_in">cd</span> babeljs
npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">安装<code>@babel/cli</code>和<code>@babel/core</code></h3>
<p>注意是开发依赖：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D @babel/cli @babel/core
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照官方的说法：如果不手动指定安装<code>@babel/core</code>，npx会安装babel6.x。</p>
<h2 data-id="heading-2">创建一个<code>es6</code>文件</h2>
<pre><code class="hljs language-bash copyable" lang="bash">cat <<<span class="hljs-string">EOF > 01.js
 const a = 0
 const b = '1'
 export &#123; a &#125;
 export default b
EOF</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">用npx跑一下</h2>
<pre><code class="hljs language-bash copyable" lang="bash">% npx babel 01.js      
const a = 0;
const b = <span class="hljs-string">'1'</span>;
<span class="hljs-built_in">export</span> &#123; a &#125;;
<span class="hljs-built_in">export</span> default b;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很贴心，给每行都加了分号。</p>
<h2 data-id="heading-4">使用presets</h2>
<p>安装一个大家都极为熟悉的npm包：<code>@babel/preset-env</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D @babel/preset-env
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在npx指定加载这个preset：</p>
<pre><code class="hljs language-bash copyable" lang="bash">% npx babel 01.js --presets=@babel/preset-env 
<span class="hljs-string">"use strict"</span>;

Object.defineProperty(exports, <span class="hljs-string">"__esModule"</span>, &#123;
  value: <span class="hljs-literal">true</span>
&#125;);
exports[<span class="hljs-string">"default"</span>] = exports.a = void 0;
var a = 0;
exports.a = a;
var b = <span class="hljs-string">'1'</span>;
var _default = b;
exports[<span class="hljs-string">"default"</span>] = _default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就很熟悉的味道。</p>
<h3 data-id="heading-5">支持JSX</h3>
<p>先改一下<code>01.js</code>的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-number">0</span>
<span class="hljs-keyword">const</span> b = <span class="hljs-string">'1'</span>
<span class="hljs-keyword">const</span> c = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="hljs-keyword">export</span> &#123; a, c &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意新增了变量c，返回一个jsx节点。</p>
<p>如果我们还使用之前的编译命令，就会报错了，因为语法解析认为这是错误的js代码：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">%</span><span class="bash"> npx babel 01.js --presets=@babel/preset-env</span>                                   
SyntaxError: /Users/kema/git/exp2fun/babeljs/01.js: Support for the experimental syntax 'jsx' isn't currently enabled (3:11):

  1 | const a = 0
  2 | const b = '1'
<span class="hljs-meta">></span><span class="bash"> 3 | const c = <h1>Hello</h1></span>
    |           ^
  4 | export &#123; a, c &#125;
  5 | export default b
  6 |

Add @babel/preset-react (https://git.io/JfeDR) to the 'presets' section of your Babel config to enable transformation.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照提示，安装<code>@babel/preset-react</code>并执行：</p>
<pre><code class="hljs language-shell copyable" lang="shell"> npx babel 01.js --presets=@babel/preset-env,@babel/preset-react
"use strict";

Object.defineProperty(exports, "__esModule", &#123;
  value: true
&#125;);
exports["default"] = exports.c = exports.a = void 0;
var a = 0;
exports.a = a;
var b = '1';
<span class="hljs-meta">#</span><span class="bash"> 所以页面顶部要先 import React from <span class="hljs-string">'react'</span></span>
var c = /*#__PURE__*/React.createElement("h1", null, "Hello");
exports.c = c;
var _default = b;
exports["default"] = _default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，这里的变量c被转成了<code>react</code>组件。</p>
<p>顾名思义，<code>@babel/preset-react</code>是转react组件，你猜有没有<code>@babel/preset-vue</code>？</p>
<h3 data-id="heading-6">jsx -> vue</h3>
<p>有但不叫这个名字，而是<code>@vue/babel-preset-jsx</code>:</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm i -D @vue/babel-preset-jsx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>期待一下吧：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">%</span><span class="bash"> npx babel 01.js --presets=@babel/preset-env,@vue/babel-preset-jsx</span>
"use strict";

Object.defineProperty(exports, "__esModule", &#123;
  value: true
&#125;);
exports["default"] = exports.c = exports.a = void 0;
var a = 0;
exports.a = a;
var b = '1';
var c = h("h1", ["Hello"]);
exports.c = c;
var _default = b;
exports["default"] = _default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完美。</p>
<p>通过上面的几个小栗子能看到，在不同preset的加持下，jsx可以转成不同框架下的组件。</p>
<p>来看一下jsx在react下的完整形态：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-number">0</span>
<span class="hljs-keyword">const</span> b = <span class="hljs-string">'1'</span>
<span class="hljs-keyword">const</span> c = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
<span class="hljs-keyword">export</span> &#123; a, c &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> b
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">%</span><span class="bash"> npx babel 01.js --presets=@babel/preset-env,@babel/preset-react</span>  
"use strict";

Object.defineProperty(exports, "__esModule", &#123;
  value: true
&#125;);
exports["default"] = exports.c = exports.a = void 0;

var _react = _interopRequireDefault(require("react"));

function _interopRequireDefault(obj) &#123; return obj && obj.__esModule ? obj : &#123; "default": obj &#125;; &#125;

var a = 0;
exports.a = a;
var b = '1';

var c = /*#__PURE__*/_react["default"].createElement("h1", null, "Hello");

exports.c = c;
var _default = b;
exports["default"] = _default;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">plugins</h2>
<p>babel的插件原理和使用还是很好理解的，而且官方插件就很丰富。日常的话，当伸手党就可以。</p>
<p>这里拿一个官方插件<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Fbabel-plugin-proposal-decorators" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/babel-plugin-proposal-decorators" ref="nofollow noopener noreferrer"><code>@babel/plugin-proposal-decorators</code></a>简单做个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 02.js</span>
@annotation
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">annotation</span>(<span class="hljs-params">target</span>) </span>&#123;
  target.annotated = <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置插件的时候，插件参数通过命令行就不好去配置了，所以这里我们用<code>.babelrc</code>来配置转换插件及参数：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"plugins"</span>: [
    [
      <span class="hljs-string">"@babel/plugin-proposal-decorators"</span>,
      &#123;
        <span class="hljs-attr">"decoratorsBeforeExport"</span>: <span class="hljs-literal">true</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">%</span><span class="bash"> npx babel 02.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转出来的代码很多，基本上都是polyfill的操作。</p>
<p>当然也可以配合<code>presets</code>参数使用</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx babel 02.js --presets=@babel/preset-env
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转成es5，node就可以直接用了。</p>
<h2 data-id="heading-8">more</h2>
<p>更多配置项说明，请见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2Fbabel-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/babel-cli" ref="nofollow noopener noreferrer">官方文档</a>。</p></div>  
</div>
            