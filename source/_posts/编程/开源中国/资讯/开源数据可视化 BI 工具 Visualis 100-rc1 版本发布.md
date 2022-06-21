
---
title: '开源数据可视化 BI 工具 Visualis 1.0.0-rc1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0621/112623_IScF_4252687.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 03:08:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0621/112623_IScF_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:8px; margin-right:8px"><span><strong><span style="color:#0052ff">Visualis简介</span></strong></span></p> 
<p style="margin-left:8px; margin-right:8px"><span>Visualis是一个基于宜信开源项目Davinci开发的数据可视化BI工具。现已集成到一站式数据应用开发门户DataSphere Studio中。Visualis支持拖拽式报表定义、图表联动、钻取、全局筛选、多维分析、实时查询等数据开发探索的分析模式，并提供水印、数据质量校验等金融级增强功能。</span></p> 
<p><span>开源项目地址：<u>https://github.com/WeBankFinTech/Visualis</u></span></p> 
<p><strong><span>本次发布的1.0.0-rc1版本，完成了针对DSS1.0.1和Linkis1.1.1的适配，对接了DSS的结果集可视化分析、工作流报表开发，邮件发送等多个功能，是首个接入DSS1.0和Linkis1.0的版本。</span></strong></p> 
<p><span><span>Visualis支持多种数据图形渲染，在配置相应的数据源，配置不同的指标和维度后，可以开发出不同的数据展示图形，通过仪表盘（DashBoard）或数据大屏</span><span>（Display）绑定Widget制成数据看板。</span></span></p> 
<p><img alt height="286" src="https://static.oschina.net/uploads/space/2022/0621/112623_IScF_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong><span style="color:#0052ff">新特性</span></strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span>[Widget组件] 新增DataWrangler的表格形式</span></p> </li> 
 <li> <p><span>[Source组件] 查询对接presto引擎</span></p> </li> 
</ul> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong><span style="color:#0052ff">特性增强</span></strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:windowtext">[组件优化] 组件只显示最新的当前版</span></p> </li> 
 <li> <p><span style="color:windowtext">[Source组件] 发布后Source不产生版本，Source复用</span></p> </li> 
 <li> <p><span style="color:windowtext">[Source组件] 优化拷贝逻辑，数据源不需要拷贝</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget默认入口改为图标驱动</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget图表驱动-表格尺寸默认改为“小”</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget-编辑器设置-多选拖拽默认值改为“是”</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] 背景设置-背景颜色RGB默认更改，展示默认值改为静态模式</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] 新增DataWrangler的表格形式</span></p> </li> 
 <li> <p><span style="color:windowtext">[View组件] View中特殊语句如refresh table不默认加limit</span></p> </li> 
 <li> <p><span style="color:windowtext">[邮件组件] 邮件发送标题支持去掉时间戳</span></p> </li> 
 <li> <p><span style="color:windowtext">[View组件] 支持快速选择指标的别名为原字段名</span></p> </li> 
 <li> <p><span style="color:windowtext">[后端改造] 后台-JDBC数据源加密改造</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] Display中表格区域放大后，图表需要等比放大</span></p> </li> 
 <li> <p><span style="color:windowtext">[View组件] 只要字段被转换成数值型，即使它实际为String类型，也要支持数值型相关的操作</span></p> </li> 
 <li> <p><span style="color:windowtext">[DSS工作流] 节点中“菜单内容”选择Visualis，下方弹出的组件发生变化</span></p> </li> 
 <li> <p><span style="color:windowtext">[邮件组件] 邮件标题日期，支持引用linkis的内置变量</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] Display打开后默认缩放比例不要5%，最好100%</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] 折线图、柱状图等坐标轴支持调整读数方式（如10,0000/100K等）</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] 折线图、柱状图的数据标签，支持调整显示密度</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] 双Y轴图，左右两边的轴的取值范围支持调成不一样</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget开启多选时，从字段拖拽到指标/维度栏后，顺序应当与之前保持一致</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget字段列表的展示顺序应当与上游结果集的顺序一致</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget配置中允切换择查询引擎</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] 背景设置-背景颜色RGB默认更改，展示默认值改为"静态模式"</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget-编辑器设置-多选拖拽默认值改为"是"</span></p> </li> 
</ul> 
<h2 style="margin-left:8px; margin-right:8px; text-align:left"><span><strong><span style="color:#0052ff">Bug修复</span></strong></span></h2> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span><span style="color:windowtext">[Widget组件] widget节点更新时间优化</span></span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget执行发布后，配置绑定失败</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] 当Widget执行失败时工作流应该立即结束</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget中“分类型/数值型”的字段顺序应与上游暂存表顺序一致</span></p> </li> 
 <li> <p><span><span style="color:windowtext">[View组件] 取消View节点为非绑定CS表功能</span></span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] Widget执行发布后，配置绑定失效</span></p> </li> 
 <li> <p><span style="color:windowtext">[Widget组件] 多个Widget绑定一个Display时，工作流执行失败问题</span></p> </li> 
 <li> <p><span style="color:windowtext">[DashBoard组件] 点击DashBoard的数据同步按钮报错</span></p> </li> 
 <li> <p><span style="color:windowtext">[Display组件] 点击删除Display按钮失效</span></p> </li> 
</ul> 
<div style="margin-left:0; margin-right:0; text-align:left"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0"> 
    <div style="margin-left:0; margin-right:0"> 
     <p><strong style="color:rgba(0, 0, 0, 0.9)">WeDataSphere</strong></p> 
     <p>微众银行自研打造的WeDataSphere——微数域，是一套金融级、全连通、一站式、开源开放的大数据平台套件，正在Github上逐步开源中。</p> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            