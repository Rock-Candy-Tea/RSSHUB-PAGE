
---
title: 'RRQMSocket v6.1.0 发布，网络通信服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6106'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 15:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6106'
---

<div>   
<div class="content">
                                                                                            <p>RRQMSocket v6.1.0 已经发布，网络通信服务框架。</p> 
<p>此版本更新内容包括：</p> 
<h2>版本号:6.1.0</h2> 
<p><strong>更新日期：2021.12.18</strong> <strong>更新描述：</strong> 本次更新TCP部分内容调整，取消net461平台发布（由net45完全替代），增加net5平台独立平台发布。谨慎更新，望周知。</p> 
<p>【RRQMCore】 修复：RRQM序列化字典bug。 修改：重构BytePool，改为<strong>静态类</strong>相关操作，优化其运行逻辑。 优化：ByteBlock用法，可以直接new新对象，其实质效果和BytePool.GetByteBlock一致。</p> 
<p>【RRQMSocket】 增加：TCP客户端取消PreviewConnect函数，统一改为OnConnecting（或Connecting事件）。 增加：Channel在发出操作指令时，可携带相关信息，接收方可通过LastOperationMes获取。 修改：BaseSocket继承自RRQMDependencyObject，可以随意注入RRQM依赖属性。 修改：Udp相关运行逻辑。 修改：Config中取消关于内存池的相关设置，改为BytePool静态设置。 修改：数据处理适配器中关于Logger的使用，如果有输出，直接抛出异常即可。 优化：数据处理适配器测试器的多样性。 优化：数据处理适配器的安全性，避免一个适配器多用的情况。 优化：数据处理适配器的赋值时机，新版本可以在任何时候设置适配器（包括构造函数），但是如果客户端有重连需求，则最好在Connecting中设置。</p> 
<p>【RRQMSocket.FileTransfer】 修复：文件传输一系列小bug。 增加：批量文件传输。</p> 
<p>详情查看：<a href="https://gitee.com/dotnetchina/RRQMSocket/releases/v6.1.0">https://gitee.com/dotnetchina/RRQMSocket/releases/v6.1.0</a></p>
                                        </div>
                                      
</div>
            