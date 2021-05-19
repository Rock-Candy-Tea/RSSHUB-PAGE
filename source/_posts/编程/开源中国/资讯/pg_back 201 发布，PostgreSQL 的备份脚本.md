
---
title: 'pg_back 2.0.1 发布，PostgreSQL 的备份脚本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6456'
author: 开源中国
comments: false
date: Wed, 19 May 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6456'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pg_back 是一个用于 PostgreSQL 的转储工具。它的目标是以你想要的格式一次性转储所有或某些带有 Globals 的数据库，因为简单地调用 pg_dumpall 只能转储普通 SQL 格式的数据库。</p> 
<p>在幕后，pg_back 使用 pg_dumpall 来转储 roles 和表空间的定义，使用 pg_dump 来转储所有或每个选定的数据库到一个单独的自定义格式的文件。它还提取数据库级别的 ACL 和没有被 pg_dump 11 之前的版本所转储的配置。最后，它转储 PostgreSQL 实例的所有配置选项。</p> 
<p>pg_back 2.0.1 正式发布，该版本更新内容如下：</p> 
<ul> 
 <li>cbd16a2 确保在 Windows 上使用 passfile；</li> 
 <li>965b068 修复或跳过 Windows 和 macOS 上的测试；</li> 
 <li>67722a1 改进 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freadme.md%2F" target="_blank">README.md</a>；</li> 
 <li>acaa33a 设置 github actions；</li> 
 <li>3e0e420 允许 postgresql URIs 作为连接字符串；</li> 
 <li>1d6f207 在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FREADME.md" target="_blank">README.md</a> 中反斜杠转义文档；</li> 
 <li>b942f68 在 Windows 下强制采用传统的时间戳格式；</li> 
 <li>a0c97c0 让 locking 在 Windows 上正常工作；</li> 
 <li>1c40ad7 用 jackc/pgx 替换 lib/pq；</li> 
 <li>cd3f91b 设置默认主机为 /var/run/postgresql；</li> 
 <li>184b1d1 告诉 pg_dump 和 pg_dumpall 永远不要提示密码；</li> 
 <li>9d6c222 使用 goreleaser 来构建版本和软件包；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Forgrim%2Fpg_back%2Freleases%2Ftag%2Fv2.0.1" target="_blank">https://github.com/orgrim/pg_back/releases/tag/v2.0.1</a></p>
                                        </div>
                                      
</div>
            