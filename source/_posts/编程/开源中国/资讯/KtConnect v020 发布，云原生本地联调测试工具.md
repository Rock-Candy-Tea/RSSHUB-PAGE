
---
title: 'KtConnect v0.2.0 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1258'
author: 开源中国
comments: false
date: Sun, 17 Oct 2021 13:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1258'
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
 <li>Kubernetes最低兼容版本提高到1.16</li> 
 <li>使用更轻量的代理Pod替换代理Deployment</li> 
 <li>在Windows下的socks模式默认不再自动设置全局代理</li> 
 <li>新增开启自动全局代理的--setupGlobalProxy参数</li> 
 <li>新增Exchange命令的ephemeral模式（实验性功能）</li> 
 <li>修复Exchange命令连接时常卡顿的问题（重大BUG修复）</li> 
 <li>去除Connect命令的--global参数，自动适配用户权限</li> 
 <li>优化Connect命令的--cidr参数，支持指定多个IP区段</li> 
 <li>当PortForward目标端口被占用时提供更优雅的报错信息</li> 
 <li>参数--label更名为--withLabel</li> 
 <li>增加--withAnnotation参数为代理Pod增加额外标注</li> 
 <li>Connect命令增加--disablePodIp参数支持禁用Pod IP路由</li> 
 <li>在代理Pod上增加Kt-User标注用于记录本地用户名</li> 
 <li>移除Check命令</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            