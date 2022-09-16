
---
title: 'UIStackView之一问一答'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/611f860e7c1040b982616dc51ddf82af~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 07:42:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/611f860e7c1040b982616dc51ddf82af~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h1 data-id="heading-0">前言</h1>
<p>此篇文章作为在使用UIStackView前的一些答疑，既是扫盲篇，也是实用篇，以下会讲述一些实用的案例，目的就是让更多的人拥抱UIStackView。同时欢迎小伙伴通过评论区讲讲使用StackView遇到的问题。</p>
<h1 data-id="heading-1">答疑</h1>
<h2 data-id="heading-2">排列视图间距大小不一</h2>
<p><strong>问：排列视图间距大小不一，可以用UIStackView吗？</strong><br>
答：当然可以用，UIStackView虽然有space属性，但是适用于所有的排列视图，如果想要指定某个排列视图之间的间距，有以下两种方法：</p>
<ul>
<li>使用 <code>- (void)setCustomSpacing:(CGFloat)spacing afterView:(UIView *)arrangedSubview API_AVAILABLE(ios(11.0),tvos(11.0));</code>方法，不过这个方法有版本的限制。</li>
<li>使用一个UIView进行填充；即在需要间隙的位置插入一个空的view，并设置好其宽度或高度来充当两个排列视图的间距。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/611f860e7c1040b982616dc51ddf82af~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="截屏2022-09-07 22.49.43.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">排列视图对齐位置不一致</h2>
<p><strong>问：排列视图的对齐位置不一致，如何使用UIStackView？</strong><br>
答：我们可以选择一种合适的对齐方式保证适用于绝大多数排列视图，剩下的视图使用UIView进行封装，然后在View中进行约束布局。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae9641a24604e1188a5f50c92e3dfe0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="截屏2022-09-07 23.08.00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">排列视图大小不一致</h2>
<p><strong>问：排列视图的大小不一致，可以用UIStackView吗？</strong><br>
答：可以的，UIStackView中的排列视图不需要设置位置，至于尺寸大小可以根据自身需要设置。（设置方式<code>AutoLayout</code>）</p>
<h2 data-id="heading-5">灵活多变的UI设计</h2>
<p><strong>问：多变的UI设计适合使用UIStackView吗？</strong><br>
答：再合适不过了，为什么这么说呢，虽然通过<code>AutoLayout</code>可以自适应，来解决灵活多变的UI布局，但是这会有繁琐的代码来控制。而通过使用<code>UIStackView</code>，我们仅添加一次排列视图，而后可以通过控制排列视图的显示或隐藏<code>(hidden)</code>就能使<code>UIStackView</code>重新布局。</p>
<h2 data-id="heading-6">列表可用？</h2>
<p><strong>问：UIStackView可以用于列表布局吗？</strong><br>
答：可以，使用UIStackView可以快捷的布局简单列表，相比较UITableView较为简单，使用UITableView往往需要设置代理，实现代理等。<br>
具体做法：一般采用<code>UIScrollView + UIStackView</code>，ScrollView控制滚动，StackView管理内容。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36a239978f994d259d5958652ac7d9f8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="2022-09-08 18-47-16.2022-09-08 18_48_45.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">拉伸、压缩</h2>
<p><strong>问：听说UIStackView可以自适应排列视图，那么排列视图如果有拉伸或者压缩的需求可以使用UIStackView吗？</strong><br>
答：可以，UIStackView会优先根据<strong>抗拉伸优先级<code>Content Hugging Priority</code></strong>（优先级越高，越不容易被拉伸）、<strong>抗压缩优先级<code>Content Compression Resistance Priority</code></strong>（优先级越高，越不容易被压缩）去约束排列视图，并不会和StackView布局相冲突。</p>
<h1 data-id="heading-8">The end</h1>
<p>总而言之，如果你怕麻烦，那就快来使用UIStackView，把麻烦事都交给它。</p>
<p>如果有比较难以理解或者初学者不懂的问题，稍后也会在这整理。</p>
<p>如果你还没有使用过UIStackView的可以查看我的上篇文章「<a href="https://juejin.cn/post/7139925799594885133" target="_blank" title="https://juejin.cn/post/7139925799594885133">使用UIStackView来简化iOS的界面布局</a>」。</p></div>  
</div>
            