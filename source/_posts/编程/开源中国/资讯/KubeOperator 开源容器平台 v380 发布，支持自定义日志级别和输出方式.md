
---
title: 'KubeOperator 开源容器平台 v3.8.0 发布，支持自定义日志级别和输出方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-acaa80872fa6e966a9e3537045762f52_1440w.png'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 14:19:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-acaa80872fa6e966a9e3537045762f52_1440w.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <div>
  6月15日，开源容器平台KubeOperator正式发布v3.8.0版本。在这一版本中，KubeOperator支持Kubernetes的最新版本，即v1.20.6版本，同时支持自定义日志级别和输出方式。另外，该版本还提供了对GPU Operator的支持，并完成若干功能优化和Bug修复。
 </div> 
</div> 
<h2 style="text-align:left">新增功能</h2> 
<div style="text-align:left"> 
 <div>
  <strong>1. 集群部署支持Kubernetes v1.20.6版本</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  KubeOperator v3.8.0支持Kubernetes最新的v1.20.6版本。注意：KubeOperator不支持跨大版本升级，即不支持将v1.18.x的Kubernetes集群升级至v1.20.x。KubeOperator v3.8.0离线包所携带的Kubernetes版本为 v1.20.6版本和v1.18.18版本。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic4.zhimg.com/80/v2-acaa80872fa6e966a9e3537045762f52_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图1 KubeOperator的版本管理</p> 
<div style="text-align:left"> 
 <div>
  <strong>2. Server容器日志支持输出到控制台，并存储到文件</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  KubeOperator v3.8.0版本支持将KubeOperator Server核心组件的日志输出到控制台并存储到文件，同时支持自定义日志级别。
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  以默认的/opt/kubeoperator为例，配置文件为app.yaml，其中可以设定的参数如下：
 </div> 
</div> 
<div style="text-align:left">
 <em>level: debug # 日志级别，支持info、debug</em>
</div> 
<div style="text-align:left">
 <em>out_put: fileAndStd # 输出位置（file直接打印、std输出到文件、fileAndStd直接打印并且输出到文件）</em>
</div> 
<div style="text-align:left">
 <em>max_age: 2592000 # 日志保留的最大时间，单位为秒，默认为10天</em>
</div> 
<div style="text-align:left">
 <em>rotation: 86400 # 日志保留的间隔时间，单位为秒，默认为1天</em>
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic4.zhimg.com/80/v2-a574240e1d6b6c2887545bf5b80313fe_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图2 Server日志信息设置和查看</p> 
<div style="text-align:left"> 
 <div>
  <strong>3. 持久卷支持添加NFS</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  支持在集群存储页面中，通过页面表单的方式在Kubernetes集群上创建NFS类型的PV（即PersistentVolume，持久化存储卷）。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic2.zhimg.com/80/v2-11bc9449bb81ca5b0491b8f3f0eaab39_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图3 在存储页面添加NFS类型的持久化存储卷</p> 
<div style="text-align:left"> 
 <div>
  <strong>4. 支持GPU Operator</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  KubeOperator v3.8.0版本支持GPU Operator。GPU Operator可以直接管理Kubernetes集群中的NVIDIA GPU资源，并自动执行与引导GPU节点相关的任务。由于GPU是集群中的特殊资源，因此需要先安装一些组件，然后才能将应用程序、工作负载部署到GPU上。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  这些组件包括NVIDIA驱动程序（用于启用CUDA）、Kubernetes设备插件、容器运行时，以及其他诸如自动节点标记、监控等组件，通过GPU Operator可以自动帮助我们完成这些组件、驱动程序的安装操作。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  GPU Operator适用于Kubernetes集群需要快速扩展的场景，例如在云或本地配置额外的GPU节点，以及管理底层软件组件的生命周期。由于GPU Operator将所有的内容作为容器运行，包括NVIDIA驱动程序，因此管理员可以轻松地交换各种组件，只需启动或停止容器即可。（原文可参见： 
  <strong>https://github.com/NVIDIA/gpu-operator</strong> ）
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic1.zhimg.com/80/v2-1a75074e601b8e732c1659f088e4758e_1440w.jpg" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图4 GPU Operator的架构实现</p> 
<div style="text-align:left"> 
 <div>
  <strong>5. 集群扩容操作支持添加GPU主机</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  这一功能的使用场景为：在使用KubeOperator部署Kubernetes集群时未开启安装GPU套件，集群中也没有包含GPU的工作节点。若在扩容过程中，扩容的节点需要支持NVIDIA GPU，则可以通过开启“安装GPU套件”选项实现对NVIDIA GPU的支持。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic2.zhimg.com/80/v2-940a06c92eeb8c873f3129782622602d_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图5 Kubernetes集群扩容时开启NVIDIA GPU支持</p> 
<div style="text-align:left"> 
 <div>
  <strong>6. 集群健康检查增加节点数量同步功能</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  KubeOperator v3.8.0在集群健康检查时支持同步节点数量，若用户手动在Kubernetes集群上删除节点后，可通过节点信息同步来确保KubeOperator和管理的Kubernetes集群节点信息保持一致。
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic4.zhimg.com/80/v2-65c9c3767a159d75555f9fc504193ca7_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图6 KubeOperator集群健康检查</p> 
<div style="text-align:left"> 
 <div>
  <strong>7. 启用docker-registry增加登录认证</strong>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  在KubeOperator集群工具中启用docker-registry仓库，增加了Docker Login认证，从而有效提高仓库安全性。仓库登录的默认用户名和密码为：admin/kubeoperator。使用docker-registry前需要在系统当中配置Docker私有仓库信任，具体配置如下:
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic1.zhimg.com/80/v2-201742cb9411f1e43dd73f57b7e770f5_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">图7 修改Docker私有仓库信任</p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
    <img src="https://pic1.zhimg.com/80/v2-218aad86128d01b7ac2ae4abbef303b3_1440w.png" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left">​图8 使用Docker登录docker-registry</p> 
<h2 style="text-align:left">优化改进</h2> 
<div style="text-align:left"> 
 <div>
  ■ 支持通过仓库设置页面直接跳转到Nexus仓库的操作；
 </div> 
 <div>
   
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
  ■ 补全了绑定、解绑集群资源等操作日志；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 删去正常主机状态同步任务的日志打印；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 优化持久卷表单国际化显示；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 优化删除持久卷时的提示信息；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 集群监控支持自定义时间搜索；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 根据集群版本动态匹配Dashboard和CoreDNS版本；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 点击”集群详情“创建部署计划时，增加了是否存在仓库的判断。
 </div> 
</div> 
<h2 style="text-align:left">BUG修复</h2> 
<div style="text-align:left"> 
 <div>
  ■ 解决了用户添加存储类时，可以选择失败状态的存储提供商的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了添加Local Volume持久卷失败的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了监控界面数据被覆盖的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了项目管理员添加集群时默认项目显示错误的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了集群升级任务中断后，重启服务集群状态仍然处于升级中的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了创建集群时，容器网络设置不能恢复默认值的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了DNS缓存与Traefik同时启用导致集群创建失败的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了修改凭据明文显示的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了仓库高级搜索页地址选项显示错误的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了添加集群时，概览页面缺少部分信息的问题；
 </div> 
</div> 
<div style="text-align:left"> 
 <div>
   
 </div> 
 <div>
  ■ 解决了项目管理员高级搜索结果匹配错误的问题。
 </div> 
</div> 
<div style="text-align:left">
  
</div>
                                        </div>
                                      
</div>
            