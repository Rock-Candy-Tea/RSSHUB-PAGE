
---
title: '详解｜Design Tokens 在设计系统中的意义与应用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cQRNdVYYztf8ZwMtOqy3.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 26 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cQRNdVYYztf8ZwMtOqy3.jpg'
---

<div>   
<blockquote><p>编辑导语：Design Tokens对于产品设计来说是个十分有用的工具和方法，本篇文章作者详细介绍了Design Tokens在设计系统中的意义与应用，讲述了其优势以及具体的使用方法，一起来学习一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5447505 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cQRNdVYYztf8ZwMtOqy3.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是 Design Tokens</h2>
<p>Design Tokens 并不是一个新概念，它是一种设计师和开发共同使用的工作思维和方法。Tokens 的本意是“令牌 /指令”，与 Design 连起来可以被理解为<strong>“设计变量”</strong>。</p>
<p>如下图，我们可以分别将 button 的背景色、文字色、文字属性定义成 Token，用代码化的语言，将组件的每一部分属性进行有规律的代码化命名。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hZtNWdctMvBAEcOQM5zs.jpeg" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="725" height="323" referrerpolicy="no-referrer"></p>
<p>大家应该都对设计系统有一定的了解（关于组件库和设计系统的相关概念可以阅读：B</p>
<p>端组件设计及工作经验系列文章），尽管我们可以通过设计规范、组件库、素材库等手段，对设计和开发的流程进行提效，但实际上却经常遇到令人头疼的细节问题，比如：</p>
<ul>
<li>开发所用的字号 / 颜色 / 间距等细节和设计稿不一样；</li>
<li>设计师根据新的业务需求设计了一张组件库中没有的卡片，但不确定卡片的背景和边框应该用哪个颜色；</li>
<li>产品新增了暗黑模式，设计和开发都面临巨大的工作量；</li>
<li>老板用了已上线的产品，觉得主题色的蓝色太重，想换主题色为浅蓝色。</li>
</ul>
<p>以上这些问题，其实都可以通过 Token 进行优化解决。Design Tokens 相当于将设计组件进一步拆解，使其<strong>原子化</strong>，将组件的<strong>每一种属性都转变为一个前端变量</strong>。</p>
<p>可以说，Token 本质上就是找到了<strong>组件、属性和代码之间的对应关系</strong>，统一了样式和前端语言，使组件和设计系统可以被快速管理。</p>
<h2 id="toc-2">二、Design Tokens 有哪些优势</h2>
<p>Design Tokens 在设计系统中相当于一种正确且唯一的设计决定，在使用时有四大优势：</p>
<ol>
<li>设计语义更易理解；</li>
<li>设计产出更加一致；</li>
<li>设计成果更准还原；</li>
<li>设计改进更易维护。</li>
</ol>
<h3>1. 设计语义 更易理解</h3>
<p>每一个组件中的复杂属性都可以被 Token 进行语义化的描述，帮助设计师和开发建立“画面感”。</p>
<p>举个例子：#495FDF 这个颜色，按照设计系统中的命名方式，它可能会被叫做 Blue 60。而当我们通过Token语义的方式让它达到组件级别的精度时，它会被叫做：color-button-border-focused。设计师和开发在使用时，就能迅速了解到这个颜色应用在哪里：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0Ddm2sjMcC5AiNDr8GEY.jpeg" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="722" height="341" referrerpolicy="no-referrer"></p>
<h3>2. 设计产出更加一致</h3>
<p>在实际设计过程中，一款产品通常会有不同的设计师参与产出设计稿。对于不熟悉设计规范的设计师，经常会有这样的困惑：“组件库的组件不全，我新设计的卡片，背景色应该使用设计系统中的哪一个红色？Red50 还是 Red60？”。</p>
<p>这时如果我们给卡片背景色定义一个 Token，不同设计师根据 Token来选择颜色，在卡片背景色上使用的颜色就一定是唯一的，这就能确保不同设计师产出设计稿的一致性。</p>
<h3>3. 设计成果更准还原</h3>
<p>当设计师在验收开发内容时，往往会花很多时间去检查开发结果与设计稿的一致性。使用 Token 就能确保设计稿被高效、准确地还原。</p>
<p>举个例子，在不使用 Token 的情况下，开发使用的是一个硬代码的模式，当输入不正确的色彩代码的时候，系统无从判断这个颜色是否使用正确，也就不会报错。</p>
<p>而在使用了 Token 之后，如果开发引用了错误的或根本不存的色值时，系统就会给出报错提示，开发由此得以自行检验，设计师的验收成本也会大幅降低：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/KtuZPBkfP6mULEf0de4s.jpeg" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="718" height="304" referrerpolicy="no-referrer"></p>
<h3>4. 设计改进更易维护</h3>
<p>设计的变更和迭代将变得更加轻松。举个例子，你的产品需要更新主题色，如果没有 Token，对于设计和开发来说将会是极大的工作量，需要一个个组件修改，还很容易漏掉或混淆一些细节。</p>
<p>但如果用 Token，开发只需重新输入每一个Token对应的新色值，就可以做到产品全局的颜色更换，不需要一个个组件的排查和更改，省时、高效、准确。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Zxj6pNVlLhkVtbZ838Sg.jpeg" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="713" height="367" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、如何使用 Design Tokens</h2>
<h3>1. Token 的命名方式</h3>
<p>关于 Token 的命名，不同的公司、团队、产品有不同的定义方式，但都遵循一定的<strong>逻辑和规则</strong>，且设计和前端要达成信息同步。这种命名的思路和给组件命名很相似，都需要先<strong>对组件的属性进行分类和整理</strong>。</p>
<p>我们可以从组件系统中的核心元素入手，将整个组件系统拆解出<strong>“形、色、字、构、质”</strong>这几个大的方面，并依照不同的<strong>类别、元件、属性、等级和状态</strong>，对 Token 进行命名上的规范定义：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/xunbZhYq8Y3s3zjwHXRI.png" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="706" height="341" referrerpolicy="no-referrer"></p>
<p>举个例子，下图中的 button，它的背景色 Token 使用上图中的命名方式，从左到右分别是它的类别、元件、属性、等级、状态，所以这个 button 的背景色所对应的 Token 就是：color-button-background-primary-nomal：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/4nKGivthhBGBuJ7pRVwr.png" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="712" height="429" referrerpolicy="no-referrer"></p>
<p>有了这样一个系统性的命名规则之后，我们就可以以表格的形式，将设计系统中所有涉及到 Token 的元素特征都整理出来，作为设计和开发拉通提效的基准：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/x78d2yruhVajfIZyCBa5.png" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="711" height="467" referrerpolicy="no-referrer"></p>
<h3>2. Token 的应用方式</h3>
<p>通常设计和开发是需要使用一套<strong>完整的 Token 列表</strong>来实现信息对齐。</p>
<p>如果你的团队在使用 Figma 作为设计协同工具，也可以<strong>使用插件：Figma Tokens</strong>。设计师将整理好的 Token 文档导入到这个插件中，而开发可以利用这个插件高效生成Token 对应的JSON 文件，直接复制用于编写代码，这样就可以很好的保证设计与开发协作的一致性和准确率：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜Design Tokens 在设计系统中的意义与应用" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/zdNeX1QPAHtw1zvJyurV.jpeg" alt="详解｜Design Tokens 在设计系统中的意义与应用" width="719" height="391" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：元尧；公众号：长弓小子；</p>
<p>本文由@ 元尧 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5444055" data-author="796023" data-avatar="https://static.woshipm.com/APP_U_202205_20220513165559_1122.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            