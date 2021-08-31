
---
title: 'Apache Tika 2.1.0 发布，内容检测和分析框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2994'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 06:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2994'
---

<div>   
<div class="content">
                                                                                            <p>Apache Tika 2.1.0 现已发布，这是一个用于检测和提取元数据和结构化文本内容的工具包。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>优化了 tika-parsers-extended 的打包</li> 
 <li>当没有指定编码时，Tika 应用程序会以 UTF-8 格式写入 </li> 
 <li>将 PDF 的默认渲染策略从 NO_TEXT 更改为 ALL</li> 
 <li>修复了当用户指定了 tesseract 路径但未同时指定 TesserData 路径时，指向错误的 TesserData 目录的问题</li> 
 <li>修复了 Icu4j 编码检测器可能会返回非标准的字符集名称的问题</li> 
 <li>在 tika core 中添加一个简单的 UrlFetcher，作为 tika fetcher http的基本替代方案</li> 
 <li>为 Google Cloud Storage 添加 tika-pipes 支持</li> 
 <li>修复 ODT 文件的 xhtml 输出中的标记排序错误</li> 
 <li>修复了 OpenSearch 发射器中嵌入式文档的序列化，并修复 Solr 发射器中某些使用情况下嵌入式文档未被索引的问题</li> 
 <li>将 pipeClientId 系统属性添加到 PipesServer，以便每个子进程可以登录到它自己的记录器</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253CCAC1dCwXv_ZSwqESfTMusCno385gTojH09e%2Bv9v3tA1Pr00Ojrw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            