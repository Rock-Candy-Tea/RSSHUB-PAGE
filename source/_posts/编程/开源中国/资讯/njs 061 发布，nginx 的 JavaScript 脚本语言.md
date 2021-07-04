
---
title: 'njs 0.6.1 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4050'
author: 开源中国
comments: false
date: Sun, 04 Jul 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4050'
---

<div>   
<div class="content">
                                                                    
                                                        <p>njs 0.6.1 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p>作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p>新版本下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p>此版本的更新内容主要是修复 bug：</p> 
<ul> 
 <li>Bugfix：修复<code>RegExpBuiltinExec()</code>使用 UTF-8 时仅支持正则表达式的问题</li> 
 <li>Bugfix：修复使用非赋值表达式解析导出默认声明的问题</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.6.1" target="_blank">详情查看 changelog</a>。</p>
                                        </div>
                                      
</div>
            