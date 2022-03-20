
---
title: 'Deno 1.20.1 发布，JavaScript 运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6965'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6965'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Deno 1.20.1 已发布，值得注意的是，没有 1.20.0 版本，详情可见 <span style="background-color:#ffffff; color:#24292f"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13993" target="_blank">#13993</a>。v1.20.1 更新内容如下：</p> 
<ul> 
 <li>BREAKING：默认情况下不继承权限（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13668" target="_blank">#13668</a>）</li> 
 <li>feat(cli)：支持数据 url ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13667" target="_blank">#13667</a> )</li> 
 <li>feat(cli)：更新到 TypeScript 4.6.2 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13474" target="_blank">#13474</a> )</li> 
 <li>feat(compat)：CJS/ESM 互操作性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13553" target="_blank">#13553</a>）</li> 
 <li>feat(core)：扩展的事件循环中间件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13816" target="_blank">#13816</a> )</li> 
 <li>feat(core)：codegen ops（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13861" target="_blank">#13861</a>）</li> 
 <li>feat(ext/crypto)：128bit IVs 的 AES-GCM 支持( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13805" target="_blank">#13805</a> )</li> 
 <li>feat(ext/fetch)：允许 Response status 101 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13969" target="_blank">#13969</a> )</li> 
 <li>feat(ext/net)：使用 socket2 crate 创建 TcpListener ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13808" target="_blank">#13808</a> )</li> 
 <li>feat(ext/web)：添加<code>AbortSignal.timeout()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13687" target="_blank">#13687</a>）</li> 
 <li>feat(net)：添加 Deno.UnixConn 接口 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13787" target="_blank">#13787</a> )</li> 
 <li>feat(ops)：自定义 arity（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13949" target="_blank">#13949</a>）</li> 
 <li>feat(ops)：可选的 OpState（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13954" target="_blank">#13954</a>）</li> 
 <li>feat(unstable)：添加 Deno.upgradeHttp API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13618" target="_blank">#13618</a> )</li> 
 <li>feat：“deno bench”子命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13713" target="_blank">#13713</a>）</li> 
 <li>feat：“deno task”子命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13725" target="_blank">#13725</a>）</li> 
 <li>feat：添加 Deno.TcpConn 类，从 Deno.connect 更改返回类型 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13714" target="_blank">#13714</a> )</li> 
 <li>feat：允许在配置文件中指定导入映射（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13739" target="_blank">#13739</a>）</li> 
 <li>feat：deno 测试 --trace-ops ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13770" target="_blank">#13770</a> )</li> 
 <li>fix(compat)：dynamic imports 的 cjs/esm interop ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13792" target="_blank">#13792</a> </li> 
 <li>fix(core)：不要覆盖来自 V8 的结构化克隆错误信息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13942" target="_blank">#13942</a>）</li> 
 <li>fix(core)：nuke Deno.core.ops pre-snapshot ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13970" target="_blank">#13970</a> )</li> 
 <li>fix(ext/crypto)：用“use”处理 JWK 导入（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13912" target="_blank">#13912</a>）</li> 
 <li>fix(ext/crypto): 使用 EcKeyImportParams 字典 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13894" target="_blank">#13894</a> )</li> 
 <li>fix(ext/http)：在压缩时删除 content-length header（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13866" target="_blank">#13866</a>）</li> 
 <li>fix(test)：跳过对 HTML 注释中块的类型检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13889" target="_blank">#13889</a>）</li> 
 <li>fix：shell 完成提示 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13876" target="_blank">#13876</a> )</li> 
 <li>fix：将 reqwest 升级到 0.11.10 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13951" target="_blank">#13951</a> )</li> 
 <li>perf(web)：通过添加新<code>U16String</code>类型进行优化<code>TextDecoder</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13923" target="_blank">#13923</a>）</li> 
 <li>perf(web)：优化 Blob.text 和 Blob.arrayBuffer ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13981" target="_blank">#13981</a> )</li> 
 <li>perf(web)：为 BlobParts 使用 DOMString ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13979" target="_blank">#13979</a> )</li> 
 <li>perf：opt-level-3 all of ext ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13940" target="_blank">#13940</a> )</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases%2Ftag%2Fv1.20.1" target="_blank">https://github.com/denoland/deno/releases/tag/v1.20.1</a></p>
                                        </div>
                                      
</div>
            