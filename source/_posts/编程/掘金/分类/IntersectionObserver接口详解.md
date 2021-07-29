
---
title: 'IntersectionObserver接口详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/393b1776b50245b6a039af49069fc8e8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 07:13:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/393b1776b50245b6a039af49069fc8e8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1 概念</h3>
<p>MDN</p>
<pre><code class="copyable">IntersectionObserver接口(从属于Intersection Observer API)为开发者提供了一种可以异步监听目标元素与其祖先或视窗(viewport)交叉状态的手段。祖先元素与视窗(viewport)被称为根(root)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>讲白了，就是观察一个元素是否在视窗(指定根元素)内可见</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/393b1776b50245b6a039af49069fc8e8~tplv-k3u1fbpfcp-watermark.image" alt="121.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2 相关API</h3>
<h4 data-id="heading-2">构造函数</h4>
<pre><code class="copyable">var io = new IntersectionObserver(callback, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码会返回一个<code>IntersectionObserver</code>实例，<code>callback</code>是当元素的可见性变化时候的回调函数，<code>options</code>是一些配置项（可选）。</p>
<p>我们使用返回的这个实例来进行一些操作</p>
<pre><code class="copyable">io.observe(document.querySelector('img'))  开始观察，接受一个DOM节点对象
io.unobserve(element)   停止观察 接受一个element元素
io.disconnect() 关闭观察器
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">options</h4>
<h5 data-id="heading-4">root</h5>
<p>用于观察的根元素，默认是浏览器的视口，也可以指定具体元素，指定元素的时候用于观察的元素必须是指定元素的子元素</p>
<h5 data-id="heading-5">threshold</h5>
<p>用来指定交叉比例，决定什么时候触发回调函数，是一个数组，默认是<code>[0]</code></p>
<pre><code class="copyable">const options = &#123;
    root: null,
    threshold: [0, 0.5, 1]
&#125;
var io = new IntersectionObserver(callback, options)
io.observe(document.querySelector('img'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码，我们指定了交叉比例为0，0.5，1，当观察元素img0%、50%、100%时候就会触发回调函数</p>
<h5 data-id="heading-6">rootMargin</h5>
<p>用来扩大或者缩小视窗的的大小，使用css的定义方法，<code>10px 10px 30px 20px</code>表示top、right、bottom 和 left的值</p>
<pre><code class="copyable">const options = &#123;
    root: document.querySelector('.box'),
    threshold: [0, 0.5, 1],
    rootMargin: '30px 100px 20px'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了方便理解，我画了张图，如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cedf8315926745b99352a1980c0b4db0~tplv-k3u1fbpfcp-watermark.image" alt="1234.png" loading="lazy" referrerpolicy="no-referrer">
首先我们来看下图上的问题，蓝线是什么呢？他就是咱们定义的root元素，我们添加了<code>rootMargin</code>属性，将视窗的增大了，虚线就是现在的视窗，所以元素现在也就在视窗里面了。</p>
<p>由此可见，root元素只有在<code>rootMargin</code>为空的时候才是绝对的视窗</p>
<h5 data-id="heading-7">callback</h5>
<p>上面我们说到，当元素的可见性变化时，就会触发callback函数。</p>
<p>callback函数会触发两次，元素进入视窗（开始可见时）和元素离开视窗（开始不可见时）都会触发</p>
<pre><code class="copyable">var io = new IntersectionObserver((entries)=>&#123;
    console.log(entries)
&#125;)

io.observe($0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码，请在chrome控制台进行调试，这里我使用了<code>$0</code>选择了上一次我审查元素的选择的节点</p>
<p>运行结果如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7700d8bfcbd42c2a717b1b8e0537d57~tplv-k3u1fbpfcp-watermark.image" alt="2345.png" loading="lazy" referrerpolicy="no-referrer">
我们可以看到callback函数有个<code>entries</code>参数，它是个<code>IntersectionObserverEntry</code>对象数组，接下来我们重点说下IntersectionObserverEntry对象</p>
<h5 data-id="heading-8">IntersectionObserverEntry</h5>
<p><code>IntersectionObserverEntry</code>提供观察元素的信息，有七个属性。</p>
<pre><code class="copyable">boundingClientRect 目标元素的矩形信息\
intersectionRatio 相交区域和目标元素的比例值 intersectionRect/boundingClientRect 不可见时小于等于0\
intersectionRect 目标元素和视窗（根）相交的矩形信息 可以称为相交区域\
isIntersecting 目标元素当前是否可见 Boolean值 可见为true\
rootBounds 根元素的矩形信息，没有指定根元素就是当前视窗的矩形信息\
target 观察的目标元素\
time 返回一个记录从`IntersectionObserver`的时间到交叉被触发的时间的时间戳
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面几个矩形信息的关系如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5902a834d03d4e3d904ee5a010ffee43~tplv-k3u1fbpfcp-watermark.image" alt="345.png" loading="lazy" referrerpolicy="no-referrer">
所以，<strong>intersectionRatio</strong>和<strong>isIntersecting</strong>是用来判断元素是否可见的</p>
<h3 data-id="heading-9">兼容性</h3>
<p>目前IntersectionObserver是一个实验中的功能，请酌情使用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f938bce275ae4ad7a1846193f44331ef~tplv-k3u1fbpfcp-watermark.image" alt="222222222.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            