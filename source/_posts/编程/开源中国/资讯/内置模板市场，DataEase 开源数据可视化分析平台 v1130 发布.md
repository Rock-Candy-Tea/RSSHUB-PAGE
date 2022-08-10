
---
title: '内置模板市场，DataEase 开源数据可视化分析平台 v1.13.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-582941f921d2bc84e1b6268e07358660c4f.png'
author: 开源中国
comments: false
date: Wed, 10 Aug 2022 13:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-582941f921d2bc84e1b6268e07358660c4f.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="538" src="https://oscimg.oschina.net/oscnet/up-582941f921d2bc84e1b6268e07358660c4f.png" width="1358" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">8月8日，DataEase开源数据可视化分析平台正式发布v1.13.0版本。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在这一版本中，DataEase平台新增“模板市场”模块，用户可以直接在模板市场中选择合适的模板进行仪表板创建；数据源支持方面，DataEase平台基于MongoDB BI Connector对MongoDB数据源做了全新的支持，解决了一些JDBC（Java Database Connectivity，Java数据库连接）无法处理的问题；API数据源支持以选择的方式组合多层级中的字段，操作起来更加便捷；视图方面，AntV图库支持了数值格式化，并新增了标题的备注功能，AntV表格支持阈值设置，新增世界地图支持，并可以对地图进行自定义设置。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">X-Pack增强功能方面，DataEase对用户管理、角色管理、组织管理、权限管理等模块进行了UI交互的优化与调整，重构了行列权限功能，支持白名单设置，支持查看指定用户的最终权限等。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">最后，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h1 style="margin-left:1.8em; margin-right:.63em; text-align:left">新增功能</h1> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"><strong>■ 模板市场：内置“模板市场”板块，可直接创建仪表板</strong></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">DataEase 在v1.13.0版本中内置了模板市场模块，用户可以在系统内直接预览DataEase官方在线模板，也可以在模板市场中选择合适的模板直接创建对应的仪表板。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:center"><img align="left" src="https://p8.itc.cn/q_70/images01/20220810/0990e93eee4a4e2ca4d8a6493cce377c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">截至2022年8月4日，DataEase模板市场上的精品数据大屏模板已达到28个。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"><strong>■ 数据源：API数据源支持以选择的方式组合多层级中的字段</strong></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在DataEase v1.13.0版本之前，API数据源在添加数据表时，需要用户自己编写JsonPath路径，且在一个数据表内只能指向同一层级的字段。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在新版本中，DataEase API数据源会将返回数据的数据结构展示出来，让用户以勾选的方式组合数据结构中多个不同层级的字段，最终构建出一个数据表。在选择字段的同时，还会给出数据的预览效果，极大地降低了用户的使用门槛，操作起来更加便捷准确。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:center"><img align="left" src="https://p7.itc.cn/q_70/images01/20220810/22fa5c9fae5348d7beb98a1c3d731563.png" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"><strong>■ 视图：新增世界地图支持，可自定义进行地图设置</strong></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在以往版本的DataEase中，仅支持了中国的省、市、区三个级别的地图。社区用户反馈较多的世界地图需求在DataEase v1.13.0版本中得到支持。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在v1.13.0版本中，DataEase将地图设置解耦，用户可以在地图设置中按需添加国家，或者更细粒度的县、乡级别的地图，满足用户个性化的地图展示需求。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:center"><img align="left" src="https://p8.itc.cn/q_70/images01/20220810/98132f108e994b17ad801e4e4f3d7053.png" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"><strong>■ 视图：AntV图库支持标题备注功能</strong></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">图形化是数据直观的展现形式，文字可以对数据进行更进一步的解读。在DataEase v1.13.0版本中，我们对AntV图库的所有视图标题均增加了备注功能，用户可以在备注信息中加上自己对数据的补充说明，以便更加准确地表述数据的真实意义。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:center"><img align="left" src="https://p9.itc.cn/q_70/images01/20220810/dd244be170fc46b78cf798e6d6a43e91.png" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"><strong>■ X-Pack增强包：行权限支持复杂规则设置</strong></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">v1.13.0版本之前的DataEase中，用户添加多字段的行权限只能创建多条行权限规则，而且每条行权限规则中的逻辑关系只能支持一种。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">在v1.13.0版本中，DataEase重构了行权限设置的功能。在一条行权限规则中，对一个授权对象可以进行多字段多关系的定义，极大地简化了行权限规则的使用和管理。</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:center"><img align="left" src="https://p1.itc.cn/q_70/images01/20220810/f4d9cb0aa64647c9a98dfd651e4f78df.png" referrerpolicy="no-referrer"></p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left"> </p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">除了上述提到的新增功能外，DataEase v1.13.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h1 style="margin-left:1.8em; margin-right:.63em; text-align:left">功能优化</h1> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（仪表板）：仪表板背景支持直接重新上传；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（仪表板）：优化仪表板编辑按钮显示位置，优先在组件外侧显示，且可以左右位置自适应改变；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（仪表板）：仪表板预览界面增加仪表板信息弹出提示；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（仪表板）：日期过滤组件增加时分级别支持；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（视图）：自定义地图文件与系统地图文件解耦；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（视图）：下钻后延续第一层的排序规则（仅对升降序有效）；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（视图）：小数精度从2位提升至8位；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（系统管理）：优化用户管理，增加手机号前缀字段；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor（系统管理）：新增用户时自动过滤账号开头结尾的空字符串；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:left">■ refactor：菜单增加复合权限校验，防止用户访问无权限页面。</p> 
<h1 style="margin-left:1.8em; margin-right:.63em; text-align:left">Bug修复</h1> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（系统管理）：修复定时报告发送邮件附件名称过长导致展示错误的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（视图）：修复ECharts图库中，“仪表盘”视图标签内容格式编辑时项目重复的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（视图）：修复透视表指标类表头字体大小不改变的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（数据源）：修复同步Oracle数据库数据出错的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（视图）：修复批量设置ECharts时提示背景未生效的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（数据集）：修复删除定时同步任务后，该数据集仍无法执行同步的问题（#2678）；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（视图）：禁用ECharts地图提示触发位置；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（系统管理）：修复系统管理员不能创建用户模板分类的问题 （#2771）；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（仪表板）：修复下拉框模糊搜索逻辑错误的问题；</p> 
<p style="color:#191919; margin-left:1.8em; margin-right:.63em; text-align:justify">■ fix（视图）：修复计算字段下钻异常的问题。</p>
                                        </div>
                                      
</div>
            