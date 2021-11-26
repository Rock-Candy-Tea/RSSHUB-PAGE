
---
title: '腾讯开源｜TAT Agent-助力轻松完成云服务器运维管理任务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1364'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 18:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1364'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">项目简介</h2> 
<p><span style="background-color:#ffffff; color:#333333">腾讯云自动化助手<span> </span></span><strong style="color:#333333">TAT<span> </span></strong><span style="background-color:#ffffff; color:#333333">是云服务器的原生运维部署工具，可以远程执行 Shell、PowerShell、Python 等脚本。</span><strong style="color:#333333">TAT Agent<span> </span></strong><span style="background-color:#ffffff; color:#333333">是 TAT 产品的客户端程序，其运行于云服务器 CVM、轻量应用服务器 Lighthouse、黑石物理服务器2.0 CPM 内部，负责完成命令执行动作、并上报结果给服务端。</span></p> 
<h2>适用场景</h2> 
<p><span style="background-color:#ffffff; color:#333333">通过自动化助手，无需登录服务器，也无需打开入站端口、SSH，便可以直接管理实例，批量、周期性执行 Shell 等命令。轻松完成运行自动化运维脚本、轮询进程、安装或卸载软件、更新应用以及安装补丁等常见管理任务。</span></p> 
<h2>技术亮点</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>TAT Agent 作为 TAT 产品的关键角色，具备以下技术亮点：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>1）在设计之初调研分析了业界趋势，采用 Rust 开发，拥有良好的内存安全性、可靠性；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>2）基于云上资源信息完成全自动鉴权，不需要客户端显式提供密钥、密码等权证信息，有良好的便捷性及安全性；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>3）命令下发链路 https 加密，命令密文传输、不可篡改。</span></p> 
<h2>项目案例</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>服务腾讯云众多内部客户：容器、云防火墙、日志 CLS、大数据等多个内部团队和项目；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>服务腾讯云公有云客户：TAT 在云服务器 CVM 控制台（含黑石物理服务器2.0 CPM）、轻量应用服务器 Lighthouse 控制台均已上线 ，腾讯云客户可直接在云主机页面找到命令下发入口，进行远程命令的执行、查询。</span></p> 
<h2>项目地址</h2> 
<ul> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px;"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Ftat" target="_blank"><span>https://cloud.tencent.com/product/tat</span></a></li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px;"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftat-agent" target="_blank"><span>https://github.com/Tencent/tat-agent</span></a></li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            