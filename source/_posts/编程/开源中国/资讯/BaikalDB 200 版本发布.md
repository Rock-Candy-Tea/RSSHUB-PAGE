
---
title: 'BaikalDB 2.0.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6439'
author: 开源中国
comments: false
date: Thu, 20 May 2021 20:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6439'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2FBaikalDB%2Freleases%2Ftag%2Fv2.0.0" target="_blank">Release BaikalDB v2.0.0 · baidu/BaikalDB (github.com)</a></p> 
<h1>Notice:  </h1> 
<p>滚动升级顺序：BaikalMeta=>BaikalStore=>BaikalDB<br> 如没特殊说明，后续升级步骤都应该按上述顺序进行</p> 
<h1>New Features：</h1> 
<ul> 
 <li>支持cmake编译</li> 
 <li>增加bvar监控</li> 
 <li>修复部分统计信息问题</li> 
 <li>支持b'11'、 0b11、 x'AA'、 0xAA 字面</li> 
 <li>支持子查询</li> 
 <li>支持table t1 join table t2</li> 
 <li>支持binlog</li> 
 <li>增加全局索引的online ddl操作，alter table xxx add index global idx(filed);</li> 
 <li>代价相关会结合一些规则判断，增加索引选择正确率</li> 
 <li>暂时使用直方图+内部的distinct count做等值判断，cmskectch在大表情况下准确性较低</li> 
 <li>支持information_schema流程 ，需要添加新的information_schema的表可以参考src/common/information_schema.cpp</li> 
 <li>统计信息和规则选择索引部分做了修改，选择更准确些</li> 
 <li>增加虚拟索引，alter table id_name_c add VIRTUAL index idx_name (name); 查看受影响的sql：show virtual index;用来新建索引前评估影响</li> 
 <li>using docker-compose to build a minimal three node cluster</li> 
 <li>增加roaringbitmap，可以用于精确统计一些uv，用法与hll类似</li> 
 <li>增加TDIGEST用来做分位值的估算</li> 
 <li>增加db探测store的功能，在单个store假死的情况下可以快速恢复系统，集群更稳定</li> 
 <li>addpeer前会检查rocksdb是否stalling，提前拒绝addpeer，减少禁写风险</li> 
 <li>增加dataindex，在install snapshot时会判断follower的数据是否已经是新的</li> 
 <li>默认从snappy改成增加lz4压缩</li> 
 <li>最底层增加zstd压缩，通过-enable_bottommost_compression开启</li> 
 <li>add funcs: date_add, date_sub, utc_timestamp, last_insert_id</li> 
 <li>rocksdb事务锁改成bthread锁；不阻塞pthread</li> 
 <li>store增加令牌桶流控(qos)，对每类sql做并发限制，降低突发流量对正常sql的影响，默认不开启</li> 
 <li>对每个请求做内存限制，通过db_sql_memory_bytes_limit(8G)和store_sql_memory_bytes_limit(16G)控制</li> 
 <li>定期调用tcmalloc接口回收内存src/common/memory_profile.cpp</li> 
 <li>支持loaddata语句，load的文件目前只能放在server端（相对于baikaldb的路径）</li> 
 <li>一个表多机房时可以设置一个主机房(main_logical_room)，leader总是在主机房内</li> 
 <li>增加索引屏蔽概念，已屏蔽的索引不会被选择，在线索引操作调整：</li> 
</ul> 
<p>    - drop index设置屏蔽状态，2天（table_tombstone_gc_time_s）后自动发起删除流程；目的是删错索引可以快速restore恢复，减少误操作影响<br>     - add index流程走完后，索引为屏蔽状态，需要二次确认restore；防止流程走完后，索引影响老业务，并且无人关注到<br>    - 屏蔽状态的索引转为正常索引：alter table xxx restore index idx</p> 
<h1>Bug Fixes：</h1> 
<ul> 
 <li>修复meta双buf问题</li> 
 <li>修复多次删除创建同名后restore恢复表不一致问题</li> 
 <li>单语句事务可能会导致raft卡住的bug修复</li> 
 <li>修复之前GetApproximateSizes不准的bug</li> 
 <li>修复一些可能的内存泄露问题</li> 
 <li>修复只读事务bug，优化部分流程</li> 
 <li>prepare insert current time default value</li> 
 <li>fix count(*) return NULL expected 0 when filter expr is always false</li> 
 <li>ignore non-json format comment for sql string</li> 
 <li>update last_insert_id when client set the value</li> 
</ul> 
<h1>Performance Improvements:</h1> 
<ul> 
 <li>主表、索引覆盖、全局索引seek优化，去除table_record到mem_row的转化</li> 
 <li>通过plan复用优化select prepare stmt性能</li> 
 <li>提升cstore扫描性能</li> 
 <li>降低qos，memlimit的开销</li> 
 <li>增加了推荐的conf配置</li> 
</ul>
                                        </div>
                                      
</div>
            