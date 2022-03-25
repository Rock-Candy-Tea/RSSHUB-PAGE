
---
title: 'Deno 1.20.2 发布，JavaScript 运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5856'
author: 开源中国
comments: false
date: Fri, 25 Mar 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5856'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.20.2 已发布，包括以下变更：</p> 
<ul> 
 <li>feat(lsp): 支持 deno.enablePaths 设置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13978" target="_blank">#13978</a>)</li> 
 <li>fix(bench): 在 JavaScript 中需要 <code>--unstable</code> 标志 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14091" target="_blank">#14091</a>)</li> 
 <li>fix(compat): 将 <code>collect::<Vec<_>>().join("")</code> 的实例更改为 <code>collect::()</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14082" target="_blank">#14082</a>)</li> 
 <li>fix(tests): 在安装测试中不要使用全局环境变量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14078" target="_blank">#14078</a>)</li> 
 <li>fix(ext/fetch): 用用户代码连接异步错误栈 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13899" target="_blank">#13899</a>)</li> 
 <li>fix(unstable): 升级 deno_task_shell 到 0.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14073" target="_blank">#14073</a>)</li> 
 <li>fix: 升级 swc_ecmascript 到 0.137.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14067" target="_blank">#14067</a>)</li> 
 <li>fix(runtime): 实际上不继承运行时权限 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14024" target="_blank">#14024</a>)</li> 
 <li>fix(ops): 在操作返回失败时抛出 TypeError (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14033" target="_blank">#14033</a>)</li> 
 <li>fix(cli): 改进 <code>deno compile</code>错误消息 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13944" target="_blank">#13944</a>)</li> 
 <li>fix(cli): 在升级命令中添加对 DENO_CERT 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F13862" target="_blank">#13862</a>)</li> 
 <li>fix(config-file): 修正 config-file.v1.json 模式，允许任务中的冒号名称 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14013" target="_blank">#14013</a>)</li> 
 <li>perf(http): 关闭连接资源时避免 Set.has() (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14085" target="_blank">#14085</a>)</li> 
 <li>perf(http): 避免在每个请求中检查 promise (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Fpull%2F14079" target="_blank">#14079</a>)</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p>
                                        </div>
                                      
</div>
            