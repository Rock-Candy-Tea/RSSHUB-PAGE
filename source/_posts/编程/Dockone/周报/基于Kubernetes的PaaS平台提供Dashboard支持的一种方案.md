
---
title: '基于Kubernetes的PaaS平台提供Dashboard支持的一种方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/0f635f3f309fe18344e98d566e05234f.png'
author: Dockone
comments: false
date: 2021-09-15 11:06:53
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/0f635f3f309fe18344e98d566e05234f.png'
---

<div>   
<br>我一直在负责维护的PaaS平台引入了Kubernetes作为底层支持，可以借助Kubernetes的生态做更多的事情，这篇博客主要介绍如何为用户提供Dashboard功能，以及一些可以扩展的想法。希望读者有一定的Kubernetes使用经验，并且了解RBAC的功能。<br>
<h3>Dashboard功能</h3>Kubernetes原生提供了Web界面，也就是Dashboard，具体的参考可以见官方文档：<a href="https://kubernetes.io/zh/docs/tasks/access-application-cluster/web-ui-dashboard/" rel="nofollow" target="_blank">https://kubernetes.io/zh/docs/ ... oard/</a>：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/0f635f3f309fe18344e98d566e05234f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/0f635f3f309fe18344e98d566e05234f.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
安装完成后，我们一般是通过Token来使用的，不同的Token有着不同的权限。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/f79339fddbb1e6a363d33bca6ca016b7.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/f79339fddbb1e6a363d33bca6ca016b7.jpeg" class="img-polaroid" title="02.jpeg" alt="02.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
上面所说的<code class="prettyprint">Token</code>是<code class="prettyprint">Bearer Token</code>，除了在界面上输入之外，你可以这么来用，通过添加header即可。<br>
<pre class="prettyprint">curl -H "Authorization: Bearer $&#123;TOKEN&#125;" https://&#123;dashboard&#125;/api/myresource<br>
</pre><br>
<h3>PaaS平台使用Dashboard简要讨论</h3><h4>需求分析</h4>Dashboard本身的功能是十分强大的，但是给所有人admin权限显然是不现实的。对于一个普通用户来讲，PaaS平台的将他的应用（代码）部署好并运行，他所需要关注的就只有属于他自己的项目，平台也需要做好权限控制，避免一个用户操作了另一个用户的应用。<br>
<h4>权限系统设计</h4>基于以上的需求讨论，平台需要做的操作就是为每个用户创建属于自己的权限提供，并限制可以访问到的资源。考虑这样的情况：<br>
<br>我们有一个用户A，他拥有自己的一个应用群组（G），群组中部署了一系列应用程序（a1, a2…）。在Kubernetes中，这样的群组概念我们将其映射为namespace，<code class="prettyprint">群组（G）&lt;=> 用户空间（NS）</code>，我们需要控制的权限控制策略就变成了用户A在用户空间NS的权限控制。<br>
<h4>Token分发策略</h4>拥有了权限控制后，所需要打就是将Token分发给用户，当然这是一种极度不安全的做法，Kubernetes中的Token创建之后一般是不会改变的，分发这样的Token会有很大的安全风险，有两个方面：<br>
<ol><li>用户A将Token保存了下来，那么他就能不经过平台登录Dashboard，这样不利于审计工作</li><li>Token一旦泄露，PaaS平台很难做到反应（因为Token脱离了平台的控制，无法判断究竟是什么时候发生了泄露，也无法马上吊销这个Token），安全风险比较高</li></ol><br>
<br>因此, 最好的做法就是不把Token交给用户，用户每次想要登录Dashboard，从平台进行跳转，跳转时携带安全信息，在Dashboard登录时，由平台自己的程序请求Token，避免经手用户。<br>
<br><strong>注意</strong>：如果到这里，你没有理解上面的内容，建议回去再看一次需求，如果还是理解不了，就不要往下看了，下面只是介绍具体的实现方案。<br>
<h3>Kubernetes权限限制</h3>Kubernetes本身有着比较复杂的权限控制系统，设计时没必要纠结过多，按照可以给用户和不能给用户的权限进行区分就好了。我直接贴一下我的权限控制策略吧，并不一定适合每个人，只是可以做个参考。<br>
<pre class="prettyprint">---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: Role<br>
metadata:<br>
name: xxx:xxx-group-yyy<br>
namespace: xxx-group-yyy<br>
rules:<br>
# 可以查看当前NS下面的service，pod，logs，events<br>
- apiGroups: [""]<br>
resources: ["services", "pods", "pods/log", "events"]<br>
verbs: ["get", "list", "watch"]<br>
<br>
# 可以使用exec命令进入容器<br>
- apiGroups: [""]<br>
resources: ["pods/exec"]<br>
verbs: ["create", "list", "watch"]<br>
<br>
# 可以查看deployments和replicasets<br>
- apiGroups: ["extensions", "apps"]<br>
resources: ["deployments", "replicasets"]<br>
verbs: ["get", "list", "watch"]<br>
<br>
# 可以查看job，cronjob以及ingress<br>
- apiGroups: ["batch", "extensions"]<br>
resources: ["cronjobs", "jobs", "ingresses"]<br>
verbs: ["get", "list", "watch"]<br>
</pre><br>
正如上面的注释一样，尽可能只给用户只读的权限，也许你已经发现了，甚至不需要给用户namespace的查看权限，这也是为了安全，避免用户得知其他人的namespace。<br>
<h3>分发Token以及安全性保证</h3>这是本篇博客的核心内容：如何使得用户可以无感知的登录到Dashboard（对用户隐藏Token）。<br>
<br>该方案用到的方法是：添加一层访问控制的网关，用于处理Token获取的操作，具体的流程图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/1a98e41a014d17fabf2f924a0b9d0e5e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/1a98e41a014d17fabf2f924a0b9d0e5e.png" class="img-polaroid" title="03.png" alt="03.png" referrerpolicy="no-referrer"></a>
</div>
<br>
需要注意的有几点：<br>
<ol><li>PaaS给出的<code class="prettyprint">secret_code</code>是有时效性的，不允许用户一直用同一个<code class="prettyprint">secret_code</code>进行访问</li><li>网关与PaaS平台间的通信应该加密，网关必须是PaaS平台可信的</li><li>网关不应该长期保存<code class="prettyprint">Token</code></li><li>网关的访问最好添加OpenID校验，确保网关可以精确定位到每个用户的每次访问</li></ol><br>
<br><h4>体验优化</h4><ol><li>首先，第2步到第3步，<code class="prettyprint">secret_code</code>获取之后，可以以302重定向的方式跳转至网关入口</li><li>网关可以临时性的保存<code class="prettyprint">secret_code</code>与<code class="prettyprint">Token</code>的映射关系，既能够提升用户体验，也能有效减缓PaaS平台的压力</li><li>Dashbaord的webshell功能是基于websocket支持的，所以请确保你的网关可以通过websocket请求，否则终端连接后几分钟就断了，websocket可以持续几个小时那么久</li><li>跳转到网关时，可以携带更多的信息，比如携带某个Pod的ID，网关就可以直接跳转到对应的Pod，用户打开webshell就很方便了</li></ol><br>
<br>网关的实现我不做过多的说明了，只有一点建议，<code class="prettyprint">secret_code</code>在跳转到网关后，马上进行校验。由于<code class="prettyprint">Dashboard</code>的前端路由实现问题，<code class="prettyprint">secret_code</code>最好在校验后加密放置到cookie中，实现方面的问题其他可以发邮件与我讨论。<br>
<h3>总结</h3>这篇博客主要介绍了一种允许普通用户使用Dashboard的功能。在实现策略上，利用了Kubernetes的权限限制，Token隐藏的方案，该方案目前我已经加入到了我负责的PaaS平台中，稳定性方面可以满足工作需求，安全性正如博客中介绍，大家可以自行斟酌。<br>
<br>我很抱歉博客中字多图少，也没有给出具体的实现。首先代码实现是不重要的，其次因为是公司的代码，不方便分享，请见谅。<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2020/12/05/2020-12-" rel="nofollow" target="_blank">https://corvo.myseu.cn/2020/12/05/2020-12-05-</a>基于Kubernetes的PaaS平台提供dashboard支持的一种方案/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            