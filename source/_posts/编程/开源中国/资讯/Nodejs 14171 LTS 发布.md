
---
title: 'Node.js 14.17.1 LTS 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3468'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 23:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3468'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。Node.js 由Node.js Foundation（已与JS Foundation合并为OpenJS Foundation）持有和维护，亦为 Linux 基金会的项目。Node.js采用Google开发的V8运行代码，使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E4%25BA%258B%25E4%25BB%25B6%25E9%25A9%2585%25E5%258B%2595">事件驱动</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fw%2Findex.php%3Ftitle%3D%25E9%259D%259E%25E9%2598%25BB%25E5%25A1%259E%26action%3Dedit%26redlink%3D1">非阻塞</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%25BC%2582%25E6%25AD%25A5IO">异步输入输出</a>模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于资料密集的即时应用程序。</p> 
<p>Node.js 14.17.1 LTS 正式发布，本次更新内容如下：</p> 
<p>值得注意的变化：</p> 
<ul> 
 <li>[6035492c8f] - deps：更新 ICU 至 69.1；</li> 
 <li>[9417fd0bc8] - 错误：将源代码映射堆栈与规范对齐；</li> 
</ul> 
<p>其他：</p> 
<ul> 
 <li>[87fa636953] - assert：重构以使用更多的 primordials；</li> 
 <li>[cfff3b4462] - assert：重构以避免不安全的数组迭代；</li> 
 <li>[dd18def7db] - async_hooks：重构以避免不安全的数组迭代；</li> 
 <li>[5f3e96b570] - async_hooks, doc：用 1 替换 process.stdout.fd；</li> 
 <li>[f4cb8b8281] - benchmark：避免使用 console.log()；</li> 
 <li>[9e4c1f2f2c] - benchmark：使用 process.hrtime.bigint()；</li> 
 <li>[3c886e0ad6] - buffer：移除 atob/btoa 中的 TODOs；</li> 
 <li>[c5b86f8c2f] - buffer：删除无法访问的代码；</li> 
 <li>[9ae2a27d44] - buffer：使 FastBuffer 可以安全地构造；</li> 
 <li>[ff546ff744] - buffer：重构以使用 primordials 而不是 Array#reduce；</li> 
 <li>[5acf0a5ba3] - buffer：重构以使用更多的 primordials；</li> 
 <li>[52fd42ec46] - build：解决MSBuild v16.10.0中的错误；</li> 
 <li>[5df0f35bf6] - build：为 V8 构建添加解决方法；</li> 
 <li>[754aa384e0] - build：移除对 distutils.spawn 的依赖；</li> 
 <li>[5de7e64f3a] - build：修复 make test-npm；</li> 
 <li>[e5fae63108] - child_process：减少中止处理程序的代码重复</li> 
 <li>[598d2bdf09] - child_process：将 already-aborted 的控制器视为 aborting；</li> 
 <li>[b8c4d30e77] - deps: 更新 cjs-module-lexer 至 1.2.1；</li> 
 <li>[bac9ba4f8a] - dgram：提取 cluster lazy 加载方法，使其可测试；</li> 
 <li>[9f67c0852c] - 文档：清理 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fevents.md" target="_blank">events.md</a> 结构</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Freleases%2Ftag%2Fv14.17.1" target="_blank">https://github.com/nodejs/node/releases/tag/v14.17.1</a></p>
                                        </div>
                                      
</div>
            