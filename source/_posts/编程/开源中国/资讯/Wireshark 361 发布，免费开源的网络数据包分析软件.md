
---
title: 'Wireshark 3.6.1 发布，免费开源的网络数据包分析软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2105'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2105'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wireshark 是世界上最流行的网络协议分析器。它被用于故障排除、分析、开发和教育。Wireshark 3.6.1 发布，更新内容如下：</p> 
<h3>新功能和更新功能</h3> 
<ul> 
 <li>在 Wireshark 3.6.0 中删除了 <code>console.log.level</code> 。这个版本在 CLI 上增加了一个 <code>-o console.log.level:</code> 向后兼容的选项，映射到新的日志子系统。</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>允许十六进制转储中的亚秒级时间戳 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F15562" target="_blank">Issue 15562</a>.</li> 
 <li>GRPC：如果 GRPC 消息体长度为 0，会显示一个不必要的空 Protobuf 树项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17675" target="_blank">Issue 17675</a>.</li> 
 <li>不能在没有 Rosetta 2 的 M1 MacBook Air Monterey 上安装 "ChmodBPF.pkg" 或 "将 Wireshark添加到系统 path.pkg” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17757" target="_blank">Issue 17757</a>.</li> 
 <li>TECMP: LIN Payload 被切断了 1 个字节 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17760" target="_blank">Issue 17760</a>.</li> 
 <li>如果一个 64 位的 BASE_CUSTOM 类型的字段被应用为一个列，Wireshark 会崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17762" target="_blank">Issue 17762</a>.</li> 
 <li>命令行选项 <code>-o console.log.level</code> 导致 wireshark 和 tshark 启动时退出 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17763" target="_blank">Issue 17763</a>.</li> 
 <li>设置 WIRESHARK_LOG_LEVEL=debug 会破坏接口捕获 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17764" target="_blank">Issue 17764</a>.</li> 
 <li>在没有 tshark 的情况下，无法构建 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17766" target="_blank">Issue 17766</a>.</li> 
 <li>IEEE 802.11 动作帧没有被解析，总是被视为格式错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17767" target="_blank">Issue 17767</a>.</li> 
 <li>IEC 60870-5-101 链接地址字段是 1 个字节，但应该有 0、1 或 2 个字节的可配置长度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17775" target="_blank">Issue 17775</a>.</li> 
 <li>dfilter: 'tcp.port not in &#123;1&#125;' 使 Wireshark 崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fwireshark%2Fwireshark%2F-%2Fissues%2F17785" target="_blank">Issue 17785</a>.</li> 
</ul> 
<h3>更新的协议支持</h3> 
<ul> 
 <li>ANSI A I/F、AT、BitTorrent DHT、FF、GRPC、IEC 101/104、IEEE 802.11、IEEE 802.11 Radiotap、IPsec、Kafka、QUIC、RTMPT、RTSP、SRVLOC、Sysdig Event 和 TECMP。</li> 
</ul> 
<h3>新的和更新的捕获文件支持</h3> 
<ul> 
 <li>BLF 和 RFC 7468</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.wireshark.org%2Fdocs%2Frelnotes%2Fwireshark-3.6.1.html" target="_blank">https://www.wireshark.org/docs/relnotes/wireshark-3.6.1.html</a></p>
                                        </div>
                                      
</div>
            