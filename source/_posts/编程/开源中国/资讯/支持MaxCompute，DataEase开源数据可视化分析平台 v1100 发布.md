
---
title: '支持MaxCompute，DataEase开源数据可视化分析平台 v1.10.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0c6f4b47d87771c7f4f249e2723da1a67c7.png'
author: 开源中国
comments: false
date: Mon, 09 May 2022 19:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0c6f4b47d87771c7f4f249e2723da1a67c7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="678" src="https://oscimg.oschina.net/oscnet/up-0c6f4b47d87771c7f4f249e2723da1a67c7.png" width="1694" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">5月9日，DataEase开源数据可视化分析平台正式发布v1.10.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，DataEase平台新增了对MaxCompute数据源的支持；仪表板方面，加入了辅助设计网格，同时增加了矩阵密度，让用户在制作仪表板的时候可以更精确、方便地对指定视图或组件进行相关放置；视图方面，优化了更换数据集时字段的自动匹配功能，让用户在更替同结构数据集时无需对视图再次进行编辑。对于所有视图中的指标，我们均加入了去重计数的支持。</p> 
<p style="margin-left:0; margin-right:0">另外，新版DataEase对表格的一些功能做了增强，AntV表格支持设置数据格式，明细表支持下拉及翻页等模式；X-Pack增强功能方面，用户可以对首页及帮助文档进行自定义设置；安装部署方面，DataEase正式实现了对ARM64架构的支持。最后，我们还对其他一些常用的功能进行了功能优化和问题修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#0a7be0">■ 新增MaxCompute数据源支持</span></strong></p> 
<p style="margin-left:0px; margin-right:0px">MaxCompute（ODPS）是适用于数据分析场景的企业级SaaS（Software as a Service）模式云数据仓库，以Serverless架构提供快速、全托管的在线数据仓库服务，消除了传统数据平台在资源扩展性和弹性方面的限制，最小化用户运维投入，使您可以经济并高效地分析处理海量数据。</p> 
<p style="margin-left:0; margin-right:0">在v1.10.0版本中，DataEase新增MaxCompute数据源，用户可以在DataEase中连接阿里云的MaxCompute服务，在DataEase平台上对MaxCompute数据进行展示和分析。</p> 
<p><img alt height="1574" src="https://oscimg.oschina.net/oscnet/up-cd919d99d547f3b62f33fe0ff3a5feb0855.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ AntV表格功能增强</span></strong></p> 
<p style="margin-left:0; margin-right:0">数值格式化对于简洁明了地展示数据有着很大的帮助。例如通过千分符的设置，可以让金融从业人员快速地分辨出数额的大小；通过限定小数位数，可以统一所有数据显示格式等。</p> 
<p style="margin-left:0; margin-right:0">DataEase在v1.10.0版本中优先对AntV表格新增了数值格式的支持，目前支持的格式选项有：数量单位、单位后缀、千分符、小数位数、百分比等。用户可以对需要添加格式的指标字段进行单独的格式设置。</p> 
<p><img alt height="1574" src="https://oscimg.oschina.net/oscnet/up-ff29289d00b3f70be8cab5bef9fec9e18ba.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0a7be0">■ 支持ARM64架构下的安装运行</span></strong></p> 
<p style="margin-left:0; margin-right:0">在国产化的大背景之下，越来越多的用户将ARM架构的服务器作为了底层IT基础设施，社区用户也多次提出需要在ARM架构下运行DataEase的需求。</p> 
<p style="margin-left:0; margin-right:0">从v1.10.0版本开始，DataEase正式增加了对ARM架构的支持，用户可以在“鲲鹏“及“飞腾”等ARM架构服务器上安装并运行DataEase开源数据可视化分析平台。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#0a7be0">■ 自定义首页及帮助文档（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">对于企业用户来说，相比于默认的DataEase标准化首页，更希望自己的企业员工在使用DataEase的时候看到自己按需预置的首页。同样的，每个企业也会有从自身实际情况出发编写定制化帮助文档的需求。</p> 
<p style="margin-left:0; margin-right:0">为了满足上述需求，DataEase从v1.10.0版本开始，在X-Pack增强包中新增了首页链接及帮助文档链接的自定义设置支持，企业用户可以对相关内容进行个性化设置。</p> 
<p><img alt height="1572" src="https://oscimg.oschina.net/oscnet/up-48546abdbe469dea16e2781fcfeb31854de.png" width="2878" referrerpolicy="no-referrer"></p> 
<p>除了上述提到的新增功能外，DataEase v1.10.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span><span> </span>refactor（视图）：优化后文本卡仅支持一个维度；</p> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span><span> </span>refactor（视图）：视图明细导出优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（视图）：优化后视图联动不清除历史联动条件；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板外部参数设置和视图跳转设置中，添加或选中参数时自动启用相应功能；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：复用模板悬浮显示全称；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：仪表板模板导出支持同时导出服务器静态图片；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor（仪表板）：避免事件冲突，仪表板全屏预览状态不显示流媒体控制条；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor（仪表板）：优化流媒体，关闭IO隐藏缓冲区等；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■<span> </span></span>refactor：升级Apache Doris版本 （v0.15→v1.0.0）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0a7be0">■</span><span> </span>refactor：优化后用户修改密码后强制退出。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#0a7be0">■</span><span style="color:#3e3e3e"><span> </span>fix：修复精简模式添加Excel数据集时最多只能添加100条的问题 （#2141）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：修复Excel数据集在单元格中包含特殊符号或空值时会报错的问题（#2138）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：删除数据表中重复的索引（#1864）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：修复同时同步多个数据集时会出现部分数据集数据为空的情况（#2159）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：在任务管理模块中设置定时报告，用户只能看到自己定制的定时报告。（#2065）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：管理员可以对所有定时报告进行删除操作（#2064）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■<span> </span></span>fix：修复文本过滤组件中的搜索框搜到的字段，某些情况下拖拽后显示值不正确的问题（#2037）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：修复了定时任务创建全量任务，执行完成后修改为增量，发现增量不生效的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■</span><span> </span>fix：修复移动端设计时，等待区可能出现空白的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e"><span style="color:#0a7be0">■<span> </span></span>fix：修复移动端使用域名访问报错的问题。</span></p>
                                        </div>
                                      
</div>
            