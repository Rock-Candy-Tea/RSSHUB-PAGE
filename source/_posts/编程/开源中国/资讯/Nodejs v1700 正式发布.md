
---
title: 'Node.js v17.0.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7773'
author: 开源中国
comments: false
date: Thu, 21 Oct 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7773'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Node.js 是能够在服务器端运行 JavaScript 的开放源代码、跨平台 JavaScript 运行环境。Node.js 由Node.js Foundation（已与 JS Foundation 合并为 OpenJS Foundation）持有和维护，亦为 Linux 基金会的项目。Node.js 采用 Google 开发的 V8 运行代码，使用事件驱动、非阻塞和异步输入输出模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于资料密集的即时应用程序。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Node.js 17.0.0 正式发布，本次更新值得注意的变化包括：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用与移除</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<code>4b030d0573</code>] - <strong>doc</strong>: 在<span> </span><code>http</code><span> </span>中弃用<span> </span><code>.aborted</code><span> </span>属性和<span> </span><code>abort</code>、<span> </span><code>aborted</code><span> </span>事件 (doc-only) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F36670" target="_blank">#36670</a></li> 
 <li>[<code>36e2ffe6dc</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>module</strong>: 移除子路径文件夹映射 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40121" target="_blank">#40121</a></li> 
 <li>[<code>64287e4d45</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>module</strong>: 运行时弃用斜杠结尾（trailing slash）模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40117" target="_blank">#40117</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">OpenSSL 3.0</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Node.js 现在包含 OpenSSL 3.0，特别是提供 QUIC 支持的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fquictls%2Fopenssl" target="_blank">quictls/openssl</a>。在 OpenSSL 3.0 中，使用新的 FIPS 模块再次提供 FIPS 支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">虽然 OpenSSL 3.0 API 与 OpenSSL 1.1.1 提供的 API 基本兼容，但由于对允许的算法和密钥大小的严格限制，预计会对 Node.js 的生态产生一些影响。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">如果你在使用 Node.js 17 的应用程序中遇到<code>ERR_OSSL_EVP_UNSUPPORTED</code>错误，很可能是你的应用程序或正在使用的模块尝试使用 OpenSSL 3.0 默认不再允许的算法或密钥大小。开发者可以添加<code>--openssl-legacy-provider</code>命令行选项 ，作为这些收紧限制的临时解决方法以恢复应用程序。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">有关 OpenSSL 3.0 中所有功能的详细信息，请参阅<a href="https://www.oschina.net/news/159359/openssl-3-0-released">该链接</a>。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">V8 9.5</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">V8 JavaScript 引擎已经更新到 V8 9.5。该版本为<span> </span><code>Intl.DisplayNames</code><span> </span>API 提供了额外的支持类型，并在<span> </span><code>Intl.DateTimeFormat</code><span> </span>API 中扩展了<span> </span><code>timeZoneName</code><span> </span>选项。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Readline Promise API</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><code>readline</code><span> </span>模块提供了一个接口，用于从 Readable 流（如<span> </span><code>process.stdin</code>）中一次一行地读取数据。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">下面的简单例子说明了<span> </span><code>readline</code><span> </span>模块的基本用途。</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">import * as readline from 'node:readline/promises';
import &#123; stdin as input, stdout as output &#125; from 'process';

const rl = readline.createInterface(&#123; input, output &#125;);

const answer = await rl.question('What do you think of Node.js? ');

console.log(`Thank you for your valuable feedback: $&#123;answer&#125;`);

rl.close();
</pre> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他值得注意的变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<code>1b2749ecbe</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>dns</strong>: 在<span> </span><code>dns.lookup()</code><span> </span>中默认设置<span> </span><code>verbatim=true</code><span> </span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39987" target="_blank">#39987</a></li> 
 <li>[<code>59d3d542d6</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>errors</strong>: 在导致退出的关键异常上打印 Node.js 版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F38332" target="_blank">#38332</a></li> 
 <li>[<code>a35b7e0427</code>] - <strong>deps</strong>: 将 npm 升级到 8.1.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40463" target="_blank">#40463</a></li> 
 <li>[<code>6cd12be347</code>] - <strong>(SEMVER-MINOR)</strong> <strong>fs</strong>: 添加<span> </span><code>FileHandle.prototype.readableWebStream()</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39331" target="_blank">#39331</a></li> 
 <li>[<code>d0a898681f</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>lib</strong>: 添加<span> </span><code>structuredClone()</code><span> </span>全局方法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39759" target="_blank">#39759</a></li> 
 <li>[<code>e4b1fb5e64</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>lib</strong>: 公开 <code>DOMException</code> 为全局<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39176" target="_blank">#39176</a></li> 
 <li>[<code>0738a2b7bd</code>] - <strong>(SEMVER-MAJOR)</strong> <strong>stream</strong>: 在错误的流上完成也应该以错误的行为结束 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39235" target="_blank">#39235</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv17.0.0%2F" target="_blank">https://nodejs.org/en/blog/release/v17.0.0/</a></p>
                                        </div>
                                      
</div>
            