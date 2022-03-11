
---
title: 'iPad 横屏适配经验'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/hm8plAY2W1D04Rm7uXBG.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 11 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/hm8plAY2W1D04Rm7uXBG.jpg'
---

<div>   
<blockquote><p>编辑导语：虽然国内软件的iPad用户占比不大，但依然存在着横屏适配的需求。本文作者讲述了自己做iPad横屏适配的背景，并对竞品的适配方式进行了分析研究，用自己的亲身经历提供了参考，推荐对ipad横屏适配感兴趣的童鞋阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-768165 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/hm8plAY2W1D04Rm7uXBG.jpg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景</h2>
<p>在我参与的一款资料查询 App 中，对 iPad 只支持竖屏以手机 UI 尺寸拉伸，每个季度都有用户反馈希望适配 iPad 横屏。经过询问用户发现，因为 iPad mini 尺寸刚好可以放在工作服口袋中，随时拿出来使用，而 iPad 屏幕远比手机大，浏览资料视野更大更舒服。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/cgLGKc4xYh0mPCBkZAZs.png" alt="iPad 横屏适配经验" width="600" height="400" referrerpolicy="no-referrer"></p>
<p>但另外一方面，后台数据显示当前 iPad 用户占比只有 1%，用户呼声够不上星星之火，不足以燎原。先别谈说服团队做 iPad 横屏适配，连说服自己都难。本来以为这事就像水中投石，水波消散就没有下文了。直到有一天，同样是资深用户的高管自己拿着 iPad 装上我们的 App 用了几天，终于忍不了，开始推动 iPad 横屏适配。</p>
<h2 id="toc-2">二、参考</h2>
<p>我们肯定不是第一个做 iPad 横屏适配的，但在网上搜了一圈，别说横屏适配，连 iPad 界面设计的文章都很少，下面 3 篇算不错的。这也是我决定写下本文的原因，为后来者提供经验，少踩坑。</p>
<ol>
<li>《利用好 iPad 的大屏幕 —— 如何为 iPadOS 14 设计 app？》，https://steppark.net/15942969497015.html</li>
<li>《iPad 交互设计探索系列：iPad 适用产品篇》，https://www.jianshu.com/p/65211fddefb9</li>
<li>《iPad 交互设计探索系列：iPad 导航设计篇》，https://www.jianshu.com/p/0c8e315d39d4</li>
</ol>
<h2 id="toc-3">三、研究</h2>
<p>没得经验参考就只能先从竞品分析开始了。经过对 iOS 系统应用、微信、QQ、微信阅读、得到、豆瓣、淘宝和有道词典的分析，我和同事总结成 5 种横屏适配模式。</p>
<h3>1. 内容响应式</h3>
<p>典型 App：iOS 应用商店</p>
<p>特征：标题栏和 Tabbar 通栏拉伸，内容区根据宽度向右响应式布局。</p>
<p>适用场景：全部场景。</p>
<p>评价：灵活性和用户体验都很好，但设计和开发成本很大。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/JOsZuOKpVdjLL1defxTJ.png" alt="iPad 横屏适配经验" width="600" height="278" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/Pf4YfPbiT71ksAMymUMq.png" alt="iPad 横屏适配经验" width="600" height="278" referrerpolicy="no-referrer"></p>
<h3>2. 左右分栏</h3>
<p>典型 App：iOS 设置、淘宝、微信、QQ</p>
<p>特征：左右分开显示，左边通常固定显示首页或者目录导航。右侧根据左侧选择显示对应的详情内容。</p>
<p>适用场景：频繁需要使用导航切换内容。</p>
<p>评价：用户体验适中，合理的利用横屏更大地展示更多的内容。设计成本小，需额外设计一个右侧默认为空的情况。开发成本要看是否改程序架构，相当于把手机两个手机界面合并成一个屏幕，可能有些程序架构很难这么修改。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/KqLEbvoUpzbT2Yn9CzX0.png" alt="iPad 横屏适配经验" width="600" height="278" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/nIIZKEhRrGWJDzO93BiJ.png" alt="iPad 横屏适配经验" width="599" height="380" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/v8hzgzTRgZKU9qM5Xu5h.png" alt="iPad 横屏适配经验" width="599" height="743" referrerpolicy="no-referrer"></p>
<h3>3. 按竖屏宽度显示</h3>
<p>典型 App：微信阅读</p>
<p>特征：标题栏和 Tabbar 通栏拉伸，内容直接按竖屏的宽度显示。</p>
<p>适用场景：全部场景。</p>
<p>评价：用户体验适中，设计与开发成本小，大多数产品采用此模式，但是没有更好的展现横屏宽屏的优势。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/iC7FsDUmwXJIJBrpmyiP.png" alt="iPad 横屏适配经验" width="598" height="277" referrerpolicy="no-referrer"></p>
<h3>4. 全屏通栏拉伸</h3>
<p>典型 App：豆瓣</p>
<p>特征：横屏为全屏通栏拉伸，所有元素与竖屏一致。</p>
<p>适用场景：全部场景。</p>
<p>评价：设计和开发成本最小，但是相当于没有适配。用户体验较差，横屏情况下内容集中，左侧右侧很空，或者被拉得很长，阅读体验较差。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/ScEI7Ui9UhKCVMgcpYmM.png" alt="iPad 横屏适配经验" width="600" height="262" referrerpolicy="no-referrer"></p>
<h3>5. 混合模式</h3>
<p>当然也不是所有 App 都采用单一的模式。比如微信阅读，在其他页面是按竖屏宽度显示。但到了图书阅读界面，则是左右分栏充分利用 iPad 大屏幕展现内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/DyMhyUct3wDpKnZkupHZ.png" alt="iPad 横屏适配经验" width="600" height="278" referrerpolicy="no-referrer"></p>
<p>以上竞品分析所有截图我们都保存在 Figma 中，有需要的读者可前往获取。</p>
<p>链接：https://www.figma.com/community/file/1071850659054902697/iPad-横屏适配竞品分析</p>
<h2 id="toc-4">四、执行</h2>
<p>非常遗憾的是虽然高管牵头做适配，但开发资源确实有限。不能为了设计师邀功拿业绩就从头把 iOS App 重构一遍，因此我们决定用最少的资源做最核心的优化。</p>
<p>适配计划分为 2 期。第 1 期将所有页面用按竖屏宽度显示进行横屏适配。第 2 期挑选核心页面用内容响应式或左右分栏进行优化。</p>
<h3>1. 先开发再验收</h3>
<p>在第 1 期我们就踩坑了，按照原来的工作流程，我们将所有的 iPad 横屏页面做好线框图、再输出所有视觉效果图。虽然都是线上页面不用重新设计，只需要拉伸画面或者调整间距，但所有线上页面也是一个不小的工作量。</p>
<p>就在进行过程中，iOS 工程师就皱着眉头来提议，由于代码架构和资源所限，设计师如果调整的视觉效果图未必能 100% 实现。<strong>不如反过来，让他先把所有页面强行横屏，再由设计师走查发现问题进行修改，这样节省时间效果也可控。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/t9ebXEPUO3SaDVlV4ma0.png" alt="iPad 横屏适配经验" width="597" height="89" referrerpolicy="no-referrer"></p>
<p><strong>可见，不同的项目类型可以采取不同的工作流程。</strong> iPad 横屏适配项目流程和常规工作流程刚好相反，以往是先设计再开发，改成先开发再走查，节省设计师产出效果图时间，也保障最终实现效果。</p>
<h3>2. 核心场景决定核心页面</h3>
<p>在第 2 期挑选核心页面时，我也犯了错误。最开始我觉得核心是脸面，因此挑选 Tabbar 导航的首页、个人中心等用户一打开 App 就看得到的页面进行优化。但实际上用户真正的核心使用场景是在详情页查阅资料，这才是真正的核心页面。</p>
<p>在得到主管纠正后，我们转而开始为资料阅读页面提供左内容右目录的布局，便于用户方便地在长文中精确定位想读的内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="iPad 横屏适配经验" src="https://image.yunyingpai.com/wp/2022/03/PeUbTOx71atlYCALQc4P.png" alt="iPad 横屏适配经验" width="598" height="450" referrerpolicy="no-referrer"></p>
<p>2 期计划并非适配的终结，随着 App 功能的迭代，此后老界面修改和新界面设计需要考虑到 iPad 横屏的适配问题，就成为了日常工作的内容了。</p>
<h2 id="toc-5">五、总结</h2>
<p>按照以往的项目总结，最后应该汇报项目数据结果。但由于 iPad 用户本身可怜的占比，即使我们官方公众号推文宣布适配 iPad 横屏后，也没有 iPad 用户站出来点赞，而是又引发出使用华为、小米等安卓 Pad 的用户，要求也适配。</p>
<p>考虑到不同的安卓品牌适配方式不一样，而且安卓厂商自己又有平行世界等通用兼容方案，我们就没再继续参与了。</p>
<p>虽然没有外部用户反馈，但公司内部同事和开发团队使用后确实感觉很棒。所以我觉得这次适配项目真正值得思考的是：<strong>如果一个需求用户反馈很少，也没有数据支撑，但对体验影响很大，如何推动团队进行优化呢？</strong></p>
<p> </p>
<p>作者：龙爪槐守望者，微信公众号：龙爪槐守望者</p>
<p>本文由 @龙爪槐守望者 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5350709" data-author="81282" data-avatar="http://image.woshipm.com/wp-files/2016/04/mylogo.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            