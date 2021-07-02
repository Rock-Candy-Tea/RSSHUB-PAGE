
---
title: '疯狂操作 CSS3 实现 60 FPS 动画效果，CodeReview 时同事直呼：细节！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9739876a7e414499ada77df939e08817~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 23:00:37 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9739876a7e414499ada77df939e08817~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
</blockquote>
<h2 data-id="heading-0">前言小叙</h2>
<p>FPS 全称：<strong>Frames per second</strong>，即 <strong>【每秒帧数】</strong> 的意思。</p>
<p>通常来讲，当动画的每秒帧数低于 12 （即 <strong>12 FPS</strong> 以下）时，我们的大脑就能快速从动画中区分出一些静止的图片，所以此时的动画<strong>并不是</strong>无缝动画。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9739876a7e414499ada77df939e08817~tplv-k3u1fbpfcp-watermark.image" alt="vertical-syn-dh02.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一旦播放速率（每秒帧数）达到 <strong>16-24 FPS</strong> 时，大脑就会认为这些画面是连续移动的场景，看起来就是影片的效果了（大部分数字电影拍摄是每秒 24 帧）。</p>
<p>所以，我们可以大致了解到：<strong>FPS 越高，画面越流畅！</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/724a85b2880a4ff6bbc1d039961c55ba~tplv-k3u1fbpfcp-watermark.image" alt="40255c644548a1c4240b2d6ed32101f3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>明白这些后，我们可以便可开始本篇正题了：<strong><em>CSS3 实现 60 FPS 的动画效果！</em></strong></p>
<h2 data-id="heading-1">常规操作</h2>
<p><strong>本瓜知道你会说：“CSS3 动画，有手就行！”</strong></p>
<p>知道我们的目标是实现下图动画效果时，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dacbe0ad7bc84aa4bbcccb2e565ebc27~tplv-k3u1fbpfcp-watermark.image" alt="0_rXGvLKSlZGRmz4Jd_.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你信手拈来，一顿操作！</p>
<p>很棒，恭喜你能轻松写出以下这段<strong>超级常规的</strong> CSS3 动画~</p>
<pre><code class="copyable"><div class="layout">
<div class="app-menu"></div>
<div class="header">
<div class="menu-icon"></div>
</div>
</div>

.app-menu &#123;
left: -300px;
transition: left 300ms linear;
&#125;

.app-menu-open .app-menu &#123;
left: 0px;
transition: left 300ms linear;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的实现效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8fddb2619934855ad5d88be994de229~tplv-k3u1fbpfcp-watermark.image" alt="0_ZWyuzfeBSbFbQjOy_.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你确实做到了，<strong>但，到此为止吗？这次，不止于此！</strong></p>
<p>于是，咱打开控制台 <strong>Performance Ctrl+E</strong> 进行录制这段动画来<strong>进一步分析分析</strong>。</p>
<p><a href="https://imagelol.com/image/InlDJh" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/InlDJh.md.png" alt="InlDJh.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>我们可以看到它的 <strong>Timeline</strong> 中 <strong>FPS 指标（绿色部分）</strong></p>
<p><a href="https://imagelol.com/image/InlZIW" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/InlZIW.md.png" alt="InlZIW.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<blockquote>
<ul>
<li>
<p>图中绿色部分的高点表示以 60 FPS 进行渲染，低点则表示以低于 60 FPS 进行渲染；</p>
</li>
<li>
<p>红色条表示卡顿；</p>
</li>
</ul>
</blockquote>
<p>我们发现它存在问题：</p>
<p><strong>1. 绿色部分的高度并不一致，说明 FPS 不稳定；</strong></p>
<p><strong>2. 绿色部分有相当一部分处在低点，说明 FPS 不流畅；</strong></p>
<p><strong>3. 存在很多红色条，说明动画很卡；</strong></p>
<p>所以，结论是：我们这种方法实现的 CSS3 动画，并不流畅！！</p>
<p><strong>我们期望的是：高度齐平，绿色都处于高点，红色条越少越好。</strong> 别方，带着期望，继续往下看！</p>
<h2 data-id="heading-2">进阶操作</h2>
<p>你非常棒，并且异于常人！！你想到了使用 <strong>Transform</strong> 来实现！！</p>
<p>CSS 代码：</p>
<pre><code class="copyable">.app-menu &#123;
-webkit-transform: translateX(-100%);
transform: translateX(-100%);
transition: transform 300ms linear;
&#125;
.app-menu-open .app-menu &#123;
-webkit-transform: none;
transform: none;
transition: transform 300ms linear;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55ea90b1aacb46e3862d5ec3008ae56f~tplv-k3u1fbpfcp-watermark.image" alt="2222.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>控制台看下 Timeline：</p>
<p><a href="https://imagelol.com/image/In8fhU" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/In8fhU.png" alt="In8fhU.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>的确不一样了，<strong>跟【常规操作】中的 Timeline 图作比，高度都更加齐平了！更多绿色部分处于高点了！红色条也减少了！</strong></p>
<p><strong>这表示我们的动画效果，更流畅了！</strong></p>
<ul>
<li>这里动画效果为什么更流畅了呢？暂时按下不表，后文解释。</li>
</ul>
<h2 data-id="heading-3">高级操作</h2>
<p>噢噢噢，原来你是位高级前端，你还会这样 <strong>will-change</strong> 这样高级的操作！</p>
<p>CSS 代码：</p>
<pre><code class="copyable">.app-menu &#123;
-webkit-transform: translateX(-100%);
transform: translateX(-100%);
transition: transform 300ms linear;
will-change: transform;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe1b0f1681044c88181ff10edc3e6e3~tplv-k3u1fbpfcp-watermark.image" alt="333_.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>控制台看下 Timeline：</p>
<p><a href="https://imagelol.com/image/In8CGi" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/In8CGi.png" alt="In8CGi.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><strong>天呐噜！</strong></p>
<p><strong>相较于【进阶操作】，我们更加接近目标：高度基本齐平了！绿色位置绝大部分都处在高位！红条减的更少了！</strong></p>
<p>这么厉害的嘛？不妨再往下看！</p>
<h2 data-id="heading-4">顶级操作</h2>
<p><strong>至此，你的手中还有牌吗？</strong></p>
<p>或许我们还能从 DOM 结构找找突破口！</p>
<p>将前文的 DOM 改造成：</p>
<pre><code class="copyable"><div class="menu">
<div class="app-menu"></div>
</div>
<div class="layout">
<div class="header">
<div class="menu-icon"></div>
</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 layout 区域之外创建 menu，然后使用 js 中的 <strong>transitionend 函数</strong>来监听，使 menu--animatable 类在过渡时间结束时被移除。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d2043f0b0794ef5af5859c6a4ca6cbe~tplv-k3u1fbpfcp-watermark.image" alt="0_EFkarCSe2mQEYK0e_.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>// js</p>
<pre><code class="copyable">function toggleClassMenu() &#123;
myMenu.classList.add("menu--animatable");
if(!myMenu.classList.contains("menu--visible")) &#123;
myMenu.classList.add("menu--visible");
&#125; else &#123;
myMenu.classList.remove('menu--visible');
&#125;
&#125;

function OnTransitionEnd() &#123;
myMenu.classList.remove("menu--animatable");
&#125;

var myMenu = document.querySelector(".menu");
var oppMenu = document.querySelector(".menu-icon");
myMenu.addEventListener("transitionend", OnTransitionEnd, false);
oppMenu.addEventListener("click", toggleClassMenu, false);
myMenu.addEventListener("click", toggleClassMenu, false);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// 完整 css</p>
<pre><code class="copyable">menu &#123;
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 150;
&#125;

.menu--visible &#123;
    pointer-events: auto;
&#125;

.app-menu &#123;
    background-color: #fff;
    color: #fff;
    position: relative;
    max-width: 400px;
    width: 90%;
    height: 100%;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
    -webkit-transform: translateX(-103%);
            transform: translateX(-103%);
    display: flex;
    flex-direction: column;
    will-change: transform;
    z-index: 160;
    pointer-events: auto;            
&#125;

.menu--visible .app-menu &#123;
    -webkit-transform: none;
            transform: none;
&#125;

.menu--animatable .app-menu &#123;
    transition: all 130ms ease-in;
&#125;

.menu--visible.menu--animatable  .app-menu &#123;
    transition: all 330ms ease-out;
&#125;

.menu:after &#123;
    content: '';
    display: block;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.4);
    opacity: 0;
    will-change: opacity;
    pointer-events: none;
    transition: opacity 0.3s cubic-bezier(0,0,0.3,1);
&#125;

.menu--visible.menu:after &#123;
    opacity: 1;
    pointer-events: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的 Timeline：</p>
<p><a href="https://imagelol.com/image/In89lr" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/In89lr.md.png" alt="In89lr.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><strong>这就是 CSS3 实现 60 FPS动画的顶级操作！</strong></p>
<p><strong>高度全部齐平！！全部处在高位！！没有红条！！</strong></p>
<p><strong>这是完美的 FPS 动画！如丝般顺滑！</strong></p>
<p><strong>你做到了！(๑•̀ㅂ•́)و✧</strong></p>
<h2 data-id="heading-5">原理探寻</h2>
<p>我们在此做简单回顾：</p>



































<table><thead><tr><th>级别</th><th>实现核心方式</th><th>FPS 绿块效果</th><th>动画顺滑程度</th></tr></thead><tbody><tr><td>常规操作</td><td><code>transition: left 300ms linear;</code></td><td>高度不齐平、较多处于低点、很多红条</td><td>30% 顺滑</td></tr><tr><td>进阶操作</td><td><code>transition: transform 300ms linear;</code></td><td>高度比较齐平、较少处于低点、较少红条</td><td>60% 顺滑</td></tr><tr><td>高级操作</td><td><code>will-change: transform;</code></td><td>高度基本齐平、很少处于低点、很少红条</td><td>80% 顺滑</td></tr><tr><td>顶级操作</td><td><code>transitionend 函数</code></td><td>高度完全齐平、全部处于高点、没有红条</td><td>100% 顺滑</td></tr></tbody></table>
<p><strong>原理呢？原理还得回归底层，来看看浏览器的渲染机制！</strong></p>
<p><img src="https://s3.jpg.cm/2021/07/02/InXLPw.png" alt="InXLPw.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是浏览器渲染的关键步骤，相信大家都很熟悉：</p>
<ol>
<li>Styles（样式）: 浏览器计算要应用于元素的样式；</li>
<li>Layout（布局）：浏览器计算每个元素生成形状和位置，比如 width、height、margin、left/top/right/bottom 这些；</li>
<li>Paint（渲染）：浏览器将每个元素的像素填充到图层中；</li>
<li>Composite（合成）：浏览器开始在屏幕上绘制所有图层的时候；</li>
</ol>
<p>第 4 步“合成”给了我们很多操作空间：</p>
<p>我们可以使用 <strong>transform</strong> 和 <strong>opacity</strong> 两个属性实现四种最常用的动画：</p>
<ol>
<li>位置动画：translateX(n) translateY(n) translateZ(n);</li>
<li>大小动画：transform: scale(n);</li>
<li>旋转动画：transform: rotate(ndeg);</li>
<li>不透明度动画：opacity: n;</li>
</ol>
<p><strong>在第 4 步操作为什么具有魔法呢？</strong></p>
<p>笨蛋，当然是避免重绘、回流增加渲染负担啦~</p>
<p><a href="https://imagelol.com/image/InXxZu" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/InXxZu.th.png" alt="InXxZu.th.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>所以，我们的【进阶操作】控制 <strong>transform</strong> 比【常规操作】控制 <strong>left</strong> 属性更优！</p>
<p>而【高级操作】中的 <strong>will-change</strong> 能告知浏览器元素会有哪些变化，这样浏览器能在变化之前做好优化准备工作，将一部分复杂计算提前准备好，所以页面的反应更加快速灵敏。</p>
<p>【顶级操作】中改造分离 DOM，然后用 JS控制，手动添加 menu--animatable 类，然后用到 <strong>transitionend 事件</strong> 会在 CSS transition 结束后触发，移除 menu--animatable 类。实现完全体的 60FPS 动画！</p>
<blockquote>
<p><strong>通常来说，我们能做到进阶操作或高级操作中的实现应该就够了，如果在特殊情景下，如对 FPS 要求特别高，我们再开拓思路，启用顶级操作！（顶级操作是把宝刀，一般不拿出来~）</strong></p>
</blockquote>
<h2 data-id="heading-6">写在结尾</h2>
<p>我们都知道编码习惯非常重要，但同时又一直苦于思考，如何将一些原理知识与实际编码结合？！</p>
<p><strong>而本篇是基于浏览器渲染原理，对 CSS3 动画的一个很好结合实践！</strong></p>
<p><strong>CodeReview 时，同事都直呼：细节！</strong></p>
<p>“秒啊~ 我理解的原理知识用来面试，你理解的原理知识用来工作中日常编码，细节！高级！”</p>
<p><a href="https://imagelol.com/image/InXMXG" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.jpg.cm/2021/07/02/InXMXG.th.png" alt="InXMXG.th.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>ok，以上便是本次分享~ 都看到这儿了，撰文不易、需要鼓励~ b(￣▽￣)d</p>
<blockquote>
<p>我是掘金安东尼，输出暴露输入，技术洞见生活，下期再会~</p>
</blockquote>
<p>参考：</p>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/48674410" target="_blank" rel="nofollow noopener noreferrer">为什么电影24帧就算流畅，主机30帧就算流畅，而电脑游戏需要60帧流畅？</a></li>
<li><a href="https://www.reneelab.net/frames-per-second.html" target="_blank" rel="nofollow noopener noreferrer">FPS幀數是什麼？24fps、30fps、60fps有什麼區別？</a></li>
<li><a href="https://medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-CSS3-db7b98610108" target="_blank" rel="nofollow noopener noreferrer">how-to-achieve-60-fps-animations-with-CSS3</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement/transitionend_event" target="_blank" rel="nofollow noopener noreferrer">transitionend_event</a></li>
</ul></div>  
</div>
            