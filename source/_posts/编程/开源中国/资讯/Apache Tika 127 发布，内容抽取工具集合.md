
---
title: 'Apache Tika 1.27 发布，内容抽取工具集合'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4387'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4387'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Tika 1.27 已发布，Tika 是一个内容抽取的工具集合 (a toolkit for text extracting)。它集成了 POI 和 Pdfbox，并且为文本抽取工作提供了一个统一的界面。其次，Tika 也提供了便利的扩展 API，用来丰富其对第三方文件格式的支持。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.apache.org%2Ftika%2F1.27%2FCHANGES-1.27.txt" target="_blank">主要更新内容</a>：</p> 
<ul> 
 <li>将 MP4 解析迁移到 Drew Noakes 的元数据提取器上 (TIKA-3459)<br> 如需恢复至旧版解析器，关闭 NoakesMP4Parser 并通过 tika-config.xml 打开 MP4Parser</li> 
 <li>防止在 tika-server 的 -spawnChild 模式下，由于无法绑定到端口而重启失败时，出现罕见的无限循环 (TIKA-3441).</li> 
 <li>提升 likelihood 在 tika-server 的 jvm 重启时不会被弃用的可能性 (TIKA-3441).</li> 
 <li>弃用实验性的 PDFPreflightParser (TIKA-3437).</li> 
 <li>通过 Ryan421 对 zip 条目名称应用编码检测 (TIKA-3374).</li> 
 <li>在 tika-server 中为 /tika 端点添加 json 输出 (TIKA-3352).</li> 
 <li>如果有一个文件通过 TikaInputStream 传入，Tika 的 PDFParser 会使用底层文件 (TIKA-3350)</li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftika.apache.org%2Fdownload.html" target="_blank">https://tika.apache.org/download.html</a></p>
                                        </div>
                                      
</div>
            