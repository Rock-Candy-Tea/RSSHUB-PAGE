
---
title: 'MySQL复制可能造成数据一致的地方'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3d0801f3a246eab2f29e66df642245~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 23:06:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3d0801f3a246eab2f29e66df642245~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上周在讲复制故障处理，利用DML在从主上手工造数据，导致主从复制中断，然后处理复制故障，同时给大家安利了：</p>
<p>课程Demo程序：主从故障自动修复：zhishutech/ReplGurd (github.com)  建议fork|star | watch  有完善的地方请pull回来</p>
<p>复制主从数据一致性校验、修复程序：pt-table-checksum/pt-table-sync 使用。</p>
<p><strong>结课QA环节一个学生问到：老师除了误操作写了从节点造成数据不一致性外，还有哪些原因？</strong></p>
<p>看到这个问题，当时我真的是一口鲜血喷在了屏幕上啊？</p>
<p>在4月26日MySQL复制原理及应用中刚讲了复制原理及半同步中可能出现的数据不一致时间点，整整用了一节课，在5月10日课中，被问到这个问题。有点无语了，老师也想说你们是我见过最差的一届了，怎么刚讲过，你们都忘了呢~~~ ：） 好吧。当时就利用老师的特权给你们留个作业，回顾：MySQL复制原理及应用场景，试试能不能解答复制主从可能造成主从数据不一致的地方。果真有很给力的同学，不管什么是哪一届都还是有很多优秀的同学，第二天一早就收到一份作业，也分享出来，给各位一个参考：</p>
<p><strong>主从复制可能造成不一致分析（作者A1364-路遥-北京）</strong></p>
<p>MYSQL5.7 之前半同步复制采用的是 AFTER_COMMIT 方式--比 AFTER_SYNC 会有更大概率造成数据不一致</p>
<p>AFTER_COMMIT 是先做 REDO COMMIT 后传 BINLOG，做事务提交，只是不给客户端返回。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3d0801f3a246eab2f29e66df642245~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>AFTER_COMMIT模式下丢失数据实验</strong></p>
<p>版本8.0.23 （版本不重要，原理没变，所有MySQL都一样，本期课程使用的MySQL 8.0.23）</p>
<p>主库参数</p>
<p>+-------------------------------------------+--------------+</p>
<p>| Variable_name | Value |</p>
<p>+-------------------------------------------+--------------+</p>
<p>| rpl_semi_sync_master_enabled | ON |</p>
<p>| rpl_semi_sync_master_timeout | 60000000000 |</p>
<p>| rpl_semi_sync_master_trace_level | 32 |</p>
<p>| rpl_semi_sync_master_wait_for_slave_count | 1 |</p>
<p>| rpl_semi_sync_master_wait_no_slave | ON |</p>
<p>| rpl_semi_sync_master_wait_point | AFTER_COMMIT |</p>
<p>| rpl_semi_sync_slave_enabled | OFF |</p>
<p>| rpl_semi_sync_slave_trace_level | 32 |</p>
<p>+-------------------------------------------+--------------+</p>
<p>从库参数</p>
<p>+-------------------------------------------+--------------+</p>
<p>| Variable_name | Value |</p>
<p>+-------------------------------------------+--------------+</p>
<p>| rpl_semi_sync_master_enabled | OFF |</p>
<p>| rpl_semi_sync_master_timeout | 60000000000 |</p>
<p>| rpl_semi_sync_master_trace_level | 32 |</p>
<p>| rpl_semi_sync_master_wait_for_slave_count | 1 |</p>
<p>| rpl_semi_sync_master_wait_no_slave | ON |</p>
<p>| rpl_semi_sync_master_wait_point | AFTER_COMMIT |</p>
<p>| rpl_semi_sync_slave_enabled | ON |</p>
<p>| rpl_semi_sync_slave_trace_level | 32 |</p>
<p>+-------------------------------------------+--------------+</p>
<p>从库上停掉IO_THREAD模拟从库异常</p>
<p><strong>stop replica io_thread;</strong></p>
<p>主库上插入一条数据，此时会HANG住（但是这条数据已经写入了，开启一个会话是可以查到该数据的）</p>
<p>insert into t values(1);</p>
<p>开启新SESSION查询T表</p>
<p>select * from t;</p>
<p>+------+</p>
<p>| id |</p>
<p>+------+</p>
<p>| 1 |</p>
<p>+------+</p>
<p>开启另一个会话杀掉主库MYSQLD进程pkill -9 mysqld</p>
<p>此时从库中是查不到这条数据的。</p>
<p>select * from t;</p>
<p>Empty set (0.00 sec)</p>
<p><strong>如果此时发生主从切换则主从数据发生不一致。这也是after_commit模式复制中幻读现象。 如图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7ecea8571d4e39977359350f2c7078~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>AFTER_SYNC 是先传 binlog 后做 REDO COMMIT</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c71df3ea812b44e2ad7930d7b25c408a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>```</p>
<p>极端有两种情况：</p>
<p>1. 当主库还没来的及把日志传输到从库上；主库上在完成write binlog后crash</p>
<p>2.日志已经传输到从库上,完成了wait slave ack，此时发生crash；应用端此时并没有接收到主库返回OK。</p>
<p>情况1. 主库Crash恢复后，这个事务操作数据可以被commit，这种事务可以称为local commit或是幽灵事务，并没有真正的完成半同步。</p>
<p>情况2. 产生脏数据，是一个业务没得到确认的事务。也可以称为幽灵事务。</p>
<p><strong>在after_sync中，确实不会丢数据了，但有可能会多数据。</strong></p>
<p>那么使用复制如何保证数据的绝对一致性呢？</p>
<p>1. 首先这个需求是假的，不存在的，如果想要绝对的一致目前可以考虑MySQL Group Replication。</p>
<p>2. 再次，如果一定要用复制架构，同时又要绝对的一致性，考虑使用增强半同步结合session_track_gtids功能使用。</p>
<p>3. 复制一定是binlog row格式+gtid，同时在数据库故障时，注意local commit问题，引入数据校验机器。</p>
<p>孔子曰：三人行，必有我师。大胆交流，不耻下问。加油，学到了才是真本事。欢迎交流。</p>
<blockquote>
<p>本文使用 <a href="https://juejin.cn/post/6940875049587097631" target="_blank">文章同步助手</a> 同步</p>
</blockquote></div>  
</div>
            