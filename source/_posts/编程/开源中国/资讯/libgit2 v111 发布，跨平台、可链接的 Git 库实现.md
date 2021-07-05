
---
title: 'libgit2 v1.1.1 发布，跨平台、可链接的 Git 库实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9910'
author: 开源中国
comments: false
date: Mon, 05 Jul 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9910'
---

<div>   
<div class="content">
                                                                    
                                                        <p>libgit2 是一个可以在应用程序中使用的跨平台、可链接的 Git 库实现。libgit2 1.1.1 版本是一个错误修复版本，该版本的更新内容如下：</p> 
<ul> 
 <li>修复了在少数情况下解压包文件可能失败的错误；</li> 
 <li>确保工作树路径在更多情况下得到验证；</li> 
 <li>再次支持没有 thread-safety 的构建（ <code>THREADSAFE=OFF</code>）；</li> 
 <li>再次支持没有 mmap ( <code>NO_MMAP</code>) 的构建；</li> 
 <li>mbedTLS 在非默认位置得到支持；</li> 
 <li>畸形的分支名称或远程缺失的分支会被忽略；</li> 
 <li>在更多情况下使用编译器的内在因素来检测算术溢出；</li> 
 <li>配置缓存在具有严格对齐的系统上正常运行；</li> 
 <li>为 <code>git_blob_filter_options</code> 增加了一个缺失的初始化函数选项（ <code>git_blob_filter_options_init</code>）；</li> 
 <li>修复了多个文档；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Freleases%2Ftag%2Fv1.1.1" target="_blank">https://github.com/libgit2/libgit2/releases/tag/v1.1.1</a></p>
                                        </div>
                                      
</div>
            