
---
title: 'Gawk 5.2.0 发布，Unix 数据_文本处理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9881'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9881'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p>awk 是一种编程语言，用于在 linux/unix下对文本和数据进行处理，且支持用户自定义函数和动态正则表达式等先进功能。Gawk 是 awk 的 GNU 版本，它提供了 Bell 实验室和 GNU 的一些扩展。</p> 
   <p>目前 Gawk 5.2.0 版本发布了，这版本带来如下改动：</p> 
   <ul> 
    <li>添加了内存管理器 pma  (Persistent Malloc) 的实验性支持，它允许在不同的 AWK 程序之间维护变量、数组和用户函数的值。</li> 
    <li>支持高精度算术，使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mpfr.org%2F" target="_blank">mpfr</a> 库实现。</li> 
    <li>更新了 Libtool 2.4.7 和 Bison 3.8.2 组件。</li> 
    <li>更改了数字比较的逻辑，使其符合 SI 语言中使用的逻辑。对于用户来说，主要影响 Infinity 和 Nan 与常数的比较。</li> 
    <li>在关联数组中使用 FNV1-A 散列函数，包括“FNV1A”中 AWK_HASH 变量的说明。</li> 
    <li>删除了使用 CMAKE 的程序集支持（CMAKE 支持代码没有需求，五年未更新）。</li> 
    <li>添加了 mkbool() 函数来创建布尔值，这些值是数字，但被处理为 Boolean 类型。</li> 
    <li>在 BWK 模式下，当指示标志是“--traditional”时，默认支持由 -r 选项包含的范围表达式（“--re-interval”）。</li> 
    <li>在 Rwarray的扩展中，提出了 Writeall() 和 Readall() 两个新函数，用于一次记录和读取所有变量和数组。</li> 
    <li>添加了 Gawkbug 脚本，以传输错误信息。。</li> 
    <li>移除对 OS/2 和 VAX/VMS 的支持，长期缺乏维护。</li> 
   </ul> 
   <p>更新邮件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.gnu.org%2Farchive%2Fhtml%2Fhelp-gawk%2F2022-09%2Fmsg00000.html" target="_blank">https://lists.gnu.org/archive/html/help-gawk/2022-09/msg00000.html</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            