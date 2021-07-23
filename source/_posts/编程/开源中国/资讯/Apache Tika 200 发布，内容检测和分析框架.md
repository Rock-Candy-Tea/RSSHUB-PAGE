
---
title: 'Apache Tika 2.0.0 发布，内容检测和分析框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8956'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 06:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8956'
---

<div>   
<div class="content">
                                                                                            <p>Apache Tika 是一个用于检测和提取元数据和结构化文本内容的工具包。Apache Tika 2.0.0 发布，更新内容如下：</p> 
<p>常规：</p> 
<ul> 
 <li>如果 tesseract 在用户的路径上，OCR 现在会自动对 PDF 文件进行触发；</li> 
 <li>在 tika-app、tika-server 和其他任何使用了 log4j 的地方将 log4j 升级到 log4j2；</li> 
 <li>默认情况下，当为 OCR 渲染一个页面时，PDFParser 不会渲染字形/文字；</li> 
 <li>删除了废弃的元数据键/属性；</li> 
 <li>删除了废弃的 PDFPreflightParser；</li> 
 <li>删除了不指定字符集就读取输入流或转换为字节的危险调用；</li> 
 <li>解析器可以在实例化时通过 tika-config.xml 进行配置；</li> 
 <li>改变了翻译器实现的命名空间以避免与 tika-core 分开打包；</li> 
</ul> 
<p>tika-parsers</p> 
<ul> 
 <li>解析器模块被分成三个主要模块：tika-parsers-standard, tika-parsers-extended 和 tika-parsers-ml；</li> 
 <li>CompressorParser：用户必须将 com.github.luben:zstd-jni 依赖项添加到 classpath 来处理zstd 文件；</li> 
 <li>ChmParser 被移到 org.apache.tika.parser.microsoft.chm；</li> 
 <li>RTFParser 被移到 org.apache.tika.parser.microsoft.rtf；</li> 
</ul> 
<p>tika-server</p> 
<ul> 
 <li>tika-server 现在默认会 fork 一个进程，将解析工作隔离在 fork 的进程中；</li> 
 <li>大部分通过命令行进行的 tika-server 的传统配置已经被移至通过 tika-config.xml 文件进行配置；</li> 
 <li>tika-server的 "enableFileUrl" 已被删除，改为使用 FileSystemFetcher；</li> 
 <li>tika-server 的 /metadata 端点需要 tika-server-standard 来写入 XMP/rdf 输出；</li> 
 <li>在 tika-server 中，对于那些可以通过配置对象在每次解析中进行配置的解析器来说，通过 ParseContext 传入的配置对象，配置对象将只更新那些用户修改过的字段；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.apache.org%2Ftika%2F2.0.0%2FCHANGES-2.0.0.txt" target="_blank">https://downloads.apache.org/tika/2.0.0/CHANGES-2.0.0.txt</a></p>
                                        </div>
                                      
</div>
            