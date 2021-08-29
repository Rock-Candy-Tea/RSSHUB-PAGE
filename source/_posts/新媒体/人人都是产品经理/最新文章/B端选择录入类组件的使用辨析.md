
---
title: 'B端选择录入类组件的使用辨析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vD6DbxGlwbh5onDyZL3w.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 29 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vD6DbxGlwbh5onDyZL3w.jpg'
---

<div>   
<blockquote><p>编辑导读：在很多设计中，选择录入类组件的理解和使用都比较模棱两可，很多其他产品在实际应用中往往也不够规范，使产品体验的一致性受到影响。本文将具体探究下这几种组件的特性和适用场景，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5114799 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vD6DbxGlwbh5onDyZL3w.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="B端选择录入类组件的使用辨析-一、前言">一、前言</h2>
<p>不久前在进行一个Web端HRM系统的需求设计，场景是对于从企业离职的员工，HR可以根据员工能力和表现选择是否将其设置为优秀离职人才，对于优秀离职人才将进行定期关怀，以便后续重新返聘的可能。在设计过程中，对于设置优秀离职人才这个交互，感觉使用单选框、多选框、开关都能达到目的，究竟哪一种组件才是最合理的选择呢？</p>
<p>​这个问题让我回想起之前在很多设计中对于这几种选择录入类组件的理解和使用都比较模棱两可，很多其他产品在实际应用中往往也不够规范，使产品体验的一致性受到影响。本文将具体探究下这几种组件的特性和适用场景：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/mKjOpFDL7YPpDQYq5T9X.png" alt width="1920" height="720" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<h2 id="B端选择录入类组件的使用辨析-二、单选框（Radio）和多选框（Checkbox）">二、单选框（Radio）和多选框（Checkbox）</h2>
<h3 id="B端选择录入类组件的使用辨析-1.来源">1. 来源</h3>
<p id="B端选择录入类组件的使用辨析-单选框"><strong>1）单选框</strong></p>
<p>单选框一般被认为来源于收音机(Radio)上的物理按钮，当一个按钮被按下时，另一个按钮将会被弹起，使得永远只有一个按钮处于被按下的状态。</p>
<p>这种说法可能也不够严谨，因为收音机上的按钮在被按下后，不仅呈现出了“按下”的状态，同时也会立马触发收音机的广播，即立即生效。实际上绝大多数UI界面中无论单选框还是多选框一般都是仅作为录入，触发生效往往需要配合“提交”操作来进行。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YvZdXEGrFlIxpdKEnn4S.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p id="B端选择录入类组件的使用辨析-多选框"><strong>2）多选框</strong></p>
<p>多选框来源于生活中常见的各种多项选择场景，如饭店菜单、考试多选题等。多选框一般也是作为内容录入的组件，一般在进行选择后同样需要配合后续的“提交”动作，就像选择菜品后下单，选择答案后交卷，这种“选择类”场景多用在表单或者表格中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/bvh6HW87VePsgUAfwQyb.png" alt width="1920" height="850" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p>多选框还有另一种“设置类”场景，这种场景下多选框用于启用某种模式、应用某项设置，与开关（Switch）非常类似，这也使得多选框在实际产品中的应用要比单选框复杂得多，后文将详细阐述多选框与开关的使用区别。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/GjpDcuKjL13KabrbfjNj.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<h3 id="B端选择录入类组件的使用辨析-2.简单定义及外观样式">2. 简单定义及外观样式</h3>
<p id="B端选择录入类组件的使用辨析-单选框.1"><strong>1）单选框</strong></p>
<p>可以概括为从最少两个或两个以上的互斥关系选项之中选择一项的组件，外观样式通常由“圆形外框+文字标签”组成，选中时圆形外框样式发生改变表明选中状态。</p>
<p id="B端选择录入类组件的使用辨析-多选框.1"><strong>2）多选框</strong></p>
<p>可以概括为从多个并列关系的选项中选择多个的组件，多选框最少可以一个都不选。外观样式通常由“圆形或方形外框+文字标签”组成，选中时一般在外框中出现√表明选中状态。与单选框相比多选框还有一种特殊的“半选中状态”（half-selected）,一般出现在表格（Table）或者树选择（Tree select）中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/HmGygMvGDelztBlV2e2w.png" alt width="1920" height="760" referrerpolicy="no-referrer"></p>
<h3 id="B端选择录入类组件的使用辨析-3.交互细节">3. 交互细节</h3>
<p id="B端选择录入类组件的使用辨析-触发区域"><strong>1）触发区域</strong></p>
<p>单选框和多选框本身外框尺寸都比较小，因此需要将触发区域增大至整个标签范围，方便用户点击</p>
<p id="B端选择录入类组件的使用辨析-排版"><strong>2）排版</strong></p>
<p>单选框和多选框在B端各类表单中应用较多，在页面空间允许的范围内，最好将选项纵向对齐排列，方便用户直观比较，需要横向排布时，选项间应该设置清晰明显的间隔。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/rnmu4bBSfy7fO7cF6lL0.png" alt width="1920" height="560" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p id="B端选择录入类组件的使用辨析-单选框的容错机制"><strong>3）单选框的容错机制</strong></p>
<p>单选框在选择过后一定要有一个选中项，因此就不能恢复至“空状态”。在比较典型的社交场景中，一些涉及隐私的信息比如婚姻状态选择，可以给用户提供诸如“保密”“不展示”之类的选项，防止用户在选择之后无法回退。</p>
<h3 id="B端选择录入类组件的使用辨析-4.单选框、多选框和下拉选择（Select）的使用辨析">4. 单选框、多选框和下拉选择（Select）的使用辨析</h3>
<p>对比单选框、多选框和下拉选择的外观样式不难发现，它们之间最重要的区别在于信息传达效率和包容度的不同。</p>
<p id="B端选择录入类组件的使用辨析-单选框和多选框的特点"><strong>1）单选框和多选框的特点</strong></p>
<p>单选框和多选框的所有选项信息都是直接暴露出来，如果选项过多将占用较多界面空间并且影响用户的阅读效率和界面整体规整度，信息包容度低但信息传达直观高效；</p>
<p id="B端选择录入类组件的使用辨析-下拉选择的特点"><strong>2）下拉选择的特点</strong></p>
<p>下拉选择则是收在下拉菜单里，只有选择值是用户一眼能看到的，信息包容度高，节省空间，与其他输入类组件并用时能保持整体界面的规整度，但每次都得点开再进行选择也牺牲了一定的信息传达效率和操作便利性。</p>
<p id="B端选择录入类组件的使用辨析-适用单选框和多选框的场景"><strong>3）适用单选框和多选框的场景</strong></p>
<p>因此，单选框和多选框更适用于选项数量较少（一般不超过5个），有一定界面编排空间，且用户需要直观看到不同选项内容并进行比较选择的场景，如选择会员购买方案。</p>
<p id="B端选择录入类组件的使用辨析-适用下拉选择的场景"><strong>4）适用下拉选择的场景</strong></p>
<p>相反，下拉选择更适用于选项数量较多，表单配置复杂、包含各类不同样式组件或界面空间不足，且用户对于被隐藏的选项内容有一定预期的场景，比如选择省份。同时下拉器扩展性更高，下拉菜单可以进行多种类型的变体设计，满足不同业务场景的需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/qo8JK6xJtwSFpZKbAVrB.png" alt width="1920" height="800" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<h2 id="B端选择录入类组件的使用辨析-三、开关（Switch）">三、开关（Switch）</h2>
<h3 id="B端选择录入类组件的使用辨析-1.来源.1">1. 来源</h3>
<p>开关（Switch）这个组件就是模仿现实生活中的开关而设计的，现实生活中灯的开关一按，灯马上就亮了，因此开关有一个最大的特征：即时性。这在Ant Design设计系统的全局规则中也给出了注释：“当用户切换「开关」按钮将直接触发状态改变“，因此不同于单选框和多选框这种录入型组件，开关同时兼备录入和触发两种属性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/7IiALazfGjbXWERJT1Jp.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<h3 id="B端选择录入类组件的使用辨析-2.简单定义及样式">2. 简单定义及样式</h3>
<p>开关是一种特殊的选择组件，只能从“开启/关闭”两种状态选择其一，并且选择的结果会立即生效，通常点击后页面或者开关本身会有加载效果，或者点击后给出反馈，告知用户操作已生效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/JX8dXlE68MHKxqHNt9q7.png" alt width="1920" height="500" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<h3 id="B端选择录入类组件的使用辨析-3.开关和多选框的使用辨析">3. 开关和多选框的使用辨析</h3>
<p>上面提到复选框也经常作为开启某种模式或者应用某类设置使用，在这种场景下它与开关的逻辑十分相似，让人容易混淆。对于这两种组件的使用区别当前已有很多讨论，说法各异，这里根据我自己的探究和经验，从以下几点阐述下自己的看法：</p>
<p id="B端选择录入类组件的使用辨析-开关的即时性"><strong>1）开关的即时性</strong></p>
<p>开关的即时性决定了当开关与需要提交的表单一起出现时会存在矛盾，因此在表单中进行状态选择时，尽量选择单选框、多选框，避免使用开关。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/VCt8SdGGvgbHnzLQctHz.png" alt width="1920" height="680" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p id="B端选择录入类组件的使用辨析-开关更适合控制一组设置吗"><strong>2）开关更适合控制一组设置吗</strong></p>
<p>苹果官方人机界面指南中指出“开关比复选框具有更多的视觉权重，因此当它控制的功能比复选框通常更多时，它看起来更好。例如，您可以使用开关让人们打开或关闭一组设置”，然而在复选框的设计指南中又举了用复选框控制一组设置的例子。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/4SpbwwfrH7UL0F5tDLqT.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p>再来看一个飞书的例子，飞书管理后台中使用了开关来控制一组设置的开启，而在飞书客户端的设置里用的都是复选框。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/I1u3zL2GuphiFRduNlt2.png" alt width="1920" height="800" referrerpolicy="no-referrer"></p>
<section class="page_image_error js_catchremoteimageerror js_uneditable custom_select_card js_uneditablemouseover custom_select_card_selected">
<section class="page_image_error_loaded js_loaded"><i class="img js_nocatch js_noimgpopup js_noimgselected"></i></section>
</section>
<p>对于这个问题，个人认为苹果官方人机指南所说的因为开关比复选框具有更多视觉权重，所以更适合用来控制一组设置的说法并不准确，复选框本身也具有明显的选中和非选中状态，尽管开关组件自身大小以及在视觉效果上可进行设计的空间都更大，但是好像并不足以成为决定性的因素。</p>
<p>同时因为开关的即时性，如果是在需要提交的表单或者模态弹窗中用开关控制一组设置，反而是多选框更合适。</p>
<p id="B端选择录入类组件的使用辨析-从组件的来源分析"><strong>3）从组件的来源分析</strong></p>
<p>从组件的来源及发展历史来看，勾选的交互是基于PC键鼠操作设计的，单选框和多选框组件本身尺寸较小，因而触发区域会扩大至整体标签区域，方便鼠标点击；而开关是诞生于移动设备触控交互的组件，在移动端界面本身配置就比较简化，这时候配合开关自身相对较大的触发区域，用手指点击起来非常方便顺畅。</p>
<p>而在PC端，因为屏幕尺寸更大，同时很多B端系统配置项多、界面布局相较移动端要复杂很多，这时候要把鼠标移至开关热区去点击，反而没有勾选框来得方便，这种操作体验在一个纵列中有多个连续的开关时尤为明显。</p>
<p id="B端选择录入类组件的使用辨析-我的观点"><strong>4）我的观点</strong></p>
<p>依据开关的即时生效特性，开关更适合用在不需要提交操作的页面中，用来控制功能或设置的开启/关闭，在需要提交操作的表单或者弹窗中，建议使用多选框。</p>
<p>开关和勾选框都可以用来控制一组设置的开启/关闭，使用开关进行控制时，最好将它控制的下属组件都设置为立即生效，这取决于设置本身对于系统的影响，如果设置对于系统重要功能影响较大，则建议改用多选框去控制，让用户多一步“提交”操作进行确认，提升容错性。</p>
<h2 id="B端选择录入类组件的使用辨析-四、总结">四、总结</h2>
<p>回到开头设置优秀离职人才场景中的组件问题，这个需求流程涉及到的不只是在离职人员的编辑弹窗中操作，还涉及到在离职人员表格中的状态展示和设置优秀人才的单独操作。首先弹窗中的编辑操作是需要提交的，用开关比较矛盾；单选框和多选框在弹窗中都可以适用，但考虑还需要在离职人员表格中的状态展示和单独编辑，为了保持整体的交互一致性，最后选用了单选框。</p>
<p>总的来说，这几种选择录入类组件在B端系统中应用非常广泛，可能正是因为太司空见惯了，所以容易忽略它们细节上的特性和区别。尽管有时候这些组件的使用问题并不会对用户体验产生决定性的影响，但对细节的探究正是设计师严谨的工作态度和工匠精神的体现，只有秉持着这种对细节的打磨和追求才能不断提升产品的用户体验。</p>
<p>另外虽然文中做了一些各个组件的特性和适用总结，但可能在不同产品和系统中情况会更加复杂，需要设计师根据实际情况灵活处理。</p>
<p> </p>
<p>本文由@齐治设计 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5113384" data-author="1287163" data-avatar="http://image.woshipm.com/wp-files/2021/06/wfZQvGrpj70UUfx8nd1y.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            