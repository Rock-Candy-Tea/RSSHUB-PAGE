
---
title: 'MyExcel 4.1.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1d7714443311ea91e9d792dd0338d3b01e6.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 02:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1d7714443311ea91e9d792dd0338d3b01e6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd<span><span><span>.</span></span><span style="color:#d73a49"><span><span style="color:#d73a49"><span><span style="color:#d73a49">class</span></span></span></span></span><span><span>)</span></span></span>
        .sheet(<span><span><span><span><span><span>0</span></span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span><span><span><span><span>0</span></span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .detectedMerge() <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 识别合并单元格并填充数据，默认不识别</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path);</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新如下</strong>：</p> 
<ul> 
 <li>修复读取xls文件，无合并单元格情况下调用detectedMerge方法异常问题；</li> 
 <li>修复HtmlToExcelFactory读取多个table合并到一个sheet时被覆盖问题；</li> 
 <li>原velocity模板引擎依赖修改，解决1.7版本安全漏洞问题；</li> 
 <li>新增InputStream、String（绝对路径、http形式、base64位形式）图片导出功能；</li> 
 <li>POI版本升级为5.2.2；</li> 
</ul> 
<p>图片导出格式支持如下：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki%2F%25E5%259B%25BE%25E7%2589%2587%25E5%25AF%25BC%25E5%2587%25BA" target="_blank">https://github.com/liaochong/myexcel/wiki/%E5%9B%BE%E7%89%87%E5%AF%BC%E5%87%BA</a></p> 
<p><img height="1388" src="https://oscimg.oschina.net/oscnet/up-1d7714443311ea91e9d792dd0338d3b01e6.png" width="1874" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            