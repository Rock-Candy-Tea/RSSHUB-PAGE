
---
title: '前端有必要学习webpack吗？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic2.zhimg.com/v2-d1785315565056542c52a2b78616c8f8_1440w.jpg'
author: 知乎
comments: false
date: Thu, 22 Jul 2021 03:04:58 GMT
thumbnail: 'https://pic2.zhimg.com/v2-d1785315565056542c52a2b78616c8f8_1440w.jpg'
---

<div>   
doodlewind的回答<br><br><p>学当然可以学，但在今天可能已经不那么有意义和必要了。</p><p>Webpack 是不是个好东西？当然是。我还记得五年前刚毕业只会糊 jQuery 上传 FTP 的时候。那时见到 Webpack 然后仔细把它 1.x 版本晦涩的文档啃下来的感觉，简直是颠覆了我的想象——居然还有工具能把多份 JS 源码按依赖关系组合起来（<i>而不只是逐个 uglify 完了拼在一起</i>）？啥啥啥这个 chunk 是啥？哇这个 require.ensure 不就是完美的按需加载吗？哇这个插件机制简直扩展性爆炸啊！当时和同事安利 Webpack 的感觉，大致就是这样的：</p><figure data-size="small"><img src="https://pic2.zhimg.com/v2-d1785315565056542c52a2b78616c8f8_1440w.jpg" data-caption data-size="small" data-rawwidth="850" data-rawheight="528" data-default-watermark-src="https://pic2.zhimg.com/v2-2c1cc2a1245a8275a2bec91e3e749c04_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-d1785315565056542c52a2b78616c8f8_r.jpg" referrerpolicy="no-referrer"></figure><p>Webpack 应该是首创了文档 example 里直接放构建产物代码给你读的硬核操作。如果你初次阅读时还没接触过 Node.js 的 CommonJS 规范，那基本肯定是看不懂但大受震撼：</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-e510d3288769085ba72ca82e6986c57f_1440w.jpg" data-caption data-size="normal" data-rawwidth="2718" data-rawheight="2362" data-default-watermark-src="https://pic4.zhimg.com/v2-531a8f1894ed995dcdf57ecae7c80d3b_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-e510d3288769085ba72ca82e6986c57f_r.jpg" referrerpolicy="no-referrer"></figure><p>Webpack 产物的奇怪结构很容易让初学者困扰。但对于「Webpack 到底是如何工作的」这样的问题，倒很容易一段话说清楚：<b>把每个 JS 模块的代码包在一个函数里，这些函数可以拼在一起得到一个 bundle 文件。然后在这个 bundle 的最上面，固定生成一个用来求值这些函数（模块）的辅助函数即可。在运行时只要从入口模块开始求值，就能递归地获取到并缓存全部模块了</b>。比如下面这两个不同模块里的 JS 代码：</p><div class="highlight"><pre><code class="language-js"><span><span class="c1">// b.js</span>
<span class="kr">export</span> <span class="k">default</span> <span class="mi">42</span><span class="p">;</span>

<span class="c1">// a.js</span>
<span class="kr">import</span> <span class="nx">b</span> <span class="nx">from</span> <span class="s1">'./b.js'</span><span class="p">;</span>
<span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">b</span><span class="p">);</span>
</span></code></pre></div><p>原理上就会被整个转换成下面这样：</p><div class="highlight"><pre><code class="language-js"><span><span class="c1">// dist.js</span>

<span class="c1">// 这个 runtime 函数是固定的，直接字符串拼接到编译产物头上就行了</span>
<span class="c1">// 所有独立 module 都会被包成函数，作为 modules 数组传入</span>
<span class="kd">function</span> <span class="nx">runtime</span><span class="p">(</span><span class="nx">modules</span><span class="p">)</span> <span class="p">&#123;</span>
  <span class="c1">// 所有 module 的缓存就放在一个对象里</span>
  <span class="kr">const</span> <span class="nx">module_cache</span> <span class="o">=</span> <span class="p">&#123;&#125;;</span>

  <span class="c1">// 每个 module 在 require 依赖时，都会调用到这个函数</span>
  <span class="kd">function</span> <span class="nx">webpack_require</span><span class="p">(</span><span class="nx">id</span><span class="p">)</span> <span class="p">&#123;</span>
    <span class="c1">// 朴素的缓存命中逻辑</span>
    <span class="k">if</span> <span class="p">(</span><span class="nx">module_cache</span><span class="p">[</span><span class="nx">id</span><span class="p">])</span> <span class="k">return</span> <span class="nx">module_cache</span><span class="p">[</span><span class="nx">id</span><span class="p">].</span><span class="nx">exports</span><span class="p">;</span>

    <span class="c1">// 缓存没有命中时就生成一个新 module</span>
    <span class="c1">// 每个 module 在 export 字段时，都会挂载到这里的 export 属性上</span>
    <span class="kr">const</span> <span class="nx">module</span> <span class="o">=</span> <span class="nx">module_cache</span><span class="p">[</span><span class="nx">id</span><span class="p">]</span> <span class="o">=</span> <span class="p">&#123;</span>
      <span class="nx">exports</span><span class="o">:</span> <span class="p">&#123;&#125;</span>
    <span class="p">&#125;;</span>

    <span class="c1">// 根据 module 的 id 找到相应函数，传入其 exports 和 require</span>
    <span class="nx">modules</span><span class="p">[</span><span class="nx">id</span><span class="p">](</span><span class="nx">module</span><span class="p">,</span> <span class="nx">module</span><span class="p">.</span><span class="nx">exports</span><span class="p">,</span> <span class="nx">webpack_require</span><span class="p">);</span>

    <span class="c1">// 每次 require 最终返回的都是某个 module 的 exports 结果</span>
    <span class="k">return</span> <span class="nx">module</span><span class="p">.</span><span class="nx">exports</span><span class="p">;</span>
  <span class="p">&#125;</span>

  <span class="c1">// 整个 runtime 返回的是入口 module 的求值结果</span>
  <span class="k">return</span> <span class="nx">webpack_require</span><span class="p">(</span><span class="mi">1</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="c1">// b.js 的变换结果，其 module 编号为 0</span>
<span class="kd">function</span> <span class="nx">b</span><span class="p">(</span><span class="nx">this_module</span><span class="p">,</span> <span class="nx">webpack_exports</span><span class="p">,</span> <span class="nx">webpack_require</span><span class="p">)</span> <span class="p">&#123;</span>
  <span class="c1">// 挂载 export default 结果</span>
  <span class="nx">webpack_exports</span><span class="p">[</span><span class="s1">'default'</span><span class="p">]</span> <span class="o">=</span> <span class="mi">42</span><span class="p">;</span>
<span class="p">&#125;</span>

<span class="c1">// a.js 的变换结果，其 module 编号为 1</span>
<span class="kd">function</span> <span class="nx">a</span><span class="p">(</span><span class="nx">this_module</span><span class="p">,</span> <span class="nx">webpack_exports</span><span class="p">,</span> <span class="nx">webpack_require</span><span class="p">)</span> <span class="p">&#123;</span>
  <span class="c1">// 获取 b 模块的 default 字段</span>
  <span class="kr">const</span> <span class="nx">exported</span> <span class="o">=</span> <span class="nx">webpack_require</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
  <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">exported</span><span class="p">[</span><span class="s1">'default'</span><span class="p">]);</span>
<span class="p">&#125;</span>

<span class="nx">runtime</span><span class="p">([</span><span class="nx">b</span><span class="p">,</span> <span class="nx">a</span><span class="p">]);</span> <span class="c1">// 数组下标顺序和 module 编号一致</span>
</span></code></pre></div><p>这个 <code>runtime</code> 函数就是 Webpack 产物里最上面的那堆 bootstrap 简化后的结果，具体逻辑看一下注释或者贴到控制台里跑一下就知道了（也可以参见 Rich Harris 的这个 <a href="http://link.zhihu.com/?target=https%3A//gist.github.com/Rich-Harris/79a02519fb00837e8d5a4b24355881c0" class=" wrap external" target="_blank" rel="nofollow noreferrer">gist</a>）。总之我们可以认为，Webpack 的整个架构都是为了完成这样的代码生成工作而服务的。这样一来，我们就可以很自然地理解 Webpack 的很多基础性设计了：</p><ul><li>为了支持对 JS 源码的依赖分析，它需要依靠 Babel 来获取 AST（勘误，最早用的是 <a href="http://link.zhihu.com/?target=https%3A//github.com/acornjs/acorn" class=" wrap external" target="_blank" rel="nofollow noreferrer">Acorn</a>）。</li><li>为了支持 JS 以外乱七八糟的文件格式，它需要设计一套可扩展的 loader 机制，让你配置哪种文件要用哪种 loader 来加载。</li><li>为了支持对 loader 的预处理结果做各种优化处理（有些类似 LLVM 的优化 pass），它需要开放出一堆 hooks 和另一套处理规范，于是有了插件的概念，甚至搞出了 <a href="http://link.zhihu.com/?target=https%3A//github.com/webpack/tapable" class=" wrap external" target="_blank" rel="nofollow noreferrer">Tapable</a> 这样的库来支撑复杂的插件控制逻辑。</li></ul><p>上面这些东西对应的源码细节，可能都不知道被分析过多少次了。但这样的文章读一篇以后再读十篇，你又学到了什么呢？一方面，这些工具都是你自己跑进 node_modules 在源码里加一堆 console.log 就能研究，函数跳来跳去迟早能找到你想要的东西。另一方面更重要的是，个人觉得前端社区普遍存在的一个问题是跟风和视野的局限——<i>好多人都在研究 Webpack 原理所以我也要研究，我们都在用 Webpack 所以它非常厉害</i>。</p><p>对前端来说，Webpack 这个工具已经很成熟了。反倒是多看下新涌现出来的思路，多接触前端之外的技术，会让你觉得并不只有 Webpack 值得研究：</p><ul><li>打包 JS 必须用 JS 写的 Babel 吗？现在已经有了 <a href="http://link.zhihu.com/?target=https%3A//esbuild.github.io/" class=" wrap external" target="_blank" rel="nofollow noreferrer">esbuild</a> 和 <a href="http://link.zhihu.com/?target=https%3A//github.com/swc-project/swc" class=" wrap external" target="_blank" rel="nofollow noreferrer">swc</a>。</li><li>前端代码一定要生成 bundle 后才能启动本地环境吗？现在已经有了借助浏览器原生 ESM 能力的 Snowpack 和 Vite。甚至像 QuickJS 已经内置了引擎级的 ESM 支持，基于它的项目都可以不需要打包工具了。</li><li>Webpack 默认只能喂饱单核，其他语言的工具也这样吗？Ninja 对多核的利用堪称楷模，增量编译 Chromium 这种恐龙级项目都很快，<a href="http://link.zhihu.com/?target=https%3A//www.aosabook.org/en/posa/ninja.html" class=" wrap external" target="_blank" rel="nofollow noreferrer">它的设计故事很值得一读</a>。</li></ul><p>你看，如果想推动社区构建系统的进步，许多工作的重心已经不在 Webpack 上了。而如果是想提高自己的技术水平，单纯学习 Webpack 的配置和啃它的源码固然也是个选择。但个人还是觉得如果能找到自己想解答的问题，以问题驱动的形式来探索，那或许会更好：</p><ul><li>Webpack 的这种打包手法是唯一的选择吗？它跟 JS 生态下的其它 bundler 工具（如 Rollup）有什么原理上的差别？</li><li>如果想在你负责的现有系统中接入或换掉 Webpack，需要哪些改造？是否值得？</li><li>Webpack 和其他语言的构建系统相比又有什么差别？优劣对比如何？</li><li>基于 Webpack 的构建系统离最高效的形式还有多远？瓶颈在哪？</li></ul><p>话说我们才刚把老项目从 Webpack 迁到了 Vite 上，<a href="https://zhuanlan.zhihu.com/p/391077878" class="internal">写了篇历史项目的 Vite 迁移总结</a>——这里其实也没深入学习 Webpack，但也不需要嘛。</p><p>所以个人觉得只有尝试找到并解答那些「真正重要的」问题，才有机会实现出新的工程突破。也希望大家都能尽早完成对框架层工具的祛魅，找到你想投入和改进的领域。然后你就不会再来知乎问这类「有没有必要学习 X」的问题了。</p>  
</div>
            