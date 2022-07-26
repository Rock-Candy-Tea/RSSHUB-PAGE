
---
title: 'B端交互｜如何制定B端项目全局框架'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/07/Sa8x10bNnVCegTQCU6xx.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 26 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/07/Sa8x10bNnVCegTQCU6xx.jpg'
---

<div>   
<blockquote><p>编辑导语：交互设计本质上就是设计产品的使用方式的过程，“如何才能做出合理的B端交互决策”是很多人都在思考的问题。在这篇文章里，作者聚焦具体的实战场景，分享了一些自己做B端交互设计的经验，一起看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-842848 aligncenter" src="https://image.yunyingpai.com/wp/2022/07/Sa8x10bNnVCegTQCU6xx.jpg" alt referrerpolicy="no-referrer"></p>
<p>这阵子想了想关于交互知识的分享，还是应该要拓展成一整个系列的内容，包含各类组件、控件和行为的解析。</p>
<p>基于我的分享习惯，我会尽量避免使用太过理论还是空泛的方式进行讲解，而是聚焦具体的实战场景，帮助大家理解如何做出合理的交互决策。</p>
<h2 id="toc-1">一、交互的全局框架是什么</h2>
<p>交互设计本质上就是设计产品的使用方式的过程，账号怎么填写，表单怎么导出，数据怎么筛选，列表怎么排序等等……针对每个功能的使用方式，都可以花很长的时间去考虑其合理性。一个项目的交互，就是这个项目所有功能使用方式的总和。</p>
<p>那设计师如何开始项目的交互设计？直接进入细节，开始跟着原型制定输入框的状态，下拉菜单的展开逻辑吗？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/dH64VLP21YnfT3MuMWu1.png" width="987" height="595" referrerpolicy="no-referrer"></p>
<p>这样肯定是不行的，项目的交互内容又多又杂，设计师会很快陷入这些细枝末节中疲于奔命。头疼医头脚疼医脚，容易造成项目细节缺乏统一性，前后矛盾，体验割裂。</p>
<p>所以，理解项目交互设计的正确思路，就要知道在项目中有哪些交互内容，它们对应的层级和设计对象是什么。</p>
<p>在这里，我把需要设计的交互对象拆分成4个种类，它们从大到小依次为：</p>
<ol>
<li>全局框架：项目的主要模块排版和布局，产品使用的主要依据和步骤</li>
<li>功能流程：需要较多操作步骤才可以完成的一个完整的用户使用目标</li>
<li>组件操作：一些复杂模块、业务组件的完整操作方法和状态</li>
<li>控件使用：基础控件元素的操作方法和状态</li>
</ol>
<p>我们先围绕在全局框架这个类型进行解释，什么是项目的主要模块排版和布局，以及为什么全局框架可以决定产品的主要使用依据和步骤。</p>
<p>比如大家都用过 Adobe 的软件，应该会有个感觉，就是熟悉了其中一款后用下一个，立马就能上手，完成一些最基本的操作。而如果不是 Adobe 系列的软件，用起来感觉就感觉非常别扭，往往要从头开始学起，比如对标 PS 的 Affinity Photo、Pixelmator。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/mRe3VcVdm7Mww0l39GJM.png" referrerpolicy="no-referrer"></p>
<p>为什么会出现这样的反差？就是因为 Adobe 尽可能统一了自己生态内的软件全局框架，操作方式，让全家桶用户可以用最快的方法适应不同的软件。</p>
<p>包括顶部的属性栏，左侧的工具栏，中间的标签栏、创作区域，右侧的不同工作窗口排列形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/iirvW9quXohUps98tJlH.png" referrerpolicy="no-referrer"></p>
<p>除了主要界面的布局框架外，还包含一些二级窗口的框架结构也是统一和固定的。比如打开 PS 内的首选项设置和属性设置窗口，和其它几个软件的属性设置窗口几乎一致。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/ykmFOnzNvvkHVcOXT0r1.png" referrerpolicy="no-referrer"></p>
<p>而在 Affinity 中，软件首选项设置就没有使用左侧导航，而是类似 Mac 通用设置的快速入口分层模式，用惯了 Adobe 再换这个就会有股说不出的别扭。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/Hv3Xdwt2ZzubgmdzzqVn.png" referrerpolicy="no-referrer"></p>
<p>可能有同学有疑问，Photoshop 并不是只有这几种窗口，其它窗口不就样式和上面这类不一样嘛？那是因为窗口的框架肯定是要考虑功能和场景的，即使使用了多种窗口类型，那也是有规律的应用在操作方式相近的场景中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/hjZvAYbw5WWOfBhsgoLH.png" width="990" height="323" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/J4FtVl8xyrxDUoQbIyZf.png" width="978" height="339" referrerpolicy="no-referrer"></p>
<p>再回想一下 PhotoShop 的基本操作流程，就是在创建文件以后，通过左侧工具添加图层元素到中间画布区域进行排版，再在右侧属性栏中调节画布对象的图层顺序、属性。</p>
<p>PhotoShop 作为平面领域中的独角兽，直接影响了绝大多数同类设计软件的框架结构和布局方法。因为绝大多数设计师学习设计的入门软件都是 PS，想要让用户更快上手自己的软件，那就应该顺着他们已经习惯的方式来。</p>
<p>所以，从 Sketch 开始，它的框架和操作流程都和 PhotoShop 高度相似，再之后的 Adobe XD、Figma、即时设计等，都应用了几乎相同的全局框架，所以你只要掌握其中一个就能立马熟悉其它软件的使用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/QS26hLlafAdhMmfHXUjm.png" referrerpolicy="no-referrer"></p>
<p>而当实际功能和 UI 设计软件高度相似的其它几个 “办公应用” 结构框架不同时，上手就变得异常的困难和别扭。比如 Axure、Keynote、PowerPoint，先学了设计软件再去学这几个软件的同学一定深有感触。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/ByeBNSli55SrzJMC3UmR.png" referrerpolicy="no-referrer"></p>
<p>而其它行业的软件，如果没有一个具备绝对主导性的产品作为标杆，那么每家公司的产品框架就各不相同。比如 3D 建模软件中的 C4D、Blender、犀牛，视频剪辑工具中的 Pr、Finalcut、达芬奇，你就是熟练掌握其中一款，对专业术语和必要功能逻辑了如指掌，也需要通过基本教学才能掌握其它同类软件。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/mrR78mLcUBZdZfwC6EjL.png" width="992" height="255" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/KMZreP4G4iNZHoAqbshQ.png" width="996" height="256" referrerpolicy="no-referrer"></p>
<p>这就是框架带来的作用，它是软件使用方式和操作流程的主要依据，其它细节的交互和操作都是附着于全局框架下的子集内容。之所以交互设计要从全局框架开始，原因就是设计师要：</p>
<p><strong>先确定产品整体操作的方式，再去考虑按钮和表单那些细节的处理。</strong></p>
<h2 id="toc-2">二、B端产品的全局框架拆解</h2>
<p>虽然前面举例的都是软件案例，但只要仔细留意，你们就会发现网页端管理系统的操作框架和一般软件别无二致。只不过相比较五花八门的专业软件来说，B 端管理系统的操作框架模式经过了长期的演化形成了固定的几种套路。所以网上找到的管理界面案例，看起来只是围绕几个固定的布局翻来覆去的改颜色和图标。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/qimPuTk3IN8nbrldLjGe.png" referrerpolicy="no-referrer"></p>
<p>虽然它们看起来都很像，但依旧包含很多交互细节是需要设计师留意和制定的，不是简单照搬就能设计出符合项目需要的全局框架。</p>
<p>所以，交互的全局框架到底怎么设计？</p>
<p>它不是一个个体，而是一个由多个组件、页面类型、适配方式组成的合集概念。想要有效制定，就需要先了解合集中包含的要素有哪些，以及它们的基本特点。</p>
<h3>1. 全局框架中的组件</h3>
<p><strong>在全局框架的范畴中，包含的组件模块类型可以分成两个大类，全局组件和浮层元素。</strong></p>
<p>全局组件是指在项目多数页面中都会存在并进行交互的组件，功能往往和当前页面没有直接联系，比如路径跳转、色彩切换、快捷操作等。</p>
<p>而包含的浮层元素，本质上也是全局组件，只是它们的共性是不会默认展示，需要被特定条件触发才能被感知。比如断网提示、删除确认、侧边抽屉等都是全局化的浮层要素，也是需要在前期做好规划的内容。</p>
<p>下面就针对这个两种类型的组件一一展开解释。</p>
<p><strong>（1）全局组件</strong></p>
<p><strong>a. 导航栏</strong></p>
<p>导航栏不仅仅是 B 端管理系统，也是网站设计中最重要的组件。优秀的导航栏可以清晰的展示项目的页面层级结构，帮助用户高效的访问目标页面。全局框架制定的一步，就是根据项目的具体情况，选择合适的导航类型。</p>
<p><strong>导航栏主要使用上方、左侧、混合型三种布局形式：</strong></p>
<ol>
<li>上方导航：适合选项内容较少，预留更多横向空间内容区域。</li>
<li>左侧导航：适合选项、层级较多的情况，方便折叠和上下滚动。</li>
<li>混合导航：适合需要有效区分不同功能区块的场景。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/rmIx2yFEayBLg07aoBOg.png" referrerpolicy="no-referrer"></p>
<p>确定导航栏的类型，还需要确定导航的操作逻辑，包含几级菜单，默认、展开、选中、关闭的交互。</p>
<p><strong>b. 顶部栏</strong></p>
<p>除了导航外，另一个基本必备的组件，就是顶部栏，除了放最基础的用户和设置选项外，它的角色定位要根据需求决定，最常见的包含下方几种：</p>
<ul>
<li>标题栏：主要用来展示页面标题、副标题，或者面包屑控件。</li>
<li>工具栏：包含比较多的操作要素，如搜索、新增、邀请、消息管理等。</li>
<li>菜单栏：包含较多针对当前页面/模块的菜单选项和内容切换操作。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/iDDTduBerJPG1tAhQQXA.png" referrerpolicy="no-referrer"></p>
<p>当然，以上几种情况并不是绝对的。设计师需要根据项目的实际需求出发，去梳理项目包含哪些全局控件或操作，然后再决定如何分配到导航或者顶部菜单上，而不是先定义菜单的类型再往里面填内容和字段。</p>
<p><strong>c. 页面标签栏</strong></p>
<p>页面标签栏是一个类似浏览器标签栏的组件，用来展示和关闭当前项目内打开的页面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/5XeQABtTzLfCunhrdbKe.png" referrerpolicy="no-referrer"></p>
<p>标签栏的使用在远古时期的 B 端项目应用非常普遍，因为已经入土的 IE 浏览在那个年代是没有页面标签功能的，导致开启多个页面的切换非常麻烦。</p>
<p>随着浏览器标签的普及，它已经不适用于多数 B 端项目，但依旧有一小部分项目是需要结合它的优势才可以更好的提升操作效率。</p>
<p>在一些需要持续打开和来回切换页面的项目，如客服系统、财务审核、合同审批，因为打开新页面仅仅需要加载内容区域而不是全局，没有新建窗口后的空白页面加载过程，就能带来更好的体验。</p>
<p><strong>d. 内容模块</strong></p>
<p>内容模块是用来容纳和显示页面相关内容的模块，这是个被很多人忽略的组件类型，包含模块标题栏和操作区域。</p>
<p>一个成熟的 B 端项目会统一制定内容模块的组件结构，保证大量页面和模块之间样式的统一性。比如下面的模块案例。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/zstqnsTBav0KHrC0siTp.png" referrerpolicy="no-referrer"></p>
<p>如果只是简单做个标题再统一间距参数，那么这个组件也就没必要在这里提了，因为这仅仅是设计问题而不是交互问题。内容模块的制定是为了尽可能考虑各种内容场景，并进行统一处理。</p>
<p>例如要应用一级分页标签、多层级分页标签、操作按钮、内容折叠等。考虑的越全，后面处理起来越工整，否则就像下方淘宝卖家端千牛的案例一样，损害用户的体验和操作效率。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/07/cLr0HxKhZuobNGzbgk7u.png" referrerpolicy="no-referrer"></p>
<p>内容模块是很难在初期一口气全部定完，不仅需要产品经理前期给出详尽的需求和产品原型，还依赖设计师自身的经验判断。</p>
<p>所以，它的制定流程是在前期先根据掌握的信息制定出最初的版本，然后在完成后续的页面中逐渐进行补充、优化并替换。</p>
<p> </p>
<p>作者：酸梅干超人；公众号：超人的电话亭（ID：Superman_Call）</p>
<p>本文由 @超人的电话亭 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash ，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5540593" data-author="840505" data-avatar="https://image.woshipm.com/wp-files/2021/07/JCf8Fx1LZhUm0zOfxAw4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            