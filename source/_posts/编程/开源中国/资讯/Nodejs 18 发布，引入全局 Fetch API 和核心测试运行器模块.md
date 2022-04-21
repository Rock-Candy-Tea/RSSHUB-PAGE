
---
title: 'Node.js 18 发布，引入全局 Fetch API 和核心测试运行器模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4045'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4045'
---

<div>   
<div class="content">
                                                                                            <p>Node.js 18 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Fannouncements%2Fv18-release-announce%2F" target="_blank">已发布</a>，该版本的亮点包括将 V8 JavaScript 引擎更新到 10.1、默认启用全局 Fetch API 以及核心测试运行器模块。Node.js 18 是未来 6 个月的“当前”版本，然后在 2022 年 10 月升级为 LTS ，升级为  LTS 后将支持到 2025 年 4 月。</p> 
<h3><strong>新的浏览器兼容 API</strong></h3> 
<h4><span style="color:#333333"><strong>全局 Fetch API</strong></span><strong>（实验性）</strong></h4> 
<p>Node.js 18 默认提供一个实验性的全局 Fetch API，该实现来自 HTTP/1.1 客户端 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fundici.nodejs.org%2F%23%2F" target="_blank">undici</a> ，且受到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnode-fetch%2Fnode-fetch" target="_blank">node-fetch</a> 的启发。</p> 
<p>此 API 的示例用法：</p> 
<pre>const res = await fetch('https://nodejs.org/api/documentation.json');
if (res.ok) &#123;
  const data = await res.json();
  console.log(data);
&#125;</pre> 
<p>通过此添加，可以使用以下全局变量：<code>fetch</code>、 <code>FormData</code>、<code>Headers</code>、<code>Request</code>、<code>Response</code>。</p> 
<ul> 
 <li>可以通过 <code>--no-experimental-fetch</code> 命令行标志来禁用 API。</li> 
 <li>该 API 将保持实验性，直到添加更多测试覆盖率，且 API 实现了尽可能多的规范。</li> 
</ul> 
<h4>Web Streams API（实验性）</h4> 
<p>Node.js 现在在全局范围内公开了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStreams_API" target="_blank">Web Streams API 的实验性实现。</a>这意味着以下 API 可用：</p> 
<ul> 
 <li><code>ReadableStream</code>, <code>ReadableStreamDefaultReader</code>, <code>ReadableStreamBYOBReader</code>, <code>ReadableStreamBYOBRequest</code>, <code>ReadableByteStreamController</code>, <code>ReadableStreamDefaultController</code>, <code>TransformStream</code>, <code>TransformStreamDefaultController</code>, <code>WritableStream</code>, <code>WritableStreamDefaultWriter</code>, <code>WritableStreamDefaultController</code>, <code>ByteLengthQueuingStrategy</code>, <code>CountQueuingStrategy</code>, <code>TextEncoderStream</code>, <code>TextDecoderStream</code>, <code>CompressionStream</code>, <code>DecompressionStream</code>.</li> 
</ul> 
<h4>其他全局 API</h4> 
<p>此外，以下 API 现在在全局范围内公开：</p> 
<ul> 
 <li><code>Blob</code>- <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fapi%2Fbuffer.html%23class-blob" target="_blank">https://nodejs.org/api/buffer.html#class-blob</a></li> 
 <li><code>BroadcastChannel</code>- <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fapi%2Fworker_threads.html%23class-broadcastchannel-extends-eventtarget" target="_blank">https://nodejs.org/api/worker_threads.html#class-broadcastchannel-extends-eventtarget</a></li> 
</ul> 
<h3>测试运行器模块（实验性）</h3> 
<p>引入新的 <code>node:test</code> 模块，有助于创建以 TAP 格式报告结果的 JavaScript 测试。可通过 <code>import test from 'node:test';</code> 引入该模块。以下是具有两个子测试的父测试示例：</p> 
<pre>test('top level test', async (t) => &#123;
  await t.test('subtest 1', (t) => &#123;
    assert.strictEqual(1, 1);
  &#125;);

  await t.test('subtest 2', (t) => &#123;
    assert.strictEqual(2, 2);
  &#125;);
&#125;);</pre> 
<p>注意：测试运行器模块只能使用<code>node:</code>前缀，<code>node:</code>前缀表示加载核心模块，省略前缀并导入<code>'test'</code>会尝试加载用户区模块。</p> 
<p>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v18.x%2Fdocs%2Fapi%2Ftest.html" target="_blank">文档中阅读</a>该测试运行器的更多内容。</p> 
<h2>工具链和编译器升级</h2> 
<p>Node.js 为几个不同的平台提供了预构建的二进制文件。</p> 
<ul> 
 <li>Linux 的预构建二进制文件现在基于 Red Hat Enterprise Linux (RHEL) 8 构建，且与基于 glibc 2.28 或更高版本的 Linux 发行版兼容，例如 Debian 10、RHEL 8、Ubuntu 20.04。</li> 
 <li>macOS 的预构建二进制文件需要 macOS 10.15 或更高版本。</li> 
 <li>对于 AIX，支持的最低架构从 Power 7 提升到 Power 8。</li> 
 <li>由于在 Node.js 中构建 V8 依赖项的问题，用于 32 位 Windows 的预构建二进制文件将不可用。</li> 
</ul> 
<h2>V8 更新到  10.1</h2> 
<p>V8 引擎更新到 10.1 版本，该版本包括以下新功能：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Ffeatures%2Ffinding-in-arrays" target="_blank">findLast() 和 findLastIndex() 数组方法</a></li> 
 <li>对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-99%23intl.locale-extensions" target="_blank"><code>Intl.Locale</code> API</a> 的改进</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-99%23intl-enumeration" target="_blank"><code>Intl.supportedValuesOf</code></a> 函数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fv8%2Fissues%2Fdetail%3Fid%3D9888" target="_blank">类字段</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fv8%2Fissues%2Fdetail%3Fid%3D10793" target="_blank">私有类方法</a>的性能改进</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Fannouncements%2Fv18-release-announce%2F" target="_blank">更新公告</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Freleases%2Ftag%2Fv18.0.0" target="_blank">完整更新列表</a> | <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps+%3A%2F%2Fnodejs.org%2Fen%2Fdownload%2Fcurrent%2F" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            