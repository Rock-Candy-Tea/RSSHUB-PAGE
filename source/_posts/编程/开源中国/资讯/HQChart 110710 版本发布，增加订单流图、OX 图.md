
---
title: 'HQChart 1.10710 版本发布，增加订单流图、OX 图'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-61c1989f48b2db36b2cf418b5420a8032e0.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 12:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-61c1989f48b2db36b2cf418b5420a8032e0.png'
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
<p><strong style="color:#333333">增加新功能</strong></p> 
<ol> 
 <li>增加订单流图形，详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F122888661" target="_blank">HQChart使用教程30-K线图如何对接第3方数据32-订单流</a></li> 
 <li>增加OX图， 详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F122635700" target="_blank">HQChart使用教程86-技术指标OX图</a></li> 
 <li>指标引擎增加ANY, ALL函数</li> 
 <li>增加完全空心K线图</li> 
 <li>增加简单K线训练模式</li> 
 <li>指标函数WINNER, COST价格计算方位调整到0-5000</li> 
 <li>指标标题栏增加自定义图标按钮，详见教程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F122950050" target="_blank">HQChart实战教程50-自定义指标栏工具按钮</a></li> 
</ol> 
<p>订单流效果图</p> 
<p><img alt height="713" src="https://oscimg.oschina.net/oscnet/up-61c1989f48b2db36b2cf418b5420a8032e0.png" width="1360" referrerpolicy="no-referrer"></p> 
<p>OX图效果图</p> 
<p><img alt height="829" src="https://oscimg.oschina.net/oscnet/up-a5f3ad9631b3c17f626f47a100426661130.png" width="1676" referrerpolicy="no-referrer"></p> 
<p>指标栏自定义按钮</p> 
<p><img alt height="528" src="https://oscimg.oschina.net/oscnet/up-76575b5dc13d73b1d1abf05d13761f9c328.png" width="1408" referrerpolicy="no-referrer"></p> 
<p>完全空心K线图</p> 
<p><img alt height="753" src="https://oscimg.oschina.net/oscnet/up-2847b4049742cbada62fcebb5b44c136bbf.png" width="1376" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#333333">更新日志</strong></p> 
<ul> 
 <li>10710 JSUniAppCanvasHelper.MeasureText() 增加空格宽度</li> 
 <li>10708 K线训练增加自动调整左右边框间距</li> 
 <li>10706 KLineTrainSimpleChartContainer中RightSpaceCount强制设置为0</li> 
 <li>10705 小程序增加 “简单K线训练”</li> 
 <li>10704 小程序去掉"简单图形"，'雷达图'，"饼图"， '地图'。 只做K线，通用图形不做</li> 
 <li>10703 增加 KLineTrainSimpleChartContainer</li> 
 <li>10701 小程序X，Y轴分割线支持样式自定义</li> 
 <li>10697 小程序K线支持阴线阳新都为空心柱</li> 
 <li>10695 右键菜单K线类型增加空心阳线阴线</li> 
 <li>10693 K图支持完全空心K线柱</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址1：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址2：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp插件地址:：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>第3方数据对接例子：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart-Super" target="_blank">https://github.com/jones2000/HQChart-Super</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客:：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p>
                                        </div>
                                      
</div>
            