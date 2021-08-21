
---
title: 'Unity跨平台UI解决方案：可能是最全的FairyGUI系列教程-第五天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13a3efde579c462d864e27de436c02ec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 23:32:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13a3efde579c462d864e27de436c02ec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
</blockquote>
<h2 data-id="heading-0">👉关于作者</h2>
<blockquote>
<p>众所周知，人生是一个漫长的流程，不断克服困难，不断反思前进的过程。在这个过程中会产生很多对于人生的质疑和思考，于是我决定将自己的思考，经验和故事全部分享出来，以此寻找共鸣！！！<br>
专注于Android/Unity和各种游戏开发技巧，以及各种资源分享（网站、工具、素材、源码、游戏等）</p>
</blockquote>
<h2 data-id="heading-1">👉即将学会</h2>
<p>从头到尾了解并学习FairyGUI在Unity平台的应用</p>
<h2 data-id="heading-2">👉背景</h2>
<p>Unity 2019.x系列</p>
<p>FairyGUI 2021.2系列</p>
<h2 data-id="heading-3">👉实践过程</h2>
<h3 data-id="heading-4">组件-重点</h3>
<p>组件是什么？</p>
<p>你点击资源->新建组件，看看出现什么</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13a3efde579c462d864e27de436c02ec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>这不就是舞台（中央操作区）做布局用的吗？没错，组件就是布局，可以理解为组件就是Unity中的Canvas，Android中的xml布局，那既然是布局，就可以封装布局（封装组件），所以：</p>
<ol>
<li>组件可以包含多个元件（布局里面可以包含多个控件），比如舞台中有按钮图片等</li>
<li>组件可以包含组件（布局可以嵌套布局），比如复用性较高的控件封装一个组件，在主组件中拖入使用</li>
<li>组件封装后，可以把她整体又当成一个元件</li>
</ol>
<p>啊，这关系好乱啊，不过仔细想明白后，对FairyGUI的理解就顺畅多了。</p>
<p>来看看组件的属性：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0abcc5ec1cc545c298a2d927b3096a07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<ol>
<li><strong>同时作为锚点</strong> 勾选这个选项后，元件的原点位置将设置为轴心所在的位置。默认情况下，每个元件的(0,0)都是在左上角；勾选了轴心同时作为锚点后，则元件的(0,0)在轴心的位置。Unity中默认是中心为锚点，这是左上角，保持默认即可。</li>
<li><strong>溢出处理</strong> 设置超出舞台矩形区域的内容怎么显示，有可见，隐藏，垂直/水平/自由滚动</li>
<li><strong>自定义遮罩</strong> 详情看下面遮罩内容</li>
<li><strong>点击穿透</strong> 比如带有透明区域的png图片，默认情况下，空白区域点击事件照样触发，勾选后，透明区域不再响应事件，若项目中需要多个带有透明的PNG重叠且各自触发事件，建议勾选，因为不勾选，虽然能够看到下一层的图片效果，但是点击事件被第一层的透明区域拦截了，无法下发到下一层PNG上。</li>
<li><strong>扩展</strong> 详情看下方扩展介绍</li>
<li><strong>设计图功能</strong> 显示在舞台上，做布局的时候可以参考整体的UI图，就像印着写字帖一样，更快速，更精准的布局，甚至都不用UI进行尺寸标注</li>
</ol>
<h3 data-id="heading-5">自定义遮罩</h3>
<p><strong>普通遮罩</strong></p>
<p>可以设置组件内一个图片或者图形作为组件的遮罩。</p>
<p>当使用图形（Graph）作为遮罩时，有图形的区域内容可见，例如，一个圆形，则圆形区域内可见，其他区域不可见。</p>
<p>当使用图片作为遮罩时，图片内透明度为0的像素对应区域的内容不可见，反之可见。超出图片区域的内容不可见。</p>
<p><strong>反向遮罩</strong>（挖洞）</p>
<p>效果和正常遮罩相反，也就是可见的区域变不可见，不可见的区域变可见。</p>
<p>使用图形（Graph）作为遮罩时，有图形的区域内容不可见，例如，一个圆形，则圆形区域内不可见，其他区域可见。</p>
<p>使用图片（Image）作为遮罩时，图片内透明度为0的像素对应区域的内容可见，反之不可见。超出图片区域的内容可见。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6647ad6b62734e6faf75ea3f86c7a008~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/6998782565897207839" loading="lazy" referrerpolicy="no-referrer">扩展</h3>
<p>这个功能就相当有意思了，刚才我们说了，中央操作区也是一个组件，一个组件就相当于一个页面，一般都是只有一个主页面，当你的页面复杂或者想要分开管理的时候可以创建多个组件，然后放到一个组件里，将这个组将当成主页面。当某个组件（页面）复用性高的时候，这种方法很有用。</p>
<p>Android里面布局代码过多的时候，通常都会提炼出一个布局，或者复用性较高的布局提炼出来（比如APP的标题栏复用很高），这样后续其他布局使用的时候直接使用include关键字直接引入布局，相当便利。</p>
<p>当你选择扩展为“按钮”的时候，会发什么效果？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c8ddf294ba4b9cb3070eff4f499e89~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>修改保存后妥妥的发现组件的图标变成了按钮的图标；</p>
<p>这时候我就产生疑问了：难道按钮进度条这些都是用组件封装的？</p>
<p>我选择不同的扩展，保存后发现组件的图标会对应修改，表现出的效果相当明显了</p>
<ol>
<li>按钮/标签/进度条/下拉框等功能都是组件修改封装而来</li>
<li>组件就相当于基类，你想要实现其他功能，可以在组件上进行修改封装，之后在主组件（主布局）中使用</li>
<li>元件包含基础元件/组合型元件/特殊元件，是官方已经封装好的控件，上面元件有分类，组件就包含元件里面的组合型元件，组件还可以凭你的想象自由组合成新控件</li>
</ol>
<h3 data-id="heading-7">滚动容器</h3>
<p>对组件或者列表设置了“溢出处理”为“水平滚动”、“垂直滚动”，“自由滚动”后，组件或者列表即成为滚动容器。点击“溢出处理”旁边的<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6c559ed96347c8aea4a22c1af533be~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/6998782565897207839" loading="lazy" referrerpolicy="no-referrer">​按钮，可以设置详细的滚动的相关属性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4add7aaa7504130a0000210bebf49b5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<ol>
<li>触摸滚动效果 是否允许用户直接拖拽滚动区域内的内容。一般在移动平台上使用，PC上较少，PC上一般需要拖动滚动条，或使用鼠标滚轮。</li>
<li>滚动条组件 设置滚动条资源。一般不需要设置，全局有一个设置，在主菜单“文件->项目属性->默认值”里。如果你要使用不同于全局设置的滚动条资源，那么在这里设置。</li>
<li>下拉/上拉刷新组件 设置上拉刷新或下拉刷新时需要显示的组件。一般是你封装好的组件</li>
<li>页面模式 以视口大小为页面大小，每次滚动的距离是一页。一般在移动平台上使用，PC上较少，拖动滚动条进行滚动操作与这个模式冲突。</li>
<li>禁用裁剪边缘 一般情况下，视口不包括边缘设置的部分，也即是容器设置四周的留空部分也会被裁剪。如果需要，可以勾选这个选项，使容器四周的留空部分不被裁剪。</li>
<li>浮动显示 勾选后，滚动条不占据视口的位置，而是直接覆盖在视口上面。例如一个适用于手机的滚动条，它是细条且半透明的，只在滚动时才显示出来，用于提示滚动位置。那么我们把它设置为“浮动”，这样就不会挤占视口的显示空间。</li>
</ol>
<h2 data-id="heading-8">👉其他</h2>
<blockquote>
<p>📢作者：小空和小芝中的小空<br>
📢转载说明：务必注明来源：<a href="https://juejin.cn/user/4265760844943479" title="https://juejin.cn/user/4265760844943479" target="_blank">芝麻粒儿 的个人主页 (juejin.cn)</a>。<br>
📢欢迎点赞👍收藏🌟留言📝</p>
</blockquote></div>  
</div>
            