
---
title: 'Anolis OS 8.2 正式版发布，100% 兼容 CentOS 8'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0234e4ccdb6af82642701125de4f1aa8327.png'
author: 开源中国
comments: false
date: Thu, 13 May 2021 06:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0234e4ccdb6af82642701125de4f1aa8327.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Anolis OS 8.2 的首个正式发布版本已 GA。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0234e4ccdb6af82642701125de4f1aa8327.png" referrerpolicy="no-referrer"></p> 
<h1><strong>简介</strong></h1> 
<p>Anolis OS 8 是OpenAnolis社区发行的开源Linux发行版，与CentOS 8 100% 兼容，支持多计算架构，提供稳定、高性能、安全、可靠的操作系统。</p> 
<p>本次发布的GA版是<strong>Anolis OS 8.2 的首个正式发布版本</strong>，支持x86_64 和aarch64架构，搭载双内核RHCK（RHEL Compatible Kernel）和ANCK（OpenAnolis Cloud Kernel）。其中ANCK是由社区Cloud Kernel SIG组基于上游4.19 LTS kernel研发，提供对稳定、性能、隔离能力的增强，和<strong>飞腾、海光、兆芯、鲲鹏</strong>芯片的完善支持。</p> 
<h1><strong>发布内容</strong></h1> 
<p>Anolis OS 8 GA发布内容包括<strong>ISO、虚拟机镜像和repo源</strong>。</p> 
<h2><strong>1、ISO列表</strong></h2> 
<table style="width:677px"> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-x86_64-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构的安装 ISO</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-aarch64-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>aarch64架构的安装 ISO</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-src-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>source 包ISO</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p>ISO安装注意事项可参阅</p> 
<p> https://mirrors.openanolis.org/anolis/8/isos/GA/ReadMe-install.txt</p> 
<h2><strong>2、虚拟机镜像列表</strong></h2> 
<table> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-x86_64-ANCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构虚拟机镜像搭配ANCK内核</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-x86_64-RHCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构虚拟机镜像搭配RHCK内核[注1]</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.2-GA-aarch64-ANCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>aarch64架构虚拟机镜像搭配ANCK内核</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>AnolisOS-8.2-GA-aarch64-RHCK.qcow2</p> </td> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>aarch64架构虚拟机镜像搭配RHCK内核</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p>注1：RHCK内核兼容CentOS8.2的内核，当前版本是 kernel-4.18.0-193.el8。</p> 
<p>注2：镜像缺省sudo用户anuser，对应登录密码是anolisos。</p> 
<h2><strong>3、下载列表</strong></h2> 
<ul> 
 <li> <p>社区网站</p> </li> 
</ul> 
<p>https://mirrors.openanolis.org/anolis/8/isos/GA/ </p> 
<ul> 
 <li> <p>阿里云镜像</p> </li> 
</ul> 
<p>https://mirrors.aliyun.com/anolis/</p> 
<h2><strong>4、REPO源列表</strong></h2> 
<table> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>BaseOS</p> </td> 
   <td style="vertical-align:top"> <p>BaseOS 软件包源，该源目的是提供安装基础的所有核心包。</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AppStream</p> </td> 
   <td style="vertical-align:top"> <p>AppStream 软件包源，该源提供额外的多场景，多用途的用户态程序，数据库等。该部分引入了额外的RPM Module形态。</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>PowerTools</p> </td> 
   <td style="vertical-align:top"> <p>PowerTools 软件包源， 该源提供开发者需要的额外包。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>Plus</p> </td> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>Plus 软件包源，该源提供OpenAnolis SIG组专门研发包，如ANCK内核，Dragonwell8 JDK等。</p> </td> 
  </tr> 
 </tbody> 
</table> 
<h1><strong>亮点</strong></h1> 
<ul> 
 <li> <p>100% 兼容<strong>CentOS 8</strong>软件生态，兼容<strong>国际主流 Linux</strong> 厂商发行版；</p> </li> 
 <li> <p>支持x86_64 和aarch64架构及飞腾、海光、兆芯、鲲鹏等芯片，适配 x86 及 arm64 <strong>主流服务器</strong>硬件；</p> </li> 
 <li> <p>支持 Linux Kernel <strong>4.19 LTS</strong> 版本并同步上游社区<strong>最新成果</strong>，帮助用户及时获得开源社区创新红利；</p> </li> 
 <li> <p>支持<strong>Dragonwell云原生Java</strong>运行时；</p> </li> 
 <li> <p>提供CentOS系统到Anolis OS迁移工具，帮助系统及应用的<strong>顺滑迁移</strong>。</p> </li> 
</ul> 
<p>详细发行声明，可参阅</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.openanolis.org%2Fanolis%2F8%2Fisos%2FGA%2FReadMe.txt" target="_blank">https://mirrors.openanolis.org/anolis/8/isos/GA/ReadMe.txt  </a></p> 
<h1><strong>硬件支撑</strong></h1> 
<h2><strong>支持架构</strong></h2> 
<p>x86_64 和aarch64</p> 
<h2><strong>Cloud Kernel平台兼容性</strong></h2> 
<p>Cloud Kernel内核已验证支持的服务器如下，后续将逐步增加对其他服务器的支持，也欢迎广大合作伙伴/开发者参与贡献和验证。</p> 
<table> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>架构</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>CPU</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>飞腾</p> </td> 
   <td style="vertical-align:top"> <p>aarch64</p> </td> 
   <td style="vertical-align:top"> <p>Phytium FT-2000+/64,</p> <p>Phytium S2500/64</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>海光</p> </td> 
   <td style="vertical-align:top"> <p>x86_64</p> </td> 
   <td style="vertical-align:top"> <p>Hygon C86 7185 32-core Process</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>兆芯</p> </td> 
   <td style="vertical-align:top"> <p>x86_64</p> </td> 
   <td style="vertical-align:top"> <p>Zhaoxin KH-37800D</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>鲲鹏</p> </td> 
   <td style="vertical-align:top"> <p>aarch64</p> </td> 
   <td style="vertical-align:top"> <p>Kunpeng-920</p> </td> 
  </tr> 
 </tbody> 
</table> 
<h1><strong>附录</strong></h1> 
<p>Anolis OS 8 comes with no guarantees or warranties of any sorts,either written or implied.</p> 
<p>Individual packages in the distribution come with their own licences.</p> 
<h1><strong>反馈</strong></h1> 
<p>Bug跟踪</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.openanolis.cn%2F" target="_blank">https://bugs.openanolis.cn/</a></p> 
<p>邮件列表</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flists.openanolis.cn%2F" target="_blank">http://lists.openanolis.cn/</a></p>
                                        </div>
                                      
</div>
            