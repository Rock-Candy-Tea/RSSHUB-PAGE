
---
title: '原生JS实现图片懒加载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202c88e5e17a4fda938c86d65e8295d3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 18:37:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202c88e5e17a4fda938c86d65e8295d3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>图片懒加载是一种网页性能优化的方式，它能极大的提高用户体验。同时在面试的时候也经常容易被面试官问到其实现和原理，很早之前就接触过，由于最近几个月都没有写文章了，想着借此机会顺便复习一下</p>
</blockquote>
<h3 data-id="heading-0">为什么需要懒加载？</h3>
<p>在一些图片比较多的网站（比如说大型电商网站）图片是非常多的，如果我们在打开网页的一瞬间就把网站的所有图片加载出来，很有可能造成卡顿和白屏的现象，用户体验变得极其的差，要是遇到脾气暴躁的小伙伴相信直接反手就是一个Ctrl+W。<br>
因为图片真的很多，一瞬间就把网站的所有图片加载出来浏览器短时间内根本处理不完，但是我们打开网站的那一瞬间仅仅只能看到视口内的图片，这时候去加载网页最底部的图片是非常浪费资源和没有必要的，所以遇到这种情况使用<code>懒加载</code>技术就显得尤为必要了。</p>
<h3 data-id="heading-1">懒加载实现原理</h3>
<p>懒加载的原理其实很简单，就是预先将图片真实的<code>src</code>放在我们自定义的属性里面（比如<code>data-src</code>），当图片出现在了我们的视口范围之内的时候，再把<code>data-src</code>赋值给<code>src</code>属性，完成图片加载。</p>
<pre><code class="hljs language-html copyable" lang="html">// 页面初始化时
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img11.360buyimg.com/pop/s590x470.jpg.webp"</span> /></span>

// 当图片出现在了视口范围之内
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img11.360buyimg.com/pop/s590x470.jpg.webp"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://img11.360buyimg.com/pop/s590x470.jpg.webp"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>这里有个点就是初始化时可以不给img标签加上<code>src</code>属性，因为只要存在<code>src</code>属性，浏览器就会去执行一次请求将其指向的资源下载并应用到文档内，这里不加上可以提升一些性能</em></strong></p>
<h3 data-id="heading-2">具体实现</h3>
<p>基于前面讲解的思路，我们自己手写一个懒加载</p>
<p>新建一个<code>lazyload.html</code>文件，初始化dom结构并设置对应的样式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>lazy load<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.img</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">220px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">220px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#ccc</span>;
      <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">40px</span>;
      <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">50px</span>;
    &#125;

    <span class="hljs-selector-class">.pic</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-comment"><!--将真实的src先放在data-src中--></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/183679/11/2189/143829/6091f5d8E933e7ad1/e3e2001666f2ce7b.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img12.360buyimg.com/n7/jfs/t1/192682/11/617/163213/608b887aEddbbbee3/9570466a90d02f79.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img14.360buyimg.com/n7/jfs/t1/156161/35/18802/268242/60641d96Eca3dee7f/4a32070a19deb4f5.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/130179/12/9273/167054/5f5468edE9d4ecd9c/39f7520d9f76b695.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img14.360buyimg.com/n7/jfs/t1/100888/13/13132/105320/5e5533c6Ea8daa487/f95d7ba4da5581c5.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/173986/31/8862/291849/6098d6d0E26c55012/c2144f6e074556d2.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/110754/4/12605/101916/5ee43244E6fbf9433/c42fb5e3f9558a59.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/148370/31/1084/45848/5eedc2eeEfdc2cd46/f3c3a6f0bd7998be.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img10.360buyimg.com/n7/jfs/t1/165930/8/7273/171076/602fd5dfE65a52775/ee27074b7037c020.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img13.360buyimg.com/n7/jfs/t1/190093/28/117/193777/60867822Ea949fbec/6fe51b122d0fdc5a.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pic"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"加载中..."</span> <span class="hljs-attr">data-src</span>=<span class="hljs-string">"https://img14.360buyimg.com/n7/jfs/t1/119501/15/6768/115886/5eca6c36Eb3541dc9/2f4534173878a23c.jpg"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是JS部分，我们需要提前知道几个值，一个是当前浏览器窗口的视口高度，另一个是每张图片距离视口顶部的距离，因为只有当图片距离顶部的距离小于我们的视口高度，那么就代表这张图片已经出现在我们的视口范围内了。</p>
<h4 data-id="heading-3">获取浏览器视口高度</h4>
<p>获取可视区域的高度我们通常使用<code>window.innerHeight</code>就可以拿到了，当然如果需要兼容低版本IE浏览器的话则可以使用<code>document.documentElement.clientHeight</code>来获取，这里我们做一个兼容处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> viewPortHeight = <span class="hljs-built_in">window</span>.innerHeight || <span class="hljs-built_in">document</span>.documentElement.clientHeight
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">获取图片离顶部的距离</h4>
<p>这里我们简单粗暴一点，直接使用<code>getBoundingClientRect()</code>这个方法来获取，对这个方法不了解的小伙伴可以点击<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Element/getBoundingClientRect" target="_blank" rel="nofollow noopener noreferrer">这里</a>进行查看</p>
<p>到这里，我们所需要的两个值就都可以拿到了，下面直接上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取所有图片</span>
<span class="hljs-keyword">const</span> imgList = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'img'</span>)
<span class="hljs-comment">// 用于记录当前显示到了哪一张图片</span>
<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lazyload</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 获取浏览器视口高度,这里写在函数内部是考虑浏览器窗口大小改变的情况</span>
  <span class="hljs-keyword">const</span> viewPortHeight = <span class="hljs-built_in">window</span>.innerHeight || <span class="hljs-built_in">document</span>.documentElement.clientHeight
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = index; i < imgList.length; i++) &#123;
    <span class="hljs-comment">// 这里用可视区域高度减去图片顶部距离可视区域顶部的高度</span>
    <span class="hljs-keyword">const</span> distance = viewPortHeight - imgList[i].getBoundingClientRect().top;
    <span class="hljs-comment">// 如果可视区域高度大于等于元素顶部距离可视区域顶部的高度，说明图片已经出现在了视口范围内</span>
    <span class="hljs-keyword">if</span> (distance >= <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 给图片赋值真实的src，展示图片</span>
      imgList[i].src = imgList[i].getAttribute(<span class="hljs-string">'data-src'</span>);
      <span class="hljs-comment">// 前i张图片已经加载完毕，下次从第i+1张开始检查是否需要显示</span>
      index = i + <span class="hljs-number">1</span>;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 定义一个防抖函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, delay = <span class="hljs-number">500</span>, ...args</span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 这里的e是event事件对象</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) <span class="hljs-built_in">clearTimeout</span>(timer);
    timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      fn.apply(<span class="hljs-built_in">this</span>, args);
    &#125;, delay);
  &#125;;
&#125;

<span class="hljs-comment">// 页面加载完成执行一次lazyload，渲染第一次打开的网页视口内的图片</span>
<span class="hljs-built_in">window</span>.onload = lazyload;
<span class="hljs-comment">// 监听Scroll事件，为了防止频繁调用，使用防抖函数进行优化</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"scroll"</span>, debounce(lazyload, <span class="hljs-number">600</span>));
<span class="hljs-comment">// 浏览器窗口大小改变时重新计算</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, debounce(lazyload, <span class="hljs-number">600</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">最后效果</h3>
<p>到这里我们的图片懒加载就写完了，下面是效果图，喜欢的朋友麻烦点个赞吧</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202c88e5e17a4fda938c86d65e8295d3~tplv-k3u1fbpfcp-watermark.image" alt="collapse.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            