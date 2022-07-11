
---
title: '支持达梦数据源，DataEase 开源数据可视化分析平台 v1.12.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/d6b5eb942ace4411995b6ceac8c76266?from=pc'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 05:18:00 GMT
thumbnail: 'https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/d6b5eb942ace4411995b6ceac8c76266?from=pc'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:justify">
 <img alt="支持达梦数据源，DataEase开源数据可视化分析平台v1.12.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/d6b5eb942ace4411995b6ceac8c76266?from=pc" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
  
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">7月11日，DataEase开源数据可视化分析平台正式发布v1.12.0版本。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在这一版本中，数据源支持方面，DataEase平台新增对达梦数据库的支持；仪表板方面，DataEase对基础操作区和仪表板配置区进行了大量的布局优化，增加了对更多仪表板样式属性的支持，用户能够更方便地对视图、过滤组件等进行批量的统一设置；视图方面，新增视图级别计算字段支持，用户可以在此计算字段中使用聚合函数，满足更多数据处理需求；X-Pack增强功能方面，增加了对CAS（Central Authentication Service，中央认证服务）的支持，企业用户可以通过配置CAS来实现企业内部系统的单点登录。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">最后，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">新增功能</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ 数据源：支持达梦数据库数据源</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">达梦数据库管理系统是达梦公司推出的具有完全自主知识产权的高性能数据库管理系统，产品简称为DM。最新的DM8版本数据库采用了全新的体系架构，在保证大型通用的基础上，针对可靠性、高性能、海量数据处理和安全性等方面做了大量的研发和改进工作，极大地提升了达梦数据库产品的性能、可靠性和可扩展性。在国产化浪潮的驱动下，达梦数据库在国产数据库中扮演着越来越重要的角色。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在v1.12.0版本中，DataEase新增对达梦数据库（DM8）数据源的支持。用户可以将达梦数据库的相关连接信息加入到DataEase中，在DataEase平台对达梦数据库中的数据进行展示和分析。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img alt="支持达梦数据源，DataEase开源数据可视化分析平台v1.12.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/4ffe005e26b04fd5a261b5a6c6927977?from=pc" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <strong><span style="color:#0a7be0">■ 数据集：直连模式下SQL数据集支持设置查询参数</span></strong>
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在DataEase v1.12.0版本之前，数据的查询条件都是通过过滤组件或者视图的过滤条件来进行外查询的，需要先将全部数据查询出来后再进行筛选，在数据量较大的情况下容易引起卡顿。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">DataEase v1.12.0版本在直连模式下新增对SQL数据集设置查询参数的支持，用户可以在定义SQL数据集的语句中设置查询参数，过滤组件在使用时会将参数值带入内查询中，进行数据的筛选，从而减少筛选的数据量，提升查询效率。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img alt="支持达梦数据源，DataEase开源数据可视化分析平台v1.12.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/981041987fc04679a5c3b661030df0c2?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ 视图：支持视图级别计算字段</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在以往版本的DataEase中，计算字段是隶属于数据集下的，对于计算字段的操作会影响到整个数据集，从而影响到所有基于该数据集制作的视图。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">DataEase v1.12.0版本中，将计算字段分为两个作用域，原来的计算字段归为数据集级别，新增视图级别计算字段的支持。在视图级别的计算字段中，支持AVG、SUM、COUNT、MIN、MAX等聚合函数，可以适用于更多的数据处理场景。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img alt="支持达梦数据源，DataEase开源数据可视化分析平台v1.12.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/aebe1bac6910423bba2dff5a2daba96d?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#0a7be0">■ X-Pack增强包：CAS单点登录支持</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">CAS（Central Authentication Service，中央认证服务）是耶鲁大学发起的一个企业级的开源项目，旨在为Web应用系统提供一种可靠的单点登录解决方法（属于Web SSO范畴）。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在DataEase v1.12.0版本中，新增对Apereo CAS的支持，企业用户可以通过配置CAS来实现企业内部系统的单点登录。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img alt="支持达梦数据源，DataEase开源数据可视化分析平台v1.12.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/8786f0d344994c37b95211a2a702221f?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">除了上述提到的新增功能外，DataEase v1.12.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">功能优化</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（数据集）：优化数据集数据预览页面的请求数据策略；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板主题优化，支持主题色切换；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：主题控制适配所有的过滤组件；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板基础操作区操作布局优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板配置区操作布局优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板图标、字体、布局等样式调整；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：视图明细查看拆分为明细数据查看和图片查看；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：过滤组件禁止同数据集同时绑定多个字段；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：视图重置增加提示（#2426）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>perf（仪表板）：优化了使用虚拟DOM优化过滤组件数据量大的情况下出现卡顿的问题。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">Bug修复</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：数据集预览和更新时增加数据源权限校验，防止使用无权限数据源执行SQL的问题（#2430）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：插件操作加入权限控制，解决了普通用户或者API能越权上传、卸载插件的问题（#2429，#2431）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：修复了驱动管理引入的任意文件写入漏洞（#2428）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：升级Apache Doris组件至最新版本，解决了Fastjson的漏洞问题；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：移除Spring Security依赖，修复存在的认证漏洞（#2517）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：处理MySQL数据库表名称含有小数点的情况（#2457）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：修复过滤组件删除默认选项后保存无效的问题；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：修复地图看板的按钮始终在最上层的问题；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：修复移动端画布重置功能不能完全重置数据的问题；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#0a7be0">■</span><span> </span>fix：修复文本转数值后做维度的排序问题。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">特别鸣谢</h1> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:justify">感谢NOP Team向DataEase开源社区及时反馈一系列漏洞。</p>
                                        </div>
                                      
</div>
            