
---
title: 'CSS 布局的本质是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/618d27fc7c9b4a1a88398aa2cde6eee8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 07:01:55 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/618d27fc7c9b4a1a88398aa2cde6eee8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">UI 发展史</h2>
<p>自从图形界面操作系统问世以来，之上的应用软件基本都会绘制界面，这也是用户使用软件的接口，叫做 UI （user interface）。涉及到用户体验、设计、具体界面的开发，是软件中和用户最近的一部分，也是多个职能的岗位交集最多的部分。</p>
<p>根据操作系统不同，会有不同的界面的开发方式。安卓、ios、windows 等都有各自的创建 ui 的库，但是更底层的绘图库却是有标准的：跨平台的绘图 api 接口标准 OpenGL 以及 windows 下的 DirectX。</p>
<p>因为各个操作系统绘制 ui 的方式不同，所以跨平台的绘制方案逐渐流行开来，也就是浏览器。基于浏览器服务器的软件架构叫做 B/S 架构，而基于客户端的叫做 C/S 架构。</p>
<p>在一段时间内，B/S 架构的应用越来越多，C/S 架构的应用也更多的混合 B/S 的方案来实现。</p>
<p>在移动互联网时代来临之后，大家发现网页的体验比不上原生，虽然后面发展出了 PWA （渐进式WebApp）等技术，但离原生的体验还是有差距的，所以原生开发应用的方案又占了上风。</p>
<p>但是安卓、ios 绘制界面、书写逻辑的方式都不同，双端要分别实现，开发、测试的人力都是双份的，这样的成本是比较高的。为了节省成本，大家又摸索出了跨端引擎的方案，也就是说还是通过网页来写渲染和交互的逻辑，但是渲染用的 api 是由安卓、ios 分别实现，这样就实现了跨端的渲染，逻辑部分也是由 JS 来写，一些需要的设备能力 api 分别由安卓、ios 实现然后注入到 JS 引擎里。</p>
<p>和安卓、ios 的跨端方案逐渐流行一样，桌面端也出现了 electron 的方案，通过网页来渲染界面和写逻辑，需要用的 api 注入到 JS 引擎中，而且 electron 是直接把 Node.js 的 api 注入到了 JS 引擎中，在网页里实现一些原生功能的时候可以直接使用 Node.js 的 api，此外还有一些 api 是 elctron 额外注入的，比如剪贴板、电源监视器等。</p>
<p>发展到现在，UI 的绘制方案逐步向网页靠拢，基于 html、css、js 的 web 技术成为了创建 UI 界面的主流方案。</p>
<h2 data-id="heading-1">网页的物理层和逻辑层</h2>
<p>大家用过 canvas 的 api 应该知道，如果直接绘制的话需要指定什么内容绘制到什么地方，每一部分都要计算，而这是比较繁琐的，所以浏览器提供了一些布局用的样式，并且提供了 css 来描述，而内容部分则是通过 html 描述。</p>
<p>开发者只需要使用 html 描述内容的结构，然后用 css 来描述布局和如何渲染，就可以完成界面的绘制。网页会把 html 解析成 dom 树，把 css 解析成 cssom 树，之后把两者合并成 render 树，自动计算出什么内容绘制到什么位置，实现最终的渲染。</p>
<p>dom 是有 id、class、tagName 等标识的，逻辑的部分就通过这些标识给具体 dom 绑定一些事件处理函数，然后在函数里面操作 dom 来实现的界面的交互。</p>
<p>dom api 是最终浏览器提供给开发者的构建 web 应用的接口，算是 web 应用的物理层。</p>
<p>当然，现在开发 web 应用并不会直接基于 dom api，而是会选择某一个前端框架，比如 vue、react、angular 等。</p>
<p>这些框架实现了组件的功能，也就是对页面做的逻辑的拆分，把相同功能的 html、css、js 聚合在一起，使之可以复用。并且提供了 mvvm 的功能，自动做数据到具体 dom 的映射，而不再需要开发者手动操作 dom。</p>
<p>前端框架做的事情相当于是 web 应用的逻辑层，最终的渲染和交互还是通过 dom api，但是用户不需要直接操作，而是在逻辑层描述组件和数据，由前端框架完成数据到 dom 的自动映射。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/618d27fc7c9b4a1a88398aa2cde6eee8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在的跨端方案基本都是对物理层的 dom api 做了替换，然后上层对接一个逻辑层的前端框架来支持跨端的应用开发。</p>
<h2 data-id="heading-2">css 的两部分</h2>
<p>css 是浏览器提供给开发者的描述界面的方式，而描述界面分为两部分：</p>
<ul>
<li>
<p>内容绘制在什么地方</p>
</li>
<li>
<p>内容怎么绘制</p>
</li>
</ul>
<p>内容绘制在什么地方就是布局的部分，主要是 display 和 position 的样式。而内容怎么绘制则跟具体内容相关，font、text、image 等内容都有各自的一些样式。</p>
<p>本文我们主要来探究 css 做布局的部分。</p>
<h3 data-id="heading-3">盒模型</h3>
<p>首先，所有的内容都会有一些空白和与其他元素的间距，所以 css 抽象出了盒模型的概念，也就是任何一个块都是由 content、padding（空白）、border、margin（间距）这几部分构成。</p>
<h3 data-id="heading-4">display</h3>
<p>但是盒与盒之间也是有区别的，有的盒可以在同一行显示，有的则是独占一行，而且对内容的位置的计算方式也不一样。于是提供了 display 样式来设置盒类型，比如 block、inline、inline-block、flex、table-cell、grid 等，分别设置成不同的盒类型，就会使用不同的计算规则。</p>
<ul>
<li>
<p>block 的元素会独占一行、可以设置内容的宽高，具体计算规则叫做 BFC。</p>
</li>
<li>
<p>inline 的元素宽高由内容撑开不可设置，不会独占一行，具体计算规则叫做 IFC。</p>
</li>
<li>
<p>flex 的子元素可以自动计算空白部分，由 flex 样式指定分配比例，具体计算规则叫做 FFC。</p>
</li>
<li>
<p>grid 的子元素则是可以拆分成多个行列来计算位置，具体计算规则叫 GFC。</p>
</li>
</ul>
<p>这些都是不同盒类型的布局计算规则。</p>
<h3 data-id="heading-5">position</h3>
<p>根据不同盒类型的布局计算规则往往不够用，很多场景下需要一些用户自定义的布局规则，所以 css 提供了 position 样式，包括 static、relative、absolute、fixed、sticky。</p>
<h4 data-id="heading-6">static</h4>
<p>默认盒的定位方式就是 static，也就是流式的，上个盒子显示到什么地方了，下个盒子就在下面继续计算位置，显示在什么位置是由内容多少来决定的。</p>
<p>最开始的时候网页主要是用来显示一些文本，所以流式的位置计算规则就很方便。</p>
<h4 data-id="heading-7">relative</h4>
<p>流式的规则是根据上个盒子的位置自动计算出下个盒子的位置，但有的时候想做一些偏移，这种就可以通过 relative 来指定，设置 position 为 relative，然后通过 top、bottom、left、right 来指定如何偏移。</p>
<p>相对布局给流式布局增加一些灵活性，可以在流式计算规则的基础上做一些偏移。</p>
<h4 data-id="heading-8">absolute</h4>
<p>流式的计算规则具体什么内容显示在什么位置是不固定的，只适合文字、图片等内容的布局。但是比如一些面板需要固定下来，就在某个位置不要动，就可以通过 position 设置为 absolute，就可以脱离文档流了。这时候就可以根据上个非流式的 position 来计算现在的 position。</p>
<h4 data-id="heading-9">fixed</h4>
<p>absolute 是根据上一个脱离了文档流的 position 来计算位置的，最外层的 absolute 的元素是根据窗口定位。如果想直接根据窗口来定位可以指定 position 为 fixed。这个时候的 top、bottom、left、right 就是相对于窗口的。</p>
<h4 data-id="heading-10">sticky</h4>
<p>sticky 的效果在滚动的时候如果超过了一定的高度就 fixed 在一个位置，否则的话就 static。相当于基于 static 和 fixed 做的一层封装，实现导航条吸顶效果的时候可以直接用。</p>
<p>或许就是因为太常用，才封装出了这样一个 position 的属性值吧，之前都是通过 js 监听滚动条位置来分别设置 static 和 fixed 的。</p>
<h3 data-id="heading-11">float</h3>
<p>脱离文档流还可以通过 float，文档流内的块盒会占据一行，可以通过 float 让元素先脱离文档流，不再占据一行，等设置完改行的样式，再用 clear 清除浮动，让后面的元素继续在文档流中布局。</p>
<p>但是有了 flex 的盒之后，不再需要这样 float、clear 了，直接在文档流中放个 flex 盒，flex 盒内就可以在同一行内做弹性的布局。</p>
<h3 data-id="heading-12">小结</h3>
<p>所谓的布局就是确定元素的位置，设置了盒的类型（display）之后对于内容如何渲染会有不同的规则，比如 BFC、IFC、FFC、GFC 等。</p>
<p>盒与盒之间默认是流式的，也就是 position 为 static，但有的时候想在流中做下偏移，用 relative。当不想跟随文档流了，可以设置 absolute 来相对于上个非 static 位置来计算一个固定的位置，如果想直接相对于窗口，就用 fixed。</p>
<p>当需要做吸顶效果的时候，要根据滚动位置切换 static 和 fixed，这时候 css 还有一个 sticky 的定位方式可以直接用。</p>
<p>也就是说，盒内部的布局计算规则根据 display 来确定，还可以用 position 做一些调整。之前块盒需要先用 float 脱离文档流，布局完再 clear，现在用 flex 盒就可以了。</p>
<h2 data-id="heading-13">vscode 是如何布局的</h2>
<p>讲了 css 的布局方式（也就是 display 配合 position）之后，我们来看一个具体的案例： vscode 是如何布局的。</p>
<p>vscode 是我们经常用的 ide，它基于 electron，也就是通过网页来绘制界面，那么它是怎么做布局的呢？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d628335c5cb4de5a565532c2ed07a3f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 分为了标题栏、状态栏、内容区，是上中下结构，而内容区又分为了活动栏、侧边栏、编辑区，是左中右结构。窗口可以调整大小，而这个上中下嵌套左中右的结构是不变的。</p>
<p>这种布局如何实现呢？</p>
<p>css 的布局就是 display 配合 position 来确定每一块内容的位置。我们的需求是窗口放缩但每一块的相对位置不变，这种用 absolute 的布局就可以实现。</p>
<p>首先，最外层是上中下的结构，可以把每一块设置为 absolute，然后分别设置 top 值，然后中间部分由分为了左中右，可以再分别设置左中右部分的 left 值，这样就完成了每一块的布局。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/278f399edd0a41edbb45dacb0e10db2f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3e27cc2bc4744f0ba8299e7d71ece33~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是整体的布局，每一块内部则根据不同的布局需求分别使用流式、弹性等不同的盒，配合绝对、相对等定位方式来布局。</p>
<p>但是，绝对定位是要指定具体的 top、bottom、left、right 值，是静态的，而窗口大小改变的时候需要动态的设置具体的值。这时候就需要监听窗口的 resize 事件来重新布局，分别计算不同块的位置。</p>
<p>而且 vscode 每一块的大小是也是可以拖动改变大小的，也要在拖动的时候重新计算 left、top 的值。</p>
<h2 data-id="heading-14">总结</h2>
<p>现代软件基本都是有用户界面的，而不同操作系统下构建 UI 的方式不同，所以跨平台渲染的浏览器的方案逐渐流行开来。移动互联网时代之后，为了综合原生的体验和网页的跨平台，出现了跨端引擎的方案，也就是基于安卓、ios 分别实现 dom api 并注入一些设备能力的 api 给 JS 引擎，业务代码通过 dom api 来描述 UI。</p>
<p>dom api 是浏览器提供给开发者的描述 UI 的方式，是物理层。现在的前端框架可以完成组件的封装和数据到 dom 的映射，不再需要直接操作 dom，算是逻辑层。</p>
<p>因为跨端引擎实现了 dom api，所以上层可以对接前端框架。</p>
<p>UI 是通过 css 来描述的，而 css 可以分为两部分： 布局和具体元素的渲染。</p>
<p>具体 font、text、image 等分别有不同的样式来描述如何渲染，而布局是确定每个元素的位置，由 display 配合 position 来确定。</p>
<p>网页的每一个内容都是一个盒，由 content、padding、border、margin 构成，而 display 是设置盒的类型，不同的盒有不同的布局规则，比如 BFC、IFC、FFC、GFC 等。</p>
<p>当有一些需要定制的布局规则，可以使用 position。默认的 position 是 static，也就是流式的，根据上个盒来确定下个盒的位置，可以使用 relative 做一些偏移，如果想相对于某个位置固定，可以使用 absolute，当直接相对窗口的时候使用 fixed。此外，在做吸顶效果的时候，可以使用 sticky，它是基于 static 和 fixed 的封装。</p>
<p>因为文档流的局限性，块盒要在同一行的时候需要用 float 脱离文档流，但有了 flex 盒之后就不用脱离了，在流中放一个 flex 盒就行，内部可以做弹性的横向竖向布局。</p>
<p>知道了 display 和 position 都怎么做布局，也就是计算盒的位置以后，我们看了下 vscode 是怎么布局的。</p>
<p>vscode 是上中下嵌套左中右的结构，窗口改变或者拖动都可以调整每块大小，所以使用嵌套的 absolute 的方式来做整体的布局。每一块的内部则综合使用流式、弹性等方式配合 position 分别做更细节的布局。</p>
<p>css layout 的本质就是确定元素的位置，之前的 css layout 可以说是 display + float + position，现在是 display + position 就可以了。display: flex 可以替代 float 做到更强的布局效果。</p>
<p>网页的 css 布局方案已经应用在越来越多的领域，比如跨端引擎通过安卓、ios 实现 css，kraken 基于 flutter 实现 css，所以 css 的布局方式是我们必须掌握的技能。希望这篇文章能帮大家梳理清楚 css 布局的思路，对各种布局都能够分析清楚特性，然后用合适的方案来实现。</p></div>  
</div>
            