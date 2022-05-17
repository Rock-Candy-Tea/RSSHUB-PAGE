
---
title: 'APIJSON 5.1.0 发布，腾讯面试考察•感谢两个贡献者者'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-be58dbcd2ac9cb629bf45f978e0d99a5497.png'
author: 开源中国
comments: false
date: Tue, 17 May 2022 09:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-be58dbcd2ac9cb629bf45f978e0d99a5497.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-be58dbcd2ac9cb629bf45f978e0d99a5497.png" referrerpolicy="no-referrer"></p> 
<p><strong>APIJSON 5.1.0：提升可扩展性；解决 bug；优化功能和代码；完善文档等</strong></p> 
<h2>功能</h2> 
<ul> 
 <li> <p style="color:#24292f; text-align:start">请求参数校验：REFUSE 新增支持 !key 排除禁止字段，优化 MUST 和 REFUSE 处理性能；部分常量改为可自定义静态变量；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">解决 PUT 不能完整替代 json, jsonb 字段的数组值，感谢 @weiwei162 的贡献 #387；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">解决 Oracle 分页获取时无法获取除第一页以外的数据，感谢 @SingleDogL 的贡献 #390；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">解决高并发下生成主键冲突导致新增记录失败等；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">优化 SQL 执行缓存；优化角色权限、参数校验、远程函数的初始化；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">优化登录报错和远程函数执行报错的提示；优化主键泛型；优化代码；</p> </li> 
</ul> 
<h2>文档</h2> 
<ul> 
 <li> <p style="color:#24292f; text-align:start">更新 @combine 条件组合说明为 5.0+ 的条件任意组合格式；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">更新 5.0 新增的 @having&:"...", @having:&#123;...&#125; 两种用法；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">完善 JOIN 的类型以及 join:&#123;...&#125; 这种可带 ON 及功能符的写法；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">完善 JOIN ON 的各种关联方式、支持多字段关联、支持其它条件的说明；</p> </li> 
 <li> <p style="color:#24292f; text-align:start">相关推荐新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fqietingfengsong%2Farticle%2Fdetails%2F124097229" target="_blank">apijson在同一个接口调用中 使用远程函数写入更新时间和创建时间</a>，感谢博主，点赞、收藏支持下博主吧~</p> </li> 
 <li> <p style="color:#24292f; text-align:start">生态项目新增 路由插件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAPIJSON%2Fapijson-router" target="_blank">apijson-router</a>，对外暴露类 RESTful 接口，内部转成 APIJSON 接口执行，点 Star 支持下作者吧~ <img alt src="https://oscimg.oschina.net/oscnet/up-52ca6a2f79d571f5e8409df72fa2e80624f.png" referrerpolicy="no-referrer"></p> </li> 
</ul> 
<p><strong>完整更新日志具体见</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<h1> </h1> 
<h1><strong>APIJSON 简介</strong></h1> 
<p>腾讯 APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。<br> <strong>为各种增删改查提供了完全自动化的万能 API，零代码实时满足千变万化的各种新增和变更需求。</strong><br> 能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。<br> 适合中小型前后端分离的项目，尤其是 <strong>初创项目、内部项目、低代码/零代码、小程序、BaaS、Serverless</strong> 等。</p> 
<p>通过万能的 API，前端可以定制任何数据、任何结构。<br> 大部分 HTTP 请求后端再也不用写接口了，更不用写文档了。<br> 前端再也不用和后端沟通接口或文档问题了。再也不会被文档各种错误坑了。<br> 后端再也不用为了兼容旧接口写新版接口和文档了。再也不会被前端随时随地没完没了地烦了。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7082eac80de0002f12726045e116c7f0d40.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c1a705834de1c195bc0d3801d316c3cd4c3.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4486cc0195a24ee1f5935f01ce8adc8bf07.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_associate.gif" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-07f7a7662cfe64b0c5221457013e1aaa3b7.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-391864b212bacd388d6b8acfa7a296d15af.jpg" referrerpolicy="no-referrer"></p> 
<h3><img alt src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_summary.gif" referrerpolicy="no-referrer"></h3> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li><strong>解决十大痛点</strong>(APIJSON 可大幅提振开发效率、强力杜绝联调扯皮、巧妙规避文档缺陷、非常节省流量带宽等)</li> 
 <li><strong>开发提速很大</strong>(CRUD 零代码热更新全自动，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</li> 
 <li><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</li> 
 <li><strong>社区影响力大</strong> (GitHub 1W+ Star 在 400W+ Java 项目中排名前 110，远超 FLAG, BAT 等国内外绝大部分开源项目)</li> 
 <li><strong>各项荣誉成就</strong> (腾讯内外 5 个奖项、腾讯开源前十、腾讯后端项目 Star 第一、GitHub Java 日周月榜大满贯 等)</li> 
 <li><strong>多样用户案例</strong>(腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</li> 
 <li><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</li> 
 <li><strong>周边生态丰富</strong>(Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</li> 
 <li><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</li> 
 <li><strong>功能丰富强大</strong> (增删改查、分页排序、分组聚合、各种条件、各种 JOIN、各种子查询、跨库连表 等零代码实现)</li> 
 <li><strong>使用安全简单</strong>(自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</li> 
 <li><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</li> 
 <li><strong>高质可靠代码</strong>(代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</li> 
 <li><strong>兼容各种项目</strong>(协议不限 HTTP，与其它库无冲突，对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo)</li> 
 <li><strong>工程轻量小巧</strong>(仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</li> 
 <li><strong>多年持续迭代</strong>(自 2016 年开源至今已连续维护 5 年多，累计 2600+ Commits、80+ Releases，不断更新迭代中...)</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b29f8fef54355cdd60e6844c4e58d68c32e.png" referrerpolicy="no-referrer"></p> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAPIJSON%2Fapijson-router" target="_blank">apijson-router</a> 【新】APIJSON 的路由插件，可控地对公网暴露类 RESTful 简单接口，内部转成 APIJSON 格式请求来执行。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FkvnZero%2Fhyperf-APIJSON" target="_blank">hyperf-APIJSON</a> 【新】PHP 版 APIJSON，基于 Hyperf(PHP Swoole)，支持 APIJSON 多种关联和多个功能符</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON，支持大部分 APIJSON 功能，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p><a href="https://gitee.com/tiangao/apijson-go">apijson-go</a> 【新】Go 版 APIJSON，支持 单表查询、列表筛选、关联查询、多个功能符等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> 字节跳动工程师开发的 Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持大部分 APIJSON 功能，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONBoot_Hive" target="_blank">APIJSONBoot_Hive</a> 【新】APIJSON + SpringBoot 连接 Hive, Hadoop 使用的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvcoolwind%2Fapijson-practice" target="_blank">apijson-practice</a>【新】BAT 技术专家开源的 APIJSON 参数校验注解 Library 及相关 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqiujunlin%2FAPIJSONDemo" target="_blank">APIJSONDemo</a>【新】APIJSON 接入 ClickHouse 使用 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONDemo_ClickHouse" target="_blank">APIJSONDemo_ClickHouse</a> 【新】APIJSON + SpringBoot 连接 ClickHouse 使用的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandream7%2Fapijson-db2" target="_blank">apijson-db2</a> APIJSON 接入 IBM 数据库 DB2 的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p><a href="https://gitee.com/drone/apijson-examples">apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f482266123d569305b78c7ce6362a5e78d5.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e7578a99fa987aa49b6c1a618812e1d2461.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b4ff79ca9a9c63844b09f259a91696cfacf.jpg" referrerpolicy="no-referrer"></p> 
<p><strong>腾讯 APIJSON - 零代码、全功能、强安全 ORM 库</strong></p> 
<p>后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构！</p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p> 
<p>创作不易、坚持更难，右上角点 ⭐Star 支持下吧 ^_^</p>
                                        </div>
                                      
</div>
            