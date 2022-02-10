
---
title: '超全面！开关、复选框和单选组件在web表单应用分析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/qQXB4M4pImKz7fGCom4D.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 10 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/qQXB4M4pImKz7fGCom4D.jpg'
---

<div>   
<blockquote><p>编辑导语：如何针对具体场景选择合适的组件，是web表单设计中的常见问题。那么，你知道开关、单选、复选框等组件的适用场景该如何选择吗？本篇文章里，作者就该问题做了详细解答，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5311565 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/qQXB4M4pImKz7fGCom4D.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在web表单设计中，我们会经常遇到在开关、单选、复选框三个组件的选择使用上纠结，特别是只有两种状态下，比如开启/关闭、启用/关闭、显示/隐藏、同意/不同意、默认/自定义……</p>
<p>我们发现使用Switch开关、Radio单选和Checkbox复选这三个组件好像也都是可以的，这时应该选择哪个组件更合适呢？</p>
<p>本文主要探讨这三个组件的基本特点，以‍及在web表单设计中，这三个组件使用上有什么区别，以及常见的场景如何去选择。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/704iBiBUpQZhEzc5Ve0s.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="683" height="210" referrerpolicy="no-referrer"></p>
<h3>文章概览</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/1GJirEPfYKhOyLI2xfZX.jpeg" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="684" height="242" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、Switch 开关•它就像是灭霸的响指</h2>
<h3>1. 简要了解开关</h3>
<p>开关作为仿照物理开关的映射，提供了两种最为简单、直接的对立选项，比如开/关、启动/禁用等。它就像生活中控制灯泡的开关，点击灯泡立即亮起。所以它的<strong>意符也必须明确，不然用户都不知道，即将要启动/关闭什么</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/eCuXMdCZ1LSBt5tUMtdV.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="684" height="169" referrerpolicy="no-referrer"></p>
<h3>2.开关组件的特点</h3>
<ol>
<li><strong>对象标签名称须传达清晰</strong>，能够让用户能够明确感知操作后的动作开启或关闭什么；</li>
<li>主体标签信息和按钮是分离的，<strong>两个视觉焦点</strong>；</li>
<li>一般点击后会立即反馈；</li>
<li>没有hovering效果，有动作效果，<strong>更适合手指操作</strong>；</li>
<li>非W3C组织官方html标记，极端情况不支持 Javascript。</li>
</ol>
<h3>3. 苹果公司对开关组件的设计规范</h3>
<p>苹果的「Human Interface Guidelines」有着这么一份对于开关组件的使用规范定义，我们不妨可以借鉴。</p>
<p><strong>1) 避免使用开关控制局部细节或者次要的设置</strong>。开关的视觉权重比较高，所以用它控制内容较多更为合适，比如可以将它作为总开关打开或关闭一组设置。</p>
<p><strong>2) 通常不要用开关替代复选框</strong>。如果我们的规范中定义了复选框，则尽可能保持一致的使用规范。</p>
<h3>4. 开关使用场景举例</h3>
<p>通过上述对开关组件特点，结合苹果组件的规范，我们基本可以梳理出以下几条主要主要使用场景：</p>
<p><strong>1）开关的标签意符需传达清晰</strong></p>
<p>和单选、复选框不一样的是，因为开关主体的信息和按钮是分离的。用户在点击开关按钮前，<strong>必须清晰告知用户点击后会发生什么</strong>，甚至有时我们需要通过增加副标题来加以说明。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/keocefPFZ7EYAM5iTaIC.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="673" height="268" referrerpolicy="no-referrer"></p>
<p><strong>2）一般只为立即生效的场景使用开关按钮</strong></p>
<p>在表单填写时，往往最终会有「提交」按钮作为结束态，开关作为表单字段的填写，用户点击后并不能够立即生效，而是需要再次点击「提交」按钮。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/YqKlUXD2NJxvpR06L4cu.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="688" height="216" referrerpolicy="no-referrer"></p>
<p><strong>3）有风险，需着重提醒用户</strong></p>
<p>开关的视觉权重较高，在复杂的表单信息中，<strong>它能够很快吸引到用户的注意力</strong>，并能够给用户以视觉提醒。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Cmor1atHWXyePpRUdB5d.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="680" height="310" referrerpolicy="no-referrer"></p>
<p><strong>4）避免大面积使用开关，使用它控制局部细节或者次要设置</strong></p>
<p>开关在视觉感知上它和按钮上有些接近，所以尽可能避免在表单中大量使用开关来控制局部层级内容，这时推荐使用复选框来替代开关作为局部。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/DcXANLz1q22G5DFWCf83.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="688" height="300" referrerpolicy="no-referrer"></p>
<p><strong>5）把它作为高层级内容控制或信息设置</strong></p>
<p>把它用来作为总控制来显示更高层级内容，<strong>避免web表单中大面积的使用开关按钮</strong>，会和其他的基本组件造成视觉干扰。这样可以<strong>既凸显其重要性，又能提升用户浏览表单的效率</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/gbuWv1DvVtlTqoNh4sAD.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="685" height="337" referrerpolicy="no-referrer"></p>
<h3>5. 小结</h3>
<p>开关按钮就像是灭霸的戒指，<strong>视觉突出且反应快</strong>。用户浏览表单、填写内容组之间，<strong>一般不需要很强的视觉差异</strong>。如果填写的表单信息之间对比差异过大，<strong>开关往往给用户造成过大的视觉干扰，反而阻碍用户浏览表单的效率</strong>。</p>
<h2 id="toc-2">二、Checkbox 复选框• 它是一个机器小能手</h2>
<h3>1. 简要了解复选框</h3>
<p>让用户在两个布尔值之间进行选择，勾选后和未勾选表示“是/否、要/不要、开启/关闭…” 等问题。以下内容主要讨论单个复选框的使用情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bxkbx9gVfbwUxbzaI9hK.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="691" height="167" referrerpolicy="no-referrer"></p>
<h3>2.复选框的特点</h3>
<p>1）为了便于用户快速理解，一般复选框的标签内容是一句话，不会用逗号去作隔开。</p>
<p>2）作为单选状态时，操作对象和标签主体内容视觉焦点是不分开的，选择后就知道它被选中了。</p>
<p>3）可直接表示标签内容的开启、关闭。</p>
<h3>3. 场景举例分析</h3>
<p><strong>1) 用户基本清楚会发生什么，使用复选框</strong></p>
<p>如果使用开关或者单选框，我们会发现视觉干扰特别严重，一般表单内容不需要特别去强调每一个字段的开启状态。当然如果排版限制，我们也是可以将复选框放到标签的右侧（放右侧复选框需对齐）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/vyfEwjcXEK2ZR6JswiTO.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="683" height="251" referrerpolicy="no-referrer"></p>
<p><strong>2）表单中的复选框生效，需要配合提交按钮</strong></p>
<p>一般情况下，表单填写中，复选框不会像开关点击后立即生效，它需要配合提交按钮生效。所以用户在提交前可查看他们填写的表单，更有助于在信息防错。</p>
<p>（Ps. 在设置页，复选框可单独作为设置且立即生效。）复选框的主体标签信息和复选按钮在一起，特别是对于<strong>批量填写或设置一批字段，使用复选框效率更高</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/NFrBhFe3YX4RXMSc09AV.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="680" height="284" referrerpolicy="no-referrer"></p>
<p><strong>3）用复选框来控制表单局部细节</strong></p>
<p>如上述，如果控制对象的功能是表单的一个局部，或信息内容不是很多，用户也清楚知道选择后会是什么，这时候复选框更适合。</p>
<p>这时我们<strong>不需要过重地给用户强调什么，用复选框会比使用开关让整个表单的结构内容更清晰</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ggYfdXRmsKJjUagZ0c53.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="685" height="312" referrerpolicy="no-referrer"></p>
<h3>4. 小结</h3>
<p>复选框就像是一个机器小能手，它的应用拓展性比开关更强，它<strong>既可以作为层级内容使用，又可以作为设置项，点击后并立即生效</strong>。</p>
<p>在表单中，<strong>作为局部、或者细节内容控制，使用复选框更合适</strong>。它也不会像单选按钮阅读有信息阻断的问题，<strong>不会像开关有强视觉干扰，它会让我们的视觉焦点更集中表单信息上</strong>。</p>
<h2 id="toc-3">三、Radio 单选按钮• 白天不懂夜的黑</h2>
<h3>1. 简要了解单选按钮</h3>
<p>单选按钮最早的设计模型，来源于收音机切换频道的按键，当我们按下其中一个，其他的按钮就会被弹出，按下的那个按钮就成为了选中的状态。单选按钮可谓是泾渭分明，有你不能有我。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/woX2l9turqEvOtTrxWLl.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="690" height="145" referrerpolicy="no-referrer"></p>
<h3>2. 单选按钮的特点</h3>
<p>单选按钮的优点是，<strong>将所有信息条件暴露给到用户，它不像开关在使用上带有去猜测、探索的必要</strong>。</p>
<p>1）每个选择都非常直观，如果希望用户阅读完所有选项，用它再好不过了。</p>
<p>2）拓展性更强，相较于开关、复选框的布尔值，单选能承载两个或两个以上选择。</p>
<p>3）必须提供默认值，且默认值可以承载内容。</p>
<h3>3. 场景举例分析</h3>
<p><strong>1）需要让用户明确知道两者的区别，甚至需要强调两个选项的不同</strong></p>
<p>如果采用复选框，用户需要在两个差距较大的选项中去作思考。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7tTXmwwWH9pMe3JnJQ0I.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="684" height="204" referrerpolicy="no-referrer"></p>
<p><strong>2）开启/关闭的单选状态，使用复选框</strong></p>
<p>复选框对于绝大多数用户都是非常清楚，使用复选框在空间、视觉焦点更是更集中的，所以如果只针对开启/关闭的状态，推荐使用复选框</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/CzRXA6eMphIqccGcp8eG.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="698" height="260" referrerpolicy="no-referrer"></p>
<p><strong>3）每个选项都关联内容时，使用单选按钮</strong></p>
<p>我们知道，<strong>如果默认选项设计的好，会让很多人保持选择默认选项</strong>。</p>
<p>下图这个案例，如果采用复选框或者开关，用户就不得不去探索思考开启后是什么，还要担心理解开启/关闭后带来的影响，而对于绝大多数用户来说，这边的报名设置系统默认内容无需改动。需注意给用户提供的默认选择，一定要是安全、方便的选项。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/G8N8KqEkx3i7SAoYlwxd.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="681" height="157" referrerpolicy="no-referrer"></p>
<p><strong>4）较长需隐藏拆分的内容情况，使用单选按钮</strong></p>
<p>在表单设计中，如果遇到的内容需要重新组织或者拆分时，选择使用单选按钮。这样不仅能够做到表单信息简洁，也能够提高用户的浏览效率。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/L9BK4OiaouVBHv2PhIoN.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="686" height="263" referrerpolicy="no-referrer"></p>
<p><strong>5）垂直排列单选，信息阅读更佳</strong></p>
<p>如果字段名称较长，需要添加副标题加以说明，这时单选按钮承载的信息较多，使用垂直排列让用户有一致的起始阅读线，眼球转动幅度最小，信息获取体验更佳。如果标签文字较少，也可以横排不至于占用太多的垂直空间。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="超全面！开关、复选框和单选组件在web表单应用分析" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MgL9Eyulalimow51C1hF.png" alt="超全面！开关、复选框和单选组件在web表单应用分析" width="688" height="298" referrerpolicy="no-referrer"></p>
<h3>4. 小结</h3>
<p>单选按钮就是白天和黑夜，互不干扰的条件，<strong>希望用户阅读完这两个选项，使用单选按钮再好不过了，考虑到单选按钮提供的默认选项，提供的要是绝大多数用户需要的，且是安全方便的</strong>，如果单选按钮标签文字过多，在排版时垂直排列拓展性更强，阅读体验更佳。</p>
<h2 id="toc-4">四、全文总结</h2>
<p>1）开关更像是一个灭霸的戒指闪闪发光，不过在表单结构、各种控件内容较多，<strong>需要页面清晰、避免过多的视觉突出</strong>，所以尽量避免让无数个戒指闪亮中表单中。</p>
<p>2）复选框它更像是一个机器小能手，<strong>适用和拓展性极强</strong>，即可以单独作为设置，不用配合其他提交按钮，也可以作为表单填写的一部分。当我们犹豫使用哪个组件时，选择它一般不会错。</p>
<p>3）单选按钮就像是白天和黑夜，完全不见彼此。单选条件承载的信息也较多，如果希望<strong>用户对比感知到两者信息的不同，那么使用单选按钮</strong>。</p>
<p>4）最后理论永远只是指导实践的一部分，上述内容可能只是在用户认知和易用性之间，找到一个相对平衡的点，具体的使用场景情况，还是要具体问题具体分析。</p>
<p>参考文献</p>
<p>Nielsen Norman Group</p>
<p>Human Interface Guidelines</p>
<p>http://www.woshipm.com/pd/374314.html</p>
<p>http://www.woshipm.com/ucd/1267601.html</p>
<p> </p>
<p>本文由 @小高杂谈 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5310316" data-author="827583" data-avatar="http://image.woshipm.com/wp-files/2020/07/on9910t6Rr5DBSwsMwQk.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            