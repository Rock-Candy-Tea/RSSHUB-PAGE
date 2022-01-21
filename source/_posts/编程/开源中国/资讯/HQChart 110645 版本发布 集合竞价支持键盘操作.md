
---
title: 'HQChart 1.10645 版本发布 集合竞价支持键盘操作'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-64edec2060bad945fe69138a391a950be68.gif'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 12:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-64edec2060bad945fe69138a391a950be68.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统简介</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">HQChart是国内第1个基于传统PC股票客户端软件(C++)移植到js/py平台的一个项目, 包含K线图图形库及麦语法(分析家语法)指标执行器.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>平台支持：js, vue, uniapp, 小程序</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>注意事项</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left">由于HQChart是一个金融类的插件，所以请大家不要把插件使用在违法的地方。请根据<a href="https://gitee.com/jones2000/HQChart/blob/master/%E7%94%A8%E6%88%B7%E5%8D%8F%E8%AE%AE.txt">HQChart用户使用协议</a>文明使用插件.</li> 
 <li style="text-align:left">HQChart内置数据源仅供开发测试使用，请不要使用在任何商业用途。目前内置数据源已取消跨域功能。本地调试请参考教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F120008624" target="_blank">解决Chrome本地调试跨域</a>， 如果是VUE请使用127.0.0.1:8080<span> </span><span style="background-color:#ffffff; color:#40485b">站点调试</span></li> 
</ol> 
<p style="text-align:left"><strong style="color:#333333">增加新功能</strong></p> 
<ol> 
 <li>分时图集合竞价区域支持键盘左右移动</li> 
 <li>增加收盘价线宽度设置</li> 
 <li>增加指标名字和参数之间的距离设置参数</li> 
 <li>分时图最后一个数据支持显示最后的更新时间</li> 
 <li>小程序增加K线绘制最后的K线信息回调. 详见教程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F118774299" target="_blank">HQChart实战教程43-K线面积图最后一个数据增加动画点</a></li> 
 <li>秒周期支持拖拽下载数据</li> 
 <li>增加动态增加自定义指标脚本窗口. 详见教程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F90301000" target="_blank">HQChart使用教程5- K线图控件操作函数说明</a></li> 
</ol> 
<p> </p> 
<p>集合竞价键盘移动效果图</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-64edec2060bad945fe69138a391a950be68.gif" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>最后一根K线绘制回调app端应用效果图</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-241c693699fe96ef8c2a9097fd0c93afcd9.gif" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#333333">更新日志</strong></p> 
<ul> 
 <li>10599 OnKLinePageChange() 增加叠加指标</li> 
 <li>10604 秒周期支持拖拽下载数据</li> 
 <li>10606 小程序 KLineChartContainer::DragDownloadData() 支持秒周期下载</li> 
 <li>10618 小程序修正ChartData::MergeMinuteData() 当历史数据为空时合并数据报错</li> 
 <li>10617 修正ChartData::MergeMinuteData() 当历史数据为空时，合并数据报错</li> 
 <li>10613 小程序 DynamicChartTitlePainting::FullDraw() 增加指标名字与参数之间的间距设置</li> 
 <li>10612 增加指标名字和参数之间的距离设置参数</li> 
 <li>10611 小程序指标名字颜色使用单独的配色</li> 
 <li>10609 分时图标题增加总是显示最后的分时数据配置</li> 
 <li>10642 小程序增加AddScriptIndexWindow(), AddAPIIndexWindow()</li> 
 <li>10640 增加AddAPIIndexWindow</li> 
 <li>10645 小程序增加ON_DRAW_KLINE_LAST_POINT事件</li> 
 <li>10643 分时图支持集合竞价区域键盘移动十字光标</li> 
</ul> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp插件地址: </strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            