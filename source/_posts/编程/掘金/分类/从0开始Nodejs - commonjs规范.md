
---
title: '从0开始Node.js - common.js规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf67aed7d7e483c9e04a890020ca387~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 03:19:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf67aed7d7e483c9e04a890020ca387~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>开始之前，我们先在本地新建一个目录，然后</li>
</ul>
<pre><code class="copyable">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成一个包含package.json的目录结构，然后在目录下新建一个index.js作为入口js文件。新建一个module目录包含index.js及lib.js文件。
之后的目录结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf67aed7d7e483c9e04a890020ca387~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>首先我们需要知道的是common.js规范的require是会引入js并 <strong>执行</strong></li>
</ul>
<p>下面是个简单的demo:
module/index.js文件如下：</p>
<pre><code class="copyable">console.log('start');
require('./lib');
console.log('end');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module/lib.js文件如下：</p>
<pre><code class="copyable">console.log('lib');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在控制台执行 node module/index.js 结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da0bf4d7cc03434996c89894d6f58c2d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然lib.js被引入并被执行了。</p>
<ul>
<li>其次是require函数是有返回值的</li>
</ul>
<p>我们修改一下上面的代码如下</p>
<pre><code class="copyable">console.log('start');
const res = require('./lib');
console.log('libres', res);
console.log('end');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再重新执行代码得到的输出结果为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cabd7cfc0ad74a0fa5c2a52ac406dc18~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到reqiure('./lib.)得到的返回值是一个空对象。
下面问题就来了，如果我希望得到非空的返回对象应该怎么做？</p>
<ul>
<li>exports</li>
</ul>
<p>node.js提供了输出关键字 exports 。
我们如下修改下lib.js代码</p>
<pre><code class="copyable">console.log('lib');
exports.lib = 'lib'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次用node执行module目录下面的index.js。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa065dfb110e45ccbfad744082e44b05~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到require的返回res是一个对象，包含了lib属性。
当然我们还可以exports输出更多的其他类型的变量。</p>
<pre><code class="copyable">console.log('lib');
exports.lib = 'lib'
exports.obj = &#123; a: 1, b: 2 &#125;;
exports.fun = (a) => console.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台打印的结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1babe84d4d7468fa19340c6f3d59957~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么exports输出的是对象还是是对象的引用呢？即reqiure得到的对象修改会影响对象的本身吗？测试一下,如下修改module目录下的lib.js和index.js。
index.js</p>
<pre><code class="copyable">console.log('start');
const res = require('./lib');
res.obj2 = &#123; c: 1, d: 2 &#125;
console.log('end');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lib.js</p>
<pre><code class="copyable">console.log('lib');
exports.lib = 'lib'
exports.obj = &#123; a: 1, b: 2 &#125;;
exports.fun = (a) => console.log(a)

setTimeout(() => &#123; console.log('lib-exports', exports), 1000 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>node module/index.js控制台输出如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4917b1ae68bd4926bf70745932a8ed2e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到exports和require之间传递的是对象的引用。require对象的修改会影响exports对象。</p>
<ul>
<li>module.exports</li>
</ul>
<p>如果不想导出的始终是个对象。那么可以使用module.exports导出。
lib.js</p>
<pre><code class="copyable">console.log('lib');
exports.lib = 'lib'
exports.obj = &#123; a: 1, b: 2 &#125;;
exports.fun = (a) => console.log(a);
module.exports = () => &#123; console.log('Node.js') &#125;;

setTimeout(() => &#123; console.log('lib-exports', exports), 1000 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module/index.js</p>
<pre><code class="copyable">module/index.js
console.log('start');
const res = require('./lib');
console.log('libres', res);
res.obj2 = &#123; c: 1, d: 2 &#125;
console.log('end');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e168229625bf42b68137355589ac3baf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到res打印的结果不再是个object而是一个function。
而同时index.js里面对res添加的属性obj2也不会添加到lib里面的exports对象上。</p>
<p>在浏览器端，webpack打包代码时是支持require命令的。那么看下webpack是如何实现require的。
首先安装webpack和webpack-cli。</p>
<pre><code class="copyable">npm install webpack webpack-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的package.json文件如下</p>
<pre><code class="copyable">&#123;
  "name": "nodejs-start-from-0",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "dependencies": &#123;&#125;,
  "devDependencies": &#123;
    "webpack": "^5.37.1",
    "webpack-cli": "^4.7.0"
  &#125;,
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "keywords": [],
  "author": "",
  "license": "ISC"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意安装的webpack和webpack-cli版本，此版本应该是2021年5月份左右最新的版本
然后执行如下命令：</p>
<pre><code class="copyable">webpack ./index.js --devtool source-map  --mode development --target node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果在dist目录下的main.js文件中</p>
<pre><code class="copyable">/******/ (() => &#123; // webpackBootstrap
/******/ var __webpack_modules__ = (&#123;

/***/ "./lib.js":
/*!****************!*\
  !*** ./lib.js ***!
  \****************/
/***/ ((module, exports) => &#123;

console.log('lib');
exports.lib = 'lib'
exports.obj = &#123; a: 1, b: 2 &#125;;
exports.fun = (a) => console.log(a);
module.exports = () => &#123; console.log('Node.js') &#125;;

setTimeout(() => &#123; console.log('lib-exports', exports), 1000 &#125;)

/***/ &#125;)

/******/ &#125;);
/************************************************************************/
/******/ // The module cache
/******/ var __webpack_module_cache__ = &#123;&#125;;
/******/ 
/******/ // The require function
/******/ function __webpack_require__(moduleId) &#123;
/******/ // Check if module is in cache
/******/ var cachedModule = __webpack_module_cache__[moduleId];
/******/ if (cachedModule !== undefined) &#123;
/******/ return cachedModule.exports;
/******/ &#125;
/******/ // Create a new module (and put it into the cache)
/******/ var module = __webpack_module_cache__[moduleId] = &#123;
/******/ // no module.id needed
/******/ // no module.loaded needed
/******/ exports: &#123;&#125;
/******/ &#125;;
/******/ 
/******/ // Execute the module function
/******/ __webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 
/******/ // Return the exports of the module
/******/ return module.exports;
/******/ &#125;
/******/ 
/************************************************************************/
var __webpack_exports__ = &#123;&#125;;
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => &#123;
/*!******************!*\
  !*** ./index.js ***!
  \******************/
console.log('start');
const res = __webpack_require__(/*! ./lib */ "./lib.js");
console.log('libres', res);
res.obj2 = &#123; c: 1, d: 2 &#125;
console.log('end');
&#125;)();

/******/ &#125;)()
;
//# sourceMappingURL=main.js.map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到lib.js被放在了__webpack_modules__对象中，我们写在lib.js里面的代码被放在key为'lib.js'的属性里面。
然后在index.js里面通过执行</p>
<pre><code class="copyable">const res = __webpack_require__(/*! ./lib */ "./lib.js");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入的lib.js。
下面看看__webpack_require__的实现</p>
<pre><code class="copyable">/******/ function __webpack_require__(moduleId) &#123;
/******/ // Check if module is in cache
/******/ var cachedModule = __webpack_module_cache__[moduleId];
/******/ if (cachedModule !== undefined) &#123;
/******/ return cachedModule.exports;
/******/ &#125;
/******/ // Create a new module (and put it into the cache)
/******/ var module = __webpack_module_cache__[moduleId] = &#123;
/******/ // no module.id needed
/******/ // no module.loaded needed
/******/ exports: &#123;&#125;
/******/ &#125;;
/******/ 
/******/ // Execute the module function
/******/ __webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 
/******/ // Return the exports of the module
/******/ return module.exports;
/******/ &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从main.js里面拷出来
前面是判断缓存。后面__webpack_modules__[moduleId](module, module.exports, <strong>webpack_require</strong>);这一句其实就是执行的lib.js。同时传入了module和module.exports。
在lib.js执行的部分可以看到：</p>
<pre><code class="copyable">module.exports = () => &#123; console.log('Node.js') &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports最终被module.exports覆盖成了这个。所以输出的是module.exports的这个function。</p>
<p>以上。</p></div>  
</div>
            