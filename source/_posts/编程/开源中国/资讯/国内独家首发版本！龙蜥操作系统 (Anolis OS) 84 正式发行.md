
---
title: '国内独家首发版本！龙蜥操作系统 (Anolis OS) 8.4 正式发行'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=385'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 10:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=385'
---

<div>   
<div class="content">
                                                                    
                                                        <h1><strong>引言</strong></h1> 
<p>继<a href="https://www.oschina.net/news/141281/anolis-os-8-2-released" target="_blank">龙蜥操作系统(Anolis OS)  8.2</a>如期首发之后，龙蜥社区(OpenAnolis)在版本发布、生态完善和技术创新的路线上持续演进，终于迎来了龙蜥操作系统(Anolis OS)  8.4的发布，该版本依旧是<strong>国内仅有的首发版本</strong>！</p> 
<p>龙蜥操作系统(Anolis OS)  8.4版本依然秉承与国际主流Linux厂商发行版 100% 兼容的原则，且提供配套的迁移工具，助力用户完美平滑地迁移至龙蜥操作系统(Anolis OS)，满足CentOS停服后的各领域、各行业用户的使用习惯和需求。在硬件生态方面通过和Intel 及国内芯片厂商的合作，支持Intel、海光、兆芯、飞腾、鲲鹏等一系列芯片平台，进行软、硬一体的优化，充分发挥硬件平台的性能。</p> 
<p>在基本库、应用生态上融入了适合云场景新组件，各组件经过云计算场景超大规模部署的打磨和完善，可满足各个行业领域对于不同生产环境下不同方案的实际需求。</p> 
<h1><strong>发布内容</strong></h1> 
<p>龙蜥操作系统(Anolis OS)  8.4发布内容包括<strong>ISO、虚拟机镜像和repo源</strong>。</p> 
<h2><strong>1、ISO列表</strong></h2> 
<table> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-x86_64-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构的安装 ISO</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-aarch64-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>aarch64架构的安装 ISO</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-src-dvd.iso</p> </td> 
   <td style="vertical-align:top"> <p>source 包ISO</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p><br> ISO安装注意事项可参阅</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F%C2%A0https%3A%2F%2Fmirrors.openanolis.org%2Fanolis%2F8%2Fisos%2FGA%2FReadMe-install.txt" target="_blank">https://mirrors.openanolis.org/anolis/8/isos/GA/ReadMe-install.txt</a></p> 
<h2><strong>2、虚拟机镜像列表</strong></h2> 
<table style="width:677px"> 
 <tbody> 
  <tr> 
   <td style="vertical-align:top"> <p><strong>名称</strong></p> </td> 
   <td style="vertical-align:top"> <p><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-GA-x86_64-ANCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构虚拟机镜像搭配ANCK内核</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-GA-x86_64-RHCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>x86_64架构虚拟机镜像搭配RHCK内核[注1]</p> </td> 
  </tr> 
  <tr> 
   <td style="vertical-align:top"> <p>AnolisOS-8.4-GA-aarch64-ANCK.qcow2</p> </td> 
   <td style="vertical-align:top"> <p>aarch64架构虚拟机镜像搭配ANCK内核</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>AnolisOS-8.4-GA-aarch64-RHCK.qcow2</p> </td> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>aarch64架构虚拟机镜像搭配RHCK内核</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p>注1：RHCK内核兼容CentOS 8.4的内核，当前版本是 kernel-4.18.0-305.an8</p> 
<p>注2： 镜像缺省sudo用户anuser，对应登录密码是anolisos。</p> 
<h2><strong>3、下载列表</strong></h2> 
<ul> 
 <li> <p>社区网站</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.openanolis.cn%2Fanolis%2F8.4%2Fisos%2F" target="_blank">https://mirrors.openanolis.cn/anolis/8.4/isos/</a></p> 
<ul> 
 <li> <p>阿里云镜像</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.aliyun.com%2Fanolis%2F8.4%2F" target="_blank">https://mirrors.aliyun.com/anolis/8.4/</a></p> 
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
   <td style="vertical-align:top"> <p> </p> <p>AppStream</p> </td> 
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
  <tr> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>DDE</p> </td> 
   <td colspan="1" rowspan="1" style="vertical-align:top"> <p>DDE桌面主包以及依赖包</p> </td> 
  </tr> 
 </tbody> 
</table> 
<h1><strong>亮点</strong></h1> 
<ul> 
 <li> <p>100% 兼容<strong>国际主流 Linux</strong> 厂商发行版；</p> </li> 
 <li> <p>支持x86_64 和aarch64架构及飞腾、海光、兆芯、鲲鹏等芯片，适配 x86 及 arm64 <strong>主流服务器</strong>硬件；</p> </li> 
 <li> <p>支持 Linux Kernel <strong>4.19 LTS</strong> 版本并同步上游社区<strong>最新成果</strong>，帮助用户及时获得开源社区创新红利；</p> </li> 
 <li> <p>支持开源分布式关系数据库<strong>OceanBase</strong>；</p> </li> 
 <li> <p>支持安全容器<strong>Kata Containe</strong><strong>rs</strong>；</p> </li> 
 <li> <p> 支持开源云原生关系型数据库<strong>PolarDB for PostgreSQL</strong>；</p> </li> 
 <li> <p><strong>基础应用组件</strong>升级；</p> <p> Python 3.9/SWIG 4.0/Subversion 1.14/Redis 6/PostgreSQL 13MariaDB 10.5；</p> </li> 
 <li> <p> <strong>工具链</strong>升级；</p> <p> GCC Toolset 10/LLVM Toolset 11.0.0/Rust Toolset 1.49.0/Go Toolset 1.15.7；</p> </li> 
 <li> <p> 提供CentOS系统到Anolis OS迁移工具，帮助系统及应用的<strong>顺滑迁移</strong>；</p> </li> 
</ul> 
<p>详细发行声明，可参阅</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.openanolis.org%2Fanolis%2F8.4%2Fisos%2FReadMe.txt" target="_blank">https://mirrors.openanolis.org/anolis/8.4/isos/ReadMe.txt</a></p> 
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
<h1><strong>致谢</strong></h1> 
<p>衷心感谢参与和协助Anolis OS 8 项目的所有成员！尤其是产品发布小组（https://openanolis.cn/sig/SIG-Distro）！</p> 
<p>是你们的辛勤付出和对开源的热爱，才保障版本顺利发布，也为龙蜥操作系统(Anolis OS) 8 更好地发展提供无限空间！</p> 
<h1><strong>反馈</strong></h1> 
<p>Bug跟踪</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.openanolis.cn%2F" target="_blank">https://bugs.openanolis.cn/</a></p> 
<p>邮件列表</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flists.openanolis.cn%2F" target="_blank">http://lists.openanolis.cn/</a></p>
                                        </div>
                                      
</div>
            