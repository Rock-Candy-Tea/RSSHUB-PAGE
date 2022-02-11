
---
title: 'Nim 1.6.4 发布，修复 1.6.2 引入的 C FFI 回归'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8722'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8722'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p>Nim 1.6.4 发布了，该版本包含 33 次提交，最重要的修复是针对 1.6.2 中引入的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19342" target="_blank">C FFI 回归。</a>，并在<a href="https://www.oschina.net/news/174465/nim-1-6-2-released"> 1.6.2 版本</a>的基础上带来了一些总体改进。</p> 
  <h2 style="margin-left:0px">Bug修复</h2> 
  <ul> 
   <li>修复了“潜在的 C FFI 回归”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19342" target="_blank">#19342</a>）</li> 
   <li>修复了“re.split 使用零宽度字符的意外结果”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F14468" target="_blank">#14468</a>）</li> 
   <li>修复了“strformat 越界”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19107" target="_blank">#19107</a>）</li> 
   <li>修复了“将空列表添加到非空列表，会破坏后一个列表”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19297" target="_blank">#19297</a>）</li> 
   <li>修复了“使用带有 var 参数的 varargs 时的错误结果”。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F16617" target="_blank">#16617</a> )</li> 
   <li>修复了“将空的 <code>DoublyLinkedList</code> 添加到非空的 <code>DoublyLinkedList</code>，会破坏后一个列表”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19314" target="_blank">#19314</a>）</li> 
   <li>修复了“使用 gc:orc 在对象内部传递数组时，出现静默 FFI 错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19497" target="_blank">#19497</a>）</li> 
   <li>更多更改可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fcompare%2Fv1.6.2...v1.6.4" target="_blank">点此查看</a></li> 
  </ul> 
  <p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnim-lang.org%2Fblog%2F2022%2F02%2F08%2Fversion-164-released.html" target="_blank">https://nim-lang.org/blog/2022/02/08/version-164-released.html</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            