
---
title: '超全面B端设计规范总结'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/10/2wG9D2WoVUmhfNYQK4aB.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 15 Oct 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/10/2wG9D2WoVUmhfNYQK4aB.jpg'
---

<div>   
<blockquote><p>编辑导语：本文作者全面总结了B端系统的设计规范，包含UI规范、组件规范，总结了在实际工作中常用的组件，希望对正处于B端领域设计的你有所帮助。本篇文章适合正在从事B端设计工作的小伙伴阅读，一起来看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-702960 aligncenter" src="https://image.yunyingpai.com/wp/2021/10/2wG9D2WoVUmhfNYQK4aB.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>不知不觉已经深耕在B端这个领域3年有余，很多人接触过B端后会觉得乏味，因为B端的设计在视觉上并没有C端那么有冲击力，更多的是结合业务逻辑，设计出符合业务需求的交互，以及界面排版的合理性，达到产品的可用性、易用性、好用性。</p>
<p>由于业务的复杂性，功能实现的难度程度相比C端会高很多，但是B端系统会有很多相似的组件可以共用，设计师一般会在项目前期做好这些组件的规范，便于后期设计使用，同时开发也能减少开发量，公用组件库不仅能减少开发时间还能达到系统界面统一的效果，降低用户的学习成本。</p>
<p>B端的组件也是丰富多样、同时也比较复杂，因此此篇文章我只对组件样式做统计，并作简单的介绍，具体的组件使用场景后续一一分享，欢迎持续关注~</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/MuxCSiGau9SAEP6sKS5I.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<p>B端的系统规范我分为两大类，分别是<strong>：UI规范、组件规范。</strong></p>
<p><strong>UI规范：</strong>色彩、字体、布局、图标。</p>
<p><strong>组件规范：</strong>按钮、面包屑、导航菜单、分页、下拉菜单、滑条、日期选择框、树、标签页、输入框、表单、上传、气泡卡片、表格、警告提示、弹窗/抽屉</p>
<h2 id="toc-1">一、UI规范</h2>
<h3>1. 色彩</h3>
<p><strong>系统色彩规范，包含核心（品牌）色、辅助色、中性色</strong></p>
<p><strong>1）品牌色</strong></p>
<p>即产品主色，产品主色的设定直接影响产品气质和直观感受，也是产品直接对外的形象，品牌色要根据产品特性、用户使用场景、产品定位等进行选，尽量做好色彩的延伸性，可支持换肤，品牌色的应用场景包括操作状态、按钮色、可操作图标等</p>
<p><strong>2）辅助色</strong></p>
<p>用于提示其他场景，比如：成功、失败、警告、无效等</p>
<p><strong>3）中性色</strong></p>
<p>常用于文本、背景、边框、分割线等，需要考虑深色背景和浅色背景的差异，可以选择同一色相控制透明度变化，用来表现不同的层级结构</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/eVnAWV5U9wRI6dG91y69.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<p>一整套系统所涉及到的色彩往往不止这几种，如果我们只限制在上面所总结的几种颜色，那么在一些需要多种颜色时就比较难区分，比如一些常见的数据图表分析，就会涉及到多种颜色的结合使用，所以我们会根据主要的色彩规范衍生更多的色系供特殊情况使用，因此在作色彩规范时会准备一个<strong>“其它色”。</strong></p>
<p><strong>4）其它色</strong></p>
<p>如统计图、数据可视化、多个标签的不同配色方案根据项目情况单独设定，通过基本色彩衍生而来</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/G4Pk4NisaPBUscdlRGm5.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<h3>2. 字体</h3>
<p><strong>字体是体系化界面设计中最基本的构成之一。</strong></p>
<p>字体的大小、色彩区分体现界面信息的层级关系。</p>
<ul>
<li>中文字体建议选择：苹方体、思源黑体</li>
<li>英文字体建议选择：Helvetica Neue、思源黑体</li>
<li>系统中字体大小为：14px、16px、18px、20px、24px、26px、28px、30px、36px…</li>
<li>字体行高设定：根据文字大小及使用场景设置行高，行高=文字大小+8px</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/CJHsILu75NcG4nNNGMPI.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<p>常规默认的系统字体规范最小为12px，上篇文章【B端系统】我的设计踩坑总结（上）中我也提到过关于不同分辨率下，不同显示器分辨率和布局的默认设置情况，字体规范会作不同的梯度，这里就不再赘述，感兴趣的可以回头看看。</p>
<h3>3. 布局</h3>
<p><strong>B端系统的用户的主流分辨率主要为 1920、1440 和 1366，个别系统还存在 1280 的显示设备，通过动态适配布局来完成在不同</strong><strong>分辨率下展示内容。</strong></p>
<p>系统中存在的结构方式有<strong>：左右结构、上下结构。</strong></p>
<p>系统适配：采用24栅格。</p>
<p><strong>1）左右结构布局</strong></p>
<p>常被用于左右布局的设计方案中，常见的做法是将左边的导航栏固定宽度，顶部栏固定高度（有顶部栏的情况下），对右边的内容展示区域进行动态缩放。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/AhN03FW2Oj2zYLkCfGeb.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<p><strong>2）上下结构布局</strong></p>
<p>常被用于上下布局的设计方案中，常见的做法是将顶部栏固定，对下边的内容展示区域进行动态缩放，内容区域左右两边固定有最小值。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/doApBZUAgER6ctkgnThw.jpeg" alt="超全面B端设计规范总结" width="597" height="336" referrerpolicy="no-referrer"></p>
<h3><strong>4. 图标</strong></h3>
<p><strong>B端系统图标简洁为主、分类区分、便于识别，默认大小：16X16px，SVG格式为主。</strong></p>
<p>对于图标来讲，相信大家都不会陌生，而对于B端的图标，图标主要注重简洁易懂，并且一般起到分类标识和点缀的效果。</p>
<p>这里分享一下我在工作中怎么整理我的项目图标，以及怎么便捷的和开发小哥哥配合传图，图标设计我使用AI完成，大小都设置为16x16px，画好的图标直接保存为SVG格式，然后批量上传到<strong>iconfont.cn，</strong>在这里我会根据不同的项目分类，开发小哥哥只需要在每个项目中下载需要的图标即可，这样大大提高了工作效率。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/PIy3ylaDrcikkXo3zoKh.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、组件规范</h2>
<h3>1. 按钮</h3>
<p><strong>是按钮触发事件或动作，他们让用户知道接下来会发生什么。</strong></p>
<p>按钮的样式分为5种，分别是：<strong>主按钮、默认按钮、虚线按钮、文本按钮、链接按钮。</strong></p>
<ul>
<li><strong>主按钮：</strong>用于主行动点，一个操作区域只能有一个主按钮。</li>
<li><strong>默认按钮：</strong>用于没有主次之分的一组行动点。</li>
<li><strong>虚线按钮：</strong>常用于添加操作。</li>
<li><strong>文本按钮：</strong>用于最次级的行动点。</li>
<li><strong>链接按钮：</strong>用于作为外链的行动点。</li>
<li>按钮的状态分为4种，分别是：<strong>正常、突出显示、禁用、已选中。</strong></li>
<li><strong>正常（normal）：</strong>表示控件处于活动状态，但是当前并未使用。</li>
<li><strong>突出显示（highlighted）：</strong>表示控件正被按住或正被使用。</li>
<li><strong>禁用（disabled）：</strong>表示按钮未启用且无法使用。</li>
<li><strong>已选中（selected）：</strong>仅特定控件具有该状态，表示控件当前已被选中。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/i9YYAmnp4gASN0tFUXJq.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<h3>2. 面包屑</h3>
<p><strong>面包屑是一种导航系统，显示当前页面在系统层级结构中的位置，并能向上返回。</strong></p>
<p>面包屑组件在B端系统是常用的组件，同时在网站中也是常用的，面包屑的样式分为2种：<strong>短面包屑、长面包屑。</strong></p>
<ul>
<li><strong>短面包屑：</strong>用户层级比较浅的页面。</li>
<li><strong>长面包屑：</strong>用户层级比较深的页面。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/I1fa2dgCBjHRwrJ0LiLZ.jpeg" alt="超全面B端设计规范总结" width="595" height="335" referrerpolicy="no-referrer"></p>
<h3>3. 导航菜单</h3>
<p><strong>为页面和功能提供导航的菜单列表。</strong></p>
<p>导航菜单一般分为2种模式：<strong>左右结构导航、上下结构导航。</strong></p>
<ul>
<li><strong>左右结构导航：</strong>我们见过最多的就是左右结构的导航，通常会采用图标+文案的形式呈现，并且有层级区分，采用点击展开的形式收缩二级目录，左右结构的导航一般都会支持左侧收缩的交互功能，为内容展示区域提供更大的展示空间，一键收缩或者鼠标左右拖动收缩，可根据实际情况而选择合适的交互方式。</li>
<li><strong>上下结构导航：</strong>菜单排版在顶部左侧或者右侧，这样的导航方式在网站中比较常见，但是在B端系统中也会使用，我曾接触过的实际项目中就有使用，主要运用于页面内容量大，导航无次级时。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/rbmkifBSHd1AyLnBneFM.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>4. 分页</h3>
<p><strong>采用分页的形式分隔长列表，每次只加载一个页面。</strong></p>
<p>分页的样式也是多种多样，在不同情况下也会选择不同的样式，我这里总结了我们目前系统使用的3种分页样式：<strong>常规样式、长版样式、简洁样式。</strong></p>
<ul>
<li><strong>常规样式：</strong>默认展示的样式即常规样式，控制在五个数字间，避免数字太多太混乱</li>
<li><strong>长版样式：</strong>当数据信息量巨大的情况下，分页的数量也会增多，采用多数字可切换的样式</li>
<li><strong>简洁样式：</strong>页数固定或最多不超过10页时，一般采用左右切换的样式</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/Z7g8mDhEmn4UgDOjY2mT.jpeg" alt="超全面B端设计规范总结" width="595" height="335" referrerpolicy="no-referrer"></p>
<h3>5. 下拉菜单</h3>
<p><strong>下拉菜单向用户显示操作或选项的列表。</strong></p>
<p>下拉菜单样式可分为2种：<strong>一级下拉、多级下拉。</strong></p>
<ul>
<li><strong>一级下拉：</strong>最简单的下拉选择样式，直接平铺可选择的选项内容。</li>
<li><strong>多级下拉：</strong>下拉框种存在层级关系（主次层级）、样式可分为<strong>左右分级展示、上下错位分级展示、树结构分级展示</strong>（这里关于树结构的下拉展示方式没有作样式，不过后面有关于树结构的组件介绍，可参考其样式）。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/puhZJjvRw9GrDKfLia3e.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>6. 滑条</h3>
<p><strong>上下滑动展示更多内容。</strong></p>
<p>滑条是作为产品中不可缺少的组件，无论是web端还是移动端，都会运用到，滑条的样式也都差距不大，也没有很大的设计发散，主要是还是根据实际需求情况区分其交互形式。</p>
<p>例如：在我的实际工作中，我选择的交互方式是，滑条不会一直显示在界面中（避免页面整体视觉效果受到干扰），只有当鼠标移动到可滑动的区域才会出现滑条（告知用户页面内容可滑动看更多），所以我的组件中会出现两个样式。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/ss6eujvTNVwmiotJr0UC.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<h3>7. 日期选择框</h3>
<p><strong>输入或选择日期的控件。</strong></p>
<p>对于B端系统来说，日期会根据业务的情况精度提取会不同，精确到日、时、分、秒，作为时间设置和过滤条件使用时，一般会使用到时间区间，所以日期选择框分为以下3种：<strong>普通日期选择、区间日期选择、精准日期选择。</strong></p>
<ul>
<li><strong>普通日期选择：</strong>只可选择某年月日时间精度。</li>
<li><strong>区间日期选择：</strong>可选择不同年月日时间区间。</li>
<li><strong>精准日期选择：</strong>可选择年月日、时分秒高精度时间。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/lkDrH7AnJgOydlVsGMWv.jpeg" alt="超全面B端设计规范总结" width="601" height="338" referrerpolicy="no-referrer"></p>
<h3>8. 单选/多选框</h3>
<p><strong>在一组可选项中进行单项/多项选择时。</strong></p>
<p><strong>注意组件的使用场景：</strong>单选/多选框看是简单又常见的组件，但是在实际项目中运用时也需要做到细致的区分，选项只支持单选时我们就采用合适的圆形单选框，支持多选时就采用方形的多选框，做好单选和多选的场景区分.</p>
<p><strong>注意组件的状态区分：</strong>单选/多选框的样式虽然简单，但是也有3种显示状态：<strong>默认、选中、不可选。</strong></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/hLARNf9EqLHgz6JVvDw1.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>9. 树</h3>
<p><strong>树型展示和树型选择控件。</strong></p>
<p>树组件在B端系统中常用于权限设置，大部分的B端系统都会有权限设置的功能，当然在我实际工作中出来权限设置使用树结构外，还有其它的使用场景，比如：组织维护、职能维护、事项维护等等。</p>
<p>树结构可以清晰的展示层级关系，并且节约空间，但是在一些复杂的需求中，树结构比较难维护，所以在选择组件时也需要考虑实际业务场景和维护成本。</p>
<p>下图中左侧为展示效果的树结构、右侧为可操作（选择）的树结构效果展示，两种效果都可运用到上文提到的下拉选择框中使用。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/f2I2tLPvzcr3FPHGqA0V.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>10. 标签页</h3>
<p><strong>选项卡切换组件。</strong></p>
<p>标签页分为2种形式：<strong>横向标签、纵向标签。</strong></p>
<ul>
<li><strong>横向标签：</strong>横向的标签样式是最常用的样式，包括在网站和移动端都会运用，标签样式分为文字+线条、文字+色块，分别区分选中和默认的状态形式，标签除了默认固定的标签外，还会有可编辑的标签，可满足增删除功能，所以这类标签会有“删除”标识，例如网页页签就是可编辑的标签样式。</li>
<li><strong>纵向标签：</strong>纵向标签有点类似左右结构的导航菜单，也是通过点击选中页签，实现页面内容的切换变化。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/XIMglBNBzUwJaqLhCbcB.jpeg" alt="超全面B端设计规范总结" width="599" height="337" referrerpolicy="no-referrer"></p>
<h3>11. 输入框</h3>
<p><strong>文本输入框、数字输入框。</strong></p>
<p>输入框是最为常见的组件了，这里就不做组件的介绍，主要还是分享一下关于输入框组件在不同显示器上排版布局的区别吧，例如在移动端输入框的文本和输入框一般会采用上下结构，因为移动端的尺寸比较小，可展示内容的区域有限。</p>
<p>而在web端，会根据此页面的内容量以及内容显示的形式来区分显示方式，例如弹窗中内容较少时，输入框样式一般会采用上下结构，内容较多页面空间较大时会选中左右结构排版，当然，这并不是固定的排版思维，而是需要根据实际情况选中合适的排版方式。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/fLNRmZ1tOy61hbzFSUcl.jpeg" alt="超全面B端设计规范总结" width="602" height="339" referrerpolicy="no-referrer"></p>
<h3>12. 表单</h3>
<p><strong>高性能表单控件，自带数据域管理，包含数据录入、校验以及对应样式。</strong></p>
<p>表单在我认为，即多个输入框的组合，表单的样式可直接根据输入框的两种样式作区分展示，左右结构和上下结构，普通的表单是会根据实际业务情况固定输入的字段信息，而对于一些特殊的表单信息，用户可以增减表单的内容时，表单的样式则会和普通的样式作区分，并且交互方式也会有所区分。</p>
<p>例如下图右侧的表单样式即为可增减的表单，支持点击右下角的“添加”按钮增加一个和上面一样的表单内容信息，可点击表单模块右上角的“x”删除此表单，达到用户自定义表单内容数量的要求。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/FjyWWpzbdSmDk2igL9g1.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>13. 上传</h3>
<p><strong>文件选择上传和拖拽上传控件。</strong></p>
<p>上传的功能我们不少见，对于B端系统来讲，上传表单、文件是最为常见的操作，这里我总结了3种上传的组件样式：<strong>单件上传、图片上传、批量上传。</strong></p>
<ul>
<li><strong>单件上传：</strong>单文件上传一般是上传一个或者几个文件，常采用按钮或拖拽的交互形式。</li>
<li><strong>图片上传：</strong>简单的图片替换上传，常用于企业logo替换、登录页图片替换等场景，需告知用户图片上传的状态。</li>
<li><strong>批量上传：</strong>对于大批量的文件上传需要告知用户文件的状态，支持用户取消上传操作，例如：常用的百度网盘上传和下载文件。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/5dCmLHFsREkMqePDpNg4.jpeg" alt="超全面B端设计规范总结" width="601" height="338" referrerpolicy="no-referrer"></p>
<h3>14. 气泡卡片</h3>
<p><strong>点击/鼠标移入元素，弹出气泡式的卡片浮层。</strong></p>
<p>由于B端产品内容量巨大，需要在有限的空间展示所有的数据不为是个难题，所以为了在有限的空间展示重要额内容，达到界面的可阅读性、采用次要内容隐藏的功能，通过点击或者悬浮展示全面的内容。</p>
<p>最常见的表格内容太长出现“…”，鼠标移入出现悬浮气泡显示完整的信息；名称后面跟随“？/！”图标，鼠标移入出现悬浮气泡显示注释的信息；数据分析图表，鼠标移入出现悬浮气泡显示数据的信息等等。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/wUL8s8b8DV4UK32JbAwx.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>15. 表格</h3>
<p><strong>展示行列数据。</strong></p>
<p>表格作为常见的组件，样式是多种多样的，并且每一种表格的交互都各不相同，使用的常见也各有差异，下图我只展示了2种表格的样式，但是实际上远不止于此，在我目前工作种涉及的一个项目中就采用了超过5种的表格样式，这里我就不做详细介绍，后期我会单独总结关于表格的不同样式以及使用场景</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/vhDXOhWjYGYj7yIDbcJU.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>16. 警告提示</h3>
<p><strong>警告提示，展现需要关注的信息。</strong></p>
<p>警告提示一般分为四个状态：<strong>成功、信息注释、警告、错误（失败）.</strong></p>
<p>根据提醒内容的显示以及是否需要用户手动操作，我总结了四种样式，如下图：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/p5H6pwQL6gCH1KwsSe3r.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<h3>17. 弹窗/抽屉</h3>
<p><strong>信息展示和信息填写的浮层面板。</strong></p>
<p>弹窗和抽屉都是内容展示的不同出现方式，组件的选择同样需要根据实际需求情况，比如需要参考页面信息填写表单信息，采用抽屉的样式则更为合理，这样就可以在右侧填写表单，在左侧参考数据对比，抽屉的样式可以是浮窗也可以是直接从右侧推出，左边内容被挤压得形式，这样得交互方式在我得实际项目中也是常用之一。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="超全面B端设计规范总结" src="http://image.woshipm.com/wp-files/2021/10/RLZT1Ic3cpcP4J3f1YdA.jpeg" alt="超全面B端设计规范总结" width="600" height="338" referrerpolicy="no-referrer"></p>
<p>此篇文章我只总结了我实际工作中常用的组件，还有很多不常用的组件没有作全面的总结，后期有机会再做总结吧！，也希望对处于B端领域的你有所帮助，欢迎一起探讨关于B端设计有趣的事！</p>
<p> </p>
<p>本文由 @设计小余 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5175891" data-author="1131797" data-avatar="http://image.woshipm.com/wp-files/2021/08/318nVsgz69UPnNMipSIh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            