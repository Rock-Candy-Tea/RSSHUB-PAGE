
---
title: 'WAL-G 1.1 发布，数据库恢复工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4128'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 06:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4128'
---

<div>   
<div class="content">
                                                                                            <p>WAL-G 是 WAL-E 的继承者，是一个用于 PostgreSQL、MySQL/MariaDB 和 MS SQL Server（MongoDB 和 Redis 测试版）的归档恢复工具。</p> 
<p>WAL-G 1.1 发布，更新内容如下：</p> 
<h3>功能/修复：</h3> 
<ul> 
 <li>在 GitHub 发布的版本中包含了 libsodium；</li> 
 <li>UserData 现在必须是有效的 JSON；</li> 
 <li>backup-list 现在可以按照完成的天文时间来排序备份；</li> 
</ul> 
<h3>Postgres:</h3> 
<ul> 
 <li>防止 .history 文件被覆盖的问题修复；</li> 
 <li>Wal-verify 现在可以从备用数据库运行；</li> 
 <li>Wal-verify 现在可以忽略永久备份了；</li> 
</ul> 
<h3>MongoDB：</h3> 
<ul> 
 <li>增加对 MongoDB 5.0 的支持；</li> 
</ul> 
<h3>SQLServer：</h3> 
<ul> 
 <li>修复 MSSQL 驱动导入；</li> 
</ul> 
<h3>MySQL：</h3> 
<ul> 
 <li>增加 <code>--turbo</code> 标志以禁用限制器；</li> 
 <li>修复 <code>--detailed</code> 的备份列表错误；</li> 
 <li>在 binlog-push 中添加 <code>--until</code> 标志；</li> 
</ul> 
<h3>Redis:</h3> 
<ul> 
 <li>增加 6.2 支持和 redis-cli 错误解决；</li> 
</ul> 
<h3>存储：</h3> 
<ul> 
 <li>S3：支持客户 SSE 密钥；</li> 
 <li>Azure：支持不含前面'?' 的 <code>AZURE_STORAGE_SAS_TOKEN</code>；</li> 
 <li>Azure：禁用不必要的系统日志写入；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fwal-g-11-released-2278%2F" target="_blank">https://www.postgresql.org/about/news/wal-g-11-released-2278/</a></p>
                                        </div>
                                      
</div>
            