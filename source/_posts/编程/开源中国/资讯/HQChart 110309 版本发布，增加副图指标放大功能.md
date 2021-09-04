
---
title: 'HQChart 1.10309 版本发布，增加副图指标放大功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-085c5ec476e3324dbeb667a22ef2b1b30d5.gif'
author: 开源中国
comments: false
date: Sat, 04 Sep 2021 06:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-085c5ec476e3324dbeb667a22ef2b1b30d5.gif'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><strong>系统简介</strong></p> 
<p style="text-align:left">HQChart是国内第1个基于传统PC股票客户端软件(C++)移植到js/py平台的一个项目, 包含K线图图形库及麦语法(分析家语法)指标执行器.</p> 
<p style="text-align:left"><strong>平台支持：js, vue, uniapp, 小程序</strong></p> 
<p style="text-align:left"><strong>注意事项</strong></p> 
<ol> 
 <li style="text-align:left">由于HQChart是一个金融类的插件，所以请大家不要把插件使用在违法的地方。请根据<a href="https://gitee.com/jones2000/HQChart/blob/master/%E7%94%A8%E6%88%B7%E5%8D%8F%E8%AE%AE.txt">HQChart用户使用协议</a>文明使用插件.</li> 
 <li style="text-align:left">HQChart内置数据源仅供开发测试使用，请不要使用在任何商业用途。目前内置数据源已取消跨域功能。本地调试请参考教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F120008624" target="_blank">解决Chrome本地调试跨域</a>， 如果是VUE请使用127.0.0.1:8080 <span style="background-color:#ffffff; color:#40485b">站点调试</span></li> 
</ol> 
<p style="text-align:left"><strong>增加新功能</strong></p> 
<ol> 
 <li style="text-align:left">双击副图指标放大功能。设置详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F90272733" target="_blank">HQChart使用教程1- 如何快速创建一个K线图页面</a></li> 
 <li style="text-align:left">优化根据刻度文字自动调整左右边框间距。设置详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F90272733" target="_blank">HQChart使用教程1- 如何快速创建一个K线图页面</a></li> 
 <li style="text-align:left">自定义Y轴刻度支持2行文字输出。设置详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F103174483" target="_blank">HQChart使用教程50-Y轴自定义刻度设置说明</a></li> 
 <li style="text-align:left">增加HQChart用户使用协议。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fblob%2Fmaster%2F%25E7%2594%25A8%25E6%2588%25B7%25E5%258D%258F%25E8%25AE%25AE.txt" target="_blank">用户协议</a></li> 
</ol> 
<p style="text-align:left">双击副图指标放大</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-085c5ec476e3324dbeb667a22ef2b1b30d5.gif" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">自定义Y轴刻度支持2行文字输出</p> 
<p style="text-align:left"><img alt height="653" src="https://oscimg.oschina.net/oscnet/up-5ce6550be8a8b83665e82be62fbac737e76.png" width="1423" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>10309 小程序修正分时图ChartStickLine柱子太粗了。</li> 
 <li>10305 修正uniapp分时图指标工具栏$报错</li> 
 <li>10302 修正OnTouchDBClick()手势坐标没有转换到K线图相对坐标</li> 
 <li>10285 修正DrawInsideHorizontal，DrawCustomHorizontal没有处理最小化窗口指标</li> 
 <li>10284 小程序增加双击副图缩放指标窗口</li> 
</ul> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p style="text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:left"><strong>源码地址：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="text-align:left"><strong>源码地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="text-align:left"><strong>uniapp插件地址: </strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="text-align:left"><strong>个人博客: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p> 
<p style="text-align:left"><strong>QQ交流群: 950092318</strong></p>
                                        </div>
                                      
</div>
            