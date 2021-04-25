
---
title: 'Catchadmin 发布 v2.6.1 小版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://svg.hamm.cn/gitee.svg?type=star&user=jaguarjack&project=catchAdmin'
author: 开源中国
comments: false
date: Sun, 25 Apr 2021 09:10:00 GMT
thumbnail: 'https://svg.hamm.cn/gitee.svg?type=star&user=jaguarjack&project=catchAdmin'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><code>CatchAdmin</code>是一款基于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.thinkphp.cn%2F" target="_blank">thinkphp framework</a>和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin%2F" target="_blank">element admin</a>二次开发而成后台管理系统。因为 thinkphp 的简单高效，文档齐全。在看了很多 thinkphp 生态中的后台管理系统，发现没有一款合适的前后端分离系统。遂开发了 CatchAdmin。 完全利用了 thinkphp6 的新版本特性 ServiceProvider，将管理系统模块之间的耦合降到了最低限度。不同于其他后台管理框架，CatchAdmin 讲每个功能模块作为最小单元，每个模块都有独立的 controller，路由，模型，数据表，尽可能将模块之间的影响降到最低，降低了模块之间耦合度。基于 CatchAdmin 可以开发 cms，CRM，OA 等 等系统。也封装了很多实用的工具，提升开发体验。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.catchadmin.com%2F" target="_blank">文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.catchadmin.com%2F" target="_blank">演示地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fapidoc.catchadmin.com%2F" target="_blank">接口文档</a> | <a href="https://gitee.com/jaguarjack/catchAdmin">项目源码</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fakasishikelu%2Fthinkphp6" target="_blank">看云分析</a> <a href="https://www.oschina.net/news/118798/catchadmin-2-2-released#extensions">扩展</a></p> 
<p style="text-align:left"><a href="https://gitee.com/jaguarjack/catchAdmin" target="_blank"><img src="https://svg.hamm.cn/gitee.svg?type=star&user=jaguarjack&project=catchAdmin" referrerpolicy="no-referrer"> </a><a href="https://gitee.com/jaguarjack/catchAdmin" target="_blank"><img src="https://svg.hamm.cn/gitee.svg?type=fork&user=jaguarjack&project=catchAdmin" referrerpolicy="no-referrer"> </a><img src="https://svg.hamm.cn/badge.svg?key=Base&value=ThinkPHP6" referrerpolicy="no-referrer"> <img src="https://svg.hamm.cn/badge.svg?key=Data&value=MySQL5.5" referrerpolicy="no-referrer"> <img src="https://svg.hamm.cn/badge.svg?key=Runtime&value=PHP7.1" referrerpolicy="no-referrer"> <img src="https://svg.hamm.cn/badge.svg?key=License&value=Apache-2.0" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>更新</strong></p> 
<p style="text-align:left"><strong>v2.6 版本重构了前台页面，使用后台的 Json 是来渲染前端的表格和表单，大大提升了开发效率。</strong></p> 
<ol> 
 <li> <p>修复组件切换导致 JS 报错，页面会卡顿</p> </li> 
 <li> <p>支持创建菜单的 reseful 快捷方式</p> </li> 
 <li> <p>新增获取省市区数据命令</p> </li> 
 <li> <p>优化基础组件</p> </li> 
 <li> <p>新增导入组件</p> </li> 
 <li> <p>新增导出组件</p> </li> 
 <li> <p>新增模型导入方法</p> </li> 
 <li> <p>更新前端 catch-table 组件</p> </li> 
 <li> <p>....<br> <strong>预览</strong></p> </li> 
</ol> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083332_Qfg6.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083333_KxE7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083334_a1lH.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083335_PLfh.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083335_BDPu.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083336_Q8z0.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083337_mGIU.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083338_xr7X.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083338_X22n.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083338_hCqG.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083340_mf0q.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083340_omXJ.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083341_QKI7.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://static.oschina.net/uploads/img/202009/11083342_5Qq4.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.catchadmin.com%2F" target="_blank">体验地址</a></strong></p> 
<p style="text-align:left">- 账号: catch@admin.com</p> 
<p style="text-align:left">- 密码: catchadmin</p>
                                        </div>
                                      
</div>
            