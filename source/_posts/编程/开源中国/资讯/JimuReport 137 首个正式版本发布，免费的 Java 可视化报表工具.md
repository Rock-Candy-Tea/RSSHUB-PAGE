
---
title: 'JimuReport 1.3.7 首个正式版本发布，免费的 Java 可视化报表工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 02:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p>积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！！！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.3.7 | 2021-08-02</p> 
<p>集成依赖</p> 
<pre style="text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>spring-boot-starter-jimureport<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.3.7<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="text-align:left">增量SQL</p> 
<pre style="text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_param`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`widget_type`</span> varchar(50) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询控件类型'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`search_flag`</span>,
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`search_mode`</span> int(1) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询模式1简单2范围'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`widget_type`</span>,
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`dict_code`</span> varchar(255) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'字典'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`search_mode`</span>;
</code></pre> 
<p>#升级日志</p> 
<p>重点新功能</p> 
<ul> 
 <li>工具栏支持隐藏自定义设置</li> 
 <li>加入表达式引擎，支持复杂表达式</li> 
 <li>数据库兼容优化，支持含国产等14种数据库</li> 
 <li>sql解析优化</li> 
 <li>支持双击复制文本</li> 
 <li>换行自适应高度</li> 
 <li>报表设计时行高列宽无法定量化设置</li> 
 <li>补空白行功能</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>JSON文本导致报表数据解析异常问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3Y8Y9">issues/I3Y8Y9</a></li> 
 <li>希望报表内容能支持选择复制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F355" target="_blank">#355</a></li> 
 <li>字段内容过长设置自动换行后行高不能自动适应 <a href="https://gitee.com/jeecg/JimuReport/issues/I3Y6PZ">issues/I3Y6PZ</a></li> 
 <li>单类别的图表修改颜色后无法保存 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F361" target="_blank">#361</a></li> 
 <li>传参报表 下拉框可选项 多于实际内容 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F326" target="_blank">#326</a></li> 
 <li>带换行符的文本显示问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3Y36C">issues/I3Y36C</a></li> 
 <li>导出Excel 的时候报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F362" target="_blank">#362</a></li> 
 <li>查询时回车,会刷新页面,而不是返回查询结果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F374" target="_blank">#374</a></li> 
 <li>报表设计权限管理(只能看到自己创建的报表) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F368" target="_blank">#368</a></li> 
 <li>联动钻取报表超链接设置——原始参数下拉框无可选数据字段 <a href="https://gitee.com/jeecg/JimuReport/issues/I40TVU">issues/I40TVU</a></li> 
 <li>大量数据时使用导出Excel方法获取的结果报错。<a href="https://gitee.com/jeecg/JimuReport/issues/I40NLQ">issues/I40NLQ</a></li> 
 <li>报表复制, 主子参数绑定关系丢失 <a href="https://gitee.com/jeecg/JimuReport/issues/I40IMT">issues/I40IMT</a></li> 
 <li>显示问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F390" target="_blank">#390</a></li> 
 <li>动态属性中没有值的显示0，应该显示空的，不是数值类型的 <a href="https://gitee.com/jeecg/JimuReport/issues/I40E4A">issues/I40E4A</a></li> 
 <li>Api数据源字段展示问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I409J8">issues/I409J8</a></li> 
 <li>导出pdf日期格式化无效 <a href="https://gitee.com/jeecg/JimuReport/issues/I412JQ">issues/I412JQ</a></li> 
 <li>可不可以关闭最上面的分页控制栏 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F191" target="_blank">#191</a></li> 
 <li>解析列名的时候，会生成两次 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F387" target="_blank">#387</a></li> 
 <li>分页获取表格数据，当输入页码数，再点击上一页和首页没反应 <a href="https://gitee.com/jeecg/JimuReport/issues/I40KH4">issues/I40KH4</a></li> 
 <li>分组报表、设置表格边框、200多条记录时导出excel报错(项目上线急解决) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F397" target="_blank">#397</a></li> 
 <li>日期无法进行格式化显示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F394" target="_blank">#394</a></li> 
 <li>数据源是否支持达梦数据库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F399" target="_blank">#399</a></li> 
 <li>支持自动增加空白行功能 <a href="https://gitee.com/jeecg/JimuReport/issues/I40QED">issues/I40QED</a></li> 
 <li>公式添加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F310" target="_blank">#310</a></li> 
 <li>数据报表增加行级间颜色变化设置选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F288" target="_blank">#288</a></li> 
 <li>报表设计单元格设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F338" target="_blank">#338</a></li> 
 <li>导出excel自定义规则，显示规则不显示值 <a href="https://gitee.com/jeecg/JimuReport/issues/I3MX8U">issues/I3MX8U</a></li> 
 <li>小数位带千分符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F391" target="_blank">#391</a></li> 
 <li>设置小数位数后，导出的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F392" target="_blank">#392</a></li> 
</ul> 
<p>#代码下载</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul> 
 <li>体验官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
 <li>快速集成文档 ：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></li> 
 <li>技术文档： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com" target="_blank">http://report.jeecg.com</a></li> 
 <li>QQ群：212391162</li> 
</ul> 
<h3 style="text-align:left">为什么选择 JimuReport?</h3> 
<blockquote> 
 <p>永久免费，支持各种复杂报表，并且傻瓜式在线设计，非常的智能，低代码时代，这个是你的首选！</p> 
</blockquote> 
<ul> 
 <li>采用SpringBoot的脚手架项目，都可以快速集成</li> 
 <li>Web 版设计器，类似于excel操作风格，通过拖拽完成报表设计</li> 
 <li>通过SQL、API等方式，将数据源与模板绑定。同时支持表达式，自动计算合计等功能，使计算工作量大大降低</li> 
 <li>开发效率很高，傻瓜式在线报表设计，一分钟设计一个报表，又简单又强大</li> 
 <li>支持 ECharts，目前支持28种图表，在线拖拽设计，支持SQL和API两种数据源</li> 
 <li>支持分组、交叉，合计、表达式等复杂报表</li> 
 <li>支持打印设计（支持套打、背景打印等）可设置打印边距、方向、页眉页脚等参数 一键快速打印 同时可实现发票套打，不动产证等精准、无缝打印</li> 
 <li>大屏设计器支持几十种图表样式，可自由拼接、组合，设计炫酷大屏</li> 
 <li>可设计各种类型的单据、大屏，如出入库单、销售单、财务报表、合同、监控大屏、旅游数据大屏等</li> 
</ul> 
<p>#系统截图</p> 
<ul> 
 <li>报表设计器（专业一流 数据可视化,解决各类报表难题） <img alt src="https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png" referrerpolicy="no-referrer"></li> 
 <li>报表设计器（完全在线设计，简单易用）</li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>打印设计（支持套打、背景打印）</li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9b6cd73719de68e0e45e1cf95cd6104a103.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-8863ea4e67c02dbd844bb8022652f1be651.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>数据报表（支持分组、交叉，合计等复杂报表）</li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fe2ac0dfc3933734961924de0538b3049d2.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-be956cbc19287e4df9cc46c9d15e96da99d.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>图形报表（目前支持28种图表） <img alt src="https://oscimg.oschina.net/oscnet/up-3eda428ef182cb64a1a8e132e4bfeb87718.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-22096123c5b6a10a801967c33cc33a7af11.png" referrerpolicy="no-referrer"></li> 
</ul> 
<p>#功能清单</p> 
<pre style="text-align:left"><code>├─报表设计器
│  ├─数据源
│  │  ├─支持多种数据源，如Oracle,MySQL,SQLServer,PostgreSQL等主流的数据库
│  │  ├─支持SQL编写页面智能化，可以看到数据源下面的表清单和字段清单
│  │  ├─支持参数
│  │  ├─支持单数据源和多数数据源设置
│  ├─单元格格式
│  │  ├─边框
│  │  ├─字体大小
│  │  ├─字体颜色
│  │  ├─背景色
│  │  ├─字体加粗
│  │  ├─支持水平和垂直的分散对齐
│  │  ├─支持文字自动换行设置
│  │  ├─图片设置为图片背景
│  │  ├─支持无线行和无限列
│  │  ├─支持设计器内冻结窗口
│  │  ├─支持对单元格内容或格式的复制、粘贴和删除等功能
│  │  ├─等等
│  ├─报表元素
│  │  ├─文本类型：直接写文本；支持数值类型的文本设置小数位数
│  │  ├─图片类型：支持上传一张图表；支持图片动态生成
│  │  ├─图表类型
│  │  ├─函数类型
│  │  └─支持求和
│  │  └─平均值
│  │  └─最大值
│  │  └─最小值
│  ├─背景
│  │  ├─背景颜色设置
│  │  ├─背景图片设置
│  │  ├─背景透明度设置
│  │  ├─背景大小设置
│  ├─数据字典
│  ├─报表打印
│  │  ├─自定义打印
│  │  └─医药笺、逮捕令、介绍信等自定义样式设计打印
│  │  ├─简单数据打印
│  │  └─出入库单、销售表打印
│  │  └─带参数打印
│  │  └─分页打印
│  │  ├─套打
│  │  └─不动产证书打印
│  │  └─发票打印
│  ├─数据报表
│  │  ├─分组数据报表
│  │  └─横向数据分组
│  │  └─纵向数据分组
│  │  └─多级循环表头分组
│  │  └─横向分组小计
│  │  └─纵向分组小计
│  │  └─合计
│  │  ├─交叉报表
│  │  ├─明细表
│  │  ├─带条件查询报表
│  │  ├─表达式报表
│  │  ├─带二维码/条形码报表
│  │  ├─多表头复杂报表
│  │  ├─主子报表
│  │  ├─预警报表
│  │  ├─数据钻取报表
│  ├─图形报表
│  │  ├─柱形图
│  │  ├─堆叠柱形图
│  │  ├─折线图
│  │  ├─饼图
│  │  ├─动态轮播图
│  │  ├─折柱图
│  │  ├─散点图
│  │  ├─漏斗图
│  │  ├─雷达图
│  │  ├─象形图
│  │  ├─地图
│  │  ├─仪盘表
│  │  ├─关系图
│  │  ├─图表背景
│  │  ├─图表动态刷新
│  │  ├─图表数据字典
│  ├─参数
│  │  ├─参数配置
│  │  ├─参数管理
│  ├─导入导出
│  │  ├─支持导入Excel
│  │  ├─支持导出Excel、pdf；支持导出excel、pdf带参数
│  ├─打印设置
│  │  ├─打印区域设置
│  │  ├─打印机设置
│  │  ├─预览
│  │  ├─打印页码设置
├─大屏设计器
│  ├─系统功能
│  │  ├─静态数据源和动态数据源设置
│  │  ├─基础功能
│  │  └─支持拖拽设计
│  │  └─支持增、删、改、查大屏
│  │  └─支持复制大屏数据和样式
│  │  └─支持大屏预览、分享
│  │  └─支持系统自动保存数据，同时支持手动恢复数据
│  │  └─支持设置大屏密码
│  │  └─支持对组件图层的删除、组合、上移、下移、置顶、置底等
│  │  ├─背景设置
│  │  └─大屏的宽度和高度设置
│  │  └─大屏简介设置
│  │  └─背景颜色、背景图片设置
│  │  └─封面图设置
│  │  └─缩放比例设置
│  │  └─环境地址设置
│  │  └─水印设置
│  │  ├─地图设置
│  │  └─添加地图
│  │  └─地图数据隔离
│  ├─图表
│  │  ├─柱形图
│  │  ├─折线图
│  │  ├─折柱图
│  │  ├─饼图
│  │  ├─象形图
│  │  ├─雷达图
│  │  ├─散点图
│  │  ├─漏斗图
│  │  ├─文本框
│  │  ├─跑马灯
│  │  ├─超链接
│  │  ├─实时时间
│  │  ├─地图
│  │  ├─全国物流地图
│  │  ├─地理坐标地图
│  │  ├─城市派件地图
│  │  ├─图片
│  │  ├─图片框
│  │  ├─轮播图
│  │  ├─滑动组件
│  │  ├─iframe
│  │  ├─video
│  │  ├─翻牌器
│  │  ├─环形图
│  │  ├─进度条
│  │  ├─仪盘表
│  │  ├─字浮云
│  │  ├─表格
│  │  ├─选项卡
│  │  ├─万能组件
└─其他模块
   └─更多功能开发中。。</code></pre>
                                        </div>
                                      
</div>
            