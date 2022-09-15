
---
title: 'pgBadger v12.0 发布，PostgreSQL 性能分析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2273'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2273'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">pgBadger 是一款 PostgreSQL 性能分析器，专为提高速度而构建，并基于 PostgreSQL 日志文件提供详细报告。 pgBadger v12.0 现已发布，</span><span style="background-color:#ffffff; color:#0d0a0b">这是一个主要版本，修复了用户在过去五个月中报告的问题，并进行了一些改进：</span></p> 
<ul> 
 <li>删除对 Tsung output 的支持。</li> 
 <li>当有数百个绑定参数要替换时，提高 pgbadger 的性能。</li> 
 <li>删除选项 -n | --nohighlight，其自升级到 pgFormatter 4 后不再使用。</li> 
 <li>使用 POST 方法将 auto_explain 计划发送到 explain.depesz.com 以避免 GET 长度参数限制。</li> 
 <li>应用 --exclude-query 和 --include-query 来绑定/解析跟踪。</li> 
 <li>将 pgBadger 报告示例的链接添加到文档中。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpgbadger-v120-released-2509%2F" target="_blank">https://www.postgresql.org/about/news/pgbadger-v120-released-2509/</a></p>
                                        </div>
                                      
</div>
            