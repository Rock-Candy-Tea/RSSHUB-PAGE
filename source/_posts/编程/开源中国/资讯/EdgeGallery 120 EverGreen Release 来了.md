
---
title: 'EdgeGallery 1.2.0 EverGreen Release 来了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4e4365295ea6f3a32a29aba1b874d455533.png'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 14:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4e4365295ea6f3a32a29aba1b874d455533.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>EdgeGallery 1.2.0版本正式发布</strong></p> 
<p>2021年7月7日，经过社区开发者三个多月的共同努力，<strong>EdgeGallery社区即将正式发布第五个版本EverGreen Release</strong>。此版本是EdgeGallery的1.2.0正式版本。本次版本发布后，EdgeGallery共有29个代码仓已经发布。</p> 
<p>此次新版本功能增强分布于EdgeGallery所有功能模块中，尤其在虚机应用的集成、平台开放能力增强，以及Developer、AppStore和MECM平台体验优化上有明显提升。</p> 
<ul> 
 <li> <p><strong>新开源仓库列表</strong></p> </li> 
</ul> 
<table cellpadding="0" cellspacing="0" style="width:677px"> 
 <thead> 
  <tr> 
   <td> <p><strong>模块</strong></p> </td> 
   <td> <p><strong>类型</strong></p> </td> 
   <td> <p><strong>URL</strong></p> </td> 
   <td> <p><strong>说明</strong></p> </td> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td> <p>Installer</p> </td> 
   <td> <p>配置仓</p> </td> 
   <td> <p>https://gitee.com/edgegallery/installer</p> </td> 
   <td> <p>EdgeGallery离线包制作以及离线安装、在线安装、docker compose方式安装脚本</p> </td> 
  </tr> 
  <tr> 
   <td> <p>filesystem</p> </td> 
   <td> <p>产品仓</p> </td> 
   <td> <p>https://gitee.com/edgegallery/file-system</p> </td> 
   <td> <p>EdgeGallery平台内的应用镜像管理服务</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4e4365295ea6f3a32a29aba1b874d455533.png" referrerpolicy="no-referrer"></p> 
<p>图1  EdgeGallery v1.2.0 EverGreen版本架构图</p> 
<p><strong>dgeGallery</strong></p> 
<h1><strong>EverGreen版本</strong><strong>重要特性</strong></h1> 
<h2><strong>01 亮点功能</strong></h2> 
<p><strong>【虚机应用支持】</strong></p> 
<ul> 
 <li> <p>全流程支持虚机应用的快速集成、测试和在AppStore发布，MECM平台支持虚机应用的分发和部署</p> </li> 
 <li> <p>虚机应用集成能力增强，支持虚机规格配置、网络配置和环境变量配置等</p> </li> 
</ul> 
<p><strong>【开放能力增强】</strong></p> 
<ul> 
 <li> <p>AI软硬件能力</p> </li> 
</ul> 
<p>支撑昇腾/Atlas硬件以及开放API：支持昇腾20+开放能力，包括图像修复、目标定位、超分辨图像算法等</p> 
<p>新增AI换脸、OCR、智慧货架、姿态识别等开放API能力</p> 
<ul> 
 <li> <p>行业套件支持特定行业场景</p> </li> 
</ul> 
<p>工业现场南向设备管理通信：提供基于Fledge的工业南向设备管理方案以及部署脚本</p> 
<p>工业视觉场景：PCB质量检测，提供开放能力和PCB板质量检测样例应用</p> 
<p>泛视频领域：提供可用于视频会议、在线课堂等场景的开源样例应用</p> 
<p><strong>【功能与界面体验优化】</strong></p> 
<ul> 
 <li> <p>Developer、AppStore和MECM平台增加管理员操作界面</p> </li> 
 <li> <p>Appstore界面易用性优化，提供应用在线体验功能</p> </li> 
</ul> 
<h2><strong>02 其他新功能</strong></h2> 
<ul> 
 <li> <p>增加镜像文件管理服务，解决EdgeGallery中心节点模块间镜像文件共享问题</p> </li> 
 <li> <p>提供边缘自治管理界面和边缘节点健康检查功能</p> </li> 
 <li> <p>所有模块支持数据持久化能力</p> </li> 
</ul> 
<h2><strong>03 增强特性</strong></h2> 
<p><strong>【安全增强】</strong></p> 
<ul> 
 <li> <p>用户管理模块增加动态验证码校验功能，解决恶意注册和邮件轰炸等安全漏洞问题；</p> </li> 
 <li> <p>应用调测过程中，VNC远程登录沙箱环境设置非root用户操作，限制访问权限</p> </li> 
</ul> 
<p><strong>【按需部署】</strong></p> 
<ul> 
 <li> <p>提供基于Ansible的离线部署脚本与离线安装包，支持用户自定义按需部署</p> </li> 
 <li> <p>支持以docker-compose方式部署EdgeGallery各子模块</p> </li> 
 <li> <p>支持树莓派部署</p> </li> 
</ul> 
<p><strong>详细Release Notes链接：</strong><a href="https://gitee.com/edgegallery/docs/blob/master/Release%20Notes/EdgeGallery_RN_zh.md" target="_blank">https://gitee.com/edgegallery/docs/blob/master/Release%20Notes/EdgeGallery_RN_zh.md</a></p> 
<p><strong>V1.2.0版本下载地址：</strong></p> 
<p><a href="https://gitee.com/edgegallery/docs/blob/master/Release%20Notes/EdgeGallery_RN_zh.md" target="_blank">https://www.edgegallery.org/download/</a></p> 
<h1><strong>下一版本的展望</strong></h1> 
<p>随着最新E版本的发布，社区在开发流程、能力开放、商用可部署性等方面日趋完善。在下一个版本F Release规划中，社区计划在如下方面做进一步提升和增强：</p> 
<ol> 
 <li>提供应用多形态Workload支持（如WASM/FaaS/容器/虚机）</li> 
 <li>提供移动端边缘计算管理</li> 
 <li>提供标准化的集成工业互联网平台的Profile等</li> 
</ol> 
<p>欢迎访问https://gitee.com/edgegallery参与社区讨论与贡献，共同定义开发社区F版本功能。</p> 
<h1><strong>致谢</strong></h1> 
<p><strong>感谢社区所有贡献者在前五个版本发布中做出的贡献与支持，谢谢！</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d876df41dd46804fa8dda39338bdc53660f.png" referrerpolicy="no-referrer"></p> 
<h1><strong>关于EdgeGallery</strong></h1> 
<p>EdgeGallery是由设备厂商、运营商，垂直行业伙伴等联合发起的一个5G 边缘计算开源项目。目的是打造一个符合5G MEC“联接+计算”特点的边缘计算公共平台，以Edge Native 技术为底座，实现网络能力（尤其是5G网络）开放的标准化和MEC 应用开发、测试、迁移和运行等生命周期管理流程的通用化。</p> 
<p>EdgeGallery项目自2020年8月6日启动至今，已发布5个版本。目前社区已有8家高级会员、19家普通会员、48家组织和300+开发者。现有130多款应用在AppStore中集成，近30家合作伙伴或厂商已经部署使用。</p> 
<p><strong>项目详情请参考：</strong></p> 
<p>项目托管地址 <a href="https://gitee.com/EdgeGallery">https://gitee.com/EdgeGallery</a></p> 
<p>社区门户网站链接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.edgegallery.org" target="_blank">https://www.edgegallery.org</a></p>
                                        </div>
                                      
</div>
            