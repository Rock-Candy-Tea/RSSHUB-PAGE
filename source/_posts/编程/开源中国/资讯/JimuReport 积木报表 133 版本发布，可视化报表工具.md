
---
title: 'JimuReport 积木报表 1.3.3 版本发布，可视化报表工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
author: 开源中国
comments: false
date: Mon, 17 May 2021 09:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p>积木报表，是一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计报表！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，重点此软件是完全免费的！！！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.3.3-beta | 2021-05-17</p> 
<p>集成依赖</p> 
<pre style="text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>spring-boot-starter-jimureport<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.3.3-beta<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="text-align:left">增量SQL</p> 
<pre style="text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_field`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`search_value`</span> varchar(100) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询默认值'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`dict_code`</span>;

<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db`</span> 
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`json_data`</span> text <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'json数据，直接解析json内容'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`db_source_type`</span>;

<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_data_source`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`connect_times`</span> int(1) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'连接次数'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`update_time`</span>;
</code></pre> 
<p>#升级日志</p> 
<p>新功能</p> 
<ul> 
 <li>新的打印方式“打印表格”针对单据打印更清晰(不支持图表的打印)</li> 
 <li>新的PDF生成更清晰(对支持图表的支持还不好，待优化)</li> 
 <li>支持联动和钻取</li> 
 <li>优化excel导入和导出</li> 
 <li>支持横屏和竖屏设置</li> 
 <li>设计器支持自动保存功能</li> 
 <li>支持json格式数据集</li> 
 <li>系统变量支持当前时间当前日期</li> 
 <li>支持格式刷</li> 
 <li>支持插入多列多行</li> 
 <li>查询条件支持默认值</li> 
 <li>删除不支持快捷键</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>api数据源的报表参数每次修改api会导致参数文本清空 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F186" target="_blank">#186</a></li> 
 <li>api数据源无效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F183" target="_blank">#183</a></li> 
 <li>自定义api 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F177" target="_blank">#177</a></li> 
 <li>1.3.1-beta3API预览报错 <a href="https://gitee.com/jeecg/JimuReport/issues/I3IE3O">issues/I3IE3O</a></li> 
 <li>1.3.1-beta3版本，连接SQL Server，数据查询报错 <a href="https://gitee.com/jeecg/JimuReport/issues/I3IF5W">issues/I3IF5W</a></li> 
 <li>点打印按钮卡住 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F180" target="_blank">#180</a></li> 
 <li>[BUG] 导入的模板无法设置任何属性,都报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F169" target="_blank">#169</a></li> 
 <li>1.3.1-beta2版本 导出到excel和pdf，请求api的业务数据为空 <a href="https://gitee.com/jeecg/JimuReport/issues/I3HMWQ">issues/I3HMWQ</a></li> 
 <li>本地使用idea调试正常，jar包发布到服务器上报错如下<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F211" target="_blank">#211</a></li> 
 <li>数据钻取无法使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F187" target="_blank">#187</a></li> 
 <li>希望打印增加按分页打印全部的功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F200" target="_blank">#200</a></li> 
 <li>分组单元格进行合并后，预览报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F155" target="_blank">#155</a></li> 
 <li>没有自动保存，很难受，而且一段时间后保存不了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F201" target="_blank">#201</a></li> 
 <li>1.3.1-beta4版本，设计页面问题反馈 <a href="https://gitee.com/jeecg/JimuReport/issues/I3ITX4">issues/I3ITX4</a></li> 
 <li>当导出列表里含大写的IOS时（或含大写英文），导出就报错 <a href="https://gitee.com/jeecg/JimuReport/issues/I3IIR9">issues/I3IIR9</a></li> 
 <li>严重bug mac下新建模版不好用 <a href="https://gitee.com/jeecg/JimuReport/issues/I3NL58">issues/I3NL58</a></li> 
 <li>SnowflakeIdWorker类中SystemUtils.getHostName()在mac环境下为空 <a href="https://gitee.com/jeecg/minidao/issues/I3NKZH">issues/I3NKZH</a></li> 
 <li>popup组件设置单选在单表和主表状态下不起效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2478" target="_blank">#2478</a></li> 
 <li>导出excel或pdf只能导出第一页 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F157" target="_blank">#157</a></li> 
 <li>API带参数查询失败 <a href="https://gitee.com/jeecg/JimuReport/issues/I3JKM5">issues/I3JKM5</a></li> 
 <li>API接口返回超过5S怎么处理哈 <a href="https://gitee.com/jeecg/JimuReport/issues/I3O960">issues/I3O960</a></li> 
 <li>集成1.3.1-beta4 服务启动失败 <a href="https://gitee.com/jeecg/JimuReport/issues/I3O34Q">issues/I3O34Q</a></li> 
 <li>1.3.1-beta4 中API数据集无法自动发送token <a href="https://gitee.com/jeecg/JimuReport/issues/I3OVQL">issues/I3OVQL</a></li> 
 <li>打印页面没有纵向横向切换 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F2450" target="_blank">#245</a></li> 
 <li>饼图的提示内容，缺少百分比的支持 <a href="https://gitee.com/jeecg/JimuReport/issues/I3NP5F">issues/I3NP5F</a></li> 
 <li>1.3.1-beta2版本 请求非官方的业务接口时， X-Access-Token放到了请求参数中，建议放在header中更好<a href="https://gitee.com/jeecg/JimuReport/issues/I3HDEI">issues/I3HDEI</a></li> 
 <li>使用系统变量占位符#&#123;&#125; 书写SQL数据集，出现的问题。望解答 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F203" target="_blank">#203</a></li> 
 <li>模板案例列表中，上传封面后不成功，日志提示报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F189" target="_blank">#189</a></li> 
 <li>使用系统变量占位符#&#123;&#125; 书写SQL数据集，出现的问题。望解答 <a href="https://gitee.com/jeecg/JimuReport/issues/I3J5U7">issues/I3J5U7</a></li> 
 <li>大屏柱形图不支持交互 <a href="https://gitee.com/jeecg/JimuReport/issues/I3MXKK">issues/I3MXKK</a></li> 
 <li>js计算合计精度误差问题</li> 
</ul> 
<p>#代码下载</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul> 
 <li>集成文档 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></li> 
 <li>数据库脚本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fblob%2Fmaster%2Fdb" target="_blank">jimureport.sql</a></li> 
 <li>技术官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
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
   └─更多功能开发中。。
</code></pre>
                                        </div>
                                      
</div>
            