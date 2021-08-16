
---
title: 'CloudCanal 社区版正式发布 1.0.1，支持数据校验与数据订正并修复若干问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4076'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4076'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">CloudCanal是一款由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.clougence.com" target="_blank">ClouGence</a>发行的集结构迁移、数据全量迁移/校验/订正、增量实时同步为一体的数据迁移同步平台。产品包含完整的产品化能力，助力企业打破数据孤岛、完成数据互融互通，从而更好的使用数据。</span></p> 
<h1>版本发布</h1> 
<p>CloudCanal社区版1.0.1正式发布</p> 
<p>新特性</p> 
<p><span style="background-color:#ffffff; color:#333333">• 创建任务支持批量裁剪列</span><br> <span style="background-color:#ffffff; color:#333333">• 支持MySQL->MySQL数据源数据校验、订正任务</span><br> <span style="background-color:#ffffff; color:#333333">• 支持数据校验和数据订正任务的重跑</span><br> <span style="background-color:#ffffff; color:#333333">• 无主键无唯一键表也支持update delete</span><br> <span style="background-color:#ffffff; color:#333333">• 支持用户自定义配置异步任务调度相关参数</span><br> <span style="background-color:#ffffff; color:#333333">• parser新增监控项：增量数据处理与写入队列发布延迟</span><br> <span style="background-color:#ffffff; color:#333333">• 支持oracle->oracle迁移</span><br> <span style="background-color:#ffffff; color:#333333">• 支持pg->pg 无嵌套结构的array类型结构迁移和同步</span><br> <span style="background-color:#ffffff; color:#333333">• 新增约束冲突处理策略，针对pg/tidb为对端时，发生duplicated key时支持insert转update逻辑</span><br> <span style="background-color:#ffffff; color:#333333">• 新增kafka commit log</span></p> 
<h1>BUG FIX&优化</h1> 
<p><span style="background-color:#ffffff; color:#333333">• 内核获取列meta信息性能优化</span><br> <span style="background-color:#ffffff; color:#333333">• 优化页面展示数据源顺序，优先展示使用频次高的数据源</span><br> <span style="background-color:#ffffff; color:#333333">• 修复polardb reader读取时cpu load异常偏高的问题</span><br> <span style="background-color:#ffffff; color:#333333">• 修复任务状态展示异常问题</span><br> <span style="background-color:#ffffff; color:#333333">• Oracle->Oracle结构迁移采用新的schema体系</span><br> <span style="background-color:#ffffff; color:#333333">• ES写入优化，单主键表使用主键作为默认_id值</span><br> <span style="background-color:#ffffff; color:#333333">• 修复由于没有获取时间精度、timeformat等ES结构迁移异常</span><br> <span style="background-color:#ffffff; color:#333333">• 优化oracle 物化视图drop index逻辑</span><br> <span style="background-color:#ffffff; color:#333333">• 修复ClickHouse写入null值问题</span><br> <span style="background-color:#ffffff; color:#333333">• 修复mysql->ck无主键表结构迁移问题</span><br> <span style="background-color:#ffffff; color:#333333">• 修复mysql->pg结构迁移中约束中列的映射问题</span><br> <span style="background-color:#ffffff; color:#333333">• 隐藏资源限制相关无效页面</span><br> <span style="background-color:#ffffff; color:#333333">• 修复mysql->tidb同步时schema is null的问题</span></p> 
<h1>关联资料</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F84" target="_blank">CloudCanal Release信息汇总</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F75" target="_blank">CloudCanal安装使用文档(含下载地址)</a></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F76" target="_blank"><span style="color:inherit">MySQL到ClickHouse实时同步-CloudCanal实战</span></a></p>
                                        </div>
                                      
</div>
            