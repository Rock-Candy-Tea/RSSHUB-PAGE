
---
title: 'ReactNative在游戏营销场景中的实践和探索-性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d781fe9617b42d8a2b1f591ae3ead80~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:07:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d781fe9617b42d8a2b1f591ae3ead80~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>作者：字节游戏中台客户端团队 - 熊文源</strong></p>
<p>客户端跨端框架已经发展了很多年了，最近比较流行的小程序、Flutter、ReactNative，都算是比较成功、成熟的框架，面向的开发者也不一样，很多大型app都广泛的使用了，笔者有幸很早就参与学习使用了这些优秀的跨端方案，在这几年的开发和架构设计中，除了在App中支撑了千万级DAU，也慢慢将ReactNative跨端方案运用到了游戏，来提升开发、迭代效率。本次文章我们就会分5个章节介绍我们在游戏中的一些探索和实践，相信大家也能从中有所收获：</p>
<ul>
<li><strong>第一篇：游戏中使用ReactNative的背景介绍</strong></li>
<li><strong>第二篇：简介游戏中怎么集成ReactNative</strong></li>
<li><strong>第三篇：简介游戏中的ReactNative性能优化</strong></li>
<li><strong>第四篇：ReactNative Hermes引擎简介</strong></li>
<li><strong>第五篇：ReactNative 新架构介绍</strong></li>
</ul>
<p>（本篇为系列第三篇）</p>
<p>随着版本不断迭代完善，基本具有大量上线游戏的能力，随着游戏业务越来越多，在不同的游戏环境中，也碰到不少问题，这也从侧面体现出了游戏场景和架构的复杂性，主要核心问题还是在于ReactNative的沉浸式体验、启动性能、内存、渲染性能问题等，似乎这些问题也是ReactNative的通病，为了解决这些问题，我们开始专项优化。</p>
<h3 data-id="heading-0">1. 启动性能优化</h3>
<p>针对启动性能问题，我们也测试列大量数据，ReactNative在纯客户端App中，性能表现还算不错，但在游戏低内存、cpu过度占用的情况下，该问题显得格外突出，要解决这些问题，首先我们需要了解ReactNative加载的主要时间消耗，可以参考下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d781fe9617b42d8a2b1f591ae3ead80~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体页面渲染显示前，需要首先加载加载初始化 React Native Core Bridge，主要包含ReactNative的运行环境、UI和API组件功能等，然后才能运行业务的 JS，执行render绘制UI，完成后，React Native 才能将 JS 的组件渲染成原生的组件。因页面的加载流程是固定不变的，所以我们可以采用了提前预加载Core bridge的方案来提升加载性能，当游戏营销页面启动前，预先加载好原生端bridge，这样在打开业务是指需要运行前端JS代码渲染，设计思路上我们也根据业务场景设计了模式：</p>
<ul>
<li>预加载业务包：提前加载好完整的业务包到内存，生成并缓存ReactInstanceManager对象，在业务启动时，从内存缓存中获取该对象，并直接运行绑定rootview，经过改造，该方案能提升整体的打开速度30%-50%左右，游戏环境下，手机设备基本都达到秒开，模拟器设备在2s内，但这种通过内存换取速度的方法，在业务量大后，很明显是不可取的，所以整包预加载的局限性比较强。</li>
</ul>

<ul>
<li>Common包预加载：针对全包预加载的局限性，我们提出了分包方案，预加载common包，研究发现ReactNative打包生成的业务包其实有两部分内容，一部分是公共的基础组件、API包，统称common包，一部分是业务的核心逻辑包。改造打包方式，可以把原有的全包模式分离成common+bussiness，在多业务包模式下，可以共享统一的common包，在打开业务前，我们会优先预加载common包，并缓存对应的ReactInstanceManager对象，用户触发打开业务后，再加载bussiness 包，该方案相对于全包预加载性能略差，但比不预加载能提升15%-20%左右，同时支持多业务运行环境，具体思路可以参考开源项目<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhoujianbang%2Freact-native-multibundler" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhoujianbang/react-native-multibundler" ref="nofollow noopener noreferrer">react-native-multibundler</a></li>
</ul>

<ul>
<li>从时序运行上，除了core bridge的初始化外，js 运行到页面显示，实际上也占用了不少时间，在预加载core bridge上，我们更近一步，支持了预加载rootview，提前将要渲染页面的rootview运行起来缓存在内存，当然这里加载的还是基础模块，在业务打开时，路由触发展示页面即可，可以做到页面无延时打开，但是对内存的开销，比预加载core bridge 更高。</li>
</ul>
<p>当然上述方案都是通过内存换性能，不同的加载方式都做到了云控，随时切换、关闭。除了这些方案外同样还有其他方式能优化启动性能：</p>
<ol>
<li>Lazy module，将引擎自定义的API Native Module改造成懒加载方式，整体性能提升在5% 左右。</li>
<li>业务代码做到按需require，不需要展示的部分，采用lazy require，提升页面的显示、渲染速度。</li>
<li>裁剪业务包，将业务代码没有用到React的module、API、组件删除，减少业务包大小来提升启动性能。</li>
<li>分包方案，从测试数据来看，业务包越小，启动性能越好，包大小无法减小后，将业务包按照路由拆分为子包，也能立竿见影的解决启动速度问题。将业务包按照路由页面和功能分成多个子的业务子包，让首屏业务逻辑包变小，做到按需加载其他业务包，提升首页启动性能。</li>
</ol>
<p>这些方案都从引擎加载的角度解决了启动性能慢，做到了按需加载，整体性能达到了最优化。但是在游戏中，业务页面的显示还是太依赖服务度请求来完成页面的渲染，所以在逐步优化后，发现网络请求对于页面的显示也占了很大一部分，为了进一步提升首屏显示，我么增加了网络请求预拉取、图片预缓冲方案：</p>
<ol>
<li>网络预拉取，对于一些对首屏显示影响较大的网络请求，在引擎加载后，在合适时机从云控平台获取后，根据配置拉取并缓存到内存，打开业务后，优先从缓存中读取网络接口内容并显示。</li>
<li>图片预缓存，对于一些加载较慢的图片，将链接配置到云端后，在合适时机提前预加载到Fresco内存，页面打开后Fresco会从缓存中直接读取bitmap</li>
</ol>
<p>除了这些方案外，替换JSC引擎到hermes，也能很好的解决启动性能问题，后面章节会重点介绍。</p>
<h3 data-id="heading-1">2. 内存优化</h3>
<p>以上所有的优化更多是针对启动性能的优化设计，也是业内用于提升加载性能的方案，在游戏的复杂环境下，除了性能外，对于内存的要求也是很严格的，游戏启动后，本身对于内存的消耗就比一般的原生app高，所以在内存使用上会更精确和严格，那ReactNative是怎么优化内存的：</p>
<ol>
<li>分包方案，分包方案除了在启动速度上有很大优化外，实现了按需加载，对于内存来说也做到了最优化。</li>
<li>字体加载，因游戏字体库无法和原生字体共享，导致在ReactNative页面使用字体会大大增加整体的内存，为了降低字体的内存，我们支持了字体的裁剪方案，按需打入字体，删掉一些生僻的字，大大降低了字体包的大小。另外字体文件对于业务包大小影响也比较大，我们支持字体的动态下发和加载。</li>
<li>图片优化，除了业务UI和JS本身占用的内存外，内存上占用比较大的是图片，而且图片有缓存，为了降低图片的内存消耗，我们支持了webp、gif等格式的图片，有损压缩，同时对于网络图片做到了按手机分辨率下发。另外提供API到前端业务，按需清理不使用的图片，及时释放内存，并控制图片缓存大小。</li>
</ol>
<h3 data-id="heading-2">3. 渲染性能</h3>
<p>除了内存、启动性能外，在游戏中的渲染性能也至关重要，ReactNative受限于游戏内的内存和CPU负载高，同等复杂度页面，表现不如原生App。为了能优化这些指标，我们对ReactNative的渲染流程做了分析和优化，支持静止状态下帧率基本达到了60fps，大致优化如下：</p>
<ol>
<li>ReactNative是前端事件驱动原生UI渲染的，所以设计上ReactNative会在Frame Buffer每一帧绘画结束后的回调在UI线程中处理UI更新，即使没有更新的情况下也会空运转，这在UI线程负载本就较高的游戏中，增加了UI的负担</li>
<li>动画、点击事件都是同样的设计，会不断的有任务空转占用UI线程，增加了UI线程每次绘制的时间</li>
<li>解决这个问题，就是要支持资源的按需加载，我们将动画、UI更新事件放到了消息map，每次一帧渲染完成后，我们会检查map消息，是否有需要处理的消息，没有后续就不再在一帧渲染完成后调度UI线程，当用户触发了动画或者UI更新，会发送消息map，并注册帧渲染的callback，在callback中检查map消息更新UI</li>
</ol>
<p>另外ReactNative采用的是原生UI渲染，在打开硬件加速的情况，整体渲染性能表现比较高，但是在游戏环境中，大部分游戏都是不开硬件加速的（自渲染组件和引擎的缘故），对于比较复杂的ReactNative UI，更新UI时整体FPS会偏低，UI响应会比较慢，特别是在模拟器（限制fps30）的情况下，渲染性能更加差强人意。在复杂交互的情况，要怎么提升性能？</p>
<ol>
<li>简单的UI设计，没有大图背景的情况下，不开硬件加速，整体渲染性还不算差，但有大的背景情况下，UI性能表现尤其差，所以解决渲染问题，其实更多的是要解决大图渲染的问题</li>
<li>ReactNative 提供了renderToHardwareTextureAndroid 来用native内存换渲染的性能，导致的问题是内存消耗较高，对于图片不是太多、内存限制不是很严格的业务，可以采用该方式提升性能</li>
<li>对于大量使用图片的业务，我们设计一套采用opengl渲染方式的组件，支持纹理图(比较通用的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fcommand-line%2Fetc1tool.html%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.google.cn/studio/command-line/etc1tool.html?hl=zh-cn" ref="nofollow noopener noreferrer">etc1</a>)，从内存和渲染性能上，明显都得到了很大的提升，但这种模式依赖硬件加速，所以一般是在Dialog窗口模式中使用，<strong>具体的实现原理，大家可以关注作者文章</strong>，后面会详细和大家分享</li>
</ol>
<p><strong>核心示例代码：</strong></p>
<pre><code class="copyable"> /* GLES20.glCompressedTexImage2D(target, 0, ETC1.ETC1_RGB8_OES , bitmap.getWidth(), bitmap.getHeight(), 0, etc1tex.getData().capacity(), etc1tex.getData());*/
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            