
---
title: 'APIJSON 5.0.0 发布，零代码强安全 ORM 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-119f4b2b101ca5925aead7f7d7aae190a64.png'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 09:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-119f4b2b101ca5925aead7f7d7aae190a64.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start"><strong>腾讯 IEG 数据产品开发组负责人 xinlin：</strong><br> ”腾讯的 APIJSON 开源方案，它可以做到零代码生成接口和文档，并且整个生成过程是自动化。</p> 
<p style="color:#24292f; text-align:start">当企业有元数据的时候，马上就可以获得接口“</p> 
<p style="color:#24292f; text-align:start">引用来源：腾讯游戏业务竟然是这样利用低代码平台的 | ArchSummit 全球架构师峰会 2021（深圳）</p> 
<p style="color:#24292f; text-align:start"><img height="504" src="https://oscimg.oschina.net/oscnet/up-119f4b2b101ca5925aead7f7d7aae190a64.png" width="1510" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"> </p> 
<p><strong style="color:#24292f">腾讯科技 后台开发高级工程师 雷大锤：</strong><br> <span style="background-color:#ffffff; color:#24292f">“可以抽出时间来看apijson了，这个可以为T10做准备，也是业界很火的东西，可以提升个人影响力！”</span></p> 
<p><span style="background-color:#ffffff; color:#24292f">引用来源：腾讯人工作日常—在沟通和扯皮中度过的一周</span><br> <img height="406" src="https://oscimg.oschina.net/oscnet/up-7f7dd8b3b44219c5a8d3249ce6416676dde.png" width="1522" referrerpolicy="no-referrer"></p> 
<h2> </h2> 
<h2><strong>APIJSON 5.0.0 更新内容：</strong><span style="background-color:#ffffff; color:#24292f">条件任意组合、增强 JOIN, HAVING 等各种功能</span></h2> 
<div> 
 <div> 
  <h2 style="text-align:start">功能</h2> 
  <p style="color:#24292f; text-align:start"><strong>条件组合新增支持任意逻辑表达式<span> </span>@combine:"a | (b & !(c | d))"；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160291080-c2c0ec30-420d-4239-a830-684ec2cd0501.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160291080-c2c0ec30-420d-4239-a830-684ec2cd0501.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><strong>JOIN 新增支持多个字段关联及引用赋值；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290900-a8b11d48-bebd-4a32-94c2-6e4821d977cb.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290900-a8b11d48-bebd-4a32-94c2-6e4821d977cb.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><strong>JOIN ON 新增支持带非引用赋值关联的普通条件；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290080-f4c71795-7fe5-42dc-a862-2cb2c7e0e850.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290080-f4c71795-7fe5-42dc-a862-2cb2c7e0e850.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><strong>JOIN ON 新增支持 &#123;&#125;, <>, $, ~, !, >, <, >=, <= 等多种关联方式；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160289972-b8c63a0d-61bb-45dc-8a7d-59a9b58bd980.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160289972-b8c63a0d-61bb-45dc-8a7d-59a9b58bd980.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start">& INNER JOIN 新增支持单独设置 JOIN 语句中的字段、条件、分组、聚合、排序等；<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290272-1330c8de-fc5f-4d9f-932b-5704eb79e78e.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290272-1330c8de-fc5f-4d9f-932b-5704eb79e78e.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start">* CROSS JOIN 允许没有 JOIN ON 引用赋值关联条件；<br> 模糊搜索 key$:value 新增支持 key 中定制占位符 %, _ 与 value 的拼接方式；<br> 包含选项范围新增支持传路径，例如 key<>:&#123; path: "$", value:82001 &#125;；</p> 
  <p style="color:#24292f; text-align:start"><strong>聚合函数<span> </span>@having<span> </span>支持复杂条件组合，且新增<span> </span>@having& 简化 AND 连接的写法；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290179-ffdbf6c1-c451-46a7-b05f-5c333532e33c.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290179-ffdbf6c1-c451-46a7-b05f-5c333532e33c.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><strong>对<span> </span>@having:"表达式" 和 key&#123;&#125;:"表达式" 新增支持单引号、反引号、各种关键词等；</strong><br> <strong>新增支持<span> </span>@having:"match(arg0..)AGAINST(..)%2=1" 全文检索等函数后带数学表达式；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290338-859f2348-0197-4798-9b43-f2a594a2ea1a.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290338-859f2348-0197-4798-9b43-f2a594a2ea1a.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start">对 key&#123;&#125;:">0;length(key)<=5" 新增支持部分为 RAW SQL；<br> 新增支持 NULL 值<span> </span>@null:"tag"；<br> 新增支持类型转换<span> </span>@cast:"date:DATE"；<br> 新增数组关键词 compat 解决对聚合函数字段通过 query:2 分页查总数返回值错误；<br> 状态信息 msg 新增提问注意事项；</p> 
  <p style="color:#24292f; text-align:start">权限控制：分拆对角色的校验的代码为多个方法，方便灵活重写部分代码；<br> 完善对 id, id&#123;&#125;, userId, userId&#123;&#125; 的条件强制前置 AND 处理；<br> 预估容量新增对 HAVING 聚合函数的处理；<br> 拼错单词 globle 纠正为 global；<br> 去除不必要的 synchonized；<br> 原来的 combine 重命名为 combineMap，combineExpression 重命名为 combine；</p> 
  <p style="color:#24292f; text-align:start">升级自身, fastjson 版本分别为 5.0.0, 1.2.79；</p>   
  <h2 style="text-align:start">使用登记</h2> 
  <p style="color:#24292f; text-align:start"><strong>新增 珠海采筑电子商务有限公司(房地产巨头万科发起)，多个项目使用，感谢<span> </span>@fanpocha<span> </span>的登记<span> </span>#367；</strong><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160292138-977ecd5f-4714-4c59-a5e6-9f8cffba4e29.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160292138-977ecd5f-4714-4c59-a5e6-9f8cffba4e29.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><strong>新增 乐拼用车 的 Logo，感谢<span> </span>@VamChao<span> </span>的登记<span> </span>#187#issuecomment-1009633459；</strong></p> 
  <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290608-f7660152-3146-4a3f-99b0-8165c72ef16a.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290608-f7660152-3146-4a3f-99b0-8165c72ef16a.png" referrerpolicy="no-referrer"></a></p>   
  <h2 style="text-align:start">文档</h2> 
  <p style="color:#24292f; text-align:start">新增功能演示及说明的 GIF 图；<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290688-5716336a-1ae6-4232-8c8b-0e3d21e6774f.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290688-5716336a-1ae6-4232-8c8b-0e3d21e6774f.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2FTommyLemon%2FStaticResources%2Fmaster%2FAPIJSON%2FAPIJSON_query_associate.gif" target="_blank"><img alt src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_associate.gif" referrerpolicy="no-referrer"></a></p>   
  <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F160290711-96cac0f7-cb9f-477e-aa11-343001f68f53.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/160290711-96cac0f7-cb9f-477e-aa11-343001f68f53.png" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2FTommyLemon%2FStaticResources%2Fmaster%2FAPIJSON%2FAPIJSON_query_summary.gif" target="_blank"><img alt src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_summary.gif" referrerpolicy="no-referrer"></a></p> 
  <p style="color:#24292f; text-align:start"> </p> 
 </div> 
</div> 
<div> 
 <p style="color:#24292f; text-align:start"><strong>完整更新日志具体见</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FAPIJSON%2Freleases" target="_blank">Release 发布版本</a>。</p> 
</div> 
<h1> </h1> 
<h1><strong>APIJSON 简介</strong></h1> 
<p style="color:#24292e">APIJSON 是一种专为 API 而生的 JSON 网络传输协议 以及 基于这套协议实现的 ORM 库。<br> <strong>为各种增删改查提供了完全自动化的万能 API，零代码实时满足千变万化的各种新增和变更需求。</strong><br> 能大幅降低开发和沟通成本，简化开发流程，缩短开发周期。<br> 适合中小型前后端分离的项目，尤其是 <strong>初创项目、内部项目、低代码/零代码、小程序、BaaS、Serverless</strong> 等。</p> 
<p style="color:#24292f; text-align:start">通过万能的 API，前端可以定制任何数据、任何结构。<br> 大部分 HTTP 请求后端再也不用写接口了，更不用写文档了。<br> 前端再也不用和后端沟通接口或文档问题了。再也不会被文档各种错误坑了。<br> 后端再也不用为了兼容旧接口写新版接口和文档了。再也不会被前端随时随地没完没了地烦了。</p> 
<p style="color:#24292f; text-align:start"><img height="1174" src="https://oscimg.oschina.net/oscnet/up-7082eac80de0002f12726045e116c7f0d40.png" width="1976" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"><img height="720" src="https://oscimg.oschina.net/oscnet/up-c1a705834de1c195bc0d3801d316c3cd4c3.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"><img height="720" src="https://oscimg.oschina.net/oscnet/up-4486cc0195a24ee1f5935f01ce8adc8bf07.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"><img src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_associate.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"><img height="720" src="https://oscimg.oschina.net/oscnet/up-07f7a7662cfe64b0c5221457013e1aaa3b7.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"><img height="720" src="https://oscimg.oschina.net/oscnet/up-391864b212bacd388d6b8acfa7a296d15af.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<h3><img src="https://raw.githubusercontent.com/TommyLemon/StaticResources/master/APIJSON/APIJSON_query_summary.gif" referrerpolicy="no-referrer"></h3> 
<h3>为什么选择 APIJSON？</h3> 
<ul> 
 <li><strong>解决十大痛点</strong><span> </span>(APIJSON 可大幅提振开发效率、强力杜绝联调扯皮、巧妙规避文档缺陷、非常节省流量带宽等)</li> 
 <li><strong>开发提速很大</strong><span> </span>(CRUD 零代码热更新全自动，APIJSONBoot 对比 SSM、SSH 等保守估计可提速 20 倍以上)</li> 
 <li><strong>腾讯官方开源</strong> (使用 GitHub、Gitee、工蜂 等平台的官方账号开源，微信公众号、腾讯云+社区 等官方公告)</li> 
 <li><strong>社区影响力大</strong> (GitHub 1W+ Star 在 400W+ Java 项目中排名前 110，远超 FLAG, BAT 等国内外绝大部分开源项目)</li> 
 <li><strong>各项荣誉成就</strong> (腾讯内外 5 个奖项、腾讯开源前十、腾讯后端项目 Star 第一、GitHub Java 日周月榜大满贯 等)</li> 
 <li><strong>多样用户案例</strong><span> </span>(腾讯内部用户包含 互娱、音乐、云与智慧，外部用户包含 500 强上市公司、数千亿资本国企 等)</li> 
 <li><strong>适用场景广泛</strong> (社交聊天、阅读资讯、影音视频、办公学习 等各种 App、网站、公众号、小程序 等非金融类项目)</li> 
 <li><strong>周边生态丰富</strong><span> </span>(Android, iOS, Web 等各种 Demo、继承 JSON 的海量生态、零代码 接口测试 和 单元测试 工具等)</li> 
 <li><strong>文档视频齐全</strong> (项目介绍、快速上手、安装部署 等后端、前端、客户端的 图文解说、视频教程、代码注释 等)</li> 
 <li><strong>功能丰富强大</strong> <span style="background-color:#ffffff; color:#24292f">(增删改查、分页排序、分组聚合、各种条件、各种 JOIN、各种子查询、跨库连表 等零代码实现)</span></li> 
 <li><strong>使用安全简单</strong><span> </span>(自动增删改查、自动生成文档、自动管理版本、自动控制权限、自动校验参数、自动防SQL注入等)</li> 
 <li><strong>灵活定制业务</strong> (在后端编写 远程函数，可以拿到 session、version、当前 JSON 对象 等，然后自定义处理)</li> 
 <li><strong>高质可靠代码</strong><span> </span>(代码严谨规范，商业分析软件源伞 Pinpoint 代码扫描报告平均每行代码 Bug 率低至 0.15%)</li> 
 <li><strong>兼容各种项目</strong><span> </span>(协议不限 HTTP，与其它库无冲突，对各类 Web 框架集成友好且提供 SpringBoot, JFinal 的 Demo)</li> 
 <li><strong>工程轻量小巧</strong><span> </span>(仅依赖 fastjson，Jar 仅 280KB，Java 文件仅 59 个共 13719 行代码，例如 APIJSONORM 4.3.1)</li> 
 <li><strong>多年持续迭代</strong><span> </span>(自 2016 年开源至今已连续维护 5 年多，累计 2600+ Commits、80+ Releases，不断更新迭代中...)</li> 
</ul> 
<h3><strong>APIJSON 生态项目</strong></h3> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FkvnZero%2Fhyperf-APIJSON" target="_blank">hyperf-APIJSON</a> 【新】<span style="background-color:#ffffff; color:#24292f">PHP 版 APIJSON，基于 Hyperf(PHP Swoole)，支持 APIJSON 多种关联和多个功能</span>符</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaozb%2FAPIJSON.NET" target="_blank">APIJSON.NET</a> C# 版 APIJSON，支持大部分 APIJSON 功能，支持 MySQL, PostgreSQL, SQL Server, Oracle, SQLite</p> 
<p style="color:#24292e"><a href="https://gitee.com/tiangao/apijson-go">apijson-go</a> 【新】Go 版 APIJSON，支持 单表查询、列表筛选、关联查询、多个功能符等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevinaskin%2Fapijson-node" target="_blank">apijson-node</a> 字节跳动工程师开发的 Node.ts 版 APIJSON，提供 nestjs 和 typeorm 的 Demo</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangchunlin%2Fuliweb-apijson" target="_blank">uliweb-apijson</a> Python 版 APIJSON，支持大部分 APIJSON 功能，支持 MySQL, PostgreSQL, SQL Server, Oracle 等</p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONBoot_Hive" target="_blank">APIJSONBoot_Hive</a> 【新】<span style="background-color:#ffffff; color:#24292e">APIJSON + SpringBoot 连接 Hive, Hadoop 使用的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvcoolwind%2Fapijson-practice" target="_blank">apijson-practice</a>【新】<span style="background-color:#ffffff; color:#24292f">BAT 技术专家开源的 APIJSON 参数校验注解 Library 及相关 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqiujunlin%2FAPIJSONDemo" target="_blank">APIJSONDemo</a>【新】<span style="background-color:#ffffff; color:#24292f">APIJSON 接入 </span><span style="background-color:#ffffff; color:#24292e">ClickHouse</span><span style="background-color:#ffffff; color:#24292f"> 使用 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenyanlann%2FAPIJSONDemo_ClickHouse" target="_blank">APIJSONDemo_ClickHouse</a> 【新】<span style="background-color:#ffffff; color:#24292e">APIJSON + SpringBoot 连接 ClickHouse 使用的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandream7%2Fapijson-db2" target="_blank">apijson-db2</a> <span style="background-color:#ffffff; color:#24292f">APIJSON 接入 IBM 数据库 DB2 的 Demo</span></p> 
<p style="color:#24292e"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxlongwei%2Flight4j" target="_blank">light4j</a> 整合 APIJSON 和微服务框架 light-4j 的 Demo，同时接入了 Redis</p> 
<p style="color:#24292e"><a href="https://gitee.com/drone/apijson-examples" target>apijson-examples</a> 关于 APIJSON 包含 admin, upms, web 的多端 Demo</p> 
<p><strong>感谢热心的作者们的贡献，点 ⭐Star 鼓励他们继续完善吧^_^</strong></p> 
<p> </p> 
<p><img height="1440" src="https://oscimg.oschina.net/oscnet/up-40b62f658e2cc63806b0d1e84119dc5bd05.png" width="2554" referrerpolicy="no-referrer"></p> 
<p><img height="1436" src="https://oscimg.oschina.net/oscnet/up-e7578a99fa987aa49b6c1a618812e1d2461.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-b4ff79ca9a9c63844b09f259a91696cfacf.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p><strong>​腾讯 APIJSON - <span style="background-color:#ffffff; color:#24292f">零代码、全自动、强安全 ORM </span>库</strong></p> 
<p><span style="background-color:#ffffff; color:#24292f">后端接口和文档零代码，前端(客户端) 定制返回 JSON 的数据和结构！</span></p> 
<p><a href="https://gitee.com/Tencent/APIJSON">https://gitee.com/Tencent/APIJSON</a></p> 
<p>创作不易、坚持更难，右上角点 ⭐Star<strong> </strong>支持下吧 ^_^</p> 
<p> </p>
                                        </div>
                                      
</div>
            