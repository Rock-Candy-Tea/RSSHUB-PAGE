
---
title: 'go-zero 1.3.2 发布，web 和 rpc 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4702'
author: 开源中国
comments: false
date: Tue, 05 Apr 2022 20:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4702'
---

<div>   
<div class="content">
                                                                                            <p>go-zero 1.3.2 发布了。go-zero 是一个集成了各种工程实践的 web 和 rpc 框架。通过弹性设计保障了大并发服务端的稳定性，经受了充分的实战检验。go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 API 文件一键生成 Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript 代码，并可直接运行。</p> 
<p>本次更新内容包括：</p> 
<p>框架：<br> 1. 支持 cgroups v2<br> 2. 新增 httpc 包用来治理客户端 HTTP 请求<br> 3. model 支持 ‘-’ 忽略字段<br> 4. 支持 Oracle 的参数选择符 :N<br> 5. 支持 redis 的 GetSet 命令<br> 6. redis SetBit 增加了返回原值<br> 7. RedisLock 取消了可重入机制<br> 8. http 请求返回 Traceparent，符合 OpenTelemetry 规范<br> 9. 小的改进和 bug 修复</p> 
<p>goctl：<br> 1. api 文件支持针对路由组设置单独的 timeout，用 1s, 500ms 这样的方式表示<br> 2. model 生成时区分了 goctl 生成代码和用户扩展代码，便于修改 schema 后再次生成<br> 3. goctl rpc proto 命令移除<br> 4. goctl docker 支持通过 -base 指定基础镜像<br> 5. goctl env install [-f] 一键安装依赖<br> 6. 更多改进和 bug 修复</p> 
<p>更新详情查看：https://github.com/zeromicro/go-zero/releases/tag/v1.3.2</p>
                                        </div>
                                      
</div>
            