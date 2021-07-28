
---
title: '百万PV商城实践系列 - 前端图片资源优化实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01ee0ed39c884308bf983638962eb367~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 15:31:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01ee0ed39c884308bf983638962eb367~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️ 本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p><code>百万PV商城系列</code>主要收录我在商城项目中的<code>实践心得</code>，我会从<code>视觉体验</code>、<code>性能优化</code>、<code>架构设计</code>等三个维度出发，一步一步为大家讲解商城项目中前端<code>出现的问题</code>，<code>问题解决的思路与方案</code>，最后再进行<code>代码实践</code>。让你在工作中碰到类似问题时，能够更加得心应手。</p>
<p>本篇是商城实践系列的第一篇文章，主要内容是对商城项目中常见场景的图片资源加载进行优化，提升视觉体验与页面性能。</p>
<h2 data-id="heading-1">背景</h2>
<p>在日常生活中，<code>Yoyo们</code>肯定都用过一些电商公司的<code>App</code>、<code>Web</code>、<code>小程序</code>等应用。在浏览的过程中，会有非常多琳琅满目的图片，比如常见的商品卡、商品详情、轮播图、 广告图等组件都需要使用一些后台管理配置上传的图片资源。</p>
<p>除此之外，这些组件所在的页面也大都是流量承担非常大的页面，如果用户的体验感官比较差，必然会影响用户的留存转化。那么，本篇文章我们就来学习一下图片资源优化的一些方案技巧，我会分别从普通图片、高保真图片、长屏渲染图这三个场景，依次给大家讲讲工作中的实战操作。如果碰到相应的优化场景，你就能够从容以对了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01ee0ed39c884308bf983638962eb367~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">普通图片优化</h2>
<p>对于普通图片优化，我以懒加载(lazyLoad)作为主要的实施手段。懒加载说白了就是优先加载可视窗口内的图片资源，而可视窗口外的内容只有滚动后进入可视窗口内才会进行加载。</p>
<p>那么，我为什么会用懒加载，以及懒加载的实现方案到底是什么呢？下面，我通过一个简单的<code>React</code>的图片懒加载方案的实现，来一步一步说明。</p>
<h3 data-id="heading-3">为什么使用懒加载？</h3>
<p>一般来说，刚进入网页页面就会有大批量的图片资源加载，这会间接影响页面的加载，增加白屏加载时间，影响用户体验。因此，我们的诉求就是<code>不在可视化窗口</code>内的图片不尽兴加载，尽可能<code>减少本地带宽</code>的浪费和<code>请求资源</code>的数量。</p>
<p>那么，为什么我会推荐懒加载做为普通图片资源的主要实施手段呢？因为它有两大优点。</p>
<ul>
<li>减少带宽资源消耗，减少不必要的资源加载消耗。</li>
<li>防止并发加载图片资源导致的资源加载阻塞，从而减少白屏时间。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51e16bc65cae423ab099e512089a20d1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">实现简单的懒加载</h3>
<p>那么，懒加载怎么实现呢？实现的方式有两种。</p>
<ul>
<li>通过<code>scroll</code>事件来监听视窗滚动区域实现。该方法兼容性好，绝大多数浏览器和<code>WebView</code>都兼容支持。</li>
<li>通过<code>IntersectionObserver API</code>观察<code>DOM</code>是否出现在视窗内，该方法优点在于调用简单，只是部分移动端兼容没有上一种方式好。</li>
</ul>
<p>两种形式都是在观察当前<code>DOM</code>是否出现在了可视窗口内，如果出现的话就将<code>data-src</code>中的图片地址赋值给<code>src</code>，然后开始加载当前的图片。</p>
<p>那么，下面我们就开始着手实现一个基于<code>scroll</code>事件的懒加载示例吧。</p>
<h3 data-id="heading-5">页面布局</h3>
<p>我们先画一个基本的页面布局出来，主要是将视窗和图片加载出来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ImageLazy = <span class="hljs-function">() =></span> &#123;
  
  <span class="hljs-keyword">const</span> [list, setList] = useState([
    <span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>
  ])

  <span class="hljs-keyword">const</span> ref = useRef<HTMLDivElement | <span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"scroll-view"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">ref</span> &#125;></span>
      &#123;list.map((id) => &#123;
          return (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;id&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"scroll-item"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">img</span>
                <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> '<span class="hljs-attr">100</span>%', <span class="hljs-attr">height:</span> '<span class="hljs-attr">100</span>%' &#125;&#125;
                <span class="hljs-attr">data-src</span>=<span class="hljs-string">&#123;</span> `$&#123; <span class="hljs-attr">prefix</span> &#125;<span class="hljs-attr">split-</span>$&#123;<span class="hljs-attr">id</span>&#125;<span class="hljs-attr">.jpg</span>` &#125;
              /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          );
        &#125;)&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.scroll-item</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.scroll-view</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
  <span class="hljs-attribute">overflow</span>: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看效果图，在页面上只显示了两张图片，但其实所有的图片都已经加载完了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea2de86884ab4732ac9a752481417672~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">注册scroll事件</h3>
<p>为<code>scroll-view</code>绑定了<code>ref</code>之后，同时需要在<code>useEffect</code>中对<code>scroll</code>事件进行绑定和注销。</p>
<p>如下，我先获取当前组件所有的<code>img</code>元素(真实操作最好使用指定className)，为<code>ref.current</code>进行<code>addEventListener</code>添加事件监听操作，然后在回调中执行对应的方法。</p>
<p>同时，在<code>return</code>的时候，也需要将其事件移除，避免造成一些意外情况。</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> imgs = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'img'</span>);
    <span class="hljs-built_in">console</span>.log(ref.current, <span class="hljs-string">'current'</span>)
    ref.current?.addEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listens run'</span>)
    &#125;)
    <span class="hljs-keyword">return</span> (
      ref.current?.removeEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listens end'</span>)
      &#125;)
    )
  &#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图，在我滚动的时候，同时执行了<code>ScrollCallback</code>，控制台打印了很多执行结果，意味着我们的事件已经添加成功了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9437000c441409984ac48507bc4f970~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">滚动回调 & 节流函数</h3>
<p>通过下面的分析图，我们可以看到<code>clientHeight </code>是我们视窗的高度，而在<code>ScrollView</code>当中每次滚动都会触发<code>scroll</code>方法回调，可以拿到当前页面视窗的滚动距离<code>scrollTop </code>。</p>
<p>那么，我们又如何判断元素是否出现在页面上呢？</p>
<p>通过元素的<code>offsetTop</code>属性，可以知道当前元素距离顶部的偏移距离。那么，当我们拿到窗口的高度<code>clientHeight</code>，滚动的距离<code>scrollTop</code>，以及元素距离顶部的距离<code>offsetTop</code>，就可以推断出下面一套条件公式，通过<code>视窗高度(dom.clientHeight) + 滚动距离(dom.scrollTop) > 元素距离顶部距离(image.offsetTop)</code>来判断当前元素是否出现在页面可视范围内了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78414350a8a3464180b779c2f5adcded~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将其转换为函数方法实现结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scrollViewEvent</span> (<span class="hljs-params">images: HTMLCollectionOf<HTMLImageElement></span>) </span>&#123;
    
  <span class="hljs-comment">// 可视化区域高度</span>
  <span class="hljs-keyword">const</span> clientHeight = ref.current?.clientHeight || <span class="hljs-number">0</span>
  
  <span class="hljs-comment">// 滚动的距离</span>
  <span class="hljs-keyword">const</span> scrollTop = ref.current?.scrollTop || <span class="hljs-number">0</span>
  
  <span class="hljs-comment">// 遍历imgs元素</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> image <span class="hljs-keyword">of</span> images) &#123;
    <span class="hljs-keyword">if</span> (!image.dataset.src) <span class="hljs-keyword">continue</span>
  
    <span class="hljs-comment">// 判断src是否已经加载</span>
    <span class="hljs-keyword">if</span> (image.src) <span class="hljs-keyword">continue</span>
    
    <span class="hljs-comment">//图片距离顶部距离</span>
    <span class="hljs-keyword">let</span> top = image.offsetTop
    
    <span class="hljs-comment">// 公式</span>
    <span class="hljs-keyword">if</span> (clientHeight + scrollTop > top) &#123;
     <span class="hljs-comment">// 设置图片源地址，完成目标图片加载</span>
      image.src = image.dataset.src || <span class="hljs-string">''</span>
      image.removeAttribute(<span class="hljs-string">'data-src'</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我也通过<code>ahook</code>中的<code>useThrottleFn</code>做一点节流的小优化来避免频繁的进行函数回调。在<code>500ms</code>内，事件只会执行一次，避免额外执行带来的性能消耗。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useThrottleFn &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ahooks'</span>

<span class="hljs-comment">// 截流函数hook</span>
<span class="hljs-keyword">const</span> &#123; run &#125; = useThrottleFn(scrollViewEvent, &#123;
  <span class="hljs-attr">wait</span>: <span class="hljs-number">500</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，我们将其放入到<code>scroll</code>事件回调中执行。不过，在组件一开始其实是触发不了<code>scroll</code>事件，因此，需要我们手动来初始化当前第一次页面中的图片数据。</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> imgs = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'img'</span>);
  <span class="hljs-built_in">console</span>.log(ref.current, <span class="hljs-string">'current'</span>)
  ref.current?.addEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-function">() =></span> &#123;
    run(imgs)
  &#125;)
  run(imgs)
  <span class="hljs-keyword">return</span> (
    ref.current?.removeEventListener(<span class="hljs-string">'scroll'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listens end'</span>)
    &#125;)
  )
&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，我们的一个<code>图片懒加载</code>基本就实现完成了，我们来看看效果吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0735ebd4c46a4daab69811f4fa557e44~tplv-k3u1fbpfcp-watermark.image" alt="iShot2021-07-18 12.29.51.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>对于懒加载来说，每个<code>item</code>最好设置一个高度，防止在一开始没有图片时，组件因为没有高度而导致页面元素暴露下视窗内导致懒加载失效。</p>
</blockquote>
<h2 data-id="heading-8">高保真图片优化</h2>
<p>对于高保真这类图片而言，很多都是由<code>相关运营人员</code>配置的活动图，一般在大促期间会有很多<code>微页面</code>，或者是<code>图片链接</code>，都是通过<code>图片 + 热区</code>的形式发布给用户浏览的。</p>
<p>因此，绝大多数运营诉求都是尽可能清晰展示对应的图片。那么懒加载显然并不能很好的解决问题，因此我在原先懒加载的基础上，新增了一些加载状态给用户视觉上的体验感官，目前市面上产品主要使用<code>骨架屏</code> 或者是<code>渐进式加载</code>等方案来让图片显示过渡更加的平滑，避免加载失败或者加载图片卡顿的尴尬。</p>
<h3 data-id="heading-9">如何实现</h3>
<p>通过下面的这张图，依旧先来梳理下实现逻辑。在图片组件中，分别有两张图进行轮流替换，当高清资源图加载完毕后，需要将<code>骨架图</code>或者<code>缩略图</code>隐藏，显示已经加载好的高清图。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c029f710dac645a7b5a067c8cee4022c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">图片组件</h3>
<p>分析结束后, 可以跟我来实现一个简单的图片组件，通过<code>img</code>中的<code>onLoad</code>事件来判断需要显示的图片是否已经加载完了。通过对应的<code>状态(status)</code>来控制略缩图的显示和隐藏。下面我就以渐进式加载来作为案例，参考下图，我们来实现一个简单的状态切换组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.css"</span>;

interface ImageProps <span class="hljs-keyword">extends</span> React.ImgHTMLAttributes<HTMLImageElement> &#123;
  <span class="hljs-attr">thumb</span>: string;
&#125;

type ImageStatus = <span class="hljs-string">'pending'</span> | <span class="hljs-string">'success'</span> | <span class="hljs-string">'error'</span>

<span class="hljs-keyword">const</span> Image: React.FC<ImageProps> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [status, setImageStatus] = React.useState<ImageStatus>(<span class="hljs-string">'pending'</span>);

  <span class="hljs-comment">/**
   * 修改图片状态
   * <span class="hljs-doctag">@param </span>status 修改状态
   */</span>
  <span class="hljs-keyword">const</span> onChangeImageStatus = <span class="hljs-function">(<span class="hljs-params">status: ImageStatus</span>) =></span> &#123;

    <span class="hljs-comment">/** TODO setTime模拟请求时间 */</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> setImageStatus(status), <span class="hljs-number">2000</span>)
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span>
        <span class="hljs-attr">className</span>=<span class="hljs-string">"image image__thumb"</span>
        <span class="hljs-attr">alt</span>=<span class="hljs-string">&#123;props.alt&#125;</span>
        <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;props.thumb&#125;</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">visibility:</span> <span class="hljs-attr">status</span> === <span class="hljs-string">'success'</span> ? "<span class="hljs-attr">hidden</span>" <span class="hljs-attr">:</span> "<span class="hljs-attr">visible</span>" &#125;&#125;
      /></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span>
        <span class="hljs-attr">onLoad</span>=<span class="hljs-string">&#123;()</span> =></span> onChangeImageStatus('success')&#125;
        onError=&#123;() =>onChangeImageStatus('error')&#125;
        className="image image__source"
        alt=&#123;props.alt&#125;
        src=&#123;props.src&#125;
      />
    <span class="hljs-tag"></></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Image;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>filter: blur(25px);</code>属性，对略缩图添加了一部分模糊效果，这样就可以避免一些马赛克图的尴尬，来达到部分毛玻璃，或者说是高斯模糊的一些小特效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81f8c549a1f742bd9c65e2a0417de7f5~tplv-k3u1fbpfcp-watermark.image" alt="iShot2021-07-20 00.58.24.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>通过<code>onLoad</code>加载完毕的事件，我们做了一个简单的渐进式图片加载，那么相应的类似于骨架屏等其它的加载态也可以通过一样的状态判断来进行实现的。只是将缩略图换成了其它组件，仅此而已。</p>
</blockquote>
<h2 data-id="heading-11">长渲染图优化</h2>
<p>在商品详情页面，运营会配置一些商品的详细描述图文，不仅对图片的质量会比较高，同时图片也会非常长。那么很显然，我们并不可能说直接拿到图片就显示在页面上，如果用户的网速比较慢的情况下，页面上就会直接出现一个很长的白条，或者一张加载失败的错误图。这些很明显不是我们想要的结果。</p>
<p>那么，该怎么办呢？</p>
<p>我们先看下淘宝等电商平台的一个商品详情，当你点开看大图时，会发现只显示了图片的一部分，会分成很多张张大小一致的图片给我们。</p>
<p>依照这个思路，我们也做了相对应的切图优化，将一张长图分成多个等比例大小的多张图块，来进行一个分批渲染调优，减少单次渲染长图的压力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e3129a81424197bc65d6bc4cb756b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">切图成块</h3>
<p>那么，下面我会从模拟后端长图切短图在将其切割好的图片依次显示在页面中进行展示。话不多说，我们直接进入正题。</p>
<p>首先，结合下面的分析图，我们的切图原理其实非常简单，将一张长图分成长宽相等的小图，如果最后一张不满足<code>切割块高度</code>的话直接将剩余高度给单切成图片。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536acc8ce579434ca914e833f0685224~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，下面我就写一个简单的node代码来带大家实战一下切图的过程。</p>
<h3 data-id="heading-13">Node切图</h3>
<p>如下图，我会模拟一张运营上传的一张长图，然后切割成若干份右边高<code>200</code>的短图（大小按照需求评估）。下面，我们就来看下实现效果的教程和代码吧。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7447eefb75e4c9bb226ed382ffc2f70~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，安装<code>sharp</code>用于图片处理，<code>image-size</code>用于图片大小信息的获取。</p>
<pre><code class="hljs language-js copyable" lang="js"># shell

yarn add sharp image-size
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当拿到图片的高度和宽度的时候，那么意味着我可以通过一个<code>while</code>循环将切割的等份高度给计算好。</p>
<pre><code class="hljs language-js/** copyable" lang="js/**">const SPLIT_HEIGHT = 200

/** @name 长图高度 */
let clientHeight = currentImageInfo.height

/** @name 切割小图高度 */
const heights = []

while (clientHeight > 0) &#123;
  /** @if 切图高度充足时 */
  if (clientHeight >= SPLIT_HEIGHT) &#123;
    heights.push(SPLIT_HEIGHT)
    
    clientHeight -= SPLIT_HEIGHT
    
  &#125; else &#123;
    /** @else 切割高度不够时，直接切成一张，高度清0 */
    heights.push(clientHeight)
    
    clientHeight = 0
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/489cf6f06bed427f8445c773cac889f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，当我知道了切割的图片大小后，就可以对切割好的<code>heights</code>遍历，通过<code>裁剪偏移</code>切割成为真实的图片，并生成新的文件并保存起来。</p>
<p>下面代码中，我创建一个<code>marginTop</code>偏移量，每切割一次，就会将其<code>height</code>累加向下偏移，直到切割图片到最后一页结束为止。此时<code>mariginTop</code> 为图片的高度。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** <span class="hljs-doctag">@name </span>偏移量 */</span>
<span class="hljs-keyword">let</span> marginTop = <span class="hljs-number">0</span>

heights.forEach(<span class="hljs-function">(<span class="hljs-params">h, index</span>) =></span> &#123;
  sharp(<span class="hljs-string">'./input.jpg'</span>)
    .extract(&#123; <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">top</span>: marginTop, <span class="hljs-attr">width</span>: currentImageInfo.width, <span class="hljs-attr">height</span>: h &#125;)
    .toFile(<span class="hljs-string">`./img/split_<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>_block.jpg`</span>).then(<span class="hljs-function"><span class="hljs-params">info</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`split_<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>_block.jpg切割成功`</span>)
    &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(err), <span class="hljs-string">'error'</span>)
    &#125;)
    marginTop += h
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图，<code>img文件夹</code>下多了一些<code>零碎的图片</code>，然后检查一下图片是否<code>拼接完整</code>，如果没有问题的话，那么我们就完成了一个简单的长图切块的需求，下一步就是放到前端进行<code>渲染</code>了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3f7c20d812849dcbca055738f2c46b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">前端展示</h3>
<p>前端拿到对应的切片后，直接拼凑在前端页面上展示，处理掉中间的缝隙或者和毛边后，和长图渲染毫无差别。我渲染时依旧是采用懒加载的形式做了简单的加载优化，整体效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3690f937438e42d9bc9bb147c6275c3b~tplv-k3u1fbpfcp-watermark.image" alt="iShot2021-07-19 00.41.35.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看完了加载效果后，那么来看看加载的响应时间吧。</p>
<p>由于我切好的图片并没有做<code>文件上的优化</code>，因此单张图存在<code>体积过大</code>，但是丝毫不影响首屏的加载，下面可以看一张在<code>Flow3G</code>下的加载时间对比。</p>
<p>对于单张长图意味着用户可能会看到4s左右的<code>白屏</code>或者是<code>骨架屏</code>，而切片后加载可以优先的将部分内容展现给用户。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2911d24864bd4b418976732d933b5478~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">解决毛边或者缝隙</h3>
<p>本方案在最终实现时，可能会有部分瑕疵，具体切图方案和设备型号有关系。如果碰到问题，可以参考我的一些解决方案：</p>
<ul>
<li>第一种是通过<code>vertical-center</code>设置垂直中心值来解决基线对齐问题。</li>
<li>第二种是将<code>img</code>设置成一个真实<code>block</code>元素解决。</li>
<li>第三种是我常用的是通过<code>flex-direction</code>设置为<code>column</code>为子元素做垂直排列解决问题。</li>
<li>第四种是通过<code>background</code>图片的方式解决问题。但这样做的话如果想使用懒加载，就需要更改部分<code>css</code>样式偏移来达到可视窗口显示。</li>
</ul>
<h2 data-id="heading-16">参考资源</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ffrontend-digest.com%2Fprogressively-loading-images-in-react-107cb075417a%3Fgi%3D18c351878404" target="_blank" rel="nofollow noopener noreferrer" title="https://frontend-digest.com/progressively-loading-images-in-react-107cb075417a?gi=18c351878404" ref="nofollow noopener noreferrer"># Progressively Loading Images In React</a></li>
<li><a href="https://juejin.cn/post/6965761736083243044" target="_blank" title="https://juejin.cn/post/6965761736083243044"># 前端性能优化——图片篇</a></li>
<li><a href="https://juejin.cn/post/6844903614138286094" target="_blank" title="https://juejin.cn/post/6844903614138286094"># 懒加载和预加载</a></li>
<li><a href="https://juejin.cn/post/6844903496102199304" target="_blank" title="https://juejin.cn/post/6844903496102199304"># 性能优化之组件懒加载: Vue Lazy Component 介绍</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FWangly19%2Flazy-image" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/Wangly19/lazy-image" ref="nofollow noopener noreferrer"># 示例图片&Demo地址</a></li>
</ul>
<h2 data-id="heading-17">总结</h2>
<p>本篇文章中，我讲了三种不同图片的优化策略。市面上已经有很多<code>开源库</code>能够较为方便的实现<code>懒加载</code>和<code>渐进加载</code>的方式。同时，对于骨架屏，很多组件库都有对应的组件，封装起来成本也较小。</p>
<p>因此，如果在项目中确实涉及很多图片资源，那么文章中提到的优化方案是我比较推荐的。</p>
<ul>
<li>能做成懒加载的尽量不要全量加载</li>
<li>给予用户一定的状态提示，骨架屏或者是过渡图能做尽量别拉下。</li>
<li>长图能切图尽量切图，将其拆开来优化是非常方便的。</li>
<li>所有的图片能上<code>CDN</code>就尽可能上<code>CDN</code>。</li>
<li>能压缩的图片尽可能去进行压缩。</li>
</ul>
<blockquote>
<p>对于一个商城项目来说，它的挑战性不是在于功能的实现逻辑上，而在于部分视觉感受与体验的优化上。如果觉得文章对你有帮助，可以点个👍，给我加个油。如果对前端电商项目想了解更多的Yoyo们可以关注本专栏。</p>
</blockquote>
<h2 data-id="heading-18">近期好文</h2>
<ul>
<li><a href="https://juejin.cn/post/6984908770149138446" target="_blank" title="https://juejin.cn/post/6984908770149138446"># 【收藏就会】浏览器WebStorage缓存使用指南</a></li>
<li><a href="https://juejin.cn/post/6976782987480432670" target="_blank" title="https://juejin.cn/post/6976782987480432670"># 我 & 掘金，毕业一年后，我被掘金签约了｜2021 年中总结</a></li>
<li><a href="https://juejin.cn/post/6970841540776329224" target="_blank" title="https://juejin.cn/post/6970841540776329224"># 总结TypeScript在项目开发中的应用实践体会</a></li>
</ul>
<h2 data-id="heading-19">尾注</h2>
<blockquote>
<p>本文首发于：掘金技术社区<br>
类型：签约文章<br>
作者：wangly19<br>
收藏于专栏：<a href="https://juejin.cn/column/6984070080191528997" target="_blank" title="https://juejin.cn/column/6984070080191528997"># 百万PV商城实践系列</a><br>
公众号: ItCodes 程序人生</p>
</blockquote></div>  
</div>
            