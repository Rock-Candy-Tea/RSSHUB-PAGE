
---
title: 'HQChart 1.10594 版本发布，增加飞狐函数 SYSPARAM() 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fb235fb613bb6d01cd62dfd1b492bd5fac6.png'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 12:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fb235fb613bb6d01cd62dfd1b492bd5fac6.png'
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
 <li>DRAWBAND绘图函数支持横屏</li> 
 <li>叠加指标共享Y轴增加是否调整共享Y轴数值选项</li> 
 <li>画图工具选中点支持方框模式</li> 
 <li>支持飞狐函数SYSPARAM(2)，主图可见K线最初位置.</li> 
 <li>支持飞狐函数SYSPARAM(3)，主图可见K线最后位置.</li> 
 <li>支持飞狐函数SYSPARAM(4)，主图可见K线最高价</li> 
 <li>支持飞狐函数SYSPARAM(5)，主图可见K线最低价.</li> 
</ol> 
<div> 
 <div>
   
 </div> 
 <div>
  <span>DRAWBAND横屏效果</span>
 </div> 
 <div>
  指标脚本：
  <span>DRAWBAND(OPEN,RGB(0,224,224),CLOSE,RGB(255,96,96));</span>
 </div> 
 <div>
  <span><img alt height="677" src="https://oscimg.oschina.net/oscnet/up-fb235fb613bb6d01cd62dfd1b492bd5fac6.png" width="380" referrerpolicy="no-referrer"></span>
 </div> 
 <div>
   
 </div> 
 <div> 
  <p>画图工具选中点为方框效果图</p> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-7fe8bb9501c77f950be978153e7f0e4f2f2.gif" referrerpolicy="no-referrer"></p> 
  <p>飞狐SYSPARAM函数效果，K线缩放移动都会触发指标重新计算</p> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-2d4f51d33b9eead50b0c6caa096555ba0b2.gif" referrerpolicy="no-referrer"></p> 
  <p> </p> 
  <p><strong style="color:#333333">更新日志</strong></p> 
  <ul> 
   <li>10588 DRAWBAND支持横屏</li> 
   <li>10587 增加K线缩放拖拽以后触发指标计算配置</li> 
   <li>10585 增加画布工具点搜否始终显示选项</li> 
   <li>10583 画图工具选中点支持方框模式</li> 
   <li>10582 内置画图工具设置菜单支持rgb颜色</li> 
  </ul> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp插件地址: </strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            