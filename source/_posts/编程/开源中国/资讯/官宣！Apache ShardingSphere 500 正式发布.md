
---
title: '官宣！Apache ShardingSphere 5.0.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pica.zhimg.com/80/v2-185e126de7d64409f3f4193270a347bc_1440w.webp'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 17:25:00 GMT
thumbnail: 'https://pica.zhimg.com/80/v2-185e126de7d64409f3f4193270a347bc_1440w.webp'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <div>
  <span><span>11 月 10 日，是 Apache ShardingSphere 进入 Apache 基金会的三周年纪念日。在这特殊的一天，我们很高兴的宣布 Apache ShardingSphere 迎来了 5.0.0 GA 版本的正式发布。</span></span>
  <span> </span>
  <strong><span>经过近两年的优化和打磨，ShardingSphere 5.0.0 GA 版正式开启了以可插拔架构为核心的全新阶段，实现了由过去数据分片单一应用场景到现在复杂应用环境下综合数据治理的身份转变与能力提升。</span></strong>
 </div> 
</blockquote> 
<div style="text-align:left"> 
 <div>
  <span><span>5.0.0 具体版本发布信息如下：</span></span>
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>1<span> </span></span></em><em><span>新特性</span></em></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>支持注释解析</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：初步支持 openGauss</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：增加增量同步是否已完成检测算法 SPI 接口</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：增加数据校验算法 SPI 接口</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：迁移前自动建表基本支持 MySQL 和 openGauss</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：与 proxy 整合更完善，支持迁移完成自动切换配置</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：提供更多的 DistSQL 支持，数据校验、切换配置等</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：支持 DistSQL 自动触发迁移</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：Shadow 规则管理</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：弹性伸缩任务管理</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：Proxy 实例熔断</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：读写分离读库禁用</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>ALTER RESOURCE</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>DROP SHARDING ALGORITHM</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>CREATE SHARDING ALGORITHM</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>CREATE DEFAULT SHARDING [TABLE | DATABASE] STRATEGY</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>SHOW ALL VARIABLES</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>新增 DistSQL 语法：</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>SHOW VARIABLE variableName;</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>Proxy 支持 openGauss</span></span>
  </div> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>2 API 变更</span></em></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>ShardingSphere-JDBC 增加 schema name 配置</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>增加默认分片键配置</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>默认 authority provider 由<span> </span></span></span>
   <span style="background-color:#f6f6f6"><span>NATIVE</span></span>
   <span> </span>
   <span><span>调整为<span> </span></span></span>
   <span style="background-color:#f6f6f6"><span>ALL_PRIVILEGES_PERMITTED</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>SCTL 语法调整，与 DistSQL RAL 语法合并</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>SHOW RESOURCES</span></span>
   <span> </span>
   <span><span>DistSQL 调整为<span> </span></span></span>
   <span style="background-color:#f6f6f6"><span>SHOW SCHEMA RESOURCES</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>影子库压测：移除<span> </span></span></span>
   <span style="background-color:#f6f6f6"><span>shadow</span></span>
   <span> </span>
   <span><span>逻辑字段，支持 shadow 算法</span></span>
  </div> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>3 增强</span></em></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>元数据重构以及性能提升</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持 MySQL union/union all 语句解析</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持 PostgreSQL ABORT 语句</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持 PostgreSQL CREATE INDEX 语句未指定索引时，自动生成索引</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持带逻辑 schema 的 SQL 语句执行</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持绑定表配置不同分片键</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>ShardingSphere 内核性能优化</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>Proxy 支持对部分 information_schema 表的查询，优化客户端连接体验</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>DistSQL 支持用引号的的方式将关键字作为参数名</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>ADD RESOURCE</span></span>
   <span> </span>
   <span><span>语句中 password 支持特殊字符</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>ADD RESOURCE</span></span>
   <span> </span>
   <span><span>支持自定义 JDBC 参数和连接池属性</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>DROP RESOURCE</span></span>
   <span> </span>
   <span><span>支持可选参数 ignore single tables，用于忽略单表规则限制</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>支持在读写分离规则的基础上，使用 DistSQL 创建 sharding table rule</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>SHOW DATABASES</span></span>
   <span> </span>
   <span><span>语句支持 like 语法</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>CREATE SHARDING TABLE RULE</span></span>
   <span> </span>
   <span><span>支持使用 inline 表达式指定资源</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>CREATE SHARDING TABLE RULE</span></span>
   <span> </span>
   <span><span>支持使用 dataNodes 的方式配置分片</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>CREATE SHARDING TABLE RULE</span></span>
   <span> </span>
   <span><span>支持复用已有算法</span></span>
  </div> </li> 
 <li> 
  <div>
   <span style="background-color:#f6f6f6"><span>SET VARIABLE</span></span>
   <span> </span>
   <span><span>，支持修改 Proxy 配置</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>PostgreSQL 协议完善（支持 Portal、未指定类型的数据等）</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>Proxy 支持切换 Netty 线程池在部分场景提高性能</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>Proxy 与数据库交互的 fetch size 可配置</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：完善对 PostgreSQL 的支持</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：数据校验支持源端和目标端并行计算</span></span>
  </div> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>4 重构</span></em></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>重构 SingleTable 功能以支持 Encrypt 多数据源</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>重构 examples，调整模块结构</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>调整注册中心节点持久化数据结构</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：重构增量同步是否已完成检测算法默认实现</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：重构数据校验算法默认实现</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>弹性伸缩：移除 HTTP API 和独立打包</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>影子库压测：去除 DML 重写流程</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>影子库压测：支持 DDL 路由</span></span>
  </div> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>5 漏洞修复</span></em></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 
  <div>
   <span><span>修复 INTERVAL 分片算法问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 SHOW INDEX FROM TABLE FROM TABLE 语句改写异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Encrypt 多表关联改写异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复子查询 index out of range 异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Oracle 分页异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Sharding 场景下未配置 KeyGenerateStrategy 时改写异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Oracle 方言大小写导致 Federation 执行引擎异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Sharding/Encrypt 整合使用时改写异常</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Oracle 元数据加载异常的问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复</span></span>
   <span> </span>
   <span style="background-color:#f6f6f6"><span>SHOW RESOURCES<span> </span></span></span>
   <span><span>语句无法展示自定义属性的问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 SQL 执行异常不抛出的问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Etcd 无法发送节点新增事件</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 PostgreSQL Proxy 查询结果可能丢失包含 null 值的数据行的问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 PostgreSQL 元数据列顺序可能错乱的问题</span></span>
  </div> </li> 
 <li> 
  <div>
   <span><span>修复 Proxy 字符编码可能不正确的问题</span></span> 
  </div> </li> 
</ul> 
<div style="text-align:left"> 
 <div>
  <span><span>🔗下载链接：</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fdocument%2Fcurrent%2Fcn%2Fdownloads%2F" target="_blank"><span><span>https://shardingsphere.apache.org/document/current/cn/downloads/</span></span></a>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  <span><span>🔗更新日志：</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere%2Fblob%2Fmaster%2FRELEASE-NOTES.md" target="_blank"><span><span>https://github.com/apache/shardingsphere/blob/master/RELEASE-NOTES.md</span></span></a>
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  <span><span>🔗项目地址：</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2F" target="_blank"><span><span>https://shardingsphere.apache.org/</span></span></a>
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><em><span>6 社区建设</span></em></h2> 
<div style="text-align:left"> 
 <div>
  <span><span>Apache ShardingSphere 5.0.0 版本的发布离不开社区用户的支持和贡献，期间</span></span>
  <span> </span>
  <strong><span>共有 168 位 Contributor 提交了 4468 个 PR</span></strong>
  <span> </span>
  <span><span>，助力 ShardingSphere 5.0.0 版本的全力发布，感谢社区伙伴们的大力支持。</span></span>
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div style="text-align:center">
    <img src="https://pica.zhimg.com/80/v2-185e126de7d64409f3f4193270a347bc_1440w.webp" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div style="text-align:center">
   
 </div> 
 <div>
  <span><span>再次欢迎大家测试</span></span>
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Fdocument%2Fcurrent%2Fcn%2Fdownloads%2F" target="_blank"><span><span>使用 ShardingSphere 5.0.0</span></span></a>
  <span> </span>
  <span><span>，同时欢迎大家参与社区讨论！</span></span>
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            