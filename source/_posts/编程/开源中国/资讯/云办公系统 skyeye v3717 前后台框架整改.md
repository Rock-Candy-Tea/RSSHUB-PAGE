
---
title: '云办公系统 skyeye v3.7.17 前后台框架整改'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5ed8c1b1cc6dd6109e9c3e0edcc802bd5fb.png'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 09:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5ed8c1b1cc6dd6109e9c3e0edcc802bd5fb.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">智能办公 OA 系统 [SpringBoot2 - 快速开发平台]，适用于医院，学校，中小型企业等机构的管理。包含文件在线操作、工作日志、多班次考勤、CRM、ERP 进销存、项目管理、EHR、拖拽式生成问卷、日程、笔记、工作计划、行政办公、薪资模块、动态表单、知识库、公告模块、企业论坛、云售后模块、生产模块、系统模块化同步模块等多种复杂业务功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">云办公系统 skyeye v3.7.17</span><span style="color:#333333"><span> </span>发布</span><span style="color:#333333"> ，</span>更新内容：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>US：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left">前台新增上传工具类配置函数</li> 
 <li style="text-align:left">前台新增tagEditor重置数据以及清空数据的配置函数</li> 
 <li style="text-align:left">前台新增表格类型的数据填充加载工具，主要用于ERP，CRM以及工作流等</li> 
 <li style="text-align:left">新增数据字典功能，删除多余的类型、分类等配置功能</li> 
 <li style="text-align:left">后台框架接口获取入参的方式修改</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">erp：</span> <a href="https://gitee.com/doc_wei01/erp-pro">https://gitee.com/doc_wei01/erp-pro</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">OA： <a href="https://gitee.com/doc_wei01/skyeye">https://gitee.com/doc_wei01/skyeye</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">报表：<a href="https://gitee.com/doc_wei01/skyeye-report">https://gitee.com/doc_wei01/skyeye-report</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">企业版信息： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDQlRxcVRMWWVjbU1i%3F_from%3D1%26disableReturnList%3D1" target="_blank">https://docs.qq.com/doc/DQlRxcVRMWWVjbU1i?_from=1&disableReturnList=1</a> ，有问题可以联系作者，详情请看开发计划。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">效果图</h4> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>效果图</th> 
   <th>效果图</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> <p style="margin-left:0; margin-right:0"><img height="1874" src="https://oscimg.oschina.net/oscnet/up-5ed8c1b1cc6dd6109e9c3e0edcc802bd5fb.png" width="3840" referrerpolicy="no-referrer"></p> </td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> <p style="margin-left:0; margin-right:0"><img height="1874" src="https://oscimg.oschina.net/oscnet/up-897ade8bb3f620af49f3b328246d2a17527.png" width="3840" referrerpolicy="no-referrer"></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left; white-space:normal"> <p style="margin-left:0; margin-right:0"><img height="1874" src="https://oscimg.oschina.net/oscnet/up-663ccf58463169bc534f976c5bb82ff53d4.png" width="3840" referrerpolicy="no-referrer"></p> </td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left; white-space:normal"> <p style="margin-left:0; margin-right:0"><img height="1874" src="https://oscimg.oschina.net/oscnet/up-144b56569c2d2b84ef4a7c9c440ee24ddbc.png" width="3840" referrerpolicy="no-referrer"></p> </td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            