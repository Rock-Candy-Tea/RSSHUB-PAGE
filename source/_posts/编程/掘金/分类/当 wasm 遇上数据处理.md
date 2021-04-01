
---
title: '当 wasm 遇上数据处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4cf15261a864f94975795131148e0ab~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 19:48:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4cf15261a864f94975795131148e0ab~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文/ 阿里<a href="https://imgcook.alibaba-inc.com/blog" target="_blank" rel="nofollow noopener noreferrer">淘系 F(x) Team</a> - <a href="https://github.com/WenheLI" target="_blank" rel="nofollow noopener noreferrer">文赫</a></p>
</blockquote>
<h2 data-id="heading-0">背景：JavaScript 中的哪些数学困境</h2>
<p>本文主要讲述了，如何快速的将一些已经成熟的算法迁移到 JavaScript 并在生产环境中部署的一些心得和体会。而文中提到的能力也会合入我们的开源项目 -- <a href="https://github.com/imgcook/datacook" target="_blank" rel="nofollow noopener noreferrer">Datacook</a> 中。
后续，我们也会单独出一篇文章来介绍 Datacook 的前世今生和使用场景～</p>
<p>首先我们来看看， Datacook 到底是个啥？
Datacook 的定位是<strong>一个高性能的 Node.js 和浏览器通用的数据处理 / 特征工程 / 数据集制作的工具库</strong>。</p>
<img width="88.94062863795111%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4cf15261a864f94975795131148e0ab~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
> 可以参考上方的 README，我们可以通过上面的方法调用 datacook 中的各类方法。 
<p>后期也会嵌入到 ODPS 环境作为 JavaScript 进行数据处理的一个组成部分。同时，借助 Datacook，将数据处理链路迁移至 JavaScript 使我们可以在 JavaScript 完成完整的深度学习链路（数据处理 / 特征工程 / 模型训练 / 模型推理 / 模型部署）。</p>
<h2 data-id="heading-1">能不能在 JavaScript 中实现一个 Beta 分布的函数？</h2>
<p>这几天收到同学提出的一个问题 “能不能在 JavaScript 中实现一个 Beta 分布（Beta Distribution -- 下文简称 Beta）的函数？”。
刚接手这个问题的时候很疑惑，这种统计学常用的分布按理说在 Python 的中都有实现，为啥不能通过直接调用或者使用 <a href="https://alibaba.github.io/pipcook/#/manual/intro-to-boa" target="_blank" rel="nofollow noopener noreferrer">Boa</a> 来完成这个能力？究其原因，是因为这个同学想把功能部署在 Serverless 服务上，这就对容器用了较高要求导致直接使用 Python 或者使用 Boa 变得十分困难。
那么，为了让这位同学能够成功的把 Beta 分布部署在 Serverless 上，我开始了复习统计的旅程（大雾 🙃🙃🙃</p>
<h2 data-id="heading-2">第一次尝试： JavaScript</h2>
<p>去Wiki上简单的查了一下 Beta 分布的定义，发现只要满足下面的公式产生的随机数就可以算是 Beta 分布：
<img width="100%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61688463e60e4ed389281c1f6c292cb6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
其中 x 是随机数，</p><div align="middle"><img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f729d242dfe24882bf1a22ac8982659f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></div><br>
!#card=math&code=%5CGamma%20%3D%20%28n-1%29%21&id=EvCCi)。
看到这么简单的公式，我寻思好家伙，这不是10分钟就能整出来的一个函数（然而这却是噩梦的开始）
看到公式的几十分钟后，便有了如下的代码：<p></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> gamma = <span class="hljs-function">(<span class="hljs-params">n</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> res = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> idx = <span class="hljs-number">1</span>; idx < n-<span class="hljs-number">1</span>; idx++) res *= idx;
    <span class="hljs-keyword">return</span> res;
&#125;

<span class="hljs-keyword">const</span> beta = <span class="hljs-function">(<span class="hljs-params">a, b, x</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> B = gamma(a)*gamma(b)/gamma(a+b);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.pow(x, a-<span class="hljs-number">1</span>)*<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">1</span>-x, b-<span class="hljs-number">1</span>)/B;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随便试了几个数，okay 符合预期，可以考虑封装封装拿到 Serverless 上部署了。然而，就在这个时候，忽然得知 a 和 b 的取值可能上万。那这，不用试也知道，gamma 函数会溢出到 NaN 导致不可用的；而且那样的运算对资源的消耗也是巨大的，需要想办法去优化算法了。</p>
<h2 data-id="heading-3">第二次尝试：tfjs + 数学优化</h2>
<p>对于阶乘入参过大导致的溢出，常见的优化便是取对数，即：</p>
<img width="32.71245634458673%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e0372318b8246b7be73f4e56d12647a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>对于我们的情况：
<img width="86.9615832363213%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6847d6416fde4f44ac12f585aa9093ca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>同时，为了加速运算和保证精确度，我们使用了 tfjs 来实现数学运算逻辑。</p>
<p>基于上面的公式，我们就可以来实现我们的第二版 Beta 函数了～ （代码因为太长了就不在这边展示了）
然而，因为输入的原因，哪怕使用数学公式上的变换，对于较大或者较小的值来说，结果还是会出现下溢 -- 导致结果不准。</p>
<h2 data-id="heading-4">第三次尝试：不要重复造轮子</h2>
<p>经过了前两次冲击，深刻意识到了 Don't Repeat Yourself(DRY, 不要重复造轮子)，这个法则的含义。我开始在 Github 上寻找 Beta 分布的实现。然而，这些实现都大多数实现都是基于 python 和 c++ 的。
但是不管 python 还是 c++ 的实现都依赖了大量的第三方运算库和高级数学函数（这俩都是 js 所缺失的）。就在这时忽然发现有很多 c++ 的实现都只依赖了 stdlib 内的 random 函数就可以完成，忽然想到是不是可以通过 WebAssembly 的方法把这些实现直接编译到 JS 运行时使用？</p>
<h3 data-id="heading-5">Emscripten</h3>
<p>Emscripten 是一个基于 llvm 的用来将 c/c++ 代码编译到 WASM 的工具链。具体的细节可以参考<a href="https://emscripten.org/docs/introducing_emscripten/index.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>。这边我们就不再赘述了～ 在本篇中，我们将使用这个工具链来帮助我们快速的生成所需的 WASM 字节码和对应的胶水代码。</p>
<h4 data-id="heading-6"><img width="71.24563445867288%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7181b89fa3e74c88b35db5d7444f21c4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></h4>
<h3 data-id="heading-7">C++</h3>
<p>我们先来看一段 c++ 的 Beta 函数实现：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><random></span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><stdlib.h></span></span>

<span class="hljs-comment">// refer to https://gist.github.com/sftrabbit/5068941</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">beta_distribution</span>
&#123;</span>
  <span class="hljs-keyword">public</span>:
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">param_type</span>
    &#123;</span>
      <span class="hljs-keyword">public</span>:
        <span class="hljs-keyword">typedef</span> beta_distribution distribution_type;

        <span class="hljs-function"><span class="hljs-keyword">explicit</span> <span class="hljs-title">param_type</span><span class="hljs-params">(<span class="hljs-keyword">double</span> a = <span class="hljs-number">2.0</span>, <span class="hljs-keyword">double</span> b = <span class="hljs-number">2.0</span>)</span>
          : <span class="hljs-title">a_param</span><span class="hljs-params">(a)</span>, <span class="hljs-title">b_param</span><span class="hljs-params">(b)</span> </span>&#123; &#125;

        <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">a</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> a_param; &#125;
        <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">b</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> b_param; &#125;
  
      <span class="hljs-keyword">private</span>:
        <span class="hljs-keyword">double</span> a_param, b_param;
    &#125;;

    <span class="hljs-function"><span class="hljs-keyword">explicit</span> <span class="hljs-title">beta_distribution</span><span class="hljs-params">(<span class="hljs-keyword">double</span> a = <span class="hljs-number">2.0</span>, <span class="hljs-keyword">double</span> b = <span class="hljs-number">2.0</span>)</span>
      : <span class="hljs-title">a_gamma</span><span class="hljs-params">(a)</span>, <span class="hljs-title">b_gamma</span><span class="hljs-params">(b)</span> </span>&#123; 
        rng.seed(rand());
      &#125;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">param</span><span class="hljs-params">(<span class="hljs-keyword">double</span> a, <span class="hljs-keyword">double</span> b)</span>
    </span>&#123;
      a_gamma = gamma_dist_type(a);
      b_gamma = gamma_dist_type(b);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">seed</span><span class="hljs-params">(<span class="hljs-keyword">uint32_t</span> seed)</span> </span>&#123;
      rng.seed(seed);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">generate</span><span class="hljs-params">()</span> </span>&#123;
      <span class="hljs-keyword">return</span> generate_internal(a_gamma, b_gamma);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">min</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-number">0.0</span>; &#125;
    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">max</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-number">1.0</span>; &#125;

    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">a</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> a_gamma.alpha(); &#125;
    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">b</span><span class="hljs-params">()</span> <span class="hljs-keyword">const</span> </span>&#123; <span class="hljs-keyword">return</span> b_gamma.alpha(); &#125;

  <span class="hljs-keyword">private</span>:
    <span class="hljs-keyword">typedef</span> <span class="hljs-built_in">std</span>::gamma_distribution<<span class="hljs-keyword">double</span>> gamma_dist_type;

    <span class="hljs-built_in">std</span>::mt19937 rng;

    gamma_dist_type a_gamma, b_gamma;

    <span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">generate_internal</span><span class="hljs-params">(
      gamma_dist_type& x_gamma,
      gamma_dist_type& y_gamma)</span>
    </span>&#123; 
      <span class="hljs-keyword">double</span> x = x_gamma(rng);
      <span class="hljs-keyword">return</span> x / (x + y_gamma(rng));
    &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码便是基于这个 <a href="https://gist.github.com/sftrabbit/5068941" target="_blank" rel="nofollow noopener noreferrer">gist</a> 修改得到的。其中核心主要是通过 <code>stdlib</code> 中的 <code>gamma_distribution</code> 来完成高精度的 gamma 函数计算继而实现高精度的 beta 函数。其次就是随机数生成的逻辑，因为 js 的随机数的限制（无法设置 seed / 随机长度不够）我们也使用了 <code>stdlib</code> 中实现的 <code>rand.h</code> 来完成随机数生成。
上面的代码，使我们可以仅通过 <code>stdlib</code> 就生成 Beta 分布的能力。</p>
<h3 data-id="heading-8">Emscripten 💗 C++</h3>
<p>有了 C++ 的逻辑实现，我们需要仅需要通过 Emscripten 将 Beta 这个类暴露出去就好了。
在之前的代码基础上，我们只需要：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><emscripten/bind.h></span></span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">beta_distribution</span> &#123;</span>
 ....    
&#125;

<span class="hljs-comment">// Binding code</span>
  EMSCRIPTEN_BINDINGS(Beta) &#123;
  class_<beta_distribution>(<span class="hljs-string">"Beta"</span>)
    .constructor<<span class="hljs-keyword">double</span>, <span class="hljs-keyword">double</span>>()
    .constructor<>()
    .function(<span class="hljs-string">"generate"</span>, &beta_distribution::generate)
    .function(<span class="hljs-string">"setParam"</span>, &beta_distribution::param)
    .function(<span class="hljs-string">"setSeed"</span>, &beta_distribution::seed)
    ;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码，我们告诉 Emscripten 将 我们定义的 <code>beta_distribution</code> 这个 class 以 Beta 这个名字暴露给 Javascript。并实现两个 constructor：入参为两个 double 或者入参为空。
除此之外，我们也将<code>beta_distribution</code> 实现好的三个函数分布注册到 <code>generate</code> , <code>setParam</code> 和 <code>setSeed</code>  JavaScript 的函数空间中。</p>
<h3 data-id="heading-9">编译 & 使用</h3>
<p>有了上面的源码以及 Emscripten 的工具链，我们就可以把上面的实现编译到 WASM 了～
首先，我们先来看看编译参数：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ emcc 
--<span class="hljs-built_in">bind</span> 
  -O3 
  -s ALLOW_MEMORY_GROWTH=1 
  -s MODULARIZE=1  
  -o ./beta.js 
  ./beta.cpp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的命令有几个部分：</p>
<ul>
<li>emcc 就是 Emscripten 版本的 gcc 是我们编译的入口</li>
<li>--bind 是通知编译器我们需要把 c++ class bind 到 JS 上</li>
<li>-O3 意味着最高级的代码优化</li>
<li>-s ALLOW_MEMORY_GROWTH=1 通知编译器内存可以增长</li>
<li>-s MODULARIZE=1 将编译产物模块化 （这一步是为了防止作用域的污染）</li>
</ul>
<p>经过上面的编译，我们就可以得到一个 <code>./beta.js</code> 的胶水代码，其中包含了如何加载 WASM 文件以及将 c++ 的函数/类定义映射到 JS 空间的逻辑；以及一个 <code>./beta.wasm</code> 的 ByteCode 这里面就是我们具体的 Beta 函数的逻辑了。</p>
<p>接下来我们就可以调用这个 WASM 模块了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> betaModule = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./beta'</span>)
<span class="hljs-keyword">const</span> Beta = (<span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> betaModule()).Beta;
<span class="hljs-keyword">const</span> beta = <span class="hljs-keyword">new</span> Beta(<span class="hljs-number">1</span>, <span class="hljs-number">.5</span>)
<span class="hljs-built_in">console</span>.log(beta.generate())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止，我们就通过 WASM + c++ 的方式将一个较为复杂的数学函数轻松的移植到了 JavaScript 的环境中～
而且这段 WASM 代码，也在 3.8 大促期间作为 serverless 服务出现。</p>
<h2 data-id="heading-10">Review 一下</h2>
<h3 data-id="heading-11">性能</h3>
<p>我们先来看一下 wasm 和 c++ native 的运行性能，我们将在 loop 中循环调用我们的实现来计算运算耗时。
我们会惊奇的发现，在这个场景中， wasm 的运行效率随着调用次数的增加而显著优于 c++。这方面可能的原因是，v8 虚拟机对循环和 cache 的优化。初次之外，c++ 会调用系统的 RNG （Random Number Genertor）这部分作为 system call 的耗时是显著的；而 WASM 并不会通过 system call 来完成这部分逻辑。（对于性能这块欢迎来讨论/分析可能的原因。）
<img width="53.43422584400466%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae3716395e0d48429f529a6f54d90672~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">GC</h3>
<p>在部署到生产环境的时候，我们也不是一帆风顺的。由于 WASM 作为一个运行在 JavaScript 中的虚拟机，WASM 自己生成出来的东西没有办法被自动回收，作为调用者也需要注意内存的回收。像是这一次在 38 场景中，初期就出现了因为频繁实例化 WASM 对象导致了，内存泄漏；后期通过修改代码调用逻辑来修复了～
在线上运行中，该实例的内存占用稳定在了很低的一个值（0.01%）上面。</p>
<h2 data-id="heading-13">总结</h2>
<p>总结一下这一次的开发体验，借助 Emscripten 的工具链，我们可以快速的把一些在 c/c++ 生态上已有的生态迁移到 JavaScript。总体开发体验很棒，而且产物稍加修改就可以在生产环境中运行；同时 Emscripten 也提供了 asm.js 作为无法运行 WASM 环境的 fallback 解决方案。</p>
<p>但是，不得不说，Emscripten 还是太重了，生成了很多胶水代码。这一部分都是后期可以持续优化的地方；同时，Emscripten 的代码模型，对于多个平行的 WASM 项目还是不太友好（依赖全局变量，不模块化容易互相污染，模块化增加复杂度）。在工程侧来讲，作为同时用较重的 JavaScript 逻辑和 WASM 逻辑的项目，打包 / 构建 / 测试链路都不是很完善。感觉上面的方向都可以搞大事情。</p>
<p>最后打一个广告，本次实现的 Beta 函数会作为 <a href="https://github.com/imgcook/datacook" target="_blank" rel="nofollow noopener noreferrer">datacook</a> 的一个函数导出供社区使用。同时接下来也会对 Boost 库中常用的数学方法导出到 WASM。也欢迎有兴趣的同学一起来共建学习。</p>
<div align="middle"><img width="26.07683352735739%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1509f53438c84d8a99db0d6bcba13c6d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></div>
  <br>
  <hr>
  <div align="middle"><a href="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" target="_blank" rel="nofollow noopener noreferrer"> 淘系前端-F-x-Team 开通微博</a> 啦！</div>
  <div align="middle">除文章外还有更多的团队内容等你解锁🔓</div>
  <div align="middle">
    <a href="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" target="_blank" rel="nofollow noopener noreferrer"> 
      <img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adb82f16b0f24a438daf299730dc50df~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
    </a>
  </div>
  <br></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            