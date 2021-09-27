
---
title: 'mica 微服务组件集 2.5.5 发布，支持 Java 17'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 09:52:00 GMT
thumbnail: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0"><span>一、mica（云母）</span></h2> 
<p style="margin-left:0; margin-right:0"><code><span>mica</span></code><span>是一个微服务组件集，但不仅仅是组件，我们关注的是微服务生态并持续演进，尽量做到开箱即用，简化使用和排坑。总共已有 40+ 组件，并且很多组件已经打通。</span></p> 
<p style="margin-left:0; margin-right:0"><img alt="mica 2.x 模块图" src="https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg" referrerpolicy="no-referrer"></p> 
<div> 
 <h2 style="margin-left:0; margin-right:0"><span>二、版本说明</span></h2> 
 <table border="1" cellspacing="0" class="ne-table" id="DFQxR" style="border-collapse:collapse; border:1px solid #d9d9d9; table-layout:fixed; width:748px"> 
  <tbody> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>最新版本</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mica 版本</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>spring boot 版本</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>spring cloud 版本</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.5.5</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mica 2.5.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.5.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2020</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.4.11</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mica 2.4.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.4.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2020</span></p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.1.1-GA</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mica 2.0.x~2.1.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>2.2.x ~ 2.3.x</span></p> </td> 
    <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>Hoxton</span></p> </td> 
   </tr> 
  </tbody> 
 </table> 
 <p style="margin-left:0; margin-right:0"><strong><span>说明：</span></strong><span>mica 对 Spring cloud 为非强制依赖，除了 mica-jobs、mica-prometheus 其他组件</span><strong><span>普通 Spring boot 项目也可以使用</span></strong><span>。</span></p> 
 <h2 style="margin-left:0; margin-right:0"><span>三、更新记录</span></h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span style="color:#40485b">✨ mica-http 添加 HttpException 方便异常时获取相应信息。</span></li> 
  <li><span style="color:#40485b">✨ mica-http ResponseSpec 添加 isNotOk 用于重试断言。</span> </li> 
  <li><span style="color:#40485b">✨ mica-core 优化 bean copy 和 bean map 支持 java17。</span></li> 
  <li><span style="color:#40485b">✨ mica-core 优化 Mica Context 接口。</span> </li> 
  <li><span style="color:#40485b">✨ 优化 github action。</span></li> 
  <li><span style="color:#40485b">✨ 升级 gradle 版本到 7.2，支持 java17。</span> </li> 
  <li><span style="color:#40485b">🐛 mica-qrcode 修复 toImage 字符集问题。</span></li> 
  <li><span style="color:#40485b">🐛 mica-xss 目前只支持 servlet 只在 servlet 下启用。</span> </li> 
  <li><span style="color:#40485b">🐛 mica-core 修复 ObjectUtil#toBoolean 方法，感谢</span><span style="color:#40485b"> </span><span style="background-color:#f7f7f9; color:rgba(0, 0, 0, 0.8)">@caiqyxyx</span><span style="color:#40485b"> </span><span style="color:#40485b">同学反馈。</span></li> 
  <li><span style="color:#40485b">⬆️ 升级到 Spring boot 到 2.5.5。</span> </li> 
  <li><span style="color:#40485b">⬆️ 升级到 Spring cloud 2020.0.4。</span></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0"><span>四、mica生态</span></h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>mica-auto (Spring boot starter 利器):</span><a href="https://gitee.com/596392912/mica-auto?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank"><span>https://gitee.com/596392912/mica-auto</span></a></li> 
  <li><span>mica-weixin（jfinal weixin 的 spring boot starter）：</span><a href="https://gitee.com/596392912/mica-weixin?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank"><span>https://gitee.com/596392912/mica-weixin</span></a> </li> 
  <li><span>mica-mqtt（基于 t-io 实现的 mqtt组件）：</span><a href="https://gitee.com/596392912/mica-mqtt?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank"><span>https://gitee.com/596392912/mica-mqtt</span></a></li> 
  <li><span>Spring cloud 微服务 http2 方案（h2c）:</span><a href="https://gitee.com/596392912/spring-cloud-java11?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank"><span>https://gitee.com/596392912/spring-cloud-java11</span></a> </li> 
  <li><span>mica-security（mica权限系统 vue 改造中）:</span><a href="https://gitee.com/596392912/mica-security?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank"><span>https://gitee.com/596392912/mica-security</span></a></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0"><span>五、文档</span></h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>文档地址（官网）：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwiki.dreamlu.net%2Fguide%2Fgetting-started.html%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank"><span>http://wiki.dreamlu.net</span></a></li> 
  <li><span>文档地址（语雀-可关注订阅）：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fdreamlu%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank"><span>https://www.yuque.com/dreamlu</span></a></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            