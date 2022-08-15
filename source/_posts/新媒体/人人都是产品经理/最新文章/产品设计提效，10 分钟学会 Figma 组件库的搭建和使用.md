
---
title: '产品设计提效，10 分钟学会 Figma 组件库的搭建和使用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/08/2inDzb7IOmEyqKz9tcLK.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 15 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/08/2inDzb7IOmEyqKz9tcLK.jpg'
---

<div>   
<blockquote><p>编辑导语：做设计时，如果一个一个的修改按钮，很容易让设计师沦为做图机器，如果提前搭建好可复用的组件模板，就可以一次性批量修改，解放生产力，让设计师把更多的时间精力投入到业务需求的深入思考中。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-850355 aligncenter" src="https://image.yunyingpai.com/wp/2022/08/2inDzb7IOmEyqKz9tcLK.jpg" alt referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/OAd4oRVVQXsv1tRE4Kcy.png" alt width="1920" height="1934" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景</h2>
<h3>1. 为什么需要 Figma 组件库</h3>
<p>当我们在做设计稿的时候，例如做一个按钮，如果没有做成可复用的组件，那后面在其他模块要用到按钮的地方可能又需要重新画，会有很多的重复劳动。又或是另一种场景，我们需要把按钮的尺寸或颜色统一调整，可能需要一个一个去改，很容易改错或者疏忽。</p>
<p>总之，一次性设计是使设计师沦为做图机器的罪魁祸首。如果我们提前搭建好可复用的组件模板，就可以达到复用的目的，而且可以一键批量修改，从而解放生产力，把更多的时间精力投入到业务需求的深入思考中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/VGQjobbZio2m2JG4zcp2.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>2. Figma 组件库在设计体系中的定位</h3>
<p>设计体系（Design System，也可以叫设计系统）是可复用组件的集合，由清晰的标准引导，通过机制化的组织流程和具象的指南与工具加以整合，以帮助开发者（设计、研发等）高效且一致地创建大量的应用，并且动态地确保用户体验的一致性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/NPAG05hOHW0VBv0hD9kp.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>需要指出的是，设计体系不只是组件库，不只是样式指南。当你浏览上面这些案例内容的时候，你固然会看到组件库和样式指南，但更值得关注的是它们陈述的设计目的、设计理念、设计原则、设计模式、设计与工程同步的方法等等。</p>
<p>Figma 团队做了一个专门以设计体系为题的网刊，域名为 designsystems.com。该网站有大量围绕设计体系的文章、教程及代码库。</p>
<p>总的来讲，Figma 组件库是设计系统中的一部分，是沉淀设计规范的设计资产。作为连接设计师和设计师、设计师和开发的桥梁，组件库首先应该是灵活易用的；其次，组件库是需要跟随产品不断进化的，这就要求它是容易被维护的，否则它就会落后于产品迭代，直至逐渐被遗弃。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/K8OSgGuqMaUcmcRRvi4k.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、Figma 组件库如何助力设计提效</h2>
<h3>1. 线上调用、实时同步</h3>
<p>跨团队使用组件库(样式、组件)、实时更新、组件库的主题颜色一键切换、组件可以增加提示语等功能，所有的调用方式都是线上的，不需要任何本地文件的传输。如果组件库有更新，只需要 Review 之后 Update 即可实时同步。</p>
<h3>2. 多人协作、共创共建</h3>
<p>Figma 组件库可以有多个设计师共同创建，大家只需要约束好相应的组件层级嵌套规范，每个人可以负责自己所属的模块，分别更新、分别发布。</p>
<h3>3. 灵活拼装、自由组合</h3>
<p>Figma 组件库有非常高的自定义拼装能力，不解除组件的基础上也能够改变一些颜色、圆角、布局间距等。对于一些特殊的业务场景，也能将基础组件拆分开进行组合。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/8MXwH5HiR8GzljuDL5Jb.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、Figma 组件库搭建经验分享</h2>
<h3>1. 原子设计理论</h3>
<p>提到组件库，不得不提到原子构建理论。Atomic Design(原子设计)是构建Design System 的核心指导理论。化学中，所有的物体都是由原子构成，原子组合构成分子，分子组合构成有机物，最终形成了宇宙万物。</p>
<p>2013年 Brad Forst 将此理论运用在界面设计中，形成一套设计系统，包含5个层面：原子、分子、组织、模板、页面。那么对应设计系统来说，我们的颜色、字体、图标以及按钮、标签等都会对应到相应的原子和分子，通过组件之间的搭配组合，最终构成页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/lXCiIcXTjLDg9KPCToi8.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>2. Foundation 全局基础样式</h3>
<p>在设计系统中，基础样式可以理解为构成设计稿最基础的「原子」。如果你的设计稿中全部都使用共享样式，当后续需要调整时，只需要调整样式库即可，设计稿会跟着变化，而不需要一个个调整；样式库还可以通过 Design Token 来映射到前端代码中，以提高最终开发的还原度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/tqh8OLxcDjIk457Yhm1W.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>样式是 Figma 中的一些可以复用的模式，目前支持四种：</p>
<p><strong>1）颜色样式（Color）</strong></p>
<p>颜色样式可以用于填充颜色、描边颜色、文字颜色。是页面整体风格表现的重要基本元素，它可以建立品牌的识别性，梳理页面的视觉层级关系，突出内容并平衡其他视觉元素。建议大家可以按照功能和属性将颜色进行分组命名，比如，比如品牌色、成功色、警告色等，并将默认、悬浮、点击、禁用等颜色放在一组，方便团队其他设计师使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/Al5x7tYbfjH6vSZnAr6q.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>2）文本样式（Text）</strong></p>
<p>文本样式中包括：字号、字重、行高和字距等。需要注意的是不要单纯的将名称命名为T1、T2等纯符号性的名称，可以在后面加上适当的语义化描述，比如一级标题、常规正文等文案，同时也可以在描述里添加对应的使用说明，这样当鼠标悬浮在这个样式上，会给用户带来提示性的预览。这种办法同样适用于颜色、阴影等全局样式，会更加方便大家调用且能够很好的解除新用户的使用疑虑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/Yiz95VBAggTdHv36KmxR.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>3）效果样式（Effect）</strong></p>
<p>效果样式包括：外阴影、内阴影、模糊、背景模糊等。阴影值应该遵循现实物理世界中物体的特性。因此在阴影的设定上采用了三层阴影的表达方式，让阴影更加柔和，更符合真实光源下的物体状态。物体的高度直接影响阴影，离地面越高阴影越大，模糊值越高，反之相反。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/0rTm94EyMMk3Ht07c7y5.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>4）布局栅格（Layout Grid）</strong></p>
<p>横向和纵向布局参考。可以通过栅格样式来制定全局的尺寸和间距规范，尤其是用在响应式网页的设计当中，可以通过栅格来做出一些适配效果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/9l3E1Tm7c9dSNGxUPC2G.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>3. 创建样式</h3>
<p>在 Figma 中创建四种样式（颜色 Color、文本 Text、效果 Effects、栅格 Layout Grid）的操作类似。</p>
<p>这里以颜色为例，选中一个图层，Fill 填充颜色之后，点击右边的四个点图标，在弹出的 Color Styles 颜色样式面板中点击加号，然后再填写样式的命名就能创建了。这里补充一下命名中使用斜杠“/”可以给样式进行分组。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/EhRdhMoQjACtp5HjVWoX.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1）批量创建样式</strong></p>
<p>如果想一次性创建多个颜色样式，可以将所有的颜色通过矩形平铺出来之后，按下快捷键 Cmd+R，来批量更改好图层命名。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/x719heco4GTqv74XQb9V.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>然后再通过插件「Styler-Generate Styles」就能一键批量创建样式，解放双手。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/Tc0ZsOPG3e5ROOvqov3c.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>以上是以颜色样式距离，其他的文字样式、效果样式的创建方法也是同理。</p>
<p><strong>2）样式命名</strong></p>
<p>样式命名对于共享样式库的显示顺序十分重要，你可以通过斜线分隔命名的方式来给它们归类。比如说你可以设置一系列的警告颜色，都以 error/ 开头，再设置一组排版文字的颜色，都以 Text/ 开头，这样它们就会被自动归类，方便你在使用时查找。一般有以下几种分类依据：</p>
<ul>
<li>按色调分类</li>
<li>按主题分类</li>
<li>按场景分类</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/OhPdZWG8JfxprHMZLXE4.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>3）样式描述</strong></p>
<p>给样式添加描述和给组件添加描述作用一致，描述信息可以帮助你判断哪里该用哪种样式，保持团队风格统一。另外补充一下，描述也是可以被检索到的，例如可以尝试名称用英文和前端对齐，描述用中文方便英文不好的同时协作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/N51FFoAqUBfClYLvIfim.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>4. 组件类型</h3>
<p><strong>1）主组件（Main component）</strong></p>
<p>在左边图层列表内显示为紫色的，图标为四个菱形组成的图形。它作为主组件，它的变化会实时同步到它所有的实例组件中，有时也称之为父组件。</p>
<p><strong>2）实例组件（Instance）</strong></p>
<p>对着主组件接着按下 <code>Cmd D</code> 复制的元素，它们在左侧图层列表内显示为紫色的空心菱形。它们作为主组件的引用，会自动同步主组件的各个属性变动。一个主组件可以有多个实例组件，有时我们也称其为子组件。实例组件有以下特点：</p>
<ul>
<li>可以修改很多属性，比如背景色、文字内容、布局间距等，修改的属性不会再跟着主组件同步；</li>
<li>图层结构不可以改动，也不可以删除图层，按删除键不会删除而是隐藏图层；</li>
<li>内部图层尺寸不可以改，但是实例组件整体的尺寸可以更改。</li>
<li>实例的编辑可以逆向覆盖。只要在实例替换面板中点选 Push overrides to main component，即可将当前的实例属性同步给母版及所有的实例。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/FYrP722c0Gpw7NbVxvQC.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>5. 组件嵌套</h3>
<p>组件的嵌套，类似原子理论中「分子组合成组织」的过程。它所对应的元素往往是一些较为复杂的控件、卡片等。比如我们上面做的按钮组件，将它的实例结合图标、文案编为一个结果页 Frame，再将 Frame 组件化即可完成一个组件的嵌套。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/BlVYQpIGGj6el6uq7Rys.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>6. 组件集（Variants）</h3>
<p>当我们有很多相近的组件时，可以把它们做成一个组件集（也称变体）。这样在引用时就不用从一堆相似组件中寻找了，只需要切换不同的多组件属性即可。例如按钮可以按照类型（Type）和状态（State）共四种。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/rp1soXrcmV1ybVKf3xx1.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1）属性切换</strong></p>
<p>那么，我们就可以把它创建为一个有两个维度属性的变体，此时可以通过组合 Type 和 State 属性来切换四种状态。其中 Type 和 State 称为属性名，后面的选项（比如 Default、Hover）称为属性值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/RQfr9IeeYdrTA5mU5vRq.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>2）创建组件集</strong></p>
<p>创建组件集有两种方式。一是选中多个主组件，在右侧就会出现组合为变体组件集（Combine as variants）选项，点击之后这些主组件就会被一个组件集（紫色虚线的 Frame）装起来，在组件调用面板也变成了一个组件；二是选中没有做成组件对普通图层，点击上方的 Create component set也能创建组件集。默认会调用左上第一个属性的组件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/fHPdBN71ZbFLGlhz0x3d.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>3）组件集命名</strong></p>
<p>创建组件集的时候 Figma 会自动根据组件名称中斜线（<code>/</code>）分割的值来生成属性列表，所以在创建之前推荐先按照一定规则命名。如下图，我们按照 <code>Button/Type/State</code> 的格式给每个按钮命名，Figma 会自动提取出所有可能的属性，生成右侧的属性值列表。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/suGfpF4buQ2CNg3BJ4jA.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>4）属性和值</strong></p>
<p>按照上图命名的四个按钮组合为变体组件集之后，在右侧会显示自动分好类的属性值，不过我们还需要手动更改一下属性名，也就是把 Property 1 改为 State，把 Property 2 改为 Type。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/ngG7JkW8PLtDmQ7svIwi.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>5）组件调用</strong></p>
<p>此时按下 <code>Shift+I</code> 打开组件调用面板，可以看到四个按钮组件在这里只显示为一个按钮。拖拽一个实例组件到画布中，我们就可以在右边通过选择属性来切换不同的按钮变体了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/Va8RHHoMHPgJBjMgdI8c.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>6）属性值顺序调整</strong></p>
<p>这里右侧的属性名和属性值的显示顺序可以在变体组件集的面板中调整。从组件调用面板拖拽出来的实例组件，各项属性值都默认选第一个，所以我们一般会把使用频率比较大的属性值排在第一位。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/in9a9U8JhmFTPdAXvTvb.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>7）组件属性- Boolean Property</strong></p>
<p>上述实例组件右侧面板中的属性选择都是下拉菜单的形式，如果我们的组件是现实隐藏，例如图标左侧是否带图标，可以通过组件属性的现实隐藏来实现。选中图标，点击右侧面板 Layer 右边的箭头，修改默认值为 True 或 False。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/IcOjhg0ky9merdsT3KMl.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>后面在调用的时候，就能通过开关的形式来切换是否现实图标，同时组件集内部的数量也并不会增加，可以节省内存消耗。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/sHYTbvIxXYSofMT8QD4W.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>8）组件集内增加组件</strong></p>
<p>我们可以直接在变体组件集里面添加新的组件，选中变体组件集之后在右下角出现一个紫色的加号，点击它可以添加变体组件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/FLfOeYzZu88AMR8Rp9gp.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>9）组件集属性冲突</strong></p>
<p>假设我们要添加一个禁用状态的主按钮。点击添加变体，此时虚线框中会复制出一个按钮，我们把它的背景色修改。可以看到，选中变体组件集时在右侧会出现属性冲突的提示。因为这个新添加的变体组件属性也会被复制过来，和已有的组件属性一样，就有了冲突。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/n7zcGwB92IcnSShYwFWe.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>这里发生冲突的是它的 State 属性，它也是 Default，我们把它更改为 Disable，属性冲突的提示就消失了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/8Y5vCZAxHdQ07RLh9VHm.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>10）组件集内增加属性名</strong></p>
<p>当需要增加属性类型的维度时，可以点击 Properties 右侧的加号按钮，创建新的 Variant，创建好之后相当于多了一个新的属性名，便可以将每个组件设置对应属性名的属性值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/1VHxYx42CsgJ4cFaO7rZ.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>11）注意事项</strong></p>
<p>变体可以帮我们避免大海捞针式的选择，将组件切换简化为少量属性组合，但是在创建和使用变体时养成一些好的习惯可以帮我们更好的利用它。</p>
<ul>
<li>并不是任何组件都适合组合在一起成为变体，我们一般把同一组件的不同状态组合为变体；</li>
<li>切换变体的时候也相当于替换组件，所以我们要确保一个变体组件集内的各个组件结构和命名一致，这样在切换的时候已修改的属性才会被保留；</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/kj0635dfhvg377WjFoV0.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<ul>
<li>如果需要解除变体组件集，可以直接将组件从虚线框内拖拽出来，全部拖拽出来这个组件集虚线框就会消失；</li>
<li>组件集也是一个 Frame，不过是一个特殊的 Frame，这个紫色虚线框是可以修改的，你还可以给它添加自动布局属性来自动排布里面的组件变体；</li>
<li>使用 Config 2022 更新的组件属性中的新功能，例如 Boolean Property、Swap Instance Property，可以一定程度上减少组建集内部的组件数量，避免巨型变体组件集，如果 一个变体组件集内有几千个组件，可能会消耗大量内存，导致操作 Figma 卡顿。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/mgVTaUPLer92kxz52gDG.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、Figma 组件库的发布、更新和使用</h2>
<p>组件库制定的意义，就是让团队每一位成员都能用到最新的组件，提升效率、保证一致输出。那么接下来就讲一下如何在 Figma 中发布、更新和适用组件库</p>
<h3>1. 发布组件库</h3>
<ol>
<li>Asset 点击 Team library 按钮（书本图标）；</li>
<li>Library 面板上，点 Publish；</li>
<li>二次确认面板，再次点击 Publish 即可发布成功；</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/wDnhTfGvgN3yc1IFwiqs.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1）发布频率</strong></p>
<p>当组件库发生变动，维护者发布后使用者在文件中会收到通知，来决定是否同步更新到设计稿。如果维护者频繁发布，使用者也会频繁收到通知，所以最好将更新发布固定在一定频率，比如每天下午六点发布一次，这样使用者只需要每天早上更新一次就可以了。</p>
<p><strong>2）私有组件 Private components</strong></p>
<p>当组件库中有一些临时或者很少复用的组件，可以给这些临时组件的命名前加上 _ 或者 . ，也就是英文符号下划线或点。在发布组件库的时候，Figma 会自动隐藏这些私有组件，这样你在构建组件库的时候可以遵循原子化方法，同时发布出去给其他设计师使用的组件库也很简洁，不会有一些临时组件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/SnyuiNRqv4sR3287tFQr.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>2. 复用组件库</h3>
<p>创完了组件库，团队成员的复用步骤如下：在Tteam library 开启想生效的组件库，开启后在 Assets 中就可以找到组件库对应的组件然后复用，可以通过分组形势查找，也可以通过关键词模糊搜索。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/0zpENX8rE0gAbYZAakrO.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>3. 更新组件库</h3>
<p>组件库也可以理解成是设计团队的一个小的产品，也是需要不断更新迭代的，当我们的组件库有更新内容的时候，可以和发布组件时进行同样的操作，点击 Assets 面板中的 Team Library 按钮，就能将在组件库中修改的内容发布更新至云端。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/Qw2PcAcn8R7dTI8ANRKU.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1）同步云端组件库</strong></p>
<p>当原组件库发生变化，Figma 右下方回弹出一个提示框，点击 Review 进行查看，可以预览所有在本文件中用到的组件库中的组件的更新的情况，确认之后点击更新，即可将变化同步到所有用到此组件库的文件。通过这种更新同步组件库的方式，便能够达到一键修改，全剧替换的便捷操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/DVdzKRE0cgMGR3Wb5ahC.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>2）复制组件的注意事项</strong></p>
<p>组件通过<strong>复制粘贴</strong>来复用只适用于两种情况：对于同文件下完全适用；对于跨文件的情况，组件<strong>只有在作为组件库发布后才可以跨文件粘贴复用</strong>，否则，复制粘贴的方式只能直接拷贝母版，无法以实例的状态拷贝！</p>
<p>比如上面做好的 Button 组件，同文件复制粘贴没有问题。但对于跨文件复用的场景，如果跳过发布，由文件 A 直接拷贝到文件 B ，拷贝后显示的就是没有正确复用的 Main component 状态；只有在 Libraries 发布后，拷贝到文件 B 时才显示为被复用的实例状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/053EwYvMv76T4AwHWz5M.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>4. 组件的替换</h3>
<p>组件的替换主要有两种形式，一种是组件与组件的切换，点击右侧面板组件名称的下拉选择器，例如从按钮切换到复选框，属于两个完全不同的组件切换；另一种是组件集内组建属性的切换，在组件属性的选择其中切换即可，例如按钮内部的各种状态切换。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/08/XM2FT4x2f67dKa2XNaCq.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、结语</h2>
<p>Figma 组件库是一个强大的提效工具，也是设计系统中很重要的一部分。作为连接设计师和设计师、设计师和开发的桥梁，有了统一的标准后，输出出的效率也会大大提高，对于团队来说能很好的提升产品的品牌感和体验。另外组件库是需要跟随产品不断进化的，这就要求它是容易被维护的，需要梳理清楚它的使用者是谁，要把 Figma 组件库当作一个设计团队的产品来维护和升级，方便使用对象的查找、复用和理解。</p>
<p>由于时间和篇幅有限，关于 Figma 组件库介绍中存在的疏误之处还望大家给与指正，欢迎大家一起学习和讨论。</p>
<p>参考文献：</p>
<p>《设计体系：数字产品设计的系统化方法》</p>
<p>https://help.figma.com/hc/en-us/articles/5579474826519-Create-and-use-component-properties</p>
<p>https://help.figma.com/hc/en-us/articles/4404856784663-Swap-style-and-component-librarieshttps://mp.weixin.qq.com/s/PoEk5vRRrquLOTOH3QZgIw</p>
<p> </p>
<p>作者：波波 Bobby He ；深耕 B端体验设计，持续学习输出中。</p>
<p>本文由 @波波Bobby He 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5564773" data-author="813234" data-avatar="https://image.woshipm.com/wp-files/2021/11/RtNDHJUeQJBTTP7In5Qd.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            