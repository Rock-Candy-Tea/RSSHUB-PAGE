
---
title: 'GoEdge v0.2.9 已经发布，快速构建 CDN & WAF 平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3053'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 10:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3053'
---

<div>   
<div class="content">
                                                                                            <p>GoEdge v0.2.9 已经发布，快速构建 CDN & WAF 平台</p> 
<p>此版本更新内容包括：</p> 
<p>此版本主要改进细节、修复Bug。</p> 
<blockquote> 
 <p>注意：这个版本可能会重新记录一些统计数据。</p> 
</blockquote> 
<h3>EdgeAdmin</h3> 
<ul> 
 <li>优化节点创建和安装流程</li> 
 <li>修复节点无法修改线路的Bug</li> 
 <li>优化代码/支持IP名单的更多格式的导入、导出</li> 
 <li>访问日志搜索增加域名和IP搜索</li> 
 <li>访问日志显示节点信息</li> 
 <li>增加全局服务访问日志</li> 
 <li>安全设置中增加允许记住登录选项</li> 
 <li>安全设置检查IP时同时也检查直接连接管理平台的上游IP</li> 
 <li>修复在MySQL8下安装提示无法创建edgeTest的问题</li> 
 <li>提升节点配置同步速度（从60秒提升到10秒以内）</li> 
</ul> 
<h3>EdgeAPI</h3> 
<ul> 
 <li>修复多个表unique key无法升级到问题</li> 
 <li>修复WAF检查IP状态可能会出现panic错误的Bug</li> 
 <li>边缘节点没有集群的时候视为删除</li> 
 <li>运行日志只显示已经设置集群的节点</li> 
</ul> 
<h3>EdgeDNS</h3> 
<blockquote> 
 <p>此功能为企业版专有。</p> 
</blockquote> 
<ul> 
 <li>DNS节点增加在线状态通知</li> 
 <li>支持内置线路</li> 
 <li>增加解析测试</li> 
 <li>实现DNS节点远程安装</li> 
 <li>DNS节点可以修改SSH登录相关信息</li> 
 <li>可以远程停止和启动DNS节点</li> 
</ul> 
<p>下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a> 文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p> 
<p>详情查看：<a href="https://gitee.com/liuxiangchao/EdgeAdmin/releases/v0.2.9">https://gitee.com/liuxiangchao/EdgeAdmin/releases/v0.2.9</a></p>
                                        </div>
                                      
</div>
            