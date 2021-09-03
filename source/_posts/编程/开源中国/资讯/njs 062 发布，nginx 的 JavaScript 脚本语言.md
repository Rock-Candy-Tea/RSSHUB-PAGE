
---
title: 'njs 0.6.2 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7987'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7987'
---

<div>   
<div class="content">
                                                                                            <p>njs 0.6.2 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p>作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p>新版本下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p>此版本主要更新内容：</p> 
<p>nginx modules:</p> 
<ul> 
 <li> <p>Bugfix: 修复<code>js_filter</code>双向注册时 CPU 被占用的问题</p> </li> 
</ul> 
<p>Core:</p> 
<ul> 
 <li> <p>Feature: 引入<code>AggregateError</code>实现</p> </li> 
 <li> <p>Feature: 添加其他的<code>Promise</code>构造函数方法，添加了以下方法：<code>Promise.all()</code> , <code>Promise.allSettled()</code> , <code>Promise.any()</code> , <code>Promise.race()</code> .</p> </li> 
 <li> <p>Improvement: 从代码生成器中删除递归 (recursion)</p> </li> 
 <li> <p>Bugfix: 修复其余参数解析没有绑定标识符的问题</p> </li> 
 <li> <p>Bugfix: 修复 resolve/reject 对<code>Promise.prototype.finally()</code>的回调</p> </li> 
 <li> <p>Bugfix: 修复<code>%TypedArray%.prototype.join()</code>与分离缓冲区的问题</p> </li> 
 <li> <p>Bugfix: 修复交互式 shell 中的内存泄漏问题</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.6.2" target="_blank">详情查看 Changelog</a>。</p>
                                        </div>
                                      
</div>
            