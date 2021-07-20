
---
title: '基于客户和用户需求的B端产品系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rNGTPNq92ePm8p0yqtkr.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 20 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rNGTPNq92ePm8p0yqtkr.jpg'
---

<div>   
<blockquote><p>编辑导语：基于互联网的发展，B端产品不断涌入市场，面对竞争，做好客户与用户需求这方面的工作就显得尤为重要。作者分享了自己在项目中的规划与设计思路，并对此进行复盘分析，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4903181 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rNGTPNq92ePm8p0yqtkr.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景概述</h2>
<p>随着产业互联网的大势愈发成熟，B端企业和产品需求越来越多。这个项目是集后台系统、APP、硬件为一体的系统项目，本文是对项目规划与设计思路进行复盘分析，既是自己对项目的总结和回顾，也希望能带给你一些启发和思考。</p>
<ul>
<li>产品定位：【装维AI营维系统】是在装维场景下，为运营商提供语音质检与分析服务，帮助其提升服务和营销质量，建立装维服务数字化管理机制。</li>
<li>目标客户：运营商相关部门（如网络部）</li>
<li>目标用户：运营商运营人员、装维师傅</li>
<li>解决的核心问题：打开装维服务过程黑盒，助力提升装维服务和营销执行率，进而提升客户满意度和渠道产能。</li>
<li>主要场景：通过录音笔对装维上门服务过程进行录音，将录音送至后台进行质检分析，基于规则模型得出直接结果，包括得分、合违规情况、多维度分析等等。</li>
</ul>
<p>在商业模式上，该项目主要采用的是运营制，即按月提供运营服务，在我接手这个项目时，已经有了基础框架，但是整体产品还出于探索阶段，客户有意向的项目都还在poc（试用）。</p>
<p>这个阶段产品规划的重点，一方面是找到更多产品卖点（拓展新商机），另一方面是保障产品使用的稳定性（保障交付）。以下是从客户和用户需求的角度对整个产品系统的思考和设计过程的整理分析：</p>
<h2 id="toc-2">二、客户及用户需求分析</h2>
<p>B端产品跟C端有一个重要的区别就是，除了用户，我们更需要关注产品购买决策者——也就是客户的诉求，这是我们产品之所以能够存活下来的关键。</p>
<p>因此，在开展产品规划与设计工作之前需要针对客户和用户需求进行了深入调研和分析。</p>
<h3>1. 客户需求收集</h3>
<p>为了更加精准的击中客户痛点，笔者主要从以下几个方面入手去挖掘客户需求：</p>
<ul>
<li>客户直接反馈：在poc阶段或者前期商务阶段，通过与客户进行商务沟通，对接客户关注的要点</li>
<li>市场侧反馈：市场侧是最靠近客户的一群人，他们最连接客户想要什么，所以他们的意见是客户需求的重要来源</li>
<li>市场分析、竞争分析：由于b端产品都是企业内部资源，相关材料一般很难获取到，因而市场和竞品分析一般做起来没那么容易，但是如果能够获取到市场和竞争对手的情况，便可以做到知己知彼，挖掘产品突破点</li>
<li>产品经理洞察：经营丰富的产品经理可以基于对业务的认知洞察出解决客户问题的好需求，这个取决于产品个人</li>
<li>用户调研：即使用户不是最终购买产品的决策者，但是深入调研用户使用场景，可以更好地解决客户的问题，有充足的调研举证才有足够的产品说服力</li>
</ul>
<p>基于以上方法，笔者逐渐聚焦了项目中客户关注的重点：</p>
<ul>
<li>装维师傅抵触，怕花了钱他们却不用；</li>
<li>转写效果（尤其是方言）；</li>
<li>模型准确性（本来合格的判为违规）；</li>
<li>合违规、分数与他们实际关注的点的强关联性（能不能真的反映出问题）；</li>
<li>佩戴之后真实的提升怎样，要能够直观看到；</li>
<li>……</li>
</ul>
<h3>2. 用户需求收集</h3>
<p>关于用户需求收集的方法网上太多了，就不在这里赘述了，这里需要强调一下调研一线使用场景的重要性。这里笔者跟随装维师傅上门，观察了他们进行装维服务的整个过程，这样能够对用户使用状态有个清晰且宏观认识、身临其境地找到生产环境所遇到的问题。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/jjExhRva3WkbqrxR83Wn.jpeg" alt width="616" referrerpolicy="no-referrer"></p>
<p>通过现场调研情况，对装维师傅整个服务过程进行了梳理，输出用户体验地图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lqnKVda1eA3BIx7d9Szk.jpg" alt width="668" height="1174" referrerpolicy="no-referrer"></p>
<p>从体验地图可以看出，装维师傅在接单后预约上门、上门服务过程中、结束后同步上传录音这三个点的情绪体验较差，在接单上门时，工单分配机制过于机械，有些人单子多得做不完，有些人又没单子。</p>
<p>在服务过程中，由于操作流程复杂、项目较多，而时间又很紧，装维师傅都是一路小跑着做的，如果要增加额外的操作的话，会影响他们的服务效率和体验；在结束服务后，同步和上传录音的过程比较耗费时间。</p>
<h3>3. 需求分析</h3>
<p>完成了对客户和用户需求的收集后，得到需求池，接下来要做的就是从多个维度对需求进行分析，关于需求分析工具有KONA模型、SWOT、5W1H1V、重要紧急十字象限法等，可以根据实际需要选择来进行分析。这里提供几个适用于B端产品客户和用户需求的分析维度：</p>
<ul>
<li>业务价值：注意是从商业角度出发，注重解决客户最痛的痛点，有助于商务推广和提高成单率</li>
<li>可复用度：需求可复用在标准化产品上，满足其它项目的交付，而不是过于定制化</li>
<li>可行性：需要从技术边界、用户体验等角度评估需求是否可行</li>
<li>成本：从研发成本、运营成本等角度评估，考虑投资回报率</li>
</ul>
<h2 id="toc-3">三、产品规划与设计</h2>
<p>在前期市场推广阶段，产品已经有了雏形，通过拾音-上传-转写并质检的整个过程，基本已经实现了对服务流程的监控：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/T1Bztssw1HM34ELCJ7Nv.png" alt width="777" height="745" referrerpolicy="no-referrer"></p>
<p>到这里，产品经理脑海里的关于要做什么思路基本已经清晰，下一步就是基于已有的这个产品系统去管理需求、进行合理的版本规划，也就是考虑怎么做的事情了。</p>
<p>版本规划不是最重要功能一个版本全做了，而是要考虑研发资源，考虑紧急程度，一般每一个版本需要有一个核心目标，优先满足跟这个核心目标相关联的需求的设计和开发。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DXlWVcNXlTcHi2olBHb0.png" alt width="648" height="850" referrerpolicy="no-referrer"></p>
<h3>1. 拾音方案规划与设计</h3>
<ul>
<li>目标人群：装维师傅</li>
<li>需求描述：硬件拾音优化三步走：蓝牙耳机→B1录音笔；离线录音→在线+离线；APP→SDK。</li>
<li>需求价值：简化操作流程，避免干扰正常操作流程，降低装维师傅抵触心理</li>
</ul>
<p>方案设计详情：</p>
<p><strong>（1）蓝牙耳机→B1录音笔</strong></p>
<p>项目前期拾音设备使用的是蓝牙耳机，由于在试点过程中发现了较多问题，如耗电过高、拾音效果差、打电话影响拾音等，所以将拾音设备更换成领夹录音笔B1，录音方式由在线录音更改为离线录音，这样装维师傅只需上门点击设备录音，结束服务后关闭录音，然后集中上传即可。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/soqCZxGNkH8brabhGKza.jpeg" alt width="848" referrerpolicy="no-referrer"></p>
<p>完成了方案集成后，在试点过程中发现，由于文件较大及受蓝牙协议传输限制，音频同步时间较长，1小时音频需要10-20分钟以上，这在对于装维师傅来说肯定是难以接受的，所以开始推动硬件厂商压缩音频，但是压缩音频会一定程度上影响音频质量进而影响转效果。</p>
<p>为了压缩音频所带来的影响，选取了8倍和4倍压缩的设备录制了音频传回来进行了测试分析。</p>
<p>如下图，左侧是压缩后的音频大小和同步时长，右侧为压缩前后的转写效果对比。总体来说：8倍压缩音频比4倍压缩音频音质差异不大，可正常实现转写。</p>
<p>音频同步时长正常情况下能够比原来缩短1/2左右，不过部分安卓机缩短情况并不明显。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DzMfLrYiv5VJK1w6INMh.jpeg" alt width="629" referrerpolicy="no-referrer"></p>
<p>基于以上测试结论，最终采用了8倍压缩的在线方案，同时为用户提供了通过有线传输的方式同步音频（硬件自带连接线，但是需要额外采购otg转接头），有线传输的同步时间非常快，1小时音频基本几秒就可以完成同步。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/iw57EKee4onnWbb4mDuK.jpeg" alt width="629" referrerpolicy="no-referrer"></p>
<p><strong>（2）离线录音→在线+离线</strong></p>
<p>在试点（poc）项目应用了一段时间后发现，离线方案最大的问题还是同步过程过于缓慢，使用otg有线传输的话一方面操作不方便，另一方面也一定程度增加了我们的（采购）成本。</p>
<p>所以还是需要寻找其他解决办法，内部讨论后，最终决定采用在线+离线的方案，即主流程使用在线拾音，如果中途异常中断，B1还在继续录音，那么可以将离线录制（丢失）的音频补录上传。</p>
<p>在设计过程中，这里有个难点就是，异常情况非常多，必须每一种情况都考虑到并设计处理机制，包括：录音中异常中断、异常中断自动重连成功、重连成功如果b1正在录音、重连成功b1已停止录音、中断期间b1录制了其它离线录音、多个录音笔……</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/3mH32x3hF07VUn1rTlkM.png" alt width="637" height="766" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/0DPESc509thvLzFK37Jy.png" alt width="692" height="686" referrerpolicy="no-referrer"></p>
<p><strong>（3）APP→SDK</strong></p>
<p>通过前面从蓝牙到录音笔、从离线到在线录音，拾音方案的改造已经完成了一大半。但是依然面临两个问题：</p>
<ul>
<li>对于装维师傅来说，录音操作干扰了他们的服务流程，因为他们在服务前后必须要打开我们的APP进行录音和上传，有些容易忘，有些比较抵触；</li>
<li>由于上传音频的时间没有限制，导致音频造假情况较为严重，很多装维师傅都是下来之后随便录了一段传上去。</li>
</ul>
<p>装维师傅都会使用一个由运营商提供的工单APP，主要用于接单、回单、上传装维相关信息等工单处理。</p>
<p>所以，为了尽可能降低对装维服务流程的干扰，我们决定采用嵌入SDK的拾音方案，即将我们的录音及分析功能作为SDK嵌入他们的工单APP里，具体业务流程如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bEzZXc4CLObp1wM8We5h.png" alt width="647" height="525" referrerpolicy="no-referrer">SDK方案将录音流程与他们的工单绑定，当装维师傅上门后点击签到时，自动开始录音，点击回单时自动结束录音，这样就不需要单独打开装维助手APP进行录音了；由于录音操作与他们工单系统管理，所以也避免了装维师傅线下录制造假音频的情况。</p>
<p>到这里，总体来说拾音方案改造主体基本完成。不过也面临不少挑战厄待解决：由于与第三方的对接联调成本问题、不好测试、使用过程中的异常情况……</p>
<h3>2. 后台系统设计</h3>
<p>后台系统的目标人群可以分为两类：客户、运营人员（用户），运营人员包括客户运营和我们自己的运营人员。这里从客户和用户的角度阐述具体方案设计详情：</p>
<p><strong>（1）针对客户的需求设计</strong></p>
<p>针对客户需求的重点在于助力市场推广，增加新的产品卖点，基于调研和需求分析结果，主要规划了建立标签体系、突出营销两大部分功能。</p>
<p><strong>标签体系：</strong></p>
<p>标签体系包括规则标签+话术标签+客户画像标签。规则标签和话术标签统一为一个标签，用于对规则和话术的分类管理：<br>
<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7xs07n7RxARv56cnulk2.jpg" alt width="508" height="825" referrerpolicy="no-referrer"></p>
<p>客户画像标签主要用于装维师傅上门后基于对客户的了解，给客户打标签（如下图），以此建立客户的基本画像：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/VD64jN2PHLVHfqOj6SM5.png" alt width="655" height="826" referrerpolicy="no-referrer"></p>
<p>标签体系的建立，一方面将零散的规则、话术进行了分类，便于前端web和APP页面更加直观地展示，另一方面基于标签建立客户画像也为客户收集客户信息、后续进一步进行精准服务和营销做了铺垫。</p>
<p><strong>突出营销：</strong></p>
<p>突出营销的目的，主要把营销的规则进行分类，在营销首页即可看到产品销售情况，也就是营销规则标签（如路由器、智能组网等）的命中情况。</p>
<p>通过直观展示产品营销报表，客户可以看到装维师傅的产品营销执行情况，更有针对性地施加引导装维师傅，从而提升产品营销的执行率，达到提升装维渠道产能的目的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/PDO1MyDYKCw2IZjXVWPd.png" alt width="679" height="812" referrerpolicy="no-referrer"></p>
<p><strong>（2）针对用户的需求设计</strong></p>
<p>针对用户的需求重点在于提升用户体验，降低操作成本，这里主要列举三个需求方向：</p>
<p><strong>Poc标注：</strong></p>
<p>Poc标注包含一期和二期，一期为修改转写结果，通过短时间优化转写效果，提升产品Poc试点效果。</p>
<p>二期将语料与规则绑定，以此来提升建立标注集，运营人员在线即可优化模型，由此降低了运营人员的操作成本（以前是在线下编辑模型文档，然后再复制粘贴上去）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/YTzseybGaGBid5kaWZTV.jpg" alt width="650" height="959" referrerpolicy="no-referrer"></p>
<p><strong>报表优化：</strong></p>
<p>报表概览页面主要承担了音频质检结果与统计的作用，对于客户管理员统计数据、汇总分析来说较为关键，因此对该页面进行了优化。</p>
<p>一方面在顶部增加以区域为维度、（产品）营销命中模块，增加分析维度的多样性。</p>
<p>另一方面，以前的报表只能按区域数据，归集方式较为单一，优化后，用户可以按照区域、时间、装维师傅等维度选择目标数据进行统计对比分析，功能数据展示更加灵活。</p>
<p>其次，去掉了冗杂的“查看”（下钻到次级页面）的功能，使重点更加清晰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AqWmwTEyoqxKJkqWUrKW.jpg" alt width="681" height="1900" referrerpolicy="no-referrer"></p>
<p><strong>体验优化：</strong></p>
<p>虽然相对于c端产品，b端产品在用户体验上要求没那么严格和重要，但是良好的用户体验既能给用户带来流程高效的使用体验、留下良好的印象，也是积攒良好口碑的重要因素。</p>
<p>如果在满足了客户及用户核心功能需求之外用户体验也能能够做的好，将作为加分项提示客户对产品的信任度，为后续产品市场和推广都奠定好了基础。</p>
<p>体验方面，b端产品有参考的设计体系，常用的有阿里的Ant design、谷歌的Material design等等，按照规范设计一般不会出太大问题，这里举一个从用户体验角度进行优化的例子——首页报表及布局优化：</p>
<p>如下图所示，左侧为优化前的首页报表，左侧图下方左右分别为规则合违规情况统计和服务趋势统计表，存在两个问题，一方面只有各个规则的横向占比对比，没有单股规则的合违规情况。</p>
<p>其次是服务量趋势图占比过大，压缩了左侧更重要的规则分析图表，有点喧宾夺主。</p>
<p>如右图所示优化后，通过柱状图的展示方式，用户可以直观看到所有规则的合违规对比以及单个规则合违规情况，右侧为按时间维度的每个规则的趋势图，通过这两个图表可以更加完整地呈现规则合违规情况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cEsIA8dRF4IGWqi0vEn5.jpg" alt width="699" height="1040" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、总结</h2>
<p>对待客户需求，要去粗取精，找到客户需求表象背后的真实真正痛点，针对性满足并考虑标准化，而不是被客户牵着鼻子走说要做什么立马满足。</p>
<p>对待用户需求，重点是要搞清楚用户在决策链中的角色，他们在场景中遇到的问题是否与业务强相关。</p>
<p>总之，用产品的人不一定是最后买产品的人，作为b端产品经理，要在用户、客户与商业利益之间寻找平衡，我们要做的不仅是做好产品满足用户和客户当前的需求，更重要的是怎么为客户（企业）创造长远的价值。</p>
<p>最后，笔者整理了B端产品的客户和用户需求与产品设计模型，希望在b端产品设计之路上能为你提供参考。</p>
<p>在需求收集阶段，结合客户与用户需求，从市场分析、竞争分析、客户反馈、数据分析、户调研、市场侧反馈等渠道收集整理需求。</p>
<p>然后从业务价值、可复用度、可行性、紧急程度、开发成本等方面综合分析与评估，最后结合自身产品形态与技术边界进行产品规划与设计（如下图）。</p>
<p style="text-align: center;"><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/30VtYrqgaMn4czYo0XEO.jpeg" alt width="616" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">模型</p>
<p> </p>
<p>本文由 @行者陈 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4895501" data-author="196765" data-avatar="http://wen.woshipm.com/assets/images/def_head.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            