
---
title: '电商最小存货 - SKU 和 算法实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 15:56:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b9845f2d65f419ba5eb876d2bf56af3~tplv-k3u1fbpfcp-watermark.image" alt="晴天.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 113 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fsku-about" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/sku-about" ref="nofollow noopener noreferrer">电商最小存货 - SKU 和 算法实现</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>目前电商平台的业务中，只要有商品，不可避免的会遇到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259C%2580%25E5%25B0%258F%25E5%25AD%2598%25E8%25B4%25A7%25E5%258D%2595%25E4%25BD%258D%2F892217%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%9C%80%E5%B0%8F%E5%AD%98%E8%B4%A7%E5%8D%95%E4%BD%8D/892217?fr=aladdin" ref="nofollow noopener noreferrer">SKU</a> 方面功能。这篇文章就从理论到实践，从商品创建到商品购买，手把手带你实现 SKU 相关的“核心算法”。</p>
<p>让我们看看实际场景：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc5eb806c3204824b09abe663cd80cf3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了上图规格选中预处理，就能够帮助用户在购买商品时，直观的了解到商品是否可以购买。</p>
<p>在我们实际开发过程中，商品创建页会先进行规格组装，商品购买页会对规格选择做处理。规格组装通过规格组合成 SKU 集合，规格选择根据规格内容获取库存数据量，计算 SKU 是否可被选择，两者功能在电商流程中缺一不可。</p>
<h2 data-id="heading-1">组装 SKU 实践</h2>
<h4 data-id="heading-2">属性描述</h4>
<p>根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259C%2580%25E5%25B0%258F%25E5%25AD%2598%25E8%25B4%25A7%25E5%258D%2595%25E4%25BD%258D%2F892217%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%9C%80%E5%B0%8F%E5%AD%98%E8%B4%A7%E5%8D%95%E4%BD%8D/892217?fr=aladdin" ref="nofollow noopener noreferrer">百度百科</a>解释的 SKU</p>
<ul>
<li>最小存货单位( Stock Keeping Unit ) 在连锁零售门店中有时称单品为一个 SKU，定义为保存库存控制的最小可用单位，例如纺织品中一个 SKU 通常表示规格、颜色、款式。</li>
</ul>
<h4 data-id="heading-3">业务场景</h4>
<ul>
<li>只要是做电商类相关的产品，比如购物 APP、购物网站等等，都会遇到这么一个场景，每个商品对应着多个规格，用户可以根据不同的规格组合，选择出自己想要的产品。我们自己在生活中也会经常用到这个功能。</li>
</ul>
<p>通过上面描述，让我们把概念和实际数据关联起来，下面让我们来举个🌰 ：</p>
<p>现有规格</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> type = [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"女裤"</span>]
<span class="hljs-keyword">const</span> color = [<span class="hljs-string">"黑色"</span>, <span class="hljs-string">"白色"</span>]
<span class="hljs-keyword">const</span> size = [<span class="hljs-string">"S"</span>,<span class="hljs-string">"L"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么根据现有规格，可以得到所有的 SKU 为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"S"</span>],
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"S"</span>],
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"S"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"S"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"L"</span>],
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述 SKU 是如何得到的呢，让我们一起看看实现思路，并且通过上面的🌰 来计算一遍。</p>
<h3 data-id="heading-4">SKU 组合实现思路</h3>
<h4 data-id="heading-5">笛卡尔积</h4>
<p>首先让我们来看看笛卡尔积的描述</p>
<ul>
<li>笛卡尔乘积是指在数学中，两个[集合] <em>X</em> 和 <em>Y</em> 的笛卡尔积(Cartesian product)，又称 [ 直积 ] ，表示为 <em>X</em>  ×  <em>Y</em>，第一个对象是 <em>X</em> 的成员而第二个对象是 <em>Y</em> 的所有可能 [ 有序对 ] 的其中一个成员</li>
<li>假设集合 A = &#123; a, b &#125;，集合 B = &#123; 0, 1, 2 &#125;，则两个集合的笛卡尔积为 &#123; ( a, 0 ),  ( a, 1 ),  ( a, 2),  ( b, 0),  ( b, 1),  ( b, 2) &#125;</li>
</ul>
<p>看来笛卡尔积满足组合计算的条件，那么下面先来一波思维碰撞，先通过导图，看看怎么实现</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8ce8a7ab96f4b48a9f5ea61f6c23102~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>通过上面的思维导图，可以看出这种规格组合是一个经典的排列组合，去组合每一个规格值得到最终 SKU。</p>
<p>那么让我们来进行代码实现，看看代码如何实现笛卡尔积。</p>
<h3 data-id="heading-6">实现代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
 * 笛卡尔积组装
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> <span class="hljs-variable">list</span></span>
 * <span class="hljs-doctag">@returns </span>[]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">descartes</span>(<span class="hljs-params">list</span>) </span>&#123;
  <span class="hljs-comment">// parent 上一级索引;count 指针计数</span>
  <span class="hljs-keyword">let</span> point = &#123;&#125;; <span class="hljs-comment">// 准备移动指针</span>
  <span class="hljs-keyword">let</span> result = []; <span class="hljs-comment">// 准备返回数据</span>
  <span class="hljs-keyword">let</span> pIndex = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 准备父级指针</span>
  <span class="hljs-keyword">let</span> tempCount = <span class="hljs-number">0</span>; <span class="hljs-comment">// 每层指针坐标</span>
  <span class="hljs-keyword">let</span> temp = []; <span class="hljs-comment">// 组装当个 sku 结果</span>

  <span class="hljs-comment">// 一：根据参数列生成指针对象</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index <span class="hljs-keyword">in</span> list) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> list[index] === <span class="hljs-string">'object'</span>) &#123;
      point[index] = &#123; <span class="hljs-attr">parent</span>: pIndex, <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;;
      pIndex = index;
    &#125;
  &#125;

  <span class="hljs-comment">// 单维度数据结构直接返回</span>
  <span class="hljs-keyword">if</span> (pIndex === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> list;
  &#125;

  <span class="hljs-comment">// 动态生成笛卡尔积</span>
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-comment">// 二：生成结果</span>
    <span class="hljs-keyword">let</span> index;
    <span class="hljs-keyword">for</span> (index <span class="hljs-keyword">in</span> list) &#123;
      tempCount = point[index].count;
      temp.push(list[index][tempCount]);
    &#125;
    <span class="hljs-comment">// 压入结果数组</span>
    result.push(temp);
    temp = [];

    <span class="hljs-comment">// 三：检查指针最大值问题，移动指针</span>
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
      <span class="hljs-keyword">if</span> (point[index].count + <span class="hljs-number">1</span> >= list[index].length) &#123;
        point[index].count = <span class="hljs-number">0</span>;
        pIndex = point[index].parent;
        <span class="hljs-keyword">if</span> (pIndex === <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">return</span> result;
        &#125;
        <span class="hljs-comment">// 赋值 parent 进行再次检查</span>
        index = pIndex;
      &#125; <span class="hljs-keyword">else</span> &#123;
        point[index].count++;
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们看看实际的输入输出和调用结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1164320629884d06ad02dc83f905a52a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么这个经典的排列组合问题就这样解决啦。接下来，让我们再看看，如何在商品购买中，去处理商品多规格选择。</p>
<h2 data-id="heading-7">商品多规格选择</h2>
<p>开始前回顾下使用场景</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad5fc81d76af4f8f8d587137ce60babb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个图片已经能很明确的展示业务需求了。结合上述动图可知，在用户每次选择了某一规格后，需要通过程序的计算去处理其他规格情况，以便给用户提供当前情况下可供选择的其他规格。</p>
<p>那么让我们来看看实现思路，首先在初始化中，提供可选择的 SKU，从可选择的 SKU 中去剔除不包含的规格内容，在剔除后，提供可以进行下一步选择的规格，后续在每次用户点击情况下，处理可能选中的 SKU，最终在全部规格选择完成后，得到选中的 SKU。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acf9b83f4ab5403fbde268a6c40e0d3c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">商品多规格选择实现思路</h2>
<h4 data-id="heading-9">邻接矩阵</h4>
<p>首先，看下什么是邻接矩阵，来自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E9%2582%25BB%25E6%258E%25A5%25E7%259F%25A9%25E9%2598%25B5%2F9796080%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E9%82%BB%E6%8E%A5%E7%9F%A9%E9%98%B5/9796080?fr=aladdin" ref="nofollow noopener noreferrer">百度百科</a>的解释</p>
<ul>
<li>用一个二维数组存放顶点间关系（边或弧）的数据，这个二维数组称为邻接矩阵。</li>
<li>逻辑结构分为两部分：V 和 E 集合，其中，V 是顶点，E 是边。因此，用一个一维数组存放图中所有顶点数据。</li>
</ul>
<p>字面描述可能比较晦涩难懂，那么让我们来看看图片帮助理解，如果两个顶点互通（有连线），那么它们对应下标的值则为 1，否则为 0。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1cb4d8707d49aeb0bfc9b7c0063961~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">让我们继续前面的🌰 数据来看</h4>
<p>规格</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> type = [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"女裤"</span>]
<span class="hljs-keyword">const</span> color = [<span class="hljs-string">"黑色"</span>, <span class="hljs-string">"白色"</span>]
<span class="hljs-keyword">const</span> size = [<span class="hljs-string">"S"</span>,<span class="hljs-string">"L"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设总 SKU 的库存值为下面示例，可选为有库存，不可选为某项规格无库存</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"S"</span>], <span class="hljs-comment">// S 无号</span>
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"S"</span>], <span class="hljs-comment">// S 无号</span>
  [<span class="hljs-string">"男裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"S"</span>], <span class="hljs-comment">// S 无号</span>
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"黑色"</span>, <span class="hljs-string">"L"</span>],
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"S"</span>], <span class="hljs-comment">// S 无号</span>
  [<span class="hljs-string">"女裤"</span>, <span class="hljs-string">"白色"</span>, <span class="hljs-string">"L"</span>],
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么根据邻接矩阵思想，可以得到结果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad2e35a3373b4157b6e12737703ad697~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，SKU 中每两规格都可选择，那么相对的标志值为 1，否则为 0，当整条规格选中都是 1，才会使整条 SKU 链路可选。</p>
<p>思路是有了，但是如何通过代码去实现呢，想必大家也有各种方式去实现，那么我就介绍下自己的实现方式：集合。</p>
<h3 data-id="heading-11">计算思路</h3>
<h4 data-id="heading-12">集合</h4>
<p>高中过去好多年了，难免忘记，这里通过集合说明图一起回顾下集合的定义</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cac8a20f759743e4ade09d1275f2c36e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图来自百度图片</p>
<p>想起集合，那么计算思路算是有了，这边我们需要用集合相等的情况，去处理 SKU 和规格值的计算。</p>
<p>实现思维导图</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ebef0fe0c67494e990198f9c3a86e3a~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>假设一个集合 A&#123;a, b, c&#125; 和另外一个集合 B&#123;a, e&#125;，如何快速判断 B 是否是 A 的子集。这个问题比较简单的方法是用 B 中所有元素依次和 A 中的元素进行比较，对于集合中的元素，每个元素值都是唯一的。通过这样的特性，我们可以把所有字母转换为一个质数，那么 <strong>集合 A 可以表示为集合元素</strong>(<strong>质数</strong>)**的积，B 同样，**B 是否是 A 的子集，这个只需要将 B 除以 A，看看是否可以整除 ，如果可以那么说明，B 是 A 的子集。</li>
<li>那么根据邻接矩阵思路，整条 SKU 都会有一个<code>集合值</code>，集合值由所有涉及规格对应<code>乘积</code>得到的结果，在选择规格过程中，每次选择去根据集合值去反向整除规格对应值去判断是否是子集，是否为 1。</li>
<li>现在根据乘法算法，有了以上的分析，我们可以整理下算法过程：
<ul>
<li>数据预处理，把所有需要处理的规格内容一一对应一个不重复的质数，把 ITEM 组合转换为每个质数的积</li>
<li>根据用户已经选择的 ITEM 进行扫描所有的 ITEM，如果 ITEM 已经被选中，则退出，如果没有， 则和所有已经选择的 ITEM 进行相乘 (因为一个组合不可能出现两个类目相同的 ITEM，所以选中的 ITEM 需要去掉和当前匹配的 ITEM 在同一个类目中的 ITEM ) ，这个乘机就是上文中的集合 B</li>
<li>把集合 B 依次和 SKU 组合构成的积 (相当于上文中的集合 A) 进行相除，比较，如果整除，则退出，当前匹配的 SKU 可以被选中，如果一直到最后还没有匹配上，则当前匹配的 SKU 不可被选中。</li>
</ul>
</li>
</ul>
<p>我们通过集合的思想，看看核心代码吧。</p>
<h3 data-id="heading-13">核心代码</h3>
<p>计算质数方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 准备质数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Int&#125;</span> </span>num 质数范围
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-attr">getPrime</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-comment">// 从第一个质数 2 开始</span>
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>;
  <span class="hljs-keyword">const</span> arr = [];
  <span class="hljs-comment">/**
   * 检查是否是质数
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Int&#125;</span> <span class="hljs-variable">number</span></span>
   * <span class="hljs-doctag">@returns</span>
   */</span>
  <span class="hljs-keyword">const</span> isPrime = <span class="hljs-function">(<span class="hljs-params">number</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> ii = <span class="hljs-number">2</span>; ii < number / <span class="hljs-number">2</span>; ++ii) &#123;
      <span class="hljs-keyword">if</span> (number % ii === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;;
  <span class="hljs-comment">// 循环判断，质数数量够完成返回</span>
  <span class="hljs-keyword">for</span> (i; arr.length < total; ++i) &#123;
    <span class="hljs-keyword">if</span> (isPrime(i)) &#123;
      arr.push(i);
    &#125;
  &#125;
  <span class="hljs-comment">// 返回需要的质数</span>
  <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-comment">// 上述动图入参以及返回结果展示：</span>
<span class="hljs-comment">// getPrime(500) return==> </span>
<span class="hljs-comment">// 0: (8) [2, 3, 5, 7, 11, 13, 17, 19]</span>
<span class="hljs-comment">// 1: (8) [23, 29, 31, 37, 41, 43, 47, 53]</span>
<span class="hljs-comment">// 2: (8) [59, 61, 67, 71, 73, 79, 83, 89]</span>
<span class="hljs-comment">// 3: (8) [97, 101, 103, 107, 109, 113, 127, 131]</span>
<span class="hljs-comment">// 4: (8) [137, 139, 149, 151, 157, 163, 167, 173]</span>
<span class="hljs-comment">// 5: (8) [179, 181, 191, 193, 197, 199, 211, 223]</span>
<span class="hljs-comment">// 6: (8) [227, 229, 233, 239, 241, 251, 257, 263]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化处理，得到第一批邻接矩阵结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 初始化，格式需要对比数据，并进行初始化是否可选计算
 */</span>
<span class="hljs-attr">init</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.light = util.cloneTwo(<span class="hljs-built_in">this</span>.maps, <span class="hljs-literal">true</span>);
  <span class="hljs-keyword">var</span> light = <span class="hljs-built_in">this</span>.light;

  <span class="hljs-comment">// 默认每个规则都可以选中，即赋值为 1</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < light.length; i++) &#123;
    <span class="hljs-keyword">var</span> l = light[i];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < l.length; j++) &#123;
      <span class="hljs-built_in">this</span>._way[l[j]] = [i, j];
      l[j] = <span class="hljs-number">1</span>;
    &#125;
  &#125;
  <span class="hljs-comment">// 对应结果值，此处将数据处理的方法对应邻接矩阵的思维导图</span>
  <span class="hljs-comment">// 0: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 1: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 2: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 3: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 4: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 5: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>
  <span class="hljs-comment">// 6: (8) [1, 1, 1, 1, 1, 1, 1, 1]</span>

  <span class="hljs-comment">// 得到每个可操作的 SKU 质数的集合</span>
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.openway.length; i++) &#123;
    <span class="hljs-comment">// 计算结果单行示例：</span>
    <span class="hljs-comment">// this.openway[i].join('*') ==> eval(2*3*5*7*11*13*17*19)</span>
    <span class="hljs-built_in">this</span>.openway[i] = <span class="hljs-built_in">eval</span>(<span class="hljs-built_in">this</span>.openway[i].join(<span class="hljs-string">'*'</span>));
  &#125;
  <span class="hljs-comment">// return 初始化得到规格位置，规格默认可选处理，可选 SKU 的规格对应的质数合集</span>
  <span class="hljs-built_in">this</span>._check();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算是否可选方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 检查是否可以选择，更新邻接矩阵对应结果值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Boolean&#125;</span> </span>isAdd 是否新增状态
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-attr">_check</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">isAdd</span>) </span>&#123;
  <span class="hljs-keyword">var</span> light = <span class="hljs-built_in">this</span>.light;
  <span class="hljs-keyword">var</span> maps = <span class="hljs-built_in">this</span>.maps;
  
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < light.length; i++) &#123;
    <span class="hljs-keyword">var</span> li = light[i];
    <span class="hljs-keyword">var</span> selected = <span class="hljs-built_in">this</span>._getSelected(i);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < li.length; j++) &#123;
      <span class="hljs-keyword">if</span> (li[j] !== <span class="hljs-number">2</span>) &#123;
      <span class="hljs-comment">//如果是加一个条件，只在是 light 值为 1 的点进行选择</span>
        <span class="hljs-keyword">if</span> (isAdd) &#123;
          <span class="hljs-keyword">if</span> (li[j]) &#123;
            light[i][j] = <span class="hljs-built_in">this</span>._checkItem(maps[i][j], selected);
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          light[i][j] = <span class="hljs-built_in">this</span>._checkItem(maps[i][j], selected);
        &#125;
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.light;
&#125;，

<span class="hljs-comment">/**
 * 检查是否可选内容，更新邻接矩阵对应结果值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Int&#125;</span> </span>item 当前规格质数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> <span class="hljs-variable">selected</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-attr">_checkItem</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item, selected</span>) </span>&#123;
  <span class="hljs-comment">// 拿到可以选择的 SKU 内容集合</span>
  <span class="hljs-keyword">var</span> openway = <span class="hljs-built_in">this</span>.openway;
  <span class="hljs-keyword">var</span> val;
  <span class="hljs-comment">// 拿到已经选中规格集合*此规格集合值</span>
  val = item * selected;
  <span class="hljs-comment">// 可选 SKU 集合反除，查询是否可选</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < openway.length; i++) &#123;
    <span class="hljs-built_in">this</span>.count++;
    <span class="hljs-keyword">if</span> (openway[i] % val === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加规格方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** 选择可选规格后处理
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;array&#125;</span> </span>point [x, y]
 */</span>
<span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">point</span>) </span>&#123;
  point = point <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> ? point : <span class="hljs-built_in">this</span>._way[point];
  <span class="hljs-comment">// 得到选中规格对应的质数内容</span>
  <span class="hljs-keyword">var</span> val = <span class="hljs-built_in">this</span>.maps[point[<span class="hljs-number">0</span>]][point[<span class="hljs-number">1</span>]];

  <span class="hljs-comment">// 检查是否可选中</span>
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.light[point[<span class="hljs-number">0</span>]][point[<span class="hljs-number">1</span>]]) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
      <span class="hljs-string">'this point ['</span> + point + <span class="hljs-string">'] is no availabe, place choose an other'</span>
    );
  &#125;
  <span class="hljs-comment">// 判断是否选中内容已经存在已经选择内容中</span>
  <span class="hljs-keyword">if</span> (val <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.selected) <span class="hljs-keyword">return</span>;
  
  <span class="hljs-keyword">var</span> isAdd = <span class="hljs-built_in">this</span>._dealChange(point, val);
  <span class="hljs-built_in">this</span>.selected.push(val);
  <span class="hljs-comment">// 选择后邻接矩阵对应数据修改为 2，以做是否可选区分</span>
  <span class="hljs-built_in">this</span>.light[point[<span class="hljs-number">0</span>]][point[<span class="hljs-number">1</span>]] = <span class="hljs-number">2</span>;
  <span class="hljs-built_in">this</span>._check(!isAdd);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>移除已选规格方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 移除已选规格
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> </span>point 
 */</span>
<span class="hljs-attr">remove</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">point</span>) </span>&#123;
  point = point <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> ? point : <span class="hljs-built_in">this</span>._way[point];
  <span class="hljs-comment">// 容错处理</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">var</span> val = <span class="hljs-built_in">this</span>.maps[point[<span class="hljs-number">0</span>]][point[<span class="hljs-number">1</span>]];
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;

  <span class="hljs-keyword">if</span> (val) &#123;
    <span class="hljs-comment">// 在选中内容中，定位取出需要移除规格质数</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.selected.length; i++) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.selected[i] == val) &#123;
        <span class="hljs-keyword">var</span> line = <span class="hljs-built_in">this</span>._way[<span class="hljs-built_in">this</span>.selected[i]];
        <span class="hljs-comment">// 对应邻接矩阵内容更新为可选</span>
        <span class="hljs-built_in">this</span>.light[line[<span class="hljs-number">0</span>]][line[<span class="hljs-number">1</span>]] = <span class="hljs-number">1</span>;
        <span class="hljs-comment">// 从已选内容中移除</span>
        <span class="hljs-built_in">this</span>.selected.splice(i, <span class="hljs-number">1</span>);
      &#125;
    &#125;
  <span class="hljs-comment">// 进行重新计算</span>
  <span class="hljs-built_in">this</span>._check();
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">整体代码</h3>
<p>开源代码将在 9 月中旬提供。如需，请关注微信公众号：政采云前端团队。回复 sku，即可获取开源地址。</p>
<h2 data-id="heading-15">总结</h2>
<p>看来老师没有骗我们，在学习中学到的<strong>经典排列组合</strong>，<strong>邻接矩阵</strong>，<strong>集合</strong>还是很有用处的。其中经典排列组合<strong>笛卡尔积</strong>思想不用死记硬背，通过理解就可以完成递归树状图的大量情况。根据邻接矩阵，可以简化空间复杂程度，通过集合思想，实现选择数据判断。</p>
<p>相信阅读完本篇文章的你，对于电商规格处理的两个算法已经有了大体了解。</p>
<h3 data-id="heading-16">参考文献</h3>
<p>1.上述集合计算思路借鉴文献， 详情见<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgit.shepherdwind.com%2Fsku-search-algorithm.html" target="_blank" rel="nofollow noopener noreferrer" title="http://git.shepherdwind.com/sku-search-algorithm.html" ref="nofollow noopener noreferrer">链接</a>。</p>
<p>2.另一种正则匹配实现思路文献借鉴，详情见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fshepherdwind%2F2141756" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/shepherdwind/2141756" ref="nofollow noopener noreferrer">链接</a>。</p>
<p>3.邻接矩阵思路借鉴文献，详情见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fshepherdwind%2F2141756" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/shepherdwind/2141756" ref="nofollow noopener noreferrer">链接</a>。</p>
<h2 data-id="heading-17">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6997536906967777316" target="_blank" title="https://juejin.cn/post/6997536906967777316">你需要知道的项目管理知识</a></p>
<p><a href="https://juejin.cn/post/6984547134062198791" target="_blank" title="https://juejin.cn/post/6984547134062198791">最熟悉的陌生人rc-form</a></p>
<p><a href="https://juejin.cn/post/6987140782595506189" target="_blank" title="https://juejin.cn/post/6987140782595506189">如何搭建适合自己团队的构建部署平台</a></p>
<p><a href="https://juejin.cn/post/6961201207964598286" target="_blank" title="https://juejin.cn/post/6961201207964598286">聊聊Deno的那些事</a></p>
<h2 data-id="heading-18">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Fopenweekly%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/openweekly/" ref="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-19">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 50 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            