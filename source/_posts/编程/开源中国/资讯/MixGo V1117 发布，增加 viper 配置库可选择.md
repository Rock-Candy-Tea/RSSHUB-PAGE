
---
title: 'MixGo V1.1.17 发布，增加 viper 配置库可选择'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://openstr.com/cover/aa328ff33de085aa8fc87301056f3407.jpg?size=small&share=true'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 14:21:00 GMT
thumbnail: 'https://openstr.com/cover/aa328ff33de085aa8fc87301056f3407.jpg?size=small&share=true'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">MixGo 是一个 Go 快速开发标准工具包；内部模块高度解耦，整体代码基于多个独立的模块构建，即便用户不使用我们的 mixcli 脚手架快速生成代码，也可以使用这些独立模块。例如：你可以只使用 xcli 来构建你的命令行交互；可以使用 xdi 来管理全局对象的依赖；可以使用 xwp 来处理 MQ 队列消费；所有的模块你可以像搭积木一样随意组合。</p> 
<h1 style="text-align:left">请帮忙 Star 一下</h1> 
<ul> 
 <li style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fmix" target="_blank">https://github.com/mix-go/mix</a></li> 
 <li style="text-align:left"><a href="https://gitee.com/mix-go/mix">https://gitee.com/mix-go/mix</a></li> 
</ul> 
<h2 style="text-align:left">独立模块</h2> 
<p style="text-align:left">核心模块全部可独立使用。</p> 
<ul> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/mixcli">mix-go/mixcli</a> 快速创建 Go 项目的脚手架，类似前端界的 Vue CLI</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/xcli">mix-go/xcli</a> 命令行交互与指挥管理工具，同时它还包括命令行参数获取、中间件、程序守护等。</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/xdi">mix-go/xdi</a> 处理对象依赖关系的 IoC、DI 库，可以实现统一管理依赖，全局对象管理，动态配置刷新等。</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/xwp">mix-go/xwp</a> 一个通用工作池、协程池，可动态扩容缩容。</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/xfmt">mix-go/xfmt</a> 可以打印结构体嵌套指针地址内部数据的格式化库</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/varwatch">mix-go/varwatch</a> 监视配置结构体变量的数据变化并执行一些任务</li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/src/dotenv">mix-go/dotenv</a> 具有类型转换功能的 DotEnv 环境配置库</li> 
</ul> 
<h2 style="text-align:left">快速开始</h2> 
<p style="text-align:left">提供了现成的脚手架工具，快速创建项目，立即产出。</p> 
<ul> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/cli-skeleton#readme">编写一个 CLI 程序</a> 
  <ul> 
   <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/cli-skeleton#%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA-worker-pool-%E9%98%9F%E5%88%97%E6%B6%88%E8%B4%B9">编写一个 Worker Pool 队列消费</a></li> 
  </ul> </li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/api-skeleton#readme">编写一个 API 服务</a></li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/web-skeleton#readme">编写一个 Web 服务</a> 
  <ul> 
   <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/web-skeleton#%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA-WebSocket-%E6%9C%8D%E5%8A%A1">编写一个 WebSocket 服务</a></li> 
  </ul> </li> 
 <li><a href="https://gitee.com/mix-go/mix/blob/master/examples/grpc-skeleton#readme">编写一个 gRPC 服务、客户端</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>go get github.com/mix-go/mixcli</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
  ▸ CLI
    API
    Web (contains the websocket)
    gRPC</pre> 
 </div> 
</div> 
<p style="text-align:left">如果编译时报错，整理一下依赖</p> 
<div style="text-align:left"> 
 <div> 
  <pre>go mod tidy</pre> 
 </div> 
</div> 
<h2 style="text-align:left">推荐阅读</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F391857663" target="_blank">MixGo 在 IDE Goland 中的如何使用</a></li> 
</ul> 
<h2 style="text-align:left">视频教程</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenstr.com%2Fwatch%2Faa328ff33de085aa8fc87301056f3407" target="_blank"><img alt="使用 MixGo 快速开发 API 项目" src="https://openstr.com/cover/aa328ff33de085aa8fc87301056f3407.jpg?size=small&share=true" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenstr.com%2Fwatch%2F41e9dc609cb8f9a4530fe8f7a37f1130" target="_blank"><img alt="从 PHP 转 Go 的基础知识对比视频讲解" src="https://openstr.com/cover/41e9dc609cb8f9a4530fe8f7a37f1130.jpg?size=small&share=true" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:left">技术交流</h2> 
<p style="text-align:left">知乎：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fonanying" target="_blank">https://www.zhihu.com/people/onanying</a><br> 官方QQ群：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshang.qq.com%2Fwpa%2Fqunwpa%3Fidkey%3Db3a8618d3977cda4fed2363a666b081a31d89e3d31ab164497f53b72cf49968a" target="_blank">284806582</a>, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshang.qq.com%2Fwpa%2Fqunwpa%3Fidkey%3Dd2908b0c7095fc7ec63a2391fa4b39a8c5cb16952f6cfc3f2ce4c9726edeaf20" target="_blank">825122875</a> 敲门暗号：gopher</p> 
<h2 style="text-align:left">PHP 框架</h2> 
<p style="text-align:left">OpenMix 同时还有 PHP 生态的框架</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fmix" target="_blank">https://github.com/mix-php/mix</a></li> 
 <li><a href="https://gitee.com/mix-php/mix">https://gitee.com/mix-php/mix</a></li> 
</ul> 
<h2 style="text-align:left">License</h2> 
<p style="text-align:left">Apache License Version 2.0, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank">http://www.apache.org/licenses/</a></p>
                                        </div>
                                      
</div>
            