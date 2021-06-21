
---
title: '【Flutter 基础】 视图布局-前言'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2538'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 23:54:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=2538'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><em>注：本文从个人公众号（岛前屿端）中迁移重新发布</em></p>
<blockquote>
<p>Flutter 是谷歌的移动 UI 框架，可以从单个代码库快速的为移动端(iOS & Android)、Web、桌面端、嵌入式设备上构建高质量的原生用户界面和应用程序。</p>
</blockquote>
<hr>
<p>在学习 Flutter 的过程中也看到一些人对于 Flutter 的议论。他们大多觉得 Flutter <strong>不够友好、括号太多了，导致看起来代码非常复杂，对此嗤之以鼻并以唱衰之</strong>。</p>
<p>当然也有一些人认为，不再以 xml 的方式实现结构布局且以<strong>代码逻辑来驱动和构建布局的方式</strong>对于一些审美感不高的人是一种乐于接受的方式。</p>
<p><strong>所谓江湖纷杂，流派众多，也是各花入各眼。孰对孰错并无绝对之说。</strong></p>
<p>而我的看法则是较为中立，应该是各取一半吧：</p>
<blockquote>
<p>以代码驱动构建布局确实是可以省下对于布局的搔首挠耳之苦，但对于较为复杂的结构代码驱动的形式就显得没那么游刃有余了。当然在一些特性上相对传统确实是较为便捷不可否认。</p>
</blockquote>
<p>这段时间学习以来，看过一些大侠们的作品，功力不一般。大多为独立实现的作品，让我看了煞是羡慕。</p>
<p>不过说来惭愧我也学了一月有余，对于 Flutter 的整体认识程度还不是很高，还不能很全面的去讲解整个 Flutter 的体系。但我能做到的是将我在学习过程中我遇到的问题、踩到的坑、理解上的问题解决完后，再重新整理输出出来，以便有需要或有兴趣学的少侠们提供帮助参考。</p>
<p>Ok，以上就是我瞎逼逼的废话了。那么接下来就来看一看 Flutter 的视图布局吧。</p>
<h2 data-id="heading-0">视图的布局方式</h2>
<p>简单说一下我对 Flutter 视图布局的看法，在前篇中我有提到 Flutter 是使用了 Dart 语言进行编写，所以弱化了视图编辑的部分。视图的渲染、结构、布局都通过代码逻辑来生成。</p>
<p>这在一定程度上在视图结构和逻辑的关联性是强了，但在直观布局结构方面却弱了，所以就导致在代码中会发现嵌套层次很多很深，同时也会对开发者的能力有了一些要求，当然如果有面向对象编程的经验的话，那么就上手来说问题并不大。</p>
<p>在 Flutter 中主要的布局方式有两种：</p>
<ul>
<li>多子类元素布局</li>
<li>单子类元素布局</li>
</ul>
<p>还有一个比较特殊的 <strong>LayoutBuilder</strong>，这个主要是构建一个可以<strong>依赖父窗口大小的 Widget 树</strong>。</p>
<p>此外在官方文档术语描述中将 2 个 Widget  嵌套关系为 Widget 下的子 Widget，这不便于一些已经学过 html 或 xml 的少侠们理解，故在此约定：</p>
<p><code>约定：在接下来的 《Flutter 视图布局》系列文章中我将 widget 下的第一级 widget 称之为“子元素”以便让少侠们理解。</code></p>
<h3 data-id="heading-1">多子类元素布局</h3>
<p>多子类元素布局的 Widget 有 <strong>10 种</strong>：</p>
<ul>
<li><strong>Row</strong> 在水平方向上排列子元素的列表。</li>
<li><strong>Column</strong> 在垂直方向上排列子元素的列表。</li>
<li><strong>ListBody</strong> 一个 Widget，它沿着一个给定的轴，顺序排列它的子元素。</li>
<li><strong>ListView</strong> 可滚动的列表控件。ListView 是最常用的滚动 Widget，它在滚动方向上一个接一个地显示它的子元素。在纵轴上，子元素们被要求填充ListView。</li>
<li><strong>Table</strong> 为其子元素使用表格布局算法的 Widget。</li>
<li><strong>Wrap</strong> 可以在水平或垂直方向多行显示其子元素。</li>
<li><strong>Flow</strong> 一个可以实现流式布局算法的 Widget。</li>
<li><strong>Stack</strong> 可以允许其子元素简单的堆叠在一起。</li>
<li><strong>IndexedStack</strong> 从一个子元素列表中显示单个子元素的 Stack。</li>
<li><strong>CustomMultiChildLayout</strong> 使用一个委托来对多个子元素进行设置大小和定位的小部件。</li>
</ul>
<p>每一种 Widget 所实现的布局方式都不一样，都有一个<strong>主要的实现场景，以及对子元素的展示方式</strong>。</p>
<h3 data-id="heading-2">单子类元素布局</h3>
<p>单子类元素布局的 Widget 有18种：</p>
<ul>
<li><strong>Container</strong> 一个拥有绘制、定位、调整大小的 Widget。</li>
<li><strong>Padding</strong> 可以将其子元素添加填充指定的空间的 Widget。</li>
<li><strong>Center</strong> 将其子元素居中显示在自身内部的 Widget。</li>
<li><strong>Align</strong> 一个 Widget，它可以将其子元素对齐，并可以根据子元素的大小自动调整大小。</li>
<li><strong>Baseline</strong> 根据子项的基线对它们的位置进行定位的 Widget。</li>
<li><strong>IntrinsicWidth</strong> 一个 Widget，它将它的子元素的宽度调整其本身实际的宽度。</li>
<li><strong>IntrinsicHeight</strong> 一个 Widget，它将它的子元素的高度调整其本身实际的高度。</li>
<li><strong>AspectRatio</strong> 一个 Widget，试图将子元素的大小指定为某个特定的长宽比。</li>
<li><strong>Transform</strong> 在绘制子元素之前应用转换的 Widget。</li>
<li><strong>Offstage</strong> 一个布局 Widget，可以控制其子元素的显示和隐藏。</li>
<li><strong>ConstrainedBox</strong> 对其子项施加附加约束的 Widget。</li>
<li><strong>FittedBox</strong> 按自己的大小调整其子元素的大小和位置。</li>
<li><strong>LimitedBox</strong> 一个当其自身不受约束时才限制其大小的盒子。</li>
<li><strong>OverflowBox</strong> 对其子项施加不同约束的 Widget，它可能允许子项溢出父级。</li>
<li><strong>SizedBox</strong> 一个特定大小的盒子。这个 Widget 强制它的孩子有一个特定的宽度和高度。如果宽度或高度为NULL，则此 Widget 将调整自身大小以匹配该维度中的孩子的大小。</li>
<li><strong>SizedOverflowBox</strong> 一个特定大小的 Widget，但是会将它的原始约束传递给它的孩子，它可能会溢出。</li>
<li><strong>FractionallySizedBox</strong> 一个 Widget，它把它的子项放在可用空间的一小部分。关于布局算法的更多细节，见RenderFractionallySizedOverflowBox。</li>
<li><strong>CustomSingleChildLayout</strong> 一个自定义的拥有单个子元素的布局 Widget。</li>
</ul>
<p>每一种 Widget 都会影响其子元素最终的<strong>视图显示效果，如大小、位置、边框、背景等</strong>。</p>
<h2 data-id="heading-3">布局分篇</h2>
<p>由于 Widget 布局的种类多达 <strong>28 + 1</strong> 种，单篇文章中无法将其一一列举说完，所以我打算将其分为多篇文章来对其进行说明。</p>
<p>关于单子类元素布局的 Widget，因部分只会在特定的需求场景中使用，所以这部分我可能不会太深入细说。</p>
<p>在整理之后，我考虑将其按如下分篇：</p>
<h3 data-id="heading-4">多子类元素布局</h3>
<ul>
<li>Row、Column（一）</li>
<li>ListBody、ListView（二）</li>
<li>Table、Wrap、Flow（三）</li>
<li>Stack、IndexedStack（四）</li>
</ul>
<h3 data-id="heading-5">单子类元素布局</h3>
<ul>
<li>Container、Padding、Center、Align、Baseline（一）</li>
<li>IntrinsicWidth、IntrinsicHeight、AspectRatio （二）</li>
<li>Transform、Offstage（三）</li>
<li>ConstrainedBox、FittedBox、LimitedBox、OverflowBox （四）</li>
<li>SizedBox、SizedOverflowBox、FractionallySizedBox（五）</li>
</ul>
<p>由于 <strong>CustomMultiChildLayout、CustomSingleChildLayout</strong> 较为相似，我将它们与 <strong>LayoutBuilder</strong> 放在一起。</p>
<blockquote>
<p>此外我还考虑为了方便各位少侠小伙伴们更直观的学习和参考，我还将 Flutter 系列的 MyApp 项目同步到了 Github 上，以后如有文章更新都会将文章内的代码<strong>同步更新到 Github 的项目里</strong>。让有需要的小伙伴可以 clone 下来学习</p>
<p>当然，在代码中我尽量写了<strong>足够详细的注释</strong>，也是希望让少侠 & 小伙伴们不要去猜代码，这没有意义，而是要看懂这是怎么回事，然后再去尝试修改代码运行得到结果。</p>
</blockquote>
<p>Github 地址：<a href="https://github.com/linxsbox/myapp.git" target="_blank" rel="nofollow noopener noreferrer">github.com/linxsbox/my…</a></p></div>  
</div>
            