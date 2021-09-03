
---
title: 'Vue2.0是如何做到从浏览器不可识别到可识别的呢？(compile阶段源码解析)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213be361bf66497d9feb5da3bd79592b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:03:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213be361bf66497d9feb5da3bd79592b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><code>vue</code> 的构建其实是分为了两种版本，即完整版本: <code>runtime+compiler</code> 和 运行时版本: <code>runtime</code> 。这两种版本各有什么不同呢？</p>
<p>让我们打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23Vue-compile" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#Vue-compile" ref="nofollow noopener noreferrer">Vue官网</a> 可以看到Vue给我们提供了一个 <code>compile</code> 函数，通过传入html的字符串就可以获得两个渲染函数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213be361bf66497d9feb5da3bd79592b~tplv-k3u1fbpfcp-watermark.image" alt="Untitled.png" loading="lazy" referrerpolicy="no-referrer">
注意加粗部分的 <strong><strong>完整版时可用</strong></strong> 表达的意思就是只能在runtime+compiler的构建模式下才能使用。</p>
<blockquote>
<p><em>由于完整版需要编译器的参与，所以传统的html中的js如果都这么写的话那么每次项目运行时编译就会耗费很长的时间。</em></p>
</blockquote>
<p>我们现在大多数项目（ <code>webpack\vite</code> 等在内的打包工具下）基本都是只有runtime阶段，而compile阶段则是由像 <code>vue-loader</code> 这种插件帮我们在项目运行的预编译阶段就已经做了</p>
<p> 但是为了更好的学（面）习（试）源（吹）码（牛） 🤩, 所以我们还是需要了解其中的原理以及学习其中良好的代码风格。</p>
<h1 data-id="heading-1">正文</h1>
<p>首先准备好vue2.x的源码，由于版本不同代码可能不太相同，这里使用的版本是 <code>2.6.14</code> </p>
<p>我们知道vue的编译分为了三个阶段:</p>
<ul>
<li>
<p>模版解析阶段 ：即将一堆模板字符串用正则等方式解析成抽象语法树AST（解析器）</p>
</li>
<li>
<p>优化阶段：遍历AST，找出其中的静态节点，并打上标记（优化器）</p>
</li>
<li>
<p>代码生成阶段：将AST转换成渲染函数（代码生成器）</p>
</li>
</ul>
<p>下面我们将根据源码中文件的调用顺序一步一步的了解 <code>compile</code> 阶段，vue到底做了哪些工作。</p>
<blockquote>
<p><em>多图警告⚠️ 恐图者甚！！！</em></p>
</blockquote>
<h2 data-id="heading-2">入口文件</h2>
<p>首先进入到入口文件<code>src/platforms/web/entry-runtime-with-compiler.js</code> </p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bf8612a9aac4c478318b7b6b7b42116~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>这里首先通过判断有没有 render函数，如果有了那就直接通过render函数返回dom。</p>
</li>
<li>
<p>反之则获取template模版。重点看图片注释</p>
</li>
<li>
<p>然后就走到了 <code>compileToFunctions</code> 函数部分，返回了render函数和staticRender函数用于生成 <code>VDOM</code> </p>
</li>
</ol>
<h2 data-id="heading-3">生成Render函数</h2>
<p>进入到 <code>compileToFunctions</code> 函数中，发现调用了 <code>createCompiler</code> 函数</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ece4de9efe94af9ab43ef57cc67f166~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>随后进入到 <code>createCompiler</code> 函数中，发现通过又调用了 <code>createCompilerCreator</code> 函数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2dca9a889c643b7bd300c6e46e6dba0~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个函数返回了一个对象 <code>CompiledResult</code> 用于返回render和staticRender和ast等属性，这个对象的类型如下:</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">
declare type CompiledResult = &#123;

  <span class="hljs-attr">ast</span>: ?ASTElement;

  render: string;

  staticRenderFns: <span class="hljs-built_in">Array</span><string>;

  stringRenderFns?: <span class="hljs-built_in">Array</span><string>;

  errors?: <span class="hljs-built_in">Array</span><string | WarningMessage>;

  tips?: <span class="hljs-built_in">Array</span><string | WarningMessage>;

&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入到 <code>createCompilerCreator</code> 函数发现通过函数闭包，返回了一个对象其中有两个函数， <code>compile</code>函数 和 <code>compileToFunctions</code>函数 ，compile函数中，执行<code>createCompilerCreator</code> 传入的函数参数 <code>baseCompile</code> 进行编译的三个流程。其中具体的代码如下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94da0e1174b545dd81d8886871830740~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以最重要的就是这个 <code>compile</code> 函数，我们也可以看到返回的第二个函数也调用了一下这个compile，其实作用就是使这个 <code>compileToFunctions</code> 具有编译生成 <code>render</code>函数的作用。</p>
<p>由此这个函数就开始了编译的三个阶段</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04c9606e427547ef81d91965a06656e0~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Vue通过HTMLParse这个库将template模版解析成AST树。</p>
</li>
<li>
<p>通过optimize标记静态节点作为常量，并在使得在VDOM diff时不在更新。</p>
</li>
<li>
<p>通过 <code>generate</code> 函数生成 <code>render</code>函数和 <code>staticRenderFns</code> 函数用于后面生成虚拟DOM</p>
</li>
</ul>
<p>具体的这三个流程的代码的话可以自行查看，这里不在赘述。主要说一下 <code>generate</code> 函数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecfea64f2b904df2b19ce74ae851e862~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>函数中通过挂载到 <code>vm</code>上到 <code>_c</code>实例方法（其实就是调用了 <code>createElement</code> 方法）进行 <code>ast</code>生成的，然后render字符串通过 <code>with()包裹返回</code>， <code>staticRenderFns</code>在之前已经做过静态标记，所以就直接取state里的staticRenderFns了。 ☠️</p>
<blockquote>
<p><em>除了</em> <code>_c</code> <em>方法还有</em> <code>_m</code> <em>等方法通过</em> <code>core/instance/render.js</code> <em>下</em> <code>renderMixin</code><em>函数调用</em> <code>installRenderHelpers</code> <em>函数，挂载到实例上</em></p>
</blockquote>
<p>以上就是全部的compile阶段的整个流程，其中有部分代码(HTMLParse解析、optimize如何做静态标记、生成render字符串)没有深入探究，后续有机会再探讨！ 🤣</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fcaibaojian.com%2Fvue-design%2Fappendix%2Fast.html" target="_blank" rel="nofollow noopener noreferrer" title="http://caibaojian.com/vue-design/appendix/ast.html" ref="nofollow noopener noreferrer">Vue模版AST标记详情</a>可参考</p>
<h2 data-id="heading-4">后记</h2>
<p>既然我们通过 <code>compile阶段</code> 得到了render函数， <code>runtime阶段</code>那么Vue又是如何将render函数转换生成虚拟dom的呢？ 😎</p>
<p>其实在 <code>new Vue()</code> 时Vue就调用了 <code>initRender</code> 方法，调用了一个 <code>_c</code> 方法也就是 <code>createElement</code> 方法(也就是在开发时写render函数的参数 <code>h</code>)，这个方法返回了一个 <code>_createElement</code> 方法就会去递归创建 <code>Vnode</code> 树。具体代码在 <code>core/vdom/index.js</code> 中。</p>
<h3 data-id="heading-5">实例化流程</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32249176c06a48ae8ef1a56ac82a3be3~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>initMixin方法中</code>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbeccc33050e48618a74c1c97b9342b9~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生成vdom后，vue就将对data等进行数据劫持等操作，以及其他的一些操作。至此，Vue就走到了created阶段，data和vdom也准备好了。</p>
<h2 data-id="heading-6">✍️中西结合疗效好</h2>
<p>最后结合Vue的生命周期图来看，就能更好的理解 Vue的整个生命周期函数过程了</p>
<p>✋全文只代表作者个人观点，有分析错误的，记得指出哦～ 😀</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b83d13aade0a4fe785a5b67c72ce7953~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 9.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            