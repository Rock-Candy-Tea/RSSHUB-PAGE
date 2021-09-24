
---
title: 'Deno 1.14 正式发布，引入新的 Web Crypto API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8266'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8266'
---

<div>   
<div class="content">
                                                                                            <p>Deno 1.14 已发布，包括以下新特性和变更：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23web-crypto-api-additions" target="_blank">引入新的 Web Crypto API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23customization-options-for-deno-lint-and-deno-fmt" target="_blank"><span>增加针对</span><code>deno lint</code><span> </span>和<span> </span><code>deno fmt</code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23customization-options-for-deno-lint-and-deno-fmt" target="_blank">的自定义选项</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23urlpattern" target="_blank">引入 URLPattern</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23stabilization-of-native-server-side-websocket-api" target="_blank">原生服务器端 WebSocket API 进入稳定状态</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23zero-copy-arraybuffer-transfers-between-workers" target="_blank">worker 之间的零拷贝 ArrayBuffer 传输</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23file-locking-apis" target="_blank">引入 File locking API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23changes-to-os-signals-apis" target="_blank">对 OS signals API 的更改</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23mutual-tls-support-in-fetch" target="_blank">在<span> </span><code>fetch</code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23mutual-tls-support-in-fetch" target="_blank">中提供 Mutual TLS 支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23basic-auth-support-in-deno_auth_tokens" target="_blank"><span>在</span><code>DENO_AUTH_TOKENS</code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23basic-auth-support-in-deno_auth_tokens" target="_blank">中提供基本身份验证支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23url-parsing-is-now-3x-faster" target="_blank">URL 解析速度提升了 3 倍</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23gid-and-uid-can-now-be-specified-for-subprocesses" target="_blank">支持为子进程指定<code>gid</code><span> </span>和<span> </span><code>uid</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23much-faster-std%252Fhttp-module" target="_blank">更快的<span> </span><code>std/http</code><span> 模块</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23updates-to-vscode-extension" target="_blank">更新 VSCode 扩展</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23typescript-4.4" target="_blank">TypeScript 4.4</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23v8-9.4" target="_blank">V8 9.4</a></li> 
</ul> 
<hr> 
<h3 style="margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23web-crypto-api-additions" target="_blank">引入新的 Web Crypto API</a></h3> 
<p>此版本引入了许多新的 Web Crypto API：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>crypto.subtle.exportKey()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>HMAC 密钥现在支持以 JWK 和<span style="color:#24292e">"raw"</span>格式导出</li> 
   <li>RSA 密钥现在支持以 pkcs#8 格式导出</li> 
  </ul> </li> 
 <li><code>crypto.subtle.importKey()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>HMAC 密钥现在可以以 JWK 和<span style="color:#24292e">"raw"</span>格式导入</li> 
   <li>现在支持以 pkcs#8 格式导入 RSA 密钥</li> 
   <li>PBKDF2 密钥现在支持以"raw"格式导入</li> 
  </ul> </li> 
 <li><code>crypto.subtle.generateKey()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>现在支持生成 RSA-OAEP 密钥</li> 
   <li>现在支持生成 ECDH 密钥</li> 
   <li>现在支持生成 AES 密钥</li> 
  </ul> </li> 
 <li><code>crypto.subtle.deriveBits()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>现在支持 PBKDF2 派生</li> 
   <li>现在支持 HKDF 派生</li> 
  </ul> </li> 
 <li><code>crypto.subtle.verify()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>现在支持 ECDSA 签名验证</li> 
  </ul> </li> 
 <li><code>crypto.subtle.encrypt()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>现在支持 RSA-OAEP 加密</li> 
  </ul> </li> 
 <li><code>crypto.subtle.decrypt()</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>现在支持 RSA-OAEP 解密</li> 
  </ul> </li> 
</ul> 
<hr> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23urlpattern" target="_blank">引入 URLPattern</a></h3> 
<p>此版本引入了一个新的不稳定的 Web 平台 API，用于根据模式匹配 URL。<code>URLPattern</code>是流行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpillarjs%2Fpath-to-regexp" target="_blank"><code>path-to-regexp</code></a>库的内置替代品 。</p> 
<pre><code class="language-javascript">const pattern = new URLPattern(&#123; pathname: "/books/:id" &#125;);

console.log(pattern.test("https://example.com/books/123")); // true
console.log(pattern.test("https://example.com/books/123/456")); // false
console.log(pattern.test("https://example.com/books")); // false

console.log(pattern.exec("https://example.com/books/123").pathname); // &#123; input: "/books/123", groups: &#123; id: "123" &#125; &#125;</code></pre> 
<hr> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23file-locking-apis" target="_blank">引入 File locking API</a></h3> 
<p style="margin-left:0; margin-right:0; text-align:start">此版本引入了四个新的可用于文件锁定的不稳定 API：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Deno.flock</code></li> 
 <li><code>Deno.flockSync</code></li> 
 <li><code>Deno.funlock</code></li> 
 <li><code>Deno.funlockSync</code></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start">这些 API 对于像<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.land%2Fx%2Fsqlite%40v3.1.1" target="_blank"><code>sqlite</code></a>提供适当的数据库同步这种项目来说是必不可少的 。</p> 
<hr> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14%23much-faster-std%252Fhttp-module" target="_blank">更快的<span> </span><code>std/http</code><span> 模块</span></a></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno_std" target="_blank">Deno 标准库</a> 0.107.0 版本对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.land%2Fstd%400.107.0%2Fhttp" target="_blank"><code>http</code>模块</a>进行了重大改进 。</p> 
<p style="margin-left:0; margin-right:0; text-align:start">在 v1.13 中原生 HTTP server API 到达稳定状态后，团队重写了<code>http/server.ts</code>模块，并使用了新的稳定 API。最终实现了显著的性能提升，以及创建了对用户更友好的 API——主要用于处理 HTTP 服务器的问题，例如错误处理和连接的多路复用。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.14" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            