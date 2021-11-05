
---
title: 'Pigsty v1.2 发布，使用 PG 14 作为默认数据库版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-083815824d78ae12d293b0b80955e55569c.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 07:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-083815824d78ae12d293b0b80955e55569c.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Pigsty 1.2 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fc5TUYl_hBIqxopAppaU72g" target="_blank">发布</a>。该版本包含两个重磅更新，第一是使用 PostgreSQL14 作为默认的数据库版本；第二是将监控系统与管控部署系统解耦，可用于独立监控各种现存数据库实例。</span></p> 
<p><img height="395" src="https://oscimg.oschina.net/oscnet/up-083815824d78ae12d293b0b80955e55569c.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="color:#000000">Pigsty 项目作者<span style="background-color:#ffffff">冯若航</span>表示，PostgreSQL 14 是上个月发布的新版本，在各个方面，特别是在可观测性上有了显著改进。在前两个版本中，PG 14 作为一套备选配置模板供极客用户尝鲜使用。<span style="background-color:#ffffff">在多个组织的生产环境中进行了部署与充分测试打磨后，</span>v1.2 版本中 <strong>PG 14 已经成为了 Pigsty 的默认数据库版本</strong>。同时，适配 PG14 的时序数据扩展：TimescaleDB 2.5，与地理空间扩展 PostGIS 3.1 也已经默认安装启用，配合分布式数据库插件 Citus10 ，真正让 Pigsty 成为<strong>开箱即用的（“时空超融合”）开源PostgreSQL数据库发行版</strong>。（此处借鉴了 MatrixDB 的 Slogan）</span></p> 
<p><img height="281" src="https://oscimg.oschina.net/oscnet/up-1bb30de7be4492c4fa1976e557764c17414.png" width="500" referrerpolicy="no-referrer"></p> 
<p><em>“<span style="color:#000000"><span style="background-color:#ffffff">三者相互兼容，可组合使用，Pigsty 算是真正实现了我先前</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODAyNTM5Ng%3D%3D%26mid%3D2247483706%26idx%3D1%26sn%3Db842684b41ac6dde8310448ae0a81a76%26chksm%3Dfe4b34e1c93cbdf7dcfcdae5f3ddc38bc422989421266dcda957fa2b596e361815624c92b3ec%26scene%3D21%23wechat_redirect" target="_blank">对 PG 的设想</a>”</em></p> 
<p><span style="color:#000000">第二个值得一提的新特性是<strong>监控部署模式</strong>。“在此之前，Pigsty 作为一个发行版，监控系统与部署方案是浑然一体的。但是，很多用户反馈说，他们希望只使用 Pigsty 的监控系统部分，毕竟这个世界上已经跑着很多很多的 PG 实例了。如果能用 Pigsty 监控系统监控已有的数据库实例，云数据库，以及其他 RDS 发行版，衍生产品与各类发行版，那该多好啊？”</span></p> 
<p><img height="446" src="https://oscimg.oschina.net/oscnet/up-46fd5221cd629e4a35ed183ff369dbbb92c.png" width="500" referrerpolicy="no-referrer"></p> 
<p><em><span style="color:#000000"><span style="background-color:#ffffff">最小部署模式在本地不同端口启动 </span><span style="background-color:#ffffff"><code>pg_exporter</code></span><span style="background-color:#ffffff"> 以监控外部 PG 实例</span></span></em></p> 
<p><span style="background-color:#ffffff; color:#333333">此外，Pigsty v1.2 还提供了三种可选的监控部署模式：完整部署，精简部署，最小部署。其中新增的最小部署模式，不再需要远程机器的登陆与管理权限，只要你有一个连接串可以只读访问远程数据库，即可将其纳入监控管理。所有监控功能浓缩在一台机器上，管理简单方便。尽管只有 PG 本身的指标，但 Pigsty 监控系统的大部分功能仍然可以正常工作。（经过测试，Pigsty 也可以直接用来监控 MatrixDB、GreenPlum，因此监控其他 PG 衍生/兼容的数据库产品与发行版也不在话下。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="725" src="https://oscimg.oschina.net/oscnet/up-500fadb9aae2c38c106b65491bb2b770c6e.jpg" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><em><span style="background-color:#ffffff">尽管只有 PG 本身的指标，但大部分监控图标仍可以正常工作。</span></em></span></p> 
<p><span style="color:#333333">v1.2 还包含了一些有趣的更新与改进：</span></p> 
<ul> 
 <li><span style="color:#333333"><strong><span>配置模板被进一步精简</span></strong></span><span style="color:#333333">。现在只有两种模板：生产环境（默认） or 沙箱环境。</span></li> 
 <li><span style="color:#333333">规格参数模板进一步丰富。在原来的 tiny （1C1G）模版与 oltp|olap|crit （64C 400G）中间，提供了一系列平滑过度的规格：mini（2C4G），small（4C8G），medium（8C16G），large（16C32G）等。在配置（</span><span style="color:#333333"><code>configure</code></span><span style="color:#333333">）过程中，安装向导会自动根据你机器的规格选择对应的，更为精细平滑的参数模板，进一步优化用户体验。</span></li> 
</ul> 
<p><img height="399" src="https://oscimg.oschina.net/oscnet/up-46f3ea1216ef8d25d48723991185f2f63fd.png" width="500" referrerpolicy="no-referrer"> </p> 
<p style="margin-left:0; margin-right:0"><em><span>Pigsty 始终保留着 </span><span><code>./configure && make install</code></span><span> 一行命令完成安装的传统</span></em></p> 
<p style="margin-left:0; margin-right:0"><span>同时，新添加的<code>pgsql-migration</code></span><span>将自动生成数据库迁移所需的命令、脚本与手册，使基于逻辑复制的在线不停机数据库迁移变得简单无比（已经用这个东西在生产环境迁移了几十套数据库了）。</span><span><code>pgsql-audit</code></span><span> 剧本则根据审计需求，生成对应数据库实例的审计报告。公告指出，更多的实用功能将在后续版本中添加。</span></p> 
<p style="margin-left:0; margin-right:0"><img height="298" src="https://oscimg.oschina.net/oscnet/up-c3e2dc4ba78e1d0243205530817efba24fc.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><em>APPLOG 应用可以画出哪些应用访问了哪些权限，<span style="background-color:#ffffff">（参考阅读：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU5ODAyNTM5Ng%3D%3D%26mid%3D2247484750%26idx%3D1%26sn%3Db2db051aa7b379f161ba461f56dbdbbc%26chksm%3Dfe4b3095c93cb983d3f496420fc8e291fd86400cb946e1e112f1a495b427c01930b2d072393d%26scene%3D21%23wechat_redirect" target="_blank">微信读相册那些事</a><span style="background-color:#ffffff">），演示：http://demo.pigsty.cc/d/applog-app</span></em></p> 
<p style="margin-left:0; margin-right:0"><span>在应用方面，v1.2 提供了两个新的简单 Pigsty App：用于可视化Apple iOS15新隐私日志的 <code>applog</code></span><span> 应用，以及查询中国各大公司工作休息时间的 <code>worktime</code> 应用；均可一键安装，开箱即用。</span><span style="color:#000000"><span style="background-color:#ffffff">冯若航</span></span><span>称，这两个应用功能简单但实用，更重要的是开发只用了一个小时不到。Pigsty 在产出具有基本功能的应用原型时，确实是一个非常趁手的工具。</span></p> 
<p style="margin-left:0; margin-right:0"><img height="296" src="https://oscimg.oschina.net/oscnet/up-b7f05a76f1430df6e22d027f7688acf4ebb.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><em>“<span style="color:#000000"><span style="background-color:#ffffff">Working Time 是一个有趣的项目，可以查询各大公司工作休息情况。我用这个项目的公开数据做了个查询界面：http://demo.pigsty.cc/d/worktime-query</span></span>”</em></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#333333">公告指出，按照开发规划，PG14 才是 Pigsty v1.0 正式发布的契机，差不多也正好是项目开源一周年。但因为一些原因，Pigsty 提前发布了基于 PG13 的 v1.0 可用版本。“错过了这个里程碑，甚是可惜。所以而目前这个版本（v1.2），算是我心目中的一个理想版本了。”</span></p> 
<h4><strong><span>后续计划</span></strong></h4> 
<p><span style="color:#000000"><span style="background-color:#ffffff">冯若航指出，尽管</span></span><span>关于数据库部署他有很多想法，但大的原则还是部署好的东西，能不折腾就不折腾。v1.2 已经部署了几套生产环境，不出意外的话，部署与管控将维持现状到下一个大版本 PG15。</span></p> 
<p><span>新的功能将尽可能关注管理节点本身，例如新的监控指标与监控面板，新的场景与应用。</span>目前计划或进行中的几个事项包括：</p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">PGSQL  v8，提供更加层次分明的监控面板组织，面向不同用户群体提供不同的主题视图。</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="283" src="https://oscimg.oschina.net/oscnet/up-6b4996c4588698bf1a599e4cff46cd2cae9.jpg" width="500" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">PGCAT v2，提供更为丰富的系统目录导航浏览，Yet another PgAdmin</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="550" src="https://oscimg.oschina.net/oscnet/up-e02f28df52323ec703c2b5b1828925e5647.jpg" width="500" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">REDIS v1beta，Redis 经常会与 PG 搭配使用，后续版本会将 Redis 部署与监控整合为一个完整的解决方案。</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="344" src="https://oscimg.oschina.net/oscnet/up-2558087d49afe0ff560d46d438491e724c0.jpg" width="500" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li><span>基于 timescaledb 重构 ISD 气象历史数据查询应用，这是一个严肃的实用应用，有着真实的应用场景。天气数据是很典型的时序数据，非常适合演示timescaledb的能力。</span></li> 
 <li><span>基于 PostGIS 开发一个行政区划地理编码与逆编码的应用，并将之前开发的旅行照片打卡地图移植到 Pigsty 中。这是非常典型的地理空间应用，很适合演示 Pigsty 地理空间处理分析可视化的能力。</span></li> 
</ul> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fc5TUYl_hBIqxopAppaU72g" target="_blank">查看发布公告</a>。 </p>
                                        </div>
                                      
</div>
            