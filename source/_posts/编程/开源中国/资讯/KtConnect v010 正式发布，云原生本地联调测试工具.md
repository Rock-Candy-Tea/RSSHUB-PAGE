
---
title: 'KtConnect v0.1.0 正式发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=758'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 23:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=758'
---

<div>   
<div class="content">
                                                                                            <p><u><strong>项目介绍</strong></u></p> 
<p>KtConnect是一款能让开发者本地运行的服务与Kubernetes集群中的服务双向互连的实用工具，由阿里云·云研发团队开源。</p> 
<p>🐬提供以下功能🐬</p> 
<ul> 
 <li>直接访问集群任意服务地址：打通本地与Kubernetes集群网络，本地直连任意Pod IP、服务Cluster IP和服务域名</li> 
 <li>本地服务一秒添加到集群：从Kubernetes集群直接访问开发者本地的服务进程，快速预览验证开发中的功能效果</li> 
 <li>用本地服务置换集群服务：将Kubernetes集群中的指定服务临时替换为本地服务，快速进行端到端功能测试联调</li> 
</ul> 
<p><u><strong>更新内容</strong></u></p> 
<ul> 
 <li>增强Windows下的connect命令支持</li> 
 <li>移除对本地kubectl客户端工具的依赖</li> 
 <li>新增适用于Linux的tun连接模式（alpha）</li> 
 <li>使用provide命令替代run命令</li> 
 <li>新增clean命令，清理集群中残留的代理Pod</li> 
 <li>支持service.namespace.svc结构的服务域名解析</li> 
 <li>完善缺失sshuttle依赖等运行时错误的报错信息</li> 
 <li>connect命令的dump2hosts参数支持完整服务域名</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            