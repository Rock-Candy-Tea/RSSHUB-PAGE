
---
title: '免费的可视化 Web 报表工具，JimuReport v1.4.4-beta 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 09:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                                            <p>项目介绍</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.4.4-beta | 2022-03-21</p> 
<p>集成依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>jimureport-spring-boot-starter<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.4.4-beta<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p>#升级日志</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">重点解决静态资源加载冲突问题 和 导出PDF报错问题</p> 
</blockquote> 
<p>升级Sql</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_share`</span> 
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`preview_lock_status`</span> <span>varchar</span>(<span>1</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'密码锁状态'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`status`</span>;
</code></pre> 
<p>Issues处理</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>引入swagger 3.0 版本报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4X617">#I4X617</a></li> 
 <li>版本1.4.32跟工作流版本7.1.0.M4有冲突、导致静态资源404<a href="https://gitee.com/jeecg/JimuReport/issues/I4YCXR">#I4YCXR</a></li> 
 <li>若依分离集成积木报表版本报错<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F832" target="_blank">#832</a></li> 
 <li>若依微服务,运行在linux上浏览器报错不显示<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F847" target="_blank">#847</a></li> 
 <li>引入依赖后访问swagger文档404<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F712" target="_blank">#712</a></li> 
 <li>eladmin引入积木报表无法访问swagger-ui.html页<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F777" target="_blank">#777</a></li> 
 <li>数据横向循坏的时候 如果没有数据的话 会现在数据库字段<a href="https://gitee.com/jeecg/JimuReport/issues/I4VBJI">#I4VBJI</a></li> 
 <li>动态列，三级数据存在错乱的严重bug<a href="https://gitee.com/jeecg/JimuReport/issues/I4RP9G">#I4RP9G</a></li> 
 <li>设置自动换行后，数据显示不全<a href="https://gitee.com/jeecg/JimuReport/issues/I4QZBO">#I4QZBO</a></li> 
 <li>图表控件挡住滚动条的问题<a href="https://gitee.com/jeecg/JimuReport/issues/I4ONL5">#I4ONL5</a></li> 
 <li>关于报表查询页存在XSS漏洞攻击修复<a href="https://gitee.com/jeecg/JimuReport/issues/I4NEVO">#I4NEVO</a></li> 
 <li>数据报表查询报表和折线图时，导出图片中图形数据不正确<a href="https://gitee.com/jeecg/JimuReport/issues/I4MASB">#I4MASB</a></li> 
 <li>导出PDF后的条码没有显示下方的覆盖文字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F754" target="_blank">#754</a></li> 
 <li>新建报表加载缓慢，地图数据改为加载json<a href="https://gitee.com/jeecg/JimuReport/issues/I4NSTK">#I4NSTK</a></li> 
 <li>报表查询报错<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4Y351">#I4Y351</a></li> 
 <li>mongodb无法解析sql<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4XCP2">#I4XCP2</a></li> 
 <li>关于查询框中下拉多选样式bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F809" target="_blank">#809</a></li> 
 <li>api数据集报表 驼峰形式的字段查询无效<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F799" target="_blank">#799</a></li> 
 <li>1.4.32预览报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4Y651">#I4Y651</a></li> 
 <li>JavaBean数据集无法分sheet导出<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F825" target="_blank">#825</a></li> 
 <li>反射型XSS漏洞修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3223" target="_blank">#3223</a></li> 
 <li>消息通知长连接启动心跳机制，后端代码小bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3473" target="_blank">#3473</a></li> 
 <li>自带图形报表企业实时销售数据导出excel格式乱<a href="https://gitee.com/jeecg/JimuReport/issues/I4Y2EX">#I4Y2EX</a></li> 
 <li>负数转换大写金额报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4XRK1">#I4XRK1</a></li> 
 <li>使用now()函数导出时候，导出excel日期错误<a href="https://gitee.com/jeecg/JimuReport/issues/I4X0WC">#I4X0WC</a></li> 
 <li>图片偏移量设置 - 横向偏移(px)：无效<a href="https://gitee.com/jeecg/JimuReport/issues/I4X0EQ">#I4X0EQ</a></li> 
 <li>积木1.4.3分组排序bug<a href="https://gitee.com/jeecg/JimuReport/issues/I4WZ1N">#I4WZ1N</a></li> 
 <li>升级到1.4.3版本 /jmreport/exportPdf接口空指针<a href="https://gitee.com/jeecg/JimuReport/issues/I4WYUZ">#I4WYUZ</a></li> 
 <li>sql查询报表报错null<a href="https://gitee.com/jeecg/JimuReport/issues/I4WYOM">#I4WYOM</a></li> 
 <li>分享链接的预览密码忽略<a href="https://gitee.com/jeecg/JimuReport/issues/I4WWKE">#I4WWKE</a></li> 
 <li>文字换行展示最后面会出现半个字<a href="https://gitee.com/jeecg/JimuReport/issues/I4WORF">#I4WORF</a></li> 
 <li>积木报表html打印预览空白区域问题<a href="https://gitee.com/jeecg/JimuReport/issues/I4WNR1">#I4WNR1</a></li> 
 <li>积木报表导出pdf打不开，文件已损坏<a href="https://gitee.com/jeecg/JimuReport/issues/I4WMYE">#I4WMYE</a></li> 
 <li>导出pdf后，上传的图片都不呈现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F813" target="_blank">#813</a></li> 
 <li>查询菜单选择日期范围页面崩溃<a href="https://gitee.com/jeecg/JimuReport/issues/I4XBKF">#I4XBKF</a></li> 
 <li>升级到1.4.32版本 导出pdf接口空指针<a href="https://gitee.com/jeecg/JimuReport/issues/I4XBM8">#I4XBM8</a></li> 
 <li>1.4.32版本自定义系统日期变量，查询条件中日期变成了NAN<a href="https://gitee.com/jeecg/JimuReport/issues/I4YF8V">#I4YF8V</a></li> 
 <li>1.4.32导出pdf图片报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4Y043">#I4Y043</a></li> 
 <li>横向动态列分组功能，默认排序数据与列错位<a href="https://gitee.com/jeecg/JimuReport/issues/I4LNR4">#I4LNR4</a></li> 
 <li>使用自定义了系统变量，不同的电脑，有的可以，有的报错。<a href="https://gitee.com/jeecg/JimuReport/issues/I4TSXS">#I4TSXS</a></li> 
 <li>饼状图配置网络报表 传递参数的问题<a href="https://gitee.com/jeecg/JimuReport/issues/I4VAZR">#I4VAZR</a></li> 
 <li>图表联动时，配置的数据字典功能失效<a href="https://gitee.com/jeecg/JimuReport/issues/I4W5NG">#I4W5NG</a></li> 
 <li>积木分栏只能设置一次<a href="https://gitee.com/jeecg/JimuReport/issues/I4WDTS">#I4WDTS</a></li> 
 <li>柱形图设置超链接，点击任何一列都默认用第一列的数据<a href="https://gitee.com/jeecg/JimuReport/issues/I4WP5Y">#I4WP5Y</a></li> 
</ul> 
<p>#代码下载</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>体验官网：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
 <li>快速集成文档 ：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></li> 
 <li>技术文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com" target="_blank">http://report.jeecg.com</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JimuReport?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">永久免费，支持各种复杂报表，并且傻瓜式在线设计，非常的智能，低代码时代，这个是你的首选！</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用SpringBoot的脚手架项目，都可以快速集成</li> 
 <li>Web 版设计器，类似于excel操作风格，通过拖拽完成报表设计</li> 
 <li>通过SQL、API等方式，将数据源与模板绑定。同时支持表达式，自动计算合计等功能，使计算工作量降低</li> 
 <li>开发效率很高，傻瓜式在线报表设计，一分钟设计一个报表，又简单又强大</li> 
 <li>支持 ECharts，目前支持28种图表，在线拖拽设计，支持SQL和API两种数据源</li> 
 <li>支持分组、交叉，合计、表达式等复杂报表</li> 
 <li>支持打印设计（支持套打、背景打印等）可设置打印边距、方向、页眉页脚等参数 一键快速打印 同时可实现套打，不动产证等精准、无缝打印</li> 
 <li>大屏设计器支持几十种图表样式，可自由拼接、组合，设计炫酷大屏</li> 
 <li>可设计各种类型的单据、大屏，如出入库单、销售单、财务报表、合同、监控大屏、旅游数据大屏等</li> 
</ul> 
<p>#系统截图</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>报表设计器（专业一流 数据可视化,解决各类报表难题）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png" referrerpolicy="no-referrer"></li> 
 <li>报表设计器（完全在线设计，简单易用）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>打印设计（支持套打、背景打印）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9b6cd73719de68e0e45e1cf95cd6104a103.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-8863ea4e67c02dbd844bb8022652f1be651.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>数据报表（支持分组、交叉，合计等复杂报表）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fe2ac0dfc3933734961924de0538b3049d2.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-be956cbc19287e4df9cc46c9d15e96da99d.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>图形报表（目前支持28种图表）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-3eda428ef182cb64a1a8e132e4bfeb87718.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-22096123c5b6a10a801967c33cc33a7af11.png" referrerpolicy="no-referrer"></li> 
 <li>数据报表斑马线</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e77ba28f6fb56d1147c13388e7e5d19d1bc.png" referrerpolicy="no-referrer"></p> 
<p>#功能清单</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─报表设计器
│  ├─数据源
│  │  ├─支持多种数据源，如Oracle,MySQL,SQLServer,PostgreSQL等主流的数据库
│  │  ├─支持SQL编写页面智能化，可以看到数据源下面的表清单和字段清单
│  │  ├─支持参数
│  │  ├─支持单数据源和多数数据源设置
│  │  ├─支持Nosql数据源Redis，MongoDB
│  │  ├─支持存储过程
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
│  │  └─打印
│  ├─数据报表
│  │  ├─分组数据报表
│  │  └─横向数据分组
│  │  └─纵向数据分组
│  │  └─多级循环表头分组
│  │  └─横向分组小计
│  │  └─纵向分组小计
│  │  └─分版
│  │  └─分栏
│  │  └─动态合并格
│  │  └─自定义分页条数
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
   └─更多功能开发中。。
</code></pre>
                                        </div>
                                      
</div>
            