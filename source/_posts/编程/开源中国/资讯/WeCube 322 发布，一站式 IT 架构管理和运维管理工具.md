
---
title: 'WeCube 3.2.2 发布，一站式 IT 架构管理和运维管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2122'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 14:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2122'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube 简介</span></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="color:#333333">微众银行在分布式架构实践的过程中，发现将银行核心系统构建于分布式架构之上，会遇到一些与传统单体应用不同的痛点（例如，服务器增多，部署难度大；调用链长，全链路跟踪困难； 系统复杂，问题定位时间长等），在逐步解决这些痛点的过程中，总结了一套IT管理的方法论和最佳实践，并研发了与之配套的IT管理工具体系。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="color:#333333">WeCube就是将该套方法论和最佳实践，从微众内部众多IT管理工具体系中提炼出来，整合成一套开箱即用的、开源的、一站式IT架构管理和运维管理工具，主要用于简化分布式架构IT管理，并可以通过插件进行功能扩展。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">此次版本更新主要功能和优化点如下。</p> 
<p style="color:#24292f; text-align:start"><strong>Features:</strong><br> Monitor Plugin – 全新业务监控管理。</p> 
<p style="color:#24292f; text-align:start"><strong>Enhancements:</strong><br> WeCube Platform - 支持插件s3文件声明；<br> WeCube Platform - 支持私钥登陆;<br> WeCube Platform - 增加数据写入任务节点;<br> WeCube Platform - 优化新插件注册事务保证;<br> WeCMDB Plugin – 数据权限配置编辑回显问题;<br> WeCMDB Plugin – 数据权限应用导致数据查询报错问题;<br> Taskman Plugin – 支持模板导入导出;<br> Taskman Plugin – 支持附件与超时通知;<br> Taskman Plugin – 支持表单中指定数据模型查询;<br> Artifacts Plugin - 部署包数据模型及包上传插件接口;<br> Artifacts Plugin - 修复数据模型查询错误问题;<br> Terminal Plugin - 修复删除提示xss问题;<br> Itsdangerous Plugin - 修复删除提示xss问题;<br> Terraform Plugin - 优化接口Token校验。</p> 
<p style="color:#24292f; text-align:start"><strong>WeCube镜像和插件包列表</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Component</th> 
   <th>Version</th> 
   <th>Download Link</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube image</td> 
   <td style="border-style:solid; border-width:1px">v3.2.2</td> 
   <td style="border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-wecmdb</td> 
   <td style="border-style:solid; border-width:1px">v2.0.6</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-wecmdb-v2.0.6.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-wecmdb-v2.0.6.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-saltstack</td> 
   <td style="border-style:solid; border-width:1px">v1.10.9</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-saltstack-v1.10.9.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-saltstack-v1.10.9.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-monitor</td> 
   <td style="border-style:solid; border-width:1px">v2.0.0</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-monitor-v2.0.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-monitor-v2.0.0.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-artifacts</td> 
   <td style="border-style:solid; border-width:1px">v1.1.7</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-artifacts-v1.1.7.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-artifacts-v1.1.7.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-taskman</td> 
   <td style="border-style:solid; border-width:1px">v0.1.1</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-taskman-v0.1.1.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-taskman-v0.1.1.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-notifications</td> 
   <td style="border-style:solid; border-width:1px">v0.2.0</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-notification-v0.2.0.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-notification-v0.2.0.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-capacity</td> 
   <td style="border-style:solid; border-width:1px">v1.0.4</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-capacity-v1.0.4.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-capacity-v1.0.4.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-itsdangerous</td> 
   <td style="border-style:solid; border-width:1px">v0.2.3</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-itsdangerous-v0.2.3.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-itsdangerous-v0.2.3.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-terminal</td> 
   <td style="border-style:solid; border-width:1px">v1.0.2</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terminal-v1.0.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terminal-v1.0.2.zip</a></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">wecube-plugins-terraform</td> 
   <td style="border-style:solid; border-width:1px">v0.5.2</td> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fplugins-v2%2Fwecube-plugins-terraform-v0.5.2.zip" target="_blank">https://wecube-1259801214.cos.ap-guangzhou.myqcloud.com/plugins-v2/wecube-plugins-terraform-v0.5.2.zip</a></td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#24292f; text-align:start"><strong>插件配置最佳实践</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.2.2%2Fstandard.zip" target="_blank">标准安装配置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.2.2%2Fbootcamp.zip" target="_blank">上手指引配置</a></li> 
</ul> 
<p style="color:#24292f; text-align:start"><strong>编排文件</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.2.2%2Fworkflows.zip" target="_blank">workflows</a></p> 
<p style="color:#24292f; text-align:start"><strong>演示系统</strong>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.2.2%2Fdemo_system.zip" target="_blank">演示系统</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2F4523d14ea55a20293f6fa2e1da524618_demo-app-spring-boot_1.5.3.tar.gz" target="_blank">demo-app-spring-boot</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd502c4127f7c3cc6fb7a060eab1e31bb_demo-app-spring-boot-db_1.0.1.tar.gz" target="_blank">demo-app-spring-boot-db</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fd87dd39bfb554f6b40286c5965925179_demo-app-nginx_0.1.1.tar.gz" target="_blank">demo-app-nginx</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fdemo_system%2Fbootcamp-app-java-spring-boot_1.0.0.tar.gz" target="_blank">bootcamp-app-spring-boot</a></li> 
</ul> 
<p style="color:#24292f; text-align:start"><strong>演示说明</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwecube-1259801214.cos.ap-guangzhou.myqcloud.com%2Fv3.2.2%2FWeCube%25E5%2585%25A8%25E9%2587%258F%25E4%25BD%2593%25E9%25AA%258C%25E8%25BF%2587%25E7%25A8%258B%25E8%25AF%25B4%25E6%2598%258E.pdf" target="_blank">演示说明</a></p>
                                        </div>
                                      
</div>
            