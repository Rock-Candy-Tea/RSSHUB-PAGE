
---
title: 'njs 0.7.7 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2415'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2415'
---

<div>   
<div class="content">
                                                                                            <p>njs 0.7.7 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p>作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p>新版本下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p><strong>主要变化</strong></p> 
<p style="color:#000000; text-align:justify"><strong>nginx modules:</strong></p> 
<ul> 
 <li style="text-align:justify"> <p style="text-align:justify">Feature: 扩展了可以指定 js 指令的 nginx 配置上下文的数量</p> 
  <ul> 
   <li style="text-align:justify"> <p style="text-align:justify">HTTP: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_import" target="_blank">js_import</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_path" target="_blank">js_path</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_set" target="_blank">js_set</a>和<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_var" target="_blank">js_var</a>指令支持在<code>server</code>和<code>location</code><span> 上下文中使用。</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_content" target="_blank">js_content</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_body_filter" target="_blank">js_body_filter</a><span> 和</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_header_filter" target="_blank">js_header_filter</a><span> 指令支持在</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_rewrite_module.html%23if" target="_blank">if</a><span> 上下文中使用</span></p> </li> 
   <li style="text-align:justify"> <p style="text-align:justify">Stream: the<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_import" target="_blank">js_import</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_path" target="_blank">js_path</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_set" target="_blank">js_set</a> 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fhttp%2Fngx_http_js_module.html%23js_var" target="_blank">js_var</a><span> 支持在</span><span> </span><code>server</code><span> </span>上下文中使用</p> </li> 
  </ul> </li> 
 <li style="text-align:justify"> <p style="text-align:justify">Feature: 添加<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23r_internal" target="_blank"><code>r.internal</code></a>属性</p> </li> 
 <li style="text-align:justify"> <p style="text-align:justify">Bugfix: <span>修复在 </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23ngx_fetch" target="_blank">Fetch API</a> 中读取 response body 的问题</p> </li> 
 <li style="text-align:justify"> <p style="text-align:justify">Bugfix: <span>修复 </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fstream%2Fngx_stream_js_module.html" target="_blank">stream</a> 中的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fstream%2Fngx_stream_js_module.html%23js_fetch_timeout" target="_blank">js_fetch_timeout</a> 问题</p> </li> 
 <li style="text-align:justify"> <p style="text-align:justify">Bugfix: 修复<span> </span><code>0</code><span> </span>fetch timeout 的 socket 泄露问题</p> </li> 
</ul> 
<p style="color:#000000; text-align:justify"><strong>Core:</strong></p> 
<ul> 
 <li style="text-align:justify"> <p style="text-align:justify">Feature:扩展<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23njs_api_fs" target="_blank"><code>fs</code></a>模块。添加<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_opensync" target="_blank"><code>fs.openSync()</code></a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_promises_open" target="_blank"><code>fs.promises.open()</code></a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_fstatsync" target="_blank"><code>fs.fstatSync()</code></a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_readsync" target="_blank"><code>fs.readSync()</code></a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_writesync_buf" target="_blank"><code>fs.writeSync()</code></a></p> <p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23fs_filehandle" target="_blank"><code>FileHandle</code></a><span>实现了以下属性：</span><code>fd</code>,<span> </span><code>read()</code>,<span> </span><code>stat()</code>,<span> </span><code>write()</code>,<span> </span><code>close()</code></p> </li> 
 <li style="text-align:justify"> <p style="text-align:justify">Bugfix: 修复<code>parseInt()</code>,<span> </span><code>parseFloat()</code>,<span> </span><code>Symbol.for()</code><span>没有参数的问题</span></p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.7.7" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            