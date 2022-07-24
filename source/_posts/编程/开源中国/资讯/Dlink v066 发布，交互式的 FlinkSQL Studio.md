
---
title: 'Dlink v0.6.6 发布，交互式的 FlinkSQL Studio'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2964'
author: 开源中国
comments: false
date: Sun, 24 Jul 2022 00:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2964'
---

<div>   
<div class="content">
                                                                                            <p>Dlink v0.6.6 已经发布，交互式的 FlinkSQL Studio。</p> 
<p>此版本更新内容包括：</p> 
<p>新特性：</p> 
<ul> 
 <li>新增运维中心的作业历史版本列表</li> 
 <li>新增数据开发的历史版本对比功能</li> 
 <li>新增 Flink MySql Catalog</li> 
 <li>新增 FlinkSQLEnv 默认的 Flink Mysql Catalog</li> 
 <li>新增 1.13 版本 Doris 连接默认隐藏 _<em>DORIS_DELETE</em></li> 
 <li>新增 dlink-connector-pulsar</li> 
 <li>新增选择 Checkpoint 重启任务</li> 
 <li>升级 Flink 1.15.0 到 1.15.1</li> 
 <li>新增数据开发的元存储查看</li> 
 <li>新增数据开发的 Flink 元存储信息和列详情</li> 
 <li>添加和更新开源协议头</li> 
 <li>新增作业批量导出导入 Json 文件</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>修复 Flink-connector-phoenix 问题</li> 
 <li>修复作业实例导致的内存溢出</li> 
 <li>升级 Flink 版本和修复 CDC 的问题</li> 
 <li>修复任务实例耗时解析错误的问题</li> 
 <li>修复 Catalog SPI 和 sql 的问题</li> 
 <li>修复运维中心的 Checkpoint 错误以及添加 Savepoint 信息</li> 
 <li>捕获 SQLSinkBuilder 中 translateToPlan 的异常</li> 
 <li>修复打包时发生的异常 修复 CopyrightUtil 问题</li> 
 <li>修复 Flink Yarn Application 提交失败的问题</li> 
 <li>修复报警实例删除的问题</li> 
 <li>允许依赖环路</li> 
 <li>删除未被引用的类</li> 
 <li>修复作业历史字段 null 的问题</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>优化 Flinksql 执行图获取失败时的返回提示</li> 
 <li>从 API 中移除敏感信息如密码</li> 
 <li>修复已被删除的用户登录，显示信息不正确问题</li> 
 <li>优化运维中心的 Checkpoint 页面</li> 
</ul> 
<p>贡献者： <a href="https://www.oschina.net/youpomian">@a279780399 </a> @aiwenmo @Arnu- @darren-da @dzygcc <a href="https://www.oschina.net/forus0322">@Forus0322 </a> <a href="https://www.oschina.net/gaogao110">@yuan </a> @JPengCheng <a href="https://www.oschina.net/mydq">@mydq </a> @syyangs799 @wmtbnbo @zhu-mingye</p> 
<p>详情查看：<a href="https://gitee.com/DataLinkDC/Dinky/releases/v0.6.6">https://gitee.com/DataLinkDC/Dinky/releases/v0.6.6</a></p>
                                        </div>
                                      
</div>
            