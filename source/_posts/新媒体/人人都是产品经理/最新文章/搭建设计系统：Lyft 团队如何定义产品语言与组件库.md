
---
title: '搭建设计系统：Lyft 团队如何定义产品语言与组件库'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/8godHTU4tq957VDy9yTq.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 19 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/8godHTU4tq957VDy9yTq.jpg'
---

<div>   
<blockquote><p>编辑导读：随着互联网行业发展，设计系统这一概念越来越热门。通常设计系统由使用指导文档和可复用的组件库组成，对于定调产品设计语言和提升生产效率都极具意义。但设计系统的搭建并不是一件容易的事，本篇文章展现了Lyft 团队的设计师搭建其设计系统的方法论以及一些小技巧，能够对各团队搭建自身设计系统时带来一定的帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4475746 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/8godHTU4tq957VDy9yTq.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>2019 年底，我协助将 <strong>Lyft</strong> [1] 全部的设计系统从 Sketch 移动到 Figma 。具有 “讽刺” 意味的是，在离开 Airbnb 前，其设计系统的迁移也是我负责的最后几个项目之一。这两次经历帮助我意识到一些在 Figma 中进行共享库（ Shared Library ）设计时每个人都该考虑的基本问题。</p>
<p>（[1]Lyft 是美国一家网约车公司，于 2012 年创立，类似于 Uber、滴滴）</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/M8cUMSxaWMHlpNnmkTpk.jpeg" referrerpolicy="no-referrer"></p>
<p>在这篇文章中，我将介绍在创建多个 Lyft 产品语言和组件库时，自己运用的一些优秀案例。最后，我还将介绍一些有用的小技巧，帮助各位对设计系统进行高效维护。</p>
<h2 id="toc-1">一、体系理念：系统中的秩序性</h2>
<p>当我们开始着手在 Figma 中创建系统时，需要先退一步，通过几个例子重新评估 Sketch 中已做的工作，并重新审视此前确定的 <strong>布局</strong>、<strong>视觉层次结构 </strong>与 <strong>命名规则</strong>。我们意识到，为了在这些新的库中建立坚实基础，必须花时间在系统中<strong>再创建一个可适用于文件中每个元素的子系统</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/xCs0Etx1GxoLwT8xKUhC.jpeg" referrerpolicy="no-referrer"></p>
<p>左图为轮播页面组件的主要组件，右图为该组件的内部嵌套组件。需要补充的是，文件的画布区域还存在 <strong>#F4F4FA</strong> 的背景填充。</p>
<p>我们使用<strong>可视层次结构</strong>（ Visual hierarchy ）来设置每个组件页面，以帮助区分<strong>主要组件和内部嵌套组件</strong>。所有<strong>主要组件</strong>都放置在内部轮廓为 4px 且没有背景填充的框架中。这些框架充当组件标签纸。</p>
<p><strong>内部嵌套组件 </strong>放置在白色背景的框架里。通过显示所有内部组件，使维护人员可获取到主组件内部可配置项的快照。这些内部嵌套组件的作用是 <strong>让用户能够灵活配置内部嵌套组件 </strong>，以此重新配置主组件来达到最终所需的形式。同时内部嵌套组件能促进该主要组件的通用性，提升其维护与使用的效率性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/iKQb9fUAQnwtgvaS6MfQ.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">填充系统语言</p>
<p>在每个框架中，都使用了特定的边距。建立边距系统的好处是它可以统一画布上的所有元素之间（从一个页面到另一个页面，从一个库到另一个库）的视觉效果。</p>
<p>我们组件库的边距系数包括：</p>
<ul>
<li><strong>60px：</strong>内部框架间距（顶部，右侧，底部和左侧）</li>
<li><strong>40px：</strong>框架标题到第一个主要组件之间</li>
<li><strong>24px：</strong>框架标题到字幕之间（可选）</li>
<li><strong>24px：</strong>垂直方向的主要组件之间</li>
<li><strong>40px：</strong>水平方向的主要组件之间</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/722FqCmIkarMZwuhQxMO.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图层从上到下视觉上重新排列</p>
<p>通常在 Figma 中，新创建的图层将默认创建在当前图层上方。而将图层根据正常的视觉框架层次从上到下、从左到右重新排列是一件繁琐的任务。</p>
<p>但在管理大量主要组件和内部组件时，以这种方式排列图层能帮助维护人员<strong>快速浏览有时比较混乱的画布</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ij1fxuY07NBe60RhY2fH.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">焦点紧凑型按钮的命名规则</p>
<p>与用户在<strong> Slack</strong>[2]上共同进行快速调研后，我们发现他们中的大多数人使用 <strong>资源面板</strong>（ Assets Panel ）来搜索和发现组件。因此组件的命名方式对这个工作流程就变得十分重要。</p>
<p>（[2]Slack 是一款企业协作应用软件，集合聊天群组、大规模工具集成、文件整合以及统一搜索功能于一体。允许团队和企业通过群组进行沟通，有点类似国内的钉钉和企业版微信。Slack 目前的日活跃用户数已突破 1000 万大关，付费人数已达 8.8 万人，且它的用户中有 65 家是来自财富 100 强的公司。）</p>
<p>我们创建了以下应用于所有组件的命名结构：</p>
<p><strong>文件名称 / 页面名称 / 框架名称 / 组件名称（变量、样式、类型和状态）</strong></p>
<p>其中：</p>
<ul>
<li><strong>文件名称</strong>（ file name ）是特定库的名称，用户需要在资源面板中启用该名称的库才能使用其模型文件中的组件（例如，核心 UI 组件（ Android / iOS ），核心 UI 组件（ Web ）， 核心用户界面颜色等）。</li>
<li><strong>页面名称</strong>（ page name ）是组件的名称（即 “轮播页面指示器（ Carousel Page Indicator ）”，“按钮”（ Button ），“列表项（ List Item ）等”。</li>
<li><strong>框架名称</strong>（ frame name ）是组件的最高级分组，通常是按大小命名（即按钮的 4 种大小：Focus ，Focus Compact ，Drive 和 Drive Compact ）。</li>
<li><strong>组件名称</strong>（ component name ）是主要组件及其变体的名称。由于变体的数量众多，我们使用反斜杠（/）将它们按照不同的类型定义并分类，例如按 “状态” 等。事实上即使这些变体被放在更多的类目里，也有助于相似变体组件的存储。它们更容易在「实例」下拉列表中灵活切换，或者更容易在「资源」（ Assets ） 文件夹中查找。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MqXCCHbFDOFyl3TLLXfG.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">「实例」下拉列表中的文件夹显示结构</p>
<h2 id="toc-2">二、更具灵活性的组件</h2>
<p><strong>创建原子元素</strong>（ atomic elements ）是设计系统的基础。我们将 Lyft 的产品语言分解为原子元素，然后用于创建特定的组件。这些内部嵌套组件（即前文的原子元素）有助于大型团队之间保持设计的一致性（例如按钮这类原子元素）以及降低维护成本，尤其当这些内部嵌套组件在多个复杂组件（例如文本字段，文本区域，下拉列表等）之间共用时。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Qir9W2jZdgToHLEvTF6J.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表项组件包括 3 个操作区域：开始区，中间区和结束区</p>
<p>这个示例展示了内部组件是如何构成列表项组件的。我们为该组件设置了多个区域，以便对其进行重新配置从而创建不同的变体。在每个区域下，可以选择不同的内部组件。另外，还可以将其设置为相同大小，并使每个区域仅允许使用固定几种选择（例如驾车页面开始区域默认仅使用 4 个内部组件）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ESRK4sTuJDgEyUdczLZi.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">起始区域所允许使用的内部组件</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/0nzYVWENXs8BuIEmtbxT.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">中间区域所允许使用的内部组件</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OjUxBMLS98GRsKGLorW4.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">结束区域所允许使用的内部组件</p>
<p>对于像「列表项」这样的复杂组件，内部组件非常有用，可以灵活地重新配置组件以适应各种情况。</p>
<h2 id="toc-3">三、“响应式设计” 相关</h2>
<p>当我们在创建灵活的共享组件时，还要考虑让这些组件可以按照你想要的方式进行响应。我们可以在 Figma 界面的「设计」（Design）面板中设置这些选项。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/2xS0Bxr08RuCEfkgNVIm.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Figma中的「设计」面板</p>
<p>由于大多数应用程序都需要支持各种屏幕尺寸和平台，为了更好将程序普及到所有用户，<strong>创建响应式组件</strong>（ Responsive components ）极为重要。而实现这一目的的方法是通过适当的定义，让组件图层根据你所设置的 “水平” 和 “垂直” 约束值，相应调整大小。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/C6TxVTNejktlV5PhlxyO.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">水平约束</p>
<h3>1. 水平约束</h3>
<ul>
<li>左侧：将图层固定在框架的左侧。</li>
<li>右侧：将图层固定在框架的右侧。</li>
<li>左右拉伸：图层沿x轴增长或收缩。</li>
<li>居中：图层在框架的水平中心浮动。</li>
<li>缩放：图层按框架尺寸的百分比增长或收缩。</li>
</ul>
<p>举一个设置水平约束的例子。例如在调整列表项组件的大小时，你希望图标保留在同一位置的同时允许文本层增大或缩小。这时只需将下方图例内「Start」层的水平约束设置为 “左侧”，并将<strong>「Middle」</strong>层设置为 “左右拉伸” 即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/BZxkLjhI6VbdHuazEFeO.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表项组件的水平约束设置示例</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/bpWKYcpsvUWQ7vHtarOQ.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">垂直约束</p>
<h3>2. 垂直约束</h3>
<ul>
<li>顶部：将图层固定在框架的顶部。</li>
<li>底部：将图层固定在框架的底部。</li>
<li>上下拉伸：图层沿y轴增长或收缩</li>
<li>居中：图层在框架的垂直中心浮动。</li>
<li>缩放：图层按框架尺寸的百分比增长或收缩。</li>
</ul>
<p>再举一个设置垂直约束的例子，例如在调整文本区域组件的大小时，你希望消息层固定在底部的同时文本区域增大或缩小。这时只需将下方图例内<strong>「Message」</strong>层设置为 “底部” 垂直约束，并将<strong>「Text」</strong>框架层的垂直约束设置为 “上下拉伸“ 即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/mvnGGKgDqkRLrdRWUKTx.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">「Text Area」组件的垂直约束设置示例</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/beky9Z70u0OarxbEHpjF.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">调整大小选项（见 8 号标注）：设置「自动宽度」，「自动高度」和「固定大小」（从左往右）</p>
<p>还有一些与此类似的约束功能可以在图层类型内设置，以适应内容的缩小或放大。这些约束项可以跟你之前设置的约束项共存。</p>
<h3>3. 自动宽度适配</h3>
<p>「自动宽度适配」选项可以 <strong>使文字图层的宽度根据所填的内容而自动调整</strong>。当我想要<strong>「文本」</strong>图层根据内容增长时，通常会将<strong>「文本」</strong>图层的宽度设置为「自动宽度适配」。即通过设置左侧「水平约束」（ horizontal constraints ）和「自动宽度适配」（ auto width ），<strong>文本图层将根据文字内容相应地调整大小</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ffYFtUcwaXMPn2TmtPVo.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">文本区域组件的自动宽度适配文本设置示例</p>
<h3>4. 自动高度适配</h3>
<p>「自动高度适配」选项可以 <strong>使文本图层的高度根据所填的内容而自动增加</strong>。原始文字图层的宽度将决定内容何时换行。当我希望将内容换行到组件中的第二行时，通常将文本图层的高度设置为「自动高度适配」。通过将「水平约束」与「自动高度适配」选项一起设置为左右约束，文本层将按照我的意图进行包装。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/e0R9PTrVkIe2ctzVJJAd.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">文本区域组件的自动高度适配文本设置示例</p>
<h3>5. 固定尺寸</h3>
<p>无论内容如何，该选项的参数都会设置在文本图层的宽度和高度中。<strong>文字图层的宽度设置项将决定内容何时换行，而超出文字层的高度设置的内容将不会被剪切</strong>。</p>
<p>创建灵活组件的另一种方法是利用<strong>自动布局功能</strong>（ Auto Layout feature ），该功能会根据内容做出相应的调整。很多组件与<strong>「自动布局」</strong>配合使用得非常好，其中包括按钮、列表和面板。但是此功能有其局限性，如何展示其优势取决于你的组件使用场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MaHt14ffxt3h9cjfLgeh.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">使用自动布局的响应式按钮</p>
<p><strong>「自动布局」能够统一设置间距、描边和圆角半径</strong>，而这正是创建按钮所需的全部元素。当你输入内容时，「自动布局」会在保持内边距不变的基础上自动调整大小。这同样适用于设置了「自动布局」的按钮堆叠场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/9c2wGz9F0tlVQ9C9Pwik.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">其他元素随文字内容变化而调整</p>
<p>当你将文字内容复制粘贴到文本图层中时，设计中的其余元素会随之调整，这正是「自动布局」功能的强大之处，同时这也是进行本地化测试的好方法。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/CfkO8UywyObJc1n3sloO.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">自动布局使自动排序变得简单</p>
<p>有没有发现对列表或菜单中重复的 UI 元素重新排序很麻烦？通过「自动布局」，你可以通过简单地拖放或使用键盘上的上、下箭头键来对它们进行重新排序。</p>
<h2 id="toc-4">四、设计技巧</h2>
<p>在管理设计系统团队的所有组件库时，我通常会 <strong>使用键盘快捷键来帮助我更有效地工作</strong>。其中一部分快捷键用法同其他设计软件相同，另一部分则需要些巧妙的专业提示，使其在 Figma 中更加容易发挥功效。</p>
<p><strong>「选择所有相同实例」功能</strong>（ Select All with Same Instance ）。当需要在包含主要组件的页面中重命名许多内部组件时，只需导航至「编辑」菜单，然后选择「选择所有相同的实例」即可</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/15IoKpnWPVyf8uUjScq4.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">编辑 > 选择所有相同的实例</p>
<p><strong>「创建组件」功能</strong>。任何一个做设计系统设计师都知道最后总归是要创建组件的。我经常键入 Option + Command + K 以快速创建组件。</p>
<p><strong>「重命名图层」功能</strong>。Figma 的默认重命名功能非常强大。选择多个图层并输入Command + R 会触发一个「重命名图层」模式，它具有更多的重命名选项，包括查找和替换，数字的升序和降序以及在当前名称前添加或附加。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/5MoSkYv1r1MPucHmyGkf.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Command + R when multiple layers are selected</p>
<p style="text-align: center;">选择多个图层并输入Command + R</p>
<p><strong>「粘贴所选内容」功能</strong>。粘贴是我最常使用的功能。在 Figma 中，只需键入 Shift + Command + V（当已经选择了某些内容时）即可完成此操作。</p>
<p><strong>「放大图层」功能</strong>。要快速放大图层，只需在「图层」菜单中双击该图层的图标即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UUKN6M0KovtDRrfZPZNy.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">在任意图层上实现快速缩放</p>
<p><strong>「组件说明」功能</strong>。这是一种传达有关组件特定详细信息的方式。将鼠标悬停在 “资源” 和 “代码” 面板中的实例上时就会显示。我们利用该区域为我们的工程合作伙伴提供移交信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/WMUb96TJiLBjWpX7uoQR.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">放置在组件描述中的工程切换信息</p>
<p><strong>「忽略约束」功能</strong>。当想暂时忽略组件层上的水平 / 垂直约束设置项时，你可以在调整组件大小时按住 Command 键。想要继续使用约束，松开 Command 即可。</p>
<p><strong>「防止自动嵌套」功能</strong>。我在画布上移动图层时发现的一件令人沮丧的事情 —— 移动的图层会自动被放置在其他框架中。想要防止这种情况发生，可以在拖动图层时按住空格键。</p>
<p><strong>「替换实例」功能</strong>。这是一个专业的小提示，可用于替换任何实例，但我专门用它来替换图标；从 “资源” 面板中拖动组件时，按住 Option 键。你也可以使用 “资产” 面板搜索字段，从而提高效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZHku73yxlYlxXCLpL5N5.jpeg" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">方便地替换图标</p>
<h2 id="toc-5">五、最终思考</h2>
<p>第一次构建 Airbnb 组件库时期，也是我第一次接触到设计系统相关内容。在过程中我收获良多。正是一开始就采用了 “ <strong>系统的秩序性 </strong>” 这一理念，我才有能力搭建出设计系统如此复杂的东西，并得以让设计系统以一种 <strong>一致、高质量、灵活的 </strong>方式呈现。而这种理念，以及上文提及的所有内容，就是我在 Figma 中构建 Lyft 设计系统的秘诀。</p>
<p> </p>
<p>作者：Jeremy D.</p>
<p>原文：https://design.lyft.com/building-a-design-system-library-3a1f0d09088f</p>
<p>译者：邵俊森，审核：李泽慧、张聿彤，编辑：徐小淇</p>
<p>本文由 @三分设 翻译发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4471275" data-author="719867" data-avatar="http://image.woshipm.com/wp-files/2020/04/GJMm6mJS8RLrwBroDbkk.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            