
---
title: '聊聊各端手势体系以及对 Web 标准手势的思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48bc138d960e453185107e620a42cdf3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 19:16:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48bc138d960e453185107e620a42cdf3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「北海 Kraken」是一款基于 Flutter 的 Web 渲染引擎，通过基于 W3C 标准来开发实现前端开发者常用的能力。 Kraken 团队也积极探索定义新的问题以及能力，期望通过参推动标准定制的方式让 Web 技术变得更好。
欢迎大家关注 「北海 Kraken」： <a href="http://openkraken.com/" target="_blank" rel="nofollow noopener noreferrer">openkraken.com/</a></p>
</blockquote>
<p>在过去，早期的 Web 更多用做内容展示的页面，最早从后端框架中直出，再配上各种 CSS 以及 JS 的交互内容，以完成最终对页面内容的展示，那时候的 Web 更多属于 【内容开发】，做内容的直出与展示。而如今现代 Web 开发体系已经有了翻天覆地的变化，早已超出了【内容开发】的范畴，在各个领域都有 JavaScript 的身影。同样，Web 也已经脱离了客户端以及浏览器的限制，各式各样基于 Web 标准或者私有标准的 Web runtime 层出不穷。【Web 应用开发】区别于传统的【内容开发】，它对开发者提出了更高的要求，也对 Web 的能力提出了更高的要求，无论是基于标准化方面的考量，还是基于对易用性的考虑，我们都期望 Web 开发者可以获得通过更高级的封装的标准的高性能的能力。</p>
<p>而手势能力就是其中的一块。</p>
<p>目前在 Web 标准中，手势能力是属于缺失的一块能力，更多的开发者通过 <a href="http://hammerjs.github.io/" target="_blank" rel="nofollow noopener noreferrer">hammer.js</a> 来获得一个通过 JavaScript 模拟出来的手势事件来开发一个手势强交互的应用，或者是直接基于更底层的 <a href="https://www.w3.org/TR/touch-events/" target="_blank" rel="nofollow noopener noreferrer">Touch event</a>来做进一步的封装。</p>
<p>但是无论是类 <a href="http://hammerjs.github.io/" target="_blank" rel="nofollow noopener noreferrer">hammer.js</a> 的前端手势方案，还是 <a href="https://www.w3.org/TR/touch-events/" target="_blank" rel="nofollow noopener noreferrer">Touch event</a>的封装，都会导致一些问题，我将从易用性、性能、标准化的角度来做进一步的分析：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48bc138d960e453185107e620a42cdf3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>易用性：</strong>
开发者必须手动去实现或者封装更高一级的手势能力，无法直接从 element 上获得某个高级手势的 event 事件。无论是开发成本，都需要额外加载或者执行额外的 CDN，都是对前端资源的一种损耗。</li>
<li><strong>性能：</strong>
通过 JavaScript 实现的方案需要频繁地通过 Bridge 将手势的能力传递到前端，然后再去计算模拟相关的手势事件。频繁的传递数据增加了 Bridge 的消耗，不断执行的 JavaScript 会阻塞 UI 线程，如果需要更强大的手势能力支撑，我们必须进一步封装【竞争场】等能力的实现来达到手势竞争的目的，而这部分能力本应下沉到渲染引擎本身，而不是在 JavaScript 中处理。</li>
<li><strong>标准化：</strong>
各个开发者实现的标准不统一，判断的基准不一致，透出的 event 能力不对齐会导致各个平台甚至到各个页面的标准不统一。譬如说在同一个 iOS 设备上访问两个不同开发者开发的页面，不统一的手势能力可能会给用户带来及其糟糕的体验。非标准化的手势能力在各个端上也显得格外突出，下面我介绍各端的手势能力时会介绍这些差异点。</li>
</ul>
<h2 data-id="heading-0">连续手势与离散手势</h2>
<p>首先我需要介绍一下连续手势与离散手势的概念，以便读者可以更好地区分这两种手势的不同，以及了解实现不同的手势能力对开发、性能、易用性等纬度的影响。</p>
<p>首先，我们需要知道，由于在端侧有各种各样的屏幕操作的设备，常见的比如说类 apple pencil 的电子笔设备（pen），手指直接触摸操作（touch），还有鼠标（mouse）等。所以在 <a href="https://www.w3.org/TR/pointerevents/" target="_blank" rel="nofollow noopener noreferrer">W3C 标准</a>中， 将所有的接触屏幕的物理设备抽象成了一个 <a href="https://www.w3.org/TR/pointerevents/#intro" target="_blank" rel="nofollow noopener noreferrer">pointer</a>，无论上层是那种物理设备，对于屏幕只感知与抽象这一个触摸到的点，基于 type 区分具体的上层的物理设备。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd0a91c972b4d2d836ef7994b849b11~tplv-k3u1fbpfcp-zoom-1.image" alt="pointer" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个完整的手势包含了手指开始接触屏幕（pointer down），然后手指在屏幕上进行偏移（pointer move），以及手指抬起离开屏幕（pointer up），暂时不讨论 cancel、out 等情况。当然，其中中间 pointer move 的过程是可以省略的，最常见的省略 pointer move 的手势譬如说 click 或者 long press 等（当然，如果点击设备不是一个鼠标而是一根手指，其实手指实际接触是肯定会产生轻微移动情况的，譬如在 FLutter 中，允许这个细微的移动距离在 18 个像素点内，即视为不移动）。可以预见的是未来会有更多的物理设备操作屏（甚至不是屏），基于底层触摸点的 pointer 抽象有利于上层做更多的扩展。</p>
<p>了解了这些，接下来我们来了解一下连续手势与离散手势的差异。</p>
<ul>
<li>连续手势：从 pointer down 到 pointer moves 到 pointer up，中间过程可以通过 state 状态来描述的手势，可以清楚地通过不同的回调或者不同的状态让开发者感知目前手势所处的状态的手势。常见连续手势：pan。</li>
<li>离散手势：完整手势触发完毕后才会通过回调来通知开发者，无中间状态的转换。常见离散手势：click。</li>
</ul>
<p>连续手势会频繁通过回调或者状态来通知开发者目前手势所处的状态，我们来看一种情况：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">element.addEventLisenter(<span class="hljs-string">'pan'</span>, <span class="hljs-function">(<span class="hljs-params">gestureEvent</span>) =></span> &#123;
<span class="hljs-keyword">if</span> (gestureEvent.state === <span class="hljs-string">'up'</span>) &#123;
<span class="hljs-comment">// do something...</span>
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设我们需要在 Web 标准中实现 pan 这个手势，如果它是一个连续手势，而我们的场景只需要用 up 这种状态，就需要不断地将当前的状态通过 Bridge 以及 JS engine 传递到 JavaScript 中，这频繁的传递开销是对设备性能的一种浪费。当然，也有框架方案通过更加细分的粒度去解决这个事情，譬如说拆分成 <code>panstart</code>、<code>panupdate</code>、<code>panend</code>等，当开发者不给这些方法注册回调时，可以在框架内部判断并做相应优化。然而细分的 API 抽象不够底层，对于开发者来说也并不那么友好。</p>
<p>而对于离散手势，我们则不需要考虑手势过程中的状态传递，只需要把最终的结果返回给开发者即可，离散手势屏蔽了许多内部处理的细节，保证了开发者注册的回调只能完整的手势操作完以后才能被命中。有效地降低了连续手势数据的传递量。但是相较于连续手势，离散手势的缺点是开发者无法很好地感知中间状态。</p>
<p>接下来我们来看一下各个端上实现的手势体系、优缺点以及差异性。</p>
<h2 data-id="heading-1">各端手势体系</h2>
<h3 data-id="heading-2">hammer.js</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ccd69d567784fb1ac1c310314bb3ab7~tplv-k3u1fbpfcp-zoom-1.image" alt="hammer" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Pan</li>
</ul>
<p>Pan  的需要有一个最小距离以及方向，只要达到这个条件可以频繁触发。
详见：<a href="https://github.com/hammerjs/hammer.js/blob/master/src/recognizers/pan.js#L42" target="_blank" rel="nofollow noopener noreferrer">github.com/hammerjs/ha…</a></p>
<ul>
<li>Swipe</li>
</ul>
<p>距离与速度达到一定阈值的滑动。
详见：<a href="https://github.com/hammerjs/hammer.js/blob/master/src/recognizers/swipe.js#L36" target="_blank" rel="nofollow noopener noreferrer">github.com/hammerjs/ha…</a></p>
<ul>
<li>Pinch （向外捏时放大，向内捏时缩小）</li>
<li>Press （长按，默认时间在 250 ms 以上 ，替代了 long press）</li>
</ul>
<p>详见：<a href="https://github.com/hammerjs/hammer.js/blob/master/src/recognizers/press.js#L78" target="_blank" rel="nofollow noopener noreferrer">github.com/hammerjs/ha…</a></p>
<p>hammer.js 作为一个前端实现的 gesture lib，通过注册 Touch 事件做封装来完成具体的操作的判断，在前端做手势的方案在前面已经提过，需要不断地通过 Bridge 以及 JS engine 传递到 JavaScript 中，然后才能最终在 JavaScript 中处理手势操作，只要有操作就会被抛到 JavaScript 中进行处理，频繁的传递耗费了许多不必要的性能。我们更希望这部分能力可以下沉到渲染引擎本身，这样可以节省非常多不必要的数据传递开销。</p>
<p>如果在基础手势判断之上想进一步引入更加复杂的【竞技场】等能力，这部分会使得 JavaScript 中的逻辑更加复杂，即便抛开“能不能”在前端做相关实现来说，过多的 JavaScript 运行占用计算资源也是我们并不想要的。</p>
<p>同时，需要单独引入一个 CDN 脚本来支持相关的功能，对于包体积以及首屏也增加了额外的成本。但是又考虑到本身浏览器并不自带这些功能，一般开发者也无法很好地将这套方案优化并下沉到浏览器中，所以在反而在大部分前端业务场景成为来较优的技术选型。</p>
<h3 data-id="heading-3">Flutter</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e48de2c55fc542ac9a8ba625ce493ad9~tplv-k3u1fbpfcp-zoom-1.image" alt="Flutter" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Tap</li>
<li>Double tap</li>
<li>Long press （500 ms 以上的长按）</li>
<li>Vertical(Horizontal) drag  横（纵）滑</li>
</ul>
<p>在 drag 上做了进一步封装，在 x 轴或者 y 轴偏移超过最小距离并达到阈值速度可触发。</p>
<ul>
<li>scale</li>
</ul>
<p>scale 会包含放大缩小以及旋转的手势，相当于其他端中的 Pinch + Rotation</p>
<ul>
<li>Pan</li>
</ul>
<p>Pan 内部实现，需要达到一个最小速度以及最小移动距离的 drag 才能触发 Pan，Pan 是基于 drag 之上的封装，增加了判断。Flutter 内置一个 pointer down + pointer moves + pointer up 只能触发一次手势，所以 Pan 只能触发一次（与 hammer 不同，为有状态手势）
详见： <a href="https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/gestures/monodrag.dart#L579" target="_blank" rel="nofollow noopener noreferrer">github.com/flutter/flu…</a></p>
<p>Flutter 的手势体系除了 Long press 均为连续手势，无离散手势，Tap 也会通过 TapDown、TapUp 等状态来完成。每个中间状态会通过不同的回调函数来支持开发者处理逻辑，返回参数也根据中间状态的不同而不同。排除 Widget 的统一封装来看，跟安卓类似，回调过多，且返回参数不统一，不利于标准化。但是对于内部的手势回调来说，细分的接口各司其职，传递所需的参数都是必须的，开发者可以直接获取具体的返回信息。</p>
<h3 data-id="heading-4">iOS</h3>
<ul>
<li>Tap（离散手势，100 ms 左右的点击行为）</li>
<li>Long Press (连续手势，500 ms 以上的点击行为)</li>
<li>Pan （连续手势，平移，类似 drag，但是可以在移动过程中不断变化方向）</li>
<li>Swipe （离散手势）</li>
<li>Pinch（连续手势，向外捏时放大，向内捏时缩小）</li>
<li>Rotation（连续手势，旋转）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb15ca0c80f4fb396ac26d748c04c1d~tplv-k3u1fbpfcp-zoom-1.image" alt="iOS手势" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了方便大家了解各个手势的区别，尤其是 Pan 跟 Swipe 的区别，特地放上了<a href="https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures" target="_blank" rel="nofollow noopener noreferrer">iOS 开发者文档的一些图片</a>。</p>
<p>iOS 的手势可以带上多个 touch pointer，同时满足了几个手指操作的能力。比如三指滑动（三根手指的swipe）、双指点击（两根手指的 Tap）等。它提供了开发者对某一个手势处理成一个注册回调函数，通过 state 判断目前手势的状态。离散手势与连续手势共存。</p>
<h3 data-id="heading-5">Android</h3>
<ul>
<li>View 上直接提供 click 以及 touch 的一些方法
<ul>
<li>OnDragListener：拖动事件。</li>
<li>OnLongClickListener：长按抬起时的事件。</li>
</ul>
</li>
<li>GestureDetector.OnGestureListener
<ul>
<li>onDown：手势识别器的 down 事件。</li>
<li>onFling： 类似 swipe。</li>
<li>onLongPress： 长按。</li>
<li>onScroll：scroll view 滚动时的事件。</li>
<li>onShowPress：按下后没抬起，相当于（up、move、down 的中间 move 状态，只是没move）。</li>
<li>onSingleTapUp： 点击抬起，对应 onDown。</li>
</ul>
</li>
<li>GestureDetector.OnDoubleTapListener： 双击。</li>
<li>ScaleGestureDetector：旋转，捏，分 begin、onScale、end。</li>
</ul>
<p>相对来说，Android 的手势体系比较细分，大致上跟 FLutter 比较像，但是 Flutter 是不同手势在不同类中的，Flutter 基本上都是离散手势，安卓很多连续手势，但是更加细分。</p>
<h2 data-id="heading-6">标准</h2>
<p>综上分析了 Flutter、iOS、Android 以及一个前端实现的 gesture lib（hammer.js），不难发现，每个端实现的手势方案都大同小异。无非都实现了这几种方法： click（Tap）、swipe、Pan、Long Press （Press）、Pinch 与 Rotation（或者 Scale）。但是各个平台对每个手势的实现还是有些许的差异，无论是具体手势的代码逻辑判断还是具体手势的拆分或者命名，均有不同。</p>
<p>那在 Web 技术上，我们应该使用怎么样一套手势规范，来兼顾易用性、性能以及标准化呢？就目前来看，基于 Web 技术体系发展来的 Web runtime 的已经非常多了，诸如 Web、React Native、小程序等体系已经在端侧带来了巨大的运行时碎片化。未来不止于移动端上，还有各种 IOT 设备出现，可能会有越来越多的 Web runtime 会出现。未来可能会有更多领域会有不一样的终端设备，而折叠屏、柔性屏的到来也可能会让端侧的设备（手机、IOT、车载等）形成更多更复杂的的跨端场景，随之而来的也是更多的交互手势来与这些设备进行“沟通交流”。</p>
<p>很遗憾的是目前 W3C 上没有相应的手势规范，我们更期望有一个统一的既定标准来规范，我们也在 <a href="https://github.com/w3c/chinese-ig" target="_blank" rel="nofollow noopener noreferrer">W3C 中文兴趣小组</a>上发起了一个<a href="https://github.com/w3c/chinese-ig/issues/240" target="_blank" rel="nofollow noopener noreferrer">讨论</a>，目前此讨论已经提到了 <a href="https://github.com/w3c/uievents/issues/293" target="_blank" rel="nofollow noopener noreferrer">UIEvent</a>。我们期望通过易用性、性能以及标准化这几个纬度去讨论手势规范以及对应的手势标准化能力的必要性，以及最终推动规范建立的可行性，也欢迎更多的小伙伴加入该讨论。</p>
<p>此外，该标准提案目前已经在 <a href="http://openkraken.com/" target="_blank" rel="nofollow noopener noreferrer">北海 Kraken</a> 上实现，开发者可以直接使用 <a href="http://openkraken.com/guide/advanced/gesture" target="_blank" rel="nofollow noopener noreferrer">增强的手势能力</a> 来开发复杂的交互应用。后续  <a href="http://openkraken.com/" target="_blank" rel="nofollow noopener noreferrer">北海 Kraken</a> 团队将会在复杂的业务场景上定义出更多问题以及通用能力，期望可以通过参与推动标准定制的方式让 Web 技术变得更好。</p></div>  
</div>
            