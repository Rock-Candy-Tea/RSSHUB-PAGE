
---
title: '从_海外维修系统_项目，解析B端产品设计（上）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q6PaHEgfQkNwGg9r47T7.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 27 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q6PaHEgfQkNwGg9r47T7.jpg'
---

<div>   
<blockquote><p>编辑导语：B端产品与C端产品的设计有所不同，在初始阶段，B端产品的设计便需要考虑到整体模块的设计，避免因后续过大幅度改动导致的用户操作不便或用户流失。本篇文章里，作者结合终端维修系统搭建案例，总结了B端产品的设计策略，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5113203 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q6PaHEgfQkNwGg9r47T7.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>近两年B端产品得到关注度越来越高，相关的比如 ERP、CRM、后台、中台等设计也出现在UI设计师的工作中，那么如何去设计B端产品，以及它与C端产品的设计有什么不同。结合我最近完成的一个终端维修系统来和大家做一个简单的分享，希望能够帮助到你。</p>
<p>首先我们要确认一点，相较于C端产品，B端在拿到PRD文档开始，就要从整体宏观的角度去考虑每一个模块，以及各个模块间的衔接。所以就要求我们对所要执行的项目做到了如指掌的地步，记住“你”是除了产品经理外最熟悉各个功能的人。</p>
<h2 id="toc-1">一、项目背景</h2>
<p>我司作为非洲第三大视频运营商，海外产品主要以机顶盒、智能电视、数字电视一体机为主。每年销售量达百万级别，后期的维修数量也相对巨大。海外落后的管理导致维修数据仍以Excel形式按季度上传，为了能对问题设备的总结归纳预判有相对应的数据支撑是该项目的研发原因。</p>
<h2 id="toc-2">二、设计前期准备</h2>
<p>1）根据海外反馈以及产品沟通，本产品的主要解决：</p>
<ul>
<li>维修数据回馈慢；</li>
<li>从不同的维度（大区、国家、员工、设备）查看维修数据；</li>
<li>规范化业务流程。</li>
</ul>
<p>2）用户维度确认：</p>
<ul>
<li>海外事业部经理；</li>
<li>大区经理；</li>
<li>门店经理；</li>
<li>维修人员。</li>
</ul>
<p>3）业务需求，根据问题提出对应的解决方案，再根据不同的角色维度，定义对应的使用权限：</p>
<ul>
<li>海外事业部总经理：泛非所有数据、大区维修数据（可切换筛选）、维修率、修复率、单一设备的维修情况（可筛选）；</li>
<li>大区经理：大区维修数据、门店维修数据、维修率、修复率、单一设备的维修情况（可筛选）；</li>
<li>门店经理：自家门店维修数据、维修率、修复率、单一设备的维修情况（可筛选）、设备入库、设备出库；</li>
<li>维修人员：自家门店维修数据、维修率、修复率、单一设备的维修情况（可筛选）、维修数据录入。</li>
</ul>
<p>4）使用场景：</p>
<ul>
<li>位置：办公室工位；</li>
<li>设备：PC；</li>
<li>浏览器：Chrome；</li>
<li>语言：中文、英语、葡语（前期适配中英两种语言）。</li>
</ul>
<h2 id="toc-3">三、从产品目标出发，提出解决方案</h2>
<p>B端产品着重解决问题，问题清晰明了，根据问题提出解决方案。</p>
<h3>1. 数据回馈慢（主要针对维修人员）</h3>
<p>采用线上办公，维修人员通过设计的维修系统办公，维修完成一例上传一例。</p>
<h3>2. 从不同的维度（大区、国家、员工、设备）查看维修数据</h3>
<p>定义不同的权重，通过登录名称区分，后台给与授权。</p>
<h3>3. 规范化业务流程（门店经理 and 维修人员）</h3>
<p>门店经理负责每日需要维修设备的入库，维修人员根据入库的设备逐一维修，维修完成提交维修结果，门店经理每日结束后从修好的数据库内批量出库。完成一整套维修流程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q34ufcBqFTHI1ZVjdJFD.png" alt width="680" height="307" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、需求分析</h2>
<h3>1. 基本页面流程梳理</h3>
<p>根据PRD文档，列出功能架构，个人建议架构采用横向树形图；这里面提到一个名词“节点”。</p>
<p>节点：是树状结构当中的基本单位，使用节点可以表示不同数据间的组成关系（从属关系与并列关系）通常节点会分为几类特殊情况。</p>
<ul>
<li>根节点：整个树状结构的开端被称为根节点。一个树状结构一定只有一个根，在思维导图中，根节点就代表着它的开端，用于延展出更多的树状结构，可以理解为产品总和。</li>
<li>子节点：根节点之外的节点被称为子节点。一个树状结构子节点数量是没有具体限制，在树形选择当中是直接展示出来的部分。可以理解为一级导航。</li>
<li>叶节点：没有连接到其他子节点的节点。叶节点属于一类特殊的子节点，它是整个树状结构的最末端节点，在树形选择当中是一个重要的概念，可以理解为二级导航或一级导航下的功能模块。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/1x9cIfwgYufAIQNkgxc7.png" alt width="681" height="317" referrerpolicy="no-referrer"></p>
<p>当然，现实中的功能架构要比上面的图例中复杂得多，但只要你理清楚树状架构，基本上我们的页面基本模块间关系就梳理好了。</p>
<h3>2. 针对问题，出解决方案</h3>
<p>这一步是项目中最关键的，我的工作步骤是：</p>
<ol>
<li>深入确认问题，详细了解该功能；</li>
<li>根据自己以往的经验绘制出方案原型；</li>
<li>与用户（使用者）沟通该方案的可行性，听取对方意见（也可以是产品经理）；</li>
<li>缝缝补补最终确认。</li>
</ol>
<p>给新手一个建议：多去大厂的开源B端组件库寻求解决方案。例如：AntDesign、DevUI、Portal、LEGAODesign等。</p>
<p>关于需求这部分，不是本期重点，我之后会专门写一篇文章讲述需求分析。</p>
<h2 id="toc-5">五、合理的设计系统，适应多角色、多维度用户</h2>
<p>B端产品相较于C端产品，在设计理念、交互方式、视觉表现上面有很大的不同，B端产品组件化、栅格化的需求相较于C端产品更为重要。</p>
<h3>1. 导航样式</h3>
<p>网格系统确定前，首先要确定导航样式；常见的B端导航样式有3种：横向式、纵向式、横纵式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RpimGa0q85xmJqR8CoSY.png" alt width="683" height="371" referrerpolicy="no-referrer"></p>
<p>考虑维修系统的使用场景（办公室对操作效率、专注度有要求）、未来的内容承载力（不会很复杂，但也会增加导航）、复杂程度选择纵向式导航，进而去确定网格系统。</p>
<h3>2. 网格系统</h3>
<p>建立网格系统之前，我们首先要了解市面上的主流浏览器的尺寸：1440*900、1366*768、1920*1080；1920*1080多为24寸以上显示器，海外本土条件不允许，删除；最终选择占比较高的1440*900。</p>
<p>浏览器无高度限制，但我们在设计的时候尽量考虑在一屏内展示完全，去掉浏览器顶部导航占据的位置，剩余高度在700~760之间，间距（水槽）按8X像素、列数为网页版常用的12C；依此来建立网格系统。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/l0yGzUcdNdAf6Lzd7bpX.png" alt width="680" height="499" referrerpolicy="no-referrer"></p>
<p>注：具体采用多少列网格，可根据原型图来确定。基本结构在交互原型阶段可以大致出来，所以在绘制原型图的过程中也要认真对待。</p>
<h3>3. 色彩系统</h3>
<p>B端设计非常依赖于设计系统，好的颜色定义，能帮我们设计出一些更加统一、舒适、层级分明、可读性强的界面。</p>
<p>主色：是我们系统的代表颜色，一般与品牌色相关联（蓝色#0A5CFF）。</p>
<ul>
<li>主色的选择需要尽量选择冷色系，这是为了避免用户长时间使用带来视觉疲劳；</li>
<li>避免与错误、警告颜色冲突；</li>
<li>在亮色模式下，饱和度和亮度不低于70。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DSgJIJeJOTjKGP7BVXSn.png" alt width="681" height="360" referrerpolicy="no-referrer"></p>
<p>根据主色制作出24色带，进而提炼出12色带作为标准色，12色带的提炼原则：将颜色相近的删掉，不符合品牌调性的删除，不符合产品性质的删除。</p>
<p>网上有很多生成色板的网站，工作中为了方便可以直接在网站上生成。但小编希望大家能够理解色板的制作原理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/q5xE4PsPcYLumnMnAn9a.png" alt width="683" height="433" referrerpolicy="no-referrer"></p>
<p>色板包含120个有彩色+12个中性色，作用不同，使用情境不同。</p>
<p>中性色主要被大量的应用在界面的文字部分，此外背景、边框、分割线等场景中。</p>
<h3>4. 文字</h3>
<p>我们的用户通过文本来理解内容和完成工作，科学的字体系统将大大提升用户的阅读体验及工作效率。</p>
<p>关于字体默认使用系统字体，在设计时也可以提供一套我们的品牌字体，但字体要始终保持良好的易读性和可读性，体现了友好、稳定和专业的特性。个人建议浏览器默认字体就可以，无需费力去挑选合适的字体。</p>
<p>字体的字号、字重、行高直接参照AntDesign的设计规范就可以。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/c9GgBtwokoeL2fu6pJ3M.png" alt width="679" height="255" referrerpolicy="no-referrer"></p>
<p>关于字重方面，以regular 和 medium 的两种字体重量为主。</p>
<p>关于文字颜色与背景色搭配时，要做到清晰可读，可在：https://color.review 测试，至少要达到AA的标准。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/e9Mi9Bc08HiTRjt6BdaM.png" alt width="681" height="394" referrerpolicy="no-referrer"></p>
<h3>5. Icon</h3>
<p>图标是将某个概念转换成清晰易读的图形，以降低用户的理解成本，提升界面的美观度为目的。由于B端在设计中图标往往只占了很小的比重，在调用时也会被缩到比设计稿小很多倍的尺寸，设计时要注意简单、清晰、准确。</p>
<p>因为屏幕分辨率的不同，没有规定最小操作热区。但受到文字（Chrome浏览器中限制最小的字体为12px）的限制，12px渐渐成为大家公认图标操作热区的最小值。16px、24px、32px都是PC端常见的图标尺寸。</p>
<p>这里我们采用48*48作为图标的设计尺寸。由此可制作出Keyline。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5fdT1X4ywTRCn04w1O69.png" alt width="684" height="323" referrerpolicy="no-referrer"></p>
<p>Icon的制作需保证icon的初始结构，采用点线面（圆、方、三角形）构成。不做夸张处理，在一致性方面：图标的一致性体现在对重复性元素的的管理、元素间的比例上面。</p>
<h3>6. 容器</h3>
<p>容器为全局样式中的一种类别，用于盛放不同组件（文字、icon等）的载体，我们可以理解为“盒子”。常见的容器有：组件的背景、按钮的各种状态、消息反馈的提示等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oWyOVamv3tYOWOFL6rPl.png" alt width="681" height="241" referrerpolicy="no-referrer"></p>
<p>注意其中的颜色运用要选取色板中的颜色，不能违背用户认知。</p>
<ul>
<li>红色：失败提示、警示按钮；</li>
<li>橙色：异常操作；</li>
<li>绿色：成功、完成；</li>
<li>蓝色（主色）：提示、可执行操作。</li>
</ul>
<p>注：在前景色与容器搭配时，注意前景色的清晰度问题，可在https://color.review上面测试。</p>
<h3>7. 阴影</h3>
<p>阴影来源于现实生活的反映物体与物体之间距离。在UI界面中，我们往往通过模拟元素的投影来表示元素之间的高度距离与层次关系。有上、下、左、右四个方向，依靠XY的数值调整。</p>
<p>阴影可根据不同的应用场景分为四种：默认投影、悬停投影、弹框投影、文字投影；根据不同场景设置不同的投影参数。</p>
<p>Y轴距离：文字 < 默认 < 悬停 < 弹框。</p>
<p>下图为：AntDesign的向下投影参数，可供参考。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/LmwovFU79OKESwINaa6r.png" alt width="681" height="382" referrerpolicy="no-referrer"></p>
<p>随着近年来弥散投影的广泛喜爱，这里是否适合，设计师可自己尝试。</p>
<p><strong>为了更为连贯的讲解，也为了能让大家慢慢消化，以上为B端设计界面前的准备内容，下一篇《从“海外维修系统”项目，解析B端产品设计（下）》将为大家详细讲解组件搭建、控件设计的问题。谢谢！</strong></p>
<p> </p>
<p>本文由@肥猫豆豆 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5098796" data-author="1269505" data-avatar="https://static.woshipm.com/APP_U_202108_20210825092344_6746.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            