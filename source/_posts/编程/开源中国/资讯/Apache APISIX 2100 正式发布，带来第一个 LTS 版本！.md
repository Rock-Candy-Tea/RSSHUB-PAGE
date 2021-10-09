
---
title: 'Apache APISIX 2.10.0 正式发布，带来第一个 LTS 版本！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7319'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 11:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7319'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0"><span>Apache APISIX 2.10 版本正式发布！<span>这是</span><span style="color:#ff3c37"><strong>Apache APISIX 首个 LTS 版本</strong>，<span style="color:#3e3e3e">同时支持 10+ 个新功能和新插件。快速阅读了解 2.10.0 版本的新特性吧！</span></span></span></p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>里程碑：第一个 </strong><span style="color:#ff0000"><strong>LTS</strong></span><strong><span> </span>版本</strong></h2> 
<p style="margin-left:0; margin-right:0">对于 Apache APISIX 来说，本次发布的 2.10.0 是一个具有里程碑意义的版本，因为 Apache APISIX 2.10.0 是我们的第一个 LTS （Long Time Support）的版本。</p> 
<p style="margin-left:0; margin-right:0">我们会在 Apache APISIX 2.10.0 的基础上发布后续的 patch 版本，也就是 2.10.1、2.10.2 等版本。这些版本会从主分支上 backport bugfix。</p> 
<p style="margin-left:0; margin-right:0">按计划，10 月份我们会发布首个 LTS 版本的首个 patch 版本，也就是  Apache APISIX 2.10.1。</p> 
<p style="margin-left:0; margin-right:0">之后我们会交替发布 2.10.x（例如 2.10.2 ） 和 2.x（例如 2.11.0）两个版本线，保持功能迭代的同时，确保 LTS 版本能够得到较新的 bugfix。</p> 
<p style="margin-left:0; margin-right:0">值得一提的是，Apache APISIX 2.10.0 的 docker 镜像将会内置 APISIX OpenResty，无需自行编译就能用到 Apache APISIX 的全部功能。</p> 
<h2 style="margin-left:0px; margin-right:0px">新功能：<strong>service 增加<span> </span><span style="color:#ff3c37">hosts 属性</span></strong></h2> 
<p style="margin-left:0; margin-right:0"><span>在 Apache APISIX 2.10.0 版本里面，我们给 </span><code>service</code><span> 加上了 </span><code>hosts</code><span> 属性。</span><span>就像<span> </span><span style="background-color:#f0f0f0; color:#000000">service</span><span> </span>里面其他字段一样，<span style="background-color:#f0f0f0; color:#000000">route</span><span> </span>可以从<span> </span><span style="background-color:#f0f0f0; color:#000000">service</span><span> </span>中继承<span> </span><span style="background-color:#f0f0f0; color:#000000">hos</span><span style="background-color:#f0f0f0; color:#000000">ts</span><span> </span>属性。</span></p> 
<p style="margin-left:0; margin-right:0">下面的配置：</p> 
<pre style="margin-left:0; margin-right:0"><code><em># services/1</em>
&#123;
    <span style="color:#98c379">"hosts"</span>: [<span style="color:#98c379">"bar.com"</span>]
&#125;
<em># routes/1</em>
&#123;
    <span style="color:#98c379">"upstream"</span>: &#123;
        <span style="color:#98c379">"nodes"</span>: &#123;
            <span style="color:#98c379">"127.0.0.1:1980"</span>: 1
        &#125;,
        <span style="color:#98c379">"type"</span>: <span style="color:#98c379">"roundrobin"</span>
    &#125;,
    <span style="color:#98c379">"service_id"</span>: <span style="color:#98c379">"1"</span>,
    <span style="color:#98c379">"uri"</span>: <span style="color:#98c379">"/hello"</span>
&#125;</code></pre> 
<p style="margin-left:0; margin-right:0">相当于：</p> 
<pre style="margin-left:0; margin-right:0"><code><em># routes/1</em>
&#123;
    <span style="color:#98c379">"upstream"</span>: &#123;
        <span style="color:#98c379">"nodes"</span>: &#123;
            <span style="color:#98c379">"127.0.0.1:1980"</span>: 1
        &#125;,
        <span style="color:#98c379">"type"</span>: <span style="color:#98c379">"roundrobin"</span>
    &#125;,
    <span style="color:#98c379">"hosts"</span>: [<span style="color:#98c379">"bar.com"</span>],
    <span style="color:#98c379">"uri"</span>: <span style="color:#98c379">"/hello"</span>
&#125;</code></pre> 
<p style="margin-left:0; margin-right:0"><span>这么修改之后，Apache APISIX 里面的<span> </span></span><span style="color:#000000"><span style="background-color:#f0f0f0">route</span></span><span> 和<span> </span><span style="background-color:#f0f0f0; color:#000000">service</span><span> </span>的关系与 Nginx 里面的<span> </span></span><span style="color:#000000"><span style="background-color:#f0f0f0">location</span></span><span> 和<span> </span><span style="background-color:#f0f0f0; color:#000000">server</span><span> </span>的关系越来越相似。</span><span>可以这么说，本次修改让 service 从鸡肋变成了鸡腿，把 service 又拉回了 Apache APISIX 配置核心三角：</span><span>route、upstream、service 之中。</span></p> 
<h2 style="margin-left:0px; margin-right:0px">新功能：<strong>支持设置</strong><span style="color:#ff0000"><strong>镜像请求</strong></span><strong>的比例</strong></h2> 
<p style="margin-left:0; margin-right:0">proxy-mirror 插件支持设置镜像请求的比例，是用户们一直在期待的功能，我们在 Apache APISIX  2.10.0 上支持了这个功能。</p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>通过设置<span> </span></span><span style="color:#000000"><span style="background-color:#f0f0f0">sample_ratio</span></span><span>，可以控制被镜像到测试服务的请求数量。</span><span>比如，下述的配置将 <span style="background-color:#f0f0f0; color:#000000">sample_ratio</span><span> </span>设置为 0.5，会将一半的请求镜像到测试服务上：</span></p> 
<pre style="margin-left:0; margin-right:0"><code>&#123;
    <span style="color:#98c379">"plugins"</span>: &#123;
        <span style="color:#98c379">"proxy-mirror"</span>: &#123;
            <span style="color:#98c379">"host"</span>: <span style="color:#98c379">"http://127.0.0.1:1986"</span>,
            <span style="color:#98c379">"sample_ratio"</span>: 0.5
        &#125;
    &#125;,
    <span style="color:#98c379">"upstream"</span>: &#123;
        <span style="color:#98c379">"nodes"</span>: &#123;
            <span style="color:#98c379">"127.0.0.1:1980"</span>: 1
        &#125;,
        <span style="color:#98c379">"type"</span>: <span style="color:#98c379">"roundrobin"</span>
    &#125;,
    <span style="color:#98c379">"uri"</span>: <span style="color:#98c379">"/hello"</span>
&#125;</code></pre> 
<h2 style="margin-left:0px; margin-right:0px">新组件：<strong>APISIX </strong><span style="color:#ff0000"><strong>Python</strong></span><strong><span> </span>Plugin Runner</strong></h2> 
<p style="margin-left:0; margin-right:0">继<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI1MDU3NjQ5OA%3D%3D%26mid%3D2247485840%26idx%3D1%26sn%3D64f6ce58831d210646a38ae215dea330%26chksm%3De981628ddef6eb9b52b292ba9294498a6ab0f7b88c296259f24a7e5cae45099e3eb9a3d52900%26scene%3D21%23wechat_redirect" target="_blank">Java Plugin Runner</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI1MDU3NjQ5OA%3D%3D%26mid%3D2247486454%26idx%3D1%26sn%3D905ab375e0f33a173ba90a0f541995b7%26chksm%3De98160ebdef6e9fd58079446c1543c7d6f8fabac966acb4e4165d80bf42f6c64a8183583ff1a%26scene%3D21%23wechat_redirect" target="_blank">Go Plugin Runner</a><span> </span>之后，Apache APISIX 又迎来了新的 Plugin Runner。</p> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI1MDU3NjQ5OA%3D%3D%26mid%3D2247488107%26idx%3D1%26sn%3Dc04b2c48aeec344f9c0e56fe897bae68%26chksm%3De9817976def6f060309d96e722bb2743be64962464e0f8e0d6516c20fbd2da32978759439cc9%26scene%3D21%23wechat_redirect" target="_blank">Apache APISIX Python Plugin Runner</a><span> </span>已于 9 月 6 日发布了 0.1.0 版本。</p> 
<p style="margin-left:0; margin-right:0">Python 是一门有着深厚群众基础的编程语言，一直以容易上手和灵活多变而著称。如今你我也能用这门语言，给 Apache APISIX 编写插件了。</p> 
<p style="margin-left:0; margin-right:0">除了 Python Plugin Runner 之外，社区的伙伴也在开发其他编程语言的 Plugin Runner，比如 JavaScript Plugin Runner，欢迎大家参与开发。</p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>下载</strong></h2> 
<p style="margin-left:0; margin-right:0">除了上述新功能和组件外，Apache APISIX 2.10.0 版本还引入了十余个新功能和插件，详情请查看本次发布对应的 Change log。</p> 
<p style="margin-left:0; margin-right:0"><strong>下载 Apache APISIX 2.10.0</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>源代码：</strong>请访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fdownloads%2F" target="_blank">https://apisix.apache.org/downloads/</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>二进制安装包：</strong>请访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fzh%2Fdocs%2Fapisix%2Fhow-to-build%2F" target="_blank">https://apisix.apache.org/zh/docs/apisix/how-to-build/</a></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><strong>关于 Apache APISIX</strong></h2> 
<p style="margin-left:0; margin-right:0">Apache APISIX 是一个动态、实时、高性能的开源 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。Apache APISIX 可以帮忙企业快速、安全的处理 API 和微服务流量，包括网关、Kubernetes Ingress 和服务网格等。</p>
                                        </div>
                                      
</div>
            