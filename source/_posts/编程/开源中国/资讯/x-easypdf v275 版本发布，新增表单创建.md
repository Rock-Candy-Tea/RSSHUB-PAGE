
---
title: 'x-easypdf v2.7.5 版本发布，新增表单创建'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d182ea4b7df15e77b9c97ebf904bb8474bd.png'
author: 开源中国
comments: false
date: Tue, 05 Apr 2022 09:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d182ea4b7df15e77b9c97ebf904bb8474bd.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#40485b">x-easypdf基于pdfbox二次封装，极大降低使用门槛，以组件化的形式进行pdf的构建。简单易用，仅需一行代码，便可完成pdf的相关操作</span></p> 
<p>本次更新内容如下：<br> 新特性：<br> 1. 文档替换器XEasyPdfDocumentReplacer优化文本替换逻辑<br> 2. 文档表单填写器XEasyPdfDocumentFormFiller新增创建表单的方法<br> 3. 新增文档表单XEasyPdfDocumentForm类，可创建文本域<br> 4. 新增文档表单文本属性XEasyPdfDocumentFormTextField类，可添加表单文本属性</p> 
<p>原有变更：<br> 1. 文档提取器XEasyPdfDocumentExtractor移除extractByRegions方法，可用extractTextByRegions方法替换<br> 2. 文档提取器XEasyPdfDocumentExtractor移除extract方法，可用extractText方法替换<br> 3. 文档提取器XEasyPdfDocumentExtractor移除extractForSimpleTable方法，可用extractTextForSimpleTable方法替换</p> 
<p>问题修复：<br> 无</p> 
<p>表单创建简单示例：</p> 
<pre><code class="language-java">String filePath = OUTPUT_PATH + "testCreate.pdf";
        XEasyPdfHandler.Document
                // 创建文档
                .build()
                // 添加页面
                .addPage(
                        // 创建空白页
                        XEasyPdfHandler.Page.build()
                )
                // 获取表单填写器
                .formFiller()
                // 创建表单
                .create()
                // 创建第一个文本属性
                .createTextField()
                // 设置映射名称
                .setMappingName("property1")
                // 设置位置坐标
                .setPosition(50F,700F)
                // 开启打印
                .enablePrint()
                // 完成文本属性创建
                .finish()
                // 创建第二个文本属性
                .createTextField()
                // 设置映射名称
                .setMappingName("property2")
                // 设置位置坐标
                .setPosition(200F,700F)
                // 设置默认值
                .setDefaultValue("test")
                // 设置最大字符数
                .setMaxLength(11)
                // 完成文本属性创建
                .finish()
                // 完成表单操作
                .finish()
                // 完成填写器操作
                .finish(filePath);</code></pre> 
<p>效果如下：</p> 
<p><img alt height="741" src="https://oscimg.oschina.net/oscnet/up-d182ea4b7df15e77b9c97ebf904bb8474bd.png" width="1267" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            