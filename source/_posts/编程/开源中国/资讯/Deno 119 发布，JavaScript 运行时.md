
---
title: 'Deno 1.19 发布，JavaScript 运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2973'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2973'
---

<div>   
<div class="content">
                                                                                            <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.19 已发布，包括以下变更：</p> 
<ul> 
 <li>Deno 已升级到 Google V8 9.9 JavaScript/WebAssembly 引擎</li> 
 <li>feat: 添加 Deno.FsFile，弃用 Deno.File (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13660" target="_blank">#13660</a>)</li> 
 <li>feat: 在权限提示中添加提示，以显示允许标记 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13695" target="_blank">#13695</a>)</li> 
 <li>feat: 永远不提示 hrtime 权限 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13696" target="_blank">#13696</a>)</li> 
 <li>feat: 默认的权限提示 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13650" target="_blank">#13650</a>)</li> 
 <li>feat(compat): 在 web workers 中支持 --compat (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13629" target="_blank">#13629</a>)</li> 
 <li>feat(compile): 在 deno 编译中用 eszip 取代 bundling (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13563" target="_blank">#13563</a>)</li> 
 <li>feat(coverage): 添加 "--output" 标志 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13289" target="_blank">#13289</a>)</li> 
 <li>feat(ext/console): 在对象检查中提供更好的循环信息 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13555" target="_blank">#13555</a>)</li> 
 <li>feat(ext/http): 增加对 unix domain sockets 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13628" target="_blank">#13628</a>)</li> 
 <li>feat(ext/net): 增加 Conn.setNoDelay 和 Conn.setKeepAlive (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13103" target="_blank">#13103</a>)</li> 
 <li>feat(ext/web): 添加 CompressionStream API (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F11728" target="_blank">#11728</a>)</li> 
 <li>feat(lsp): 增加重定向诊断和快速修复 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13580" target="_blank">#13580</a>)</li> 
 <li>feat(lsp): 支持在悬停时链接到 JSDoc 中的符号 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13631" target="_blank">#13631</a>)</li> 
 <li>feat(runtime): 稳定 addSignalListener API (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13438" target="_blank">#13438</a>)</li> 
 <li>feat(watch): 添加 "--no-clear-screen" 标志 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13454" target="_blank">#13454</a>)</li> 
 <li>fix(ext/console): 修复 css 样式中未捕获的 TypeError (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13567" target="_blank">#13567</a>)</li> 
 <li>fix(ext/crypto): 加密/解密中的可选 additionalData (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13669" target="_blank">#13669</a>)</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p>
                                        </div>
                                      
</div>
            