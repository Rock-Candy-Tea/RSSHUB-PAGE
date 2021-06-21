
---
title: '前端构建工具的新宠--vite2.x'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99180aedf4fe4948acb5efb92d440120~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 00:46:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99180aedf4fe4948acb5efb92d440120~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">vite的简介</h3>
<p>vite它是法语单词‘轻快’的意思。它和我们以前使用Vue-cli的作用基本相同，都是项目<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>初始化</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;初始化&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">初</span><span class="mord cjk_fallback" style="color:#13c078;">始</span><span class="mord cjk_fallback" style="color:#13c078;">化</span></span></span></span></span></span> <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>构建工具</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;构建工具&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">构</span><span class="mord cjk_fallback" style="color:#13c078;">建</span><span class="mord cjk_fallback" style="color:#13c078;">工</span><span class="mord cjk_fallback" style="color:#13c078;">具</span></span></span></span></span></span>，相当于Vue项目构建的第二代产品，是个升级版本，当然它也包含了项目的编译功能，不过目前vite不仅仅支持vue的项目构建，还支持react,react-ts等等项目的构建。值得一提的是它的<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>生产环境</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;生产环境&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">生</span><span class="mord cjk_fallback" style="color:#13c078;">产</span><span class="mord cjk_fallback" style="color:#13c078;">环</span><span class="mord cjk_fallback" style="color:#13c078;">境</span></span></span></span></span></span>的打包用的是<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mi>R</mi><mi>o</mi><mi>l</mi><mi>l</mi><mi>u</mi><mi>p</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;Rollup&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord" style="color:#13c078;"><span class="mord mathnormal" style="margin-right:0.00773em;color:#13c078;">R</span><span class="mord mathnormal" style="color:#13c078;">o</span><span class="mord mathnormal" style="margin-right:0.01968em;color:#13c078;">l</span><span class="mord mathnormal" style="margin-right:0.01968em;color:#13c078;">l</span><span class="mord mathnormal" style="color:#13c078;">u</span><span class="mord mathnormal" style="color:#13c078;">p</span></span></span></span></span></span>来进行打包。</p>
<blockquote>
<p>Rollup是JavaScriptd的模块bundler(打包器)，可以将一小段代码编译为更大或更复杂的内容，例如库或应用程序。</p>
</blockquote>
<h3 data-id="heading-1">vite的进一步了解</h3>
<h4 data-id="heading-2">简单的了解一下ES Module</h4>
<p>在浏览器支持 ES 模块之前，没有 JavaScript 的原生机制可以让开发者以模块化的方式开发。这也正是 “打包” 这个概念出现的原因：使用工具抓取、处理并将我们的源码模块串联成可以在浏览器中运行的文件。</p>
<blockquote>
<p>而module sciprt允许在浏览器中直接运行原生支持模块,当遇见import依赖时，会直接发起http请求对应的模块文件。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"module"</span>>
   <span class="hljs-comment">// index.js可以通过export导出模块，也可以在其中继续使用import加载其他依赖 </span>
    <span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span>  ./index.js 
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">vite的特点</h4>
<ol>
<li>
<p>主打特点就是轻快的<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>冷服务启动</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;冷服务启动&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">冷</span><span class="mord cjk_fallback" style="color:#13c078;">服</span><span class="mord cjk_fallback" style="color:#13c078;">务</span><span class="mord cjk_fallback" style="color:#13c078;">启</span><span class="mord cjk_fallback" style="color:#13c078;">动</span></span></span></span></span></span>，使用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mtext>原生</mtext><mi>E</mi><mi>S</mi><mn>6</mn><mi>i</mi><mi>m</mi><mi>p</mi><mi>o</mi><mi>r</mi><mi>t</mi><mtext>的形式</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;原生ES6 import的形式&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">原</span><span class="mord cjk_fallback" style="color:#13c078;">生</span><span class="mord mathnormal" style="margin-right:0.05764em;color:#13c078;">E</span><span class="mord mathnormal" style="margin-right:0.05764em;color:#13c078;">S</span><span class="mord" style="color:#13c078;">6</span><span class="mord mathnormal" style="color:#13c078;">i</span><span class="mord mathnormal" style="color:#13c078;">m</span><span class="mord mathnormal" style="color:#13c078;">p</span><span class="mord mathnormal" style="color:#13c078;">o</span><span class="mord mathnormal" style="margin-right:0.02778em;color:#13c078;">r</span><span class="mord mathnormal" style="color:#13c078;">t</span><span class="mord cjk_fallback" style="color:#13c078;">的</span><span class="mord cjk_fallback" style="color:#13c078;">形</span><span class="mord cjk_fallback" style="color:#13c078;">式</span></span></span></span></span></span>，【浏览器解析 imports，利用了 type="module" 功能，然后拦截浏览器发出的 ES imports 请求并做相应处理】<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>在开发预览中，它是不进行打包的</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;在开发预览中，它是不进行打包的&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">在</span><span class="mord cjk_fallback" style="color:#13c078;">开</span><span class="mord cjk_fallback" style="color:#13c078;">发</span><span class="mord cjk_fallback" style="color:#13c078;">预</span><span class="mord cjk_fallback" style="color:#13c078;">览</span><span class="mord cjk_fallback" style="color:#13c078;">中</span><span class="mord cjk_fallback" style="color:#13c078;">，</span><span class="mord cjk_fallback" style="color:#13c078;">它</span><span class="mord cjk_fallback" style="color:#13c078;">是</span><span class="mord cjk_fallback" style="color:#13c078;">不</span><span class="mord cjk_fallback" style="color:#13c078;">进</span><span class="mord cjk_fallback" style="color:#13c078;">行</span><span class="mord cjk_fallback" style="color:#13c078;">打</span><span class="mord cjk_fallback" style="color:#13c078;">包</span><span class="mord cjk_fallback" style="color:#13c078;">的</span></span></span></span></span></span>。</p>
</li>
<li>
<p>开发中<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>热更新</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;热更新&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">热</span><span class="mord cjk_fallback" style="color:#13c078;">更</span><span class="mord cjk_fallback" style="color:#13c078;">新</span></span></span></span></span></span>，【Vite 的是通过<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mi>W</mi><mi>e</mi><mi>b</mi><mi>S</mi><mi>o</mi><mi>c</mi><mi>k</mi><mi>e</mi><mi>t</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;WebSocket&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord mathnormal" style="margin-right:0.13889em;color:#13c078;">W</span><span class="mord mathnormal" style="color:#13c078;">e</span><span class="mord mathnormal" style="color:#13c078;">b</span><span class="mord mathnormal" style="margin-right:0.05764em;color:#13c078;">S</span><span class="mord mathnormal" style="color:#13c078;">o</span><span class="mord mathnormal" style="color:#13c078;">c</span><span class="mord mathnormal" style="margin-right:0.03148em;color:#13c078;">k</span><span class="mord mathnormal" style="color:#13c078;">e</span><span class="mord mathnormal" style="color:#13c078;">t</span></span></span></span></span></span>  来实现热更新通信，当代码改动以后，通过 websocket 仅向浏览器推送改动的文件。因此 Vite 本地热更新的速度不会受项目的大小影响太多，在大型项目中本地开发速度快。Vite 的客户端热更新代码是在 app.vue 文件编译过程中，将代码注入进去的。】<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>只要一保存，预览结果就会更新</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;只要一保存，预览结果就会更新&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">只</span><span class="mord cjk_fallback" style="color:#13c078;">要</span><span class="mord cjk_fallback" style="color:#13c078;">一</span><span class="mord cjk_fallback" style="color:#13c078;">保</span><span class="mord cjk_fallback" style="color:#13c078;">存</span><span class="mord cjk_fallback" style="color:#13c078;">，</span><span class="mord cjk_fallback" style="color:#13c078;">预</span><span class="mord cjk_fallback" style="color:#13c078;">览</span><span class="mord cjk_fallback" style="color:#13c078;">结</span><span class="mord cjk_fallback" style="color:#13c078;">果</span><span class="mord cjk_fallback" style="color:#13c078;">就</span><span class="mord cjk_fallback" style="color:#13c078;">会</span><span class="mord cjk_fallback" style="color:#13c078;">更</span><span class="mord cjk_fallback" style="color:#13c078;">新</span></span></span></span></span></span></p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>按需进行编译</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;按需进行编译&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">按</span><span class="mord cjk_fallback" style="color:#13c078;">需</span><span class="mord cjk_fallback" style="color:#13c078;">进</span><span class="mord cjk_fallback" style="color:#13c078;">行</span><span class="mord cjk_fallback" style="color:#13c078;">编</span><span class="mord cjk_fallback" style="color:#13c078;">译</span></span></span></span></span></span>，不会刷新全部DOM节点，这个会加快我们的开发流程</p>
</li>
</ol>
<h3 data-id="heading-4">webpack与vite的多方面对比</h3>
<h4 data-id="heading-5">1. 打包过程的区别</h4>
<p><strong>webpack:</strong></p>
<ol>
<li>识别入口文件</li>
<li>逐级<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>递归识别依赖，构建依赖图谱</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;递归识别依赖，构建依赖图谱&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">递</span><span class="mord cjk_fallback" style="color:#13c078;">归</span><span class="mord cjk_fallback" style="color:#13c078;">识</span><span class="mord cjk_fallback" style="color:#13c078;">别</span><span class="mord cjk_fallback" style="color:#13c078;">依</span><span class="mord cjk_fallback" style="color:#13c078;">赖</span><span class="mord cjk_fallback" style="color:#13c078;">，</span><span class="mord cjk_fallback" style="color:#13c078;">构</span><span class="mord cjk_fallback" style="color:#13c078;">建</span><span class="mord cjk_fallback" style="color:#13c078;">依</span><span class="mord cjk_fallback" style="color:#13c078;">赖</span><span class="mord cjk_fallback" style="color:#13c078;">图</span><span class="mord cjk_fallback" style="color:#13c078;">谱</span></span></span></span></span></span></li>
<li>将代码转化成AST抽象语法树，在AST阶段中去处理代码</li>
<li>把AST抽象语法树变成浏览器可以识别的代码， 然后进行输出</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99180aedf4fe4948acb5efb92d440120~tplv-k3u1fbpfcp-watermark.image" alt="bad.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>vite：</strong></p>
<ol>
<li>当声明一个 script 标签类型为 module 时，浏览器就会像服务器发起一个GET</li>
<li>Vite 通过<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mtext>劫持浏览器</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;劫持浏览器&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord cjk_fallback" style="color:#13c078;">劫</span><span class="mord cjk_fallback" style="color:#13c078;">持</span><span class="mord cjk_fallback" style="color:#13c078;">浏</span><span class="mord cjk_fallback" style="color:#13c078;">览</span><span class="mord cjk_fallback" style="color:#13c078;">器</span></span></span></span></span></span>的这些请求，并在后端进行相应的处理，将项目中使用的文件通过简单的分解与整合，然后再返回给浏览器。</li>
<li>vite整个过程中没有对文件进行打包编译，所以其运行速度比原始的webpack开发编译速度快出许多。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8b2860c7543482eacf20cb43a0d49e7~tplv-k3u1fbpfcp-watermark.image" alt="good.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2. 构建依赖的区别</h4>
<p><strong>webpack:</strong><br>
底层使用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mi>n</mi><mi>o</mi><mi>d</mi><mi>e</mi><mi mathvariant="normal">.</mi><mi>j</mi><mi>s</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;node.js&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord" style="color:#13c078;"><span class="mord mathnormal" style="color:#13c078;">n</span><span class="mord mathnormal" style="color:#13c078;">o</span><span class="mord mathnormal" style="color:#13c078;">d</span><span class="mord mathnormal" style="color:#13c078;">e</span><span class="mord" style="color:#13c078;">.</span><span class="mord mathnormal" style="margin-right:0.05724em;color:#13c078;">j</span><span class="mord mathnormal" style="color:#13c078;">s</span></span></span></span></span></span>写的打包器预构建依赖，没有使用esbuild快。</p>
<p><strong>vite:</strong><br>
Vite 将会使用 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mi>e</mi><mi>s</mi><mi>b</mi><mi>u</mi><mi>i</mi><mi>l</mi><mi>d</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;esbuild&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord mathnormal" style="color:#13c078;">e</span><span class="mord mathnormal" style="color:#13c078;">s</span><span class="mord mathnormal" style="color:#13c078;">b</span><span class="mord mathnormal" style="color:#13c078;">u</span><span class="mord mathnormal" style="color:#13c078;">i</span><span class="mord mathnormal" style="margin-right:0.01968em;color:#13c078;">l</span><span class="mord mathnormal" style="color:#13c078;">d</span></span></span></span></span></span> 预构建依赖。Esbuild 使用 Go 编写，并且比以 Node.js 编写的打包器预构建依赖快 10-100 倍。</p>
<h4 data-id="heading-7">3. HMR（热替换）的区别</h4>
<p><strong>webpack：</strong><br>
热更新效率低下，即使是 HMR 更新速度也会随着应用规模的增长而显著下降。</p>
<p><strong>vite:</strong><br>
HMR是在EMS的基础上实现的，还会使用缓存所以很快</p>
<ul>
<li>在 Vite 中，HMR 是在原生 ESM 上执行的。当编辑一个文件时，Vite 只需要精确地让已编辑的模块与其最近的 HMR 边界之间的链失效（大多数时候只需要模块本身），使 HMR 更新始终快速，无论应用的大小。</li>
<li>Vite 同时利用 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="#13c078"><mrow><mi>H</mi><mi>T</mi><mi>T</mi><mi>P</mi><mtext>头来加速整个页面的重新加载</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;#13c078&#125;&#123;HTTP 头来加速整个页面的重新加载&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:#13c078;"><span class="mord mathnormal" style="margin-right:0.08125em;color:#13c078;">H</span><span class="mord mathnormal" style="margin-right:0.13889em;color:#13c078;">T</span><span class="mord mathnormal" style="margin-right:0.13889em;color:#13c078;">T</span><span class="mord mathnormal" style="margin-right:0.13889em;color:#13c078;">P</span><span class="mord cjk_fallback" style="color:#13c078;">头</span><span class="mord cjk_fallback" style="color:#13c078;">来</span><span class="mord cjk_fallback" style="color:#13c078;">加</span><span class="mord cjk_fallback" style="color:#13c078;">速</span><span class="mord cjk_fallback" style="color:#13c078;">整</span><span class="mord cjk_fallback" style="color:#13c078;">个</span><span class="mord cjk_fallback" style="color:#13c078;">页</span><span class="mord cjk_fallback" style="color:#13c078;">面</span><span class="mord cjk_fallback" style="color:#13c078;">的</span><span class="mord cjk_fallback" style="color:#13c078;">重</span><span class="mord cjk_fallback" style="color:#13c078;">新</span><span class="mord cjk_fallback" style="color:#13c078;">加</span><span class="mord cjk_fallback" style="color:#13c078;">载</span></span></span></span></span></span>（再次让浏览器为我们做更多事情）：源码模块的请求会根据 304 Not Modified 进行协商缓存，而依赖模块请求则会通过 Cache-Control: max-age=31536000,immutable 进行强缓存，因此一旦被缓存它们将不需要再次请求</li>
</ul>
<h3 data-id="heading-8">vite快速搭建vue开发环境</h3>
<p><strong>需要注意的是vite目前它只支持Vue3.x的版本，不支持Vue2.x版本;而且Node.js 版本 >= 12.0.0</strong></p>
<pre><code class="copyable">npm init @vitejs/app <project-name> -- --template vue
cd <project-name>
npm install
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们可以看到这个页面，就算是成功搭建啦~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c112f4c48ec4c7d8cb0d9a7e63db7a4~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-06-20 下午3.44.48.png" loading="lazy" referrerpolicy="no-referrer">
当然，我们也可以使用附加的命令行选项直接指定项目名称和你想要使用的模板，目前支持的模板预设包括一下内容：</p>
<ul>
<li>vanilla</li>
<li>vanilla-ts</li>
<li>vue</li>
<li>vue-ts</li>
<li>react</li>
<li>react-ts</li>
<li>preact</li>
<li>preact-ts</li>
<li>lit-element</li>
<li>lit-element-ts</li>
<li>svelte</li>
<li>svelte-ts</li>
</ul>
<h3 data-id="heading-9">vite快速搭建react-ts开发环境</h3>
<h4 data-id="heading-10">创建基本的项目</h4>
<pre><code class="hljs language-js copyable" lang="js">npm init @vitejs/app my-vite-app --  --template react-ts
npm install
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过终端提供的链接可以打开如下的界面，这也就预示着咱们的项目构建成功啦：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46bdf13e978f4a68b14dd880e4a1006b~tplv-k3u1fbpfcp-watermark.image" alt="屏幕快照 2021-06-20 下午4.04.21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">结合使用antd框架</h4>
<pre><code class="copyable">npm add antd
在全局index.scss中使用@import 'antd/dist/antd.css'导入全局样式
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">文件别名配置修改</h4>
<p>vite提供了一个vite.config.ts文件，我们可以在这个文件中进行别名配置</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 在vite.config.ts文件中,添加resolve对象进行所需的别名配置</span>
 <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [reactRefresh()],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: [
      &#123; <span class="hljs-attr">find</span>: <span class="hljs-string">'@'</span>, <span class="hljs-attr">replacement</span>: <span class="hljs-string">'/src'</span> &#125;,
    ]
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在tsconfig.json中添加paths和baseUrl属性</span>
&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"ESNext"</span>,
    <span class="hljs-string">"lib"</span>: [<span class="hljs-string">"DOM"</span>, <span class="hljs-string">"DOM.Iterable"</span>, <span class="hljs-string">"ESNext"</span>],
    <span class="hljs-string">"allowJs"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"forceConsistentCasingInFileNames"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"ESNext"</span>,
    <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"Node"</span>,
    <span class="hljs-string">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"isolatedModules"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"noEmit"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"jsx"</span>: <span class="hljs-string">"react"</span>,
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"@/*"</span>: [<span class="hljs-string">"src/*"</span>]
    &#125;,
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"."</span>
  &#125;,
  <span class="hljs-string">"include"</span>: [<span class="hljs-string">"./src"</span>]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就可以体验超快速的vue/react开发了~</p>
<h3 data-id="heading-13">总结</h3>
<p>vite确实有惊人的速度，当然也会有一些缺陷，如果大家想了解更多请关注vite的<a href="https://cn.vitejs.dev/guide/" target="_blank" rel="nofollow noopener noreferrer">官网</a>,本篇文章也是小白摸路，如有错误的地方，请多多指正啊~</p></div>  
</div>
            