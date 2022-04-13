
---
title: 'HQChart 1.10807 版本发布，DRAWTEXT,DRAWICON 函数功能扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1fd53c42744bc836d28288072393aa96334.gif'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 12:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1fd53c42744bc836d28288072393aa96334.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统简介</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">HQChart是国内第1个基于传统PC股票客户端软件(C++)移植到js/py平台的一个项目, 包含K线图图形库及麦语法(分析家语法)指标执行器.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>平台支持：js, vue, uniapp, 小程序</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>注意事项</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left">由于HQChart是一个金融类的插件，所以请大家不要把插件使用在违法的地方。请根据<a href="https://gitee.com/jones2000/HQChart/blob/master/%E7%94%A8%E6%88%B7%E5%8D%8F%E8%AE%AE.txt">HQChart用户使用协议</a>文明使用插件.</li> 
 <li style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F123170153" target="_blank">HQChart商业使用说明及用户使用协议</a></li> 
 <li style="text-align:left">HQChart内置数据源仅供开发测试使用，请不要使用在任何商业用途。目前内置数据源已取消跨域功能。本地调试请参考教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F120008624" target="_blank">解决Chrome本地调试跨域</a>， 如果是VUE请使用127.0.0.1:8080<span> </span><span style="background-color:#ffffff; color:#40485b">站点调试</span></li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">增加新功能</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>HQChart增加商用使用说明,详见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F123170153" target="_blank">HQChart商业使用说明及用户使用协议</a></li> 
 <li>DRAWICON支持小程序/app绘制图片，详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F124140916" target="_blank">HQChart使用教程91-如何在app中使用DRAWICON绘制图片</a></li> 
 <li>DRAWTEXT支持背景色，连线等设置, 详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F123132528" target="_blank">HQChart使用教程88-DRAWTEXT添加背景色及边框</a>， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F123750892" target="_blank">HQChart使用教程90-DRAWTEXT添加连线</a></li> 
 <li>K线支持最后一根k线倒计时功能(呼吸灯), 详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F123674077" target="_blank">HQChart使用教程89-最后一根k线倒计时功能</a></li> 
 <li>增加指标EMA</li> 
 <li>H5增加叠加K线历史数据拖拽下载</li> 
 <li>小程序增加叠加日线历史数据拖拽下载</li> 
 <li>K线图增加键盘Ctrl+(left/right)移动十字光标</li> 
</ol> 
<p>DRAWICON在app上效果</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1fd53c42744bc836d28288072393aa96334.gif" referrerpolicy="no-referrer"></p> 
<p>DRAWTEXT增加功能效果图</p> 
<p><img alt height="645" src="https://oscimg.oschina.net/oscnet/up-d5cf508f30efe2c711ab5abf82fc4beda5c.png" width="1288" referrerpolicy="no-referrer"></p> 
<p>K线呼吸灯效果</p> 
<p><img alt height="494" src="https://oscimg.oschina.net/oscnet/up-1195c02df5b3d8a012153988fd546147e19.gif" width="374" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">更新日志</strong></p> 
<ul> 
 <li>10795 切换股票和周期增加图形销毁函数</li> 
 <li>10796 切换指标增加图形销毁事件</li> 
 <li>10797 ChartMultiHtmlDom增加销毁标识</li> 
 <li>10799 小程序增加指标图形销毁事件</li> 
 <li>10800 小程序增加DRAWICON外部绘图绑定事件</li> 
 <li>10801 小程序分时图增加ON_PHONE_TOUCH事件支持</li> 
 <li>10802 小程序修正分时图ON_PHONE_TOUCH事件没有更新x,y坐标。</li> 
 <li>10784 K线图增加键盘Ctrl+(left/right)移动十字光标</li> 
 <li>10781 修正新版DRAWNUMBER读取配置错误</li> 
 <li>10780 小程序DRAWTEXT, DRAWNUMBER函数重构，增加支持CKLINE</li> 
 <li>10778 重构DRAWNUMBER函数，支持BACKGROUND,CKLINE。</li> 
 <li>10776 DRAWTEXT增加连线功能</li> 
 <li>10773 小程序增加K线倒计时接口</li> 
 <li>10772 K线倒计时支持框架内坐标</li> 
 <li>10770 增加K线最新数据倒计时时间接口</li> 
 <li>10767 增加EMA指标</li> 
 <li>10766 增加EMA3， EMA4， EMA5，EMA6指标</li> 
 <li>10765 小程序EMA周期支持数组</li> 
 <li>10764 EMA周期为0是，返回无效数</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更多更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址1：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址2：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp插件地址:：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>第3方数据对接例子：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart-Super" target="_blank">https://github.com/jones2000/HQChart-Super</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客:：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p>
                                        </div>
                                      
</div>
            