
---
title: 'KtConnect v0.3.6 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4124'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 11:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4124'
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
 <li>增加birdseye命令用于查看集群各Service的重定向状态</li> 
 <li>增加forward命令用于将集群的Service映射到本地端口</li> 
 <li>connect命令增加--ingressIp参数用于支持Ingress域名解析</li> 
 <li>connect命令增加--includeDomains参数，支持额外的MacOS域名后缀</li> 
 <li>config命令兼容set key = value格式</li> 
 <li>在Windows下开启--disableTunDeivce时，自动切换为hosts DNS模式</li> 
 <li>完善config命令的参数自动补全</li> 
 <li>优化CIDR的合并逻辑，避免在API Server IP与CIDR相近时导致空的IP范围</li> 
 <li>修复一处导致无法多人同时对同一个Service使用mesh命令的BUG</li> 
 <li>修复Windows环境下误退出时移除非Kt路由的BUG</li> 
 <li>修复Mac环境..svc格式域名失效的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            