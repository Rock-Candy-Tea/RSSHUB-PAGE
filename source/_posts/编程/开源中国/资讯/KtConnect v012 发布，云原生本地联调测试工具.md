
---
title: 'KtConnect v0.1.2 发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5006'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 09:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5006'
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
 <li>自动解析本地DNS配置，移除connect命令的--localDomain参数</li> 
 <li>使用vpn模式时自动检测并安装sshuttle，简化初次使用的准备工作</li> 
 <li>解决Exchange和Mesh连接闲置超时报"lost connection to pod"的问题</li> 
 <li>修复Connect命令开启debug模式时无法连接的错误</li> 
 <li>优化Windows环境下的屏幕输出，适配非管理员用户的使用场景</li> 
 <li>新增--imagePullSecret参数支持指定拉取代理Pod镜像使用的Secret（感谢@pvtyuan的提交）</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            