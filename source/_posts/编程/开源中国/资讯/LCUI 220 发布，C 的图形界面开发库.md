
---
title: 'LCUI 2.2.0 发布，C 的图形界面开发库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8594'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 13:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8594'
---

<div>   
<div class="content">
                                                                    
                                                        <p>LCUI 2.2.0 发布了。LCUI 是一个用 C 语言编写的图形界面开发库，可用于构建简单的桌面应用程序。</p> 
<h2>更新概要</h2> 
<h3>问题修复</h3> 
<ul> 
 <li>conditional jump or move depends on uninitialised value(s) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2F717486861541b93e5ab95a246dfce90650d4273c" target="_blank">7174868</a>)</li> 
 <li><strong>gui:</strong> 水平滚动条未起作用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fissues%2F219" target="_blank">#219</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2F31dee2494d7e5c88af02052084f962cf71797141" target="_blank">31dee24</a>)</li> 
 <li><strong>gui:</strong> 当部件的定位为绝对定位时，尺寸计算错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2F35bfa3f0e7d92c53f95fa9825217d115df8c74c0" target="_blank">35bfa3f</a>)</li> 
 <li><strong>gui:</strong> 组件在隐藏后未更新样式 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2Ff0a6e30a6d85d466cbfffc5fd0c2e91aacb574c9" target="_blank">f0a6e30</a>)</li> 
 <li><strong>image:</strong> 图片后缀名检测方式错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2F46095e70e39e5f1440fb1b5b9effaa35b76c6bbe" target="_blank">46095e7</a>)</li> 
 <li><strong>util:</strong> 当 dict 的操作函数被编译器内联时会报错 ‘NULL’ 未声明 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2Fc9c990167d44da9ca54fd3fed5753567aade1825" target="_blank">c9c9901</a>)</li> 
 <li>移除错误的 <code>CSSParser_GetRuleParser()</code> 宏 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2F3bd6b715729255607760abadbf72c22d8c2681c8" target="_blank">3bd6b71</a>)</li> 
 <li>LCUI_PostSimpleTask() 中的变量命名冲突 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2Ff0382d435a5b0d19a14165101605e7f021191e8a" target="_blank">f0382d4</a>)</li> 
</ul> 
<h3>新功能</h3> 
<ul> 
 <li><strong>font:</strong> 添加 TextStyle 的操作函数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommit%2Fc0ccdf81e5404fc21cd804ec95e0a030800a75fc" target="_blank">c0ccdf8</a>)</li> 
</ul> 
<h3>社区动态</h3> 
<p>自上次更新以来，LCUI 新增了一位贡献者 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fcommits%3Fauthor%3DWhoAteDaCake" target="_blank">WhoAteDaCake</a>，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopencollective.com%2Flcui" target="_blank">OpenCollective</a> 上共新增 55 美元捐赠收入，分别来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopencollective.com%2Flog" target="_blank">Log</a> (50 美元）和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopencollective.com%2Fbuddhalow" target="_blank">Buddhalow</a> (5 美元)。</p> 
<h3>其它更新</h3> 
<ul> 
 <li>添加适用于 LCUI 2.x 的文档</li> 
 <li>启动贡献者激励计划</li> 
 <li>参加开源软件供应链点亮计划 - 暑期 2021</li> 
 <li>重新规划发展路线</li> 
</ul> 
<h2>全新的文档</h2> 
<p>众所周知，程序员们不喜欢写文档也不喜欢用没有文档的项目，在此之前 LCUI 一直都没有一个完整的能够讲述各方面设计和用法的文档，估计大部分人对这个项目的了解也就仅限于更新资讯、自述文档和一些示例代码，懒得浪费时间去深入了解。为了解决这一问题，降低上手难度，我们花了点时间整理了适用于 LCUI 2.x 的文档，你可以通过这个链接访问文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.lcui.lc-soft.io%2Fv%2Fcn%2F" target="_blank">https://docs.lcui.lc-soft.io/v/cn/</a></p> 
<p>写文档的理由除了解决上述几个问题外，还有以下几个：</p> 
<ul> 
 <li><strong>给想学习 UI 开发或开发 UI 库的开发者提供参考资料。</strong> 在作者开发 LCUI 前，作者为了解如何创建 GUI 的程序、如何操作图形数据、如何在屏幕上绘制图形等问题，尝试过利用搜索引擎、技术论坛提问、加入编程群等简单手段来寻找答案，但均未得到合适的结果。当然作者自身的资料收集能力较弱是导致这个问题的原因之一，另一个原因则是技术环境的问题，那个时候令人印象深刻的就是搜索时常常能搜到某技术网站上的各种低质量复制粘贴转载的文章、只为混分数不正面回答技术问题的回帖，以及喜欢挑别人错误然后阴阳怪气或问候全家的技术大牛。在这种环境下想找点资料还是挺困难的，如果现在还有人像曾经的作者一样有着类似的想法的话，那么这文档对他们或许有所帮助，至少能避免再次走上作者曾经所走过的弯路。</li> 
 <li><strong>可持续发展。</strong> 开源项目是否能够长期发展取决于贡献者的数量和活跃度，拥有众多活跃贡献者的项目往往比只有作者才能维护的项目靠谱得多。增加贡献者的方法之一就是提供文档，文档能让用户更深入的了解项目并让他们发现项目中存在的各种各样的问题，促使他们成为能够解决这些问题的贡献者。</li> 
 <li><strong>征集改进意见。</strong> LCUI 中的一些功能的实现方式并不是最优的，我们希望有相关经验的开发者能够给出更好的实现方式。</li> 
 <li><strong>收集其他人的经验和见解。</strong> 作者对一些概念的理解可能过于肤浅，我们希望知道其他人是怎样理解这些概念的、如何以更严谨的方式来表达。</li> 
</ul> 
<p>写文档的难点在于如何用准确的词语将零碎的知识点组织成清晰连贯的句子表达出来，受限于作者的阅读和写作经验，第一版的内容很少，主要以讲解示例代码的方式来介绍各种概念和用法，大部分内容的组织和表达方式参考了前端社区的技术文档，虽然有很多参考对象，但作者在编写期间也还会常常因缺乏灵感、找不到合适的题材而导致没有任何产出。</p> 
<p>我们希望在文档的后续更新中加入更多的 UI 开发相关知识，而不是仅限于讲解 LCUI 自身的设计和各种接口，让读者即便不用 LCUI 开发应用也能利用从该文档所学到的知识快速上手其它 UI 开发工作。如果你认可这一做法且希望将自己多年积累的 UI 相关的开发经验和见解通过文档的形式分享给其他开发者，欢迎参与完善文档。</p> 
<h2>贡献者激励计划</h2> 
<p>Android 端适配计划自 2020 年 7 月份发布至今，没有任何进展。当时我们比较乐观，尝试过在众包和码市上发布项目，虽然发布后的这一两个月内确实有收到数名开发者的意向，但都没有实质性的进展。竞标者提交的竞标理由大都只有简短几个字，无法看出他们的真实意图，而且他们在平台上展示的资料太少，不确定他们是否真的适合负责该项目，不确定的因素多到令人感到焦虑，最终致使我们决定撤销项目。</p> 
<p>当然悬赏计划并不会因此作罢，Android 端适配计划没有进展的主要原因是钱太少了，尤其是对于在外包平台上接项目的开发者而言，赚钱是他们的主要目的，给不了足够的钱扯再多的理由也是虚的，和画大饼压榨员工的老板没什么区别。花钱找人写代码更像是一种雇佣关系，既然我们无法提供足够奖金，那么我们可以提供一些对于贡献者有价值的东西来弥补奖金的不足，以将这个关系转变为合作关系。出于这种目的，我们制定了贡献者激励计划，将一些待办事项都列入到这个计划内，并放在项目主页上展示，以吸引感兴趣的贡献者参与进来。如需了解更多可访问项目主页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flcui.lc-soft.io%2F%23joinus" target="_blank">https://lcui.lc-soft.io/#joinus</a></p> 
<h3>存在意义</h3> 
<p>在看到这激励计划时你可能会有疑问：有能力解决这些问题的开发者哪会浪费时间去搞这个？把时间用在睡觉、健身、学习、娱乐、陪家人、赚加班费等事情上不香吗？的确，有很多有意义有价值的事情需要我们去做，对于有兴趣参与开源项目并分享自己技术的人而言，参与激励计划也是一件有意义的事情，而对于我们而言，它的意义在于：</p> 
<ul> 
 <li>给其他开发者一个打造或推广开源项目的机会。</li> 
 <li>寻找合适的解决方案。因悬赏任务而开发的项目，会优先考虑我们的需求并给出合适的解决方案，能让我们快速上手并将之应用到 LCUI 中。</li> 
 <li>促进技术交流和合作。都是国人开发的开源项目，交流和合作比较方便一些，而且由于项目的依赖关系，还有机会为对方的项目反馈问题和建议、贡献代码。</li> 
 <li>合理利用现有资源，节约成本。在用其他开源项目前需要花大量时间找文档学习，遇到问题时不容易找到方法，如果用的项目是国人开发的且他有空给你提供技术支持，那就简单多了。</li> 
 <li>让更多的人参与进来。开源的意义在于大家都可以参与推动项目的发展，而让大家参与的前提是他们知道这个项目是什么、打算做什么以及他们能提供哪些帮助，如果所有工作都让我们自己独自承当的话，那这个项目就会一直停留在自娱自乐的水平。</li> 
</ul> 
<h3>适合人群</h3> 
<ul> 
 <li>因刷腻了算法题而想找点有技术含量、有挑战性且现实项目中存在的问题来解决的<strong>算法爱好者</strong>。</li> 
 <li>想通过参与项目来锻炼编程能力顺便赚点零花钱的<strong>学生</strong>。积累的项目经历对他们完成课设或毕设也有帮助。</li> 
 <li>想参与或开发一个有亮点、有技术含量的项目来提升自己的开源影响力和就业竞争力的<strong>初中级开发者</strong>。常常能看到有人吐槽程序员内卷很严重，只会在简历中吹牛和熟练背诵面试题的话可能还不足以体现出优势，如果有“参与或开发开源项目”这一加分项的话应该会好很多。</li> 
 <li>发现自己打算开发或已开发的开源项目与 LCUI 的新功能需求相符的<strong>资深开发者</strong>。给自己打算开发的开源项目调研用户需求，或是给自己的开源项目增加一个用户，这对项目的发展也有所帮助。</li> 
 <li>想参与开源项目并与他人进行技术交流的<strong>编程爱好者</strong>。</li> 
</ul> 
<h3>参与流程</h3> 
<ul> 
 <li><strong>挑选任务</strong>：在计划内的任务列表或文档中的待办事项列表中挑选你感兴趣的任务。</li> 
 <li><strong>确认任务有效</strong>：在 LCUI 的 GitHub 代码库主页里搜索相关的 Issue 和 Pull Request，检查该任务是否被他人认领。</li> 
 <li><strong>发起需求讨论</strong>：在 LCUI 的 GitHub Discussions 里新建讨论帖，表明你想认领的任务和想要了解的内容，通过与我们交流让需求更明确。</li> 
 <li><strong>确定正式的开发任务</strong>：在需求讨论明确后，我们会整理全部需求然后作为新的 issue 提交。</li> 
 <li><strong>开始开发</strong>：在 LCUI 的 GitHub 代码库主页 Fork 一份副本到你的名下，然后克隆代码库到本地，在新的分支中展开你的工作。</li> 
 <li><strong>提交验收请求</strong>：工作完成后在 GitHub 上向 LCUI 提交拉取请求（Pull Request），等待我们审查。</li> 
 <li><strong>解决验收问题</strong>：审查期间我们可能会提交一些审查意见，你需要针对这些意见做相应的改动。</li> 
 <li><strong>验收完毕</strong>：审查完后我们会接受你的拉取请求，从你的分支拉取你所做的改动并合入主干分支。</li> 
 <li><strong>接收赏金</strong>：你将会通过悬赏平台或转账的形式收到赏金。</li> 
</ul> 
<p>注：以上流程同样适用于 Gitee，你可以根据个人喜好来选择 GitHub 或 Gitee。</p> 
<h2>开源软件供应链点亮计划 - 暑期 2021</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsummer.iscas.ac.cn%2F" target="_blank">开源软件供应链点亮计划 - 暑期 2021</a>（以下简称 <code>暑期 2021</code>）是由 <code>中国科学院软件研究所</code> 与 <code>openEuler 社区</code> 共同举办的一项面向高校学生的暑期活动，旨在鼓励在校学生积极参与开源软件的开发维护，促进优秀开源软件社区的蓬勃发展。</p> 
<p>像 LCUI 这种功能少、文档少、活跃度低、工作上用不到项目是很难有资深开发者愿意花费时间参与贡献的，即便如此，参与 LCUI 项目对于时间充足、充满技术热情的学生而言仍然是一个适合用来提高编程能力的选择，所以 LCUI 社区报名参加了此活动，并且提供了三个活动项目。</p> 
<p>与上面的 <code>贡献者激励计划</code> 不同的是，<code>暑期 2021</code> 由众多机构主办，活动参与方主要角色为学生、社区和导师，面向满 18 周岁在校学生，项目都有着较高的奖金，与项目难度对应的税前奖金分别为高（12000 元）、中（9000 元）、低（6000 元），项目完成后，导师也有 5000 元奖金。</p> 
<p>以下是活动项目清单。由于每位导师最多同时指导三个项目，因此 LCUI 项目作者只能发布这三个项目，如果你有意向成为 LCUI 社区的项目导师指导其他新人参与 LCUI 项目，则可以在贡献者激励计划中挑选你感兴趣的任务然后发布为活动项目，不过这要等到下一期的活动了。关于如何成为导师，详见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsummer.iscas.ac.cn%2Fhelp%2Fmentor%2F" target="_blank">导师指南</a>，为了能够顺利成为导师，我们建议你先通过解决 LCUI 的一些问题来获得 LCUI 项目贡献者身份。</p> 
<p>如果你对这些项目有改进建议和想法，欢迎向我们反馈。</p> 
<h3>LCUI 的布局引擎开发 - 高难度</h3> 
<p>LCUI 的布局引擎支持正常流布局和弹性盒子布局，它的工作是根据于每个 UI 组件中的样式和布局参数计算它们的几何属性，与 UI 组件模块有着较强的依赖关系。由于依赖关系的存在使得它不利于做单元测试，对其做单元测试必须先初始化 UI 组件模块，而且按照模块化设计思想，布局引擎应该设计成包含布局元素定义、布局参数定义和相关接口的独立模块，被 UI 组件模块单向依赖，UI 组件模块只需要负责将布局元素附加在 UI 组件上并管理好布局元素之间的关系和布局参数即可。出于这些问题的考虑，我们希望开发一个独立于 LCUI 项目的布局引擎来解决它们。</p> 
<p><strong>产出要求：</strong></p> 
<ul> 
 <li>调研 LCUI 源码中的布局引擎的功能需求和实现方式，完成需求分析报告文档</li> 
 <li>调研 yoga、SnapKit 等开源的布局引擎，收集它们的特点、用法、设计风格等信息，整理成调研报告文档</li> 
 <li>结合需求文档和调研报告文档，完成项目的 API 设计规范文档</li> 
 <li>参考主流开源项目的 README.md 文档的写法，完成项目的自述文档</li> 
 <li>添加单元测试，测试覆盖率达到 80% 以上，无内存访问越界、内存泄露等问题</li> 
 <li>完成全部 API 的实现，代码编译无警告</li> 
 <li>将 LCUI 的布局引擎替换为该布局引擎，通过 LCUI 的所有测试，无布局错乱等问题</li> 
 <li>提供性能测试程序</li> 
</ul> 
<p><strong>技能要求：</strong></p> 
<ul> 
 <li>熟悉 C 或 C++ 编程语言</li> 
 <li>熟悉在 Linux 和 Windows 系统环境中开发</li> 
 <li>熟悉常见数据结构和算法</li> 
 <li>了解 Git 的基本用法</li> 
</ul> 
<h3>LCUI 的 2D 图形库开发 - 中等难度</h3> 
<p>LCUI 的图形处理模块只支持绘制矩形、边框、盒形阴影以及透明度混合，考虑到以后的硬件加速支持、对接其它图形库、扩展更多图形绘制能力等需求，以及历史遗留代码较多、代码设计不严谨、扩展性较差等问题，我们希望开发一个独立于 LCUI 项目的 2D 图形库来解决它们。</p> 
<p><strong>产出要求：</strong></p> 
<ul> 
 <li>调研 LCUI 源码中的图形处理类函数的使用情况和需求，完成需求分析报告文档</li> 
 <li>调研 cario、skia、OpenCV 等主流图形库，收集这些库的特点、用法、设计风格等信息，整理成调研报告文档</li> 
 <li>结合需求文档和调研报告文档，完成项目的 API 设计规范文档</li> 
 <li>参考主流开源项目的 README.md 文档的写法，完成项目的自述文档</li> 
 <li>为每个功能模块添加单元测试，测试覆盖率达到 80% 以上，无内存访问越界、内存泄露等问题</li> 
 <li>完成全部 API 的实现，代码编译无警告</li> 
 <li>用该 2D 图形库代替 LCUI 原有图形模块，通过 LCUI 的所有测试，无渲染内容异常等问题</li> 
 <li>提供性能测试程序，渲染性能不低于 LCUI 原有的图形模块</li> 
</ul> 
<p><strong>技能要求：</strong></p> 
<ul> 
 <li>熟悉 C 或 C++ 编程语言</li> 
 <li>熟悉在 Linux 和 Windows 系统环境中开发</li> 
 <li>了解计算机图形学</li> 
 <li>了解常见数据结构和算法</li> 
 <li>了解 Git 的基本用法</li> 
</ul> 
<h3>LCUI 的基础工具类函数库开发 - 中等难度</h3> 
<p>LCUI 项目中包含了数据结构、字符串、日志、时间、定时器、字符编码等实用类的函数，它们的设计风格和用法不统一，与 LCUI 头文件有较强的依赖，因此我们希望将这些函数分离到独立的项目中作为函数库来维护。</p> 
<p><strong>产出要求：</strong></p> 
<ul> 
 <li>调研 LCUI 源码中的基础工具类函数的使用情况和需求，完成需求分析报告文档</li> 
 <li>调研 tbox、glib 常见开源工具类库，收集这些库的特点、用法、设计风格等信息，整理成调研报告文档</li> 
 <li>结合需求文档和调研报告文档，完成项目的 API 设计规范文档</li> 
 <li>参考主流开源项目的 README.md 文档的写法，完成项目的自述文档</li> 
 <li>为每个功能模块添加单元测试，测试覆盖率达到 80% 以上，无内存访问越界、内存泄露等问题</li> 
 <li>完成全部 API 的实现，代码编译无警告</li> 
 <li>将 LCUI 内的工具类函数替换为该函数库的函数，通过 LCUI 的所有测试</li> 
</ul> 
<p><strong>技能要求：</strong></p> 
<ul> 
 <li>熟悉在 Linux 和 Windows 系统环境中开发</li> 
 <li>熟悉 C 或 C++ 编程语言</li> 
 <li>了解常见数据结构和算法</li> 
 <li>具备良好的文字表达能力</li> 
 <li>了解 Git 的基本用法</li> 
</ul> 
<h2>发展路线</h2> 
<h3>3.0 开发计划</h3> 
<p>距离上次版本更新已经快一年了，如果按照以往的 3-4 个月更新一次的节奏，这么长的时间应该够完成 3 次更新，版本能更新到 2.4.0。究其原因，可能是作者沉迷于工作（加班）导致业余编码兴趣减弱，可能是作者心态变得浮躁不容易静下心来专注于编码，也可能是作者厌倦于底层编码工作想搞点其它方面的事情，又或者都有。</p> 
<p>这种程度的更新频率只会对项目的发展产生消极的影响，为了改变现状，我们计划在 3.0 版本中对 LCUI 的大部分源码进行重构，使 LCUI 能够像主流开源项目那样拥有统一的编码风格、清晰的目录结构、良好的架构设计、简单易用的接口、较低的内存开销、易于裁剪和定制的模块等特性。如需了解更多信息，可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flc-soft%2FLCUI%2Fissues%2F239" target="_blank">issue#239</a>。</p> 
<p>当然，我们并不打算承担所有开发工作，部分的开发任务已经被列入到贡献者激励计划中，以此吸引更多贡献者，毕竟从 LCUI 诞生至今这段时间内，应该有很多开发者已经成为了资深工程师甚至高级技术专家，对于他们而言这些任务难度并不高，是个不错的施展才华的机会。</p> 
<h3>定位</h3> 
<p>现阶段如果像主流 GUI 库那样以“提供成熟可靠的 GUI 解决方案”为定位的话似乎不太现实，从上述的贡献者激励计划和暑期 2021 活动中我们可以看出，将 LCUI 项目拆分成多个小项目并以技术交流和合作的方式交给其他贡献者负责维护是一个不错的选择，因此我们决定给 LCUI 建立一个新的定位：以探索和实践新的 GUI 开发技术为目的，通过技术交流、合作来培养开源项目作者和贡献者，为开源社区贡献一个独具特色的 GUI 解决方案。</p> 
<h3>文档</h3> 
<p>LCUI 的文档有待继续完善，我们未来的计划如下：</p> 
<ul> 
 <li>补充更多的内容。</li> 
 <li>添加英文版文档。等文档完整后添加英文版本，再做一些推广。</li> 
 <li>探索出版图书和制作实战课程的可行性。此前作者在 Gitee 上有收到过好几次图书编辑发来的合作邀请，但都拒绝了，原因是作者对如何撰写图书和如何制作课程没有头绪，而且也没时间，不过等文档完善后可以考虑这方面的事情，这或许对作者 35 岁以后的职业生涯有所帮助。</li> 
</ul> 
<h3>社区</h3> 
<p>贡献者激励计划和暑期 2021 可能会给 LCUI 项目带来贡献者，为了让这些贡献者顺利完成任务，作者作为 LCUI 社区中的唯一核心开发人员将会投入一些时间和精力在需求确认、技术指导、代码审查等工作上面。</p> 
<p>我们希望更多的人能够参与进社区，参与方式包括但不仅限于：</p> 
<ul> 
 <li>为文档提供改进建议。</li> 
 <li>为 3.0 开发计划提供建议。</li> 
 <li>为贡献者激励计划和暑期 2021 中的开发任务提供改进意见、参考资料、开发思路。</li> 
 <li>为以后的图书出版和课程制作提供选题、大纲、讲述方式等方面的建议。</li> 
 <li>审查贡献者提交的代码，给出合适的改进建议。</li> 
</ul>
                                        </div>
                                      
</div>
            