
---
title: 'KtConnect v0.1.1 正式发布，云原生本地联调测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7732'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 00:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7732'
---

<div>   
<div class="content">
                                                                                            <p><u><strong>项目介绍</strong></u></p> 
<p>KtConnect是一款能让开发者本地运行的服务与Kubernetes集群中的服务双向互连的实用工具，由阿里云·云研发团队开源。提供以下功能</p> 
<p>🐬提供以下功能🐬</p> 
<ul> 
 <li>直接访问集群任意服务地址：打通本地与Kubernetes集群网络，本地直连任意Pod IP、服务Cluster IP和服务域名</li> 
 <li>本地服务一秒添加到集群：从Kubernetes集群直接访问开发者本地的服务进程，快速预览验证开发中的功能效果</li> 
 <li>用本地服务置换集群服务：将Kubernetes集群中的指定服务临时替换为本地服务，快速进行端到端功能测试联调</li> 
</ul> 
<p><u><strong>更新内容</strong></u></p> 
<ul> 
 <li>发布包从tar.gz格式改为zip格式，方便Windows用户使用</li> 
 <li>新增--serviceAccount参数支持指定代理Pod使用的ServiceAccount</li> 
 <li>新增--useKubectl参数支持使用本地kubectl工具连接集群</li> 
 <li>增强clean命令支持清理残留的ConfigMap和注册表数据</li> 
 <li>修复Kubernetes地址有上下文路径会导致无法连接的问题</li> 
 <li>修复执行connect使用sudo导致.ktctl目录owner变成root的问题</li> 
</ul> 
<p><u><strong>项目文档</strong></u></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fquickstart" target="_blank">快速开始</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Fkt-connect%2F%23%2Fzh-cn%2Fdownloads" target="_blank">下载地址</a></li> 
</ul>
                                        </div>
                                      
</div>
            