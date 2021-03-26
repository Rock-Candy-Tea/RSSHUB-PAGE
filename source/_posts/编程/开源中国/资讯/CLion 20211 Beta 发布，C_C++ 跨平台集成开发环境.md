
---
title: 'CLion 2021.1 Beta 发布，C_C++ 跨平台集成开发环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0326/070744_EX7d_4937141.png'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 07:14:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0326/070744_EX7d_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>CLion 2021.1 Beta 已正式发布，新版本修复了项目模型和更多的 MISRA 检查。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2021/0326/070744_EX7d_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>对于 Makefile 项目 
  <ul> 
   <li>更新 Makefile 项目所使用的工具链会触发项目的重新加载</li> 
   <li>提取大量项目的 make target 现在可以正常工作了</li> 
   <li>对于使用 MinGW 工具链的 Makefile 项目，CLion 现在可以在加载项目时正确处理带 "\" 和 "/" 的目录</li> 
  </ul> </li> 
 <li>对于汇编数据库项目 
  <ul> 
   <li>Clang-cl 现在支持此类项目</li> 
  </ul> </li> 
 <li>新的 MISRA C 和 C++ 检查 
  <ul> 
   <li>异常对象不应具有指针类型</li> 
   <li>一些新的检查现在禁止使用特定的库函数，例如 stdlib.h 的 bsearch 和 qsort，ctime 库的时间处理函数，或者 cstdlib 库的 atof、atoi 和 atol</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fclion%2F2021%2F03%2Fclion-2021-1-goes-beta%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            