
---
title: '详解矩阵算法在电商sku组件中的应用一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 18:04:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://github.com/bigo-frontend/blog/" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h3 data-id="heading-0">前言</h3>
<p>在电商里，什么是 sku？</p>
<p>简单的来说，比如一件裙子，颜色有红色、白色，码数有 XL、XXL，我们选择红色、XL，那这个规格的组合就是一个 sku。</p>
<p>而 spu 则是指这件裙子，要区分开来。</p>
<p>以前刚开始接触到这种 sku 选择器，还以为只是简简单单的几个 tab 组合后传给后端，但是等到实际开发才知道这种 sku 选择器，是后端告诉你有什么规格，比如颜色有几种，码数有几种，然后再告诉你有几种组合方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.product.skuAttrSortedList = [
  &#123;
    <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"颜色"</span>,
    <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"1"</span>,
    <span class="hljs-string">"attrValues"</span>: [
      <span class="hljs-string">"红"</span>,
      <span class="hljs-string">"白"</span>
    ]
  &#125;,
  &#123;
    <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"码数"</span>,
    <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-string">"attrValues"</span>: [
      <span class="hljs-string">"XL"</span>,
      <span class="hljs-string">"XXL"</span>
    ]
  &#125;
];
<span class="hljs-built_in">this</span>.product.skuList = [
  &#123;
    <span class="hljs-string">"showPrice"</span>: <span class="hljs-string">"6.00"</span>,
    <span class="hljs-string">"favType"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuId"</span>: <span class="hljs-string">"1234"</span>,
    <span class="hljs-string">"originalSalePrice"</span>: <span class="hljs-string">"12.01"</span>,
    <span class="hljs-string">"salePrice"</span>: <span class="hljs-string">"11.01"</span>,
    <span class="hljs-string">"discount"</span>: <span class="hljs-string">"-40%"</span>,
    <span class="hljs-string">"saleCurrency"</span>: <span class="hljs-string">"USD"</span>,
    <span class="hljs-string">"skuMinVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuIncreaseVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"maxBuyVolume"</span>: <span class="hljs-number">99</span>,
    <span class="hljs-string">"skuStatus"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuImg"</span>: <span class="hljs-string">"https://s4.forcloudcdn.com/item/images/dmc/7cdb5ab0-88b5-45a4-a5af-d683ccbd9336-750x1000.jpeg_750x0c.jpeg"</span>,
    <span class="hljs-string">"skuAttrList"</span>: [
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"12"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"颜色"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"红"</span>
      &#125;,
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"13"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"码数"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"XL"</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-string">"showPrice"</span>: <span class="hljs-string">"6.00"</span>,
    <span class="hljs-string">"favType"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuId"</span>: <span class="hljs-string">"2345"</span>,
    <span class="hljs-string">"originalSalePrice"</span>: <span class="hljs-string">"12.01"</span>,
    <span class="hljs-string">"salePrice"</span>: <span class="hljs-string">"11.01"</span>,
    <span class="hljs-string">"saleCurrency"</span>: <span class="hljs-string">"USD"</span>,
    <span class="hljs-string">"discount"</span>: <span class="hljs-string">"-40%"</span>,
    <span class="hljs-string">"skuMinVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuIncreaseVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"maxBuyVolume"</span>: <span class="hljs-number">99</span>,
    <span class="hljs-string">"skuStatus"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuImg"</span>: <span class="hljs-string">"https://s4.forcloudcdn.com/item/images/dmc/4a085065-0f92-4406-a55e-ae4150b91def-779x974.jpeg_750x0c.jpeg"</span>,
    <span class="hljs-string">"skuAttrList"</span>: [
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"12"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"颜色"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"红"</span>
      &#125;,
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"13"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"码数"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"XXL"</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-string">"skuId"</span>: <span class="hljs-string">"3456"</span>,
    <span class="hljs-string">"originalSalePrice"</span>: <span class="hljs-string">"12.01"</span>,
    <span class="hljs-string">"salePrice"</span>: <span class="hljs-string">"11.01"</span>,
    <span class="hljs-string">"saleCurrency"</span>: <span class="hljs-string">"USD"</span>,
    <span class="hljs-string">"discount"</span>: <span class="hljs-string">"-40%"</span>,
    <span class="hljs-string">"skuMinVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuIncreaseVolume"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"maxBuyVolume"</span>: <span class="hljs-number">99</span>,
    <span class="hljs-string">"skuStatus"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"skuImg"</span>: <span class="hljs-string">"https://s4.forcloudcdn.com/item/images/dmc/4a085065-0f92-4406-a55e-ae4150b91def-779x974.jpeg_750x0c.jpeg"</span>,
    <span class="hljs-string">"skuAttrList"</span>: [
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"12"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"颜色"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"白"</span>
      &#125;,
      &#123;
        <span class="hljs-string">"attrNameId"</span>: <span class="hljs-string">"13"</span>,
        <span class="hljs-string">"attrName"</span>: <span class="hljs-string">"码数"</span>,
        <span class="hljs-string">"attrValue"</span>: <span class="hljs-string">"XXL"</span>
      &#125;
    ]
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我唯一想到的就只有循环破解，那时间复杂度会随着规格越来越多而变得越来越大，虽然可行，但 js 执行在一些低端机就会有卡顿。</p>
<p>曾经在微信公众号发现一篇文章，讲的是如何用矩阵解决 sku 算法问题，当时粗略看了下，哇塞，好巧妙的办法！如今 stalar 电商项目刚好可以运用一下，说干就干！</p>
<p>产品需求是想，我选择一个规格后，其他可选的规格可点，不可选的规格置灰不可点击，可选不可选就是根据后端返回的组合列表得出的，就像
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddb637736cbb4812b60c3d246749abeb~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d73ec8a2eb7406589acf2563513f780~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
上面组合列表 skuList 有白色的 sku 只有一个（白色、XXL），所以码数中只有 XXL 可选。那为什么还有个红色可选？当然啦，用户想换种颜色看看你总得允许吧 ~</p>
<p>那我们怎么用矩阵来实现这种筛选呢？</p>
<p>我们画个图，利用矩阵列的求交集即可以得出剩余可选规格，那我们先拿到所有可选规格，定义两个计算属性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">vertex</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.product.skuAttrSortedList || []).reduce(<span class="hljs-function">(<span class="hljs-params">total, current</span>) =></span> [...total, ...(current.attrValues || [])], []);
&#125;,
<span class="hljs-function"><span class="hljs-title">len</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.vertex.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就是利用这个 vertex 建立一个全为 0 的邻接矩阵，这个可以用一个一维数组表示。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.adjoinArray = <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.len * <span class="hljs-built_in">this</span>.len).fill(<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以就有了下面这样一个矩阵：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e2739c53bb4e8d87ab22c4be587b9c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实把矩阵的行与行首尾相连就是我们的一维数组了，也就是说 this.adjoinArray[4] 指的是 矩阵 B3 位置的值，那我们反过来，B3 位置的值对应的是数组哪个索引呢？我们可以先想想怎么算到这个索引，也就是怎么把矩阵每个点的位置映射成一维数组的索引）</p>
<p>接着我们得定义一个数组 specsS，存对应属性已选择的规格</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">specsS: [];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且初始化它</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.specsS = <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.product.skuAttrSortedList.length).fill(<span class="hljs-string">''</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要把可以组合的点填充为 1，比如我们以红色为点，根据 skuList 这个组合列表，得到可到达的点有 XL 和 XXL，当然还有同级的白色(后面需要一个方法专门填充同级点)。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54719580ec4f4fcc96507249d1620cf6~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
利用邻接矩阵的对称性（其实就是可以反过来选择）可变成
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcdb118bbc7d4695a02a18593892d7f8~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们需要把 skuList 这个组合列表整个转成 矩阵填充 1 的展示，这个怎么用代码实现呢？首先定义一个填写 1 的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">setAdjoinVertexs</span>(<span class="hljs-params">side, sides</span>)</span> &#123;
      <span class="hljs-keyword">let</span> pIndex = <span class="hljs-string">''</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.vertex.length; i += <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">if</span> (side === <span class="hljs-built_in">this</span>.vertex[i]) &#123;
          pIndex = i;
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
      sides.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> index = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.vertex.length; i += <span class="hljs-number">1</span>) &#123;
          <span class="hljs-keyword">if</span> (item === <span class="hljs-built_in">this</span>.vertex[i]) &#123;
            index = i;
            <span class="hljs-keyword">break</span>;
          &#125;
        &#125;
        <span class="hljs-built_in">this</span>.adjoinArray[pIndex * <span class="hljs-built_in">this</span>.len + index] = <span class="hljs-number">1</span>;
      &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来看下两个循环干了些啥，如果我们传入 side = '红色'，sides = [‘红色’,'XL']
第一个循环其实是在矩阵中找到红色这一行，pIndex 得到的是 0</p>
<p>第二个循环则是在矩阵中找到可到达点所在列，比如找到 XL 所在列索引 index 是 2</p>
<p>找到了起始点的行，可到达点的列，那我们就可以把他们的交点填充为 1</p>
<p>还记得前面我让大家想如何将矩阵的点位置映射成数组的索引么？其实就是这里的 pIndex * this.len + index</p>
<p>知道原理了，赶紧上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">initSpec</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.specCombinationList.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> <span class="hljs-built_in">this</span>.fillInSpec(item.skuAttrValueList));
    &#125;,
<span class="hljs-function"><span class="hljs-title">fillInSpec</span>(<span class="hljs-params">params</span>)</span> &#123;
      params.forEach(<span class="hljs-function">(<span class="hljs-params">param</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.setAdjoinVertexs(param, params);
      &#125;);
    &#125;,
<span class="hljs-function"><span class="hljs-title">setAdjoinVertexs</span>(<span class="hljs-params">side, sides</span>)</span> &#123;
      <span class="hljs-keyword">let</span> pIndex = <span class="hljs-string">''</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.vertex.length; i += <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">if</span> (side === <span class="hljs-built_in">this</span>.vertex[i]) &#123;
          pIndex = i;
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
      sides.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> index = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.vertex.length; i += <span class="hljs-number">1</span>) &#123;
          <span class="hljs-keyword">if</span> (item === <span class="hljs-built_in">this</span>.vertex[i]) &#123;
            index = i;
            <span class="hljs-keyword">break</span>;
          &#125;
        &#125;
        <span class="hljs-built_in">this</span>.adjoinArray[pIndex * <span class="hljs-built_in">this</span>.len + index] = <span class="hljs-number">1</span>;
      &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(注：initSpec 方法里的 specCombinationList 是处理过的 skuList 组合列表)</p>
<p>但实际上我们选了红色，白色依旧是可选项，所以我们需要填充同级点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">initSameLevel</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.product.skuAttrSortedList.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> params = [];
        <span class="hljs-comment">// 获取同级别顶点</span>
        item.attrValues.forEach(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.optionSpecs.includes(val)) params.push(val);
        &#125;);
        <span class="hljs-comment">// 同级点位创建</span>
        <span class="hljs-built_in">this</span>.fillInSpec(params);
      &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 optionSpecs 数组是什么呢？
其实就是可到达点数组，也就是可选规格，是我们本次算法的目的</p>
<p>所以我们需要定义一个计算属性，optionSpecs，它是根据用户选择动态变化的。我们想，那它的初始值是什么呢？</p>
<p>当我们执行完 initSpec 后，就能知道初始的可选规格有哪些
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0216ad00e9ff441988d2c5c616e5bd3e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
根据该矩阵我们就能找到最一开始可选的规格有哪些。</p>
<p>怎么找？我们可以把所有列求并集，上图矩阵所有列求并集就能得到[1, 1, 1, 1]
也就是，只要那一行某一列是 1，并集的结果就是 1，并集是 1 代表那一行的规格最一开始是可选的，这样看我们最一开始 4 个规格都是可点击的。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c89f79a50fde418bbd0d8b8de97c7930~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae357d3044c45c28ab3b07ef266c3c4~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如何求列的并集呢
我们把每一列当成一个数组，第 x 行并集就是这 7 个数组的索引 x-1 对应值相加，相加结果大于等于 1 即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取某一规格所在那一列</span>
<span class="hljs-function"><span class="hljs-title">getVertexCol</span>(<span class="hljs-params">param</span>)</span> &#123;
      <span class="hljs-keyword">let</span> idx = <span class="hljs-string">''</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.vertex.length; i += <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">if</span> (param === <span class="hljs-built_in">this</span>.vertex[i]) &#123;
          idx = i;
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
      <span class="hljs-keyword">const</span> col = [];
      <span class="hljs-built_in">this</span>.vertex.forEach(<span class="hljs-function">(<span class="hljs-params">item, pIndex</span>) =></span> &#123;
        col.push(<span class="hljs-built_in">this</span>.adjoinArray[idx + <span class="hljs-built_in">this</span>.len * pIndex]);
      &#125;);
      <span class="hljs-keyword">return</span> col;
    &#125;,
<span class="hljs-comment">// 得到每一行格子的和，然后放进一个数组</span>
    <span class="hljs-function"><span class="hljs-title">getColSum</span>(<span class="hljs-params">params</span>)</span> &#123;
      <span class="hljs-keyword">const</span> paramsVertex = params.map(<span class="hljs-function">(<span class="hljs-params">param</span>) =></span> <span class="hljs-built_in">this</span>.getVertexCol(param));
      <span class="hljs-keyword">const</span> paramsVertexSum = [];
      <span class="hljs-built_in">this</span>.vertex.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> rowTotal = paramsVertex
          .map(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value[index])
          .reduce(<span class="hljs-function">(<span class="hljs-params">total, current</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> newTotal = total;
            newTotal += current || <span class="hljs-number">0</span>;
            <span class="hljs-keyword">return</span> newTotal;
          &#125;, <span class="hljs-number">0</span>);
        paramsVertexSum.push(rowTotal);
      &#125;);
      <span class="hljs-keyword">return</span> paramsVertexSum;
    &#125;,
<span class="hljs-comment">// 把paramsVertexSum数组中值为1的索引找出来，然后到规格列表数组中匹配得到并集</span>
    <span class="hljs-function"><span class="hljs-title">getUnion</span>(<span class="hljs-params">params</span>)</span> &#123;
      <span class="hljs-keyword">const</span> paramsColSum = <span class="hljs-built_in">this</span>.getColSum(params);
      <span class="hljs-keyword">const</span> union = [];
      paramsColSum.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (item && <span class="hljs-built_in">this</span>.vertex[index]) union.push(<span class="hljs-built_in">this</span>.vertex[index]);
      &#125;);
      <span class="hljs-keyword">return</span> union;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那初始化时的可选规格列表我们顺利拿到了，也就是上面我们提到的 optionSpecs = 四个规格的数组，我们就可以填充同级点了，这是因为要排除掉一开始就不可选的属性值。最终初始化的矩阵如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21d0470c043a409094df765793782ddd~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当用户点击某一个规格时，我们怎样得到剩余可选规格呢？
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42f4fa3b0a3a4a66a1d23552714d3a77~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
当我们选中红色这一列就可以知道，这时为 1 的有红色、白色、XL 和 XXL，那剩余可选规格就是红色、白色、XL 和 XXL。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee187196bf204350952aea0dc9a2e700~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为这个例子只有 color 和 size 两个规格，所以只要我们选中 color 一列，就可以知道 size 可选是哪些
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3110eb7b4e8740acae7935c832fccc5a~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
如果再多一个规格，比如是套餐
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81a3fd5d77704c05b8dc9e18f8b93f94~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
所以不难看出，我们选泽红色、XL 后，剩余可选可以通过求交集得出。
聚焦每一行，当这一行每个格子都为 1，这一行的交集的结果才是 1。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8103161b5114b3ebad3de88bad0b09e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
所以红色列和 XL 列的交集结果是[1, 0, 1, 1, 1, 1]，即可选的有红色、XL、XXL、套餐 1、套餐 2。</p>
<h3 data-id="heading-1"><a href="https://github.com/bigo-frontend/blog/issues/31" target="_blank" rel="nofollow noopener noreferrer">三个规格的选择变化其实不能这么简单的求交集，我将在第二篇里为大家说明，但原理是一样的，当前篇所讲的方法只适用于两个规格！！第二篇链接：</a></h3>
<p>到这里大家应该知道了，这个 sku 选择器采用矩阵算法的原理了，就是用户每次选择一个属性值后，都能动态得到一个剩余可选属性的数组
代码上如何求交集</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">getIntersection</span>(<span class="hljs-params">params</span>)</span> &#123;
      <span class="hljs-keyword">const</span> paramsColSum = <span class="hljs-built_in">this</span>.getColSum(params);
      <span class="hljs-keyword">const</span> intersection = [];
      paramsColSum.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (item >= params.length && <span class="hljs-built_in">this</span>.vertex[index]) intersection.push(<span class="hljs-built_in">this</span>.vertex[index]);
      &#125;);
      <span class="hljs-keyword">return</span> intersection;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也是要跟上面求并集那样，拿到每一行所有格子值的和，如果和大于等于已选规格列数（item >= params.length 其实就是这一行每个格子是否都为 1），交集则为 1。交集为 1 的行对应的规格就 push 到剩余可选规格数组。</p>
<p>这样我们就可以完善之前说的计算属性 optionSpecs 可选规格数组的获取方法了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed: &#123;
     <span class="hljs-function"><span class="hljs-title">optionSpecs</span>(<span class="hljs-params"></span>)</span> &#123;  
 <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getSpecOptions(<span class="hljs-built_in">this</span>.specsS);  
     &#125;
&#125;,
<span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">getSpecOptions</span>(<span class="hljs-params">params</span>)</span> &#123;
      <span class="hljs-keyword">let</span> specOptionCanChoose = [];
      <span class="hljs-keyword">if</span> (params.some(<span class="hljs-built_in">Boolean</span>)) &#123;
specOptionCanChoose = <span class="hljs-built_in">this</span>.getIntersection(params.filter(<span class="hljs-built_in">Boolean</span>));
      &#125; <span class="hljs-keyword">else</span> &#123;
        specOptionCanChoose = <span class="hljs-built_in">this</span>.getUnion(<span class="hljs-built_in">this</span>.vertex);
      &#125;
      <span class="hljs-keyword">return</span> specOptionCanChoose;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们需要两个方法来判断该规格是否是可选规格以及判断该规格是否已选</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">isActive</span>(<span class="hljs-params">val, idx</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.specsS[idx] === val;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">isOption</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.optionSpecs.includes(val);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就能 disable 掉不可选的规格，以及高亮已选规格。</p>
<p>以上主要参考的是掘金大神写的关于 sku 选择组件如何利用图和矩阵算法实现的文章
<a href="https://juejin.cn/post/url">juejin.cn/post/684490…</a>
我只是捋清他的思路，并转换成了 vue 的组件在电商项目中实际运用，大家可以思考下 sku 组件可否用链表的方式来实现呢哈哈？</p>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div>  
</div>
            