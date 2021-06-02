
---
title: '服务端表格组件 GCExcel 发布更新，大幅提升 Excel 模板处理性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a47cd14a4b6878aea7db6a348b76d2e56b0.gif'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 09:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a47cd14a4b6878aea7db6a348b76d2e56b0.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:white"><span style="color:#555555">GrapeCity Documents for Excel </span></span><span style="background-color:white"><span style="color:#555555">（简称：GcExcel）是一款基于 Java 平台的服务端高性能表格组件，可与 </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fspreadjs" target="_blank"><span style="background-color:white"><span style="color:#2676c0">纯前端表格控件 SpreadJS</span></span></a> <span style="background-color:white"><span style="color:#555555">前后端兼容，无需依赖 Office、POI 或第三方应用软件，在前端展示电子表格数据，在服务端批量创建、加载、编辑、打印、导入/导出 Excel 文档，为您开发的应用程序提供在线文档的前后端数据同步、在线填报与服务端批量导出与打印，以及类 Excel 报表模板设计与服务端高性能处理等一整套 </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fsheet" target="_blank"><span style="background-color:white"><span style="color:#2676c0">类 Excel </span></span><span style="background-color:white"><span style="color:#2676c0">全栈解决方案</span></span></a><span style="background-color:white"><span style="color:#555555">。</span></span></p> 
<p><span style="background-color:white"><span style="color:#555555">近日，服务端表格组件 GcExcel  V4.0 Update1发布更新，本次发布，产品更专注于增强现有的功能集和性能指标，并针对Excel模板处理性能进行了优化。</span></span></p> 
<p><span style="background-color:white"><span style="color:#555555">以下是本次更新的主要内容：</span></span></p> 
<h2>Excel 模板处理性能大幅提升</h2> 
<p><span style="background-color:white"><span style="color:#555555">GcExcel  </span></span>从模板生成Excel文档的速度比以往更快，在处理多个数据源记录时更加高效，且随着记录数量的增加，将模板生成到最终报告中的速度也会增加。</p> 
<p>以下是<span style="background-color:white"><span style="color:#555555">GcExcel  </span></span><span style="background-color:white"><span style="color:#555555">处理</span></span>100,000条记录的性能测试报告：</p> 
<p><img alt height="759" src="https://oscimg.oschina.net/oscnet/up-a47cd14a4b6878aea7db6a348b76d2e56b0.gif" width="1200" referrerpolicy="no-referrer"></p> 
<p>如下是<span style="background-color:white"><span style="color:#555555">GcExcel  </span></span><span style="background-color:white"><span style="color:#555555">的</span></span>性能指标对比（相对上一个版本）</p> 
<p><img alt height="277" src="https://oscimg.oschina.net/oscnet/up-2e54b094c25d8151a707007e3c724af62aa.png" width="752" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2>增加与前端表格控件 SpreadJS 的更多功能支持</h2> 
<p>SpreadJS 和 GcExcel 结合使用，可在不依赖 Office、POI 和第三方软件的情况下，满足在线文档的前后端数据同步、在线填报与服务端批量导出与打印，以及类 Excel 报表模板设计与服务端高性能处理等功能，为您开发的应用程序提供整套类 Excel 全栈解决方案。</p> 
<p>因此，每一次版本升级，GcExcel都将与纯前端表格控件 SpreadJS 的产品兼容性作为前提，并时刻保持对 SpreadJS 的产品功能兼容性支持。</p> 
<p>本次更新，GcExcel增加的与 SpreadJS 功能支持包括：</p> 
<p>1. 支持RangeTemplate单​​元格类型</p> 
<p>2. 在CheckboxList和RadioButtonList单元格类型上应用自定义对象</p> 
<p>3. 工作簿元素的ToJson和FromJSON方法</p> 
<p>4. 获取并将自定义对象设置为单元格值</p> 
<p> </p> 
<p> </p> 
<h2>其他功能更新：</h2> 
<p>1. GcExcel支持将公式字符串解析为语法树：即可将公式表达式解析为语法树，以便直接创建、解析和修改公式。</p> 
<p>2. GcExcel在保存Excel文件时可忽略公式。</p> 
<p>3. GcExcel增加了全新的加载JSON重载方法。</p> 
<p>4. 改进了GcExcel设置值时的计算引擎性能。</p> 
<p> </p> 
<p><span style="background-color:white"><span style="color:#555555">以上就是服务端表格组件GrapeCity Documents for Excel（GcExcel） V4.0 Update1的主要功能介绍，如需了解更多新版本信息，欢迎访问</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fgrapecitydocuments%2Fexcel-java" target="_blank"><span style="background-color:white"> GcExcel</span><span style="background-color:white">产品官网</span></a><span style="background-color:white"><span style="color:#555555">。</span></span></p>
                                        </div>
                                      
</div>
            