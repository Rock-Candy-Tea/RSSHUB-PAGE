
---
title: '关于 UI设计 切图，我们应该如何给开发人员'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7ef00d42804bb6aa05225bf0fdf86f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 22:56:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7ef00d42804bb6aa05225bf0fdf86f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>每个 UI 设计到了尾声，不可避免的会遇到一些<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mockplus.cn%2F%3Fhome%3D1%3Fhmsr%3Dwenjj" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mockplus.cn/?home=1?hmsr=wenjj" ref="nofollow noopener noreferrer"><strong>切图</strong></a>上的问题，下面我就跟大家分享几个我遇到过的切图问题，希望能帮你避开一些坑，减少重复切图，减少沟通成本！</p>
<p><strong>01 代码更容易实现线性渐变、径向渐变、角度渐变。网格渐变往往需要我们切图</strong></p>
<p>设计中，我们通常用的渐变有：线性渐变、径向渐变、角度渐变、网格渐变。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7ef00d42804bb6aa05225bf0fdf86f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这当中，代码实现线性渐变、径向渐变、角度渐变 相对来说要简单一些，而网格渐变则需要消耗更多的开发精力。我们也不会在这上面去增加开发工作量。</p>
<p>所以，在我们输出设计稿给开发的时候，有网格渐变的部分直接切给开发。</p>
<p>比如下面设计稿上的渐变背景色：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7faf5d46f0344b5db6a830fab65f9f73~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>02 文字能不用透明度就不用透明度，直接给原始的16 进制色值</strong></p>
<p>16 进制色就是在开发中设定颜色的代码，每个颜色都有对应的 16 进制色，如 #000000 是黑色，#FFFFFF 是白色。</p>
<p>比如我在调这个文字颜色的时候可以用 #000000 40% 的透明度，也可以直接用 #999999 这个色，这两个呈现的颜色没有任何区别。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1c938acf6143539f97d271ed9b9cd1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是交给开发写的话，第一种除了要写 #000000 的黑色之外，还要写一串 Alpha 透明值，这样做会更消耗性能，且在不同屏幕分辨率、不同操作系统下，所实现的透明效果也会有偏差。</p>
<p>所以，在这种非必要情况下，样式可以用不带透明度实现的话，就不要带。</p>
<p><strong>03 切一整张大图，可能会发生拉伸变形或是图片被裁剪的问题</strong></p>
<p>如果是一整张的切下来，会导致不同尺寸的手机把切图拉伸变形，或者会裁剪多出比例的部分。</p>
<p>比如我们切的这张启动页大小为 375*812 的三倍图，这张图在 iphone13 mini（375*812px）和安卓（360*640px）上等比展示就会产生不同的效果——</p>
<p>安卓屏就会被裁切掉一些（展示图片来自网络）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39d63055f620403db7653ac441f0fe68~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如何保证在这种情形下，启动页的图片可以适配不同尺寸的屏幕呢？</p>
<p>我们可以将上下分开切，让开发分别定上面插画和logo的位置，以此保证他俩都能完整展示。</p>
<p>将一张图切成这两张：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df3bf6e74d2d4818aed4c30d101ff183~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>设定插画距离头部是 30px，底部 logo 距离底部是 30px</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a039ea156d764a9784db289d471b2491~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样在其他屏幕上，也是依照「插画距离头部30px，底部 logo 距离底部是 30px」这个规则来写，就能保证这张图上的所有内容不被裁切了！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b7bc56662fc4509a370730503329efc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>04 不要将切片与 icon 贴在一起</strong></p>
<p>一些初次切 icon 的同学会这么做↓</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29190da8c9c944cd9eb012dc6166c243~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这么做会导致以下几点问题：</p>
<p>· 如果 icon 有 0.5 像素点，那么贴边切很可能会被裁掉一些；</p>
<p>· icon 的高矮长宽不一，但开发会全按一个尺寸来写，导致 icon 被拉伸或压缩；</p>
<p>· icon 设计规范不一致，出现各式各样的尺寸。</p>
<p>所以我们都会给一套的 icon 固定一个同样大小、正方形的框，以此来规避掉以上出现的问题。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15f0616fad1f4b458e149256f8378afd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>05 通知icon与带数量的小红点不用切在一起</strong></p>
<p>我们在做通知消息的时候右上角会有消息数量的标识：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcac433bb1a44f8f8f38533195bd18e5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当数字分别为个位数、十位数、99+ 时，红色底板的宽度会根据数字长短发生变换：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6061b66a3143d8875f115dd33f5d41~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们不需要每种情况的小红点都切一遍，只需要定好数字在红底里的左右间距，让开发根据数字长短做自适应即可。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24753aeec6424046baacaca080588617~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们提供切图只需要切铃铛部分。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eedf005a853b43808e29a45b743dcaa4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>总结</strong></p>
<p>以上就是我在实际项目中遇到的切图问题了，切图是一项靠经验积累的 UI 必修课，希望你在阅读之后留个印象，以后遇到类似问题也有了解决之法。</p>
<p>切图就用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mockplus.cn%2F%3Fhome%3D1%3Fhmsr%3Dwenjj" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mockplus.cn/?home=1?hmsr=wenjj" ref="nofollow noopener noreferrer"><strong>摹客</strong></a>。</p>
<p>以上文章来源于菜心设计铺 ，作者花菜</p></div>  
</div>
            