
---
title: '如何快速搭建C端产品的设计系统'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/crxsHUuHRqMLkrEBkz0f.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 31 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/crxsHUuHRqMLkrEBkz0f.jpg'
---

<div>   
<blockquote><p>编辑导语：在产品搭建中，设计师需要针对产品定位、前端开发、用户体验等方面来进行产品设计方案的确定。那么产品设计应当从哪些方面着手搭建C端产品设计系统？本文作者结合其自身经验、较为系统地总结了快速搭建C端产品设计系统的方案，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4629496 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/crxsHUuHRqMLkrEBkz0f.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>文章主旨在于拆解和分析设计系统中基础要素所制定规则的原由以及其合理性，了解设计系统基础要素的搭建依据从而更灵活地为其所用。</p>
<p><strong>前期资料整理</strong></p>
<p>搭建自研产品的设计系统前需要做大量的工作，首先要针对产品定位来确定设计系统的MVP的范围，这样来保证搭建设计系统的完整性；其次再学习和借鉴已有、成熟的设计系统；最后要根据现有的团队、产品规模和人力来推进工作，需要设计师和前端开发紧密配合，尽可能多地同时更新内容。</p>
<p>前期梳理其他设计系统整理表单抽取部分，链接如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/W5RJhXwWHNrZkI36rmv6.png" alt width="756" height="564" referrerpolicy="no-referrer"></p>
<p>备注：以上仅为个人从产品的业务维度理解后的分类，仅供参考。</p>
<p><strong>设计系统存在的价值的定义：</strong></p>
<ul>
<li>解决特定的设计问题，快速输出可复用的产品界面；</li>
<li>总结获得成功的使用体验，为用户持续提供友好体验；</li>
<li>便于产品在多终端的管理。</li>
</ul>
<p><strong>介入的契机</strong></p>
<p>产品由0到1后、且开始进入有序又紧凑的迭代时考虑设计系统才是比较合适的。原因有二。</p>
<ol>
<li>已过磨合期的团队、工作流程和业务的稳定性是搭建设计系统的前提。</li>
<li>此阶段是产品快速成长阶段，业务模块和使用终端的丰富，对设计工作的挑战会大大加强。设计工作横向关联上下游以及设计师多人协作的工作衔接，纵向关系到设计品质在细节的把控和精进，特别需要有系统的设计规则统一指导设计工作的进行。</li>
</ol>
<p><strong>设计系统的内容</strong></p>
<p>在此次设计系统的研究方向主要在移动端，为产品设计过程提供设计依据和规则指导。</p>
<p>设计系统（Design system）从以下五个部分来构成：</p>
<ol>
<li>设计原则（Pprinciples）；</li>
<li>基础元素（通常指UI Design elements）；</li>
<li>组件库（Components of organisms）；</li>
<li>模版（Templates）；</li>
<li>模式（Patterns）。</li>
</ol>
<p><strong>具体搭建设计系统的方法和内容：</strong><strong>怎样去获得具有合理性元素的方法以及部分设计系统的内容。</strong></p>
<h2 id="toc-1">一、设计原则</h2>
<p>设计原则需要依据产品定位来设定，不同行业属性的产品有携带不同的产品基因，因此在初期设定时会以产品本身的业务为基础，来探索系统的合理性、易操作性、高效、美观。使用最基础或通用的一些设计原则做引导。</p>
<h2 id="toc-2">二、基础元素 Design elements</h2>
<p>统一画版——在不同环境中尺寸参考如下表，我们设定主要的开发尺寸：375*667，在Sketch文件中一倍图的基准尺寸中，1Px=1Pt，视觉设计可与开发尺寸保持一致性。</p>
<p>导出文件原则统一为Sketch导出2X图交付给开发，所有元素的设定尽量保持在不佳条件下仍然可以被用户使用为前提。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/XVSfUJ4zzDtrUsckiHkt.jpeg" alt="设计系统的研究与整理（中）" width="687" height="168" referrerpolicy="no-referrer"></p>
<p>基础元素框架：包含字体、色彩、图标、空间、微动效。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/vXNGWhkIBfQw1JVKFDMS.jpeg" alt="设计系统的研究与整理（中）" width="685" height="524" referrerpolicy="no-referrer"></p>
<h3>1. 元素——字体</h3>
<p><strong>设计依据</strong></p>
<ul>
<li>行宽（Measure or line length）每行文本的宽度；45个<最佳行宽的字符数<75个；阐述一个句子（包括字母和空格）阅读最舒服在66个字符，最多不超过80个字符。</li>
<li>行高（Leading or line height）文字基线之间的距离；行高=基线高度（basicline-height）/字体大小 行高 =（1.5至2）* 字大小（依据W3C的WEB内容可访问性指南，设置段落间距）。</li>
<li>字母间距（Tracking or letter spaceing）字母之间的间距，影响文本的密度；其他适用设计原则：行宽越大，行高也应越大；无衬线字体比衬线字体需要更大行高；粗字体比细字体需要更大行高。</li>
</ul>
<p><strong>1）字号&行高</strong></p>
<ul>
<li>分级：分级定义内容如何被阅读，通过字号来体现内容的层级，使得要表达的重要信息可以快速被感知。</li>
<li>分度：根据分级的内容给出对应整体的字号、行高，此处行字号以2递增的数列，行高采用（1.5-2）*字号，具体数值根据实际视觉效果确定。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/iui5sHS9EKyzruSlgXhx.jpeg" alt="设计系统的研究与整理（中）" width="699" height="122" referrerpolicy="no-referrer"></p>
<p><strong>2）色值&功能</strong></p>
<p>在选定颜色色相后，可以根据无障碍设计原则，来选择合适的颜色色值。从功能优先的角度出发首要考虑人眼对色彩的可识别度。</p>
<p>在WCAG 2.0（Web content accessibility guideline） 中将颜色对比等级分为3种，A级、AA级、AAA级。等级越高意味着颜色的对比度越高，呈现出来的视觉压力越大。</p>
<ul>
<li>A级：对比度3:1，是普通观察者可接受的最低对比度；</li>
<li>AA级：对比度4.5:1，是普通视力损失的人可接受的最低对比度；</li>
<li>AAA级：对比度7:1，是严重视力损失的人可接受的最低对比度。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/xBMcHF6XN4GE819cGyjf.jpeg" alt="设计系统的研究与整理（中）" width="686" height="101" referrerpolicy="no-referrer"></p>
<p>可以借助以下工具获取符合无障碍设计原则的色彩：</p>
<ul>
<li>色彩对比度检测工具：对已有或即将优化选定的色彩取值进行检测，从结果数值看是否符合要求。附工具链接：https://webaim.org/；http://t.cn/EVo4rxU</li>
<li>色彩推荐色值工具：此工具可以根据输入的色值进行临近色的推荐，设计者可以从推荐中安全选出符合要求的颜色。附工具链接：https://contrast-finder.tanaguru.com/</li>
</ul>
<p>以下是通过实际项目内字体颜色优化前后的对比：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/D3iSTwWA1Ap6QvEIrhG5.jpeg" alt="设计系统的研究与整理（中）" width="687" height="182" referrerpolicy="no-referrer"></p>
<p><strong>3）字体家族&字重</strong></p>
<p>以iOS系统中常用字体——苹方字体家族为例，字重共6级，分别为：Extralight-极细；Light-细；Regular-常规；Medium-中等；Bold-粗；Semibold-特粗。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/XPcrRh2hJ8fP02lW5QVm.jpeg" alt="设计系统的研究与整理（中）" width="688" height="120" referrerpolicy="no-referrer"></p>
<p>字体家族的选择时需考虑到字体家族的丰富和完整性，部分字体家族字重的类型较少，在选用时需考虑其后拓展性而谨慎使用。</p>
<ul>
<li>移动端建议选择造型宽厚、开发、笔画较粗的字体家族，此类字体在字号很小的时候也都有较好的易读性；</li>
<li>在构建产品的字体规范时，字重的选择建议在3-4个左右，形成粗细对比度从而对应不同信息的视觉重量。</li>
</ul>
<h3>2. 元素——色彩</h3>
<p><strong>设计依据</strong></p>
<p>色彩模式介绍</p>
<p>从原色色彩屏显光学三原色RGB，印刷三原色CMYK；色彩模式：HSB、HSL、RGB、CMYK、LAB、灰度、位图、双色调、索引颜色和多通道等；其中HSB、HSL都是由RGB。</p>
<p>备注：目前常用设计工具Sketch、PS使用的是HSB模式；CSS采用的是HSL模式，在设计中不能直接把HSB的数值直接套用在HSL上。</p>
<ul>
<li>H色相Hue：色彩的质地面貌；</li>
<li>S饱和度Saturation：颜色的浓淡；</li>
<li>B明度Brightness：描述颜色的明暗。</li>
<li>色彩体系：在构建产品色板时，倾向的色阶主色可以从以下色彩体系的色板上选取；日本PCCS、美国Munsell-、德国Ostwald、瑞典NCS。</li>
</ul>
<p><strong>1）色板划分</strong></p>
<p>色彩体系中以调色板为单位目前划分为基础色板、中性色板；使用色彩工具生成色板，例如使用Antdesign中的色板生成工具，先选择好色板的主色，选取颜色时，明确色彩在界面中的使用场景和范围后优先确定色相，再选择饱和度和明度。</p>
<ul>
<li>基础色板：包含由单色色阶、临色色阶等系列色阶构成的色彩系列，部分基础色板会直接采用品牌色。</li>
<li>中性色板：包含黑、白、灰，和由黑白调和的各种深浅不同的灰色系列（补充配色曲线和色阶）。</li>
</ul>
<p><strong>2）配色管理</strong></p>
<p>在设置色彩关系时需要先了解在不同文化定义下对颜色的固有的意义和引起的情绪倾向，然后再了解几种色彩关系，运用色彩关系来指导选择配色。</p>
<p>此处采用HSB模式，H取值范围（0-360）；S取值范围（0-100%）；B取值范围（0-100%）。</p>
<p>色阶的配色流程首先选定色阶内的主色，然后横向衍生出同饱和度和明度临近色的色阶，再从临近色中的单个色彩纵向衍生出此色的单色色阶，最后组成色板系列。</p>
<p><strong>具体配色的基础原则和方法</strong></p>
<p><strong>① 近似色色板配色方案</strong></p>
<p>也称为临色，以一种颜色用作主色，相邻颜色辅助，含有相同的基础色，可以形成低对比度，色相相近的和谐色彩组合；较多用来构成界面整体的氛围。</p>
<p>通过以下三种方法可以得出不同冷暖感受的临近色色阶。</p>
<p>方法一</p>
<p>取色相值H为变量，H数值的梯度决定此色阶的丰富性，即H的取值越接近，色彩之间的对比越弱，形成的色阶微变化越多；由此方法可得出其他近似色配色，如下图所示。</p>
<p>在HSB模式中近似色色阶构成方法如下， 以主色为#ff0000，改变色相，饱和度与明度一致的临色色阶（H值有序改变；S、B值不变），当H的数值按5的倍数增加从H=0到H=50，可以配置出10色的临色色阶，设计者依据所需修改增加的数值范围，获取不同色板：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/x3d2hPtN6GuU0UvEK5vn.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>从上表选取颜色可得出临近色板如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/m6IeYh3y0N67SmCz5z9i.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>举例：以Antdesign中的#f5222d为色阶的主色，使用上述方法改变色相H值，得出饱和度与明度一致的临色色阶（H值有序改变；S、B值不变）。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/ixEgAdRFNZDO92CncYnG.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>从上表选取颜色可得出临近色板如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/SuwMCsYakr78xe3j8WEp.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>以主色为#f5222d，有序改变H、S、B值，分别可得出下图左右两组不同明度的临近色色阶：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/OCJUAGZUVQX4lxXtJvHP.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p><strong>② 单色色板配色方案</strong></p>
<p>选择其中一种颜色为主色，次颜色的色相H值不变。此类型单色的呈现是通过对颜色明度和饱和度的改变所得到，单色色阶的构成方法有三种，根据HSB的色彩模式，如下图中1、2、3。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/KR2Pilm6yQaHVmm0ByyF.jpeg" alt="设计系统的研究与整理（中）" width="687" height="112" referrerpolicy="no-referrer"></p>
<p>根据上图图表1，以主色为#ff0000，在H:0、B:100时，有序改变S的数值，形成以下单色色阶：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/S3F6JkS4HHmxIT7YrONF.jpeg" alt="设计系统的研究与整理（中）" referrerpolicy="no-referrer"></p>
<p>根据图表2，以主色为#ff0000，在H:0、S:100时；有序改变B的数值，形成以下单色色阶：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/xuwnXiOdGao30g8MdtaP.jpeg" alt="设计系统的研究与整理（中）" referrerpolicy="no-referrer"></p>
<p>我以上方法所得的色阶与Antdesign的基础色板中红色色阶进行对比，整体的色彩梯度与Antdesign比较接近，并可以通过调整变量数值之间大小达到对整体色阶的微调。</p>
<p>在实际使用过程中根据环境色还可对单个色值进行微调。在搭建单色色阶时，建议以纯色来作为主色延展其他颜色，以下是用#ff0000，H:0S:100B:100延展出的单色色阶。</p>
<p>（备注：纯手工电脑调色，由于不知道ANTDESIG色板的构成逻辑，只能尝试各种方法后再与其进行对比，这样来校验其方法的可行性，用HBS来调色肉眼可测其结果还是比较接近的。）</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/W6mWsYje0JIC4SR0M7du.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/KBz3tGbP2dSe455ssdSd.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p><strong>③ 不用纯色为主色的情况下</strong></p>
<p>设主色为#f5222d，根据单色色阶的构成方法1、2可得出以下色阶：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/lix8gyqYSyyeTP1nxb3P.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>设主色为#f5222d，根据单色色阶图表3的方法可得出以下色阶：</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/oUEVElsmTDK3hK6trj0P.jpeg" alt="设计系统的研究与整理（中）" width="680" height="102" referrerpolicy="no-referrer"></p>
<p>配色总结：考虑到色彩的冷暖、轻重、虚实所传达的信息后从氛围、情感、意境上选择相对匹配的图片，对图片中的色彩进行提取从而组成一套配色，推荐工具有Eagle。</p>
<p><strong>3）设计系统中的色彩管理</strong></p>
<p>色彩管理参考方法<strong>1</strong>，通过管理在主题中对颜色命名，<strong>推荐在产品级中使用</strong>。</p>
<ul>
<li>主题：每个主题基于特定的主背景色在UI中基于某个色彩调性的颜色值；</li>
<li>命名：在色彩体系中，颜色的角色或用法给出统一命名，与实际色值无关。例如命名为Test-02，在白色主题中作为错误提示可以映射为#de1e28，在黑色主题中可以映射为#ff1818；</li>
<li>职能：颜色的角色或用法，例如完成提示、错误提示等；</li>
<li>色值：颜色的实际样式，例如#da1e28。</li>
</ul>
<p>在以白色为主题的背景下，命名为Test-02用于错误提示其映射的色值为#da1e28；其Test-02不仅可以在同一主题里替换成不同的色值，也可以在不同主题下替换色值。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/413vZmGjZcw19sVu2FJQ.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>色彩管理参考方法<strong>2</strong>，通过职能来管理颜色，<strong>推荐在系统级的平台使用。</strong></p>
<p>以颜色的职能为主来划分，包含以下色彩模块：</p>
<p>Colors\background color\text color\font\fontsize\opacity\line height\spacing\sizing\shadow\time\touch\media query\z-index</p>
<p>在这些分类好的色彩模块内再进行色彩的命名。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/d42gGlJjqC0qK8p4mlfC.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>总结色彩体系的搭建：</p>
<ul>
<li>设定主色；</li>
<li>延展临色和单色色阶；</li>
<li>通过色彩管理方式将确定的颜色进行分类、命名、赋予职能；</li>
<li>后期的维护和更新。</li>
</ul>
<p>附：配色工具推荐</p>
<ul>
<li>https://mycolor.space/</li>
<li>https://uigradients.com/ #CanYouFeelTheLoveTonight</li>
<li>https://colors.muz.li/palette/ffb3bf/8587f2/22aa1b/b7e4ff/0fa87a</li>
<li>https://material.io/design/color/#tools-for-picking-colors</li>
<li>推荐阅读：https://en.wikibooks.org/wiki/Color_Models:RGB,HSV,_HS</li>
</ul>
<h3>3. 元素——空间</h3>
<p><strong>设计依据</strong></p>
<p>空间体系是用于对UI元素的测量、标定和排序，是成为出色设计的关键，其目的是为了设计出灵活、高效、具有创造性和一致性美观的页面排版和布局。</p>
<p>构建空间体系需要先定义基础单位，基础单位是用来创建支持测量空间比例的度量衡。PT与DP分别是对应IOS和Android系统的设计单位，此处以PT为单位，统一使用画板尺寸为375*667。</p>
<p>与平面设计不同的是，在UI产品中有很多不同的屏幕尺寸的用户端，但是通常需要具有相同板式的设计来达到产品的统一，由此可见UI空间体系需要是整体考虑到布局的动态适配和展示。</p>
<p><strong>1）黄金分割在布局中的应用</strong></p>
<p>确定版心，由版心的位置来定义到上下、左右的边距，在设定UI边距的时候需要考虑各应用系统状态栏、固有高度，具体的数据值可以利用黄金分割比例，在以高为667的垂直矩形和以高为375的水品矩形上可以取得以下数值，并通过实例对黄金分割在用户界面中如何使用做出部分展示。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/b1TBLBf2wjCh531Q6hEY.jpeg" alt="设计系统的研究与整理（中）" width="689" height="111" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/EBNJotaFffD7UgcSBTd7.jpeg" alt="设计系统的研究与整理（中）" width="687" height="386" referrerpolicy="no-referrer"></p>
<p>参考方法:</p>
<p>以垂直矩形的数据代入界面，在具体使用黄金分割比例取界面数值时，需要考虑实际的视觉效果，下图为如何在已有界面布局下优化元素的宽高值。同样的方法也常在插画或Banner的布局中应用。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/q3ywZaq4AUSbScXnFGdG.jpeg" alt="设计系统的研究与整理（中）" width="685" height="385" referrerpolicy="no-referrer"></p>
<p><strong>2）空间比例的次序感——网格系统的使用</strong></p>
<p>网格系统在平面设计中用来解决报刊、杂志、画册中图文混排时的效率和美观问题，决定了纸张内部分割，页面设置决定了不同要素的位置。网格赋予图书的连贯性，使其整体看上去更加和谐一致。如果将界面375*667想象成纸张，其页面设置就决定了不同组件和元素之间的位置。</p>
<p><strong>① 解决以图片排版为主的网格方法</strong></p>
<p>1 采用方根矩形（Root rectangles）规划组件尺寸，代入公式A：B=X：A方根矩形可以分为更小的保持原有比例的矩形。</p>
<p>由下图可见，在667*375的界面上所分割形成的为三次方根矩形，每一个新的小矩形和界面都拥有相同的比例。通常在使用版面大的模块布局切割时使用，能够形成多个比例协调的矩形分割。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/zn4VPC5Dxlh3iNcx8EA5.jpeg" alt="设计系统的研究与整理（中）" width="684" height="384" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/ZfGJ5PzD93KiNafdqMEz.jpeg" alt="设计系统的研究与整理（中）" width="684" height="384" referrerpolicy="no-referrer"><br>
<strong>② 解决以文字排版为主网格方法</strong></p>
<p>采用现代主义原则的网格，步骤如下：</p>
<ol>
<li>按照黄金分割比划分两端边距，确定版心；</li>
<li>按照预期的栏数粗略的对版心进行分栏；</li>
<li>用双横线分割栏的高度；</li>
<li>根据整体的文字数量，设定每行字体的数量。45个<最佳行宽的字符数<75个；阐述一个句子（包括字母和空格）阅读最舒服在66个字符，最多不超过80个字符。</li>
<li>根据字高来计算每栏中的间距，行高 =（1.5至2）*字大小 (依据W3C的WEB内容可访问性指南，设置段落间距)。通常文字在手机端中竖屏分栏用得比较少，可以使用在对图文有特殊要求的产品排版中。</li>
</ol>
<p><strong>3）界面内元素与元素之间的空间关系</strong></p>
<p>在大量对当前国内外设计系统中UI空间调研，发现都选择使用8倍数的规则，部分有区分对应的组件模块和文字之间的倍数，比如在Carbon design system中，对组件的空间排版使用布局（Spacing scale）来命名，对文字空间使用间距（Layout scale）来命名。在Material design中被统一使用成Layout，只区别使用8pt和4pt的对应空间系数的梯度。</p>
<ul>
<li><strong>8pt网格规则，</strong>利用8的倍数来计量、设置界面中元素的尺寸以及各自之间的间距大小、宽窄；任何需要自定义的元素数值都是8的倍数，多用于面积较大元素，例如组件与组件、卡片与卡片之间；</li>
<li><strong>4pt网格规则，</strong>多用于图标或小文本块之间。</li>
</ul>
<p>设计这些间距倍率需要根据全局的界面空间来设定，无论是4还是8都需要依据产品实际界面的需求来考虑。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/c4JMdrBPHzMAgdqLugAc.jpeg" alt="设计系统的研究与整理（中）" width="682" height="230" referrerpolicy="no-referrer"></p>
<p><strong>4）视觉感知与开发实际操作的空间距离</strong></p>
<p>实际设计过程中，字体因本身的结构会导致与周边元素的空间距离在视觉感知上跟实际设定的数值有所偏差，因此我们在设计字体与其他元素的空间距离时，结合4pt网格可以参考以下2种方式。</p>
<p><strong>① 以基线为参考设定间距</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/mmxzr47T5F4PPuhZYePo.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>中文字体：基线与文本框间距相仿，如上图所示，蓝色代表基线，红色为文本框，在设定间距时可以直接使用4pt网格规则。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/QGwb9XzhNGgM3Nse6KBY.jpeg" alt="设计系统的研究与整理（中）" width="687" height="103" referrerpolicy="no-referrer"></p>
<p>英文字体：英文字体的基线与文本框的间距相差较大，以英文字母为排版内容的主体时，英文字体的基线必须位于4pt网格上，从基线向下到相临的元素、从Cap height 向上到相临的原色之间必须使用4的整数倍(即下图中的C的距离)。<strong><br>
</strong></p>
<p><strong>② 以文本框为参考设定间距</strong></p>
<p>由上图可知，直接使用以文本框来定义元素之间的间距时，需要考虑加上文本框到基线之间的距离后，再整体的给出间距的数值。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计系统的研究与整理（中）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/11/wEKdKq6pcdeMthWvxvim.jpeg" alt="设计系统的研究与整理（中）" width="680" height="102" referrerpolicy="no-referrer"></p>
<p>附设计推荐：https://uxdesign.cc/the-4px-baseline-grid-89485012dea6</p>
<h3>4. 元素——ICON</h3>
<p>ICON在设计系统中更倾向纯粹的视觉感受和信息传达。</p>
<ul>
<li>ICON需要根据其图标的用途大多可分为两类：信息图标、装饰图标；信息图标中包含实用程序图标、对象图标、操作图标、Doctype图标、产品图标等。</li>
<li>从应用的视觉层级依次分为三类形式：1 面性；2 线面结合；3 线描；视觉层级的重量需要匹配界面的层级，比如在一级界面中的主功能ICON也是需要从视觉重量上重于其他二、三级界面内的ICON。</li>
<li>具体制作中，从图案造型上首要考虑用户的认别性，多使用高频率出现的图案造型，减少用户对新图标的学习成本，不能为了设计而去设计，其次需要考虑到产品内所有ICON的一致性和拓展性。</li>
</ul>
<p>由于ICON需要根据不同的产品品牌风格来设计不同的视觉风格，此一枚好的ICON是展示出设计师的绘画基础能力和对信息的理解能力，所以此处暂不做深入的细节设计展开。</p>
<h3>5. 微交互——Micro interaction</h3>
<p>个人观点：微交互包含产品中简短交互流程（不用解决某一功能的交互模块）且还包含微动效。</p>
<p>统一动效的逻辑规律，能更快地让用户在使用中熟悉产品并快速引导用户举一反三、将其经验复制去使用同一产品的其他功能。</p>
<p>此类别粗泛的归类可放在基础元素中来说，相对细致的了解还是归类在组件库中更为合适。</p>
<h2 id="toc-3">三、组件库 Components of organisms</h2>
<p>组件的整理相对UI元素会更需要理解产品的业务逻辑，通过对大部分设计系统内的组件梳理，设计系统中组件的类型分两种。</p>
<p><strong>1）分类型组件</strong></p>
<p>从ALIBABA FUSION、ANTDESIGN SYSTEM、发现此类设计系统是有对组件的内容进行分类的，大部分设计系统将组件库分为五个模块来管理：</p>
<ol>
<li>Navigation导航；</li>
<li>数据录入；</li>
<li>数据展示；</li>
<li>Feedback反馈；</li>
<li>通用。</li>
</ol>
<p><strong>2）未分类类型，而是采用总览的形式全部展示出来</strong></p>
<p>例如：CarbonDesign system、NAVDesign system、Lightningdesign system，在业务功能简单的前期下可以采用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/iG4EcCDc5gQj8lmE4NNn.jpg" alt width="682" height="389" referrerpolicy="no-referrer"></p>
<p>组件通过设计和编码以解决界面内特定的UI问题，特别是在运营端的产品设计中会更适合组件的应用。既能够提升用户在使用过程的效率优化用户体验，同时相同功能的组件代码可以调用也减少开发工作量。</p>
<p>因此在设计系统中，组件作为常用的重要部分，与代码和UI的关联非常强。前期在没有整体了解前，为方便理解透彻优先采用有分类组件的设计系统，后期在具体搭建基金服务设计系统时就可以根据所需来选择式的加入到搭建的组件库，方便后期的复用。</p>
<h2 id="toc-4">四、模版 Templates</h2>
<p>界面风格的打样或者说是在做其他界面时的范本，个人理解是一项很综合的需求，无论是产品本身功能界面的展示，或者是在接入SDK或者在跳转三方平台使用时，需要保持产品的视觉统一的调性。</p>
<p>其模版可以在产品接入不同渠道时提供统一的视觉风格和代码参考，这项与产品的品牌推广也是密切相关的。</p>
<p>以电商购物车界面，参数上不外是商铺名称、商品图片和名称、售价、数量、折扣优惠等；但在文字的排版、用色的选择、字体粗细的搭配等等不同的元素进行搭配时会形成不同的视觉风格，大概可以理解为同样的猪肉，可以是粤菜里的叉烧、湘菜里的辣椒小炒肉、淮扬菜里的四喜丸子；不同的厨师不同的风味，不同的设计师不同的风格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/0dLxzXbA6V9Ltb39nM84.png" alt width="688" height="312" referrerpolicy="no-referrer"></p>
<p>形成模版就一定要具有延展性，有固定不能更改的元素，包括元素的位置或功能；也要有可以让其跟随填入的内容来进行变化的部分，这样的模版才具有高效的应用性，不然做出来的也只是自娱自乐。</p>
<p>自制过PPT的小伙伴们肯定有比较深的感触，好用的模版和不好用的模版对于使用者来说可不是节省一点点的时间，设计系统中的模版更是需要精炼才能符合更多的场景界面的需求。</p>
<h2 id="toc-5">五、模式 Patterns</h2>
<p>模式是为达成目标所设计出的特定的交互流程和视觉样式，这种类型多发生在业务成熟后才会形成，产品在初创阶段由于业务不稳定性决定其功能的交互或视觉都是在不断的调整和改变，只有待业务稳定后形成一定的规律或者为达成目的制定规则后，设计系统中就可以开始依据其业务来探索尝试适合的设计模式。</p>
<p>设计模式的原则包括六种：开闭原则（Open Close Principle）、里氏代换原则（Liskov Substitution Principle）、依赖倒转原则（Dependence Inversion Principle）、接口隔离原则（Interface Segregation Principle）、迪米特原则（Demeter Principle）、合成复用原则（Composite Reuse Principle）。</p>
<p>其中个人比较多用到的是开闭原则和迪米特原则，在双录功能中主要考虑是在设计完成后，如果又因为监管而需要调整，那就尽量避免修改已有的代码，而是能够在原来基础上进行拓展、维护和升级。分析市场同类产品功能时一般会先将整条页面流程拉出来分析其中的功能流程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/gy6e6Mfl9ZwwoLU7QbR5.png" alt width="689" height="1116" referrerpolicy="no-referrer"></p>
<p>抽象出其功能流程，其中的双录功能是购买其他的金融产品时也会复用的，此功能是依据业务成熟明确的规则来制定其模式。能将业务流程进行对比和分析，可以发现尽管不同app里双录的内容会少许不同，但是关键的几个环节都是一致的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/sty3HWUwTYmGPtVuETfs.png" alt width="686" height="118" referrerpolicy="no-referrer"></p>
<p>例如下图中红色圈内的步骤，是通过对不同产品的双录功能流程的分析，最后总结出同类型必定会涉及到的界面功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/MFa0uSoBotsa4bwgVzov.png" alt width="686" height="388" referrerpolicy="no-referrer"></p>
<p>将其抽象后再进行设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/VVTeTnij6kP0bqzbvaBD.png" alt width="685" height="169" referrerpolicy="no-referrer"></p>
<p>UI设计师在设计工作中不会太多地涉及到业务流程和功能流程，比较多是通过交互的页面流程图开始设计制作界面，但是在设计系统中搭建模式就需要了解更多同业务相关的功能流程，这样才能产出实用的设计模式。具体的界面涉及到公司业务此处不做展示。</p>
<p>设计系统从0到1的过程会比较艰难，好的设计系统是具有生命一样能伴随产品的成长而成长。</p>
<p>以上内容为个人在实际项目完成后的总结分析，图片涉及到部分app产品，其界面仅为个人学习使用不作为商业用途。</p>
<p> </p>
<p>本文由 @bell-wang 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4250302" data-author="1053261" data-avatar="http://image.woshipm.com/wp-files/2020/09/y4nsaZCQtSxwS1OkzBex.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            