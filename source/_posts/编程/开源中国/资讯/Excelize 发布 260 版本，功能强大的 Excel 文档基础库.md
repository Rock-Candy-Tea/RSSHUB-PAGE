
---
title: 'Excelize 发布 2.6.0 版本，功能强大的 Excel 文档基础库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bd35868e434366c093343872cef9f06f18b.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 09:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bd35868e434366c093343872cef9f06f18b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292e; margin-left:0px; margin-right:0px; text-align:center"><img alt="Excelize 发布 2.6.0 版本，功能强大的 Excel 文档基础库" height="292" src="https://oscimg.oschina.net/oscnet/up-bd35868e434366c093343872cef9f06f18b.png" width="440" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">Excelize</a><span> </span>是 Go 语言编写的用于操作 Office Excel 文档基础库，基于 ECMA-376，ISO/IEC 29500 国际标准。可以使用它来读取、写入由 Microsoft Excel™ 2007 及以上版本创建的电子表格文档。支持 XLSX / XLSM / XLTM 等多种文档格式，高度兼容带有样式、图片(表)、透视表、切片器等复杂组件的文档，并提供流式读写 API，用于处理包含大规模数据的工作簿。可应用于各类报表平台、云计算、边缘计算等系统。入选 2020 Gopher China - Go 领域明星开源项目(GSP)、2018 年开源中国码云最有价值开源项目<span> </span><a href="https://gitee.com/xurime/excelize">GVP</a>(Gitee Most Valuable Project)，目前已成为 Go 语言最受欢迎的 Excel 文档基础库。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">开源代码</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>GitHub:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">github.com/xuri/excelize</a></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>Gitee:</strong><span> </span><a href="https://gitee.com/xurime/excelize">gitee.com/xurime/excelize</a></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>中文文档:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize%2Fzh-hans%2F" target="_blank">xuri.me/excelize/zh-hans</a></p> 
<p style="color:#24292e; text-align:start">2022年4月11日，社区正式发布了 2.6.0 版本，该版本包含了多项新增功能、错误修复和兼容性提升优化。下面是有关该版本更新内容的摘要，完整的更改列表可查看<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize%2Fcompare%2Fv2.5.0...v2.6.0" target="_blank">changelog</a>。</p> 
<p style="color:#24292e; text-align:start">此版本中最显著的变化包括：</p> 
<h3 style="text-align:start">兼容性提示</h3> 
<ul> 
 <li>重命名导出常量<span> </span><code>NameSpaceDublinCoreMetadataIntiative</code><span> </span>为<span> </span><code>NameSpaceDublinCoreMetadataInitiative</code><span> </span>以修复拼写错误</li> 
 <li>重命名导出变量<span> </span><code>ErrUnsupportEncryptMechanism</code><span> </span>为<span> </span><code>ErrUnsupportedEncryptMechanism</code></li> 
 <li>重命名导出变量<span> </span><code>ErrDataValidationFormulaLenth</code><span> </span>为<span> </span><code>ErrDataValidationFormulaLength</code></li> 
 <li>重命名导出变量<span> </span><code>ErrDefinedNameduplicate</code><span> </span>为<span> </span><code>ErrDefinedNameDuplicate</code></li> 
 <li>移除了导出变量<span> </span><code>XMLHeaderByte</code></li> 
 <li>移除了设置数据数据验证列表函数<span> </span><code>SetSqrefDropList</code><span> </span>的第二个形参<span> </span><code>isCurrentSheet</code><span> </span>和异常返回值</li> 
 <li>移除了行迭代器中的导出字段<span> </span><code>TotalRows</code></li> 
</ul> 
<h3 style="text-align:start">新增功能</h3> 
<ul> 
 <li><code>ProtectSheet</code><span> </span>新增支持通过指定的算法保护工作表，支持的算法包括: XOR、MD4、MD5、SHA1、SHA256、SHA384 和 SHA512</li> 
 <li><code>UnprotectSheet</code><span> </span>支持通过指定第二个可选参数在移除工作表保护时验证密码</li> 
 <li>新增 71 项公式函数: AVERAGEIFS, BETADIST, BETA.DIST, BETAINV, BETA.INV, BINOMDIST, BINOM.DIST, BINOM.DIST.RANGE, BINOM.INV, CHIINV, CHITEST, CHISQ.DIST, CHISQ.DIST.RT, CHISQ.INV, CHISQ.INV.RT, CHISQ.TEST, CONFIDENCE.T, CORREL, COVAR, COVARIANCE.P, CRITBINOM, ERROR.TYPE, EXPON.DIST, EXPONDIST, F.DIST, F.DIST.RT, FDIST, F.INV, F.INV.RT, FINV, FORMULATEXT, F.TEST, FTEST, GAMMA.DIST, GAMMADIST, GAMMA.INV, GAMMAINV, GAMMALN.PRECISE, GAUSS, HOUR, HYPGEOM.DIST, HYPGEOMDIST, INDIRECT, LOGINV, LOGNORM.DIST, LOGNORMDIST, LOGNORM.INV, MODE, MODE.MULT, MODE.SNGL, NEGBINOM.DIST, NEGBINOMDIST, PHI, SECOND, SERIESSUM, SUMIFS, SUMPRODUCT, SUMX2MY2, SUMX2PY2, SUMXMY2, T.DIST, T.DIST.2T, T.DIST.RT, TDIST, TIMEVALUE, T.INV, T.INV.2T, TINV, T.TEST, TTEST, TYPE</li> 
 <li>保存或另存为工作簿时增加对文件扩展名进行检查</li> 
 <li>支持设置工作簿视图模式和显示/隐藏标尺</li> 
 <li>引入依赖库 NFP (number format parser) 以增加对自定义时间、日期和文本类型数字格式的支持，可对包含 19 种语言（南非荷兰语、孟加拉语、汉语、英语、法语、德语、奥地利语、爱尔兰语、意大利语、俄语、西班牙语、泰语、藏语、土耳其语、威尔士语、沃洛夫语、科萨语、彝语和祖鲁语）本地月份名称和 12 小时制格式的数字格式表达式进行解析，相关 issues #660, #764, #1093, #1112 和 #1133</li> 
 <li>新增 API:<span> </span><code>SetWorkbookPrOptions</code><span> </span>和<span> </span><code>GetWorkbookPrOptions</code><span> </span>支持设置和获取工作簿中的<span> </span><code>FilterPrivacy</code><span> </span>与<span> </span><code>CodeName</code><span> </span>属性，以解除部分情况下向工作簿中嵌入 VBA 工程时的限制，相关 issue #1148</li> 
 <li>公式计算引擎支持中缀运算符后包含无参数公式函数的计算</li> 
 <li>支持以文本形式读取布尔型单元格的值</li> 
 <li>通过<span> </span><code>AddChart</code><span> </span>函数添加圆环图时，支持指定圆环图内径大小，解决 issue #1172</li> 
 <li>新增导出 4 项错误信息<span> </span><code>ErrPasswordLengthInvalid</code>,<span> </span><code>ErrUnsupportedHashAlgorithm</code>,<span> </span><code>ErrUnsupportedNumberFormat</code>,<span> </span><code>ErrWorkbookExt</code>，以便开发者可根据不同的错误类型进行采取相应处理</li> 
</ul> 
<h3 style="text-align:start">兼容性提升</h3> 
<ul> 
 <li>提升与 LibreOffice 电子表格应用程序的兼容性，修复在 LibreOffice 中打开的工作表名包含空格时，自动过滤器失效的问题，解决 issue #1122</li> 
 <li>提升对工作簿中替代内容的支持，保留工作簿、工作表以及 drawingML 中的替代内容</li> 
 <li>提升与页面设置中打印质量 DPI 设置属性的兼容性</li> 
</ul> 
<h3 style="text-align:start">问题修复</h3> 
<ul> 
 <li>修复另存为工作簿时，页面布局属性丢失的问题，解决 issue #1117</li> 
 <li>修复部分情况下，对工作表进行修改后合并单元格区域未更新的问题</li> 
 <li>修复样式解析异常导致的粗体和部分其他字体样式丢失问题，解决 issue #1119</li> 
 <li>修复部分情况下将文档保存为 XLAM / XLSM / XLTM / XLTX 格式后文档损坏的问题</li> 
 <li>单元格样式支持继承行/列样式，以修复对工作表进行修改后合并单元格区域单元格样式不正确的问题，解决 issue #1129</li> 
 <li>修复部分情况下获取单元格样式 ID 错误的问题</li> 
 <li>修复编号为 42 的内建数字格式定义错误的问题</li> 
 <li>修复部分情况下数字精度解析错误的问题</li> 
 <li><code>SetCellDefault</code><span> </span>支持设置非数字类型单元格的值，解决 issue #1139</li> 
 <li>修复部分情况下另存为工作簿时，显示或隐藏工作表标签属性丢失的问题，解决 issue #1160</li> 
 <li>修复部分情况下嵌套公式计算错误的问题，解决 issue #1164</li> 
 <li>修复部分情况下公式计算结果精度不准确以及在 x86 和 arm64 架构 CPU 下公式计算结果精度不一致的问题</li> 
 <li>修复部分情况下使用科学记数法表示的数值解析失败的问题</li> 
 <li>修复图表轴最大值最小值为 0 时不起作用的问题</li> 
</ul> 
<h3 style="text-align:start">性能优化</h3> 
<ul> 
 <li>提高使用行迭代器进行流式读取的性能，当读取包含大规模数据的电子表格文档时，内存开销相较于上一版本降低最高约 50%，内存垃圾回收次数降低约 80%</li> 
</ul> 
<h3 style="text-align:start">其他</h3> 
<ul> 
 <li>Go Modules 依赖模块更新</li> 
 <li>单元测试与文档更新</li> 
 <li>包含简体中文、英语、法语、俄语、日语、韩语、阿拉伯语、德语和西班牙语的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize" target="_blank">多国语言文档网站</a>更新</li> 
</ul>
                                        </div>
                                      
</div>
            