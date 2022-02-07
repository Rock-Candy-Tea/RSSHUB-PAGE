
---
title: '龙蜥 LoongArch GA 版正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6feb40beb29c51ede6cb938c761ee1d898d.png'
author: 开源中国
comments: false
date: Sun, 06 Feb 2022 07:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6feb40beb29c51ede6cb938c761ee1d898d.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-6feb40beb29c51ede6cb938c761ee1d898d.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#000000"><strong>简介</strong></span></h1> 
<p><span style="color:#888888">继  </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg4MTMyMTUwMQ%3D%3D%26mid%3D2247485709%26idx%3D1%26sn%3Dbd231b79cbe1c4573758598b0162839e%26chksm%3Dcf66fa7ff81173692b514cd09ce3eb27e1515fc862b6ea30bc1c9e9f6768eeb2fb79c8769dfa%26scene%3D21%23wechat_redirect" target="_blank"><span><strong><span>Anolis OS LoongArch 预览版</span></strong></span></a><span><span style="color:#888888">发布后，现迎来龙蜥 LoongArch 正式版首发，该正式版</span><span style="color:#888888">在预览版的基础上提供了 AppStream、PowerTools 等仓库。</span><span style="color:#888888">Anolis OS 8.4 LoongArch 版是龙蜥社区发起的项目，完美地支持 LoongArch 体系架构，是打造国产化生态环境中重要的一项成果。</span></span></p> 
<p><span style="color:#888888">龙芯指令系统（LoongArch®）是龙芯中科基于二十年的 CPU 研制和生态建设积累推出的新指令集，具有较好的自主性、先进性与兼容性的新平台。包括基础架构部分和向量指令、虚拟化、二进制翻译等扩展部分，近 2000 条指令。</span></p> 
<h1 style="margin-left:8px; margin-right:8px"><span style="color:#000000"><strong>发布内容</strong></span></h1> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#888888">Anolis OS 8.4 LoongArch 正式版发布产品包括</span><span style="color:#ffa900"><strong> ISO、软件仓库、虚拟机镜像、容器镜像</strong></span><span style="color:#888888">。</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#888888">ISO列表：</span></p> <p><span style="color:#888888"><em><span>https://mirrors.openanolis.cn/anolis/8.4/isos/GA/loongarch64/AnolisOS-8.4-GA-loongarch64-dvd.iso </span></em></span><span style="color:#888888"> loongarch64架构的安装 ISO 镜像</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#888888">虚拟机镜像列表：</span></p> <p style="margin-left:0; margin-right:0"><em><span style="color:#888888">https://mirrors.openanolis.cn/anolis/8.4/isos/GA/loongarch64<span style="color:#888888">/AnolisOS-8.4-GA-loongarch64.qcow2</span></span></em><span style="color:#888888"><span style="color:#888888"> loongarch64架构的虚拟机镜像</span></span></p> </li> 
 <li> <p><span style="color:#888888">容器镜像列表：<br> docker pull openanolis/anolisos:8.4-loongarch64</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#888888">软件仓库列表：<br> <em>https://mirrors.openanolis.cn/anolis/8.4/BaseOS/loongarch64/os/</em><br> <em>https://mirrors.openanolis.cn/anolis/8.4/AppStream/loongarch64/os/<br> https://mirrors.openanolis.cn/anolis/8.4/PowerTools/loongarch64/os/</em></span></p> </li> 
</ul> 
<h1 style="margin-left:8px; margin-right:8px; text-align:justify"><strong style="color:#000000">亮点</strong></h1> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>支持图形界面和多种安装场景</p> </li> 
 <li> <p>使用 <span style="color:#ffa900"><strong>docker-ce 20.10.3</strong></span> 为默认的容器管理工具</p> </li> 
 <li> <p>使用 lbrowser 浏览器和 evolution 邮件客户端，lbrowser 基于 chromium 内核开发，支持 npapi 插件功能，支持国家商用密码算法模块和国产安全协议模块，修复目前已知所有安全漏洞。</p> </li> 
 <li> <p>内核更新到 <span style="color:#ffa900"><strong>4.19.190-4</strong></span></p> </li> 
</ul> 
<h1 style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><strong style="color:#000000">硬件支撑</strong></h1> 
<table align="center" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#333333; display:table; font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"><strong><span style="color:#888888">CPU</span></strong></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"><strong><span style="color:#888888">内存</span></strong></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"><strong><span style="color:#888888">硬盘</span></strong></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle"> <pre style="margin-left:0; margin-right:0"><span style="color:#888888">3a5000
3b5000
3c5000</span></pre> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle"> <pre style="margin-left:0; margin-right:0"><span style="color:#888888">4GB以上</span></pre> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle"> <pre style="margin-left:0; margin-right:0"><span style="color:#888888">120GB以上</span></pre> </td> 
  </tr> 
 </tbody> 
</table> 
<h1 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><strong style="color:#000000">已知问题</strong></h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#333333; display:table; font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">问题单</span></p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">问题描述</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">67</span></p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">kdump</span> <span style="color:#888888">没有服务文件</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">84</span></p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">内核没有 softlockup_panic、hardlockup_panic 等配置项</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">284</span></p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">rust 无法编译</span></p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">305</span></p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"><span style="color:#888888">内核没有提供 abi 包</span></p> </td> 
  </tr> 
 </tbody> 
</table> 
<h1><strong style="color:#000000">镜像地址</strong></h1> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span style="color:#000000">主机镜像：</span></strong></p> 
<p><em><span style="color:#888888">https://mirrors.openanolis.cn/anolis/8.4/isos/GA/loongarch64/</span></em></p> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span style="color:#000000">容器镜像：</span></strong></p> 
<p><code><span><span style="color:#0e9ce5">docker</span> pull openanolis/anolisos:<span style="color:#0e9ce5">8</span>.<span style="color:#0e9ce5">4</span>-loongarch64</span></code></p> 
<ul style="list-style-type:none; margin-left:0; margin-right:0"> 
 <li style="list-style-type:none; text-align:right"> </li> 
</ul> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span style="color:#000000">配置 EPEL 仓库：</span></strong></p> 
<pre><code>cat > /etc/yum.repos.d/epel.repo << EOF
[epel]
name=epel
baseurl=http://pkg.loongnix.cn/loongnix-server/8.3/epel/loongarch64/release/Everything/
gpgcheck=0
EOF</code></pre> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span style="color:#000000">配置容器仓库：</span></strong></p> 
<p><span style="color:#888888">执行以下命令编辑 /etc/docker/daemon.json，增加 insecure-registries 的配置，重新加载并重启 docker 使配置生效。</span>​​​​​​​</p> 
<pre><code>mkdir -p /etc/docker/
tee /etc/docker/daemon.json <<-‘EOF’
&#123;
“insecure-registries”:[“harbor.loongnix.cn”]
&#125;
EOF
sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl restart docker</code></pre> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#888888">使用以下帐号进行登陆：</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#888888">用户名：loongsoncloud</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#888888">密码：loongson@SYS3</span>​​​​​​​</p> 
<pre><code>docker login harbor.loongnix.cn</code></pre> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#888888">拉取镜像：</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span><span style="color:#0e9ce5">docker</span> pull harbor.loongnix.cn/mirrorloongsoncontainers/alpine:v3.<span style="color:#0e9ce5">11</span>.<span style="color:#0e9ce5">11</span></span></code></pre> 
<h1 style="margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#000000"><strong>附录</strong></span></h1> 
<p><span style="color:#888888">Anolis OS 8 comes with no guarantees or warranties of any sorts, either written or implied. The individual packages in the distribution come with their own licences.  </span></p> 
<h1 style="margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#000000"><strong>致谢</strong></span></h1> 
<p><span style="color:#888888">衷心感谢参与和协助龙蜥社区（<span style="color:#888888">OpenAnolis</span>）的所有成员，尤其是产品发布小组。</span></p> 
<p><span style="color:#888888">特别感谢来自 LoongArch SIG 组的成员（https://openanolis.cn/sig/LoongArch）</span></p> 
<p><span style="color:#888888">龙芯中科、统信软件、中科方德、万里红、红旗软件、阿里云</span></p> 
<p><span style="color:#888888">是你们的辛勤付出，以及对开源的热爱才保障版本顺利发布，也为龙蜥操作系统(Anolis OS) 8 更好地发展提供无限空间！</span></p> 
<h1 style="margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#000000"><strong>反馈</strong></span></h1> 
<p><span style="color:#888888">Bug跟踪：https://bugzilla.openanolis.cn/</span></p> 
<p><span style="color:#888888">邮件列表：loongarch@lists.openanolis.cn</span></p>
                                        </div>
                                      
</div>
            