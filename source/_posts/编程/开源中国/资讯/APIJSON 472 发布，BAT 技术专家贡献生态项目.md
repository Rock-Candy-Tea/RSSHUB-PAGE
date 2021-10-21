
---
title: 'APIJSON 4.7.2 发布，BAT 技术专家贡献生态项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ae99251b42b7998edddb53c95f0185a6804.png'
author: 开源中国
comments: false
date: Thu, 21 Oct 2021 10:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ae99251b42b7998edddb53c95f0185a6804.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="1438" src="https://oscimg.oschina.net/oscnet/up-ae99251b42b7998edddb53c95f0185a6804.png" width="2520" referrerpolicy="no-referrer"></p> 
<p><strong>APIJSON 4.7.1-4.7.2 更新内容</strong><br> 解决 @raw 对应值包含 date_format 等特殊文本时查询报错，感谢圆通工程师反馈 bug 及贡献源码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fpull%2F278" target="_blank">#278</a><span style="background-color:#ffffff; color:#24292f"><span> </span>；</span><br> 解决远程函数拿不到有效的当前对象，导致校验参数容易放行等问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fissues%2F281" target="_blank">#281</a><span style="background-color:#ffffff; color:#24292f"><span> </span>；</span><br> 解决操作符 UNIQUE 校验不允许重复失效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fissues%2F282" target="_blank">#282</a><span style="background-color:#ffffff; color:#24292f"><span> </span>；</span><br> 优化文档，贡献者名单新增圆通工程师等 3 人，感谢贡献 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fpull%2F278" target="_blank">#278</a><span style="background-color:#ffffff; color:#24292f"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fpull%2F279" target="_blank">#279</a><span style="background-color:#ffffff; color:#24292f"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Fpull%2F280" target="_blank">#280</a><span style="background-color:#ffffff; color:#24292f"><span> </span>；</span></p> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<p>另外感谢 BAT 技术专家 为 APIJSON 贡献生态项目 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvcoolwind%2Fapijson-practice" target="_blank">apijson-practice</a>。</p> 
<h1><strong>APIJSON 简介</strong></h1> 
<p style="color:#24292e">APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。<br> <strong>为各种增删改查提供了完全自动化的万能 API，零代码实时满足千变万化的各种新增和变更需求。</strong><br> 能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。<br> 适合中小型前后端分离的项目，尤其是 <strong>初创项目、内部项目、低代码/零代码、小程序、BaaS、Serverless</strong> 等。</p> 
<p style="color:#24292f; text-align:start">通过万能的 API，前端可以定制任何数据、任何结构。<br> 大部分 HTTP 请求后端再也不用写接口了，更不用写文档了。<br> 前端再也不用和后端沟通接口或文档问题了。再也不会被文档各种错误坑了。<br> 后端再也不用为了兼容旧接口写新版接口和文档了。再也不会被前端随时随地没完没了地烦了。</p> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li><strong>解决十个痛点</strong><span> </span>(APIJSON 可帮助用户 提振开发效率、杜绝联调扯皮、规避文档缺陷、节省流量带宽 等)</li> 
 <li><strong>开发提速很大</strong><span> </span>(CRUD 零代码热更新自动化，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</li> 
 <li><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</li> 
 <li><strong>社区影响力大</strong> (GitHub 1W+ Star 在 400W+ Java 项目中排名前 130，远超 FLAG, BAT 等国内外绝大部分开源项目)</li> 
 <li><strong>各项荣誉成就</strong> (腾讯内部 3 个奖项、腾讯首个 GVP 获奖项目、腾讯后端项目 Star 第一、GitHub Java 日周月榜大满贯 等)</li> 
 <li><strong>多样用户案例</strong><span> </span>(腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</li> 
 <li><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</li> 
 <li><strong>周边生态丰富</strong><span> </span>(Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</li> 
 <li><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</li> 
 <li><strong>功能丰富强大</strong> (增删改查、分页排序、分组聚合、各种 JOIN、各种子查询、跨库跨表、性能分析 等零代码实现)</li> 
 <li><strong>使用安全简单</strong><span> </span>(自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</li> 
 <li><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</li> 
 <li><strong>高质可靠代码</strong><span> </span>(代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</li> 
 <li><strong>兼容各种项目</strong><span> </span>(协议不限 HTTP，与其它库无冲突，对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo)</li> 
 <li><strong>工程轻量小巧</strong><span> </span>(仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</li> 
 <li><strong>多年持续迭代</strong><span> </span>(自 2016 年开源至今已连续维护 5 年，累计 2500+ Commits、80+ Releases，不断更新迭代中...)</li> 
</ul> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON ，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p style="color:#24292e"><a href="https://gitee.com/tiangao/apijson-go" target>apijson-go</a> 【新】Go 版 APIJSON，目前支持 单表查询、列表筛选、关联查询等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxianglong111%2FAPIJSON-php" target="_blank">APIJSON-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqq547057827%2Fapijson-php" target="_blank">apijson-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> 字节跳动工程师开发的 Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite 等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZerounary%2FAPIJSONParser" target="_blank">APIJSONParser</a> 第三方 APIJSON 解析器，将 JSON 动态解析成 SQL</p> 
<p style="color:#24292e"><a href="https://gitee.com/own_3_0/ff-api-json" target>FfApiJson</a> <span style="background-color:#ffffff; color:#40485b">用JSON格式直接生成sql 借鉴APIJSON 支持多数据源</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvcoolwind%2Fapijson-practice" target="_blank">apijson-practice</a>【新】<span style="background-color:#ffffff; color:#24292f">BAT 技术专家开源的 APIJSON 参数校验注解 Library 及相关 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONDemo_ClickHouse" target="_blank">APIJSONDemo_ClickHouse</a> 【新】<span style="background-color:#ffffff; color:#24292e">APIJSON + SpringBoot 连接 ClickHouse 使用的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frainboy-learn%2Fapijson-learn" target="_blank">apijson-learn</a> 【新】APIJSON 学习笔记和源码解析</p> 
<p style="color:#24292e"><a href="https://gitee.com/csgitter/APIJSONBoot" target>ApiJsonBoot</a> 基于 APIJSON 的<span style="background-color:#ffffff; color:#40485b">零代码 API 生成框架</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p style="color:#24292e"><a href="https://gitee.com/drone/apijson-examples" target>apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p style="color:#24292e"><a href="https://gitee.com/zhiyuexin/ApiJsonByJFinal">ApiJsonByJFinal</a> 整合 APIJSON 和 JFinal 的 Demo</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAirforce-1%2FSpringServer1.2-APIJSON" target="_blank">SpringServer1.2-APIJSON</a> 智慧党建服务器端，提供 上传 和 下载 文件的接口</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengxianggui%2Fapijson-builder" target="_blank">apijson-builder</a> 一个方便为 APIJSON 构建 RESTful 请求的 JavaScript 库</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p><img height="1438" src="https://oscimg.oschina.net/oscnet/up-57e0517b913693348746bf9ed28eadcca06.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><strong>​APIJSON - <span style="background-color:#ffffff; color:#24292f">零代码、热更新、全自动 ORM </span>库</strong></p> 
<p><span style="background-color:#ffffff; color:#24292f">后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构！</span></p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p>
                                        </div>
                                      
</div>
            