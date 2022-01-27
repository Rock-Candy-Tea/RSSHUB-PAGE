
---
title: 'MyExcel 4.0.0.RC3 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 10:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">年前最后一版，祝大家新年快乐，平安顺遂！！！</span></strong></p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd.class)
        .sheet(<span><span><span>0</span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span><span>0</span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .detectedMerge() <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 识别合并单元格并填充数据，默认不识别</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p><strong>本次更新点如下</strong>：</p> 
<ul> 
 <li>修复ColumnSaxExcelReader读取含空格列空指针异常问题；</li> 
 <li>SaxExcelReader新增detectedMerge方法，支持合并单元格识别填充；</li> 
 <li>模板导出，新增applyDefaultStyle方法，允许自定义样式+默认样式，如样式名称相同，自定义样式会覆盖默认样式；</li> 
 <li>引入commons-csv替换自研csv导入，解决可能的内存占用过大问题；</li> 
 <li>SaxExcelReader新增csvDelimiter方法，支持设置csv读取所需的分隔符；</li> 
 <li>过期SaxExcelReader charset方法，使用csvCharset代替，增强语义；</li> 
 <li>修改ColumnSaxExcelReader ignoreBlankRow方法为ignoreBlankCell方法；</li> 
 <li>删除大量冗余代码，修改读取逻辑，提升读取性能；</li> 
 <li>升级POI版本为5.2.0，解决log4j等组件安全漏洞问题；</li> 
 <li>移除部分内部类public修饰符；</li> 
 <li>冗余代码删除，减少包体积；</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            