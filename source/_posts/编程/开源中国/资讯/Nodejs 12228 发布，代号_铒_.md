
---
title: 'Node.js 12.22.8 发布，代号_铒_'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8625'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 23:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8625'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境，采用 Google 开发的 V8 运行代码，使用事件驱动、非阻塞和异步输入输出模型等技术来提高性能。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Node.js 12.22.8 （代号“铒”） 已发布，更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>显著变化：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>此版本包含一个 c-ares 更新，以修复 Node.js 12.22.5 中引入的回归：解析包含下划线的 CNAME 记录。  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fissues%2F39780" target="_blank">#39780</a></li> 
 <li><span style="color:#2e3033">根证书已经更新为来自 Mozilla 的网络安全服务证书 3.71 版本。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40280" target="_blank">#40281</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033"><strong>其他提交</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F2d42295d2a" target="_blank"><code>2d42295d2a</code></a>] -<span> </span><strong>build</strong>：将 macOS GitHub 运行器固定到 macos-10.15  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41124" target="_blank">#41124</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F41e09ec71b" target="_blank"><code>41e09ec71b</code></a>] -<span> </span><strong>child_process</strong>：保留对具有高级序列化的数据的引用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38728" target="_blank">#38728</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2Ff0be07796e" target="_blank"><code>f0be07796e</code></a>] -<span> </span><strong>crypto</strong>：更新根证书  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40280" target="_blank">#40280</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F4c9f920d34" target="_blank"><code>4c9f920d34</code></a>] -<span> </span><strong>deps</strong>：更新 OpenSSL-1.1.1m 的 archs 文件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41172" target="_blank">#41172</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F60d7d4171e" target="_blank"><code>60d7d4171e</code></a>] -<span> </span><strong>deps</strong>：将 openssl 源升级到 1.1.1m  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41172" target="_blank">#41172</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F7feff67419" target="_blank"><code>7feff67419</code></a>] -<span> </span><strong>deps</strong>：将 -fno-strict-aliasing 标志添加到 libuv  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40631" target="_blank">#40631</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F534ac7c7c6" target="_blank"><code>534ac7c7c6</code></a>] -<span> </span><strong>deps</strong>：将 c-ares 更新到 1.18.1<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40660" target="_blank">#40660</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2Fc019fa9b70" target="_blank"><code>c019fa9b70</code></a>] -<span> </span><strong>deps</strong>：更新到 cjs-module-lexer @1.2.2  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39402" target="_blank">#39402</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2Fb13340eff4" target="_blank"><code>b13340eff4</code></a>] -<span> </span><strong>doc</strong>：将替代版本链接添加到包页面  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F36915" target="_blank">#36915</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F243b2fbfdb" target="_blank"><code>243b2fbfdb</code></a>] -<span> </span><strong>lib</strong>：修复正则表达式以检测 `/` 和 `\`   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40325" target="_blank">#40325</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F70e094a26b" target="_blank"><code>70e094a26b</code></a>] -<span> </span><strong>repl</strong>：修复错误消息打印   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38209" target="_blank">#38209</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F02b432a704" target="_blank"><code>02b432a704</code></a>] -<span> </span><strong>src</strong>：修复 AfterGetAddrInfo 中的崩溃<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39735" target="_blank">#39735</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F7479447d6a" target="_blank"><code>7479447d6a</code></a>] -<span> </span><strong>test</strong>：破解 child-process-pipe-dataflow  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40838" target="_blank">#40838</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2F833e199393" target="_blank"><code>833e199393</code></a>] -<span> </span><strong>tools</strong>：更新 certdata.txt   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40280" target="_blank">#40280</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2Fe4339fe286" target="_blank"><code>e4339fe286</code></a>] -<span> </span><strong>tools</strong>：添加脚本以更新 c-ares  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40660" target="_blank">#40660</a></li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fcommit%2Ff50b9c1e8a" target="_blank"><code>f50b9c1e8a</code></a>] -<span> </span><strong>worker</strong>：避免在 NearHeapLimit 上潜在的死锁  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38403" target="_blank">#38403</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Freleases%2Ftag%2Fv12.22.8" target="_blank">https://github.com/nodejs/node/releases/tag/v12.22.8</a></p>
                                        </div>
                                      
</div>
            