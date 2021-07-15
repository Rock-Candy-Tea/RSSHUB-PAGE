
---
title: 'iOS无感知上拉加载更多功能实现'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 17:26:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></h3>
<h2 data-id="heading-1">RxSwift编写wanandroid客户端现已开源</h2>
<p><strong>目前RxSwift编写wanandroid客户端已经开源了——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FseasonZhu%2FRxStudy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seasonZhu/RxStudy" ref="nofollow noopener noreferrer">项目链接</a>。记得给个star喔！</strong></p>
<p><strong>附上一张效果图片：</strong></p>
<div align="center">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8059a3160c6c4f169664979574888f2a~tplv-k3u1fbpfcp-watermark.image" alt="RPReplay_Final1625472730.2021-07-05 16_13_58.gif" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p><strong>本篇文章是从6月更文中热心网友的留言中进行的开发与探索：</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d89d64b571b44f8782b908dbf2e9449e~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210709_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>6月确实因为日更的原因，这个功能没有实现，趁着7月的时候，解决了。</p>
<p><strong>废话了这么多，那么我们进入主题吧。</strong></p>
<h2 data-id="heading-2">什么是无感知上拉加载更多</h2>
<p>什么是无感知，这个这样理解：<strong>在网络情况正常的情况下，用户对列表进行连续的上拉时，该列表可以无卡顿不停出现新的数据。</strong></p>
<p>如果要体验话，Web端很多已经做到了，比如掘金的首页，还有比如掘金iOS的App，列表都是无感知上拉加载更多。</p>
<p>说来惭愧，写了这久的代码，还真的没有认真思考这个功能怎么实现。</p>
<h2 data-id="heading-3">如何实现无感知上拉加载更多</h2>
<p>我在看见这位网友留言的时候，就开始思考了。</p>
<p>在我看来，有下面几个着手点：</p>
<ul>
<li>
<p>列表滑动时候的是如何知道具体滑动的位置以触发接口请求，添加更多数据？</p>
</li>
<li>
<p>从UIScrollView的代理回调中去找和<strong>scrollView的位置（contentOffset）大小（contentSize）关系密切的回调。</strong></p>
</li>
<li>
<p>网络上有没有比较成熟的思路？</p>
</li>
</ul>
<h3 data-id="heading-4">顺着这条线，我先跑去看了UIScrollViewDelegate的源码：</h3>
<pre><code class="copyable">public protocol UIScrollViewDelegate : NSObjectProtocol &#123;

    
    @available(iOS 2.0, *)
    optional func scrollViewDidScroll(_ scrollView: UIScrollView) // any offset changes

    @available(iOS 3.2, *)
    optional func scrollViewDidZoom(_ scrollView: UIScrollView) // any zoom scale changes

    .
    .
    .
    .
    .
    .
    /// 代码很多，这里就不放上来，给大家压力了。
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接上结论吧：<strong>看了一圈，反正没有和contentSize或者位置相关的回调代理。</strong><code>scrollViewDidScroll</code>这个回调里面虽然可以回参<code>scrollView</code>，但是对于我们需要的信息还不够具体。</p>
<p>思考：<strong>既然UIScrollViewDelegate的代理没有现成的代理回调，自己使用KVO去监听试试？</strong></p>
<h3 data-id="heading-5">网上的思路（一）</h3>
<p>就在我思考的同时，我也在网络上需求实现这个功能的答案，让后看到这样一个思路：</p>
<blockquote>
<p>实现方法很简单，需要用到tableView的一个代理方法，就可轻松实现。- (void)tableView:(UITableView *)tableView willDisplayCell:(UITableViewCell *)cell forRowAtIndexPath:(NSIndexPath *)indexPath就是这个方法，自定义显示cell。这个方法不太常用。但是这个方法可在每个cell将要第一次出现的时候触发。然后我们可设置当前页面第几个cell将要出现时，触发请求加载更多数据。</p>
</blockquote>
<p>我看了之后，心想着，多写一个TableView的代理，总比写KVO的代码少，先试试再说，于是代码撸起：</p>
<pre><code class="copyable">extension SwiftCoinRankListController: UITableViewDelegate &#123;
    
    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) &#123;
        let row = indexPath.row
        let distance = dataSource.count - 25
        print("row: \(row), distance:\(distance)  ")
        if row == distance &#123;
            loadMore()
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本代码可以在开源项目中的<code>SwiftCoinRankListController.swift</code>文件查看具体的逻辑，其主要就是通过cell显示的个数去提前请求加载数据，然后我们看看效果：</p>
<div align="center">
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af5d4dd2f955452aa26656df8391c8e2~tplv-k3u1fbpfcp-watermark.image" alt="620A94AE4920C54C6E1B85E1776AC83C.2021-07-09 17_47_45.gif" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>Gif可能看起来还好，我说我调试的感受：</p>
<p><strong>虽然做到了上拉无感知，但是当手滑的速度比较快的时候，到底了新的数据没有回来，就会在底部等一段时间。</strong></p>
<p>功能达到了，但是感受却不理想，果然还是<strong>监听的细腻程度不够。</strong></p>
<h3 data-id="heading-6">网上的思路（二）</h3>
<p>然后在继续的搜索中，我看到了另外一个方案：</p>
<blockquote>
<p>很多时候我们上拉刷新需要提前加载新数据，这时候利用MJRefreshAutoFooter的属性triggerAutomaticallyRefreshPercent就可以实现，该属性triggerAutomaticallyRefreshPercent默认值为1，然后改成0的话划到底部就会自动刷新，改成-1的话，在快划到底部44px的时候就会自动刷新。</p>
</blockquote>
<p>MJRefresh？使用MJRefreshAutoFooter，这个简单，我直接把基类的footer给替换掉就可以了，本代码可以在开源项目中的<code>BaseTableViewController.swift</code>文件查看：</p>
<pre><code class="copyable">/// 设置尾部刷新控件,更新为无感知加载更多
let footer = MJRefreshAutoFooter()
footer.triggerAutomaticallyRefreshPercent = -1
tableView.mj_footer = footer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看看效果：</p>
<div align="center">
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2e7886b9c74422284e37aa4fb667774~tplv-k3u1fbpfcp-watermark.image" alt="992BC78FBAC7B8CB36A6DC679897DA21.2021-07-09 18_04_09.gif" loading="lazy" referrerpolicy="no-referrer"></p>
</div>
<p>直接说感受：</p>
<p><strong>代码改动性少，编写简单，达到预期效果，爽歪歪。比方案一更丝滑，体验好。</strong></p>
<p>到此，功能就实现，难道就完了？</p>
<p>当然，不会，我们去看看源码吧。</p>
<h2 data-id="heading-7">MJRefresh代码的追根朔源</h2>
<p>首先我们看看<code>MJRefreshAutoFooter.h</code>文件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5cd6a21ef454664b632965900438ae2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有个专门的属性<code>triggerAutomaticallyRefreshPercent</code>去做自动刷新，那么我们去<code>MJRefreshAutoFooter.m</code>中去看看吧：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa409909617349249a3dddbc9a0e5d15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意看喔，这个.m文件有一个<code>- (void)scrollViewContentOffsetDidChange:(NSDictionary *)change</code>方法，并且还调用了<code>super</code>，从这个方法名中我们可以明显的得到<strong>当scrollView的contentOffset变化的时候进行回调的监听。</strong>，我们顺藤摸瓜，看看<code>super</code>是什么，会不会有新的发现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b09a5c826e9f499e801b2116fb64f394~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>稍微跟着一下源代码，MJRefreshAutoFooter的继承关系如下：</p>
<blockquote>
<p>MJRefreshAutoFooter => MJRefreshFooter => MJRefreshComponent</p>
</blockquote>
<p>所以这个super的调用我们就去<code>MJRefreshComponent.m</code>里面去看看吧：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9abaf3cb4664f51b9c893b7416fda7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的截图我们可以得到下面的一些信息与结论：</p>
<ul>
<li>
<p>MJRefreshComponent是通过KVO去监听scrollView的contentOffset变化，思路上我们对齐一致了。</p>
</li>
<li>
<p>该类并没有实现其具体方法，而是将其交由其子类去实现，这一点通过看<code>MJRefreshComponent.h</code>的注释可以得到：</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d707e60883f44b4b9f13962d1ce6810~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>MJRefreshComponent从本质上更像虚基类。</li>
</ul>
<h2 data-id="heading-8">总结</h2>
<p>如果不是掘友提出这个问题，我可能都不会太仔细的去研究这个功能，也许继续普普通通的使用一般的上拉加载更多就够了。</p>
<p>这次的实践，其实是从思路到寻找方法，最后再到源码阅读。</p>
<p><strong>思路也许不困难，但是真正一点点实现并完善功能，每一步都并不容易，这次我也仅仅是继续使用了MJRefresh这个轮子。</strong></p>
<p>想起有一天，在群里吹水看见的一张图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7f2e06329724ac292834afd646599f6~tplv-k3u1fbpfcp-watermark.image" alt="云程序员来了.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>灵魂拷问，直击人心，大部分时间我们不也是云程序员呢？</p>
<p><strong>知行合一方能开拓新的天地。</strong></p>
<h2 data-id="heading-9">参考文章</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F55c0f5b5670f" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/55c0f5b5670f" ref="nofollow noopener noreferrer">iOS 关于列表上拉（平滑加载数据）自动加载数据的问题</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F227976796819" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/227976796819" ref="nofollow noopener noreferrer">MJRefresh小技巧(上拉提前刷新)</a></p></div>  
</div>
            