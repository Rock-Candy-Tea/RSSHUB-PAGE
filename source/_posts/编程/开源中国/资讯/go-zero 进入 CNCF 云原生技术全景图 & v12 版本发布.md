
---
title: 'go-zero 进入 CNCF 云原生技术全景图 & v1.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4786a83eb5dbf1ddeb34fbded485c63c681.png'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 09:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4786a83eb5dbf1ddeb34fbded485c63c681.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">go-zero 1.2 发布了。go-zero 是一个集成了各种工程实践的 web 和 rpc 框架。通过弹性设计保障了大并发服务端的稳定性，经受了充分的实战检验。go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 API 文件一键生成 Go, iOS, Android, Kotlin, Dart, TypeScript 代码，并可直接运行。</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新内容包括：</p> 
  </div> 
  <p style="color:#24292f; text-align:start">框架：</p> 
  <ol> 
   <li>支持 k8s 服务发现，使用<code>k8s://namespace/service:port</code><span> </span>作为 RPC<span> </span><code>Target</code><span> 配置值即可</span>。更多服务发现方式可以通过插件方式支持，比如 consul, nacos 等。</li> 
   <li><span>logx content 字段支持 json 内容，</span><code>logx.Infov/Errorv/Slowv</code>.</li> 
   <li><span>logx 可以禁用统计日志，</span><code>logx.DisableStat()</code>.</li> 
   <li>更多改进和 bug 修复。</li> 
  </ol> 
  <p style="color:#24292f; text-align:start">goctl:</p> 
  <ol> 
   <li>优化了 goctl mongodb 在不带 cache 情况下的代码生成</li> 
   <li>优化了 gRPC 代码生成</li> 
   <li>优化了 model 生成时的命名</li> 
   <li>goctl 打印 error 时带上了版本和详细信息</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Fissues%2F915" target="_blank">#915</a><span> 解决了 gRPC 内联类型的代码生成</span></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Fissues%2F925" target="_blank">#925</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Fissues%2F929" target="_blank">#929</a><span> 优化了 mysql 的 NULL 数据类型转换</span></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Fissues%2F968" target="_blank">#968</a><span> 解决软连接代码生成问题</span></li> 
  </ol> 
 </div> 
</div> 
<div>
  
</div> 
<div> 
 <div>
  <span style="background-color:#ffffff; color:#333333">更新详情查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Freleases" target="_blank">https://github.com/tal-tech/go-zero/releases</a></span>
 </div> 
</div> 
<div>
 <img height="1863" src="https://oscimg.oschina.net/oscnet/up-4786a83eb5dbf1ddeb34fbded485c63c681.png" width="1242" referrerpolicy="no-referrer">
</div>
                                        </div>
                                      
</div>
            