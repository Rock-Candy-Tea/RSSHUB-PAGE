
---
title: 'pgBadger 11.7 发布，PostgreSQL 性能分析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4799'
author: 开源中国
comments: false
date: Tue, 25 Jan 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4799'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">pgBadger 是一款 PostgreSQL 性能分析器，专为提高速度而构建，并基于 PostgreSQL 日志文件提供详细报告。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这个版本的 pgBadger 修复了过去 5 个月以来用户报告的一些问题，以及一些改进。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加了新的选项<span> </span><code>--no-progressbar</code>，可以不显示 progressbar 而保留其他输出</li> 
 <li>增加了新的选项<span> </span><code>--day-report</code>，可以用来在指定的一天内重建一个 HTML 报告。就像选项<span> </span><code>--month-report</code><span> </span>，但它只针对一天。其格式为：YYYY-MM-DD</li> 
 <li>改进对 Heroku logplex 和 cloudsql json 日志的解析。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">其他更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新贡献指南和 Makefile.PL 以提高一致性、清晰度和依赖性</li> 
 <li>修正在二进制模式下使用最后一次解析文件（--last-parsed）的问题</li> 
 <li>增加了对<span> </span><code>--last-parsed</code><span> </span>使用的回归测试，并修复了仅对临时文件报告的回归测试。</li> 
 <li>当启用<span> </span><code>--iso-week-number</code><span> </span>和<span> </span><code>--incremental</code><span> </span>选项时，修正计算周数报告的周数。</li> 
 <li>防止多行 jsonlog 在调试模式下打印太多的未知格式行</li> 
 <li>即使使用了<span> </span><code>-q</code><span> </span>或<span> </span><code>-quiet</code>，仍用<span> </span><code>-v</code><span> </span>打印调试信息</li> 
 <li>修复 jsonlog 文件的自动检测</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdarold%2Fpgbadger%2Freleases%2Ftag%2Fv11.7" target="_blank">https://github.com/darold/pgbadger/releases/tag/v11.7</a></p>
                                        </div>
                                      
</div>
            