
---
title: '体验了一把 swc 替代 babel 和 tsc'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2873'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 23:33:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=2873'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/next.js" ref="nofollow noopener noreferrer">Next.js 11</a> 已经使用了 <strong>swc</strong> 替换 <strong>babel</strong> 进行了 <strong>js</strong> 代码编译，构建速度提升了不少。于是针对自己的组件库进行了一波优化。</p>
<p>组件库使用了 <strong>React + TypeScript</strong> 编译用的 <strong>TypeScript</strong> 自带的 <strong>tsc</strong> 进行编译成 <strong>es5</strong> 代码</p>
<h3 data-id="heading-1">配置项文件 <code>.swcrc</code></h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"jsc"</span>: &#123;
    <span class="hljs-attr">"parser"</span>: &#123;
      <span class="hljs-attr">"syntax"</span>: <span class="hljs-string">"typescript"</span>,
      <span class="hljs-attr">"tsx"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">"decorators"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">"dynamicImport"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">"transform"</span>: &#123;
      <span class="hljs-attr">"legacyDecorator"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">"decoratorMetadata"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">"target"</span>: <span class="hljs-string">"es5"</span>,
    <span class="hljs-attr">"keepClassNames"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"loose"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">"module"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"commonjs"</span>,
    <span class="hljs-attr">"strict"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"strictMode"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"lazy"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"noInterop"</span>: <span class="hljs-literal">false</span>
  &#125;,
  <span class="hljs-attr">"sourceMaps"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原来构建完成需要将近12s左右，现在仅需要不到1s完成构建编译，看来确实如官方所说的快很多</p>
<p>官方描述 <strong>swc</strong> 编译与其他工具 <strong>esbuild、tsc、babel</strong> 编译成不同目标代码的性能对比
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fswc.rs%2Fdocs%2Fbenchmark-transform" target="_blank" rel="nofollow noopener noreferrer" title="https://swc.rs/docs/benchmark-transform" ref="nofollow noopener noreferrer">性能对比</a></p>
<h2 data-id="heading-2">踩到的坑</h2>
<p>对于这个编译工具，虽然相比其他工具有明显的性能提升，但是也有一定的局限性</p>
<h3 data-id="heading-3">优点</h3>
<ul>
<li>编译速度快；</li>
<li>配置简单，开箱即用；</li>
</ul>
<h3 data-id="heading-4">缺点</h3>
<ul>
<li>可使用的插件很少，官方文档上都没有；</li>
<li>目前生产环境使用该工具构建的案例很少(仅有 <strong>Next.js</strong> 框架)；</li>
<li>针对使用 <strong>Typescript</strong> 的项目编译成后无法生成相应的 <code>*.d.ts</code> 声明文件；</li>
</ul>
<p>由于项目中在引入一些通用文件模块时使用了相对路径别名，举个🌰子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原本的写法</span>
<span class="hljs-keyword">import</span> &#123; moduleA &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../../common/utils/tool'</span>
<span class="hljs-comment">// 这样的写法读起来不太优雅，于是换成了 =></span>
<span class="hljs-keyword">import</span> &#123; moduleA &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'src/common/utils/tool'</span>
<span class="hljs-comment">// 这样就能更清楚地知道模块的位置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在实际构建编译后生成的路径文件映射实际上是错误的，尽管官方说已经修复了这个问题，但是感觉不是一个问题，</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"jsc"</span>: &#123;
     <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"src/*"</span>:[<span class="hljs-string">"./src/*"</span>]
    &#125;,
&#125;
<span class="hljs-comment">// 使用该配置映射之后</span>
<span class="hljs-comment">// import &#123; moduleA &#125; from 'src/common/utils/tool' => </span>
<span class="hljs-comment">// import &#123; moduleA &#125; from './src/common/utils/tool'</span>
<span class="hljs-comment">// 根本没有生效!!!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswc.rs%2Fdocs%2Fconfiguring-swc%23jscpaths" target="_blank" rel="nofollow noopener noreferrer" title="https://swc.rs/docs/configuring-swc#jscpaths" ref="nofollow noopener noreferrer">参考</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fswc-project%2Fswc%2Fissues%2F702" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/swc-project/swc/issues/702" ref="nofollow noopener noreferrer">issue</a></li>
</ul>
<h3 data-id="heading-5">解决办法</h3>
<p>不适用 <code>jsc.paths</code>，使用 <code>tsc-alias</code> 完美解决这个问题</p>
<p>###<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Ftsc-alias" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/tsc-alias" ref="nofollow noopener noreferrer">tsc-alias</a></p></div>  
</div>
            