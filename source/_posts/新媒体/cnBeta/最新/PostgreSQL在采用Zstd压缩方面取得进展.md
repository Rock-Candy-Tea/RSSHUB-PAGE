
---
title: 'PostgreSQL在采用Zstd压缩方面取得进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0313/e6019e926061dcd.jpg'
author: cnBeta
comments: false
date: Sun, 13 Mar 2022 09:33:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0313/e6019e926061dcd.jpg'
---

<div>   
早在2月份，PostgreSQL就开始了对Zstd压缩的支持，<strong>现在随着过去一周的最新代码变化，这种由Facebook开发的现代压缩算法现在能够在这个领先的开源数据库服务器中发挥更大的作用。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0313/e6019e926061dcd.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>上个月，PostgreSQL的开发者开始围绕处理Zstd压缩作为其LZ4压缩的替代方案进行基础设施的改变。最近几天落地的代码工作包括支持Zstd基础备份压缩，现在PostgreSQL客户端和服务器端的压缩都支持使用Zstd。</p><p>另一个大的补充是这个提交提供了Zstd对WAL中全页写操作的压缩。PostgreSQL的超前写入日志现在支持使用Zstd对全页镜像进行Zstd压缩，目前这是在默认的Zstd压缩级别3下进行的。</p><p>至于Zstd的WAL性能优势，开发人员是这样解释的："zstd很容易超越pglz，而且比LZ4更好，因为人们希望以额外的CPU为代价获得更多的压缩率，但两者在各自的情况下都足够好，所以在其中一个或另一个之间的选择主要是对工作负载模式和涉及的模式的研究。"</p><p>在最终的PostgreSQL 15版本中，我们可以看到这个Zstd压缩工作和更多的内容。</p><p><strong>了解更多：</strong></p><p><a href="https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=7cf085f077df8dd9b80cf1f5964b5b8c142be496" _src="https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=7cf085f077df8dd9b80cf1f5964b5b8c142be496" target="_blank">https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=7cf085f077df8dd9b80cf1f5964b5b8c142be496</a><br></p>   
</div>
            