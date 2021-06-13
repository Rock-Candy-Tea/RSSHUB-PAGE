
---
title: 'Apache Dubbo 3.0.0 正式版即将发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2281931ac68a65cecb77495e99f84c95a1a.png'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 09:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2281931ac68a65cecb77495e99f84c95a1a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">在今年3月份<strong>Apache Dubbo</strong>发布首个3.0分支预览版本3.0.0.preview时，官方已预告6月份将发布3.0正式版。</p> 
<p style="text-align:start">恰逢端午假期，前方传来最新消息，Dubbo项目的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases" target="_blank">GitHub发布页面</a>3.0.0版已显示为预发布状态。按照惯例，需要发起社区邮件投票，通过后将进入正式版本的发布流程。Apache  Dubbo 3.0.0版发布后，相关构建稍后将会同步至Maven中央仓库，并提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Forg.apache.dubbo%2Fdubbo" target="_blank">下载</a>。</p> 
<p style="text-align:start"><img alt="Dubbo Architecture" src="https://oscimg.oschina.net/oscnet/up-2281931ac68a65cecb77495e99f84c95a1a.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">Apache Dubbo 3.0版本核心特性</h2> 
<ul> 
 <li>应用级服务发现机制</li> 
 <li>下一代RPC协议: <strong>Triple</strong></li> 
 <li><span style="color:#252525">全新的路由规则</span></li> 
 <li><span style="color:#252525">显著的性能提升</span></li> 
 <li>Kubernetes 服务集成</li> 
</ul> 
<h2 style="text-align:start"><span style="color:#252525">分支差异</span></h2> 
<p style="text-align:start"><span style="color:#252525">在 master 分支的 03223c7 提交之前的大部分更改已迁移至 3.0.0版本。</span></p> 
<h2 style="text-align:start"><span style="color:#252525">升级兼容性</span></h2> 
<p style="text-align:start"><span style="color:#252525">    几乎兼容2.7.x 版本所有相同的行为。</span></p> 
<h2 style="text-align:start"><span style="color:#252525">扩展</span></h2> 
<p style="text-align:start"><span style="color:#252525">Dubbo核心仓库的版本发布中将不再提供第三方 SDK 的一些扩展，现提供 dubbo-spi-extensions 项目来支持这些不太常用的扩展。</span></p> 
<p style="text-align:start"><span style="color:#252525">目前支持的扩展：</span></p> 
<ul> 
 <li><span style="color:#252525">Zookeeper作为注册中心、Metadata Report</span><span style="color:#252525">、配置中心</span></li> 
 <li><span style="color:#252525">Nacos作为注册中心、</span> <span style="background-color:#ffffff; color:#24292e">Metadata Report</span><span style="color:#252525">、配置中心</span></li> 
 <li><span style="color:#252525">Kubernetes注册中心</span> </li> 
 <li>Redis作为<span style="background-color:#ffffff; color:#24292e">Metadata Report</span></li> 
 <li>Apollo<span style="color:#252525">配置中心</span></li> 
 <li><span style="color:#252525">提供</span> <span style="color:#252525">Hessian2 和 jdk 作为默认序列化程序</span></li> 
 <li>Triple<span style="color:#252525">协议支持Protobuf</span></li> 
</ul> 
<h2 style="text-align:start">升级迁移<span style="color:#252525">注意事项</span></h2> 
<ul> 
 <li> <p><span style="color:#252525">部分Spring 相关配置列表可能会发生变化，官方将在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdubbo.apache.org%2Fzh%2Fdocs%2Fv3.0%2F" target="_blank">dubbo-website</a> 中提供升级指南。</span></p> </li> 
 <li> <p><span style="color:#252525">为提供高质量的兼容性，</span><span style="color:#252525">Dubbo 3 早期版本默认开启双注册双订阅。</span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            