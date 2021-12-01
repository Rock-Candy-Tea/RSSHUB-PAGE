
---
title: 'Apache APISIX 2.11.0 正式发布，蓄力两月带来更多新功能！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9586'
author: 开源中国
comments: false
date: Wed, 01 Dec 2021 09:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9586'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">Apache APISIX 2.11.0 版本是继上次 2.10.0 LTS 版本发布后，第一个带有新功能的版本。不仅丰富了插件库，还带来了新鲜的生态支持。具体功能详情大家可以下划查看哦。</p> 
<p style="margin-left:0; margin-right:0"><em>新功能</em></p> 
<p style="margin-left:0; margin-right:0"><strong>新增基于<span style="color:#ff3c00"><span> </span>LDAP<span> </span></span>的认证插件</strong></p> 
<p style="margin-left:0; margin-right:0">Apache APISIX 长长的认证插件名单上又添加了新成员——基于 LDAP的<span> </span><code>ldap-auth</code><span> </span>插件。通过该插件我们可以打通 LDAP 的账户体系和 Apache APISIX 的 Consumer 机制。</p> 
<p style="margin-left:0; margin-right:0">我们通过代码端简单进行示例展示：</p> 
<pre style="margin-left:0; margin-right:0"><code><span>curl http://127.0.0.1:9080/apisix/admin/consumers -H <span style="color:#dd1144">'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1'</span> -X PUT -d <span style="color:#dd1144">'</span></span></code><code><span>&#123;</span></code><code><span>    "username": "user01",</span></code><code><span>    "plugins": &#123;</span></code><code><span>        "ldap-auth": &#123;</span></code><code><span>            "user_dn": "cn=user01,ou=users,dc=example,dc=org"</span></code><code><span>        &#125;</span></code><code><span>    &#125;</span></code><code><span>&#125;'</span></code></pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<pre style="margin-left:0; margin-right:0"><code><span>curl http://127.0.0.1:9080/apisix/admin/routes/1 -H <span style="color:#dd1144">'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1'</span> -X PUT -d <span style="color:#dd1144">'</span></span></code><code><span>&#123;</span></code><code><span>    "methods": ["GET"],</span></code><code><span>    "uri": "/hello",</span></code><code><span>    "plugins": &#123;</span></code><code><span>        "ldap-auth": &#123;</span></code><code><span>            "base_dn": "ou=users,dc=example,dc=org",</span></code><code><span>            "ldap_uri": "localhost:1389",</span></code><code><span>            "uid": "cn"</span></code><code><span>        &#125;,</span></code><code><span>    &#125;,</span></code><code><span>    "upstream": &#123;</span></code><code><span>        "type": "roundrobin",</span></code><code><span>        "nodes": &#123;</span></code><code><span>            "127.0.0.1:1980": 1</span></code><code><span>        &#125;</span></code><code><span>    &#125;</span></code><code><span>&#125;'</span></code></pre> 
<p style="margin-left:0; margin-right:0">在上述配置中，我们把<span> </span><code>user01</code><span> </span>绑定到<span> </span><code>route 1</code><span> </span>上。这样我们在访问<span> </span><code>route 1</code><span> </span>时就带上了<span> </span><code>user01</code><span> </span>的密码，就可以通过 LDAP 的身份认证了。</p> 
<p style="margin-left:0; margin-right:0">运行结果就像这样：</p> 
<pre style="margin-left:0; margin-right:0"><code><span>$ curl -i -uuser01:password1 http://127.0.0.1:9080/hello</span></code><code><span>HTTP/1.1 200 OK</span></code><code><span>...</span></code><code><span>hello, world</span></code></pre> 
<p style="margin-left:0; margin-right:0"><em>新功能</em></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#ff3c00">可观测性</span><span>层面对接更多监控体系</span></strong></p> 
<p style="margin-left:0; margin-right:0">新版本的 Apache APISIX 丰富了对外部监控服务的支持。在这方面，我们新增了两个插件：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">上报指标到 datadog 的 <code>datadog</code><span> </span>插件</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">上报访问日志到 Apache Skywalking 的 <code>skywalking-logger</code><span> </span>插件</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">Datadog 是海外广泛使用的 SaaS 监控服务，而 Apache Skywalking 是享誉全球的开源监控软件。如今用户只需在路由上简单配置一下，就能实现与它们的对接。</p> 
<p style="margin-left:0; margin-right:0">Datadog 示例：</p> 
<pre style="margin-left:0; margin-right:0"><code><span>curl http://127.0.0.1:9080/apisix/admin/routes/1 -H <span style="color:#dd1144">'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1'</span> -X PUT -d <span style="color:#dd1144">'</span></span></code><code><span>&#123;</span></code><code><span>      "plugins": &#123;</span></code><code><span>            "datadog": &#123;&#125;</span></code><code><span>       &#125;,</span></code><code><span>      "upstream": &#123;</span></code><code><span>           "type": "roundrobin",</span></code><code><span>           "nodes": &#123;</span></code><code><span>               "127.0.0.1:1980": 1</span></code><code><span>           &#125;</span></code><code><span>      &#125;,</span></code><code><span>      "uri": "/hello"</span></code><code><span>&#125;'</span></code></pre> 
<p style="margin-left:0; margin-right:0">Apache SkyWalking 示例：</p> 
<pre style="margin-left:0; margin-right:0"><code><span>curl http://127.0.0.1:9080/apisix/admin/routes/1 -H <span style="color:#dd1144">'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1'</span> -X PUT -d <span style="color:#dd1144">'</span></span></code><code><span>&#123;</span></code><code><span>      "plugins": &#123;</span></code><code><span>            "skywalking-logger": &#123;</span></code><code><span>                "endpoint_addr": "http://127.0.0.1:12800"</span></code><code><span>            &#125;</span></code><code><span>       &#125;,</span></code><code><span>      "upstream": &#123;</span></code><code><span>           "type": "roundrobin",</span></code><code><span>           "nodes": &#123;</span></code><code><span>               "127.0.0.1:1980": 1</span></code><code><span>           &#125;</span></code><code><span>      &#125;,</span></code><code><span>      "uri": "/hello"</span></code><code><span>&#125;'</span></code></pre> 
<p style="margin-left:0; margin-right:0"><em>新功能</em></p> 
<p style="margin-left:0; margin-right:0"><strong>通过网关暴露<span> </span><span style="color:#ff3c00">Azure</span><span> </span>的<span> </span><span style="color:#ff3c00">FaaS</span><span> </span>函数</strong></p> 
<p style="margin-left:0; margin-right:0">网关能做的不仅仅是代理内部服务，我们也可以用它来连接外部的系统。</p> 
<p style="margin-left:0; margin-right:0">现在通过<span> </span><code>azure-functions</code><span> </span>插件，就可以利用 HTTP 请求触发 Azure functions 服务上的函数了。</p> 
<p style="margin-left:0; margin-right:0">接下来我们将通过下方示例来展示如何把 Azure 上配置好的函数，跟 Apache APISIX 上<span> </span><code>/azure_HttpTrigger</code><span> </span>路由连接起来。​​​​​​​</p> 
<pre style="margin-left:0; margin-right:0"><code><span>curl http://127.0.0.1:9080/apisix/admin/routes/1 -H <span style="color:#dd1144">'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1'</span> -X PUT -d <span style="color:#dd1144">'</span></span></code><code><span>&#123;</span></code><code><span>    "plugins": &#123;</span></code><code><span>        "azure-functions": &#123;</span></code><code><span>            "function_uri": "http://test-apisix.azurewebsites.net/api/HttpTrigger",</span></code><code><span>            "authorization": &#123;</span></code><code><span>                "apikey": "<Generated API key to access the Azure-Function>"</span></code><code><span>            &#125;</span></code><code><span>        &#125;</span></code><code><span>    &#125;,</span></code><code><span>    "uri": "/azure_HttpTrigger"</span></code><code><span>&#125;'</span></code></pre> 
<p style="margin-left:0; margin-right:0">对该路由的访问，等价于对 FaaS 平台上的函数调用。与此同时，我们也可以在此过程中加入鉴权、限流等对应的限制。</p> 
<p style="margin-left:0; margin-right:0"><em>新功能</em></p> 
<p style="margin-left:0; margin-right:0"><strong>提供<span> </span><span style="color:#ff3c00">WASM</span><span> </span>相关支持</strong></p> 
<p style="margin-left:0; margin-right:0">目前 Apache APISIX 已开始提供对 WASM 的初步支持。凭借 Proxy WASM SDK，我们可以采用 Lua 以外的语言，编写运行在 Apache APISIX 内部的插件。</p> 
<p style="margin-left:0; margin-right:0">有别于之前的外部插件功能，这一机制是运行在 Apache APISIX 内部的，所以在性能上相比之前会更加出色。</p> 
<p style="margin-left:0; margin-right:0">在 Apache APISIX 里使用 WASM 插件，就像采用 Lua 插件一样，两者都支持在路由和全局范围上生效。我们在 Apache APISIX 代码仓库里放置了一个基于 WASM 实现的<span> </span><code>fault-injection</code><span> </span>插件，感兴趣的读者可以看一下它跟 Lua 版本的同名插件的区别。</p> 
<p style="margin-left:0; margin-right:0">更多关于 Apache APISIX 支持 WASM 的技术细节可以参考：https://apisix.apache.org/zh/blog/2021/11/19/apisix-supports-wasm</p> 
<p style="margin-left:0; margin-right:0">目前 Apache APISIX 对 WASM 的支持还处于早期阶段，我们会在接下来的几个版本中逐渐去完善与丰富相关细节。</p> 
<p style="margin-left:0; margin-right:0"><em>完善</em></p> 
<p style="margin-left:0; margin-right:0"><strong><span>现有<span style="color:#ff3c00">插件</span>功能更为丰富</span></strong></p> 
<p style="margin-left:0; margin-right:0">当然，除了上述新增的多项功能，我们还完善了 Apache APISIX 现有插件功能，比如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">limit-req/conn/count 等插件现已支持采用一组变量作为限制时的 key</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">proxy-cache 引入基于内存的后端 </p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">更多插件新功能与新增组件细节，可参考本次发布对应的 Change log[1]。</p> 
<p style="margin-left:0; margin-right:0"><strong>下载</strong></p> 
<p style="margin-left:0; margin-right:0">获取最新版本的 Apache APISIX 2.11.0，可通过以下方式进行下载安装：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">源代码：请访问https://apisix.apache.org/downloads/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">二进制安装包：请访问https://apisix.apache.org/zh/docs/apisix/how-to-build/</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">[1]: https://github.com/apache/apisix/blob/release/2.11/CHANGELOG.md#2110</p> 
<p style="margin-left:0; margin-right:0"><strong>关于 Apache APISIX</strong></p> 
<p style="margin-left:0; margin-right:0">Apache APISIX 是一个动态、实时、高性能的开源 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。Apache APISIX 可以帮助企业快速、安全地处理 API 和微服务流量，包括网关、Kubernetes Ingress 和服务网格等。</p> 
<p style="margin-left:0; margin-right:0"><strong>Apache APISIX 落地用户（仅部分）</strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Apache APISIX GitHub：https://github.com/apache/apisix</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Apache APISIX 官网：https://apisix.apache.org/</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Apache APISIX 文档：https://apisix.apache.org/zh/docs/apisix/getting-started</span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            