
---
title: 'Word 模板引擎 poi-tl V1.10.0 发布，支持批注和代码高亮'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2191ee1ba6234a25c11bef63df4ce2934a0.png'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 08:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2191ee1ba6234a25c11bef63df4ce2934a0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>当程序员需要创建Word文档的时候，使用模板生成word可能是一个更好的选择，poi-tl<span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.85)">基于Microsoft Word模板和数据生成新的Word文档，可能是Java中最好的Word模板引擎。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">V1.10.0正式版本已经发布，增加了很多新特性：</span></p> 
<ul> 
 <li>全方位支持Word批注功能（注：当前Apache POI原生还不支持批注）</li> 
 <li>图片支持SVG、Base64，支持自动识别各种图片类型</li> 
 <li>新增插件HighlightRenderPolicy：Word中代码块高亮展示，支持26种语言和上百种着色样式</li> 
 <li>新增插件MarkdownRenderPolicy：Markdown转为word文档，包括表格、代码块、锚点、引用、加粗斜体等</li> 
 <li>若干性能和功能优化、BUGFIX</li> 
</ul> 
<h4 style="text-align:left">代码高亮示例</h4> 
<pre><code class="language-java">HighlightRenderData code = new HighlightRenderData();
code.setCode("/**\n"
        + " * @author John Smith <john.smith@example.com>\n"
        + "*/\n"
        + "package l2f.gameserver.model;\n"
        + "\n"
        + "public abstract strictfp class L2Char extends L2Object &#123;\n"
        + "  public static final Short ERROR = 0x0001;\n"
        + "\n"
        + "  public void moveTo(int x, int y, int z) &#123;\n"
        + "    _ai = null;\n"
        + "    log(\"Should not be called\");\n"
        + "    if (1 > 5) &#123; // wtf!?\n"
        + "      return;\n"
        + "    &#125;\n"
        + "  &#125;\n"
        + "&#125;");
code.setLanguage("java"); 
code.setStyle(HighlightStyle.builder().withShowLine(true).withTheme("zenburn").build());</code></pre> 
<h4 style="text-align:left">生成示例</h4> 
<p><img alt height="371" src="https://oscimg.oschina.net/oscnet/up-2191ee1ba6234a25c11bef63df4ce2934a0.png" width="480" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            