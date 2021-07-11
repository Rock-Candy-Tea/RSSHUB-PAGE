
---
title: '无限无缝自动轮播滚动列表 IntersectionObserver实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e4bf3b8338049deae368d23a20c4dab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 01:19:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e4bf3b8338049deae368d23a20c4dab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>在一个数据看板项目中，需要实现一个像 LED 屏幕一样，无限无缝轮播学生数据的组件，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e4bf3b8338049deae368d23a20c4dab~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-07-11 at 15.20.21.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>“这还不简单，直接用 Swiper 啊！”<br>
然而实在不想为了这一小功能而引入一个 4M 大小的 Npm 包，于是决定自己动手实现</p>
<h3 data-id="heading-1">思路</h3>
<p>直接把所有数据放在 Dom 中，之后用 <code>Css Animation</code> 控制它们持续向上，显然是不可能的，咱们的数据可能有成千上万条<br>
所以肯定需要 JS 的介入，来在某些时机动态地删改数据</p>
<p>但也不能直接定时地对数据进行 shift + push 操作，否则数据元素的位置会瞬间偏移到上方</p>
<p>我想到的是，把数据分为上下两块 A 和 B，让其自然向上移动，当滚动到 A、B 的交界处碰到容器上边缘（即 A 完全看不到）时，将 A -> B，B -> C，并重置动画，如下 Demo 所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d692854c81c4e179779ae3cc06f6f98~tplv-k3u1fbpfcp-watermark.image" alt="Kapture 2021-07-11 at 15.51.30.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如此便实现了旧数据的删除与新数据的增加，并且视窗内的数据元素从肉眼看上去是无缝衔接的</p>
<h3 data-id="heading-2">实现方式1</h3>
<p>思路有了，接下来就是代码的实现方式</p>
<p>首先我想当然地，用 <code>CSS Animation</code> 让容器内的数据的 top 值不断减小（负数），同时 JS 利用 <code>setInterval</code> 在恰好的时间节点动态地更替数据</p>
<p>然而重点就在于，这个“恰好的时间节点”是无法把控的，首先 JS 的定时器本就不完全精确，另外 CSS 与 JS 的定时器更不会如我们所愿地完全一致</p>
<h3 data-id="heading-3">实现方式2</h3>
<p>既然 JS 和 CSS 不愿顺从彼此，那就只能二选一了</p>
<p>于是我把动画也交给 JS 来执行，让其在 <code>window.requestAnimationFrame</code> 中按照一定频率增加对应元素的 top 值，并在其值增加到一定节点时操作数据</p>
<p>如此是能呈现出预期效果，但也产生了新的问题：</p>
<ul>
<li>top 值改变的频率与单位值如果小了，视觉上会出现明显的跳帧（可用 <code>transitions</code> 来修补过渡）</li>
<li>由于是 JS 通过 DOM 操作实现的动画，性能成本一下高了起来，在低端机器上将卡得惨不忍睹...</li>
</ul>
<h3 data-id="heading-4">最终方式</h3>
<p>术业有专攻，看来动画还是得交给 CSS 来实现，那么问题就回到了如何保持 CSS 与 JS 改变时机的一致性<br>
定时器已经行不通了，所以 JS 需要寻找新的方式来感知数据元素们所在的位置</p>
<p>于是我把目光转向了一个较冷门的 API：<code>IntersectionObserver</code>（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F11%2Fintersectionobserver_api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/11/intersectionobserver_api.html" ref="nofollow noopener noreferrer">教程在此</a>）</p>
<p>在对一个 Dom 进行 <code>observe</code> 后，便能及时得知其可见状态的改变，因此我们可以很方便地在 A 数据由可见 -> 不可见时收到通知，进行数据更替操作<br>
而因为交叉观察器只会在元素的可见状态改变时触发 callback，因此性能问题也无需担心</p>
<h3 data-id="heading-5">安全边际</h3>
<p>由于 <code>IntersectionObserver</code> 是异步的（包括主流的 <code>setState</code>等也是），因此要是数据在动画重置时还没有完成更替，可就露馅了，所以我们不妨留点安全边际</p>
<p>例如数据块 A：10条数据，B：5条数据<br>
在滚动到第5条数据不可见时，咱就先对前5条数据进行更替，如此数据在滚动到第10条数据不可见时肯定已经更新完毕，可以放心地重置动画，动画重置后，再对余下的10条数据进行全部更新</p>
<h3 data-id="heading-6">浏览器兼容性</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/131d2be905b5486aa915972210e1e245~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>绝大多数浏览器是不用担心的了<br>
再不济，咱还有 <code>polyfill</code>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fintersection-observer" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/intersection-observer" ref="nofollow noopener noreferrer">intersection-observer</a></p></div>  
</div>
            