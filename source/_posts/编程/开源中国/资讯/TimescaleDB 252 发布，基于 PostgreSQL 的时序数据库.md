
---
title: 'TimescaleDB 2.5.2 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6052'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6052'
---

<div>   
<div class="content">
                                                                                            <p>TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。此版本增加了对分布式超表（多节点 TimescaleDB）的支持，并添加了一些新特性和功能增强，让用户对数据的控制更加清晰和灵活。</p> 
<p>TimescaleDB 2.5.2 现已发布，这个版本值得注意的特性包括：</p> 
<h3>错误修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3900" target="_blank">#3900</a> 改进自定义扫描节点的注册</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3911" target="_blank">#3911</a> 修复 GRANT 命令的 role 类型解析</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3918" target="_blank">#3918</a> 使用一次性过滤器修复 DataNodeScan 计划</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3921" target="_blank">#3921</a> 修复插入内部压缩表时的 segfault 错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3938" target="_blank">#3938</a> 修复 32 位平台上的 subtract_integer_from_now 并改进错误处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3939" target="_blank">#3939</a> 在 time_bucket_gapfill 中修复映射（projection）处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3948" target="_blank">#3948</a> 在数据提取器中避免双重 PGclear()</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F3979" target="_blank">#3979</a> 修复索引谓词的解析</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4015" target="_blank">#4015</a> 在 interpolate 中消除浮点取整的不稳定性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4020" target="_blank">#4020</a> 修复 ALTER TABLE EventTrigger 初始化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4024" target="_blank">#4024</a> 修复过早的缓存释放调用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4037" target="_blank">#4037</a> 修复具有目录条目的已删除块的状态</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4069" target="_blank">#4069</a> 修复 ANY 结构中的 riinfo NULL 处理问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fpull%2F4071" target="_blank">#4071</a> 修复扩展安装权限提升问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Freleases%2Ftag%2F2.5.2" target="_blank">https://github.com/timescale/timescaledb/releases/tag/2.5.2</a></p>
                                        </div>
                                      
</div>
            