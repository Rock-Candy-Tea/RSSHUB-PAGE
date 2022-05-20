
---
title: 'HQChart 1.11027 版本发布，增加指标图形拖拽，报价列表，成交明细表'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f438cee4584531c29988719aa0ecd48f7c7.gif'
author: 开源中国
comments: false
date: Fri, 20 May 2022 04:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f438cee4584531c29988719aa0ecd48f7c7.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统简介</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">HQChart 是国内第 1 个基于传统 PC 股票客户端软件 (C++) 移植到 js/py 平台的一个项目，包含 K 线图图形库及麦语法 (分析家语法) 指标执行器.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>平台支持：js, vue, uniapp, 小程序</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>注意事项</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left">由于 HQChart 是一个金融类的插件，所以请大家不要把插件使用在违法的地方。请根据<span> </span><a href="https://gitee.com/jones2000/HQChart/blob/master/%E7%94%A8%E6%88%B7%E5%8D%8F%E8%AE%AE.txt">HQChart 用户使用协议</a>文明使用插件.</li> 
 <li style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F123170153" target="_blank">HQChart 商业使用说明及用户使用协议</a></li> 
 <li style="text-align:left">HQChart 内置数据源仅供开发测试使用，请不要使用在任何商业用途。目前内置数据源已取消跨域功能。本地调试请参考教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjones2000.blog.csdn.net%2Farticle%2Fdetails%2F120008624" target="_blank">解决 Chrome 本地调试跨域</a>， 如果是 VUE 请使用 127.0.0.1:8080<span> </span><span style="background-color:#ffffff; color:#40485b">站点调试</span></li> 
</ol> 
<p><strong style="color:#333333">增加新功能</strong></p> 
<ol> 
 <li>增加台湾,日本股票后缀</li> 
 <li>量比支持多日分时图数据。详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F124286883" target="_blank">HQChart使用教程29-走势图如何对接第3方数据8-量比数据</a> </li> 
 <li>增加分笔明细图,分价表图. 详见教程<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F124360747" target="_blank">HQChart使用教程92-如何创建分笔明细表</a></li> 
 <li>K线面积图把最左边的空隙补上</li> 
 <li>增加报价列表图(h5,小程序,uniapp)。详见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000%2Farticle%2Fdetails%2F124544643" target="_blank">HQChart使用教程94-如何创建报价列表</a></li> 
 <li>增加图形选中功能</li> 
 <li>增加指标图形拖拽</li> 
 <li>增加选中图形键盘del删除功能</li> 
</ol> 
<p>指标图形拖拽效果图</p> 
<p><br> <img alt src="https://oscimg.oschina.net/oscnet/up-f438cee4584531c29988719aa0ecd48f7c7.gif" referrerpolicy="no-referrer"></p> 
<p>报价列表效果图</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7c0bcc22725e6ac8e6865ed78f78354604f.gif" referrerpolicy="no-referrer"></p> 
<p>多日量比数据图效果图</p> 
<p><img alt height="1130" src="https://oscimg.oschina.net/oscnet/up-4097df2a41271acd3d22f1021b0ffee1892.png" width="2384" referrerpolicy="no-referrer"></p> 
<p>成交明细表格效果图</p> 
<p><img alt height="1072" src="https://oscimg.oschina.net/oscnet/up-be0ea22f3f5403e7ecd78879b790b00d7c2.png" width="2188" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong style="color:#333333">更新日志</strong></p> 
<ul> 
 <li>11016 分时图增加背景标题扩展画法</li> 
 <li>11014 报价列表重绘接口开放</li> 
 <li>11012 报价列表右键事件增加内部坐标</li> 
 <li>10839 修正画图工具黄金分割线横屏显示错误</li> 
 <li>10819 小程序 MAX(), MIN() 支持多个变量比较</li> 
 <li>10818 小程序 JSAlgorithm::Add(), JSAlgorithm::Subtract(), JSAlgorithm:: Multip() 修正判断数字逻辑错误</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更新日志详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart%2Fcommits%2Fmaster" target="_blank">https://github.com/jones2000/HQChart/commits/master</a></p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在线演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource2.zealink.com%2Fvuehqweb%2Fhq.demo.page.html" target="_blank">https://opensource2.zealink.com/vuehqweb/hq.demo.page.html</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://oscimg.oschina.net/oscnet/up-135d2e548fbce46ff870a3b78f0ec4aa7e6.png" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址 1：<a href="https://gitee.com/jones2000/HQChart">https://gitee.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码地址 2：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart" target="_blank">https://github.com/jones2000/HQChart</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>uniapp 插件地址:：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D4591" target="_blank">https://ext.dcloud.net.cn/plugin?id=4591</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>第 3 方数据对接例子：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjones2000%2FHQChart-Super" target="_blank">https://github.com/jones2000/HQChart-Super</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>个人博客:：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fjones2000" target="_blank">https://blog.csdn.net/jones2000</a></strong></p>
                                        </div>
                                      
</div>
            