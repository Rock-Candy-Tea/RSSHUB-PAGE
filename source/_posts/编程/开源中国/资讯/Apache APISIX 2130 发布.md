
---
title: 'Apache APISIX 2.13.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aedcb216c8a16d403771a6dc127a445bd26.png'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 17:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aedcb216c8a16d403771a6dc127a445bd26.png'
---

<div>   
<div class="content">
                                                                                            <p>距离 Apache APISIX 上一次发布 LTS 版本已经过去了大半年的时间，今天，Apache APISIX 社区带来了一个全新的 LTS 版本——2.13.0。该 LTS 版本不仅性能更加稳定，而且支持了更多的可观测性、服务发现插件和更完善的多语言开发体系。</p> 
<p>如果你在追求整体稳定性的同时，也想尝试一下新功能，不妨考虑将现有的 Apache APISIX 升级到 2.13.0。后续社区也会在 2.13.0 版本的基础上发布一系列 patch 版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-aedcb216c8a16d403771a6dc127a445bd26.png" referrerpolicy="no-referrer"></p> 
<h2>功能更新</h2> 
<h3>新变化：不再默认暴露 API</h3> 
<p>在 2.13.0 之前的版本中，我们允许插件注册可供客户端调用的 API。例如，<code>jwt-auth</code> 插件会注册一个 JWT 签名的接口，客户端可以访问该接口，以生成用于校验的签名。但这个设计有一个潜在的缺陷——由于暴露出来的是接口而不是路由，因此无法像对待路由一样为其加强安全防护。虽然现有的机制允许用户通过编写对应的 plugin interceptor 来拦截接口访问，但这种方式仍然存在安全隐患。</p> 
<p><strong>所以从 2.13.0 版本开始，我们决定做出重大变更，不再默认暴露</strong> <strong>API</strong>**。**如果用户需要暴露接口，则需要通过 <code>public-api</code> 插件将接口绑定到对应的路由上。这种方式会带来两个好处：</p> 
<ol> 
 <li>注册的 API 会有更高的能见度，目前注册的 API 只有通过显示配置才会生效，访问方式也是由用户自定义。</li> 
 <li>允许采用更多的安全防护选项，注册的 API 和路由拥有同样的权限控制。</li> 
</ol> 
<p>当然，2.13.0 版本还有其他的新变化，比如修复了历史版本的不合理行为。如需了解具体优化信息，请查阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fapisix%2Fblob%2Frelease%2F2.13%2Fdocs%2Fzh%2Flatest%2FCHANGELOG.md%232130" target="_blank">2.13.0 Changelog</a>。</p> 
<h3>新功能：可观测性层面对接更多的监控体系</h3> 
<p>作为 API 网关，Apache APISIX 一直致力于连接更多的服务，打通更多的可观测性上下游。我们在每个版本都会为此添砖加瓦，2.13.0 版本也不例外。</p> 
<p><strong>这次我们新增了一个 tracing 插件：</strong><code>**opentelemetry**</code>**，允许发送 OpenTelemetry tracing 数据到配置的 collector。**下面简单通过一个示例来看一下。</p> 
<p>在静态配置里面设置了 collector：</p> 
<pre><code class="language-YAML">plugin_attr:
  opentelemetry:
    resource:
      service.name: APISIX
      tenant.id: business_id
    collector:
      address: "127.0.0.1:4317"
    batch_span_processor:
      drop_on_queue_full: false
      max_queue_size: 6
      batch_timeout: 2
      inactive_timeout: 1
      max_export_batch_size: 2
</code></pre> 
<p>之后就可以在特定的路由上开启 tracing：</p> 
<pre><code class="language-PowerShell">curl http://127.0.0.1:9080/apisix/admin/routes/1  -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
&#123;
    "methods": ["GET"],
    "uris": [
        "/uid/*"
    ],
    "plugins": &#123;
        "opentelemetry": &#123;
            "sampler": &#123;
                "name": "always_on"
            &#125;
        &#125;
    &#125;,
    "upstream": &#123;
        "type": "roundrobin",
        "nodes": &#123;
            "127.0.0.1:8089": 1
        &#125;
    &#125;
&#125;'
</code></pre> 
<p>命中该路由的请求将会上报 OpenTelemetry 的数据到对应的 collector。</p> 
<p><strong>此外，我们还新增了两个日志插件，支持把日志上报到 ClickHouse 和 Loggly 中。</strong></p> 
<p>ClickHouse 是地表最快的 OLAP 数据库之一。Apache APISIX 支持发送 access log 和 error log 到 ClickHouse，示例如下：</p> 
<pre><code class="language-PowerShell">curl http://127.0.0.1:9080/apisix/admin/routes/1 -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
&#123;
      "plugins": &#123;
            "clickhouse-logger": &#123;
                "user": "default",
                "password": "a",
                "database": "default",
                "logtable": "test",
                "endpoint_addr": "http://127.0.0.1:8123"
            &#125;
       &#125;,
      "upstream": &#123;
           "type": "roundrobin",
           "nodes": &#123;
               "127.0.0.1:1980": 1
           &#125;
      &#125;,
      "uri": "/hello"
&#125;'
curl http://127.0.0.1:9080/apisix/admin/plugin_metadata/error-log-logger -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
&#123;
  "clickhouse": &#123;
      "user": "default",
      "password": "a",
      "database": "error_log",
      "logtable": "t",
      "endpoint_addr": "http://127.0.0.1:8123"
  &#125;
&#125;'
</code></pre> 
<p>Loggly 是 SolarWinds 旗下的日志处理 SaaS 平台，我们支持通过 syslog 或 HTTP/HTTPS 的方式发送 access log。示例如下：</p> 
<p>配置上报方式</p> 
<pre><code class="language-PowerShell">curl http://127.0.0.1:9080/apisix/admin/plugin_metadata/loggly -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
&#123;
   "protocol": "http"
&#125;'
</code></pre> 
<p>配置需要上报的路由</p> 
<pre><code class="language-PowerShell">curl http://127.0.0.1:9080/apisix/admin/routes/1 -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
&#123;
    "plugins":&#123;
        "loggly":&#123;
            "customer_token":"xxx",
        &#125;
    &#125;,
    "upstream":&#123;
        "type":"roundrobin",
        "nodes":&#123;
            "127.0.0.1:80":1
        &#125;
    &#125;,
    "uri":"/index.html"
&#125;'
</code></pre> 
<h3>更完善的多语言开发体系</h3> 
<p>Apache APISIX 自 2.11 版本起开始支持 Wasm（Proxy Wasm SDK），但 LTS 版本一直没有提供相应支持。在此次发布的 Apache APISIX 2.13.0 版本中，我们新增并完善了该功能。</p> 
<p>在经过半年超过 10000 行代码（包括测试和文档）的开发后，APISIX 现已全面支持在<strong>处理请求头、请求体、响应头、响应体四个阶段运行 Wasm 代码</strong>。2.13.0 版本是第一个支持 Wasm 的 LTS 版本，可以说是一个新的里程碑。</p> 
<p>除了 Wasm 之外，我们也正在开发传统的、基于 RPC 的多语言插件体系。不久之前，我们发布了 Python Runner 0.2.0 版本。几天后，我们也会发布 Go Runner 0.3.0 版本。</p> 
<h2>Bug 修复</h2> 
<ul> 
 <li> <p>SkyWalking 和 OpenTelemetry 没有追踪认证失败。</p> </li> 
 <li> <p><code>log-rotate</code> 切割日志不支持按整点完成。</p> </li> 
 <li> <p><code>deepcopy</code> 没有复制 <code>metatable</code>。</p> </li> 
 <li> <p><code>request-validate</code> 对 JSON 里面重复键的处理 。</p> </li> 
 <li> <p><code>prometheus</code> 重复计算指标。</p> </li> 
 <li> <p>当 <code>conf.headers</code> 缺失时，<code>proxy-rewrite</code> 中的 <code>conf.method</code> 不生效 。</p> </li> 
 <li> <p><code>traffic-split</code> 首条规则失败时无法匹配。</p> </li> 
 <li> <p>etcd 超时触发 <code>resync_delay</code> 。</p> </li> 
 <li> <p><code>proto</code> 定义冲突。</p> </li> 
 <li> <p><code>limit-count</code> 配置不变，重置计数器。</p> </li> 
 <li> <p>Admin API 的 <code>plugin-metadata</code> 和 <code>global-rule</code> 计数有误。</p> </li> 
 <li> <p>合并 route 和 service 时 labels 丢失。</p> </li> 
</ul> 
<h2>更多细节</h2> 
<p>除了上述功能和组件外，Apache APISIX 2.13.0 版本还更新了如下功能：</p> 
<ul> 
 <li>grpc-transcode 支持通过 <code>.pb</code> 文件处理带 import 的 proto 定义。</li> 
 <li>支持从 K8s 配置中获取上游节点。</li> 
 <li>新增 <code>csrf</code> 插件，提供跨站请求伪造防护。</li> 
 <li>新增 <code>mocking</code> 插件，方便生成测试数据。</li> 
</ul>
                                        </div>
                                      
</div>
            