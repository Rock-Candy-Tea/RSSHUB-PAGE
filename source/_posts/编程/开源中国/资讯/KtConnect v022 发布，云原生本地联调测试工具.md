
---
title: 'KtConnect v0.2.2 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6732'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 09:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6732'
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
 <li>exchange命令退出时将等待原服务Pod实例完全恢复再切流，防止退出过程中服务不可用</li> 
 <li>connect命令新增--excludeIps参数，用于排除指定的非集群IP段</li> 
 <li>connect命令新增--proxyAddr参数，用于指定Socks5代理监听的IP地址</li> 
 <li>exchange/mesh/provide命令增加本地端口是否有服务监听的检查</li> 
 <li>修复connect命令--cidr参数指定多个IP段出错的问题</li> 
 <li>修复当本地服务重启或响应超时以后，exchange的连接会自动断开的问题（重大BUG）</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            