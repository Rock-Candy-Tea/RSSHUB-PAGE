
---
title: 'Chrome 103 发布，引入 Deflaw-Raw 压缩格式、本地字体访问'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=237'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=237'
---

<div>   
<div class="content">
                                                                                            <p>Chrome 103 稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromereleases.googleblog.com%2F2022%2F06%2Fstable-channel-update-for-desktop_21.html" target="_blank">发布</a>啦。</p> 
<p>Chrome 103  <span style="color:#121212">引入了 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5207422375297024">103 Early Hints HTTP 响应代码</a><span style="color:#333333">进行导航的</span><span style="color:#121212">支持，</span><span style="color:#333333">当 103 响应包含 </span><code><link rel=preload></code><span style="color:#333333"> 或其他链接标头时，Chrome 会在收到响应之前尝试预加载指定资源。该功能为 Web 开发人员提供了一种优化</span>核心 Web<span style="color:#333333"> Vitals 的方法，例如最大内容绘制 (LCP)。</span></p> 
<p><span style="color:#333333">Chrome 103 Beta 还添加了 “deflate-raw” 压缩格式支持，允许 Web 开发人员在没有任何页眉 / 页脚的情况下访问原始 deflate 流，这种 deflate-raw 支持可帮助 Web 应用程序读取和写入 zip 文件。</span></p> 
<p>此外，Chrome 103 改进了本地字体访问功能，允许枚举本地字体和所述字体的元数据，以便在 Web 应用程序中用于自定义的文本堆栈。</p> 
<p style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5188935855636480" target="_blank">角色属性的 ARIA 属性反射</a> ：该功能提供了一个 JavaScript AP，允许 Web 开发人员直接查询和修改“角色”ARIA 属性。实现了“角色”属性的属性反射。</p> 
<p style="margin-left:0px">此外还有新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5768400507764736" target="_blank">AbortSignal.timeout() 静态方法</a> ，它返回一个新的 AbortSignal 对象，该对象在给定的毫秒数后自动中止。开发人员可以使用此方法轻松实现信号接收异步 API 的超时，例如 fetch()。</p> 
<p style="margin-left:0px">更多内容可在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromereleases.googleblog.com%2F" target="_blank">Chrome 博客</a> 中阅读，关于 103 版本的更多功能可在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeatures%23milestone%253D103" target="_blank">ChromeStatus.com</a> 查看。</p>
                                        </div>
                                      
</div>
            