
---
title: 'WeCube 2.9.2 发布，一站式 IT 架构管理和运维管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5867'
author: 开源中国
comments: false
date: Mon, 10 May 2021 03:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5867'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube简介</span></span></h2> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">微众银行在分布式架构实践的过程中，发现将银行核心系统构建于分布式架构之上，会遇到一些与传统单体应用不同的痛点（例如，服务器增多，部署难度大；调用链长，全链路跟踪困难； 系统复杂，问题定位时间长等），在逐步解决这些痛点的过程中，总结了一套IT管理的方法论和最佳实践，并研发了与之配套的IT管理工具体系。</span></span></p> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube就是将该套方法论和最佳实践，从微众内部众多IT管理工具体系中提炼出来，整合成一套开箱即用的、开源的、一站式IT架构管理和运维管理工具，主要用于简化分布式架构IT管理，并可以通过插件进行功能扩展。</span></span></p> 
<p style="text-align:start">此次版本更新主要功能和优化点如下。</p> 
<p style="text-align:start"><strong>Features:</strong><br> Terraform Plugin – 支持存量云平台资源发现&纳管功能;<br> WeCube Platform - 编排节点支持创建数据记录;<br> WeCube Platform - 编排节点支持上下文数据拆分;</p> 
<p style="text-align:start"><strong>Enhancements:</strong><br> WeCube Platform - 修复系统数据模型图中跨插件引用展示错误;<br> WeCube Platform - 优化编排页面数据保存;<br> WeCube Platform - 优化插件注册中系统参数显示;<br> WeCube Platform - 修复保存编排最后一个节点配置丢失问题;<br> Monitor Plugin - 支持历史告警定时清理;<br> Monitor Plugin - 调整k8s监控配置，增加namespace等信息;<br> Monitor Plugin - 业务日志监控支持正则匹配转换;<br> Monitor Plugin - 更新第三方redis-exporter版本;<br> Monitor Plugin - 增加监控对象采集间隔配置;<br> Monitor Plugin - 修复对象组阈值导入导出功能;<br> Monitor Plugin - 修复表单误操作关闭问题;<br> CMDB Plugin - 优化视图标签&选择框的展示;<br> SaltStack Plugin - 修复安装Minion时ssh端口不生效问题;<br> Terminal Plugin – 优化i18n翻译。</p> 
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
   <td>v2.9.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-wecmdb</td> 
   <td>v1.5.10</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-wecmdb-v1.5.10.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-wecmdb-v1.5.10.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-saltstack</td> 
   <td>v1.10.7</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-saltstack-v1.10.7.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-saltstack-v1.10.7.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-monitor</td> 
   <td>v1.11.4</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-monitor-v1.11.4.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-monitor-v1.11.4.zip</a></td> 
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
   <td>v1.0.4</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-capacity-v1.0.4.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-capacity-v1.0.4.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-itsdangerous</td> 
   <td>v0.2.2</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-itsdangerous-v0.2.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-itsdangerous-v0.2.2.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-terminal</td> 
   <td>v0.2.2</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terminal-v0.2.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terminal-v0.2.2.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-terraform</td> 
   <td>v0.2.0</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terraform-v0.2.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terraform-v0.2.0.zip</a></td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><strong>插件配置最佳实践</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.2%2Fstandard.zip" target="_blank">标准安装配置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.2%2Fbootcamp.zip" target="_blank">上手指引配置</a></li> 
</ul> 
<p style="text-align:start"><strong>编排文件</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.2%2Fworkflows.zip" target="_blank">workflows</a></p> 
<p style="text-align:start"><strong>演示系统</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.2%2Fdemo_system.zip" target="_blank">演示系统</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2F4523d14ea55a20293f6fa2e1da524618_demo-app-spring-boot_1.5.3.tar.gz" target="_blank">demo-app-spring-boot</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd502c4127f7c3cc6fb7a060eab1e31bb_demo-app-spring-boot-db_1.0.1.tar.gz" target="_blank">demo-app-spring-boot-db</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd87dd39bfb554f6b40286c5965925179_demo-app-nginx_0.1.1.tar.gz" target="_blank">demo-app-nginx</a></li> 
</ul> 
<p style="text-align:start"><strong>演示说明</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv2.9.2%2FWeCube%25E5%2585%25A8%25E9%2587%258F%25E4%25BD%2593%25E9%25AA%258C%25E8%25BF%2587%25E7%25A8%258B%25E8%25AF%25B4%25E6%2598%258E.pdf" target="_blank">演示说明</a></p>
                                        </div>
                                      
</div>
            