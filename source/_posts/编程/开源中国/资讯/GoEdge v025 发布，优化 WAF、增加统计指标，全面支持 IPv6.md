
---
title: 'GoEdge v0.2.5 发布，优化 WAF、增加统计指标，全面支持 IPv6'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-868dc93cc764a6e5db81c8bc9008b13b78d.png'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 08:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-868dc93cc764a6e5db81c8bc9008b13b78d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-868dc93cc764a6e5db81c8bc9008b13b78d.png" width="600" referrerpolicy="no-referrer"></p> 
<p><br> <strong>GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以快速构建 CDN & WAF 平台的工具。</span></p> 
<p style="text-align:start">此版本主要优化WAF、增加统计指标，以及对IPv6全面支持。</p> 
<h3 style="text-align:start">编译方式变更</h3> 
<p style="text-align:start">社区版编译增加 <code>community</code> 标签，先前运行和编译的命令为：</p> 
<div style="text-align:start"> 
 <pre>go build xxx.go
go run xxx.go</pre> 
</div> 
<p style="text-align:start">改成：</p> 
<div style="text-align:start"> 
 <pre>go build -tags community xxx.go
go run -tags community xxx.go</pre> 
</div> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>[WAF]<strong>增加和优化多个WAF动作</strong></li> 
 <li>[WAF]<strong>实现新的CC规则，可以组合多个对象</strong></li> 
 <li>[WAF]在IP名单里测试是否包含IP时，同时也检查绑定的IP名单</li> 
 <li>[WAF]IP名单中可以通过IP查找访问日志</li> 
 <li><strong>实现自定义统计指标，用来统计数据项目和绘制图表，并增加一组公用的统计指标</strong></li> 
 <li>Dashboard增加统计指标图表</li> 
 <li>节点列表增加流量信息</li> 
 <li>节点列表可以按照CPU、内存、流量信息排序</li> 
 <li><strong>在几乎所有填写网络地址的地方支持IPv6</strong></li> 
 <li>SSH认证：公钥认证方式增加用户名选项</li> 
 <li>修复搜索关键词可能带来的安全问题</li> 
 <li>管理界面可以切换风格</li> 
 <li>访问日志增加更容易可视化的时间显示</li> 
 <li>路径规则文字改成路由规则</li> 
 <li>安装时不检查API地址是否可以绑定</li> 
 <li>创建网站服务后自动开启Websocket和访问日志</li> 
 <li>增加恢复模式，用来修正因API地址错误而无法登录的情形</li> 
 <li>自动替换API节点时增加对新节点的测试</li> 
 <li>优化使用IP查找访问日志的速度</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>设置 <code>max_prepared_stmt_count</code> 失败时提示更详细</li> 
 <li>增加多个统计数据自动清理任务</li> 
 <li>其他配合EdgeAdmin做的变更</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>缓存写入后增加Content-Length对比校验</li> 
 <li>其他配合EdgeAdmin做的变更</li> 
</ul> 
<p>Demo演示：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.goedge.cn" target="_blank">http://demo.goedge.cn</a><br> 下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> 文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            