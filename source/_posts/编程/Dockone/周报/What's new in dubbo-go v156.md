
---
title: "What's new in dubbo-go v1.5.6"
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3501'
author: Dockone
comments: false
date: 2021-04-28 00:26:32
thumbnail: 'https://picsum.photos/400/300?random=3501'
---

<div>   
<br>作者 | 铁城  dubbo-go 社区 committer<br>
来源 | <a href="https://mp.weixin.qq.com/s/c9psMl6BOLMNGeSd9BDzjw">阿里巴巴云原生公众号</a><br>
<br>dubbogo 社区近期发布了 dubbogo v1.5.6。该版本和 dubbo 2.7.8 对齐，提供了命令行工具，并提供了多种加载配置的方式。<br>
<br>相关改进实在太多，本文只列出相关重大 feature 和 性能提升项。<br>
<br><h2>1. 命令行工具</h2>熟悉dubbo 的朋友可能知道 dubbo 支持 telnet 命令行在线调试。<br>
<br>本次发布也增加了 dubbo-go 的 cli 命令行工具，可以方便用户直连特定服务，通过编写 json 文件来定义传输结构和数据，发起调用进行在线调试，打印返回数据和耗时情况。<br>
<br>目前支持嵌套 struct，但是只支持单个参数的请求包和回包。数据类型由于需要在 json 中定义，只支持 golang 基本数据类型：字符串、整形、浮点。<br>
<br>社区后续会再发一篇文章，着重讲解其原理和实现。相关 pr 为 <a href="https://github.com/apache/dubbo-go/pull/818"></a><a href="https://github.com/apache/dubbo-go/pull/818" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/818</a>，由 dubbogo 最年轻的 00 后 apache committer 李志信同学实现。<br>
<br><h2>2. 代理实现扩展</h2>重构 Proxy，添加 ImplementFunc 函数，允许项目对 Proxy 的代理进行重新实现。在使用 ProxyFactory 自定义注册的场景下，创建的 proxy.Proxy 也自定义实现，可以对返回数据进行修改。<br>
<br>主要应用场景为在网关泛化调用场景下。懂得的人自然懂。<br>
<br>相关 pr  <a href="https://github.com/apache/dubbo-go/pull/1019"></a><a href="https://github.com/apache/dubbo-go/pull/1019" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/1019</a>，由本文作者亲自操刀。<br>
<br><h2>3. 启动时指定配置文件的路径</h2>用户使用之前版本的 dubbogo 时，一直吐槽其只提供环境变量的方式，加载指定的配置文件。<br>
<br><code class="prettyprint">export CONF_PROVIDER_FILE_PATH=&quot;../profiles/dev/server.yml&quot;<br>
export CONF_CONSUMER_FILE_PATH=&quot;../profiles/dev/server.yml&quot;<br>
export APP_LOG_CONF_FILE=&quot;../profiles/dev/log.yml&quot;</code><br>
<br>v1.5.6 提供了新的配置文件加载接口：在启动命令行通过  proConf、conConf、logConf三个 flag 设定配置文件路径。<br>
<br>服务提供方：<br>
<br><code class="prettyprint">go run . -proConf ../profiles/dev/server.yml -logConf ../profiles/dev/log.yml</code><br>
<br>服务消费方：<br>
<br><code class="prettyprint">go run . -conConf ../profiles/dev/client.yml -logConf ../profiles/dev/log.yml</code><br>
<br>相关 pr <a href="https://github.com/apache/dubbo-go/pull/1039"></a><a href="https://github.com/apache/dubbo-go/pull/1039" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/1039</a>，由南京信息工程大学大三学生 陈家鹏实现。<br>
<br><h2>4. 自定义加载 ServerConfig 和 ReferenceConfig</h2>新增 ConfigPostProcessor 接口，用户可以依据该接口提供两个的方法，在部署 dubbogo 服务时加载自定义的配置。<br>
<br>```<br>
// 服务提供方配置<br>
PostProcessServiceConfig(*common.URL)<br>
<br>// 服务消费方配置<br>
PostProcessReferenceConfig(*common.URL)<br>
```<br>
<br>相关 pr  <a href="https://github.com/apache/dubbo-go/pull/943"></a><a href="https://github.com/apache/dubbo-go/pull/943" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/943</a>，由即将奔五十的 dubbo chairman 北纬亲自操刀实现，chairman 同志老当益壮，号召大家向 chairman 筒子学习。<br>
<br><h2>5. 扩展 URL 的比较</h2>在common/url.go里面提供 CompareURLEqualFunc，可以让用户自定义 URL 比较，提高比对效率。相关技术细节见如下链接。<br>
<br><blockquote><br>common/url.go：<br>
  <a href="https://github.com/apache/dubbo-go/pull/854/files#diff-5111f14762c010c3029a67743796fea97ab1015d35c96670a4cfa25f30145464">_</a><a href="https://github.com/apache/dubbo-go/pull/854/files#diff-5111f14762c010c3029a67743796fea97ab1015d35c96670a4cfa25f30145464_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... 5464_</a></blockquote>目前的 URL 实现并未达到最终状态。未来的 dubbogo 3.x 版本中，将借鉴 dubbo 的 URL 实现，将 common.URL 拆分为ServiceConfigURL、ServiceAddressURL和InstanceAddressURL，分别对应配置中心、注册中心和元数据中心的 schema，尽量将变更压力降低到最低粒度。<br>
<br>该功能对应的 pr  <a href="https://github.com/apache/dubbo-go/pull/854" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/854</a> 由阿里双十一中间件大队长展图同学实现。展图同学一直奋战在编程一线。<br>
<br><h2>6. 注册中心优化</h2>复用了 zookeeper 链接以及优化了服务发现中心逻辑，大大减少了与 zookeeper 的 tcp 链接数目，减少了使用的 goroutine 数目，降低了 dubbo-go 的内存占用量。<br>
<br>我们会把同样的逻辑服用到 nacos、etcd、consul 等各个注册中心，通过减少 goroutine 数目，减轻注册中心压力，并减少 consumer 和 provider 内存的使用。<br>
<br>该功能对应的 pr <a href="https://github.com/apache/dubbo-go/pull/1010" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/1010</a> 由现在蚂蚁中间件工作的 王文学 同学在涂鸦工作时实现。<br>
<br><h2>7. API 形式进行配置</h2>以前版本的 dubbogo 只提供了从配置文件读取配置选项，该功能增加以 API 的方式进行配置，用户可以通过调用相关 API 初始化配置。<br>
<br>用户可以通过 API 进行相关参数设定，无需再加载配置文件。<br>
<br>可以参考示例： <a href="https://github.com/apache/dubbo-go-samples/tree/master/config-api">_</a><a href="https://github.com/apache/dubbo-go-samples/tree/master/config-api_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... -api_</a><br>
<br>相关 pr <a href="https://github.com/apache/dubbo-go/pull/1020" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/1020</a> 也是由李志信实现。<br>
<br><h2>8. grpc 优化</h2><ul><li>打通 dubbo-go中 consumer config 的超时时间 connect_timeout 和 gRPC server 的超时时间，用户可以自定义 gRPC 超时时间机制。</li></ul><br>
<br>```<br>
<h1>connect timeout</h1>connect_timeout: "3s"<br>
<br><h1>application config</h1>application:<br>
  organization: "dubbo.io"<br>
  name: "GreeterGrpcConsumer"<br>
  module: "dubbo-go greeter grpc client"<br>
  version: "0.0.1"<br>
  environment: "dev"<br>
```<br>
<ul><li><br>将处理注册中心服务变更事件的机制改为同步，防止 provider 端服务频繁重启导致上下线事件处理顺序出错。</li><li><br>使用 gRPC 协议时，异步等待 dubbo-go 的 service 都暴露完后，才将所有 dubbo-go service 对应的 gRPC service 注册到 gRPC server 上并启动 gRPC server。以此修复 provider 端的只能注册一个 service 的问题。</li></ul><br>
<br>总体功能由 <a href="https://github.com/apache/dubbo-go/pull/1056" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go/pull/1056</a> 等多个 pr 构成，由 All In 了 dubbogo 的 上海识装信息科技有限公司【知名 APP 得物所在公司】工程师 柯瞻、 dubbogo 社区负责人 于雨、阿里工程师云兴 以及 南京某公司的张天同学 共同负责实现。<br>
<br><h2>9. hessian2 go 最新 feature</h2>除了  dubbo-go 自身的改进外，dubbo-go-hessian2 项目截止目前最新版本 v1.9.2 也做了如下重大改进：<br>
<ul><li>内置支持 java.util.Locale：<a href="https://github.com/apache/dubbo-go-hessian2/pull/264">_</a><a href="https://github.com/apache/dubbo-go-hessian2/pull/264_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... /264_</a></li><li>内置支持 java.util.UUID：<a href="https://github.com/apache/dubbo-go-hessian2/pull/256">_</a><a href="https://github.com/apache/dubbo-go-hessian2/pull/256_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... /256_</a></li><li>支持编码 no pojo object：<a href="https://github.com/apache/dubbo-go-hessian2/pull/243">_</a><a href="https://github.com/apache/dubbo-go-hessian2/pull/243_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... /243_</a></li><li>内置支持 java.sql.Time：<a href="https://github.com/apache/dubbo-go-hessian2/pull/219">_</a><a href="https://github.com/apache/dubbo-go-hessian2/pull/219_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... /219_</a></li><li>内置支持 java.sql.Date：<a href="https://github.com/apache/dubbo-go-hessian2/pull/221">_</a><a href="https://github.com/apache/dubbo-go-hessian2/pull/221_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... /221_</a></li></ul><br>
<br>dubbo-go-hessian2：<a href="https://github.com/apache/dubbo-go-hessian2">_</a><a href="https://github.com/apache/dubbo-go-hessian2_" rel="nofollow" target="_blank">https://github.com/apache/dubbo-go-hessian2_</a><br>
<br>总体 pr 由 dubbo-go-hessian2 项目负责人 望哥、李志信、张艳明等同学完成。<br>
<br><h2>10. 回顾与展望</h2>dubbogo 目前处于一个比较稳定成熟的状态，1.5 版本会被持续维护，以修复 BUG 和进行一些必要的最低幅度的优化。<br>
<br>更多信息：<a href="https://github.com/apache/dubbo-go/releases/tag/v1.5.6">_</a><a href="https://github.com/apache/dubbo-go/releases/tag/v1.5.6_" rel="nofollow" target="_blank">https://github.com/apache/dubb ... .5.6_</a><br>
<br>目前最新的朝云原生方向的发展3.0 版本基于 v1.5.x，在兼容 dubbo 3.0 的同时，将向后兼容 v2.7.x，计划于 4 月底发布第一个版本。<br>
<br><h3><strong>作者简介</strong></h3><strong>铁城 (Github ID cityiron)</strong>，dubbo-go 社区 committer，主要参与 dubbo-go 1.5 版本迭代、 dubbo-go 3.0 服务路由和云原生方面工作、以及 dubbo-go-pixiu 项目负责人。目前就职于阿里盒马事业群，从事交易流程工作，擅长使用 Java/Go 语言，专注于云原生和微服务等技术方向。
                                
                                                              
</div>
            