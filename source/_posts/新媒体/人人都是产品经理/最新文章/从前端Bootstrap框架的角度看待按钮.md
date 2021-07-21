
---
title: '从前端Bootstrap框架的角度看待按钮'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Rmc0juLCufur7kAMb2JT.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 21 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Rmc0juLCufur7kAMb2JT.jpg'
---

<div>   
<blockquote><p>编辑导语：作为一名设计师，是否只要做好设计就可以了？但其实设计师的想法实现是依赖于代码的，因此是先有前端后有UI的，作者分享了一些从Bootstrap框架的角度去理解按钮在代码中的相关知识，我们一起来看下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4909541 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Rmc0juLCufur7kAMb2JT.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>设计师的想法实现依赖于代码，这也是为什么先有前端，而后有UI。很多时候，为了提高效率，开发在写前端页面时会采用现成的框架。</p>
<p>作为设计师在了解一定的代码基础后，设计稿会更加有依据，和开发交流也变得容易。下面我们就从Bootstrap框架的角度去理解按钮在代码中的相关知识，这里每一个点都已被验证可实现，可以作为细节纳入设计思考中。</p>
<h2 id="toc-1">一、基本案例 Base Example</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/fc4cNbYSXVChalq6xJDo.png" alt width="580" height="213" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Dcqhz5Ik2uxoJBqbRD9F.png" alt width="580" height="280" referrerpolicy="no-referrer"></p>
<ul>
<li>主按钮：通常用有颜色的背景形状加文字，它也被叫做号召按钮Call to Action，需要引起用户的注意，鼓励用户采取某种行为。</li>
<li>次按钮：默认采用灰底黑字的样式，与主按钮搭配使用，减少视觉上的干扰</li>
<li>提示按钮：红绿黄分别代表代表危险，成功，警示。这样的颜色搭配也和生活中人们的普遍认知相符合，例如红绿灯。</li>
<li>文本按钮：通常自带按钮语意，或带有颜色或下划线，用于辅助交互，不会分散主按钮元素的注意力。</li>
</ul>
<h2 id="toc-2">二、边框按钮 Outline Buttons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZD2p3akNu6epmHtdVCP3.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/4WkWjgDKdsGXksky0jX1.jpeg" alt referrerpolicy="no-referrer"></p>
<p>也被称作幽灵按钮Ghost Button，它看起来是空心的，由一个可识别形状的线框和文字构成，通常与主按钮搭配，用于次要操作，这种按钮有助于设置视觉层次结构。</p>
<h2 id="toc-3">三、浅色背景按钮Light Buttons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BoNSUt69bUCrR8vOariT.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7DGF0StshWnO9kwBlSVg.jpeg" alt referrerpolicy="no-referrer"></p>
<ul>
<li>Light Buttons：在需要用多颜色来表示多功能的系统中，浅色背景按钮在视觉上不会影响主按钮，并可以很好地帮助区分功能。</li>
<li>Light Hover Buttons：向用户提供对悬浮按钮的反馈是一种很好的交互（其他按钮也一样），用户知道他们的动作已被系统接受，对下一步操作充满期待，更有信心。</li>
</ul>
<h2 id="toc-4">四、带图标按钮 Buttons with Icons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qm3RjemN1CjVL1lRt024.jpeg" alt referrerpolicy="no-referrer"></p>
<p>在按钮中加入图标会让单调的按钮更加生动，整个页面页会变得活泼。</p>
<ul>
<li>图标左文字右：用户先看到图标后看到文字，在熟悉某个界面后，这种布局让用户在寻找某个操作时更加容易。</li>
<li>文字左图标右：图标起到对文字进一步解释的作用。</li>
</ul>
<h2 id="toc-5">五、链接按钮 Link Buttons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/NdA7aehn7W6NcD5XOv0d.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pc24UmHJCIHUZgGxetRk.jpeg" alt width="990" height="109" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、社交按钮 Social Buttons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mQUmnP9us4cACrypUq05.jpeg" alt referrerpolicy="no-referrer"></p>
<ul>
<li>这些按钮简化了将网站内容连接到用户的社交媒体的过程。为了易于识别，通常会用各自的品牌标识。</li>
</ul>
<h2 id="toc-7">七、状态 States</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/s7cGbscB3sFrvEFhK2kJ.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/zX6bSefkOgnTkhzLwDyO.jpeg" alt width="1001" height="130" referrerpolicy="no-referrer"></p>
<p>常见的按钮状态有6种：Normal, Hover, Active, Focus, Visited ，Disabled。</p>
<ul>
<li>Normal正常：光标没有悬停在按钮上时的样式，按钮所链接的页面之前没有被点击过。</li>
<li>Hover鼠标悬停：光标悬停在按钮上时，按钮给出变化提示用户可点击。</li>
<li>Active激活：按钮被点击后系统在处理一些进程，例如提交中，等待中等。</li>
<li>Focus聚焦：按下按钮后由正常或悬停状态发生的微妙变化，不易察觉。</li>
<li>Visited已访问：用户在之前已访问过该页面。</li>
<li>Disabled禁用：由于各种原因用户不可点击该按钮，通常按钮置灰或光标移置按钮时给出不可点击状态提示。</li>
</ul>
<h2 id="toc-8">八、按钮字体样式 Button Font Styles</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7DTUCOz9MGYysxH5ip7x.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cTbsPo5qF3V1ENQvwpBA.jpeg" alt referrerpolicy="no-referrer"></p>
<ul>
<li>字重：合理设置字重能将内容进行区分，突出重点，在版面中，对比越强烈，信息层级区分越明显，在字重的选择上，可以大胆的进行跨等级选择，例如常规体直接与中粗体进行对比。Contrast is king对比为王！</li>
<li>大写字母：给人重要，有力量，可信赖的观感，他们看上去较大，需要花费时间力气去阅读。通常用于导航，标题，标签等需要引起用户注意的地方。</li>
<li>小写字母：给人非正式，友善亲和的观感，通常用于句子类内容较多的地方。</li>
</ul>
<p>合理利用大小写的组合可以让文本更加易读，减轻用户的视觉负担。</p>
<h2 id="toc-9">九、按钮文本颜色 Button Text</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TBtKP68DqcOEx8vS0SJf.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/U2J2AiA71ZpbpARXjju5.jpeg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-10">十、按钮样式 Button Styles</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/J6Cq0sCrogWntmq0kT6J.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KsjchKCtOmrWTJglt4cw.jpeg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-11">十一、尺寸 Size</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/vCwhYo8lzOcWbCUI6cHd.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/um4QdQUvGpSklfscGs2b.jpeg" alt referrerpolicy="no-referrer"></p>
<ul>
<li>尺寸是让用户了解元素重要性和构建组件层次结构的重要因素。主按钮通常要足够大，容易找到，但不能太大，影响整体布局。次按钮等其他类型按钮不能过小，保证易用性，这点在移动端的规范更为严格。</li>
<li>系统中同类按钮尺寸要保持一致性。</li>
</ul>
<h2 id="toc-12">十二、按钮阴影 Buttons with Shadow</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/IhZfQm418pvQaRvR2bmg.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AhJMXX0mxjV3hDwBWGWD.gif" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Iru5nPBma5iHJU7VZK5B.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/eQaYRnmFJode0lOtX03b.gif" alt referrerpolicy="no-referrer"></p>
<p>在设置按钮阴影的颜色时，吸取按钮本身的颜色然后调整其透明度会比黑色阴影有更佳的视觉感受。</p>
<h2 id="toc-13">十三、悬浮按钮可选颜色 Hover Button Option</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6H4OQJxYE0IoEv7Y5idi.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rPG9SCk7yUjRgiyao8QM.gif" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-14">十四、透明按钮 Transparent Buttons</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QCr0bcInxFFrLhxJbWkv.jpeg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/vlx4pDCJFvBaCZocf1O7.gif" alt referrerpolicy="no-referrer"></p>
<p>适用于深色背景，按钮的背景吸取文字的颜色并降低其透明度。</p>
<hr>
<p>除了按钮，还有很多其他组件的代码相关知识可以去了解，例如弹窗，面包屑，导航，下拉，输入框等。在对这些组件有了一定了解后，在特定的业务场景下，设计师便知道哪些需要出图，哪些可以用框架自带的组件，以及如何用现有组件与对提高效率有很大帮助。</p>
<p>附：更多Bootstrap的相关信息请访问官方文档：https://getbootstrap.com/docs/4.3/components/</p>
<p> </p>
<p>本文由 @B端交互设计师 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4882463" data-author="1056101" data-avatar="http://image.woshipm.com/wp-files/2021/07/Yrd73KD3d3mi8wnKZtXe.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            