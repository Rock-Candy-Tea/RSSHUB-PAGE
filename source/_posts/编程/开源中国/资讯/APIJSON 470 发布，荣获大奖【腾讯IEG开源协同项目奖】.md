
---
title: 'APIJSON 4.7.0 发布，荣获大奖【腾讯IEG开源协同项目奖】'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6291180557291ef361561a069dd5323dc25.png'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 09:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6291180557291ef361561a069dd5323dc25.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img src="https://oscimg.oschina.net/oscnet/up-6291180557291ef361561a069dd5323dc25.png" referrerpolicy="no-referrer"></p> 
<p>感谢腾讯同事 fineday009, <span style="background-color:#ffffff; color:#24292e">jun0315</span>, <span style="background-color:#ffffff; color:#24292e">Wscats, caohao-php</span> 为 APIJSON 贡献代码。<br> 感谢 Rkyzzy, kxlv2000, <span style="background-color:#ffffff; color:#24292e">gdjs2</span>, 403f, gujiachun 为 APIJSON 共 6 次 贡献代码。</p> 
<p><strong>APIJSON 4.7.0 更新内容</strong><br> <span style="background-color:#ffffff; color:#40485b">新增数据源关键词 @datasource，可由业务完全自定义；<br> 解决 Oracle 低版本分页语法兼容问题，OFFSET LIMIT 改为 ROWNUM+子查询；<br> 优化分页查询、各种 JOIN、查询计划 等并修复相关  bug。</span></p> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<p><span style="background-color:#ffffff; color:#40485b"><a href="https://gitee.com/APIJSON/APIJSON-Demo/tree/master/APIJSON-Java-Server">APIJSON-Demo</a> 新增 连接池及多数据源 Demo（Druid + HikariCP），可自由切换。</span><br>  </p> 
<h1><strong>APIJSON 简介</strong></h1> 
<p>APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。<br> 为 <strong>简单的增删改查、复杂的查询、简单的事务操作</strong> 提供了<strong>完全自动化的万能 API</strong>。<br> 能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。<br> 适合中小型前后端分离的项目，尤其是 BaaS、Serverless、互联网创业项目和企业自用项目。</p> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li> <p><strong>解决十大痛点</strong> (APIJSON 大幅提振开发效率、强力杜绝联调扯皮、巧妙规避文档缺陷、非常节省流量带宽 等)</p> </li> 
 <li> <p><strong>开发提速巨大</strong> (CRUD 零代码热更新自动化，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</p> </li> 
 <li> <p><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</p> </li> 
 <li> <p><strong>社区影响力大</strong> (GitHub 11.1K Star 在 423W Java 项目中排名前 130，远超 FLAG, BAT 等国内外绝大部分开源项目)</p> </li> 
 <li> <p><strong>各项荣誉成就</strong> (腾讯内部3个奖项、腾讯首个 GVP 获奖项目、腾讯后端项目 Star 第一、GitHub Java 周榜第一 等)</p> </li> 
 <li> <p><strong>多样用户案例</strong> (腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</p> </li> 
 <li> <p><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</p> </li> 
 <li> <p><strong>周边生态丰富</strong> (Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</p> </li> 
 <li> <p><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</p> </li> 
 <li> <p><strong>功能丰富强大</strong> (增删改查、分页排序、分组聚合、各种 JOIN、各种子查询、跨库跨表、性能分析 等零代码实现)</p> </li> 
 <li> <p><strong>使用安全简单</strong> (自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</p> </li> 
 <li> <p><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</p> </li> 
 <li> <p><strong>高质可靠代码</strong> (代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</p> </li> 
 <li> <p><strong>兼容各种项目</strong> (对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo，协议不限 HTTP，与其它库无冲突)</p> </li> 
 <li> <p><strong>工程轻量小巧</strong> (仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</p> </li> 
 <li> <p><strong>多年持续迭代</strong> (自 2016 年开源至今已连续维护 4 年，累计 2426 Commits、85 Releases，不断更新迭代中...)</p> </li> 
</ul> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON ，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p><a href="https://gitee.com/tiangao/apijson-go" target>apijson-go</a> 【新】Go 版 APIJSON，目前支持 单表查询、列表筛选、关联查询等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxianglong111%2FAPIJSON-php" target="_blank">APIJSON-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqq547057827%2Fapijson-php" target="_blank">apijson-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> 字节跳动工程师开发的 Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite 等</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZerounary%2FAPIJSONParser" target="_blank">APIJSONParser</a> 第三方 APIJSON 解析器，将 JSON 动态解析成 SQL</p> 
<p><a href="https://gitee.com/own_3_0/ff-api-json" target>FfApiJson</a> <span style="background-color:#ffffff; color:#40485b">用JSON格式直接生成sql 借鉴APIJSON 支持多数据源</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONDemo_ClickHouse" target="_blank">APIJSONDemo_ClickHouse</a> 【新】<span style="background-color:#ffffff; color:#24292e">APIJSON + SpringBoot 连接 ClickHouse 使用的 Demo</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frainboy-learn%2Fapijson-learn" target="_blank">apijson-learn</a> 【新】APIJSON 学习笔记和源码解析</p> 
<p><a href="https://gitee.com/csgitter/APIJSONBoot" target>ApiJsonBoot</a> 基于 APIJSON 的<span style="background-color:#ffffff; color:#40485b">零代码 API 生成框架</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p><a href="https://gitee.com/drone/apijson-examples" target>apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p><a href="https://gitee.com/zhiyuexin/ApiJsonByJFinal">ApiJsonByJFinal</a> 整合 APIJSON 和 JFinal 的 Demo</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAirforce-1%2FSpringServer1.2-APIJSON" target="_blank">SpringServer1.2-APIJSON</a> 智慧党建服务器端，提供 上传 和 下载 文件的接口</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengxianggui%2Fapijson-builder" target="_blank">apijson-builder</a> 一个方便为 APIJSON 构建 RESTful 请求的 JavaScript 库</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p> </p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-c4bb34c8d9c725915101c6be722114c7704.png" referrerpolicy="no-referrer"></p> 
<p><strong>​APIJSON - 零代码接口与文档 ORM 库（</strong>腾讯内外五个奖项、腾讯开源五个第一<strong>）</strong></p> 
<p>后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构！</p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p>
                                        </div>
                                      
</div>
            