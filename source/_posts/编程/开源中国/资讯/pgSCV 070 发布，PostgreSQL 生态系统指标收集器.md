
---
title: 'pgSCV 0.7.0 发布，PostgreSQL 生态系统指标收集器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4296'
author: 开源中国
comments: false
date: Sat, 24 Jul 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4296'
---

<div>   
<div class="content">
                                                                                            <p>pgSCV 0.7.0 正式发布，更新内容如下：</p> 
<p><strong>更新：</strong></p> 
<ul> 
 <li>增加对 Patroni 的支持；</li> 
 <li>增加 Patroni 指标与 Patroni 2.1.0 中引入的内置指标的兼容性；</li> 
 <li>增加 TLS 支持；</li> 
 <li>增加基本认证；</li> 
 <li>在每次调用收集器之前发现 postgres 设置。Postgres 设置描述了 Postgres 的属性，如版本、数据和 WAL 块大小、pg_stat_statements 的位置等等，这些设置被收集器使用以调整指标收集。</li> 
 <li>移除查询规范化；在声明指标中使用 <code>queryid</code> 标签替代 <code>md5</code>;</li> 
 <li>引入 ADR；</li> 
 <li>修正只用 ENV 变量配置时禁用自动发现的问题；</li> 
 <li>修正文件系统挂起时的指标收集；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fweaponry%2Fpgscv%2Freleases%2Ftag%2F0.7.0" target="_blank">https://github.com/weaponry/pgscv/releases/tag/0.7.0</a></p>
                                        </div>
                                      
</div>
            