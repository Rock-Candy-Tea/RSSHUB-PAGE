
---
title: 'Design Token 应用指南——设计篇'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/LT6zX6ZenZlfayiH7kvp.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 11 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/LT6zX6ZenZlfayiH7kvp.jpg'
---

<div>   
<blockquote><p>编辑导语：在产品设计流程中，从设计到研发落地，期间需要让研发团队与前线团队理解产品的设计规范，而合适的方式方法不仅有助于减少沟通成本，同时也有利于后期的产品迭代升级。本篇文章里，作者介绍了design token这一方法，让我们一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4539129 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/LT6zX6ZenZlfayiH7kvp.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在线设计、研发协作工具和组件概念的普世化，让设计、研发效率大大提升；在数字产品发展到今天，数字产品对迭代速度、个性化品质要求也越来越强。设计师应该如何应对，做到更快速、高效地从设计到研发的落地？本文将通过介绍 Design Token 的基本知识及 Design Token 在设计中通过应用为大家提供新的问题解决思路。</p>
<h2 id="toc-1">一、关于设计的一致性</h2>
<p>设计师对于原子设计理论（Atomic Design Methodology）肯定不陌生，从原子（Atoms）、分子（Molecules）、组织（Organisms）、模板（Templates）、页面（Pages）包括标准流程（Patterns）到更完善的设计体系（Design Systems），一切的一切都是为了产品设计、研发效率和一致性提供帮助。同时，它们也是传达设计原则、构成产品独特气质的基石。</p>
<p>为了让上述的“设计基石”更统一，设计师一定会有一套设计规则（设计规范），但令人遗憾的是对于这些关键规则最熟悉的人，也大多是规则的制定者，其他设计师对该规则的细节则不甚清晰，在生产过程中大多是通过组件的复制、样式的复制完成产品的设计。</p>
<p>而开发者对规范的理解成本则更高，这在开发落地过程中则基本上依赖设计师和工程师的线下沟通，存在较高的沟通和走查的时间成本。</p>
<h2 id="toc-2">二、什么是 Design Token?</h2>
<p>“Token”原本的意思是“令牌”，在工程逻辑中用于用户身份与服务器端进行验证，而在设计体系中，Design Token 则可以简单理解为封装的视觉样式参数。</p>
<p>它是通过规定样式参数，并通过一套符合设计师、工程师理解的统一的命名规则，为这些样式参数的定义名称。</p>
<p>例如在真实的产品设计、研发过程中，这个环节大多是断掉的，通常看到的样式代码几乎都没有辨识性的参数。当时间一久、产品复杂起来，想要全局迭代维护将是意见非常痛苦的事情，但如果我们将这些样式参数规范和封装起来，用语义化的方式进行描述和管理，开发过程就会清晰得多：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/VqVsibkcz6X4phX6WuQK.png" alt="Design Token 应用指南——设计篇" width="804" height="236" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">lightningdesignsystem-design tokens</p>
<p>设计也是同理：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/6jFaN5oDHo7WUBGp2j4M.png" alt="Design Token 应用指南——设计篇" width="788" height="425" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">lightningdesignsystem-UI Kit</p>
<p>通过 Design Token 可以更有效地保障设计、开发落地的一致性和可拓展性。接下来我将以 Sketch 为主要输出工具的案例，给大家详细讲解以下内容：</p>
<ol>
<li>什么样的产品需要用到 Design Token？</li>
<li>如何更高效地在设计文件中管理样式参数？</li>
<li>如何向研发输出 Design Token？</li>
</ol>
<h2 id="toc-3">三、什么样的产品需要用到 Design Token?</h2>
<p>界面需要支持暗黑模式、用户自定义、高频运营皮肤需求的长生命周期产品。</p>
<h3>1. 如何更高效地在设计文件中管理样式参数？</h3>
<p><strong>1）提炼元素</strong></p>
<p>提炼核心影响视觉风格的元素：形、色、字、构、质，落实到绘图工具中（以 Sketch 最新版本为例），可通过样式库管理样式类型有：形（倒角）、色（色彩）、字（文字）、质（投影），间距则需要设计师通过记忆制定好的间距阶直接应用到设计中即可。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/dv9CokMVtaZyTsq14kAg.png" alt="Design Token 应用指南——设计篇" width="777" height="146" referrerpolicy="no-referrer"></p>
<p><strong>2）样式管理</strong></p>
<p>由于设计师对于样式管理个人习惯和产品体量的差异，大致可以分为以下两种管理方式。</p>
<p><strong>① 以组件维度管理</strong></p>
<p>即以基础组件为中心，分散式管理应用在组件中的样式。以色彩为例，下图中应用按钮中的灰色线框样式被归类到“按钮”下。同时，该样式也同样应用到输入框中，因此，该样式还需要被归类到“输入框”下。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/1zas8BpvvF5SEzZNq1pZ.png" alt="Design Token 应用指南——设计篇" width="783" height="92" referrerpolicy="no-referrer"></p>
<p>这种管理方式在设计师在调用过程中看似应用目标更清晰，但当业务不断发展出现了复合型组件时，组件之间发生了嵌套，且复合组件中也需要用到相同的线框样式时，这个相同的线框样式还可能出现在更多的复合组件中。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/go6nLsArEcwLRofaV8TP.png" alt="Design Token 应用指南——设计篇" width="787" height="234" referrerpolicy="no-referrer"></p>
<p>当需要对样式进行全局调整时，则需要考验设计师是否还能记得这个相同的线框样式应用在哪些组件里。无疑，这种方式对于样式的维护和管理是个大的挑战。因此可以采用更为集成化的抽象维度管理。</p>
<p><strong>② 以抽象维度管理</strong></p>
<p>即样式不与组件绑定，仅以样式本身的性质进行分类。还是以上述的线框样式为例，在分类上则以该样式的性质进行归类，如：线框/灰色。在样式应用时，这三个组件则可直接引用统一样式，将原本的三个相同样式进行了集成化管理。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/8mnAk8a2XILkf6lYmOPB.png" alt="Design Token 应用指南——设计篇" width="795" height="270" referrerpolicy="no-referrer"></p>
<p><strong>3）定义框架</strong></p>
<p>基于抽象维度管理方法，在设计文件中我们可以通过结合 Symbol 及样式库对：形（倒角）、色（色彩）、字（文字）、质（投影）分别进行集中管理：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/sWYdbhvru4YP1i2VmaQl.png" alt="Design Token 应用指南——设计篇" width="797" height="190" referrerpolicy="no-referrer"></p>
<p>图中的示例中可以看到，样式的分类可以通过“性质+具体样式”的框架进行管理。</p>
<p><strong>4）定义命名规则</strong></p>
<p>基于上述框架，还可在“性质”中增加“应用范围”层级，可以更好地管理样式的应用范围。</p>
<p>如：常见的自定义主题涉及到需要支持变更的品牌色；产品中相对需要固定的功能色（错误、成功、告警等）。这样的分类框架，可以帮助设计师进行样式集成管理的同时，也能对应用场景有清晰规划。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/jcNTScFPCZia1LDV1rVT.png" alt="Design Token 应用指南——设计篇" width="797" height="222" referrerpolicy="no-referrer"></p>
<p>在“具体样式”层级中，也可针对具体管理对象灵活调整，例如：在文字样式管理中可添加文字对齐方向；在投影样式管理中减少“应用范围”。</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/YHW5anEdthTnL4lFO6kA.png" alt="Design Token 应用指南——设计篇" width="799" height="327" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、如何向研发输出 Design Token？</h2>
<p>通过完成上述管理样式参数的方法，就可以在 Sketch 中的样式库中呈现一套完整的样式表。</p>
<p>图层样式：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/O5r132C4Awtg8zc3Hhff.png" alt="Design Token 应用指南——设计篇" width="799" height="307" referrerpolicy="no-referrer"></p>
<p>文字：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/JxpL9DnlHLrN5biACMzr.png" alt="Design Token 应用指南——设计篇" width="798" height="204" referrerpolicy="no-referrer"></p>
<p>为了将这些样式提取到研发同学方便查看的环境，设计同学需将样式库中的样式转录至 Excel 表中：</p>
<p><img data-action="zoom" class=" aligncenter" title="Design Token 应用指南——设计篇" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/ifqO8DEcewmuhnqYBfHB.png" alt="Design Token 应用指南——设计篇" width="797" height="158" referrerpolicy="no-referrer"></p>
<p>具体研发命名与分类方式可基于该表格与研发同学共同拟定、优化形成最终的设计、研发 Design Token 对照表。</p>
<p>在日常产品设计过程中，设计同学在对样式进行调整后并定稿后，需及时将修改点同步到对照表中，并及时通知研发同学及时修改研发侧 Design Token，确保设计、研发的一致性。</p>
<p> </p>
<p>作者：腾讯CDC；公众号：腾讯CDC体验设计</p>
<p>原文链接：https://mp.weixin.qq.com/s/eg_hP8o3oEAAVwAxmqhvGw</p>
<p>本文由@腾讯CDC体验设计 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4539006" data-author="178575" data-avatar="http://image.woshipm.com/wp-files/2016/12/7kjhx1gt26OgIdXxqEHg.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182616_8026.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            