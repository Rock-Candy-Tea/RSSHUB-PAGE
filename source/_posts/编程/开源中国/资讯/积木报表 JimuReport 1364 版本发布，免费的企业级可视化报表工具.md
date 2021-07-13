
---
title: '积木报表 JimuReport 1.3.64 版本发布，免费的企业级可视化报表工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 12:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p>积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！！！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.3.64-beta | 2021-07-13</p> 
<p>集成依赖</p> 
<pre style="text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>spring-boot-starter-jimureport<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.3.64-beta<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="text-align:left">增量SQL</p> 
<pre style="text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_param`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`search_flag`</span> int(1) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询标识0否1是 默认0'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`update_time`</span>;
<span style="color:#d73a49">update</span> jimu_report_db_param <span style="color:#d73a49">set</span> search_flag = 0;
<span style="color:#d73a49">create</span> <span style="color:#d73a49">table</span> jimu_dict <span style="color:#d73a49">like</span> sys_dict;
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> jimu_dict <span style="color:#d73a49">select</span> * <span style="color:#d73a49">from</span> sys_dict;
<span style="color:#d73a49">create</span> <span style="color:#d73a49">table</span> jimu_dict_item <span style="color:#d73a49">like</span> sys_dict_item;
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> jimu_dict_item <span style="color:#d73a49">select</span> * <span style="color:#d73a49">from</span> sys_dict_item;
</code></pre> 
<p>#升级日志</p> 
<p>新功能</p> 
<ul> 
 <li>分组报表功能重构，支持分组内小计，支持设置分组字段排序、动态补数据等</li> 
 <li>新版导出pdf功能重构，支持表达式、字体样式、背景、套打、交叉表头</li> 
 <li>字典表名改成jimu_*前缀，与系统表区分</li> 
 <li>超链接颜色跟随字体颜色走 不设置默认蓝色</li> 
 <li>导出excel支持api方式调用</li> 
 <li>循环块重复设定bug修复</li> 
 <li>动态循环表头如果list为空会出现空指针的问题</li> 
 <li>横向分组后台报错</li> 
 <li>api超时提示、select * 多个字段引起报错，页面显示的是表名不存在，提示不正确,提示修改 tb JMREP-2066</li> 
 <li>微服务下自定义项目前缀参数customPrePath，不好使</li> 
 <li>解决springboot2.5集成minidao空指针问题</li> 
 <li>支持动态数据源配置（minidao默认数据源名：minidaoDataSource，如果不配置则随机走第一个数据源配置）</li> 
 <li>钻取新窗口不显示下一页</li> 
 <li>严重：模板里面设置的行高，预览时，恢复成默认高度了</li> 
 <li>主子报表有字典值没有翻译，导致子表查询不出来</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>导出excel时，图片未导出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F230" target="_blank">#230</a></li> 
 <li>积木报表不支持MYSQL内置函数，视图解析时出错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F277" target="_blank">#277</a></li> 
 <li>表格小数点数值为0,设置显示位数无效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F136" target="_blank">#136</a></li> 
 <li>上传模板不支持xls <a href="https://gitee.com/jeecg/JimuReport/issues/I3SSJ0">I3SSJ0</a></li> 
 <li>查询栏查询时间类型及范围查找，无法显示默认值 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SN3P">3SN3P</a></li> 
 <li>钻取到下一页面，能否增加返回到上一页操作 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SL05">I3SL05</a></li> 
 <li>图表联动可以看到已删除的图标 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SEV4">I3SEV4</a></li> 
 <li>列比较多，编辑时列只显示到AX列，后面的列没显示出来造成无法进行修改 <a href="https://gitee.com/jeecg/JimuReport/issues/I3RQIT">I3RQIT</a></li> 
 <li>对每页10条的选项改成没有20信息后，打印和导出的数据数量都不对，都是10条 <a href="https://gitee.com/jeecg/JimuReport/issues/I3NZF8">I3NZF8</a></li> 
 <li>sql数据集中SQL解析失败问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3NCM7">I3NCM7</a></li> 
 <li>使用函数希望支持单元格拖拽选择 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SZPP">I3SZPP</a></li> 
 <li>SpringBoot 2.5.0 集成后数据库未初始化 <a href="https://gitee.com/jeecg/JimuReport/issues/I3TD7G">I3TD7G</a></li> 
 <li>springboot按文档集成报错 <a href="https://gitee.com/jeecg/JimuReport/issues/I3QC15">I3QC15</a></li> 
 <li>启动报MinidaoAutoConfiguration初始化失败 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SIEX">I3SIEX</a></li> 
 <li>希望取消数据字典的入侵式行为，通过api或json的方式进行前端缓存 <a href="https://gitee.com/jeecg/JimuReport/issues/I3UIJ4">I3UIJ4</a></li> 
 <li>url参数可以放在报表里么？ <a href="https://gitee.com/jeecg/JimuReport/issues/I3U3Q5">I3U3Q5</a></li> 
 <li>在线设计不好管理 <a href="https://gitee.com/jeecg/JimuReport/issues/I3UQEE">I3UQEE</a></li> 
 <li>浏览器传参直接在报表上显示导出没有带参数导出 <a href="https://gitee.com/jeecg/JimuReport/issues/I3ZAEU">I3ZAEU</a></li> 
 <li>当鼠标在api地址输入框失去焦点的时候，接口参数会被清空 <a href="https://gitee.com/jeecg/JimuReport/issues/I3YP2X">I3YP2X</a></li> 
 <li>横向分组，如果数据缺失，报表显示错误。 <a href="https://gitee.com/jeecg/JimuReport/issues/I3XT94">I3XT94</a></li> 
 <li>根据查询条件查询，导出Excel没有传入参数 <a href="https://gitee.com/jeecg/JimuReport/issues/I3XI9M">I3XI9M</a></li> 
 <li>能否小计动态列到其他非一列的格子？ <a href="https://gitee.com/jeecg/JimuReport/issues/I3XYZ3">I3XYZ3</a></li> 
 <li>api数据集get请求后台取不到参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F322" target="_blank">#322</a></li> 
 <li>积木报表 列超出设定纸张宽度后，调整会格式出问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F359" target="_blank"> #359</a></li> 
 <li>报表设计器功能优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F321" target="_blank">#321</a></li> 
 <li>图形报表条件搜索时图层数据错乱问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F325" target="_blank"> #325</a></li> 
 <li>非jeecg-boot项目集成积木报表，在上传背景图片时，请求头中没有加上token，是否可以加上？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F318" target="_blank"> #318</a></li> 
 <li>首页分页问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F291" target="_blank">#291</a></li> 
 <li>使用多数据对比柱状图时，如果查询条件后图表重叠 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F305" target="_blank">#305</a></li> 
 <li>表格中存在负数，合计的时候，设置两位小数不起作用，而且数据不正确<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F293" target="_blank"> #293</a></li> 
 <li>1.3.1-beta4 API数据源 请求超时<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F319" target="_blank"> #319</a></li> 
 <li>合并两行表格，打印数据显示有问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F298" target="_blank">#298</a></li> 
 <li>预览和设计加载外网js ,加载慢<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F316" target="_blank"> #316</a></li> 
 <li>【bug】交叉报表导出报错问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F339" target="_blank">#339</a></li> 
 <li>报表连接600多张表的SQL Server，后编辑SQL页面卡死 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F333" target="_blank">#333</a></li> 
 <li>表头在横向分组的情况下，excel导出失败<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F353" target="_blank"> #353</a></li> 
 <li>积木报表的主子表在主表没有数据的情况下页面会出错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2660" target="_blank">#2660</a></li> 
 <li>【报表设计器】添加了链接后字体无法改变颜色<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2702" target="_blank"> #2702</a></li> 
 <li>【报表设计器】循环块无法取消 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2606" target="_blank">#2606</a></li> 
</ul> 
<p>#代码下载</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul> 
 <li>集成文档 ：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></li> 
 <li>数据库脚本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fblob%2Fmaster%2Fdb" target="_blank">jimureport.sql</a></li> 
 <li>技术官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
 <li>技术文档： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com" target="_blank">http://report.jeecg.com</a></li> 
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
   └─更多功能开发中。。
</code></pre>
                                        </div>
                                      
</div>
            