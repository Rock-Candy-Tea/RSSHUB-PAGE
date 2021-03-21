
---
title: Apache PDFBox 2.0.23 发布，Java 的 PDF 处理类库
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Sat, 20 Mar 2021 07:32:00 GMT
thumbnail: 
---

<div>   
<div class="content">
                                                                                            <p>Apache PDFBox 2.0.23 已经发布。Apache PDFBox 库是一个开源的用于处理 PDF 文档的 Java 工具。</p> 
<p><strong>部分更新内容</strong></p> 
<ul> 
 <li>Bug 修复 
  <ul> 
   <li>修复了 Transparency Group 中的问题</li> 
   <li>修复了 getLastSignatureDictionary 修改 PDDocument 内部结构的问题</li> 
   <li>修复了 AcroForm PDTextField 格式化丢失的问题</li> 
   <li>修复了 Type1Parser.parseASCII 抛出不同异常的问题</li> 
   <li>修复了 WinANSIEncoding 渲染符号 TTF 字体时出现错误字形的问题</li> 
   <li>修复了 isOwnerPassword 中的 ArrayIndexOutOfBoundsException</li> 
   <li>修复了 COSStream.getFilterList 中的 ClassCastException </li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>完善文档签名</li> 
   <li>通过反转 ToUnicode CMap，允许重用子集字体</li> 
   <li>提高签名验证的性能</li> 
   <li>向 PDFXrefStreamParser 添加更多检查并减少内存占用</li> 
   <li>在 ShowColorBoxes.java 示例中添加旋转框</li> 
   <li>在 PDDeviceN.toRGBWithTintTransform() 中使用 StringBuilder 作为键</li> 
   <li>不会在 PDDeviceN.toRGBWithTintTransform() 中使用 RGB 循环</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202103.mbox%2F%253C8705a2b5-c418-436d-c2b0-d9c770e98798%40apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            