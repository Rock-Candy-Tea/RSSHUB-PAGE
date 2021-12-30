
---
title: 'KtConnect v0.2.5 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4231'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 23:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4231'
---

<div>   
<div class="content">
                                                                                            <p><u><strong>项目介绍</strong></u></p> 
<p>KtConnect是一款能让开发者本地运行的服务与Kubernetes集群中的服务双向互连的实用工具，由阿里云·云效团队开源。</p> 
<p>🐬提供以下功能🐬</p> 
<ul> 
 <li>直接访问集群任意服务地址：打通本地与Kubernetes集群网络，本地直连任意Pod IP、服务Cluster IP和服务域名</li> 
 <li>本地服务一秒添加到集群：从Kubernetes集群直接访问开发者本地的服务进程，快速预览验证开发中的功能效果</li> 
 <li>用本地服务置换集群服务：将Kubernetes集群中的指定服务临时替换为本地服务，快速进行端到端功能测试联调</li> 
</ul> 
<p><u><strong>更新内容</strong></u></p> 
<ul> 
 <li>优化Provide命令的"--expose"参数，支持多端口和端口映射</li> 
 <li>优化Clean命令的清理标记方式，解决资源清理不彻底问题</li> 
 <li>优化Connect命令Pod IP范围的计算逻辑，避免对无关IP段的路由影响</li> 
 <li>添加"--nodeSelector"参数，支持指定Shadow Pod到指定节点</li> 
 <li>解决Auto Mesh以后，服务重新部署可能导致Mesh失效的问题</li> 
 <li>修复Clean命令清理时遇到状态已经是Terminating的资源会报错的问题</li> 
 <li>修复本地KubeConfig无全局Pod权限时Connect命令报错的问题</li> 
 <li>修复Connect命令在某些异常退出情况下会有资源残留的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            