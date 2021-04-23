
---
title: '如何搭建HMI：设计规范（上）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ziuquGGFjMzf9zYb5ASQ.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 23 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ziuquGGFjMzf9zYb5ASQ.jpg'
---

<div>   
<blockquote><p>导语：本文作者入行做车载HMI已有2年余久，沉淀输出了一些行业内容的内容。HMI行业还是一片蓝海，很多设计师都不敢轻易的进入这个新型的行业，觉得有难度、门槛、视觉要求高。这篇文章先带你入行，文章以一些HMI基础知识作为讲解，在设计规范的内容作者会添加很多干货，结合实际案例讲解。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4486146" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ziuquGGFjMzf9zYb5ASQ.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>先给大家打一个预防针：（规范是用来打破的，本篇文章只做为参考价值）</p>
<p>设计规范包含什么内容？</p>
<p>设计规范包含：视觉规范和交互规范，本章节先说一下视觉规范，车载交互内容会安排在后续写作中…</p>
<p>视觉规范：车载端设计和移动端、web端设计显示差别还是蛮大的的，最主要的差异就在于布局的不同，接下来我们从文字、颜色、布局、圆角、图标 等角度讲解，PS：偶尔还会穿插一些工作心得的内容。</p>
<h2 id="toc-1">一、文字规范</h2>
<p>文字是UI界面设计中重要的组成元素，对于文字的使用是检验设计师基础功底的时候，用的好坏会直接影响到用户在使用产品的过程中的一个体验，文字的使用从这几个纬度出发：字体选择、字号大小、颜色、字重、行高。</p>
<h3>1. 字体选择</h3>
<p>我要做一个良心的博主，让你们避免侵权问题，别在傻乎乎的犯字体侵权的错误了。</p>
<p>在做车机系统设计的时候，需要选定该款车机中文、英文、数字或多国语言需要用什么字体。</p>
<p>如果在乙方公司呢，客户会指定给到你相对于的字体包，插播一段小插曲（职场心得）：当客户选定字体后，如果该款字体是付费字体，你得先和客户确认是否得到使用许可，避免后续官司纠纷）在甲方爸爸工作的同学一般会遇到两种情况：</p>
<ol>
<li>公司已明确字体（请专业字体设计师设计一套）；</li>
<li>用常规设计的字体，建议使用（中文字体：思源黑体、英文/数字：Roboto）如果有做海外项目的，对于Roboto未涵盖的语言，建议使用Noto Sans字体。Noto Sans源自类似于Roboto的度量标准，旨在实现视觉上和谐的国际化。</li>
</ol>
<p>这边肯定会有人问为什么不能用苹果字体呢？他不是免费字体嘛？</p>
<p>普及一下：首先该车机系统属于商业用途，并且未得到许可使用，这就是侵权，在app store上 发布的app是可以免费使用的，因为这是在苹果生态下使用，所以不属于侵权。</p>
<h3>2. 字号大小与字阶</h3>
<p><strong>2.1 字号大小</strong></p>
<p>车机端的字号大小的制定也是要循规蹈矩，字号肯定要远大于移动端和web端，为了确保文字信息的扫描性，结合了：基于IDX & 同济 (2020) 百度Apollo中控视觉基础研究项目，设置清晰的文字阶级参数，还有谷歌Android Automotive OS 研究，以下是用字的规范（标红色区域是他们之间的区别）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/U3cfR6aW2fnN3rRMrfVI.png" width="704" height="326" referrerpolicy="no-referrer"></p>
<p>可参考谷歌：字体大小的遵循4px倍数大小增量</p>
<p>我们在做项目的时候，规定的字体大小维持在4px，这样有助于保持一致性和视觉层次感。</p>
<p><strong>2.3 用字的注意事项</strong></p>
<p>字体大小要控制在20px，这个要谨慎使用，一般都是使用在小标签辅助类的文字上，最小的正文字号为24px。</p>
<p><strong>2.3 设定文字规范有两个好处</strong></p>
<ol>
<li>文字样式复用，不管对于设计师还是开发同学来说，都是极大提高工作效率的一件事情；</li>
<li>对于界面设计来说，有规可循，避免设计时降低的整体的视觉感。</li>
</ol>
<h3>3. 字体用色规则</h3>
<ol>
<li>文字与背景颜色对比度要遵循WCAG的标准，需要考虑到无障碍设计需求，因此保持在4.5:1 – 7:1对比度，确保文字清晰易读；</li>
<li>将注意力需要集中最重要的区域内容；</li>
<li>文本元素之间传达视觉层次感。</li>
</ol>
<h3>4. 字体字重</h3>
<p>字重是指一种字体的粗细样式，下面展示字重的种类：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gOLwQVsvq3BSbBBMRhmC.png" width="605" height="303" referrerpolicy="no-referrer"></p>
<p>上实际案列讲解：</p>
<p>谨慎使用中等字体粗细 ，尽量别用最粗的字体，这样会使得页面感觉差别很大，过度的不是那么自然，没有了细腻、轻盈的感觉。</p>
<p>所以在制定字体规范的时候就尽量将Bold 字重去掉，如果你想通过加粗字体的方式来和下面信息作为区分，请选择Medium字重（根据实际项目需求来定，我的规范只做参考价值）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/RrmEmeAEq3e6BT0uTX80.png" width="598" height="374" referrerpolicy="no-referrer"></p>
<h3>5. 字体行高</h3>
<p>为什么要加这一pa，因为这个问题一直有小伙伴问到我 我就一次性解决了，文字模块需要增加安全距离，这块比较复杂不行我后期录一期视屏讲解，下文也有详细的讲解。</p>
<p>字体的文本的高度一直困扰着设计师，我该用什么方式去对接开发？在设计过程我们是否可以使用文字字号的高度进行对齐方式，而不是使用文字区域的行高，NO 肯定是不可以的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/JI385ybFn7OZk2simFTG.png" width="599" height="284" referrerpolicy="no-referrer"></p>
<p>微信朋友圈主页作为案列：</p>
<p>文本的行高肯定是要大于字号的，个人动态的字号为16px（在@1x设计稿中）如果是多行文本的时候，微信是手动调整了文本行高（正常Line：22px  微信实际Line：20px），当行高为20px的时候，需要将文本上移3px 才能使得图片和文本视觉在一条线上面。</p>
<p>如果按照这个进行开发的话，开发小哥需要在CSS属性过程中注意图片和文本之间的实际差异，这种左右高度不一致的设计，会直接导致在开发布局过程中变得更加繁琐。</p>
<p><img data-action="zoom" class="aligncenter" title="undefined" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/07JID9x1vcQ7mcCtyAFm.png" alt="undefined" width="601" height="338" referrerpolicy="no-referrer"></p>
<p>最后的结论：按照文本的行高来对接开发 。</p>
<p>普及一下小知识点：车载的段落的行高一般为字号的140%-180%的视觉呈现，提供舒适的阅读环境给到用户（取整数）下面是一些专业性的知识了解一下：在设计字体过程中，字体设计师一般都会给字体预留安全距离，让字体展示更加稳定。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/BXhc0nwvdMKz7m4A79Hc.png" width="600" height="269" referrerpolicy="no-referrer"></p>
<p>我们在做设计的时候，将字号设置为30px，但实际字体的空间是需要包含上下部分的安全距离，最终实际高度就变成了42px（Font:pingfang） 穿插一个小干货：在不同字体下相同字号，行高（Line Height）是不同的，Ant Design的30号字，行高为38px （详见配图  计算方式）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/NYsEtCw9Q6En7dyJjXl2.png" width="603" height="251" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、颜色规范</h2>
<h3>1. 使用场景</h3>
<p>场景：白天阳光暴晒（阳光强度有很多档位早、中、下午） 、 梅雨季节阴雨连天 、夜晚模式、地下隧道等。</p>
<p>驾驶汽车在室外不确定因素会比较的多，光线强度的干扰尤其重要，照明会根据一天中的时间、天气、窗户的色调等等而有很大不同。当你设计的车载应用程序在现实世界中使用时，在设计时在计算机上看到的颜色并不总是相同。</p>
<p>考虑颜色亮度如何影响驾驶条件，以及低对比度的颜色在阳光直射下如何被洗掉。始终在多种光照条件下预览您的应用，以查看颜色的显示方式。如有必要，请进行调整以在大多数用例中提供最佳的观看体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/dm9lwwsjQZmKYEdNcrWt.png" width="598" height="538" referrerpolicy="no-referrer"></p>
<p>最初车机厂商系统大多数都是偏爱深色背景，具有代表性的两家系统谷歌的 Android Auto 系统和苹果 Carplay 系统，我在做项目最初也是沿用了深色系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UH1r76tPiSgS68LyWQpb.png" width="596" height="276" referrerpolicy="no-referrer"></p>
<h3>2. 色彩中的“TF BOY”组合</h3>
<p>我想用一句苹果的官方话说：“配色可以提供交互性，提供视觉连贯性，并且对界面赋予生命力。”这句话总结的真的非常到位。</p>
<p>集中注意力认真听，重点来了！UI设计中颜色的使用法则，在一个页面设计中需要讲究 60-30-10法则， 在60％+30％+10％的比例下创造一种平衡感，是为了视角能够从一个焦点舒适的过渡到下一个点，避免给驾驶中的我们产生视觉落差很大的感觉。</p>
<p>一个项目车载系统的色彩规范，包括了品牌色、语义色、中性色。</p>
<p><strong>1）品牌色</strong></p>
<p>又称为“强调色”，通常一个车载系统只有一个品牌色，也是出现频率较高的一种颜色，强调色一般使用场景为：tab的切换选中，按钮开启状态、音乐在播放中的音符小动画等等（拿我练习稿讲解）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/858sndkfpB4YmItlyEOF.png" width="601" height="279" referrerpolicy="no-referrer"></p>
<p><strong>2）语义色</strong></p>
<p>语义色需要在UI界面中承载这具有准确的信息传达，在复杂的场景里颜色的倾向性应十分明显，减少用户的理解成本和理解时间，给出行体验者带来良好的驾驶体验。</p>
<p>根据交通标志的定义，红色表示禁止、停止、危险，那么用户需要在第一时间识别出这种信息，黄色为警示或不良结果等，绿色则代表通行、成功，上诉说的颜色为状态色。下面要讲一下功能色：链接色大家第一时间肯定想到的是蓝色。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Aw5LPc6SaPm6pIbUStRQ.png" width="601" height="338" referrerpolicy="no-referrer"></p>
<p><strong>3）中性色</strong></p>
<p>主要用于除文字外，还被运用到背景色、分割线、置灰填充、边框、等场景中（注：根据背景色的变化，系统其余颜色也随之而变，这是两套用色规范切换）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/SqXHOTKetPlTif2GYoiK.png" width="600" height="375" referrerpolicy="no-referrer"></p>
<h3>3. 如何制作HMI色彩规范？</h3>
<p>尽量使用较少的颜色，颜色饱和度不要过高，避免对驾驶的视觉干扰，吸引驾驶者的注意力，让老司机翻了车。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/TyPhVpKx4VDWlbt7BOcS.png" width="604" height="280" referrerpolicy="no-referrer"></p>
<p>避免让交互性元素和非交互性元素使用相同的配色（如果交互式和非交互式元素具有相同的颜色，则很难知道在何处点击）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/zWE9WbIrD3gH8CHSipwJ.png" width="598" height="372" referrerpolicy="no-referrer"></p>
<p>保持色彩一致性（请勿使用不同的颜色来任意，区分单个屏幕中的重复组件。当颜色不能增加价值时，请谨慎使用）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/akjhTOGkwcDQ5TsuzZZZ.png" width="598" height="489" referrerpolicy="no-referrer"></p>
<p>建立视觉层次（通过不透明度值或者是同一色系，但不要通过将过多的不透明度或对比度值应用于太多元素来过度使用它们）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/LHOnii97L2K7UFLPSAP3.png" width="601" height="307" referrerpolicy="no-referrer"></p>
<p>尽量使用深色背景，这是市面上很多车厂的选择（不过蔚来、特斯拉、小鹏、carplay都相继推出了白色版本，来适配白天，我们项目中后期也加入白天模式，经过了路测在阳光很刺眼情况下，黑色会反光，无法看清显示屏幕内容）最终在实际各种照明条件下，对应用配色方案进行测试。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IZFz1GmKuSJ0lB8fw8oI.png" width="605" height="277" referrerpolicy="no-referrer"></p>
<p>车载UI系统中使用足够色彩对比度，上诉在使用场景中有所提到。</p>
<p>继续讲干货：在后续文章安排里我会单独拿出WCAG从感知，可操作性，易于理解和稳定性去详细讲解，这次先挑重点说。</p>
<p>WCAG全称是Web Content Accessibility Guidlines（网页内容无障碍指南）它们是一组是网页内容更容易访问的建议，主要针对残疾人，一共分为三个级别 A（最低）、AA、AAA（最高）。</p>
<p>讲个概念：两个白色的对比度是 1:1 , 白色（#FFFFFF）与黑色（#000000）的对比度为 21:1。</p>
<p>做颜色对比的网站链接 <a href="https://next.rsuitejs.com/en/tools/palette">https://next.rsuitejs.com/en/tools/palette，</a>要满足 AAA 级准则，文本视觉呈现及文本图像至少要有 7:1 的对比度，针对大号文本以及大文本图像至少有 4.5:1 的对比度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/QBXuv2gfWrzl0TJB6YbX.png" width="602" height="339" referrerpolicy="no-referrer"></p>
<h3>总结：</h3>
<p>对于颜色运用的细节，是证明了一位设计师的深度、且具备耐久力。</p>
<p>上诉全部阐述对于颜色的规则不适用全部的设计方案，还是具体项目具体分析，用户人群不同，运用场景也不一致，比如驾驶者和后排人的屏幕设计内容肯定会有差别。</p>
<p>还有一个点在设计需要阅读内容页面，例如：微信发来的消息、设置中文本，最好能够达到AAA标准。</p>
<p> </p>
<p>作者：设计界的影帝</p>
<p>原文链接：<a style="font-size: 16px;" href="https://www.zcool.com.cn/article/ZMTIyNjAxMg==.html">https://www.zcool.com.cn/article/ZMTIyNjAxMg==.html</a></p>
<p>本文由@设计界的影帝 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4473641" data-author="1144194" data-avatar="http://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            