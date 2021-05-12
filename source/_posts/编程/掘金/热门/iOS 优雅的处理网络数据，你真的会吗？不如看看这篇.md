
---
title: 'iOS 优雅的处理网络数据，你真的会吗？不如看看这篇.'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b43c349ca64ac8b0cec6310baac3e4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 18:01:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b43c349ca64ac8b0cec6310baac3e4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b43c349ca64ac8b0cec6310baac3e4~tplv-k3u1fbpfcp-watermark.image" alt="1573177142153102.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>本文同步发表于我的<a href="https://user-gold-cdn.xitu.io/2020/7/4/17318f81cd4e34e9?w=173&h=173&f=jpeg&s=14515" target="_blank" rel="nofollow noopener noreferrer">微信公众号</a>，扫一扫文章底部的二维码或在微信搜索 <a href="https://user-gold-cdn.xitu.io/2020/7/4/17318f81cd4e34e9?w=173&h=173&f=jpeg&s=14515" target="_blank" rel="nofollow noopener noreferrer">HelloWorld杰少</a> 即可关注。</p>
</blockquote>
<p>相信大家平时在用 App 的时候, 往往有过这样的体验，那就是加载网络数据等待的时间过于漫长，滚动浏览时伴随着卡顿，甚至在没有网络的情况下，整个应用处于不可用状态。那么我们该怎么去提高用户体验，保证用户没有漫长的等待感，还可以轻松自在的享受等待，对加载后的内容有明确的预期呢?</p>
<h2 data-id="heading-0">案例分享</h2>
<p>在现代的工作生活中，手机早已不是单纯的通信工具了，它更像是一个集办公，娱乐，消费的终端，潜移默化的成为了我们生活的一部分。所以作为 iOS 开发者的我们，在日常的开发中，也早已不是处理显示零星的数据这么简单，为了流量往往我们需要在 App 里显示大量有价值的信息来吸引用户，如何优雅的显示这些海量的数据，考量的就是你的个人经验了。</p>
<p>正如大多数 iOS 开发人员所知，显示滚动数据是构建移动应用中常见的任务，Apple 的 SDK 提供了 UITableView 和 UICollectionVIew 这俩大组件来帮助执行这样的任务。但是，当需要显示大量数据时，确保平滑如丝的滚动可能会非常的棘手。所以今天正好趁这个机会，和大家分享一下处理大量可滚动数据方面的个人经验。</p>
<p>在这篇文章中，你将会学到以下内容：</p>
<p>1.让你的 App 可以无限滚动（infinite scrolling），并且滚动数据无缝加载</p>
<p>2.让你的 App 数据滚动时避免卡顿，实现平滑如丝的滚动</p>
<p>3.异步存储（Cache）和获取图像，来使你的 App 具有更高的响应速度</p>
<h2 data-id="heading-1">无限滚动，无缝加载</h2>
<p>提到列表分页，相信大家第一个想到的就是 MJRefresh，用于上拉下拉来刷新数据，当滚动数据到达底部的时候向服务器发送请求，然后在控件底部显示一个 Loading 动画，待请求数据返回后，Loading 动画消失，由 UITableView 或者 UICollectionView 控件继续加载这些数据并显示给用户，效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09a575869366466e88589a4e422023dd~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这种情况下就造成了一种现象，那就是 App 向服务器请求数据到数据返回这段时间留下了一个空白，如果在网络差的情况下，这段空白的时间将会持续，这给人的体验会很不好。那该如何去避免这种现象呢！或者说我们能否去提前获取到其余的数据，在用户毫无感知的情况下把数据请求过来，看上去就像无缝加载一样呢！</p>
<p>答案当然是肯定的！</p>
<p>为了改善应用程序体验，在 iOS 10 上，Apple 对 UICollectionView 和 UITableView 引入了 Prefetching API，它提供了一种在需要显示数据之前预先准备数据的机制，旨在提高数据的滚动性能。</p>
<p>首先，我先和大家介绍一个概念：无限滚动，无限滚动是可以让用户连续的加载内容，而无需分页。在 UI 初始化的时候 App 会加载一些初始数据，然后当用户滚动快要到达显示内容的底部时加载更多的数据。</p>
<p>多年来，像 Instagram, Twitter 和 Facebook 这样的社交媒体公司都使这种技术。如果查看他们的 App ，你就可以看到无限滚动的实际效果，这里我就给大伙展示下 Instagram 的效果吧！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ed499f840cc457d91ac0dc2074dfa12~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">如何实现</h2>
<p>由于 Instagram 的 UI 过于复杂，在这我就不去模仿实现了，但是我模仿了它的加载机制，同样的实现了一个简单的数据无限滚动和无缝加载的效果。</p>
<p>简单的说下我的思路：</p>
<p>先自定义一个 Cell 视图，这个视图由一个 UILabel 和 一个 UIImageView 构成，用于显示文本和网络图片；然后模拟网络请求来获取数据，注意该步骤一定是异步执行的；最后用 UITableView 来显示返回的数据，在 viewDidLoad 中先请求网络数据来获取一些初始化数据，然后再利用 UITableView 的 Prefetching API 来对数据进行预加载，从而来实现数据的无缝加载。</p>
<p>那关于无限滚动该如何实现呢！其实这个无限滚动并不是真正意义上的永无止尽，严格意义上来讲它是有尽头的，只不过这个功能背后的数据是不可估量的，只有大量的数据做支持才能让应用一直不断的从服务端获取数据。</p>
<p>正常情况下，我们在构建 UITableView 这个控件的时候，需要对它的行数（numsOfRow）做一个初始化，这个行数对我们实现无限加载和无缝加载是一个很关键的因素，假设我们每次根据服务端返回的数据量去更新 UITableView 的行数并 Reload，那我之前说的 Prefetching API 在这种情况下就失去作用了，因为它起作用的前提是要保证预加载数据时 UITableView 当前的行数要小于它的总行数。当然前者也可以实现数据加载，但它的效果就不是无缝加载，它在每次加载数据的时候都会有一个 Loading 等待的时间。</p>
<p>回到我上面所说的无限滚动, 其实实现起来并不难，正常情况下，我们向服务端请求大量相同类型的数据的时候，都会提供一个接口，我称之为分页请求接口，该接口在每次数据返回的时候，都会告诉客户端总共有多少页数据，每页的数据量是多少，当前是第几页，这样我们就能计算出来总共的数据有多少，而这就是 UITableView 的总行数。</p>
<p>响应数据的示范如下（为清楚起见，它仅显示与分页有关的字段）：</p>
<pre><code class="copyable">&#123;

  "has_more": true,
  "page": 1,
  "total": 84,
  "items": [
 
    ...
    ...
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面，我就用代码来一步步的实现它吧！</p>
<h3 data-id="heading-3">模拟分页请求</h3>
<p>由于没有找到合适的分页测试接口，于是我自己模拟一了一个分页请求接口，每次调用该接口的时候都延时 2s 来模拟网络请求的状态，代码如下：</p>
<pre><code class="copyable"> func fetchImages() &#123;
        guard !isFetchInProcess else &#123;
            return
        &#125;
        
        isFetchInProcess = true
        // 延时 2s 模拟网络环境
        print("+++++++++++ 模拟网络数据请求 +++++++++++")
        DispatchQueue.global().asyncAfter(deadline: DispatchTime.now() + 2) &#123;
            print("+++++++++++ 模拟网络数据请求返回成功 +++++++++++")
            DispatchQueue.main.async &#123;
                self.total = 1000
                self.currentPage += 1
                self.isFetchInProcess = false
                // 初始化 30个 图片
                let imagesData = (1...30).map &#123;
                    ImageModel(url: baseURL+"\($0).png", order: $0)
                &#125;
                self.images.append(contentsOf: imagesData)

                if self.currentPage > 1 &#123;
                    let newIndexPaths = self.calculateIndexPathsToReload(from: imagesData)
                    self.delegate?.onFetchCompleted(with: newIndexPaths)
                &#125; else &#123;
                    self.delegate?.onFetchCompleted(with: .none)
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据回调处理：</p>
<pre><code class="copyable">extension ViewController: PreloadCellViewModelDelegate &#123;
        
    func onFetchCompleted(with newIndexPathsToReload: [IndexPath]?) &#123;
        guard let newIndexPathsToReload = newIndexPathsToReload else &#123;
            tableView.tableFooterView = nil
            tableView.reloadData()
            return
        &#125;
        
        let indexPathsToReload = visibleIndexPathsToReload(intersecting: newIndexPathsToReload)
        indicatorView.stopAnimating()
        tableView.reloadRows(at: indexPathsToReload, with: .automatic)
    &#125;
    
    func onFetchFailed(with reason: String) &#123;
        indicatorView.stopAnimating()
        tableView.reloadData()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">预加载数据</h3>
<p>首先如果你想要 UITableView 预加载数据，你需要在 viewDidLoad（） 函数中插入如下代码，并且请求第一页的数据：</p>
<pre><code class="copyable">override func viewDidLoad() &#123;
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        ...
        tableView.prefetchDataSource = self
        ...
         // 模拟请求图片
        viewModel.fetchImages()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，你需要实现 UITableViewDataSourcePrefetching 的协议，它的协议里包含俩个函数：</p>
<pre><code class="copyable">// this protocol can provide information about cells before they are displayed on screen.

@protocol UITableViewDataSourcePrefetching <NSObject>

@required

// indexPaths are ordered ascending by geometric distance from the table view
- (void)tableView:(UITableView *)tableView prefetchRowsAtIndexPaths:(NSArray<NSIndexPath *> *)indexPaths;

@optional

// indexPaths that previously were considered as candidates for pre-fetching, but were not actually used; may be a subset of the previous call to -tableView:prefetchRowsAtIndexPaths:
- (void)tableView:(UITableView *)tableView cancelPrefetchingForRowsAtIndexPaths:(NSArray<NSIndexPath *> *)indexPaths;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个函数会基于当前滚动的方向和速度对接下来的 IndexPaths 进行 Prefetch，通常我们会在这里实现预加载数据的逻辑。</p>
<p>第二个函数是一个可选的方法，当用户快速滚动导致一些 Cell 不可见的时候，你可以通过这个方法来取消任何挂起的数据加载操作，有利于提高滚动性能, 在下面我会讲到。</p>
<p>实现这俩个函数的逻辑代码为：</p>
<pre><code class="copyable">extension ViewController: UITableViewDataSourcePrefetching &#123;
    // 翻页请求
    func tableView(_ tableView: UITableView, prefetchRowsAt indexPaths: [IndexPath]) &#123;
        let needFetch = indexPaths.contains &#123; $0.row >= viewModel.currentCount&#125;
        if needFetch &#123;
            // 1.满足条件进行翻页请求
            indicatorView.startAnimating()
            viewModel.fetchImages()
        &#125;
        
        for indexPath in indexPaths &#123;
            if let _ = viewModel.loadingOperations[indexPath] &#123;
                return
            &#125;
            
            if let dataloader = viewModel.loadImage(at: indexPath.row) &#123;
                print("在 \(indexPath.row) 行 对图片进行 prefetch ")
                // 2 对需要下载的图片进行预热
                viewModel.loadingQueue.addOperation(dataloader)
                // 3 将该下载线程加入到记录数组中以便根据索引查找
                viewModel.loadingOperations[indexPath] = dataloader
            &#125;
        &#125;
    &#125;

    
    func tableView(_ tableView: UITableView, cancelPrefetchingForRowsAt indexPaths: [IndexPath])&#123;
        // 该行在不需要显示的时候，取消 prefetch ，避免造成资源浪费
        indexPaths.forEach &#123;
            if let dataLoader = viewModel.loadingOperations[$0] &#123;
                print("在 \($0.row) 行 cancelPrefetchingForRowsAt ")
                dataLoader.cancel()
                viewModel.loadingOperations.removeValue(forKey: $0)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，再加上俩个有用的方法该功能就大功告成了：</p>
<pre><code class="copyable">    // 用于计算 tableview 加载新数据时需要 reload 的 cell
    func visibleIndexPathsToReload(intersecting indexPaths: [IndexPath]) -> [IndexPath] &#123;
        let indexPathsForVisibleRows = tableView.indexPathsForVisibleRows ?? []
        let indexPathsIntersection = Set(indexPathsForVisibleRows).intersection(indexPaths)
        return Array(indexPathsIntersection)
    &#125;
    
    // 用于确定该索引的行是否超出了目前收到数据的最大数量
    func isLoadingCell(for indexPath: IndexPath) -> Bool &#123;
        return indexPath.row >= (viewModel.currentCount)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>见证时刻的奇迹到了，请看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a998218cf5047e7922557aa5bf4f88a~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过日志，我们也可以清楚的看到，在滚动的过程中是有 Prefetch 和 CancelPrefetch 操作的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01abebef331c4325b869966dfdeee0d1~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，到这里我就简单的实现了 UITableView 无尽滚动和对数据无缝加载的效果，你学会了吗？</p>
<h2 data-id="heading-5">如何避免滚动时的卡顿</h2>
<p>当你遇到滚动卡顿的应用程序时，通常是由于任务长时间运行阻碍了 UI 在主线程上的更新，想让主线程有空来响应这类更新事件，第一步就是要将消耗时间的任务交给子线程去执行，避免在获取数据时阻塞主线程。</p>
<p>苹果提供了很多为应用程序实现并发的方式，例如 GCD，我在这里对 Cell 上的图片进行异步加载使用的就是它。</p>
<p>代码如下：</p>
<pre><code class="copyable">class DataLoadOperation: Operation &#123;
    var image: UIImage?
    var loadingCompleteHandle: ((UIImage?) -> ())?
    private var _image: ImageModel
    private let cachedImages = NSCache<NSURL, UIImage>()
    
    init(_ image: ImageModel) &#123;
        _image = image
    &#125;
    
    public final func image(url: NSURL) -> UIImage? &#123;
        return cachedImages.object(forKey: url)
    &#125;
    
    override func main() &#123;
        if isCancelled &#123;
            return
        &#125;
        
        guard let url = _image.url else &#123;
            return
        &#125;
        downloadImageFrom(url) &#123; (image) in
            DispatchQueue.main.async &#123; [weak self] in
                guard let ss = self else &#123; return &#125;
                if ss.isCancelled &#123; return &#125;
                ss.image = image
                ss.loadingCompleteHandle?(ss.image)
            &#125;
        &#125;
        
    &#125;
    
    // Returns the cached image if available, otherwise asynchronously loads and caches it.
    func downloadImageFrom(_ url: NSURL, completeHandler: @escaping (UIImage?) -> ()) &#123;
        // Check for a cached image.
        if let cachedImage = image(url: url) &#123;
            DispatchQueue.main.async &#123;
                print("命中缓存")
                completeHandler(cachedImage)
            &#125;
            return
        &#125;
        
        URLSession.shared.dataTask(with: url as URL) &#123; data, response, error in
            guard
                let httpURLResponse = response as? HTTPURLResponse, httpURLResponse.statusCode == 200,
                let mimeType = response?.mimeType, mimeType.hasPrefix("image"),
                let data = data, error == nil,
                let _image = UIImage(data: data)
                else &#123; return &#125;
            // Cache the image.
            self.cachedImages.setObject(_image, forKey: url, cost: data.count)
            completeHandler(_image)
            &#125;.resume()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那具体如何使用呢！别急，听我娓娓道来，这里我再给大家一个小建议，大家都知道 UITableView 实例化 Cell 的方法是：tableView:cellForRowAtIndexPath: ，相信很多人都会在这个方法里面去进行数据绑定然后更新 UI，其实这样做是一种比较低效的行为，因为这个方法需要为每个 Cell 调用一次，它应该快速的执行并返回重用 Cell 的实例，不要在这里去执行数据绑定，因为目前在屏幕上还没有 Cell。我们可以在 tableView:willDisplayCell:forRowAtIndexPath: 这个方法中进行数据绑定，这个方法在显示cell之前会被调用。</p>
<p>为每个 Cell 执行下载任务的实现代码如下：</p>
<pre><code class="copyable"> func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell &#123;
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "PreloadCellID") as? ProloadTableViewCell else &#123;
            fatalError("Sorry, could not load cell")
        &#125;
        
        if isLoadingCell(for: indexPath) &#123;
            cell.updateUI(.none, orderNo: "\(indexPath.row)")
        &#125;
        
        return cell
    &#125;
    
    
    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) &#123;
        // preheat image ，处理将要显示的图像
        guard let cell = cell as? ProloadTableViewCell else &#123;
            return
        &#125;

        // 图片下载完毕后更新 cell
        let updateCellClosure: (UIImage?) -> () = &#123; [unowned self] (image) in
            cell.updateUI(image, orderNo: "\(indexPath.row)")
            viewModel.loadingOperations.removeValue(forKey: indexPath)
        &#125;

        // 1. 首先判断是否已经存在创建好的下载线程
        if let dataLoader = viewModel.loadingOperations[indexPath] &#123;
            if let image = dataLoader.image &#123;
                // 1.1 若图片已经下载好，直接更新
                cell.updateUI(image, orderNo: "\(indexPath.row)")
            &#125; else &#123;
                // 1.2 若图片还未下载好，则等待图片下载完后更新 cell
                dataLoader.loadingCompleteHandle = updateCellClosure
            &#125;
        &#125; else &#123;
            // 2. 没找到，则为指定的 url 创建一个新的下载线程
            print("在 \(indexPath.row) 行创建一个新的图片下载线程")
            if let dataloader = viewModel.loadImage(at: indexPath.row) &#123;
                // 2.1 添加图片下载完毕后的回调
                dataloader.loadingCompleteHandle = updateCellClosure
                // 2.2 启动下载
                viewModel.loadingQueue.addOperation(dataloader)
                // 2.3 将该下载线程加入到记录数组中以便根据索引查找
                viewModel.loadingOperations[indexPath] = dataloader
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对预加载的图片进行异步下载（预热）：</p>
<pre><code class="copyable">func tableView(_ tableView: UITableView, prefetchRowsAt indexPaths: [IndexPath]) &#123;
        let needFetch = indexPaths.contains &#123; $0.row >= viewModel.currentCount&#125;
        if needFetch &#123;
            // 1.满足条件进行翻页请求
            indicatorView.startAnimating()
            viewModel.fetchImages()
        &#125;
        
        for indexPath in indexPaths &#123;
            if let _ = viewModel.loadingOperations[indexPath] &#123;
                return
            &#125;
            
            if let dataloader = viewModel.loadImage(at: indexPath.row) &#123;
                print("在 \(indexPath.row) 行 对图片进行 prefetch ")
                // 2 对需要下载的图片进行预热
                viewModel.loadingQueue.addOperation(dataloader)
                // 3 将该下载线程加入到记录数组中以便根据索引查找
                viewModel.loadingOperations[indexPath] = dataloader
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取消 Prefetch 时，cancel 任务，避免造成资源浪费</p>
<pre><code class="copyable">func tableView(_ tableView: UITableView, cancelPrefetchingForRowsAt indexPaths: [IndexPath])&#123;
        // 该行在不需要显示的时候，取消 prefetch ，避免造成资源浪费
        indexPaths.forEach &#123;
            if let dataLoader = viewModel.loadingOperations[$0] &#123;
                print("在 \($0.row) 行 cancelPrefetchingForRowsAt ")
                dataLoader.cancel()
                viewModel.loadingOperations.removeValue(forKey: $0)
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过这般处理，我们的 UITableView 滚动起来肯定是如丝般顺滑，小伙伴们还等什么，还不赶紧试一试。</p>
<h2 data-id="heading-6">图片缓存</h2>
<p>虽然我在上面对我的应用增加了并发操作，但是我一看 Xcode 的性能分析，我不禁陷入了沉思，我的应用程序太吃内存了，假如我不停的刷，那我的手机应该迟早会把我的应用给终止掉，下图是我刷到 200 行的时候的性能分析图：</p>
<p><strong>内存</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4e0ee803e0e4596a9ebb4f0e9e1bff9~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>磁盘</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2856526018814b07afb33933b51b8e08~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到我的应用的性能分析很不理想，究其原因在于我的应用里显示了大量的图片资源，每次来回滚动的时候，都会重新去下载新的图片，而没有对图片做缓存处理。</p>
<p>所以，针对这个问题，我为我的应用加入了缓存 NSCache 对象，来对图片做一个缓存，具体代码实现如下：</p>
<pre><code class="copyable">class ImageCache: NSObject &#123;

    private var cache = NSCache<AnyObject, UIImage>()
    public static let shared = ImageCache()
    private override init() &#123;&#125;
   
    func getCache() -> NSCache<AnyObject, UIImage> &#123;
       return cache
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在下载开始的时候，检查有没有命中缓存，如果命中则直接返回图片，否则重新下载图片，并添加到缓存中：</p>
<pre><code class="copyable">func downloadImageFrom(_ url: URL, completeHandler: @escaping (UIImage?) -> ()) &#123;
        // Check for a cached image.
        if let cachedImage = getCacheImage(url: url as NSURL) &#123;
            print("命中缓存")
            DispatchQueue.main.async &#123;
                completeHandler(cachedImage)
            &#125;
            return
        &#125;
        
        URLSession.shared.dataTask(with: url) &#123; data, response, error in
            guard
                let httpURLResponse = response as? HTTPURLResponse, httpURLResponse.statusCode == 200,
                let mimeType = response?.mimeType, mimeType.hasPrefix("image"),
                let data = data, error == nil,
                let _image = UIImage(data: data)
                else &#123; return &#125;
            
            // Cache the image.
            ImageCache.shared.getCache().setObject(_image, forKey: url as NSURL)

            completeHandler(_image)
            &#125;.resume()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了缓存的加持后，再用 Xcode 来查看我的应用的性能，就会发现内存和磁盘的占用已经下降了很多：</p>
<p><strong>内存</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92df851def9f48a68dc4efc90d80a8cb~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>磁盘</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/217ec2c9b4864b02a67d4ba8252d5f22~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于图片缓存的技术，这里只是用了最简单的一种，外面很多开源的图片库都有不同的缓存策略，感兴趣的可以去 GitHub 上学习一下它们的源码，我在这里就不做赘述了。</p>
<h2 data-id="heading-7">最后</h2>
<p>终于写完了，长舒了一口气，这篇文章的篇幅有点长，主要是我花了一点时间做调研，然后看到这个知识点想给大家讲一下，看到那个知识点也想给大家讲一下，最终引经据典（东拼西凑）完成了这篇文章，希望大家能够喜欢 ：）。</p>
<p>按照国际惯例，最后附上项目工程地址：<a href="https://github.com/ShenJieSuzhou/ProloadDemo" target="_blank" rel="nofollow noopener noreferrer">github.com/ShenJieSuzh…</a></p>
<p><strong>相关阅读：</strong></p>
<p><a href="https://juejin.cn/post/6944994974614323213" target="_blank">UICollectionView 自定义布局！看这篇就够了</a></p>
<p><a href="https://juejin.cn/post/6942356138960617508" target="_blank">Swift  探索 UICollectionView 之 SupplementaryView 和 Decoration View</a></p>
<p><a href="https://juejin.cn/editor/drafts/6940137857952514079" target="_blank">Swift 自定义布局实现 Cover Flow 效果</a></p>
<p><a href="https://juejin.cn/post/6937473612911902727" target="_blank">UICollectionView 自定义布局实现瀑布流视图</a></p>
<p><a href="https://juejin.cn/post/6923007642168852494" target="_blank">使用 UICollectionView 实现分页滑动效果</a></p>
<p><a href="https://juejin.cn/post/6921514605810286606" target="_blank">使用 UICollectionView 实现首页卡片轮播效果</a></p>
<blockquote>
<p>关注我的技术公众号"<a href="https://user-gold-cdn.xitu.io/2020/7/4/17318f81cd4e34e9?w=173&h=173&f=jpeg&s=14515" target="_blank" rel="nofollow noopener noreferrer">HelloWorld杰少</a>"，获取更多优质技术文章。</p>
</blockquote></div>  
</div>
            