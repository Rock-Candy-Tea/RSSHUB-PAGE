
---
title: 'Boost 1.79.0 发布，可移植的 C++ 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9557'
author: 开源中国
comments: false
date: Tue, 19 Apr 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9557'
---

<div>   
<div class="content">
                                                                                            <p>Boost 是可移植的 C++ 库，目前包含了大约 160 种不同的函数库。</p> 
<p>此版本对以下的库进行了更新：Asio, Assert, Atomic, Beast, Core, Describe, Filesystem, Geometry, Integer, IO, Iterator, JSON, Log, Multi-index Containers, Nowide, Optional, Predef, Smart Pointers, System, ThrowException, Unordered, Variant2, Wave, LEAF, QVM。</p> 
<p><strong style="color:#000000"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Flibs%2Fasio%2F" target="_blank">Asio</a>:</strong></p> 
<ul style="margin-left:.25em; margin-right:0"> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   添加
   <code><span>bind_allocator</span></code>
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   添加
   <code><span>file_base</span><span>::</span><span>sync_all_on_write</span></code>flag
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   添加缺失的
   <code><span>basic_file</span><span>::</span><span>release</span><span>()</span></code>实现
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   为信号集添加对取消 per-operation 操作的支持
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   将
   <code><span>recycling_allocator</span></code>作为公开接口的一部分
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   为多项函数添加
   <code><span>nodiscard</span></code>属性
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   兼容 OpenSSL 3.0
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   增强文档
  </div> </li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   ……
  </div> </li> 
</ul> 
<p>另外，此版本存在一个已知的问题：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   Boost.JSON
   <span> </span>
   <code><span>array</span><span>::</span><span>erase</span></code>
   <span> </span>会出现 segfault 错误，详情查看 
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fboostorg%2Fjson%2Fissues%2F692" target="_blank">#692</a>.
   <span> </span>
   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Fpatches%2F1_79_0%2F0001-json-array-erase-relocate.patch" target="_blank">Patch</a>
  </div> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fboostorg.jfrog.io%2Fartifactory%2Fmain%2Frelease%2F1.79.0%2Fsource%2F" target="_blank">下载地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Fusers%2Fhistory%2Fversion_1_79_0.html" target="_blank">发布说明</a></p>
                                        </div>
                                      
</div>
            