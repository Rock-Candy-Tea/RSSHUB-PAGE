
---
title: 'Flutter _ Slivers 系列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39146293f6524b2caab4b3938299a538~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 01:58:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39146293f6524b2caab4b3938299a538~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">概述</h3>
<p>CustomScrollView：一个滚动的容器，改组件不接受任何 child，但是你可以直接提供 <code>Slivers</code> 已创建各种滚动效果，<strong>例如页面中有多个可滑动的列表，如 Appbar， 列表，网格</strong>，等这种就可以直接使用 <code>SliverAppBar</code>,<code>SliverList</code> 和 <code>SliverGrid</code></p>
<p>Slivers 不是单独指一个组件，而是指的一个系列，所以以 Sliver 开头的组件都是这个系列的，但是他们都只能作用于 <code>CustomScrollView</code> 中。</p>
<p>常用到的 Sliver 有，SliverAppbar，SliverList，SliverGrid，SliverToBoxAdapter 等</p>
<blockquote>
<p>由于 CustomScrollView 的子组件只能是 Sliver 系列，如果要将一个普通的组件放在里面，必须使用 <code>SliverToBoxAdapter</code> 进行适配才行</p>
</blockquote>
<h3 data-id="heading-1">简单的使用</h3>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      drawer: Drawer(),
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            title: Text(<span class="hljs-string">"SliverAppbar"</span>),
          ),
          SliverGrid(
            gridDelegate:
                SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: <span class="hljs-number">4</span>),
            delegate: SliverChildBuilderDelegate((context, index) &#123;
              <span class="hljs-keyword">return</span> Container(
                  color: Colors.primaries[index % Colors.primaries.length]);
            &#125;, childCount: <span class="hljs-number">40</span>),
          ),
          SliverList(
              delegate: SliverChildBuilderDelegate((context, index) &#123;
            <span class="hljs-keyword">return</span> Container(
                height: <span class="hljs-number">100</span>,
                color: Colors.primaries[index % Colors.primaries.length]);
          &#125;, childCount: <span class="hljs-number">20</span>))
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果如下：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39146293f6524b2caab4b3938299a538~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
<p>其实我们仔细一点就会发现，其实 ListView 和 GridView 等组件内部使用的都是 Slivers，</p>
<pre><code class="hljs language-dart copyable" lang="dart">ListView.builder(&#123;
 <span class="hljs-comment">//......</span>
&#125;) : <span class="hljs-keyword">assert</span>(itemCount == <span class="hljs-keyword">null</span> || itemCount >= <span class="hljs-number">0</span>),
     <span class="hljs-keyword">assert</span>(semanticChildCount == <span class="hljs-keyword">null</span> || semanticChildCount <= itemCount!),
     childrenDelegate = SliverChildBuilderDelegate(
       itemBuilder,
       childCount: itemCount,
       addAutomaticKeepAlives: addAutomaticKeepAlives,
       addRepaintBoundaries: addRepaintBoundaries,
       addSemanticIndexes: addSemanticIndexes,
     ),
     <span class="hljs-keyword">super</span>(
 <span class="hljs-comment">//....</span>
     );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那为什么要使用 Slivers 呢？最主要的原因就是可以在 slives 中添加多个组件，如在列表的上面和下面添加更多的内容。</p>
<p>并且 slivers 中，<strong>如果存在多个列表的话也是支持动态加载的</strong>，而不是会一次性全部渲染完</p>
<hr>
<h3 data-id="heading-2">各式各样的 Slivers 组件</h3>
<h4 data-id="heading-3">SliverList</h4>
<p>在上面的例子中 SliverList 使用的是 <code>SliverChildBuilderDelegate</code> 这个delegate，它可以实现动态加载，当然 SliverList 中也有和 ListView 中一样的非动态加载的delegate，就是<code>SliverChildListDelegate</code></p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverList(
    delegate: SliverChildListDelegate(
  [
    FlutterLogo(size: <span class="hljs-number">100</span>),
    FlutterLogo(size: <span class="hljs-number">100</span>),
    FlutterLogo(size: <span class="hljs-number">100</span>),
  ],
))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般在列表数量较小并且显示内容确定的情况下可以使用次 <code>delegate</code> 。</p>
<h5 data-id="heading-4">SliverFixedExtentList</h5>
<p>面的子元素中的宽高是动态的，需要手动设置高度，并且这种也不利于性能，所以我们可以使用 <code>SliverFixedExtentList</code> 来控制限制子元素的大小：</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverFixedExtentList(
    itemExtent: <span class="hljs-number">100</span>,
    delegate: SliverChildListDelegate(
      [
        FlutterLogo(),
        FlutterLogo(),
        FlutterLogo(),
      ],
    ))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>未限制前：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3dcad95996477b9f6da05349597ba5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810143917248" loading="lazy" referrerpolicy="no-referrer">，限制后：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dd18abb18854c3bab10428723990d18~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810144017236" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">SliverPrototypeExtentList</h5>
<p>一般情况下，只要固定了列表中元素的高度，就可以提升不小的性能，但是在实际的项目中，想要固定元素的高度是非常麻烦的，就算是列表中的元素只有一行文字，也有可能会出现问题，例如直接在系统层面修改字体的大小，这也会导致高度的固定导致渲染出来的效果不尽人意。但是有了 SliverPrototypeExtentList 就简单多了。</p>
<p>在 SliverPrototypeExtentList 中，可以通过 prototypeItem 来传入一个原型，这个原型并不会渲染到屏幕上，在运行的过程中，Flutter 会将原型的尺寸计算出来，之后就会把所有的元素尺寸设置成这个原型的尺寸。</p>
<pre><code class="hljs language-dart copyable" lang="dart">body: DefaultTextStyle(
  style: TextStyle(fontSize: <span class="hljs-number">60</span>, color: Colors.red),
  child: CustomScrollView(
    slivers: [
      SliverPrototypeExtentList(
          prototypeItem: Text(<span class="hljs-string">""</span>),
          delegate: SliverChildListDelegate(
            [
              Text(<span class="hljs-string">"Hello Word"</span>),
              Text(<span class="hljs-string">"Hello Word"</span>),
              Text(<span class="hljs-string">"Hello Word"</span>),
            ],
          )),
    ],
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，子元素的大小都会和 <code>prototypeItem</code> 中元素的大小进行同步，我们和 SliverFixedExtentList 对比看一下效果</p>
<pre><code class="hljs language-dart copyable" lang="dart">body: DefaultTextStyle(
  style: TextStyle(fontSize: <span class="hljs-number">60</span>, color: Colors.red),
  child: CustomScrollView(
    slivers: [
      SliverFixedExtentList(
          itemExtent: <span class="hljs-number">40</span>,
          delegate: SliverChildListDelegate(
            [
              Text(<span class="hljs-string">"Hello Word"</span>),
              Text(<span class="hljs-string">"Hello Word"</span>),
              Text(<span class="hljs-string">"Hello Word"</span>),
            ],
          )),
    ],
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p>使用 prototype：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/570f89456d074566a6a5c98c11be7d40~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810150249268" loading="lazy" referrerpolicy="no-referrer">,使用 fixed：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a6edbb59035471d8f084f04e87ab0c9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810150332297" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看到，尽管高度固定到 40，但是由于 Text 的大小被修改了，所以渲染出来的还是有问题。</p>
<hr>
<h4 data-id="heading-6">SliverFillViewport</h4>
<p>它也接受一个 delegate，支持动态的加载，只不过内部的子元素会占满整个屏幕</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverFillViewport(
    delegate: SliverChildListDelegate([
  Container(color: Colors.red),
  Container(color: Colors.yellow),
  Container(color: Colors.blue),
]))
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e169953673a54baa874a2005f9f9c7d5~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
<hr>
<h4 data-id="heading-7">SliverAppbar</h4>
<p>在 slivers 系列中，SliverAppbar 可以说是使用频率比较高的组件了，SliverAppbar 为应用栏提供了自定义滚动行为，下面我们来看一下</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      drawer: Drawer(),
      body: DefaultTextStyle(
        style: TextStyle(fontSize: <span class="hljs-number">60</span>, color: Colors.red),
        child: CustomScrollView(
          slivers: [
            SliverAppBar(
              title: Text(<span class="hljs-string">"Sliver AppBar"</span>),
            ),
            SliverToBoxAdapter(child: Placeholder()),
            SliverList(
              delegate: SliverChildListDelegate(
                [
                  FlutterLogo(size: <span class="hljs-number">200</span>),
                  FlutterLogo(size: <span class="hljs-number">200</span>),
                  FlutterLogo(size: <span class="hljs-number">200</span>),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是一个磨人的 SliverAppbar，并没有实现任何特殊效果，默认的效果如下：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afc406bfbfaf422b9aa51cc5545159bc~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
<p>可以看到在滑动的过程中，SliverAppbar 被顶上去了，这也是非常正常的。接着我们来看一下都有哪些特殊效果吧</p>
<h5 data-id="heading-8">特殊效果</h5>
<ul>
<li>
<p>floating</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverAppBar(
  title: Text(<span class="hljs-string">"Sliver AppBar"</span>),
  floating: <span class="hljs-keyword">true</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在向下滑动的时候，会首先将 SliveAppbar 显示出来，如下：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41415e3242304bd6a6a280c69a12db9f~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
</li>
<li>
<p>pinned ：一直显示在顶部，无视滑动，这样就和普通的导航栏差不多了。区别就是在滑动的时候 SliveAppbar 的底部会有一点点影子</p>
</li>
<li>
<p>snap：在滑动停止之后，导航会自动全部显示出来，需要注意的是必须搭配 floating 一起使用，如下：</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverAppBar(
  title: Text(<span class="hljs-string">"Sliver AppBar"</span>),
  snap: <span class="hljs-keyword">true</span>,
  floating: <span class="hljs-keyword">true</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/394c192d016248a884148df27fd52142~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
</li>
<li>
<p>flexibleSpace：可展开拉伸的部分</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverAppBar(
  <span class="hljs-comment">// title: Text("Sliver AppBar"),</span>
  expandedHeight: <span class="hljs-number">300</span>,
  stretch: <span class="hljs-keyword">true</span>,
  flexibleSpace: FlexibleSpaceBar(
    background: FlutterLogo(),
    title: Text(<span class="hljs-string">"FlexibleSpaceBar title"</span>),
    collapseMode: CollapseMode.parallax,
    stretchModes: [
      StretchMode.blurBackground,
      StretchMode.zoomBackground,
      StretchMode.fadeTitle,
    ],
  ),
),
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60a09ba68a504225b8e1561fd0d6f8c5~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-9">SliverOpacity</h4>
<p>透明组件，内部接受的是一个 sliver，所以需要用 SliverToAdapter 转一下</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverOpacity(
  opacity: <span class="hljs-number">0.5</span>,
  sliver: SliverToBoxAdapter(
    child: FlutterLogo(
      size: <span class="hljs-number">100</span>,
    ),
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">SliverFillRemaining</h4>
<p>该组件会填满当前页面的剩余空间</p>
<pre><code class="hljs language-dart copyable" lang="dart">SliverFillRemaining(
  hasScrollBody: <span class="hljs-keyword">false</span>,
  child: Center(
    child: CircularProgressIndicator(),
  ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>hasScrollBody ：当前组件中是否有可滚动的组件</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ce075b90a24fb7989ac3596870bde1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810174859170" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-11">案例</h3>
<p>首先看一下实现的效果(由于是 gif 图，所以看起来有一点卡)：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c0ed62b4e844ff480cca16bbfaf146e~tplv-k3u1fbpfcp-watermark.image" alt="345" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>
<p>准备数据</p>
<p>接口来源于网络，仅供学习使用</p>
<pre><code class="copyable">https://h5.48.cn/resource/jsonp/allmembers.php?gid=10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的数据类：</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Member</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> id;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> name;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> team;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> sid;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> gid;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> gname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> sname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> fname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> tname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> pid;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> pname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> nickname;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> company;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> join_day;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> height;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> birth_day;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> star_sign_12;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> star_sign_48;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> speciality;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> hobby;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> experience;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> catch_phrase;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> status;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> ranking;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> tcolor;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> gcolor;

  <span class="hljs-built_in">String</span> <span class="hljs-keyword">get</span> avatarUrl => <span class="hljs-string">"https://www.snh48.com/images/member/zp_<span class="hljs-subst">$id</span>.jpg"</span>;

  Member(
    <span class="hljs-keyword">this</span>.id,
    <span class="hljs-keyword">this</span>.name,
   <span class="hljs-comment">//.....自行添加</span>
  );

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">String</span> toString() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"<span class="hljs-subst">$id</span>  ---  <span class="hljs-subst">$name</span>"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>首页</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_DemoWidgetState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">DemoWidget</span>> </span>&#123;
  <span class="hljs-built_in">List</span><Member> _member = [];

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        title: Text(<span class="hljs-string">"案例"</span>),
      ),
      body: RefreshIndicator(
        onRefresh: () <span class="hljs-keyword">async</span> &#123;
          setState(() => _member.clear());
          <span class="hljs-keyword">final</span> url = <span class="hljs-string">"https://h5.48.cn/resource/jsonp/allmembers.php?gid=10"</span>;
          <span class="hljs-keyword">final</span> res = <span class="hljs-keyword">await</span> http.<span class="hljs-keyword">get</span>(<span class="hljs-built_in">Uri</span>.parse(url));
          <span class="hljs-keyword">if</span> (res.statusCode != <span class="hljs-number">200</span>) <span class="hljs-keyword">throw</span> Error();

          <span class="hljs-keyword">final</span> json = convert.jsonDecode(res.body);
          <span class="hljs-keyword">final</span> members = (json[<span class="hljs-string">"rows"</span>] <span class="hljs-keyword">as</span> <span class="hljs-built_in">List</span>)
              .map((e) => Member(
                    e[<span class="hljs-string">'sid'</span>], e[<span class="hljs-string">"sname"</span>],e[<span class="hljs-string">"tname"</span>], e[<span class="hljs-string">"sid"</span>], e[<span class="hljs-string">"gid"</span>],e[<span class="hljs-string">"gname"</span>],e[<span class="hljs-string">"sname"</span>],e[<span class="hljs-string">"fname"</span>],e[<span class="hljs-string">"tname"</span>],
                    e[<span class="hljs-string">"pid"</span>],e[<span class="hljs-string">"pname"</span>], e[<span class="hljs-string">"nickname"</span>], e[<span class="hljs-string">"company"</span>], e[<span class="hljs-string">"join_day"</span>], e[<span class="hljs-string">"height"</span>],    e[<span class="hljs-string">"birth_day"</span>],
                    e[<span class="hljs-string">"star_sign_12"</span>], e[<span class="hljs-string">"star_sign_48"</span>], e[<span class="hljs-string">"speciality"</span>], e[<span class="hljs-string">"hobby"</span>], e[<span class="hljs-string">"experience"</span>],
                    e[<span class="hljs-string">"catch_phrase"</span>],  e[<span class="hljs-string">"status"</span>], e[<span class="hljs-string">"ranking"</span>], e[<span class="hljs-string">"tcolor"</span>],e[<span class="hljs-string">"gcolor"</span>],
                  ))
              .toList();

          setState(() => _member = members);
        &#125;,
        child: CustomScrollView(
          slivers: [
            SliverToBoxAdapter(),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"SII"</span>, Color(<span class="hljs-number">0xffae86bb</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"SII"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"NII"</span>, Color(<span class="hljs-number">0xff91cdeb</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"NII"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"HII"</span>, Color(<span class="hljs-number">0xffa7b0ba</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"HII"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"预备生"</span>, Color(<span class="hljs-number">0xff91cdeb</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"预备生"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"荣誉毕业生"</span>, Color(<span class="hljs-number">0xff8ed2f5</span>)),
                pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"荣誉毕业生"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"S预备生"</span>, Color(<span class="hljs-number">0xff38b26d</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"S预备生"</span>),
            SliverPersistentHeader(
                delegate: _MyDelegate(<span class="hljs-string">"X"</span>, Color(<span class="hljs-number">0xffa7b0ba</span>)), pinned: <span class="hljs-keyword">true</span>),
            _buildTeamList(<span class="hljs-string">"X"</span>),
          ],
        ),
      ),
    );
  &#125;

  SliverGrid _buildTeamList(<span class="hljs-built_in">String</span> teamName) &#123;
    <span class="hljs-comment">//进行筛选</span>
    <span class="hljs-keyword">final</span> teamMember =
        _member.where((element) => element.team == teamName).toList();
    <span class="hljs-keyword">return</span> SliverGrid(
      delegate: SliverChildBuilderDelegate((context, index) &#123;
        Member m = teamMember[index];
        <span class="hljs-keyword">return</span> InkWell(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              <span class="hljs-comment">//动画</span>
              Hero(
                  tag: m.avatarUrl,
                  child: ClipOval(
                    child: CircleAvatar(
                      child: Image.network(m.avatarUrl),
                      backgroundColor: Colors.white,
                    ),
                  )),
              Text(<span class="hljs-string">"<span class="hljs-subst">$&#123;m.name&#125;</span>"</span>),
            ],
          ),
          onTap: () => Navigator.of(context)
              .push(MaterialPageRoute(builder: (_) => DetailPage(m))),
        );
      &#125;, childCount: teamMember.length),
      gridDelegate:
          SliverGridDelegateWithMaxCrossAxisExtent(maxCrossAxisExtent: <span class="hljs-number">120</span>),
    );
  &#125;
&#125;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyDelegate</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SliverPersistentHeaderDelegate</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> title;
  <span class="hljs-keyword">final</span> Color color;

  _MyDelegate(<span class="hljs-keyword">this</span>.title, <span class="hljs-keyword">this</span>.color);

  <span class="hljs-meta">@override</span>
  Widget build(
      BuildContext context, <span class="hljs-built_in">double</span> shrinkOffset, <span class="hljs-built_in">bool</span> overlapsContent) &#123;
    <span class="hljs-keyword">return</span> Container(
      height: <span class="hljs-number">35</span>,
      child: FittedBox(child: Text(title, style: TextStyle())),
      color: color,
    );
  &#125;

  <span class="hljs-comment">///<span class="markdown">最高高度</span></span>
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> maxExtent => <span class="hljs-number">35</span>;

  <span class="hljs-comment">///<span class="markdown">最新高度</span></span>
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> minExtent => <span class="hljs-number">35</span>;

  <span class="hljs-comment">///<span class="markdown">重绘</span></span>
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> shouldRebuild(<span class="hljs-keyword">covariant</span> _MyDelegate oldDelegate) &#123;
    <span class="hljs-comment">//如果 title 不相等，则重绘</span>
    <span class="hljs-keyword">return</span> oldDelegate.title != title;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码在  refresh 中进行了网络请求，然后进行解析数据，最后进行了刷新操作</p>
<p>上面代码都很简单，不太熟悉的可能就是 <code>SliverPersistentHeader</code> 了，这是一个可以置顶的 header，它可以出现在视图的任何一个位置， <code>pinned</code> 和 <code>floating</code> 属性用来控制收起是是否展示，具体意思和 SliverAppbar 中一样。</p>
</li>
<li>
<p>详情页面</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DetailPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">final</span> Member member;

  DetailPage(<span class="hljs-keyword">this</span>.member);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Scaffold(
        body: CustomScrollView(
      slivers: [
        SliverAppBar(
            expandedHeight: <span class="hljs-number">300</span>,
            pinned: <span class="hljs-keyword">true</span>,
            stretch: <span class="hljs-keyword">true</span>,
            flexibleSpace: FlexibleSpaceBar(
              centerTitle: <span class="hljs-keyword">true</span>,
              title: Text(<span class="hljs-string">"<span class="hljs-subst">$&#123;member.name&#125;</span>"</span>),
              background: Center(
                child: Padding(
                  padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">100</span>),
                  <span class="hljs-comment">//长宽比</span>
                  child: AspectRatio(
                    aspectRatio: <span class="hljs-number">1</span>,
                     <span class="hljs-comment">// 和上面那个页面的动画对应，tag 必须一致</span>
                    child: Hero(
                      tag: member.avatarUrl,
                      child: Material(
                        elevation: <span class="hljs-number">4.0</span>,
                        shape: CircleBorder(),
                        child: ClipOval(
                          child: Image.network(
                            member.avatarUrl,
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            )),
        SliverList(
            delegate: SliverChildListDelegate(
          [
            _buildInfo(<span class="hljs-string">"战队："</span>, member.team),
            _buildInfo(<span class="hljs-string">"公司："</span>, member.company),
            _buildInfo(<span class="hljs-string">"时间："</span>, member.join_day),
            _buildInfo(<span class="hljs-string">"身高："</span>, member.height),
            _buildInfo(<span class="hljs-string">"生日："</span>, member.birth_day),
            _buildInfo(<span class="hljs-string">"星座："</span>, member.star_sign_12),
            _buildInfo(<span class="hljs-string">"运势："</span>, member.star_sign_48),
            _buildInfo(<span class="hljs-string">"爱好："</span>, member.speciality),
            _buildInfo(<span class="hljs-string">"签名："</span>, member.catch_phrase),
          ],
        ))
      ],
    ));
  &#125;

  _buildInfo(<span class="hljs-built_in">String</span> label, <span class="hljs-built_in">String</span> content) &#123;
    <span class="hljs-keyword">return</span> Card(
      child: Padding(
        padding: EdgeInsets.symmetric(vertical: <span class="hljs-number">25</span>),
        child: Row(
          children: [Text(label), Text(content)],
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中有一个问题，本来使用了  <code>stretch</code> 属性之后，在下拉的时候应该会有一个放大的效果，但是运行代码的时候并没有，有知道原因的同学可以讲一下</p>
</li>
</ul>
<hr>
<blockquote>
<p>参考：B站王叔不秃</p>
</blockquote>
<blockquote>
<p>如果本文有帮助到你的地方，不胜荣幸，如有文章中有错误和疑问，欢迎大家提出!</p>
</blockquote></div>  
</div>
            