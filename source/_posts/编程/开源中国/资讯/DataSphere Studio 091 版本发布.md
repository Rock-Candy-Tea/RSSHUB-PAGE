
---
title: 'DataSphere Studio 0.9.1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2530'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 03:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2530'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="color:#404040">DataSphere Studio 0.9.1 </span><span style="color:#404040">是在微众银行的倾力帮助下，由 天翼云 大数据团队 主导完成的一个重要版本。</span></p> 
<p style="text-align:left"><span style="color:#404040">这是基于 DSS 0.9.0 的下一个发行版本。该版本旨在通过新增“新用户初始化”特性，为社区用户降低运维DSS、Linkis和Schedulis等WeDataSphere组件的运维成本，让DSS在新增新登录用户时，可以使用“新用户初始化”功能自动完成新用户的所有环境初始化操作。</span></p> 
<p style="text-align:left"><span style="color:#404040">DataSphere Studio</span><span style="color:#404040">（简称DSS）是什么？DSS是微众银行自研的一站式数据应用开发管理门户，在统一的UI下，以工作流式的图形化拖拽开发体验，将满足从数据交换、脱敏清洗、分析挖掘、质量检测、可视化展现、定时调度到数据输出应用和流式工作流开发管理等，数据应用开发全流程场景需求。</span></p> 
<p style="text-align:left"><span style="color:#404040">本次版本包含了7个改进和增强，具体如下：</span></p> 
<p style="text-align:left"><strong>特性增强</strong></p> 
<ul> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F274" target="_blank">DataSphereStudio-274</a><span style="color:#404040">] </span><span style="color:#404040">新增新用户初始化特性。不同的环境，支持配置化创建新用户所需的所有环境信息，目前包括：LDAP、管理节点账号、HDFS和Linux目录、调度账号、hive库、keytab等，且预留了相关接口，允许用户自己新增实现，或者修改脚本适配自己的环境。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F288" target="_blank">DataSphereStudio-288</a><span style="color:#404040">] </span><span style="color:#404040">新增在主控机上创建用户特性。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F289" target="_blank">DataSphereStudio-289</a><span style="color:#404040">] </span><span style="color:#404040">支持给新用户创建工作空间（支持Linux和HDFS）。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F290" target="_blank">DataSphereStudio-290</a><span style="color:#404040">] </span><span style="color:#404040">支持在Schedulis的配置中添加用户，并立刻重载。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F291" target="_blank">DataSphereStudio-291</a><span style="color:#404040">] </span><span style="color:#404040">支持给新用户初始化HIVE所需环境信息。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F292" target="_blank">DataSphereStudio-292</a><span style="color:#404040">] </span><span style="color:#404040">支持为新用户在Kerberos集群创建和分发keytab文件。</span></li> 
 <li style="text-align:left"><span style="color:#404040">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FDataSphereStudio%2Fissues%2F293" target="_blank">DataSphereStudio-293</a><span style="color:#404040">] </span><span style="color:#404040">支持给基于LDAP体系新增用户。</span></li> 
</ul> 
<h2><strong>新贡献者</strong></h2> 
<p><span style="color:#404040">DSS 0.9.1 </span><span style="color:#404040">的发布，离不开WeDataSphere社区的贡献者，他们无私地贡献自己的代码，积极地与社区伙伴进行技术交流，有了他们的助力，DSS 0.9.1 才能顺利地发布，在此感谢各位社区的贡献者! 排名不分先后:</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdet101" target="_blank">luxl</a><span style="color:#404040">： 本次版本的社区主导者。基础代码和工作空间模块，调度授权，以及创建账号部分前端开发。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHanTang1" target="_blank">HanTang</a><span style="color:#404040">： LDAP模块和hadoop主节点账号创建功能。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frootljw" target="_blank">lvjw</a><span style="color:#404040">： 贡献文档。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschumiyi" target="_blank">schumiyi</a><span style="color:#404040">： 修复初始化安装后进入应用提示未开源的问题。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftomshy1" target="_blank">tomshy1</a><span style="color:#404040">： 创建账号前端开发。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJsonLiuUp" target="_blank">JsonLiuUp</a><span style="color:#404040">： keytab创建和分发，hive库开通和授权。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fldtong" target="_blank">ldtong</a><span style="color:#404040">： 调度授权。</span></p> 
<h2><strong>升级指南</strong></h2> 
<p style="text-align:justify">本次版本涉及对一部分JAR包进行了调整，如果您已经在生产环境使用了DSS，并且不想重新安装DSS的话，只需要对其中的几个Jar进行简单替换即可，具体请参考：<strong><u><span style="color:blue">DSS 0.9.1</span><span style="color:blue">升级指南</span></u><span style="color:blue">。</span></strong></p> 
<p style="text-align:justify">请注意：本次版本提供了新用户初始化的大特性，为了使您能正常使用该特性，请在安装和升级前，先阅读 <strong><u><span style="color:blue">DSS0.9.1</span><span style="color:blue">新用户初始化使用文档</span></u><span style="color:blue">。</span></strong></p> 
<h2><strong>展望未来</strong></h2> 
<p style="text-align:justify">未来，微众银行WeDataSphere大数据团队将继续携手中国电信天翼云大数据团队，打造全面连通融合的金融级大数据平台，深耕金融级生产环境和场景的自研打磨完善，为社区用户提供更加完善自洽的大数据解决方案，赋能广大社区用户和企业服务生产及业务支持，共同推动DataSphere Studio生态圈的成长。</p>
                                        </div>
                                      
</div>
            