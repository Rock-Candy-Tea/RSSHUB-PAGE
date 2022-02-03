
---
title: '费控软件竞品分析：易快报 VS.分贝通'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/unWWwKYq6B4l64yfehEv.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 03 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/unWWwKYq6B4l64yfehEv.jpg'
---

<div>   
<blockquote><p>在上一篇文章《<strong><a href="http://www.woshipm.com/pd/5292016.html">费控报销系统，如何设计？</a></strong>》当中，我整体介绍了一下SAAS费控产品的架构设计思路。期间收到了不少朋友的私信，提出了他们的建议，在此表示感谢，今后会考虑对系统做出相应的优化。</p>
<p>今天我会对这个细分垂直领域里的部分头部玩家的产品做个分析，看看它们是如何在细节处进行设计。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5307269" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/unWWwKYq6B4l64yfehEv.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>竞品分析分为两种类型：产品整体和部分功能。前者注重产品从上线以来的所有迭代历史，着眼于整体的产品架构体系，再加上详细的行业背景和各种商业数据；而后者重点关注核心的一个或多个功能的设计，包括理念，UI/UX和业务逻辑等，会在纵向上十分深入。</p>
<p>一般来说，对亮点功能的分析在实际工作中的使用频率要远大于后者，因为只有从0开始的项目才需要一个整体产品分析，以便于向上汇报和立项，而功能上的竞品分析却时时刻刻伴随我们每一次重要功能的设计。</p>
<p>本篇文章会聚焦于行业内的两个头部企业移动端app的核心功能组的对比分析，从而让大家对费控报销领域有个详细的认识。经过一段时间的调研，我选取了易快报和分贝通作为对比分析，因为两个企业的创立背景有很大的不同，因此它们的app的业务逻辑和UI/UX设计风格有一定的对比性。</p>
<h2 id="toc-1">一、产品介绍</h2>
<p>让我们先看看两家公司的整体背景介绍和产品矩阵。</p>
<h3>1. 易快报</h3>
<p>易快报的公司全称为合思易快报，成立于2014年11月。易快报为其核心产品，是企业报销，费控与聚合消费平台。为企业提供移动报销、全程费控、聚合消费、预算管理、发票管理和电子化票据归档等一站式解决方案。此外，合思旗下还有另外的三大产品线：</p>
<ul>
<li>合思商城：平台连接滴滴打车、饿了么、各大商旅平台等，为企业员工提供一站式商旅、出行、用餐、采购服务</li>
<li>易会档：财务电子化档案管理系统，用于对电子票据档案的立卷/整理/归档等</li>
<li>合思+：各种类型的插件，主要应用于后台和其它系统的对接</li>
</ul>
<p>易快报以报销业务起家，深耕该领域多年，在智能化报销、费控和票据归档方面，产品设计的细节点基本都覆盖到位了；但在企业消费订购方面，虽然能够做到“无报销”，即员工可直接在商城打车、订餐等，企业直接付款，无需单独开票，省去员工报销时候的流程，但由于业务开展时间晚于分贝通，整个场景的覆盖面稍微少了一些。目前合思正在努力扩展供应商数量，争取早日完善全场景支付。</p>
<p>正因合思从创立之初的稳健表现和未来明确的规划，于2021年8月获D轮融资10亿元，成为费控赛道目前融资最多的企业，体现了资本对于其过往市场表现的高度认可和对未来前景的充足信心。</p>
<h3>2. 分贝通</h3>
<p>分贝通于2016年3月成立，起初定位于企业钱包，只做机票方面的场景，近几年投入主要精力用于扩展全场景，包括住宿、打车、餐饮、采购等。支付方式也从App，扩展到虚拟卡和网银。2021年初，分贝通上线报销功能，完成企业支出管理的三大部分的整合：支付+场景+报销。</p>
<p>相比于费控赛道的其它头部企业比较擅长财务领域，分贝通的DNA主要在于场景。从最早的API连接ToC平台（滴滴、京东等），到后来的介入B2B交易平台和代理商资源,再到后来的直联终端供应商，直到如今的自营直采，分贝通基本已经做到覆盖了企业员工差旅中必要支出的所有场景。此外，对于App内商城中仍旧无法满足的场景，分贝通还推出了虚拟卡服务，可绑定微信和支付宝，进行线下交易。</p>
<p>分贝通的报销功能是应投资人的要求，经过详细的客户调研后，才加进去的。因为分贝通从建立之初就秉持着“干掉报销”的理念，因此报销功能对于其来说只是为了满足部分企业无法开具电子发票而做的一种补充，从而完成整个企业支出的所有方面。但我认为，鉴于目前的经济形势，多数企业面临流动资金的困难，一个完善的报销流程对于部分企业来说或许是一个更好的选择。</p>
<h2 id="toc-2">二、移动端功能对比分析</h2>
<p>本文将围绕两个app的三个核心功能做对比分析，从而让大家能够更加深刻的体会到两家公司在该领域理念上的差异。</p>
<p>移动端报销的整体流程如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bdkheuqv2XMbfpJntbwE.png" alt width="554" height="48" referrerpolicy="no-referrer"></p>
<p>其中，费用申请、消费订购、个人报销和审批在移动端可以完成；其余的步骤只能在PC端完成（不在本文讨论范围）。</p>
<p>此外，对于“无报销”，整体流程可简化为如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/0V3RSFqKyxMkO0CZMsXa.png" alt width="389" height="48" referrerpolicy="no-referrer"></p>
<p>员工消费后无需关注发票，企业会和系统提供方按月对发票，然后记账入档。</p>
<h3>1. 事先申请</h3>
<p>对于大多数企业而言，员工的商务消费基本都需要提交申请，获得直线领导以及财务部门（有时会需要）批准通过。下面列出了这个功能在各个维度上两个app的详细对比分析：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/M8VhwqmGdBeFtiC91V3z.png" alt width="753" height="114" referrerpolicy="no-referrer"></p>
<p><strong>1）入口</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/jRwtKWZ0h37eQb76AJ8R.png" alt width="616" height="591" referrerpolicy="no-referrer"></p>
<p>我们从首页和申请单入口处能看到两者的明显区别：易快报是典型的To B类型app，流程和各节点状态均放在很明显的位置，其单据入口置于底部tab页的中心位置，便于员工查找；而分贝通的To C属性要更浓一些，首页的金刚区和一般纯C端app风格一样，布满各种消费场景的入口；虽然单据申请入口置于金刚区下面，但做的不是很明显，这也符合分贝通一贯的宗旨：去报销流程，鼓励直接消费。</p>
<p>此外，易快报的首页还增加了模块显示的位置和可见性配置，方便用户对根据自身角色对不同模块的管理。</p>
<p><strong>2）UI/UX</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/0BAuzdWo4vd4ynVipoqj.png" alt width="534" height="675" referrerpolicy="no-referrer"></p>
<p>对于表单的UI/UX来说，两者基本没什么差别，这里主要想说一下校验提示的问题：易快报的校验提示方式是在字段旁加个!，用户点击后才可以看到原因，相当于多操作了一步；分贝通则是用toast做的提示，但只有几秒钟，有时候会看不清。所以我觉得比较好的方式是直接显示校验提示在字段旁边，这样一目了然。</p>
<p>此外，分贝通无表单自动保存功能，且“稍后提交”功能需要全部字段通过校验才可以保存，用户体验稍差一些。</p>
<p><strong>3）审核流/表单配置</strong></p>
<p>两个app都做到了后台审核流的自定义配置：既可以做到对固定流程预先定好的节点属性的配置，又可以做弹性流程，用户送审时直接选择审批人，无需管理员在后台预先定义好，符合现代B端产品流程设置的标准做法。</p>
<p><strong>4）费用标准和预算控制</strong></p>
<p>易快报对员工费用申请时的费用标准和预算在后台都有详细的配置。一旦员工超额，系统会在提交表单时给予提示。对于预算管控，易快报提供预算编制、执行与控制、分析等功能，使企业可以做到预算的精细化管理。</p>
<p>虽然分贝通也上线了预算控制相关功能，但在细节和业务成熟度方面显然还需要一段时间的提高。</p>
<h3>2. 消费订购</h3>
<p>员工的事先申请批准后，即可到app中的商城进行消费。</p>
<p>在部分场景下，员工消费后，无需开具发票，企业会按月收到统一的发票，这就是现在费控赛道各个公司都在推崇的“去报销化”。</p>
<p>费控公司在简化员工企业消费流程的同时，还能从合作的供应商那里获得佣金，的确是一件双赢的事，这将会成为未来费控公司一个主要的收入来源和盈利模式。因此以易快报为代表的老牌费控企业在2018年便开始在此领域积极布局，但相比从一出生就带着消费基因的分贝通，易快报在消费场景和支付方式上仍旧有一段很长的路要走。</p>
<p>目前分贝通的这一功能基本可以笑傲整个报销赛道。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ILuG3FeIQ3UEOFB0GLep.png" alt width="608" height="99" referrerpolicy="no-referrer"></p>
<p><strong>1）场景种类</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/DwX6qfyKlYg6GaghuouX.png" alt width="512" height="520" referrerpolicy="no-referrer"></p>
<p>首先，易快报只是将聚合消费平台放在了二级页面，而分贝通将其置于首页金刚区，可以看出聚合消费目前在各自公司的地位。但正如前面所说，“无报销”可能会是今后的一个趋势，在易快报丰富场景后，我相信整个产品架构会有所调整。</p>
<p>其次，分贝通的场景明显要更加丰富（多出闪送、国际机票和用餐），且在某些场景下还做到了和终端供应商的直连，如国内航空公司，酒店等。这样整体价格会更实惠。</p>
<p><strong>2）支付方式</strong></p>
<p>易快报：只提供了线上的支付方式</p>
<p>分贝通：提供线上的App支付 + 线下的虚拟卡支付。</p>
<p>为了满足部分线上场景覆盖不到的情况，如加油站等，员工可向与分贝通合作的银行申请企业信用卡。员工填写表单提交后，由银行对其进行风控测评，而后员工得到虚拟卡额度，并将其绑定到微信和支付宝上，可在线下进行扫码交易。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TrxDUR5Kedwe5WRx8M6E.png" alt width="160" height="331" referrerpolicy="no-referrer"></p>
<p><strong>3）UI/UX</strong></p>
<p>易快报：将H5子页面内嵌于app中。这样可以缩短上线的时间，争取早日为客户提供相应的服务，弥补其在该领域的短板。</p>
<p>分贝通：除了“用餐”模块是将大众点评的H5内嵌进来之外，其余的场景均为原生页面。</p>
<p>从用户体验上来说，原生页面无论是在响应速度，还是UI的适配性上，都是要优于H5的；但相较于体验，用户其实更看重价格是否优惠以及场景覆盖是否齐全。因此该赛道的企业们今后在供应商的争夺上会更加激烈。</p>
<p>4）特色功能</p>
<p>分贝通还额外提供福利补助的场景，涉及交通补助、商旅补助、话费补助、加班餐补助等。员工可使用提供的分贝券进行消费。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/EGLKVQSH3MTHpqzjJN94.png" alt width="178" height="362" referrerpolicy="no-referrer"></p>
<h3>3. 个人报销</h3>
<p>目前，电子发票尚未完全普及，手动开票的情况依旧很多，因此员工消在企业消费后的报销流程仍然十分重要。易快报作为一家起步于SAAS报销的企业，多年来一直在不断对个人报销流程进行完善，我们可以从功能中很多细节看出其对业务的理解之深。而作为2021年初才上线报销流程的分贝通，确实还需要对相关功能进行更深层次的打磨。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ZUt0En7Yo3h0TRFkzDCl.png" alt width="756" height="90" referrerpolicy="no-referrer"></p>
<p><strong>1）发票采集</strong></p>
<p>员工在报销前需要将纸质发票或电子发票导入app内：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/8DF8K1F4ekthGgByaUk3.png" alt width="461" height="465" referrerpolicy="no-referrer"></p>
<p>从上面的UI可以看到，易快报提供的发票导入方式要多于分贝通，且易快报的后台提供发票的电子档案管理，建立全面的发票管理视角。</p>
<p><strong>2）字段和审批流</strong></p>
<p>与事先申请流程类似，报销流程的表单字段和审批流也可以在后台自定义。</p>
<p><strong>3）表单细节</strong></p>
<p>易快报的报销流程中还增加了事先申请的关联以及借款核销功能，使整个报销流程更加完整和便利化。同时，当用户无意间退出页面后，表单内容会自动保存，下次进入时仍可以继续之前的内容填写。而分贝通只是做了基本信息的收集。</p>
<p><strong>4）特色功能</strong></p>
<p>易快报还在此流程中加入了一些特色功能：</p>
<p>（1）费用分摊</p>
<p>费用分摊可对多个核算主体共同承担的费用成本，在报销时按照一定的规则进行分摊，有效促进内部形成持续的成本降低机制，进而优化项目成本结构，量化企业资源配置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ARxRQrM2u5pTBmAruncW.png" alt width="223" height="388" referrerpolicy="no-referrer"></p>
<p>（2) 单据自动生成打印模板</p>
<p>单据可自动生成统一标准的打印模板，金额大小自动转换，免去手写单据易错之忧。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/3zAEGLILa4yyOxqAJww6.png" alt width="554" height="234" referrerpolicy="no-referrer"></p>
<p>（3) 信用报销</p>
<p>通过建立信用报销机制，引导员工提高报销合规性和准确性，信用等级越高的员工，报销流程越简单、审批通过速度越快。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/UYOVL4LDT0IbFPKZJL9y.png" alt width="693" height="353" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、总结</h2>
<p>以上只是针对两个app的核心功能做了对比分析，我们可以清楚的看到两家企业目前的核心业务是什么。但不可否认的是，两种业务模式正从殊途走向同归，即都朝着SAAS+交易的方向前进。</p>
<p>报销是非常适合互联网化的，因为它的流程是单纯、线性和标准化的；而互联网化事物的核心之一就是标准化。但单纯地做报销是无法解决目前收入仅来自几十家核心企业用户的窘境的。因此扩展消费领域是传统报销软件亟需要做的。对于目前以企业商旅消费平台为核心的公司也是一样的道理，它们也需要完善报销流程场景，来增加对上游供应商的议价能力。</p>
<p>两种模式的企业犹如分别从喜马拉雅的南北坡向上登顶的登山队员，到底谁能够率先登顶，或是某个坡出现“雪崩”，都是未知，让我们一起拭目以待吧。</p>
<p> </p>
<p>作者：Dave，捷信（中国）消费金融产品经理</p>
<p>本文由 @Dave 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5306766" data-author="921802" data-avatar="https://static.qidianla.com/woshipm_def_head_4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            