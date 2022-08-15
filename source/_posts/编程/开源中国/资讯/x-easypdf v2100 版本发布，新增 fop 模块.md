
---
title: 'x-easypdf v2.10.0 版本发布，新增 fop 模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0621/111332_1f43ae97_1494292.png'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 08:04:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0621/111332_1f43ae97_1494292.png'
---

<div>   
<div class="content">
                                                                                            <p>x-easypdf v2.10.0 版本发布，新增fop模块</p> 
<p><img alt="logo" src="https://images.gitee.com/uploads/images/2021/0621/111332_1f43ae97_1494292.png" referrerpolicy="no-referrer"></p> 
<p>x-easypdf基于pdfbox/fop二次封装，拥有两大模块：pdfbox模块极大降低pdfbox的使用门槛，以组件化的形式进行pdf的构建；fop模块采用数据源的方式对xsl-fo模板进行转换。两个模块均可单独使用，也可以结合使用，帮助开发者快速生成pdf文档。</p> 
<p>本次更新内容如下：</p> 
<p>新特性：</p> 
<ul> 
 <li>新增单元格组件设置边框点线长度的方法（虚线边框设置）</li> 
 <li>新增单元格组件设置边框点线间隔的方法（虚线边框设置）</li> 
 <li>新增表格行组件设置边框点线长度的方法（虚线边框设置）</li> 
 <li>新增表格行组件设置边框点线间隔的方法（虚线边框设置）</li> 
 <li>新增表格组件设置边框点线长度的方法（虚线边框设置）</li> 
 <li>新增表格组件设置边框点线间隔的方法（虚线边框设置）</li> 
 <li>新增fop模块</li> 
 <li>新增pdf模板</li> 
 <li>新增pdf模板常数类</li> 
 <li>新增pdf模板助手</li> 
 <li>新增pdf模板数据源，支持自定义扩展数据源</li> 
 <li>新增pdf模板xml数据源</li> 
 <li>新增pdf模板thymeleaf数据源</li> 
 <li>新增pdf模板document数据源（开发中，已提供文本组件与图像组件）</li> 
 <li>新增pdf模板-文档</li> 
 <li>新增pdf模板-页面</li> 
 <li>新增pdf模板-文本组件</li> 
 <li>新增pdf模板-图像组件</li> 
</ul> 
<p>原有变更：</p> 
<ul> 
 <li>调整文档签名器结构</li> 
 <li>移除pdf转换器</li> 
 <li>移除aspose依赖</li> 
 <li>默认添加全部依赖，无需再自行添加，如有无用依赖，可自行排除</li> 
 <li>jdk最低版本由1.7调整为1.8</li> 
 <li>模块拆分： 
  <ul> 
   <li>x-easypdf为全功能模块，包含pdfbox与fop相关功能</li> 
   <li>x-easypdf-pdfbox为pdfbox模块，包含pdfbox相关功能</li> 
   <li>x-easypdf-fop为fop模块，包含fop相关功能，主要为模板导出功能</li> 
  </ul> </li> 
</ul> 
<p>问题修复：</p> 
<p>无</p> 
<p>fop模块用法演示：</p> 
<ul> 
 <li>使用步骤：</li> 
</ul> 
<ol> 
 <li> <p>设置fop配置文件路径（如使用默认配置，则可跳过此步）</p> </li> 
 <li> <p>设置数据源，并设置xsl-fo模板路径（如使用document数据源，则可跳过此步）</p> </li> 
 <li> <p>执行转换</p> </li> 
</ol> 
<ul> 
 <li>配置文件（默认配置）：</li> 
</ul> 
<pre><code class="language-xml"><?xml version="1.0"?>

<!-- NOTE: This is the version of the configuration -->
<fop version="1.0">

    <!-- Base URL for resolving relative URLs -->
    <base>.</base>

    <!-- Source resolution in dpi (dots/pixels per inch) for determining the size of pixels in SVG and bitmap images, default: 72dpi -->
    <source-resolution>72</source-resolution>
    <!-- Target resolution in dpi (dots/pixels per inch) for specifying the target resolution for generated bitmaps, default: 72dpi -->
    <target-resolution>72</target-resolution>

    <!-- Default page-height and page-width, in case value is specified as auto -->
    <default-page-settings width="21cm" height="29.7cm"/>

    <!-- Information for specific renderers -->
    <!-- Uses renderer mime type for renderers -->
    <renderers>
        <renderer mime="application/pdf">
            <filterList>
                <!-- provides compression using zlib flate (default is on) -->
                <value>flate</value>
            </filterList>

            <fonts>
                <!-- auto-detect fonts -->
                <auto-detect/>
            </fonts>
        </renderer>
    </renderers>
</fop>
</code></pre> 
<ul> 
 <li>xml（xslt）数据源演示：</li> 
</ul> 
<ol> 
 <li>使用模板:</li> 
</ol> 
<pre><code class="language-xml"><?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:xslt="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <!--模板-->
    <xsl:template match="root">
        <!--根标签-->
        <fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
            <!--页面模板-->
            <fo:layout-master-set>
                <!--单页面模板-->
                <fo:simple-page-master master-name="A4">
                    <!--页面区域主体-->
                    <fo:region-body/>
                </fo:simple-page-master>
            </fo:layout-master-set>
            <!--页面序列-->
            <fo:page-sequence master-reference="A4">
                <!--页面流-->
                <fo:flow flow-name="xsl-region-body">
                    <!--块-->
                    <fo:block text-align="center">
                        <!--文本内容-->
                        <xsl:apply-templates select="data"/>
                    </fo:block>
                </fo:flow>
            </fo:page-sequence>
        </fo:root>
    </xsl:template>
</xsl:stylesheet>
</code></pre> 
<ol start="2"> 
 <li>xml数据：</li> 
</ol> 
<pre><code class="language-xml"><?xml version="1.0" encoding="utf-8"?>
<root>
    <data>hello world</data>
</root>
</code></pre> 
<ol start="3"> 
 <li>示例代码：</li> 
</ol> 
<pre><code class="language-java">// 定义fop配置文件路径
String configPath = "H:\\\\pdf\\\\template\\\\fop.xconf";
// 定义xsl-fo模板路径
String templatePath = "H:\\\\pdf\\\\template\\\\xml\\\\template.fo";
// 定义xml数据路径
String xmlPath = "H:\\\\pdf\\\\template\\\\xml\\\\data.xml";
// 定义pdf输出路径
String outputPath = "E:\\\\pdf\\\\test\\\\fo\\\\xml.pdf";
// 转换pdf
XEasyPdfTemplateHandler.Template.build().setConfigPath(configPath).setDataSource(
    XEasyPdfTemplateHandler.DataSource.XML.build().setTemplatePath(templatePath).setXmlPath(xmlPath)
).transform(outputPath);
</code></pre> 
<ul> 
 <li>thymeleaf数据源演示：</li> 
</ul> 
<ol> 
 <li>使用模板:</li> 
</ol> 
<pre><code class="language-xml"><?xml version="1.0" encoding="utf-8"?>
<!--根标签-->
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <!--页面模板-->
    <fo:layout-master-set>
        <!--单页面模板-->
        <fo:simple-page-master master-name="A4">
            <!--页面区域主体-->
            <fo:region-body/>
        </fo:simple-page-master>
    </fo:layout-master-set>
    <!--页面序列-->
    <fo:page-sequence master-reference="A4">
        <!--页面流-->
        <fo:flow flow-name="xsl-region-body">
            <!--块-->
            <fo:block text-align="center" th:text="$&#123;data&#125;"/>
        </fo:flow>
    </fo:page-sequence>
</fo:root>
</code></pre> 
<ol start="2"> 
 <li>示例代码：</li> 
</ol> 
<pre><code class="language-java">// 定义fop配置文件路径
String configPath = "H:\\\\pdf\\\\template\\\\fop.xconf";
// 定义xsl-fo模板路径
String templatePath = "H:\\\\pdf\\\\template\\\\thymeleaf\\\\template.fo";
// 定义pdf输出路径
String outputPath = "E:\\\\pdf\\\\test\\\\fo\\\\thymeleaf.pdf";
// 定义数据map
Map<String, Object> data = new HashMap<>();
// 设置值
data.put("data", "hello world");
// 转换pdf
XEasyPdfTemplateHandler.Template.build().setConfigPath(configPath).setDataSource(
    XEasyPdfTemplateHandler.DataSource.Thymeleaf.build().setTemplatePath(templatePath).setTemplateData(data)
).transform(outputPath);
</code></pre> 
<ul> 
 <li>document数据源演示：</li> 
</ul> 
<ol> 
 <li>内置模板:</li> 
</ol> 
<pre><code class="language-xml"><?xml version="1.0" encoding="utf-8"?>
<!--根标签-->
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <!--页面模板-->
    <fo:layout-master-set></fo:layout-master-set>
</fo:root>
</code></pre> 
<ol start="2"> 
 <li>示例代码：</li> 
</ol> 
<pre><code class="language-java">// 定义pdf输出路径
String outputPath = "E:\\\\pdf\\\\test\\\\fo\\\\document.pdf";
// 转换pdf
XEasyPdfTemplateHandler.Document.build().addPage(
    XEasyPdfTemplateHandler.Page.build().addBodyComponent(
        XEasyPdfTemplateHandler.Text.build().setText("hello world").setHorizontalStyle(XEasyPdfTemplatePositionStyle.HORIZONTAL_CENTER)
    )
).transform(outputPath);
</code></pre> 
<ul> 
 <li>以上示例生成效果：</li> 
</ul> 
<p><img height="50%" src="https://oscimg.oschina.net/oscnet/up-ff6c8ccf45e54fb7b301749221dccb371b7.png" width="50%" referrerpolicy="no-referrer"></p> 
<p><img alt="dromara" src="https://dromara.org/img/logo/dromara.jpg" referrerpolicy="no-referrer"></p> 
<p>为往圣继绝学，一个人或许能走的更快，但一群人会走的更远。</p>
                                        </div>
                                      
</div>
            