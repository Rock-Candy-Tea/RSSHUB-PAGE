
---
title: 'Apache APISIX 2.8 正式发布，带来更多新功能！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8120'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 13:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8120'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache APISIX 2.8 版本正式发布！这个版本有 30+ 开发者参与，共提交了 100+ PR，支持了 1 个新功能、1 个新体验、2 个新插件、2 个新玩法，快来阅读了解 2.8 版本的新特性吧！</p> 
<h2>新功能：独立的 Keepalive 连接池</h2> 
<p>从2.7 版本开始添加 Apache APISIX 自己的补丁和 Nginx C 模块，增强原生 Nginx 的功能，希望能够动态设置越来越多的 Nginx 配置。在发布的最新版本中，Apache APISIX 已经支持在 Upstream 级别上配置独立的 Keepalive 连接池。目前包含了以下功能：</p> 
<ul> 
 <li> <p>动态设置 mTLS</p> </li> 
 <li> <p>动态设置 client_max_body_size</p> </li> 
 <li> <p>Upstream 的 keepalive（2.8 新功能）</p> </li> 
 <li> <p>gzip （2.8 新插件） 在 Apache APISIX 后续版本中，我们也会陆续允许下面的 Nginx 配置能够被动态设置：</p> </li> 
 <li> <p>real_ip</p> </li> 
 <li> <p>proxy_max_temp_file_size</p> </li> 
 <li> <p>……</p> </li> 
</ul> 
<p>Upstream 的配置举例：</p> 
<pre><code>&#123;
    "id": "backend",
    "nodes": &#123;"host:80": 100&#125;,
    "type":"roundrobin",
    "keepalive_pool": &#123;
        "size": 4,
        "idle_timeout": 8,
        "requests": 16
    &#125;
&#125;
</code></pre> 
<h2>新体验：stream 代理功能增强</h2> 
<p>在 2.8 版本中，把 ip-restriction 和 limit-conn 两个插件从 HTTP 部分的移植到了 stream 部分，这么做的好处是丰富网关在 stream 代理的功能，增加对上游服务的安全性保障。ip-restriction 可以用来做 IP 黑白名单过滤，保证只有来自特定 IP 的请求才能访问到后端服务。limit-conn 可以用来限制特定路由上同时存在的连接个数，限制客户端的并发访问量。</p> 
<h2>新插件：gzip 插件</h2> 
<p>2.8 版本中新增了 gzip 插件，使用 gzip 插件可以动态设置路由级别的 gzip 参数。</p> 
<p>gzip 配置举例：</p> 
<pre><code>&#123;
    "plugins": &#123;
        "gzip": &#123;
            "min_length": 20,
            "http_version": 1.1,
            "buffers": &#123;
                "number": 32,
                "size": 4096
            &#125;,
            "types": [
                "text/html"
            ],
            "comp_level": 1,
            "vary": false
        &#125;
    &#125;
&#125;
</code></pre> 
<h2>新插件：ua-restriction</h2> 
<p><code>ua-restriction</code> 插件用于校验 User-Agent 是否处于黑白名单中，黑白名单是一个非常常见的需求，现在可以通过插件的方式启用了。</p> 
<p><code>ua-restriction</code> 配置举例：</p> 
<pre><code>&#123;
    "plugins": &#123;
        "ua-restriction": &#123;
            "denylist": [
                "my-bot1",
                "(Baiduspider)/(\\d+)\\.(\\d+)"
            ]
        &#125;
    &#125;
&#125;
</code></pre> 
<h2>新玩法：支持通过插件的方式执行特定逻辑</h2> 
<p>得益于 Apache APISIX 架构，许多功能都是通过插件的方式实现的。从 2.8 版本开始，插件又添加了新玩法。现在 Apache APISIX 支持在选择上游节点之后，通过插件的方式执行特定逻辑。<br> 只需要在插件里定义下面的方法：</p> 
<pre><code>function _M.balancer(conf, ctx)
    core.log.notice("IP: ", ctx.balancer_ip, ", Port: ", ctx.balancer_port)
end
</code></pre> 
<p>在这个示例里，日志会输出上游的 IP 和 Port。</p> 
<p>什么场景下会运行上述方法？</p> 
<ol> 
 <li> <p>选择上游节点之后，访问上游之前</p> </li> 
 <li> <p>每次重试之前</p> </li> 
</ol> 
<p>出于性能考虑，上述方法首次运行在 OpenResty 的 access 阶段（实际上 APISIX 在 access 阶段就选好了上游节点），该方法并不与 OpenResty 的同名阶段重合。</p> 
<h2>新玩法：支持自定义 balancer</h2> 
<p>从 2.8 版本开始，用户可以自定义 balancer。这里的 balancer，是指最少连接数、轮询、一致性哈希等负载均衡器。</p> 
<p>虽然 Apache APISIX 已经提供了丰富的 balancer，但是用户可能需要用的 balancer 是和业务紧密相关的 balancer，比如：需要考虑机房、可用区等等。支持自定义 balancer，用户可以编写自己的 balancer，并通过 <code>require("apisix.balancer.your_balancer")</code>  加载到程序中。</p> 
<p>通常自定义的 balancer 需要 node 提供 host/port 以外的数据，可以把数据放到 metadata 里面，举个例子：</p> 
<pre><code>&#123;
    "nodes": [
        &#123; "host": "0.0.0.0", "port": 1980, "weight": 1, "metadata": &#123;"b": 1&#125; &#125;
    ]
&#125;
</code></pre> 
<h2>下载</h2> 
<p>下载 Apache APISIX 2.8</p> 
<ul> 
 <li> <p>源代码：请访问 https://apisix.apache.org/downloads/</p> </li> 
 <li> <p>二进制安装包：请访问 https://apisix.apache.org/zh/docs/apisix/how-to-build/</p> </li> 
</ul> 
<h1>关于 Apache APISIX</h1> 
<p>Apache APISIX 是一个动态、实时、高性能的开源 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。</p> 
<p>Apache APISIX 可以帮忙企业快速、安全的处理 API 和微服务流量，包括网关、Kubernetes Ingress 和服务网格等。全球已有数百家企业使用 Apache APISIX 处理关键业务流量，涵盖金融、互联网、制造、零售、运营商等等，比如美国航空航天局（NASA）、欧盟的数字工厂、中国航信、中国移动、腾讯、华为、微博、网易、贝壳找房、360、泰康、奈雪的茶等。</p> 
<p>200 余位贡献者，一同缔造了 Apache APISIX 这个世界上最活跃的开源网关项目。聪明的开发者们！快来加入这个活跃而多样化的社区，一起来给这个世界带来更多美好的东西吧！</p> 
<ul> 
 <li> <p>Apache APISIX 项目地址：https://github.com/apache/apisix</p> </li> 
 <li> <p>Apache APISIX 官网：https://apisix.apache.org/</p> </li> 
</ul>
                                        </div>
                                      
</div>
            