
---
title: 'FLAC 1.3.4 发布，无损压缩音频格式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3611'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3611'
---

<div>   
<div class="content">
                                                                                            <p>时隔大约 3 年，FLAC 终于发布了更新：1.3.4。</p> 
<blockquote> 
 <p>FLAC (Free Lossless Audio Codec) 是一种无损压缩音频格式，支持流媒体和压缩。它为几个受欢迎的音频播放器提供了编码器/解码器的输入插件。音频格式跟 MP3 相似，但是无损的，也就是说，音频压缩后没有任何质量的损失。</p> 
</blockquote> 
<p>此版本主要修复（与安全相关的）错误。使用 MSVC 构建时，首选使用 CMake，有关详细信息，查看“使用 CMake 构建”下的 README 文件。不推荐使用 MSVC 解决方案文件进行构建，因为这些文件在未来将会被删除。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxiph.org%2Fflac%2Fchangelog.html" target="_blank">Changelog</a></p> 
<ul> 
 <li>General: 
  <ul> 
   <li>修复 oss-fuzz 发现的 12 个解码器错误，包括 CVE-2020-0499</li> 
   <li>修复编码器错误 CVE-2021-0561</li> 
   <li>集成 oss-fuzzers</li> 
   <li>修复 Seeking 相关的问题</li> 
   <li>多项修复和改进</li> 
  </ul> </li> 
 <li>FLAC format: 
  <ul> 
   <li>无</li> 
  </ul> </li> 
 <li>Ogg FLAC format: 
  <ul> 
   <li>无</li> 
  </ul> </li> 
 <li>flac: 
  <ul> 
   <li>多项修复和改进</li> 
  </ul> </li> 
 <li>metaflac: 
  <ul> 
   <li>无</li> 
  </ul> </li> 
 <li>build system: 
  <ul> 
   <li>改进 CMake</li> 
   <li>修复 MinGW 和 MSVC</li> 
   <li>修复 clang</li> 
   <li>修复 PowerPC</li> 
   <li>修复 FreeBSD PowerPC</li> 
  </ul> </li> 
 <li>testing/validation: 
  <ul> 
   <li>将 Windows target 添加到 CI，改进日志记录</li> 
   <li>改进 CI</li> 
  </ul> </li> 
 <li>documentation: 
  <ul> 
   <li>修复 Doxygen</li> 
   <li>修复拼写错误</li> 
  </ul> </li> 
 <li>Interface changes: 
  <ul> 
   <li>libFLAC: 
    <ul> 
     <li>无</li> 
    </ul> </li> 
   <li>libFLAC++: 
    <ul> 
     <li>无</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxiph.org%2Fflac%2Fdownload.html" target="_blank">https://xiph.org/flac/download.html</a></p>
                                        </div>
                                      
</div>
            