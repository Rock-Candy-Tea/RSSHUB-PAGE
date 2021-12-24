
---
title: 'KtConnect v0.2.4 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5329'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 22:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5329'
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
 <li>支持Mesh命令的Auto模式使用Service名指定访问目标</li> 
 <li>新增Exchange命令的Switch模式，退出时不再需要等待Pod恢复</li> 
 <li>移除Shadow Pod的默认密码，统一使用临时私钥访问，提高安全性</li> 
 <li>修复本地kube config文件未配置Namespace时，ktctl运行必须指定Namespace的问题</li> 
 <li>修复使用Ctrl+C中断Exchange退出等待时概率性未清理Shadow Pod的问题</li> 
 <li>修复启动Sshuttle失败时程序无法自动退出的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            