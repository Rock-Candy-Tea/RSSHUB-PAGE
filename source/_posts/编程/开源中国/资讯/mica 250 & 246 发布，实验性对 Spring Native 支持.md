
---
title: 'mica 2.5.0 & 2.4.6 发布，实验性对 Spring Native 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
author: 开源中国
comments: false
date: Mon, 24 May 2021 10:32:00 GMT
thumbnail: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、mica（云母）</h2> 
<p><code>mica</code>是一个微服务组件集，但不仅仅是组件，我们关注的是微服务生态并持续演进，尽量做到开箱即用，简化使用和排坑。总共已有 40+ 组件，并且很多组件已经打通。</p> 
<p><img alt="mica 2.x 模块图" src="https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg" referrerpolicy="no-referrer"></p> 
<h2>二、版本说明</h2> 
<div> 
 <table border="1" cellspacing="0" style="width:748px"> 
  <tbody> 
   <tr> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>最新版本</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>mica 版本</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>spring boot 版本</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>spring cloud 版本</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.5.0</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>mica 2.5.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.5.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2020</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.4.6</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>mica 2.4.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.4.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2020</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.1.1-GA</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>mica 2.0.x~2.1.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>2.2.x ~ 2.3.x</p> </td> 
    <td style="border-color:#d9d9d9; white-space:normal"> <p>Hoxton</p> </td> 
   </tr> 
  </tbody> 
 </table> 
</div> 
<h2>三、更新记录</h2> 
<h3>v2.5.0 - 2021-05-23</h3> 
<ul> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-redis 微调，支持 Spring boot 到 2.5.0。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2b06.svg" width="18" referrerpolicy="no-referrer"> 升级 Spring boot 到 2.5.0。</li> 
</ul> 
<h3>v2.4.6 - 2021-05-23</h3> 
<ul> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-logging 完成 loki 支持 #36 #I3PX2F。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-ip2region、mica-captcha 添加对 spring-native 的支持 #38 #I3PX2N。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-jetcache 添加 metrics 支持 #37 #I3PX2K。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-caffeine 添加不支持自定义 Caffeine bean 提示。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-core R 添加 throwOn 系列方法。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> mica-redis 优化 ICacheKey 和 scan。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2728.svg" width="18" referrerpolicy="no-referrer"> 代码统一优化，减少部分阿里巴巴规约提示。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/1f41b.svg" width="18" referrerpolicy="no-referrer"> mica-logging 修复 LoggingInitializer Spring boot 2.4.x 失效的问题。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2b06.svg" width="18" referrerpolicy="no-referrer"> 升级 druid 到 1.2.6。</li> 
 <li><img alt="image" src="https://gw.alipayobjects.com/os/lib/twemoji/11.2.0/2/svg/2b06.svg" width="18" referrerpolicy="no-referrer"> 升级 Spring boot 到 2.4.6。</li> 
</ul> 
<h2>四、重点说明</h2> 
<h3>4.1 mica-logging 完成 loki 支持</h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0d09a800a23ff8be390f2726eb2bb5cad70.gif" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">更多使用请查看 </span><a href="https://gitee.com/596392912/mica/tree/master/mica-logging#loki-%E6%97%A5%E5%BF%97%E6%94%B6%E9%9B%86"><span style="color:#3498db"><strong>mica 文档</strong></span></a><span style="background-color:#ffffff; color:#000000">。</span></p> 
<h3>4.2 mica-jetcache 添加 metrics 支持</h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4f5659d26176ccbdc629c96bda39a22154a.gif" referrerpolicy="no-referrer"></p> 
<h3>4.3 实验性对 Spring native 支持</h3> 
<p>mica-ip2region、mica-captcha 添加对 spring-native 的支持，另外我们也在持续关注 GraalVM 和 spring-native 的相关 issues，持续推进 mica native 进程。</p> 
<h2>五、mica生态</h2> 
<ul> 
 <li>mica-auto (Spring boot starter 利器):<a href="https://gitee.com/596392912/mica-auto?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-auto</a></li> 
 <li>mica-weixin（jfinal weixin 的 spring boot starter）：<a href="https://gitee.com/596392912/mica-weixin?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-weixin</a></li> 
 <li>mica-mqtt（基于 t-io 实现的 mqtt组件）：<a href="https://gitee.com/596392912/mica-mqtt?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-mqtt</a></li> 
 <li>Spring cloud 微服务 http2 方案（h2c）:<a href="https://gitee.com/596392912/spring-cloud-java11?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/spring-cloud-java11</a></li> 
 <li>mica-security（mica权限系统 vue 改造中）:<a href="https://gitee.com/596392912/mica-security?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-security</a></li> 
</ul> 
<h2>六、文档</h2> 
<ul> 
 <li>mica 源码 Gitee（码云）：<a href="https://gitee.com/596392912/mica?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica</a></li> 
 <li>mica 源码 Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flets-mica%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">https://github.com/lets-mica</a></li> 
 <li>文档地址（官网）：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwiki.dreamlu.net%2Fguide%2Fgetting-started.html%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">http://wiki.dreamlu.net</a></li> 
 <li>文档地址（语雀-可关注订阅）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fdreamlu%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">https://www.yuque.com/dreamlu</a></li> 
</ul>
                                        </div>
                                      
</div>
            