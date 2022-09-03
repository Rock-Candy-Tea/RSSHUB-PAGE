
---
title: 'bootx-platform v1.1.1 工作流上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6a021b64002a32c69c9f4c12b1c047f6b5c.png'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 13:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6a021b64002a32c69c9f4c12b1c047f6b5c.png'
---

<div>   
<div class="content">
                                                                                            <h2> 🍈项目介绍</h2> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a>，非常欢迎看看项目介绍留以及个<strong>Star</strong>呀🤺🤺🤺</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">基于Spring Boot框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。前端分为vue2版和vue3版，vue2使用</span><span style="background-color:#ffffff"> </span>ANTD PRO VUE<span style="background-color:#ffffff"> 作为脚手架，vue3使用 </span>Vben-Admin-Next<span style="background-color:#ffffff"> 作为脚手架（开发中）。 移动端使用 </span>Taro<span style="background-color:#ffffff"> vue3+TS为技术栈（开发中）。分布式版本 Bootx-Cloud（计划后期重启），尽请期待。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h2><span>🍒更新说明</span></h2> 
<p><span>从20年初就动手写工作流这块的东西，然后开头了之后就一直拖拖拖，直到22年都过去了一大半，终于开始填这个鸽了好久的坑，现在将工作流基础的功能进行了集成，下一步就是对这块进行打磨和完善了。</span></p> 
<h2>🚅 路线图</h2> 
<ul> 
 <li>工作流高级功能           9月 
  <ul> 
   <li>更灵活的节点用户配置，可配置部门领导、指定角色等</li> 
   <li>会签处理</li> 
   <li>串签处理</li> 
   <li>任意节点退回</li> 
   <li>关联消息通知</li> 
   <li>更方便与现有业务整合</li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#2e2e46">移动端脚手架 taro       10月</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#2e2e46">扩展新登录方式和管理策略</span></li> 
   <li><span style="background-color:#ffffff; color:#2e2e46">消息通知</span></li> 
   <li><span style="background-color:#ffffff; color:#2e2e46">任务处理</span></li> 
   <li><span style="background-color:#ffffff; color:#2e2e46">个人信息管理</span></li> 
  </ul> </li> 
</ul> 
<h2>🛠️本次功能更新</h2> 
<ul> 
 <li>增加最新版本flowable 6.7.2 工作流集成</li> 
 <li>增加bpmn.js流程设计器集成</li> 
 <li>增加流程模型管理功能</li> 
 <li>增加工作流流程关联动态表单功能</li> 
 <li>增加工作流流程节点人员基础分配配置</li> 
 <li>增加工作流任务委派给其他用户进行处理</li> 
 <li>增加工作流初步的驳回处理</li> 
 <li>增加工作流基本的流程进度展示</li> 
 <li>优化工作流ID生成器替换为Snowflake</li> 
 <li>优化工作流部署BPMN文件时不自动生成图片</li> 
 <li>优化: 动态表单显示样式</li> 
 <li>fix: 修复未读消息数量显示错误</li> 
 <li>fix: 分配菜单权限校验报错</li> 
</ul> 
<h2>🥞新功能截图</h2> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-6a021b64002a32c69c9f4c12b1c047f6b5c.png" width="3840" referrerpolicy="no-referrer"></p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-6cb629dd5e0c67fb62ffbe437ee80f0e2e0.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>流程设计器</p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-22eec77facfd8102cfce0275321d7247d46.png" width="3840" referrerpolicy="no-referrer"></p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-ae6c739681ab28426925aa2c84194e81dad.png" width="3840" referrerpolicy="no-referrer"></p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-b138c131c78266935fb8af4f7e8549dee28.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>流程信息展示和处理</p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-7e2d267ba3d516912346aedaf0e039f3bae.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>流程节点配置</p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-0a9d97b03bc7eaa6f03ec9e9a78ef3ae842.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>节点用户配置</p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-41b6dc83cbc29cd5a02ceffa89a00fe1210.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>任务发起，关联动态表单</p>
                                        </div>
                                      
</div>
            