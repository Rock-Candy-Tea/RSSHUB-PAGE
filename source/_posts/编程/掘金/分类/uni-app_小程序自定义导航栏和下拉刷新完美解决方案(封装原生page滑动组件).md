
---
title: 'uni-app_小程序自定义导航栏和下拉刷新完美解决方案(封装原生page滑动组件)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8f9e92abda34f1fa659206462c8ff74~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 19:01:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8f9e92abda34f1fa659206462c8ff74~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">本组件优势：</h3>
<p>1、使用小程序/uniapp<strong>原生page滑动</strong>，流畅度高于scroll-view组件<br>
2、采用组件方式直接使用，只需在<strong>下拉刷新</strong>、<strong>上拉加载</strong>、<strong>加载完成时</strong>触发组件方法即可<br>
3、包含无数据时<strong>空布局</strong>展示<br>
4、可自定义<strong>下拉刷新</strong>、<strong>上拉加载</strong>样式<br>
5、采用组件的<strong>双向绑定v-model</strong><br>
6、完美解决<strong>自定义导航</strong>后看不到<strong>下拉刷新loading</strong>的问题<br></p>
<h3 data-id="heading-1">实际效果图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8f9e92abda34f1fa659206462c8ff74~tplv-k3u1fbpfcp-zoom-1.image" width="300px" loading="lazy" referrerpolicy="no-referrer"><br>
我们在page.json中开启了<strong>自定义导航栏</strong>属性和<strong>下拉刷新</strong>属性后</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 开启下拉刷新</span>
<span class="hljs-string">"enablePullDownRefresh"</span>: <span class="hljs-literal">true</span>
<span class="hljs-comment">// 自定义导航栏</span>
<span class="hljs-string">"navigationStyle"</span>: <span class="hljs-string">"custom"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，页面中的下拉刷新三个小圆点会被我们的导航栏遮盖住，导致用户下拉刷新看不到loading效果，如下图
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d73f30b38f8a4013bebbf2890853b6aa~tplv-k3u1fbpfcp-zoom-1.image" width="300px" loading="lazy" referrerpolicy="no-referrer"><br>
这样用户体验就不好了，接下来我们看看怎么解决：<br>
1、封装mscroll组件<br>
2、封装组件内<strong>下拉刷新</strong>、<strong>上拉加载</strong>、<strong>加载完成时</strong>方法<br>
3、利用<code>margin-top: -100upx;</code>在用户下拉刷新之前隐藏我们写的loading<br></p>
<h3 data-id="heading-2">封装mscroll组件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mscroll"</span>></span>
    <span class="hljs-comment"><!-- 下拉刷新 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"loading pullLoading"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 内容插槽 --></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>/></span>
    <span class="hljs-comment"><!-- 上拉加载 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"hasNextPage"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"loading"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 空布局 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"empty"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'isEmpty'</span>></span>
      <span class="hljs-comment"><!-- 自己更换图片哟 --></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">'widthFix'</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../assets/image/logoPng.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里什么都没有呀~<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">value</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-keyword">default</span> () &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-comment">// 当前页码</span>
          <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>,
          <span class="hljs-comment">// 每页条数</span>
          <span class="hljs-attr">pageSize</span>: <span class="hljs-number">10</span>,
          <span class="hljs-comment">// 是否有下一页</span>
          <span class="hljs-attr">hasNextPage</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-comment">// 数据总数</span>
          <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>
        &#125;
      &#125;
    &#125;
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 下一页</span>
      <span class="hljs-attr">hasNextPage</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-comment">// 无数据</span>
      <span class="hljs-attr">isEmpty</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-comment">// 加载中</span>
      <span class="hljs-attr">isLoading</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">// 转换一下pages</span>
    pages () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 下拉刷新</span>
    pullRefresh () &#123;
      <span class="hljs-comment">// 加载中</span>
      <span class="hljs-built_in">this</span>.isLoading = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, &#123;...this.pages, <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>&#125;)
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'getData'</span>)
    &#125;,
    <span class="hljs-comment">// 上拉加载</span>
    loadMore () &#123;
      <span class="hljs-comment">// 无下一页或加载中不加载</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.hasNextPage || <span class="hljs-built_in">this</span>.isLoading) <span class="hljs-keyword">return</span>
      <span class="hljs-comment">// 加载中</span>
      <span class="hljs-built_in">this</span>.isLoading = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, &#123;...this.pages, <span class="hljs-attr">page</span>: <span class="hljs-built_in">this</span>.pages.page + <span class="hljs-number">1</span>&#125;)
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'getData'</span>)
    &#125;,
    <span class="hljs-comment">// 加载成功方法</span>
    loadSuccess (data) &#123;
      <span class="hljs-comment">// 第一页要回到顶部</span>
      <span class="hljs-keyword">if</span> (data.page == <span class="hljs-number">1</span>) &#123;
        uni.pageScrollTo(&#123;
          <span class="hljs-attr">scrollTop</span>: <span class="hljs-number">0</span>
        &#125;)
      &#125;
      <span class="hljs-comment">// 结束下拉刷新</span>
      uni.stopPullDownRefresh()
      <span class="hljs-comment">// 关闭加载中</span>
      <span class="hljs-built_in">this</span>.isLoading = <span class="hljs-literal">false</span>
      <span class="hljs-comment">// 是否有下一页（可根据总页数和当前页数判断）</span>
      <span class="hljs-built_in">this</span>.hasNextPage = data.hasNextPage
      <span class="hljs-comment">// 是否有数据</span>
      <span class="hljs-built_in">this</span>.isEmpty = !data.total
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'scss'</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  // 加载中动画
  <span class="hljs-keyword">@keyframes</span> dotFlashing &#123;
    <span class="hljs-number">0%</span> &#123;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#ccc</span>;
    &#125;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#999</span>;
    &#125;
  &#125;
  <span class="hljs-selector-class">.mscroll</span>&#123;
    // loading
    <span class="hljs-selector-class">.loading</span> &#123;
      <span class="hljs-attribute">display</span>: flex;
      <span class="hljs-attribute">justify-content</span>: center;
      <span class="hljs-attribute">align-items</span>: center;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100</span>upx;
      <span class="hljs-attribute">overflow</span>: hidden;
      &<span class="hljs-selector-class">.pullLoading</span>&#123;
        // 这里是关键
        <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">100</span>upx;
      &#125;
      // 模拟微信小圆点
      <span class="hljs-selector-class">.dot</span> &#123;
        <span class="hljs-attribute">display</span>: inline-block;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">14</span>upx;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">14</span>upx;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#999</span>;
        <span class="hljs-attribute">animation</span>: dotFlashing <span class="hljs-number">1s</span> infinite linear alternate;
        <span class="hljs-attribute">animation-delay</span>: .<span class="hljs-number">5s</span>;
        &<span class="hljs-selector-pseudo">::before</span> &#123;
          <span class="hljs-attribute">left</span>: -<span class="hljs-number">28</span>upx;
          <span class="hljs-attribute">animation</span>: dotFlashing <span class="hljs-number">1s</span> infinite alternate;
          <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0s</span>;
        &#125;
        &<span class="hljs-selector-pseudo">::after</span> &#123;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">28</span>upx;
          <span class="hljs-attribute">animation</span>: dotFlashing <span class="hljs-number">1s</span> infinite alternate;
          <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">1s</span>;
        &#125;
        &<span class="hljs-selector-pseudo">::before</span>,
        &<span class="hljs-selector-pseudo">::after</span> &#123;
          <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
          <span class="hljs-attribute">display</span>: inline-block;
          <span class="hljs-attribute">position</span>: absolute;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">14</span>upx;
          <span class="hljs-attribute">height</span>: <span class="hljs-number">14</span>upx;
          <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
          <span class="hljs-attribute">background</span>: <span class="hljs-number">#999</span>;
        &#125;
      &#125;
    &#125;
    // 空布局
    <span class="hljs-selector-class">.empty</span>&#123;
      <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">280</span>upx;
      <span class="hljs-attribute">text-align</span>: center;
      <span class="hljs-selector-tag">img</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">180</span>upx;
      &#125;
      <span class="hljs-selector-tag">p</span>&#123;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20</span>upx;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#999</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">26</span>upx
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">使用方式</h3>
<h4 data-id="heading-4">page.json配置</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"pages"</span>: [
  &#123;
    <span class="hljs-string">"path"</span>: <span class="hljs-string">"pages/homePage/index"</span>,
    <span class="hljs-string">"style"</span>: &#123;
      <span class="hljs-string">"navigationBarTitleText"</span>: <span class="hljs-string">"页面标题"</span>, <span class="hljs-comment">// 页面标题</span>
  <span class="hljs-string">"enablePullDownRefresh"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启下拉刷新(必需)</span>
      <span class="hljs-string">"backgroundTextStyle"</span>: <span class="hljs-string">"light"</span>, <span class="hljs-comment">// 下拉刷新loading小圆点颜色，白底+白色小圆点可以实现“隐藏”原生小圆点哦</span>
      <span class="hljs-string">"navigationStyle"</span>: <span class="hljs-string">"custom"</span>, <span class="hljs-comment">// 自定义导航栏(不自定义导航栏也可以使用本组件哦，只不过就只能使用原生小圆点样式了，无法自定义下拉刷新样式)</span>
      <span class="hljs-string">"backgroundColor"</span>: <span class="hljs-string">"#F5F7F9"</span> <span class="hljs-comment">// 页面背景底色</span>
    &#125;
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">父组件使用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
                              <!-- 计算出你的导航高度 -->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'index'</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;'padding-top': '100px'&#125;"</span>></span>
    <span class="hljs-comment"><!-- 自定义导航栏 --></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;height: '100px'&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
    <span class="hljs-comment"><!-- 列表（pages必传，getData是加载方法） --></span>
    <span class="hljs-tag"><<span class="hljs-name">m-scroll</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'mscroll'</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"pages"</span> @<span class="hljs-attr">getData</span>=<span class="hljs-string">'getData'</span>></span>
      <span class="hljs-comment"><!-- 列表数据 --></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"i in list"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"i"</span>></span>模拟数据 ------------- 第&#123;&#123;i + 1&#125;&#125;条<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">m-scroll</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> mScroll <span class="hljs-keyword">from</span> <span class="hljs-string">'./mscroll'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    mScroll
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">list</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">pages</span>: &#123;
        <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">pageSize</span>: <span class="hljs-number">10</span>
      &#125;
    &#125;
  &#125;,
  <span class="hljs-comment">// 触发下拉刷新</span>
  onPullDownRefresh () &#123;
    <span class="hljs-built_in">this</span>.$refs.mscroll.pullRefresh()
  &#125;,
  <span class="hljs-comment">// 触发上拉加载</span>
  onReachBottom () &#123;
    <span class="hljs-built_in">this</span>.$refs.mscroll.loadMore()
  &#125;,
  onLoad () &#123;
    <span class="hljs-built_in">this</span>.getData()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    getData () &#123;
      <span class="hljs-comment">// 模拟请求</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.list += <span class="hljs-number">10</span>
        <span class="hljs-keyword">const</span> total = <span class="hljs-number">50</span>
        <span class="hljs-keyword">const</span> hasNextPage = total != <span class="hljs-built_in">this</span>.list
        <span class="hljs-keyword">const</span> data = &#123;
          <span class="hljs-attr">page</span>: <span class="hljs-built_in">this</span>.pages.page, <span class="hljs-comment">// 需包含页码</span>
          total, <span class="hljs-comment">// 需包含总数</span>
          hasNextPage <span class="hljs-comment">// 需包含是否下一页</span>
        &#125;
        <span class="hljs-comment">// 触发加载成功，需包含当前页码、数据总数、是否有下一页</span>
        <span class="hljs-built_in">this</span>.$refs.mscroll.loadSuccess(data)
      &#125;, <span class="hljs-number">1000</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'scss'</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  // 自定义导航栏
  <span class="hljs-selector-tag">nav</span>&#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#446AAD</span>;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-selector-tag">ul</span>&#123;
    <span class="hljs-selector-tag">li</span>&#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">20</span>upx;
      <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#eee</span>;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，代码就写完啦，考虑不周或者有bug的地方，还望多多留言告知我哟😁！</p></div>  
</div>
            