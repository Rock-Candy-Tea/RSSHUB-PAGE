
---
title: 'Prometheus 2.35 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4158'
author: 开源中国
comments: false
date: Sat, 16 Apr 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4158'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Prometheus 是 CNCF（云原生计算基金会）项目，是一个系统和服务监控系统。它以给定的时间间隔从配置的目标收集指标，评估规则表达式，显示结果，并在观察到指定条件时触发警报。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Prometheus 2.35 RC 更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[ENHANCEMENT] 更新软件包<span> </span><code>uber.go/auomaxprocs</code><span> </span>以支持<span> </span><code>cgroups2</code></li> 
 <li>[BUGFIX] 只在不安全状态为 false 时设置 TLS 凭证</li> 
 <li>[BUGFIX] 修复加载具有多个段的 WAL 时的 ID 冲突</li> 
 <li>[BUGFIX] 撤销在上下文中存储目标和元数据缓存。这可以修复<code>2.35.0-rc0</code>中引入的内存泄漏</li> 
 <li>[CHANGE] TSDB: 当 Prometheus 启动时删除 *.tmp WAL 文件</li> 
 <li>[CHANGE] promtool: 为命令<span> </span><code>check rules</code><span> </span>和<span> </span><code>check config</code><span> </span>增加新的标志<span> </span><code>-lint</code>（默认启用），导致 linter 错误的新退出代码（<code>3</code>）</li> 
 <li>[FEATURE] 支持自动将变量<code>GOMAXPROCS</code>设置为容器的 CPU 限制。用标志<span> </span><code>enable-feature=auto-gomaxprocs</code><span> </span>启用</li> 
 <li>[FEATURE] PromQL：用查询中的总样本数和峰值数扩展统计</li> 
 <li>[ENHANCEMENT] Prometheus 用 Go 1.18 构建</li> 
 <li>[BUGFIX] 修复 OpenMetrics 解析器，以正确排序大写的标签</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fprometheus%2Fprometheus" target="_blank">https://github.com/prometheus/prometheus</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            