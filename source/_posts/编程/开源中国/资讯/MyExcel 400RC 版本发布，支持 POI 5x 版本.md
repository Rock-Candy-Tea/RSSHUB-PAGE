
---
title: 'MyExcel 4.0.0.RC 版本发布，支持 POI 5.x 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 08:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd.class)
        .sheet(<span><span>0</span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span>0</span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .beanFilter(ArtCrowd::isDance) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// bean过滤</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新为大版本更新，但使用上兼容旧版本，具体更新点如下：</strong></p> 
<ul> 
 <li>POI版本升级为5.1.0，升级freemarker等模板引擎版本为最新版；</li> 
 <li>修复添加提示-prompt，excel打开异常问题；</li> 
 <li>修复添加批注，展示空间不足问题；</li> 
 <li>修复导入可能出现携带拼音的问题；</li> 
 <li>修正SaxExcelReader中sheet索引问题；</li> 
 <li> <p><span style="background-color:#ffffff; color:#24292f">支持批注-comment设置；</span></p> </li> 
 <li>增加导出图片缓存，减少导出excel文件体积；</li> 
 <li>SaxExcelReader新增xls、xlsx文件元信息获取接口-getWorkbookMetaData，可快速获取工作簿相关信息，如有多少个sheet，每个sheet最后一行行号等等信息；</li> 
 <li>SaxExcelReader新增读取Path方法，扩展读取InputStream、File渠道；</li> 
 <li><span style="background-color:#ffffff; color:#24292f">新增ColumnSaxExcelReader，支持按某一列读取</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">优化多级标题读取，支持90%以上多级标题</span></li> 
 <li>替换日志组件为slf4j，与POI保持一致；</li> 
 <li>修改Thymeleaf模板引擎入参方式，支持3.x版本；</li> 
 <li>删除冗余代码，去除内部类get/set方法，直接访问属性，减少包体积&性能提升；</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            