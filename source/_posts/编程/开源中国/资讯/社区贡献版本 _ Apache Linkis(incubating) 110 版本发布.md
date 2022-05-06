
---
title: '社区贡献版本 _ Apache Linkis(incubating) 1.1.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a89c3568fec2015d1f3d6eafaafd8ca7333.png'
author: 开源中国
comments: false
date: Thu, 05 May 2022 17:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a89c3568fec2015d1f3d6eafaafd8ca7333.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-a89c3568fec2015d1f3d6eafaafd8ca7333.png" width="900" referrerpolicy="no-referrer"></p> 
<p><span style="color:#0080ff"><strong><span style="background-color:#ffffff">Linkis 1.1.0 版本简介</span></strong></span></p> 
<p><span>Apache Linkis发布了进入Apache孵化项目之后第一个大版本-1.1.0。该版本在天翼云主导和社区同学的积极代码贡献下，不仅稳定性得到极大提升，而且此版本发布了围绕统一数据源管理服务的重磅特性。对于提供统一源数据管理服务特性，从开始讨需求特性讨论，到功能详细设计，到最后的代码迭代实现，历经前后大半年时间，并且此特性已经在部分公司的生产环境得到使用和验证。</span></p> 
<p><span>本版本在Linkis 1.0.3基础上增加了数据源管理服务，支持对hive/mysql的元数据信息查询，修复了1.0.3版本的一些已知bug，增加了多个单元测试用例规范和代码。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span><span>GitHub：</span><u>https://github.com/apache/incubator-linkis</u></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><strong>版本主要添加了以下功能：</strong></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span> 提供Restful接口针对数据源进行增删查改，以及数据源的连接测试。</span></p> </li> 
 <li> <p><span> 提供Restful接口针对元数据进行数据库、表、分区、列属性查询。</span></p> </li> 
 <li> <p><span> 提供针对数据源及元数据服务管理的Java客户端。</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><strong>缩写：</strong></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>EC: Engineconn</span></p> </li> 
 <li> <p><span>ECM: EngineConnManager</span></p> </li> 
 <li> <p><span>ECP: EngineConnPlugin</span></p> </li> 
 <li> <p><span>DMS: Data Source Manager Service</span></p> </li> 
 <li> <p><span>MDS: MetaData Manager Service</span></p> </li> 
</ul> 
<p><span style="color:#0080ff"><strong><span>版本新特性</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>[DMS-Common]</span><span style="color:#333333">[Linkis-1335]</span> <span>增加新的模块 linkis-datasource-manager-common，新增数据源数据结构、异常类、工具类。</span></p> </li> 
 <li> <p><span>[MDS-Common]</span><span style="color:#333333">[Linkis-1340]</span> <span>增加新的模块 linkis-metadata-manager-common，新增元数据数据结构、异常类、工具类。</span></p> </li> 
 <li> <p><span>[MDS-Server]</span><span style="color:#333333">[Linkis-1352]</span> <span>增加新的模块linkis-datasource-manager-server，提供数据源管理服务，通过restful接口提供了数据源的增删查改、连接测试等功能。</span></p> </li> 
 <li> <p><span>[MDS-Server]</span><span style="color:#333333">[Linkis-1356]</span><span> 增加新的模块linkis-metadata-manager-server，提供元数据管理服务，通过restful接口提供了元数据的数据库、表、列查询。</span></p> </li> 
 <li> <p><span>[MDS-Services]</span><span style="color:#333333">[Linkis-1366]</span><span> 增加新的模块linkis-metadata-manager-service-es，提供针对的elasticsearch元数据查询服务。</span></p> </li> 
 <li> <p><span>[MDS-Services]</span><span style="color:#333333">[Linkis-1368]</span><span> 增加新的模块linkis-metadata-manager-service-hive，提供针对hive的元数据查询服务。</span></p> </li> 
 <li> <p><span>[MDS-Services]</span><span style="color:#333333">[Linkis-1371]</span><span> 增加新的模块linkis-metadata-manager-service-kafka，提供针对kafka的元数据查询服务。</span></p> </li> 
 <li> <p><span>[MDS-Services]</span><span style="color:#333333">[Linkis-1373]</span><span> 增加新的模块linkis-metadata-manager-service-mysql，提供针对mysql的元数据查询服务。</span></p> </li> 
 <li> <p><span>[DMS-Client&MDS-Client]</span><span style="color:#333333">[Linkis-1418]</span><span> </span><span style="color:#333333">[Linkis-1434]</span><span style="color:#333333">[Linkis-1438]</span><span style="color:#333333">[Linkis-1441]</span><span> 增加新的数据源管理Java客户端模块 linkis-datasource-client，方便通过sdk方式进行数据源管理。</span></p> </li> 
 <li> <p><span>[DMS-Web&MDS-Web]</span><span style="color:#333333">[Linkis-1456]</span><span> [Linkis-1510] 增加数据源前端管理页面，通过该页面可以对数据源进行简单的创建，测试。</span></p> </li> 
</ul> 
<p><span style="color:#0080ff"><strong><span>功能增强</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1377]</span><span> 引入Skywalking组件, 提供分布式 trace 和 troubleshooting的基础能力</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>]</span><span style="color:#333333">[Linkis-1408]</span><span> 调整引擎资源的默认的最大空闲时间为0.5h，优化多用户场景下，资源竞争等待的时长问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>]</span><span style="color:#333333">[Linkis-1535]</span><span> 设置JAVA_ENGINE_REQUEST_INSTANCE 的值为常量1</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[DB]</span><span style="color:#333333">[Linkis-1554]</span><span> 添加DataSource DDL和DML SQL</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[MDS]</span><span style="color:#333333">[Linkis-1583]</span><span> 添加功能以获取Hive 数据源中分区的属性并修复连接问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Commons-Gateway</span><span>]</span><span style="color:#333333">[Linkis-1636]</span><span>使用正则表达式匹配网关 URL，如果匹配则正常通过</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1397]</span><span> 添加maven wrapper，支持使用mvnw脚本进行编译打包</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[EC]</span><span style="color:#333333">[Linkis-1425]</span><span>将ec的日志配置文件统一为log4j2.xml</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1563]</span><span> 优化linkis-cli 客户端脚本，移除冗余的linkis-cli-start脚本文件</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1559]</span><span> 优化安装部署脚本，安装部署时，添加数据库连接测试检查;进行数据库初始化之前，打印数据库的信息，以便人员再次确认</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1559]</span><span><span> </span>添加必要的部署日志信息以及关键信息的颜色标识，如执行步骤/创建目录的日志等。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1559]</span><span> 为spark/hadoop/hive 添加基本环境检查</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1559] </span><span>将hive元数据库HIVE_META 信息配置从linkis-env.sh迁移到 db.sh</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1557] </span><span>Spring-boot/Spring-cloud版本控制使用官方依赖管理器的pom文件方式，避免引入了太多的版本配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1621]</span><span> Spring升级，Spring-boot升级至2.3.12.RELEASE，Spring-cloud升级至Hoxton.SR12</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1558]</span><span> 单元测试JUnit 4 迁移升级至 JUnit 5</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons-Eureka]</span><span style="color:#333333">[Linkis-1313] </span><span>移除不必要的第三方依赖，一定程度减小打包后的物料包大小</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons</span><span>-Gateway</span><span>]</span><span style="color:#333333">[Linkis-1660] </span><span>使用spring-boot-starter-jetty替换直接引入jetty依赖方式，避免jetty版本冲突</span></p> </li> 
</ul> 
<p><span style="color:#0080ff"><strong><span>修复功能</span></strong></span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Install-Script</span><span>]</span><span style="color:#333333">[Linkis-1390]</span><span> 修复安装部署时创建的存储Job结果集文件目录 wds.linkis.resultSet.store.path，使用过程中切换用户后存在的权限不足的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1469]</span><span> 修复sql脚本中包含 ';'字符时，无法正确切割SQL问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>-JDBC]</span><span style="color:#333333">[Linkis-1529]</span><span> 修复 JDBC 引擎认证类型参数存在的NullPointerException的异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Entrance]</span><span style="color:#333333">[Linkis-1540]</span><span> 修复 linkis-entrance 中“kill”方法参数long类型导致null值无法识别问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1600]</span><span> 修复低版本commons-compress，导致结果集下载为excel时出错</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>Client]</span><span style="color:#333333">[Linkis-1603]</span><span> 修复客户端不支持  -runtimeMap 参数问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>-JDBC]</span><span style="color:#333333">[Linkis-1610]</span><span> 修复 jdbc引擎 对于postgresql 无法支持"show databases;"语句问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[Commons]</span><span style="color:#333333">[Linkis-1618]</span><span> 修复 http response 返回结果为xml格式，而不是json格式问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>-J</span><span>BDC</span><span>]</span><span style="color:#333333">[Linkis-1646]</span><span> 修复 JDBC 引擎查询复杂类型字段时，值显示为对象地址。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>ECP</span><span>-</span><span>Python</span><span>]</span><span style="color:#333333">[Linkis-1731]</span><span> 修复python引擎的showDF函数结果集字段行反转的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[</span><span>PS-</span><span>BML]</span><span style="color:#333333">[Linkis-1556]</span><span> 修复文件下载接口可能出现的HttpMessageNotWritableException异常</span></p> </li> 
</ul> 
<p><strong><span>【详细指引<span>】</span></span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span>数据源介绍&功能使用指引:<span> </span></span><u>https://linkis.apache.org/zh-CN/docs/latest/release</u></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span>详细安装部署见指引：</span><u>https://linkis.apache.org/zh-CN/docs/latest/deployment/quick_deploy</u></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span>官方下载链接：</span><span style="color:#0080ff">https://linkis.apache.org/zh-CN/download/main</span></p> </li> 
</ul> 
<p><strong style="color:#0080ff">贡献者寄语</strong></p> 
<p style="color:#222222; margin-left:4px; margin-right:.75em; text-align:left"><span>Apache Linkis(incubating) 1.1.0的发布离不开Linkis社区的贡献者，感谢所有的社区贡献者，包括但不仅限于本次版本的贡献者：Contributors: Alexkun、CCweixiao、Celebrate-future、Davidhua1996、FireFoxAhri、WenxiangFan、Zosimer、aleneZeng、casionone、dddyszy、det101、ganlangjie、huapan123456、huiyuanjjjjuice、husofskyzy、iture123、jianwei2、legendtkl、peacewong、pjfanning、silly-carbon、xiaojie19852006、Adamyuanyuan</span></p> 
<p><img height="750" src="https://oscimg.oschina.net/oscnet/up-2545ceb72e6dd46584ebbce6839f05e5874.png" width="300" referrerpolicy="no-referrer"></p> 
<p><span style="color:#0080ff"><strong>如何参与贡献</strong></span></p> 
<p><span><span style="color:#333333">（1）新手任务：认领入门任务，详见 </span><u>https://github.com/apache/incubator-linkis/issues/1161</u><span style="color:#333333">； <span> </span></span></span></p> 
<p><span style="color:#333333">（2）作品沉淀：发布WeDataSphere开源组建相关内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。如：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDkxNzUxMg%3D%3D%26mid%3D2247488005%26idx%3D1%26sn%3Ddf78dfb77f475c2d1ef7ee69568db5c7%26chksm%3Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0080ff">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</span></a></p> 
<p><span style="color:#333333">（3）贡献代码：PR和Issue；</span></p> 
<p><span style="color:#333333">（4）答疑：热心为开发者答疑，如社区群回答开发者问题、issue答疑等；</span></p> 
<p><span style="color:#333333">（5）其他：沙箱体验、参与活动、成为社区志愿者等。</span></p>
                                        </div>
                                      
</div>
            