
---
title: 'Red Hat Enterprise Linux 8.5 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8730'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8730'
---

<div>   
<div class="content">
                                                                                            <p>Red Hat Enterprise Linux 8.5 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redhat.com%2Fen%2Fabout%2Fpress-releases%2Fred-hat-extends-foundation-multicloud-transformation-and-hybrid-innovation-latest-version-red-hat-enterprise-linux" target="_blank">已正式发布</a>。此版本带来了许多新功能和改进，帮助简化部署、优化性能并降低环境中的风险。</p> 
<h3>RHEL 8.5 中的 Linux 容器改进</h3> 
<p>RHEL 8.5 延续了为运行 Linux 容器提供新功能和改进的传统。此版本带来的工具增加了灵活性，减少在更广泛的环境中运行 Podman 产生的不便之处。</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>容器化 Podman</span></strong> - RHEL 8 Podman 容器镜像 </span></span></span></span></span></span><span style="background-color:#ffffff; color:#151515">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcatalog.redhat.com%2Fsoftware%2Fcontainers%2Frhel8%2Fpodman%2F5dc383a0dd19c71643a22a37%3Fcontainer-tabs%3Doverview" target="_blank">rhel8/podman</a><span style="background-color:#ffffff; color:#151515">) </span><span><span><span><span><span><span style="color:#151515">现已正式发布，可帮助解锁 Podman 在云 CI/CD 系统、Windows 上的 WSL2、macOS 上的 </span></span></span></span></span></span><span style="background-color:#ffffff; color:#151515">Docker Desktop </span><span><span><span><span><span><span style="color:#151515">以及 RHEL 6、7 和 8 上的使用。开发者也</span></span></span></span></span></span><span><span><span><span><span><span style="color:#151515">可以使用 Podman 容器镜像来帮助开发和运行其他容器镜像。 </span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>默认情况下验证容器镜像签名</span>-</strong>在 RHEL 8.5 中，用户可以信任地拉取容器镜像。RHEL 8.5 提供了开箱即用的检查容器镜像签名功能，以验证它们实际上来自 Red Hat 并且未被篡改或操纵。 </span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>作为 </span></strong></span></span></span></span></span></span><strong>Rootless container </strong><span><span><span><span><span><span style="color:#151515"><strong><span>用户的原生 OverlayFS</span></strong> - RHEL 8.5 在构建和运行 </span></span></span></span></span></span>Rootless container <span><span><span><span><span><span style="color:#151515">时提供了更好的性能，并提供了对 OverlayFS 的原生支持。</span></span></span></span></span></span></p> </li> 
</ul> 
<h3>RHEL 8.5：更易于管理和部署</h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span style="color:#151515"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span>此版本继续专注于简化和改进管理和部署 RHEL 的方法。RHEL 8.5 引入了许多自动化和管理工具来自动执行手动任务、标准化大规模部署并简化其系统的日常管理。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>增强的 Web 控制台性能指标</span></strong>- 有助于识别性能问题。无论是要确定 CPU、磁盘还是网络性能问题，RHEL 8.5 Web 控制台中提供的增强指标都可以帮助解决问题。此外，还可以更轻松地将指标信息导出到 Grafana 服务器。</span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>用于硬件管理的 Ansible 模块</span></strong>- 在 RHEL 8.5 中，用户可以使用 Ansible 来管理智能平台管理接口 (IPMI) 的设置，例如系统的电源状态和设备的引导顺序。</span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>VPN 和 Postfix 的系统角色</span> </strong>- 可以使用系统角色减少设置 VPN 和 Postfix 所需的时间。</span></span></span></span></span></span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span style="color:#151515"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span>管理系统的一部分是处理安全性和策略合规性。为此，RHEL 8.5 具有许多功能，可在部署新系统或管理现有基础架构时帮助管理安全性和合规性。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3>SQL Server 功能增强</h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span style="color:#151515"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span>在 RHEL 上运行 Microsoft SQL Server 的用户将看到许多增强的功能，帮助更有效地配置、管理和操作 RHEL。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>Microsoft SQL Server 的 RHEL 系统角色</span> </strong>- 可用于 RHEL 8.5。此系统角色允许 IT 管理员和 DBA 以自动化方式更快地安装、配置和调整 SQL Server。  </span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span style="color:#151515"><strong><span>用于 Red Hat Insights 的 SQL Server 评估 API</span> </strong>- 通过提供来自 Microsoft 的 SQL Server 评估 API 的信息，帮助为系统和数据库管理员提供最佳用户体验。它有助于提供来自 Microsoft 的最佳实践来评估 SQL Server 的配置，并为用户提供针对通过 API 发现的问题进行修复的功能。</span></span></span></span></span></span></p> </li> 
</ul> 
<h3>对开发者和应用程序的支持</h3> 
<p>归根结底，RHEL 用于运行用户的应用程序和基础架构。作为构建和运行下一代应用程序的坚实基础，RHEL 8.5 支持 OpenJDK 17 和 .NET 6。</p> 
<p>详情查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redhat.com%2Fen%2Fblog%2Fwhats-new-rhel-85" target="_blank"> what's new </a>页面和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faccess.redhat.com%2Fdocumentation%2Fen-us%2Fred_hat_enterprise_linux%2F8%2Fhtml%2F8.5_release_notes%2Findex" target="_blank"> release note</a>。</p>
                                        </div>
                                      
</div>
            