
---
title: 'CNCF宣布Linkerd正式毕业！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9378'
author: Dockone
comments: false
date: 2021-07-31 10:07:29
thumbnail: 'https://picsum.photos/400/300?random=9378'
---

<div>   
<br>专为云原生软件构建可持续生态系统的云原生计算基金会（CNCF）日前宣布，Linkerd项目已经正式毕业。Linkerd是第一个加入CNCF Sandbox的项目（当时基金会内部还在使用「开端」项目的表述），如今又成为第一个顺利毕业的服务网格项目。<br>
<br>这也是Expedia、JPMC、微软、Nordstrom等领先企业在生产阶段使用的首个服务网格项目。<br>
<br>Linkerd是一种服务网格，能够为云原生应用程序提供至关重要的可观察性、安全性与可靠性功能，且无需做出任何代码变更。此项目由Buoyant于2016年创建，并于2017年初以基金会第五个项目的身份正式加盟CNCF。作为第一个服务网格项目以及第一个使用Rust编程语言以提高安全性及性能水平的CNCF项目，Linkerd如今已经在为微软、Nordstrom、Expedia、JPMC、Clover Health、Entain以及H-E-B等组织的关键任务生产系统提供支持。<br>
<br>根据最新的云原生调查报告，27%的组织在生产环境中使用服务网格，这一比例较上一年增长了50%；另有42%的企业正在评估或者有计划使用服务网格技术。但Linkerd在这个快速增长的领域也面临着前所未有的竞争压力，好在其用户群体一直急速增长，凭借着良好的口碑征服着更多受众的心。Linkerd项目高度关注简单性、高性能与最终用户体验，并由此在全球范围内吸引到数百名贡献者、在GitHub上狂收几万颗星，也建立起一个由用户及爱好者们组成的活跃社区。<br>
<br>云原生计算基金会CTO Chris Aniszczyk表示，“服务网格可以说是云原生技术领域发展最快的分支之一。而自从Linkerd的诞生掀起服务网格热潮以来，这个前沿项目就一直处于领先地位。随着组织逐步转向云原生，流量管理、可观察性以及安全性正成为基础设施中的关键组成部分。我们很高兴能看到Linkerd一直在不断发展、持续适应变化中的行业需求，并为服务网格及关于代理的其他项目铺平了一条宽阔的生态系统构建之道。”<br>
<br>Buoyant公司CTO、Linkerd项目创始人Oliver Gould也表示，“我们很高兴Linkerd能够像Kubernetes、Prometheus以及Envoy等其他成熟的云原生项目一样，顺利从CNCF毕业。我们的使命是将简单性与同理心带给服务网格领域，我们不知疲倦地工作、只为消除人们对于服务网格或复杂或笨拙的错误印象。虽然我们也做出了具有争议的技术决策——例如采用Rust而非C++，构建专用于服务网格的「微代理」而非通用代理、专注于Kubernetes而非构建抽象层等——但这些决策通通得到了全球运营者社区的验证、理解与支持。”<br>
<br>Buoyant公司CEO兼Linkerd支持者William Morgan提到，“Linkerd顺利毕业的背后，代表着一股令人难以置信的快速发展势头。单是过去一年之内，我们就见证了Linkerd迎来300%的下载量增长，并得到<a href="https://www.cncf.io/blog/2021/02/19/how-a-4-billion-retailer-built-an-enterprise-ready-kubernetes-platform-powered-by-linkerd/">Elkjøp</a>，<a href="https://www.cncf.io/blog/2021/04/19/when-lebron-scores-latency-matters-realizing-10x-throughput-while-driving-down-costs-and-sleeping-through-the-night/">Entain</a>，<a href="https://www.cncf.io/blog/2021/06/21/how-h-e-b-achieved-four-nines-of-reliability-using-kubernetes-and-linkerd/">H-E-B</a>，HP，微软以及NAV等知名组织的采用。凭借着比其他同类解决方案更快、更轻量化、更简单的特性，Linkerd已经成为服务网格的未来，而它在设计上表现出的用户关怀与同心必将继续推动它保持领先地位。”<br>
<br>面对新冠疫情的突然爆发，H-E-B公司最近决定将Linkerd部署到生产环境当中，帮助客户顺利收取日用杂货。公司工程总监Justin Turner指出，“我们选择服务网格并不是为了跟风，我们的团队也不关心哪种网格热度最高。我们需要的只是一套能够正常起效的服务网格，让我们专注于为自身业务构建最佳平台与工具。Linkerd凭借着易用性大大降低了运营复杂度，由此支撑的功能显著简化了我们的决策流程。Linkerd已经成为我们得以快速达成目标的一项关键因素。”<br>
<br>Linkerd项目自身也在制定广泛的发展路线图，包括服务器与客户端策略、帮助Linkerd数据平面在Kubernetes之外运行的“网格扩展”等等。为了始终让项目在简单性、性能与最终用户体验之间取得最佳平衡点，开发团队也在努力降低用户负担与操作复杂性。<br>
<br>为了正式从孵化状态毕业，Linkerd显示出稳定、完善且符合预期的项目成熟度，包括快速增长的采用率以及建立可持续、高包容度社区的承诺。Linkerd具有清晰的维护路径、由最终生产用户组成的指导委员会以及对开放治理理念的明确承诺。Linkerd项目每年都会组织第三方安全审计，最近还在严格的生产测试中引入了代理模糊测试机制。<br>
<br><strong>原文链接：<a href="https://www.cncf.io/announcements/2021/07/28/cloud-native-computing-foundation-announces-linkerd-graduation/?hss_channel=tw-3286770860">Cloud Native Computing Foundation Announces Linkerd Graduation</a></strong>
                                
                                                              
</div>
            