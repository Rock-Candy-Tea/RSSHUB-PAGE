
---
title: 'KubeCube v1.1 版本发布，部署更加轻量'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.kubecube.io/blog/2021/12/24/kubecube-v1.1-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83/imgs/auth-webhook.png'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 15:33:00 GMT
thumbnail: 'https://www.kubecube.io/blog/2021/12/24/kubecube-v1.1-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83/imgs/auth-webhook.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; text-align:left">KubeCube 迎来了 v1.1 版本的发布，新增了 OAuth2 的 GitHub 登录支持、租户配额的算法优化、Warden 热插拔安装包的本地和远端拉取支持等新的特性，也修复了若干已知问题，详见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubecube-io%2FKubeCube%2Fblob%2Frelease-v1.1%2Fdocs%2Fchangelog.md" target="_blank">ChangeLog</a>。</p> 
<p style="color:#222222; text-align:left">v1.1 版本中最主要的特性是 Auth-Proxy 能力的支持，使得部署更加轻量，无需侵入修改 kube-apiserver 的配置。用户可以使用 RESTful、client-go、kubectl 等方式访问被 KubeCube 纳管的 K8s 集群，享受统一的认证能力。</p> 
<h2 style="text-align:left">使用 Auth-Webhook 的困境</h2> 
<p style="color:#222222; text-align:left"><img alt="Auth-Webhook" src="https://www.kubecube.io/blog/2021/12/24/kubecube-v1.1-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83/imgs/auth-webhook.png" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; text-align:left">在 KubeCube v1.1 版本之前，KubeCube 使用 K8s 提供的 Auth-Webook 方式来拓展认证能力，该方式通过为 kube-apiserver 指定认证后端来达到认证拓展的目的，kube-apiserver 会使用认证 Webhook 返回的 UserInfo 去进行下一步的鉴权流程。</p> 
<p style="color:#222222; text-align:left">该方式虽然能够使用 K8s 原生的方式拓展认证能力，但是在实际使用中存在一定的不足。如<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubecube-io%2FKubeCube%2Fissues%2F62" target="_blank">Issues#62</a><span> </span>中所指出的，该方式需要修改 kube-apiserver 的启动参数，为其<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fzh%2Fdocs%2Freference%2Faccess-authn-authz%2Fauthentication%2F%23webhook-token-authentication" target="_blank">指定额外的认证 Webhook 后端</a>，当我们的 K8s 集群是多 Master 节点的高可用集群时，需要修改每一个 Master 节点的 kube-apiserver 的配置，这在很多场景几乎是无法接受的。另外在一些云厂商的托管 K8s 场景下，往往只对用户提供工作节点，此时想修改 kube-apiserver 的配置是非常困难的。</p> 
<h2 style="text-align:left">Warden-Auth-Proxy</h2> 
<p style="color:#222222; text-align:left"><img alt="Auth-Proxy" src="https://www.kubecube.io/blog/2021/12/24/kubecube-v1.1-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83/imgs/auth-proxy.png" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; text-align:left">对于 Auth-Webhook 面临的困境，我们设计了 Warden-Auth-Proxy 模块来解决问题。Warden-Auth-Proxy 即 K8s 集群的认证代理，它对外提供了类似<span> </span><code>kubectl proxy</code><span> </span>的代理能力。不同的是，它会解析 request 中的 Bearer Token 为 UserInfo，然后使用 K8s 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fzh%2Fdocs%2Freference%2Faccess-authn-authz%2Fauthentication%2F%23user-impersonation" target="_blank">impersonation 能力</a>进行用户伪装。</p> 
<p style="color:#222222; text-align:left">值得一提的是，Auth-Proxy 模块之所以集成在作为 Cluster Agent 的 Warden 中，而不是集成在管控集群的 KubeCube 中，是因为在设计上希望做到两点：</p> 
<ol> 
 <li>对于各个集群的请求能够就近访问本集群的代理服务，而不是跨集群访问 KubeCube 中的代理服务。</li> 
 <li>即使当 KubeCube 发生 Crash 的时候，各个集群的认证鉴权能力依然能够保持正常。</li> 
</ol> 
<p style="color:#222222; text-align:left">Auth-Proxy 的原理并不复杂，但是在实现中，需要注意以下几个问题：</p> 
<h3 style="text-align:left">1. kubectl exec 命令代理协议问题</h3> 
<p style="color:#222222; text-align:left">对于代理<span> </span><code>kubectl exec</code><span> </span>的场景，使用普通的 HTTP 代理并不可行，究其原因是因为通信协议不匹配。</p> 
<p style="color:#222222; text-align:left">不同于其他的 HTTP RESTful 请求，<code>kubectl exec</code><span> </span>命令实际是使用的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSPDY" target="_blank">SPDY 协议</a>，SPDY 协议是 google 开发的 TCP 会话层协议, SPDY 协议中将 HTTP 的 request/response 称为 Stream，并支持 TCP 的链接复用，同时多个 stream之间通过 stream-id 来进行标记，简单来说就是支持在单个链接同时进行多个请求响应的处理，并且互不影响 。</p> 
<p style="color:#222222; text-align:left">在代理<span> </span><code>kubectl exec</code><span> </span>请求时，需要 Upgrade HTTP 协议，即通过 101(switching protocal) 状态码切换至 SPDY 协议来继续与下游服务通信。</p> 
<div style="margin-left:0; margin-right:0; text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-go"><strong style="color:#204a87">func</strong> <strong style="color:#000000">(</strong><span style="color:#000000">h</span> <strong style="color:#ce5c00">*</strong><span style="color:#000000">UpgradeAwareHandler</span><strong style="color:#000000">)</strong> <span style="color:#000000">ServeHTTP</span><strong style="color:#000000">(</strong><span style="color:#000000">w</span> <span style="color:#000000">http</span><strong style="color:#000000">.</strong><span style="color:#000000">ResponseWriter</span><strong style="color:#000000">,</strong> <span style="color:#000000">req</span> <strong style="color:#ce5c00">*</strong><span style="color:#000000">http</span><strong style="color:#000000">.</strong><span style="color:#000000">Request</span><strong style="color:#000000">)</strong> <strong style="color:#000000">&#123;</strong>
  <em>// 尝试协议 upgrade
</em>  <strong style="color:#204a87">if</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">tryUpgrade</span><strong style="color:#000000">(</strong><span style="color:#000000">w</span><strong style="color:#000000">,</strong> <span style="color:#000000">req</span><strong style="color:#000000">)</strong> <strong style="color:#000000">&#123;</strong>
<strong style="color:#204a87">return</strong>
<strong style="color:#000000">&#125;</strong>
<strong style="color:#204a87">if</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">UpgradeRequired</span> <strong style="color:#000000">&#123;</strong>
<span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Responder</span><strong style="color:#000000">.</strong><span style="color:#000000">Error</span><strong style="color:#000000">(</strong><span style="color:#000000">w</span><strong style="color:#000000">,</strong> <span style="color:#000000">req</span><strong style="color:#000000">,</strong> <span style="color:#000000">errors</span><strong style="color:#000000">.</strong><span style="color:#000000">NewBadRequest</span><strong style="color:#000000">(</strong><span style="color:#4e9a06">"Upgrade request required"</span><strong style="color:#000000">))</strong>
<strong style="color:#204a87">return</strong>
<strong style="color:#000000">&#125;</strong>

  <strong style="color:#ce5c00">...</strong>

  <em>// 构建 golang 经典的 ReverseProxy
</em><span style="color:#000000">proxy</span> <strong style="color:#ce5c00">:=</strong> <span style="color:#000000">httputil</span><strong style="color:#000000">.</strong><span style="color:#000000">NewSingleHostReverseProxy</span><strong style="color:#000000">(</strong><strong style="color:#ce5c00">&</strong><span style="color:#000000">url</span><strong style="color:#000000">.</strong><span style="color:#000000">URL</span><strong style="color:#000000">&#123;</strong><span style="color:#000000">Scheme</span><strong style="color:#000000">:</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Location</span><strong style="color:#000000">.</strong><span style="color:#000000">Scheme</span><strong style="color:#000000">,</strong> <span style="color:#000000">Host</span><strong style="color:#000000">:</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Location</span><strong style="color:#000000">.</strong><span style="color:#000000">Host</span><strong style="color:#000000">&#125;)</strong>
<span style="color:#000000">proxy</span><strong style="color:#000000">.</strong><span style="color:#000000">Transport</span> <strong style="color:#000000">=</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Transport</span>
<span style="color:#000000">proxy</span><strong style="color:#000000">.</strong><span style="color:#000000">FlushInterval</span> <strong style="color:#000000">=</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">FlushInterval</span>
<span style="color:#000000">proxy</span><strong style="color:#000000">.</strong><span style="color:#000000">ErrorLog</span> <strong style="color:#000000">=</strong> <span style="color:#000000">log</span><strong style="color:#000000">.</strong><span style="color:#000000">New</span><strong style="color:#000000">(</strong><span style="color:#000000">noSuppressPanicError</span><strong style="color:#000000">&#123;&#125;,</strong> <span style="color:#4e9a06">""</span><strong style="color:#000000">,</strong> <span style="color:#000000">log</span><strong style="color:#000000">.</strong><span style="color:#000000">LstdFlags</span><strong style="color:#000000">)</strong>
<strong style="color:#204a87">if</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Responder</span> <strong style="color:#ce5c00">!=</strong> <strong style="color:#204a87">nil</strong> <strong style="color:#000000">&#123;</strong>
<span style="color:#000000">proxy</span><strong style="color:#000000">.</strong><span style="color:#000000">ErrorHandler</span> <strong style="color:#000000">=</strong> <span style="color:#000000">h</span><strong style="color:#000000">.</strong><span style="color:#000000">Responder</span><strong style="color:#000000">.</strong><span style="color:#000000">Error</span>
<strong style="color:#000000">&#125;</strong>
<span style="color:#000000">proxy</span><strong style="color:#000000">.</strong><span style="color:#000000">ServeHTTP</span><strong style="color:#000000">(</strong><span style="color:#000000">w</span><strong style="color:#000000">,</strong> <span style="color:#000000">newReq</span><strong style="color:#000000">)</strong>
<strong style="color:#000000">&#125;</strong>
</code></pre> 
</div> 
<h3 style="text-align:left">2. kubeconfig 配置问题</h3> 
<p style="color:#222222; text-align:left">对于使用 kubeconfig 与集群通信的场景，默认的 kubeconfig 中的<span> </span><code>cluster server</code><span> </span>的地址往往直接指向 kube-apiserver，这使得用户与集群的通信没有经过 Warden-Auth-Proxy 代理。</p> 
<p style="color:#222222; text-align:left">因此，对于上述场景，我们需要在 kubeconfig 上做文章。KubeCube 提供下载 kubeconfig 的能力，使用当前 user 下载的 kubeconfig，包含了 user 的访问凭证，包含了该 user 所能访问的所有 cluster 的 context，user 可以自行切换 context 来对 KubeCube 纳管的集群进行访问。KubeCube 通过改写 kubeconfig 中的 kube-apiserver 地址为 Warden-Auth-Proxy 地址来使得用户通过该 kubeconfig 执行的 kubectl 或 client-go 请求会被 Warden-Auth-Proxy 所代理。</p> 
<div style="margin-left:0; margin-right:0; text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><code class="language-yaml"><strong style="color:#204a87">apiVersion</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">v1</span><u>
</u><strong style="color:#204a87">clusters</strong><strong style="color:#000000">:</strong><u>
</u>- <strong style="color:#204a87">cluster</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">certificate-authority-data</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">member_1_cluster_ca_data&#125;</span><u>
</u><u>    </u><strong style="color:#204a87">server</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">member_1_warden_auth_proxy_addr&#125;</span><u>
</u><u>  </u><strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1</span><u>
</u>- <strong style="color:#204a87">cluster</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">certificate-authority-data</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">pivot_cluster_ca_data&#125;</span><u>
</u><u>    </u><strong style="color:#204a87">server</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">pivot_warden_auth_proxy_addr&#125;</span><u>
</u><u>  </u><strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">pivot-cluster</span><u>
</u><strong style="color:#204a87">contexts</strong><strong style="color:#000000">:</strong><u>
</u>- <strong style="color:#204a87">context</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">cluster</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1</span><u>
</u><u>    </u><strong style="color:#204a87">user</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1-admin</span><u>
</u><u>  </u><strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1-admin@member-1</span><u>
</u>- <strong style="color:#204a87">context</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">cluster</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">pivot-cluster</span><u>
</u><u>    </u><strong style="color:#204a87">user</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">pivot-cluster-admin</span><u>
</u><u>  </u><strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">pivot-cluster-admin@pivot-cluster</span><u>
</u><strong style="color:#204a87">current-context</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1-admin@member-1</span><u>
</u><strong style="color:#204a87">kind</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">Config</span><u>
</u><strong style="color:#204a87">users</strong><strong style="color:#000000">:</strong><u>
</u>- <strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">member-1-admin</span><u>
</u><u>  </u><strong style="color:#204a87">user</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">token</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">user_token&#125;</span><u>
</u>- <strong style="color:#204a87">name</strong><strong style="color:#000000">:</strong><u> </u><span style="color:#000000">pivot-cluster-admin</span><u>
</u><u>  </u><strong style="color:#204a87">user</strong><strong style="color:#000000">:</strong><u>
</u><u>    </u><strong style="color:#204a87">token</strong><strong style="color:#000000">:</strong><u> </u>&#123;<span style="color:#000000">user_token&#125;</span><u>
</u></code></pre> 
</div> 
<h3 style="text-align:left">3. security 通信安全问题</h3> 
<p style="color:#222222; text-align:left"><img alt="Auth-Proxy-security" src="https://www.kubecube.io/blog/2021/12/24/kubecube-v1.1-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83/imgs/auth-proxy-security.png" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; text-align:left">在对通信安全有较高要求的场景下，我们需要保证从<span> </span><code>Client——>Warden-Auth-Proxy——>kube-apiserver</code><span> </span>的通信链路是加密的，可靠的。我们使用以下方式加以保证：</p> 
<ul> 
 <li>KubeCube 使用 Bearer Token 作为用户访问凭证，Invalid Bearer Token 会被 Warden-Auth-Proxy 拒绝，相当于服务端要求验证客户端身份。</li> 
 <li>应使用 TLS 对 Warden-Auth-Proxy 进行服务端身份校验，需要相应的 CA 证书，该 TLS 能力在规划中，还未支持。当前使用<span> </span><code>insecure-skip-tls-verify</code><span> </span>跳过，在后续版本中，会增加对 TLS 能力的支持。</li> 
 <li>Warden-Auth-Proxy 与 kube-apiserver 之间，通过 mTLS 进行双向加密通信，Warden-Auth-Proxy 持有 K8s 集群的 admin 证书，并以 admin 身份伪装成目标 user 与 kube-apiserver 进行通信。</li> 
</ul> 
<h2 style="text-align:left">写在最后</h2> 
<p style="color:#222222; text-align:left">未来我们会持续提供更多功能，帮助企业简化容器化落地。也欢迎大家参与贡献，提出宝贵的建议。添加以下微信进入 KubeCube 交流群。</p> 
<p style="color:#222222; text-align:left"><img alt="kubecube微信" height="303" src="https://www.kubecube.io/imgs/kubecube-wechat.png" width="300" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; text-align:left"><strong>作者简介：</strong><span> </span>蔡鑫涛，网易数帆轻舟容器平台资深开发，KubeCube 核心 Committer</p>
                                        </div>
                                      
</div>
            