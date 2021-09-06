
---
title: 'CDN 工具 GoEdge v0.3.0 发布，大幅提升交互体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8dc5dce8696be035814f2dfa061f2832f96.png'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 09:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8dc5dce8696be035814f2dfa061f2832f96.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。<br> <br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-8dc5dce8696be035814f2dfa061f2832f96.png" width="600" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#24292f">v0.3.0主要优化交互体验，减少交互环节。</span></p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>节点IP增加是否启用、是否在线状态设置</li> 
 <li>IP名单批量导入IP支持CIDR</li> 
 <li>添加DNS账号时自动读取DNS服务商下域名</li> 
 <li>Dashboard可以提示API节点升级提示</li> 
 <li>全局访问日志增加WAF日志</li> 
 <li>创建集群时自动创建缓存策略和WAF策略/优化界面</li> 
 <li>新安装检查数据库权限后删除测试表</li> 
 <li>选择DNS线路时增加搜索</li> 
 <li>节点如果没有设置DNS线路就使用默认线路，不再强制要求选择线路</li> 
 <li>DNS服务商支持搜索</li> 
 <li>添加IP到IP名单时，可以选择批量输入</li> 
 <li>缓存设置中增加清理和预热功能</li> 
 <li>缓存策略里的默认缓存条件增加、修改或者删除后自动保存</li> 
 <li>可以在节点列表中直接修改节点所属线路</li> 
 <li>健康检查连续下线次数默认值从1次改为3次</li> 
 <li>优化数据库节点管理</li> 
 <li>BUG：修改accessKeys package因为大小写而无法编译的问题</li> 
 <li>BUG: 修复缓存条件状态码无法修改的问题</li> 
 <li>优化多处交互</li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>看板中节点排行增加条数限制</li> 
 <li>优化WAF日志查询速度</li> 
 <li>优化服务配置更新机制</li> 
 <li>修复健康检查可能导致DNS不断同步的问题</li> 
 <li>健康检查失败10分钟内不重复提醒</li> 
 <li>提升指标统计查询速度</li> 
 <li>BUG: 修复节点转移集群后没有删除老的DNS记录的问题</li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>提升缓存文件读取速度5%~20%</li> 
 <li>优化指标统计写入数据逻辑</li> 
 <li>调整ACME证书申请链接的优先级为最高，避免因URL跳转而导致无法申请证书</li> 
 <li>请求源站错误时增加503、504错误</li> 
 <li>BUG: 缓存预热时不重复写入</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292e">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292e">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            