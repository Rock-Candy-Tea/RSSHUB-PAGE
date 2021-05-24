
---
title: '手把手教你使用JavaScript实现一个slider无限滚动插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ab252ac0340424ca38be7df6f7fa133~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 18:48:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ab252ac0340424ca38be7df6f7fa133~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 滚动插件的使用缘由</h1>
<p>在项目开发中，图片滚动的应用场景特别多。有很多设计依靠滚动来实现。那么此时我们可以选择不同的滚动插件达到相同的效果。但是，外部插件却是是比较优秀，但是同时因为功能性代码太多，根据我们 组的开发情况，我们基本杜绝了外部插件，除非特殊情况必须使用。<br>
而我编写的这个插件，可以实现目前设计中的各种滚动场景，支持自定义滚动距离，只要你是以下结构，你就可以直接将该滚动插件套用。当然，不是说一定要url>li 结构，而是只要是这种列表形式的dom结构都可以。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ab252ac0340424ca38be7df6f7fa133~tplv-k3u1fbpfcp-watermark.image" alt="1621564832.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>PC</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d645ee4976a04063af8840ccd170cbdd~tplv-k3u1fbpfcp-watermark.image" alt="1621560803 (1).png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<p><strong>Mobile</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93ea635dbe584c459e29433f5ee20a49~tplv-k3u1fbpfcp-watermark.image" alt="1621560827.png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<h1 data-id="heading-1">2. 需求驱动开发</h1>
<p>我的页面并不是只有一个滚动，而是有很多个滚动效果。因此，并不能将代码写死在具体某一个dom（或者class名称）上。毕竟，在不同的结构中，class名称不可能一模一样。也不能因为滚动，就添加额外的class名称来控制。最简单的就是按照需要，提取公共的参数。<br></p>
<ul>
<li>parent: 滚动列表的父容器,</li>
<li>children: 具体滚动列表集合,</li>
<li>scrollStep：每次滑动的宽度,</li>
<li>currentIndex：当前滚动显示的索引,</li>
<li>childCls： child列表的class名称,</li>
<li>isInfiniteScroll：是否需要支持无限滚动,</li>
<li>paginationMethods：该插件根据需求支持3钟分页按钮，该方法可以自定义需要哪些，不局一个分页,</li>
<li>paginationStep：每一页显示的个数（总共有4个card，默认4页，值设置为2，那么页数为2页）,</li>
<li>customInitDom：当进行无限循环，每页有多个card, 当最后一个只有1个card,需要将剩下的card使用占位符占位，该值表示使用什么节点进行占位，默认为li</li>
</ul>
<p>tip： 我们利用CSS transform 来实现移动。</p>
<h1 data-id="heading-2">3. 基本结构</h1>
<p>下面呈现了该组件的基本结构，其实就是一个 slider 组件类，然后new 了一个组件出来。
我们还在组件内部，进行初始化了一系列的私有变量，每一个变量已近进行了详细注释。看到这里，可能对变量不是很清楚使用，这个没关系，我们后续每隔方法中会使用到。
但是注意 prototype上的 originListDoms 变量，它的作用是：当界面进行大小拖拽时，界面处于PC/Mobile的样式之间来回切换，如果mobile和pc一页显示的数量不一致，例如上面示例图中的情况，那么就需要存储原有的dom,这个参数就是用于存储改值的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Slider</span>(<span class="hljs-params">parent, children, scrollStep, currentIndex, childCls, isInfiniteScroll, paginationMethods, paginationStep, customInitDom</span>) </span>&#123;
 <span class="hljs-comment">// dom 相关参数初始化</span>
  paginationStep = paginationStep || <span class="hljs-number">1</span>; <span class="hljs-comment">// 默认每页1个card</span>
  <span class="hljs-keyword">var</span> parent = parent;
  <span class="hljs-keyword">var</span> childCount = <span class="hljs-built_in">Math</span>.ceil(children.length / paginationStep); <span class="hljs-comment">// 多少个card</span>
  <span class="hljs-keyword">var</span> scrollStep = scrollStep; <span class="hljs-comment">// 每次滑动的距离</span>
  <span class="hljs-keyword">var</span> currentIndex = currentIndex; <span class="hljs-comment">// 当前选中的index(分页显示使用或者 正常滑动的索引)</span>
  <span class="hljs-keyword">var</span> infiniteCurrentIndex = currentIndex; <span class="hljs-comment">// 无限滚动的索引（无限滚动时，分页的索引使用currentIndex）</span>

 <span class="hljs-comment">// 位置相关参数初始化</span>
  <span class="hljs-keyword">var</span> startPosition, <span class="hljs-comment">// 滑动开始的位置</span>
  endPosition, <span class="hljs-comment">// 滑动结束位置</span>
  deltaX, <span class="hljs-comment">// 横向滑动距离</span>
  deltaY, <span class="hljs-comment">// 纵向滑动距离</span>
  isTouchStartFirst = <span class="hljs-number">1</span>, <span class="hljs-comment">// 是否第一次touch滚动</span>
  isScroll; <span class="hljs-comment">// isScroll 为0时，表示纵向滑动，1为横向滑动</span>
  <span class="hljs-keyword">var</span> isScrollProgress = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 是否在滑动中，用于计算滑动时不能点击card</span>

 <span class="hljs-comment">// 如果滑动元素有a标签，滑动中禁止点击</span>
  <span class="hljs-keyword">var</span> hrefAs = parent.find(<span class="hljs-string">'a'</span>); <span class="hljs-comment">// 计算滑动中，将card link禁用</span>
  <span class="hljs-keyword">var</span> isPc = <span class="hljs-built_in">window</span>.iSPc();
 
  <span class="hljs-built_in">this</span>.initMobileOrPcSlider = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
 
  &#125;
&#125;
Slider.prototype.originListDoms = &#123;&#125;;


<span class="hljs-comment">//实例化Slider</span>
<span class="hljs-keyword">var</span> slider = <span class="hljs-keyword">new</span> Slider(gallery, children, scrollStep, <span class="hljs-number">0</span>, childCls, isInfiniteScroll, paginationMethods, paginationStep, customInitDom);

slider.initMobileOrPcSlider();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4. 组件初始化</h1>
<p>下面进行了伪代码的编写，我们首先进行了事件 dom等一系列的初始化，为什么呢？为了当自适应的时候，pc/mobile样式切换时进行，重置之前所有的参数，方便后续初始化。<br></p>
<p>为什么需要将 手机滚动事件、pc滚动事件也一起注册，同样是为了应付PC 调整尺寸大小时，为了平板尺寸大小时，能够进行滑动。<br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.initMobileOrPcSlider = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

  <span class="hljs-comment">// 清除所有的事件，dom初始化等</span>
  gallery.siblings(<span class="hljs-string">'.gallery-pagination'</span>).remove();
  gallery.siblings(<span class="hljs-string">'.gallery-pagination-circle'</span>).remove();
  gallery.css(<span class="hljs-string">'marginLeft'</span>, <span class="hljs-string">'0px'</span>);
  gallery.css(<span class="hljs-string">'transform'</span>, <span class="hljs-string">' translate3d(0px, 0px, 0px)'</span>);
  <span class="hljs-comment">// 2. 先卸载移动事件，避免resize时，重复注册</span>
  gallery.off(<span class="hljs-string">'touchstart'</span>);
  gallery.off(<span class="hljs-string">'mousedown'</span>);



  <span class="hljs-comment">// 是如果无限滚动处，进行dom处理</span>
  isInfiniteScroll && infiniteScrollDomInit();

  <span class="hljs-comment">// 注册动画滚动结束事件 </span>
  initTransitionend();
  
  <span class="hljs-comment">// 注册手机滑动效果</span>
  registerMobileScroll();
 

 <span class="hljs-comment">// 注册PC 滑动效果</span>
 registerPCScroll();

<span class="hljs-comment">// 动态添加小圆点</span>
<span class="hljs-keyword">if</span> (paginationMethods） &#123;
 <span class="hljs-comment">//初始化自定义的小圆点</span>
getCustomPagination(paginationMethods);
&#125; <span class="hljs-keyword">else</span> &#123;
 <span class="hljs-comment">// 根据pc mobile 初始化小圆点或者分页按钮</span>

isPc ? initPCGalleryPagination() : initMobileGalleryPagination();&#125;

&#125;
preventHrefLink();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理card上的a标签，滑动不能点击</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> preventHrefLink = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    hrefAs.on(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (isScrollProgress) &#123;
        e.preventDefault();
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;
    &#125;);
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，那么接下来，我们就开始按照上面的伪代码，丰满每一个小的步骤。</p>
<h2 data-id="heading-4">4.1 无限循环处理</h2>
<p>无限滚动，实际利用了一个视觉的障眼法。按照以下步骤实现：<br></p>
<ul>
<li>将第一张，拷贝到最后一个位置，最后一个张内容，拷贝到第一个位置。例如下面的卡片。</li>
<li>dom准备好后，将滚动区域向前移动一个card距离（每次滚动的的间距）</li>
<li>注册滚动结束时的事件。滚动可以向前滚动，可以向后滚动。如果向前滚动到最前面的一张（card3备份，索引为0）,那么将其索引设置为3（card3原图）。并在滚动结束时滚动到card3原图。因为滚动的时候使用了动画，那么在滚动到card3原图时，不使用动画，直接跳转，视觉上和card3备份图内容一致，感觉不到任何差异，就完成了无缝切换的效果。当然，滚动到最后一张图也是类似操作，当最后一张card1复制 滚动结束时，将索引设置为Card1,并消除动画，移动到card1原图，实现无缝切换。<br></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce531229ad394de59ec3fdbde42b2293~tplv-k3u1fbpfcp-watermark.image" alt="1621818371.png" loading="lazy" referrerpolicy="no-referrer"><br>
到此，无限滚动处理完成，相关代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
   * 无限循环gallery, 初始化时，将第一个添加到最后，将最后一个添加到第一个
   */</span>
  <span class="hljs-keyword">var</span> infiniteScrollDomInit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">var</span> children = parent.find(childCls);

    <span class="hljs-comment">// 获取第一页元素和最后一页元素</span>
    <span class="hljs-keyword">var</span> preToEndDom = children.slice(<span class="hljs-number">0</span>, paginationStep);
    <span class="hljs-keyword">var</span> endToPreDom = children.slice(paginationStep * (childCount - <span class="hljs-number">1</span>), paginationStep * (childCount - <span class="hljs-number">1</span>) + <span class="hljs-number">2</span>);

    <span class="hljs-comment">// endToPreDom 如果不够一页内容，则使用li填充</span>
    <span class="hljs-keyword">var</span> endPageCount = endToPreDom.length;
    <span class="hljs-keyword">if</span> (endPageCount < paginationStep) &#123;

      <span class="hljs-comment">// 最后一页数量只有一条，但是每一页需要显示paginationStep，则现在父组件末尾添加一些空的占位符</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = endPageCount; i < paginationStep; i++ ) &#123;
        customInitDom = customInitDom || <span class="hljs-string">'<li></li>'</span>;
        parent.append($(customInitDom));
      &#125;
      endToPreDom = parent.find(childCls).slice(paginationStep * (childCount - <span class="hljs-number">1</span>), paginationStep * (childCount - <span class="hljs-number">1</span>) + <span class="hljs-number">2</span>);
    &#125;
    
    <span class="hljs-comment">// 添加到最前面和最后面</span>
    parent.prepend($(endToPreDom.clone()));
    parent.append($(preToEndDom.clone()));
    parent.css(<span class="hljs-string">'marginLeft'</span>, -(scrollStep) + getUnit());

    <span class="hljs-comment">// 更新a标签（添加的dom也需要追加）</span>
    hrefAs = parent.find(<span class="hljs-string">'a'</span>);
  &#125;



  <span class="hljs-comment">/**
   * 当动画滚动结束后，将isScrollProgress设置为false，表示滚动结束
   * - 当滚动到最前面或者最后面，初始化index索引，并将其滚动到与其内容相同的card上
   */</span>
  <span class="hljs-keyword">var</span> initTransitionend = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    parent.on(<span class="hljs-string">'transitionend'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;


      <span class="hljs-comment">// 移动完成，将表示设置为false</span>
      isScrollProgress = <span class="hljs-literal">false</span>;

      <span class="hljs-comment">// 如果滑动到最最后面，索引修改为 第一个</span>
      <span class="hljs-keyword">if</span> (infiniteCurrentIndex == childCount) &#123;
        infiniteCurrentIndex = <span class="hljs-number">0</span>;
        move(infiniteCurrentIndex, <span class="hljs-number">0</span>);
      &#125;
  
      <span class="hljs-comment">// 如果滑动到最前面，索引修改为 最后一个</span>
      <span class="hljs-keyword">if</span> (infiniteCurrentIndex < <span class="hljs-number">0</span>) &#123;
        infiniteCurrentIndex = childCount - <span class="hljs-number">1</span>;
        move(infiniteCurrentIndex, <span class="hljs-number">0</span>);
      &#125;
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4.2 给slider注册滑动事件</h2>
<p>现在，我们需要给Slider注册上滚动事件，让我们手动滑动时，能够进行滚动。当然，如果你是希望自动播放，那么你可以通过setInterval等相关的操作实现。<br>
我们上面在定义参数时，<code>isScrollPrgress</code>就是表示，是否在滚动中。滚动中就不进行第二次滚动触发。不管是PC/Mobile都是一样的。<br>
我们还需要注意一点：滚动时，如果滚动的角度小（例如是纵向滑动，就不应该滚动），那么避免滚动。<br></p>
<ul>
<li>Mobile 滑动效果，通过 touchstart, touchmove, touched来实现。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-comment">// -------手机滑动效果 start</span>
    parent.on(<span class="hljs-string">'touchstart'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
      <span class="hljs-comment">// 如果在移动中，不再进行下一次移动</span>
      <span class="hljs-keyword">if</span> (isScrollProgress) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">var</span> touch = e.originalEvent.targetTouches[<span class="hljs-number">0</span>];
      startPosition = &#123;
          <span class="hljs-attr">x</span>: touch.clientX,
          <span class="hljs-attr">y</span>: touch.clientY
      &#125;
      isTouchStartFirst = <span class="hljs-number">1</span>;

      parent.on(<span class="hljs-string">'touchmove'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        isScrollProgress = <span class="hljs-literal">true</span>;
        <span class="hljs-keyword">var</span> touch = e.targetTouches[<span class="hljs-number">0</span>];
        endPosition = &#123;
            <span class="hljs-attr">x</span>: touch.clientX,
            <span class="hljs-attr">y</span>: touch.clientY
        &#125;;
        deltaX = endPosition.x - startPosition.x;
        deltaY = endPosition.y - startPosition.y;
        <span class="hljs-comment">//  只有刚开始的touchstart，才去判断滑动的方向</span>
        <span class="hljs-keyword">if</span>(isTouchStartFirst === <span class="hljs-number">1</span>)&#123;
            isScroll = (<span class="hljs-built_in">Math</span>.abs(deltaX)  * <span class="hljs-number">1.3</span>- <span class="hljs-built_in">Math</span>.abs(deltaY)) > <span class="hljs-number">0</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">0</span>;
        &#125;
        isTouchStartFirst++;
        <span class="hljs-comment">//  isScrolling为0时，表示纵向滑动，1为横向滑动</span>
        <span class="hljs-keyword">if</span> (isScroll === <span class="hljs-number">1</span>) &#123;
          e.preventDefault();
          <span class="hljs-keyword">if</span> (deltaX !== <span class="hljs-number">0</span> && isInfiniteScroll) &#123;
            mouseMoveTransation(deltaX);
          &#125;
        &#125;
      &#125;);
      parent.on(<span class="hljs-string">'touchend'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span> ((<span class="hljs-built_in">Math</span>.abs(deltaY) > <span class="hljs-number">10</span> && <span class="hljs-built_in">Math</span>.abs(deltaX) < <span class="hljs-number">10</span>) || isScroll === <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span>(deltaX < <span class="hljs-number">0</span>) &#123;
          movePre();
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(deltaX > <span class="hljs-number">0</span>) &#123;
          moveNext();
        &#125;

        parent.off(<span class="hljs-string">'touchmove'</span>);
        parent.off(<span class="hljs-string">'touchend'</span>);
      &#125;);
    &#125;);
    <span class="hljs-comment">// --------Mobile滑动效果 end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>PC 滑动效果，通过 mousedown, mousemove, mouseup来实现。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    parent.on(<span class="hljs-string">'mousedown'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ev</span>) </span>&#123;
      <span class="hljs-comment">// 如果在移动中，不再进行下一次移动</span>
      <span class="hljs-keyword">if</span> (isScrollProgress) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      ev.preventDefault();
      ev.stopPropagation();
      ev.cancelable = <span class="hljs-literal">false</span>;
      startPosition = &#123;
          <span class="hljs-attr">x</span>: ev.pageX
      &#125;
      $(<span class="hljs-string">"body"</span>).on(<span class="hljs-string">'mousemove'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        isScrollProgress = <span class="hljs-literal">true</span>;
          endPosition = &#123;
              <span class="hljs-attr">x</span>: e.pageX,
          &#125;;
          deltaX = endPosition.x - startPosition.x;
          <span class="hljs-keyword">if</span> (deltaX !== <span class="hljs-number">0</span> && isInfiniteScroll) &#123;
            mouseMoveTransation(deltaX);
          &#125;
      &#125;);

      $(<span class="hljs-string">"body"</span>).on(<span class="hljs-string">'mouseup'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span>(deltaX < <span class="hljs-number">0</span>) &#123;
          movePre();
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(deltaX > <span class="hljs-number">0</span>) &#123;
          moveNext();
        &#125;

        $(<span class="hljs-string">"body"</span>).off(<span class="hljs-string">'mousemove'</span>);
        $(<span class="hljs-string">"body"</span>).off(<span class="hljs-string">'mouseup'</span>);
      &#125;);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4.3 根据拖拽移动</h2>
<p>加入我们开始滑动，但是鼠标左右拖拽，那么此时将card随着鼠标的位置进行移动，这样会显得我们的slider比较活跃。当然，该操作是在 mousemove/touchmove时触发的。<br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">var</span> mouseMoveTransation =  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mouseMoveWidth</span>) </span>&#123;
    mouseMoveWidth = isPc ? ( mouseMoveWidth / parent.width() * <span class="hljs-number">100</span>) : mouseMoveWidth / <span class="hljs-number">100</span>;
    <span class="hljs-keyword">var</span> transtationWidth = tranlateX + mouseMoveWidth;
    parent.css(<span class="hljs-string">'transform'</span>, <span class="hljs-string">'translate3d('</span> + transtationWidth + getUnit()  + <span class="hljs-string">', 0px, 0px)'</span>);
    parent.css(<span class="hljs-string">'transitionDuration'</span>, <span class="hljs-string">'0s'</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">4.4 移动处理</h2>
<p>上面的准备操作依据完成了，<code>movePre</code>和<code>moveNext</code>还是一个空壳。 那么下面开始直接实现移动效果。<br></p>
<p>每次移动后，进行了分页刷新 reloadPagination，这里先知道就可以了，分页的方法放在最后。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
   * 计算滚动距离
   * <span class="hljs-doctag">@param<span class="hljs-type">&#123;*&#125;</span></span>current 当前索引
   */</span>
vargetScrollWidth = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">current</span>) </span>&#123;
returnscrollStep * current;
  &#125;

vargetUnit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">// var unit = isPc ? '%' : '%';</span>
<span class="hljs-keyword">return</span><span class="hljs-string">'%'</span>;
  &#125;

<span class="hljs-comment">/**
   * 移动一个图片
   * <span class="hljs-doctag">@param<span class="hljs-type">&#123;*&#125;</span></span>current 当前选中页面
   * <span class="hljs-doctag">@param<span class="hljs-type">&#123;*&#125;</span></span>transitionDuration 滑动消费时间
   */</span>
varmove = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">current, transitionDuration</span>) </span>&#123;
tranlateX = -getScrollWidth(current);
parent.css(<span class="hljs-string">'transform'</span>, <span class="hljs-string">'translate3d('</span> + tranlateX + getUnit()  + <span class="hljs-string">', 0px, 0px)'</span>);
varnewTransitionDuration = (transitionDuration === <span class="hljs-literal">undefined</span> || transitionDuration === <span class="hljs-literal">null</span>) ? <span class="hljs-number">0.6</span> : transitionDuration;
parent.css(<span class="hljs-string">'transitionDuration'</span>, (<span class="hljs-built_in">parseFloat</span>(newTransitionDuration) * paginationStep) + <span class="hljs-string">'s'</span>);
reloadPagination();
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的方法，是移动一个图片，通过css的属性实现的。对应无限滚动和普通滚动都是一致的。那么接下来我们就处理<code>movePre</code>和<code>moveNext</code>方法。<br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
   * 滑动方式左移动
   */</span>
  <span class="hljs-keyword">var</span> movePre = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    isInfiniteScroll ? infiniteMovePre() : finiteMovePre();
  &#125;;

  <span class="hljs-comment">/**
   * 滑动方式右移动
   */</span>
  <span class="hljs-keyword">var</span> moveNext = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    isInfiniteScroll ? infiniteMoveNext() : finiteMoveNext();
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>普通滑动事件处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">/**
   * 向左边移动
   */</span>
  <span class="hljs-keyword">var</span> finiteMovePre = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (currentIndex >= childCount - <span class="hljs-number">1</span>) &#123;
      isScrollProgress = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">return</span>;
    &#125;
    currentIndex++;
    move(currentIndex);
  &#125;
  
  <span class="hljs-comment">/**
   * 向右边移动
   */</span>
  <span class="hljs-keyword">var</span> finiteMoveNext = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (currentIndex <= <span class="hljs-number">0</span>) &#123;
      isScrollProgress = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">return</span>;
    &#125;
    currentIndex--;
    move(currentIndex);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无限滚动滑动事件处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** 
   * 无限循环向左移动
   * curentIndex 用于显示pagination，因此保持更新
  */</span>
  <span class="hljs-keyword">var</span> infiniteMovePre = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

    <span class="hljs-comment">// 处理pagination 的index,逻辑保持不变</span>
    <span class="hljs-keyword">if</span> (currentIndex >= childCount - <span class="hljs-number">1</span>) &#123;
      currentIndex = <span class="hljs-number">0</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      currentIndex++;
    &#125;

    infiniteCurrentIndex++;
    move(infiniteCurrentIndex);
  &#125;
  
  <span class="hljs-comment">/**
   * 无限循环向右边移动
   * curentIndex 用于显示pagination，因此保持更新
   */</span>
  <span class="hljs-keyword">var</span> infiniteMoveNext = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (currentIndex <= <span class="hljs-number">0</span>) &#123;
      currentIndex = childCount - <span class="hljs-number">1</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      currentIndex--;
    &#125;

    infiniteCurrentIndex--;
    move(infiniteCurrentIndex);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按钮方式点击分页</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">/**
   * 通过按钮左移动
   */</span>
  <span class="hljs-keyword">var</span> clickPreMove = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isScrollProgress) &#123;
      isScrollProgress = <span class="hljs-literal">true</span>;
      movePre();
    &#125;
  &#125;;
  <span class="hljs-comment">/**
   * 通过按钮右移动
   */</span>
  <span class="hljs-keyword">var</span> clickNextMove = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!isScrollProgress) &#123;
      isScrollProgress = <span class="hljs-literal">true</span>;
      moveNext();
    &#125;
  &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4.5 分页处理</h2>
<p>这里，我选择了2中分页方式，一种小圆点方式，一种是按钮方式。小圆点方式可以用于PC,也可以用于Mobile。而按钮建议用于PC.</p>
<p><strong>小圆点分页</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">var</span> initMobileGalleryPagination = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> pagination = <span class="hljs-string">'<div class="gallery-pagination-circle">$&#123;items&#125;</div>'</span>, items = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < childCount; i++) &#123;
      <span class="hljs-keyword">let</span> spanDom = i === <span class="hljs-number">0</span> 
        ? <span class="hljs-string">'<span class="select-span" indexValue="'</span> + i + <span class="hljs-string">'" ></span>'</span> 
        : <span class="hljs-string">'<span indexValue="'</span> + i + <span class="hljs-string">'"></span>'</span>;
      items += spanDom;
    &#125;
    pagination = pagination.replace(<span class="hljs-string">'$&#123;items&#125;'</span>, items);
    parent.after(pagination);
    
    <span class="hljs-comment">// pagination 注册点击事件</span>
    <span class="hljs-keyword">var</span> paginationDom = parent.next()[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">if</span> (paginationDom) &#123;
      $(paginationDom).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'span'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">var</span> index = $(e.target).attr(<span class="hljs-string">'indexValue'</span>);
        currentIndex = index;
        infiniteCurrentIndex = index;
        move(index);
      &#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>按钮分页</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> initPreAndNextPagination = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    
    <span class="hljs-keyword">var</span> prePagination = $(<span class="hljs-string">'<span class="pre-pagination-btn"></span>'</span>);
    <span class="hljs-keyword">var</span> nextPagination = $(<span class="hljs-string">'<span class="next-pagination-btn"></span>'</span>);

    prePagination.on(<span class="hljs-string">'click'</span>, clickNextMove);
    nextPagination.on(<span class="hljs-string">'click'</span>, clickPreMove);

    <span class="hljs-comment">// 在父级的父级身上添加按钮</span>
    <span class="hljs-keyword">var</span> wrapper = parent.parent();
    wrapper.parent().css(<span class="hljs-string">'position'</span>, <span class="hljs-string">'relative'</span>);

    wrapper.siblings(<span class="hljs-string">'.pre-pagination-btn'</span>).remove()
    wrapper.siblings(<span class="hljs-string">'.next-pagination-btn'</span>).remove();

    wrapper.after(nextPagination);
    wrapper.after(prePagination);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**通过名字，自定义分页 **</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
   * 自定义分页：分页有很多种，当想自定义不同类型的分页，可以传递方法名称
   * 
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>paginationArr 自定义方法名称字符串 [initMobileGalleryPagination, initPCGalleryPagination, initPreAndNextPagination]
   */</span>
  <span class="hljs-keyword">var</span> getCustomPagination = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">paginationArr</span>) </span>&#123;
    <span class="hljs-keyword">var</span> originPagiantions = &#123;
      <span class="hljs-attr">initMobileGalleryPagination</span>: initMobileGalleryPagination,
      <span class="hljs-attr">initPCGalleryPagination</span>: initPCGalleryPagination,
      <span class="hljs-attr">initPreAndNextPagination</span>: initPreAndNextPagination,
    &#125;;
    paginationArr.map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">method</span>) </span>&#123;
      originPagiantions[method] && originPagiantions[method]();
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>不同分页方式分页reload</strong>
该方法在move函数中使用到的，每次通过说移动结束，需要手动更新分页显示。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> reloadPagination = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> paginationDom = parent.next();

    <span class="hljs-comment">// PC 页码方式分页</span>
    <span class="hljs-keyword">var</span> currentPage = paginationDom.find(<span class="hljs-string">'.current-page'</span>);
    <span class="hljs-keyword">if</span> (currentPage.length > <span class="hljs-number">0</span>) &#123;
      currentPage.text(currentIndex + <span class="hljs-number">1</span>);
    &#125;

    <span class="hljs-comment">// 底部Circle分页 点击分页后，更新页码</span>

    <span class="hljs-keyword">if</span> (paginationDom.hasClass(<span class="hljs-string">'gallery-pagination-circle'</span>)) &#123;
      <span class="hljs-keyword">var</span> circleSpans = paginationDom.children(<span class="hljs-string">'span'</span>);
      circleSpans.removeClass(<span class="hljs-string">'select-span'</span>);
      circleSpans.eq(currentIndex).addClass(<span class="hljs-string">'select-span'</span>);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">5. 窗口调整Resize初始化</h1>
<p>用户在使用的过程中，肯定会遇到拖拽，那么在拖拽的时候，我们不仅仅是css进行适应，还应该有JS注册事件。在上面我们已经在初始化中清除了所有的事件，方便resize时，重新初始化。但是我们可能做得更好，在进行resize时，如果是PC样式，那么就不在重复渲染。<br></p>
<p>我们公共resize和节流函数进行配合达到这个目的。<br></p>
<p>定义全局变量，通过 windowIsResize ，我们可以直到窗口是否移动。<br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.windowIsResize = <span class="hljs-literal">false</span>;
; (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">$</span>) </span>&#123;
  <span class="hljs-comment">// 上一次记录</span>
  <span class="hljs-keyword">var</span> preWindowWidth = $(<span class="hljs-built_in">window</span>).width();
  <span class="hljs-keyword">var</span> preDevice = iSPc();



  $(<span class="hljs-built_in">window</span>).resize(throttle(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

    <span class="hljs-comment">// resize 获取</span>
    <span class="hljs-keyword">var</span> currentWindowWidth = $(<span class="hljs-built_in">window</span>).width();
    <span class="hljs-keyword">var</span> currentDdevice = iSPc();

    <span class="hljs-comment">// 宽度相等或者设备相等，直接设置为false</span>
    <span class="hljs-keyword">if</span> (currentWindowWidth === preWindowWidth || currentDdevice === preDevice) &#123;
      <span class="hljs-built_in">window</span>.windowIsResize = <span class="hljs-literal">false</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">window</span>.windowIsResize = <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-comment">// 更新</span>
    preWindowWidth = currentWindowWidth;
    preDevice = currentDdevice;
  &#125;, <span class="hljs-number">200</span>));
&#125;)($);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过设备宽度判断，是否重新渲染slider</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">;(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$, <span class="hljs-built_in">document</span></span>) </span>&#123;
  resizeGallery();
  $(<span class="hljs-built_in">window</span>).resize(throttle(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 宽度变化且设备变化，重新初始化gallery</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.windowIsResize) &#123;
      

    <span class="hljs-keyword">var</span> slider= <span class="hljs-keyword">new</span> Slider(gallery, children, scrollStep, <span class="hljs-number">0</span>, childCls, isInfiniteScroll, paginationMethods, paginationStep, customInitDom);
    slider.initMobileOrPcGallery();

    &#125;
  &#125;, <span class="hljs-number">200</span>));
&#125;)($);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，Slider组件已经完成，肯定会存在一些小的问题，大家事件了可以告知我~~</p></div>  
</div>
            