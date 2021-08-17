
---
title: 'Flutter 重识 NestedScrollView'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03ef014ed8a0483d8c1b54baf2c02cc5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 17:19:55 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03ef014ed8a0483d8c1b54baf2c02cc5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fextended_nested_scroll_view" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/extended_nested_scroll_view" ref="nofollow noopener noreferrer">extended_nested_scroll_view</a> 是我的第一个上传到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_nested_scroll_view" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_nested_scroll_view" ref="nofollow noopener noreferrer">pub.dev</a> 的 Flutter 组件.</p>
<p>一晃眼都快3年了，经历了43个版本迭代，功能稳定，代码与官方同步。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03ef014ed8a0483d8c1b54baf2c02cc5~tplv-k3u1fbpfcp-watermark.image" alt="8C0553A1-5925-4E77-BF3B-3C771531B9B6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而我最近一直筹备着对其进行重构。怎么说了，接触 Flutter 3年了，认知也与当初有所不同。我相信自己如果现在再面对 <code>NestedScrollView</code> 的问题，我应该能处理地更好。</p>
<p>注意： 后面用到的 <code>SliverPinnedToBoxAdapter</code> 是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_sliver" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_sliver" ref="nofollow noopener noreferrer">extended_sliver</a>里面一个组件，你把它当作 <code>SliverPersistentHeader</code>( Pinned 为 true，minExtent = maxExtent) 就好了。</p>
<h2 data-id="heading-1">NestedScrollView 是什么</h2>
<blockquote>
<p>A scrolling view inside of which can be nested other scrolling views, with their scroll positions being intrinsically linked.</p>
</blockquote>
<p>将外部滚动(Header部分)和内部滚动(Body部分)联动起来。里面滚动不了，滚动外面。外面滚动没了，滚动里面。那么 <code>NestedScrollView</code> 是如何做到的呢？</p>
<p><code>NestedScrollView</code> 其实是一个 <code>CustomScrollView</code>, 下面为伪代码。</p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
      controller: outerController,
      slivers: [
       ...<Widget>[Header1,Header2],
      SliverFillRemaining()(
        child: PrimaryScrollController(
          controller: innerController,
          child: body,
        ),
      ),
      ],
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>outerController 是 <code>CustomScrollView</code> 的 <code>controller</code>， 从层级上看，就是外部</li>
<li>这里使用了 <code>PrimaryScrollController</code> ，那么 <code>body</code> 里面的任何滚动组件，在不自定义 <code>controller</code> 的情况下，都将公用 <code>innerController</code>。</li>
</ul>
<p>至于为什么会这样，首先看一下每个滚动组件都有的属性 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscroll_view.dart%23L111" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scroll_view.dart#L111" ref="nofollow noopener noreferrer">primary</a>，如果 controller 为 null ，并且是竖直方法，就默认为 true 。</p>
<p><code>primary = primary ?? controller == null && identical(scrollDirection, Axis.vertical),</code></p>
<p>然后 在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscroll_view.dart%23L392" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scroll_view.dart#L392" ref="nofollow noopener noreferrer">scroll_view.dart</a> 中，如果 <code>primary</code> 为 true，就去获取 <code>PrimaryScrollController</code> 的 controller。</p>
<pre><code class="hljs language-dart copyable" lang="dart">    <span class="hljs-keyword">final</span> ScrollController? scrollController =
        primary ? PrimaryScrollController.of(context) : controller;
    <span class="hljs-keyword">final</span> Scrollable scrollable = Scrollable(
      dragStartBehavior: dragStartBehavior,
      axisDirection: axisDirection,
      controller: scrollController,
      physics: physics,
      scrollBehavior: scrollBehavior,
      semanticChildCount: semanticChildCount,
      restorationId: restorationId,
      viewportBuilder: (BuildContext context, ViewportOffset offset) &#123;
        <span class="hljs-keyword">return</span> buildViewport(context, offset, axisDirection, slivers);
      &#125;,
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这也解释了为啥有些同学给 body 中的滚动组件设置了 controller，就会发现内外滚动不再联动了。</p>
</blockquote>
<h2 data-id="heading-2">为什么要扩展官方的</h2>
<p>理解了 <code>NestedScrollView</code> 是什么，那我为啥要扩展官方组件呢？</p>
<h3 data-id="heading-3">Header 中包含多个 Pinned Sliver 时候的问题</h3>
<h4 data-id="heading-4">分析</h4>
<p>先看一个图，你觉得列表向上滚动最终的结果是什么？代码在下面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df6e44e5a9ab49f5be96fcf53595676c~tplv-k3u1fbpfcp-watermark.image" alt="AB435C89-515B-4FFC-BACF-96511CC72D51.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
          slivers: <Widget>[
            SliverToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header: 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.yellow.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverPinnedToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header: Pinned 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.red.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header: 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.yellow.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverFillRemaining(
              child: Column(
                children: <span class="hljs-built_in">List</span>.generate(
                    <span class="hljs-number">100</span>,
                    (index) => Container(
                          alignment: Alignment.topCenter,
                          child: Text(<span class="hljs-string">'body: 里面的内容<span class="hljs-subst">$index</span>,高度100'</span>),
                          height: <span class="hljs-number">100</span>,
                          decoration: BoxDecoration(
                              color: Colors.green.withOpacity(<span class="hljs-number">0.4</span>),
                              border: Border.all(
                                color: Colors.black,
                              )),
                        )),
              ),
            )
          ],
        ),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯，没错，列表的第一个 Item 会滚动到 Header1 下面。但实际上，我们通常的需求是需要列表停留在 Header1 底边。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11643805bec54b4e915c72f785d146bd~tplv-k3u1fbpfcp-watermark.image" alt="905DB40E-20D4-43FD-BE71-6C0868DA7093.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Flutter 官方也注意到了这个问题，并且提供了 <code>SliverOverlapAbsorber</code>
<code>SliverOverlapInjector</code> 来处理这个问题，</p>
<ul>
<li><code>SliverOverlapAbsorber</code> 来包裹 <code>Pinned</code> 为 <code>true</code> 的 <code>Sliver</code></li>
<li>在 body 中使用 <code>SliverOverlapInjector</code> 来占位</li>
<li>用 <code>NestedScrollView._absorberHandle</code> 来实现 <code>SliverOverlapAbsorber</code> 和 <code>SliverOverlapInjector</code> 的信息传递。</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">   <span class="hljs-keyword">return</span> Scaffold(
     body: NestedScrollView(
       headerSliverBuilder: (BuildContext context, <span class="hljs-built_in">bool</span> innerBoxIsScrolled) &#123;
         <span class="hljs-keyword">return</span> <Widget>[
           <span class="hljs-comment">// 监听计算高度，并且通过 NestedScrollView._absorberHandle 将</span>
           <span class="hljs-comment">// 自身的高度 告诉 SliverOverlapInjector</span>
           SliverOverlapAbsorber(
             handle: NestedScrollView.sliverOverlapAbsorberHandleFor(context),
             sliver: SliverPinnedToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header: Pinned 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.red.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            )
           )
         ];
       &#125;,
       body: Builder(
         builder: (BuildContext context) &#123;
           <span class="hljs-keyword">return</span> CustomScrollView(
             <span class="hljs-comment">// The "controller" and "primary" members should be left</span>
             <span class="hljs-comment">// unset, so that the NestedScrollView can control this</span>
             <span class="hljs-comment">// inner scroll view.</span>
             <span class="hljs-comment">// If the "controller" property is set, then this scroll</span>
             <span class="hljs-comment">// view will not be associated with the NestedScrollView.</span>
             slivers: <Widget>[
               <span class="hljs-comment">// 占位，接收 SliverOverlapAbsorber 的信息</span>
               SliverOverlapInjector(handle: NestedScrollView.sliverOverlapAbsorberHandleFor(context)),
               SliverFixedExtentList(
                 itemExtent: <span class="hljs-number">48.0</span>,
                 delegate: SliverChildBuilderDelegate(
                     (BuildContext context, <span class="hljs-built_in">int</span> index) => ListTile(title: Text(<span class="hljs-string">'Item <span class="hljs-subst">$index</span>'</span>)),
                   childCount: <span class="hljs-number">30</span>,
                 ),
               ),
             ],
           );
         &#125;
       )
     )
   );
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你觉得这种方法不清楚，那我简化一下，用另外的方式表达。我们也增加一个 100 的占位。不过实际操作中是不可能这样做的，这样会导致初始化的时候列表上方会留下 100 的空位。</p>
<pre><code class="hljs language-dart copyable" lang="dart">   CustomScrollView(
          slivers: <Widget>[
            SliverToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header0: 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.yellow.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverPinnedToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header1: Pinned 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.red.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverToBoxAdapter(
              child: Container(
                alignment: Alignment.center,
                child: Text(<span class="hljs-string">'Header2: 100高度'</span>),
                height: <span class="hljs-number">100</span>,
                color: Colors.yellow.withOpacity(<span class="hljs-number">0.4</span>),
              ),
            ),
            SliverFillRemaining(
              child: Column(
                children: <Widget>[
                  <span class="hljs-comment">// 我相当于 SliverOverlapAbsorber</span>
                  Container(
                    height: <span class="hljs-number">100</span>,
                  ),
                  Column(
                    children: <span class="hljs-built_in">List</span>.generate(
                        <span class="hljs-number">100</span>,
                        (index) => Container(
                              alignment: Alignment.topCenter,
                              child: Text(<span class="hljs-string">'body: 里面的内容<span class="hljs-subst">$index</span>,高度100'</span>),
                              height: <span class="hljs-number">100</span>,
                              decoration: BoxDecoration(
                                  color: Colors.green.withOpacity(<span class="hljs-number">0.4</span>),
                                  border: Border.all(
                                    color: Colors.black,
                                  )),
                            )),
                  ),
                ],
              ),
            )
          ],
        ),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那问题来了，如果 <code>NestedScrollView</code> 的 <code>Header</code> 中包含多个 <code>Pinned</code> 为 <code>true</code> 的 <code>Sliver</code>， 那么 <code>SliverOverlapAbsorber</code> 便无能为力了，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F22393" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/issues/22393" ref="nofollow noopener noreferrer">Issue 传送门</a>。</p>
<h4 data-id="heading-5">解决</h4>
<p>我们再来回顾 <code>NestedScrollView</code> 长什么样子的，可以看出来，这个问题应该跟 <code>outerController</code> 有关系。参照前面简单 demo 来看，只要我们让外部少滚动 100，就可以让列表停留在 Pinned Header1 底部了。</p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
      controller: outerController,
      slivers: [
       ...<Widget>[Header1,Header2],
      SliverFillRemaining()(
        child: PrimaryScrollController(
          controller: innerController,
          child: body,
        ),
      ),
      ],
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">maxScrollExtent</h5>
<p>我们再思考一下，是什么会影响一个滚动组件的滚动最终距离？</p>
<blockquote>
<p>答案是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscroll_position.dart%23L143" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scroll_position.dart#L143" ref="nofollow noopener noreferrer">ScrollPosition.maxScrollExtent</a></p>
</blockquote>
<p>知道了是什么东西影响，我们要做的就是在合适的时候修改这个值，那么如何获取时机呢？</p>
<p>将下面代码</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> maxScrollExtent => _maxScrollExtent!;
  <span class="hljs-built_in">double?</span> _maxScrollExtent;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为以下代码</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> maxScrollExtent => _maxScrollExtent!;
  <span class="hljs-comment">//double? _maxScrollExtent;</span>
  <span class="hljs-built_in">double?</span> __maxScrollExtent;
  <span class="hljs-built_in">double?</span> <span class="hljs-keyword">get</span> _maxScrollExtent => __maxScrollExtent;
  <span class="hljs-keyword">set</span> _maxScrollExtent(<span class="hljs-built_in">double?</span> value) &#123;
    <span class="hljs-keyword">if</span> (__maxScrollExtent != value) &#123;
      __maxScrollExtent = value;
   &#125;
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以在 set 方法里面打上 debug 断点，看看是什么时候 <code>_maxScrollExtent</code> 被赋值的。</p>
<p>运行例子 ，得到以下 <code>Call Stack</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71059fefddd84a44a9e8cc12e7567c86~tplv-k3u1fbpfcp-watermark.image" alt="AEF1EF26-CD2B-40B9-A0EC-B6FC921A00BA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8a71fbe94b44b89ac37b8d387cdfdc3~tplv-k3u1fbpfcp-watermark.image" alt="449A65EF-CCB9-4F44-BECE-556DC94B12E6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这里，我们应该知道，可以通过 override <code>applyContentDimensions</code> 方法，去重新设置 <code>maxScrollExtent</code></p>
<h5 data-id="heading-7">ScrollPosition</h5>
<p>想要 override <code>applyContentDimensions</code> 就要知道 <code>ScrollPosition</code> 在什么时候创建的，继续调试, 把断点打到 <code>ScrollPosition</code> 的构造上面。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f3779af33f43d8a6ee3d32c1f22ed4~tplv-k3u1fbpfcp-watermark.image" alt="3D912727-EDAF-4669-A5C6-342FFB4219F7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
ScrollController.createScrollPosition --> ScrollPositionWithSingleContext --> ScrollPosition
</code></pre>
<p>可以看到如果不是特定的 <code>ScrollPosition</code>，我们平时使用的是默认的
<code>ScrollPositionWithSingleContext</code>，并且在 <code>ScrollController</code> 的 <code>createScrollPosition</code> 方法中创建。</p>
<p>增加下面的代码，并且给 demo 中的 <code>CustomScrollView</code> 添加 <code>controller</code> 为 <code>MyScrollController</code>，我们再次运行 demo，是不是得到了我们想要的效果呢？</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyScrollController</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ScrollController</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  ScrollPosition createScrollPosition(ScrollPhysics physics,
      ScrollContext context, ScrollPosition oldPosition) &#123;
    <span class="hljs-keyword">return</span> MyScrollPosition(
      physics: physics,
      context: context,
      initialPixels: initialScrollOffset,
      keepScrollOffset: keepScrollOffset,
      oldPosition: oldPosition,
      debugLabel: debugLabel,
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyScrollPosition</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ScrollPositionWithSingleContext</span> </span>&#123;
  MyScrollPosition(&#123;
    <span class="hljs-meta">@required</span> ScrollPhysics physics,
    <span class="hljs-meta">@required</span> ScrollContext context,
    <span class="hljs-built_in">double</span> initialPixels = <span class="hljs-number">0.0</span>,
    <span class="hljs-built_in">bool</span> keepScrollOffset = <span class="hljs-keyword">true</span>,
    ScrollPosition oldPosition,
    <span class="hljs-built_in">String</span> debugLabel,
  &#125;) : <span class="hljs-keyword">super</span>(
          physics: physics,
          context: context,
          keepScrollOffset: keepScrollOffset,
          oldPosition: oldPosition,
          debugLabel: debugLabel,
          initialPixels: initialPixels,
        );

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> applyContentDimensions(<span class="hljs-built_in">double</span> minScrollExtent, <span class="hljs-built_in">double</span> maxScrollExtent) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.applyContentDimensions(minScrollExtent, maxScrollExtent - <span class="hljs-number">100</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fnested_scroll_view.dart%23L1352" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/nested_scroll_view.dart#L1352" ref="nofollow noopener noreferrer">_NestedScrollPosition</a></h5>
<p>对应到 <code>NestedScrollView</code> 中，可以为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fnested_scroll_view.dart%23L1352" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/nested_scroll_view.dart#L1352" ref="nofollow noopener noreferrer">_NestedScrollPosition</a> 添加以下的方法。</p>
<p><code>pinnedHeaderSliverHeightBuilder</code> 回调是获取 <code>Header</code> 当中一共有哪些 <code>Pinned</code> 的 <code>Sliver</code>。</p>
<ul>
<li>对于 SliverAppbar 来说，最终固定的高度应该包括 <code>状态栏的高度</code>(MediaQuery.of(context).padding.top) 和 <code>导航栏的高度</code>(kToolbarHeight)</li>
<li>对于 <code>SliverPersistentHeader</code> ( Pinned 为 true )， 最终固定高度应该为 <code>minExtent</code></li>
<li>如果有多个这种 Sliver， 应该为他们最终固定的高度之和。</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> applyContentDimensions(<span class="hljs-built_in">double</span> minScrollExtent, <span class="hljs-built_in">double</span> maxScrollExtent) &#123;
    <span class="hljs-keyword">if</span> (debugLabel == <span class="hljs-string">'outer'</span> &&
        coordinator.pinnedHeaderSliverHeightBuilder != <span class="hljs-keyword">null</span>) &#123;
      maxScrollExtent =
          maxScrollExtent - coordinator.pinnedHeaderSliverHeightBuilder!();
      maxScrollExtent = math.max(<span class="hljs-number">0.0</span>, maxScrollExtent);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.applyContentDimensions(minScrollExtent, maxScrollExtent);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Body 中多列表滚动互相影响的问题</h3>
<p>大家一定有这种需求，在 <code>TabbarView</code> 或者 <code>PageView</code> 中的列表，切换的时候列表的滚动位置要保留。这个使用 <code>AutomaticKeepAliveClientMixin</code>，非常简单。</p>
<p>但是如果把 <code>TabbarView</code> 或者 <code>PageView</code> 放到<code>NestedScrollView</code> 的 <code>body</code> 里面的话，你滚动其中一个列表，也会发现其他的列表也会跟着改变位置。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F21868" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/issues/21868" ref="nofollow noopener noreferrer">Issue 传送门</a></p>
<h4 data-id="heading-10">分析</h4>
<p>先看 <code>NestedScrollView</code> 的伪代码。<code>NestedScrollView</code> 之所以能上内外联动，就是在于 <code>outerController</code> 和 <code>innerController</code> 的联动。</p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
      controller: outerController,
      slivers: [
       ...<Widget>[Header1,Header2],
      SliverFillRemaining()(
        child: PrimaryScrollController(
          controller: innerController,
          child: body,
        ),
      ),
      ],
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>innerController</code> 负责 <code>Body</code>，将 <code>Body</code> 中没有设置过 controller 的列表的 <code>ScrollPosition</code> 通过 <code>attach</code> 方法，加载进来。</p>
<blockquote>
<p>当使用列表缓存的时候，切换 tab 的时候，原列表将不会 <code>dispose</code>，就不会从 controller 中 <code>detach</code> 。  innerController.positions 将不止一个。而 <code>outerController</code> 和 <code>innerController</code> 的联动计算都是基于 positions 来进行的。这就是导致这个问题的原因。</p>
</blockquote>
<p>具体代码体现在
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fnested_scroll_view.dart%23L1135" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/nested_scroll_view.dart#L1135" ref="nofollow noopener noreferrer">github.com/flutter/flu…</a></p>
<pre><code class="hljs language-dart copyable" lang="dart">        <span class="hljs-keyword">if</span> (innerDelta != <span class="hljs-number">0.0</span>) &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> _NestedScrollPosition position <span class="hljs-keyword">in</span> _innerPositions)
            position.applyFullDragUpdate(innerDelta);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">解决</h4>
<blockquote>
<p>不管是3年前还是现在再看这个问题，第一感觉，不就是只要找到当前<code>显示</code>的那个列表，只让它滚动就可以了嘛，不是很简单吗?</p>
</blockquote>
<p>确实，但是那只是看起来觉得简单，毕竟这个 issue 已经 open 3年了。</p>
<h5 data-id="heading-12">老方案</h5>
<ol>
<li>在 <code>ScrollPosition</code> <code>attach</code> 的时候去通过 <code>context</code> 找到这个列表所对应的标志，跟 <code>TabbarView</code> 或者 <code>PageView</code> 的 index 关联进行对比。</li>
</ol>
<p><a href="https://juejin.cn/post/6844903713887223821" target="_blank" title="https://juejin.cn/post/6844903713887223821">Flutter 扩展NestedScrollView （二）列表滚动同步解决 (juejin.cn)</a></p>
<ol start="2">
<li>通过计算列表的相对位置，来确定当前 <code>显示</code> 的列表。</li>
</ol>
<p><a href="https://juejin.cn/post/6844903764168704007" target="_blank" title="https://juejin.cn/post/6844903764168704007">Flutter 你想知道的Widget可视区域,相对位置,大小 (juejin.cn)</a></p>
<p>总体来说，</p>
<ul>
<li>1方案更准确，但是用法比较繁琐。</li>
<li>2方案受动画影响，在一些特殊的情况下会导致计算不正确。</li>
</ul>
<h5 data-id="heading-13">新方案</h5>
<p>首先我们先准备一个的 demo 重现问题。</p>
<pre><code class="hljs language-dart copyable" lang="dart">      NestedScrollView(
        headerSliverBuilder: (
          BuildContext buildContext,
          <span class="hljs-built_in">bool</span> innerBoxIsScrolled,
        ) =>
            <Widget>[
          SliverToBoxAdapter(
            child: Container(
              color: Colors.red,
              height: <span class="hljs-number">200</span>,
            ),
          )
        ],
        body: Column(
          children: [
            Container(
              color: Colors.yellow,
              height: <span class="hljs-number">200</span>,
            ),
            Expanded(
              child: PageView(
                children: <Widget>[
                  ListItem(
                    tag: <span class="hljs-string">'Tab0'</span>,
                  ),
                  ListItem(
                    tag: <span class="hljs-string">'Tab1'</span>,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      
 <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ListItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> ListItem(&#123;
    Key key,
    <span class="hljs-keyword">this</span>.tag,
  &#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> tag;

  <span class="hljs-meta">@override</span>
  _ListItemState createState() => _ListItemState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_ListItemState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">ListItem</span>>
    <span class="hljs-title">with</span> <span class="hljs-title">AutomaticKeepAliveClientMixin</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">super</span>.build(context);
    <span class="hljs-keyword">return</span> ListView.builder(
      itemBuilder: (BuildContext buildContext, <span class="hljs-built_in">int</span> index) =>
          Center(child: Text(<span class="hljs-string">'<span class="hljs-subst">$&#123;widget.tag&#125;</span>---<span class="hljs-subst">$index</span>'</span>)),
      itemCount: <span class="hljs-number">1000</span>,
    );
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> <span class="hljs-keyword">get</span> wantKeepAlive => <span class="hljs-keyword">true</span>;
&#125;         
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">Drag</h6>
<p>现在再看这个问题，我在思考，我自己滚动了哪个列表，我自己不知道？？</p>
<p>看过上一篇 <a href="https://juejin.cn/post/6992507132704882719" target="_blank" title="https://juejin.cn/post/6992507132704882719">Flutter 锁定行列的FlexGrid - 掘金 (juejin.cn)</a> 的小伙伴，应该知道在拖拽列表的时候是会生成一个 <code>Drag</code> 的。那么有这个 <code>Drag</code> 的 <code>ScrollPosition</code> 不就对应正在显示的列表吗？？</p>
<p>具体到代码，我们试试打日志看看，</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fnested_scroll_view.dart%23L1625" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/nested_scroll_view.dart#L1625" ref="nofollow noopener noreferrer">github.com/flutter/flu…</a></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  Drag drag(DragStartDetails details, VoidCallback dragCancelCallback) &#123;
    <span class="hljs-built_in">print</span>(debugLabel);
    <span class="hljs-keyword">return</span> coordinator.drag(details, dragCancelCallback);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d9b9668beda40d18cf114fe8335b861~tplv-k3u1fbpfcp-watermark.image" alt="2F350159-7545-4D81-8720-ABED291428FB.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>理想很好，但是现实是骨感的，不管我是滚动 <code>Header</code> 还是 <code>Body</code> ，都只打印了 <code>outer</code> 。 那意思是 Body 里面的手势全部被吃了？？</p>
<p>不着急，我们打开 <code>DevTools</code> ，看看 <code>ListView</code> 里面的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscrollable.dart%23L384" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scrollable.dart#L384" ref="nofollow noopener noreferrer">ScrollableState</a> 的状态。(具体为啥要看这里面，可以去读读 <a href="https://juejin.cn/post/6994231790198063134" target="_blank" title="https://juejin.cn/post/6994231790198063134">Flutter 锁定行列的 FlexGrid (juejin.cn)</a>)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05eb3f7caf1b409bb85a47f83a9145c9~tplv-k3u1fbpfcp-watermark.image" alt="6D8E3694-613E-4489-AB67-D0773ADD5051.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哈哈，<code>gestures</code> 居然为 <code>none</code>，就是说 <code>Body</code> 里面没有注册手势。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscrollable.dart%23L543" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scrollable.dart#L543" ref="nofollow noopener noreferrer">github.com/flutter/flu…</a> <code>setCanDrag</code> 方法中，我们可以看到只有 <code>canDrag</code> 等于 <code>false</code> 的时候，我们是没有注册手势的。当然也有一种可能，<code>setCanDrag</code> 也许就没有被调用过，默认的 <code>_gestureRecognizers</code> 就是空。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-meta">@protected</span>
  <span class="hljs-keyword">void</span> setCanDrag(<span class="hljs-built_in">bool</span> canDrag) &#123;
    <span class="hljs-keyword">if</span> (canDrag == _lastCanDrag && (!canDrag || widget.axis == _lastAxisDirection))
      <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (!canDrag) &#123;
      _gestureRecognizers = <span class="hljs-keyword">const</span> <<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>&#123;&#125;;
      <span class="hljs-comment">// Cancel the active hold/drag (if any) because the gesture recognizers</span>
      <span class="hljs-comment">// will soon be disposed by our RawGestureDetector, and we won't be</span>
      <span class="hljs-comment">// receiving pointer up events to cancel the hold/drag.</span>
      _handleDragCancel();
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">switch</span> (widget.axis) &#123;
        <span class="hljs-keyword">case</span> Axis.vertical:
          _gestureRecognizers = <<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>&#123;
            VerticalDragGestureRecognizer: GestureRecognizerFactoryWithHandlers<VerticalDragGestureRecognizer>(
              () => VerticalDragGestureRecognizer(),
              (VerticalDragGestureRecognizer instance) &#123;
                instance
                  ..onDown = _handleDragDown
                  ..onStart = _handleDragStart
                  ..onUpdate = _handleDragUpdate
                  ..onEnd = _handleDragEnd
                  ..onCancel = _handleDragCancel
                  ..minFlingDistance = _physics?.minFlingDistance
                  ..minFlingVelocity = _physics?.minFlingVelocity
                  ..maxFlingVelocity = _physics?.maxFlingVelocity
                  ..velocityTrackerBuilder = _configuration.velocityTrackerBuilder(context)
                  ..dragStartBehavior = widget.dragStartBehavior;
              &#125;,
            ),
          &#125;;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Axis.horizontal:
          _gestureRecognizers = <<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>&#123;
            HorizontalDragGestureRecognizer: GestureRecognizerFactoryWithHandlers<HorizontalDragGestureRecognizer>(
              () => HorizontalDragGestureRecognizer(),
              (HorizontalDragGestureRecognizer instance) &#123;
                instance
                  ..onDown = _handleDragDown
                  ..onStart = _handleDragStart
                  ..onUpdate = _handleDragUpdate
                  ..onEnd = _handleDragEnd
                  ..onCancel = _handleDragCancel
                  ..minFlingDistance = _physics?.minFlingDistance
                  ..minFlingVelocity = _physics?.minFlingVelocity
                  ..maxFlingVelocity = _physics?.maxFlingVelocity
                  ..velocityTrackerBuilder = _configuration.velocityTrackerBuilder(context)
                  ..dragStartBehavior = widget.dragStartBehavior;
              &#125;,
            ),
          &#125;;
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
    _lastCanDrag = canDrag;
    _lastAxisDirection = widget.axis;
    <span class="hljs-keyword">if</span> (_gestureDetectorKey.currentState != <span class="hljs-keyword">null</span>)
      _gestureDetectorKey.currentState!.replaceGestureRecognizers(_gestureRecognizers);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在 <code>setCanDrag</code> 方法中打一个断点，看看调用的时机。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71526e412fa4427a8d940398c4596bf0~tplv-k3u1fbpfcp-watermark.image" alt="443ACE15-B343-4B07-98A8-DB00FFCA3AF8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>RenderViewport.performLayout</li>
</ol>
<p>performLayout 方法中计算出当前 <code>ScrollPosition</code> 的最小最大值</p>
<pre><code class="hljs language-dart copyable" lang="dart">     <span class="hljs-keyword">if</span> (offset.applyContentDimensions(
              math.min(<span class="hljs-number">0.0</span>, _minScrollExtent + mainAxisExtent * anchor),
              math.max(<span class="hljs-number">0.0</span>, _maxScrollExtent - mainAxisExtent * (<span class="hljs-number">1.0</span> - anchor)),
           ))
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>ScrollPosition.applyContentDimensions</li>
</ol>
<p>调用 <code>applyNewDimensions</code> 方法</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> applyContentDimensions(<span class="hljs-built_in">double</span> minScrollExtent, <span class="hljs-built_in">double</span> maxScrollExtent) &#123;
    <span class="hljs-keyword">assert</span>(minScrollExtent != <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(maxScrollExtent != <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(haveDimensions == (_lastMetrics != <span class="hljs-keyword">null</span>));
    <span class="hljs-keyword">if</span> (!nearEqual(_minScrollExtent, minScrollExtent, Tolerance.defaultTolerance.distance) ||
        !nearEqual(_maxScrollExtent, maxScrollExtent, Tolerance.defaultTolerance.distance) ||
        _didChangeViewportDimensionOrReceiveCorrection) &#123;
      <span class="hljs-keyword">assert</span>(minScrollExtent != <span class="hljs-keyword">null</span>);
      <span class="hljs-keyword">assert</span>(maxScrollExtent != <span class="hljs-keyword">null</span>);
      <span class="hljs-keyword">assert</span>(minScrollExtent <= maxScrollExtent);
      _minScrollExtent = minScrollExtent;
      _maxScrollExtent = maxScrollExtent;
      <span class="hljs-keyword">final</span> ScrollMetrics? currentMetrics = haveDimensions ? copyWith() : <span class="hljs-keyword">null</span>;
      _didChangeViewportDimensionOrReceiveCorrection = <span class="hljs-keyword">false</span>;
      _pendingDimensions = <span class="hljs-keyword">true</span>;
      <span class="hljs-keyword">if</span> (haveDimensions && !correctForNewDimensions(_lastMetrics!, currentMetrics!)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
      &#125;
      _haveDimensions = <span class="hljs-keyword">true</span>;
    &#125;
    <span class="hljs-keyword">assert</span>(haveDimensions);
    <span class="hljs-keyword">if</span> (_pendingDimensions) &#123;
      applyNewDimensions();
      _pendingDimensions = <span class="hljs-keyword">false</span>;
    &#125;
    <span class="hljs-keyword">assert</span>(!_didChangeViewportDimensionOrReceiveCorrection, <span class="hljs-string">'Use correctForNewDimensions() (and return true) to change the scroll offset during applyContentDimensions().'</span>);
    _lastMetrics = copyWith();
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>ScrollPositionWithSingleContext.applyNewDimensions</li>
</ol>
<p>不特殊定义的话，默认 <code>ScrollPosition</code> 都是 <code>ScrollPositionWithSingleContext</code>。<code>context</code> 是谁呢？
当然是 <code>ScrollableState</code></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> applyNewDimensions() &#123;
    <span class="hljs-keyword">super</span>.applyNewDimensions();  
    context.setCanDrag(physics.shouldAcceptUserOffset(<span class="hljs-keyword">this</span>));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里提了一下，平时有同学问。不满一屏幕的列表  controller 注册不触发 或者 NotificationListener 监听不触发。原因就在这里，physics.shouldAcceptUserOffset(this) 返回的是 <code>false</code>。而我们的处理办法就是 设置 physics  为 <code>AlwaysScrollableScrollPhysics</code>， shouldAcceptUserOffset 放</p>
</blockquote>
<p><code>AlwaysScrollableScrollPhysics</code> 的 <code>shouldAcceptUserOffset</code> 方法永远返回 <code>true</code> 。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AlwaysScrollableScrollPhysics</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ScrollPhysics</span> </span>&#123;
  <span class="hljs-comment">/// <span class="markdown">Creates scroll physics that always lets the user scroll.</span></span>
  <span class="hljs-keyword">const</span> AlwaysScrollableScrollPhysics(&#123; ScrollPhysics? parent &#125;) : <span class="hljs-keyword">super</span>(parent: parent);

  <span class="hljs-meta">@override</span>
  AlwaysScrollableScrollPhysics applyTo(ScrollPhysics? ancestor) &#123;
    <span class="hljs-keyword">return</span> AlwaysScrollableScrollPhysics(parent: buildParent(ancestor));
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">bool</span> shouldAcceptUserOffset(ScrollMetrics position) => <span class="hljs-keyword">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>ScrollableState.setCanDrag</li>
</ol>
<p>最终达到这里，去根据 <code>canDrag</code> 和 <code>axis</code>(水平/垂直)</p>
<h6 data-id="heading-15">_NestedScrollCoordinator</h6>
<p>那接下来，我们就去 <code>NestedScrollView</code> 代码里面找找看。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fnested_scroll_view.dart%23L1612" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/nested_scroll_view.dart#L1612" ref="nofollow noopener noreferrer">github.com/flutter/flu…</a></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> applyNewDimensions() &#123;
    <span class="hljs-keyword">super</span>.applyNewDimensions();
    coordinator.updateCanDrag();
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们看到调用了 <code>coordinator.updateCanDrag()</code>。</p>
<p>首先我们看看 <code>coordinator</code> 是什么？不难看出来，用来协调 <code>outerController</code> 和 <code>innerController</code> 的。</p>
<pre><code class="hljs language-dart copyable" lang="dart">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_NestedScrollCoordinator</span>
    <span class="hljs-keyword">implements</span> <span class="hljs-title">ScrollActivityDelegate</span>, <span class="hljs-title">ScrollHoldController</span> </span>&#123;
  _NestedScrollCoordinator(
    <span class="hljs-keyword">this</span>._state,
    <span class="hljs-keyword">this</span>._parent,
    <span class="hljs-keyword">this</span>._onHasScrolledBodyChanged,
    <span class="hljs-keyword">this</span>._floatHeaderSlivers,
  ) &#123;
    <span class="hljs-keyword">final</span> <span class="hljs-built_in">double</span> initialScrollOffset = _parent?.initialScrollOffset ?? <span class="hljs-number">0.0</span>;
    _outerController = _NestedScrollController(
      <span class="hljs-keyword">this</span>,
      initialScrollOffset: initialScrollOffset,
      debugLabel: <span class="hljs-string">'outer'</span>,
    );
    _innerController = _NestedScrollController(
      <span class="hljs-keyword">this</span>,
      initialScrollOffset: <span class="hljs-number">0.0</span>,
      debugLabel: <span class="hljs-string">'inner'</span>,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们看看 <code>updateCanDrag</code> 方法里面做了什么。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> updateCanDrag() &#123;
    <span class="hljs-keyword">if</span> (!_outerPosition!.haveDimensions) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">double</span> maxInnerExtent = <span class="hljs-number">0.0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> _NestedScrollPosition position <span class="hljs-keyword">in</span> _innerPositions) &#123;
      <span class="hljs-keyword">if</span> (!position.haveDimensions) <span class="hljs-keyword">return</span>;
      maxInnerExtent = math.max(
        maxInnerExtent,
        position.maxScrollExtent - position.minScrollExtent,
      );
    &#125;
    <span class="hljs-comment">// _NestedScrollPosition.updateCanDrag</span>
    _outerPosition!.updateCanDrag(maxInnerExtent);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_NestedScrollPosition.updateCanDrag</code></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> updateCanDrag(<span class="hljs-built_in">double</span> totalExtent) &#123;
    <span class="hljs-comment">// 调用 ScrollableState 的 setCanDrag 方法</span>
    context.setCanDrag(totalExtent > (viewportDimension - maxScrollExtent) ||
        minScrollExtent != maxScrollExtent);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道原因之后，我们试试动手改下。</p>
<ul>
<li>修改 <code>_NestedScrollCoordinator.updateCanDrag</code> 为如下:</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> updateCanDrag(&#123;_NestedScrollPosition? position&#125;) &#123;
    <span class="hljs-built_in">double</span> maxInnerExtent = <span class="hljs-number">0.0</span>;

    <span class="hljs-keyword">if</span> (position != <span class="hljs-keyword">null</span> && position.debugLabel == <span class="hljs-string">'inner'</span>) &#123;
      <span class="hljs-keyword">if</span> (position.haveDimensions) &#123;
        maxInnerExtent = math.max(
          maxInnerExtent,
          position.maxScrollExtent - position.minScrollExtent,
        );
        position.updateCanDrag(maxInnerExtent);
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (!_outerPosition!.haveDimensions) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> _NestedScrollPosition position <span class="hljs-keyword">in</span> _innerPositions) &#123;
      <span class="hljs-keyword">if</span> (!position.haveDimensions) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      maxInnerExtent = math.max(
        maxInnerExtent,
        position.maxScrollExtent - position.minScrollExtent,
      );
    &#125;
    _outerPosition!.updateCanDrag(maxInnerExtent);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改 <code>_NestedScrollPosition.drag</code> 方法为如下:</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-built_in">bool</span> _isActived = <span class="hljs-keyword">false</span>;
  <span class="hljs-meta">@override</span>
  Drag drag(DragStartDetails details, VoidCallback dragCancelCallback) &#123;
    _isActived = <span class="hljs-keyword">true</span>;
    <span class="hljs-keyword">return</span> coordinator.drag(details, () &#123;
      dragCancelCallback();
      _isActived = <span class="hljs-keyword">false</span>;
    &#125;);
  &#125;

  <span class="hljs-comment">/// <span class="markdown">Whether is actived now</span></span>
  <span class="hljs-built_in">bool</span> <span class="hljs-keyword">get</span> isActived &#123;
    <span class="hljs-keyword">return</span> _isActived;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改 <code>_NestedScrollCoordinator._innerPositions</code> 为如下:</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"> <span class="hljs-built_in">Iterable</span><_NestedScrollPosition> <span class="hljs-keyword">get</span> _innerPositions &#123;
    <span class="hljs-keyword">if</span> (_innerController.nestedPositions.length > <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">final</span> <span class="hljs-built_in">Iterable</span><_NestedScrollPosition> actived = _innerController
          .nestedPositions
          .where((_NestedScrollPosition element) => element.isActived);
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$&#123;actived.length&#125;</span>'</span>);
      <span class="hljs-keyword">if</span> (actived.isNotEmpty) <span class="hljs-keyword">return</span> actived;
    &#125;
    <span class="hljs-keyword">return</span> _innerController.nestedPositions;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在再运行 demo ， 切换列表之后滚动看看，是否👌了？结果是失望的。</p>
<ol>
<li>虽然我们在 <code>drag</code> 操作的时候，确实可以判断到谁是激活的，但是手指 up ，开始惯性滑动的时候，<code>dragCancelCallback</code> 回调已经触发，<code>_isActived</code> 已经被设置为 <code>false</code> 。</li>
<li>当我们在操作 <code>PageView</code> 上方黄色区域的时候(通常情况下，这部分可能是 <code>Tabbar</code> ), 由于没有在列表上面进行 <code>drag</code> 操作，所以这个时候 <code>actived</code> 的列表为 0.</li>
</ol>
<pre><code class="hljs language-dart copyable" lang="dart">      NestedScrollView(
        headerSliverBuilder: (
          BuildContext buildContext,
          <span class="hljs-built_in">bool</span> innerBoxIsScrolled,
        ) =>
            <Widget>[
          SliverToBoxAdapter(
            child: Container(
              color: Colors.red,
              height: <span class="hljs-number">200</span>,
            ),
          )
        ],
        body: Column(
          children: [
            Container(
              color: Colors.yellow,
              height: <span class="hljs-number">200</span>,
            ),
            Expanded(
              child: PageView(
                children: <Widget>[
                  ListItem(
                    tag: <span class="hljs-string">'Tab0'</span>,
                  ),
                  ListItem(
                    tag: <span class="hljs-string">'Tab1'</span>,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-16">是否可见</h6>
<p>问题好像又走到了老地方，怎么判断一个视图是可见。</p>
<p>首先，我们这里能拿到最直接的就是 <code>_NestedScrollPosition</code>，我们看看这个家伙有什么东西可以利用。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da67f7cb5424c5aa47d8719c323a9ab~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-09 下午4.44.08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一眼就看到了 <code>context(ScrollableState)</code>，是一个 <code>ScrollContext</code>，而 <code>ScrollableState</code> 实现了 <code>ScrollContext</code>。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-comment">/// <span class="markdown">Where the scrolling is taking place.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">Typically implemented by [ScrollableState].</span></span>
  <span class="hljs-keyword">final</span> ScrollContext context;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一眼 <code>ScrollContext</code>，<code>notificationContext</code> 和 <code>storageContext</code> 应该是相关的。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ScrollContext</span> </span>&#123;
  <span class="hljs-comment">/// <span class="markdown">The [BuildContext] that should be used when dispatching</span></span>
  <span class="hljs-comment">/// <span class="markdown">[ScrollNotification]s.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">This context is typically different that the context of the scrollable</span></span>
  <span class="hljs-comment">/// <span class="markdown">widget itself. For example, [Scrollable] uses a context outside the</span></span>
  <span class="hljs-comment">/// <span class="markdown">[Viewport] but inside the widgets created by</span></span>
  <span class="hljs-comment">/// <span class="markdown">[ScrollBehavior.buildOverscrollIndicator] and [ScrollBehavior.buildScrollbar].</span></span>
  BuildContext? <span class="hljs-keyword">get</span> notificationContext;

  <span class="hljs-comment">/// <span class="markdown">The [BuildContext] that should be used when searching for a [PageStorage].</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">This context is typically the context of the scrollable widget itself. In</span></span>
  <span class="hljs-comment">/// <span class="markdown">particular, it should involve any [GlobalKey]s that are dynamically</span></span>
  <span class="hljs-comment">/// <span class="markdown">created as part of creating the scrolling widget, since those would be</span></span>
  <span class="hljs-comment">/// <span class="markdown">different each time the widget is created.</span></span>
  <span class="hljs-comment">// TODO(goderbauer): Deprecate this when state restoration supports all features of PageStorage.</span>
  BuildContext <span class="hljs-keyword">get</span> storageContext;

  <span class="hljs-comment">/// <span class="markdown">A [TickerProvider] to use when animating the scroll position.</span></span>
  TickerProvider <span class="hljs-keyword">get</span> vsync;

  <span class="hljs-comment">/// <span class="markdown">The direction in which the widget scrolls.</span></span>
  AxisDirection <span class="hljs-keyword">get</span> axisDirection;

  <span class="hljs-comment">/// <span class="markdown">Whether the contents of the widget should ignore [PointerEvent] inputs.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">Setting this value to true prevents the use from interacting with the</span></span>
  <span class="hljs-comment">/// <span class="markdown">contents of the widget with pointer events. The widget itself is still</span></span>
  <span class="hljs-comment">/// <span class="markdown">interactive.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">For example, if the scroll position is being driven by an animation, it</span></span>
  <span class="hljs-comment">/// <span class="markdown">might be appropriate to set this value to ignore pointer events to</span></span>
  <span class="hljs-comment">/// <span class="markdown">prevent the user from accidentally interacting with the contents of the</span></span>
  <span class="hljs-comment">/// <span class="markdown">widget as it animates. The user will still be able to touch the widget,</span></span>
  <span class="hljs-comment">/// <span class="markdown">potentially stopping the animation.</span></span>
  <span class="hljs-keyword">void</span> setIgnorePointer(<span class="hljs-built_in">bool</span> value);

  <span class="hljs-comment">/// <span class="markdown">Whether the user can drag the widget, for example to initiate a scroll.</span></span>
  <span class="hljs-keyword">void</span> setCanDrag(<span class="hljs-built_in">bool</span> value);

  <span class="hljs-comment">/// <span class="markdown">Set the [SemanticsAction]s that should be expose to the semantics tree.</span></span>
  <span class="hljs-keyword">void</span> setSemanticsActions(<span class="hljs-built_in">Set</span><SemanticsAction> actions);

  <span class="hljs-comment">/// <span class="markdown">Called by the [ScrollPosition] whenever scrolling ends to persist the</span></span>
  <span class="hljs-comment">/// <span class="markdown">provided scroll <span class="hljs-code">`offset`</span> for state restoration purposes.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">The [ScrollContext] may pass the value back to a [ScrollPosition] by</span></span>
  <span class="hljs-comment">/// <span class="markdown">calling [ScrollPosition.restoreOffset] at a later point in time or after</span></span>
  <span class="hljs-comment">/// <span class="markdown">the application has restarted to restore the scroll offset.</span></span>
  <span class="hljs-keyword">void</span> saveOffset(<span class="hljs-built_in">double</span> offset);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看 <code>ScrollableState</code> 中的实现。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ScrollableState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">Scrollable</span>> <span class="hljs-title">with</span> <span class="hljs-title">TickerProviderStateMixin</span>, <span class="hljs-title">RestorationMixin</span>
    <span class="hljs-keyword">implements</span> <span class="hljs-title">ScrollContext</span> </span>&#123;
 
  <span class="hljs-meta">@override</span>
  BuildContext? <span class="hljs-keyword">get</span> notificationContext => _gestureDetectorKey.currentContext;

  <span class="hljs-meta">@override</span>
  BuildContext <span class="hljs-keyword">get</span> storageContext => context; 
    
&#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>storageContext</code> 其实是</li>
</ul>
<p><code>ScrollableState</code> 的 <code>context</code>。</p>
<ul>
<li><code>notificationContext</code> 查找下引用，可以看到。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ff0daea77d746b788567be5e812eec3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-09 下午5.00.01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>果然，谁触发的事件，当然是 <code>ScrollableState</code> 里面的 <code>RawGestureDetector</code> 。</p>
<pre><code class="hljs language-dart copyable" lang="dart">    NotificationListener<ScrollNotification>(
      onNotification: (ScrollNotification scrollNotification) &#123;
  <span class="hljs-comment">/// <span class="markdown">The build context of the widget that fired this notification.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">This can be used to find the scrollable's render objects to determine the</span></span>
  <span class="hljs-comment">/// <span class="markdown">size of the viewport, for instance.</span></span>
  <span class="hljs-comment">// final BuildContext? context;</span>
        <span class="hljs-built_in">print</span>(scrollNotification.context);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>; 
      &#125;,
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终我们还是要在 <code>storageContext</code> 上面下功夫了。之前 # <a href="https://juejin.cn/post/6844904015994552333" target="_blank" title="https://juejin.cn/post/6844904015994552333">Flutter Sliver一生之敌</a> # 系列里面我们对 <code>Sliver</code> 相关知识进行过梳理。对于 <code>TabbarView</code> 或者 <code>PageView</code> 当前显示的元素，在 <code>RenderSliverFillViewport</code> 当中应该是唯一的(除非你把 <code>viewportFraction</code> 的值设置为小于 <code>1</code> 的数值 )。我们可以通过  <code>_NestedScrollPosition</code> 的
<code>Context</code> 向上找到 <code>RenderSliverFillViewport</code>，看看 <code>RenderSliverFillViewport</code> 中的 child 是否为 <code>_NestedScrollPosition</code> 的 <code>Context</code> 。</p>
<ul>
<li>修改 <code>_NestedScrollCoordinator._innerPositions</code> 为如下:</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">
  <span class="hljs-built_in">Iterable</span><_NestedScrollPosition> <span class="hljs-keyword">get</span> _innerPositions &#123;
    <span class="hljs-keyword">if</span> (_innerController.nestedPositions.length > <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">final</span> <span class="hljs-built_in">Iterable</span><_NestedScrollPosition> actived = _innerController
          .nestedPositions
          .where((_NestedScrollPosition element) => element.isActived);
      <span class="hljs-keyword">if</span> (actived.isEmpty) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> _NestedScrollPosition scrollPosition
            <span class="hljs-keyword">in</span> _innerController.nestedPositions) &#123;
          <span class="hljs-keyword">final</span> RenderObject? renderObject =
              scrollPosition.context.storageContext.findRenderObject();

          <span class="hljs-keyword">if</span> (renderObject == <span class="hljs-keyword">null</span> || !renderObject.attached) &#123;
            <span class="hljs-keyword">continue</span>;
          &#125;

          <span class="hljs-keyword">if</span> (renderObjectIsVisible(renderObject, Axis.horizontal)) &#123;
            <span class="hljs-keyword">return</span> <_NestedScrollPosition>[scrollPosition];
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> _innerController.nestedPositions;
      &#125;

      <span class="hljs-keyword">return</span> actived;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> _innerController.nestedPositions;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 <code>renderObjectIsVisible</code> 方法中查看是否存在于 <code>TabbarView</code> 或者 <code>PageView</code> 中，并且其 <code>axis</code> 与 <code>ScrollPosition</code> 的 <code>axis</code> 相垂直。如果有的话，用 <code>RenderViewport</code> 当前的 <code>child</code> 调用 <code>childIsVisible</code> 方法验证是否包含 <code>ScrollPosition</code> 所对应的 <code>RenderObject</code>。注意，这里调用了 <code>renderObjectIsVisible</code> 因为可能有嵌套(多级)的 <code>TabbarView</code> 或者 <code>PageView</code>。</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-built_in">bool</span> renderObjectIsVisible(RenderObject renderObject, Axis axis) &#123;
    <span class="hljs-keyword">final</span> RenderViewport? parent = findParentRenderViewport(renderObject);
    <span class="hljs-keyword">if</span> (parent != <span class="hljs-keyword">null</span> && parent.axis == axis) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> RenderSliver childrenInPaint
          <span class="hljs-keyword">in</span> parent.childrenInHitTestOrder) &#123;
        <span class="hljs-keyword">return</span> childIsVisible(childrenInPaint, renderObject) &&
            renderObjectIsVisible(parent, axis);
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>向上寻找 <code>RenderViewport</code> ，我们只在 <code>NestedScrollView</code> 的 <code>body</code> 的中找，直到 <code>_ExtendedRenderSliverFillRemainingWithScrollable</code>。</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">  RenderViewport? findParentRenderViewport(RenderObject? object) &#123;
    <span class="hljs-keyword">if</span> (object == <span class="hljs-keyword">null</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;
    object = object.parent <span class="hljs-keyword">as</span> RenderObject?;
    <span class="hljs-keyword">while</span> (object != <span class="hljs-keyword">null</span>) &#123;
      <span class="hljs-comment">// 只在 body 中寻找</span>
      <span class="hljs-keyword">if</span> (object <span class="hljs-keyword">is</span> _ExtendedRenderSliverFillRemainingWithScrollable) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
      &#125;
      <span class="hljs-keyword">if</span> (object <span class="hljs-keyword">is</span> RenderViewport) &#123;
        <span class="hljs-keyword">return</span> object;
      &#125;
      object = object.parent <span class="hljs-keyword">as</span> RenderObject?;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用 <code>visitChildrenForSemantics</code> 遍历 <code>children</code>，看是否能找到 <code>ScrollPosition</code> 所对应的 <code>RenderObject</code></li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart">    <span class="hljs-comment">/// <span class="markdown">Return whether renderObject is visible in parent</span></span>
  <span class="hljs-built_in">bool</span> childIsVisible(
    RenderObject parent,
    RenderObject renderObject,
  ) &#123;
    <span class="hljs-built_in">bool</span> visible = <span class="hljs-keyword">false</span>;

    <span class="hljs-comment">// The implementation has to return the children in paint order skipping all</span>
    <span class="hljs-comment">// children that are not semantically relevant (e.g. because they are</span>
    <span class="hljs-comment">// invisible).</span>
    parent.visitChildrenForSemantics((RenderObject child) &#123;
      <span class="hljs-keyword">if</span> (renderObject == child) &#123;
        visible = <span class="hljs-keyword">true</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        visible = childIsVisible(child, renderObject);
      &#125;
    &#125;);
    <span class="hljs-keyword">return</span> visible;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">还有其他方案吗</h4>
<p>其实对于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F21868" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/issues/21868" ref="nofollow noopener noreferrer">Body 中多列表滚动互相影响的问题</a>
，如果你只是要求列表保持位置的话，你完全可以利用 <code>PageStorageKey</code> 来保持滚动列表的位置。这样的话，<code>TabbarView</code> 或者 <code>PageView</code> 切换的时候，<code>ScrollableState</code> 会 <code>dispose</code>，并且从将 <code>ScrollPosition</code> 从 <code>innerController</code> 中 <code>detach</code> 掉。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    <span class="hljs-keyword">if</span> (widget.controller != <span class="hljs-keyword">null</span>) &#123;
      widget.controller!.detach(position);
    &#125; <span class="hljs-keyword">else</span> &#123;
      _fallbackScrollController?.detach(position);
      _fallbackScrollController?.dispose();
    &#125;

    position.dispose();
    _persistedScrollOffset.dispose();
    <span class="hljs-keyword">super</span>.dispose();
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而你需要做的是在上一层，利用比如
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fprovider" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/provider" ref="nofollow noopener noreferrer">provider | Flutter Package (flutter-io.cn)</a> 来保持列表数据或者其他数据状态。</p>
<pre><code class="hljs language-dart copyable" lang="dart">   NestedScrollView(
        headerSliverBuilder: (
          BuildContext buildContext,
          <span class="hljs-built_in">bool</span> innerBoxIsScrolled,
        ) =>
            <Widget>[
          SliverToBoxAdapter(
            child: Container(
              color: Colors.red,
              height: <span class="hljs-number">200</span>,
            ),
          )
        ],
        body: Column(
          children: <Widget>[
            Container(
              color: Colors.yellow,
              height: <span class="hljs-number">200</span>,
            ),
            Expanded(
              child: PageView(
                <span class="hljs-comment">//controller: PageController(viewportFraction: 0.8),</span>
                children: <Widget>[
                  ListView.builder(
                    <span class="hljs-comment">//store Page state</span>
                    key: <span class="hljs-keyword">const</span> PageStorageKey<<span class="hljs-built_in">String</span>>(<span class="hljs-string">'Tab0'</span>),
                    physics: <span class="hljs-keyword">const</span> ClampingScrollPhysics(),
                    itemBuilder: (BuildContext c, <span class="hljs-built_in">int</span> i) &#123;
                      <span class="hljs-keyword">return</span> Container(
                        alignment: Alignment.center,
                        height: <span class="hljs-number">60.0</span>,
                        child:
                            Text(<span class="hljs-keyword">const</span> Key(<span class="hljs-string">'Tab0'</span>).toString() + <span class="hljs-string">': ListView<span class="hljs-subst">$i</span>'</span>),
                      );
                    &#125;,
                    itemCount: <span class="hljs-number">50</span>,
                  ),
                  ListView.builder(
                    <span class="hljs-comment">//store Page state</span>
                    key: <span class="hljs-keyword">const</span> PageStorageKey<<span class="hljs-built_in">String</span>>(<span class="hljs-string">'Tab1'</span>),
                    physics: <span class="hljs-keyword">const</span> ClampingScrollPhysics(),
                    itemBuilder: (BuildContext c, <span class="hljs-built_in">int</span> i) &#123;
                      <span class="hljs-keyword">return</span> Container(
                        alignment: Alignment.center,
                        height: <span class="hljs-number">60.0</span>,
                        child:
                            Text(<span class="hljs-keyword">const</span> Key(<span class="hljs-string">'Tab1'</span>).toString() + <span class="hljs-string">': ListView<span class="hljs-subst">$i</span>'</span>),
                      );
                    &#125;,
                    itemCount: <span class="hljs-number">50</span>,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">重构代码</h2>
<h3 data-id="heading-19">体力活</h3>
<p>3年不知不觉就写了 18 个 Flutter 组件库和 3 个 Flutter 相关 工具。</p>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Flike_button" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/like_button" ref="nofollow noopener noreferrer">like_button | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fextended_image_library" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/extended_image_library" ref="nofollow noopener noreferrer">extended_image_library | Flutter Package (pub.dev)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_nested_scroll_view" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_nested_scroll_view" ref="nofollow noopener noreferrer">extended_nested_scroll_view | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_text" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_text" ref="nofollow noopener noreferrer">extended_text | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_text_field" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_text_field" ref="nofollow noopener noreferrer">extended_text_field | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_image" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_image" ref="nofollow noopener noreferrer">extended_image | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_sliver" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_sliver" ref="nofollow noopener noreferrer">extended_sliver | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fpull_to_refresh_notification" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/pull_to_refresh_notification" ref="nofollow noopener noreferrer">pull_to_refresh_notification | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fwaterfall_flow" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/waterfall_flow" ref="nofollow noopener noreferrer">waterfall_flow | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Floading_more_list" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/loading_more_list" ref="nofollow noopener noreferrer">loading_more_list | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_tabs" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_tabs" ref="nofollow noopener noreferrer">extended_tabs | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fhttp_client_helper" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/http_client_helper" ref="nofollow noopener noreferrer">http_client_helper | Dart Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_text_library" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_text_library" ref="nofollow noopener noreferrer">extended_text_library | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_list" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_list" ref="nofollow noopener noreferrer">extended_list | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_list_library" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_list_library" ref="nofollow noopener noreferrer">extended_list_library | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fff_annotation_route_library" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/ff_annotation_route_library" ref="nofollow noopener noreferrer">ff_annotation_route_library | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Floading_more_list_library" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/loading_more_list_library" ref="nofollow noopener noreferrer">loading_more_list_library | Dart Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fff_annotation_route" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/ff_annotation_route" ref="nofollow noopener noreferrer">ff_annotation_route | Dart Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fff_annotation_route_core" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/ff_annotation_route_core" ref="nofollow noopener noreferrer">ff_annotation_route_core | Dart Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fflex_grid" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/flex_grid" ref="nofollow noopener noreferrer">flex_grid | Flutter Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fassets_generator" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/assets_generator" ref="nofollow noopener noreferrer">assets_generator | Dart Package (flutter-io.cn)</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2FJsonToDart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/JsonToDart" ref="nofollow noopener noreferrer">fluttercandies/JsonToDart: The tool to convert json to dart code, support Windows，Mac，Web. (github.com)</a></p>
</li>
</ol>
<p>可以说每一次官方发布 <code>Stable</code> 版本，对于我来说都是一次体力活。特别是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_nested_scroll_view" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_nested_scroll_view" ref="nofollow noopener noreferrer">extended_nested_scroll_view</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_text" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_text" ref="nofollow noopener noreferrer">extended_text</a>
, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_text_field" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_text_field" ref="nofollow noopener noreferrer">extended_text_field </a>
, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fextended_image" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/extended_image" ref="nofollow noopener noreferrer">extended_image</a> 这 4 个库，<code>merge</code> 代码是不光是体力活，也需要认真仔细去理解新改动。</p>
<h3 data-id="heading-20">结构重构</h3>
<p>这次乘着这个改动的机会，我将整个结构做了调整。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3959287229384e869ae596c0f502731e~tplv-k3u1fbpfcp-watermark.image" alt="E5A53922-AF95-4B13-805A-36F19286344D.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><code>src/extended_nested_scroll_view.dart</code> 为官方源码，只做了一些必要改动。比如增加参数，替换扩展类型。最大程度的保持官方源码的结构和格式。</p>
</li>
<li>
<p><code>src/extended_nested_scroll_view_part.dart</code> 为扩展官方组件功能的部分代码。增加下面3个扩展类，实现我们相应的扩展方法。</p>
</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_ExtendedNestedScrollCoordinator</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">_NestedScrollCoordinator</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_ExtendedNestedScrollController</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">_NestedScrollController</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_ExtendedNestedScrollPosition</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">_NestedScrollPosition</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在 <code>src/extended_nested_scroll_view.dart</code> 修改初始化代码即可。以后我只需要用 <code>src/extended_nested_scroll_view.dart</code> 跟官方的代码进行 <code>merge</code> 即可。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  _NestedScrollCoordinator? _coordinator;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-keyword">super</span>.initState();
    _coordinator = _ExtendedNestedScrollCoordinator(
      <span class="hljs-keyword">this</span>,
      widget.controller,
      _handleHasScrolledBodyChanged,
      widget.floatHeaderSlivers,
      widget.pinnedHeaderSliverHeightBuilder,
      widget.onlyOneScrollInBody,
      widget.scrollDirection,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">小糖果🍬</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d3d47aad8cb475a95a007a16053d1b6~tplv-k3u1fbpfcp-watermark.image" alt="F794DA85-4559-45EC-92B0-FFA16D2B87FE.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你看到这里，已经看了6000字，感谢。送上一些的技巧，希望能对你有所帮助。</p>
<h3 data-id="heading-22">CustomScrollView center</h3>
<p><code>CustomScrollView.center</code> 这个属性我其实很早之前就讲过了，
<a href="https://juejin.cn/post/6844904008339947528" target="_blank" title="https://juejin.cn/post/6844904008339947528">Flutter Sliver一生之敌 (ScrollView) (juejin.cn)</a>。
简单地来说:</p>
<ul>
<li><code>center</code> 是开始绘制的地方，既绘制在  <code>zero scroll offset</code> 的地方， 向前为负，向后为正。</li>
<li><code>center</code> 之前的 <code>Sliver</code> 是倒序绘制。</li>
</ul>
<p>比如下面代码，你觉得最终的效果是什么样子的？</p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
        center: key,
        slivers: <Widget>[
        SliverList(),
        SliverGrid(key:key),
        ]
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下，<code>SliverGrid</code> 被绘制在了开始位置。你可以向下滚动，这个时候，上面的 <code>SliverList</code> 才会展示。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e2aa564e4548fa9a4a025fec721547~tplv-k3u1fbpfcp-watermark.image" alt="F2C1BFDA-2919-45BD-B71A-F601F248797B.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>CustomScrollView.anchor</code> 可以控制 <code>center</code> 的位置。
0 为 viewport 的 leading，1 为 viewport 的 trailing，既这个是 viewport 高度垂直(宽度水平)的占比。比如如果是 0.5，那么绘制 <code>SliverGrid</code> 的地方就会在 <code>viewport</code> 的中间位置。</p>
<p>通过这2个属性，我们可以创造一些有趣的效果。</p>
<h4 data-id="heading-23">聊天列表</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e56c0452f887455388be17ef68ef1365~tplv-k3u1fbpfcp-watermark.image" alt="chatList.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflutter_instant_messaging%2Fblob%2Fmaster%2Fclient%2Flib%2Fmain.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flutter_instant_messaging/blob/master/client/lib/main.dart" ref="nofollow noopener noreferrer">flutter_instant_messaging/main.dart at master · fluttercandies/flutter_instant_messaging (github.com)</a> 一年前写的小 demo，现在移到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflutter_challenges%2Fblob%2Fmain%2Flib%2Fchat_sample.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flutter_challenges/blob/main/lib/chat_sample.dart" ref="nofollow noopener noreferrer">flutter_challenges/chat_sample.dart at main · fluttercandies/flutter_challenges (github.com)</a> 统一维护。</p>
<h4 data-id="heading-24">ios 倒序相册</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3ddf9b15d34279acc2d54c8d074e84~tplv-k3u1fbpfcp-watermark.image" alt="iosPhotoAlbum.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflutter_challenges%2Fblob%2Fmain%2Flib%2Fios_photo%2520album.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flutter_challenges/blob/main/lib/ios_photo%20album.dart" ref="nofollow noopener noreferrer">flutter_challenges/ios_photo album.dart at main · fluttercandies/flutter_challenges (github.com)</a> 代码在此。</p>
<p>起源于马师傅给 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fwechat_assets_picker" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/wechat_assets_picker" ref="nofollow noopener noreferrer">wechat_assets_picker | Flutter Package (flutter-io.cn)</a>提的需求(尾款都没有结)，要让相册查看效果跟 Ios 原生的一样。 Ios 的设计果然不一样，学习(chao)就是了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83c4993cc3be44b58efcf7febb42df02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">斗鱼首页滚动效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3e70cd220dd4886804ea8fe850cf24a~tplv-k3u1fbpfcp-watermark.image" alt="float_scroll.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflutter_challenges%2Fblob%2Fmain%2Flib%2Ffloat_scroll.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flutter_challenges/blob/main/lib/float_scroll.dart" ref="nofollow noopener noreferrer">flutter_challenges/float_scroll.dart at main · fluttercandies/flutter_challenges (github.com)</a> 代码在此。</p>
<p>不得不再提提，<code>NotificationListener</code>，它是 <code>Notification</code> 的监听者。通过 <code>Notification.dispatch</code> ，通知会沿着当前节点（BuildContext）向上传递，就跟冒泡一样，你可以在父节点使用 <code>NotificationListener</code> 来接受通知。 Flutter 中经常使用到的是 <code>ScrollNotification</code>，除此之外还有<code>SizeChangedLayoutNotification</code>、<code>KeepAliveNotification</code> 、<code>LayoutChangedNotification</code> 等。你也可以自己定义一个通知。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:oktoast/oktoast.dart'</span>;

<span class="hljs-keyword">void</span> main() &#123;
  runApp(<span class="hljs-keyword">const</span> MyApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyApp(&#123;Key key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> OKToast(
      child: MaterialApp(
        title: <span class="hljs-string">'Flutter Demo'</span>,
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: MyHomePage(),
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyHomePage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> MyHomePage(&#123;Key key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  _MyHomePageState createState() => _MyHomePageState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> NotificationListener<TextNotification>(
      onNotification: (TextNotification notification) &#123;
        showToast(<span class="hljs-string">'星星收到了通知: <span class="hljs-subst">$&#123;notification.text&#125;</span>'</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
      &#125;,
      child: Scaffold(
          appBar: AppBar(),
          body: NotificationListener<TextNotification>(
            onNotification: (TextNotification notification) &#123;
              showToast(<span class="hljs-string">'大宝收到了通知: <span class="hljs-subst">$&#123;notification.text&#125;</span>'</span>);
              <span class="hljs-comment">// 如果这里改成 true, 星星就收不到信息了，</span>
              <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
            &#125;,
            child: Center(
              child: Builder(
                builder: (BuildContext context) &#123;
                  <span class="hljs-keyword">return</span> RaisedButton(
                    onPressed: () &#123;
                      TextNotification(<span class="hljs-string">'下班了!'</span>)..dispatch(context);
                    &#125;,
                    child: Text(<span class="hljs-string">'点我'</span>),
                  );
                &#125;,
              ),
            ),
          )),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TextNotification</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Notification</span> </span>&#123;
  TextNotification(<span class="hljs-keyword">this</span>.text);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> text;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>而我们经常使用的下拉刷新和上拉加载更多的组件也可以通过监听 <code>ScrollNotification</code> 来完成。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fpull_to_refresh_notification" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/pull_to_refresh_notification" ref="nofollow noopener noreferrer">pull_to_refresh_notification | Flutter Package (flutter-io.cn)</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Floading_more_list" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/loading_more_list" ref="nofollow noopener noreferrer">loading_more_list | Flutter Package (flutter-io.cn)</a></p>
<h3 data-id="heading-26">ScrollPosition.ensureVisible</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc60ca6f5f94f3b967faeeca47b5ae7~tplv-k3u1fbpfcp-watermark.image" alt="QQ20210812-205510-HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要完成这个操作，应该大部分人都是会的。其实万变不离其中，通过当前对象的 <code>RenderObject</code> 去找到对应的 <code>RenderAbstractViewport</code>，然后通过 <code>getOffsetToReveal</code> 方法获取相对位置。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-comment">/// <span class="markdown">Animates the position such that the given object is as visible as possible</span></span>
  <span class="hljs-comment">/// <span class="markdown">by just scrolling this position.</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown">See also:</span></span>
  <span class="hljs-comment">///</span>
  <span class="hljs-comment">/// <span class="markdown"><span class="hljs-bullet"> *</span> [ScrollPositionAlignmentPolicy] for the way in which <span class="hljs-code">`alignment`</span> is</span></span>
  <span class="hljs-comment">/// <span class="markdown">   applied, and the way the given <span class="hljs-code">`object`</span> is aligned.</span></span>
  Future<<span class="hljs-keyword">void</span>> ensureVisible(
    RenderObject object, &#123;
    <span class="hljs-built_in">double</span> alignment = <span class="hljs-number">0.0</span>,
    <span class="hljs-built_in">Duration</span> duration = <span class="hljs-built_in">Duration</span>.zero,
    Curve curve = Curves.ease,
    ScrollPositionAlignmentPolicy alignmentPolicy = ScrollPositionAlignmentPolicy.explicit,
  &#125;) &#123;
    <span class="hljs-keyword">assert</span>(alignmentPolicy != <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(object.attached);
    <span class="hljs-keyword">final</span> RenderAbstractViewport viewport = RenderAbstractViewport.of(object);
    <span class="hljs-keyword">assert</span>(viewport != <span class="hljs-keyword">null</span>);

    <span class="hljs-built_in">double</span> target;
    <span class="hljs-keyword">switch</span> (alignmentPolicy) &#123;
      <span class="hljs-keyword">case</span> ScrollPositionAlignmentPolicy.explicit:
        target = viewport.getOffsetToReveal(object, alignment).offset.clamp(minScrollExtent, maxScrollExtent) <span class="hljs-keyword">as</span> <span class="hljs-built_in">double</span>;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> ScrollPositionAlignmentPolicy.keepVisibleAtEnd:
        target = viewport.getOffsetToReveal(object, <span class="hljs-number">1.0</span>).offset.clamp(minScrollExtent, maxScrollExtent) <span class="hljs-keyword">as</span> <span class="hljs-built_in">double</span>;
        <span class="hljs-keyword">if</span> (target < pixels) &#123;
          target = pixels;
        &#125;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> ScrollPositionAlignmentPolicy.keepVisibleAtStart:
        target = viewport.getOffsetToReveal(object, <span class="hljs-number">0.0</span>).offset.clamp(minScrollExtent, maxScrollExtent) <span class="hljs-keyword">as</span> <span class="hljs-built_in">double</span>;
        <span class="hljs-keyword">if</span> (target > pixels) &#123;
          target = pixels;
        &#125;
        <span class="hljs-keyword">break</span>;
    &#125;

    <span class="hljs-keyword">if</span> (target == pixels)
      <span class="hljs-keyword">return</span> Future<<span class="hljs-keyword">void</span>>.value();

    <span class="hljs-keyword">if</span> (duration == <span class="hljs-built_in">Duration</span>.zero) &#123;
      jumpTo(target);
      <span class="hljs-keyword">return</span> Future<<span class="hljs-keyword">void</span>>.value();
    &#125;

    <span class="hljs-keyword">return</span> animateTo(target, duration: duration, curve: curve);
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo 代码地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fzmtzawqlp%2F139af3739d3f171df88ce0219a44f6fd" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/zmtzawqlp/139af3739d3f171df88ce0219a44f6fd" ref="nofollow noopener noreferrer">ensureVisible 演示 (github.com)</a></p>
<p>留个问题，当你点击 <code>点我跳转顶部,我是固定的</code> 这个按钮的时候，你猜会发生什么现象。</p>
<h2 data-id="heading-27">Flutter 挑战</h2>
<p>之前跟掘金官方提过，是否可以增加 <code>你问我答</code>/ <code>你出题我挑战</code> 模块，增加程序员之间的交流，程序员都是不服输的，应该会 🔥 吧？ 想想都刺激。我创建一个新的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjq.qq.com%2F%3F_wv%3D1027%26k%3DQnncnj0y" target="_blank" rel="nofollow noopener noreferrer" title="https://jq.qq.com/?_wv=1027&k=Qnncnj0y" ref="nofollow noopener noreferrer">FlutterChallenges qq 群 321954965</a> 来进行交流；<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflutter_challenges" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flutter_challenges" ref="nofollow noopener noreferrer">仓库</a>，用来讨论和存放这些小挑战代码。平时收集一些平时有一些难度的实际场景例子，不单单只是秀技术。进群需要通过推荐或者验证，欢迎喜欢折腾自己的童鞋
。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d6492d82ab74ef8a0296809207124e4~tplv-k3u1fbpfcp-watermark.image" alt="765C2B11D14A50B6A967989C3F389F89.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/170a850a53814f3bb58d64bb90468a22~tplv-k3u1fbpfcp-watermark.image" alt="39661F87CC0AF9632C8AF35A1D28334A.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>情人节 + 七夕 这是不是个巧合 ？？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d26c6377c649139dee5cfa61eb66c9~tplv-k3u1fbpfcp-watermark.image" alt="144135BF9EF5646F6ACB8352387C7FB9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">美团饿了么点餐页面</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adba7c510495484c8b763edff0db34f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要求:</p>
<ol>
<li>左右2个列表能联动，整个首页上下滚动联动</li>
<li>通用性，可成组件</li>
</ol>
<p>如果你认真看完了 <code>NestedScrollView</code>，我想应该有办法来做这种功能了。</p>
<h3 data-id="heading-29">增大点击区域</h3>
<p>增加点击区域，这应该是平时应该会遇到的需求，那么在 Flutter 中应该怎么实现呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93b490daf0eb4da4bd8e7ef0d1e3d599~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原始代码地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fzmtzawqlp%2F8abda3c688c01c0b7c8d37236e58e191" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/zmtzawqlp/8abda3c688c01c0b7c8d37236e58e191" ref="nofollow noopener noreferrer">增大点击区域 (github.com)</a></p>
<p>为了测试方便，请添加在 <code>pubspec.yaml</code> 中 添加财经龙大佬的 <code>oktoast</code> 。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml">  <span class="hljs-attr">oktoast:</span> <span class="hljs-string">any</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要求:</p>
<ol>
<li>不要改变整个结构和尺寸。</li>
<li>不要直接 <code>Stack</code> 把整个 <code>Item</code> 重写。</li>
<li>通用性。</li>
</ol>
<p>完成效果如下, 扩大的范围理论上可以随意设置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a193cf59cc64f18a8aaee47682f313d~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-30">结语</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65c47cf62fa54b1f9f6e54be2b59c34b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"> 第一次把掘金干爆，只能将文章一部分代码都移到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fzmtzawqlp" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/zmtzawqlp" ref="nofollow noopener noreferrer">gist.github.com/zmtzawqlp</a> (突然想起来一些说什么万字文章的标题党是不是有点打脸呀，我看接近 9000 就不能再写了)。这篇写的比较多，想到了什么就写。不管是什么技术，只有深入了才能领会其中的道理。维护开源组件，确实是一件很累的事情。但是这会不断强迫你去学习，在不停更新迭代当中，你都会学习到一些平时不容易接触到的知识。积沙成塔，撸遍 <code>Flutter</code> 源码不再是梦想。</p>
<p>爱 <code>Flutter</code>，爱<code>糖果</code>，欢迎加入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies" ref="nofollow noopener noreferrer">Flutter Candies</a>，一起生产可爱的Flutter小糖果<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjq.qq.com%2F%3F_wv%3D1027%26k%3D5bcc0gy" target="_blank" rel="nofollow noopener noreferrer" title="https://jq.qq.com/?_wv=1027&k=5bcc0gy" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8afe301bcc2a4fccbdbcee6d05927a8c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">QQ群:181398081</a></p>
<p>最最后放上 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies" ref="nofollow noopener noreferrer">Flutter Candies</a> 全家桶，真香。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/192cbc5338cc4848af54c629d6865050~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            