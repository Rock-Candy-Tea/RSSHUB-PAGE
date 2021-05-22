
---
title: 'Apache Arrow 4.0.0 发布，内存数据交换格式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8288'
author: 开源中国
comments: false
date: Sat, 22 May 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8288'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Arrow 4.0.0 现已发布，该版本涵盖了 3 个月的开发工作，包括来自 114 个不同贡献者的 711 个已解决的问题。此外，自 3.0.0 发布以来，Yibo Cai、Ian Cook 和 Jonathan Keane 已被邀请为 Arrow 的 committers，Andrew Lamb 和 Jorge Leitão 则加入了项目管理委员会（PMC）。</p> 
<p>Apache Arrow 是 Apache 基金会的顶级项目之一，目的是作为一个跨平台的数据层来加快大数据分析项目的运行速度。它包含一组规范的内存中的平面和分层数据表示，以及多种语言绑定以进行结构操作。 它还提供低架构流式传输和批量消息传递，零拷贝进程间通信（IPC）和矢量化的内存分析库。</p> 
<p>新版本的一些更新内容如下：</p> 
<p><strong>Arrow Flight RPC notes</strong></p> 
<p>在 Java 中，应用程序现在可以在写入数据时启用零拷贝优化（ARROW-11066）。这有可能破坏源代码的兼容性，所以默认情况下不启用。</p> 
<p>Arrow Flight 现在已被打包给 C#/.NET。</p> 
<p><strong>Linux packages notes</strong></p> 
<p>此前曾有由 Bintray 提供的用于 C++ 和 C GLib 的 Linux 软件包。但自 2021-05-01 起，Bintray 已不再可用。因此，它们现在由 Artifactory 提供。鉴于 URL 已经改变，所以用户需要改变安装说明。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farrow.apache.org%2Finstall%2F" target="_blank">安装页面</a>的新说明。以下是需要修改的摘要：</p> 
<p>对于 Debian GNU Linux 和 Ubuntu 用户：</p> 
<ul> 
 <li>用户需要更改<code>apache-arrow-archive-keyring</code>的安装说明： 
  <ul> 
   <li>程序包名称更改为<code>apache-arrow-apt-source</code>。</li> 
   <li>下载网址已从<code>https://apache.bintray.com/arrow/...</code>更改为<code>https://apache.jfrog.io/artifactory/arrow/...</code>。</li> 
  </ul> </li> 
</ul> 
<p>对于 CentOS 和 Red Hat Enterprise Linux 用户：</p> 
<ul> 
 <li>用户需要更改<code>apache-arrow-release</code>的安装说明： 
  <ul> 
   <li>下载网址已从<code>https://apache.bintray.com/arrow/...</code>更改为<code>https://apache.jfrog.io/artifactory/arrow/...</code>。</li> 
  </ul> </li> 
</ul> 
<p><strong>C++ notes</strong></p> 
<p>Arrow C++ 库现在包括一个 vcpkg.json 清单文件和一个新的 CMake 选项-DARROW_DEPENDENCY_SOURCE=VCPKG，以简化使用 vcpkg 包管理器的依赖关系安装。这提供了一种在 Linux、macOS 和 Windows 上安装 C++ 库依赖项的替代方法。</p> 
<p>macOS 上的默认内存分配器已从 jemalloc 改为 mimalloc，在一系列宏基准测试中产生了性能优势（ARROW-12316）。</p> 
<p>根据 Arrow 格式规范，现在不允许非单调的密集联合偏移量，并在 Array::ValidateFull 中返回一个错误（ARROW-10580）。</p> 
<p><strong>Compute layer</strong></p> 
<p>计算内核中的自动隐式转换（ARROW-8919）。例如，对于两个数组的加法，首先将数组转换为它们的公共数字类型，而不是在类型不相等时出错。</p> 
<p>已为数字数据添加了计算函数<code>quantile</code>（ARROW-10831）和<code>power</code>（ARROW-11070）。</p> 
<p>用于字符串处理的计算函数已添加到：</p> 
<ul> 
 <li>修剪字符（ARROW-9128）。</li> 
 <li>提取由正则表达式模式捕获的子字符串（<code>extract_regex</code>，ARROW-10195）。</li> 
 <li>计算 UTF8 字符串长度（<code>utf8_length</code>，ARROW-11693）。</li> 
 <li>根据正则表达式模式匹配字符串（<code>match_substring_regex</code>，ARROW-12134）。</li> 
 <li>替换与文字模式或正则表达式匹配的非重叠子字符串（<code>replace_substring</code>和<code>replace_substring_regex</code>，ARROW-10306）。</li> 
</ul> 
<p>现在可以对十进制和 fixed-width 的二进制数据进行排序（ARROW-11662）。</p> 
<p><code>sum</code>内核的精度得到了提高（ARROW-11758）。</p> 
<p><strong>CSV</strong></p> 
<ul> 
 <li>CSV writer 已添加（ARROW-2229）。</li> 
 <li>CSV reader 现在可以推断出带有小数秒的时间戳列（ARROW-12031）。</li> 
</ul> 
<p><strong>Dataset</strong></p> 
<p>Arrow Datasets 获得了各种性能改进和新功能。一些重点：</p> 
<ul> 
 <li>可以在扫描时从任意表达式投影新列（ARROW-11174）</li> 
 <li>Parquet 在高延迟文件系统上的读取性能得到了改善，通常是在有成千上万的文件或更多的文件时。</li> 
 <li>可以写入 Null partition keys（ARROW-10438）</li> 
 <li>可以读取压缩的 CSV 文件（ARROW-10372）</li> 
 <li>文件系统支持异步操作（ARROW-10846）</li> 
 <li>用法和 API 文档已添加（ARROW-11677）</li> 
</ul> 
<p><strong>Files and filesystems</strong></p> 
<ul> 
 <li>修复了一些罕见的 GZip 文件实例无法正确读取的情况（ARROW-12169）。</li> 
 <li>添加了对设置 S3 代理参数的支持（ARROW-8900）。</li> 
 <li>HDFS 文件系统现在可以一次写入 2GB 以上的数据（ARROW-11391）。</li> 
</ul> 
<p>更多详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farrow.apache.org%2Fblog%2F2021%2F05%2F03%2F4.0.0-release%2F" target="_blank">https://arrow.apache.org/blog/2021/05/03/4.0.0-release/</a> </p>
                                        </div>
                                      
</div>
            