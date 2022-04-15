
---
title: 'OA办公软件篇（一）：组织架构'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/2pqpakjKkvTApWZ7ttc3.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 15 Apr 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/2pqpakjKkvTApWZ7ttc3.jpg'
---

<div>   
<blockquote><p>编辑导读：办公自动化（Office Automation，简称OA），是将现代办公和现代计算机技术结合起来的一种新型办公方式。组织架构是把企业员工有序纳入的一种重要方式，是OA系统的根。本文作者对OA办公软件的组织架构展开分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5396424 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/2pqpakjKkvTApWZ7ttc3.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景</h2>
<p>在说组织架构之前，我们先来说说OA本身。</p>
<p>百度百科解释OA为：办公自动化（Office Automation，简称OA），是将现代办公和现代计算机技术结合起来的一种新型办公方式。</p>
<p>钉钉、企业微信都属于市面上比较成熟且用户群体广泛的OA办公软件，钉钉是标准的老板思维，企业微信则是更侧重于生态圈的打造。</p>
<p>我们公司目前是全员都使用公司自研的OA系统来进行上下班打卡、审批等操作。在过去，不同的子公司曾经使用过不同的OA软件：传统医药公司用企业微信，因为更看重客户维系；互联网公司用钉钉，因为更看重效率。<strong>将所有子公司都切换为使用自研OA的契机为：要进行统一管理及全面的数字化管理。</strong></p>
<p>对于企业来说，组织架构是管理的核心部分；对于OA系统来说，组织架构按照企业规则进行管理和呈现就是OA系统的根，是把企业员工有序纳入的一种重要方式，所以今天我们着重来讲OA中的组织架构。</p>
<h2 id="toc-2">二、作用</h2>
<p>OA系统的核心是组织管理，帮助组织提升绩效。组织离不开人、目标、结构、管理这四大因素。目标是组织的前提条件，人员是基础条件，结构是载体条件，管理是维持条件。</p>
<p>对于公司来说，组织架构和组织管理的核心，将已有的组织架构抽象到软件中，是必要的操作和手段。</p>
<p>对于系统软件来说，组织架构是软件系统的权限体系的重要搭建依据，软件根据不同员工在组织中的位置给予不同的权限，比如说普通员工对于软件只有查看和使用的权限，普通管理员对于软件有查看和修改的权限，超级管理员则拥有最大权限等。</p>
<p>对于系统功能来说，组织架构是审批体系、日报抄送体系等功能的逻辑基础，软件根据组织架构的逻辑进行相应的模板处理，比如将日报抄送给所有的上级管理层查看等；是通讯体系的核心构成部分，比如通过组织架构选择员工发起群聊、打电话等。</p>
<p>对于公司员工来说，组织架构可以帮助新员工快速的了解公司的体系和人员构成，了解部门/整个公司架构。</p>
<h2 id="toc-3">三、迭代历程</h2>
<p>为什么在这里要讲迭代历程这块呢？是因为不希望还有人在为了偷懒或者不懂的情况下迷迷糊糊的做成第一个阶段的模式：纯分组管理模式。</p>
<p>我目前在做的这个OA软件的组织架构经历过两个阶段。</p>
<p><strong>第一个阶段：纯分组管理模式</strong></p>
<p>仅将人放到各个分组下面装起来。这样做的唯一好处就是不论产品经理还是研发都能够短暂以省时省力的方式把人放到系统中正常使用，但坏处却一大箩筐，各个分组之间没有联系—>导致组织不能形成层级关系—>缺少层级处理，无法用于系统权限、审批流等功能。</p>
<p><strong>第二个阶段：组织架构模式</strong></p>
<p>在组织上建立组织层级概念，使得不同部门之间能够形成上下级部门的关系，比如运营部属于医疗信息化事业部；</p>
<p>在组织内建立职工层级概念，比如事业部的总经理是张三，副总经理是李四等；</p>
<p>普通员工能够灵活管理其直属领导，比如医疗信息化事业部的张三由总经理直接管理，那就可以直接将其领导设置为总经理即可；</p>
<p>系统权限、审批流、日志抄送等功能可以直接使用组织架构的核心逻辑来进行功能设置和管理，比如公司第一负责人拥有超级管理员权限，部门管理层员工均能够拥有管理员权限，普通员工则只有普通权限等。</p>
<h2 id="toc-4">四、具体实现</h2>
<p>在说具体实现之前，需要清楚我们的OA产品具体是以什么形式去做的。</p>
<p>首先，从外在表现形式来说，可以采用APP或者小程序的方式来进行实现，现在很多轻量级的产品会采用纯小程序的方式实现，但小程序本身对包的大小有限制，因此我们使用APP+小程序的方式来实现，用户可以根据自己的需求自由选择。</p>
<p>其次，从使用权限上来说，普通员工和管理人员究竟是采用两个独立移动端来实现还是使用一个来实现，是一个值得思考的问题。我的建议是，毫不犹豫的选择用一个移动端口实现，否则结果就是最后仍然要做端口合并和权限重划分，下面分别将这两种模式做一个介绍（此处不包含Web管理端）。</p>
<p><strong>（1）两个独立移动端（如下图所示）：分为业务端（移动端）、管理端（移动端），普通员工仅使用移动端，管理人员使用这两个端口。</strong></p>
<p>设计者这么做的初衷是想要极其清晰的将普通员工和管理人员的使用分开，但实际上，从我的角度看，这其实就是一个“懒惰的做法”，因为本质上就是懒得将底层权限体系搭建起来，采用了这种分端口的方式，却给使用者和后来的产品经理都带来了不便利。实际上因为后来我们要合并这两个移动端，我基本上将权限这块进行了重构、将所有功能重新进行了梳理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/Md7NoKLIvtr3yTPsa54i.png" alt width="258" height="138" referrerpolicy="no-referrer"></p>
<p>以组织架构为例，在两个移动端的情况下分开的时候，业务端（移动端）主要实现的是组织架构的查看和利用组织架构进行通讯的功能，管理端（移动端）除了包含了业务端的功能之外，还有部门管理和人员管理的功能。</p>
<p><strong>（2）一个移动端合并实现。</strong></p>
<p>不分业务端和管理端的移动端，就是仅有一个OA移动端，当然它的表现形式仍然可以是小程序和APP。仍然以组织架构为例，这个OA移动端在登录上不再限制普通用户还是管理用户，只要是录入数据库中的公司员工都能够正常进行登录，区别在于将权限管理嵌入功能之中，组织架构的功能本身需要限制非管理人员进行部门管理的动作和人员管理的动作，查看组织架构和利用组织架构进行通讯功能则是基础操作。</p>
<p>接下来，我们进入正题，来说说组织架构的实现核心和重点。</p>
<p>1）移动端、Web管理端的区别</p>
<p>组织架构的移动端其实行使的主要还是查看和基本的管理操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/IZcwPgUVuTgi7OqeoRB2.png" alt width="335" height="138" referrerpolicy="no-referrer"></p>
<p>而Web管理端除了基础管理之外，还会深入的对组织架构中成员的各种权限进行管理。权限管理这一块不在这一部分进行讲解，会在下一章【OA办公软件篇（二）—权限管理】中详细说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/isM0N0NqkVIP9lGYkCpJ.png" alt width="418" height="326" referrerpolicy="no-referrer"></p>
<p>2）组织架构的创建和维护</p>
<p>创建部门的核心要素：</p>
<p>① 部门名称</p>
<p>② 选择上级部门，是为了将组织之间形成联系</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/TOOvju3CKvada3D8Dcph.png" alt width="395" height="290" referrerpolicy="no-referrer"></p>
<p>③ 部门负责人：选择部门负责人的时候需要选择负责人的层级，层级表示此人在部门中的位置；一个部门支持多层级管理者。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/QeUkGNo6UZbXilELMrQF.png" alt width="417" height="902" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/GsV7tlhXlCsEc5Ztqw9n.png" alt width="390" height="856" referrerpolicy="no-referrer"></p>
<p>3）人员管理</p>
<p>除了人员姓名、电话、职位等基本信息之外，部门需要在组织架构中进行选择，直属领导同样可以进行选择，直属领导不会默认为顺级负责人，原因为可能存在普通员工跨级直属管理的现象，比如我们某个子公司的销售就是由总经理直接进行管理的。</p>
<p>关于角色，管理层的角色才会是管理员，是什么角色这个一是系统会按照在组织架构中的位置默认赋予，另一个是在Web管理端/移动端可以进行调整。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/iWKoRJRHY4au0nCulAS7.png" alt width="414" height="863" referrerpolicy="no-referrer"></p>
<p>4）组织架构的查看</p>
<p>组织架构的查看有两个方式，一种是像这种“分组+跳转页面形式”，在当前页面只展示第一级，要看哪一个就点击哪一个，跳转至一个新的页面展开查看，一级一级点进去看就可以了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/W0OyOBfoIebdpoN3AGqJ.png" alt width="374" height="427" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/haG7tEuN49cXrxqd26xG.png" alt width="357" height="646" referrerpolicy="no-referrer"></p>
<p>另一种是在当前页面可以一级一级的展开去看，需要查看详情再点击部门进入新页面查看，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/JkdGYk1tBboLGBdGATOF.png" alt width="414" height="874" referrerpolicy="no-referrer"></p>
<p>5）关于通讯部分</p>
<p>从组织架构发起通讯，分为两部分，一部分是电话的维护和使用，另一部分则是即时通讯的使用，因为这些对于组织架构来说不是重点，所以不再过多描述。</p>
<p>写在最后：这一篇博客除了讲组织架构之外，也讲了很多OA方面点，尤其是里面关于OA产品层面迭代的思考，值得每一个产品经理思考。从我个人来说，如何做出有价值的产品，如何在产品设计中不给别人添麻烦，是我需要不断警醒和思考的！</p>
<p> </p>
<p>本文由 @暴躁PM棠九九 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5396010" data-author="1154176" data-avatar="http://image.woshipm.com/wp-files/2022/04/jvJt4FRreC5L3kO0zqGm.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.qidianla.com/woshipm_def_head_1.jpg" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            