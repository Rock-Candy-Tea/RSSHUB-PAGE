
---
title: 'KtConnect v0.3.2 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2333'
author: 开源中国
comments: false
date: Mon, 28 Mar 2022 23:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2333'
---

<div>   
<div class="content">
                                                                    
                                                        <p><u><strong>项目介绍</strong></u></p> 
<p>KtConnect是一款能让开发者本地运行的服务与Kubernetes集群中的服务双向互连的实用工具，由阿里云·云效团队开源。</p> 
<p>🐬提供以下功能🐬</p> 
<ul> 
 <li>直接访问集群任意资源IP：打通本地与Kubernetes集群网络，本地直连任意Pod IP、服务Cluster IP</li> 
 <li>本地解析集群服务域名：使本地能直接用服务名或完整域名访问集群Service，同时不影响本地原有的域名解析</li> 
 <li>本地服务一秒添加到集群：从Kubernetes集群直接访问开发者本地的服务进程，快速预览验证开发中的功能效果</li> 
 <li>用本地服务置换集群服务：将Kubernetes集群中的指定服务临时替换为本地服务，快速进行端到端功能测试联调</li> 
</ul> 
<p><u><strong>更新内容</strong></u></p> 
<ul> 
 <li>增加Recover命令用于立即恢复指定服务被Exchange或Mesh的流量</li> 
 <li>Connect运行时自动静默清理集群里的过期资源，可部分替代手工执行Clean命令的功能</li> 
 <li>Connect命令增加--useShadowDeployment参数，支持使用Deployment部署Shadow容器</li> 
 <li>Connect命令增加--podQuota参数，支持配置ShadowPod和RouterPod的资源限额</li> 
 <li>Connect命令路由规则不再读取节点的PodCIDR配置，去除对节点权限的依赖</li> 
 <li>Connect命令的hosts域名解析模式增加对Service变化的监听和自动适配</li> 
 <li>Exchange和Mesh的目标被占用时，显示占用者信息</li> 
 <li>Mesh命令的manual模式现在统一使用Service名作为目标参数</li> 
 <li>修复Windows环境在某些情况下路由设置不生效的问题</li> 
 <li>修复Windows环境下CPU和内存占用时常飙高的问题</li> 
 <li>修复ktctl未加子命令时的运行报错</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fdownloads" target="_blank">下载地址</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            