
---
title: 'WeCube 3.1.0 发布，一站式 IT 架构管理和运维管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9781'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 14:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9781'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube简介</span></span></h2> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">微众银行在分布式架构实践的过程中，发现将银行核心系统构建于分布式架构之上，会遇到一些与传统单体应用不同的痛点（例如，服务器增多，部署难度大；调用链长，全链路跟踪困难； 系统复杂，问题定位时间长等），在逐步解决这些痛点的过程中，总结了一套IT管理的方法论和最佳实践，并研发了与之配套的IT管理工具体系。</span></span></p> 
<p style="text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube就是将该套方法论和最佳实践，从微众内部众多IT管理工具体系中提炼出来，整合成一套开箱即用的、开源的、一站式IT架构管理和运维管理工具，主要用于简化分布式架构IT管理，并可以通过插件进行功能扩展。</span></span></p> 
<p style="text-align:start">此次版本更新主要功能和优化点如下。</p> 
<p style="text-align:start"><strong>Features:</strong><br> WeCube Platform - 插件接口支持对象/字符串/数字数组传参;<br> WeCube Platform - 编排多上下文指定根计算节点支持;<br> WeCube Platform - 优化编排上下文取数计算;<br> Monitor Plugin - SNMP监控支持;<br> Monitor Plugin – 自定义视图支持层级对象;<br> Terraform Plugin - 全新优化版本，支持自定义插件接口以及参数多种类型的组合转换;<br> Terraform Plugin - 新增插件调试功能;<br> Terraform Plugin - 支持插件定义和多云配置导入导出。</p> 
<p style="text-align:start"><strong>Enhancements:</strong></p> 
<p style="text-align:start">WeCube Platform - 编排标签及过滤支持;<br> WeCMDB Plugin - 视图/表格CI数据管理支持分组控制显示;<br> WeCMDB Plugin - 报表树状结构展示;<br> WeCMDB Plugin - 修复数据管理复制新增空行问题;<br> WeCMDB Plugin - 优化视图加载;<br> WeCMDB Plugin - CI状态变更支持编排触发;<br> WeCMDB Plugin - 支持CI属性分组编辑控制;<br> Monitor Plugin – 指标及自定义视图交互优化;<br> Notification Plugin - 新增腾讯云短信通知支持。<br> Terminal Plugin – 支持WeCube表达式的动态终端授权。</p> 
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
   <td>v3.1.0</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-wecmdb</td> 
   <td>v2.0.3</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-wecmdb-v2.0.3.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-wecmdb-v2.0.3.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-saltstack</td> 
   <td>v1.10.9</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-saltstack-v1.10.9.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-saltstack-v1.10.9.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-monitor</td> 
   <td>v1.12.0</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-monitor-v1.12.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-monitor-v1.12.0.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-artifacts</td> 
   <td>v1.1.4</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-artifacts-v1.1.4.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-artifacts-v1.1.4.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-service-mgmt</td> 
   <td>v0.7.1</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-service-mgmt-v0.7.1.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-service-mgmt-v0.7.1.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-notifications</td> 
   <td>v0.2.0</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-notification-v0.2.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-notification-v0.2.0.zip</a></td> 
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
   <td>v0.2.3</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terminal-v0.2.3.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terminal-v0.2.3.zip</a></td> 
  </tr> 
  <tr> 
   <td>wecube-plugins-terraform</td> 
   <td>v0.4.0</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terraform-v0.4.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terraform-v0.4.0.zip</a></td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><strong>插件配置最佳实践</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.1.0%2Fstandard.zip" target="_blank">标准安装配置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.1.0%2Fbootcamp.zip" target="_blank">上手指引配置</a></li> 
</ul> 
<p style="text-align:start"><strong>编排文件</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.1.0%2Fworkflows.zip" target="_blank">workflows</a></p> 
<p style="text-align:start"><strong>演示系统</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.1.0%2Fdemo_system.zip" target="_blank">演示系统</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2F4523d14ea55a20293f6fa2e1da524618_demo-app-spring-boot_1.5.3.tar.gz" target="_blank">demo-app-spring-boot</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd502c4127f7c3cc6fb7a060eab1e31bb_demo-app-spring-boot-db_1.0.1.tar.gz" target="_blank">demo-app-spring-boot-db</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd87dd39bfb554f6b40286c5965925179_demo-app-nginx_0.1.1.tar.gz" target="_blank">demo-app-nginx</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fbootcamp-app-java-spring-boot_1.0.0.tar.gz" target="_blank">bootcamp-app-spring-boot</a></li> 
</ul> 
<p style="text-align:start"><strong>演示说明</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.1.0%2FWeCube%25E5%258A%259F%25E8%2583%25BD%25E4%25BD%2593%25E9%25AA%258C%28standard%29_v3.pdf" target="_blank">演示说明</a></p>
                                        </div>
                                      
</div>
            