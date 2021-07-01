
---
title: '关于前端position属性和display属性，这篇文章已足够'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c27838307242fcb06a76404f6e00b1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:42:43 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c27838307242fcb06a76404f6e00b1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在我初学前端的时候，对position和display，尤其是flex特别的混乱，故总结一套，希望能帮助到有需要的同学。这里我想特别告诫一下移动端学习web的同学，例如position:relative，web端叫相对定位，意思是这个属性加在一个元素上，这个元素就使用相对定位的规则在ui上去渲染；而不是和移动端那样设置了相对布局，子布局里都按相对布局去排列，和移动前端还是有很大的差别的，只要记住相对定位和相对布局是有区别的。
<br></p>
<h2 data-id="heading-0">一、关于position属性</h2>
<h3 data-id="heading-1">1.1、position:static</h3>
<p>默认值，没有定位，置顶元素使用正常的布局行为，即文档常规流中当前的布局位置，此时top、bottom、left、right属性无效。
<br></p>
<p>例：我在外层黄色div往里放了1个红色和蓝色div标签，如下（当然position不写默认就是static）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c27838307242fcb06a76404f6e00b1~tplv-k3u1fbpfcp-watermark.image" alt="static.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1.2、position:relative</h3>
<p>相对定位，不脱离文档流。参考自身静态位置，通过top、bottom、left、right定位，并且可以通过z-index进行层次分级
<br></p>
<p>例：我在蓝色div里放置了一个红色div；红色div的css如下，</p>
<pre><code class="copyable">.box1 &#123;
  width: 400px;
  height: 300px;
  background: red;
  position: relative;
  left: 50%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终ui如下图，可以看到红色div确实离左边的距离为蓝色的一半
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38ce7166f07c44d6bd38518bc65e543a~tplv-k3u1fbpfcp-watermark.image" alt="relative.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">1.3、position:absolute</h3>
<p>绝对定位，脱离文档流。通过top、bottom、left、right、定位。定位的起始位置由最近不为static的父元素。否则为body的坐标原点。可以通过z-index进行层次分级
<br></p>
<p>例：粉色div设置为position:static。在粉色div放入一个红色div设置为position:absolute,使用了left:10%。最终如下图，可以看到红色div不是以粉色区域定位，而是往上找到黑色区域定位。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62ae4208bcf74550acaa9f93cb736b94~tplv-k3u1fbpfcp-watermark.image" alt="absolute_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假如把粉色div改成position:absolute或者是position:relative的话最终如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/401fd9e650914118901be53d943df118~tplv-k3u1fbpfcp-watermark.image" alt="absolute_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">1.4、position:fixed</h3>
<p>固定定位，脱离文档。相对于浏览器窗口进行定位。怎么拖动滚动条都不会发生变化
<br></p>
<p>例：红色div设置position:fixed。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13f219b5b1df4a5eb7c29f4e317a8fa6~tplv-k3u1fbpfcp-watermark.image" alt="fixed.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">1.5、position:sticky</h3>
<p>粘性定位，他是relative和fixed的结合。当即将要画出屏幕时他就是fixed，否则和relative无异。使用sticky要搭配top、bottom、left、right来使用，否则不生效。例如写上top:0%，意思就是在top:0%这个临界点时会在relative和fixed之间切换
<br></p>
<p>例：给红色div设置position:sticky，top:0%</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe6e052493514d599fc9579f740f8da4~tplv-k3u1fbpfcp-watermark.image" alt="sticky.gif" loading="lazy" referrerpolicy="no-referrer">
<br>
<br></p>
<h2 data-id="heading-6">二、关于display属性</h2>
<h3 data-id="heading-7">2.1、display:block</h3>
<p>块级元素:</p>
<ul>
<li>总是以一个块的形式表现出来，占领一整行。若干块级元素会从上到下依次排列(使用float属性除外)</li>
<li>可以设置宽度、高度，各个方向margin及padding</li>
<li>当元素宽度width没有设置时，他的宽度充满容器</li>
<li>块级元素可以嵌套其他块级元素及行内元素</li>
<li>块级元素的display默认为block</li>
<li>块级元素有：div、h1、h2、p等等</li>
</ul>
<p>例：页面放了4个块级元素。对第3个红色div,写上了float:right后。就如同上面的第一条说的那样打乱了它的结构不会依次排列了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9af19d3d76c4a9eb3a09c8529b25e50~tplv-k3u1fbpfcp-watermark.image" alt="block.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">2.2、display:inline</h3>
<p>行内元素：</p>
<ul>
<li>它不会单独占据一行，只占据自身高度和宽度所在空间，即元素的宽高是由其文本内容撑开。若干行内元素从左到右(行内元素可以共处一行)，从上到下排列</li>
<li>行内元素不能设置宽高</li>
<li>行内元素只能设置左右margin和padding，不能设置上下margin和padding</li>
<li>行内元素使用float属性后，设置宽高生效</li>
<li>行内元素有：title、span、a、strong</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc5cfc71d2fb4999ba16ff6fb247742c~tplv-k3u1fbpfcp-watermark.image" alt="inline.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2.4、display:inline-block</h3>
<p>行内块级元素：</p>
<ul>
<li>结合了inline和block特性，既能设置宽高也不会换行</li>
<li>行内块级元素起始就是行内元素设置宽高可以生效</li>
</ul>
<br>
<br>
<h2 data-id="heading-10">三、比较特殊的display:flex</h2>
<p>弹性元素：
这里虽然是在display里，但是我个人感觉他更像是position属性，准确点更像是移动端的布局，因为position准确的说是定位方式。设为flex布局后，子元素的float，clear和vertical-align属性将失效。简单说设置为display:flex后，此元素即为弹性布局容器，接下来是说此容器的属性</p>
<h3 data-id="heading-11">3.1、容器属性：flex-direction</h3>
<ul>
<li>row(默认值)：主轴为水平方向，起点在左端</li>
<li>row-reverse：主轴为水平方向，起点在右端</li>
<li>column：主轴为竖直方向，起点在上沿</li>
<li>column-reverse：主轴为竖直方向，起点在下沿</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b22d79b332324e28b57e402d9a409ff1~tplv-k3u1fbpfcp-watermark.image" alt="flex-direction.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h3 data-id="heading-12">3.2、容器属性：flex-wrap</h3>
<ul>
<li>nowrap(默认值)：不换行</li>
<li>wrap：换行，第一行在上方</li>
<li>wrap-reverse：换行，第一行在下方</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87a3b6a0e03549a4bb3ed4a065be5b9a~tplv-k3u1fbpfcp-watermark.image" alt="flex-wrap.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h3 data-id="heading-13">3.3、容器属性：justify-content</h3>
<ul>
<li>flex-start(默认值)：左对齐</li>
<li>flex-end：右对齐</li>
<li>center: 横轴方向居中</li>
<li>space-between：两端对齐，项目之间的间隔都相等</li>
<li>space-around：每个item之间间隔相等，所以2个item之间的间隔比边缘item到边框的距离大一倍</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28126b367b274596aabe54e2c244bf56~tplv-k3u1fbpfcp-watermark.image" alt="justify-content.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h3 data-id="heading-14">3.4、容器属性：align-items(单根轴线)</h3>
<ul>
<li>flex-start：交叉轴的起点对齐</li>
<li>flex-end：交叉轴的终点对齐</li>
<li>center: 交叉轴的中点对齐</li>
<li>baseline：项目的第一行文字基线对齐</li>
<li>stretch(默认值)：如果未设置高度或为auto,将占满整个容器</li>
<li>注意点：在弹性布局下，子元素未设置高度，内容文案align-items失效，不会横向居中。得用text-align='center'才生效</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a754a69145ec4609ab9a1bfb97b04e83~tplv-k3u1fbpfcp-watermark.image" alt="align-items.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h3 data-id="heading-15">3.5、容器属性：align-content(多根轴线)</h3>
<ul>
<li>stretch(默认值)：轴线占满整个交叉轴</li>
<li>flex-start：交叉轴的起点对齐</li>
<li>flex-end：交叉轴的终点对齐</li>
<li>center: 交叉轴的中点对齐</li>
<li>space-between：与交叉轴2端对齐，轴线之间间隔平均分布</li>
<li>space-around：每根轴线2侧间距都相等，所以轴线间的间隔比轴线到边缘的间隔大一倍</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e93a4874afc4926a42d89f182540622~tplv-k3u1fbpfcp-watermark.image" alt="align-content.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">3.6、弹性布局子元素的单独属性（注意：子元素属性。上面的是容器属性）</h3>
<h4 data-id="heading-17">3.6.1、align-self</h4>
<ul>
<li>auto(默认值)：元素继承父容器的align-items属性，如果没有父容器则为stretch</li>
<li>stretch：元素被拉伸以适应容器，如果指定纵轴大小的属性为auto，则其值会使项目的边距盒尺寸 尽可能接近所在行的尺寸，但同时会遵照'min/max-width/height'属性的限制</li>
<li>center：元素位于容器中心，弹性布局子元素在纵轴上居中放置</li>
<li>flex-start：弹性布局子元素在纵轴上的起始位置(顶部)</li>
<li>flex-end：弹性布局子元素在纵轴上的终止位置(底部)</li>
<li>baseline：弹性布局子元素与基线对齐</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0076935f56454c05b6ba226880c5ad90~tplv-k3u1fbpfcp-watermark.image" alt="align-self.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h4 data-id="heading-18">3.6.2、Order</h4>
<p>项目的排列顺序，数值越小，排列越前。默认为0</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77783679f49b4c0aa235fc205581691a~tplv-k3u1fbpfcp-watermark.image" alt="Order.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h4 data-id="heading-19">3.6.3、flex、flex-grow、flex-shrink</h4>
<p>这几个属性呢有点类似移动前端的线性布局：</p>
<ul>
<li>flex和flex-grow都是使元素放大，但放大的计算公式不同</li>
<li>flex-grow： 剩余空间为弹性布局剩余宽度，然后根据比例分配</li>
<li>flex： 剩余空间为弹性布局剩余宽度与进行flex的子元素宽度之和。然后根据比例分配</li>
<li>flex-shrink： 这个属性和上面2个类似，只不过数值越大，反而缩小的越大</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba7428580a9543fda95ea6ec89f05688~tplv-k3u1fbpfcp-watermark.image" alt="others.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">四、再加上个自己总结的一个简单的后台管理</h2>
<p>希望能帮助到有需要的同学
<br>
<a href="https://github.com/lihangleo2/easy-vue-element-admin" target="_blank" rel="nofollow noopener noreferrer">github地址：https://github.com/lihangleo2/easy-vue-element-admin</a></p></div>  
</div>
            