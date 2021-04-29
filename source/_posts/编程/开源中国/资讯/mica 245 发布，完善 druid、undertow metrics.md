
---
title: 'mica 2.4.5 发布，完善 druid、undertow metrics'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://uploader.shimo.im/f/Fz3jDb8pEI5pDgDT.jpg!thumbnail'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 09:29:00 GMT
thumbnail: 'https://uploader.shimo.im/f/Fz3jDb8pEI5pDgDT.jpg!thumbnail'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、mica（云母）</h2> 
<p><code>mica</code> 是一个微服务组件集，但不仅仅是组件，我们关注的是微服务生态并持续演进，尽量做到开箱即用，简化使用和排坑。总共已有 40+ 组件，并且很多组件已经打通。</p> 
<p><img height="auto" src="https://uploader.shimo.im/f/Fz3jDb8pEI5pDgDT.jpg!thumbnail" width="1428" referrerpolicy="no-referrer"></p> 
<h2>二、版本说明</h2> 
<p><strong>注意：</strong> 2.4.5 开始去掉了 GA 后缀，<strong>mica-v2.0</strong> 分支仅做 bug 修复，不再做功能更新。</p> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <td style="height:16px; vertical-align:top"> <p>最新版本</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>mica 版本</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>spring boot 版本</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>spring cloud 版本</p> </td> 
  </tr> 
  <tr> 
   <td style="height:16px; vertical-align:top"> <p>2.4.5</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>mica 2.4.x</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>2.4.x</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>2020</p> </td> 
  </tr> 
  <tr> 
   <td style="height:16px; vertical-align:top"> <p>2.1.1-GA</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>mica 2.0.x~2.1.x</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>2.2.x ~ 2.3.x</p> </td> 
   <td style="height:16px; vertical-align:top"> <p>Hoxton</p> </td> 
  </tr> 
 </tbody> 
</table> 
<h2>三、更新记录</h2> 
<div>
 v2.4.5 - 2021-04-28
</div> 
<ul> 
 <li>✨ 添加 mica-jetcache（二级缓存）模块，方便使用。</li> 
 <li>✨ 添加 mica-lite 模块，方便 Spring boot 项目使用。</li> 
 <li>✨ mica-metrics 重构 UndertowMetrics，暴露更加有用的指标。</li> 
 <li>✨ mica-metrics 完善 DruidMetrics，暴露更加有用的指标。</li> 
 <li>✨ mica-redis 调整 bean 名称 redisTemplate 为 micaRedisTemplate 减少冲突。</li> 
 <li>✨ mica-captcha 中的 cache 改为每次读取， caffeine 会刷新，照成引用为 null。</li> 
 <li>✨ mica-captcha 优化 bean 名称和添加 generateBase64Vo 方法。</li> 
 <li>✨ mica-logging 减少 reflections 日志，readme 添加阿里云、腾讯云日志服务接入链接。</li> 
 <li>✨ mica-qrcode 添加 base64 image 方法。</li> 
 <li>✨ mica-core 添加网关通用 code。</li> 
 <li>✨ mica-core 添加 CollectionUtil computeIfAbsent 方法 避免 jdk8 下的 bugs JDK-8161372</li> 
 <li>✨ mica-core Pkcs7Encoder 中默认的 BLOCK_SIZE 改为 16 github #35 兼容更多编程语言。</li> 
 <li>🐛 mica-caffeine 多 cache name 时报错。</li> 
 <li>⬆️ 升级 spring boot 到 2.4.5</li> 
 <li>⬆️ 升级 mica-weixin 到 2.1.0（优化对 mica-caffeine 的支持）</li> 
</ul> 
<div>
 v2.4.4-GA - 2021-03-28（之前未在 开源中国发布）
</div> 
<ul> 
 <li>✨ mica-qrcode 新增模块，友好的二维码识别和生成</li> 
 <li>✨ mica-logging 重新设计，<code>logstash-logback-encoder</code> 调整为可选，<code>logstash</code> 和 <code>json</code> 需手动添加依赖</li> 
 <li>✨ mica-core 优化完善 DesensitizationUtil</li> 
 <li>✨ mica-core 添加 ImageUtil</li> 
 <li>✨ mica-ip2region 更新 db 文件 gitee #I3AJNV</li> 
 <li>🐛 mica-redis 修复 ScanOptions count 空指针</li> 
 <li>⬆️ 升级到 mica-auto 到 2.0.4</li> 
 <li>⬆️ 升级到 mica-weixin 到 2.0.6</li> 
 <li>⬆️ 升级到 spring cloud 2020.0.2</li> 
 <li>⬆️ 升级 spring boot 到 2.4.4</li> 
</ul> 
<h2>三、mica-metrics</h2> 
<p>mica-metrics 解决了 druid、undertow 没有监控指标的问题，做到了全网首发，后面会 pr 给 Druid 和 Spring boot 官方。</p> 
<div>
 <strong>3.1 druid metrics</strong>
</div> 
<p>在 mica 2.4.5 之前对 druid 只实现了 DruidDataSourcePoolMetadata，仅仅支持 3 个 jdbc 开头的指标，如下图：</p> 
<p><img height="auto" src="https://uploader.shimo.im/f/C1iDD6Oqex4wdFyc.jpg!thumbnail" width="1580" referrerpolicy="no-referrer"></p> 
<p>mica 2.4.5 进行了调整，现在新增了 10 个 Druid 的指标，并且支持多数据源。</p> 
<p><img height="auto" src="https://uploader.shimo.im/f/H8l2Uapykph05KaF.jpg!thumbnail" width="1332" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h3>3.2 undertow metrics</h3> 
<p>undertow 指标在 mica 2.4.5 彻底进行了重构，对 xwork、session、connector 的数据统计进行了收集，现已支持 22 个指标。</p> 
<p><img height="auto" src="https://uploader.shimo.im/f/jJkZ50YXqGv3gk7f.jpg!thumbnail" width="1450" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img height="auto" src="https://uploader.shimo.im/f/McKMiMcj9ykhBqCY.png!thumbnail" width="2400" referrerpolicy="no-referrer"></p> 
<h2>五、mica生态</h2> 
<ul> 
 <li>mica-auto (Spring boot starter 利器): <a href="https://gitee.com/596392912/mica-auto" target="_blank">https://gitee.com/596392912/mica-auto</a></li> 
 <li>mica-weixin（jfinal weixin 的 spring boot starter）：<a href="https://gitee.com/596392912/mica-weixin" target="_blank">https://gitee.com/596392912/mica-weixin</a></li> 
 <li>mica-mqtt（基于 t-io 实现的 mqtt组件）：<a href="https://gitee.com/596392912/mica-mqtt" target="_blank">https://gitee.com/596392912/mica-mqtt</a></li> 
 <li>Spring cloud 微服务 http2 方案（h2c）: <a href="https://gitee.com/596392912/spring-cloud-java11" target="_blank">https://gitee.com/596392912/spring-cloud-java11</a></li> 
 <li>mica-security（mica权限系统 vue 改造中）: <a href="https://gitee.com/596392912/mica-security" target="_blank">https://gitee.com/596392912/mica-security</a></li> 
</ul> 
<h2>六、文档</h2> 
<ul> 
 <li>mica 源码 Gitee（码云）：<a href="https://gitee.com/596392912/mica" target="_blank">https://gitee.com/596392912/mica</a></li> 
 <li>mica 源码 Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flets-mica" target="_blank">https://github.com/lets-mica</a></li> 
 <li>文档地址（官网）：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwiki.dreamlu.net%2Fguide%2Fgetting-started.html" target="_blank">http://wiki.dreamlu.net</a></li> 
 <li>文档地址（语雀-可关注订阅）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fdreamlu" target="_blank">https://www.yuque.com/dreamlu</a></li> 
</ul>
                                        </div>
                                      
</div>
            