
---
title: 'DataEase 开源数据可视化分析平台 v1.4.0 发布，新增两种支持数据源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-03baa3a55abf82d3710d65fc25ab01228fd.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 10:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-03baa3a55abf82d3710d65fc25ab01228fd.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="680" src="https://oscimg.oschina.net/oscnet/up-03baa3a55abf82d3710d65fc25ab01228fd.png" width="1696" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">11月8日，DataEase开源数据可视化分析平台正式发布v1.4.0版本。在该版本中，新增了对MongoDB和Amazon Redshift数据源的支持；视图方面增加引入了新图形库AntV，并在新图库基础上增加了对瀑布图的支持；底层数据连接方面，以阿里的druid替换了原有的c3p0，提升了数据库连接性能；仪表板方面，增加了对跳转功能的支持，并新增了一种仪表板组件（时间组件）。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#0a7be0">■ 数据源新增支持MongoDB和Amazon Redshift</span></strong></p> 
<p style="margin-left:0; margin-right:0">在DataEase v1.4.0版本中，我们增加了对MongoDB和Amazon Redshift数据源的支持。</p> 
<p style="margin-left:0; margin-right:0"><em><span style="color:#0a7be0">特别感谢：</span>社区开发者boolean-dev提供了针对Amazon Redshift数据源的功能PR。</em></p> 
<p style="margin-left:0; margin-right:0"><img alt height="603" src="https://oscimg.oschina.net/oscnet/up-d670c7d9a97a31469a7b5bd814e9b89156a.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 引入新图形库AntV，增加对瀑布图的支持</span></strong></p> 
<p style="margin-left:0; margin-right:0">在DataEase v1.4.0版本中，引入了蚂蚁数据可视化解决方案AntV，在新图形库的基础上完成了对原有视图图表类型的支持，并增加了新的图表类型瀑布图。</p> 
<p><img alt height="654" src="https://oscimg.oschina.net/oscnet/up-95cdbefc06fbd8a4a3a877302b38fa41ed8.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 仪表板支持跳转</span></strong></p> 
<p style="margin-left:0; margin-right:0">在DataEase v1.4.0版本中，仪表板新增了对跳转功能的支持，可以实现在仪表板之间的联动跳转，同时支持从仪表板视图打开指定的链接。</p> 
<p><img alt height="907" src="https://oscimg.oschina.net/oscnet/up-a262907870fd4142f4c95b18f4864de16ea.png" width="1840" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.4.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化仪表板排序名称优先功能；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：刷新时间可以设置为秒级别，且可以设置是否显示Loading提示；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：文字组件、Tab组件可以选择设置为背景透明而文字内容不透明；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化仪表板视图详情中背景项为可设置跟随仪表板背景；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：增加拖拽阴影动画，以避免靠右边界矩阵组件改变大小时，可能定位不准的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化编辑时全屏问题、Scroll时样式组件定位问题，去掉部分前端日志；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化编辑状态全屏错位的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化公共链接参数长度；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（视图）：优化Cron组件；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> refactor（视图）：轴线可自定义，限制刻度数不超过100；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor：优化任务日志的请求超时问题。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span> fix：修复MySQL v5.1支持相关的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复视图复制名称过长报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复Elasticsearch不能支持https的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复PostgreSQL时间格式化错误的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复不能识别Elasticsearch版本的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复Elasticsearch table-info的SQL相关问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复在编辑仪表板时，切换至全屏预览，边界上的视图可能错位的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复仪表板复制视图时没有复制下钻字段的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复公共链接的弹框问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复仪表板属性组件显示不全的问题。</p>
                                        </div>
                                      
</div>
            