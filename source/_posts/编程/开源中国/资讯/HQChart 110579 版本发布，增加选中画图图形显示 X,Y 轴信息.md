
---
title: 'HQChart 1.10579 版本发布，增加选中画图图形显示 X,Y 轴信息'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6e36294775100df0ecd1eb209e7c8fd62a8.gif'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 13:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6e36294775100df0ecd1eb209e7c8fd62a8.gif'
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>增加新功能</strong></p> 
<ol> 
 <li>增加ON_PHONE_TOUCH事件支持分时图</li> 
 <li>增加新建自定义指标窗口接口 AddScriptIndexWindow</li> 
 <li>增加北交所市场</li> 
 <li>深度图支持多语言</li> 
 <li>增加深证交易所股票期权 .SZO</li> 
 <li>增加选中画图图形显示X，Y轴坐标信息</li> 
 <li>修正K线上影线和下影线有时候不居中的问题</li> 
 <li>指标脚本引擎增加TFILTER函数</li> 
</ol> 
<p>选中画图图形显示X，Y轴坐标信息效果图</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6e36294775100df0ecd1eb209e7c8fd62a8.gif" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong style="color:#333333">更新日志</strong></p> 
<ul> 
 <li>10578 小程序增加深证交易所股票期权 .SZO</li> 
 <li>10577 小程序 DRAWICON支持FONTSIZE参数</li> 
 <li>10576 DRAWICON 支持 FONTSIZE参数</li> 
 <li>10574 增加 深证股票期权10572 分时图支持选中画图图形显示X，Y轴坐标信息</li> 
 <li>10570 修正DrawDrawPictureXCoordinate() 变量未定义报错</li> 
 <li>10568 画图工具选中增加X，Y轴坐标信息</li> 
 <li>10566 小程序增加TFILTER</li> 
 <li>10565 修改TFILTER算法</li> 
 <li>10552 小程序 JSChart.SetUSATimeType()</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp插件地址: </strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            