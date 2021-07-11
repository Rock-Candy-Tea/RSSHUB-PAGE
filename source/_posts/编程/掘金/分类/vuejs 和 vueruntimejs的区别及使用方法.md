
---
title: 'vue.js 和 vue.runtime.js的区别及使用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0e7479e5e12446c8028aaa2accd45f7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:01:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0e7479e5e12446c8028aaa2accd45f7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">两种 vue 的区别</h2>
<ul>
<li>
<p><strong>vue.js</strong> 即完整版Vue：同时包含编译器和运行时的版本。</p>
</li>
<li>
<p><strong>vue.runtime.js</strong> 即运行时版本Vue：用来创建 Vue 实例、渲染并处理虚拟 DOM 等的代码。基本上就是除去编译器的其它一切。</p>
</li>
<li>
<p><strong>两个版本对应的文件名</strong></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//完整版</span>
<script src=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.js"</span>></script>

<span class="hljs-comment">// 非完整版</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.runtime.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>运行时 + 编译器 vs. 只包含运行时</strong></li>
</ul>
<p>如果你需要在客户端编译模板 (比如传入一个字符串给 template 选项，或挂载到一个元素上并以其 DOM 内部的 HTML 作为模板)，就将需要加上编译器，即完整版：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 需要编译器</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>&#123;&#123; hi &#125;&#125;</div>'</span>
&#125;)

<span class="hljs-comment">// 不需要编译器</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  render (h) &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, <span class="hljs-built_in">this</span>.hi)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用 vue-loader 或 vueify 的时候，*.vue 文件内部的模板会在构建时预编译成 JavaScript。你在最终打好的包里实际上是不需要编译器的，所以只用运行时版本即可。</p>
<p>因为运行时版本相比完整版体积要小大约 30%，所以应该尽可能使用这个版本。</p>
<p>总结：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0e7479e5e12446c8028aaa2accd45f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">用 codesandbox.io 写 Vue 代码</h2>
<p>点击进入：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/" ref="nofollow noopener noreferrer">codesandbox</a></p>
<ol>
<li>点击Create Sandbox</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdbc04add7648008959f12c04772415~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>选择 Vue</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5209e110b1ba432fa05a83bb5fde071b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>好啦，可以写代码啦~</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bcdbab17f934b389e76ac74fcdfb020~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文参考：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Finstallation.html%23%25E5%25AF%25B9%25E4%25B8%258D%25E5%2590%258C%25E6%259E%2584%25E5%25BB%25BA%25E7%2589%2588%25E6%259C%25AC%25E7%259A%2584%25E8%25A7%25A3%25E9%2587%258A" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/installation.html#%E5%AF%B9%E4%B8%8D%E5%90%8C%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC%E7%9A%84%E8%A7%A3%E9%87%8A" ref="nofollow noopener noreferrer">vue.js教程</a></p></div>  
</div>
            