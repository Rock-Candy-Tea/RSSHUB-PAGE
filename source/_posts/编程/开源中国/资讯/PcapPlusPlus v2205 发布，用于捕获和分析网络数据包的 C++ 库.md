
---
title: 'PcapPlusPlus v22.05 发布，用于捕获和分析网络数据包的 C++ 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1818'
author: 开源中国
comments: false
date: Fri, 13 May 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1818'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PcapPlusPlus v22.05 现已发布。PcapPlusPlus 是一个多平台的 C++ 库，用于捕获、解析和制作网络数据包。它被设计成高效、强大且易于使用；为最流行的数据包处理引擎<span style="background-color:#ffffff; color:#24292f">（如 libpcap、WinPcap、DPDK 和 PF_RING）提供 C++ wrappers。</span></p> 
<p>新版本更新内容包括：</p> 
<ul> 
 <li>NTP 协议支持</li> 
 <li>支持在 macOS 上构建 Android</li> 
 <li>克隆 live devices 和 live devices list</li> 
 <li>添加对读取 SNOOP 捕获文件的支持</li> 
 <li>在调用<code>initDpdk()</code>时，增加了一个提供额外参数的选项</li> 
 <li>在 PcapPlusPlus 配置期间检测通过<code>pkg-config</code>安装的 DPDK</li> 
 <li>如果<code>insmod</code>在 DPDK 设置脚本中失败，请尝试<code>modprobe</code></li> 
 <li>支持通过 IPv4 解析 IPv6</li> 
 <li>TCP reassembly improvmements： 
  <ul> 
   <li>更新连接信息中看到的最后一个数据包的时间戳</li> 
   <li>在消息回调中添加接收到的数据包的时间戳</li> 
   <li>添加配置参数以禁用 OOO 缓冲区清理</li> 
  </ul> </li> 
 <li>删除<code>IPv4Layer</code>，<code>IPv6Layer</code>和<code>IPcapDevice</code>中已废弃的方法</li> 
 <li>Internal changes： 
  <ul> 
   <li>PcapPlusPlus CI 管道的大规模改造</li> 
   <li>将 Alpine 添加到 PcapPlusPlus CI</li> 
   <li>在 CI 中运行实时网络测试</li> 
   <li>使用标准编译器宏来检测 PcapPlusPlus 在哪个平台上运行</li> 
   <li>添加 pre-commit hooks 以检测拼写错误、尾部空格、错误的文件结尾等</li> 
   <li>在所有 Python 文件上运行 Black 格式化程序</li> 
  </ul> </li> 
 <li>大量错误修复和小改进</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseladb%2FPcapPlusPlus%2Freleases%2Ftag%2Fv22.05" target="_blank">https://github.com/seladb/PcapPlusPlus/releases/tag/v22.05</a></p>
                                        </div>
                                      
</div>
            