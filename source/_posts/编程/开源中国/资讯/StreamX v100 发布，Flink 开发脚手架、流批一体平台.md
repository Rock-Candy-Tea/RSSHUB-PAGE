
---
title: 'StreamX v1.0.0 发布，Flink 开发脚手架、流批一体平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png'
author: 开源中国
comments: false
date: Mon, 24 May 2021 09:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <p style="text-align:center"> </p> 
 <h1 style="text-align:center"><img alt height="155" src="https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png" width="500" referrerpolicy="no-referrer"></h1> 
 <p style="text-align:center"><strong>Make Flink|Spark easier!!!</strong></p> 
</div> 
<p style="text-align:center"><img src="https://img.shields.io/github/stars/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/forks/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/issues/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/downloads/streamxhub/streamx/total" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/languages/count/streamxhub/streamx" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><span style="background-color:#ffffff; color:#333333">大数据技术如今发展的如火如荼,已呈现百花齐放欣欣向荣的景象,实时处理流域 </span><code>Apache Spark</code><span style="background-color:#ffffff; color:#333333"> 和 </span><code>Apache Flink</code><span style="background-color:#ffffff; color:#333333"> 更是一个伟大的进步,尤其是</span><code>Apache Flink</code><span style="background-color:#ffffff; color:#333333">被普遍认为是下一代大数据流计算引擎, 我们在使用 </span><code>Flink</code><span style="background-color:#ffffff; color:#333333"> 时发现从编程模型, 启动配置到运维管理都有很多可以抽象共用的地方, 我们将一些好的经验固化下来并结合业内的最佳实践, 通过不断努力终于诞生了今天的框架 —— </span><code>StreamX</code><span style="background-color:#ffffff; color:#333333">, 项目的初衷是 —— 让 </span><code>Flink</code><span style="background-color:#ffffff; color:#333333"> 开发更简单, 使用</span><code>StreamX</code><span style="background-color:#ffffff; color:#333333">开发,可以极大降低学习成本和开发门槛, 让开发者只用关心最核心的业务,</span><code>StreamX</code><span style="background-color:#ffffff; color:#333333"> 规范了项目的配置,鼓励函数式编程,定义了最佳的编程方式,提供了一系列开箱即用的</span><code>Connectors</code><span style="background-color:#ffffff; color:#333333">,标准化了配置、开发、测试、部署、监控、运维的整个过程, 提供</span><code>scala</code><span style="background-color:#ffffff; color:#333333">和</span><code>java</code><span style="background-color:#ffffff; color:#333333">两套api, 其最终目的是打造一个一站式大数据平台,流批一体的解决方案</span></p> 
<h2 style="text-align:left"><strong>重要特性</strong></h2> 
<ol> 
 <li><strong> 开发脚手架</strong></li> 
 <li><strong>多版本Flink支持(多版本无缝支持1.11.x,1.12.x,1.13.x)</strong></li> 
 <li><strong>一系列开箱即用的connectors</strong></li> 
 <li><strong>支持项目编译功能(maven 编译)</strong></li> 
 <li><strong>在线参数配置</strong></li> 
 <li><strong>支持 `Applicaion` 模式， `Yarn-Per-Job` 模式启动</strong></li> 
 <li><strong>快捷的日常操作(任务`启动`、`停止`、`savepoint`，从`savepoint`恢复)</strong></li> 
 <li><strong>支持火焰图</strong></li> 
 <li><strong>支持 `notebook` (在线任务开发)</strong></li> 
 <li><strong>项目配置和依赖版本化管理</strong></li> 
 <li><strong>在线管理依赖(maven pom)和自定义jar</strong></li> 
 <li><strong>Flink SQL WebIDE</strong></li> 
 <li><strong>支持 Catalog、Hive</strong></li> 
 <li><strong>任务失败告警和重试重</strong></li> 
</ol> 
<p> </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0a291f09cc4abdf87175574936060dd07d5.png" width="1600" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6e3a24d6b1558a6bac2f99f4a15d0c92b09.png" referrerpolicy="no-referrer"></p> 
<h1>软件架构</h1> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b7e90cc994a3e2622b63f12c15bc73c3b5e.png" width="1200" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">项目地址</h2> 
<p>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com" target="_blank">http://www.streamxhub.com</a></p> 
<p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx" target="_blank">streamxhub/streamx: Make Flink|Spark easier!!! (github.com)</a></p> 
<p>Gitee: <a href="https://gitee.com/benjobs/streamx">benjobs/StreamX (gitee.com)</a></p> 
<h1>快速上手</h1> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com%2Fzh%2Fdoc%2Fguide%2Fquickstart%2F" target="_blank">快速上手开发 | StreamX (streamxhub.com)</a></p> 
   <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com%2Fzh%2Fdoc%2Fconsole%2Fquickstart%2F" target="_blank">平台快速使用 | StreamX (streamxhub.com)</a></p> 
   <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx" target="_blank">StreamX</a><span style="background-color:#ffffff; color:#333333"> 遵循 </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">Apache-2.0</a><span style="background-color:#ffffff; color:#333333"> 开源协议,将会是个长期更新的活跃项目,欢迎大家提交 PR</span><span style="background-color:#ffffff; color:#333333"> 或 Issue</span><span style="background-color:#ffffff; color:#333333">。喜欢可以给个 Star</span><span style="background-color:#ffffff; color:#333333">。现</span>已正式发布1.0.0,经历无数汗水,现终于得见天日. 现在她如初生婴儿一般满怀无限憧憬的出现在世人面前,眼下还是一团薪薪之火,期待大家的热情让她烈焰燎原起来.请多多关照,多多支持!</p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            