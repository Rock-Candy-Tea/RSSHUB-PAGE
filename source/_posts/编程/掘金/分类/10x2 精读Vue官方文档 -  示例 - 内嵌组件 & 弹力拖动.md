
---
title: '10x2 精读Vue官方文档 -  示例 - 内嵌组件 & 弹力拖动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1359'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:04:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=1359'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<hr>
<h2 data-id="heading-1">内嵌组件</h2>
<p>使用 Vue 兼容第三方生态的范例。例如基于 JavaScript 或 Jquery 的插件、widget、库等。</p>
<p><strong>一些诀窍：</strong></p>
<ul>
<li>选用的插件、widget 最好自带样式作用域隔离，比如基于 <code>BEM</code>。</li>
<li>需要依赖 DOM 元素的，应该将插件的执行时期延缓到 <code>mounted</code> 生命周期内，此时可以通过 <code>this.$el</code> 获取组件的根元素。</li>
<li>可以将插件的事件系统结合到 Vue 的程序化事件监听器中共同使用。</li>
<li>组件销毁时 <code>destored</code> 要主动去消耗插件的实例，防止内存泄漏。</li>
</ul>
<p><strong>代码示例：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">mounted: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> vm = <span class="hljs-built_in">this</span>;
    $(<span class="hljs-built_in">this</span>.$el)
        <span class="hljs-comment">// init select2</span>
        .select2(&#123; <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.options &#125;)
        .val(<span class="hljs-built_in">this</span>.value)
        .trigger(<span class="hljs-string">"change"</span>)
        <span class="hljs-comment">// emit event on change.</span>
        .on(<span class="hljs-string">"change"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-comment">//触发 v-model，将插件的事件转换为 Vue 的事件。</span>
            vm.$emit(<span class="hljs-string">"input"</span>, <span class="hljs-built_in">this</span>.value);
        &#125;);
&#125;,
<span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-comment">// update value</span>
        $(<span class="hljs-built_in">this</span>.$el).val(value).trigger(<span class="hljs-string">"change"</span>);
    &#125;,
    <span class="hljs-attr">options</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
        <span class="hljs-comment">// update options</span>
        $(<span class="hljs-built_in">this</span>.$el).empty().select2(&#123; <span class="hljs-attr">data</span>: options &#125;);
    &#125;
&#125;,
<span class="hljs-attr">destroyed</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//销毁组件</span>
    $(<span class="hljs-built_in">this</span>.$el).off().select2(<span class="hljs-string">"destroy"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">具有伸缩性的 Header Example</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>
    @<span class="hljs-attr">mousedown</span>=<span class="hljs-string">"startDrag"</span>
    @<span class="hljs-attr">mousemove</span>=<span class="hljs-string">"onDrag"</span>
    @<span class="hljs-attr">mouseup</span>=<span class="hljs-string">"stopDrag"</span>
    @<span class="hljs-attr">mouseleave</span>=<span class="hljs-string">"stopDrag"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__header"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"computedStyle"</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card__body"</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"HelloWorld"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">dragging</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">//是否按下，准备拖动</span>
      <span class="hljs-attr">start</span>: &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;, <span class="hljs-comment">//记录起点坐标</span>
      <span class="hljs-attr">distance</span>: &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125;, <span class="hljs-comment">//记录拖动的坐标</span>
    &#125;;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">computedStyle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> dy = <span class="hljs-built_in">this</span>.distance.y;
      <span class="hljs-keyword">const</span> dampen = dy > <span class="hljs-number">0</span> ? <span class="hljs-number">7</span> : <span class="hljs-number">12</span>;
      <span class="hljs-keyword">const</span> height = <span class="hljs-number">160</span> + dy / dampen; <span class="hljs-comment">//160px 是固定的头部高度，所以要加上去。</span>
      <span class="hljs-keyword">const</span> radius = dy / <span class="hljs-number">480</span> * <span class="hljs-number">100</span>;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">height</span>: height + <span class="hljs-string">"px"</span>, <span class="hljs-attr">borderBottomLeftRadius</span>: radius + <span class="hljs-string">"%"</span>,<span class="hljs-attr">borderBottomRightRadius</span>: radius + <span class="hljs-string">"%"</span> &#125;;
    &#125;,
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">startDrag</span>(<span class="hljs-params">e</span>)</span> &#123;
      e = e.changeTouches ? e.changeTouches : e;
      <span class="hljs-built_in">this</span>.dragging = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.start.x = e.pageX;
      <span class="hljs-built_in">this</span>.start.y = e.pageY;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onDrag</span>(<span class="hljs-params">e</span>)</span> &#123;
      e = e.changeTouches ? e.changeTouches : e;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dragging) &#123;
        <span class="hljs-built_in">this</span>.distance.y = e.pageY - <span class="hljs-built_in">this</span>.start.y;
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">stopDrag</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dragging) &#123;
        <span class="hljs-built_in">this</span>.dragging = <span class="hljs-literal">false</span>;
        <span class="hljs-built_in">window</span>.dynamics.animate(
          <span class="hljs-built_in">this</span>.distance,
          &#123;
            <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">window</span>.dynamics.spring,
            <span class="hljs-attr">duration</span>: <span class="hljs-number">700</span>,
            <span class="hljs-attr">friction</span>: <span class="hljs-number">280</span>,
          &#125;
        );
      &#125;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.card</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">320px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">480px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#eee</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">500px</span> auto;
  user-select: none;
&#125;
<span class="hljs-selector-class">.card__header</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">160px</span>;
  <span class="hljs-attribute">background</span>: grey;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">1s</span>;
&#125;
<span class="hljs-selector-class">.card__body</span> &#123;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">30px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>我们需要通过 <code>start</code> 来记录用户每次拖动时的起始坐标，通过拖动坐标减去起始坐标，得到的才是有效的拖动距离。</li>
<li>通过添加 <code>draging</code> 标志结合 <code>mousemove</code> 事件，用来判断用户是否已经准备拖动以及是否已处于拖动中。</li>
<li><strong>手动调参</strong>给出一个大致效果的阻尼值 <code>dampen</code>，并且通过判断的 <code>distance.y</code> 值的正负来应用不同的阻尼系数。</li>
<li><code>mouseleave</code> 事件不支持冒泡，所以进入其子元素内部不会触发离开事件。</li>
<li>使用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fdynamicsjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://dynamicsjs.com/" ref="nofollow noopener noreferrer">dynamics</a> 动画库实现物理动画。</li>
</ol>
<h2 data-id="heading-3">最后</h2>
<p>其实我对官方示例中的“阻尼”计算方式很困惑，官方中会在拖动过程中用实际的拖动距离除以一个阻尼值。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-attr">onDrag</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    e = e.changedTouches ? e.changedTouches[<span class="hljs-number">0</span>] : e;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dragging) &#123;
      <span class="hljs-comment">// dampen vertical drag by a factor</span>
      <span class="hljs-keyword">var</span> dy = e.pageY - <span class="hljs-built_in">this</span>.start.y;
      <span class="hljs-keyword">var</span> dampen = dy > <span class="hljs-number">0</span> ? <span class="hljs-number">1.5</span> : <span class="hljs-number">4</span>;
      <span class="hljs-built_in">this</span>.c.y = <span class="hljs-number">160</span> + dy / dampen;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在计算属性中修改样式时又计算了一次阻尼。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">computed</span>:&#123;
         <span class="hljs-attr">contentPosition</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> dy = <span class="hljs-built_in">this</span>.c.y - <span class="hljs-number">160</span>;
            <span class="hljs-keyword">var</span> dampen = dy > <span class="hljs-number">0</span> ? <span class="hljs-number">2</span> : <span class="hljs-number">4</span>;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">transform</span>: <span class="hljs-string">"translate3d(0,"</span> + dy / dampen + <span class="hljs-string">"px,0)"</span>
            &#125;;
          &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看上去应该只需要计算一次即可，没必要把拖动距离的计算分在两个地方，分别除以两个不同的阻尼系数，如果你能理解官方示例的真正含义，请麻烦在下面给我评论，感激不尽。</p>
<p>官方示例地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fexamples%2Felastic-header.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/examples/elastic-header.html" ref="nofollow noopener noreferrer">cn.vuejs.org/v2/examples…</a></p></div>  
</div>
            