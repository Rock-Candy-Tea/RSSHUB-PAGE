
---
title: 'Prometheus 2.38 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3134'
author: 开源中国
comments: false
date: Fri, 19 Aug 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3134'
---

<div>   
<div class="content">
                                                                                            <p>Prometheus 是 CNCF（云原生计算基金会）项目，是一个系统和服务监控系统。它以给定的时间间隔从配置的目标收集指标，评估规则表达式，显示结果，并在观察到指定条件时触发警报。</p> 
<p>Prometheus 2.38 更新内容如下：</p> 
<h3>特性：</h3> 
<ul> 
 <li>Web：添加一个 <code>/api/v1/format_query</code> HTTP API 端点，允许漂亮的格式化 PromQL 表达式。</li> 
 <li>UI：在用户界面中增加对格式化 PromQL 表达式的支持</li> 
 <li>DNS SD：支持发现目标的 MX 记录</li> 
 <li>Templates：增加 <code>toTime()</code> 模板函数，允许将样本时间戳转换为 Go <code>time.Time</code> 值</li> 
</ul> 
<h3>改进：</h3> 
<ul> 
 <li>Kubernetes SD：增加 <code>__meta_kubernetes_service_port_number</code> 元标签，指示服务端口号</li> 
 <li>Kubernetes SD: 增加 <code>__meta_kubernetes_pod_container_image</code> 元标签，表示容器镜像</li> 
 <li>PromQL：当出现 query panics 时，也会将查询本身与 panic 信息一起记录下来</li> 
 <li>UI：调整黑暗主题中的颜色，以提高对比度</li> 
 <li>Web：通过避免锁和使用原子类型来加快对 <code>/api/v1/rules</code> 的调用</li> 
 <li>Scrape：增加 <code>no-default-scrape-port</code> 特性标志，省略或删除目标搜刮地址中的任何默认HTTP(<code>:80</code>)或 HTTPS(<code>:443</code>)端口</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>TSDB：修复在快照加载期间分配系列 ID 的竞赛条件</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fprometheus%2Fprometheus%2Freleases%2Ftag%2Fv2.38.0" target="_blank">https://github.com/prometheus/prometheus/releases/tag/v2.38.0</a></p>
                                        </div>
                                      
</div>
            