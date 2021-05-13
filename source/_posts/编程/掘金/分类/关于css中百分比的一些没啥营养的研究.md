
---
title: '关于css中百分比的一些没啥营养的研究'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6bc842ad4964c6aae633fefa881da32~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 02:26:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6bc842ad4964c6aae633fefa881da32~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一些不重要的废话</h3>
<p>最近逛掘金发现，掘金有了新的功能模块————创作者中心。然后去看了看，结果是这样的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6bc842ad4964c6aae633fefa881da32~tplv-k3u1fbpfcp-watermark.image" alt="img01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哇~ 全是零~ 啥都没有。。。。。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f20577261ec14a77abfd0e0b2a0cfc47~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是琢磨着还是得整点东西才行。</p>
<p>回归正题，这次想和大佬们聊聊css中得百分比。之前以为子元素设置css中得百分比，都是相对于其父元素进行计算的，后来捣鼓了一下，发现好像没有我想的这么简单。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7a555f9ff1c4297b34aa3cdab3813e0~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">正文</h3>
<p>首先，我们先整一个元素a，再给元素a(紫)加个子元素b(绿)。如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b1e766152d94af58b72af76625888cb~tplv-k3u1fbpfcp-watermark.image" alt="percent1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52777b7d33074d17babab18658149765~tplv-k3u1fbpfcp-watermark.image" alt="percent2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以发现元素b的width是根据父元素a的width计算得来的，元素b的height是根据父元素a的height计算得来的,元素b的margin/padding是根据父元素a的width计算得来的。</p>





















<table><thead><tr><th>子元素属性</th><th>参照的父元素属性</th></tr></thead><tbody><tr><td>width</td><td>width</td></tr><tr><td>height</td><td>height</td></tr><tr><td>margin/padding-(top/left/right/bottom)</td><td>width</td></tr></tbody></table>
<p>然后我们再给元素b加一个子元素c(虽然我早就加进去了，大家假装没有看到就好)，元素c(蓝)的宽高就是按其父元素b的宽高进行计算的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b00085d8f85145c2a601dfc04bd9bb85~tplv-k3u1fbpfcp-watermark.image" alt="percent3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们进行一点点改动...</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c89fdd2afc2b460c9dfd41f076ff2e14~tplv-k3u1fbpfcp-watermark.image" alt="percent4-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>给元素a加上 position: relative; 给元素c加上 position: absolute;
发现现在元素c的百分比是按元素a的进行计算的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0a3e0fbbeca40ce86e72c02d6975d78~tplv-k3u1fbpfcp-watermark.image" alt="img02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f427cc6eac364d50a7e6e313d788a455~tplv-k3u1fbpfcp-watermark.image" alt="img03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>w3school上说是 设置百分比是基于包含块（父元素）；而absolute生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位。所以，这个给我的感觉就是，设置了定位后，百分比的计算是相对于 直接非static定位(默认定位)的父元素。
然后补充一下刚刚的表格：</p>





























<table><thead><tr><th>子元素属性</th><th>参照的父元素属性</th></tr></thead><tbody><tr><td>width</td><td>width</td></tr><tr><td>height</td><td>height</td></tr><tr><td>margin/padding-(top/left/right/bottom)</td><td>width</td></tr><tr><td>top/bottom</td><td>height</td></tr><tr><td>left/right</td><td>width</td></tr></tbody></table>
<h3 data-id="heading-2">发现新问题</h3>
<h4 data-id="heading-3">问题一</h4>
<p>我进行了一点点的小改动：</p>
<ol>
<li>元素a 去掉height，新增min-height</li>
<li>元素b 去掉padding-top</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70bf5400c74439490df73a3789d434c~tplv-k3u1fbpfcp-watermark.image" alt="percent5-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeb808b1513746869eca58fb627cf5de~tplv-k3u1fbpfcp-watermark.image" alt="percent5-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d0cf1cd2c004acc9a27ab3c7ba9e93d~tplv-k3u1fbpfcp-watermark.image" alt="percent5-3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现元素b的height为0，这个我原本理解为子元素参照的是父元素的height，而不是min-height，所以为0。
但是元素c的各项居然没啥影响，这。。。。。。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44044ad333545a5b8358f0a64e0c9e9~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">问题二</h4>
<p>当元素b没有高度的时候，发现顶上出现了一定距离，发现是margin-bottom影响的。但是，为什么呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9138ee4fd6d146f2b0d3f3fb830057c7~tplv-k3u1fbpfcp-watermark.image" alt="percent6-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53728638c5cf404f9f7026eaf2ce1465~tplv-k3u1fbpfcp-watermark.image" alt="percent6-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f636246a364049d2b73d72487eeaf141~tplv-k3u1fbpfcp-watermark.image" alt="percent6-3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大佬们，要是有知道为啥的还望指点迷津，<del>或者我自己研究明白了再来给自己答疑</del></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93fdac647cff47119f99b17896e83558~tplv-k3u1fbpfcp-watermark.image" alt="6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">最后</h3>
<p>第一次写文章，要是有啥没写正确的请大佬们指正。
<del>当然我也不一定会去改。</del></p></div>  
</div>
            