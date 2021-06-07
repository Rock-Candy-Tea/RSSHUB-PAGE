
---
title: 'JimuReport 积木报表 1.3.4 版本发布，可视化报表工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 09:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p>积木报表，是一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计报表！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，重点此软件是完全免费的！！！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.3.4-beta | 2021-06-07</p> 
<p>集成依赖</p> 
<pre style="text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>spring-boot-starter-jimureport<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.3.4-beta<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="text-align:left">增量SQL</p> 
<pre style="text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_link`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`link_chart_id`</span> varchar(50) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'联动图表的ID'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`api_url`</span>;

<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`api_convert`</span> varchar(255) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'api转换器'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`json_data`</span>;
</code></pre> 
<p>#升级日志</p> 
<p>新功能</p> 
<ul> 
 <li>图表支持javaBean和JSON数据集</li> 
 <li>HTML打印模式支持图表和图片打印</li> 
 <li>支持主子报表</li> 
 <li>导出excel图片位置问题解决</li> 
 <li>图表联动改造</li> 
 <li>兼容mariadb数据库</li> 
 <li>undertow集成导出报错 gitee I3R92I、I3NSQK、I3O1R2 github 238、255、224</li> 
 <li>导出excel api可以导出当前页，导出全部可以用printAll</li> 
 <li>预览页面token问题</li> 
 <li>预览页面每页显示数量下拉框支持自定义</li> 
 <li>地图做成下拉选择的，不需要手工配置了</li> 
 <li>预览页面mysql解密函数解密后的数据不正常显示github 262</li> 
 <li>查询条件能否支持输入检索功能 github #256、查询框大小不一致 github #257</li> 
 <li>sql解析失败，采用弹窗填参数方式</li> 
 <li>excel大数据导出,excel分sheet导出,小于1000的才设置样式，大于1000的设置默认样式</li> 
 <li>钻取支持返回上一页</li> 
 <li>支持api转换器</li> 
 <li>excel导入支持xls</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>图表联动无法绑定 上传封面功能没有开发完吗<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F214" target="_blank"> #214</a></li> 
 <li>版本由1.2.0升级到了1.3.21-beta ---报表列表查询-分页字段 <a href="https://gitee.com/jeecg/JimuReport/issues/I3QJKH">issues/I3QJKH</a></li> 
 <li>无法获取将系统日期#&#123;sys_date&#125;作为默认查询条件，现在这个可以实现吗 <a href="https://gitee.com/jeecg/JimuReport/issues/I3RDCP">issues/I3RDCP</a></li> 
 <li>地图使用静态数据无变化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2528" target="_blank"> #2528</a></li> 
 <li>报表预览的时候，有时候加载时间较长，能不能加一个loading的提示，长时间空白，感觉有点像bug<a href="https://gitee.com/jeecg/JimuReport/issues/I3OGJ7">issues/I3OGJ7</a></li> 
 <li>导出EXCEL时，出现操作失败:1,根据后台显示应该是数组越界 <a href="https://gitee.com/jeecg/JimuReport/issues/I3IT1X">issues/I3IT1X</a></li> 
 <li>undertow容器，excel导出功能不好使 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F255" target="_blank">#255</a></li> 
 <li>linux导出excel报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F238" target="_blank">#238</a></li> 
 <li>报表主页的预览模版功能，点击后跳转页面未携带Token<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F218" target="_blank"> #218</a></li> 
 <li>导出excel,不能分页! <a href="https://gitee.com/jeecg/JimuReport/issues/I3NPN2">issues/I3NPN2</a></li> 
 <li>导出excel出现异常<a href="https://gitee.com/jeecg/JimuReport/issues/I3NSQK">issues/I3NSQK</a></li> 
 <li>查询条件能否支持输入检索功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F262" target="_blank">#256</a></li> 
 <li>查询框大小不一致 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F257" target="_blank">#257</a></li> 
 <li>字典动态获取 <a href="https://gitee.com/jeecg/JimuReport/issues/I3S172">issues/I3S172</a></li> 
 <li>sql结果集中某字段有json格式数据时数据报表预览报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F270" target="_blank">#270</a></li> 
 <li>打印字迹，模糊 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F286" target="_blank">#286</a></li> 
 <li>积木报表不支持MYSQL内置函数，视图解析时出错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F277" target="_blank">#277</a></li> 
 <li>导出excel时，图片未导出<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F230" target="_blank"> #230</a></li> 
 <li>表格小数点数值为0,设置显示位数无效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F136" target="_blank">#136</a></li> 
 <li>查询栏查询时间类型及范围查找，无法显示默认值 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SN3P">issues/I3SN3P</a></li> 
 <li>钻取到下一页面，能否增加返回到上一页操作 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SL05">issues/I3SL05</a></li> 
 <li>图表联动可以看到已删除的图标 <a href="https://gitee.com/jeecg/JimuReport/issues/I3SEV4">issues/I3SEV4</a></li> 
 <li>列比较多，编辑时列只显示到AX列，后面的列没显示出来造成无法进行修改 <a href="https://gitee.com/jeecg/JimuReport/issues/I3RQIT">issues/I3RQIT</a></li> 
 <li>对每页10条的选项改成没有20信息后，打印和导出的数据数量都不对，都是10条</li> 
 <li>sql数据集中SQL解析失败问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3NCM7">issues/I3NCM7</a></li> 
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
   └─更多功能开发中。。</code></pre>
                                        </div>
                                      
</div>
            