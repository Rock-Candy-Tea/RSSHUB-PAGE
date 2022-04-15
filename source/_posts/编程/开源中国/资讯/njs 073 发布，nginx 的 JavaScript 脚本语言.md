
---
title: 'njs 0.7.3 发布，nginx 的 JavaScript 脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9743'
author: 开源中国
comments: false
date: Fri, 15 Apr 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9743'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">njs 0.7.3 已发布，njs 以 nginx 插件的方式存在，它是 JavaScript/ECMAscript 的子集，实现了大部分的 JavaScript 语言功能，没有完全遵从 ECMAScript 标准，同时抛弃了 JavaScript 比较难懂的部分。njs 不通过 V8 引擎实现，而是通过一个更小、能耗更低、更符合 nginx 应用场景的小虚拟机实现，可以理解成 nginx 为其实现了一套自己的词法解析。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">作为 nginx 的插件，njs 的安装方式是重新编译 nginx。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新版本下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Finstall.html" target="_blank">http://nginx.org/en/docs/njs/install.html</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>主要变化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Feature: 添加对模块解析回调的支持，该功能可用于让主机环境控制导入模块的加载方式</li> 
 <li>Bugfix: 修复在遍历导入的用户模块时的回溯问题</li> 
 <li>Bugfix: 修复当<code>this</code> 是慢数组时，<code>Array.prototype.concat()</code>出现的错误</li> 
 <li>Bugfix: 修复从 awaited frame 中分配 frame 的问题</li> 
 <li>Bugfix: 修复大型数组字面量的分配问题</li> 
 <li>Bugfix: 修复当<code>toString</code>转换失败时解释器出现错误的问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnginx.org%2Fen%2Fdocs%2Fnjs%2Fchanges.html%23njs0.7.3" target="_blank">详情查看 Changelog</a>。</p>
                                        </div>
                                      
</div>
            