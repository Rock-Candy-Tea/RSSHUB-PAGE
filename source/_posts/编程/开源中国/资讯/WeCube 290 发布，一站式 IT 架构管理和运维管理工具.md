
---
title: 'WeCube 2.9.0 发布，一站式 IT 架构管理和运维管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3007'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 15:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3007'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube简介</span></span></h2> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">微众银行在分布式架构实践的过程中，发现将银行核心系统构建于分布式架构之上，会遇到一些与传统单体应用不同的痛点（例如，服务器增多，部署难度大；调用链长，全链路跟踪困难； 系统复杂，问题定位时间长等），在逐步解决这些痛点的过程中，总结了一套IT管理的方法论和最佳实践，并研发了与之配套的IT管理工具体系。</span></span></p> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube就是将该套方法论和最佳实践，从微众内部众多IT管理工具体系中提炼出来，整合成一套开箱即用的、开源的、一站式IT架构管理和运维管理工具，主要用于简化分布式架构IT管理，并可以通过插件进行功能扩展。</span></span></p> 
<p style="text-align:start">此次版本更新主要功能和优化点如下。</p> 
<p style="text-align:start"><strong>Features:</strong><br> WeCube Platform - 数据查询效率大优化;<br> WeCube Platform - 编排节点数据动态绑定;<br> WeCube Platform - 编排执行数据冲突检测支持;<br> WeCube Platform - 编排执行支持高危命令检测;<br> WeCube Platform - 优化系统间认证机制;<br> Terminal Plugin – 新插件发布：支持ssh console/录屏回放/文件管理/高危命令识别等;</p> 
<p style="text-align:start"><strong>Enhancements:</strong><br> WeCube Platform - 任务编排页面中节点参数必选性校验;<br> WeCube Platform - 优化系统间认证机制;<br> WeCube Platform - 编排节点数据反选支持;<br> CMDB Plugin - 优化枚举数据接口权限控制;<br> CMDB Plugin - 优化页面换行样式;<br> Monitor Plugin - 优化归档程序并发控制;<br> Monitor Plugin - 修复外联监控告警逻辑;<br> Monitor Plugin - 告警发送增加延迟支持;<br> SaltStack Plugin - 增加主机DNS映射;<br> Artifact Plugin – 修复基线物料包选择项限制问题;<br> Artifact Plugin – 优化文件选择框排序;<br> Itsdangerous Plugin - 优化类似sudo/nohup转发命令检测;<br> Itsdangerous Plugin - 增加指定试盒范围的脚本检测接口。</p> 
<p style="text-align:start">此外，各插件还进行了以下优化：</p> 
<ol> 
 <li>增加操作记录日志;</li> 
 <li>数据接口及插件接口权限校验;</li> 
 <li>优化时区处理，统一平台时间。</li> 
</ol> 
<p style="text-align:start"><strong>WeCube镜像和插件包列表</strong></p> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>Component</th> 
   <th>Version</th> 
   <th>Download Link</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>wecube image</td> 
   <td>v2.9.0</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-wecmdb</td> 
   <td>v1.5.8</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-wecmdb-v1.5.8.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-wecmdb-v1.5.8.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-saltstack</td> 
   <td>v1.10.6</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-saltstack-v1.10.6.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-saltstack-v1.10.6.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-monitor</td> 
   <td>v1.11.2</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-monitor-v1.11.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-monitor-v1.11.2.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-qcloud</td> 
   <td>v1.8.10</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-qcloud-v1.8.10.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-qcloud-v1.8.10.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-artifacts</td> 
   <td>v1.1.3</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-artifacts-v1.1.3.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-artifacts-v1.1.3.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-service-mgmt</td> 
   <td>v0.7.1</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-service-mgmt-v0.7.1.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-service-mgmt-v0.7.1.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-notifications</td> 
   <td>v0.1.6</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-notification-v0.1.6.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-notification-v0.1.6.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-alicloud</td> 
   <td>v1.0.2</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-alicloud-v1.0.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-alicloud-v1.0.2.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-capacity</td> 
   <td>v1.0.3</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-capacity-v1.0.3.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-capacity-v1.0.3.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-itsdangerous</td> 
   <td>v0.2.1</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-itsdangerous-v0.2.1.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-itsdangerous-v0.2.1.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-terminal</td> 
   <td>v0.2.0</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terminal-v0.2.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terminal-v0.2.0.zip</a></td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><strong>插件配置最佳实践</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.0%2Fstandard.zip" target="_blank">标准安装配置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.0%2Fbootcamp.zip" target="_blank">上手指引配置</a></li> 
</ul> 
<p style="text-align:start"><strong>编排文件</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.0%2Fworkflows.zip" target="_blank">workflows</a></p> 
<p style="text-align:start"><strong>演示系统</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.0%2Fdemo_system.zip" target="_blank">演示系统</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2F4523d14ea55a20293f6fa2e1da524618_demo-app-spring-boot_1.5.3.tar.gz" target="_blank">demo-app-spring-boot</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd502c4127f7c3cc6fb7a060eab1e31bb_demo-app-spring-boot-db_1.0.1.tar.gz" target="_blank">demo-app-spring-boot-db</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd87dd39bfb554f6b40286c5965925179_demo-app-nginx_0.1.1.tar.gz" target="_blank">demo-app-nginx</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fac97667fe83d5ae961206324aeb48e63_bootcamp-app-java-spring-boot_1.0.0.tar.gz" target="_blank">bootcamp-app-spring-boot</a></li> 
</ul> 
<p style="text-align:start"><strong>演示说明</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.0%2FWeCube%25E5%2585%25A8%25E9%2587%258F%25E4%25BD%2593%25E9%25AA%258C%25E8%25BF%2587%25E7%25A8%258B%25E8%25AF%25B4%25E6%2598%258E.pdf" target="_blank">演示说明</a></p>
                                        </div>
                                      
</div>
            