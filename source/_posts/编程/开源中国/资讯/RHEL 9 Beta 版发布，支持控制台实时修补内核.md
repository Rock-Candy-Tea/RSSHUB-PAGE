
---
title: 'RHEL 9 Beta 版发布，支持控制台实时修补内核'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4986'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4986'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Red Hat Enterprise Linux (RHEL) 9 Beta 现已推出，提供了一些新功能和改进，包括从网络控制台应用内核实时补丁。RHEL 9 Beta 基于上游内核版本 5.14，并提供 RHEL 下次重大更新的预览，此版本可用于以下硬件架构：</p> 
<ul> 
 <li>Intel/AMD64 (x86_64)</li> 
 <li>ARM 64-bit (aarch64)</li> 
 <li>IBM Power LE (ppc64le)</li> 
 <li>IBM Z (s390x)</li> 
</ul> 
<p style="margin-left:0px"><strong>RHEL 9 Beta 版本内容如下：</strong></p> 
<h3 style="margin-left:0px">简化自动化和管理 </h3> 
<ul> 
 <li><strong>增强的 Web 控制台性能指标：</strong>访问附加信息，能够更好地识别性能瓶颈的潜在原因。还简化了将这些数据导出到 Grafana 等分析和报告工具的过程。</li> 
 <li><strong>通过 Web 控制台实时修补内核：</strong> 现在可以利用 Web 控制台的强大功能和易用性来应用实时内核更新。</li> 
 <li><strong>简化的镜像构建：</strong> RHEL 9 Beta 中有一些镜像构建器的改进，包括通过单个节点构建 RHEL 8 和 RHEL 9 镜像的能力，更好地支持自定义文件系统（非 LVM 挂载点）和裸机金属部署。 </li> 
</ul> 
<h3 style="margin-left:0px">增强安全性和合规性</h3> 
<ul> 
 <li><strong>通过 Web 控制台进行智能卡身份验证：</strong>用户可以使用智能卡身份验证通过 RHEL Web 控制台（sudo、SSH 等）访问远程主机。</li> 
 <li><strong>额外的安全配置文件：</strong>帮助用户符合 PCI-DSS、HIPAA 等标准。结合 Red Hat Insights 和 Red Hat Satellite 等情报收集和补救服务，现在可以使用强大的工具来快速大规模解决合规性问题。</li> 
 <li><strong>详细的 SSSD 日志记录：</strong>SSSD 是内置的企业单点登录框架，现在添加了更多事件的详细信息，例如完成任务的时间、错误、身份验证流程等，新的搜索功能让开发者能够分析性能和配置问题。</li> 
 <li><strong>集成 OpenSSL 3：</strong>将最新的安全标准应用于新的 OpenSSL 3 加密框架。内置 RHEL 实用程序已重新编译，以利用 OpenSSL 3 提供用于加密和保护数据的新安全密码。</li> 
 <li><strong>完整性测量架构(IMA) 数字哈希和签名：</strong>现在可以动态验证操作系统的完整性，以检测跨基础架构的恶意修改。</li> 
 <li><strong>默认情况下禁用 SSH root 密码登录：</strong>RHEL 9 不允许用户使用密码以“root”身份登录，以防止通过密码获取访问权限的暴力攻击。</li> 
</ul> 
<p>RHEL 9 Beta 还附带 GCC 11 和最新版本的 LLVM、Rust 和 Go 编译器，此外，Python 3.9 将成为 RHEL 9 生命周期的默认版本。值得一提的是，RHEL 9 是红帽从 CentOS Stream 开发构建的。</p> 
<p>更多版本更新内容请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redhat.com%2Fen%2Fblog%2Fwhats-new-rhel-90-beta" target="_blank">点此查看</a>。</p>
                                        </div>
                                      
</div>
            