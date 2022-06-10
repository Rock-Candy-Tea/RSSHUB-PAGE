
---
title: 'bootx-platform v1.1.0-beta-2：一大波新功能来袭'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-198d0b0c09c2087e7d22506e58ae75cc536.png'
author: 开源中国
comments: false
date: Fri, 10 Jun 2022 15:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-198d0b0c09c2087e7d22506e58ae75cc536.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0em; margin-right:0em; text-align:start">项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a></p> 
<p>基于Spring Boot框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。</p> 
<div> 
 <h2 style="margin-left:0; margin-right:0"><span>特色功能</span></h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>针对敏感信息，可以通过注解配置实现返回时自动脱敏</span></li> 
  <li><span>针对重要信息，可以通过添加注解，实现在数据库中保密存储，配合数据脱敏使用可以更好的保护系统数据的安全</span></li> 
  <li><span>支持多种范围的数据权限控制，如只能查看自己、只能查询指定部门、用户、可以查询全部的数据等等</span></li> 
  <li><span>支持嵌套查询的超级查询构造器，自动生成对应条件SQL语句</span></li> 
  <li><span>异常时返回链路追踪id，方便错误日志追踪</span></li> 
  <li><span>提供项目对应的代码生成器，方便开发</span></li> 
  <li><span>定制Mybatis Plus组件，更方便开发</span></li> 
  <li><span>支持多种消息中间件</span></li> 
  <li><span>支持全局级Websocket集成，通过事件机制可以分发到指定页面</span></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0"><span>项目选用组件说明</span></h2> 
 <table border="1" cellspacing="0" class="ne-table" id="j7PYB" style="border-collapse:collapse; border:1px solid #d9d9d9; table-layout:fixed; width:1000px"> 
  <tbody> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>组件</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>默认启用</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是否必须</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>备注</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>MySQL</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否，理论上可以替换为其他关系型数据库</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>默认使用的数据库，部分SQL语句使用了MySQL专属语法</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>Redis</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>session存储，缓存等等都用到了Redis</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>RabbitMQ</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>不使用时需要删除对应的代码即可</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>MongoDB</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>日志存储默认使用的Mongo，去掉mongo时需要切换存储类型；</span></p> <p style="margin-left:0; margin-right:0"><span>文件管理默认使用的是Mongo，去掉Mongo时，需要切换文件类型</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>MQTT</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>不使用时需要删除对应的代码即可</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>Quartz </span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>定时任务默认使用的是</span></p> <p style="margin-left:0; margin-right:0"><span>Quartz ，可以切换为XXL-JOB</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>XXL-JOB</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>可以用来替代Quartz </span></p> </td> 
   </tr> 
  </tbody> 
 </table> 
</div> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">本次功能更新</h2> 
<ul> 
 <li>增加用户全局消息Websocket推送，通过前端消息总线可以方便把消息推送到各个页面</li> 
 <li>增加flyway来对数据库进行管理</li> 
 <li>增加plumelog(lite)方式收集日志，方便对日志进行简单的管理</li> 
 <li>增加ELK相关配置，优化日志输出格式</li> 
 <li>增加不同的终端可以有不同的菜单权限列表</li> 
 <li>增加RabbitMQ消息队列模块</li> 
 <li>增加Redis简单消息队列方式,实现简单消息队列功能</li> 
 <li>增加Redis过期事件封装，实现定时消息通知功能</li> 
 <li>增加Redis简单消息队列和过期事件封装演示</li> 
 <li>增加Websocket模块及演示DEMO</li> 
 <li>增加分布式锁组件</li> 
 <li>增加分布式锁演示模块</li> 
 <li>网上商城配套开发 
  <ul> 
   <li>类目管理及相关规格、品牌、参数管理</li> 
  </ul> </li> 
 <li>升级Spring Boot为2.7.x版本</li> 
 <li>优化Redis支持集群配置</li> 
 <li>优化logback相关xml，拆分更细粒度</li> 
 <li>优化定时任务增加状态同步按钮，处理定时任务job运行状态不一致情况</li> 
 <li>优化数据权限异常类型</li> 
 <li>优化一些抛出异常的处理</li> 
 <li>优化项目pom结构</li> 
 <li>优化前端路由跳过登录鉴权配置</li> 
 <li>优化请求权限校验流程</li> 
 <li>优化MQTT .lock文件夹问题</li> 
 <li>优化前端支持内部打开外部页面</li> 
 <li>fix: 权限不拦截问题</li> 
 <li>fix: 开启验证码后, 在登录页面提示请求报错</li> 
 <li>fix: 在MacOS环境下运行日志存储报错问题</li> 
 <li>fix: mqtt ClientId配置问题导致启动时连接失败的问题</li> 
 <li>fix: RestExceptionHandler处理Throwable异常</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情查看：</span><a href="https://gitee.com/bootx/bootx-platform/releases/v1.1.0-bate-2">https://gitee.com/bootx/bootx-platform/releases/v1.1.0-bate-2</a></p> 
<h2>新功能截图</h2> 
<p><img height="1946" src="https://oscimg.oschina.net/oscnet/up-198d0b0c09c2087e7d22506e58ae75cc536.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>PlumeLog 日志管理</p> 
<p><img height="1946" src="https://oscimg.oschina.net/oscnet/up-31d6dbbccdaf8dcfc1cad8e24c7b7f80602.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>ELK日志管理</p> 
<p><img height="1072" src="https://oscimg.oschina.net/oscnet/up-42056038fc01b125a474a73f460f28eac6a.png" width="1423" referrerpolicy="no-referrer"></p> 
<p>Websocket模块</p> 
<p><img height="1129" src="https://oscimg.oschina.net/oscnet/up-4441cdcf10e1ef9727395514013ffda8f65.png" width="1540" referrerpolicy="no-referrer"></p> 
<p>接入多种消息中间件</p> 
<p><img height="1946" src="https://oscimg.oschina.net/oscnet/up-88adc89218e0ca1fbca9145e522a1552745.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>不同的终端可以有不同的菜单权限列表</p>
                                        </div>
                                      
</div>
            