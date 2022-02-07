
---
title: 'DataEase 开源数据可视化分析平台 v1.7.0 发布，新增首页模块，支持数据集列权限'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e3be69b03e1f4255eac100e9b28bbe41a.png'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 12:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e3be69b03e1f4255eac100e9b28bbe41a.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="534" src="https://oscimg.oschina.net/oscnet/up-82e3be69b03e1f4255eac100e9b28bbe41a.png" width="1636" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2月7日，DataEase开源数据可视化分析平台正式发布v1.7.0版本。在该版本中，DataEase平台新增了首页模块；X-Pack功能方面，新增对数据集列权限的支持；仪表板方面，年份和年月组件增加了对动态时间的支持。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 数据集列权限（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">用户对于数据权限的控制一般分为两类：一类是限制用户可以访问哪些数据行的数据，即行权限；一类是限制用户可以访问数据的哪些字段，即列权限。在v1.6.0版本中，DataEase在X-Pack增强包中支持了数据集的行权限，实现了同一仪表板对不同用户展示不同内容的功能。v1.7.0版本中，DataEase新增了对列权限的支持，实现了部分用户只能看到部分列的内容。</p> 
<p><img alt height="602" src="https://oscimg.oschina.net/oscnet/up-3234682073639f393e4ba163358c3e5b594.png" width="1280" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 新增首页模块</span></strong></p> 
<p style="margin-left:0; margin-right:0">随着产品的不断迭代，DataEase的功能也越来越多，如何获得DataEase最新的相关资讯，以及如何更好地使用DataEase对用户来说也越来越重要。在v1.7.0版本中，DataEase新增首页模块，该模块包含了DataEase相关的入门视频、教学视频、在线文档、最新动态等内容，用户可以通过首页及时了解DataEase的相关信息，并快速上手使用。</p> 
<p><img alt height="1372" src="https://oscimg.oschina.net/oscnet/up-d7d719103a3ee739ed676f51a14d1d4d668.png" width="2876" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 年份、年月组件增加动态时间支持</span></strong></p> 
<p style="margin-left:0; margin-right:0">DataEase中支持的时间过滤组件共有4种，分别是：年份组件、年月组件、日期组件和日期范围组件。用户可以通过在仪表板中添加时间过滤组件来查看指定时间或时间范围的数据。在v1.6.0版本中，DataEase对日期组件和日期范围组件增加了动态时间的支持。</p> 
<p style="margin-left:0; margin-right:0">在v1.7.0版本中，我们完成了对年份组件和年月组件的支持。通过动态时间设置，用户无需频繁修改时间过滤组件的查询条件，DataEase可以自动更新当天、当月、本周、今年等时间查询条件，简化用户对仪表板的维护工作。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="869" src="https://oscimg.oschina.net/oscnet/up-be56d40870aab6083cd60b0e865e436b073.png" width="1919" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.7.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（数据源）：保存数据源信息时增加重复性校验并提示；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（数据集）：计算字段在保存阶段进行语法校验；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（视图）：AntV视图样式配置项调整；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（系统管理）：新增用户使用默认密码登录时提示修改密码；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（移动端）：移动端布局拖动组件接近上下边界画布可以自动滚动；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（移动端）：移动端过滤组件标题大小跟随PC端设置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（X-Pack）：系统主题操作优化，主题切换和删除无需进入编辑状态，增加创建主题按钮；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（X-Pack）：优化定时报告列表页相关操作，增加展示字段；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor（X-Pack）：优化定时报告线程池；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>refactor：升级PostgreSQL驱动42.2.14至42.2.24。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复分享仪表板后被分享人查看时视图的联动信息失效问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：解决X-Pack菜单重启后偶尔加载不出来的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复函数描述错别字；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复新建视图可能一直Loading的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复创建视图可能导致deadlock的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：明细表默认分页数适配旧版本创建的视图；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复MongoDB视图不支持条件过滤的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复用户和组织列表中新建按钮某些情况会消失的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复AntV图库堆叠折线图线宽设置无效的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复jetty-servlets组件漏洞。</p>
                                        </div>
                                      
</div>
            