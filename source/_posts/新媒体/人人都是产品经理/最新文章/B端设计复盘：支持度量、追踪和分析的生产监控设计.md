
---
title: 'B端设计复盘：支持度量、追踪和分析的生产监控设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/yCos06ZWLsd0ZoFBz0ba.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 30 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/yCos06ZWLsd0ZoFBz0ba.jpg'
---

<div>   
<blockquote><p>编辑导语：从0到1侧重生产流程监控的系统设计思考，本篇文章侧重点在于实现监控的线上化，并通过自动预警设计解决人力投入成本高、追踪操作耗时久和发现异常不及时3个显著问题。希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-779295 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/yCos06ZWLsd0ZoFBz0ba.jpg" alt referrerpolicy="no-referrer"></p>
<p>随着业务规模的不断扩张，业务的应用场景也在不断的发生变化，不同场景下的各类问题可能会随时发生，如果不能及时发现处理，会对业务或客户造成损失，为此监控能力会变得越来越重要。</p>
<h2 id="toc-1">一、了解功能</h2>
<p>监控是中后台的基础能力，从字面意思拆开理解，就是“监视”和“控制”。</p>
<p>“监视”平台运行的关键数据，在检测到异常时采取对应的“控制”措施，如发出预警通知管理员进行解决或执行预设的自愈措施。</p>
<p>“监视”是手段，“控制”是目的，中后台搭建监控能力其实就是在不断丰富“监视”的手段，以便于更快更准的“控制”业务进展，保障平台业务健康运转。</p>
<p>我们可以通过下面1张图来理解监控能力如何帮助业务运转：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/dbiB98P5gQdjvPGnUSfm.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>当数据发生异常时，监控平台及时感知并预警通知到相应人员进行解决，也可以通过预设的策略判断是否可以进行自动处理，这些都属于及时止损的控制手段。</p>
<p>事后相应人员需要通过数据分析进行问题定位，并彻底根治该问题。最后进行问题的复盘，制定相应的预防措施，避免相同问题再次发生，在有条件的情况下还可以根据新的问题以及场景，训练出新的AI处理策略来自动采取处理措施。</p>
<h3>1. 监控设计的价值</h3>
<p>通过设计帮助用户一目了然的明确数据或流程的当前状态，为用户提供准确的数据，帮助快速定位异常问题；</p>
<p>通过配置设计允许用户通过对异常采取控制策略，保障服务的可靠性和安全性，辅助业务持续稳定运行；</p>
<p>在B端场景中，通过监控的页面设计可以实现对业务数据的异常预警和分析定位，帮助管理员及时采取控制措施，将业务损失降至最低，影响范围降至最小。</p>
<h3> 2. 监控的可应用场景</h3>
<ul>
<li>硬件监控</li>
<li>系统监控</li>
<li>应用监控</li>
<li>网络监控</li>
<li>流量分析</li>
<li>日志监控</li>
<li>安全监控</li>
<li>API监控</li>
<li>性能监控</li>
<li>业务监控</li>
</ul>
<h2 id="toc-2">二、设计功能</h2>
<h3>1. 基于业务梳理关键信息</h3>
<p>今天主要讲的是如何对一个生产线的数据进行监控设计，可以理解为“业务监控”，如何设计需要依赖业务需求，为此我们需要先了解业务的目标用户。</p>
<p><strong>1.1 了解目标用户的问题</strong></p>
<p>通过沟通得知，我们的目标用户主要以产品和运营为主，这部分用户在平台内通常会被分配生产管理员的角色，主要负责进行日常的产线投放、数据追踪和人员绩效管理等工作。</p>
<p>在日常的管理工作中，他们总是需要关注产能、质量和人效相关的问题，比如：<br>
投递到产线的订单会给各环节带来多少任务？</p>
<p>每天的任务投放和完成情况是否符合预期？</p>
<p>每个环节的质量情况是否符合预期？在某个时间段内有哪些任务完成了？</p>
<p>是否有高优任务被卡住了？</p>
<p>用户群组/供应商在各任务的表现如何？…</p>
<p>以上的这些问题，都是目标用户期望通过监控功能来解决的。</p>
<p><strong>1.2 梳理操作流程</strong></p>
<p>为了更好的服务业务，在开始设计前，我们进一步了解了目标用户目前的人工操作流程：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/KKZNW936LfsKfFi5drVI.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>首先，生产管理员在与业务完成对接后会开始<b>制定生产计划</b>：</p>
<p>根据生产线在未来一段时间内的交付数量要求，对任务进行统筹，具体拟定生产的品种、数量、质量和进度的计划；根据历史同类任务的任务流转情况，确定生产线下各任务的预估产量和人员安排。</p>
<p>制定完成计划后，基于目标<b>设定度量依据</b>：</p>
<ul>
<li>产能追踪：投放数、完成数、进行数等；</li>
<li>质量追踪：通过数、通过率、踩雷率等；</li>
<li>人效追踪：提交人数、提交时长等。</li>
</ul>
<p>进行下一步投产，并在投产后定期调取数据<b>追踪生产进展</b>：</p>
<ul>
<li>产能追踪：将完成数与计划数做比较，及时发现产能差距并补救；</li>
<li>质量追踪：通过通过率和踩雷率来确认质量情况；</li>
<li>人效追踪：基于提交人数和提交时长评估供应商或个人的效率状况。</li>
</ul>
<p>当发现异常时，基于多维度数据表格拆解<b>分析关键问题</b>：</p>
<ul>
<li>如按职责维度分析，可以判断是哪个生产职能出了问题；</li>
<li>如按资源维度分析，可以判断是哪类资源出了问题；</li>
<li>如按时间维度分析，可以判断是哪天或哪个小时的进度出了问题；</li>
<li>…</li>
</ul>
<p>定位到关键问题后，结合实际情况<b>采取相应措施</b>。</p>
<ul>
<li>产能问题：增加生产投入，或重新调整供应商分工；</li>
<li>质量问题：回收错误任务、投放地雷、追加抽检等；</li>
<li>人效问题：采取奖惩措施，如绩效扣减、禁用违规账号等。</li>
</ul>
<p>通过以上人工流程我们可以发现监控的3个关键动作：度量、追踪和分析，新的监控能力设计必须支持这3个关键动作才能满足目标用户的需求。</p>
<p>但通过以上流程我们同样也发现了人力投入成本高、追踪操作耗时久和发现异常不及时3个显著问题，这些问题会导致业务流程一旦发生异常，生产管理员没有办法及时的跟进解决，从而给业务造成一些不必要的损失。</p>
<p>那么为了支持3个关键动作并解决以上3个问题，我们在原流程基础上时，增加了自动监控的环节，通过自动预警降低人力投入、减少追踪耗时和提升定位效率。</p>
<p><b>原流程</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/uPDhTSLfTgtGG0nLOf9o.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p><b>新流程</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/wqKhzcGS5F89AmcOQk3s.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>基于新流程，我们可以开展下一步的信息层级梳理工作。</p>
<p><strong>1.3 梳理信息层级</strong></p>
<p>确认新流程后，需要与产品经理、目标用户等相关人员一起梳理监控信息的层级关系。层级可以基于以下问题构建：</p>
<p>在该环节内用户最关心什么信息？</p>
<p>在该环节内用户希望执行哪些操作？</p>
<p>以下是通过讨论后梳理出的信息层级关系：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/HYAanwHfLj2f7r51hHVj.jpg" width="700" height="138" referrerpolicy="no-referrer"></p>
<h3>2. 基于流程和层级开展设计</h3>
<p>为了便于大家理解，我们以故事的形式来描述设计，便于大家代入真实的使用场景中。</p>
<p>今天的主人公是生产管理员小明，他刚刚完成了某业务生产计划的制定，并将一批资源投放至生产线，下一步就需要针对该生产线<b>设置度量依据</b>，便于后续在线上监控生产进展是否正常。</p>
<p><strong>2.1 设定度量依据</strong></p>
<p>这里的度量依据指的是业务的核心指标，即业务关心的具体关键数值，如某个任务的通过率。业务需要衡量进展或成果是否达到预期时，通常会使用核心指标。</p>
<p>回到我们的业务场景里，从2.1的流程中我们也可以看到，生产管理员小明会使用不同的指标进行对比来确认产能、质量和人效是否达到了预期。</p>
<ul>
<li>产能追踪：将完成数与计划数做比较，及时发现产能差距并补救；</li>
<li>质量追踪：通过通过率和踩雷率来确认质量情况；</li>
<li>人效追踪：基于提交人数和提交时长评估供应商或个人的效率状况。</li>
</ul>
<p>因此，为了提升生产管理员查看核心指标的效率，我们需要在监控界面上新增一个核心指标的显示模块，支持生产管理员小明添加指标、删除指标和查看指标变化。如下是相应的交互路径，蓝框为该环节内的主要操作：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/qC2WzwvypICzXMKhR5Fb.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>生产管理员小明来到了下图的产线监控页，但因为该生产线未添加过任何核心指标，所以监控模块内会显示为空态样式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/yy4Jm9iWutoDQ5tyB7dC.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>不同的业务需求通常会对应一条不同的生产线，不同的生产线又会对应不同的衡量指标，因此在上图的界面设计中，我们遵循从左至右的视觉路径，优先在左上角显示生产线的Select框，引导用户选择对应的生产线后再设置指标；当前生产线未添加过任何核心指标时，在模块内显示“请先点击右上角设置指标”的空态提示，引导用户点击右上角的“设置指标”Button进行指标添加。</p>
<p>小明点击添加指标按钮后，在按钮下方弹出如下图所示的TreeSelect选择框。</p>
<p>我们提前按用户关心的维度将指标做了分类，通过采用TreeSelect控件，用户可以便捷选择整个大类指标，也可以通过点击二级指标前的Checkboxes来仅选择某几项指标；随着业务指标的不断增多，用户查找单个指标的成本也会变高，因此我们在树选择控件的上方增加了支持实时匹配关键字的SearchBar，便于快速定位选择某项指标。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/5j22u0Q4w3QSiwyn9kU2.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p><strong>2.2 通过指标卡片追踪进展</strong></p>
<p>小明完成并确认选择后，在模块内会显示相应的指标卡片。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/uPWRDHfNCXtV30oFr4G7.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>小明也可以通过多个核心指标进行对比，来进行相应的产能、质量、人效追踪。</p>
<ul>
<li>产能追踪：将完成数与计划数做比较，及时发现产能差距并补救；</li>
<li>质量追踪：通过通过率和踩雷率来确认质量情况；</li>
<li>人效追踪：基于提交人数和提交时长评估供应商或个人的效率状况。</li>
</ul>
<p>指标的显示统一采用了的卡片的交互样式，支持用户长按拖拽更改指标的显示顺序，为了便于用户与生产计划进行对比，我们默认显示了指标环比的变化情况，这样小明就可以快速定位到今日的指标相对昨日的变化是怎样的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/qtYPJ1I63yiKzBJKFzXT.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>环比的比率变化颜色统一使用了灰色，原因是不同数值的增减对业务而言对应的含义不同，如当日已完成资源数的指标环比下降代表异常；而当日未完成资源数则相反，指标环比上升代表异常。如果要在该模块内精细化定义不同指标变化是否异常，则会带来较大的研发定义成本，不满足从0到1快速上线的诉求，因此我们选择暂时通过指标自动预警功能来实现对异常情况的追踪。</p>
<p><strong>2.3 设置预警规则</strong></p>
<p>生产管理员小明完成核心指标的设置后，通过观察指标卡片上的环比指数发现“指标C”的变化有些接近异常，但想到自己不可能24小时不间断的人工监控这项指标，于是决定设置一个自动预警规则，当“指标C”的数值达到异常值时将自动触发预警，预警通知会发送到目前正在值班的生产管理员处，便于其能够快速对该异常进行处理。如下是相应的交互路径，蓝框为该环节内的主要操作：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/XpUvMer4ImKWC53mUSGW.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>那么首先，我们需要一个预警管理页，在这个页面可以基于指标进行预警规则的增删改查操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/IRqoxETXMK1CdynRm0d1.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>小明发现针对该产线的“指标C”并没有相应的预警规则，那么他也可以选择点击表格右上角的“新增”按钮，创建新的指标预警规则。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/xx66CcIj3ASfXapasmeF.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>创建规则采用了抽屉式表单的交互形式，采用Drawer控件来承载表单操作可以减少用户的页面跳出感，也避免了表单项较少时造成页面利用率低的体验问题。</p>
<p>在规则明细的表单项排布中，因为考虑到指标与监控对象（如生产线）有联动关系，因此在设计时会由上至下优先引导用户选择预警类型和预警对象，完成以上2个表单项后才会出现预警指标表单项，避免用户误操作；为了帮助业务更加精细化定义指标场景，我们增加了筛选条件和维度两个非必填项，可以帮助业务对指定维度指定条件下的指标进行监控。</p>
<p>在触发设置的表单项目设计中，针对触发条件采用了“参数+运算规则+阈值”的混合表单项，提供了丰富的指标条件定义范围：</p>
<p>当左侧参数选中“数值”时，中间运算规则包含“大于、小于、大于或小于”3个选项，右侧阈值输入框受运算规则选项影响展示如下：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/izHV5cMWvhZzXwwEqEWr.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>当左侧参数选中“环比”或“周同比”时，中间运算规则包含“向上波动、向下波动、向上或向下波动”3个选项，右侧阈值输入框受运算规则选项影响展示如下：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/45tbqRJfnOxOStJwSPZR.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>巡警周期也同样采用了混合表单项，提供了“分钟”或“天”的周期自定义设置：</p>
<p>当左侧选中“按分钟”时，右侧显示仅支持单选的Select组件，包含“5分钟、10分钟、30分钟、60分钟和90分钟”5个选项，默认选中5分钟；</p>
<p>当左侧选中“按天”时，右侧显示支持选择时分的TimePikcer组件，默认为空。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/dnQEy9tYAmHvXHCPBFW5.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="536" height="117" referrerpolicy="no-referrer"></p>
<p>最后的通知方式表单项，提供了“人”和“群”两种通知维度，便于用户按照实际情况选择所需的通知方式。</p>
<p><strong>2.4 进展异常出发报警通知</strong></p>
<p>小明完成了预警规则的设置后，就可以安心的先去做其他工作，系统将按照规则对相应指标进行自动监控追踪。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/G8DP1lbUOhtfl8a09dHG.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>当该指标到达了预警值时，小明的工作通讯软件便会收到下图的一条预警记录消息。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" style="color: #666666;" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/UeaPfHax5hby5o4R4GoW.jpeg" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="601" height="340" referrerpolicy="no-referrer"></p>
<p>小明点击消息卡片上的“查看预警分析”按钮，便会启动浏览器跳转至相应的预警分析页。</p>
<p>如果小明的工作通讯软件消息较多，导致该报警消息被错过，我们同样提供了相应的预警记录页，小明可以在该页面内查看近期触发过的预警记录信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/VWM1WSrjelg1g4oJocWl.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>页面顶部提供了两张统计信息卡片：</p>
<p>左侧卡片展示近7天的预警趋势，且支持鼠标Hover显示对应数值；</p>
<p>右侧近7天预警规则TOP5卡片展示最近7天内触发预警次数最多的前5个规则及对应触发预警次数，鼠标Hover规则名称时变蓝，点击后跳转对应预警分析页。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/Csdjjwk6ymkAaT1JcqHQ.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>页面底部的表格默认按最近触发预警的时间降序排列，确保用户优先看到最新的预警记录，点击对应记录表格项内的查看按钮后，跳转至对应预警分析页。</p>
<p><strong>2.5 分析关键问题</strong></p>
<p>小明可以通过观察指标卡片或预警通知获知异常后，需要快速分析定位导致异常的原因在哪里，为此他需要借助图表和数据进行下一步的分析。</p>
<p><b>2.6 通过预警分析确认异常</b></p>
<p>前面提到过，当监测到指标异常时，会自动向设置的用户发送预警通知消息，同时也会在相应的预警记录页内生产一条预警记录，用户可以通过这两个渠道进一步查看相应的图表数据。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/mch1n3uawc2xLvxMK3MG.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>小明通过预警记录进入对应的分析页，在该页可以查看规则相关的明细信息，以及被预警指标的趋势变化。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/FY5mo8RZn8o9cLvctviS.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>页面顶部展示规则明细，便于用户明确预警规则的相关信息；底部展示规则相关的指标趋势，我们可以看到该项规则内要监控的是“学科维度下的语文当日累计未完成资源数”和“学科维度下的英语当日累计未完成资源数”2项指标，因此趋势图和详情表格内会默认展示相应的2条数据：</p>
<p>趋势图内默认根据时间单位展示最近20条节点记录，横轴时间按巡警周期展示对应的时间单位（天或XX分钟），趋势线默认显示节点圆圈，超出预警值警戒线的节点圆圈高亮显示为红色，鼠标Hover节点时显示对应明细卡片；</p>
<p>详情表格左侧的竖轴展示指标维度，右侧依次展示最近20条节点（对应趋势横轴）记录的数值信息，超出预警值的节点数值变为警示的红色。</p>
<p>小明发现了触发预警的节点后，需要做进一步的历史数据对比，分析本期与过去的数据差异情况，剔除周期因素从而判断指标是否真的为异常。</p>
<p>小明可以选择点击趋势图表右上角的对比选择器，选择查看“环比”或“周同比”数据。</p>
<p>环比：本期与上期的对比，如今天和昨天； 周同比：本期与上周同期的对比，如本周三和上周三。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/eYU7jKjf57ZAaGZ7jWEE.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>右上角的对比选择器在切换选中“周同比”或“环比”后，在趋势图内除显示指标在本期的变化趋势外，会额外显示上期或上周同期的趋势线，线条色值采用饱和度降低的相同色系，目前是为了表现两条线的关联性但又不至于将二者进行混淆，当鼠标Hover节点时，在详情卡片上也会新增显示上期或上周同期的数值信息，并增加百分比率的增减信息露出，便于用户快速对比二者的数值差异；详情表格内展示的数值也会跟随“周同比”或“环比”的选择显示对应的数值比率变化信息，鼠标Hover表格项时显示对应的对比明细Tooltips提示。</p>
<p><b>2.7 多维度下钻分析挖掘原因</b></p>
<p>小明通过指标卡片或预警分析确认“指标C”发生异常，如果有过往的沉淀处理措施，小明可以直接对异常采取控制措施进行及时止损，但如果没有过往的处理经验，且无法定位导致指标异常的原因，这时候小明就可以通过假设验证法来挖掘导致异常的真正原因。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/29EQA0Yiru95YG2hedPg.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>例如，小明根据经验假设是因为某供应商在生产线内的支持不力导致了指标异常，那么为了验证假设，小明就需要采用多维度下钻分析来验证假设是否成立。</p>
<p>解释下什么是多维度下钻分析：一般中台需要对接多个不同业务，不同业务的关注点不同，所以大家对数据的维度、粒度要求也不尽相同。通过多维度数据钻取的功能，可以帮助用户更易发现问题所在，进而做出正确的决策：如按职责维度分析，可以判断是哪个生产职能出了问题；如按资源维度分析，可以判断是哪类资源出了问题；如按时间维度分析，可以判断是哪天或哪个小时的进度出了问题；…</p>
<p>那么我们就需要回到产线监控页，并在核心数据模块下方新增一个多维分析模块：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/JGppB98glzB4Lho4SvL2.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>多维分析模块的顶部提供了对应维度的筛选区，方便用户定位到单个维度内的某个值，如供应商A和供应商B曾经有过支持不力的先例，那么我们就可以着重筛选这两个供应商，来查看与他们相关的指标是否存在异常。</p>
<p>筛选区下方展示了<b>预览</b>和<b>流程</b>两个Tab：</p>
<p><b>预览</b>Tab内提供维度和指标的显示筛选，在这里筛选的维度和指标信息将实时同步显示在下图的图表内，便于用户在不同图表视图内随时控制和变更维度/指标的显示，如下图通过趋势和对比清晰展现出关联A、B两个供应商维度的“指标C”数据；</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/UiNqqfA5QQejmJkmxOBW.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="B端设计复盘：支持度量、追踪和分析的生产监控设计" src="https://image.yunyingpai.com/wp/2022/03/0oT9iGXagmKRohamQprT.png" alt="B端设计复盘：支持度量、追踪和分析的生产监控设计" width="700" height="138" referrerpolicy="no-referrer"></p>
<p>流程Tab内按流程节点展示整个生产线的流程图，且在每个节点卡片内平铺展示出所有指标数值的明细，用户可以通过流程图发现定位某项指标的数值异常发生在具体哪一个生产线环节。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/CeC9RO8Jpqf6p77iTUEP.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>点击任意环节卡片后，可以触发该环节相关的下钻数据筛选，支持用户继续针对该节点数据进行多维度分析，以进一步验证在该节点内是哪个维度导致了异常数据的发生。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/btja8gHg2Lr0lryJkKgD.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>基于以上分析能力，小明可以不停尝试更换维度进行下钻分析来验证自己的假设，直到最终挖掘出导致“指标C”异常的原因，并采取相应措施进行及时止损。</p>
<ul>
<li>产能问题：增加生产投入，或重新调整供应商分工；</li>
<li>质量问题：回收错误任务、投放地雷、追加抽检等；</li>
<li>人效问题：采取奖惩措施，如绩效扣减、禁用违规账号等。</li>
</ul>
<h3>3. 提取通用图表设计点</h3>
<p>在进行监控设计时，为了便于目标用户更加直观清晰的查看和定位数据，我们需要借用多类可视化图表来进行表现。</p>
<p>那么首先，我们需要明确该如何选用可视化图表：</p>
<p>选择正确的图表类型取决于显示的数据类型。通常，图表分为构成、对比、关系和分布4大类。</p>
<p>选择哪种类型取决于：</p>
<p>是否要显示某件事的组成部分？是否要比较值或显示一段时间内的差异？是否想更好地理解两个或多个变量之间的关系？是否要显示数据的分布？</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/KOBySvkhPSare66ZCsas.jpg" width="700" height="138" referrerpolicy="no-referrer"></p>
<div>
<p style="text-align: center;">以上图片来自互联网设计帮，作者XC</p>
</div>
<p>基于上述图片指引，在本次设计案例中，我们采用折线图（Line Chart）来表现数据趋势，采用条形图（Line Chart）表现数据对比，又基于生产线的业务特点自行设计了流程图来表现环节数据的流转变化。</p>
<p>其中关于折线图的设计使用，需注意：</p>
<p>折线图的横轴必须为时间维度，否则请勿使用折线图；</p>
<p>尽量避免同时展示的折线超过 5-7 条，否则将影响对比效率，如果一定要超过则需要增加手动隐藏功能；</p>
<p>代表不同类型的折线需要采用对比鲜明的色值，代表同类的折线可以用饱和度控制来表现数据关系（如同一数据的同环比）。</p>
<p>其中关于条形图的设计使用，需注意：</p>
<p>想展示每个类别的数量、比例和频率，应选择单个条形图；</p>
<p>想跨类别比较项目，应选择集群条形图；想显示每个类别之间的部分到整体的关系，应使用堆叠条形图；</p>
<p>底部标签文案较长时，应使用水平条形图； 在堆叠条形图中表现不同类别信息时，应尽量使用清晰明显的对比色。</p>
<h2 id="toc-3">三、总结</h2>
<p>以上是一款从0到1侧重生产流程监控的系统设计思考，本期的侧重点在于实现监控的线上化，并通过自动预警设计解决人力投入成本高、追踪操作耗时久和发现异常不及时3个显著问题。</p>
<p>后续的规划可以基于更多业务场景呈现更丰富的可视化数据分析能力，并提供图表自定义能力，将更多业务核心指标以多类图表的形式呈现在监控页面内，便于产品运营打造所需的仪表盘视图，制定相应的自动化报表推送，实现业务效率和用户体验的进一步提升。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/03/dH0hZPeyY6HEP1sBn5AM.png" alt width="700" height="138" referrerpolicy="no-referrer"></p>
<p>文献参考：</p>
<ul>
<li>https://zhuanlan.zhihu.com/p/360376342″>数据可视化：如何打造高效的仪表盘</li>
<li>https://uxplanet.org/data-heavy-applications-how-to-design-perfect-charts-c0c893fef6de”>Data-heavy applications: How to design perfect charts</li>
</ul>
<h3>#专栏作家#</h3>
<p>愚者秦，微信公众号：feather-wit，人人都是产品经理专栏作家。先后任职于爱奇艺、字节跳动的一枚体验设计师，同时是兼职写小说的斜杠青年，善于总结和抽象设计方法，热衷于探索不同用户场景下的产品策略。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5372792" data-author="86856" data-avatar="http://image.woshipm.com/wp-files/2018/10/kvMfyGYHdrCviAUcOssl.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            