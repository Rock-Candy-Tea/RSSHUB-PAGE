
---
title: '【得物技术】web端动效方案对比'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b333f72050452997fc9afc490d7744~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 02:27:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b333f72050452997fc9afc490d7744~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>为了满足业务增长的需求，我们需要创意h5作为承载，增强app趣味、增加用户留存。而如果把创意h5归纳一下，会发现可以分为游戏类和主交互类，本篇文章会对主交互类创意H5的技术选型进行对比，抛砖引玉。</p>
<h1 data-id="heading-1">技术选型 - 我们有哪些选择？</h1>
<h2 data-id="heading-2">web端动效的方式</h2>
<ul>
<li>
<p><strong>设计提供静图(jpg/jpeg/png(静态)/svg)</strong>，通过设计口述或者作出动图，通过 create-keyframe-animation 或者手写，通过 css/canvas 来实现。</p>
<ul>
<li>优势：灵活，所有动效都尽在开发的掌握。</li>
<li>劣势：开发时间长，沟通成本大，设计同学很难空口描述出想要的动效，也受开发的水平限制比较大。</li>
</ul>
</li>
<li>
<p><strong>设计提供 gif</strong>，开发用图片的形式嵌入。</p>
<ul>
<li>优势：开发成本低，沟通成本小。</li>
<li>劣势：gif 一般都比较大，比较小的噪点又过于明显，性能的性价比不高；不支持透明度；只能循环播放，较为死板。</li>
</ul>
</li>
<li>
<p><strong>设计提供 apng</strong>，开发用图片的形式嵌入。</p>
<ul>
<li>优势：同 gif，体积较 gif 小，可以与 webp 的大小相对比，性能性价比相对高</li>
<li>劣势：只能循环播放，较为死板。</li>
</ul>
</li>
<li>
<p>雪碧图序列帧，<strong>设计提供一个合成的雪碧图（静图）</strong>，开发通过序列帧的方式进行动效操作。</p>
<ul>
<li>优势：开发成本中等，沟通成本小。</li>
<li>劣势：合成的雪碧图文件大，且在不同屏幕分辨率下可能会失真。</li>
</ul>
</li>
<li>
<p><strong>视频</strong>，设计提供不等数量的视频文件，通过播放视频来达成动效的效果</p>
<ul>
<li>优势：可以便捷的操作序列帧，开发成本小，相较 gif 体积较小</li>
<li>劣势：移动端视频在不同 app、不同机型、不同系统的播放体验不大一样，尤其是 app 内，需要端侧做一些处理。</li>
</ul>
</li>
<li>
<p><strong>使用 lottie</strong>，设计同学给出 json 文件和图片文件夹，开发同学引入 lottie 插件，对 json 进行解析。</p>
<ul>
<li>优势：开发成本中等，效果不受开发同学水平限制，只要设计画的出，开发就能实现出来；灵活，基点元素可以作为一个普通的 dom 节点进行定位，整个动画可以任意播放停止甚至倒放以及从某一帧开始播放（具体能实现的参见 api 文档），灵活度非常高。</li>
<li>劣势：在开发层面和设计层面看到的帧节点以及播放速度不同，需要持续进行沟通联调，沟通成本大；lottie插件打包前 400+kb，打包后也有 200+kb，会显著增加项目的大小。</li>
</ul>
</li>
<li>
<p><strong>使用 svga</strong>，设计同学给出 .svga文件，开发引入 svga 插件，对其进行解析。</p>
<ul>
<li>优势：理论上来说同 lottie</li>
<li>劣势：实际引入中，存在“无故清除canvas画布”的问题，不稳定性极高，建议只使用在单纯播放的场景。</li>
</ul>
<p>目前，我们的动效基本通过 create-keyframe-animation+css、lottie、css+apng，这几种方案混合实现。下文我们简单描述一下这三种方案。</p>
<h1 data-id="heading-3">方案简述</h1>
<h2 data-id="heading-4">create-keyframe-animation+css</h2>
<p>create-keyframe-animation 是一个很简单的动画库，主要简化了 css 动态插入的代码复杂度。</p>
<p>举个例子：
<a href="https://bizsec-auth.alicdn.com/a9b5b21ee64d2b47/Qe9k4XSEr4zqvIg7131/87V0SJH30XGXEEEUw4s_304620391032___hd.mp4?auth_key=1618570299-0-0-46cfbdf8f3b93c6c5978aedf32161ecd" target="_blank" rel="nofollow noopener noreferrer">bizsec-auth.alicdn.com/a9b5b21ee64…</a></p>
<p>在这个动效中，用户选择的卡片不定，也就是起点位置不定。给 dom 绑定动态生成的 css 是个繁琐的过程，尤其是牵扯到多少毫秒会有什么变化，如果使用 create-keyframe-animation，只需要写一份描述代码↓，再进行注册即可。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> animation = &#123;
  <span class="hljs-number">0</span>: &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;startWidth&#125;</span>px`</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;startHeight&#125;</span>px`</span>,
    <span class="hljs-attr">transform</span>: <span class="hljs-string">`translate(<span class="hljs-subst">$&#123;startLeft-targetLeft&#125;</span>px,<span class="hljs-subst">$&#123;startTop - targetTop&#125;</span>px) rotateY(-20deg) rotateX(20deg) rotateZ(12deg)`</span>
  &#125;,
  <span class="hljs-number">17</span>: &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;startWidth * <span class="hljs-number">1.5</span>&#125;</span>px`</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;startHeight * <span class="hljs-number">1.5</span>&#125;</span>px`</span>,
  &#125;,
  <span class="hljs-number">100</span>: &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;targetWidth&#125;</span>px`</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;targetHeight&#125;</span>px`</span>,
    <span class="hljs-attr">transform</span>: <span class="hljs-string">`translate(0,0) rotateY(360deg) rotateX(0) rotateZ(0)`</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">lottie</h2>
<h3 data-id="heading-6">lottie是什么？</h3>
<ul>
<li>是 airbnb 出产的一款动效插件，现在支持开发侧的 web/RN/Android/ios/Mac os，以及设计侧的AE。</li>
<li>web 端的文档地址：Web - Lottie Docs</li>
</ul>
<h3 data-id="heading-7">lottie怎么用？</h3>
<pre><code class="hljs language-plain copyable" lang="plain">npm install lottie-web --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 此处以vue为例</span>
<span class="hljs-keyword">import</span> lottie <span class="hljs-keyword">from</span> <span class="hljs-string">'lottie-web'</span>
Vue.prototype.$lottie = lottie
<span class="hljs-comment">// 加载动画(遵从vue声明周期，这个调用需在dom节点加载出来，也即是mount之后)</span>
<span class="hljs-keyword">let</span> machineNormal = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#machineNormal'</span>)
<span class="hljs-built_in">this</span>.normalAni = <span class="hljs-built_in">this</span>.$lottie.loadAnimation(&#123;
    <span class="hljs-attr">container</span>: machineNormal, <span class="hljs-comment">// the dom element</span>
    <span class="hljs-attr">renderer</span>: <span class="hljs-string">'canvas'</span>, <span class="hljs-comment">// canvas / svg / html</span>
    <span class="hljs-attr">loop</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 自循环</span>
    <span class="hljs-attr">autoplay</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 自动播放</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'static/machine_normal.json'</span>, <span class="hljs-comment">// the animation data</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用lottie的过程中，需要注意什么？</h3>
<h4 data-id="heading-9">引入过程中</h4>
<ol>
<li>lottie 动画加载需要一个 dom 节点，这个 dom 节点可被任意操纵位置，动画加载完毕后整个 dom 的宽高会被填充为动画的宽高，也即是设计给出的动画过程中最宽、最高的那个数值。</li>
<li>同样因为 lottie 动画加载需要一个 dom节点，所以加载动画的方法需在 dom 加载完成的声明周期或者之后调用。</li>
<li>如果使用 path 参数引入 json 文件：</li>
</ol>
<p><strong>文件放在本地：</strong></p>
<ul>
<li>图片也需放在本地，通过修改.json文件的 assets 里面每一项的 u 属性，可以自定义图片文件夹的名字。</li>
</ul>
<p>例如：</p>
<pre><code class="hljs language-JSON copyable" lang="JSON">&#123;
<span class="hljs-attr">"v"</span>: <span class="hljs-string">"5.5.8"</span>,
<span class="hljs-attr">"fr"</span>: <span class="hljs-number">24</span>,
<span class="hljs-attr">"ip"</span>: <span class="hljs-number">1</span>,
<span class="hljs-attr">"op"</span>: <span class="hljs-number">53</span>,
<span class="hljs-attr">"w"</span>: <span class="hljs-number">662</span>,
<span class="hljs-attr">"h"</span>: <span class="hljs-number">827</span>,
<span class="hljs-attr">"nm"</span>: <span class="hljs-string">""</span>,
<span class="hljs-attr">"ddd"</span>: <span class="hljs-number">0</span>,
<span class="hljs-attr">"assets"</span>: [
&#123;
<span class="hljs-attr">"id"</span>: <span class="hljs-string">"image_0"</span>,
<span class="hljs-attr">"w"</span>: <span class="hljs-number">662</span>,
<span class="hljs-attr">"h"</span>: <span class="hljs-number">827</span>,
<span class="hljs-attr">"u"</span>: <span class="hljs-string">"machine_img/"</span>, <span class="hljs-comment">/* 这个就是文件夹的名字 */</span>
<span class="hljs-attr">"p"</span>: <span class="hljs-string">"img_0.png"</span>,
<span class="hljs-attr">"e"</span>: <span class="hljs-number">0</span>
&#125;,
 ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果是 vue-cli2 建议使用 static 文件夹存放，不受到打包的影响；如果使用的是vue-cli 3，那么放在public文件夹下，并且path直接写想要的文件名，例如：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.lottie = <span class="hljs-built_in">this</span>.$lottie.loadAnimation(&#123;
    <span class="hljs-attr">container</span>: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#BindDom'</span>), <span class="hljs-comment">// the dom element that will contain the animation</span>
    <span class="hljs-attr">renderer</span>: <span class="hljs-string">'svg'</span>,
    <span class="hljs-attr">loop</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">autoplay</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-string">'data.json'</span> <span class="hljs-comment">// the path to the animation json</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>文件放在cdn</strong>：</p>
<p>注意图片的文件夹应该与 json 文件放在同一目录下，例如：</p>
<pre><code class="copyable">./btn_gain.json
./btn_gain_img/img_0.png
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">动画运行过程中</h4>
<ol>
<li>在动画初始化的时候，lottie 提供生命周期以感知动画的加载状态，主要提供以下几种：</li>
</ol>
<ul>
<li>complete</li>
<li>loopComplete</li>
<li>enterFrame</li>
<li>segmentStart</li>
<li>config_ready (when initial config is done)</li>
<li>data_ready (when all parts of the animation have been loaded)</li>
<li>DOMLoaded (when elements have been added to the DOM)</li>
<li>destroy</li>
</ul>
<p>其中 DOMLoaded 理论上是最晚能感知到的周期，也即是“动画加载完成”。但实际使用下来，只有使用 canvas形式加载动效的时候，这个事件才是所有图片全部加载完成；其余情况（svg，html），都只是“开始拉取图片”，还是会展示给用户图片加载的整个过程。</p>
<p>并且，即使使用 canvas 加载，如果 json 文件与对应的图片文件夹都是云端也就是 cdn 的形式拉取的话，依旧无法感知到所有图片加载的过程。所以如果有强需求，需要用户完全不感知图片加载，建议将文件放在本地并以canvas 形式加载。</p>
<ul>
<li>lottie 提供 destroy 的 api 以清空画布，但是在 destroy 旧动画 -> load 新动画这个过程中，会有非常明显的全屏闪动，这是由于画布重新生成需要时间造成的，建议使用dom的显隐切换而不是画布的 destroy 来切换同一块动效的不同状态。</li>
<li>可任意使用 onComplete 的事件监听，不会发生事件的重新绑定。</li>
<li>lottie 不提供原生的缓停事件，但是可以通过提供的 setSpeed 方法进行多段调整速度，以达到缓停的效果。</li>
</ul>
<h1 data-id="heading-11">APNG</h1>
<h2 data-id="heading-12">APNG 是什么</h2>
<blockquote>
<p>以下来自wikipedia</p>
</blockquote>
<blockquote>
<p>Animated Portable Network Graphics (APNG) is a file format which extends the Portable Network Graphics (PNG) specification to permit animated images that work similarly to animated GIF files, while supporting 24-bit images and 8-bit transparency not available for GIFs. It also retains backward compatibility with non-animated PNG files.</p>
</blockquote>
<blockquote>
<p>The first frame of an APNG file is stored as a normal PNG stream, so most standard PNG decoders are able to display the first frame of an APNG file. The frame speed data and extra animation frames are stored in extra chunks (as provided for by the original PNG specification). APNG competes with Multiple-image Network Graphics (MNG), a comprehensive format for bitmapped animations created by the same team as PNG. APNG's advantage is the smaller library size and compatibility with older PNG implementations.</p>
</blockquote>
<blockquote>
<p>In a comparison made between GIF, APNG and WebP, it was shown that APNG kept lower file size while keeping at least equal quality.</p>
</blockquote>
<p>动画便携式网络图形（APNG）是一种继承自便携式网络图形（PNG）的文件格式，他允许像 gif 文件一样播放动图，还拥有 gif 不支持的24位图像和8位透明性。 它还保留了与非动画 PNG 文件的向后兼容性。</p>
<p>APNG 文件的第一帧存储为普通 PNG 流，因此大多数标准 PNG 解码器都能够显示 APNG 文件的第一帧。 帧速度数据和额外的动画帧存储在额外的 chunks 中（如原始的 PNG 规范所规定）。 APNG 的竞争者是由 PNG 团队创建的位图动画的全面格式——多图像网络图形（MNG）。与其相比，APNG 的优势是更小的存储大小以及对旧的 PNG 完全兼容。</p>
<p>通过对比 GIF、APNG和WebP，可以看出 APNG 在质量相同的时候有着更小的体积。</p>
<ul>
<li>APNG 是动的 PNG。</li>
<li>APNG的扩展名为 .png 或者 .apng。是的，.png 当然有可能是 APNG 文件。</li>
</ul>
<h2 data-id="heading-13">apng 的兼容性</h2>
<p>在2021年4月的现在，APNG 的兼容性如下：</p>
<p><img alt="截屏2021-04-16 下午6.20.36.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b333f72050452997fc9afc490d7744~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
可以看到99%的浏览器都兼容了，所以基本可以放心大胆的使用了。</p>
<p>对于不兼容的浏览器，APNG会显示为动画的第一帧。</p>
<h2 data-id="heading-14">apng 的优势</h2>
<p>正如上文的介绍中附上的链接，apng 比 webp 更小，对比数据来源来自：<a href="http://littlesvr.ca/apng/gif_apng_webp3.html" target="_blank" rel="nofollow noopener noreferrer">littlesvr.ca/apng/gif_ap…</a></p>





























<table><thead><tr><th>GIF = 43 920 bytes</th><th>APNG = 34 210 byte</th></tr></thead><tbody><tr><td>WebP = 41 064 bytes</td><td>Lossy WebP = 73 774 bytes</td></tr><tr><td>GIF = 43 132 bytes</td><td>APNG = 30 823 bytes</td></tr><tr><td>WebP = 55 968 bytes</td><td>Lossy WebP = 114 518 bytes</td></tr><tr><td>GIF = 200 700 bytes</td><td>APNG = 168 411 bytes</td></tr><tr><td>WebP = 424 752 bytes</td><td>Lossy WebP = 394 118 bytes</td></tr></tbody></table>
<h2 data-id="heading-15">在页面上的基础使用</h2>
<p>正如简单的png一样，一个img标签足以，但是坑多多，详见下文。</p>
<h2 data-id="heading-16">在页面上的动画化使用</h2>
<p>img 标签虽简单，但却有以下几种问题：</p>
<ol>
<li>apng 在页面上只能播放一次，所以如果一个动画需要重复播放，需要每次给动画连接添加时间戳，让浏览器认为是一个新的连接</li>
<li>apng 在安卓和ios上表现存在差距，例如安卓播放一次，ios 会播放两次</li>
<li>apng 的动画时间无法控制，很难实现中途暂停，衔接等操作</li>
</ol>
<p>如上所述，我们可以借助 apng-canvas，将其转成 canvas ，然后以使用 canvas 的方式使用它。
apng-canvas 的原理解析，可以参考网易云前端团队的文章：<a href="https://juejin.cn/post/6857678436304388104" target="_blank">Web 端 APNG 播放实现原理</a>
我们在 apng-canvas 的基础上，进行了魔改，增加了一些对 canvas 播放的控制能力，例如：控制 apng 的播放速度 和播放次数、监听播放完成的事件等等，使其更加便于使用。
这里放上我们炫酷的抽卡动效，作为 apng 配合 css 的实例：
<a href="https://bizsec-auth.alicdn.com/a9b5b21ee64d2b47/Qe9k4XSEr4zqvIg7131/Y3KzeXd6YFspWvWPkUo_303625464802___hd.mp4?auth_key=1618571359-0-0-661b5b0c992c33c45b8517da4f9ddae9" target="_blank" rel="nofollow noopener noreferrer">bizsec-auth.alicdn.com/a9b5b21ee64…</a></p>
<h1 data-id="heading-17">参考说明</h1>
<p>APNG 那些事: <a href="https://aotu.io/notes/2016/11/07/apng/index.html" target="_blank" rel="nofollow noopener noreferrer">aotu.io/notes/2016/…</a>
Web 端 APNG 播放实现原理<a href="https://juejin.cn/post/6857678436304388104" target="_blank">juejin.cn/post/685767…</a></p>
<p>文｜水程</p>
<p>关注得物技术，携手走向技术的云端</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            