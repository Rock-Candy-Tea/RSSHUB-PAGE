
---
title: 'Webpack5学习 --- source-map｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://s3.jpg.cm/2021/08/01/I8Nt8G.png'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 18:26:27 GMT
thumbnail: 'https://s3.jpg.cm/2021/08/01/I8Nt8G.png'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们的代码通常运行在浏览器上时，是通过<strong>打包压缩</strong>的，也就是真实跑在浏览器上的代码，和我们编写的代码其实是有差异的;</p>
<p>那么当代码报错需要调试时(debug)，调试转换后的代码是很困难的。</p>
<p>因为对应的代码行号、列号和内容在编译前后肯定会不一致</p>
<p>当代码报错需要调试时(debug)，调试转换后的代码是很困难的</p>
<h2 data-id="heading-0">简介</h2>
<h3 data-id="heading-1">什么是source-map</h3>
<ol>
<li>
<p>source-map是从<code>已转换的代码</code>，映射到<code>原始的源文件</code></p>
<p>​--- 是编译前的代码和编译后的代码的映射文件</p>
<p>​    --- source-map文件组合上编译后的代码，通过浏览器可以反向推导出编译前的源文件</p>
</li>
<li>
<p>让浏览器可以重构原始源并在调试器中显示重建的原始源;</p>
<p>​ --- 如果浏览器支持<code>source-map</code>, 那么浏览器在调试的时候会自动将错误映射到编译前的文件</p>
<p>​</p>
</li>
</ol>
<h3 data-id="heading-2">如何开启source-map</h3>
<ol>
<li>
<p>根据源文件，生成source-map文件，webpack在打包时，可以通过配置生成source-map;</p>
<p>--- 如 配置 <code>devtool</code>为<code>source-map</code></p>
</li>
<li>
<p>第二步:在转换后的代码，最后添加一个注释，它指向sourcemap</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. source-map 的文件名一般为 xxx.js.map 其内容看起来是一个对象，map文件是不支持注释的 </span>

<span class="hljs-comment">// 2. 在打包后的文件（如bundle.js）的最后一行，添加该文件所对应的source-map文件</span>
<span class="hljs-comment">//    浏览器会根据我们的注释，查找相应的source-map，并且根据source-map还原我们的代码，方便进行调试</span>

<span class="hljs-comment">// 3. source-map注释格式是固定的 需要以//# 开头</span>
<span class="hljs-comment">//# sourceMappingURL=common.bundle.js.map</span>

<span class="hljs-comment">// 4. 不单单js可以有source-map, css也可以有自己的source-map</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-3">source-map各字段含义</h3>
<p>具体信息可以参考MDN中对于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdevtool%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/devtool/" ref="nofollow noopener noreferrer">source-map</a>的介绍</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// source-map文件是不支持注释的，此处添加注释是为了便于理解</span>
<span class="hljs-comment">// 为了便于阅读，其中部分属性的值有做适度删减</span>
&#123;
  <span class="hljs-comment">// source-map有3个版本</span>
  <span class="hljs-comment">/*
  第一版： source-map生成的文件带下是原始文件的10倍
  第二版：source-map生成的文件带下是原始文件的5倍   是第一版的50%
  第三版：source-map生成的文件带下是原始文件的2.5倍  是第二版的50%
  */</span>
  <span class="hljs-string">"version"</span>: <span class="hljs-number">3</span>,
    
  <span class="hljs-comment">// 从哪些文件转换过来的source-map和打包的代码(最初始的文件)</span>
  <span class="hljs-string">"sources"</span>: [
    <span class="hljs-string">"webpack://webpack-demo/./src/js/format.js"</span>, 
    <span class="hljs-string">"webpack://webpack-demo/./src/js/math.js"</span>, 
    <span class="hljs-string">"webpack://webpack-demo/webpack/bootstrap"</span>,
    <span class="hljs-string">"webpack://webpack-demo/./src/index.js"</span>
  ],
    
  <span class="hljs-comment">// 转换前的变量和属性名称，如果是development这类不需要转换名称的编译，names的值就是[]</span>
  <span class="hljs-string">"names"</span>: [
    <span class="hljs-string">"module"</span>,
    <span class="hljs-string">"exports"</span>, 
    <span class="hljs-string">"num1"</span>, 
<span class="hljs-string">"__webpack_module_cache__"</span>, 
    <span class="hljs-string">"__webpack_require__"</span> 
    ],
    
  <span class="hljs-comment">// source-map用来和源文件映射的信息(比如位置信息等)，一串base64 VLQ(veriable- length quantity可变长度值)编码 </span>
  <span class="hljs-string">"mappings"</span>: <span class="hljs-string">"mCAAAA,EAAOC,QAAQC,MAAQ,IAAKC,QAAQC,IAAI,W,0ECAjC,MAAMC,EAAM,CAACC,EAAMC,IAASD,EAAOC,ICCtCC,EAA2B,GAG/B,SAASC,EAAoBC,GAE5B,IAAIC,EAAeH,EAAyBE,GAC5C,QAAqBE,IAAjBD,EACH,OAAOA,EAAaV,QAGrB,IAAID,EAASQ,EAAyBE,GAAY,CAGjDT,QAAS,IAOV,OAHAY,EAAoBH,GAAUV,EAAQA,EAAOC,QAASQ,GAG/CT,EAAOC,QCpBfQ,EAAoBK,EAAI,SAASb,EAASc,GACzC,IAAI,IAAIC,KAAOD,EACXN,EAAoBQ,EAAEF,EAAYC,KAASP,EAAoBQ,EAAEhB,EAASe,IAC5EE,OAAOC,eAAelB,EAASe,EAAK,CAAEI,YAAY,EAAMC,IAAKN,EAAWC,MCJ3EP,EAAoBQ,EAAI,SAASK,EAAKC,GAAQ,OAAOL,OAAOM,UAAUC,eAAeC,KAAKJ,EAAKC,ICC/Fd,EAAoBkB,EAAI,SAAS1B,GACX,oBAAX2B,QAA0BA,OAAOC,aAC1CX,OAAOC,eAAelB,EAAS2B,OAAOC,YAAa,CAAEC,MAAO,WAE7DZ,OAAOC,eAAelB,EAAS,aAAc,CAAE6B,OAAO,K,qCCJvD,MAAMC,EAAO,EAAQ,KAErB,UAEA5B,QAAQC,IAAI2B,EAAK1B,IAAI,EAAE,I"</span>,
    
  <span class="hljs-comment">// 打包后的文件(浏览器加载的文件)</span>
  <span class="hljs-string">"file"</span>: <span class="hljs-string">"js/bundle.js"</span>,
    
   <span class="hljs-comment">// 转换前的具体代码信息 --- 便于在点击的错误信息的时候，可以在sources标签页下查看对应的源代码</span>
  <span class="hljs-string">"sourcesContent"</span>: [<span class="hljs-string">"module.exports.print = () =>console.log('format')"</span>, <span class="hljs-string">"export const sum = (num1, num2) => num1 + num2"</span>, <span class="hljs-string">"// The module cache\nvar __webpack_module_cache__ = &#123;&#125;;\n\n// The require function\nfunction __webpack_require__(moduleId) &#123;\n\t// Check if module is in cache\n\tvar cachedModule = __webpack_module_cache__[moduleId];\n\tif (cachedModule !== undefined) &#123;\n\t\treturn cachedModule.exports;\n\t&#125;\n\t// Create a new module (and put it into the cache)\n\tvar module = __webpack_module_cache__[moduleId] = &#123;\n\t\t// no module.id needed\n\t\t// no module.loaded needed\n\t\texports: &#123;&#125;\n\t&#125;;\n\n\t// Execute the module function\n\t__webpack_modules__[moduleId](module, module.exports, __webpack_require__);\n\n\t// Return the exports of the module\n\treturn module.exports;\n&#125;\n\n"</span>, <span class="hljs-string">"// define getter functions for harmony exports\n__webpack_require__.d = function(exports, definition) &#123;\n\tfor(var key in definition) &#123;\n\t\tif(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) &#123;\n\t\t\tObject.defineProperty(exports, key, &#123; enumerable: true, get: definition[key] &#125;);\n\t\t&#125;\n\t&#125;\n&#125;;"</span>, <span class="hljs-string">"__webpack_require__.o = function(obj, prop) &#123; return Object.prototype.hasOwnProperty.call(obj, prop); &#125;"</span>, <span class="hljs-string">"// define __esModule on exports\n__webpack_require__.r = function(exports) &#123;\n\tif(typeof Symbol !== 'undefined' && Symbol.toStringTag) &#123;\n\t\tObject.defineProperty(exports, Symbol.toStringTag, &#123; value: 'Module' &#125;);\n\t&#125;\n\tObject.defineProperty(exports, '__esModule', &#123; value: true &#125;);\n&#125;;"</span>, <span class="hljs-string">"import format from './js/format'\nconst math = require('./js/math')\n\nformat.print()\n\nconsole.log(math.sum(2,5))"</span>],
    
  <span class="hljs-comment">// 所有的sources相对的根目录</span>
  <span class="hljs-string">"sourceRoot"</span>: <span class="hljs-string">""</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">eval可选值</h2>
<p>webpack为我们提供了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdevtool%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/devtool/" ref="nofollow noopener noreferrer">非常多的选项</a>(目前是26个)，来处理source-map</p>
<h3 data-id="heading-5">不生成source-map</h3>





















<table><thead><tr><th>值</th><th>说明</th></tr></thead><tbody><tr><td>false</td><td>不使用source-map，也就是没有任何和source-map相关的内容</td></tr><tr><td>(none)</td><td>production模式下的默认值，不生成source-map<br>(none)不是一个具体的值，其仅仅表示的是省略devtool选项</td></tr><tr><td>eval</td><td>development模式下的默认值，不生成source-map<br>但是它会在eval执行的代码中，添加 //# sourceURL=<br>它会被浏览器在执行时解析，并且在调试面板中生成对应的一些文件目录，方便我们调试代码</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在development模式下，每一个模块后会存在类似于//# sourceURL=webpack://webpack-demo/./src/js/format.js?"的代码</span>
<span class="hljs-comment">// 用以标明打包后的代码对应的源文件路径</span>
<span class="hljs-built_in">eval</span>(<span class="hljs-string">"module.exports.print = () =>console.log('format')\n\n//# sourceURL=webpack://webpack-demo/./src/js/format.js?"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">source-map</h3>
<p>生成一个独立的source-map文件，并且在bundle文件中有一个注释，指向source-map文件</p>
<p>开发工具会根据这个注释找到source-map文件，并且解析</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//# sourceMappingURL=bundle.js.map</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">eval-source-map</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 代码会使用eval函数包裹，不会生成独立的source-map</span>
<span class="hljs-comment">// source-map会以base64编码的形式嵌入到每一个打包后的代码后边</span>
<span class="hljs-built_in">eval</span>(<span class="hljs-string">"module.exports.print = () =>console.log('format')//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly93ZWJwYWNrLWRlbW8vLi9zcmMvanMvZm9ybWF0LmpzPzhlNDIiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsb0JBQW9CIiwiZmlsZSI6Ii4vc3JjL2pzL2Zvcm1hdC5qcy5qcyIsInNvdXJjZXNDb250ZW50IjpbIm1vZHVsZS5leHBvcnRzLnByaW50ID0gKCkgPT5jb25zb2xlLmxvZygnZm9ybWF0JykiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/js/format.js\n"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">inline-source-map</h3>
<p>会生成sourcemap，但是source-map会在base64编码后以DataUrl添加到bundle文件的后面</p>
<h3 data-id="heading-9">cheap-source-map</h3>
<p>会生成sourcemap，但是会更加高效一些(cheap低开销)，因为它没有生成列映射(Column Mapping)</p>
<p>因为在开发中，我们只需要行信息通常就可以定位到错误了</p>
<p><img src="https://s3.jpg.cm/2021/08/01/I8Nt8G.png" alt="I8Nt8G.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">cheap-module-source-map</h3>
<p>会生成sourcemap，类似于cheap-source-map，但是对源自loader的sourcemap处理会更好</p>
<p>即我们的一些模块会经过loader的处理，即会对我们的代码进行相应的转换</p>
<p>如果使用<code>cheap-source-map</code>，那么代码只能被还原到经过loader处理后的代码</p>
<p>如果使用的是<code>cheap-module-source-map</code>，代码会还原到经过loader处理前的diam</p>
<p><img src="https://s3.jpg.cm/2021/08/01/I8NNk4.png" alt="I8NNk4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">hidden-source-map</h3>
<p>会生成sourcemap，但是不会对source-map文件进行引用</p>
<p>相当于删除了打包文件中对sourcemap的引用注释</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 下边这行注释被删除了</span>
<span class="hljs-comment">//# sourceMappingURL=bundle.js.map</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们需要调试，在对应文件末尾手动添加source-map</p>
<h3 data-id="heading-12">nosources-source-map</h3>
<p>会生成sourcemap，但是生成的sourcemap只有错误信息的提示，不会生成源代码文件</p>
<p><img src="https://s3.jpg.cm/2021/08/01/I8No8S.png" alt="I8No8S.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">值的组合</h2>
<p>事实上，webpack提供给我们的26个值，是可以进行多组合的。</p>
<pre><code class="hljs language-markdown copyable" lang="markdown"> # inline-|hidden-|eval:三个值时三选一
 # nosources:可选值
 # cheap可选值，并且可以跟随module的值;
 [<span class="hljs-string">inline-|hidden-|eval-</span>][<span class="hljs-symbol">nosources-</span>][<span class="hljs-string">cheap-[module-</span>]]source-map
 # 此外 可选值还有 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">none</span>></span></span>(不写) 和 eval
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在开发和测试阶段，推荐使用 source-map或者cheap-module-source-map</p>
<p>在发布和生产阶段，推荐使用false或<code><none></code></p></div>  
</div>
            