
---
title: 'Taskover V2.1.0 发布，个人任务管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8510'
author: 开源中国
comments: false
date: Sat, 04 Sep 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8510'
---

<div>   
<div class="content">
                                                                                            <p>Taskover V2.1.0 已经发布，个人任务管理工具。</p> 
<h4>本次更新</h4> 
<ul> 
 <li>新增 Dockerfile</li> 
 <li>支持 Docker Compose、Kubernetes、Helm 等部署方式支持</li> 
</ul> 
<h4>Docker 部署</h4> 
<p>指定数据库以及相关信息，一条命令即可 Run 起来：</p> 
<pre><code>docker run -p3001:3001 -d --name=taskover \
-e DATABASE_HOST=10.211.55.2 \
-e DATABASE_PORT=3306 \
-e DATABASE_USER="zoker" \
-e DATABASE_PASSWORD="zoker" \
-e DATABASE_NAME="taskover" \
-e SECRET_KEY_BASE="ASECRETFORBUILD" \
-e RAILS_SERVE_STATIC_FILES=1 \
zoker/taskover:1.0.0
</code></pre> 
<h4>Docker Compose 部署</h4> 
<pre><code>docker-compose up
</code></pre> 
<h4>Kubernetes 部署</h4> 
<pre><code>cd src
kubectl create -f taskover.yaml
kubectl create -f taskover-svc.yaml
</code></pre> 
<h4>Helm Chart 部署</h4> 
<pre><code>cd src/k8s/helm
helm install taskover ./
</code></pre> 
<p>访问 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A3001" target="_blank">http://127.0.0.1:3001</a></p> 
<p>详情查看：<a href="https://gitee.com/kesin/taskover/releases/V2.1.0">https://gitee.com/kesin/taskover/releases/V2.1.0</a></p>
                                        </div>
                                      
</div>
            