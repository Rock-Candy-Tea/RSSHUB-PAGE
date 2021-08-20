
---
title: 'Node.js v16.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4474'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4474'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Node.js v16.7.0 现已发布。</p> 
<p>Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。Node.js 由Node.js Foundation（已与JS Foundation合并为OpenJS Foundation）持有和维护，亦为 Linux 基金会的项目。Node.js 采用 Google 开发的 V8 运行代码，使用事件驱动、非阻塞和异步输入输出模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于资料密集的即时应用程序。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>async_hooks：合并 resource_symbol 和 owner_symbol</li> 
 <li>引导程序：在 _destroy 内为 stdout 和 stderr 调用 _undestroy()</li> 
 <li>缓冲区：添加结尾选项，删除 Node.js 特定的编码选项</li> 
 <li>（SEMVER-MINOR）缓冲区：添加 Blob.prototype.stream 方法和其他清理方法</li> 
 <li>构建：运行覆盖检查器协议更改</li> 
 <li>构建：使用指针压缩修复 V8 构建</li> 
 <li>构建：在 GitHub Actions 中使用 lts 速记</li> 
 <li>（SEMVER-MINOR）加密：实现 webcrypto.randomUUID</li> 
 <li>调试器：防止同时进行堆快照</li> 
 <li>调试器：删除未定义的参数</li> 
 <li>deps：升级到 libuv 1.42.0</li> 
 <li>dgram：使用简化验证器</li> 
 <li>（SEMVER-MINOR）dns：将 “尝试” 选项添加到解析选项</li> 
 <li>（SEMVER-MINOR）fs: 添加递归 cp 方法</li> 
 <li>http：解码授权标头的 url.username 和 url.password</li> 
 <li>perf_hooks：修复 PerformanceObserver gc 崩溃</li> 
 <li>（SEMVER-MINOR）perf_hooks: Web 性能时间线合规性 (legendecas) #39297</li> 
 <li>在设置 DEFAULT_ENCODING 时修复完整性</li> 
 <li>src：修复 TextDecoder 最终刷新大小计算</li> 
 <li>src：修复 AfterGetAddrInfo 中的崩溃</li> 
 <li>（SEMVER-MINOR）src: 在 cares_wrap.h (Luan) 中修复对齐</li> 
 <li>src：向 async_wrap.h 文件添加装饰性空格字符</li> 
 <li>流：确保 text() 流消费者正确刷新</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv16.7.0%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            