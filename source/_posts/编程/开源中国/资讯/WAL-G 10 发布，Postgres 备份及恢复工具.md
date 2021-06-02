
---
title: 'WAL-G 1.0 发布，Postgres 备份及恢复工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5976'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5976'
---

<div>   
<div class="content">
                                                                    
                                                        <p>WAL-G 1.0 版本与 0.2.0+ 版本兼容。WAL-G 现在已经可以用于 MS SQL、MySQL 数据库的生产，而 MongoDB 和 Redis 的支持目前还处于测试阶段。</p> 
<p>WAL-G 1.0 正式发布，该版本更新内容如下：</p> 
<ul> 
 <li>PostgreSQL 远程备份；</li> 
 <li>提高与 PostgreSQL 13 的兼容性，引入 WALG_PREFETCH_DIR 选项；</li> 
 <li>为wal-verify添加了新的选项，现在它需要一个 timeline|integrity 参数；</li> 
 <li>现在不允许从永久备份中创建非永久的 delta 备份；</li> 
 <li>修复不支持 ListObjectsV2 的 S3 实现的兼容性；</li> 
 <li>现在可以告诉 WAL-G 将 .ready 文件直接重命名为 .done 了；</li> 
 <li>WAL prefetch 现在更快了；</li> 
 <li>Catchup-list 命令可以列出专门为 catchup 进行的 delta 备份；</li> 
 <li>支持 Yandex Cloud KMS；</li> 
 <li>GCS 存储的多部分重试；</li> 
 <li>支持 AzureUSGovernmentCloud、AzureChinaCloud、AzureGermanCloud；</li> 
 <li>为 WAL 文件添加元数据；</li> 
 <li>新增删除 PostgreSQL 单一备份的选项；</li> 
 <li>添加 Redis 备份。现在为 Redis 带来 backup-fetch、backup-push、backup-list 和 delete 命令的支持；</li> 
 <li>增加 MySQL catchup 模式：允许在上传新的日志的同时重放 binlogs；</li> 
 <li>增加 SQLServer 单个数据库的重命名恢复功能；</li> 
 <li>为 Redis/MongoDB/SQLServer 等提供错误修复、测试和改进；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fwal-g-10-released-2229%2F" target="_blank">https://www.postgresql.org/about/news/wal-g-10-released-2229/</a></p>
                                        </div>
                                      
</div>
            