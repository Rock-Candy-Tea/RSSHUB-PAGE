
---
title: 'Excelize 2.5.0 正式发布，这些新增功能值得关注'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fc2937b21ee2760d3a7809f2f192bfd194f.png'
author: 开源中国
comments: false
date: Mon, 03 Jan 2022 11:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fc2937b21ee2760d3a7809f2f192bfd194f.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img alt="Excelize 2.5.0 正式发布" height="292" src="https://oscimg.oschina.net/oscnet/up-fc2937b21ee2760d3a7809f2f192bfd194f.png" width="440" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">Excelize</a><span> </span>是 Go 语言编写的用于操作 Office Excel 文档基础库，基于 ECMA-376，ISO/IEC 29500 国际标准。可以使用它来读取、写入由 Microsoft Excel™ 2007 及以上版本创建的电子表格文档。支持 XLSX / XLSM / XLTM 等多种文档格式，高度兼容带有样式、图片(表)、透视表、切片器等复杂组件的文档，并提供流式读写 API，用于处理包含大规模数据的工作簿。可应用于各类报表平台、云计算、边缘计算等系统。入选 2020 Gopher China - Go 领域明星开源项目(GSP)、2018 年开源中国码云最有价值开源项目<span> </span><a href="https://gitee.com/xurime/excelize">GVP</a>(Gitee Most Valuable Project)，目前已成为 Go 语言最受欢迎的 Excel 文档基础库。</p> 
<h2 style="text-align:start">开源代码</h2> 
<p style="color:#24292e; text-align:start"><strong>GitHub:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">github.com/xuri/excelize</a></p> 
<p style="color:#24292e; text-align:start"><strong>Gitee:</strong><span> </span><a href="https://gitee.com/xurime/excelize">gitee.com/xurime/excelize</a></p> 
<p style="color:#24292e; text-align:start"><strong>中文文档:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize%2Fzh-hans%2F" target="_blank">xuri.me/excelize/zh-hans</a></p> 
<p style="color:#24292e; text-align:start">2022年1月3日，社区正式发布了 2.5.0 版本，该版本包含了多项新增功能、错误修复和兼容性提升优化。此版本中最显著的变化包括：</p> 
<h3 style="text-align:start">兼容性提示</h3> 
<ul> 
 <li>打开已有工作簿或在获取行迭代器后，需要调用对应的<span> </span><code>Close</code><span> </span>函数关闭工作簿和数据流</li> 
 <li>修改<span> </span><code>ReadZipReader</code><span> </span>为<span> </span><code>File</code><span> </span>的实现, 支持通过选项指定解压至内存或文件系统</li> 
 <li>移除了不必要的导出变量<span> </span><code>XMLHeader</code>，可使用<span> </span><code>encoding/xml</code><span> </span>包的<span> </span><code>xml.Header</code><span> </span>代替</li> 
 <li>移除了不再使用的导出变量<span> </span><code>ErrToExcelTime</code></li> 
</ul> 
<h3 style="text-align:start">新增功能</h3> 
<ul> 
 <li>新增 API:<span> </span><code>SetRowStyle</code><span> </span>支持设置整行样式, 相关 issue #990</li> 
 <li>新增 API:<span> </span><code>GetCellType</code><span> </span>支持获取单元格数据类型, 相关 issue #417 和 #520</li> 
 <li>新增 API:<span> </span><code>SetAppProps</code><span> </span>和<span> </span><code>GetAppProps</code><span> </span>支持设置与获取工作簿应用程序属性, 相关 issue #1095</li> 
 <li><code>GetCellValue</code>,<span> </span><code>GetRows</code>,<span> </span><code>GetCols</code>,<span> </span><code>Rows</code><span> </span>和<span> </span><code>Cols</code><span> </span>支持指定是否读取单元格原始值而不应用数字格式表达式, 相关 issue #621</li> 
 <li>新增 95 项公式函数: ACCRINT, ACCRINTM, ADDRESS, AMORDEGRC, AMORLINC, AVEDEV, AVERAGEIF, CHIDIST, CONFIDENCE, CONFIDENCE.NORM, COUNTIF, COUNTIFS, COUPDAYBS, COUPDAYS, COUPDAYSNC, COUPNCD, COUPNUM, COUPPCD, DATEVALUE, DAY, DAYS, DELTA, DEVSQ, DISC, DURATION, ERF, ERF.PRECISE, ERFC, ERFC.PRECISE, GEOMEAN, GESTEP, IFNA, IFS, INDEX, INTRATE, ISFORMULA, ISLOGICAL, ISREF, ISOWEEKNUM, MATCH, MAXA, MAXIFS, MDURATION, MINIFS, MINUTE, MONTH, ODDFPRICE, PERCENTILE.EXC, PERCENTRANK.EXC, PERCENTRANK.INC, PERCENTRANK, PRICE, PRICEDISC, PRICEMAT, PV, QUARTILE.EXC, RANK, RANK.EQ, RATE, RECEIVED, RRI, SHEETS, SLN, STANDARDIZE, STDEV.P, STDEVP, SWITCH, SYD, TBILLEQ, TBILLPRICE, TBILLYIELD, TEXTJOIN, TIME, TRANSPOSE, TRIMMEAN, VALUE, VAR, VAR.S, VARA, VARPA, VDB, WEEKDAY, WEIBULL, WEIBULL.DIST, XIRR, XLOOKUP, XNPV, XOR, YEAR, YEARFRAC, YIELD, YIELDDISC, YIELDMAT, Z.TEST, ZTEST, 相关 issue #65 和 #1002</li> 
 <li>公式计算引擎支持嵌套<span> </span><code>IF</code><span> </span>函数, 相关 issue #987</li> 
 <li>公式计算引擎支持共享公式, 相关 issue #844</li> 
 <li>公式计算引擎支持文本比较运算, 相关 issue #998</li> 
 <li>支持在数据验证中使用公式, 相关 issue #1012</li> 
 <li>支持文档压缩比限制，避免潜在的安全风险</li> 
 <li><code>SetCellFormula</code><span> </span>支持设置共享公式</li> 
 <li><code>UpdateLinkedValue</code><span> </span>在清除单元格计算缓存时将跳过 macro sheet, 相关 issue #1014</li> 
 <li>修复部分情况下，由于内部依赖关系计算错误导致的<span> </span><code>AddPicture</code><span> </span>重复创建图片的问题, 相关 issue #1017</li> 
 <li><code>AddShape</code><span> </span>支持设置形状轮廓线条宽度, 相关 issue #262</li> 
 <li>新增文档打开选项<span> </span><code>UnzipXMLSizeLimit</code><span> </span>以支持指定打开每个工作表以及共享字符表时的内存解压上限</li> 
 <li>创建样式时，若给定的自定义数字格式无效，将返回错误提示，相关 issue #1028</li> 
 <li>流式写入现已支持设置行样式</li> 
 <li>流式写入器将为时间类型单元格创建时间数字格式样式，相关 issue #1107</li> 
 <li>支持设置数据透视表报表布局“以压缩形式显示”或“以大纲形式显示”, 相关 issue #1029</li> 
 <li>行/列迭代器支持获取当前行/列序号和行/列总数, 相关 issue #1054</li> 
 <li>使用 time.Time 类型参数进行单元格赋值时，支持时区位置, 相关 issue #1069</li> 
 <li>新增导出 7 项错误信息，以便开发者可根据不同的错误类型进行采取相应处理</li> 
</ul> 
<h3 style="text-align:start">兼容性提升</h3> 
<ul> 
 <li>提升与内部带有<span> </span><code>r="0"</code><span> </span>属性工作表的兼容性</li> 
 <li>保留 XML 控制字符</li> 
 <li>提升样式设置与 Apple Numbers 的兼容性, 相关 issue #1059</li> 
 <li>页眉页脚字符数限制兼容多字节字符, 相关 issue #1061</li> 
 <li>设置单元格时将保留水平制表符, 相关 issue #1108</li> 
</ul> 
<h3 style="text-align:start">问题修复</h3> 
<ul> 
 <li>修复部分情况下删除数据验证失败的问题, 解决 issue #979</li> 
 <li>修复部分情况下设置数据验证下拉列表失败的问题, 解决 issue #986</li> 
 <li>修复公式计算引擎<span> </span><code>LOOKUP</code><span> </span>函数部分情况下计算结果错误的问题, 解决 issue #994</li> 
 <li>修复公式计算引擎<span> </span><code>LOOKUP</code><span> </span>仅支持完全匹配的问题, 解决 issue #997</li> 
 <li>修复公式计算引擎百分比计算错误的问题, 解决 issue #993</li> 
 <li>修复特定情况下单元格读取异常导致的 panic</li> 
 <li>修复设置“后 N 项”条件格式失败的问题</li> 
 <li>修复部分情况下时间解析错误的问题, 解决 issue #1026 和 #1030</li> 
 <li>修复科学记数法数字格式的单元格值解析异常的问题，解决 issue #1027</li> 
 <li>修复部分情况下浮点型数据读取异常的问题，解决 issue #1031</li> 
 <li>修复部分情况下删除工作表失败的问题</li> 
 <li>修复内建时间数字格式解析异常问题，解决 issue #1060</li> 
 <li>修复部分情况下新建样式时返回样式 ID 异常的问题</li> 
 <li>修复部分情况下删除行列后合并单元格区域异常的问题</li> 
</ul> 
<h3 style="text-align:start">性能优化</h3> 
<ul> 
 <li>合并单元格性能大幅提升，耗时降低 90%</li> 
 <li>提高流式读取性能，当内部 XML 较大时，将共享字符串表解压缩到系统临时文件，内存使用量减少约 60%, 相关 issue #109</li> 
 <li>优化读取工作表列表性能</li> 
 <li>优化设置列样式存储，缩小生成的文档体积，解决 issue #1057</li> 
</ul> 
<h3 style="text-align:start">其他</h3> 
<ul> 
 <li>Go Modules 依赖模块更新</li> 
 <li>单元测试与文档更新</li> 
 <li>包含简体中文、英语、法语、俄语、日语、韩语、阿拉伯语、德语和西班牙语的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize" target="_blank">多国语言文档网站</a>更新</li> 
</ul>
                                        </div>
                                      
</div>
            