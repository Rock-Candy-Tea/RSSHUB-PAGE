
---
title: 'Apache APISIX 2.12.0 发布，云原生的微服务 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6213'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6213'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#3e3e3e">继 2.11.0 版本发布之后，Apache APISIX 也在即将到来的新春佳节，为大家带来 2022 年<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FZvRFPIszdSfumSvJzQx7vw" target="_blank">第一个带有新功能的版本</a>。</span></p> 
<h3><strong><span style="background-color:#ffffff; color:#3e3e3e">新功能</span></strong></h3> 
<h4><strong>更多的 Serverless 集成</strong></h4> 
<p style="margin-left:0; margin-right:0">在上个版本里，Apache APISIX 增加了对 Azure Function 的支持。而这次新版本在功能上又加入了对更多 Serverless 厂商的支持。如今用户也可以在 Apache APISIX 中结合 AWS Lambda 和 Apache OpenWhisk，在网关上进行特定函数的暴露。</p> 
<h4><strong>更多的鉴权插件</strong></h4> 
<p style="margin-left:0; margin-right:0">此次的新版本，还将带来两个众人翘首以盼的新插件：<span style="background-color:#f5f6f7; color:#c7254e">forward-auth</span> 和 <span style="background-color:#f5f6f7; color:#c7254e">opa<span style="background-color:#ffffff; color:#333333">。</span></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><code><span style="color:#ab1942">forward-auth</span></code><span> 插件跟 Traefik 的同名插件功能类似，该插件可以允许把当前请求的信息发送给外部服务进行鉴权。</span></p> </li> 
</ul> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><code><span style="color:#ab1942">opa</span></code><span>插件则整合了著名的 Open Policy Agent，该插件可以通过 OPA 来完成复杂的鉴权功能。</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">通过上述两个插件，将为 Apache APISIX 的鉴权功能锦上添花，给用户带来更多丰富和上手简单的鉴权操作。</p> 
<h4><strong>更多的日志功能</strong></h4> 
<p style="margin-left:0; margin-right:0">除了上边提到的鉴权插件，本次新版本还将带来三个新的日志插件：<code><span style="color:#ab1942">google-cloud-logging</span></code><span> 、</span><span style="background-color:#f5f6f7; color:#c7254e">splunk-hec-logging</span><span> 以及 </span><span style="background-color:#f5f6f7; color:#c7254e">rocketmq-logger</span><span>。</span></p> 
<p style="margin-left:0; margin-right:0">从插件名称上也很容易理解，通过上述三个插件可以把日志分别发送到 Google Cloud、Splunk 和 Apache RocketMQ。未来，Apache APISIX 将会对接越来越多的日志服务商和开源 Broker，让日志处理变得更加轻松。</p> 
<ul> 
 <li><strong>支持记录响应体</strong></li> 
</ul> 
<p style="margin-left:0; margin-right:0">同时，此次 2.12.0 版本还在日志层面支持记录响应体。与 Apache APISIX 其他功能一样，该功能也可以通过表达式进行动态开启。这样在使用中，就可以实现仅在上游返回特定的 Content-Type 和 Content-Length 时进行日志记录，不用再去顾虑全量采集响应体而带来的问题了。</p> 
<p style="margin-left:0; margin-right:0">具体示例可参考下方：</p> 
<pre><code><span>&#123;</span></code><code><span>    <span style="color:#dd1144">"plugins"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"kafka-logger"</span>: &#123;</span></code><code><span>            <span style="color:#dd1144">"broker_list"</span> : &#123;</span></code><code><span>                <span style="color:#dd1144">"127.0.0.1"</span>:9092</span></code><code><span>            &#125;,</span></code><code><span>            <span style="color:#dd1144">"kafka_topic"</span> : <span style="color:#dd1144">"test2"</span>,</span></code><code><span>            <span style="color:#dd1144">"include_resp_body"</span>: true,</span></code><code><span>            <span style="color:#dd1144">"include_resp_body_expr"</span>: [</span></code><code><span>                [</span></code><code><span>                    <span style="color:#dd1144">"sent_http_content_length"</span>,</span></code><code><span>                    <span style="color:#dd1144">"<"</span>,</span></code><code><span>                    <span style="color:#dd1144">"4096"</span></span></code><code><span>                ],</span></code><code><span>                [</span></code><code><span>                    <span style="color:#dd1144">"sent_http_content_type"</span>,</span></code><code><span>                    <span style="color:#dd1144">"=="</span>,</span></code><code><span>                    <span style="color:#dd1144">"application/json"</span></span></code><code><span>                ],</span></code><code><span>            ]</span></code><code><span>        &#125;</span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"upstream"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"nodes"</span>: &#123;</span></code><code><span>            <span style="color:#dd1144">"127.0.0.1:1980"</span>: 1</span></code><code><span>        &#125;,</span></code><code><span>        <span style="color:#dd1144">"type"</span>: <span style="color:#dd1144">"roundrobin"</span></span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"uri"</span>: <span style="color:#dd1144">"/hello"</span></span></code><code><span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#feffff; color:#3e3e3e">上述配置会仅在 Content-Length < 4096 且 Content-Type 为 "application/json" 才记录日志。</span></p> 
<ul> 
 <li><strong>支持注册自定义变量</strong></li> 
</ul> 
<p style="margin-left:0; margin-right:0">另一个跟日志紧密相关的功能，就是新版本的 Apache APISIX 已支持注册自定义变量。同时结合 APISIX 的自定义日志格式，就可以实现完全自定义上报的日志内容。即无需修改具体的日志插件，就能实现日志生成和上报的解耦合。这里我们通过一个示例进行简单演示一下。</p> 
<p style="margin-left:0; margin-right:0">比如我们可以在自己的插件中注册一个 <code><span style="color:#ab1942">a6_route_labels</span></code><span style="background-color:#ffffff; color:#3e3e3e"> 的变量：</span></p> 
<pre><code><span>local core = require <span style="color:#dd1144">"apisix.core"</span></span></code>
<code><span>core.ctx.register_var(<span style="color:#dd1144">"a6_route_labels"</span>, function(ctx)</span></code><code><span>    local route = ctx.matched_route and ctx.matched_route.value</span></code><code><span>    if route and route.labels then</span></code><code><span>        return route.labels</span></code><code><span>    end</span></code><code><span>    return nil</span></code><code><span>end)</span></code></pre> 
<p style="margin-left:0; margin-right:0">并在自定义日志格式中使用它：</p> 
<pre><code><span>&#123;</span></code><code><span>    <span style="color:#dd1144">"log_format"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"host"</span>: <span style="color:#dd1144">"$host"</span>,</span></code><code><span>        <span style="color:#dd1144">"labels"</span>: <span style="color:#dd1144">"$a6_route_labels"</span>,</span></code><code><span>        <span style="color:#dd1144">"client_ip"</span>: <span style="color:#dd1144">"$remote_addr"</span></span></code><code><span>    &#125;</span></code><code><span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0">假设我们的 Route 长这样：</p> 
<pre><code><span>&#123;</span></code><code><span>    <span style="color:#dd1144">"plugins"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"http-logger"</span>: &#123;</span></code><code><span>            <span style="color:#dd1144">"uri"</span>: <span style="color:#dd1144">"http://127.0.0.1:1980/log"</span>,</span></code><code><span>            <span style="color:#dd1144">"batch_max_size"</span>: 1,</span></code><code><span>            <span style="color:#dd1144">"concat_method"</span>: <span style="color:#dd1144">"json"</span></span></code><code><span>        &#125;</span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"upstream"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"nodes"</span>: &#123;</span></code><code><span>            <span style="color:#dd1144">"127.0.0.1:1982"</span>: 1</span></code><code><span>        &#125;,</span></code><code><span>        <span style="color:#dd1144">"type"</span>: <span style="color:#dd1144">"roundrobin"</span></span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"labels"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"k"</span>: <span style="color:#dd1144">"v"</span></span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"uri"</span>: <span style="color:#dd1144">"/hello"</span></span></code><code><span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0">最终就会收到如下所示的日志：</p> 
<pre><code><span><span style="color:#dd1144">&#123;"client_ip":"127.0.0.1","host":"localhost","labels":&#123;"k":"v"&#125;,"route_id":"1"&#125;</span></span></code></pre> 
<h4><strong>L4 代理支持 TLS over TCP 上游</strong></h4> 
<p style="margin-left:0; margin-right:0">在 2.12.0 版本中还引入了新的 Upstream Scheme，现在 Apache APISIX 已支持代理到 TLS over TCP 上游了。</p> 
<p style="margin-left:0; margin-right:0">具体做法可参考下方，只需在 Upstream 配置中指明 Scheme 为 TLS 即可。</p> 
<pre><code><span>&#123;</span></code><code><span>    <span style="color:#dd1144">"scheme"</span>: <span style="color:#dd1144">"tls"</span>,</span></code><code><span>    <span style="color:#dd1144">"nodes"</span>: &#123;</span></code><code><span>        <span style="color:#dd1144">"127.0.0.1:1995"</span>: 1</span></code><code><span>    &#125;,</span></code><code><span>    <span style="color:#dd1144">"type"</span>: <span style="color:#dd1144">"roundrobin"</span></span></code><code><span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0">至此 Apache APISIX 的 TCP 代理功能得到了 TLS 全方位的支持。此外，我们还支持在静态文件中配置 L4 代理的 Access Log：​​​​​​​</p> 
<pre><code><span><span style="color:#dd1144">stream:</span></span></code><code><span>    enable_access_log: false         <em># enable access log or not, default false</em></span></code><code><span>    access_log: logs/access_stream.log</span></code><code><span>    access_log_format: <span style="color:#dd1144">"$remote_addr [$time_local] $protocol $status $bytes_sent $bytes_received $session_time"</span></span></code><code><span>                                            <em># create your custom log format by visiting http://nginx.org/en/docs/varindex.html</em></span></code><code><span>    access_log_format_escape: default       <em># allows setting json or default characters escaping in variables</em></span></code></pre> 
<h3><strong>更新</strong></h3> 
<h4><strong><span style="background-color:#ffffff; color:#3e3e3e">多语言插件持续完善</span></strong></h4> 
<ul> 
 <li><strong>WASM 生态功能更加丰富</strong></li> 
</ul> 
<p style="margin-left:0; margin-right:0">在之前版本中，Apache APISIX 已开放了对 WASM 生态的支持。而在 2.12.0 版本中，针对 WASM 生态又做了不少的更新细节。</p> 
<p style="margin-left:0; margin-right:0">目前 Apache APISIX 已经支持在 header_filter 的阶段运行 WASM 代码，弥补了现有外部插件无法修改响应的不足。</p> 
<p style="margin-left:0; margin-right:0">此外，我们还支持在 WASM 里面通过 Apache APISIX 这个宿主进行 HTTP 通讯。借助这一功能，我们用 WASM 也重新实现了<span> </span><code><span style="color:#ab1942">forward-auth</span></code><span> 插件。该插件的功能几乎和 Lua 版本一模一样，甚至连测试用例也是在 Lua 版本上改了下名字就能通过了。</span></p> 
<ul> 
 <li><strong>Java Plugin Runner 最新版本发布</strong></li> 
</ul> 
<p style="margin-left:0; margin-right:0">当然，我们也没有忘记针对现有的外部插件进行更新，本次 2.12.0 版本中，Apache APISIX 已允许外部插件获取请求体。</p> 
<p style="margin-left:0; margin-right:0">比如最近发布的 Java Plugin Runner 第二版就包含了这一功能。新版本的 Java Plugin Runner 还支持在运行时动态获取 APISIX 变量。</p> 
<h3><strong>完善</strong></h3> 
<h4><strong>更多细节</strong></h4> 
<p style="margin-left:0; margin-right:0">除了上述新功能和组件外，Apache APISIX 2.12.0 版本还更新了如下功能：</p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">gRPC-Web 的支持：继 gRPC 代理、HTTP 转 gRPC 之后，我们迎来了 gRPC 家族的第三个成员。现在 Apache APISIX 也支持代理 gRPC Web 协议了。</p> </li> 
</ul> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"> <code><span style="color:#ab1942">limit-count</span></code><span> 的增强：如今 </span><span style="background-color:#f5f6f7; color:#c7254e">limit-count</span><span> 插件的计数器已经支持在请求间、路由间进行共享，可以说是相当灵活了。</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>更多关于 Apache APISIX 2.12.0 的更新细节，可以查看本次发布对应的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fapisix%2Fblob%2Frelease%2F2.12%2FCHANGELOG.md%232120" target="_blank">Change log</a></span><span>。</span>​​​​​​​</p> 
<h3><strong>下载</strong></h3> 
<p style="margin-left:0; margin-right:0">想要获取最新的 Apache APISIX 2.12.0 版本，可通过以下路径下载：</p> 
<p style="margin-left:0; margin-right:0; text-align:left">源代码：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fdownloads%2F" target="_blank">https://apisix.apache.org/downloads/</a></p> 
<p style="margin-left:0; margin-right:0; text-align:left">二进制安装包：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fzh%2Fdocs%2Fapisix%2Fhow-to-build%2F" target="_blank">https://apisix.apache.org/zh/docs/apisix/how-to-build/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            