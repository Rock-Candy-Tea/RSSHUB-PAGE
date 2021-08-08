
---
title: 'MiniDao 1.8.3 发布，持久化解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4216'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 15:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4216'
---

<div>   
<div class="content">
                                                                                            <p>MiniDao 1.8.3 已经发布，持久化解决方案。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>数据库分页方言重构支持含常规、国产、大数据等28种数据库</li> 
</ul> 
<table> 
 <thead> 
  <tr> 
   <th>数据库</th> 
   <th>支持</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>MySQL</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>Oracle、Oracle9i</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>SqlServer、SqlServer2012</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>PostgreSQL</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>DB2、Informix</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>MariaDB</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>SQLite、Hsqldb、Derby、H2</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>达梦、人大金仓、神通</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>华为高斯、虚谷、瀚高数据库</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>阿里云PolarDB、PPAS、HerdDB</td> 
   <td>√</td> 
  </tr> 
  <tr> 
   <td>Hive、HBase、CouchBase</td> 
   <td>√</td> 
  </tr> 
 </tbody> 
</table> 
<ul> 
 <li>数据库实现自动适配不再需要手工配置DB类型</li> 
 <li>解决上个版本重构后，不支持SqlServer分页问题</li> 
 <li>debug模式下，解决报错: Minidao报错“Template java/lang/Object_toString.sql not found”</li> 
 <li>ID支持主键策略自动生成 @TableId(type = IdType.UUID)</li> 
 <li>@TableId 支持uuid(默认)\AUTO(自增)\ID_WORKER(雪花ID)\ID_SEQ(序列seq,必须配置seqName)四种主键策略</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/jeecg/minidao/releases/1.8.3">https://gitee.com/jeecg/minidao/releases/1.8.3</a></p>
                                        </div>
                                      
</div>
            