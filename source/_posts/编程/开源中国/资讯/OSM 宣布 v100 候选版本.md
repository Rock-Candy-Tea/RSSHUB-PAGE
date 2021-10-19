
---
title: 'OSM 宣布 v1.0.0 候选版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1019/163440_zezU_4937141.png'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 08:37:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1019/163440_zezU_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000"><img alt height="205" src="https://static.oschina.net/uploads/space/2021/1019/163440_zezU_4937141.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">今天，我们很兴奋地宣布开放服务网格（Open Service Mesh，OSM）v1.0 的<strong style="color:#0080ff">第一个候选版本</strong>[1]。自从 OSM 项目最初开放源代码以来，这是令人兴奋的一年。OSM 是一个云原生服务网格，允许你在动态微服务环境中统一管理、保护和观察应用程序流量。它现在运行在 Kubernetes 上，我们计划很快也在多集群和混合环境中支持 OSM。随着 1.0 版本在未来几周的发布，我们将提供一组稳定的、健壮的服务网格特性。你可以使用 OSM：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p><span style="color:#000000">利用自动服务实现业务流量加密（mTLS）。</span></p> </li> 
 <li> <p><span style="color:#000000">针对 HTTP、TCP 和 gRPC 流量，加强在网格内通信的应用程序之间的访问控制。</span></p> </li> 
 <li> <p><span style="color:#000000">金丝雀（灰度）和蓝/绿风格的部署。</span></p> </li> 
 <li> <p><span style="color:#000000">通过 OSM 收集和暴露的流量指标，了解应用程序流量的行为方式。</span></p> </li> 
 <li> <p><span style="color:#000000">为入口和出口流量定义细粒度的流量控制。</span></p> </li> 
 <li> <p><span style="color:#000000">和更多的</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">查看我们最新更新的<strong style="color:#0080ff">文档网站</strong>[2]，了解更多关于特性、演示和架构的信息。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">在过去的一年里，我们也花了很多时间在云原生生态系统中集成和贡献项目，我们希望在这些项目中确保互操作性。Kubernetes 的高性能入口控制器<strong style="color:#0080ff">Contour</strong>[3]就是这样一个项目。你可以了解如何利用<strong style="color:#0080ff">Contour 进入 OSM</strong>[4]。你也可以<strong style="color:#0080ff">集成 OSM 与 Flagger</strong>[5]解锁渐进交付功能，并使用 OPA Envoy 插件<strong style="color:#0080ff">集成 Open Policy Agent 与 OSM</strong>[6]。我们还继续学习和回馈<strong style="color:#0080ff">Service Mesh Interface（SMI）项目</strong>[7]，并欢迎 SMI 社区中更多的实现和与生态系统工具的集成。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">感谢所有帮助 OSM 达到这一激动人心的里程碑，给予反馈和鼓励，并为这个项目做出贡献的人。我们对 OSM 的下一个篇章感到非常兴奋。我们希望从生产体验中学习和改进，添加更多令人兴奋的特性，并改善用户体验和可调试性。我们随时欢迎你的反馈和贡献，你可以参加 2021 年 10 月 26 日的<strong style="color:#0080ff">CNCF 网络研讨会</strong>[8]。你可以通过 Open Service Mesh<strong style="color:#0080ff">邮件列表</strong>[9]、<strong style="color:#0080ff">slack</strong>[10]或参加会议参与<strong style="color:#0080ff">OSM 社区</strong>[11]。</span></p> 
<h3 style="margin-left:0; margin-right:0"><span style="color:#000000">参考资料</span></h3> 
<p><span style="color:#000000">[1] 第一个候选版本: <em>https://github.com/openservicemesh/osm/releases/tag/v1.0.0-rc.1</em></span></p> 
<p><span style="color:#000000">[2] 文档网站: <em>https://docs.openservicemesh.io/</em></span></p> 
<p><span style="color:#000000">[3] Contour: <em>https://projectcontour.io/</em></span></p> 
<p><span style="color:#000000">[4] Contour 进入 OSM: <em>https://docs.openservicemesh.io/docs/demos/ingress_contour/</em></span></p> 
<p><span style="color:#000000">[5] 集成 OSM 与 Flagger: <em>https://docs.flagger.app/tutorials/osm-progressive-delivery</em></span></p> 
<p><span style="color:#000000">[6] 集成 Open Policy Agent 与 OSM: <em>https://docs.openservicemesh.io/docs/guides/integrations/external_auth_opa/#osm-with-opa-plugin-external-authorization-walkthrough</em></span></p> 
<p><span style="color:#000000">[7] Service Mesh Interface（SMI）项目: <em>https://smi-spec.io/</em></span></p> 
<p><span style="color:#000000">[8] CNCF 网络研讨会: <em>https://community.cncf.io/events/details/cncf-cncf-online-programs-presents-cncf-live-webinarsecuring-your-workload-communications-with-open-service-mesh/</em></span></p> 
<p><span style="color:#000000">[9] 邮件列表: <em>https://groups.google.com/g/openservicemesh</em></span></p> 
<p><span style="color:#000000">[10] slack: <em>https://cloud-native.slack.com/archives/C018794NV1C</em></span></p> 
<p><span style="color:#000000">[11] OSM 社区: <em>https://github.com/openservicemesh/osm/#community</em></span></p>
                                        </div>
                                      
</div>
            