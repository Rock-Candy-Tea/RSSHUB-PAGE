
---
title: 'BaikalDB 2.1.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9029'
author: 开源中国
comments: false
date: Fri, 06 May 2022 11:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9029'
---

<div>   
<div class="content">
                                                                                            <h2>Notice:</h2> 
<p>滚动升级顺序：BaikalMeta=>BaikalStore=>BaikalDB(本次升级需要严格按照这个顺序，否则会出现兼容性问题) 回滚步骤反过来：BaikalDB=>BaikalStore=>BaikalMeta 如没特殊说明，后续升级步骤都应该按上述顺序进行</p> 
<h2>New Features：</h2> 
<ul> 
 <li>rocksdb升级到6.26.0(protobuf内部是V3.11.2比较稳定，欢迎有能力同学升级下，可以获得更好的性能)</li> 
 <li>comb multi in predicate by @wy1433 #160</li> 
 <li>local index ddl 与 gobal index ddl流程统一</li> 
 <li>新增handle/show sql代替脚本</li> 
 <li>优化旁路探测问题</li> 
 <li>where条件中datetime类似与数字20201212比较兼容mysql</li> 
 <li>支持主机房概念，可以设置主机房，让leader在主机房选出</li> 
 <li>虚拟索引过meta收集任意sql的影响面</li> 
 <li>支持substring_index</li> 
 <li>支持按照网段进行负载均衡</li> 
 <li>region split主动add peer，防止单副本运行</li> 
 <li>partition表兼容mysql语法</li> 
 <li>支持online TTL</li> 
 <li>delete、update支持子查询</li> 
 <li>支持regexp</li> 
 <li>drop index force可以直接走删除流程</li> 
 <li>新增函数： timestamp, lpad, rpad, time_format, convert_tz, isnull, database, cast, convert, default @wy1433</li> 
 <li>新增系统表：ROUTINES，KEY_COLUMN_USAGE ， REFERENTIAL_CONSTRAINTS @wy1433</li> 
 <li>兼容jdbc8.0驱动 @wy1433</li> 
 <li>支持表注释，并支持alter table修改表注释，及comment里面内容 @wy1433</li> 
 <li>drop index忽略索引名称大小写 @wy1433</li> 
 <li>支持sql单行注释写法 @wy1433</li> 
 <li>增加manual_split_region可以手工分裂</li> 
 <li>增加内存限制功能</li> 
 <li>建表使用unique index默认改成global的，可以通过unique index local来指定成local的，可以通过-unique_index_default_global=false改成默认是local的</li> 
 <li>建表使用普通索引index默认还是local的，可以通过index global指定成global的，可以通过-normal_index_default_global=true改成默认是global的</li> 
 <li>通过-open_nonboolean_sql_forbid=true可以禁止非bool表达式参与and/or计算，默认false</li> 
 <li>通过-open_non_where_sql_forbid=true可以禁止没有where条件的update/delete，默认false</li> 
 <li>通过-limit_unappropriate_sql=true可以限制手工sql（每个db执行次数少于3次）每个store并发到1，防止store被打挂，默认false</li> 
 <li>支持ingest sst方式的快速导入功能（暂未适配开源编译，将在后续开放）</li> 
</ul> 
<h2>Bug Fixes：</h2> 
<ul> 
 <li>修复子查询中常量不能替换’?‘的bug</li> 
 <li>修复insert select未更新自增主键</li> 
 <li>修复tdigest agg问题</li> 
 <li>修复各种事务问题</li> 
 <li>修复1pc和2pc混用卡住问题</li> 
 <li>修复update set now()时3副本不一致问题，rand()函数不是const</li> 
 <li>修复全局索引并发写primary和secodary的问题</li> 
 <li>修复baikaldb死循环，出core问题</li> 
 <li>修复子查询join全局索引表出core</li> 
 <li>修复fake binlog 不反查primary region</li> 
 <li>add peer过程中正好触发延时删除ingest失败</li> 
 <li>修复包含slot的like predict bug</li> 
 <li>修复current_timestamp问题</li> 
 <li>修复标量子查询core和多列问题</li> 
 <li>修复全局索引+row_ttl</li> 
 <li>修复order by超过1个表达式计算问题</li> 
 <li>write binlog错误码修复</li> 
 <li>子查询kill问题修复</li> 
 <li>datediff 问题修复</li> 
 <li>修复match against类型推导</li> 
 <li>修复全局索引+insert duplicate中values函数不生效问题</li> 
</ul> 
<h2>Performance Improvements:</h2> 
<ul> 
 <li>region、qos采用双buf降低锁冲突</li> 
 <li>join on驱动表扫描出的等值value进行去重作为被驱动表的条件，降低数据量</li> 
 <li>userinfo使用双buf提升性能</li> 
 <li>qos优化</li> 
 <li>meta cf不使用ingest</li> 
 <li>优化tdigest存储</li> 
 <li>CompactionFilter只做后2层</li> 
 <li>region split优化降低禁写时间</li> 
 <li>meta性能优化和锁优化</li> 
 <li>limit下推 @wy1433 #174</li> 
 <li>注释解析性能优化</li> 
 <li>MemRowDescriptor缓存降低多列情况下开销</li> 
 <li>局部索引内存优化</li> 
 <li>索引key解析优化</li> 
 <li>db到store改用异步请求，降低高并发下bthread数量</li> 
</ul>
                                        </div>
                                      
</div>
            