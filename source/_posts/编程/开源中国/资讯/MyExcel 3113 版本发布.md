
---
title: 'MyExcel 3.11.3 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 09:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂Excel）以及读取Excel变得极为便利，且构建、读取性能极为优异，占用内存极低（具体，请移步参考<a href="https://www.oschina.net/news/113304/myexcel-3-4-rc2-released">MyExcel&阿里EasyExcel性能对比</a>）。</p> 
<p style="text-align:left">如导入：</p> 
<pre style="text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd.class)
        .sheet(0) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > 0) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .beanFilter(ArtCrowd::isDance) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// bean过滤</span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path.toFile());</code></pre> 
<p><strong>本次更新点如下：</strong></p> 
<ul> 
 <li><span style="color:#e74c3c">修复在极少数情况下，</span><span style="color:#e74c3c">Sax读取，</span><span style="color:#e74c3c">字符串缓存数组越界问题（<strong>强烈建议升级修复</strong>）；</span></li> 
 <li>@ExcelColumn支持提示prompt；</li> 
 <li>HTML模板导出，新增sheetStrategy策略方法，多table可在同一sheet导出；</li> 
 <li>其他代码优化；</li> 
</ul> 
<p>感谢<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FQingMings" target="_blank">@</a><span style="background-color:#ffffff; color:#586069"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FQingMings" target="_blank">QingMings</a> 提供</span>sheetStrategy策略PR！！！</p> 
<p>具体，请移步文档<span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#e74c3c">================分割线================</span></strong></p> 
<p>昨天花了一段时间来清理issues，说实话很惭愧，里面有不少问题是很久之前提出的，或者提出后我回复了一次就没有再次回复的，时隔这么久，再做答复可能意义也不大了，需要向信任MyExcel，但为此遇到麻烦的同学道歉。</p> 
<p>下面针对两个主要被问及关心的问题做下统一答复，方便使用MyExcel的同学做出选择：</p> 
<p><strong>1.MyExcel会不会提供Excel模板导入导出功能？什么时候能提供？</strong></p> 
<p>答：这个问题其实从MyExcel创建之初（2019年底）就有同学问过，当时的答复是肯定会有，现在的答复依然是肯定会有，但是我无法给出一个具体的时间。</p> 
<p>原因有多个方面，<strong>一方面</strong>是MyExcel的核心能力（<strong>海量数据导入导出，高复杂度表单导出</strong>）目前仍未处于稳定状态，还有很多特性需要开发，对于Excel模板导入导出已有其他很多优秀的工具包可以协同支持，所以MyExcel短时间内不会将精力花在这上面；<strong>另一方面</strong>是个人精力，很高兴看到现在有越来越多的同学加入MyExcel的开源，但大部分情况下还是个人在独立维护（即使是大公司层面的开源作品，大部分也是很少的人在维护，这是无情的现状～），MyExcel的开源纯属于个人兴趣爱好，是没有收入的，所以无法全心全意的进行开发维护，基本都是工作之外或者牺牲周末的时间来开发迭代，结合第一点原因，这个能够完成的时间点就无法较为精准的提供。</p> 
<p>当然，MyExcel的目标是能够解决现实业务场景百分之九十的问题，Excel模板导入导出肯定是需要提供的。</p> 
<p><img height="800" src="https://oscimg.oschina.net/oscnet/up-9de1211883868c6bb4367b3815340de2532.png" width="744" referrerpolicy="no-referrer"></p> 
<p><strong>2.MyExcel什么时候升级到POI 5.0版本？</strong></p> 
<p>答：相信大部分同学注意到了，POI官方团队在21年1月20号发布了POI 5.0.0版本，该版本升级了多个依赖，性能、安全性会有一个提升。那么MyExcel什么时候会升级到5.0.0版本呢？</p> 
<p>还是无法给出一个具体的时间点，但大概率会是下半年，之所以会延迟这么久，原因在于MyExcel升级到5.0.0版本后，做功能回归时，发现有些功能（图片、水印等）无法正常运行，而且从官方文档中没有找到解决办法，为了降低升级版本可能导致的问题，所以升级版本需要延迟到5.0版本的修复版本发布。</p> 
<p><span style="color:#e74c3c"><strong>如果有同学</strong></span><span style="color:#e74c3c"><strong>想要使用MyExcel</strong></span><span style="color:#e74c3c"><strong>，务必要关注上述这两个问题，以免带来不必要的麻烦哦！！！</strong></span></p>
                                        </div>
                                      
</div>
            