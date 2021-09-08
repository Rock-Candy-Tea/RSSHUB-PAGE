
---
title: '新增支持两种数据源，DataEase 开源数据可视化分析平台 v1.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eba17a5373bf5223c512e4fd48412e96ef8.png'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 16:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eba17a5373bf5223c512e4fd48412e96ef8.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><img alt height="536" src="https://oscimg.oschina.net/oscnet/up-eba17a5373bf5223c512e4fd48412e96ef8.png" width="1356" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">9月6日，DataEase开源数据可视化分析平台正式发布v1.2.0版本。在该版本中，DataEase新增了对SQL Server和PostgreSQL数据源的支持；视图和仪表板方面，增加了对数据钻取、联动的支持，同时加入了新的视图展示图形（包括中国地图、散点图、气泡图、矩形树图等），丰富了视图展示图形的种类；数据集方面支持新增计算字段，用户可以在原有数据结构的基础上，通过计算公式增加新的统计字段。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="text-align:left">新增功能</h2> 
<p style="text-align:left"><strong><span style="color:#0a7be0">■ 数据源新增支持SQL Server和PostgreSQL</span></strong></p> 
<p style="text-align:left">在DataEase v1.2.0版本中，我们增加了对SQL Server和PostgreSQL数据源的支持。加上之前版本支持的Oracle、MySQL数据源，基本上已经涵盖了市面上主流的关系型数据库。</p> 
<p style="text-align:left"><img alt height="603" src="https://oscimg.oschina.net/oscnet/up-df2d2c1e94a8f63173a6c56ff991a0b4b0c.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><span style="color:#0a7be0">■ 视图展示图形新增支持中国地图、散点图、气泡图、矩形树图等种类</span></strong></p> 
<p style="text-align:left">在DataEase v1.2.0版本中，新增了对中国地图、散点图、气泡图、矩形树图的支持，丰富了视图展示图形的种类。用户可以利用新增的图表类型做出比之前更加丰富的可视化内容。</p> 
<p style="text-align:left"><img alt height="604" src="https://oscimg.oschina.net/oscnet/up-3f14f14fde8d613769b49cd68a670044ab7.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><span style="color:#0a7be0">■ 支持视图联动和钻取</span></strong></p> 
<p style="text-align:left">在DataEase v1.2.0版本中，新增了对视图联动和钻取的支持。通过联动和钻取的设置，用户可以在仪表板上实现数据分析与交互操作。</p> 
<p style="text-align:left"><img alt height="738" src="https://oscimg.oschina.net/oscnet/up-2a4f65ee1cad546550bc445cd6db9545a9e.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">在仪表板中可以为指定视图相关联的视图添加联动设置，当指定视图的维度选择变化时，与之相关联的视图显示数据会随之变化，方便用户进行同步观察。</p> 
<p style="text-align:left"><img alt height="738" src="https://oscimg.oschina.net/oscnet/up-ca9844b85d08217487517d2406846261acb.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">在视图中支持设置图表的钻取维度，支持设置多级钻取维度。用户通过数据钻取，可以让视图按照指定维度或条件进行数据细分呈现，从而让数据范围从一个比较大的面逐步下钻并聚焦到一个小的点上，达到数据分析的效果。</p> 
<p style="text-align:left"><img alt height="738" src="https://oscimg.oschina.net/oscnet/up-60367970b10222d85a9c1db07de9dc26962.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><span style="color:#0a7be0">■ 数据集字段管理新增计算字段</span></strong></p> 
<p style="text-align:left">DataEase v1.2.0在数据集的字段管理中，新增了计算字段的功能。当用户从原有数据字段中无法获取到所需数据时，可以通过基本的四则混合运算公式，或者直接使用DataEase内置的常用函数来生成新的字段，满足业务可视化展示的需求。</p> 
<p style="text-align:left"><img alt height="604" src="https://oscimg.oschina.net/oscnet/up-5287429bc4141052c88e9025bf42ec219df.png" width="1280" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">除了上述提到的新增功能外，DataEase v1.2.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="text-align:left">功能优化</h2> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：优化仪表板元素拖动，大小变动延迟渲染，移动使用原始Dom，优化拖动卡顿现象；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■ </span>refactor（仪表板）：优化仪表板预览模式下鼠标悬浮阴影效果；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：明细弹出样式修改；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：堆叠图优化；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：维度指标色彩区分；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：更换仪表板视图设置组件；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：堆叠项不允许指标拖入；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：图片修改为自适应，不保持宽高比例；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：scatter优化；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：重构仪表板主题设置组件，适配视图样式设置相关变化。</p> 
<h2 style="text-align:left">Bug修复</h2> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复sql注入和xss攻击的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复过滤器多条件异常问题；修复编辑数据集切换到添加数据集界面异常问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复数据集消息获取接受人权限错误的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复外部链接token存储使用vuex不使用cookie的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复外部链接带密码嵌在iframe的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复解析excel失败的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复axios异步执行导致地图切换错误的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复文本列表组件快速检索无效的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复定时查询未读消息条数错误的问题；</p> 
<p style="text-align:left"><span style="color:#0a7be0">■</span> fix：修复仪表板数字范围组件样式错误的问题。</p> 
<p style="text-align:left"><strong><span style="color:#0a7be0">致谢：</span></strong><span style="color:#0a7be0"><span style="color:#3e3e3e">特别感谢网友Mia0a、strawberrybiscuits检测出DataEase存在的SQL注入和XSS攻击漏洞。</span></span></p>
                                        </div>
                                      
</div>
            