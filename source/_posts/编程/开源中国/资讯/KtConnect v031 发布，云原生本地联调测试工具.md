
---
title: 'KtConnect v0.3.1 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3021'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3021'
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
 <li>支持指定多个KubeConfig配置文件并自动合并</li> 
 <li>支持自定义本地DNS缓存时长</li> 
 <li>修复Connect命令在某些环境下无法解析集群域名的问题</li> 
 <li>修复Exchange命令在连接自动恢复后依然打印出错日志的问题</li> 
 <li>修复Mesh命令在某些情况下会导致路由报502错误的问题</li> 
 <li>修复Clean命令对Exchange的遗留资源清理不彻底的问题</li> 
 <li>缩短心跳包间隔和服务锁超时，加速遗留资源清理</li> 
 <li>Shadow Pod和Router Pod的容器增加Ports属性</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            