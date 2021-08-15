
---
title: 'Deno 1.13 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9759'
author: 开源中国
comments: false
date: Sun, 15 Aug 2021 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9759'
---

<div>   
<div class="content">
                                                                                            <p>Deno 1.13 稳定版已发布，主要包含以下新特性和变更：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23stabilize-native-http-server-api" target="_blank">原生 HTTP server API 到达稳定状态</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23support-for-self.structuredclone%28%29" target="_blank">支持 <code>self.structuredClone()</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23use-system-certificate-store-for-tls" target="_blank">针对 TLS 使用系统证书存储 (system certificate store)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23disable-tls-verification" target="_blank">支持禁用 TLS 验证以进行测试</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23updates-to-webcrypto-apis" target="_blank">升级 WebCrypto APIs</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23updates-to-the-deno-language-server-and-vscode-extension" target="_blank">升级 Deno 语言服务器和 VSCode 扩展</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23improvements-to-the-repl" target="_blank">改进 REPL</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23support-for-navigator.hardwareconcurrency-api" target="_blank">支持 navigator.hardwareConcurrency API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23v8-9.3" target="_blank">升级 V8 至 9.3</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23type-references-in-deno-info" target="_blank">在 deno info 中使用类型引用(Type references)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23abortsignal-support-in-writefile" target="_blank">在 writeFile 中提供 AbortSignal 支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23type-check-code-examples-in-markdown-files" target="_blank">在 Markdown 文件添加类型检测的代码示例</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23spawn-subprocess-with-clean-enviroment" target="_blank">使用干净的环境生成子进程</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23permissions-apis-accept-urls" target="_blank">Permissions APIs 支持接受 URLs</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23experimental-ffi-replaces-native-plugin-system" target="_blank">使用 FFI 替换原生插件系统</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13%23experimental-websocketstream-api" target="_blank">新增实验性的 WebSocketStream API</a></li> 
</ul> 
<p><strong>原生 HTTP server API</strong></p> 
<p>原生 HTTP server API 在此版本中已进入稳定阶段，可有效地为 HTTP/1.1 和 HTTP/2 流量提供服务：</p> 
<pre>for await (const conn of Deno.listen(&#123; port: 4500 &#125;)) &#123;
  (async () => &#123;
    for await (const &#123; respondWith &#125; of Deno.serveHttp(conn)) &#123;
      respondWith(new Response("Hello World"));
    &#125;
  &#125;)();
&#125;</pre> 
<p><strong>支持</strong><code><strong>self.structuredClone()</strong></code></p> 
<p><code>self.structuredClone()</code>以简单、常用且同步的 API 公开了用于在 Web Worker 和 MessagePort 之间传递消息的结构化克隆算法。</p> 
<pre>import &#123; assert &#125; from "https://deno.land/std@0.104.0/testing/asserts.ts";

// Create an object with a value and a circular reference to itself.
const foo = &#123; bar: "baz" &#125;;
foo.foo = foo;

// Clone it
const clone = self.structuredClone(foo);

assert(clone !== foo); // assert they are not the same object
assert(clone.bar === "baz"); // assert they  do have the same value though
assert(clone.foo === clone); // assert that the circular reference is preserved

console.log("All assertions passed!");</pre> 
<p>尝试使用：</p> 
<pre>deno run https://deno.com/v1.13/structured_clone.js</pre> 
<p><strong>升级 WebCrypto APIs</strong></p> 
<p>此版本为<code>WebCrypto</code> APIs 增加了部分功能：</p> 
<ul> 
 <li><code>crypto.subtle.importKey()</code>和<code>crypto.subtle.exportKey()</code>支持导入和导出原始 HMAC 密钥</li> 
 <li><code>crypto.subtle.verify()</code>支持验证从 HMAC 密钥创建的签名</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.13" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            