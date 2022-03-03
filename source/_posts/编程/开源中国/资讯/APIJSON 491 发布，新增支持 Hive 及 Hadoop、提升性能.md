
---
title: 'APIJSON 4.9.1 发布，新增支持 Hive 及 Hadoop、提升性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8de2bdb5c8c03164dfd11ce35da8bd02591.png'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 09:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8de2bdb5c8c03164dfd11ce35da8bd02591.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="840" src="https://oscimg.oschina.net/oscnet/up-8de2bdb5c8c03164dfd11ce35da8bd02591.png" width="2086" referrerpolicy="no-referrer"></p> 
<h2><strong>APIJSON 4.9.1 更新内容</strong></h2> 
<div> 
 <p style="color:#24292f">新增支持 Hive 及 Hadoop，感谢 @chenyanlann 的贡献 #353 #356 以及生态项目 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONBoot_Hive" target="_blank">APIJSONBoot_Hive</a>，大家可以点 Star 支持下~<br> 调试时间字段新增 parse 和 sql 两个时长，例如 "time:start|duration|end|parse|sql": "1641751048573|145|1641751048718|50|95"；</p> 
 <p style="color:#24292f">提升 JOIN 结果集解析性能，减少 ArrayList 反复扩容的性能开销；</p> 
 <p style="color:#24292f">新增登记 腾讯音乐、传音、社宝科技、华能贵诚信托、投投科技、圆通、乐拼科技 等公司名及链接。</p> 
</div> 
<div> 
 <p style="color:#24292f"><strong>完整更新日志具体见</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
</div> 
<h1><strong>APIJSON 简介</strong></h1> 
<p style="color:#24292e">APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。<br> <strong>为各种增删改查提供了完全自动化的万能 API，零代码实时满足千变万化的各种新增和变更需求。</strong><br> 能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。<br> 适合中小型前后端分离的项目，尤其是 <strong>初创项目、内部项目、低代码/零代码、小程序、BaaS、Serverless</strong> 等。</p> 
<p style="color:#24292f">通过万能的 API，前端可以定制任何数据、任何结构。<br> 大部分 HTTP 请求后端再也不用写接口了，更不用写文档了。<br> 前端再也不用和后端沟通接口或文档问题了。再也不会被文档各种错误坑了。<br> 后端再也不用为了兼容旧接口写新版接口和文档了。再也不会被前端随时随地没完没了地烦了。</p> 
<p style="color:#24292f"><img height="720" src="https://oscimg.oschina.net/oscnet/up-c1a705834de1c195bc0d3801d316c3cd4c3.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f"><img height="720" src="https://oscimg.oschina.net/oscnet/up-4486cc0195a24ee1f5935f01ce8adc8bf07.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f"><img height="720" src="https://oscimg.oschina.net/oscnet/up-07f7a7662cfe64b0c5221457013e1aaa3b7.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f"><img height="720" src="https://oscimg.oschina.net/oscnet/up-391864b212bacd388d6b8acfa7a296d15af.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li><strong>解决十大痛点</strong> (APIJSON 可大幅提振开发效率、强力杜绝联调扯皮、巧妙规避文档缺陷、非常节省流量带宽等)</li> 
 <li><strong>开发提速很大</strong> (CRUD 零代码热更新全自动，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</li> 
 <li><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</li> 
 <li><strong>社区影响力大</strong> (GitHub 1W+ Star 在 400W+ Java 项目中排名前 110，远超 FLAG, BAT 等国内外绝大部分开源项目)</li> 
 <li><strong>各项荣誉成就</strong> (腾讯内外 5 个奖项、腾讯开源前十、腾讯后端项目 Star 第一、GitHub Java 日周月榜大满贯 等)</li> 
 <li><strong>多样用户案例</strong> (腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</li> 
 <li><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</li> 
 <li><strong>周边生态丰富</strong> (Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</li> 
 <li><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</li> 
 <li><strong>功能丰富强大</strong> (增删改查、分页排序、分组聚合、各种 JOIN、各种子查询、跨库连表、性能分析 等零代码实现)</li> 
 <li><strong>使用安全简单</strong> (自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</li> 
 <li><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</li> 
 <li><strong>高质可靠代码</strong> (代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</li> 
 <li><strong>兼容各种项目</strong> (协议不限 HTTP，与其它库无冲突，对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo)</li> 
 <li><strong>工程轻量小巧</strong> (仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</li> 
 <li><strong>多年持续迭代</strong> (自 2016 年开源至今已连续维护 5 年，累计 2600+ Commits、80+ Releases，不断更新迭代中...)</li> 
</ul> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FkvnZero%2Fhyperf-APIJSON" target="_blank">hyperf-APIJSON</a> 【新】<span style="background-color:#ffffff; color:#24292f">PHP 版 APIJSON，基于 Hyperf(PHP Swoole) 支持 MySQL</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON ，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fj2go%2Fapijson-go" target="_blank">apijson-go</a> 【新】Go 版 APIJSON，目前支持 单表查询、列表筛选、关联查询等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> 字节跳动工程师开发的 Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite 等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONBoot_Hive" target="_blank">APIJSONBoot_Hive</a> 【新】<span style="background-color:#ffffff">APIJSON + SpringBoot 连接 Hive, Hadoop 使用的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvcoolwind%2Fapijson-practice" target="_blank">apijson-practice</a>【新】<span style="background-color:#ffffff; color:#24292f">BAT 技术专家开源的 APIJSON 参数校验注解 Library 及相关 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqiujunlin%2FAPIJSONDemo" target="_blank">APIJSONDemo</a>【新】<span style="background-color:#ffffff; color:#24292f">APIJSON 接入 </span><span style="background-color:#ffffff">ClickHouse</span><span style="background-color:#ffffff; color:#24292f"> 使用 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONDemo_ClickHouse" target="_blank">APIJSONDemo_ClickHouse</a> 【新】<span style="background-color:#ffffff">APIJSON + SpringBoot 连接 ClickHouse 使用的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandream7%2Fapijson-db2" target="_blank">apijson-db2</a> <span style="background-color:#ffffff; color:#24292f">APIJSON 接入 IBM 数据库 DB2 的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p style="color:#24292e"><a href="https://gitee.com/drone/apijson-examples" target>apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p> </p> 
<p><img height="1436" src="https://oscimg.oschina.net/oscnet/up-f9c899549630a322c1967bcca57575175be.png" width="2558" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img height="1262" src="https://oscimg.oschina.net/oscnet/up-5f946abe9c85bfe9ae81b31e3cb3e29a088.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-b4ff79ca9a9c63844b09f259a91696cfacf.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p><strong>​腾讯 APIJSON - <span style="background-color:#ffffff; color:#24292f">零代码、热更新、全自动 ORM </span>库</strong></p> 
<p><span style="background-color:#ffffff; color:#24292f">后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构！</span></p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p> 
<p>创作不易、坚持更难，右上角点 ⭐Star<strong> </strong>支持下吧 ^_^</p> 
<p> </p>
                                        </div>
                                      
</div>
            