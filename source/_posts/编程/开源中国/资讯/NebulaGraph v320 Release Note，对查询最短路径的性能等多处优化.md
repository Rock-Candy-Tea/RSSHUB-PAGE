
---
title: 'NebulaGraph v3.2.0 Release Note，对查询最短路径的性能等多处优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://nebula-website-cn.oss-cn-hangzhou.aliyuncs.com/nebula-blog/3.2_%E7%94%BB%E6%9D%BF%201.0%20release%20notes.jpg'
author: 开源中国
comments: false
date: Mon, 01 Aug 2022 16:50:00 GMT
thumbnail: 'https://nebula-website-cn.oss-cn-hangzhou.aliyuncs.com/nebula-blog/3.2_%E7%94%BB%E6%9D%BF%201.0%20release%20notes.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="NebulaGraph v3.2.0 Release Note" src="https://nebula-website-cn.oss-cn-hangzhou.aliyuncs.com/nebula-blog/3.2_%E7%94%BB%E6%9D%BF%201.0%20release%20notes.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">NebulaGraph v3.2.0 支持 extract () 函数，对边、点属性过滤的下推以及查询最短路径的性能等进行了优化，对并发扫描属性时 Storage 服务崩溃等问题进行了修复。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">优化</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.nebula-graph.com.cn%2F3.2.0%2F3.ngql-guide%2F6.functions-and-expressions%2F2.string%2F" target="_blank">extract () 函数</a><span> </span>。</li> 
 <li>优化配置文件，增加部分配置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4310" target="_blank">#4310</a></li> 
 <li>增加优化规则，移除无用的 AppendVertices 操作符。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4277" target="_blank">#4277</a></li> 
 <li>增加优化规则，优化边过滤的下推。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4270" target="_blank">#4270</a></li> 
 <li>增加优化规则，优化点属性过滤的下推。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4260" target="_blank">#4260</a></li> 
 <li>剔除点的预测过滤器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4249" target="_blank">#4249</a></li> 
 <li>减少移动数据时连接操作的数据复制量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4283" target="_blank">#4283</a></li> 
 <li>通过下标获取属性值，减少属性查询的时间。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4242" target="_blank">#4242</a></li> 
 <li>优化查询最短路径的性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4071" target="_blank">#4071</a></li> 
 <li>优化查询子图的循环条件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4226" target="_blank">#4226</a></li> 
 <li>减少移动数据时 Traverse 和 AppendVertices 操作符的数据复制量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4176" target="_blank">#4176</a></li> 
 <li>改善优化规则，去除无效的项目操作符。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4157" target="_blank">#4157</a></li> 
 <li>使用 Arena Allocator 优化内存分配。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4239" target="_blank">#4239</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">缺陷修复</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>修复 Web 服务在接收一些特殊攻击消息时崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4334" target="_blank">#4334</a></li> 
 <li>修复并发扫描属性时 Storage 服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4268" target="_blank">#4268</a></li> 
 <li>修复插入超过限制长度的边时 Storage 服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4305" target="_blank">#4305</a></li> 
 <li>修复启用查询并发模式时服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4288" target="_blank">#4288</a></li> 
 <li>修复查找具有 NULL 属性的索引时 Storage 服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4234" target="_blank">#4234</a></li> 
 <li>修复重启后独立守护进程退出的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4269" target="_blank">#4269</a></li> 
 <li>修复 Graphviz 在线工具由于两次 JSON 转换导致 Join 点格式的解释结果不正确的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4280" target="_blank">#4280</a></li> 
 <li>修复属性查找的缺陷，不允许在 Schema 中使用英文句号（.）。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4194" target="_blank">#4194</a></li> 
 <li>修复恢复数据时机器丢失 key 的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4311" target="_blank">#4311</a></li> 
 <li>修复使用相同语句返回相同顶点不同属性时，结果显示<span> </span><code>BAD TYPE</code><span> </span>的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4151" target="_blank">#4151</a></li> 
 <li>修复无索引时，语句<span> </span><code>MATCH p=(:team)-->() RETURN p LIMIT 1</code><span> </span>的报错信息缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4053" target="_blank">#4053</a></li> 
 <li>增强运算符<span> </span><code>AND</code><span> </span>和<span> </span><code>OR</code><span> </span>的报错信息。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4304" target="_blank">#4304</a></li> 
 <li>修复索引条件下没有统计信息的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4353" target="_blank">#4353</a></li> 
 <li>修复集群内时区不同的缺陷。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4391" target="_blank">#4391</a></li> 
 <li>修复删除全文索引时崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4384" target="_blank">#4384</a></li> 
 <li>修复当发送 PUT 请求，请求体为空时，服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4405" target="_blank">#4405</a></li> 
 <li>修复当在有索引的基础上删除点和边时，语句中的 VID 的长度超出定义的长度时，Storage 服务崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Fpull%2F4406" target="_blank">#4406</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">历史版本</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnebula-graph.com.cn%2Ftags%2Frelease-note%2F" target="_blank">历史版本</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可前往 GitHub 体验该版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula%2Freleases%2Ftag%2Fv3.2.0" target="_blank">https://github.com/vesoft-inc/nebula/releases/tag/v3.2.0</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">交流图数据库技术？加入 NebulaGraph 交流群请先<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwj.qq.com%2Fs2%2F8321168%2F8e2f%2F" target="_blank">填写下你的 NebulaGraph 名片</a>，NebulaGraph 小助手会拉你进群～～</p>
                                        </div>
                                      
</div>
            