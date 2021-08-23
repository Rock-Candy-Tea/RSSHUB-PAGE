
---
title: 'mica 2.5.4 发布，新增 mica-prometheus 模块支持 http sd'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
author: 开源中国
comments: false
date: Mon, 23 Aug 2021 10:09:00 GMT
thumbnail: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <h2>一、mica（云母）</h2> 
 <p><code>mica</code>是一个微服务组件集，但不仅仅是组件，我们关注的是微服务生态并持续演进，尽量做到开箱即用，简化使用和排坑。总共已有 40+ 组件，并且很多组件已经打通。</p> 
 <p><img alt="mica 2.x 模块图" src="https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg" referrerpolicy="no-referrer"></p> 
 <h2>二、版本说明</h2> 
 <table border="1" cellspacing="0" style="width:748px"> 
  <tbody> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px"> <p>最新版本</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>mica 版本</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>spring boot 版本</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>spring cloud 版本</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.5.4</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>mica 2.5.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.5.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2020</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.4.10</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>mica 2.4.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.4.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2020</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.1.1-GA</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>mica 2.0.x~2.1.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>2.2.x ~ 2.3.x</p> </td> 
    <td style="border-color:#d9d9d9; height:33px"> <p>Hoxton</p> </td> 
   </tr> 
  </tbody> 
 </table> 
 <p><strong>说明：</strong>mica 对 Spring cloud 为非强制依赖，除了 mica-jobs、mica-prometheus 其他组件<strong>普通 Spring boot 项目也可以使用</strong>。</p> 
 <h2>三、更新记录</h2> 
 <ul> 
  <li><span style="color:#24292e">✨</span><span style="color:#24292e"> </span><span style="color:#24292e">新增 mica-prometheus 模块支持 http sd 和 alert webhook。</span></li> 
  <li><span style="color:#24292e">✨</span><span style="color:#24292e"> </span><span style="color:#24292e">mica-swagger 支持 v3 注解</span><span style="color:#24292e"> </span><span style="color:#24292e">@Tag</span><span style="color:#24292e">，</span><span style="color:#24292e">R</span><span style="color:#24292e"> </span><span style="color:#24292e">添加 v3 注解。</span> </li> 
  <li><span style="color:#24292e">✨</span><span style="color:#24292e"> </span><span style="color:#24292e">mica-logging 代码优化。</span></li> 
  <li><span style="color:#24292e">✨</span><span style="color:#24292e"> </span><span style="color:#24292e">github actions 添加缓存。</span> </li> 
  <li><span style="color:#24292e">📝</span><span style="color:#24292e"> </span><span style="color:#24292e">更新模块图。</span></li> 
  <li><span style="color:#24292e">📝</span><span style="color:#24292e"> </span><span style="color:#24292e">[Summer 2021] 添加英文 readme。</span> </li> 
  <li><span style="color:#24292e">⬆️</span><span style="color:#24292e"> </span><span style="color:#24292e">升级 Spring Native 到 0.10.2。</span></li> 
  <li><span style="color:#24292e">⬆️</span><span style="color:#24292e"> </span><span style="color:#24292e">升级到 Spring boot 到 2.5.4</span> </li> 
  <li><span style="color:#24292e">⬆️</span><span style="color:#24292e"> </span><span style="color:#24292e">升级 mica-auto 到 2.1.3 修复多模块增量编译问题。</span></li> 
  <li><span style="color:#24292e">⬆️</span><span style="color:#24292e"> </span><span style="color:#24292e">升级 jsoup 到 1.14.2，不再支持低版本 jsoup。</span> </li> 
  <li><span style="color:#24292e">⬆️</span><span style="color:#24292e"> </span><span style="color:#24292e">升级 knife4j 到 3.0.3</span></li> 
  <li><span style="color:#24292e">⬆️ 升级到 jfinal 到 4.9.16</span></li> 
 </ul> 
 <h2>四、重点说明</h2> 
 <ul> 
  <li>mica-prometheus 组件是为了方便 <code>Spring cloud</code> 服务对接 Prometheus <code>http_sd</code> 和 alert webhook，支持 <code>servlet</code> 和 <code>webflux</code>，建议集成到 Spring boot admin 这类非业务服务中。</li> 
 </ul> 
 <h3>maven</h3> 
 <pre><dependency>
  <groupId>net.dreamlu</groupId>
  <artifactId>mica-prometheus</artifactId>
  <version>$&#123;version&#125;</version>
</dependency>
</pre> 
 <h3>gradle</h3> 
 <pre>compile("net.dreamlu:mica-prometheus:$&#123;version&#125;")
</pre> 
 <h2>http-sd 使用</h2> 
 <pre>- job_name: micax-cloud
  honor_timestamps: true
  scrape_interval: 15s
  scrape_timeout: 10s
  metrics_path: /actuator/prometheus
  scheme: http
  http_sd_configs:
  - url: 'http://&#123;ip&#125;:&#123;port&#125;/actuator/prometheus/sd'
</pre> 
 <h3>效果图</h3> 
 <p><img alt="mica-prometheus 效果图" src="https://gitee.com/596392912/mica/raw/master/docs/images/mica-prometheus-show.png" referrerpolicy="no-referrer"></p> 
 <h2>alert webhook</h2> 
 <pre>receivers:
- name: "alerts"
  webhook_configs:
  - url: 'http://&#123;ip&#125;:&#123;port&#125;/actuator/prometheus/alerts'
    send_resolved: true
</pre> 
 <h3>自定义监听事件并处理</h3> 
 <pre>@Async
@EventListener
public void onAlertEvent(AlertMessage message) &#123;
// 处理 alert webhook message
&#125;
</pre> 
 <h2>五、mica生态</h2> 
 <ul> 
  <li>mica-auto (Spring boot starter 利器):<a href="https://gitee.com/596392912/mica-auto?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-auto</a></li> 
  <li>mica-weixin（jfinal weixin 的 spring boot starter）：<a href="https://gitee.com/596392912/mica-weixin?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-weixin</a> </li> 
  <li>mica-mqtt（基于 t-io 实现的 mqtt组件）：<a href="https://gitee.com/596392912/mica-mqtt?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-mqtt</a></li> 
  <li>Spring cloud 微服务 http2 方案（h2c）:<a href="https://gitee.com/596392912/spring-cloud-java11?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/spring-cloud-java11</a></li> 
  <li>mica-security（mica权限系统 vue 改造中）:<a href="https://gitee.com/596392912/mica-security?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica-security</a></li> 
 </ul> 
 <h2>六、文档</h2> 
 <ul> 
  <li>mica 源码 Gitee（码云）：<a href="https://gitee.com/596392912/mica?fileGuid=m5kv9JK8Jmc1XgqX" target="_blank">https://gitee.com/596392912/mica</a></li> 
  <li>文档地址（语雀-可关注订阅）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fdreamlu%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">https://www.yuque.com/dreamlu</a> </li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            