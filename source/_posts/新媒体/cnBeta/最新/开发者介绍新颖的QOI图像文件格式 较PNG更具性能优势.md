
---
title: '开发者介绍新颖的QOI图像文件格式 较PNG更具性能优势'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1227/e6b3a795e0e0858.png'
author: cnBeta
comments: false
date: Mon, 27 Dec 2021 10:38:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1227/e6b3a795e0e0858.png'
---

<div>   
<strong>一位名叫 Dominic Szablewski 的开发者，刚刚介绍了一种“相当不错”的新图像文件格式（简称 QOI）。</strong>开发者解释称：世界需要一种全新的图像格式，因为在 PNG、JPEG、MPEG、MOV 和 MP4 等文件类型的接缝处，还是充满了相当大的复杂性。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1227/e6b3a795e0e0858.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://phoboslab.org/log/2021/11/qoi-fast-lossless-image-compression" target="_self">Phobos Lab</a>）</p><p>Dominic Szablewski 指出：QOI 全称为“Quiet OK Image Format”，主打开源、快速、无损压缩等特性。</p><p>相比之下，目前大多数常见的编解码器不仅陈旧、封闭、依赖于庞大的库，且计算量大到难以使用。</p><p>为了做到更好，开发者决定编写一些代码。在将 QOI 发布到 <a href="https://github.com/phoboslab/qoi" target="_self">GitHub</a> 托管平台后，他还高度重视大家留下的 500 多条评论。</p><p><strong>现在看来，Szablewski 似乎已经实现了这一目标：</strong></p><blockquote><p>虽然 QOI 不会像优化的 PNG 编码器那样压缩图像，但还是能够无损地将图像压缩到近似 PNG 的大小、辅以 20-50 倍的编码速度 / 3-4 倍的解码速度。</p><p>更重要的是，QOI 的参考编解码器只用到了大约 300 行 C 语言代码，且文件格式的规范要求也只有一页的篇幅。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/1227/264ae90dfe83201.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：QOIformat.org <a href="https://qoiformat.org/" target="_self">官网</a>）</p><p><strong>Szablewski 在博客中写道：</strong></p><blockquote><p>过去几周出现了许多不同语言和库的 QOI 实现，涵盖了 Zig、Rust、Go、TypeScript、Haskell、Ć、Python、C#、Elixir、Swift、Java 和 Pascal 等选项。</p><p>此外有一款能够查看 .QOI 文件的原生应用程序，支持 Gimp、Paint.NET 和 XnView MP 的插件，对 SDL_Image 的支持（待定）也已在路上。</p></blockquote><p><strong>综上，Szablewski 认为 QOI 还是相当有希望成功出圈的。</strong></p><p>不过他也承认，该格式不大可能在短期内获得主流 Web 浏览器的支持，毕竟该领域暂时更关注于压缩比。但在游戏或其它应用场景里，QOI 的性能优势更具意义。</p>   
</div>
            