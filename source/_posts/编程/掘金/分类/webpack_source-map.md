
---
title: 'webpack_source-map'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54df45e2a744bb8948a6c00a584a49b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 19:27:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54df45e2a744bb8948a6c00a584a49b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文从构建后代码，到浏览器为什么可以看到源码映射来讨论，不研究构建部分。</p>
<ul>
<li>源码的目录树怎么生成的，在构建后代码的哪里有体现？</li>
<li>源码的代码部分有构建后代码的哪里提供的？</li>
<li>构建后代码和源码的位置映射关系维护在哪里？</li>
<li>下面通过webpack的几种配置来见分晓。</li>
</ul>
<h2 data-id="heading-0">source-map技术</h2>
<ul>
<li>这个是浏览器技术，用于代码位置的映射，也就是需要浏览器支持</li>
</ul>
<h2 data-id="heading-1">webpack之souce-map配置和原理分析</h2>
<ul>
<li>eval</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 配置</span>
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 源码</span>
<span class="hljs-comment">// config.js</span>
__webpack_public_path__ = <span class="hljs-built_in">window</span>.path + <span class="hljs-string">'/'</span>;

<span class="hljs-comment">// 效果</span>
<span class="hljs-comment">/* 3 */</span>
<span class="hljs-comment">/***/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span>, __webpack_require__</span>) </span>&#123;
<span class="hljs-built_in">eval</span>(<span class="hljs-string">"__webpack_require__.p = window.path + '/';\n\n//////////////////\n// WEBPACK FOOTER\n// ./src/views/config.js\n// module id = 3\n// module chunks = 0\n\n//# sourceURL=webpack:///./src/views/config.js?"</span>);
<span class="hljs-comment">/***/</span> &#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54df45e2a744bb8948a6c00a584a49b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>通过eval把构建后代码的部分(和源码一一对应的)形成source-map；而不是整个dist文件</li>
<li>eval中的代码是构建后的代码，只是在eval中执行，形成source-map的一个环境</li>
<li>浏览器根据sourceURL形成一个目录树，内容就是eval中的代码</li>
<li>eval特点：有最好的性能，但是它只映射到每个模块源码文件，没有行列信息</li>
<li>总结：</li>
<li>只是提供了sourceURL(生成源码目录树)、没有源码代码</li>
</ol>
<ul>
<li>source-map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 配置</span>
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 效果，会生成.map文件</span>
<span class="hljs-comment">// 下面来分析.map</span>
&#123;
    <span class="hljs-attr">version</span>:<span class="hljs-number">3</span> <span class="hljs-comment">// 版本号</span>
    <span class="hljs-attr">sources</span>:[] <span class="hljs-comment">// 源码目录树</span>
    <span class="hljs-attr">names</span>:[] <span class="hljs-comment">//</span>
    <span class="hljs-attr">mappings</span>:<span class="hljs-string">''</span> <span class="hljs-comment">// 位置映射</span>
    <span class="hljs-attr">files</span>:<span class="hljs-string">''</span> <span class="hljs-comment">// 构建后代码位置</span>
    <span class="hljs-attr">sourcesContent</span>:[] <span class="hljs-comment">// 打包后的代码的源码翻译（理解：也即是构建后的代码，如果该部分代码有对应的源码，则会替换成源码，负责显示源码）</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3aab3b7828c45afb2f7f4e2bae6255e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a45ef9ef60f64d879ec97f5e9ce8bf09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>souce-map配置，会生产.map文件</li>
<li>.map文件包含目录树(sources)、构建后代码的源码解析(sourceContent)、位置映射(mappings)</li>
<li>总结：</li>
<li>能生成源码的目录树（sources）、及源码的代码（sourceContent、mappings），具有完整的映射信息</li>
</ol>
<ul>
<li>inline-source-map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 配置</span>
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae70f453768548969f557fe47ed85dba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>效果和source-map一样</li>
<li>相对于source-map,inline-source-map就和其名字一样好理解，就是内联的，通过base放在构建代码的最后面，而没有独立生成.map文件</li>
</ol>
<ul>
<li>eval-source-map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 配置</span>
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-source-map'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 效果</span>
<span class="hljs-built_in">eval</span>(<span class="hljs-string">"__webpack_require__.p = window.path + '/';//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zcmMvdmlld3MvY29uZmlnLmpzPzZlNDQiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEscUJBQXVCIiwiZmlsZSI6IjMuanMiLCJzb3VyY2VzQ29udGVudCI6WyJfX3dlYnBhY2tfcHVibGljX3BhdGhfXyA9IHdpbmRvdy5wYXRoICsgJy8nO1xuXG5cbi8vLy8vLy8vLy8vLy8vLy8vL1xuLy8gV0VCUEFDSyBGT09URVJcbi8vIC4vc3JjL3ZpZXdzL2NvbmZpZy5qc1xuLy8gbW9kdWxlIGlkID0gM1xuLy8gbW9kdWxlIGNodW5rcyA9IDAiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///3\n"</span>);

<span class="hljs-comment">// 对比eval发现，不仅有sourceURL、而且多了sourceMappingURL</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9df8df7cf2004c5090cbfe8d0769b277~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>sourceURL=webpack-internal 会生成目录结构，这里的结构为以构建后代码的module为纬度来的=>支持模块缓存</li>
<li>sourceMappingURL。会生成完整信息的源码目录树和代码</li>
</ol>
<ul>
<li>cheap-source-map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">和source-map对比下来，.map文件中没有name属性，也即是缺少部分功能：不包含 loader 的 sourcemap
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">总结：我觉得基本可以分为两种模式</h2>
<ul>
<li>只生成源码的目录树</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">代表：<span class="hljs-built_in">eval</span>
关键词：sourceURL
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>生成源码的目录树、及源码代码（及映射）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">代码：source-map
关键词：sourceMappingURL / .map
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            