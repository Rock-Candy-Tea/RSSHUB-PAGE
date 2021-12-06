
---
title: 'JimuReport 积木报表 v1.4.2 版本发布，免费的可视化低代码报表'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 18:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.4.2 | 2021-12-06</p> 
<p>集成依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>jimureport-spring-boot-starter<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.4.2<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p>#升级日志</p> 
<p>重点新功能</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>数据源设置分页，导出excel数据为空。</li> 
 <li>设置英文或六位颜色值时，遇到设置小数位数据，颜色不显示</li> 
 <li>设置三位颜色值导出excel 无显示颜色</li> 
 <li>地图控件采用SQL数据源无法定时更新</li> 
 <li>斜线表头颜色为空会报空指针</li> 
 <li>平均数不计算空单元格</li> 
 <li>下拉选项效果改变但是查询条件值未改变</li> 
 <li>导出excel设置的分页数大于数量第一个数据源导不出来</li> 
 <li>同一单元格内无法同时解析多个参数</li> 
 <li>【导入报表】报错 list页面查询不传json_str，避免查询不到数据</li> 
 <li>被除数不能为0</li> 
 <li>导出excel和参数替换加上日志，线上不管用</li> 
 <li>预览界面时，点击查询后，滚动条会消失</li> 
 <li>内存问题 导出pdf处理完清空map、json</li> 
 <li>导出excel、pdf改造 使用response获取流</li> 
 <li>如果key不存在应该清空，否则在saas模式下sql可以解析</li> 
 <li>数据源key存在下拉框提示显示数据源id</li> 
 <li>导出excel、pdf日期格式重构，支持基本日期格式</li> 
 <li>mongo驱动换成mongodb-driver-sync, 与spring-boot-starter-data-mongodb保持一致</li> 
 <li>默认选中分页</li> 
 <li>搜索下拉框默认只显示10条数据,可以设置下拉显示条数</li> 
 <li>新建积木报表处理extJson参数配置常量类及命名修改</li> 
 <li>升级minidao版本，解决含limit的sql分页问题</li> 
 <li>钻取跳转携带token</li> 
 <li>数值计算交给bigdecimal处理</li> 
 <li>数值格式化 默认不设置小数位数</li> 
 <li>重构表达式，解决金额数字计算不准确问题</li> 
</ul> 
<p>Issues处理</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>预览界面时，点击查询后，滚动条会消失<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F599" target="_blank">issues/#599</a></li> 
 <li>分组后数据显示错误<a href="https://gitee.com/jeecg/JimuReport/issues/I4DSDM">issues/I4DSDM</a></li> 
 <li>合计行问题=SUM(E4:L4)<a href="https://gitee.com/jeecg/JimuReport/issues/I4FUJT">issues/I4FUJT</a></li> 
 <li>积木报表添加js增强代码预览分页无效<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F610" target="_blank">issues/#610</a></li> 
 <li>average()数据集表达式对列求平均没有排除空数据<a href="https://gitee.com/jeecg/JimuReport/issues/I4EUZV">issues/#I4EUZV</a></li> 
 <li>使用横向纵向组合动态列分组，后台的模板报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4EB9G">issues/#I4EB9G</a></li> 
 <li>存储过程SQL解析按字段名排序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F640" target="_blank">issues/#640</a></li> 
 <li>支持saas配置<a href="https://gitee.com/jeecg/JimuReport/issues/I4HWAM">issues/#I4HWAM</a></li> 
 <li>下拉树控件在多选的时候，如果选错了，察掉后不会及时生效，必须要重置才行<a href="https://gitee.com/jeecg/JimuReport/issues/I4FKR0">issues/#I4FKR0</a></li> 
 <li>同一单元格内无法同时解析多个参数<a href="https://gitee.com/jeecg/JimuReport/issues/I4EQ2K">issues/#I4EQ2K</a></li> 
 <li>组合动态列分组bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F607" target="_blank">issues/#607</a></li> 
 <li>如果验证数据库名和用户名不一致，连不上mongo<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F601" target="_blank">issues/#601</a></li> 
 <li>数据源设置分页，导出excel数据为空<a href="https://gitee.com/jeecg/JimuReport/issues/I4EAUY">issues/#I4EAUY</a></li> 
 <li>下钻功能问题<a href="https://gitee.com/jeecg/JimuReport/issues/I4IZ64">issues/#I4IZ64</a></li> 
 <li>分组汇总问题优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F673" target="_blank">issues/#673</a></li> 
 <li>报表导出excel或PDF时间数据缺失<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F663" target="_blank">issues/#663</a></li> 
 <li>人大金仓数据库 表名项渲染为空,看渲染页要求为首字母大写，可以配置<a href="https://gitee.com/jeecg/JimuReport/issues/I4IU2U">issues/#I4IU2U</a></li> 
 <li>1.4.0与mongodb依赖冲突，启动报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4ITG0">issues/#I4ITG0</a></li> 
 <li>javabean数据源优化，解析出来字段名以传过来为依据<a href="https://gitee.com/jeecg/JimuReport/issues/I4HK1I">issues/#I4HK1I</a></li> 
 <li>excel包含自定义格式，上传失败<a href="https://gitee.com/jeecg/JimuReport/issues/I4HVDU">issues/#I4HVDU</a></li> 
 <li>积木报表配置报表钻取单元格传值与表格传值问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F658" target="_blank">issues/#658</a></li> 
 <li>增加超链接的【参数设置】的其中一种是获取不到的参数的。<a href="https://gitee.com/jeecg/JimuReport/issues/I4HX60">issues/#I4HX60</a></li> 
 <li>数据查询工具条的时候显示总数据条数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F672" target="_blank">issues/#672</a></li> 
 <li>使用人大金仓数据源的时候后端返回的name 为小写导致不能生成表<a href="https://gitee.com/jeecg/JimuReport/issues/I4JBLE">issues/#I4JBLE</a></li> 
 <li>搜索下拉框最多只显示10条数据,根据配置显示条数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F675" target="_blank">issues/#675</a></li> 
 <li>SQL中加入自带的limit条件会报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4JFKQ">issues/#I4JFKQ</a></li> 
 <li>图表与javaBean数据源绑定报错，报错问题以附上解决方案<a href="https://gitee.com/jeecg/JimuReport/issues/I4I2X8">issues/#I4I2X8</a></li> 
 <li>使用非管理员的账号时，报表钻取问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F680" target="_blank">issues/#680</a></li> 
 <li>把单元格设置成【数字】类型后，导出Excel报错。<a href="https://gitee.com/jeecg/JimuReport/issues/I4JWH3">issues/#I4JWH3</a></li> 
 <li>钻取跳转携带token<a href="https://gitee.com/jeecg/JimuReport/issues/I4JM0I">issues/#I4JM0I</a></li> 
 <li>图形报表新建的SQL数据源，无法在报表中展现<a href="https://gitee.com/jeecg/JimuReport/issues/I4FNJC">issues/#I4FNJC</a></li> 
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
 <li>通过SQL、API等方式，将数据源与模板绑定。同时支持表达式，自动计算合计等功能，使计算工作量大大降低</li> 
 <li>开发效率很高，傻瓜式在线报表设计，一分钟设计一个报表，又简单又强大</li> 
 <li>支持 ECharts，目前支持28种图表，在线拖拽设计，支持SQL和API两种数据源</li> 
 <li>支持分组、交叉，合计、表达式等复杂报表</li> 
 <li>支持打印设计（支持套打、背景打印等）可设置打印边距、方向、页眉页脚等参数 一键快速打印 同时可实现发票套打，不动产证等精准、无缝打印</li> 
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
│  │  └─发票打印
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
   └─更多功能开发中。。</code></pre>
                                        </div>
                                      
</div>
            