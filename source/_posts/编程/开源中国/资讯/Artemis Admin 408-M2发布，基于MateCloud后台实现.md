
---
title: 'Artemis Admin 4.0.8-M2发布，基于MateCloud后台实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png'
author: 开源中国
comments: false
date: Sun, 29 Aug 2021 12:30:00 GMT
thumbnail: 'https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png'
---

<div>   
<div class="content">
                                                                                            <h2>一、发布说明</h2> 
<p style="text-align:start">Artemis Admin 4.0.8-M2在M1基础上解决了基础功能的一些bug和升级了vue的一些依赖，具体如下：</p> 
<h2 style="text-align:start">1.1 功能升级</h2> 
<ul> 
 <li>修改生产环境的配置文件</li> 
 <li>完善搜索功能</li> 
 <li>修复用户分页增加部门ID查询</li> 
 <li>菜单删除前先检查是否包含子菜单</li> 
 <li>修改用户编辑性别类型不一致导致的不选择的问题</li> 
 <li>解决状态不会自动选择默认的bug</li> 
 <li>新增角色列表查询接口</li> 
 <li>用户管理增加修改密码功能</li> 
 <li>修复表格背景颜色再深色模式下会被穿透问题</li> 
 <li>字典管理多组件调用的问题修复</li> 
 <li>字典管理功能优化，支持字典项的列表和管理</li> 
</ul> 
<h2 style="text-align:start">1.2 依赖升级</h2> 
<ul> 
 <li>升级至Vue 3.2.4</li> 
 <li>升级至Vite 2.5.1</li> 
 <li>其他请自行查看package.json</li> 
</ul> 
<h2 style="text-align:left">二、系统演示</h2> 
<h3 style="text-align:left">2.1 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcloud.mate.vip" target="_blank">http://cloud.mate.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">admin</td> 
   <td style="border-color:#dddddd">matecloud</td> 
   <td style="border-color:#dddddd">mate-system模块不能执行增删改请求</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left">如果需要验证手机号码登录，手机号码采用页面默认号码，点击获取验证码，输入1188，即可登录。</p> 
<h3 style="text-align:left">2.2  企业版：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fplus.mate.vip" target="_blank">http://plus.mate.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">admin</td> 
   <td style="border-color:#dddddd">matecloud123</td> 
   <td style="border-color:#dddddd">不能执行增删改请求，如需全部权限加微信 matecloud 联系</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">三、部分截图</h2> 
<table cellspacing="0" style="width:634px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page2.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page3.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page4.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/7.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/9.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h2>四、后台版本</h2> 
<p>Artemis Admin 4.0.8-M2对应后台版本号为4.0.9</p> 
<p>后台地址：<a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></p> 
<p><span style="background-color:#ffffff; color:#40485b">MateCloud是一款基于Spring Cloud Alibaba的微服务架构。目前已经整合Spring Cloud Gateway、Spring Security Oauth2、Feign、Dubbo、JetCache、RocketMQ等服务套件，为您的开发保驾护航！</span></p>
                                        </div>
                                      
</div>
            