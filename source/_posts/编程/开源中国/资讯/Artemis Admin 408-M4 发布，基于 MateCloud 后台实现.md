
---
title: 'Artemis Admin 4.0.8-M4 发布，基于 MateCloud 后台实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 09:20:00 GMT
thumbnail: 'https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">一、发布说明</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#40485b">Artemis Admin 4.0.8-M4在M3基础上修复bug、完善了文件管理功能和升级了vue的一些依赖，具体如下</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.1 功能升级</h2> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>修复报错页面不展示的bug</li> 
  <li>去掉用户详情功能</li> 
  <li>返回401的时候，直接退出登录</li> 
  <li>修复对话框 hook 不设置 loaded问题</li> 
  <li>修复可编辑单元格某些情况下无法提交的问题</li> 
  <li>修复可编辑单元格某些情况下无法提交的问题</li> 
  <li>修复<code>clickToRowSelect</code>会无视行选择框disabled状态的问题</li> 
  <li>修复tableAction中的divider未按预期工作</li> 
  <li>表格列设置ifshow为false，表格的列设置里依然会渲染该列的checkBox，实际应该不渲染。</li> 
  <li>统一状态字段：0：启用 1：禁用</li> 
  <li>文件管理功能的开发</li> 
  <li>增加图片缩略图和展示存储文件名</li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.2 依赖升级</h2> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc; margin-left:0px; margin-right:0px"> 
  <li>升级至Vue 3.2.12</li> 
  <li>升级至Vite 2.5.8</li> 
  <li>升级至ant-design-vue 2.2.8</li> 
  <li>升级至xlsx 0.17.2</li> 
  <li>其他请自行查看package.json</li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、系统演示</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcloud.mate.vip" target="_blank">http://cloud.mate.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">matecloud</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">mate-system模块不能执行增删改请求</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果需要验证手机号码登录，手机号码采用页面默认号码，点击获取验证码，输入1188，即可登录。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.2  企业版：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fplus.mate.vip" target="_blank">http://plus.mate.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">matecloud123</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">不能执行增删改请求，如需全部权限加微信 matecloud 联系</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">三、部分截图</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page2.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page3.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page4.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/7.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/9.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">四、后台版本</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Artemis Admin 4.0.8-M2对应后台版本号为4.0.10</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">后台地址：<a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MateCloud是一款基于Spring Cloud Alibaba的微服务架构。目前已经整合Spring Cloud Gateway、Spring Security Oauth2、Feign、Dubbo、JetCache、RocketMQ等服务套件，为您的开发保驾护航！</span></p>
                                        </div>
                                      
</div>
            