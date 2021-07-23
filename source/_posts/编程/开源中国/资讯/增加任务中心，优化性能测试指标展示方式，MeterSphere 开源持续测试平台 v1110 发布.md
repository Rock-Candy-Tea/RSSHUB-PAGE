
---
title: '增加任务中心，优化性能测试指标展示方式，MeterSphere 开源持续测试平台 v1.11.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4ad2769ebe53f0035533d5394f0303a75f7.png'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 11:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4ad2769ebe53f0035533d5394f0303a75f7.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><img alt height="542" src="https://oscimg.oschina.net/oscnet/up-4ad2769ebe53f0035533d5394f0303a75f7.png" width="1352" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">7月22日，MeterSphere一站式开源持续测试平台正式发布v1.11.0版本。</p> 
<p style="text-align:left">在这一版本中我们<span style="color:#783887"><strong>新增了全局性的任务中心功能</strong></span>，执行中的接口、性能测试均会出现在任务中心当中；同时针对性能测试用户提交较多的报告展示问题，v1.11.0版本<span style="color:#783887"><strong>新增了自由选择展示指标的报告展现方式</strong></span>，让性能测试的数据展示变得更加灵活；在MeterSphere的X-Pack功能增强包中我们还<span style="color:#783887"><strong>增加了Kubernetes资源池对接口测试的支持</strong></span>，测试资源池变为了MeterSphere系统的通用执行机。除此之外，v1.11.0版本也包含了自1.10.0版本发布以来到1.10.6所有下版本中的所有更新内容。</p> 
<h2 style="text-align:left">新增功能</h2> 
<p style="text-align:left"><span style="color:#783887"><strong>■ 增加任务中心功能，集中展示运行中的测试任务</strong></span></p> 
<p style="text-align:left">MeterSphere v1.11.0版本在系统右上方增加了任务中心功能入口，同时将原有的“工作空间切换”、“语言切换”等功能进行了样式调整。当用户选择接口测试、性能测试执行时，便会在任务中心中增加相应的任务。用户可以随时打开任务中心查看正在执行中或历史测试任务的状态，并且可以点击某一任务快速跳转到对应任务的报告页面。</p> 
<p style="text-align:left"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-c2d997c1ae17801fe97c04682030b1a0f59.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#783887"><strong>■ 优化性能测试报告指标展示方式</strong></span></p> 
<p style="text-align:left">在性能测试的报告中我们新增了测试详情标签页，在测试详情页面左侧列出了所有可选择的指标条目，用户可以自由选择。选中的指标项会出现在右侧的折线图中，折线图下方支持调整指标范围，图表中显示的指标内容同时会以表格的形式统计在图标下方。</p> 
<p style="text-align:left"><img alt height="1440" src="https://oscimg.oschina.net/oscnet/up-92c4a17cf95222625624ff931d7500758e5.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#783887"><strong>■ 接口测试支持使用Kubernetes类型资源池（X-Pack）</strong></span></p> 
<p style="text-align:left">MeterSphere的测试资源池概念最初设计时是只在性能测试指定资源池执行的。在上个版本，即v1.10.0版本中，我们增加了接口测试指定资源池执行的功能，但只支持了独立节点类型的资源池。在新发布的v1.11.0版本中，Kubernetes类型的资源池也支持执行接口测试了。至此两种类型的测试资源池对于接口测试、性能测试执行均已支持。</p> 
<p style="text-align:left"><img alt="图片" height="1440" src="https://oscimg.oschina.net/oscnet/up-69a9d82336c54e96b6d1d4b53f510f36623.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="图片" height="1440" src="https://oscimg.oschina.net/oscnet/up-22ff959b6034fd5840988b18a148a05b9f2.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="color:#783887"><strong>■ 禅道对接支持GET请求方式</strong></span></p> 
<p style="text-align:left">做过禅道对接的用户可能知道禅道目前存在GET和PATH_INFO两种接口调用方式（即其requestType参数）。在v1.11.0版本中，我们新增了对于GET请求方式的支持，用户可以根据自己使用的禅道系统的配置情况自主选择请求方式。</p> 
<p style="text-align:left"><img alt="图片" height="1440" src="https://oscimg.oschina.net/oscnet/up-a44a0b45704e28aae41c9522f935e1f77ad.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">除了上述提到的新增功能外，MeterSphere v1.11.0版本还包含很多其他功能更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<h2 style="text-align:left">功能优化</h2> 
<p style="text-align:left"><span style="color:#783887">■ </span>测试跟踪：测试用例支持回收站功能；</p> 
<p style="text-align:left"><span style="color:#783887">■ </span>接口测试：增加前后置SQL请求步骤；</p> 
<p style="text-align:left"><span style="color:#783887">■ </span>接口测试：从数据库中提取的数据列表支持循环控制器；</p> 
<p style="text-align:left"><span style="color:#783887">■ </span>接口测试：支持动态展示接口测试执行结果；</p> 
<p style="text-align:left"><span style="color:#783887">■ </span>性能测试：支持批量添加监控对象；</p> 
<p style="text-align:left"><span style="color:#783887">■ </span>系统设置及其他：工作空间项目列表支持点击跳转。</p>
                                        </div>
                                      
</div>
            