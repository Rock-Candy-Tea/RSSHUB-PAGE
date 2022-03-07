
---
title: 'JimuReport 积木报表 v1.4.3 版本发布，免费的可视化低代码报表'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Mon, 07 Mar 2022 09:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                                            <p>项目介绍</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.4.3 | 2022-03-07</p> 
<p>集成依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>jimureport-spring-boot-starter<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.4.3<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p>#升级日志</p> 
<p>重点新功能及问题修复</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>pdf导出支持换行</li> 
 <li>支持自定义表达式</li> 
 <li>数据集默认选中分页</li> 
 <li>新建积木报表处理extJson参数配置常量类及命名修改</li> 
 <li>升级minidao版本，解决含limit的sql分页问题</li> 
 <li>地图不定时刷新初始化预览页面时刷新图表</li> 
 <li>数值格式化默认不设置小数位数</li> 
 <li>空指针异常处理</li> 
 <li>金额设置小数位无效</li> 
 <li>mongodb、redis数据源配置问题</li> 
 <li>纵向分组未设置小计的列支持添加条件颜色表达式</li> 
 <li>http请求链接报错异常输出格式优化、默认超时改成5000</li> 
 <li>百分比问题处理/百分比支持小数位设置</li> 
 <li>db连接错误3次以上，禁止访问数据库连接</li> 
 <li>解决上传封面问题</li> 
 <li>list转大写如果为空会报空指针</li> 
 <li>存储过程问题修复</li> 
</ul> 
<p>Issues处理</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>导出的excel百分比显示异常<a href="https://gitee.com/jeecg/JimuReport/issues/I4L9Y6">#I4L9Y6</a></li> 
 <li>钻取跳转携带token<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I4JM0I">#I4JM0I</a></li> 
 <li>允许反射对象修改访问权限修饰符，注释掉<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F689" target="_blank">#689</a></li> 
 <li>添加JAVABean数据集时，编码检验出错，无法添加<span> </span><a href="https://gitee.com/jeecg/JimuReport/issues/I4KT5R">#I4KT5R</a></li> 
 <li>地图显示数据和实际数据不匹配<a href="https://gitee.com/jeecg/JimuReport/issues/I4JHCR">#I4JHCR</a></li> 
 <li>替换默认值和表达式,点击下拉框,并未显示待选项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F685" target="_blank">#685</a></li> 
 <li>添加图表弹窗中图表不显示<a href="https://gitee.com/jeecg/JimuReport/issues/I4GI3Q">#I4GI3Q</a></li> 
 <li>导出excel支持百分比、人民币、美元、欧元、小数支持小数设置<a href="https://gitee.com/jeecg/JimuReport/issues/I4K798">#I4K798</a></li> 
 <li>单元格没有数据，为空时点击单元格不跳转<a href="https://gitee.com/jeecg/JimuReport/issues/I4LLPY">#I4LLPY</a></li> 
 <li>报表查询列表排序不对<a href="https://gitee.com/jeecg/JimuReport/issues/I4LMXK">#I4LMXK</a></li> 
 <li>导出pdf,打印多传两个参数<a href="https://gitee.com/jeecg/JimuReport/issues/I4L9FY">#I4L9FY</a></li> 
 <li>x轴y轴新增最小值设置<a href="https://gitee.com/jeecg/JimuReport/issues/I4LZ63">#I4LZ63</a></li> 
 <li>动态列替换)->'' 修改成 )&#125;->&#125;<a href="https://gitee.com/jeecg/JimuReport/issues/I4MJSL">#I4MJSL</a></li> 
 <li>用工具类进行判断，不用apache，容易版本冲突<a href="https://gitee.com/jeecg/JimuReport/issues/I4MPJP">#I4MPJP</a></li> 
 <li>系统变量使用问题,如果token为空系统变量赋空值，不然freemark会报错<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F720" target="_blank">issues/720</a></li> 
 <li>做完的积木报表，预览生成的访问地址，默认都加了token=null<a href="https://gitee.com/jeecg/JimuReport/issues/I4SOSH">issues/I4SOSH</a></li> 
 <li>配置了customPrePath值，但分享链接中没有/test<a href="https://gitee.com/jeecg/JimuReport/issues/I4RQSO">issues/I4RQSO</a></li> 
 <li>在分组合计中在使用sum统计，统计结果翻倍<a href="https://gitee.com/jeecg/JimuReport/issues/I4QD7P">issues/I4QD7P</a></li> 
 <li>下拉框模糊查询显示问题,连续2次搜同一个汉字时 第二次之后就不显示了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F766" target="_blank">issues/766</a></li> 
 <li>添加数据源,测试连接提示成功,点击确定报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4PBBS">issues/I4PBBS</a></li> 
 <li>ApiDataConvertAdapter转换后 值为null字段的字段被清除<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F783" target="_blank">issues/783</a></li> 
 <li>SQL数据集里数据预览报错<a href="https://gitee.com/jeecg/JimuReport/issues/I4OXTC">issues/I4OXTC</a></li> 
 <li>SQL Server表名关键字查询失败<a href="https://gitee.com/jeecg/JimuReport/issues/I4STNJ">issues/I4STNJ</a></li> 
 <li>预览时候会多出一样空白行<a href="https://gitee.com/jeecg/JimuReport/issues/I4RJK7">issues/I4RJK7</a></li> 
 <li>参数渲染到报表值没有被翻译<a href="https://gitee.com/jeecg/JimuReport/issues/I4OJXM">issues/I4OJXM</a></li> 
 <li>存储过程无法被翻译成字典<a href="https://gitee.com/jeecg/JimuReport/issues/I4NZP4">issues/I4NZP4</a></li> 
 <li>加减乘除运算无效<a href="https://gitee.com/jeecg/JimuReport/issues/I4T4JS">issues/I4T4JS</a>、<a href="https://gitee.com/jeecg/JimuReport/issues/I4PWJL">issues/I4PWJL</a></li> 
 <li>图标联动失败,tomcat高版本不支持特殊格式，可以使用post请求<a href="https://gitee.com/jeecg/JimuReport/issues/I4R92U">issues/I4R92U</a>、<a href="https://gitee.com/jeecg/JimuReport/issues/I4OAUS">issues/I4OAUS</a></li> 
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
   └─更多功能开发中。。</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            