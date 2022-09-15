
---
title: 'DRYCC Workflow v1.6.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1282'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 17:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1282'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">RYCC 工作流是一个开源的超融合 PAAS 云，它基于 kubernetes、servicebroker 等技术，为运维人员、开发人员添加提供了一个方便快捷的工具，使应用程序的部署和管理变得容易。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">DRYCC 工作流包括通过 git push 从源代码构建和部署的功能、简单的应用程序配置、创建和回滚发布、管理域名和 SSL 证书、提供无缝边缘路由、聚合日志以及与团队共享应用程序。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装方法</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">首先准备一台纯净的 ubuntu/centos 主机，我们假设它的外网 IP 为<span><span> </span>209.119.4.8，系统为 ubuntu20.04，假设使用 nip.io 作为域名服务，我们需要导入如下环境变量：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>export <span style="color:#032f62">CHANNEL=stable</span>
</code>export DRYCC_REGISTRY=registry.drycc.cc
export PLATFORM_DOMAIN=43.129.186.72.nip.io
export DRYCC_ADMIN_USERNAME=admin
export DRYCC_ADMIN_PASSWORD=admin
export MINIO_PERSISTENCE_SIZE=60Gi
</pre> 
<p>如果主机在国内，则需要增加如下环境变量做镜像加速:</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6f42c1">export</span> <span style="color:#032f62">INSTALL_DRYCC_MIRROR=cn</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果主机在内网，不存在外网 IP，则需要关闭 ACME 自动证书:</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span>export</span> CERT_MANAGER_ENABLED=<span style="color:#005cc5">false</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">安装系统软件</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>apt-get <span style="color:#d73a49">update</span>
apt-<span style="color:#d73a49">get</span> <span style="color:#d73a49">install</span> curl haproxy nfs-common <span style="color:#d73a49">open</span>-iscsi</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">安装 DRYCC</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#005cc5">curl</span> -sfL https://www.drycc.cc/install.sh | bash -</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">发布内容</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Drycc 从 21 年 9 月份到现在，过去了一年整整时间，在过去的一年里发生了很多激动人心的变化，从存储到网络Drycc做到了真正统一，Drycc storage组件支持对象存储和多写卷存储，因此不再需要诸如longhorn等外部的存储组件<span style="background-color:#ffffff; color:#4d4d4d">；同时将drycc的所有组件均支持云原生部署，</span>本次主要更新如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">* Database组件中引入Patron，支持高可用、多副本、故障自动切换。<br> * Influxdb组件支持多写方案，很简陋的实现，虽然不完美，但是可以工作。<br> * drycc-cli支持远程执行命令，从此以后小伙伴们不用再羡慕`kubectl exec`了。<br> * drycc-cli支持持续输出日志流，小伙伴们也不用羡慕`tail -f`了，drycc也能做到。</p> 
<p>时光飞逝，由于时隔整整一年的时间，有太多的变化，真是一言难尽；Drycc，未来已来，你来不来？</p> 
<p> </p> 
<p> </p> 
<p>小编先不要审核通过，我没发现草稿功能，这个是先保存草稿用的。</p>
                                        </div>
                                      
</div>
            