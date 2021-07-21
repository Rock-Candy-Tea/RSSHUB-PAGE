
---
title: '基础篇 - 从构建层面看 import 和 require 的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85daad80b08e4c3480779db8304c0ae6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 19:43:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85daad80b08e4c3480779db8304c0ae6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>一切的一切，都是因为群里的一个问题</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85daad80b08e4c3480779db8304c0ae6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然说最近在做 <code>webpack</code> 相关的事情，但是也没有对着干问题做过相关的研究，网上很多文章包括 <code>vue</code> 都介绍了建议使用 <code>import</code> ，但是没有说为什么要使用 <code>import</code>，对于开发者来说，调用的方式是没有区别的，那么为什么 <code>import</code> 的包就要比 <code>require</code> 的包小呢</p>
<p><strong>这里暂时就不说什么调用方式了，什么动态加载（require）、静态编译（import）的，这个网上都有，这篇文章就是分析一下为什么要用 <code>import</code>，而不用 <code>require</code></strong></p>
<h2 data-id="heading-1">正文</h2>
<p>首先本地先基于 <code>webpack</code> 搭建一个环境只是为了测试，不需要搭建太复杂的内容</p>
<h3 data-id="heading-2">基础文件内容</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>index.js</code> 内添加两种调用方式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; b &#125; = <span class="hljs-keyword">import</span>(<span class="hljs-string">'./importtest'</span>)
  <span class="hljs-built_in">console</span>.log(b()) 
&#125;
test()

<span class="hljs-comment">// or</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; b &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./requiretest'</span>)
  <span class="hljs-built_in">console</span>.log(b()) 
&#125;
test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>importtest.js</code> 中也是简单输出一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// importtest.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>requiretest.js</code> 也是如此</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// requiretest.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'lisi'</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的方式分别执行 <code>webpack</code> 后，输出的内容分别如下</p>
<h3 data-id="heading-3">import 输出</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8eea91ac3684d9ba94d620e37d583a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在打包时一共输出了两个文件：<code>main.js</code> 和 <code>src_importtest_js.js</code>，<code>main.js</code> 里面输出的内容如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbfa505c3b8545c28c6e98ebdfc192cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>main.js</code> 里面就是 <code>index.js</code> 里面的内容，<code>importtest</code> 里面的内容，是通过一个索引的方式引用过来的，引用的地址就是 <code>src_importtest_js.js</code></p>
<h3 data-id="heading-4">require 输出</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/058cd54155ee4c579a36366db0ed3064~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>require</code> 打包时，直接输出了一个文件，就只有一个 <code>main.js</code>，<code>main.js</code> 里面输出的内容如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cbaa09b560e40eaa499342723d4e92a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>main.js</code> 里面的内容是 <code>index.js</code> 和 <code>requiretest.js</code> 里面的所有内容</p>
<pre><code class="copyable">综上所述，我们从数据角度来看 import 的包是要大于 require 的，但通过打包文件来看，由业务代码导致的文件大小其实 import 是要小于 require 的
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">多引用情况下导致的打包变化</h3>
<p>这个时候我们大概知道了 <code>import</code> 和 <code>require</code> 打包的区别，接下来我们可以模拟一下一开始那位同学的问题，直接修改一下 <code>webpack.config.js</code> 的入口即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">index1</span>: <span class="hljs-string">'./src/index1.js'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里直接保证 <code>index.js</code> 和 <code>index1.js</code> 的内容一样即可，还是先测试一下 <code>import</code> 的打包</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db9c3f75af248d6aa499c22087bb37f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的内容和单入口时打包的 <code>import</code> 基本一致，里面出了本身的内容外，都是引用的 <code>src_importtest_js</code> 的地址，那么在看看 <code>require</code> 的包</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ba89314de8541c09898b52390fee094~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里内容和单入口打包的 <code>require</code> 基本一致，都是把 <code>requiretest</code> 的内容复制到了对应的文件内</p>
<p>虽然我们现在看的感觉多入口打包，还是 <code>import</code> 的文件要比 <code>require</code> 的文件大，但是核心问题在于测试案例的业务代码量比较少，所以看起来感觉 <code>import</code> 要比 <code>require</code> 大，当我们的业务代码量达到实际标准的时候，区别就看出来了</p>
<h3 data-id="heading-6">总结</h3>
<p><strong>import:</strong> 打包的内容是给到一个路径，通过该路径来访问对应的内容</p>
<p><strong>require:</strong> 把当前访问资源的内容，打包到当前的文件内</p>
<p>到这里就可以解释为什么 <code>vue</code> 官方和网上的文章说推荐 <code>import</code> 而不推荐 <code>require</code>，因为每一个使用 <code>require</code> 的文件会把当前 <code>require</code> 的内容打包到当前文件内，所以导致了文件的过大，使用 <code>import</code>，抛出来的是一个索引，所以不会导致重复内容的打包，就不会出现包大的情况</p>
<p>当然这也不是绝对的，就好像上述案例那种少量的业务代码，使用 <code>import</code> 的代码量其实要比 <code>require</code> 大，所以不建议大家直接去确定某一种方式是最好的，某一种方式就是不行的，依场景选择方法</p>
<h2 data-id="heading-7">尾声</h2>
<p>这篇文章就是一个简单的平时技术方面基础研究的简介，不是特别高深的东西，还希望对大家有所帮助，如果有覆盖面不够，或者场景不全面的情况，还希望大家提出，我在继续补充</p>
<p>这种类型的文章不是我擅长的方向，还是喜欢研究一些新的东西，欢迎大家指教：</p>
<p><a href="https://juejin.cn/post/6970988759529553927" target="_blank" title="https://juejin.cn/post/6970988759529553927">实战篇 - 如何把性能优化的颗粒度做的更细</a></p>
<p><a href="https://juejin.cn/post/6931749943359062023" target="_blank" title="https://juejin.cn/post/6931749943359062023">思想篇 - 通过 hooks 的出现，反思组件化开发存在的问题</a></p>
<p><a href="https://juejin.cn/post/6844903955894370312" target="_blank" title="https://juejin.cn/post/6844903955894370312">范式篇 - 如何把函数式编程合理运用到日常工作中</a></p></div>  
</div>
            