
---
title: 'MariaDB 10.6.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4492'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 06:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4492'
---

<div>   
<div class="content">
                                                                                            <p>MariaDB 10.6.4 已经发布，MariaDB 10.6 是 MariaDB 当前的稳定系列，具有一些全新特性，并且具有从 MySQL 反向移植和重新实现的特性。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>InnoDB 
  <ul> 
   <li>默认情况下，InnoDB 不再获取建议文件锁</li> 
   <li>加密：自动禁用 file_key_management 插件的密钥轮换检查</li> 
   <li>MySQL 5.7.35 中的一些修复</li> 
   <li>修复了 AIX 上的刷新</li> 
   <li>buf_pool.flush_list 因缓冲池大小调整或 ROW_FORMAT=COMPRESSED 损坏 </li> 
  </ul> </li> 
 <li>优化器 
  <ul> 
   <li>在某些情况下，使用 ORDER BY .. LIMIT 子句和 “为每个记录优化检查范围” 的查询可能会产生不正确的结果</li> 
   <li>比较不同表的列（“tableX.colX=tableY.colY）的查询具有超过 32 个相等条件时可能会导致查询优化器中的堆栈溢出</li> 
   <li>如果被推送的表达式引用派生表列，该列是从具有存储函数调用、@session 变量引用或其他类似构造的表达式计算的，则无法应用 “条件下推到派生表” 优化</li> 
   <li>子查询左侧带有窗口函数的查询可能会导致崩溃</li> 
   <li>修复了 MySQL 错误：使用外连接的 DML 或锁定 SELECT 语句可能会在错误日志中产生此警告：[ERROR] InnoDB: Unlock row could not find a 3 mode lock on the record</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmariadb.com%2Fkb%2Fen%2Fmariadb-1064-release-notes%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            