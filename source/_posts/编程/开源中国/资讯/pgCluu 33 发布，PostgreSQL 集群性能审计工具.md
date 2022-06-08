
---
title: 'pgCluu 3.3 发布，PostgreSQL 集群性能审计工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5718'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5718'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">pgCluu 3.3 现已发布，这是一个维护版本；修复了过去九个月以来用户报告的问题，还增加了一些新的功能。</span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">pgCluu 是一个</span><span style="background-color:#ffffff">用于对 PostgreSQL 集群的性能进行全面审计</span><span style="background-color:#ffffff">的工具。</span><span style="background-color:#ffffff">它分为两部分，一个用于使用 psql 和 sar 获取 PostgreSQL 服务器上的统计信息的 collector；以及一个 reports builder，用于生成所有 HTML 和图表输出。</span></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">一些更新内容如下：</span></span></p> 
<ul> 
 <li>从 sar -nTCP,ETCP 添加 TCP 利用率和 TCP 错误报告。</li> 
 <li>如果 suggested index 可能与现有索引重复时，在 CREATE INDEX 中添加 comment。</li> 
 <li>添加支持以具有 pg_monitor 角色的用户身份运行 pgcluu_collect。</li> 
 <li>修复多余的索引查询，以便在 PG < 10 的情况下工作，regexp_match() 必须由 regexp_matches() 替换，并进行一些额外的重写。</li> 
 <li>用 pg_ls_waldir 替换对 pg_ls_dir 的调用，以便从 PG10 开始能够使用 pg_monitor 的权限。</li> 
 <li>修复无法使用 --lock-timeout 的问题。</li> 
 <li>在查询 pgbouncer 时，从 PGOPTIONS 内部删除 lock_timeout，之后会恢复旧值。</li> 
 <li>修复网络错误的禁用。</li> 
 <li>修复 pgbouncer 命令。</li> 
</ul> 
<p>有关更改和错误修复的完整列表，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flzlabs%2Fpgcluu%2Freleases%2Ftag%2Fv3.3" target="_blank">ChangeLog</a>。</p>
                                        </div>
                                      
</div>
            