
---
title: 'Apache bRPC 1.1.0 发布，支持 IPV6 和 UDS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6676'
author: 开源中国
comments: false
date: Fri, 15 Apr 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6676'
---

<div>   
<div class="content">
                                                                                            <p>Apache bRPC 1.1.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FM5f_NHsS2trYyAcA5qzWbQ" target="_blank">发布</a>。bRPC是一个开源高性能的工业级 RPC 框架，拥有 1,000,000+ 个实例（不包含 client）和上千种服务。</p> 
<p>此<span style="background-color:#ffffff">版本的主要变更内容为：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#1a1a1a">新功能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">支持 IPV6 和 UDS(Unix Domain Socket)</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">支持 protobuf 3.19.x</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">支持 http 协议的 dump/replay</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">支持 nshead 协议的 dump/replay</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">支持 http body 为 proto-text 格式的 request/response</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">baidu_std 协议支持传递 client 端设置的超时到 server 端</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">bthread 创建时支持通过 attr 指定继承 tls span</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">rpc_replay 支持 bazel 编译</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">Server 新增<span> </span></span><span style="background-color:#ffffff">Start(PortRange, const ServerOptions*) 接口</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">FlapMap 新增 insert(const std::pair<key_type, mapped_type>& kv) 接口</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">Server 新增 eps bvar 输出</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#1a1a1a">Bug 修复</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 CheckHealth 未设置 has_request_code</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 server 处理 stream 创建请求过程出错时发送非预期数据</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 LA selection runs too long 的出错</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 http 收到不合法请求时返回错误的 response</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 bvar status 编译错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">优化 InputMessenger client 端重试策略</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 work_stealing_queue_unittest 在 ARM 下编译错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 LatencyRecorder qps 统计不精确</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复在 gcc11 下开启 --std=c++20 时编译错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复不稳定和 UT 链接错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修复 Thrift 下载 url 错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">删除 grpc ParseH2Settings 不必要的 warning 日志</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#1a1a1a">其它改进</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">文档改进</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">修正拼写错误</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left">详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FM5f_NHsS2trYyAcA5qzWbQ" target="_blank">查看官方公告</a>。</p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">下载链接：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbrpc.apache.org%2Fdocs%2Fdownloadbrpc%2F" target="_blank">https://brpc.apache.org/docs/downloadbrpc/</a></p>
                                        </div>
                                      
</div>
            