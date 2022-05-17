
---
title: '以Amazon SageMaker Canvas为例，B端产品如何打造精致体验设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/0bjUHBa5jTuzeshbZRPq.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 17 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/0bjUHBa5jTuzeshbZRPq.jpg'
---

<div>   
<blockquote><p>编辑导语：不少产品都会应用机器学习、低代码这类概念，而这类概念对大众用户而言，可能并不属于他们所熟悉的领域，此时这类工具产品要如何搭建产品设计策略，让用户可以方便快捷地上手体验呢？本文作者结合Amazon SageMaker Canvas这款产品进行了体验总结，一起来看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5438435 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/0bjUHBa5jTuzeshbZRPq.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>低代码是最近几年B端产品的一个热门领域，能够实现只写少量代码或不写代码，类似用“乐高积木”的方式来开发。优势也是显而易见的，可以提高产品的开发效率，无开发能力的用户也能够快速上手。</p>
<p>而在数据建模领域，为了能够精准预测未来结果，业务分析师需要能够有专业的数据分析方法，甚至是代码编写能力。这对运营人员、市场人员人员是一个不小的挑战。</p>
<p>Amazon SageMaker提供了Canvas服务，通过可视化、点击式的交互方式，业务分析师无需编写任何代码，也无需 ML 专业知识，就可以生成准确的机器学习 (ML) 预测。听起来很牛，但是真正的体验怎么样呢？今天我们来测评一下。</p>
<p>文章结构如下：</p>
<ol>
<li>用户场景，数据建模之痛；</li>
<li>用户需求，业务分析师工作流程；</li>
<li>产品交互，构建精致的体验设计；</li>
<li>视觉风格，塑造轻量设计语言；</li>
<li>场景拓展，体验升级；</li>
<li>产品体验优化建议。</li>
</ol>
<h2 id="toc-1">一、用户场景分析</h2>
<p>说起“数据建模、数据预测、数据分析”这些高大上的名词，很容易让普通用户望而却步。</p>
<p>而我正是一名小白用户，不过我也是一名体验设计师。如今从事数据产品设计的相关工作，每天会跟各种数据库导入导出、实例、清洗治理等等功能打交道。内心对于这些信息还是有些不适应，因为行业门槛确实很高，不是普通用户所能轻易理解的。</p>
<p>同样对于业务分析师来说，复杂的数据建模也存在较高行业门槛。我们想象一个场景。</p>
<p>业务分析师小A想要进行数据分析，但是个人能力有限，面对复杂多变的数据集，费时费力，只能用excel 完成简单的数据图表可视化，但是数据内在的联系，相互影响的程度，很难分析出来。所以需要求助于专业的数据分析师。于是联系到了数据分析师小C，两者开始了面对面的沟通。</p>
<blockquote><p>小A：C工，我边想要有一组客户数据，想要预测下他们未来贷款的可能性。每个用户大概有20多个指标。这么办呢？</p>
<p>小C：哦哦，这个简单，你可以balabala……~</p>
<p>小A：……（一头雾水~）C工，能不能讲的简单点？</p>
<p>小C：你可以先……再……</p>
<p>小A：C工，你能帮我实现一下吗？</p>
<p>小C：可以，不过我最近比较忙，需要过一段时间才能处理这个需求。另外请走一个需求单给我。</p>
<p>小A：……</p>
<p>此时小A的内心是崩溃的。</p></blockquote>
<p>我想很多业务分析师都会遇到这样场景。如何能够帮助没有专业代码技能的业务分析师拿到想要的预测结果呢？这可能吗？</p>
<h2 id="toc-2">二、用户需求</h2>
<p>B端产品必须面向用户需求，解决用户问题。所以必须要明白用户是谁，需求是什么。</p>
<p>我们要介绍一下用户Canvas 服务的用户群体之一——业务分析师。</p>
<p>业务分析师需要通过现有数据，发现未来的机会点。例如银行的业务分析师需要为营销部门即将开展的营销活动确定目标客户，需要根据包含客户人口统计和银行历史记录的数据集，预测最有可能注册存款证的客户。或者作为业务分析师，如何通过对客户数据的分析，帮助营销外呼团队发现更有意愿接听电话的用户，从而提高团队的营销效率呢？这些都是业务分析师的重要工作。</p>
<p>业务分析师的日常工作可能会涉及以下过程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/029ABltxeJ4Z6t0OCNyc.png" alt width="680" height="180" referrerpolicy="no-referrer"></p>
<h3>1. 数据准备</h3>
<p>数据分析师会收到一个数据集，包括来自不同渠道或者不同表格的数据进行合并整理，根据自己的经验，去除重复或者无效的字段信息，提高原始数据的质量。</p>
<h3>2. 数据处理</h3>
<p>通过专业的数据分析工具，或者编写代码完成数据预测。如果结果不理想，还需要反复调整数据模型。这个阶段通常会花费较长的时间，分析师相当于反复试错，寻找到合理的数据模型。</p>
<h3>3. 结果呈现</h3>
<p>完成数据处理后，还需要通过各种数据图标，呈现出数据对结果的影响权重等等。</p>
<p>而在普通企业中，并不会配备专业的业务分析师，而是由运营人员、市场人员做出结果预测。这些人员一般不具备专业的数据建模能力，只能通过excel 或者分析软件对数据集进行简单的加工。如果是对未来数据的预测，简单的数据分析是无法满足工作需要的。</p>
<p>另外站在企业的视角，业务分析师建立了基本的模型后，希望可以进一步优化数据模型，提高数据预测的准确率，将模型沉淀成为企业的数据资产，为企业发挥更大的价值。所以需要将分析师完成的数据模型交给专业的数据科学家进一步优化。</p>
<p>所以这样一款产品的用户需求就是：</p>
<ul>
<li>简单，最大化减少产品的技能门槛；</li>
<li>高效，让用户可以尽快拿到预测数据；</li>
<li>协作，将模型沉淀为公司资产。</li>
</ul>
<h2 id="toc-3">三、产品体验设计分析</h2>
<p>与传统的业务分析师相比，互联网时代的业务分析师面临的不是数据匮乏，而是数据过剩。因此，互联网时代的数据分析师必须学会借助技术手段进行高效的数据处理。更为重要的是，互联网时代的业务分析师要不断在数据研究的方法论方面进行创新和突破。</p>
<p>从体验设计维度来看，我总结了如下几点：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/lkMIJRONymLL0Sc62NTA.png" alt width="681" height="250" referrerpolicy="no-referrer"></p>
<h3>1. 简单，易操作</h3>
<p>Canvas赋予了普通业务人员建模能力，只要你有数据和需求，就可以通过上传数据的方式，创建自己的模型，并获得预测结果。并且可以将模型信息分享给专业的数据科学家，让他们进一步优化模型。所以测评的第一感受就是“简单”。</p>
<p><strong>1）新人引导</strong></p>
<p>为了降低用户的学习成本，新人引导是必不可少的。通过简单的引导可以让用户快速上手。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/obuvNOmE2S7ebhZMnOCG.png" alt width="681" height="373" referrerpolicy="no-referrer"></p>
<p><strong>2）流程简单</strong></p>
<p>业务分析师只需要将数据优化处理后，上传到Canvas 中，经过简单的4步操作，即可完成数据预测。这大大地提高了用户的工作效率以及工作的准确率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/iM1K7hauQpSxO1ZOSaxQ.png" alt width="682" height="344" referrerpolicy="no-referrer"></p>
<h3>2. 提升用户效率</h3>
<p><strong>1）流程并行</strong></p>
<p>虽然Canvas是有步骤流程的，但是步骤之间没有强制性。就是说不需要必须完成上一步，才能点击查看下一步。因为构建模型可能花费2-15分钟的时间。用户可以回顾数据信息、构建方式等信息，查看信息是否缺失或者配置错误。</p>
<p>另外用户在模型创建过程中，也可以关闭当前工作流程，让其在后台运行。用户可以创建或者查看其他的数据模型，从而保证了效率的最大化。</p>
<p><strong>2）预览模式</strong></p>
<p>无论是Quick Build 还是Standard Build，智能分析都需要耗费一定的计算时间。用户最担心的就是无法掌控数据质量带来的时间损失。所以在启动模型计算之前，Canvas提供了计算结果预览，避免用户耗费了时间得不到想要的结果。并且结果的预览，为用户提供了反向筛查数据的依据。让小白用户做模型预测，不再是开盲盒。从而减少用户的无谓试错，增强用户信心。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/swPzFM34ZPLivT2Xnqkv.png" alt width="680" height="343" referrerpolicy="no-referrer"></p>
<h3>3. 便捷，减少用户不必要的退出</h3>
<p><strong>1）数据智能化配置</strong></p>
<p>考虑到用户需要对数据进行二次加工，Canvas 提供的数据连接功能，用户可以将多个数据组合优化，建立新的数据。系统可以自动判断数据是否具有关联性，并可以指定连接的方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/NsHFwT63rlsXWHa1MTr8.png" alt width="708" height="357" referrerpolicy="no-referrer"></p>
<p><strong>2）多版本设置</strong></p>
<p>用户很难一次性获得理想的数据模型，会通过多个版本寻找最优的解决方案。Canvas提供了版本管理功能。用户创建新版本时会自动带入上一版本的内容，只要对指标数据做出调整即可，并且可以快速切换，比起全新构建模型更加方便。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/nmhc5XZm7ElwiCKAWGjT.png" alt width="712" height="379" referrerpolicy="no-referrer"></p>
<h3>4. 可视化设计，提升体验</h3>
<p><strong>1）数据可视化</strong></p>
<p>机器学习建模等等，数据质量是关键。通过Canvas ，用户可以从多个维度了解自己的数据，真正地为数据建模做好准备。</p>
<p>表格数据都是散点数据，不够直观。所以需要借助图形可视化，帮助用户更直观地认识数据质量。例如数据的分布情况等等。Canvas 列表模式中增加了数据可视化分析，点击表头，还会展示更详细的数据分析信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/zb20pVOtmRW4eXlILS64.png" alt width="692" height="349" referrerpolicy="no-referrer"></p>
<p><strong>2）结果的可视化</strong></p>
<p>单纯的计算结果对用户并没有太大意义，所以需要向用户解释影响计算结果的关键指标。帮助用户更好地做出行动决策。Canvas提供了图表展示形式，既可以更好地理解计算结果，也便于用户快速完成分析报告。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/gLnh0P8aYZBpxGqVnwhV.png" alt width="690" height="623" referrerpolicy="no-referrer"></p>
<p>另外高级指标分析中，进一步展示了指标间的逻辑关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/QVSqO4ciXuy65AhARN7q.png" alt width="691" height="385" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、视觉风格分析</h2>
<p>视觉风格是“见仁见智”的，每个人都有不同的视觉感受。打开Canvas 后，你会明显地感受到与整个亚马逊云科技产品设计风格的不一样。由于面向非技术专业用户，虽然集成在亚马逊云科技平台上，但是采用了更多C端化的设计风格，样式更加轻量，增加了插画的元素。更加亲切。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/lTuh0ueAeWNEDGIGL3NW.png" alt width="683" height="364" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、场景拓展、体验升级</h2>
<p>B端产品不仅仅要解决用户问题，还要考虑到客户场景，用户间的协作与管理。例如用户可能只是为了简单的离线检测验证，需要能够快速获得预测结果，而有的用户则希望能够为专业的数据科学家提供基础模型，从而获得更精确的预测结果。</p>
<p>Canvas提供了Quick Build 和Standard Build两种模型构建方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/5bVMUH6ubjQN3NxcC2Vs.png" alt width="679" height="317" referrerpolicy="no-referrer"></p>
<p>Quick Build 速度更快，但是精度上会有所误差，只需要2-15分钟就可以完成结果预测。</p>
<p>Standard Build 精度更高，相应的时间也会更长，大概需要2-4个小时。并且标准模式下，产生的模型可以一键分享给数据科学家或者其他同事，进行优化升级。</p>
<h2 id="toc-6">六、Canvas 体验优化建议</h2>
<p>Canvas 也并不是完美无缺的。在体验过程中，我也发现了一些体验细节问题，主要包括2个大类的问题。希望能够改进迭代优化。</p>
<h3>1. 信息反馈</h3>
<p><strong>1）页面提示</strong></p>
<p>用户首次上传数据时，无法直接上传内容。页面中仅仅采用文字按钮提示用户可以“了解更多”。用户看到这样链接时，很容易想到帮助中心大段的文字。所以主动点击的意愿并不强烈。</p>
<p>我个人就是多次查看其他内容后，没有办法最终选择了点击链接。发现在帮助中心中插入了S3桶的链接，需要再次跳转到相关页面，才能完成数据上传，无形中增加了用户的操作成本。</p>
<p>因此页面中需要给用户精炼的提示和功能型按钮，给用户解决方案，而不是简单的链接的形式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/KBwuLXxJAbNtdzu0PzgF.png" alt width="686" height="328" referrerpolicy="no-referrer"></p>
<p><strong>2）操作提示</strong></p>
<p>在S3桶中增加了数据后，在Canvas 导入时，无法选择非CSV格式的文件，例如excel文件，但是页面上没有相应的提示信息，需要用户自己摸索。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/qn7bYLuf2dP0MfmJLtZr.png" alt width="689" height="306" referrerpolicy="no-referrer"></p>
<p><strong>3）用户路径</strong></p>
<p>Canvas相当于一个独立的功能空间，与亚马逊云科技是相互隔离的，页面中缺少返回Amazon SageMaker 和控制台的路径或者链接，用户不知道该如何返回。</p>
<h3>2. 效率提升</h3>
<p><strong>1）操作效率</strong></p>
<p>Canvas中导入的备选数据，无法直接删除，必须要去“数据管理”中才能删除。对于导入误操作用户或者强迫症用户特别不友好，同时也增加了用户操作成本。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/tD086NeYNhd1nQC6lUh2.png" alt width="683" height="321" referrerpolicy="no-referrer"></p>
<p><strong>2）屏显效率</strong></p>
<p>一屏的显示效率，特别是空页面状态，信息展示不全。用户只有滑动后才能看到上传提示信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/CJfFJwUrP2PoHKl9M99J.png" alt width="688" height="345" referrerpolicy="no-referrer"></p>
<p><strong>3）页面跳转效率</strong></p>
<p>在亚马逊云科技产品中所有任务都在同一个浏览器窗口中完成，用户无法并行操作多个窗口。当用户在Canvas中需要完成长时间的模型计算时，如果需要退出当前窗口，必然会产生模型计算是否会停止的担心。同时增加了页面跳转带来的操作成本。</p>
<h2 id="toc-7">七、总结</h2>
<p>通过Amazon SageMaker Canvas的测评体验，我们可以总结下数据产品该如何做好产品体验：</p>
<ul>
<li>围绕用户需求和场景，构建用户体验目标；</li>
<li>减少强制流程，打造并行功能，实现用户的高效操作；</li>
<li>数据表格可视化处理，建立多维度数据呈现，帮助用户深度认知；</li>
<li>关注用户场景拓展，通过协同机制，提升用户体验。</li>
</ul>
<p>以上就是我的个人体验~</p>
<h3>#专栏作家#</h3>
<p>子牧先生。公众号：子牧UXD（HelloDesign），人人都是产品经理专栏作家。产品体验设计师。8年互联网行业经验，擅长体验设计思维、设计方法论、交互设计研究。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5418801" data-author="200991" data-avatar="http://image.woshipm.com/wp-files/2020/10/KjOwksgBxtYVlDsqUgAh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            