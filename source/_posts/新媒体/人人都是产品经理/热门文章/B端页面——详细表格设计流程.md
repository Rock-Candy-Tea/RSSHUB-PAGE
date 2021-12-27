
---
title: 'B端页面——详细表格设计流程'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/AB7CimeKsd4nwO4yV8qb.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 15 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/AB7CimeKsd4nwO4yV8qb.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端页面中，表格也是常见的数据展示方式。合理的表格设计有助于清晰、高效地展示数据，提升用户的可读体验。那么，在设计过程中，设计师应当依照什么原则进行B端页面的表格设计？本篇文章里，作者总结了B端页面的表格设计流程，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4711628 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/AB7CimeKsd4nwO4yV8qb.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>本文对表格设计进行了较为全面的总结，对一些基础场景构成提出了对应的设计规范建议。全文12606字阅读需要40分钟，请耐心查看。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dOV641fyMUqjnp8PY8ig.png" alt width="777" height="378" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、表格定义</h2>
<p>表格是一种基础的数据展示形式，用来采集、整理、对比、分析数据信息的二维矩阵。几乎所有B端产品都要借助表格查询与处理数据，因此表格也被公认为数据最为清晰、高效的表现形式。</p>
<p>内容信息的排列、数据信息的展示、数据筛选工具栏的使用，数据操作按钮的摆放，这些都有对应的表格来解决，表格的形式也多种多样。表格的合理布局是提高表格可读性、感知不同数据信息之间关联与区别的重要手段。</p>
<p>在我们了解表格之前先从几个维度来探讨一下列表、表格、表单之间的联系与对比。</p>
<p><strong>列表</strong>，英文释义为List。以表格为容器，装载着文字或图表的一种形式，叫列表。</p>
<ul>
<li>展示形式：标签+数据+操作按钮；</li>
<li>数据结构：一对多；</li>
<li>常见模式：待办事项、走查清单、动态等；</li>
<li>前端类别：有序列表（<0l><li>）和无序列表(<ul><li>并列关系)。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dPR3nPGBNY9NrrVVsf8Z.png" alt width="777" height="378" referrerpolicy="no-referrer"></p>
<p><strong>表格</strong>，英文释义为Table，又称为表，即是一种可视化交流模式，又是一种组织整理数据的手段。主要承载数据的归纳、展示与对比的功能，是列表的一种。</p>
<ul>
<li>展示形式：标签+数据+操作按钮；</li>
<li>数据结构：一对多；</li>
<li>常见模式：excle；</li>
<li>前端类别：行（<tr>）、列(<td>)、表头（<th>）ps：在前端眼中列是由行拼接组成，没有单独列的概念。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/XH72wmE1ajyrUDIOoNBq.png" alt width="778" height="378" referrerpolicy="no-referrer"></p>
<p><strong>表单</strong>，英文释义为Form。表单在网页中主要负责数据采集功能。（详见我的文章《<a href="http://www.woshipm.com/pd/4369965.html">B端页面——详细表单设计流程</a>》）</p>
<ul>
<li>展示形式：标签+输入域+提示信息+操作按钮；</li>
<li>数据结构：一对一；</li>
<li>常见模式：登录页、个人信息录入等；</li>
<li>前端类别：这里的数据类型较多例如文本text、密码输入password、单选框radio、复选框checkbox等。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/vOJ64nzfkiUUQRvPVXMI.png" alt width="774" height="571" referrerpolicy="no-referrer"></p>
<p><strong>总结</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/jUJzEAIfYlFuPqEd0Ni3.png" alt width="777" height="306" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、设计原则与目标</h2>
<h3>1. 设计原则</h3>
<p>其基本设计原则是业务的全面整合，流畅的阅读体验，重要信息的快速检索，便捷的业务处理。满足业务需求+符合用户心智模型。</p>
<p><strong>1）好查找</strong></p>
<p>表格应该层级分明、一目了然，让用户更多地感受表格承载的内容信息而不是表格的形式。</p>
<p>对于提高表格查找效率，这里给出一些我个人的建议：</p>
<ul>
<li>保持一致，保持表格外观、布局一致，外观相同的表格用户会更快地接受，用户一次学习就可通用查看，凭肌肉记忆快速查找关键信息；</li>
<li>呼吸适中，表格内容区采用合适的行高和列宽，可以帮助更快地获取信息；</li>
<li>视觉降噪，通过字体、字号、颜色等多维度进行视觉降噪处理。</li>
</ul>
<p><strong>2）好处理</strong></p>
<p>表格应该是可交互的，对于查找好的数据能让用户迅速找到对应操作进行决策，如导出、编辑等的快捷操作处理。</p>
<p>处理交互提效建议：</p>
<ul>
<li>亲密性，数据选择与数据操作保持亲密性；</li>
<li>操作露出与操作隐藏，不同业务操作选择不同的操作形式，比用户多想一步。</li>
</ul>
<p><strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/L87vLn2irsaHApf6mDfu.png" alt width="774" height="229" referrerpolicy="no-referrer"></strong></p>
<h3>2. 设计目标</h3>
<p>对数据进行高效地查找、新增、编辑、删除等操作是用户对表格使用的终极目标。</p>
<h2 id="toc-3">三、表格构成</h2>
<p>从视觉角度出发将表格分为：标题、筛选操作区、表头、内容、底栏五部分进行构建。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/a55gMgYobfi0BseKFj9y.png" alt width="778" height="489" referrerpolicy="no-referrer"></p>
<h3>1. 标题</h3>
<p>对表格信息内容的整体概括，让用户对表格用途一目了然。标题内容可以包含数据来源、日期、地区等信息。同时在具体业务中也可结合图标对标题进行补充，帮助用户更形象地理解表格传达的内容。</p>
<p>标题作为重要的表示元素一般会放在表格的左上角，符合用户的阅读习惯，同时也能突出标题的重要性。但在有些情况严格意义上的标题则不存在，会被页面标题、面包屑或其他内容代替，主要看其能否表达对表格的概括。</p>
<h3>2. 筛选操作区</h3>
<p>两个区域常被称为工具栏，其实两个区的功能各不相同，也可以分开讲筛选区与操作区。</p>
<p>筛选操作区指方便用户快速定位查询数据与操作数据，是承载表格核心功能“增删改查”的重要桥梁。筛选操作区的排序方式对整个表格“好查找”起到了至关重要的左右，对不同的业务进行分析对筛选操作区进行排序变化。</p>
<h3>3. 表头</h3>
<p>表格信息是对数据属性的分类或基本概括，可以理解为表格总结，是用户快速浏览表格布局的关键信息，表头字段应当符合人们的思维惯性，保证大部分用户能理解数据。</p>
<p>表头也可以指行标签，是对所属行或列的描述。表头也可以承担一些简单的筛选、冻结与排序，方便用户对具体的行列进行筛选操作。</p>
<h3>4. 内容</h3>
<p>内容就是表格的主体区，表格的全部内容信息都在这里获取。内容区是由一个个的单元格组成，单元格所承载的内容就是内容的基本单位。</p>
<p>单元格的排列组成行或列，行/列中的数据可以是文本、计数、百分比、状态、操作等任何形式，在表尾还可以进行数据统计，例如合计、平均值等。</p>
<h3>5. 底栏</h3>
<p>底栏位于表格最下方，一般展示正文的数据概要信息，有时也做数据的分类统计，或者配合筛选操作区放置批量处理操作、备注说明等内容。</p>
<h2 id="toc-4">四、表格规范</h2>
<h3>1. 标题规范</h3>
<p>表格标题的示例展示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/TpcAbgFNxIoe9wuLmYx2.png" alt width="778" height="516" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示例：teambition项目截图</p>
<p>标题同时承担切换视图与分组的功能操作；飞书会议室管理标题随着右侧架构的变化进行变化，提醒用户当前表格显示内容；Prowork事项标题内容带表格展示日期的区间；TAPD查找过滤表格标题位于表格左上方鲜明扼要的表格展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/sLnirIBHDzCGpBvWTUKM.png" alt width="771" height="403" referrerpolicy="no-referrer"></p>
<p>上图标题使用图标样式，增加表格特征与归属感，强化品牌调性。</p>
<h3>2. 表头规范</h3>
<p><strong>1）表头类型</strong></p>
<p>根据表头的构成，可以分为以下三类：</p>
<ol>
<li><strong>纯文本表头</strong>——仅起到解释数据属性的作用；</li>
<li><strong>多功能表头</strong>——可以筛选、排序、搜索相关数据；</li>
<li><strong>多级表头</strong>——信息分类层级较多数据结构较为复杂的情况下使用。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/epxVGoC0tCGcZZKMFQiB.png" alt width="775" height="347" referrerpolicy="no-referrer"></p>
<p><strong>2）名称简化</strong></p>
<p>表头展示要注意以下几点：</p>
<ul>
<li>表头标签精简。检验标准：少一个字就会改变标签原意。</li>
<li>表头的表现形式与正文稍作区分，来凸显表头的可识别性。</li>
<li>表头标签与所在列数据对齐，完整显示标题。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PEE9ZvAJyBQULGXH3e01.png" alt width="778" height="274" referrerpolicy="no-referrer"></p>
<p><strong>可去掉表头</strong>：表格数据维度大，可以通过表格数据轻松判断表头标签，表头标签就可以省略。</p>
<p>例如电子邮箱的收件表格，每列数据的表示度都很高，去掉表头也能轻易阅读。在ProWork中待办事项表格也省略列表头。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/8LTM0gVSmq7NznCETQbE.png" alt width="778" height="274" referrerpolicy="no-referrer"></p>
<p><strong>3）提示信息</strong></p>
<p>当表头标签出现行业壁垒的专有名词或生僻字时，新用户期望搞清楚标签的含义，这时就要借用提示信息来对当前标题进行解释说明，老用户也不会因此而感觉页面冗杂。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/azbCyHNCmpkXVkNZzVI0.png" alt width="777" height="253" referrerpolicy="no-referrer"></p>
<p><strong>4）表头交互</strong></p>
<p><strong>功能复合型表头</strong></p>
<p>除了容纳行标签之外，表头也可以添加排序、搜索、筛选等功能，这些功能受列的影响，一般只能做单次筛选。通过对表头标签的筛选可快速完成筛选条件。</p>
<p>放置在表头标签上的筛选，受列内容的影响，一般做单次筛选。通过对表头标签旁按钮的点击，使用户更快捷进入到自己的筛选条件中。</p>
<p>通常，表单越左的列数据越重要的，也是筛选频率与需求最高的，因此高频的筛选场景基本可以得到满足。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/IxxPyWPxaoiJ9nj024ro.png" alt width="782" height="220" referrerpolicy="no-referrer"></p>
<p><strong>5）表头筛选</strong></p>
<p>表头筛选是一种列表内置筛选形式，类似Excel表格的操作。表头筛选和筛选区的筛选相比，只能筛选一列数据，能节约一定的空间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/g5ryfhQVpQ0Fut4Rqdo1.png" alt width="779" height="219" referrerpolicy="no-referrer"></p>
<p>虽然表头筛选能在一定程度上节约空间，但对于复杂业务的产品来说，不推荐使用，原因如下：数据信息列多，高频筛选功能可能会被遮盖，表头复杂影响用户表格阅读。</p>
<p><strong>6）表头排序</strong></p>
<p>通过对表格信息的排序可以帮助用户快速抓取有用的信息。</p>
<p>通常默认两种排序方式：升序/降序。</p>
<p>这种排序一般在表头触发，可以是正序或者倒序，按照一定的逻辑进行排列，例如是时间的表头则表示最近时间——最远时间或最远时间——最近时间排序。切换排序的逻辑一般认为是默认——升序/降序——降序/升序——默认之间来回切换，具体顺序根据业务确定。表头名称和切换图标都设置成操作热区更利于用户操作。</p>
<p>特殊排序方式较多时可以采用下拉选择直接有效展示，减少用户反复操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bEeXDTpRzXphuew0nvnA.png" alt width="780" height="373" referrerpolicy="no-referrer"></p>
<p><strong>7）固定表头</strong></p>
<p>表格垂直滚动时，对表头进行固定处理，可以帮助用户更快地找到单元格的属性和含义，尤其是单元格属性信息数据没有特征时（比如都是数字、百分比、姓名等）固定表头可以大大提高使用效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5RSeXDjdhxUlKXy5mNnx.gif" alt width="779" height="253" referrerpolicy="no-referrer"></p>
<p><strong>8）可配置列</strong></p>
<p>可配置列与配置筛选条件的功能类似，同样是考虑到不同角色的用户，查看数据的视角不一样，对应的关心的字段也会不一样。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/TdilnS7NjncUA1HxhRlk.png" alt width="778" height="277" referrerpolicy="no-referrer"></p>
<h3>3. 单元格规范</h3>
<p><strong>1）单元格</strong></p>
<p>单元格规范定义：字号、文字行高、上下左右边距、表格行高，这些部分要怎样确定呢？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/fk0HlYqY6w5ywKHRMexz.png" alt width="1280" height="256" referrerpolicy="no-referrer"></p>
<p><strong>① 字号</strong></p>
<p>在表格设计中一般采用正文字号大小按照具体业务的使用规范在12-16px之间，我一般在页面中使用14px大小的字号作为正文字号。</p>
<p><strong>② 文字行高</strong></p>
<p>与文字字号无关，是文字及其边距在页面上所占的位置高度，一般设置为字号的1.2-1.8倍大小，文字内容水平居中。</p>
<p><strong>③ 上下左右边距</strong></p>
<p>上下边距可以设置为字号大小的1-1.5倍大小，左右边距根据业务需求设置固定大小12-24px或者更宽均可，但要注意同一产品表格规范要保持相同。</p>
<p><strong>④ 表格行高</strong></p>
<p>在前面三项配置完成后就得到了具体的表格行高。单元格较为常见的高度区间在56-80之间。由于设备的差别，为了让产品都能有最好的展示效果，在表格上也会设置不同的行高，让用户根据不同的场景进行选择紧凑、舒适、宽松的行号模式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/0pcow2GPqH1Smqx9nLvr.png" alt width="777" height="253" referrerpolicy="no-referrer"></p>
<p><strong>2）盒子模型</strong></p>
<p>盒子模式是最为基础的前端框架，每个页面都是由无数个盒子构成。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/R9hVEQnEgiYWiZbzdnVL.png" alt width="775" height="292" referrerpolicy="no-referrer"></p>
<ul>
<li>Margin（外边距）：指内容的外边界与相邻元素之间的间距，外边距为透明。</li>
<li>Border（边框）：指环绕在内容周围的边框路径。</li>
<li>Padding（内边距）：指内容的外边界在其他子元素的间距。</li>
<li>Content（内容）：指最基础的内容元素。</li>
</ul>
<p>想要知道线上页面的具体数据，可以用谷歌浏览器更多工具——开发者工具进行检查。</p>
<p>如下图飞书的会议室表格，Padding内边距为12px/8px，在单元格中对应左右边距12px/上下边距8px；表格行高为57.26px，正文本字号为14px；margin外边距为4px，可以看到两行文本之间的间距。用这种方法可以通过多个盒子的查找来参考线上页面的单元格规范，来进行我们自己业务产品中的单元格规范。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dURVLVqjxZjeykvj5dOa.png" alt width="781" height="294" referrerpolicy="no-referrer"></p>
<p><strong>3）单元格合并</strong></p>
<p>对于特殊的数据类型多行或者多列共用同一数据时，可以进行单元格合并如下图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/vkJ6zFmrbuaHIXyZZSLy.png" alt width="777" height="253" referrerpolicy="no-referrer"></p>
<p><strong>4）关键数据</strong></p>
<p>单元格数据一般有文字、图标、头像、进度等，而对于较为重要的数据可以进行关键数据的标识设计，这些数据往往是用户最关心的数据，例如数据状态、数据的上升或下降等。</p>
<p>在具体业务中，如果你找对了用户想看的关键数据，将会大大提升用户体验，反之则干扰用户查找信息。这就要求我们在前期调研时用户使用场景的高度还原，尽可能多地站在用户的角度思考。</p>
<p><strong>① 标签</strong></p>
<p>关键数据较多，颜色与视觉重量要做区分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/I5H1rWh1Z386LvfDK8Om.png" alt width="777" height="253" referrerpolicy="no-referrer"></p>
<p><strong>② 图标</strong></p>
<p>名称与文件类型图标区分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tNQa2oGMwGLBmhvtxZFU.png" alt width="779" height="210" referrerpolicy="no-referrer"></p>
<p><strong>③ 人员信息</strong></p>
<p>人员信息展示在表格中也十分常见，通常会用头像+名称的方式，例如下图temabition和飞书中对人员信息的展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/sopyGZJT534oK5YDsswD.png" alt width="778" height="473" referrerpolicy="no-referrer"></p>
<p><strong>④ 进度条</strong></p>
<p>进度条或简单的数据图，它更能直观地展示数据的进度状态，方便用户对数据信息做判断如下图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/6GSEVVbiAF6pBbSmAhdi.png" alt width="775" height="530" referrerpolicy="no-referrer"></p>
<p><strong>⑤ 空表格</strong></p>
<p>表格数据为空时要给予一定的提示信息或快捷操作，让用户更快地进行对数据的操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/oR9lKmODjr2oSErzYWjk.png" alt width="777" height="341" referrerpolicy="no-referrer"></p>
<p><strong>⑥ 空单元格</strong></p>
<p>表格中的空数据要使用“-”短横线符号进行填充，数据为“0”时请使用“0”填充，避免数据为空造成用户困扰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7Vg9WQNbguXuHu1IfSZP.png" alt width="779" height="264" referrerpolicy="no-referrer"></p>
<p><strong>⑦ 数据过多</strong></p>
<p>单元格内数据信息过多 时可以采用“…”进行省略展示，鼠标悬停或点击查看省略的内容信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZeqgfhJu5NCKa2LTOjbV.png" alt width="779" height="199" referrerpolicy="no-referrer"></p>
<p><strong>5）单元格交互（可弹窗、可卡片、切换视图）</strong></p>
<p><strong>① 单元格编辑</strong></p>
<p>单元格编辑是对单条数据的修改，直接在单元格编辑信息的形式有很多，针对不同的数据提供对应的编辑方案。</p>
<p>编辑名称：鼠标移入显示编辑图标，点击图标按钮后原位光标编辑，编辑完成后随意点击空白处完成编辑退出光标。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/aiPnRwFR3hlugZj6eKG6.png" alt width="778" height="214" referrerpolicy="no-referrer"></p>
<p>状态编辑：下拉选择切换状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/IOsxMbNUm4O0pUimw2bN.png" alt width="785" height="216" referrerpolicy="no-referrer"></p>
<p>人员编辑：下拉选择切换人员并提供模糊搜索对人员信息进行搜索。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/N3lJU1rt1zEuUd5qDuCf.png" alt width="773" height="294" referrerpolicy="no-referrer"></p>
<p>时间编辑：下拉时间选择器，默认展示当前时间，点击日期切换时间，切换后确定完成编辑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/0aAxaq0bPmTi7zNNaOgT.png" alt width="778" height="296" referrerpolicy="no-referrer"></p>
<p>长文本编辑：弹出简易富文本编辑器，输入编辑内容后，点击空白处退出完成编辑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/gHwgWJXVFtXbArCPxYBM.png" alt width="775" height="209" referrerpolicy="no-referrer"></p>
<p>上述罗列的常见单元格编辑形式供您参考，针对不同的业务性质对单元格采用不同的交互形式。</p>
<p><strong>② 视图切换</strong></p>
<p>可以通过视图切换查看更多细节，例如在teambition中支持对任务的表格/列表/看板三种视图的查看，每种视图的侧重点不同，可以适应不同角色用户的不同专注点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RECiCywmRz3e9PsCifXt.png" alt width="778" height="614" referrerpolicy="no-referrer"></p>
<p><strong>③ 信息完整度</strong></p>
<p>当单元格内数据过长进行”…”省略处理后，通过鼠标hover弹出气泡来展示完整的数据信息，这时气泡的位置出现在单元格的什么方向最为合理呢？为此，我找到了下面三种做法。</p>
<p>这里我推荐的是答案例1的做法，把hover气泡显示在单元格的上方，因为这样设计符合用户的视觉动线，用户从左到右从上到下对表格进行浏览查找，气泡出现在上方可以不干扰用户紧接着的发生的视觉动作。</p>
<p>还要注意气泡的面积不宜过大，如业务必要可在气泡中增加滚动。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Ga9sXO5biR6tJ4HjhpA4.png" alt width="775" height="737" referrerpolicy="no-referrer"></p>
<p>除了对文字信息的气泡展示以外，还有可以对信息进行更多收纳，利用卡片进行详细信息展示，可以展示文字、图形、数据图等更多维度的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/9fnb5KnYU9lON8MrgluB.png" alt width="777" height="381" referrerpolicy="no-referrer"></p>
<h3>4. 行规范</h3>
<p><strong>1）行高规则</strong></p>
<p><strong>单元格数据内容不同如何确定行高？</strong></p>
<p>对于单行显示数据内容的表格，建议行高约为内容高度的2.5-3倍；对于多行显示数据的表格，建议行中内容的最高点与最低点到行框的上下边距略小于文字高度。</p>
<p><strong>① 固定表格行高</strong></p>
<p>当数据有单行信息展示有多行信息展示时（或长度不固定），要定义内容的行数（根据业务），根据行数确定行高多出的内容做省略处理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OPUO2JpeHusklY21NhQa.png" alt width="777" height="221" referrerpolicy="no-referrer"></p>
<p>固定行高时可以规范几种不同的表格行高，例如在我日常工作中规定了3种行高56px80px110px，行高较高时，我们数据内容都进行居中对齐就会有一些问题。有些单元格只有一行信息，有些有多行信息，会使页面看起来更混乱，信息查找速度降低（如图1）。</p>
<p>对此我们进行了进一步的规范，当行高小于80px时数据信息居中对齐，表格行高大于80px 时数据信息都居顶对齐，如下图2。顶对齐可以让用户查找信息时有坐标依据，更加快速。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5soxWgWmNObE7a9n7LbY.png" alt width="774" height="252" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/mVnBQUxidhqI0o71BIU2.png" alt width="779" height="425" referrerpolicy="no-referrer"></p>
<p><strong>② 流体表格行高</strong></p>
<p>在elementUI组件中，表格行高跟随行内占用最多行数的单元格变化，设置固定的上下边距，表格行高随着数据信息的换行而变化如下图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QIQJVuaV402K71Crb3cr.png" alt width="781" height="426" referrerpolicy="no-referrer"></p>
<p><strong>2）行的视觉强调</strong></p>
<p>为了强调行内信息的连续性，或采用行的分割线或者斑马纹来进行行的强调。</p>
<p>分割线的分割较为弱，对用户的视觉干扰小。</p>
<p>斑马纹又称作隔行换色、行的交替样式。它能很好地区分相邻两行，有效降低读错行的情况，同时能够加强对用户横向阅读的引导。但在设计时要尽量的减少色的反差，还要注意区分hover态与斑马纹，避免造成视觉干扰，可以根据实际情况添加1px的行版框。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/fVfnVvJIA0C1LJvbvcli.png" alt width="780" height="312" referrerpolicy="no-referrer"></p>
<p><strong>3）交互</strong></p>
<p><strong>① 行新增</strong></p>
<p>对于与一些较轻量的数据新增可以采用表格新增行内容。新增行后，要定位高亮显示所在行，让用户快速聚焦。</p>
<p>新增完成后可延时几秒高亮消失，避免过度干扰用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/fMDn0YWiPUkpYQFRr45Z.png" alt width="779" height="244" referrerpolicy="no-referrer"></p>
<p><strong>② 行编辑</strong></p>
<p>行内信息的编辑可以在鼠标hover 时单个进行编辑，也可以在行尾操作区点击编辑按钮进行全部编辑操作。</p>
<p>当然行的编辑操作是直接在表格内操作还是弹窗、抽屉、新页面的交互选择，要根据具体的业务内容与编辑信息体量来判断，这里建议与新增行信息的交互选择相同，如果新增操作是表格原位新增行那么编辑也可以采用同样的交互方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/TkAgXQ8MpmGDFyEgqSUr.png" alt width="779" height="244" referrerpolicy="no-referrer"></p>
<p><strong>③ 行排序</strong></p>
<p><strong>按逻辑排序</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/il4Rxbe6hK4Mj922wZlW.png" alt width="779" height="291" referrerpolicy="no-referrer"></p>
<p><strong>拖曳排序</strong></p>
<p>拖拽排序为用户的自定义排序，在用户拖拽时页面布局保持不变，适用于数据量较小有自定义排序的情况下。</p>
<ul>
<li>拖拽前：要让用户知道这个表格行是可以拖拽的，可以在每行首添加图标、鼠标hover改变光标样式等。</li>
<li>拖拽时：要让用户知道拖动的动作的效果，对于拖出位置给予一定的样式保留，让用户知道从哪行移出的，对于目标位置，给予一定的插入位置符号提示（虚线）或拖入后预览反馈。</li>
<li>拖拽后：及时更新表格信息，如有排序编号等数字可在排序后更新。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/JIaWoLUfDf5G456ztNWr.png" alt width="775" height="232" referrerpolicy="no-referrer"></p>
<p><strong>④ 行密度调节</strong></p>
<p>用户使用的显示屏都不尽相同，同一个行高设置在不同的设备中展示的效果也不大一样，会影响用户的阅读效率，对行高的密度设置可以提高用户体验。</p>
<p>较小的行高可以增加信息的展示效率，一屏展示更多的内容，但也容易在高密的表格中迷失。低密度的行高更高，数据的的层级展示就更加清晰。</p>
<p>具体的设置形式，可以根据表格的具体情况，操作按钮少时，可直接放与表格上方做成标签的样式让用户进行切换，表格复杂按钮较多时，可以收起在工具栏中，进入设置再更换显示密度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Aq1Mxb2WExulewZcdk2H.png" alt width="778" height="380" referrerpolicy="no-referrer"></p>
<p><strong>⑤ 展开行</strong></p>
<p><strong>展开信息</strong></p>
<p>行的展开与折叠，可以把行内无法展示的附加信息放在行下折叠收起，点击行首的展开按钮即可查看，防止用户因弹出新交互而迷失方向。</p>
<p>折叠的信息适合重要度低的主行展示不下的辅助信息，也可以避免表格的横向滑动，但如果想要同时查看多条展开行，则需要多次店家展开按钮进行查看。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/QdIBiOYQW3l2jb4RVuTv.png" alt width="778" height="398" referrerpolicy="no-referrer"></p>
<p><strong>⑥ 展开表格</strong></p>
<p>与展开行类似，这里展开内容为与当前行相关的另一子表格，这个表格有独立的表头、行、列，子表格用于对当前行信息的补充与说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/d3QQeFzLwwdSEdomBonW.png" alt width="780" height="399" referrerpolicy="no-referrer"></p>
<p><strong>⑦ 展开树表格</strong></p>
<p>展开的表格与当前表格共用同一表头，整体表格呈树型，展开的表格与当前行呈父子关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/p0zuMza3ZpYGqXODSugB.png" alt width="778" height="206" referrerpolicy="no-referrer"></p>
<h3>5. 列规范</h3>
<p><strong>1）列宽规则</strong></p>
<p><strong>① 列的宽度</strong></p>
<p>列宽的设置对于用户的高效阅读还是很有作用的，在设计时要根据具体的业务信息进行分析。</p>
<p>列信息内容长度固定时：（例如手机号、性别、身份证号等）可以设置为固定的列宽。</p>
<p>列信息内容长度不固定时：要根据产品设置的最大字符数与用户数据来进行设置。</p>
<p>如组织名称，字符限制为60，如果表格数据内容很少，可以全部展示60个字符时则全部展示；当内容较多时要根据大部分的用户数据设置表格中最多展示的字数（例如组织名称：某某某集团有限公司市场拓展与服务部第一党支部；某某某集团有限公司产品事业部第一党支部……）。</p>
<p>大部分数据都是某公司名称前缀的展示信息，在设置展示内容时最少也要保证公司名称前缀之后三个字的展示，才能让用户大致区分数据差异。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xmSdmnKlGLVn39twSWc3.png" alt width="777" height="221" referrerpolicy="no-referrer"></p>
<p><strong>② 列的间距</strong></p>
<p>列与列之间的间距保持相同大小，首列尾列与表格边缘的间距保持相同。</p>
<p>列的间距n1 保持不变，n2定义最小值，随着页面的尺寸自适应变化（我的参考：n1固定值定义为12px，n2最小值定义为24px）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OyWl7PjfGhjDmJykrpdG.png" alt width="774" height="484" referrerpolicy="no-referrer"></p>
<p><strong>③ 列的数量</strong></p>
<p>列的数量建议最多展示9条，因为人们的记忆在7±2之间，数据太多用户会找不到重点。但也不是必须，根据业务需求，如果需要大量数据展示时也要展示，因为视觉永远低于业务（好用比好看更重要）。</p>
<p>列信息从左往右视觉权重程度逐渐降低，最后一列权重高（以眼动实验或点击数据为依据得出权重高低），所以在我们的列信息展示把更重要的信息放在左边。展示不下的数据放入详情页。</p>
<p><strong>2）列的视觉强调</strong></p>
<p>列的视觉也可以根据业务需求做引导，一般配合排序或比较使用，比如数据或同类信息的对比性。</p>
<p>常见的表现形式有两种：分割线、填充底色。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/FLPU8amaulMjIYEX34u9.png" alt width="779" height="487" referrerpolicy="no-referrer"></p>
<p><strong>3）列的交互</strong></p>
<p><strong>① 列宽自定义</strong></p>
<p>在一些用户高度自定义表格中，数据的列宽不好确定的情况下，可以允许用户对列宽进行调节。</p>
<p>通过光标的变化提示列宽自定义操作，拖动可完成列宽设置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Tv1UCTAH04Tj0pELgIkh.png" alt width="776" height="266" referrerpolicy="no-referrer"></p>
<p><strong>② 列自定义</strong></p>
<p>列数据还可以根据用户需求进行自定义设置，可以选择要展示的列，也可以对列进行排序。</p>
<p>例如下面两个案例，都是在表格右上方的设置按钮对表格进行设置，清晰高效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/GYWSeKb5KllwL62glGLy.png" alt width="775" height="327" referrerpolicy="no-referrer"></p>
<p>通常系统会记住你上次的自定义设置，作为这次展示的默认形式。</p>
<p><strong>③ 滚动与固定</strong></p>
<p>表格数据量过大页面无法展示时，不得不采用水平滚动或横向拖拽来阅读数据。</p>
<p>滚动带给用户的是不稳定性，容易迷失，就需要固定重要信息作为参照让用户稳定下来。这时固定首列一般是最优解，让用户滚动数据时也能得到固定的参考，提高查找效率。</p>
<p>同时固定表尾可以方便用户找到对应信息后及时操作。如下图element组件库：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/FwiBO87FA0u6Sen9JSGT.gif" alt width="776" height="286" referrerpolicy="no-referrer"></p>
<h3>6. 表格整体规范</h3>
<p><strong>1）视觉降噪</strong></p>
<p><strong>① 留白</strong></p>
<p>表格留白，包括表格内部空间（padding）的留白和视觉留白。</p>
<p>内部空间要保证表格的可读性，视觉留白可以考虑操作按钮hover展示、更多收起等，表格颜色区分、icon 等手段来优化表格信息使其看起来更加易读。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/iPKlusXMEP9KF3X00R9e.png" alt width="781" height="222" referrerpolicy="no-referrer"></p>
<p><strong>② 减少分隔线</strong></p>
<p>不同的分隔线适用于不同的业务表格：</p>
<ul>
<li>横向分隔线：可以适用大部分数据集表格业务，是目前最常见的一种类型。</li>
<li>纵向分隔线：适用与对列之间产生数据对比的表格业务，可以局部适用列分隔线或斑马线。</li>
<li>矩阵分隔线：适用于数据非常严谨的数据场景，或者是表格没有空间留白的情况采用矩阵分隔线。</li>
<li>极简留白：表格留白空间足够，可以清晰地区分数据信息，在阅读时不需要适用辅助帮助的，可以采用此种样式。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/2fzixilrIJMO6HilRbAd.png" alt width="780" height="603" referrerpolicy="no-referrer"></p>
<p>分隔线要在数据允许的情况下尽量减小视觉占比，强调数据之间的对比与阅读效率。</p>
<p>最好不使用斑马线，对于同一类数据来说斑马线的使用是没有必要的，斑马线的视觉占比较重，虽然对数据的区分最明显，但也是最干扰视觉效率的分隔线。</p>
<p>可以省去分隔线，对于数据项较小的表格来说，可以尝试去掉分隔线。由于表格数据量小，表格内有合适的留白，也可以获得清晰了然的表格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/8YCk7IjfBVD7IDt6bi6G.png" alt width="778" height="602" referrerpolicy="no-referrer"></p>
<p><strong>③ 尽量以黑白为主</strong></p>
<p>表格的颜色尽量采用黑白色，较多的颜色会造成视觉层级的混乱，让用户迷失不知道什么是重要信息。在需要引导的地方采用颜色可以增强视觉层级，获得用户的更多关注。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/BbgSHdSsz7AefdlToywY.png" alt width="777" height="534" referrerpolicy="no-referrer"></p>
<p><strong>④ 克制使用图标</strong></p>
<p>图标的使用可以更形象地传达信息，但在严谨的表格中要尽量减少图标符号的使用，因为图标符号可能会使你本就繁多信息的表格变得更加复杂，而且为了避免用户对图标产生奇异还会加上文字说明，这样一来就会更加复杂。去除不必要的视觉干扰对表格来说是十分必要的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5wSg5NjiOCQxsahY6SQ0.png" alt width="779" height="505" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">3）操作交互</strong></p>
<p>表格的操作分三类讨论：单行操作、批量操作、全局操作。</p>
<p>三类操作是针对操作对象范围而命名的，单行操作是针对一行信息进行操作，例如编辑、查看详情等；批量操作是针对部分/全部信息进行批量操作，例如删除、导出等；全局操作是针对全部信息进行操作，例如新增等。</p>
<p>针对每一种操作类型进行不同的布局规划是提高表格“好处理”的重要手段。</p>
<p><strong>① 单行操作</strong></p>
<p>单行操作这里把针对单元格的内联操作也纳入其中。</p>
<ul>
<li>内联操作 ：是针对单个单元格的操作，具体操作形式前面单元格已做详细阐述。</li>
<li>单行操作： 一般操作放置在表格的最后一列。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/B9tT0Y3voTiy5OfEooyU.png" alt width="772" height="258" referrerpolicy="no-referrer"></p>
<p><strong>操作项聚合</strong></p>
<p>一般采用带颜色的文字作为操作按钮区分，当操作项不超过3个时直接展示，4个及以上操作时操作项采用“···”进行收起，点击更多弹出操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/HxNQADqjHNsb0WofDWiA.png" alt width="772" height="258" referrerpolicy="no-referrer"></p>
<p><strong>实例展示</strong></p>
<p>对于这样的多个操作因数据不同操作不同的状况要怎样进行设计呢，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qgGT3pWvu4RycXWW9Dlh.png" alt width="778" height="260" referrerpolicy="no-referrer"></p>
<p>这种可以有效的提高误操作但占用较大空间；用上述收起方案可以解决误操作和占用空间问题，但展开后操作项各不相同会让用户迷茫。</p>
<p>如果没有足够空表格空间，可以把操作项都放在详情页处理操作的方式，如下图单击首项进入表格详情。</p>
<p>从开发来讲迭代更加方便，节约开发成本；从用户来讲，界面认知成本低，利于用户学习操作；从“好处理”原则上说也可以让用户明显认知目标操作，不会产生误操作，有利于用户对信息的获取。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/enBI59jhR3P3IJwUC3hK.png" alt width="775" height="224" referrerpolicy="no-referrer"></p>
<p><strong>操作按钮</strong></p>
<p>可以对通俗的操作按钮使用图标表示，但操作项的形式需保持一致，建议采用文字直截了当的展示更加高效。·</p>
<p><strong>隐藏操作项</strong></p>
<p>也可以对单行操作采用hover 展示，单击后根据业务类型展示气泡、卡片、弹窗、抽屉、跳转等交互（可以查看表单页面文章了解详情）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/eBvkRZLTaplAjiYZbDCu.png" alt width="775" height="224" referrerpolicy="no-referrer"></p>
<p><strong>② 批量操作</strong></p>
<p><strong>批量选择</strong></p>
<p>批量选择一般在表格首列采用复选框进行选择，可以选择单项/多项/全部。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/XkSXNjQXURVlQDZLgkfT.png" alt width="779" height="305" referrerpolicy="no-referrer"></p>
<p><strong>复选框位置</strong></p>
<p>在首列，可以在不查看表格详细内容的前提下进行选择；在尾列，需要查看所有的表格信息后决定是否进行选择。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/zqYWEKlXri7DmBOPQtio.png" alt width="779" height="305" referrerpolicy="no-referrer"></p>
<p><strong>复选框选择范围</strong></p>
<p>对树表格的选择规范，表头全选时父表格与子表格内容都全选；父表格不勾选时下属的子表格都不被选择；也可以只勾选子表格不勾选父表格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/oawP6oKDVivjPKtDMJdv.png" alt width="779" height="305" referrerpolicy="no-referrer"></p>
<p><strong>批量选择范围</strong></p>
<p>可以进行筛选选择，表现为表头复选框右侧的下拉操作，常用于用于业务复杂场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ve8iiigoXv0pJXYKDeYQ.png" alt width="775" height="221" referrerpolicy="no-referrer"></p>
<p>可以筛选状态也可以筛选当页或者全部页，选择时告知用户是否是当页还是全部页。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/C8uMAmTedDIl1UmxqlvQ.png" alt width="782" height="306" referrerpolicy="no-referrer"></p>
<p><strong>已选项展示</strong></p>
<p>告知用户已选项数，最好跟在复选框后方便查看。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/0uXY1uxPtlOzsm02XDeR.png" alt width="779" height="222" referrerpolicy="no-referrer"></p>
<p><strong>③ 批量操作</strong></p>
<p><strong>操作按钮位置</strong></p>
<p>批量操作与批量选择是配合使用关系，按使用场景选择同时放于表格上方、下方或同时放置，在选中复选框后激活批量操作按钮，符合用户心理预期，节省操作时间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/kp6JTK1CSKBAmgAczT5I.png" alt width="780" height="342" referrerpolicy="no-referrer"></p>
<p><strong>隐藏操作</strong></p>
<p>有的表格的设计会对批量操作进行隐藏在勾选时才展示，这样操作对新用户不太友好，新用户无法预知批量操作有哪些，有可能会找不到“导出”按钮以为没有上线此功能，在设计表格时要考虑这个问题。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/cS36QlpHgYv4c20kHL6M.png" alt width="778" height="212" referrerpolicy="no-referrer"></p>
<p><strong>二次确认</strong></p>
<p>需要对一些批量操作进行二次确认，一般采用模态弹窗对用户进行强打断，以确保用户不是误点。</p>
<p>操作完成后提示用户操作结果，无任何操作后15秒消失。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/lPcUNreCNpPiJ5DDNbOA.png" alt width="777" height="269" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/kgnkmCuN6RO552ceTS8M.png" alt width="780" height="270" referrerpolicy="no-referrer"></p>
<p><strong>④ 全局操作</strong></p>
<p><strong>操作布局</strong></p>
<p>全局操作一般位于表格最上方，对全部表格起到约束统筹作用，操作对全部表格生效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/0xRtr32xXEdMkbzue0mF.png" alt width="784" height="169" referrerpolicy="no-referrer"></p>
<p><strong>操作样式</strong></p>
<ul>
<li>视觉：主按钮一般为主色填充，次按钮为灰色描边，突出主按钮样式。</li>
<li>交互：一般点击添加类按钮，会出现包含添加项目数据的表单。</li>
</ul>
<p>表单设计注意点：</p>
<p>创建数据应填写最小数据项，例如Prowork只填写项目名称就可以创建新项目，让用户用最小成本创建数据可以在详情编辑更多数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NlZGaSAaGkzYZHeMwBrv.png" alt width="779" height="263" referrerpolicy="no-referrer"></p>
<p>有连续创建需求的业务要为用户提供快捷方式 。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/azhT6lJg2YUOqo5BvxEW.png" alt width="779" height="263" referrerpolicy="no-referrer"></p>
<p><strong>4）搜索与筛选</strong></p>
<p><strong>① 搜索</strong></p>
<p>用户输入搜索可以快速定位数据条目。搜索尽量采用模糊搜索，让用户通过少量关键词进行查找。</p>
<p>触发方式有“实时筛选”和“点击按钮触发筛选”。实时筛选只适合数据量较小、数据严谨的表格页面，请谨慎使用。“点击按钮触发筛选”适合大部分表格场景。</p>
<p>根据其表现形式，可以分为以下四种类型：单标签精确搜索、多标签精确搜索、多标签模糊搜索以及多标签组合搜索。</p>
<p><strong>单标签精确搜索</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/9kQrZmddn8ncwYYcMYeG.png" alt width="780" height="203" referrerpolicy="no-referrer"></p>
<p>适用场景：表格单一数据信息特征突出，可以用此数据标签快速定位目标数据，通常这个数据标签识别性高、使用频率高。</p>
<p><strong>多标签精确搜索</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OEbLqZG0uKQ01fSCs3XZ.png" alt width="788" height="205" referrerpolicy="no-referrer"></p>
<p>适用场景：表格多个数据都具有特征，往往业务要求对数据的精确度较高。</p>
<p><strong>多标签模糊搜索</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/UoNgatwlIWa7RtQDwqpT.png" alt width="780" height="203" referrerpolicy="no-referrer"></p>
<p>适用场景：业务类型多样用户可能记忆不精确且有多个数据特征，对搜索的便捷性要求高精确性要求低。</p>
<p><strong>多标签组合搜索</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/INS9mZheBSNOoHWen5xn.png" alt width="780" height="203" referrerpolicy="no-referrer"></p>
<p>适用场景：综合筛选项，对空间的利用率高，多标签组合搜索可以得到较为精准的搜索结果。</p>
<p><strong>② 筛选</strong></p>
<p>筛选是将用户所需数据选出展示，其余数据暂时隐藏，表格数据类型较多时可以使用筛选的使用。</p>
<p><strong>tab切换</strong></p>
<p>筛选条件数据无交叉、数据类型在5个以下的建议采用tab页切换的方式进行交互，展示清晰，用户操作效率高；超过5个可以考虑下拉选择或模糊搜索。</p>
<p>例如teambition表上的任务切换，一个会议只可能对应一个会议状态，会议状态固定且数量不多，平铺的tab切换筛选则能很好解决用户会议状态筛选的需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/VhkndpA6KocSeOlgekjn.png" alt width="776" height="202" referrerpolicy="no-referrer"></p>
<p><strong>矩阵筛选</strong></p>
<p>筛选条件很多，单独筛选条件对应数据无交叉，常见于信息密集型产品，可以承载多维的数据信息。选中项的可见性也十分友好，用户理解成本与操作成本低。</p>
<p>缺点是占用太多页面空间，会压缩用表格的占比，影响首屏的展示效率，可以区分高频和低频的筛选项折叠展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/j42UgpyC09zD8H8spekt.png" alt width="780" height="340" referrerpolicy="no-referrer"></p>
<p><strong>录入筛选</strong></p>
<p>录入筛选是最常用的筛选交互。在表格上方设置筛选条件，根据用户的使用频次排列，高频在前低频在后，如果筛选条件很多，可以折叠。</p>
<p>筛选条件在顶部，可以兼容多种数据类型（数字、文本、标签、布尔值等），便于从多个维度筛选，应对各种复杂的筛选情况。因为筛选条件存在交叉，建议布局在顶部，条件选择完后，选择触发筛选（若筛选条件不交叉可以选择实时筛选）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/CbaFw1ROV2ofoHd07mGM.png" alt width="778" height="339" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/YrO2VkhknOyBJlU13jc6.png" alt width="781" height="263" referrerpolicy="no-referrer"></p>
<h3>7. 对齐规范</h3>
<p>表格中数据信息的对齐遵循一定的规则会让表格更好查找，提高效率。</p>
<p><strong>1）文本型数据左对齐（包括日期等非比较性数字）</strong></p>
<p>文字信息的阅读习惯一般是从左向右、从上到下。按照阅读习惯进行文字排列。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ykpomWGTCKzzzRD6DcBu.png" alt width="777" height="181" referrerpolicy="no-referrer"></p>
<p><strong>2）数据型数据右对齐（带小数点的以个位数为基准）</strong></p>
<p>数字的阅读习惯是从右向左，用户会先看个位再看十位、百位、千位等来确定当前数据的单位大小。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/gRVD92PKW2wowPAqPQ6s.png" alt width="777" height="181" referrerpolicy="no-referrer"></p>
<p><strong>3）固定字段居中对齐</strong></p>
<p>比如日期（2020-11-11），状态文字（未审核等）或者布尔关系的文本（是/否等），字段固定不变，居中对齐能更好地信息呈现。这里说明根据业务也可以按照文本型左对齐处理，让用户查看表格不会感觉混乱。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/pEV8g33H2OmlVMyiRk8B.png" alt width="773" height="180" referrerpolicy="no-referrer"></p>
<p><strong>4）表头与其数据对齐方式相同</strong></p>
<p>对齐方式保持相同可以使表格更好阅读，上下文保持一致。</p>
<p><strong>多级表头</strong></p>
<p>多行或多列合并居中对齐，最底层表头可以按其数据对齐方式对齐。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/XWx22MKhO10Jbc64BVod.png" alt width="780" height="134" referrerpolicy="no-referrer"></p>
<p><strong>5）最后一列操作列右对齐</strong></p>
<p>使表格更加规则，视觉统一提高操作效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tcorpuQUuUmsbvueAdz4.png" alt width="782" height="182" referrerpolicy="no-referrer"></p>
<h3>8. 字符规范</h3>
<p><strong>1）数字单位的选择与使用</strong></p>
<p>表格中的数据要根据数量级确定展示形式，不需要精确的数学呈现，可以让用户更快地查找信息，下面是展示形式的建议。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qAwqwQUXJLuCbTnjCq7G.png" alt width="782" height="182" referrerpolicy="no-referrer"></p>
<p>数据的度量单位无需重复标注，只需要在表头标识清楚即可，注意同一列单位保持一致。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/fbVKXUtPB2h9yGkgRusB.png" alt width="786" height="183" referrerpolicy="no-referrer"></p>
<p><strong>2）减少用户计算</strong></p>
<p>深入了解用户需求，根据需求为用户提供差值、升降变化、合计值、平均值等直接展示形式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dd32cAuQGCEDBSnoFRtr.png" alt width="782" height="182" referrerpolicy="no-referrer"></p>
<p><strong>3）空数据处理</strong></p>
<p>对所在表格的空数据不要进行置空不管，用“-”表示该数据不存在，若数据为0则表格填充为“0”表示，用户会更加明确。</p>
<p><strong>4）字体使用</strong></p>
<p>表格中字体保持一致，文字信息字体统一、数字信息字体统一即可。</p>
<p>数字信息字体选择——建议等宽等高字体，方便数字比较。</p>
<p>推荐一下几款等宽等高字体使用：微软雅黑<strong>、Arial、sans-serif。</strong></p>
<p>下图左侧为苹方字体右侧为微软雅黑，右侧可以快速对比数据差异。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bmdZc70KnhRoR4r4974N.png" alt width="780" height="391" referrerpolicy="no-referrer"></p>
<h3>9. 分页规范</h3>
<p><strong>1）分页</strong></p>
<p>分页可以将表内容信息划分成独立的页面来显示。</p>
<p>分页并不属于表格当中的必要构成，但当数据超过所设定的阈值时，就需要使用分页来分布加载数据，所以分页和表格是经常联系在一起的。</p>
<p>分页也可以根据不同的场景业务需求从简易型、基础型、完整型中选择最优的设计方案。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/t27olgFxnKGx7go5EnhE.png" alt width="778" height="305" referrerpolicy="no-referrer"></p>
<p><strong>2）无限滚动</strong></p>
<p>除了分页的使用还可以进行无限滚动的交互，例如下图的查看更多按钮，这个功能不太适合数据量较大的表格，在具体业务中一定要慎用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZkpQl8bTYlxgZe7IGyBb.png" alt width="781" height="227" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、表格应用场景</h2>
<h3>1. 基础表格</h3>
<p>基础表格是根基，是由行与列的单元格组成。在使用层面上能满足用户多维度查看数据的需求。因为大家都很熟知，在这一章节并不是主角，我们就不做过多赘述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/K0aFgU248YDmOo9PzDZY.png" alt width="781" height="478" referrerpolicy="no-referrer"></p>
<p>从上往下堆叠，数据过滤模块在最上方，过滤数据后，用户再由总体到具体的的浏览逻辑理解和分析。</p>
<p><strong>什么时候使用：</strong>每条条目需要都需要露出很多字段；用户在搜寻条目时有准确的查询范围时使用。</p>
<h3>2. 双栏表格</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/8sNQBVWF4BtIivpjZNYI.png" alt width="781" height="478" referrerpolicy="no-referrer"></p>
<p>将数据过滤模块放置在侧栏，当过滤条件过多、横向空间充裕时使用。</p>
<h3>3. 树形表格</h3>
<p>当表格中的数据为包含与被包含的结构时，可采取树形表格。</p>
<p>通过逐级大纲的形式来展现数据间的层级关系，让整个信息结构变得一目了然。这一表格形式常出现于项目管理工具中，比如 Teambition、Tapd、都有这样的设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/dlWheCYAJARAtlGPwyFy.png" alt width="782" height="375" referrerpolicy="no-referrer"></p>
<h3>4. 嵌套表格</h3>
<p>当一条主数据下有多条数据结构不同的关联数据进行嵌套时，这时候就可以用子表格进行创建。</p>
<p>它能够对主数据进行更加细致地解释，详细地了解主数据中数据的含义。从表象上看，就是在一个表格中还能嵌套另一个表格或其他信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/m3SHE7j1F0RCK2gsbDAK.png" alt width="781" height="390" referrerpolicy="no-referrer"></p>
<p>结合层级表的使用场景，多以查看为主，编辑需求较少。</p>
<h3>5. 交叉表格</h3>
<p>当一个表格里面有多条数据在同一个小范围的维度进行展示时，它就是交叉表格。从表象上看，就是表头有很多分组进行区分，因此它也叫做表头分组。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/K3g5rnnjcdUqiFcfTIaK.png" alt width="777" height="150" referrerpolicy="no-referrer"></p>
<h3>6. 图表表格</h3>
<p>除了在单元格中引用图表之外，很多时候都会提供图表/表格视图切换，便于用户从图形角度查看、分析自己关注的数据。</p>
<p>有时也会有“图表+表格”的形式，这时候，表格往往只作为明细放在页面底部。大量的表格也会导致视觉的单调。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ang6mf5vicN04nQPShlf.png" alt width="779" height="404" referrerpolicy="no-referrer"></p>
<p>当一个表格里面有多种图表数据进行展示时，它就是图表表格。</p>
<p>在对一些项目做定制化开发时，这是十分常见的场景。用户点击某一数据后，直接跳出数据的统计图，方便用户进行对比。</p>
<h3>7. 卡片表格</h3>
<p>可以用卡片的形式来展示信息，将信息以组的概念呈现，单张卡片内的信息按优先级进行排列。此外，卡片彼此之间又形成一个整体。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ac8fQuMXrtWKDY3aXhdt.png" alt width="779" height="249" referrerpolicy="no-referrer"></p>
<p>用户无需以特定顺序浏览条目，将每个条目以富有吸引力的方式呈现。</p>
<h2 id="toc-6">六、小结</h2>
<p>感谢本文的参考文献作者们，让我能够更充分地了解表格设计的奥秘。</p>
<p>本文的撰写花费了我大量的业余时间，希望对广大的B端产品设计能提供一点点的小帮助，如果觉得有用请点个赞吧，我会继续努力出更多优秀的文章来和大家一起探讨！</p>
<p><strong>参考资料：</strong></p>
<p>1. B端表格设计实战指南：Nick</p>
<p>2.列表页：AntDesign</p>
<p>3.web表格设计解析：小龙</p>
<p>4.web表格设计攻略：THE TAO</p>
<p>5.B端设计指南-06表格：CE青年</p>
<p>6.数据表设计：塔拉斯·巴库斯维奇（Taras Bakusevych）</p>
<p> </p>
<p>本文@🌟大星星🌟 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4689387" data-author="1102809" data-avatar="https://static.woshipm.com/WX_U_202006_20200618162820_2800.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://image.woshipm.com/wp-files/2021/07/iP7dAdOuwvvskyJDEm5y.jpg!/both/80x80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            