
---
title: 'njs 0.7.6 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1667'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1667'
---

<div>   
<div class="content">
                                                                                            <p>njs 0.7.6 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p style="margin-left:0">作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p style="margin-left:0">新版本下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p style="margin-left:0"><strong>主要变化</strong></p> 
<p style="text-align:justify">nginx modules:</p> 
<ul> 
 <li style="text-align:justify">Feature: 优化<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23r_args" target="_blank"><code>r.args&#123;&#125;</code></a>对象。添加对具有相同 key 的多参数支持，并为 key 添加了区分大小写的功能，key 和值现在是百分比解码 (percent-decoded)</li> 
 <li style="text-align:justify">Bugfix: 修复<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23r_headers_out" target="_blank"><code>r.headersOut&#123;&#125;</code></a> setter 针对特殊 header 的处理</li> 
</ul> 
<p style="text-align:justify">Core:</p> 
<ul> 
 <li style="text-align:justify">Feature: 添加<code>Symbol.for()</code>和<code>Symbol.keyfor()</code></li> 
 <li style="text-align:justify">Feature: 添加来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhtml.spec.whatwg.org%2F" target="_blank">WHATWG</a> 规范的<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23atob" target="_blank"><code>atob()</code></a>和<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23btoa" target="_blank"><code>btoa()</code></a></li> 
 <li style="text-align:justify">Bugfix: 修复大型的非十进制字面量 (non-decimal literals)</li> 
 <li style="text-align:justify">Bugfix: 修复<code>parseInt()</code>中的 Unicode 参数修剪问题</li> 
 <li style="text-align:justify">Bugfix: 修复<code>try-catch</code>块中的<code>break</code>指令</li> 
 <li style="text-align:justify">Bugfix: 修复 CLI 中的<code>async</code>函数声明</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.7.6" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            