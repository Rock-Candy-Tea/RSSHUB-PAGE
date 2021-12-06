
---
title: '新增支持 Hive 数据源，DataEase 开源数据可视化分析平台 v1.5.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6c0a31ce6eddbe11cf742577366ba79a650.png'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 11:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6c0a31ce6eddbe11cf742577366ba79a650.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="678" src="https://oscimg.oschina.net/oscnet/up-6c0a31ce6eddbe11cf742577366ba79a650.png" width="1696" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">12月6日，DataEase开源数据可视化分析平台正式发布v1.5.0版本。在该版本中，新增了对Hive数据源的支持；视图方面，图表类型增加了对词云图的支持；视图编辑的操作上，提供了重置功能，并取消了之前版本的实时保存功能；数据集方面新增同步字段功能，解决了由于数据集变化导致的视图不可用的问题；仪表板方面，增加了对视频组件的支持。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#0a7be0">■ 数据源新增支持Hive</span></strong></p> 
<p style="margin-left:0; margin-right:0">截至DataEase v1.4版本，DataEase支持的数据源包括Excel、MySQL、Oracle、SQL Server、PostgreSQL、Elasticsearch、MariaDB、Apache Doris、ClickHouse、MongoDB、Amazon Redshift等。在DataEase v1.5.0版本中，我们增加了对Hive数据源的支持。</p> 
<p style="margin-left:0; margin-right:0">Hive是基于Hadoop的一个数据仓库工具，用来进行数据提取、转化、加载，是一种可以存储、查询和分析存储在Hadoop中大规模数据的机制。Hive的优点是学习成本低，可以通过类似SQL语句实现快速MapReduce统计，使MapReduce变得更加简单，而不必开发专门的MapReduce应用程序。</p> 
<p><img alt height="599" src="https://oscimg.oschina.net/oscnet/up-436fad18061f3e51d8a79fb522baf245c58.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 数据集新增同步字段功能</span></strong></p> 
<p style="margin-left:0; margin-right:0">在之前版本的DataEase中，用户编辑数据集时，不论是否对原有字段进行修改，都可能会造成诸如视图无法显示等异常情况，且数据集表结构的变化也无法更新到之前的数据集中。DataEase v1.5.0版本中，在数据集管理页新增了同步字段功能，用户在修改了数据库表结构后，能够在DataEase中将更新的字段信息同步过来，解决之前版本中所存在的问题。</p> 
<p><img alt height="568" src="https://oscimg.oschina.net/oscnet/up-3e28d5d16e00b39706427004b8806c8b059.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 视图增加对词云图的支持</span></strong></p> 
<p style="margin-left:0; margin-right:0">视图图表的支持对于数据可视化工具来说至关重要，DataEase一直坚持在持续迭代的每个版本中不断增加对新图表类型的支持。在DataEase v1.5.0版本中，增加了新的图表类型——词云图。词云图由词汇组成类似云的彩色图形，用于展示大量文本数据。例如，制作用户画像、对用户进行聚类，实现精细化营销。</p> 
<p><img alt height="617" src="https://oscimg.oschina.net/oscnet/up-70c7446ddd80d1bde661ec89513b00f1a1a.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 仪表板支持视频组件</span></strong></p> 
<p style="margin-left:0; margin-right:0">多媒体元素对于数据可视化来说也是非常重要的组成部分，它可以丰富可视化大屏的展示形式，从另一个维度表达出数据所不能表达的内容。在DataEase v1.5.0版本中，新增了视频组件，可以实现在仪表板中播放mp4、webm格式的视频影像，满足了用户对多媒体展现形式的需求。</p> 
<p><img alt height="603" src="https://oscimg.oschina.net/oscnet/up-8a8f5b5c976c445699f73fba6ba970b4cec.png" width="1280" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.5.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span> refactor（数据集）：<span style="background-color:#ffffff; color:#3e3e3e">修复编辑数据集导致字段删除重建的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（数据集）：优化数据集查询；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：移除仪表板自动刷新时的“Loading”动画；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化仪表板PDF的导出，防止导出画面不全；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化组件间隙和仪表板画布间隙；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：增加仪表板编辑快捷入口；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：增加矩形、时间组件的属性设置项；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化仪表板上移、下移、置顶、置底移动算法，可以实时得到移动效果，解决置顶不准确的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor：规范化SQL格式及数据表编码；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor：前端代码去掉不必要的引用，加快编译速度。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复图表类型切换逻辑错误的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复SQL Server计算字段的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复取消短链接的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复源码模式运行时，视图类型样式错乱的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复PostgreSQL时间类型转换的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复Token验签逻辑错误的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复多个时间控件相互影响的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复MongoDB数据源校验有效性的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复文本组件根据仪表板缩放比例自动缩放文本大小和间隙的Bug；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复仪表板日期组件无法二次编辑的Bug。</p>
                                        </div>
                                      
</div>
            