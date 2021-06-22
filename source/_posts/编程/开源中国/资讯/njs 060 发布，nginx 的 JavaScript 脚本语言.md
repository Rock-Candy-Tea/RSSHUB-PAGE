
---
title: 'njs 0.6.0 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2071'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 06:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2071'
---

<div>   
<div class="content">
                                                                    
                                                        <p>njs 0.6.0 已发布，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Findex.html" target="_blank">njs</a> 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解为 nginx 为其实现了一套自己的词法解析。</p> 
<p>作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>添加了 let 和 const 声明支持</li> 
 <li>添加 RegExp.prototype[Symbol.split]</li> 
 <li>添加了对 RegExp 的粘性标志支持</li> 
 <li>修复了 String.prototype.lastIndexOf() 中的堆缓冲区溢出</li> 
 <li>根据规范修复 RegExp.prototype.test()</li> 
 <li>根据规范修复 String.prototype.split() </li> 
 <li>在跟踪被拒绝的 promise 时修复了未初始化值的使用</li> 
 <li>修复了具有循环引用对象的 njs.dump()</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.6.0" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            