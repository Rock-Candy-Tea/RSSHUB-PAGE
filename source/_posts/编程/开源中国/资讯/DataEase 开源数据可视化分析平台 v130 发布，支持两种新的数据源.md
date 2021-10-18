
---
title: 'DataEase 开源数据可视化分析平台 v1.3.0 发布，支持两种新的数据源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f684c04cc75b1e779350986bb7e851149f3.png'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 15:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f684c04cc75b1e779350986bb7e851149f3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="540" src="https://oscimg.oschina.net/oscnet/up-f684c04cc75b1e779350986bb7e851149f3.png" width="1356" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">10月18日，DataEase开源数据可视化分析平台正式发布v1.3.0版本。在该版本中，新增了对Elasticsearch和ClickHouse数据源的支持；视图方面增加了对组合图、水波图、明细表等新的视图展示图形的支持；仪表板方面，对仪表板的制作进行了大量的优化，支持组件自动吸附对齐、支持画布的自适应、支持组件的碰撞检测及挤压排列效果。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新增功能</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#0a7be0">■ 数据源新增支持Elasticsearch和ClickHouse</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在DataEase v1.3.0版本中，我们增加了对Elasticsearch和ClickHouse数据源的支持，以作为对市面上主流关系型数据库支持的补充。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="705" src="https://oscimg.oschina.net/oscnet/up-bed15ddbdfb8643ac5d4aec6354b6acdf53.png" width="1500" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#0a7be0">■ 视图展示图形新增支持组合图、水波图、明细表等种类</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在DataEase v1.3.0版本中，新增了对组合图、水波图、明细表的支持，丰富了视图展示图形的种类。用户可以利用新增的图表类型做出比之前更加丰富的可视化内容。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="763" src="https://oscimg.oschina.net/oscnet/up-0f6f8f7db38bf386482220e3af09a7a3c0e.png" width="1500" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="763" src="https://oscimg.oschina.net/oscnet/up-1acd7e81f17639867e9cac8bb1a7ce7c20d.png" width="1500" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#0a7be0">■ 仪表板制作功能增强</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">DataEase v1.3.0版本中，仪表板新增了组件自动吸附对齐、组件悬浮模式、组件碰撞挤压排列、画布自适应等多种新特性，简化了用户在制作仪表板时的布局操作。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="802" src="https://oscimg.oschina.net/oscnet/up-33b6cae678e00a3e27b2ae1dbbe21e7028f.png" width="1700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#0a7be0">■ 仪表板支持导出PDF</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">DataEase v1.3.0新增了对仪表板导出功能的支持。用户可以选择需要导出的仪表板，以PDF形式保存到本地。在导出PDF的同时，也可以给导出的内容添加相应的描述内容，完善导出仪表板的信息。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="717" src="https://oscimg.oschina.net/oscnet/up-5a7b5c9190cff4af94cd0de02ceae17ae0f.png" width="1450" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了上述提到的新增功能外，DataEase v1.3.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能优化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（数据源）：校验数据源状态时，同时刷新左侧菜单中数据源的状态；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（数据集）：增加自定义数据集字段校验；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（数据集）：字段编辑增加引用字段和引用函数说明；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：饼图、气泡图、矩形树图优化；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：折线面积优化；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：仪表板编辑时，文字组件、矩形组件、过滤组件样式设置面板强制在画布区域内；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：仪表板视图改变大矩阵式设计预判视图实际尺寸大小；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：仪表板矩形、文字组件、间隙等默认样式调整；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor（系统管理）：用户列表高级搜索优化；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> refactor：完善SQL注入拦截器。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Bug修复</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复仪表板多个地图Resize错误的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复Oracle时间转换问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复仪表板重做按钮不生效的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复全屏模式下输入框输入内容自动退出的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复过滤时间类型字段可能出错的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复视图更换数据集可能导致联动失效的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复全屏状态编辑仪表板时，预览仪表板再退出视图错位的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复两个表多字段关联后，创建自定义数据集出错的问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复SQL Server 2008分页问题；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0a7be0">■</span> fix：修复创建MySQL数据源时出现“Public Key Retrieval is not allowed”错误的问题。</p>
                                        </div>
                                      
</div>
            