
---
title: 'MyExcel 3.11.8 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9e620fa1d4002ab8b37ac6694917fde2f67.png'
author: 开源中国
comments: false
date: Sun, 07 Nov 2021 10:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9e620fa1d4002ab8b37ac6694917fde2f67.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd.class)
        .sheet(<span>0</span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span>0</span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .beanFilter(ArtCrowd::isDance) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// bean过滤</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新点如下：</strong></p> 
<ul> 
 <li>模板导出，支持单元格斜线绘制；</li> 
 <li>SaxExcelReader新增ignoreBlankRow方法，支持忽略空行；</li> 
 <li>SaxExcelReader新增stopReadingOnBlankRow方法，支持遇到空行时自动终止读取；</li> 
 <li><strong><span style="color:#e74c3c">SaxExcelReader支持按多级标题读取</span></strong>；</li> 
 <li>DefaultExcelBuilder\DefaultStreamExcelBuilder新增binding方法，绑定如spring等上下文；</li> 
 <li>@ExcelColumn新增writeConverter方法，支持自定义转化；</li> 
 <li>支持LocalTime读写转化；</li> 
 <li>部分类命名优化，更加符合语义上下文；</li> 
 <li>删除slf4j无效依赖，升级poi版本为4.1.2；</li> 
 <li>升级jsoup版本为1.14.3；</li> 
</ul> 
<p><strong>斜线绘制</strong></p> 
<p><img height="688" src="https://oscimg.oschina.net/oscnet/up-9e620fa1d4002ab8b37ac6694917fde2f67.png" width="672" referrerpolicy="no-referrer"></p> 
<p><strong>多级标题读取</strong></p> 
<p><img height="406" src="https://oscimg.oschina.net/oscnet/up-db9be912bdc9a7c153316908c8a0cbc5fa5.png" width="1160" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体，请移步文档<span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            