
---
title: 'Cilium母公司宣布完成4000万美元B轮融资'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=6593'
author: Dockone
comments: false
date: 2022-09-16 09:11:18
thumbnail: 'https://picsum.photos/400/300?random=6593'
---

<div>   
<br>作为Cilium与eBPF两大发展迅猛的开源技术方案背后的领先厂商，Isovalent日前宣布已完成由Thomvest Ventures领投的4000万美元B轮融资。此次新参与融资的还有M12（微软的风险基金）和Grafana Labs，连同此前曾经注资的谷歌和思科共同成为Isovalent的战略投资方。其他投资方还包括Andereessen Horowitz、Mango Capital以及Mirae Asset Capital。<br>
<br>Isovalent公司一手打造出Cilium项目和Isovalent Cilium Eneterprise。目前，Cilium已经成为云原生连接领域客观意义上的安全与可观察性标准，并被多家主要公有云服务商指定为各托管Kubernetes产品的默认配置，具体包括Google Kubernetes Engine、Google Anthos以及Amazon EKS Anywhere。Adobe、Bell Canada、Capital One、Datadog、Palantir、宜家以及Sky等大型企业的平台工程团队也与Isovalent保持着合作，借其方案在云原生环境中实现企业级连接。<br>
<br><h3>云原生服务中的全新连接与安全层</h3>Isovalent公司CEO Dan Wendlandt解释道，“我们的客户主要是企业和电信运营商。他们普遍迈过了Kubernetes的前期部署阶段，正在向以安全稳定运营为诉求的第二阶段进发。然而，Kubernetes本身并未提供安全、可观察、可靠且性能优异的网络层。因此，Cilium在众多垂直领域得到广泛应用，包括金融/支付、电子商务/零售、保险、电信、政府、数据分析、娱乐等等，这也凸显出只有我们帮助用户解决掉这些难题，他们才能在Kubernetes之旅上继续迈出下一步。”<br>
<br>正是旺盛的市场需求，推动Cilium广泛进入各大云服务商的托管Kubernetes产品，帮助更多用户轻松应对这些连接挑战。<br>
<br>微软Azure核心工程集团副总裁Deepak Bansal也表示，“随着越来越多的客户在Azure上使用Kubernetes并取得成功，我们看到市场对高级网络和安全用例提出了愈发强烈的需求。eBPF和Cilium正是Kubernetes当中实现可扩展性与安全连接的领先开源技术。Isovalent正凭借这些技术引领各开源社区。通过Azure Networking与Isovalent之间的合作关系，我们将为客户带来最佳eBPF与Cilium集成方案和使用体验。”<br>
<br>自2018年推出以来，基于eBPF技术的Cilium就始终保持着爆发式增长。Cilium项目共拥有463位贡献者，在GitHub上斩获1.28万星，并吸引到1.2万余位Slack社区成员，已经成为Kubernetes生态系统中增速最快的云原生连接项目之一。Cilium也是云原生计算基金会（CNCF）中唯一处于孵化级别的容器网络接口（CNI），预计将在2023年上半年正式毕业。<br>
<br><h3>Isovalent：Cilium与eBPF背后的先驱者</h3>Cilium的迅速崛起离不开eBPF的有力支持。eBPF是一种强大的新型Linux内核技术，现已在所有主流Linux发行版中得到广泛应用。以往，Linux内核功能的发展一直比较缓慢，新代码往往需要几年才能渗透进企业客户使用的实际版本。但eBPF提供一种安全有效的新机制，能够直接向Linux内核中注入新功能，从而引发了一波席卷所有主流Linux发行版的创新浪潮。<br>
<br>除了开发出基于eBPF的领先解决方案Cilium之外，Isovalent公司还联手Linux内核上游共同维护eBPF代码库，同时成为围绕eBPF建立开源社区的有力推手。Isovalent维持有ebpf.io网站，主办eBPF峰会（目前规模最大的eBPF社区会议），并与创始成员Meta、Netflix、谷歌和微软一道建立了eBPF基金会。<br>
<br>Andreessen Horowitz普通合伙人、SDN）先驱厂商Nicira（于2012年以12.6亿美元被VMware收购）联合创始人Martin Casado表示，“eBPF和Cilium正是新型基础设施层中的关键技术。网络与安全的焦点已经转移，先是由最初的硬件转向软件管理程序，如今又转向Linux内核。在这一新层的支持下，连接、防火墙、负载均衡与网络监控都将在Linux内核之中处理，从而为安全性和可观察性提供更丰富的上下文，同时确保所有类型的底层云基础设施均拥有一致的可见性和可控性。Isovalent公司在这一领域具备独特优势，有望成为这一关键新层中的领先厂商。”<br>
<br><h3>通过Isovalent Cilium Enterprise为客户及生态系统赋能</h3>Isovalent公司还通过商业产品Isovalent Cilium Enterprise与各领先企业及电信运营商合作。这款商业版本结合了开源Cilium的强分发与主动客户支持功能，同时添加了企业专用网络、安全性及可观察性等增强特性。<br>
<br>Isovalent Cilium Enterprise的功能包括：<br>
<ul><li>可扩展的多云网络</li><li>高效且动态的服务负载均衡</li><li>支持服务身份感知的网络防火墙</li><li>网络与API层可观察性</li><li>透明网络加密</li><li>运行时安全可观察性与保障</li><li>无Sidecar的服务网格</li></ul><br>
<br>企业希望让这些功能与Kubernetes生态系统中的其他主要供应商产品无缝对接。为此，Isovalent已经与各主要云服务商、Red Hat OpenShift、SUSE Rancher及其他领先Kubernetes发行版合作，确保为各方的共同客户提供兼容良好、更加精简的Isovalent Cilium Enterprise操作体验。<br>
<br>参与B轮融资的Grafana Labs则为Cilium奠定了对接基础，使其生成的可观察性数据能够与更广泛的开源可观察性生态间顺畅协同。Grafana Labs公司CEO兼联合创始人Raj Dutt指出，“当我们初次与Isovalent团队接触时，就意识到双方技术其实高度互补。在深入推进技术研究之后，我们很快发现只要共同努力将基于eBPF的可观察性引入Kubernetes中的监控、故障排查和安全工作流，双方的共同客户及整个社区群体都将有所收益。因此，我们很高兴能支持Isovalent的进一步发展，助力他们达成技术使命。”<br>
<br><h3>Isovalent的探索仍在继续</h3>Isovalent公司由Dan Wndlandt和Thomas Graf于2017年创立，立志以eBPF这项变革性技术为基础，将Linux网络连接与安全性融入由Kubernetes和微服务开创的新时代。在加入Isovalent之前，Wendlandt曾是SDN先驱厂商Nicira的创始员工之一，曾负责领导Open vSwitch（简称OVS）和SDN控制器（也就是现在的VMware NSX）的产品战略。Graf则是Linux内核社区的长期领导者，曾在Red Hat和思科供职期间投身于Linux网络和安全层众多关键增强功能的研发最前沿。感受到eBPF的革命性潜力，Graf及其他Isovalent团队成员于2016年建立了Cilium项目。<br>
<br>Thomvest Ventures合伙人Umesh Padval谈到，“过去一年以来，不少初创企业和大型供应商已经感受到了eBPF的巨大潜力。但Dan、Thomas和Isovalent团队早在几年之前就开始了行动。凭借卓越的技术远见，再加上对如何建立成功开源社区的深刻理解，目前各大领先企业及所有主要云服务商都在围绕Cilium进行标准化设计。Isovalent正把握着千载难逢的机会，有望在企业基础设施堆栈当中建立起前所未有、令人难以置信的全新战略层。我们很高兴能够成为他们探索之旅上的同路人。”<br>
<br>为了持续推动开源创新，Isovalent将运用B轮融资筹集的款项在eBPF社区中继续发挥主导作用，并推动Cilium成长为Kubernetes网络、安全与服务网格领域的领先技术。Isovalent公司还将迅速扩大团队规模，借此支持客户对于Isovalent Cilium Enterprise快速增长的使用需求，同时与更多生态系统合作伙伴携手，帮助他们将Isovalent接纳为Kubernetes内外安全与可观察连接的新标准。<br>
<br><strong>原文链接：<a href="https://www.prnewswire.com/news-releases/isovalent-raises-40m-series-b-as-cilium-and-ebpf-transform-cloud-native-service-connectivity-and-security-301619134.html">Isovalent Raises $40M Series B as Cilium and eBPF Transform Cloud Native Service Connectivity and Security</a></strong>
                                
                                                              
</div>
            