
---
title: 'Deno 1.18 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8618'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8618'
---

<div>   
<div class="content">
                                                                                            <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.18 已发布，包括以下变更：</p> 
<ul> 
 <li>feat: 自动发现配置文件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13313" target="_blank">#13313</a>)</li> 
 <li>feat: 在 JS 运行时错误时输出 <code>cause</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13209" target="_blank">#13209</a>)</li> 
 <li>feat: 稳定测试步骤的API (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13400" target="_blank">#13400</a>)</li> 
 <li>feat(cli, runtime): 压缩快照 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13320" target="_blank">#13320</a>)</li> 
 <li>feat(cli): 为捆绑代码添加忽略指令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13309" target="_blank">#13309</a>)</li> 
 <li>feat(compat) 在全局 vars REPL 中预加载 Node.js 内置模块 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13127" target="_blank">#13127</a>)</li> 
 <li>feat(ext/crypto): 实现 AES-GCM 解密 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13319" target="_blank">#13319</a>)</li> 
 <li>feat(ext/crypto): 实现 AES-GCM 加密 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13119" target="_blank">#13119</a>)</li> 
 <li>feat(ext/crypto): 为 wrapKey/unwrapKey 实现 AES-KW (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13286" target="_blank">#13286</a>)</li> 
 <li>feat(ext/crypto): 为 P-384 curves 实现 pkcs8/JWK (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13154" target="_blank">#13154</a>)</li> 
 <li>feat(ext/crypto): 为 ECDSA 和 ECDH 实现 pkcs8/spki/jwk exportKey (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13104" target="_blank">#13104</a>)</li> 
 <li>feat(ext/crypto): JWK 支持 unwrapKey/wrapKey (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13261" target="_blank">#13261</a>)</li> 
 <li>feat(ext/crypto): 支持 AES-CTR 加密/解密 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13177" target="_blank">#13177</a>)</li> 
 <li>feat(ext/crypto): 支持导入原始 EC keys (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13079" target="_blank">#13079</a>)</li> 
 <li>feat(ext/ffi): 推断符号类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13221" target="_blank">#13221</a>)</li> 
 <li>feat(ext/ffi): 支持符号定义的别名 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13090" target="_blank">#13090</a>)</li> 
 <li>feat(ext/ffi): UnsafeFnPointer API (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13340" target="_blank">#13340</a>)</li> 
 <li>feat(ext/websocket): 为 WebSocketStream 添加 header 信息支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F11887" target="_blank">#11887</a>)</li> 
 <li>feat(ext/websocket): 服务器自动为传入 WebSocket 处理 ping/pong (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13172" target="_blank">#13172</a>)</li> 
 <li>feat(lsp): 在悬停时提供注册表的详细信息 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13294" target="_blank">#13294</a>)</li> 
 <li>feat(runtime): 添加 op_network_interfaces (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F12964" target="_blank">#12964</a>)</li> 
 <li>feat(serde_v8): 反序列化 ArrayBuffers (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13436" target="_blank">#13436</a>)</li> 
 <li>feat(test): 增加对 "deno test --compat" 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13235" target="_blank">#13235</a>)</li> 
 <li>fix(cli): 不要从模块中剥离 shebangs (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13220" target="_blank">#13220</a>)</li> 
 <li>fix(cli): 修复 <code>deno install --prompt</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13349" target="_blank">#13349</a>)</li> 
 <li>fix(cli/dts): 增加 NotSupported 错误类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13432" target="_blank">#13432</a>)</li> 
 <li>fix(ext/console): 不要依赖 globalThis 的存在 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13387" target="_blank">#13387</a>)</li> 
 <li>fix(ext/crypto): 在 importKey 中验证 maskGenAlgorithm asn1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13421" target="_blank">#13421</a>)</li> 
 <li>fix(ext/ffi): <code>pointer</code> 类型可以接受 <code>null</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13335" target="_blank">#13335</a>)</li> 
 <li>fix(fmt): markdown 格式化不应该删除段落开头的反斜杠 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13429" target="_blank">#13429</a>)</li> 
 <li>fix(lsp): 更好地处理注册表配置错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13418" target="_blank">#13418</a>)</li> 
 <li>fix(runtime): 窗口被删除时不会崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13392" target="_blank">#13392</a>)</li> 
 <li>fix(tsc): 为 <code>Intl.ListFormat</code> 添加类型(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13301" target="_blank">#13301</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p>
                                        </div>
                                      
</div>
            