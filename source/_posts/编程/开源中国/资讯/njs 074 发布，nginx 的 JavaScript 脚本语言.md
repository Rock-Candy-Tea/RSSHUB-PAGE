
---
title: 'njs 0.7.4 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9242'
author: 开源中国
comments: false
date: Fri, 27 May 2022 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9242'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">njs 0.7.4 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新版本下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>主要变化</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">nginx modules:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Feature: 添加用于配置 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23ngx_fetch" target="_blank">Fetch API</a> 的扩展指令。目前为 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html" target="_blank">http</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fstream%2Fngx_stream_js_module.html" target="_blank">stream</a> 添加了以下指令： 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_fetch_timeout" target="_blank">js_fetch_timeout</a>,</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_fetch_verify" target="_blank">js_fetch_verify</a>,</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_fetch_buffer_size" target="_blank">js_fetch_buffer_size</a>,</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_fetch_max_response_buffer_size" target="_blank">js_fetch_max_response_buffer_size</a>.</li> 
  </ul> </li> 
 <li>Change: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23r_internal_redirect" target="_blank"><code>r.internalRedirect()</code></a> 现已支持经过转义的 URI</li> 
 <li>Bugfix: 修复 Fetch API 中对超过 8 个 header 进行<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23response" target="_blank">响应解析</a>时出现的问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Core:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Feature: 添加<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23njs_version_number" target="_blank"><code>njs.version_number</code></a>属性</li> 
 <li>Feature: 为 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23builtin_crypto" target="_blank">WebCrypto API</a> 添加与 BoringSSL 的兼容性</li> 
 <li>Bugfix: 修复当 arr 大小在 comparator 中变更时，<code>Array.prototype.sort()</code>出现的错误</li> 
 <li>Bugfix: 使用缓慢<code>this</code>参数修复<code>Array.prototype.slice()</code>出现的错误</li> 
 <li>Bugfix: fixed aggregation methods of <code>Promise</code> ctor with array-like object.</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.7.4" target="_blank">详情</a>。</p>
                                        </div>
                                      
</div>
            