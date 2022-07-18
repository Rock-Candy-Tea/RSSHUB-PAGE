
---
title: 'Design Token这样使用最聪明，赶紧收了吧，太实用了！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/07/3O58YUnlYvcm0Pt68JDp.png'
author: 人人都是产品经理
comments: false
date: Mon, 18 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/07/3O58YUnlYvcm0Pt68JDp.png'
---

<div>   
<blockquote><p>我们在设计工作的开展过程中，时常会因为参与人数多、业务背景杂而面临诸多考验。本文从概念、背景、类型、命名和应用五大方面来介绍视觉设计的原子Design Token，为大家解答在设计环节如何巧妙化解团队协作的难题。推荐设计伙伴们阅读了解～</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-837900 aligncenter" src="https://image.yunyingpai.com/wp/2022/07/3O58YUnlYvcm0Pt68JDp.png" alt referrerpolicy="no-referrer"></p>
<p>提到Design Token，很多同学可能第一反应是这是什么？其实这不是什么新名词，早在2014年，salesforce就开始在这块进行研究，它的名字来源于Jina Anne。</p>
<p>Design Token 是设计系统中的视觉设计原子。它们是一组有着统一命名规则的实体，用于存储视觉设计部分的具体参数，比如 HEX 色值、间距、尺寸的像素等。使用它可以有帮助为 UI 开发工作维护一套具备可扩展性、一致性的视觉体系。</p>
<p>在我们实际工作中，经常会面临参与成员众多以及业务背景的复杂性以及设计趋势变化的等问题和考验，你是否有以下的疑问：</p>
<ul>
<li>设计团队加入新人，因为对规范的不了解，经常会不知道不同场景对应色值的应用。</li>
<li>开发同学代码碎片化，在遇到新业务时，需要二次开发，迭代以及维护成本增加。</li>
<li>随着公司战略升级，品牌色做了调整，因为调整页面众多，经常因为某些色彩细节而忘记调整。</li>
</ul>
<p>那么接下来让我们一起了解下Design Token吧~</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/FagdjQo96I6YymTejta1.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="537" height="824" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、概念</h2>
<p>从本质上来讲，<strong>Design Token是一种设计与开发共同使用的工作思维和方法</strong>。”Token“的意思是令牌或者指令，简单的可以理解为<strong>对视觉样式封装的属性参数</strong>。在设计师以及开发都理解的命名规则上，<strong>对组件中的每一个元素进行有规律的代码化命名</strong>，统一了两个不同工种（前端与设计）的交流语言，保证设计系统可以被快速管理，确保了产品体验的灵活性一致性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/SRkFmmDw3YLmCpsyL4nJ.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="470" height="307" referrerpolicy="no-referrer"></p>
<p>上面解释如果还觉得复杂的话，你可以把Design Token理解为设计以及前端都认可的外号。例如当前按钮背景色值的外号是”colour-button-backgroung-primary-normal“，这样即使以后按钮背景色再怎么变化，前端都可以根据这个外号来应用颜色，这样的话，按钮在系统中的背景色就是唯一的。</p>
<h2 id="toc-2">二、使用场景</h2>
<p>我们可以设想一下假如没有Token，我们开发是如何工作的。</p>
<p>例如我们之前的品牌色#00704a，在页面中会大量被使用，那么当每个页面出现该颜色的时候，开发得重复编写，那后续品牌色升级，开发改起来会特别麻烦。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/yNkJiIuKT1QA5fdDODl6.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="542" height="354" referrerpolicy="no-referrer"></p>
<p>这个时候我们假如使用了Token，开发在实际工作的时候就不需要输入这个颜色的色值，而只需要这个颜色的Token“color-primary：blue-7”即可。即使后续这个品牌色值再怎么调整，也不需要开发做重复的工作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/uagxxNVwGPEITsMgogC6.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="554" height="342" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、类型</h2>
<p>Token在实际的应用中可以分为3类，<strong>全局Token</strong>（Global Token）、<strong>别名Token</strong>(Alias Token)以及<strong>组件Token</strong>(Component Token)。</p>
<h3>1. 全局Token</h3>
<p>作为全局Token，通过字面意思就知道它并没有限定使用的范围，也就是<strong>项目中所有的Token都可以从这里调取</strong>，无论是颜色、字体、行高还是圆角等。例如颜色Token通常被命名为Blue-7、Blue-8等。</p>
<h3>2. 别名Token</h3>
<p>它的存在是<strong>为了限定全局Token的使用场景</strong>，这样可以让Token更加场景化，可以被灵活调用，在后续的更改中自由替换。<strong>它的值都是从全局Token中调取过来。</strong>例如colour-primary：$blue-7。</p>
<h3>3. 组件Token</h3>
<p>这一步就是特别具体的，一般添加组件的的名称以及属性，可以直接进行开发，<strong>通常作为特定名称</strong>，大家基本上看了Token就知道它是什么。<strong>它的值一般从别名Token调取</strong>，在特殊情况下也会从全局Token中调取。例如：button-color-primary-background:$colour-primary。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/Z7LpTI8JLuaJILd1W7ri.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="541" height="269" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、命名</h2>
<h3>1. 拆解Token</h3>
<p>要想对Token进行合理命名，我们就需要对其进行原子级别的拆解。拆解为<strong>类别、元件、属性、等级、状态这5类</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/MZc5gectRsJpjDwXDB2b.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="600" height="483" referrerpolicy="no-referrer"></p>
<p>不同公司针对Token有着不同的定义方式，只要设计师与前端达成一致就好。</p>
<p>例如产品设计中的Lightning Design System在对Token进行原子级拆解的时候就包含了12种：</p>
<ol>
<li>Background Color</li>
<li>Text Color</li>
<li>Border Color</li>
<li>Font</li>
<li>Font Size</li>
<li>Opacity</li>
<li>Line Height</li>
<li>Spacing</li>
<li>Radius</li>
<li>Sizing</li>
<li>Shadow</li>
<li>Time</li>
<li>Media Query</li>
<li>Z-index</li>
</ol>
<p><strong>（1） 类别</strong></p>
<p>类别指在Token中有着最广泛应用场景，最基础的组件元素。</p>
<p>我们对常用的组件围绕形、色、字、构、质这5个维度对其进行拆解，分为圆角、色彩、文字、间距以及阴影这5类</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/ddepeIAdFE5Pyc4hAvZD.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="501" height="461" referrerpolicy="no-referrer"></p>
<p><strong>（2） 元件</strong></p>
<p><strong>元件指具体的单一的组件种类</strong>，例如按钮这个类别下就包含了主按钮、默认按钮、虚线按钮、文本按钮、链接按钮。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/j8L0UQsoz1RVkoBS0WVh.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="537" height="216" referrerpolicy="no-referrer"></p>
<p><strong>（3）属性</strong></p>
<p>这里的属性通常分为<strong>背景</strong>或者<strong>边框</strong>两种。可能会有同学疑问，为什么只有2种属性，因为这里我们的样式不与具体组件绑定，仅仅以样式本身的性质来做区分，所以在属性这里我们罗列了2种样式。</p>
<p>例如下图的弹窗，线框的描边、输入框的描边以及按钮的描边都可以调取统一的Token，将原本相同元件但不同样式的组件进行统一化管理。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/oI9EH28l1vQI7IHgn8Gj.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="495" height="307" referrerpolicy="no-referrer"></p>
<p><strong>（4） 等级</strong></p>
<p>等级的状态由组件的基本功能以及具体的使用场景决定，有部分组件只有一个等级，例如”面包屑”，这时候在Token命名的时候就可以不体现，而有的组件例如“按钮””导航“等则有多个等级；</p>
<p><strong>（5）类别</strong></p>
<p>状态则是组件在交互时候的不同样式，通常有默认、悬停、点击、禁用等，有时候还会根据场景的不同，有危险以及幽灵等状态。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/Od7rSj7F1wJGilyKKDXe.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="514" height="287" referrerpolicy="no-referrer"></p>
<h3>2.Token的命名</h3>
<p><strong>Token的命名没有唯一的表达方式，只需前端与设计保持约定一致即可。</strong>这里Token的命名方式与组件基本一致，都是按照”<strong>类别-元件-属性-等级-状态</strong>“的顺序依次往下。不同单词之间采用“<strong>–</strong>“或者”<strong>.</strong>“符号相连是可以通用的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/NBphszyLmOmoG1KJFKrW.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="594" height="332" referrerpolicy="no-referrer"></p>
<p>上面按钮的命名虽然看起来很复杂，但是它也可以很明确的告诉设计师以及前端它的使用场景。例如它告诉我们可能用于按钮的背景，它还表达了它当前的等级是什么，以及它的具体状态是什么。</p>
<h3>3. 整理Design Token</h3>
<p>有了统一的命名规则后，我们可以把涉及到Token编写的组件全部以表格的形式整理出来，开发在编写的时候可以对照图表中组件的名称，直接在导出的json文件中调用该组件的详细信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/0XLYqoWRLtynCIEhkLJX.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="531" height="418" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、应用</h2>
<p>因为我们的设计软件是Figma，因此挑选了与之匹配的插件<strong>“Figma Tokens”</strong>来辅助我们协同。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/NSnofjR7nNT3ZncjqzX1.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="445" height="283" referrerpolicy="no-referrer"></p>
<h3>1.手动输入Token</h3>
<p>我们以下图为例，尝试下怎么根据Token值在在该插件中手动输入。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/YW7Fx01CXxPBPeJFVR0r.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="610" height="960" referrerpolicy="no-referrer"></p>
<h3>2.批量导入Token</h3>
<p>手动输入大家可能觉得太麻烦，那么我们可以尝试下如何批量导入Token，这里以颜色的梯度色板为例，首先我们先在Figma里面利用Foundation插件建立Gobal梯度色板（也可以自己手动在Figma中输入产品的基础色值），随后将其导入Figma Token中。这些导入后的颜色作为全局Token，后续将会被引用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/Fl9nlwT1ndgj0xwXGyFB.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="521" height="1177" referrerpolicy="no-referrer"></p>
<p>在过去开发利用蓝湖编写组件的时候，需要选中这个组件，然后复制代码后输入该组件相对应的颜色值。现在就不需要知道这些具体的值，只需要知道组件的token名称就可以在调出的json文件中该组件的详细信息，大大提升了工作效率。</p>
<h3>3. 新建主题</h3>
<p>接下来我们在插件左侧新建别名Token（这里的命名建议采用英文，以防后续导出json出现问题），并根据颜色的应用场景分为背景色、反馈色、文字色等（具体根据当前项目所需命名）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/K4pClN977aaTT10EeaZs.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="579" height="373" referrerpolicy="no-referrer"></p>
<p>这些命名好之后我们就可以开始通过简单的样式进行应用，例如我们想更换视窗中的按钮背景颜色，这时只需选中Figma操作区的按钮背景后再选择别名Token中对应的蓝色即可进行联动替换（这里要注意的是主题顺序，选中下方主题，则会对上方主题进行覆盖）。</p>
<h3>4. 导出Json</h3>
<p>导出Json后，开发在编写代码的时候可以对这个文档直接进行直接复制 ，确保设计与开发的一致性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/L3b64WCkDwmksisR9JO0.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="501" height="435" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、写在最后</h2>
<p>以上是有关Design Token的介绍以及落地的相关内容，它对还未建立公司组件库且想提高团队的协作特别有帮助。</p>
<p>Token提供的可操作性空间很大，可支持自定义的操作很多，其实目前做到文字以及颜色的自定义就可以很快提升我们的效率了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Design Token这样使用最聪明，赶紧收了吧，太实用了！" src="https://image.yunyingpai.com/wp/2022/07/bMVnwJCygRqVs2AJlVB3.png" alt="Design Token这样使用最聪明，赶紧收了吧，太实用了！" width="606" height="323" referrerpolicy="no-referrer"></p>
<p>在未来的产品发展中我相信Token的应用不单单是作为辅助插件的支撑，会成为这些设计软件内部的标配，赋能更多的产品。不知道你们公司是如何应用Design Token，欢迎一起讨论~</p>
<p>我是江鸟，一个爱学习爱分享的设计师。</p>
<p>我们下期见~</p>
<p> </p>
<p>本文由 @江鸟的设计生活 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5528875" data-author="201510" data-avatar="http://image.woshipm.com/wp-files/2021/11/7ScndtOhNf4Is5h24P8k.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            