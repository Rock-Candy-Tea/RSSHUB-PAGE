
---
title: 'Flutter 锁定行列的 FlexGrid'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3dc93fdac74ef89065ae88de29b9d5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 17:12:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3dc93fdac74ef89065ae88de29b9d5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>之前在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.grapecity.com.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.grapecity.com.cn/" ref="nofollow noopener noreferrer">GrapeCity/ComponentOne</a> 做微软 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fuwp%2Fxaml-platform%2Fxaml-overview" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/zh-cn/windows/uwp/xaml-platform/xaml-overview" ref="nofollow noopener noreferrer">Xaml</a> 系列的控件，包括 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.microsoft.com%2Fsilverlight%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.microsoft.com/silverlight/" ref="nofollow noopener noreferrer">Silverlight</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdotnet%2Fdesktop%2Fwpf%2Fgetting-started%2F%3Fview%3Dnetframeworkdesktop-4.8" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/en-us/dotnet/desktop/wpf/getting-started/?view=netframeworkdesktop-4.8" ref="nofollow noopener noreferrer">WPF</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FWindows%2520Phone%2F9227600%3Ffromtitle%3Dwindowsphone%26fromid%3D11234211%26fr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/Windows%20Phone/9227600?fromtitle=windowsphone&fromid=11234211&fr=aladdin" ref="nofollow noopener noreferrer">Windows Phone</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fuwp%2Fget-started%2Funiversal-application-platform-guide" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/zh-cn/windows/uwp/get-started/universal-application-platform-guide" ref="nofollow noopener noreferrer">UWP</a>，一套代码多端共用，是真香。对于创建一个水平垂直方向都可以滚动的列表，是非常方便的。但是在 Flutter 平台，似乎没有看到一个开箱即食组件。</p>
<blockquote>
<p>经常听到大家讲 Flutter 辣鸡，什么什么不支持。其实 Flutter 有够开源和扩展，大部分东西只要用心，都能创造出来的，只是你愿意不愿意花时间去尝试。</p>
</blockquote>
<p>虽然说也叫 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2Fpackages%2Fflex_grid" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/packages/flex_grid" ref="nofollow noopener noreferrer">FlexGrid</a>, 但功能远远没有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fcomponentone%2Fflexgrid" target="_blank" rel="nofollow noopener noreferrer" title="https://www.grapecity.com.cn/developer/componentone/flexgrid" ref="nofollow noopener noreferrer">C# FlexGrid</a> 的多，一些功能对于我来说，不是必须，所以便未做。
在设计理念方面，Xaml 和 Flutter 大大的不一样。Xaml 模板，双向绑定用的飞起，而 Flutter 更爱 <code>immutable</code>，主张 <code>simple is fast</code>。所以对于 Flutter 版本的 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">FlexGrid</a>，更倾向设计成 Flutter 形式的轻量级的组件。</p>
<p>现在主要支持以下功能:</p>
<ul>
<li>锁定行列</li>
<li>在 <code>TabBarView</code>/<code>PageView</code> 中水平滚动连贯</li>
<li>大量数据的高性能</li>
<li>刷新动画和增量加载</li>
</ul>




















<table><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3dc93fdac74ef89065ae88de29b9d5~tplv-k3u1fbpfcp-watermark.image" alt="FrozenedRowColumn.gif" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4965592cfff14841adf5c76c4739e380~tplv-k3u1fbpfcp-watermark.image" alt="TabView.gif" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aca2d0b17d7436faa500669d290687d~tplv-k3u1fbpfcp-watermark.image" alt="HugeData.gif" loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a7fb36638c4cc78063a54d3c857fc6~tplv-k3u1fbpfcp-watermark.image" alt="Excel.gif" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb8569767354846b83a8197ffe11170~tplv-k3u1fbpfcp-watermark.image" alt="StockList.gif" loading="lazy" referrerpolicy="no-referrer"></td><td></td></tr></tbody></table>
<h2 data-id="heading-1">原理</h2>
<p>有一说一，对于设计这个组件，几乎没有任何难点，Sliver 已经足够优秀。</p>
<h3 data-id="heading-2">结构</h3>
<p>以下为伪代码，只是提供一个现实的思路。可以看到，只需要使用到 Flutter 提供的 Sliver 相关的组件，就能构造出来这样一个结构。最终代码  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflex_grid%2Fblob%2Fmain%2Flib%2Fsrc%2Fflex_grid.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flex_grid/blob/main/lib/src/flex_grid.dart" ref="nofollow noopener noreferrer">flex_grid.dart</a></p>
<pre><code class="hljs language-dart copyable" lang="dart">    CustomScrollView(
      scrollDirection: Axis.vertical,
      slivers: <Widget>[
        <span class="hljs-comment">// 表头</span>
        SliverPinnedToBoxAdapter(
          child: CustomScrollView(
            scrollDirection: Axis.horizontal,
            slivers: <Widget>[
              <span class="hljs-comment">// 锁定的列，如果有</span>
              SliverPinnedToBoxAdapter(),
              SliverList(),
            ],
          ),
        ),
        <span class="hljs-comment">// 锁定的行，如果有</span>
        SliverPinnedToBoxAdapter(
          child: CustomScrollView(
            scrollDirection: Axis.horizontal,
            slivers: <Widget>[
              <span class="hljs-comment">// 锁定的列，如果有</span>
              SliverPinnedToBoxAdapter(),
              SliverList(),
            ],
          ),
        ),
        <span class="hljs-comment">// 滚动部分</span>
        SliverList(
         CustomScrollView(
          scrollDirection: Axis.horizontal,
          slivers: <Widget>[
            <span class="hljs-comment">// 锁定的列，如果有 </span>
            SliverPinnedToBoxAdapter(),
            SliverList(),
          ],
        ))
      ],
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">水平同步滚动</h3>
<p>如果你看过 <a href="https://juejin.cn/post/6906127634498306056" target="_blank" title="https://juejin.cn/post/6906127634498306056">Flutter Tab嵌套滑动如丝 (juejin.cn)</a> 的文章，这个问题应该也不难解决。</p>
<h4 data-id="heading-4">ScrollableState</h4>
<p>首先带大家再次认识下 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscrollable.dart%23L384" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scrollable.dart#L384" ref="nofollow noopener noreferrer">ScrollableState</a>,只要你熟悉了这个类，你就大概能了解到 Flutter 中的滚动体系。</p>
<h5 data-id="heading-5">手势从何而来</h5>
<p>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fblob%2Fmaster%2Fpackages%2Fflutter%2Flib%2Fsrc%2Fwidgets%2Fscrollable.dart%23L384" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/widgets/scrollable.dart#L384" ref="nofollow noopener noreferrer">setCanDrag</a>方法中，我们根据 <code>Axis</code> 设置水平或者垂直的
Drag 监听，分别注册了以下的事件。</p>
<pre><code class="copyable">              ..onDown = _handleDragDown
              ..onStart = _handleDragStart
              ..onUpdate = _handleDragUpdate
              ..onEnd = _handleDragEnd
              ..onCancel = _handleDragCancel
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">_handleDragDown</h5>
<p>初始化一个 <code>ScrollHoldController</code> 对象, 在 <code>_handleDragStart</code> 和 <code>_handleDragCancel</code> 的时候会触发 <code>_disposeHold</code> 回调。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  Drag? _drag;
  ScrollHoldController? _hold;
  <span class="hljs-keyword">void</span> _handleDragDown(DragDownDetails details) &#123;
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
    _hold = position.hold(_disposeHold);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">_handleDragStart</h5>
<p>初始化一个 <code>Drag</code> 对象，并且注册 <code>_disposeDrag</code> 回调。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> _handleDragStart(DragStartDetails details) &#123;
    <span class="hljs-comment">// It's possible for _hold to become null between _handleDragDown and</span>
    <span class="hljs-comment">// _handleDragStart, for example if some user code calls jumpTo or otherwise</span>
    <span class="hljs-comment">// triggers a new activity to begin.</span>
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
    _drag = position.drag(details, _disposeDrag);
    <span class="hljs-keyword">assert</span>(_drag != <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">_handleDragUpdate</h5>
<p>更新状态，这里就是你看到列表开始滚动了。</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> _handleDragUpdate(DragUpdateDetails details) &#123;
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _drag?.update(details);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">_handleDragEnd</h5>
<p>这里就是手势的惯性处理</p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> _handleDragEnd(DragEndDetails details) &#123;
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _drag?.end(details);
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">_handleDragCancel</h5>
<p>调用 <code>cancel</code> 方法，触发 <code>_disposeHold</code> 和 <code>_disposeDrag</code></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> _handleDragCancel() &#123;
    <span class="hljs-comment">// _hold might be null if the drag started.</span>
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _hold?.cancel();
    _drag?.cancel();
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">_disposeHold 和 _disposeDrag</h5>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-keyword">void</span> _disposeHold() &#123;
    _hold = <span class="hljs-keyword">null</span>;
  &#125;

  <span class="hljs-keyword">void</span> _disposeDrag() &#123;
    _drag = <span class="hljs-keyword">null</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上我们知道了 Flutter 是怎么获取手势并且反馈到滚动组件上面的。篇幅有限，其实这里还有很多有趣的相关知识，我会在下一篇中讲解。</p>
<h4 data-id="heading-12">DragHoldController</h4>
<p>接下来，我们把这几个方法封装到一起，供 <code>ScrollController</code> 统一操作。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DragHoldController</span> </span>&#123;
  DragHoldController(<span class="hljs-keyword">this</span>.position);
  <span class="hljs-keyword">final</span> ScrollPosition position;
  Drag? _drag;

  ScrollHoldController? _hold;

  <span class="hljs-keyword">void</span> handleDragDown(DragDownDetails? details) &#123;
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
    _hold = position.hold(_disposeHold);
  &#125;

  <span class="hljs-keyword">void</span> handleDragStart(DragStartDetails details) &#123;
    <span class="hljs-comment">// It's possible for _hold to become null between _handleDragDown and</span>
    <span class="hljs-comment">// _handleDragStart, for example if some user code calls jumpTo or otherwise</span>
    <span class="hljs-comment">// triggers a new activity to begin.</span>
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
    _drag = position.drag(details, _disposeDrag);
    <span class="hljs-keyword">assert</span>(_drag != <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
  &#125;

  <span class="hljs-keyword">void</span> handleDragUpdate(DragUpdateDetails details) &#123;
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _drag?.update(details);
  &#125;

  <span class="hljs-keyword">void</span> handleDragEnd(DragEndDetails details) &#123;
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _drag?.end(details);
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
  &#125;

  <span class="hljs-keyword">void</span> handleDragCancel() &#123;
    <span class="hljs-comment">// _hold might be null if the drag started.</span>
    <span class="hljs-comment">// _drag might be null if the drag activity ended and called _disposeDrag.</span>
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span> || _drag == <span class="hljs-keyword">null</span>);
    _hold?.cancel();
    _drag?.cancel();
    <span class="hljs-keyword">assert</span>(_hold == <span class="hljs-keyword">null</span>);
    <span class="hljs-keyword">assert</span>(_drag == <span class="hljs-keyword">null</span>);
  &#125;

  <span class="hljs-keyword">void</span> _disposeHold() &#123;
    _hold = <span class="hljs-keyword">null</span>;
  &#125;

  <span class="hljs-keyword">void</span> _disposeDrag() &#123;
    _drag = <span class="hljs-keyword">null</span>;
  &#125;

  <span class="hljs-keyword">void</span> forceCancel() &#123;
    _hold = <span class="hljs-keyword">null</span>;
    _drag = <span class="hljs-keyword">null</span>;
  &#125;

  <span class="hljs-built_in">bool</span> <span class="hljs-keyword">get</span> hasDrag => _drag != <span class="hljs-keyword">null</span>;
  <span class="hljs-built_in">bool</span> <span class="hljs-keyword">get</span> hasHold => _hold != <span class="hljs-keyword">null</span>;

  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> extentAfter => position.extentAfter;

  <span class="hljs-built_in">double</span> <span class="hljs-keyword">get</span> extentBefore => position.extentBefore;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">ScrollController</h4>
<p>我们可以看到不管是 <code>ScrollHoldController</code> 还是 <code>Drag</code>，都是由 <code>ScrollPosition</code> 创建出来的，单个 <code>ScrollPosition</code> 控制单个列表，那么我们是不是直接利用 <code>ScrollController</code> 控制多个 <code>ScrollPosition</code> 呢？</p>
<p>为此我创建了一个用于同步 <code>ScrollPosition</code> 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflex_grid%2Fblob%2Fmaster%2Flib%2Fsrc%2Fcontroller%2Fscroll_controller.dart%23L35" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flex_grid/blob/master/lib/src/controller/scroll_controller.dart#L35" ref="nofollow noopener noreferrer">SyncControllerMixin</a>.</p>
<ul>
<li>在 <code>attach</code> 的时候创建对应的 <code>DragHoldController</code> 并且同步 <code>position</code> 的 <code>pixels</code></li>
<li>在 <code>hold</code> 和 <code>drag</code> 相关方法中去同步滚动</li>
<li><code>detach</code> 的时候移除</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">mixin</span> SyncControllerMixin <span class="hljs-keyword">on</span> ScrollController &#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">Map</span><ScrollPosition, DragHoldController> _positionToListener =
      <ScrollPosition, DragHoldController>&#123;&#125;;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> attach(ScrollPosition position) &#123;
    <span class="hljs-keyword">super</span>.attach(position);
    <span class="hljs-keyword">assert</span>(!_positionToListener.containsKey(position));
    <span class="hljs-comment">// 列表回收元素之后，再次创建，需要去将当前的滚动同步</span>
    <span class="hljs-keyword">if</span> (_positionToListener.isNotEmpty) &#123;
      <span class="hljs-keyword">final</span> <span class="hljs-built_in">double</span> pixels = _positionToListener.keys.first.pixels;
      <span class="hljs-keyword">if</span> (position.pixels != pixels) &#123;
        position.correctPixels(pixels);
      &#125;
    &#125;
    _positionToListener[position] = DragHoldController(position);
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> detach(ScrollPosition position) &#123;
    <span class="hljs-keyword">super</span>.detach(position);
    <span class="hljs-keyword">assert</span>(_positionToListener.containsKey(position));
    _positionToListener[position]!.forceCancel();
    _positionToListener.remove(position);
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    forceCancel();
    <span class="hljs-keyword">super</span>.dispose();
  &#125;

  <span class="hljs-keyword">void</span> handleDragDown(DragDownDetails? details) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.handleDragDown(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> handleDragStart(DragStartDetails details) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.handleDragStart(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> handleDragUpdate(DragUpdateDetails details) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.handleDragUpdate(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> handleDragEnd(DragEndDetails details) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.handleDragEnd(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> handleDragCancel() &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.handleDragCancel();
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> forceCancel() &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">final</span> DragHoldController item <span class="hljs-keyword">in</span> _positionToListener.values) &#123;
      item.forceCancel();
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">HorizontalSyncScrollMinxin</h4>
<p>接下来我们要把前面的东西都组合在一起，放进<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fflex_grid%2Fblob%2Fmain%2Flib%2Fsrc%2Fhorizontal_sync_scroll_minxin.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/flex_grid/blob/main/lib/src/horizontal_sync_scroll_minxin.dart" ref="nofollow noopener noreferrer">horizontal_sync_scroll_minxin.dart</a>。</p>
<ul>
<li>注册手势监听</li>
<li>传递到 SyncControllerMixin 中控制水平的同步滚动。如果达到滚动边界，</li>
</ul>
<p>外部有 <code>TabbarView</code> 和 <code>PageView</code> 的话，将让外部传入 <code>outerHorizontalSyncController</code> 接管手势</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">mixin</span> HorizontalSyncScrollMinxin &#123;
  <span class="hljs-built_in">Map</span><<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>? _gestureRecognizers;
  <span class="hljs-built_in">Map</span><<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>? <span class="hljs-keyword">get</span> gestureRecognizers =>
      _gestureRecognizers;
  SyncControllerMixin? <span class="hljs-keyword">get</span> horizontalController;
  SyncControllerMixin? <span class="hljs-keyword">get</span> outerHorizontalSyncController;
  ScrollPhysics? <span class="hljs-keyword">get</span> physics;

  <span class="hljs-keyword">void</span> initGestureRecognizers() &#123;
    _gestureRecognizers = <<span class="hljs-built_in">Type</span>, GestureRecognizerFactory>&#123;
      HorizontalDragGestureRecognizer:
          GestureRecognizerFactoryWithHandlers<HorizontalDragGestureRecognizer>(
        () => HorizontalDragGestureRecognizer(),
        (HorizontalDragGestureRecognizer instance) &#123;
          instance
            ..onDown = (DragDownDetails details) &#123;
              _handleDragDown(
                details,
              );
            &#125;
            ..onStart = (DragStartDetails details) &#123;
              _handleDragStart(
                details,
              );
            &#125;
            ..onUpdate = (DragUpdateDetails details) &#123;
              _handleDragUpdate(
                details,
              );
            &#125;
            ..onEnd = (DragEndDetails details) &#123;
              _handleDragEnd(
                details,
              );
            &#125;
            ..onCancel = () &#123;
              _handleDragCancel();
            &#125;
            ..minFlingDistance = physics?.minFlingDistance
            ..minFlingVelocity = physics?.minFlingVelocity
            ..maxFlingVelocity = physics?.maxFlingVelocity;
        &#125;,
      ),
    &#125;;
  &#125;

  <span class="hljs-keyword">void</span> _handleDragDown(
    DragDownDetails details,
  ) &#123;
    outerHorizontalSyncController?.forceCancel();
    horizontalController?.forceCancel();
    horizontalController?.handleDragDown(details);
  &#125;

  <span class="hljs-keyword">void</span> _handleDragStart(DragStartDetails details) &#123;
    horizontalController?.handleDragStart(details);
  &#125;

  <span class="hljs-keyword">void</span> _handleDragUpdate(DragUpdateDetails details) &#123;
    _handleTabView(details);
    <span class="hljs-keyword">if</span> (outerHorizontalSyncController?.hasDrag ?? <span class="hljs-keyword">false</span>) &#123;
      outerHorizontalSyncController!.handleDragUpdate(details);
    &#125; <span class="hljs-keyword">else</span> &#123;
      horizontalController!.handleDragUpdate(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> _handleDragEnd(DragEndDetails details) &#123;
    <span class="hljs-keyword">if</span> (outerHorizontalSyncController?.hasDrag ?? <span class="hljs-keyword">false</span>) &#123;
      outerHorizontalSyncController!.handleDragEnd(details);
    &#125; <span class="hljs-keyword">else</span> &#123;
      horizontalController!.handleDragEnd(details);
    &#125;
  &#125;

  <span class="hljs-keyword">void</span> _handleDragCancel() &#123;
    horizontalController?.handleDragCancel();
    outerHorizontalSyncController?.handleDragCancel();
  &#125;

  <span class="hljs-built_in">bool</span> _handleTabView(DragUpdateDetails details) &#123;
    <span class="hljs-keyword">if</span> (outerHorizontalSyncController != <span class="hljs-keyword">null</span>) &#123;
      <span class="hljs-keyword">final</span> <span class="hljs-built_in">double</span> delta = details.delta.dx;
      <span class="hljs-comment">// 如果有外面的 controller，比如 TabbarView 和 PageView，</span>
      <span class="hljs-comment">// 我们需要在表格滚动到边界的时候，让外部的 controller 接管手势。</span>
      <span class="hljs-keyword">if</span> ((delta < <span class="hljs-number">0</span> &&
              horizontalController!.extentAfter == <span class="hljs-number">0</span> &&
              outerHorizontalSyncController!.extentAfter != <span class="hljs-number">0</span>) ||
          (delta > <span class="hljs-number">0</span> &&
              horizontalController!.extentBefore == <span class="hljs-number">0</span> &&
              outerHorizontalSyncController!.extentBefore != <span class="hljs-number">0</span>)) &#123;
        <span class="hljs-keyword">if</span> (!outerHorizontalSyncController!.hasHold &&
            !outerHorizontalSyncController!.hasDrag) &#123;
          outerHorizontalSyncController!.handleDragDown(<span class="hljs-keyword">null</span>);
          outerHorizontalSyncController!.handleDragStart(DragStartDetails(
            globalPosition: details.globalPosition,
            localPosition: details.localPosition,
            sourceTimeStamp: details.sourceTimeStamp,
          ));
        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
      &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
  &#125;

  RawGestureDetector buildGestureDetector(&#123;<span class="hljs-keyword">required</span> Widget child&#125;) &#123;
    <span class="hljs-keyword">return</span> RawGestureDetector(
      gestures: gestureRecognizers!,
      child: child,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">使用</h2>




































































































<table><thead><tr><th>参数</th><th>描述</th><th>默认</th></tr></thead><tbody><tr><td>frozenedColumnsCount</td><td>锁定列的个数</td><td>0</td></tr><tr><td>frozenedRowsCount</td><td>锁定行的个数</td><td>0</td></tr><tr><td>cellBuilder</td><td>用于创建表格的回调</td><td>required</td></tr><tr><td>headerBuilder</td><td>用于创建表头的回调</td><td>required</td></tr><tr><td>columnsCount</td><td>列的个数，必须大于0</td><td>required</td></tr><tr><td>source</td><td>FlexGrid 的数据源</td><td>required</td></tr><tr><td>rowWrapper</td><td>在这个回调里面用于装饰 row Widget</td><td>null</td></tr><tr><td>rebuildCustomScrollView</td><td>当数据源改变的时候是否重新 build ， 它来自 [LoadingMoreCustomScrollView]</td><td>false</td></tr><tr><td>controller</td><td>垂直方向的 [ScrollController]</td><td>null</td></tr><tr><td>horizontalController</td><td>水平方向的 [SyncControllerMixin]</td><td>null</td></tr><tr><td>outerHorizontalSyncController</td><td>外部的 <code>SyncControllerMixin</code>, 用在 <code>ExtendedTabBarView</code> 或者 <code>ExtendedPageView</code> 上面，让水平方法的滚动更连续</td><td>null</td></tr><tr><td>physics</td><td>水平和垂直方法的  <code>ScrollPhysics</code></td><td>null</td></tr><tr><td>highPerformance</td><td>如果为true的话,  将强制水平和垂直元素的大小，以提高滚动的性能</td><td>false</td></tr><tr><td>headerStyle</td><td>样式用于来描述表头</td><td>CellStyle.header()</td></tr><tr><td>cellStyle</td><td>样式用于来描述表格</td><td>CellStyle.cell()</td></tr><tr><td>indicatorBuilder</td><td>用于创建不同加载状态的回调, 它来自  <code>LoadingMoreCustomScrollView</code></td><td>null</td></tr><tr><td>extendedListDelegate</td><td>用于设置一些扩展功能的设置, 它来自  <code>LoadingMoreCustomScrollView</code></td><td>null</td></tr><tr><td>headersBuilder</td><td>用于创建自定义的表头</td><td>null</td></tr></tbody></table>
<h2 data-id="heading-16">结语</h2>
<p>总的来说，这个组件实现不是很困难，主要是再次介绍了一下 <code>ScrollableState</code> ，而滚动相关的一些东西没有展开讲，留在下一篇介绍。是的，又要再水一篇关于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies%2Fextended_nested_scroll_view" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies/extended_nested_scroll_view" ref="nofollow noopener noreferrer">extended_nested_scroll_view</a>，三年了，<code>issue</code> 依然都还在，而我为啥又要重构这个组件，请听下回分解。</p>
<p>爱 <code>Flutter</code>，爱<code>糖果</code>，欢迎加入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies" ref="nofollow noopener noreferrer">Flutter Candies</a>，一起生产可爱的Flutter小糖果<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjq.qq.com%2F%3F_wv%3D1027%26k%3D5bcc0gy" target="_blank" rel="nofollow noopener noreferrer" title="https://jq.qq.com/?_wv=1027&k=5bcc0gy" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8afe301bcc2a4fccbdbcee6d05927a8c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">QQ群:181398081</a></p>
<p>最最后放上 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffluttercandies" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fluttercandies" ref="nofollow noopener noreferrer">Flutter Candies</a> 全家桶，真香。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/192cbc5338cc4848af54c629d6865050~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            