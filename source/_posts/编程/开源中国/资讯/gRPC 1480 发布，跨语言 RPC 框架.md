
---
title: 'gRPC 1.48.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5117'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5117'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架。</span><span style="background-color:#ffffff; color:#24292f">gRPC<span> </span></span><span style="background-color:#ffffff; color:#333333">1.48.0 现已发布，包含了一些完善、改进和错误修复；具体更新内容如下：</span></p> 
<p style="text-align:start"><strong>Core</strong></p> 
<ul> 
 <li>将 Abseil 升级到 LTS 20220623.0 。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30155" target="_blank">#30155</a>）</li> 
 <li>调用：即使没有发送操作，也向堆栈发送取消操作。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30004" target="_blank">#30004</a> )</li> 
 <li>FreeBSD 系统根目录实现。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29436" target="_blank">#29436</a>）</li> 
 <li>xDS：让 gRPC 客户端与 istio 一起工作的解决方法。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29841" target="_blank">#29841</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>在 Mac OS 上使用 Python 3.10 的 Wheels 中设置正确的平台标签。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29857" target="_blank">#29857</a>）</li> 
 <li>[Aio] 确保 Core channel 在 deallocated 时关闭。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29797" target="_blank">#29797</a>）</li> 
 <li>[Aio] 修复 wait_for_termination 返回值。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29795" target="_blank">#29795</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>在 TruffleRuby 上构建 gem。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27660" target="_blank">#27660</a>）</li> 
 <li>支持 x64-mingw-ucrt 平台上的预构建 Ruby 二进制文件。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29684" target="_blank">#29684</a>）</li> 
 <li>[Ruby] 将 ruby​​_abi_version 添加到导出的符号。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28976" target="_blank">#28976</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Objective-C</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过 Cocoapod ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fissues%2F28749" target="_blank">#28749</a> ) 的 XCFramework 二进制分发的第一个开发人员预览。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这显着加快了本地编译时间，并包括对 Apple Silicon 构建的支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>以下二进制 pod 可用于 ObjC V1 和 V2 API 
  <ul> 
   <li>gRPC-XCFramework（source pod gRPC）</li> 
   <li>gRPC-ProtoRPC-XCFramework（source pod gRPC-ProtoRPC）</li> 
  </ul> </li> 
 <li>包括以下平台和架构 
  <ul> 
   <li>ios：armv7、arm64 用于设备。用于模拟器的 arm64、i386、x86_64</li> 
   <li>macos：x86_64 (Intel)、arm64 (Apple Silicon)</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.48.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.48.0</a></p>
                                        </div>
                                      
</div>
            