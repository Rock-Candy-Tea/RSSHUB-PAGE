
---
title: '通过 Apifox Echo 学习 curl_httpie 命令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1616e471094467ba9c3745010e5f1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 19:31:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1616e471094467ba9c3745010e5f1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>curl</code>，用于发送请求的命令行工具，一个 HTTP 请求客户端（实际上它也可以做 FTP/SCP/TELNET 协议的事情，可类比于浏览器中的 fetch。</p>
<p><code>curl</code> 是最为流行的 HTTP 请求命令行工具，在谷歌浏览器控制台的网络面板中，可将当前请求转化为 <code>curl</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1616e471094467ba9c3745010e5f1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在学习及调试 HTTP 的过程中，可结合 <code>curl</code> 与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fecho.apifox.com" target="_blank" rel="nofollow noopener noreferrer" title="https://echo.apifox.com" ref="nofollow noopener noreferrer">Apifo Echo</a> 一同使用。</p>
<p><code>Apifox Echo</code> 是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapifox.cn%2Fa1shanyue" target="_blank" rel="nofollow noopener noreferrer" title="https://apifox.cn/a1shanyue" ref="nofollow noopener noreferrer">Apifox</a> 出品的一款 HTTP 简单的接口请求和返回数据服务，可以模拟各种接口请求参数和返回数据的情况，供开发人员和测试人员学习测试 API 使用。</p>
<h2 data-id="heading-0">curl</h2>
<p>直接发送 GET 请求：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl ifconfig.me
118.73.227.215
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">curl --request</h2>
<p><code>--request/-X</code>，指定请求方法，如 <code>POST</code> 等。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl \
  -X POST \
  -H <span class="hljs-string">"Accept: application/vnd.github+json"</span> \ 
  -H <span class="hljs-string">"Authorization: token <TOKEN>"</span> \
  https://api.github.com/repos/OWNER/REPO/issues \
  -d <span class="hljs-string">'&#123;"title":"Found a bug","body":"I'</span>\<span class="hljs-string">''</span>m having a problem with this.<span class="hljs-string">","</span>assignees<span class="hljs-string">":["</span>octocat<span class="hljs-string">"],"</span>milestone<span class="hljs-string">":1,"</span>labels<span class="hljs-string">":["</span>bug<span class="hljs-string">"]&#125;'

$ curl https://echo.apifox.com/post -X POST -H "</span>a: 3<span class="hljs-string">" -H "</span>b: 4<span class="hljs-string">"
&#123;
  "</span>args<span class="hljs-string">": &#123;&#125;, 
  "</span>data<span class="hljs-string">": "</span><span class="hljs-string">", 
  "</span>files<span class="hljs-string">": &#123;&#125;, 
  "</span>form<span class="hljs-string">": &#123;&#125;, 
  "</span>headers<span class="hljs-string">": &#123;
    "</span>A<span class="hljs-string">": "</span>3<span class="hljs-string">", 
    "</span>Accept<span class="hljs-string">": "</span>*/*<span class="hljs-string">", 
    "</span>B<span class="hljs-string">": "</span>4<span class="hljs-string">", 
    "</span>Connection<span class="hljs-string">": "</span>close<span class="hljs-string">", 
    "</span>Host<span class="hljs-string">": "</span>echo.apifox.com<span class="hljs-string">", 
    "</span>User-Agent<span class="hljs-string">": "</span>curl/7.79.1<span class="hljs-string">"
  &#125;, 
  "</span>json<span class="hljs-string">": null, 
  "</span>origin<span class="hljs-string">": "</span>118.113.0.137<span class="hljs-string">", 
  "</span>url<span class="hljs-string">": "</span>https://echo.apifox.com/post<span class="hljs-string">"
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">curl --head</h2>
<p><code>--head/-I</code> 发送 HEAD 请求，只需要返回 Response Header。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl --<span class="hljs-built_in">head</span> https://shanyue.tech
HTTP/2 200
server: Tengine
content-type: text/html; charset=utf-8
content-length: 33229
vary: Accept-Encoding
<span class="hljs-built_in">date</span>: Tue, 21 Jun 2022 05:54:24 GMT
vary: Accept-Encoding
x-oss-request-id: 62B15D1050ED1C32320FE906
x-oss-cdn-auth: success
accept-ranges: bytes
etag: <span class="hljs-string">"F540C0D57CDB57215AF11970EF4AAEF6"</span>
last-modified: Wed, 23 Mar 2022 14:57:44 GMT
x-oss-object-type: Normal
x-oss-hash-crc64ecma: 8545542358272103335
x-oss-storage-class: Standard
x-oss-meta-mtime: 1648047444.796073379
cache-control: no-cache
content-md5: 9UDA1XzbVyFa8Rlw70qu9g==
x-oss-server-time: 27
ali-swift-global-savetime: 1655790864
via: cache12.l2cn3051[290,290,200-0,M], cache4.l2cn3051[291,0], kunlun6.cn3145[383,382,200-0,M], kunlun3.cn3145[386,0]
x-cache: MISS TCP_MISS dirn:-2:-2
x-swift-savetime: Tue, 21 Jun 2022 05:54:24 GMT
x-swift-cachetime: 0
timing-allow-origin: *
eagleid: 791d26a916557908641262834e
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">curl --include</h2>
<p><code>--include/-i</code>，打印 Response Header 与 Response Body。</p>
<pre><code class="hljs language-bash copyable" lang="bash">HTTP/1.1 200 OK
access-control-allow-origin: *
content-type: text/plain; charset=utf-8
content-length: 15
<span class="hljs-built_in">date</span>: Wed, 17 Aug 2022 01:56:20 GMT
x-envoy-upstream-service-time: 1
strict-transport-security: max-age=2592000; includeSubDomains
server: istio-envoy
Via: 1.1 google

222.222.222.113%
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">curl --verbose</h2>
<p><code>--verbose/-v</code>，查看发送报文及 TLS handshake 的详细。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl -vvv --<span class="hljs-built_in">head</span> https://shanyue.tech
* Rebuilt URL to: https://shanyue.tech/
*   Trying 218.91.183.88...
* TCP_NODELAY <span class="hljs-built_in">set</span>
* Connected to shanyue.tech (218.91.183.88) port 443 (<span class="hljs-comment">#0)</span>
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully <span class="hljs-built_in">set</span> certificate verify locations:
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt
  CApath: none
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, [no content] (0):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=shanyue.tech
*  start <span class="hljs-built_in">date</span>: Feb  5 00:00:00 2022 GMT
*  expire <span class="hljs-built_in">date</span>: Feb  6 23:59:59 2023 GMT
*  subjectAltName: host <span class="hljs-string">"shanyue.tech"</span> matched cert<span class="hljs-string">'s "shanyue.tech"
*  issuer: C=US; O=DigiCert Inc; OU=www.digicert.com; CN=Encryption Everywhere DV TLS CA - G1
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* TLSv1.3 (OUT), TLS app data, [no content] (0):
* TLSv1.3 (OUT), TLS app data, [no content] (0):
* TLSv1.3 (OUT), TLS app data, [no content] (0):
* Using Stream ID: 1 (easy handle 0x55c5a8e24690)
* TLSv1.3 (OUT), TLS app data, [no content] (0):
> HEAD / HTTP/2
> Host: shanyue.tech
> User-Agent: curl/7.61.1
> Accept: */*
>
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, [no content] (0):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS app data, [no content] (0):
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
* TLSv1.3 (OUT), TLS app data, [no content] (0):
* TLSv1.3 (IN), TLS app data, [no content] (0):
< HTTP/2 200
HTTP/2 200
< server: Tengine
server: Tengine
< content-type: text/html; charset=utf-8
content-type: text/html; charset=utf-8
< content-length: 33229
content-length: 33229
< vary: Accept-Encoding
vary: Accept-Encoding
< date: Tue, 21 Jun 2022 06:02:59 GMT
date: Tue, 21 Jun 2022 06:02:59 GMT
< vary: Accept-Encoding
vary: Accept-Encoding
< x-oss-request-id: 62B15F13F15BB231391FB3A8
x-oss-request-id: 62B15F13F15BB231391FB3A8
< x-oss-cdn-auth: success
x-oss-cdn-auth: success
< accept-ranges: bytes
accept-ranges: bytes
< etag: "F540C0D57CDB57215AF11970EF4AAEF6"
etag: "F540C0D57CDB57215AF11970EF4AAEF6"
< last-modified: Wed, 23 Mar 2022 14:57:44 GMT
last-modified: Wed, 23 Mar 2022 14:57:44 GMT
< x-oss-object-type: Normal
x-oss-object-type: Normal
< x-oss-hash-crc64ecma: 8545542358272103335
x-oss-hash-crc64ecma: 8545542358272103335
< x-oss-storage-class: Standard
x-oss-storage-class: Standard
< x-oss-meta-mtime: 1648047444.796073379
x-oss-meta-mtime: 1648047444.796073379
< cache-control: no-cache
cache-control: no-cache
< content-md5: 9UDA1XzbVyFa8Rlw70qu9g==
content-md5: 9UDA1XzbVyFa8Rlw70qu9g==
< x-oss-server-time: 3
x-oss-server-time: 3
< ali-swift-global-savetime: 1655791379
ali-swift-global-savetime: 1655791379
< via: cache24.l2et15-1[66,66,200-0,M], cache44.l2et15-1[67,0], cache27.cn4056[128,128,200-0,M], cache64.cn4056[130,0]
via: cache24.l2et15-1[66,66,200-0,M], cache44.l2et15-1[67,0], cache27.cn4056[128,128,200-0,M], cache64.cn4056[130,0]
< x-cache: MISS TCP_MISS dirn:-2:-2
x-cache: MISS TCP_MISS dirn:-2:-2
< x-swift-savetime: Tue, 21 Jun 2022 06:02:59 GMT
x-swift-savetime: Tue, 21 Jun 2022 06:02:59 GMT
< x-swift-cachetime: 0
x-swift-cachetime: 0
< timing-allow-origin: *
timing-allow-origin: *
< eagleid: 088432cc16557913793393217e
eagleid: 088432cc16557913793393217e

<
* Connection #0 to host shanyue.tech left intact
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">curl --location</h2>
<p><code>--location/-L</code>，追踪重定向。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 重定向两次后请求到数据</span>
$ curl --location http://zhihu.com

<span class="hljs-comment"># 可使用 --head，查看到三次响应</span>
$ curl --<span class="hljs-built_in">head</span> --location http://zhihu.com
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">httpie && examples</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fhttpie.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://httpie.io/" ref="nofollow noopener noreferrer">httpie</a> 是现代化更为流行的一个 HTTP 客户端，支持色彩、JSON 等。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 发送 JSON 数据给服务器端，httpie 比 curl 方便很多，不需要自己手写 header，curl 默认为 application/x-www-form-urlencoded</span>
$ http POST https://echo.apifox.com/post <span class="hljs-string">"a: 3"</span> name=shanyue
$ curl -X POST https://echo.apifox.com/post -H <span class="hljs-string">"a: 3"</span> -H <span class="hljs-string">"content-type: application/json"</span> -d <span class="hljs-string">'&#123;"name": "shanyue"&#125;'</span>

<span class="hljs-comment"># 发送 Form 数据给服务器端，curl/httpie 都比较方便</span>
$ http POST https://echo.apifox.com/post <span class="hljs-string">"a: 3"</span> name=shanyue
$ curl -X POST https://echo.apifox.com/post -H <span class="hljs-string">"a: 3"</span> -d name=shanyue

<span class="hljs-comment"># 上传文件</span>
$ http POST https://echo.apifox.com/post < Readme.md
$ curl -X POST https://echo.apifox.com/post -H <span class="hljs-string">"content-type: application/json"</span> -d @Readme.md

<span class="hljs-comment"># multipart 上传文件</span>
$ http --multipart https://echo.apifox.com/post a=3 b@<span class="hljs-string">'Readme.md'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apifox.cn%2Fa1shanyue" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apifox.cn/a1shanyue" ref="nofollow noopener noreferrer">Apifox Echo</a> 中，还可以将请求直接转化为命令行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aacb5b2a07464b37b4932ebce2c07e52~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">作业</h2>
<ol>
<li>curl/httpie 如何发送一个 GET 请求</li>
<li>curl/httpie 如何发送 JSON 数据给服务器端</li>
<li>curl/httpie 如何发送 FORM 数据给服务器端</li>
<li>curl/httpie 如何追踪重定向路径</li>
<li>curl/httpie 如何仅返回 Response Header</li>
</ol></div>  
</div>
            