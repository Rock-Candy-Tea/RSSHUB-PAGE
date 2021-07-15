
---
title: 'RediSearch 2.0.10 发布，高性能全文搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7127'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7127'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RediSearch 2.0.10 现已发布，这是 2.0 版的维护版本，更新紧急程度为高，存在一个可能影响部分用户的严重错误。具体更新内容如下：</p> 
<p><strong>Details</strong></p> 
<ul> 
 <li> <p>Enhancements：</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2025" target="_blank">#2025</a> 数字范围搜索的性能改进</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fissues%2F1958" target="_blank">#1958 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2033" target="_blank">#2033</a> 支持对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redislabs.com%2Fredisearch%2F2.0%2FOverview%2F%23geo_index" target="_blank">GEO 类型</a>的可排序</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2079" target="_blank">#2079</a> Snowball 2.1.0 更新，添加了亚美尼亚语、塞尔维亚语和意第绪语的词根支持</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2002" target="_blank">#2002</a> 在 API 中添加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redislabs.com%2Fredisearch%2F2.0%2FStopwords%2F%23overriding_the_default_stop-words" target="_blank">stopwords</a> 列表支持</li> 
  </ul> </li> 
 <li> <p>Bug fix：</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2045" target="_blank">#2045</a> 加载 RDB 文件时可能崩溃（静默忽略别名的双重加载）</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F1994" target="_blank">#1994</a> 如果使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redislabs.com%2Fredisearch%2F2.0%2FQuery_Syntax%2F%23query_attributes" target="_blank">INORDER</a> 标志，则跳过 intersect iterator qsort</li> 
  </ul> </li> 
 <li> <p>RSCoordinator 上的错误修复：</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRSCoordinator%2Fpull%2F257" target="_blank">#257</a> 切换协调器以发送 _FT.CURSOR 而不是 FT.CURSOR，以防止在不持有锁的情况下访问数据。</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.0.10" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.0.10</a></p>
                                        </div>
                                      
</div>
            