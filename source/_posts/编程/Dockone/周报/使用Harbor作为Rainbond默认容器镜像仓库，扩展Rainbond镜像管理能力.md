
---
title: '使用Harbor作为Rainbond默认容器镜像仓库，扩展Rainbond镜像管理能力'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: '<a href='
author: Dockone
comments: false
date: 2021-12-07 05:09:50
thumbnail: '<a href='
---

<div>   
<br>Rainbond是一体化的云原生应用管理平台，它提供“以应用为中心”的抽象，使用者不需要学习K8s和容器，平台将K8s和容器封装在内部，这种封装方式能极大提高使用的易用性和安装的便利性，但封装的内部组件如何替换是一个问题，本文将讲解如何使用Harbor替换掉Rainbond原有的默认镜像仓库。<br>
<br><h4>Harbor简介</h4><a href="https://goharbor.io/"><strong>Harbor</strong></a> 是一个用于存储和分发Docker镜像的企业级Registry服务器，也是首个中国原创的云原生基金会（CNCF）的开源企业级DockerRegistry项目，通过添加一些企业必需的功能特性，例如安全、标识和管理等，扩展了开源Docker Distribution。作为一个企业级私有Registry服务器，Harbor提供了更好的性能和安全。提升用户使用Registry构建和运行环境传输镜像的效率。<br>
<br><h4>通Harbor解决Rainbond镜像管理问题</h4>​       Rainbond之前默认使用的是Docker 提供的基础Registry，使用的过程中有很多问题，例如镜像安全性，镜像清理复杂麻烦等等问题，经过不断的调研，而Harbor不仅能解决这些问题，还能扩充很多镜像管理能力，Harbor 的功能主要包括四大类：多用户的管控（基于角色访问控制和项目隔离）、镜像管理策略（存储配额、制品保留、漏洞扫描、来源签名、不可变制品、垃圾回收等）、安全与合规（身份认证、扫描和CVE例外规则等）和互操作性（Webhook、内容远程复制、可插拔扫描器、REST API、机器人账号等）。<br>
<br><h4>对接Harbor</h4>​       目前harbor支持两种形式对接Rainbond,一种是作为rainbond内部基础存储仓库，另外一种就是作为外部自定义镜像仓库。<br>
<ul><li>Harbor作为Rainbond内部基础存储仓库，进行对接非常简单，只需要在初始化平台集群的时候进行自定义即可。</li></ul><br>
<br><img src="<a href="https://pic.imgdb.cn/item/61a429c02ab3f51d9106c4f1.jpg%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a4 ... ot%3B</a>/><br>
<br>​       <br>
<br>​       Yaml文件的格式要求非常严格，避免大家在配置的时候出现问题，已把正确的yaml文件放在下面，复制就可以使用。<br>
<br>​       <strong>注意：</strong>一定修改仓库的名字，仓库的项目名称, 用户名，以及密码，不然会出现镜像上传失败的问题。<br>
<pre class="prettyprint">例：<br>
apiVersion: rainbond.io/v1alpha1<br>
kind: RainbondCluster<br>
metadata:<br>
name: rainbondcluster<br>
namespace: rbd-system<br>
spec:<br>
imageHub:<br>
domain: www.est.com/test<br>
password: Harbor12345<br>
username: admin<br>
</pre><br>
<ul><li>Harbor作为rainbond的外部仓库进行提供服务，是基于harbor以及rainbond的webhook功能，配置如下。<br>
<ul>- 保证组件已经开启了镜像仓库的webhook功能，且应用状态不是已关闭状态，并且需要将应用的 webhooks url 配置到目标镜像仓库的 webhooks 中</ul></li></ul><br>
<br><img src="<a href="https://pic.imgdb.cn/item/61a5951e2ab3f51d919ea0df.png%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a5 ... ot%3B</a>/><br>
<ul><li>目标镜像仓库里面，新建一个webhook，然后在 Endpoint 地址填写应用的 webhooks url，配置符合需求的触发事件类型即可</li></ul><br>
<br><img src="<a href="https://pic.imgdb.cn/item/61a5951e2ab3f51d919ea0ea.png%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a5 ... ot%3B</a>/> <br>
<ul><li>通过Harbor实现镜像可视化存储管理，提高了工作的便利性。</li></ul><br>
<br><img src="<a href="https://pic.imgdb.cn/item/61a6cabf2ab3f51d9172ca88.png%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a6 ... ot%3B</a>/><br>
<ul><li>基于Rainbond进行构建的时候实现漏洞自动扫描，提高了安全管理。</li></ul><br>
<br><img src="<a href="https://pic.imgdb.cn/item/61a6cb0e2ab3f51d9172f17e.png%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a6 ... ot%3B</a>/><br>
<ul><li><br>通过镜像自动清理的策略，合理利用存储，降低存储成本。<br>
<ul><li>推荐使用策略：应用到仓库匹配**, 保留最近推送的3个 artifacts基于条件tags匹配**基于条件 无 Tag</li><li>推荐定时清理：自定义 cron :  0 0 0 1 */1 *  (秒，分，时，日，月，周)</li></ul></li><li>镜像是否被签名，漏洞的等级，也可以设置成为镜像安全策略之一，这样可以保证签名过的镜像或者漏洞等级低的镜像才可以被拉取。</li></ul><br>
<br><h4>整合后的整体流程</h4><img src="<a href="https://pic.imgdb.cn/item/61a439b22ab3f51d910d5d1c.png%22" rel="nofollow" target="_blank">https://pic.imgdb.cn/item/61a4 ... ot%3B</a> style="zoom: 50%;" /><br>
<br>​       通过上面流程图可以看到，整个搭载配置的过程，用户可以自定义镜像源进行拉取镜像，经过Rainbond平台自动推送到Harbor镜像仓库里面，然后等镜像扫描完成以后在进行自动拉取，自动进行构建容器实例。<br>
<br>----<br>
<br> <a href="https://www.rainbond.com/?channel=dockone"><strong>Rainbond</strong></a> 是完全开源的企业级，面向应用的云原生 DevOps， 开发、测试、生产运维一体化平台，不要求开发者掌握容器、Kubernetes 等复杂能力，面向开发者友好；提供从源码或简单镜像持续构建云原生应用的能力，对源码无侵入，业务持续发布到云端；高效的自动化运维，帮助开发者高效管理高可用的、安全的且去中心化的业务系统。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/images/%E5%85%AC%E4%BC%97%E5%8F%B7%E4%BA%8C%E7%BB%B4%E7%A0%81.gif" alt referrerpolicy="no-referrer">
                                
                                                              
</div>
            