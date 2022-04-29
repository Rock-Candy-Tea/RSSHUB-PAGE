
---
title: 'KtConnect v0.3.3 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1699'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 12:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1699'
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
 <li>支持在任意位置使用全局参数</li> 
 <li>mesh命令对带有未知Header值的请求改为路由到默认环境，不再报"404"错误</li> 
 <li>exchange和mesh命令支持使用端口名称定义的Service Port</li> 
 <li>clean命令支持清理本地残留的路由表配置</li> 
 <li>启动时显示当前连接的Kubernetes集群名称和配置的context名称</li> 
 <li>当无法找到可用端口时，尝试监听随机端口，规避某些环境下端口检查逻辑不正常的问题</li> 
 <li>修复mesh命令退出时，Router Pod没有被正确删除的问题</li> 
 <li>修复preview命令创建的Service误用--expose参数本地端口号的问题</li> 
 <li>修复由于开发者之间的本地时间不一致，导致误清理集群未过期资源的问题</li> 
 <li>修复由于Cluster IP段与API Server地址重合，导致DNS端口Port Forward失败的问题</li> 
 <li>修复代理DNS对CName记录的域名处理不当的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fguide%2Fdownloads" target="_blank">下载地址</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            