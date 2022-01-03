
---
title: 'RRQMSocket v6.3.0 发布，网络通信服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=414'
author: 开源中国
comments: false
date: Mon, 03 Jan 2022 00:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=414'
---

<div>   
<div class="content">
                                                                                            <p>RRQMSocket v6.3.0 已经发布，网络通信服务框架。</p> 
<p>此版本更新内容包括：</p> 
<h2>版本号:6.3</h2> 
<p><strong>更新日期：2022.1.2</strong> <strong>更新描述：</strong> 本次更新为RPC部分修改较大，且RPCTool相关工具强制更新，不然无法使用。</p> 
<p>【RRQMCore】 修复：RRQM序列化多数据bug。 增加：大小端转换器RRQMBitConverter，其用法与BitConverter基本一致。</p> 
<p>【RRQMSocket】 增加：IPHost支持域名解析。 增加：NATService，可以一键完成TCP数据转发。 优化：全面解决大小端问题，RRQM系默认以RRQMBitConverter.Default小端转化。 修复：Protocol系用户协议冲突检测问题。</p> 
<p>【RRQMSocket.RPC】 重构RPC，优化调用框架。 修改：发现服务时，由配置文件的ProxyToken转换为直接传参ProxyToken。 修改：代理文件的生成不再由RRQMRPC提供，转而由RpcService直接提供。提供的代理也直接支持JsonRpc和XmlRpc。 修改：代理文件的生成，不再一次性生成，由系统提供的方法转义，可供更加细微的筛选服务。 修改：反向调用时，不再让TcpRpcClient注册服务，而是由RpcService注册，同时，反向RPC也能使用代理生成、服务筛选、out和ref关键字、调用中断取消、获取调用上下文等。 修改：UdpRpc解析器和客户端均改名为UdpRpc。 优化：在服务定义时，可通过Async属性标识本服务异步执行，但同步返回，因此，这使得反向调用变得简单，不再使用Task。 修复：ID调用的异常bug。</p> 
<p>【RRQMSocket.FileTransfer】 优化：解决大小端问题。</p> 
<p>【RRQMSocket.WebSocket】 修复：大小端问题。</p> 
<p>详情查看：<a href="https://gitee.com/dotnetchina/RRQMSocket/releases/v6.3.0">https://gitee.com/dotnetchina/RRQMSocket/releases/v6.3.0</a></p>
                                        </div>
                                      
</div>
            