
---
title: '新增 API 数据源支持，支持透视表组件，DataEase 开源数据可视化分析平台 v1.8.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2a100447be244680f832e0856aad5bb6684.png'
author: 开源中国
comments: false
date: Tue, 08 Mar 2022 14:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2a100447be244680f832e0856aad5bb6684.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="674" src="https://oscimg.oschina.net/oscnet/up-2a100447be244680f832e0856aad5bb6684.png" width="1694" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">3月3日，DataEase开源数据可视化分析平台正式发布v1.8.0版本。在该版本中，DataEase平台新增了对API数据源的支持；仪表板方面，将之前版本的视图菜单和仪表板菜单进行了合并，视图的相关操作纳入仪表板内；视图方面，除了新增基于AntV S2开发的透视表外，还基于DataEase插件体系开发了气泡地图插件；X-Pack功能方面，新增按资源维度对相关权限进行管理的功能。另外，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 新增API数据源支持</span></strong></p> 
<p style="margin-left:0; margin-right:0">日常的工作生活中，越来越多的系统或平台在为用户提供访问界面的同时，也以API的形式提供了数据的相关操作接口，其中就包括数据的查询，系统或平台可以将处理后的数据通过API接口返回给用户。</p> 
<p style="margin-left:0; margin-right:0">在v1.8.0版本中，DataEase新增API数据源，用户可以添加API数据相关的请求参数，由DataEase定时同步到系统中进行展示和分析。</p> 
<p><img alt height="659" src="https://oscimg.oschina.net/oscnet/up-7bb4dcf7c737608073571c20aa68ec09bd5.png" width="1400" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 新增透视表</span></strong></p> 
<p style="margin-left:0; margin-right:0">在v1.8.0版本之前，DataEase提供了基础的明细表和汇总表。这两个表格组件只能比较简单地罗列和展示指定的数据，不能根据用户的需求对表格数据进行分组、多维度分析等操作。</p> 
<p style="margin-left:0; margin-right:0">DataEase v1.8.0版本基于AntV S2开发了全新的透视表组件。用户可以通过简单的拖拽操作，轻松地改变表格数据展示的行列维度，对数据进行全方位、多角度、动态的分析和展示。</p> 
<p><img alt height="707" src="https://oscimg.oschina.net/oscnet/up-cdb0626345dc316338e790e59fae2720b15.png" width="1500" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 新增按资源配置权限功能（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在v1.8.0版本之前，管理员可以在DataEase上按用户维度去选定一个组织、角色或用户，并给该选定项进行各类资源的集中授权，但如果遇到给特定的新增资源进行用户授权的情况，操作起来就比较繁琐。</p> 
<p style="margin-left:0; margin-right:0">在v1.8.0版本中，新增了按资源配置权限的功能，管理员可以通过选定指定资源，批量给所需授权的组织、角色或用户进行权限管理，大大简化了相关操作。</p> 
<p><img alt height="707" src="https://oscimg.oschina.net/oscnet/up-9ec5e330278b2a5f9106647b0be534ed23f.png" width="1500" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.8.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（数据集）：数据集预览优化，去掉每页条数及翻页操作，支持以滚动方式查看更多数据；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor（视图）：视图已引用的字段在数据集中变动后的校验提示；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（视图）：优化S2汇总表及明细表，支持下钻、联动、跳转（#1075）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板加载代码优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor（仪表板）：优化仪表板分享给“我的菜单”下目录显示，调整为显示用户名而不是用户ID；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（移动端）：移动端焦点模块图标颜色调整；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（移动端）：优化移动端仪表板详情，外层布局适应多浏览器；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>style（移动端）：优化移动端搜索框样式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor：升级FastJson至1.2.79（#1820，感谢开源网安提供的扫描服务）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor：升Guava至31.0.1-jre（#1820，感谢开源网安提供的扫描服务）。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复API调用存在的权限控制问题（#1618，感谢社区用户espduino的反馈）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复XML外部实体注入漏洞（#1820，感谢开源网安提供的扫描服务）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复MongoDB常量里使用了Oracle的别名后缀问题 （#1746，感谢社区用户littleSaltZz的代码贡献）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复Elasticsearch数据源类型为nested的内嵌对象无法使用的问题（#1754）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复MongoDB拉取不到最新的collection的问题（#1767）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复MongoDB校验错误（#1744，#1745）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复安装脚本quick_start.sh网络连接失败处理逻辑的问题（#1794）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复添加DB2 SQL数据集定时同步任务，脚本内有函数时同步任务会报错的问题（#1805）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span> fix：修复Elasticsearch数据集时间格式的问题（#1721）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■ </span>fix：修复筛选器无法控制Tab组件中视图的问题（#1753）。</p>
                                        </div>
                                      
</div>
            