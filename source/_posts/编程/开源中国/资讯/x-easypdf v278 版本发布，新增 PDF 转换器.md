
---
title: 'x-easypdf v2.7.8 版本发布，新增 PDF 转换器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a23aae160c3b7f39c7670e7f124f79a3593.png'
author: 开源中国
comments: false
date: Sun, 10 Apr 2022 14:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a23aae160c3b7f39c7670e7f124f79a3593.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>x-easypdf基于pdfbox二次封装，极大降低使用门槛，以组件化的形式进行pdf的构建。简单易用，仅需一行代码，便可完成pdf的相关操作。</p> 
<p>本次更新内容如下：</p> 
<p>新特性：</p> 
<ol> 
 <li>文档替换器XEasyPdfDocumentReplacer优化文本替换逻辑</li> 
 <li>新增pdf转换器XEasyPdfConvertor，支持doc/docx/jpg/tiff/markdown/html/mhtml/rtf/odt/txt/mobi等格式转pdf，需添加aspose-words依赖</li> 
 <li>文档XEasyPdfDocument新增开启重置上下文的方法</li> 
 <li>页面XEasyPdfPage新增开启重置上下文的方法</li> 
</ol> 
<p>原有变更：</p> 
<ol> 
 <li>页面参数类XEasyPdfPageParam改为私有类</li> 
</ol> 
<p>问题修复： 无</p> 
<p>新特性说明：</p> 
<p>本次新增pdf转换器XEasyPdfConvertor，其中提供一系列转pdf的方法，需依赖aspose-words（改依赖为收费软件，使用试用版会生成水印），可配合文本替换的方法实现word转pdf模板进行模板导出的功能，可参考以下方式实现：</p> 
<p>1.  使用word制作模板：</p> 
<p><img alt height="617" src="https://oscimg.oschina.net/oscnet/up-a23aae160c3b7f39c7670e7f124f79a3593.png" width="977" referrerpolicy="no-referrer"></p> 
<p>2.  使用pdf转换器转为pdf模板（水印请自行处理）：</p> 
<p>pom文件中添加仓库与依赖：</p> 
<pre><code class="language-xml"><!--添加仓库-->
<repositories>
        <repository>
            <id>AsposeJavaAPI</id>
            <name>Aspose Java API</name>
            <url>https://repository.aspose.com/repo/</url>
        </repository>
</repositories>
<!--添加依赖-->
<dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-words</artifactId>
        <version>22.4</version>
        <type>pom</type>
</dependency></code></pre> 
<p>转换代码：</p> 
<pre><code class="language-java">// word源文件路径
String source = "C:\\Users\\Administrator\\Desktop\\test.doc";
// pdf文件路径
String dest = "C:\\Users\\Administrator\\Desktop\\test.pdf";
// 转换
XEasyPdfConvertor.toPdf(source, dest);</code></pre> 
<p>效果如下：</p> 
<p><img alt height="858" src="https://oscimg.oschina.net/oscnet/up-dc7649f2a2ddfabbc7e6f961b1fa347c61b.png" width="631" referrerpolicy="no-referrer"></p> 
<p>3. 替换模板：</p> 
<pre><code class="language-java">@Test
    public void testFill()&#123;
        // 模板文件路径
        String sourcePath = "C:\\Users\\Administrator\\Desktop\\test.pdf";
        // 替换后的文件路径
        String filePath = "C:\\Users\\Administrator\\Desktop\\testFill.pdf";
        // 字体文件路径，与模板文件字体保持一致，非必须
        String fontPath = "C:\\Windows\\Fonts\\simsun.ttc,0";
        // 定义替换字典（key为待替换字符串，value为替换后的字符串）
        Map<String, String> map = new HashMap<>(9);
        map.put("title", "测试报告");
        map.put("date", "2022-04-10");
        map.put("depart", "呼吸外科");
        map.put("no", "0001");
        map.put("name", "张三");
        map.put("sex", "男");
        map.put("age", "10");
        map.put("sign", "李某某");
        map.put("signTime", "2022-04-10 12:00:00");
        // 读取模板文件并替换保存
        XEasyPdfHandler.Document
                .load(sourcePath)
                .replacer()
                .setFontPath(fontPath)
                .enableReplaceCOSArray()
                .replaceText(map)
                .finish(filePath);
    &#125;</code></pre> 
<p>效果如下：</p> 
<p><img alt height="860" src="https://oscimg.oschina.net/oscnet/up-340ba544efce8fe3bb1c87ed29a077303d9.png" width="623" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            