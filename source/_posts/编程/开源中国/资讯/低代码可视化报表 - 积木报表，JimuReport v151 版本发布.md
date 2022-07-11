
---
title: '低代码可视化报表 - 积木报表，JimuReport v1.5.1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 10:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                                            <p>项目介绍</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">一款免费的低代码可视化报表，像搭建积木一样在线拖拽设计！低代码开发必备，功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承 “简单、易用、专业” 的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.5.1 | 2022-07-11</p> 
<p>集成依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>jimureport-spring-boot-starter<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.5.1<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p>#升级日志</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">重点修复 PDF 导出系列问题、解决百度统计 js 导致内网打不开问题；</p> 
</blockquote> 
<p>升级 sql</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>增加多租户字段，后期支持多租户功能。</code></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span>  jimu_report_data_source
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> tenant_id <span>varchar</span>(<span>10</span>) <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8 <span style="color:#d73a49">COLLATE</span> utf8_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'多租户标识'</span> <span style="color:#d73a49">AFTER</span> connect_times;

<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> jimu_dict
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> tenant_id <span>varchar</span>(<span>10</span>) <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8 <span style="color:#d73a49">COLLATE</span> utf8_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'多租户标识'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#d73a49">type</span>;

<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> jimu_report
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> tenant_id <span>varchar</span>(<span>10</span>) <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8 <span style="color:#d73a49">COLLATE</span> utf8_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'多租户标识'</span> <span style="color:#d73a49">AFTER</span> js_str;
</code></pre> 
<p>Issues 处理</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>pdf 导出内容，自动换行不完全<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I55XKX">issues/I55XKX</a></li> 
 <li>时间格式问题<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I56PQO">issues/I56PQO</a></li> 
 <li>动态分组下有图表时，会把表格里面的部分数据遮盖住<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I58W92">issues/I58W92</a></li> 
 <li>api 解析自定义解析的时候，字段全部变成小写<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F946" target="_blank">issues/946</a></li> 
 <li>cnmoney 金额转换大写的问题<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I59L47">issues/I59L47</a></li> 
 <li>柱状图数字展示重叠<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1025" target="_blank">issues/1025</a></li> 
 <li>批量查询字段数据长度受限<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5A3V1">issues/I5A3V1</a></li> 
 <li>图表报表 折线图显示问题<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5CO1P">issues/I5CO1P</a></li> 
 <li>图表的数值显示，会连轴名称一起显示<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1100" target="_blank">issues/1100</a></li> 
 <li>折线图存在显示数值问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1086" target="_blank">issues/1086</a></li> 
 <li>存储过程列名相同，取别名出错<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I59V3Z">issues/I59V3Z</a></li> 
 <li>行号函数 row () 不好使<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5AF6Y">issues/I5AF6Y</a></li> 
 <li>升级 1.5.0 后导出 PDF, 出现图片遮挡边框线条<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5BIB3">issues/I5BIB3</a></li> 
 <li>报表下钻时返回上一页下拉树参数回显有问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1086" target="_blank">issues/965</a></li> 
 <li>sql 使用系统变量作为数据字段列发生 sql 解析异常<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5CUJ3">issues/I5CUJ3</a></li> 
 <li>查询条件下拉框最右边增加一个清空功能<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1068" target="_blank">issues/1068</a></li> 
 <li>图表中图例设置，纵向位置设置为底部，调整上边距图例显示问题<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I58YJG">issues/I58YJG</a></li> 
 <li>关于数据字典多选值（比如 0,2）报表回显时的问题<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5845Y">issues/I5845Y</a></li> 
 <li>配置 customPrePath 参数后，接口 excelQuery 访问报 400 错误<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1054" target="_blank">issues/1054</a></li> 
 <li>使用最小值函数 min, 在一列上面有 null 时，最小值永远是 0<a href="https://gitee.com/jeecg/JimuReport/issues/I5CD7F">issues/I5CD7F</a></li> 
 <li>钻取报表添加条件后点击进入超链接报错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1093" target="_blank">issues/1093</a></li> 
 <li>钻取联动条件框取值问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F1089" target="_blank">issues/1089</a></li> 
 <li>针对数据为空和异常，返回不同的提示<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5AGDX">issues/I5AGDX</a></li> 
 <li>驼峰字段的没有数据，手动把小写改为驼峰才显示数据<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5D36J">issues/I5D36J</a></li> 
 <li>大屏修改保护密码提示 "您没有权限"<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F876" target="_blank">issues/876</a></li> 
 <li>大屏数据源出错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F943" target="_blank">issues/943</a></li> 
 <li>在线大屏使用百度在线地图只加载静态数据，不加载 sql 数据<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I5BI2N">issues/I5BI2N</a></li> 
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
 <li>QQ 群：212391162</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JimuReport?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">永久免费，支持各种复杂报表，并且傻瓜式在线设计，非常的智能，低代码时代，这个是你的首选！</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用 SpringBoot 的脚手架项目，都可以快速集成</li> 
 <li>Web 版设计器，类似于 excel 操作风格，通过拖拽完成报表设计</li> 
 <li>通过 SQL、API 等方式，将数据源与模板绑定。同时支持表达式，自动计算合计等功能，使计算工作量降低</li> 
 <li>开发效率很高，傻瓜式在线报表设计，一分钟设计一个报表，又简单又强大</li> 
 <li>支持 ECharts，目前支持 28 种图表，在线拖拽设计，支持 SQL 和 API 两种数据源</li> 
 <li>支持分组、交叉，合计、表达式等复杂报表</li> 
 <li>支持打印设计（支持套打、背景打印等）可设置打印边距、方向、页眉页脚等参数 一键快速打印 同时可实现套打，不动产证等精准、无缝打印</li> 
 <li>大屏设计器支持几十种图表样式，可自由拼接、组合，设计炫酷大屏</li> 
 <li>可设计各种类型的单据、大屏，如出入库单、销售单、财务报表、合同、监控大屏、旅游数据大屏等</li> 
</ul> 
<p>#系统截图</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>报表设计器（专业一流 数据可视化，解决各类报表难题）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png" referrerpolicy="no-referrer"></li> 
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
 <li>图形报表（目前支持 28 种图表）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-3eda428ef182cb64a1a8e132e4bfeb87718.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-22096123c5b6a10a801967c33cc33a7af11.png" referrerpolicy="no-referrer"></li> 
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
│  │  └─不动产证打印
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
   └─更多功能开发中。。</code></pre>
                                        </div>
                                      
</div>
            