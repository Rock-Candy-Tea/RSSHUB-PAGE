
---
title: 'vue3，后台管理列表页面各组件之间的状态关系'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932d1b0dfc45413aac0fd00c017ac2af~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 22:04:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932d1b0dfc45413aac0fd00c017ac2af~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">技术栈</h1>
<ul>
<li>vite2</li>
<li>vue 3.0.5</li>
<li>vue-router 4.0.6</li>
<li>vue-data-state 0.1.1</li>
<li>element-plus 1.0.2-beta.39</li>
</ul>
<h1 data-id="heading-1">前情回顾</h1>
<ul>
<li><a href="https://juejin.cn/post/6963783152611360781" target="_blank" title="https://juejin.cn/post/6963783152611360781">表单控件</a></li>
<li><a href="https://juejin.cn/post/6969118265175965710" target="_blank" title="https://juejin.cn/post/6969118265175965710">查询控件</a></li>
<li><a href="https://juejin.cn/post/6955416792625840135" target="_blank" title="https://juejin.cn/post/6955416792625840135">轻量级状态管理</a></li>
</ul>
<p>前面介绍的表单控件和查询控件，都是原子性的，实现自己的功能即可。
而这里要介绍的是管理后台里面的各个组件之间的状态关系。</p>
<blockquote>
<p>为啥需要状态？因为组件划分的非常原子化（细腻），所以造成了很多的组件，那么组件之间就需要一种“通讯方式”，这个就是状态了。不仅仅是传递数据，还可以实现事件总线。</p>
</blockquote>
<h1 data-id="heading-2">页面结构</h1>
<p>一般的后台管理大体是这样的结构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932d1b0dfc45413aac0fd00c017ac2af~tplv-k3u1fbpfcp-zoom-1.image" alt="后台页面结构.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体项目里页面结构会有一些变化，但是总体结构不会有太大的改变。</p>
<p>做出来的效果大体是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56eb35c61d324e1aaec854d96360a570~tplv-k3u1fbpfcp-zoom-1.image" alt="一种后台管理的效果" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>动态菜单</li>
</ul>
<p>根据用户权限加载需要的菜单。</p>
<ul>
<li>动态 tab</li>
</ul>
<p>点击一下左面的菜单，创建一个新的tab，然后加载对应的组件，一般是列表页面（组件），也可以是其他页面（组件）。</p>
<ul>
<li>查询</li>
</ul>
<p>各种查询条件那是必备的，总不能没有查询功能吧，查询控件需要提供查询条件。</p>
<ul>
<li>操作按钮组</li>
</ul>
<p>里面可以有常见的添加、修改、删除、查看按钮，也可以有自定义的其他按钮。可以“弹窗”也可以直接调用后端API。</p>
<ul>
<li>列表</li>
</ul>
<p>显示客户需要的数据，看起来简单，但是要和查询、翻页、添加、修改、删除等功能配合。</p>
<ul>
<li>分页</li>
</ul>
<p>这是和列表最接近的一个需求，因为数据有可能很大，不能一次性都显示出来，那么就需要分页处理，所以分页控件和列表控件就是天然CP。</p>
<ul>
<li>表单（添加、修改）</li>
</ul>
<p>数据提交之后，为了便于确认数据添加成功，是不是需要通知列表去更新数据呢？总不能填完数据，列表一点变化都没有吧。</p>
<ul>
<li>删除</li>
</ul>
<p>数据删掉了，不管是物理删除还是逻辑删除，列表里面都不需要再显示出来了。
也就是说删除后要通知列表更新数据。</p>
<p>总之，各个组件直接需要统筹一下状态关系。</p>
<h1 data-id="heading-3">视频演示</h1>
<p>我们来看一下实际效果。
【放视频】</p>
<h1 data-id="heading-4">设计状态</h1>
<p>我们整理一下需求，用脑图表达出来：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b54cbb771d9483c9278859d850c33f3~tplv-k3u1fbpfcp-zoom-1.image" alt="后台管的状态.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">使用“轻量级状态管理”定义状态：</h1>
<p>/store-ds/index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> VuexDataState <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> VuexDataState.createStore(&#123;
  <span class="hljs-attr">global</span>: &#123; <span class="hljs-comment">// 全局状态</span>
    <span class="hljs-attr">userOnline</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'jyk'</span> <span class="hljs-comment">//</span>
    &#125;
  &#125;,
  <span class="hljs-attr">local</span>: &#123; <span class="hljs-comment">// 局部状态</span>
    dataListState () &#123; <span class="hljs-comment">// 获取列表数据的状态 dataPagerState</span>
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">query</span>: &#123;&#125;, <span class="hljs-comment">// 查询条件</span>
        <span class="hljs-attr">pager</span>: &#123; <span class="hljs-comment">// 分页参数</span>
          <span class="hljs-attr">pageTotal</span>: <span class="hljs-number">100</span>, <span class="hljs-comment">// 0：需要统计总数；其他：不需要统计总数</span>
          <span class="hljs-attr">pageSize</span>: <span class="hljs-number">5</span>, <span class="hljs-comment">// 一页记录数</span>
          <span class="hljs-attr">pageIndex</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 第几页的数据，从 1  开始</span>
          <span class="hljs-attr">orderBy</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-literal">false</span> &#125; <span class="hljs-comment">// 排序字段</span>
        &#125;,
        <span class="hljs-attr">choice</span>: &#123; <span class="hljs-comment">// 列表里面选择的记录</span>
          <span class="hljs-attr">dataId</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 单选，便于修改和删除</span>
          <span class="hljs-attr">dataIds</span>: [], <span class="hljs-comment">// 多选，便于批量删除</span>
          <span class="hljs-attr">row</span>: &#123;&#125;, <span class="hljs-comment">// 选择的记录数据，仅限于列表里面的。</span>
          <span class="hljs-attr">rows</span>: [] <span class="hljs-comment">// 选择的记录数据，仅限于列表里面的。</span>
        &#125;,
        <span class="hljs-attr">hotkey</span>: <span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-comment">// 处理快捷键的事件，用于操作按钮</span>
        <span class="hljs-attr">reloadFirstPager</span>: <span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-comment">// 重新加载第一页，统计总数（添加后）</span>
        <span class="hljs-attr">reloadCurrentPager</span>: <span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-comment">// 重新加载当前页，不统计总数（修改后）</span>
        <span class="hljs-attr">reloadPager</span>: <span class="hljs-function">() =></span> &#123;&#125; <span class="hljs-comment">// 重新加载当前页，统计总数（删除后）</span>
      &#125;
    &#125; 
  &#125;,
  init (state) &#123;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里没有使用 Vuex，因为我觉得 Vuex 有点臃肿，还是自己做的清爽。
另外，状态里面除了数据之外，还可以有方法（事件总线）。</p>
<h1 data-id="heading-6">组件里面使用轻量级状态的方法</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入状态</span>
<span class="hljs-keyword">import</span> VueDS <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

<span class="hljs-comment">// 访问状态</span>
<span class="hljs-keyword">const</span> &#123; reg, get &#125; = VueDS.useStore()
<span class="hljs-comment">// 父组件注册列表的状态</span>
<span class="hljs-keyword">const</span> state = reg.dataListState()

<span class="hljs-comment">// 子组件里面获取父组件注册的状态</span>
<span class="hljs-keyword">const</span> dataListState = get.dataListState()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>先引入状态，然后在父组件注册（也就是注入）状态，然后在子组件就可以获取状态。
函数名就是 /store-ds/index.js 里面定义的名称。</p>
<p>然后我们还可以仿照 MVC 的 Controllar ，做一个控制类，当然也可以叫做管理类。
叫什么不是重点，重点是实现了什么功能。</p>
<h1 data-id="heading-7">列表的管理类</h1>
<p>我们可以为列表的状态写一个状态的管理类。
这个类是在单独的 js 文件里面，并不需要像 Vuex 那样去设置 action 或者 module。</p>
<p>/control/data-list.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; watch, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">import</span> VueDS <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

<span class="hljs-comment">// 仿后端API</span>
<span class="hljs-keyword">import</span> service <span class="hljs-keyword">from</span> <span class="hljs-string">'../api/dataList-service.js'</span>

<span class="hljs-comment">/**
 * * 数据列表的通用管理类
 * * 注册列表的状态
 * * 关联获取数据的方式
 * * 设置快捷键
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>modeluId 模块ID
 * <span class="hljs-doctag">@returns </span>列表状态管理类
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dataListControl</span> (<span class="hljs-params">modeluId</span>) </span>&#123;
  <span class="hljs-comment">// 显示数据列表的数组</span>
  <span class="hljs-keyword">const</span> dataList = reactive([])
  <span class="hljs-comment">// 模拟后端API</span>
  <span class="hljs-keyword">const</span> &#123; loadDataList &#125; = service()

  <span class="hljs-comment">// 访问状态</span>
  <span class="hljs-keyword">const</span> &#123; reg, get &#125; = VueDS.useStore()
  <span class="hljs-comment">// 子组件里面获取父组件注册的状态</span>
  <span class="hljs-keyword">const</span> dataListState = get.dataListState()

  <span class="hljs-comment">// 数据加载中</span>
  <span class="hljs-keyword">let</span> isLoading = <span class="hljs-literal">false</span>

  <span class="hljs-comment">/**
   * 父组件注册状态
   * <span class="hljs-doctag">@returns </span>注册列表状态
   */</span>
  <span class="hljs-keyword">const</span> regDataListState = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 注册列表的状态，用于分页、查询、添加、修改、删除等</span>
    <span class="hljs-keyword">const</span> state = reg.dataListState()

    <span class="hljs-comment">//  重新加载第一页，统计总数（添加、查询后）</span>
    state.reloadFirstPager = <span class="hljs-function">() =></span> &#123;
      isLoading = <span class="hljs-literal">true</span>
      state.pager.pageIndex = <span class="hljs-number">1</span> <span class="hljs-comment">// 显示第一页</span>
   
      <span class="hljs-comment">// 获取数据</span>
      loadDataList(modeluId, state.pager, state.query, <span class="hljs-literal">true</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        state.pager.pageTotal = data.count
        dataList.length = <span class="hljs-number">0</span>
        dataList.push(...data.list)
        isLoading = <span class="hljs-literal">false</span>
      &#125;)
    &#125;
    <span class="hljs-comment">// 先执行一下，获取初始数据</span>
    state.reloadFirstPager()

    <span class="hljs-comment">// 重新加载当前页，不统计总数（修改后）</span>
    state.reloadCurrentPager = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 获取数据</span>
      loadDataList(modeluId, state.pager, state.query).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        dataList.length = <span class="hljs-number">0</span>
        dataList.push(...data)
      &#125;)
    &#125;

    <span class="hljs-comment">// 重新加载当前页，统计总数（删除后）</span>
    state.reloadPager = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 获取数据</span>
      loadDataList(modeluId, state.pager, state.query, <span class="hljs-literal">true</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        state.pager.pageTotal = data.count
        dataList.length = <span class="hljs-number">0</span>
        dataList.push(...data.list)
      &#125;)
    &#125;

    <span class="hljs-comment">// 监听，用于翻页控件的翻页。翻页，获取指定页号的数据</span>
    watch(<span class="hljs-function">() =></span> state.pager.pageIndex, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 避免重复加载</span>
      <span class="hljs-keyword">if</span> (isLoading) &#123;
        <span class="hljs-comment">// 不获取数据</span>
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 获取数据</span>
      loadDataList(modeluId, state.pager, state.query).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        dataList.length = <span class="hljs-number">0</span>
        dataList.push(...data)
      &#125;)
    &#125;)

    <span class="hljs-keyword">return</span> state
  &#125;
 
  <span class="hljs-keyword">return</span> &#123;
    setHotkey, <span class="hljs-comment">// 设置快捷键，（后面介绍）</span>
    regDataListState, <span class="hljs-comment">// 父组件注册状态</span>
    dataList, <span class="hljs-comment">// 父组件获得列表</span>
    dataListState <span class="hljs-comment">// 子组件获得状态</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">管理类的功能：</h2>
<ol>
<li>父组件注册状态</li>
<li>子组件获取状态</li>
<li>定义列表数据的容器</li>
<li>各种监听</li>
<li>事件总线</li>
</ol>
<h3 data-id="heading-9">父组件注册状态</h3>
<p>因为使用的是局部的状态，并不是全局状态，所以在需要使用的时候，首先需要在父组件里面注册一下。看起来似乎没有全局状态简单，但是可以更好的实现复用，更轻松的区分数据，兄弟组件的状态不会混淆。</p>
<h3 data-id="heading-10">子组件获取状态</h3>
<p>因为或者状态必须在vue的直接函数内才行，所以才需要先把状态获取出来，而不能等到触发事件了再获取。</p>
<h3 data-id="heading-11">定义列表数据的容器</h3>
<p>列表数据并没有在状态里面定义，而是在管理类里面定义的，因为主要列表组件才需要这个列表数据，其他的组件并不关心列表数据。</p>
<h3 data-id="heading-12">监听：</h3>
<ul>
<li>监听页号的变化，依据当前的查询条件获取新的记录，用于翻页，不用重新统计总数。</li>
</ul>
<h3 data-id="heading-13">事件：</h3>
<ul>
<li>统计总数并且翻到第一页，用于查询条件变化，添加新记录。</li>
<li>重新获取当前页号的列表数据，用于修改数据后的更新。</li>
<li>重新获取当前页号的列表数据，并且统计总记录数，用于删除数据后的更新。</li>
</ul>
<h3 data-id="heading-14">是否重新统计总数</h3>
<p>可能你会发现上面获取数据里面有一个明显的区别，那就是是否需要统计总数。
在数据量非常大的情况下，如果每次翻页都重新统计总数，那么会严重影响性能！
其实仔细考虑一下，一些情况是不用重新统计总数的，比如翻页、修改后的更新等，这些操作都不会影响总记录数（不考虑并发操作），那么我们也就不必每次都重新统计。</p>
<h1 data-id="heading-15">文件结构</h1>
<p>基础功能搭建好了之后，剩下的就简单了，建立组件设置模板、控件、组件和使用状态即可。
总体结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b07f1d71b2a43469b34eafe63eb03de~tplv-k3u1fbpfcp-zoom-1.image" alt="文件结构" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-16">列表状态的使用</h1>
<p>基础工作做好之后我们来看看，在各个组件里面是如何使用状态的。</p>
<h2 data-id="heading-17">查询</h2>
<p>首先看看查询，用户设置查询条件后，查询控件把查询条件记入状态里面。
然后调用状态管理里的 reloadFirstPager ，获取列表数据。
查询控件支持防抖功能。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!--查询--></span>
  <span class="hljs-tag"><<span class="hljs-name">nf-el-find</span>
    <span class="hljs-attr">v-model</span>=<span class="hljs-string">"listState.query"</span>
    <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"findProps"</span>
    @<span class="hljs-attr">my-change</span>=<span class="hljs-string">"myChange"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接使用查询控件，模板内容是不是很简单了？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 加载json</span>
<span class="hljs-keyword">import</span> loadJson <span class="hljs-keyword">from</span> <span class="hljs-string">'./control/loadjson.js'</span>
<span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">import</span> VueDS <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

  <span class="hljs-comment">// 组件</span>
  <span class="hljs-keyword">import</span> nfElFind <span class="hljs-keyword">from</span> <span class="hljs-string">'/ctrl/nf-el-find/el-find-div.vue'</span>

  <span class="hljs-comment">// 属性：模块ID、查询条件</span>
  <span class="hljs-keyword">const</span> props = defineProps(&#123;
    <span class="hljs-attr">moduleId</span>:  [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">String</span>]
  &#125;)

  <span class="hljs-comment">// 设置 查询的 meta</span>
  <span class="hljs-keyword">const</span> findProps = reactive(&#123;<span class="hljs-attr">reload</span>: <span class="hljs-literal">true</span>&#125;)
  loadJson(props.moduleId, <span class="hljs-string">'find'</span>, findProps)

  <span class="hljs-comment">// 访问状态</span>
  <span class="hljs-keyword">const</span> &#123; get &#125; = VueDS.useStore()
  <span class="hljs-comment">// 获取状态</span>
  <span class="hljs-keyword">const</span> listState = get.dataListState()
  <span class="hljs-comment">// 用户设置查询条件后触发</span>
  <span class="hljs-keyword">const</span> myChange = <span class="hljs-function">(<span class="hljs-params">query</span>) =></span> &#123;
    <span class="hljs-comment">// 获取第一页的数据，并且重新统计总数</span>
    listState.reloadFirstPager()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">分页</h2>
<p>分页就很简单了，查询条件由查询控件搞定，所以这里只需要按照 el-pagination 的要求，把分页状态设置给 el-pagination 的属性即可。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!--分页--></span>
  <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
    <span class="hljs-attr">background</span>
    <span class="hljs-attr">layout</span>=<span class="hljs-string">"prev, pager, next"</span>
    <span class="hljs-attr">v-model:currentPage</span>=<span class="hljs-string">"pager.pageIndex"</span>
    <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"pager.pageSize"</span>
    <span class="hljs-attr">:total</span>=<span class="hljs-string">"pager.pageTotal"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接把状态作为属性值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">import</span> VueDS <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

<span class="hljs-comment">// 访问状态</span>
<span class="hljs-keyword">const</span> &#123; get &#125; = VueDS.useStore()
<span class="hljs-comment">// 获取分页信息</span>
<span class="hljs-keyword">const</span> pager = get.dataListState().pager
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接获取分页状态设置 el-pagination 的属性即可。
翻页的时候 el-pagination 会自动修改 pager.pageIndex 的值，而状态管理里面会监听其变化，然后获取对应的列表数据。</p>
<h2 data-id="heading-19">添加、修改</h2>
<p>添加完成之后，总记录数会增加，所以需要重新统计总记录数，然后翻到第一页。
而修改之后，一般总记录数并不会变化，所以只需要重新获取当前页号的数据即可。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--表单--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-form</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"formControl"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"model"</span>
      <span class="hljs-attr">:partModel</span>=<span class="hljs-string">"partModel"</span>
      <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"formProps"</span>
    ></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">""</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"mysubmit"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用表单控件和两个按钮。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; computed, reactive, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; ElMessage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>
<span class="hljs-comment">// 加载json</span>
<span class="hljs-keyword">import</span> loadJson <span class="hljs-keyword">from</span> <span class="hljs-string">'./control/loadjson.js'</span>

<span class="hljs-comment">// 状态</span>
<span class="hljs-keyword">import</span> VueDS <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-data-state'</span>

<span class="hljs-comment">// 仿后端API</span>
<span class="hljs-keyword">import</span> service <span class="hljs-keyword">from</span> <span class="hljs-string">'./api/data-service.js'</span>
 
  <span class="hljs-comment">// 表单组件</span>
  <span class="hljs-keyword">import</span> elForm <span class="hljs-keyword">from</span> <span class="hljs-string">'/ctrl/nf-el-form/el-form-div.vue'</span>

  <span class="hljs-comment">// 访问状态</span>
  <span class="hljs-keyword">const</span> &#123; get &#125; = VueDS.useStore()

  <span class="hljs-comment">// 定义属性</span>
  <span class="hljs-keyword">const</span> props = defineProps(&#123;
    <span class="hljs-attr">moduleId</span>:  [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">String</span>], <span class="hljs-comment">// 模块ID</span>
    <span class="hljs-attr">formMetaId</span>:  [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">String</span>], <span class="hljs-comment">// 表单的ID</span>
    <span class="hljs-attr">dataId</span>: <span class="hljs-built_in">Number</span>, <span class="hljs-comment">// 修改或者显示的记录的ID</span>
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span> <span class="hljs-comment">// 类型：添加、修改、查看</span>
  &#125;)

  <span class="hljs-comment">// 模块ID + 表单ID = 自己的标志</span>
  <span class="hljs-keyword">const</span> modFormId = computed(<span class="hljs-function">() =></span> props.moduleId + props.formMetaId)

  <span class="hljs-comment">// 子组件里面获取状态</span>
  <span class="hljs-keyword">const</span> dataListState = get.dataListState(modFormId.value)
  
  <span class="hljs-comment">// 表单控件的 model</span>
  <span class="hljs-keyword">const</span> model = reactive(&#123;&#125;)
  
  <span class="hljs-comment">// 表单控件需要的属性</span>
  <span class="hljs-keyword">const</span> formProps = reactive(&#123;<span class="hljs-attr">reload</span>:<span class="hljs-literal">false</span>&#125;)
  <span class="hljs-comment">// 加载需要的 json</span>
  loadJson(props.moduleId, <span class="hljs-string">'form_'</span> + props.formMetaId,  formProps)
  
  <span class="hljs-comment">// 仿后端API</span>
  <span class="hljs-keyword">const</span> &#123; getData, addData, updateData &#125; = service(modFormId.value)

  <span class="hljs-comment">// 监听记录ID的变化，加载数据便于修改</span>
  watch(<span class="hljs-function">() =></span> props.dataId, <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (props.type !== <span class="hljs-string">'add'</span>) &#123;
      <span class="hljs-comment">// 加载数据</span>
      getData( id ).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
        <span class="hljs-built_in">Object</span>.assign(model, data[<span class="hljs-number">0</span>])
        formProps.reload = !formProps.reload
      &#125;)
    &#125;
  &#125;,
  &#123;<span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span>&#125;)

  <span class="hljs-comment">// 提交数据</span>
  <span class="hljs-keyword">const</span> mysubmit = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 判断是添加还是修改</span>
    <span class="hljs-keyword">if</span> (props.type === <span class="hljs-string">'add'</span>)&#123;
      <span class="hljs-comment">// 添加数据</span>
      addData(model).then(<span class="hljs-function">() =></span> &#123;
        ElMessage(&#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'添加数据成功!'</span>
        &#125;)
        <span class="hljs-comment">// 重新加载第一页的数据</span>
        dataListState.reloadFirstPager()
      &#125;)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (props.type === <span class="hljs-string">'update'</span>) &#123;
      <span class="hljs-comment">// 修改数据</span>
      updateData(model, props.dataId).then(<span class="hljs-function">() =></span> &#123;
        ElMessage(&#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'修改数据成功!'</span>
        &#125;)
        <span class="hljs-comment">// 重新加载当前页号的数据</span>
        dataListState.reloadCurrentPager()
      &#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码稍微多了一些，基本上就是在合适的时机调用状态里的重新加载数据的事件。</p>
<h2 data-id="heading-20">删除</h2>
<p>删除之后也会影响总记录数，所以需要重新统计，然后刷新当前页号的列表数据。
删除的代码写在了操作按钮的组件里面，对应删除按钮触发的事件：</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">case</span> <span class="hljs-string">'delete'</span>:
        dialogInfo.show = <span class="hljs-literal">false</span>
        <span class="hljs-comment">// 删除</span>
        ElMessageBox.confirm(<span class="hljs-string">'此操作将删除该记录, 是否继续？'</span>, <span class="hljs-string">'温馨提示'</span>, &#123;
          <span class="hljs-attr">confirmButtonText</span>: <span class="hljs-string">'删除'</span>,
          <span class="hljs-attr">cancelButtonText</span>: <span class="hljs-string">'后悔了'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
        &#125;).then(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 后端API</span>
          <span class="hljs-keyword">const</span> &#123; deleteData &#125; = service(props.moduleId + meta.formMetaId)
          deleteData(dataListState.choice.dataId).then(<span class="hljs-function">() =></span> &#123;
            ElMessage(&#123;
              <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
              <span class="hljs-attr">message</span>: <span class="hljs-string">'删除成功！'</span>
            &#125;)
            dataListState.reloadPager() <span class="hljs-comment">// 刷新列表数据</span>
          &#125;)
        &#125;).catch(<span class="hljs-function">() =></span> &#123;
          ElMessage(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'info'</span>,
            <span class="hljs-attr">message</span>: <span class="hljs-string">'已经取消了。'</span>
          &#125;)
        &#125;)
        <span class="hljs-keyword">break</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除成功之后，调用状态的 dataListState.reloadPager()  刷新列表页面。</p>
<h1 data-id="heading-21">快捷键</h1>
<p>我是喜欢用快捷键实现一些操作的，比如翻页、添加等操作。<br>
用鼠标去找到“上一页”、“下一页”或者需要的页号，这个太麻烦。<br>
如果通过键盘操作就能翻页，是不是可以更方便一些呢？<br>
比如 w、a、s、d，分别表示上一页、下一页、首页、末页；数字键就是要翻到的页号。</p>
<p>是不是有一种打游戏的感觉？<br>
实现方式也比较简单，一开始打算用 Vue 的键盘事件，但是发现似乎不太好用，于是改用监听document 的键盘事件。</p>
<pre><code class="hljs language-js copyable" lang="js">
  <span class="hljs-comment">/**
   * 列表页面的快捷键
   */</span>
  <span class="hljs-keyword">const</span> setHotkey = <span class="hljs-function">(<span class="hljs-params">dataListState</span>) =></span> &#123;
    <span class="hljs-comment">// 设置分页、操作按钮等快捷键</span>
    <span class="hljs-comment">// 计时器做一个防抖</span>
    <span class="hljs-keyword">let</span> timeout
    <span class="hljs-keyword">let</span> tmpIndex = <span class="hljs-number">0</span> <span class="hljs-comment">// 页号</span>
    <span class="hljs-built_in">document</span>.onkeydown = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!(e.target <span class="hljs-keyword">instanceof</span> HTMLBodyElement)) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 表单触发，退出</span>
      <span class="hljs-keyword">if</span> (e.altKey) &#123;
        <span class="hljs-comment">// alt + 的快捷键，调用操作按钮的事件</span>
        dataListState.hotkey(e.key)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 翻页</span>
        <span class="hljs-keyword">const</span> maxPager = <span class="hljs-built_in">parseInt</span>(dataListState.pager.pageTotal / dataListState.pager.pageSize) + <span class="hljs-number">1</span>
        <span class="hljs-keyword">switch</span> (e.key) &#123;
          <span class="hljs-keyword">case</span> <span class="hljs-string">'ArrowLeft'</span>: <span class="hljs-comment">// 左箭头 上一页</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'PageUp'</span>:
          <span class="hljs-keyword">case</span> <span class="hljs-string">'a'</span>:
            dataListState.pager.pageIndex -= <span class="hljs-number">1</span>
            <span class="hljs-keyword">if</span> (dataListState.pager.pageIndex <= <span class="hljs-number">0</span>) &#123;
              dataListState.pager.pageIndex = <span class="hljs-number">1</span>
            &#125;
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'ArrowRight'</span>: <span class="hljs-comment">// 右箭头 下一页</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'PageDown'</span>:
          <span class="hljs-keyword">case</span> <span class="hljs-string">'d'</span>:
            dataListState.pager.pageIndex += <span class="hljs-number">1</span>
            <span class="hljs-keyword">if</span> (dataListState.pager.pageIndex >= maxPager) &#123;
              dataListState.pager.pageIndex = maxPager
            &#125;
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'ArrowUp'</span>: <span class="hljs-comment">// 上箭头</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'Home'</span>: <span class="hljs-comment">// 首页</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'w'</span>:
            dataListState.pager.pageIndex = <span class="hljs-number">1</span>
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'ArrowDown'</span>: <span class="hljs-comment">// 下箭头</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'End'</span>: <span class="hljs-comment">// 末页</span>
          <span class="hljs-keyword">case</span> <span class="hljs-string">'s'</span>:
            dataListState.pager.pageIndex = maxPager
            <span class="hljs-keyword">break</span>
          <span class="hljs-attr">default</span>:
            <span class="hljs-comment">// 判断是不是数字</span>
            <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">isNaN</span>(<span class="hljs-built_in">parseInt</span>(e.key))) &#123;
              <span class="hljs-comment">// 做一个防抖</span>
              tmpIndex = tmpIndex * <span class="hljs-number">10</span> + <span class="hljs-built_in">parseInt</span>(e.key)
              <span class="hljs-built_in">clearTimeout</span>(timeout) <span class="hljs-comment">// 清掉上一次的计时</span>
              timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// 修改 modelValue 属性</span>
                <span class="hljs-keyword">if</span> (tmpIndex === <span class="hljs-number">0</span>) &#123;
                  dataListState.pager.pageIndex = <span class="hljs-number">10</span>
                &#125; <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-keyword">if</span> (tmpIndex >= maxPager) &#123;
                    tmpIndex = maxPager
                  &#125;
                  dataListState.pager.pageIndex = tmpIndex
                &#125;
                tmpIndex = <span class="hljs-number">0</span>
              &#125;, <span class="hljs-number">500</span>)
            &#125;
        &#125;
      &#125;
      e.stopPropagation()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码，其实是放在状态管理类里面的，拿出来单独介绍一下，避免混淆。</p>
<ul>
<li>document.onkeydown</li>
</ul>
<p>监听键盘按下的事件，这个 e 并不是原生的 e，而是Vue封装之后的 e。
首先要判断一下事件来源，如果是 input 等触发的需要跳过，以免影响正常的数据输入。
然后是判断按了哪个按键，根据需求调用对应的函数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fe7d78a340448d88fcc96ad5423fa35~tplv-k3u1fbpfcp-zoom-1.image" alt=" e 的样子 " loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>altKey</li>
</ul>
<p>是否按下了 alt 键。有些快捷键可以是组合方式，本来想用 ctrl 键的，但是发现在网页里面 ctrl 开头的快捷键实在太多，抢不过，所以只好 用 alt。</p>
<ul>
<li>alt + a 相当于按 添加按钮</li>
<li>alt + s 相当于按 修改按钮</li>
<li>alt + d 相当于按 删除按钮</li>
</ul>
<p>你觉得 a 代表 add，d 代表 delete吗？
其实不是的，a、s、d 的键位可以对应操作按钮里面前三个按钮。就酱。</p>
<ul>
<li>数字翻页的防抖</li>
</ul>
<p>如果不做防抖的话，只能实现 1-9 的页号翻页，如果做了防抖的话，基本可以做到三位数页号的翻页。所以手欠做了个防抖。</p>
<h1 data-id="heading-22">开源</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fnaturefw%2Fnf-vite2-element" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/naturefw/nf-vite2-element" ref="nofollow noopener noreferrer">gitee.com/naturefw/nf…</a></p>
<h1 data-id="heading-23">在线演示</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnaturefw.gitee.io%2Fnf-vue-cdn%2Felecontrol%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://naturefw.gitee.io/nf-vue-cdn/elecontrol/" ref="nofollow noopener noreferrer">naturefw.gitee.io/nf-vue-cdn/…</a></p>
<p>nf-vite2-element 的仓库没来得及开通pager服务，所以放在另一个仓库里面了。</p></div>  
</div>
            