
---
title: 'datart 1.0.0-beta.0 发布，TypeScript 实现的数据可视化平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b3ea5978b9931820b965cb44b16dfc07ca8.png'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 07:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b3ea5978b9931820b965cb44b16dfc07ca8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>datart 1.0.0 首个 Beta 测试版已发布。</p> 
<p>据介绍，datart 由原 <a href="https://www.oschina.net/p/davinci" target="_blank">davinci </a>主创团队出品，是新一代数据可视化开放平台，支持各类企业数据可视化场景需求，如创建和使用报表、仪表板和大屏，进行可视化数据分析，构建可视化数据应用等。</p> 
<p><img alt="up-b3ea5978b9931820b965cb44b16dfc07ca8.png" src="https://oscimg.oschina.net/oscnet/up-b3ea5978b9931820b965cb44b16dfc07ca8.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Freleases%2Ftag%2F1.0.0-beta.0" target="_blank">发布说明显示</a>，本次升级有数据库结构变更，需要执行数据库升级补丁。升级补丁为<span> </span><code>/bin/migrations/migration.1.0.0-beta.0.sql</code></p> 
<h3 style="text-align:start">Break changes</h3> 
<p style="color:#24292f; text-align:start"><strong>本次升级有以下不兼容变更：</strong></p> 
<ul> 
 <li>删除了分组表</li> 
 <li>表格（明细表）的样式配置发生了一些变更</li> 
</ul> 
<p style="color:#24292f; text-align:start">以上变更会导致之前配置完成的分组表不可用，表格样式有所改变；需要手动重新配置；<strong>用于生产的用户请不要直接升级</strong>。</p> 
<h3 style="text-align:start">Release Notes</h3> 
<ul> 
 <li style="text-align:start">支持了英文国际化</li> 
 <li style="text-align:start">新增了透视表图表<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F336" target="_blank">#336</a></li> 
 <li style="text-align:start">重构了表格（明细表）</li> 
 <li>支持了列条件样式配置</li> 
 <li>支持了指标列数据汇总</li> 
 <li>优化了样式配置</li> 
 <li style="text-align:start">新增了富文本图表<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F363" target="_blank">#363</a></li> 
 <li style="text-align:start">支持了在图表编辑时配置是否进行数据聚合；在图表编辑器右上角扩展按钮中进行配置，用于适配多维数据源和加工完成的原始数据<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F477" target="_blank">#477</a></li> 
 <li style="text-align:start">支持了图表编辑时多选拖拽字段：</li> 
 <li>可以按住<span> </span><code>Cmd(Mac)</code><span> </span>/<span> </span><code>Ctrl(Windows)</code><span> </span>键批量选择字段</li> 
 <li>也可以在选择首字段之后，按住<span> </span><code>shift</code><span> </span>键选择尾部字段，这样中间的所有字段都会被选中</li> 
 <li style="text-align:start">支持定时任务发送 Excel</li> 
 <li style="text-align:start">优化了仪表板控制器的一系列功能</li> 
 <li>支持了级联配置<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F345" target="_blank">#345</a></li> 
 <li>新增了复选框控制器<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F348" target="_blank">#348</a></li> 
 <li style="text-align:start">优化了仪表板的联动和跳转功能</li> 
 <li>支持了跳转到指定 URL<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F333" target="_blank">#333</a></li> 
 <li>支持了表格作为的联动和跳转触发器</li> 
 <li style="text-align:start">优化了颜色选择器，支持在图表颜色配置中选择主题进行快捷配色<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F433" target="_blank">#433</a></li> 
 <li style="text-align:start">添加了建议部署文档，优化了部署脚本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F359" target="_blank">#359</a></li> 
 <li style="text-align:start">优化了仪表板图片组件的交互<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F452" target="_blank">#452</a></li> 
 <li style="text-align:start">优化了饼图标签和提示信息的显示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F456" target="_blank">#456</a></li> 
 <li style="text-align:start">优化了数据视图中数据库表显示顺序<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F55" target="_blank">#55</a></li> 
 <li style="text-align:start">优化了数据视图中数据库信息搜索的显示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F131" target="_blank">#131</a></li> 
 <li style="text-align:start">优化了仪表板组件错误提示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F463" target="_blank">#463</a></li> 
 <li style="text-align:start">优化了错误提示名称重复的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F34" target="_blank">#34</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F482" target="_blank">#482</a></li> 
 <li style="text-align:start">修复了总行数不生效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F241" target="_blank">#241</a></li> 
 <li style="text-align:start">修复了变量重名判断不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F418" target="_blank">#418</a></li> 
 <li style="text-align:start">修复了图表筛选中相对日期不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F424" target="_blank">#424</a></li> 
 <li style="text-align:start">修复了翻牌器显示不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F329" target="_blank">#329</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F402" target="_blank">#402</a></li> 
 <li style="text-align:start">修复了图表编辑数据栏中字段不能拖拽改变位置的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F346" target="_blank">#346</a></li> 
 <li style="text-align:start">修复了漏斗图多指标时显示不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F394" target="_blank">#394</a></li> 
 <li style="text-align:start"><span>修</span>复了地图提示信息显示不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F442" target="_blank">#442</a></li> 
 <li style="text-align:start">修复了日期型变量格式化不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F373" target="_blank">#373</a></li> 
 <li style="text-align:start">修复了控制器自定义默认值设置无效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F368" target="_blank">#368</a></li> 
 <li style="text-align:start">修复了容器组件自动加载的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F339" target="_blank">#339</a></li> 
 <li style="text-align:start">修复了邮箱格式验证的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F370" target="_blank">#370</a></li> 
 <li style="text-align:start">修复了权限分配不正确的一系列问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F342" target="_blank">#342</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F353" target="_blank">#353</a></li> 
 <li style="text-align:start">修复了 SQL 语法解析的一系列问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F416" target="_blank">#416</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F414" target="_blank">#414</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fpull%2F475" target="_blank">#475</a></li> 
 <li style="text-align:start">修复了点击 logo 时闪烁 404 页面的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F23" target="_blank">#23</a></li> 
 <li style="text-align:start">修复了 SQL 编辑时提示信息重复的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Fissues%2F224" target="_blank">#224</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frunning-elephant%2Fdatart%2Freleases%2Ftag%2F1.0.0-beta.0" target="_blank">详情点此查看</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            