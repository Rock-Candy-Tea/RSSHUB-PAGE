
---
title: 'JimuReport 积木报表 1.3.1 beta 版本发布，免费的 Web 报表工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 10:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p>积木报表，是一款免费的企业级Web报表工具，像搭建积木一样在线拖拽设计报表！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！<br> 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题。</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.3.1-beta2 | 2021-04-06</p> 
<p>#快速集成</p> 
<ul> 
 <li>引入依赖 jar</li> 
</ul> 
<pre style="text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>spring-boot-starter-jimureport<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.3.1-beta2<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<ul> 
 <li> <p>数据库脚本</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fblob%2Fmaster%2Fdb" target="_blank">jimureport.sql</a></p> </li> 
 <li> <p>详细集成文档</p> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></p> </li> 
</ul> 
<p>#代码下载</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul> 
 <li>技术官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
 <li>在线演示： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2Flogin" target="_blank">http://jimureport.com/login</a></li> 
 <li>技术文档： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com" target="_blank">http://report.jeecg.com</a></li> 
 <li>视频教程： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2Fdoc%2Fvideo" target="_blank">http://jimureport.com/doc/video</a></li> 
 <li>QQ群：212391162</li> 
</ul> 
<p>#升级日志</p> 
<blockquote> 
 <p>此版本变的更易集成，不再要求持久层必须mybits-plus，只要是SpringBoot2项目就可以快速简单集成。</p> 
</blockquote> 
<p>新功能</p> 
<ul> 
 <li>打印配置支持边距设置</li> 
 <li>持久层采用miniDao替换mybits-plus，不再要求持久层必须mybits-plus</li> 
 <li>自定义视图解析器，不再要求springboot必须用freeMark视图解析</li> 
 <li>报表支持javabean数据集</li> 
 <li>支持自定义header</li> 
 <li>图表联动功能实现</li> 
 <li>钻取功能实现</li> 
 <li>增加打印高清设置</li> 
</ul> 
<p>问题修复</p> 
<ul> 
 <li>api走打印全部的时候如果传printAll会查不出数据</li> 
 <li>只查询表名不查询字段，导致数据源会一直保存不上</li> 
 <li>图表联动不刷新标题bug</li> 
 <li>地图组件编辑在新增会是编辑的内容</li> 
 <li>数据源点击确定一直在加载中、SQL数据源多个参数的时候删除一个会变成字符串、api只解析$里面的</li> 
 <li>API带分页，打印、导出pdf和excel只显示一页处理</li> 
 <li>设计器页面样式调整</li> 
 <li>字典维护页面弹窗错乱处理</li> 
 <li>数据源走本地打印全部没数据</li> 
 <li>字典缓存逻辑有问题</li> 
 <li>sql解析的时候验证是否存在表，不在保存处做处理，不然会出现大数据问题</li> 
 <li>去掉total双引号，有的数据库会报错</li> 
 <li>查询框被遮住了</li> 
 <li>图表联动的时候，可以添加多个图表，钻取逻辑调整</li> 
 <li>导出excel报空指针问题</li> 
 <li>积木报表大屏登陆的时候出现token为空</li> 
 <li>当出现在inner join和and存在的时候，回将on后面也截取掉，导致后台报错</li> 
 <li>报表钻取不传参前台会报错</li> 
 <li>excel导出边框颜色问题</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>数据源是sql并且字段包含双引号报错 <a href="https://gitee.com/jeecg/JimuReport/issues/I395AA">issues/I395AA</a></li> 
 <li>可否增加打印清晰度默认值的设定 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F96" target="_blank">#96</a></li> 
 <li>数据格式为数值，当设置小数位数后，数据格式的千分符失效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F102" target="_blank">#102</a></li> 
 <li>上传excel文件，编辑有问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F108" target="_blank"> #108</a></li> 
 <li>报表打印的时候,使用的参数都是默认参数,导致无法打印当前请求的报表内容 <a href="https://gitee.com/jeecg/JimuReport/issues/I2KRVF">issues/I2KRVF</a></li> 
 <li>积木报表api数据源带参，解析时参数无效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2295" target="_blank">#2295</a></li> 
 <li>API数据集问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3B0O5">issues/I3B0O5</a></li> 
 <li>版本1.2.0 sql语句 字段表名 报表预览时查询total的双引号问题 <a href="https://gitee.com/jeecg/JimuReport/issues/I3DLWY">issues/I3DLWY</a></li> 
 <li>自定义打印尺寸241*140，点击打印报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F126" target="_blank">#126</a></li> 
 <li>是否支持主子表？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F34" target="_blank"> #34</a></li> 
 <li>使用postgresql 数据库存储报表数据bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F82" target="_blank"> #82</a></li> 
 <li>支持图表间的数据联动吗<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F84" target="_blank"> #84</a></li> 
 <li>无法根据查询条件打印 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F93" target="_blank">#93</a></li> 
 <li>打印全部：无法打印，带参查询出来的数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F99" target="_blank">#99</a></li> 
 <li>上传excel模板兼容性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F112" target="_blank"> #112</a></li> 
 <li>1.2.0版本导出excel问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F115" target="_blank">#115</a></li> 
 <li>内容太多超出边界，打印时少半截的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F121" target="_blank">#121</a></li> 
 <li>积木报表sql数据集，带参条件解析错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2306" target="_blank">#2306</a></li> 
 <li>oracle数据库中DATE类型字段无法显示短日期或长日期 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F130" target="_blank">#130</a></li> 
 <li>api数据源接口返回0条数据，但是报表依旧显示初始化的数据<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F104" target="_blank"> #104</a></li> 
 <li>sql解析成功但动态报表配置明细无法解析 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2305" target="_blank">#2305</a></li> 
 <li>使用oracle数据库时，无法创建报表（进入新建报表页面前就报错）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F73" target="_blank"> #73</a></li> 
 <li>积木报表，合并单元格的文字，预览显示不全<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2307" target="_blank"> #2307</a></li> 
 <li>SQL数据源报表，页面数据显示正常，导出excle，excle中无数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F123" target="_blank">#123</a></li> 
</ul> 
<h3 style="text-align:left">为什么选择 JimuReport?</h3> 
<blockquote> 
 <p>永久免费，支持各种复杂报表，并且傻瓜式在线设计，非常的智能，低代码时代，这个是你的首选！</p> 
</blockquote> 
<ul> 
 <li>采用SpringBoot+Mybatis-Plus的脚手架项目，都可以快速集成</li> 
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
│  │  └─纵向分组小计（预计2021.04.05）
│  │  └─合计
│  │  ├─交叉报表
│  │  ├─明细表
│  │  ├─带条件查询报表
│  │  ├─表达式报表
│  │  ├─带二维码/条形码报表
│  │  ├─多表头复杂报表（预计2021.04.05发布）
│  │  ├─主子报表
│  │  ├─预警报表（预计2021.04.05发布）
│  │  ├─数据钻取报表（预计2021.04.05发布）
│  ├─图形报表
│  │  ├─柱形图
│  │  ├─折线图
│  │  ├─饼图
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
            