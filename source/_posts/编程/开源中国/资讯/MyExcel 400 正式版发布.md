
---
title: 'MyExcel 4.0.0 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-85160bd6c0bfab35ff6c1c1b7a86e3f340e.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 13:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-85160bd6c0bfab35ff6c1c1b7a86e3f340e.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">经过3个RC版本，大版本</span></strong><strong><span style="color:#e74c3c">4.0.0（基于POI 5.2.0）正式版发布！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd<span>.<span style="color:#d73a49">class</span>)</span>
        .sheet(<span><span><span><span>0</span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span><span><span>0</span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .detectedMerge() <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 识别合并单元格并填充数据，默认不识别</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p>本次更新点如下：</p> 
<ul> 
 <li>修复自定义写转化返回null导致的空指针问题；</li> 
 <li><span style="color:#e74c3c">DefaultStreamExcelBuilder新增autoMerge方法，配合@MultiColumn可实现非列表字段自动合并</span>；</li> 
 <li>其他冗余代码删除；</li> 
</ul> 
<p>原涉及到单元格合并，除标题外需采用模板，流程稍微复杂，本次版本新增了按数据结构自动合并能力，具体如下：</p> 
<p>数据结构定义：</p> 
<pre><code class="language-java">public class Grade &#123;
        @ExcelColumn(title = "年级")
        String grade;

        @ExcelColumn(title = "学生姓名")
        @MultiColumn(classType = String.class)
        List<String> studentNames;
&#125;</code></pre> 
<p>创建方法：</p> 
<pre><code class="language-java">try (DefaultStreamExcelBuilder<Grade> excelBuilder = DefaultStreamExcelBuilder.of(Grade.class)
                .autoMerge()
                .start()) &#123;
&#125;</code></pre> 
<p>使用@MultiColumn标记聚合列，配合autoMerge方法，可自动实现非聚合列自动合并，效果如下：</p> 
<p><img height="626" src="https://oscimg.oschina.net/oscnet/up-85160bd6c0bfab35ff6c1c1b7a86e3f340e.png" width="264" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a>，参考聚合列导出</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p> 
<p><img height="1612" src="https://oscimg.oschina.net/oscnet/up-913c492ab432efe2b64e6448152740766a1.png" width="2880" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            