
---
title: 'PostgreSQL 发布所有支持版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3799'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3799'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">PostgreSQL 全球开发组发布了其数据库系统所有支持版本的更新，包括 14.1、13.5、12.9、11.14、10.19 和 9.6.24。此版本关闭了两个安全漏洞并修复了过去三个月报告的 40 多个错误。其中，9.6.24 是 PostgreSQL 9.6 的最终版本。</span></p> 
<p><strong>安全问题</strong></p> 
<ul> 
 <li>CVE-2021-23214：服务器处理来自中间人的未加密字节 
  <ul> 
   <li>受影响的版本：9.6 - 14。当服务器配置为使用具有 clientcert 要求的信任身份验证或使用证书身份验证时，尽管使用 SSL 证书验证和加密，中间人攻击者可以在首次建立连接时注入任意 SQL 查询。</li> 
  </ul> </li> 
 <li>CVE-2021-23222：libpq 处理来自中间人的未加密字节 
  <ul> 
   <li>受影响的版本：9.6 - 14。尽管使用了 SSL 证书验证和加密，中间人攻击者仍可以向客户端的前几个查询注入错误响应。如果更多先决条件成立，攻击者可以窃取客户端的密码或其他可能在会话早期传输的机密数据。与对 CVE-2021-23214 的任何利用一样，服务器必须使用具有 clientcert 要求的信任身份验证或使用证书身份验证。</li> 
  </ul> </li> 
</ul> 
<p><strong>其它主要更新内容</strong></p> 
<ul> 
 <li>在传送以部分 WAL 记录结尾的 WAL 段后主服务器崩溃的情况下修复物理复制。应用此更新时，请在主服务器之前更新备用服务器，以便它们在主服务器发生崩溃时准备好处理修复程序</li> 
 <li>修复并行 VACUUM 以便它处理低于 min_parallel_index_scan_size 阈值的索引，如果表至少有两个大于该大小的索引</li> 
 <li>修复 CREATE INDEX CONCURRENTLY 和 REINDEX CONCURRENTLY 写入损坏索引的原因</li> 
 <li>修复 <span style="background-color:#ffffff; color:#0d0a0b">attaching/detaching </span>可能允许某些 INSERT/UPDATE 查询在活动会话中行为不当的分区</li> 
 <li>修复了使用 CREATE TYPE 创建新范围类型的问题，该类型可能导致后续事件触发器或 CREATE TYPE 命令的后续执行出现问题</li> 
 <li>修复作为组合的一部分的域的数组中元素字段的更新</li> 
 <li>禁止 FETCH FIRST WITH TIES 和 FOR UPDATE SKIP LOCKED 的组合</li> 
 <li>修复数字 power() 函数中的极端情况精度损失</li> 
 <li>修复了在子事务中恢复 Portal 快照的问题，这可能会导致崩溃</li> 
 <li>如果事务在导出其快照后失败，则正确清理。</li> 
 <li>修复了备用服务器上可能导致性能下降的 "溢出子事务" 环绕跟踪</li> 
 <li>确保在升级备用服务器期间正确考虑准备好的事务</li> 
 <li>确保在重命名表时使用正确的锁定级别</li> 
 <li>删除同时删除拥有对象的角色时避免崩溃</li> 
 <li>当 shared_memory_type 为 sysv 时，禁止将 huge_pages 设置为 on</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-141-135-129-1114-1019-and-9624-released-2349%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            