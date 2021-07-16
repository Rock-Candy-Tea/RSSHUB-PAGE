
---
title: 'Node.js 16.5.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1925'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1925'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。Node.js 由Node.js Foundation（已与JS Foundation合并为OpenJS Foundation）持有和维护，亦为 Linux 基金会的项目。Node.js 采用 Google 开发的 V8 运行代码，使用事件驱动、非阻塞和异步输入输出模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于资料密集的即时应用程序。</p> 
<p>Node.js 16.5.0 正式发布，本次更新内容如下：</p> 
<h3><strong>实验性 Web Streams API：</strong></h3> 
<p>Node.js 现在公开了一个实验性的 Web Streams API 实现。</p> 
<p>因为它是实验性 API，所以该 API 并没有公开在全局对象中，而只能使用新的 stream/web 核心模块访问。</p> 
<pre><code>import &#123; ReadableStream, WritableStream &#125; from 'stream/web';
// Or from 'node:stream/web'
</code></pre> 
<p>导入模块将在每个进程中发出一个实验警告。实现了原始 API，我们现在正致力于将其与各种现有的核心 API 集成。</p> 
<h3>显着变化：</h3> 
<ul> 
 <li> <strong>(SEMVER-MINOR)</strong> <strong>fs</strong>: 允许临时目录前缀为空字符串；</li> 
 <li><strong>deps</strong>: 将 npm 升级到 7.19.1；</li> 
</ul> 
<h3>其他：</h3> 
<ul> 
 <li> <strong>build</strong>: 更新 gcovr 以兼容 gcc 8；</li> 
 <li> <strong>build</strong>: 将 riscv 加入 host_arch_cc；</li> 
 <li> <strong>build</strong>: 删除 Makefile 中未使用的注释；</li> 
 <li> <strong>build</strong>: 允许使用 Makefile 构建 riscv64；</li> 
 <li> <strong>build</strong>: 缩短 tarball 构建工作流程中使用的路径；</li> 
 <li> <strong>build</strong>: 向 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjs2c.py%2F" target="_blank">js2c.py</a> 传递目录而不是文件列表；</li> 
 <li> <strong>build</strong>: 不要向 V8 测试运行器传递 <code>-mode</code> 参数；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv16.5.0%2F" target="_blank">https://nodejs.org/en/blog/release/v16.5.0/</a></p>
                                        </div>
                                      
</div>
            