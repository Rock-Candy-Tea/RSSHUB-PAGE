
---
title: 'x-easypdf v2.7.3 版本发布，PDF 构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3381'
author: 开源中国
comments: false
date: Sat, 26 Feb 2022 19:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3381'
---

<div>   
<div class="content">
                                                                                            <p>x-easypdf 基于 pdfbox 二次封装，极大降低使用门槛，以组件化的形式进行 pdf 的构建。简单易用，仅需一行代码，便可完成 pdf 的相关操作。</p> 
<p>本次更新内容如下：</p> 
<ol> 
 <li>新增ttc字体支持</li> 
 <li>新增设置文本间隔方法</li> 
 <li>修复文档设置版本无效问题</li> 
 <li>修复表单设值后编辑器乱码问题</li> 
</ol> 
<p>ttc字体使用为：“字体路径”+“,”+“字体下标”的形式</p> 
<p>示例：</p> 
<pre><code class="language-java">@Test
    public void test() throws IOException &#123;
        String fontPath = "E:\\pdf\\msyhl.ttc,0";
        String filePath = OUTPUT_PATH + "testText.pdf";
        XEasyPdfHandler.Document.build().addPage(
                XEasyPdfHandler.Page.build(
                        PDRectangle.A4,
                        XEasyPdfHandler.Text.build(20F, "Hello World").setCharacterSpacing(10F).setHorizontalStyle(XEasyPdfPositionStyle.CENTER)
                )
        ).setFontPath(fontPath).setVersion(1.7F).save(filePath).close();
        System.out.println("finish");
    &#125;</code></pre>
                                        </div>
                                      
</div>
            