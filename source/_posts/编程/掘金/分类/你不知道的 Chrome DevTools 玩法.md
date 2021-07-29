
---
title: '你不知道的 Chrome DevTools 玩法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6243655db63d4ca3980ab7511789aa73~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 03:08:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6243655db63d4ca3980ab7511789aa73~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>笔者在前段时间的开发时，需要通过 <code>Chrome DevTools</code>来分析一个接口，调试中发现了控制台中的 <code>copy</code> 函数，非常的好用，进而发现了新世界，学习到了 Chrome 一些奇怪的调试技巧，这里总结分享给大家，希望能对各位的开发起到帮助！</p>
</blockquote>
<p>多图预警，建议在Wifi环境下阅读本文章。</p>
<h2 data-id="heading-0">开发者工具函数</h2>
<h3 data-id="heading-1">copy</h3>
<p><code>copy</code> 函数可以让你在 <code>console</code> 里拿到任意的资源，甚至包括一些变量，在复制一些特别冗长的数据时特别有用，当复制完成后，直接使用 <code>ctrl + v</code> 即可。</p>
<p><code>copy</code> 接受一个变量作为参数，如果有多个参数，则忽略第一个后面的所有参数，当需要复制不存在变量名的数据时，可以配合 <code>Store As Global</code> 来使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6243655db63d4ca3980ab7511789aa73~tplv-k3u1fbpfcp-zoom-1.image" alt="copy的使用" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">Store As Global</h3>
<p>当我们从控制台获取一些数据却没有变量名时（在开发时特别常见），可以通过右键点击数据旁的小三角形，通过其来储存为全局变量，变量名为 <code>temp1</code> 一直延续下去，就可以配合 <code>copy</code> 获取变量名打印了，该功能对 HTML 元素同样适用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f0239faf1954e179b3a7a95ed08bbb1~tplv-k3u1fbpfcp-zoom-1.image" alt="Store As Global的使用" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">$</h3>
<p>这个 <code>$</code> 和 <code>jQuery</code> 中的 <code>$</code> 有部分相似之处，均可以作为选择器来使用，这里依次介绍其用法。</p>
<p>首先是 <code>$0 ~ $4</code> 可以获取点击的 HTML 元素，其中 <code>$0</code> 对应着最后一次点击的元素，<code>$1</code> 次之，依序排列直到<code>$4</code> 。</p>
<p>根据这个操作可以很轻易的复制一个元素，并对其执行一些 DOM 操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f60357a63d446039f2c4ee4c219402a~tplv-k3u1fbpfcp-zoom-1.image" alt="$的使用" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还可以作为选择器使用，其中 有两种用法，分别是单 <code>$</code> 和双 <code>$</code>，需要注意的是，双 <code>$</code> 返回的并非 <code>NodeList</code>而是一个纯正的数组，直接方便了我们在控制台调用API😉。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06be81a0ec0f4849a4774a78aa4ef01a~tplv-k3u1fbpfcp-zoom-1.image" alt="$的使用" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有时仅仅需要获取上一次输出没有变量名的数据该怎么办？这时你心中应该有一个答案，就是通过 <code>Store As Global</code> 把其变为一个变量，但是这样太麻烦了，<code>$_</code> 可以帮你解决这个烦恼，其返回结果就是上次执行结果的引用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f2fcda0344a42b993ebebbcf40141b5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里可以看到并不会重新计算一遍结果，而是直接引用。</p>
<p>最后关于<code>$</code> 命令操作是重磅戏，可以通过 <code>$i</code> 安装 NPM 库，这是一条未曾设想过的道路，笔者查阅发现时，属实被震撼到了。在<code>Console Importer</code> 插件的帮助之下，就可以帮助我们实现这一操作！首先在谷歌应用商店安装好该插件后，在命令台输入 <code>$i('lodash')</code> 后，神奇的事情就会出现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6afb479294d43f68e3d05d7b2e6dd23~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时就可以在 <code>Console</code> 中使用 <code>Lodash</code> 了！</p>
<h3 data-id="heading-4">getEventListeners</h3>
<p>可以方便的获取元素绑定的事件，特别是配合 <code>$</code> 使用，不过获取事件功能也可以在 <code>Element</code> 中查看，主要是当元素嵌套层级深且复杂时，可以不用点击而通过选择器来查看元素。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b8ab601b0d4414294281ded61157d8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">monitor</h3>
<p>这是 <code>DevTools</code> 自带的监听器，简单的说明就是监听函数的函数，使用起来很简单，直接套娃就行。目前没发现有什么特别方便的地方和使用它的需求，了解即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f931f35c1eb14d7e8136fa0c660663a9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">Preserve Log</h3>
<p>在我们调试页面时，经常遇到页面跳转或刷新的情况，此时打印的输出会被刷新掉😭，看不到想要的数据。在调试面板最右边的齿轮图标处，有 <code>Preserve Log</code>选项，可以保存上一次打印的输出，这里用 <code>Math.random</code> 作演示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1413bd2529344805a26d10a8a0f45cc1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">inspect</h3>
<p><code>inspect</code> 提供了一个可以快速跳转到 DOM 元素对应位置的方法，对于一些嵌套层级复杂或者未知的元素，可以通过 <code>inspect</code> 配合调试，将元素的选择器至传入函数中，则会自动跳转到其对应位置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/351db9cf0cdf4986a422602de4619a70~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">元素面板</h2>
<p>元素面板即为 <code>Elements</code> 面板的内容，我们一般用其获取对应元素的信息，比如 <code>Styles && Computed && Layout</code> 等，其中我们会对元素做一些操作，比如操作一个元素的显隐要怎么办？其中一个答案就是右键该元素，然后选择 <code>Hide Element</code>，但这样做有点麻烦，能不能有更好更快的办法呢？答案是有的，直接选择该元素，在键盘上按下 "h" 即可切换元素的显隐状态，Amazing！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc373db4f29048b9b127f8843b71d1ff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不仅如此，还可以直接拖动元素达到调整元素位置的功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afbe7ab7f44c49248976fba2f62bf2bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">Layout</h3>
<p><code>Layout</code> 是归属于元素面板的子面板，在其中可以查看元素的布局，特别是对于 <code>flex && grid</code> 来说，简直是好用的不得了，接下来我们先看 <code>grid</code> 布局的操作:</p>
<p>当用户点击一个使用 <code>grid</code> 布局的元素时，则会显示出其所有的小方格。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794578b8dc9a4a01be30578826c56094~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然这还不够，我们还想要知道更详细的信息，比如每个格子所占的容量，宽度是多少，可以点击 <code>Overlay display settings</code> 下的选项来操作。</p>
<p>其中第一个下拉框可以选择展示 <code>line names</code> 和 <code>line numbers</code>，也就是线段的别名和线段对应的序号。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8b4a09692e7457aaad2a2a342927f70~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>后续三个选项分别为</p>
<ul>
<li><strong>显示轨道大小</strong>：切换以显示或隐藏轨道大小。</li>
<li><strong>显示区域名称</strong>：在具有命名网格区域的网格的情况下，切换以显示或隐藏区域名称。</li>
<li><strong>扩展网格线</strong>：默认情况下，网格线仅显示在带有display: grid或display: inline-grid设置在其上的元素内部；当打开此选项时，网格线沿每个轴延伸到视口的边缘。</li>
</ul>
<p>文字描述可能看起来不好理解，下面有动图挨个解释😊。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8320cca3fdc24261b2a9b6278b55e4e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一选项可以很清楚的看到每行每列的宽度，第二个选项可以看到每一个“块”的别名，第三个选项可能看的不是很清楚，其延伸 <code>grid</code> 的线段至视口边缘，可以仔细观察最下方和最右方，发现会多了几条虚线。</p>
<p>在 <code>Grid overlays</code> 有一个颜色块和一个带有鼠标的虚线块，其功能也很有用，分别是自定义每个 <code>grid</code> 的网格覆盖颜色和突出显示网格。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aebe7cc663a04c9e9eca2183c9219301~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>都说到 <code>grid</code> 了，怎么能不提 <code>flex</code> ？目前在 Chrome 91 版本来看，调试 <code>flex</code> 的功能是要更多一些的，喜欢 <code>grid</code> 的不要担心，在92版本会同步两者的功能！</p>
<p>这里介绍其最新的特性，通过元素面板的 <code>Styles</code> 子面板，在对应元素的样式里多了一个小按钮，点击该按钮能够很方便的切换 <code>flex</code> 的各种布局。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a496d773dc99430896d131416615bddf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">Animations动画组</h2>
<p>还记得刚来组里时，第一个需求需要用到动画展示。当时调试动画全靠一点一点的数值修改，浪费了很多时间。最近发现调试工具中有动画组的概念，能够很方便的调试和观察动画。不过该功能隐藏的很深，藏在 <code>More Tools</code> 里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c6aa93d4e704caab8538102676ce9ba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>里面的功能异常强大，能够捕捉所有当前在运作的动画组，并且修改其速度和耗时，在需要多个动画配合的时候非常好用。这里是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/" ref="nofollow noopener noreferrer">Codepen的官网</a>可通过它来感受 <code>Animations</code> 的强大，其由上至下分为4个区域:</p>
<ol>
<li>最上方的区域可以清除所有捕捉的动画组，或者更改当前选定动画组的速度。</li>
<li>第二行可以选择不同的动画组，此时下方面板将会更新为当前动画组的动画时间线。</li>
<li>在中间拥有时间线的区域，可以理解为动画的进度条，可以通过拖动来跳转到动画对应的时间点。</li>
<li>在最下方的区域里，可以修改选定的动画。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/155df51d935045649a8f6f472186bfb8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在使用动画组捕捉动画后，我们可以进行慢速播放，重播动画。把鼠标放在动画上面则可以看动画预览，这里最棒的就是可以体验不同动画组合过后的效果，并修改动画组的时间与延迟，甚至是关键帧偏移。</p>
<p>可以拖动动画的实心圆，也就是其关键帧，来控制动画的持续时间（最左和最右的两个实心圆）。也可以拖动中间的实心圆来控制运动曲线，可以通过调试来获得最想要的效果。</p>
<p>中间有一条红色的线，可以拖动它来控制当前动画执行的过程在哪里，这里注意左侧的拖动和右侧动画的转变。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a872933b9574e8ea00e74129caaa123~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了动画组，排列组合再也不是梦！</p>
<h2 data-id="heading-11">完结撒花</h2>
<p>本次介绍的功能多是一些笔者认为实用的功能，比如各种命令行函数，又或者是 Chrome 的新特性，比如 <code>flex && grid</code> 的调试功能，这些功能在开发中若是处置得当，能够很好的提升开发效率，当然还有很多很多调试功能没有介绍，毕竟如何利用好 <code>DevTools</code> 也是一门很深的学问，这些特性就留在日后开发中挖掘再来补坑吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1474641c84da4d22838159d50571e9f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            