
---
title: 'njs 0.7.5 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4216'
author: 开源中国
comments: false
date: Thu, 23 Jun 2022 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4216'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">njs 0.7.5 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新版本下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Findex.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>主要变化</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">nginx modules:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Change: 遵循 nginx header 结构的变化</li> 
 <li>Bugfix: 修复当缺少值时，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Freference.html%23r_headers_out" target="_blank"><code>r.headersOut&#123;&#125;</code></a> 出现的特殊 getter</li> 
 <li>Change: 当 header 不存在时，为<code>Content-Type</code>返回未定义的值而不是空字符串。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Core:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Bugfix: 修复对 awaited 函数抛出异常的捕获</li> 
 <li>Bugfix: 修复函数值初始化</li> 
 <li>Bugfix: 修复当 await 无效时解释器出现的问题</li> 
 <li>Bugfix: 在迭代期间，当更改 source array 时修复类型化数组构造函数</li> 
 <li>Bugfix:使用字节字符串修复 <code>String.prototype.replace()</code></li> 
 <li>Bugfix: <span style="color:#000000">修复生成字节字符串的模板字面量</span></li> 
 <li>Bugfix: 修复稀疏数组的数组迭代器</li> 
 <li>Bugfix: <span style="color:#000000">在将平面数组转换为 slow 数组时修复可用内存</span></li> 
 <li>Bugfix: properly handling <code>NJS_DECLINE</code> in <code>promise</code> native functions.</li> 
 <li>在<code>promise</code>原生函数中正确处理<code>NJS_DECLINE</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.7.5" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            