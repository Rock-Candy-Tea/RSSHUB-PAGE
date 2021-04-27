
---
title: 'APIJSON 4.6.7 发布，破万星•感谢腾讯同事和 SUSTech 等 6 个贡献者'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-13b0f81a5ad1bbb82b5ca92366c711bf5f7.png'
author: 开源中国
comments: false
date: Tue, 27 Apr 2021 09:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-13b0f81a5ad1bbb82b5ca92366c711bf5f7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="1436" src="https://oscimg.oschina.net/oscnet/up-13b0f81a5ad1bbb82b5ca92366c711bf5f7.png" width="2558" referrerpolicy="no-referrer"></p> 
<p>感谢腾讯同事 fineday009 为 APIJSON, apijson-framework, APIJSON-Demo 贡献代码。</p> 
<p>感谢 SUSTech CSE department 的 Rkyzzy, kxlv2000 为 APIJSON 共 3 次 贡献代码。</p> 
<p>感谢 gdjs2 两次为 APIJSON 贡献代码，感谢 403f, gujiachun 为 APIJSON 贡献代码。</p> 
<p><strong>APIJSON 4.6.1-4.6.7 更新内容</strong></p> 
<p>加强对 JOIN 和 SQL 函数的防护；</p> 
<p>优化状态信息和日志打印；</p> 
<p>新增登记用户 投投科技-行业领先的平台型金融科技公司；</p> 
<p>贡献者 新增多个生态项目及作者，说明包括知乎基础研发架构师；</p> 
<p>新增一个 Go 版本的 APIJSON：apijson-go；</p> 
<p>新增一个 PHP 版本的 APIJSON：APIJSON-php；</p> 
<p>新增用户发的文章 全国行政区划数据抓取与处理；</p> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<p><img height="1430" src="https://oscimg.oschina.net/oscnet/up-254059ce8971bc4e0638223b7bcc7c7651c.png" width="2472" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h1><strong>APIJSON 简介</strong></h1> 
<p style="text-align:start">APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。</p> 
<p style="text-align:start">为 <strong>简单的增删改查、复杂的查询、简单的事务操作</strong> 提供了<strong>完全自动化的万能 API</strong>。</p> 
<p style="text-align:start">能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。</p> 
<p style="text-align:start">适合中小型前后端分离的项目，尤其是 BaaS、Serverless、互联网创业项目和企业自用项目。</p> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li><strong>解决十大痛点</strong> (APIJSON 大幅提振开发效率、强力杜绝联调扯皮、巧妙规避文档缺陷、非常节省流量带宽 等)</li> 
 <li><strong>开发提速巨大</strong> (CRUD 零代码热更新自动化，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</li> 
 <li><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</li> 
 <li><strong>社区影响力大</strong> (GitHub 10.4K Star 在 370W Java 项目中排名前 140，远超 FLAG, BAT 等国内外绝大部分开源项目)</li> 
 <li><strong>各项荣誉成就</strong> (腾讯内部两个奖项、腾讯首个 GVP 获奖项目、腾讯后端项目 Star 第一、GitHub Java 周榜第一 等)</li> 
 <li><strong>多样用户案例</strong> (腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</li> 
 <li><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</li> 
 <li><strong>周边生态丰富</strong> (Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</li> 
 <li><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</li> 
 <li><strong>功能丰富强大</strong> (增删改查、分页排序、分组聚合、各种 JOIN、各种子查询、跨库跨表、性能分析 等零代码实现)</li> 
 <li><strong>使用安全简单</strong> (自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</li> 
 <li><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</li> 
 <li><strong>高质可靠代码</strong> (代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</li> 
 <li><strong>兼容各种项目</strong> (对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo，协议不限 HTTP，与其它库无冲突)</li> 
 <li><strong>工程轻量小巧</strong> (仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</li> 
 <li><strong>多年持续迭代</strong> (自 2016 年开源至今已连续维护 4 年，累计 2364 Commits、84 Releases，不断更新迭代中...)</li> 
</ul> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FvincentCheng%2Fapijson-doc" target="_blank">apijson-doc</a> APIJSON 官方文档，提供排版清晰、搜索方便的文档内容展示，包括设计规范、图文教程等</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fruoranw%2FAPIJSONdocs" target="_blank">APIJSONdocs</a> APIJSON 英文文档，提供排版清晰的文档内容展示，包括详细介绍、设计规范、使用方式等</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON ，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p style="text-align:start"><a href="https://gitee.com/tiangao/apijson-go" target>apijson-go</a> Go 版 APIJSON，目前支持 单表查询和列表筛选</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxianglong111%2FAPIJSON-php" target="_blank">APIJSON-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqq547057827%2Fapijson-php" target="_blank">apijson-php</a> PHP 版 APIJSON，基于 ThinkPHP，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo，支持 MySQL, PostgreSQL, SQL Server, Oracle</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite 等</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZerounary%2FAPIJSONParser" target="_blank">APIJSONParser</a> 第三方 APIJSON 解析器，将 JSON 动态解析成 SQL</p> 
<p style="text-align:start"><a href="https://gitee.com/own_3_0/ff-api-json" target>FfApiJson</a> <span style="background-color:#ffffff; color:#40485b">用JSON格式直接生成sql 借鉴APIJSON 支持多数据源</span></p> 
<p style="text-align:start"><a href="https://gitee.com/csgitter/APIJSONBoot" target>ApiJsonBoot</a> 基于 APIJSON 的<span style="background-color:#ffffff; color:#40485b">零代码 API 生成框架</span></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p style="text-align:start"><a href="https://gitee.com/drone/apijson-examples" target>apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p style="text-align:start"><a href="https://gitee.com/zhiyuexin/ApiJsonByJFinal">ApiJsonByJFinal</a> 整合 APIJSON 和 JFinal 的 Demo</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAirforce-1%2FSpringServer1.2-APIJSON" target="_blank">SpringServer1.2-APIJSON</a> 智慧党建服务器端，提供 上传 和 下载 文件的接口</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengxianggui%2Fapijson-builder" target="_blank">apijson-builder</a> 一个方便为 APIJSON 构建 RESTful 请求的 JavaScript 库</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p> </p> 
<p><strong>腾讯 APIJSON - 零代码接口与文档 ORM 库</strong></p> 
<p>腾讯内外四个奖项、腾讯开源五个第一：后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构</p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p>
                                        </div>
                                      
</div>
            