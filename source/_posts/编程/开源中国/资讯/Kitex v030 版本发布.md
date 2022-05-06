
---
title: 'Kitex v0.3.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6940'
author: 开源中国
comments: false
date: Fri, 06 May 2022 10:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6940'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">Feature</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F366" target="_blank">#366</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F426" target="_blank">#426</a><span> </span>] 功能(client): 客户端支持预热操作。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F395" target="_blank">#395</a><span> </span>] 功能(mux): 连接多路复用支持优雅关闭。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F399" target="_blank">#399</a><span> </span>] 功能(protobuf): 定义 fastpb protocol API 并在编解码模块对应支持。</li> 
</ul> 
<h2 style="text-align:left">Optimise</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F402" target="_blank">#402</a><span> </span>] 优化(connpool): 导出 pkg/remote/connpool 里的 getCommonReporter。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F389" target="_blank">#389</a><span> </span>] 优化(rpcinfo)：填充由 defaultCodec 解码得到的 rpcinfo 中缺失的 Invocation().PackageName， Invocation().ServiceName and Config().TransportProtocol 字段。</li> 
</ul> 
<h2 style="text-align:left">Bugfix</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F413" target="_blank">#413</a><span> </span>] 修复(mux): 在 NetpollMux transHandler 中设置 sendMsg的PayloadCodec，以修复泛化请求编码报错问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fissues%2F411" target="_blank">issue #411</a>。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F406" target="_blank">#406</a><span> </span>] 修复(grpc): 修复 http2 framer 的读写逻辑，例如避免对端无法及时收到 framer。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F398" target="_blank">#398</a><span> </span>] 修复(utils)：修复了 Dump() 接口无法 dump 出 ring 里所有数据的 bug。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F428" target="_blank">#428</a><span> </span>] 修复(trans)：当写入失败时，关闭连接以避免内存泄漏。</li> 
</ul> 
<h2 style="text-align:left">Tool</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F340" target="_blank">#340</a><span> </span>] tool(protobuf): 重新设计并实现 Protobuf 生成代码，不使用反射完成编解码，当前仅支持 proto3。</li> 
</ul> 
<h2 style="text-align:left">Chore</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F396" target="_blank">#396</a><span> </span>] chore: 用 bytedance/gopkg 里的 xxhash3 替换掉 cespare/xxhash。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F400" target="_blank">#400</a><span> </span>] chore: 升级 workflow 的 go 版本到 1.18。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F407" target="_blank">#407</a><span> </span>] chore: 单独增加文件对 grpc 源码使用做声明。</li> 
</ul> 
<h2 style="text-align:left">Test</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F401" target="_blank">#401</a><span> </span>] test: 补充 kitex/server 的单测。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F393" target="_blank">#393</a><span> </span>] test: 补充 pkg/remote/bound package 单测。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F403" target="_blank">#403</a><span> </span>] test: 补充 netpollmux package 单测。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F401" target="_blank">#401</a><span> </span>] test: 补充 klog package 单测。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F392" target="_blank">#392</a><span> </span>] test: 补充 utils package 单测。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F373" target="_blank">#373</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F432" target="_blank">#432</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F434" target="_blank">#434</a><span> </span>] test: 补充 gRPC transport 部分的单测，单测覆盖率提升到 76%。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F424" target="_blank">#424</a><span> </span>] test: 补充 transmeta 实现 handler 的单元测试。</li> 
</ul> 
<h2 style="text-align:left">Dependency Change</h2> 
<ul> 
 <li>github.com/cloudwego/netpoll: v0.2.0 -> v0.2.2</li> 
 <li>github.com/bytedance/gopkg: 20210910103821-e4efae9c17c3 -> 20220413063733-65bf48ffb3a7</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更多资讯</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Kitex:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex" target="_blank">https://github.com/cloudwego/kitex</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">原文：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Freleases%2Ftag%2Fv0.3.0" target="_blank">Release v0.3.0 · cloudwego/kitex (github.com)</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            