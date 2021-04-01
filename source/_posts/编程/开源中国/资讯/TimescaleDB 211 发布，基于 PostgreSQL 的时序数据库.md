
---
title: 'TimescaleDB 2.1.1 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=886'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=886'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TimescaleDB 2.1.1 现已发布，这是一个维护版本，包含了自 2.1.0 版本以来的 bugfixes，官方将其视为高度优先升级。TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。 </p> 
<p>该版本中的 bug 修复解决了超表、自定义作业和 gapfill 查询的 CREATE INDEX 和 UPSERT 问题。同时，这个版本标志着 TimescaleDB 在 PG13 中成为一个受信任的扩展，因此安装扩展时不再需要超级用户权限。</p> 
<p><strong>Minor features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2998" target="_blank">＃2998</a> 将 timescaledb 标记为受信任的扩展</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2948" target="_blank">＃2948</a> 修复直方图反序列化中的 4 个错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2974" target="_blank">＃2974</a> 修复为带有 dropped columns 的超表创建索引的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2990" target="_blank">＃2990</a> 修复 cagg 的 job_config_check 中的 segfault</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F2987" target="_blank">＃2987</a> 修复由于 embed_log_hook_callback 中的 txns 导致的崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3042" target="_blank">＃3042</a> Commit end transaction for CREATE INDEX</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3053" target="_blank">＃3053</a> 修复 gapfill/hashagg planner 的交互</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3059" target="_blank">＃3059</a> 修复带有默认列的超表上的 UPSERT</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.1.1" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.1.1</a></p>
                                        </div>
                                      
</div>
            