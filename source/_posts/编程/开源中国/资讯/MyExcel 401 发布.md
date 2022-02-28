
---
title: 'MyExcel 4.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 08:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd<span><span>.</span><span style="color:#d73a49"><span><span style="color:#d73a49">class</span></span></span><span>)</span></span>
        .sheet(<span><span><span><span><span>0</span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span><span><span><span>0</span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .detectedMerge() <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 识别合并单元格并填充数据，默认不识别</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p>本次更新如下：</p> 
<ul> 
 <li>修改DefaultStreamExcelBuilder.of(classType,workbook)逻辑，原只能在指定的workbook上新增sheet，现改为：如果已经存在指定的sheet，且未达到最大条数，则继续追加，不新增sheet，否则新增sheet；</li> 
 <li><span style="color:#e74c3c">修改临时文件目录为系统临时文件目录，解决可能的文件权限问题</span>：在部分场景下，系统权限较为严格，如不在系统临时文件目录下，则无法正常读写；</li> 
 <li>DefaultStreamExcelBuilder允许动态指定sheetName覆盖@ExcelModel sheetName属性；</li> 
 <li>过期自定义临时文件目录方法；</li> 
</ul> 
<p style="color:#24292f; text-align:start"><strong>升级4.x版本注意事项</strong></p> 
<p style="color:#24292f; text-align:start">因POI 4.x与5.x版本存在部分不兼容情况，MyExcel低版本升级为4.x（POI 5.x）时，需要注意以下事项：</p> 
<ol> 
 <li>POI版本必须为5.x</li> 
 <li>排除掉poi-ooxml-schemas依赖（POI 5.x以poi-ooxml-full作为代替）</li> 
 <li>commons-io版本为2.11.0</li> 
</ol> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            