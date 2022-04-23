
---
title: 'Deno 1.21 发布，JavaScript 运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4291'
author: 开源中国
comments: false
date: Sat, 23 Apr 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4291'
---

<div>   
<div class="content">
                                                                                            <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.21 已发布，包括以下变更：</p> 
<ul> 
 <li>feat(bench): 更新 API，新增控制台报告器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14305" target="_blank">#14305</a>)</li> 
 <li>feat(cli/fmt): 在格式化文件时忽略 .git 文件夹 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14138" target="_blank">#14138</a>)</li> 
 <li>feat(core): 添加对 realms 的初始支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14019" target="_blank">#14019</a>)</li> 
 <li>feat(ext/net): <code>Deno.upgradeHttp</code> 处理 unix 连接 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13987" target="_blank">#13987</a>)</li> 
 <li>feat(ext/web): 增加 globalThis.reportError() (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13799" target="_blank">#13799</a>)</li> 
 <li>feat(repl): 导入模块时不进行类型检查 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14112" target="_blank">#14112</a>)</li> 
 <li>feat(repl): 添加 <code>--eval-file</code> 标志，以便在启动时执行一个脚本文件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14247" target="_blank">#14247</a>)</li> 
 <li>feat(repl): 增加全局 <code>clear()</code> 函数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14332" target="_blank">#14332</a>)</li> 
 <li>feat(test): 在 <code>Deno.TestContext</code> 中添加 <code>name</code>、 <code>origin</code> 和 <code>parent</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14007" target="_blank">#14007</a>)</li> 
 <li>feat(test): 改进测试报告输出 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14255" target="_blank">#14255</a>)</li> 
 <li>feat(test): 格式化用户代码输出 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14271" target="_blank">#14271</a>)</li> 
 <li>feat(test): 跳过错误的内部 stack frames (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14302" target="_blank">#14302</a>)</li> 
 <li>feat(test): 在测试中对 JavaScript 错误使用结构化数据 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14287" target="_blank">#14287</a>)</li> 
 <li>feat: 为类型检查添加 "deno check" 子命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14072" target="_blank">#14072</a>)</li> 
 <li>feat: 增加 <code>DENO_NO_PROMPT</code> 变量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14209" target="_blank">#14209</a>)</li> 
 <li>feat: 更好的格式化 <code>AggregateError</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14285" target="_blank">#14285</a>)</li> 
 <li>fix(cli/emit): 用 <code>// @ts-check</code> 检查 JS roots(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14090" target="_blank">#14090</a>)</li> 
 <li>fix(permissions): 如果权限提示失败，回退到拒绝访问的状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14235" target="_blank">#14235</a>)</li> 
 <li>fix: <code>-watch</code> 会丢失项目 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14317" target="_blank">#14317</a>)</li> 
 <li>perf(fmt/lint): 增量格式化和提示 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14314" target="_blank">#14314</a>)</li> 
 <li>perf(runtime): 绕过 tokio 文件，将操作缓冲区大小提高到 64 K (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14319" target="_blank">#14319</a>)</li> 
 <li>perf: 将 <code>Deno.writeTextFile</code> 和类似函数移至 Rust (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14221" target="_blank">#14221</a>)</li> 
 <li>upgrade: rusty_v8 0.42.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14334" target="_blank">#14334</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases%2Ftag%2Fv1.21.0" target="_blank">https://github.com/denoland/deno/releases/tag/v1.21.0</a></p>
                                        </div>
                                      
</div>
            