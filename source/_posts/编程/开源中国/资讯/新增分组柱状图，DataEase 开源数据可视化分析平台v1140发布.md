
---
title: '新增分组柱状图，DataEase 开源数据可视化分析平台v1.14.0发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/576be1f09e084e89b935b734a9afe01b~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=nV3puQ28ClHEaJ5ygdB0buxp1AM%3D'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 15:38:00 GMT
thumbnail: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/576be1f09e084e89b935b734a9afe01b~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=nV3puQ28ClHEaJ5ygdB0buxp1AM%3D'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/576be1f09e084e89b935b734a9afe01b~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=nV3puQ28ClHEaJ5ygdB0buxp1AM%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">9月5日，DataEase开源数据可视化分析平台正式发布v1.14.0版本。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在这一版本中，DataEase首页设计全新升级，用户可以在首页上更直观地查看到快速入门、在线文档、教学视频等信息；数据集方面，SQL数据集参数化支持子查询，并且对查询SQL的传输进行了相应的加密处理；视图方面，AntV图库新增分组柱状图、基础面积图、富文本视图等新视图类型，用户在进行数据可视化展示的时候有了更多选择。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">X-Pack增强功能方面，DataEase新增对登录页页脚设置的支持，用户可以在页脚添加备案信息、版权声明等个性化信息；同时，X-Pack增强功能包还新增批量导入用户的功能，用户可以通过Excel对存量用户进行批量导入。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">最后，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">新增功能</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ 首页：全新设计，信息展示更直观</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">v1.14.0版本的DataEase上线了新版的“首页”板块。在新版本的首页中，用户可以在首页上更直观地查看到快速入门、在线文档、教学视频等信息。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/91d97ffc153a4ca1a918a3087692accf~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=myYSNe%2BGh%2FyQZtbaxu8jxX9r5uo%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ 视图：新增分组柱状图、基础面积图、富文本视图</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在DataEase v1.14.0版本中，AntV图库新增分组柱状图、基础面积图、富文本视图等新视图类型，用户在进行数据可视化展示的时候有了更多的选择，可以通过更丰富多样的形式对数据进行展示。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/cdbbaecdf042481ca4eb2565a56601aa~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=WRQWvNdGiQ9eMqsO8bSR0Xi1DJI%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ X-Pack增强包：支持批量导入用户，登录页面支持页脚设置</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">v1.14.0版本之前，DataEase已经提供了LDAP、OIDC、CAS等多种用户登录认证方式的接入，但有些用户可能并没有采纳这些认证方式。当有大量用户需要创建时，管理员的工作量会比较大。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在v1.14.0版本中，DataEase增加了批量导入用户的功能。管理员可以收集用户相关信息，或者从其他已有系统中导出用户信息列表，按照DataEase要求的格式录入到Excel模板中，然后在“用户管理”页面选择“批量导入”即可，极大地减少了用户的创建工作。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/832faf3efe194d3ead426808b68201e8~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=hVPrM%2FCoHA1QLEROyQRAIMG5R4o%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">同时，DataEase v1.14.0版本支持登录页页脚个性化设置。当有备案信息标注或者版权声明的需求时，用户可以在“页脚设置”中按照自己的需要设置相应的显示内容。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/291493ec03e643edaa158fe3fd11b5e5~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663054516&x-signature=f7H82s8JNr%2FSUc52K59vXmUKCQA%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">除了上述提到的新增功能外，DataEase v1.14.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">功能优化</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：视图编辑按钮区对没有点击事件的视图，隐藏跳转设置和联动设置选项；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：导出视图明细Excel时，数值类型按照原格式进行导出（#2811）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：日期范围组件允许选择同一天；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：时间组件默认值格式调整；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（视图）：ECharts去掉不用的内容格式设置项；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（系统管理）：插件管理交互优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（系统管理）：站内消息交互优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■<span> </span></span>refactor（系统管理）：数据同步交互优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■<span> </span></span>refactor（X-Pack）：系统配置交互优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■<span> </span></span>refactor（X-Pack）：定时报告交互优化。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">Bug修复</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span style="color:#3e3e3e"><span> </span>fix（数据源）：修复API数据表对空值字段的处理问题（#2845）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix（仪表板）：修复下拉树过滤器在某些情况下无法过滤数据的问题（#2916，#2922）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span><span style="color:#3e3e3e">fix（仪表板）：修复下拉树在全屏预览状态下无法输入的问题（#2788）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span style="color:#3e3e3e"><span> </span>fix（仪表板）：修复数字范围过滤组件标题样式的问题（#2851）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix（仪表板）：修复明细表翻页后跳转获取的参数不准确的问题（#2846）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix（仪表板）：修复视图放大时自有背景丢失的问题（#2908）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■<span> </span></span>fix（仪表板）：修复ClickHouse数据源不能使用时间过滤器的问题（#2270，#2956）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix（视图）：支持副轴字体大小自动跟随仪表板缩放，修复相同字体大小主副轴实际显示大小不同的问题（#2911）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix（视图）：修复瀑布图维度字段为时间格式时不显示合计的问题（#2881）；</p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><span style="color:#0a7be0">■<span> </span></span>fix：修复CSS中不再支持的样式深度选择符号“>>>”导致命令行报错的问题（#2806，感谢社区用户Dovahkinn的贡献）。</p>
                                        </div>
                                      
</div>
            