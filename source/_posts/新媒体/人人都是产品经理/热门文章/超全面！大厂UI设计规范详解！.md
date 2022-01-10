
---
title: '超全面！大厂UI设计规范详解！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.yunyingpai.com/wp/2022/01/xZdEcGQiibizpNAL35Ju.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 09 Jan 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/01/xZdEcGQiibizpNAL35Ju.jpg'
---

<div>   
<blockquote><p>编辑导语：建立合适的UI设计规范，对提升用户体验有很大帮助。这篇文章讲述了设计规范的定义和来由，并说明了在文字、色彩、阴影、圆角、布局、栅格、图标、文案和组件等方面的详细设计规范，推荐对UI设计感兴趣的同学阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-736188 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/xZdEcGQiibizpNAL35Ju.jpg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、设计规范综述</h2>
<h3>1.1 定义</h3>
<p>作为一个B端产品，为了应对公司快速迭代开拓市场和一部分购买者的定制化需求，与此同时还要保障产品间的用户体验一致性，近年来设计规范这一解决方案不断升温，如Salesforce，antdesign等纷纷推出了自己的设计规范。</p>
<p>那么到底什么是设计规范呢？和设计语言、设计原则、组件库等有什么关系呢？</p>
<p>我认为的设计规范是以下的定义：设计规范由设计原则、设计语言和组件库构成，在设计原则的指导下使用设计语言和组件库创建体验一致的用户界面。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/ydMTA2COa5rrt47VJy5S.png" alt="超全面！大厂UI设计规范详解！" width="600" height="303" referrerpolicy="no-referrer"></p>
<p>设计原则：即整个设计规范所要遵循的全局规则，为设计提供方向指导。以下给出几个例子：</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/d8TdVG0tjQDVhtcjNjXM.png" alt="超全面！大厂UI设计规范详解！" width="599" height="370" referrerpolicy="no-referrer"></p>
<p>设计语言：包括色彩，文字、图标等。</p>
<p>组件库：分为基础组件（按钮，下拉列表等）及业务组件（商品模块）。</p>
<p>在做设计语言和组件库时，有一个基本原则是，少即是多(less is more)，用尽可能少的样式来实现设计目标，例如按钮提供三种尺寸即可，在适应不同场景需求的同时保证体验的一致性；另一方面，保持克制的设计规范可以进一步减少设计师的决策时间，提高设计效率。</p>
<h3>1.2 理论基础-原子设计</h3>
<p><strong>1.2.1 什么是原子设计</strong></p>
<p>原子设计是构建设计规范的核心指导理论。2013年，Brad从化学中得到了灵感，创建了原子设计理论。在化学中，所有的物体都是由原子构成，原子构成分子，进而构成宇宙万物。对应到界面中，界面也是如此，所有的元素都是由文字、颜色等最基本的元素构成的。这些基本元素构成组件，组件构成页面。</p>
<p>原子设计概念的提出使得设计规范演变成为了一种更为高效、科学的设计规范，极大的改善了设计师与前端工程师的工作体验。</p>
<p><strong>1.2.2 原子设计系统的五个层次</strong></p>
<p>原子设计包含五个同时工作的阶段，以更慎重和更具层次的方式创建界面设计规范。</p>
<ol>
<li>原子：原子是构成界面的最小元素，例如颜色、文本、图标、线条。它们在在界面这个维度上不能再被细分。例如图标，本身是可以继续细分的，但是对于界面而言，图标细分得到的元素是没有任何意义的。</li>
<li>‌分子：原子按照一定的规律组合就构成了分子，它们拥有独特的功能，例如下拉列表，步进器等。</li>
<li>‌组织：在界面中组织体现为由分子原子组成的模块，例如数据概览的卡片。</li>
<li>‌模板：在界面中，模板的体现是原型图，是页面的基本形态，可以让我们快速试错，搭建出一个功能良好的整体。</li>
<li>‌页面：在模板的基础上将占位符更换为真实内容，并进行视觉优化即为页面。</li>
</ol>
<h3>1.3 为什么需要设计规范</h3>
<p><strong>1.3.1 软件危机</strong></p>
<p>在讲述设计规范之前，我想先讲述一个互联网史上的真实事件——软件危机。</p>
<p>19世纪80年代，软件的复杂度进一步提升，大规模软件甚至会由由数百万行代码组成，有数以百计的程序员参与其中，抽象语言解放了程序员的生产力和想象力，人们可以像写文学小说一样随意发挥地去写代码。</p>
<p>摆在面前的问题是如何高效且可靠地维护与迭代如此庞大的软件。之后C++、Java等我们熟知的面向对象的编程语言诞生了。</p>
<p>面向对象这种模式有一个很重要的特征是封装。这就好比当你在写王者荣耀的代码时，小兵是出现频率较高的模块，你可以提前把王者荣耀里的一个小兵封装成一个代码块，当你需要用到它时，不必重新一行一行写，只需要把它整体调用即可。</p>
<p>纵观软件发展史，20世纪60年代的第一次软件危机创造了“模块”概念；20世纪80年代第二次软件危机引出了“面向对象编程”，创造了“对象”概念。</p>
<p>模块与对象本质上都是对软件进行拆分与封装，只是对象拆分的粒度更大，维度更高。这点与原子设计的原理不谋而合，从色彩文字等基础元素，到按钮、选择器等基础组件、再到典型模块，也是对大型软件的设计元素不同粒度的拆分与封装。</p>
<p><strong>1.3.2 设计规范的优势</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/sq6zFOn6Sz3wTKPtroDG.png" alt="超全面！大厂UI设计规范详解！" width="599" height="251" referrerpolicy="no-referrer"></p>
<p>设计层面：解决用户体验一致性，减少设计成本，提高设计效率，使得设计师可以快速承接新需求。沉淀设计资产，使得设计更加持续地输出价值，减少一次性设计，同时使设计师从样式中解放出来，站在更高的层面上来思考业务与体验。</p>
<p>开发层面：与设计规范同步形成研发资产，避免重复造轮子，保证代码质量，降低维护和拓展的成本。</p>
<p>测试层面：避免重复的无意义走查。之前遇到过一个深色模式的需求，尽管只换了颜色，但是测试仍然把所有组件都测试了一遍，加上重复的设计、开发量，导致原本一个很简单的需求，居然花费了12人天的工作量。</p>
<p>产品层面：提高产品迭代与优化效率，降低试错成本。</p>
<p>协作层面：降低不同设计师之间以及设计师与开发工程师之间的沟通成本。</p>
<h3>1.4 为什么要自己做设计规范</h3>
<p>这个时候可以会有小伙伴问，目前市面上有这么多的第三方设计规范，例如antdesign，element，有必要自己重复造轮子做一遍吗？答案是非常有必要。原因如下：</p>
<p>第一，B端自身的业务性决定了市场上没有万能的设计规范，那些设计规范的组件并不能100%满足我们产品的需求。另外一方面使用封装好的第三方设计规范，在此基础上进行修改，效率很低，适配的复杂度和重新开发相差无几。</p>
<p>第二，大家都在使用第三方设计规范时，产品的同质化便不可避免。为了避免这种情况发生，我们必须要从设计语言开始，设计自己的规范。</p>
<p>那些大厂的成熟的组件库该如何用呢？我认为应该把它当成一个字典，有不会的地方，可以去参考人家的成熟的解决方案。</p>
<h3>1.5 设计规范的落地</h3>
<p><strong>1.5.1 落不了地的原因</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/JzLoSkNMxEawLQ47GvEp.png" alt="超全面！大厂UI设计规范详解！" width="598" height="253" referrerpolicy="no-referrer"></p>
<p><strong>1.设计层面：</strong></p>
<ul>
<li>组件扩展性弱：有的设计师做出来的组件虽然看着很好，但是实际上使用时，适配效率很低，用组件去扩展和重新做的效率差不多。</li>
<li>脱离业务：大部分时候设计师手中都有任务，于是这个任务就落在了实习生的肩上，但是实习生不了解业务，做出来的是空中楼阁，抛开业务谈设计规范的都是耍流氓。</li>
<li>缺乏开发思维：设计师不了解开发的实现方式，可能会做出来开发较难实现的组件。</li>
</ul>
<p><strong>2.开发层面</strong></p>
<p>缺少开发资源：设计规范的作用是巨大而缓慢的，不能即时产出很大的价值。</p>
<p>另外一方面，设计规范的落地会增加开发工程师很多的工作量，且无法量化收益。这也导致很多时候无法争取到足够的开发资源来做这件事，导致达不到预期的效果。</p>
<p><strong>1.5.2 如何落地</strong></p>
<p>说完了落不了地的原因，那么如何落地呢？我认为要从以下四个方面来推进：</p>
<ol class="list-paddingleft-2">
<li>写一份设计规范的价值的提案给领导，争取到足够的开发资源。</li>
<li>借鉴敏捷开发的思想，小步迭代快速推进，将设计规范的覆盖放在每次迭代过程中。</li>
<li>把设计规范的开发交给熟悉业务的设计师来做，通过业务提炼复用率高的典型元素，优先开发，最大化投入产出比。</li>
<li>设计师在做设计规范时，要不断与开发工程师沟通，保证设计规范的还原度。</li>
</ol>
<h2 id="toc-2">二、文字规范</h2>
<p>B端UI界面的视觉设计是一种偏向于排版的设计类型，而其中对于文字的使用更是重中之重。</p>
<p>文字包括字体，字重，字号，行高、颜色五个属性。一般情况下，字体采用系统自带的字体（例如苹方、微软雅黑、思源黑体），另外对于B端来说，一般都会有较为重要的数据，这时可以采用特殊字体给与一定的强调，最常用的便是DINpro。</p>
<p>还有一点要注意，我们使用的字体一般是基于用户有什么字体，而由于win和Mac默认字体不同，所以要提前预留好字体风格类似的多种字体。并且可以设置多个字体，通过逗号隔开，如果第一个字体用户没有，那么会自动替换成下一个字体。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/wWXGvDeIzrnpYCZde51i.png" alt="超全面！大厂UI设计规范详解！" width="600" height="175" referrerpolicy="no-referrer"></p>
<p>字号上，精简为主，可以用字重和颜色来表现层级，就不要用字号来体现。淘宝在2019年的改版中便升级了这一点。将原来的11个字体层级缩减至了7个。</p>
<p>行高上，我们目前采用的方案是行高是字体行高为150%字号，取4的倍数。</p>
<p>但是目前会遇到额外间距的问题。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/4lm8YyLKbOrB5v8mcMyC.png" alt="超全面！大厂UI设计规范详解！" width="600" height="367" referrerpolicy="no-referrer"></p>
<p>前段时间谷歌发布了新的CSS更新“leading trim”，可能会是之后的行高解决方案。感兴趣的小伙伴可以点击链接了解一下（https://blog.csdn.net/weixin_39781930/article/details/111576051）</p>
<p>字重上，以开发的视角来看的话，包括从100-900的九个字重。一般我们只采用regular、medium、semibold三个字重。</p>
<h2 id="toc-3">三、色彩规范</h2>
<h3>3.1 基本介绍</h3>
<p><strong>3.1.1 色彩的作用</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/uh8RmsrhjL24iIBUEeb3.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<p>B端产品中，颜色不仅仅用来传达品牌调性，更多的是用来传达以下信息：</p>
<ol class="list-paddingleft-2">
<li>反馈信息 通过不同的颜色给予信息反馈，例如红色代表错误信息，绿色代表成功信息。</li>
<li>突出层级 通过色彩可以对内容信息进行分层级展示，提高用户读取信息的效率。</li>
<li>表明状态 通过颜色来区分某个事物处于何种状态。</li>
</ol>
<p><strong>3.1.2 组成</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/7OUIeTWkESu6SY9kGqNR.png" alt="超全面！大厂UI设计规范详解！" width="600" height="311" referrerpolicy="no-referrer"></p>
<p>在真实的设计场景中，对色彩的复杂度要求是非常高的。色彩规范应该基本覆盖一套产品对用色的所有场景。</p>
<p>一套完整的色彩规范，包括品牌主色、语义色、中性色。</p>
<ol class="list-paddingleft-2">
<li>品牌主色：通常，一套产品只有一个品牌主色，是界面中出现最多的颜色，在需要用色强调而且没有其他要求时，一般都会选择主色，例如tab的选中态，图表的颜色等。</li>
<li>语义色：即功能色，借助人们的对色彩的心理模型，帮助人高效获得信息。例如绿色代表通行、成功，红色代表禁止、错误，橙色代表警告、</li>
<li>中性色：除文字外，中性色还被大量运用在分割线、边框、背景等场景中。</li>
</ol>
<p><strong>3.1.3 色彩系统的原则</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/JbJ36tK8HVtCirupvwtF.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<ul>
<li>理性的：我们在选色时，尽可能避免个人的设计风格，减少配色的主观性，理性有逻辑地选色。</li>
<li>可扩展的：使用这种选色方法可以扩展生成更多的颜色，以适应不同的变化。</li>
<li>和谐的：色彩规范中的颜色互相搭配使用时，应该是和谐的。</li>
</ul>
<h3>3.2 如何制作色彩规范</h3>
<p>在开始制作色彩规范之前，先介绍一下HCL色彩空间。</p>
<p>HCL (Hue-Chroma-Luminance) 与 RGB、HSB一样同属色彩空间的一种，因为最早由国际照明协会 CIE 提出，又被称作 CIELch。</p>
<p>目前大家常用的色彩数值可视化的色彩空间是HSB，设计师可以通过H(色相)，S（饱和度），B（明度）三个数值来量化色彩，实现理性配色。</p>
<p>但是传统的HSB色彩空间的缺点是，明度数值是基于计算机元件而言，而非人眼。另外，计算机的明度与人眼感觉到的明度并非线性匹配，这就导致在不同颜色中，即使色相相同，我们感觉到的明度（即感官明度）也是不一致的。</p>
<p>而HCL就避免了这个缺点，在HCL中，只要两种颜色的L相同，感官明度就是相同的，HCL可以完美的量化我们对色彩明度的感觉。但是目前主流的设计软件基本上不支持HCL色彩空间配色，因此要借助插件或者网站。这里给大家推荐Figma的一个插件：HCL color。不用figma的小伙伴可以去这个网站http://tristen.ca/hcl-picker/#/hcl/12/1.03/000000/F69877。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/lV1e6PCrTQ6MIgQ4Tm6N.png" alt="超全面！大厂UI设计规范详解！" width="599" height="273" referrerpolicy="no-referrer"></p>
<h3>3.3 落地</h3>
<p>落地分为两个方面：设计方面和开发方面。</p>
<p><strong>3.3.1 设计方面</strong></p>
<p>将颜色生成样式库，并规定设计同事不可以手动调色，只可以从设计规范中取色。</p>
<p><strong>3.3.2 开发方面</strong></p>
<p>在前期与开发同事沟通，将每个颜色定义为一个变量，在代码中不使用具体的色值，而是例如red-100的的色值，这样做的好处是：</p>
<ul>
<li>在需要替换某个色值时，只需要在底层对变量改变即可实现全局的更改，提高了很多效率。</li>
<li>开发同事完全从库中取色，保证了色彩的准确性，提高了设计稿的落地率。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/11Acihd4jlxGWBmF43vx.png" alt="超全面！大厂UI设计规范详解！" width="599" height="388" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、阴影规范</h2>
<p>现实生活中的物体不可完全重叠，当光打过来时，每个物体都会产生阴影。这是我们理解物体的层叠关系的重要依据。依据现实中的这一行为，我们把阴影规范挪到屏幕世界中，使得用户更容易理解我们的系统。阴影规范提供给了我们另一个表达元素区别的维度，不同的阴影清楚地传达了不同的交互状态。</p>
<p>某一对象在屏幕中的高度视觉表现为其阴影，阴影越大，高度越高。但是生活中真实的阴影错综复杂，我们不可能也没必要完全复刻，我们只需要能够表达出元素层级即可。与按钮相同，我们将阴影分为三个等级，分别为，S、M、L。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/XsPsOI62OfWSuVZEanA4.png" alt="超全面！大厂UI设计规范详解！" width="597" height="306" referrerpolicy="no-referrer"></p>
<p>S：突出组件悬停效果，表示可供性。对于这个数据概览卡片来说，鼠标移入移出时阴影的显示与隐藏提供了一个交互可能性，表明它是可以点击交互的。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/JXeedsbqEjsay3XmHBkL.png" alt="超全面！大厂UI设计规范详解！" width="600" height="286" referrerpolicy="no-referrer"></p>
<p>M：给下拉列表，气泡提示等使用的阴影。因为这些元素是与由底层元素展开而来的，但又不属于底层元素，所以将中等层级的阴影给了这些元素。</p>
<p>L：模态组件阴影。例如弹窗。当弹窗出现时，弹窗位于绝对的最顶层，所以阴影最大。</p>
<h2 id="toc-5">五、圆角规范</h2>
<p>圆角是用一段与图形两边相切的圆弧替换原来的直角，圆角的大小用圆弧的半径R表示。在界面中运用圆角主要有以下两个好处：</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/jh58Kf2EeVAJbdybG4U6.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<ol class="list-paddingleft-2">
<li>亲和感。我们倾向于“避免尖锐的边缘，因为在自然界中它们可能会构成威胁”。运用圆角矩形能给我们带来亲和感，圆角越大，亲和感越高。</li>
<li>辨识度。相对于没有圆角，人可以更快的辨识圆角矩形。</li>
</ol>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/J5ULt9etjulrgCgKPjPm.png" alt="超全面！大厂UI设计规范详解！" width="599" height="224" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、布局规范</h2>
<p>对于组件库来说，我们可以把组件比喻为积木，而布局则是把积木搭建为各种不同成品的图纸。</p>
<h3>6.1 盒子模型</h3>
<p><strong>6.1.1 设计师为什么需要了解盒子模型</strong></p>
<p>在介绍布局之前，先介绍一下盒子模型。虽然盒子模型是前端开发中的一个概念，但是了解一些前端知识对我们设计的落地以及与前端的沟通上大有裨益。我们可以带着盒子模型的思维去做设计，这样开发人员拿到设计稿后，更容易了解我们的布局逻辑，降低沟通成本，提高落地率。</p>
<p><strong>6.1.2盒子模型是什么</strong></p>
<p>盒子（box）模型是开发中经常用到的CSS模型，我们日常所见到的界面都是由一个一个的盒子拼接而成的。打开安卓手机的开发者选项中的显示布局边界，便可以看到手机上的各个盒子的排列。</p>
<p>在电脑浏览器打开检查视图，也可以看到每个元素对应的盒子。我们可以理解为开发同事都是先画一个一个的盒子，然后在盒子里填充，也与我们提供的矩形切图相对应。并且盒子间存在嵌套情况，几个小盒子可以作为一个大盒子的内容。</p>
<p>以我们的生活来举例的话，例如我们去买月饼，大盒子里装了四个小盒子，每个小盒子里是一个月饼。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/57QckDT9ENHmVT7jfCdZ.png" alt="超全面！大厂UI设计规范详解！" width="597" height="275" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/4jPOV47wWUdkELvDVBIT.png" alt="超全面！大厂UI设计规范详解！" width="599" height="324" referrerpolicy="no-referrer"></p>
<p><strong>6.1.3 设计师如何利用盒子模型</strong></p>
<p>了解了盒子模型后，我们在设计时，该如何利用呢？做设计时，对任何元素都尽量用一个矩形给他封装，这样子前端在定位元素和确定间距时可完美实现设计稿的内容。</p>
<p>而前段时间figma更新的auto layout 功能与盒子模型基本完美对应。我们在设计时可以使用这个让开发更容易get我们的设计稿，减少沟通时间。</p>
<p>以标签页为例，我们设计时，不只是画个横线与文字就行了，这样开发无法理解到设计稿，后面还会继续找我们询问触控热区。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/mtBSvyZcnItsBnrJsy86.png" alt="超全面！大厂UI设计规范详解！" width="600" height="178" referrerpolicy="no-referrer"></p>
<h3>6.2 导航</h3>
<p>导航将网站的信息架构分组归类展示给用户，方便用户到达想去的界面。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/YM428iSdXIYMGu4FeDuC.png" alt="超全面！大厂UI设计规范详解！" width="600" height="392" referrerpolicy="no-referrer"></p>
<p><strong>6.2.1 顶部导航</strong></p>
<p>优点：符合人眼浏览网页的视觉动线，给用户提供更沉浸式的浏览体验。</p>
<p>缺点：扩展性差，由于顶部空间有限，无法承载太多的菜单项。另外由于水平菜单的特性决定了无法承载太多的层级，当扩展至三个或四个层级时，顶部导航的易用性极差。</p>
<p>通用性较差：同样受空间的限制，菜单项字数被严格限制。</p>
<p>适用产品：整体结构无论是广度还是深度均较简单且之后不会扩展很多功能的产品。</p>
<p><strong>6.2.2 侧边导航</strong></p>
<p>优点:侧边导航是以树形控件的方式来表示的，相对于顶部导航，无论是数量和层级，扩展性均较好。</p>
<p>方便寻找：由于纵向浏览无需把每个单个菜单完整浏览，相对水平菜单，定位更快。</p>
<p>缺点：由于用户在浏览内容的过程中，不可避免会被左侧常驻的导航栏打断视线流,阅读沉浸感较低。</p>
<p>适用产品：目前结构不是非常复杂但之后会迭代增加很多功能的产品。</p>
<p><strong>6.2.3 混合导航</strong></p>
<p>优点：扩展性好:由于增加了-个顶部的一级菜单，扩展性是三者中最好的。</p>
<p>缺点：</p>
<ul>
<li>交互路径长：除了和侧边导航-样存在沉浸感低的问题，由于每个菜单项都需要点击顶部和侧边两次,操作效率低。</li>
<li>占用空间大：在B端产品中，界面空间寸土寸金，混合导航常驻的两个导航占用了较多的空间。</li>
</ul>
<p>适用产品：目前结构已经非常复杂的庞大产品。</p>
<h3>6.3 栅格</h3>
<p><strong>6.3.1 栅格介绍</strong></p>
<p><strong>1. 来源</strong></p>
<p>栅格系统原本来源于平面设计，早在20世纪初，德国、荷兰、瑞士等国的平面设计师们发现通过维持视觉秩序,从而使版面能更加清晰有效地传递信息，二战后这种理念在瑞士得到了良好的发展。有兴趣的小伙伴可以去看下由瑞士设计师大师Josef Miller—Brockmann (约瑟夫.米勒-布罗克曼)所著的《平面设计中的网格系统》一书。</p>
<p><strong>2. 优势</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/ovQpkuKYlJgPHijeUyhc.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<ul class="list-paddingleft-2">
<li>高效：将布局标准化，可减少设计决策的时间，让设计师专注于内容.上的设计呈现。</li>
<li>响应式布局:由于web端尺寸多样，使用栅格系统可以做到自适应布局(在面对多个分辨率的系统时，无需设计多套方案，仅需设计一套来适配即可)</li>
<li>美观:提高内容的规律性，让设计更有秩序和节奏感，赋予界面数学逻辑美感，提高用户的阅读和浏览效率,为用户提供更好的体验。</li>
<li>协作:由于栅格系统的可复用性，多个设计师合作时，可以共用-套栅格系统，提升整体布局的统-性。同时也避免了设计与开发的反复确认的情况，使得部门内部与部门间沟通更顺畅。</li>
</ul>
<p><strong>6.3.3 组成与原理</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/O46X6dJBcYhhYPW6SiP3.png" alt="超全面！大厂UI设计规范详解！" width="600" height="471" referrerpolicy="no-referrer"></p>
<p>栅格系统包括页边距，列和水槽。</p>
<p>页边距：指内容区与页面的边距。</p>
<p>列和槽：列是承载内容的容器，水槽是两个列(即内容)之间的间距。在前端视角中列宽是根据百分比而不是固定值定义的。通常说的栅格数就指的列数。水槽越宽，页面留白越多，呼吸感越强。</p>
<p>自适应原理：在网页应用的设计中较为常见的一种响应方式，当屏幕宽度改变时，页边距和水槽宽不变，列宽自适应。</p>
<p>计算公式：以24栅格(即有24列)为例，页面自适应部分总宽度: 24*列宽 +23*水槽宽+2*页边距。</p>
<h3>6.4 间距</h3>
<p>在设计间距系统中，我们一般会基于8点网格系统和亲密性原理规定几个典型值。例如4,8,(12,)16,24,32……。遇到间距时在这些值中选取合适的即可。另外一般我们会使得大模块的纵向间距与栅格系统中的水槽大小相同。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/gzouFtVE8oRJ3hvvyR3r.png" alt="超全面！大厂UI设计规范详解！" width="599" height="265" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、图标规范</h2>
<h3>7.1 图标重要性</h3>
<p>当一个界面完全由文本构成时，用户被迫阅读每个文字来找到自己想要的信息。而引入图标后，降低了用户的认知负荷，帮助用户更快导航，提高用户使用产品的效率。另外一方面、设计精致风格统一的图标提高界面的美观度的同时，也为用户带来了连贯一致的使用体验。</p>
<h3>7.2图标规范的内容</h3>
<p>尺寸：由于不同形状(三角形，圆形、长方形、正方形)具有不同的视觉大小，仅仅规范图标的大小是不够的，通常我们会设计一套图标keyline，来保证不同的图标具有相同的视觉大小。</p>
<p>填充/描边：一般的系统功能图标采用描边。工作台的常用功能入口一般采用带背景的填充图标，原因是在空间有限的的区域，太多形状会显得杂乱，另一方面面型图标的视觉面积较大，短时间内更加容易识别。</p>
<p>除此之外，还包括圆角、端点、线宽、倾斜角度等其他规范。</p>
<h3>7.3 落地</h3>
<p>在产品中，图标通常有多种尺寸，我们一般会为每个尺寸的图标各创建一个frame来进行管理，其中，我们会把同一个图标的填充版和描边版创建为一个组件集，这样在调用时可以直接控制图标的填充和描边，在做有选中态和非选中态的组件时尤为方便。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/nAo4tPuPziGCtkwNbA3D.gif" alt="超全面！大厂UI设计规范详解！" width="600" height="280" referrerpolicy="no-referrer"></p>
<p>另外，在命名上，我们会用图标的内容为它命名而非表意，例如一个灯泡的图标，我们会直接命名为灯泡而非创意。</p>
<h3>7.4 图标库推荐</h3>
<p>在这里给大家推荐几个我常用的图标库，在来不及画图标时，可以先用这些迅速建立起一个图标组件库。之后有时间了再慢慢更新为自己的图标。</p>
<p>Iconfont：国内功能很强大且图标内容很丰富的矢量图标库,提供矢量图标下载、在线存储、格式转换等功能，特点是图标非常丰富。</p>
<p>Remixicon：Remix Icon 是一套面向设计师和开发者的开源图标库。质量很高，风格中性大气，因此适用于很多风格的项目，分为“线性图标”和“面型图标”两种风格。相比于 Material Icons，RemixIcon 看起来风格会更统一、简约且精致硬朗一些。</p>
<p>IconPark：这是字节CUX设计团队出品和维护的开源图标库，如今已对外开放使用，特点是图标大小，线宽等多个属性均可设置，自由度较高。</p>
<h2 id="toc-8">八、文案规范</h2>
<h3>8.1 文案是什么</h3>
<p>文案是我们的产品与用户交流的最基础最简单的沟通工具。文案存在于产品的各个地方，例如按钮文案告诉用户按钮的作用，轻提示文案告诉用户反馈结果。对于新用户来说，文案肯定比图标易理解，另外一方面，文案更不容易产生歧义，例如一个图标可以会有多种意思，而文案相对更精确。</p>
<h3>8.2 文案规范的重要性</h3>
<p>伴随着B端的业务功能的快速迭代，由于设计师、产品经理的水平、文案风格、对文案的重视程度不同，导致系统内部文案积累了很多问题。最明显的问题是同一场景文案不一致，会给用户带来体验的割裂感，增加用户使用产品的认知成本。</p>
<p>而通过构建文案规范，可以规范文案的使用和编写，提高文案的质量，给用户带来连贯一致的使用体验。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/AnKpS4wiN7yXQUHgjGLC.png" alt="超全面！大厂UI设计规范详解！" width="599" height="289" referrerpolicy="no-referrer"></p>
<h3>8.3 文案撰写的原则</h3>
<p>这里给大家介绍一些产品文案通用的一些原则，包括，准确，简洁、用户视角。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/KnoWf2Shx8DRVEdVfYrh.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<p><strong>8.3.1 准确原则</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/SaKansVdU2Hn8pFlzRpV.png" alt="超全面！大厂UI设计规范详解！" width="599" height="289" referrerpolicy="no-referrer"></p>
<p><strong>8.3.2 简洁原则</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/P2TdtowRhUzDjqkAHVb8.png" alt="超全面！大厂UI设计规范详解！" width="599" height="284" referrerpolicy="no-referrer"></p>
<p><strong>8.3.3 用户视角原则</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/z3N2P78Do21QoWAsQVFV.png" alt="超全面！大厂UI设计规范详解！" width="599" height="275" referrerpolicy="no-referrer"></p>
<h3>8.4 落地</h3>
<p>一般情况下，文案没有专门的人来负责，国外可能会有“UX Writer” 这样的专门职位来负责，在国内一般会交给体验设计师来负责。</p>
<p>文案规范的落地分为四步：</p>
<ol>
<li>遍历页面，列出所有的文案</li>
<li>梳理相同或相似场景的文案，将文案归类整理</li>
<li>根据实际情况制定产品文案的原则，并撰写一部分典型场景的文案。</li>
<li>输出文档，包含文案撰写原则及典型场景的文案。</li>
</ol>
<p>九、组件库</p>
<h3>9.1 组件库是什么</h3>
<p>组件库相当于乐高的一个个积木，通过组件的拼搭可以迅速搭建出一个页面。通常我们将组件库分为基础组件和业务组件两大类，前者是系统通用组件（图标/按钮/输入框等），后者是由业务决定的相对更复杂的组件模块。</p>
<p>而对于B端产品和C端产品，二者的组件库又有些许差异。</p>
<p>C端的组件库更追求极致的交互和视觉体验，因此需要考虑视觉、性能、实现、兼容性，另一方面，C端会根据活动、节日切换不同的主题，也要考虑组件视觉上的个性化扩展。</p>
<p>对于B端而言，组件库更看重可复用性和稳定性，保证可以支持业务快速迭代。另外B端会涉及到各种各样的数据录入与展示，因此相对更高的要求是大而全，覆盖面广。</p>
<h3>9.2 如何做组件库</h3>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/N6RexCD5GRLVnFll6Ulh.png" alt="超全面！大厂UI设计规范详解！" width="599" height="250" referrerpolicy="no-referrer"></p>
<p><strong>9.2.1 确定组件库的内容</strong></p>
<p>新产品：对于新产品来说，业务体量较小，较难抽取共性，组件也不全面，因此较好的方式是参考大厂的组件库确定要做哪些组件，它们的相对成熟，参考价值较高。</p>
<p>成熟产品：对于已经成熟的产品来说，我们可以直接遍历页面，穷举出所有用到的组件，除基础组件外，提炼出复用率高的业务组件进行结构化和组件制定。</p>
<p><strong>9.2.2 搭建每个组件</strong></p>
<p>以警告提示（Alert）为例，演示单个组件的建立方法。</p>
<p><strong>1. 定义组件</strong></p>
<p>根据业务定义警告提示的使用场景，警告提示用于重要信息的提醒，采用非浮层的方式展现在页面顶部，被动出现，且不会自动关闭。</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/eGDhOsJoluYyXablqX9z.png" alt="超全面！大厂UI设计规范详解！" width="597" height="367" referrerpolicy="no-referrer"></p>
<p><strong>2. 拆分组件</strong></p>
<p>这一步是将组件拆分为元件。对警告组件进行拆分后得到如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="超全面！大厂UI设计规范详解！" src="https://image.yunyingpai.com/wp/2022/01/dSEl0GSTBdLtsWyWmq26.png" alt="超全面！大厂UI设计规范详解！" width="600" height="397" referrerpolicy="no-referrer"></p>
<p><strong>3. 重组输出</strong></p>
<p>根据业务场景，我们把各个元件重组为组件，建成组件集，并定义各种组件的使用规则。</p>
<p><strong>9.2.3 输出文档并替换到产品中</strong></p>
<p>在组件库建立完成后，只有在日常设计中真正使用组件库，提高组件库在设计稿中的覆盖率，才能真正达到组件库的效果。这就要求我们要输出一份完整的组件库描述文档，在团队中进行推广，加强设计团队的公用意识。另外，我们还要与开发工程师配合逐步完成现有页面的组件替换。</p>
<p><strong>9.2.4 定期维护组件库</strong></p>
<p>组件库的内容并非一成不变，而是在不断地更新，以保证所包含的组件都是最新和有用的。与其他数据一样，组件也会有增删改。</p>
<p>增：当有新的组件产生时，我们需要通过判断它的拓展性和复用率，以确定是否将它入库。</p>
<p>删：随着产品的不断升级迭代，如果某个组件已经不用或复用率很低时，我们可以考虑是否要将它删除。</p>
<p>改：不可避免的，组件会随着业务而进行升级，我们可以通过数据埋点和A/B test的方式来确定某个组件是否要进行改动。</p>
<h2 id="toc-9">十、大厂设计规范推荐</h2>
<h3>10.1 PC端设计规范</h3>
<p><strong>1. Ant Design</strong></p>
<p>Ant Design是由蚂蚁集团体验技术部经过大量的项目实践与总结，逐步打磨出来的，基于「自然」、「确定性」、「意义感」、「生长性」四大设计价值观，通过模块化解决方案，降低冗余的生产成本，让设计者专注于更好的用户体验，是非常完整的一套设计规范。</p>
<p><strong>2. Zent</strong></p>
<p>Zent是有赞 PC 端 Web UI 规范的 React 实现版本，提供了一整套基础的 UI 组件以及常用的业务组件。通过 Zent，可以快速搭建出风格统一的页面，提升开发效率。目前有 50+组件，这些组件都已经在有赞的各类 PC 业务中广泛使用。</p>
<p><strong>3. Element</strong></p>
<p>Element是由饿了么公司前端团队开源一套为开发者、设计师和产品经理准备的基于 Vue 2.0的组件库，提供了配套设计资源。</p>
<p><strong>4. AT-UI</strong></p>
<p>AT-UI 是一款基于 Vue 2.x 的前端 UI 组件库，主要用于快速开发 PC 网站产品，在众多的的组件库中，AT-UI 属于视觉风格比较清新的一款。</p>
<h3>10.2 移动端设计规范</h3>
<p><strong>1. Vant</strong></p>
<p>Vant 是有赞前端团队开源的移动端组件库，于 2017 年开源，已持续维护 4 年时间。Vant 对内承载了有赞所有核心业务，对外服务十多万开发者，是业界主流的移动端组件库之一。目前 Vant 官方提供了 Vue 2 版本、Vue 3 版本和微信小程序版本。</p>
<p><strong>2. NutUI-JDL</strong></p>
<p>NutUI-JDL 是一套基于京东物流视觉规范的移动端组件库，包含了36+高质量组件和详尽的文档和实例。</p>
<h2 id="toc-10">十一、结语</h2>
<p>本次的分享到这里就结束了，希望可以对大家有帮助。由于文章字数较多，笔者几经修改，仍不免有疏漏错误之处，如发现错误，请读者于评论区或私信指出，不胜感激。</p>
<p> </p>
<p>作者：JIN石为KAI；公众号：MICU设计</p>
<p>原文链接：https://mp.weixin.qq.com/s/DfjWSmsLBS15StV8p7feHw</p>
<p>本文由 @MICU设计 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
                      
</div>
            