
---
title: 'go-zero 1.2.5 发布，web 和 rpc 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=937'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 09:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=937'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">go-zero 1.1.4 发布了。go-zero 是一个集成了各种工程实践的 web 和 rpc 框架。通过弹性设计保障了大并发服务端的稳定性，经受了充分的实战检验。go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 API 文件一键生成 Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript 代码，并可直接运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新内容包括：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>框架：</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>修复 gRPC 负载均衡在32位cpu可能崩溃的问题</li> 
 <li>修复 logx.WithContext 和 logx.WithDuration 并发问题</li> 
 <li>添加 redis.Decr, redis.Decrby, redis.Lindex 方法</li> 
 <li>支持 sqlc, mongoc 自定义 cache</li> 
 <li>客户端关闭的请求返回 HTTP 状态码499</li> 
 <li>MapReduce 支持传入 context</li> 
 <li>Unmarshal 的 default, options 标签支持数组</li> 
 <li>httpx.SetErrorHandler 支持 http timeout</li> 
 <li>添加 fx.NoneMatch, fx.First, fx.Last</li> 
 <li>ETCD 支持 TLS</li> 
</ol> 
<p><strong>goctl</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>修复 goctl upgrade windows 问题</li> 
 <li>修复 goctl 生成时路径使用根路径 / 的问题</li> 
 <li>支持 PostgreSQL 的 bytea 类型</li> 
 <li><span>添加 </span><code>goctl bug</code><span> ，便于更方便的提交bug</span></li> 
 <li>model生成时保持 Go 关键词可用</li> 
 <li>支持 MySQL 的 bit 类型</li> 
 <li>添加 --remote，用来使用远端 git 仓库作为模板</li> 
 <li>修复 --home bug</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新详情查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Freleases%2Ftag%2Fv1.1.4" target="_blank">https://github.com/tal-tech/go-zero/releases/tag/v1.</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftal-tech%2Fgo-zero%2Freleases%2Ftag%2Fv1.2.5" target="_blank">2.5</a></p>
                                        </div>
                                      
</div>
            