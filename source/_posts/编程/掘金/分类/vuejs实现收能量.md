
---
title: 'vue.js实现收能量'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81fff39136c64302bde09dd4250fe647~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:47:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81fff39136c64302bde09dd4250fe647~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>其他活动实现:</p>
<blockquote>
<p>抽奖转盘: <a href="https://juejin.cn/post/6974993300491075598" target="_blank">vue.js实现抽奖转盘</a><br>红包雨: <a href="https://juejin.cn/post/6976134094048624653" target="_blank">vue.js实现红包雨</a></p>
</blockquote>
<h4 data-id="heading-0">1.实现的放大的同时上下移动 (先将代码部分抽出现实现)</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81fff39136c64302bde09dd4250fe647~tplv-k3u1fbpfcp-watermark.image" alt="能量4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-comment"><!-- <div class="father">
    <div class="test"></div>
    <div class="test"></div>
    <div class="test"></div>
    <div class="test"></div>
  </div> --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
     <span class="hljs-keyword">@keyframes</span> father&#123;
      <span class="hljs-number">0%</span>   &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
      &#125;
      <span class="hljs-number">50%</span>  &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, -<span class="hljs-number">15px</span>)
      &#125;
      <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0px</span>)
      &#125;
    &#125;
    <span class="hljs-selector-class">.father</span>&#123;
      <span class="hljs-attribute">animation</span>: father <span class="hljs-number">1.5s</span> ease-in-out <span class="hljs-number">1s</span> forwards infinite
    &#125;
    <span class="hljs-selector-class">.test</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-attribute">background-color</span>: burlywood;
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">animation</span>: star-stone <span class="hljs-number">1s</span> ease-in-out <span class="hljs-number">0s</span> forwards alternate;
    &#125;
    <span class="hljs-keyword">@keyframes</span> star-stone&#123;
      <span class="hljs-selector-tag">from</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-selector-tag">to</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
      &#125;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为泡泡的出现是随机出现的,那么必须保证上下移动的步调是一致的,所以必须将上下移动的css动画放在子元素的父级</p>
<h4 data-id="heading-1">2.实现能量的排版与自动出现</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c875563ff8224304817c7fa31438f109~tplv-k3u1fbpfcp-watermark.image" alt="能量5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">2.1先定义是否显示的option参数,因为import进来的数据,存在引用,所以这里使用工厂函数</h5>
<p>/indexOption.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">imgArrFun</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">5</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">6</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">7</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">8</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">9</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">10</span>,
      <span class="hljs-attr">isShow</span>: <span class="hljs-literal">false</span>,
    &#125;,
  ]
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">idArrFun</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2.2实现</h5>
<p>index.vue</p>
<p>html:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 能量分布 --></span>
 <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"['father', centerVisible ? 'star-energy-center' : 
 `position$&#123;index + 1&#125;`]"</span>  <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in imgList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"item.isShow"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[item.isShow ? 'star-stone': '' ]"</span> 
     <span class="hljs-attr">src</span>=<span class="hljs-string">"@/assets/image/starEnergy/starStone.png"</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
 
 <span class="hljs-comment"><!-- 可领取 --></span>
 <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"!pushVisible && bubbleShow"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star-energy-button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"combine"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css:</p>
<pre><code class="hljs language-css copyable" lang="css">   <span class="hljs-selector-class">.star-stone</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">animation</span>: star-stone <span class="hljs-number">1s</span> ease-in-out <span class="hljs-number">0s</span> forwards alternate;
    &#125;
    <span class="hljs-keyword">@keyframes</span> star-stone&#123;
      <span class="hljs-selector-tag">from</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-selector-tag">to</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
      &#125;
    &#125;
    <span class="hljs-keyword">@keyframes</span> father&#123;
      <span class="hljs-number">0%</span>   &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
      &#125;
      <span class="hljs-number">50%</span>  &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, -<span class="hljs-number">15px</span>)
      &#125;
      <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0px</span>)
      &#125;
    &#125;
    <span class="hljs-selector-class">.position1</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">48px</span>;
    &#125;
    <span class="hljs-selector-class">.position2</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">178px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">180px</span>;
    &#125;
    <span class="hljs-selector-class">.position3</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">178px</span>;
    &#125;
    <span class="hljs-selector-class">.position4</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">178px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">440px</span>;
    &#125;
    <span class="hljs-selector-class">.position5</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">244px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">570px</span>;
    &#125;
    <span class="hljs-selector-class">.position6</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">244px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">50px</span>;
    &#125;
    <span class="hljs-selector-class">.position7</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">308px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">180px</span>;
    &#125;
    <span class="hljs-selector-class">.position8</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">308px</span>;
    &#125;
    <span class="hljs-selector-class">.position9</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">308px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">440px</span>;
    &#125;
    <span class="hljs-selector-class">.position10</span> &#123;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">438px</span>;
    &#125;
    
    <span class="hljs-selector-class">.father</span>&#123;
      <span class="hljs-keyword">@include</span> position(absolute, <span class="hljs-number">130px</span>, <span class="hljs-number">130px</span>);
      <span class="hljs-attribute">left</span>: <span class="hljs-number">310px</span>;
      <span class="hljs-attribute">right</span>: <span class="hljs-number">310px</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">243px</span>;
      <span class="hljs-attribute">animation</span>: father <span class="hljs-number">1.5s</span> ease-in-out <span class="hljs-number">1s</span> forwards infinite
    &#125;
   <span class="hljs-selector-class">.star-energy-center</span>&#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">transition</span>: all <span class="hljs-number">1s</span> linear;
      <span class="hljs-attribute">animation</span>: star-energy-center <span class="hljs-number">2s</span> linear forwards alternate;
    &#125;
    <span class="hljs-keyword">@keyframes</span> star-energy-center &#123;
      <span class="hljs-number">0%</span>   &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
      &#125;
      <span class="hljs-number">50%</span>   &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
      &#125;
      <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">200px</span>);
        <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">1s</span>;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js部分</p>
<pre><code class="hljs language-js copyable" lang="js">  computed: &#123;
    <span class="hljs-comment">// 没有泡泡就让按钮显示不可以按</span>
    <span class="hljs-string">'bubbleShow'</span> () &#123;
      <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">this</span>.imgList.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.isShow) || []
      <span class="hljs-keyword">return</span> list.length > <span class="hljs-number">0</span>
    &#125;,
  &#125;,
  <span class="hljs-keyword">async</span> created () &#123;
    <span class="hljs-built_in">this</span>.imgList = imgArrFun()
    <span class="hljs-comment">// 首次加载先让能量随机出现</span>
    <span class="hljs-built_in">this</span>.getStarEnergyData()
  &#125;,
  
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 获取星能量倒计时和可领取奖励数</span>
    <span class="hljs-keyword">async</span> getStarEnergyData () &#123;
      <span class="hljs-built_in">this</span>.$loading.show()
      <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> xxxx接口(<span class="hljs-built_in">this</span>.token)
      <span class="hljs-built_in">this</span>.isCombineVisible = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.starEnergyData = data.info
      <span class="hljs-comment">// 拿到后台返回的数据</span>
      <span class="hljs-keyword">const</span> energyBouns = <span class="hljs-number">10</span> * +<span class="hljs-built_in">this</span>.ruleData.wealthBonus
      <span class="hljs-built_in">this</span>.showEnergyNum = <span class="hljs-built_in">this</span>.starEnergyData.accumulateWealthNum >= energyBouns ?
      <span class="hljs-number">10</span> : (+<span class="hljs-built_in">this</span>.starEnergyData.accumulateWealthNum % energyBouns) / 
      <span class="hljs-built_in">this</span>.ruleData.wealthBonus
      <span class="hljs-built_in">this</span>.showStarEnergy(<span class="hljs-built_in">this</span>.showEnergyNum)
      <span class="hljs-built_in">this</span>.surplusTime = +<span class="hljs-built_in">this</span>.starEnergyData.surplusTime
    &#125;,
    <span class="hljs-comment">// 点击合成</span>
    <span class="hljs-keyword">async</span> combine () &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isCombineVisible) &#123; <span class="hljs-comment">// 设置isCombineVisible防止重复点击</span>
        <span class="hljs-built_in">this</span>.pushVisible = <span class="hljs-literal">true</span> <span class="hljs-comment">// 因为按下去是其他样式,所以设定一个状态</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-keyword">async</span> () => &#123;
          <span class="hljs-built_in">this</span>.pushVisible = <span class="hljs-literal">false</span>
          <span class="hljs-keyword">await</span> getStarEnergyApi(<span class="hljs-built_in">this</span>.token) <span class="hljs-comment">// 合成的时候需要进行一次上报</span>
          <span class="hljs-built_in">this</span>.isCombineVisible = <span class="hljs-literal">false</span>
          <span class="hljs-built_in">this</span>.centerVisible = <span class="hljs-literal">true</span> <span class="hljs-comment">// 主要是做收能量的动效</span>
          <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'father'</span>)[<span class="hljs-number">0</span>].addEventListener(
          <span class="hljs-string">'animationend'</span>, <span class="hljs-built_in">this</span>.animationendFunc)
        &#125;, <span class="hljs-number">100</span>)
      &#125;
    &#125;,
    <span class="hljs-comment">// 消失之后,将数据初始化</span>
    animationendFunc () &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.centerVisible) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-built_in">this</span>.imgList = imgArrFun()
      <span class="hljs-built_in">this</span>.showBouns = <span class="hljs-literal">true</span>
      <span class="hljs-comment">// 2s之后将显示弹框隐藏,居中class隐藏,重新调接口</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.showBouns = <span class="hljs-literal">false</span>
        <span class="hljs-built_in">this</span>.centerVisible = <span class="hljs-literal">false</span>
        <span class="hljs-built_in">this</span>.getStarEnergyData()
      &#125;, <span class="hljs-number">2000</span>)
    &#125;,
    <span class="hljs-comment">// 显示能量球以及开始倒计时</span>
    <span class="hljs-keyword">async</span> showStarEnergy (num) &#123;
      <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer)
      <span class="hljs-built_in">this</span>.countDown(<span class="hljs-built_in">this</span>.surplusTime)
      <span class="hljs-built_in">this</span>.ids = idArrFun()
      <span class="hljs-built_in">this</span>.imgList = imgArrFun()
      <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">this</span>.getRandom(num, <span class="hljs-built_in">this</span>.ids)
      <span class="hljs-built_in">this</span>.imgList.forEach(<span class="hljs-function">(<span class="hljs-params">img</span>) =></span> &#123;
        res.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
          <span class="hljs-keyword">if</span> (img.id === item) &#123;
            img.isShow = <span class="hljs-literal">true</span>
          &#125;
        &#125;)
      &#125;)
    &#125;,
     <span class="hljs-comment">// 获取随机数</span>
    getRandom (num, ids) &#123;
      <span class="hljs-comment">// 输出数组</span>
      <span class="hljs-keyword">const</span> out = []
      <span class="hljs-comment">// 输出个数</span>
      <span class="hljs-keyword">while</span> (out.length < num) &#123;
        <span class="hljs-keyword">const</span> temp = (<span class="hljs-built_in">Math</span>.random() * ids.length) >> <span class="hljs-number">0</span>
        out.push(ids.splice(temp, <span class="hljs-number">1</span>)[<span class="hljs-number">0</span>])
      &#125;
      <span class="hljs-keyword">return</span> out
    &#125;,
    <span class="hljs-comment">// 倒计时</span>
    countDown (seconds = <span class="hljs-number">60</span>) &#123;
      <span class="hljs-comment">// 定时器</span>
      <span class="hljs-built_in">this</span>.timeObj = dateTransform(seconds)
      <span class="hljs-built_in">this</span>.timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 把转换后的结果显示出来</span>
        <span class="hljs-built_in">this</span>.timeObj = dateTransform(seconds)
        <span class="hljs-keyword">if</span> (seconds < <span class="hljs-number">0</span>) &#123;
          <span class="hljs-built_in">this</span>.zeroHandle()
        &#125;
        seconds--
      &#125;, <span class="hljs-number">1000</span>)
    &#125;,
    <span class="hljs-comment">// 生成泡泡逻辑</span>
    zeroHandle () &#123;
      <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer)
      <span class="hljs-built_in">this</span>.activeStarNum = <span class="hljs-built_in">this</span>.activeStarNum + <span class="hljs-built_in">this</span>.ruleData.wealthBonus
      <span class="hljs-built_in">this</span>.countDown(<span class="hljs-built_in">this</span>.ruleData.onlineTime)
      <span class="hljs-comment">// 如果已经有了10个泡泡,就不往下执行了</span>
      <span class="hljs-keyword">const</span> imgHiddenList = <span class="hljs-built_in">this</span>.imgList.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !item.isShow) || []
      <span class="hljs-keyword">if</span> (imgHiddenList.length !== <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.showBubble()
      &#125;
    &#125;,
     <span class="hljs-comment">// 显示泡泡</span>
    showBubble () &#123;
      <span class="hljs-comment">// 如果泡泡数存在,下次就随机出现得范围就是isShow不为true得</span>
      <span class="hljs-keyword">const</span> resArr = <span class="hljs-built_in">this</span>.imgList.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !item.isShow).map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.id)
      <span class="hljs-keyword">if</span> (resArr.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">this</span>.ids = [...resArr]
      <span class="hljs-comment">// 将出现的设置为true</span>
      <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">1</span>, <span class="hljs-built_in">this</span>.ids)
      <span class="hljs-built_in">this</span>.imgList.forEach(<span class="hljs-function">(<span class="hljs-params">img</span>) =></span> &#123;
        res.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
          <span class="hljs-keyword">if</span> (img.id === item) &#123;
            img.isShow = <span class="hljs-literal">true</span>
          &#125;
        &#125;)
      &#125;)
    &#125;,
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意:
从动画上来说,最重要的是在没有点击居中的时候,应该是按照UI图的样式进行10个球固定位置的分布,等点击收能量的时候,进行一个整体的动画,给一个过渡的效果,让每个球,做同样的操作,而不是针对单个球不同的位置做相应的操作</p>
<p>从逻辑上来说,随机出现小球,一定要注意去排除已经出现过的小球.</p></div>  
</div>
            