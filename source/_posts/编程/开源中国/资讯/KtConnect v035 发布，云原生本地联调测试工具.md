
---
title: 'KtConnect v0.3.5 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=611'
author: 开源中国
comments: false
date: Mon, 30 May 2022 00:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=611'
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
 <li>增加Config命令用于支持全局默认配置</li> 
 <li>Exchange/Mesh/Preview命令支持跳过本地端口检查</li> 
 <li>增加对本地路由只有部分设置成功情况的检查</li> 
 <li>去除Connect命令对集群Namespace查询权限的依赖</li> 
 <li>支持自定义本地DNS的代理目标地址和顺序</li> 
 <li>支持定制嵌入kubeconfig配置</li> 
 <li>规范化本地配置目录结构并更名为".kt"</li> 
 <li>修复一处Hosts文件修改影响内网域名访问的问题</li> 
 <li>修复Windows下与OpenVPN共存时的DNS顺序问题</li> 
 <li>修复某些Windows环境本地路由未正确移除的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            