
---
title: 'Excelize 发布 2.6.1 版本更新，支持工作簿加密保护'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-efe1db7589e8603f1b37d26a16c64c582ba.png'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 08:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-efe1db7589e8603f1b37d26a16c64c582ba.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img alt="Excelize 发布 2.6.1 版本更新" height="332" src="https://oscimg.oschina.net/oscnet/up-efe1db7589e8603f1b37d26a16c64c582ba.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">Excelize</a><span> </span>是 Go 语言编写的用于操作 Office Excel 文档基础库，基于 ECMA-376，ISO/IEC 29500 国际标准。可以使用它来读取、写入由 Microsoft Excel™ 2007 及以上版本创建的电子表格文档。支持 XLSX / XLSM / XLTM 等多种文档格式，高度兼容带有样式、图片 (表)、透视表、切片器等复杂组件的文档，并提供流式读写 API，用于处理包含大规模数据的工作簿。可应用于各类报表平台、云计算、边缘计算等系统。入选 2020 Gopher China - Go 领域明星开源项目 (GSP)、2018 年开源中国码云最有价值开源项目<span> </span><a href="https://gitee.com/xurime/excelize">GVP</a>(Gitee Most Valuable Project)，目前已成为 Go 语言最受欢迎的 Excel 文档基础库。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">开源代码</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>GitHub:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">github.com/xuri/excelize</a></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>Gitee:</strong><span> </span><a href="https://gitee.com/xurime/excelize">gitee.com/xurime/excelize</a></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><strong>中文文档:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize%2Fzh-hans%2F" target="_blank">xuri.me/excelize/zh-hans</a></p> 
<p style="color:#24292e; text-align:start">2022年8月22日，社区正式发布了 2.6.1 版本，该版本包含了多项新增功能、错误修复和兼容性提升优化。下面是有关该版本更新内容的摘要，完整的更改列表可查看<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize%2Fcompare%2Fv2.6.0...v2.6.1" target="_blank">changelog</a>。</p> 
<p style="color:#24292e; text-align:start">此版本中最显著的变化包括：</p> 
<h3 style="text-align:start">兼容性提示</h3> 
<ul> 
 <li>重命名导出类型<span> </span><code>TabColor</code><span> </span>为<span> </span><code>TabColorRGB</code></li> 
 <li>重命名导出常量<span> </span><code>TotalColumns</code><span> </span>为<span> </span><code>MaxColumns</code></li> 
 <li>重命名导出变量<span> </span><code>ErrMaxFileNameLength</code><span> </span>为<span> </span><code>ErrMaxFilePathLength</code></li> 
 <li>重命名导出变量<span> </span><code>ErrWorkbookExt</code><span> </span>为<span> </span><code>ErrWorkbookFileFormat</code></li> 
 <li>移除了导出变量<span> </span><code>ErrEncrypt</code></li> 
 <li>工作表名称不再区分大小写</li> 
</ul> 
<h3 style="text-align:start">新增功能</h3> 
<ul> 
 <li>新增 34 项公式函数: CONVERT, COVARIANCE.S, DAVERAGE, DAYS360, DCOUNT, DCOUNTA, DGET, DMAX, DMIN, DPRODUCT, DSTDEV, DSTDEVP, DSUM, DVAR, DVARP, EDATE, EOMONTH, EUROCONVERT, GROWTH, HYPERLINK, MINVERSE, MMULT, NETWORKDAYS, NETWORKDAYS.INTL, PEARSON, RSQ, SKEW.P, SLOPE, STDEVPA, STEYX, TREND, WEEKNUM, WORKDAY, WORKDAY.INTL</li> 
 <li>新增<span> </span><code>DeleteComment</code><span> </span>函数支持删除单元格批注，相关 issue #849</li> 
 <li>通过<span> </span><code>AddShape</code><span> </span>函数添加形状时支持指定宏</li> 
 <li>新增对 1900 和 1904 日期系统的支持，相关 issue #1212</li> 
 <li>新增更新超链接支持，相关 issue #1217</li> 
 <li>通过<span> </span><code>AddPicture</code><span> </span>添加图片时，现已允许插入 EMF、WMF、EMZ 和 WMZ 格式图片，相关 issue #1225</li> 
 <li>优化打开工作簿失败时的错误提示信息，新增导出变量<span> </span><code>ErrWorkbookPassword</code><span> </span>定义了打开工作簿时密码验证失败的错误提示信息，以便开发者可根据不同的错误类型进行采取相应处理</li> 
 <li>新增导出常量<span> </span><code>MinFontSize</code>、<code>MinColumns</code><span> </span>和<span> </span><code>MaxCellStyles</code><span> </span>以定义最小字号、最小列号和单元格样式数量上限</li> 
 <li>公式引擎新增数组公式支持</li> 
 <li>支持根据给定的密码对工作簿进行加密保护，相关 issue #199</li> 
 <li>设置单元格富文本格式时，支持通过指定 RichTextRun 中的 vertAlign 属性设置上标和下标</li> 
 <li>通过<span> </span><code>DeleteDataValidation</code><span> </span>函数删除数据验证时，支持省略第二个引用区域参数以删除工作表中的全部数据验证，相关 issue #1254</li> 
 <li>公式计算引擎支持带有百分比符号的条件比较表达式</li> 
 <li>公式计算引擎支持依赖依赖公式计算，相关 issue #1262</li> 
 <li>新增文档打开选项<span> </span><code>MaxCalcIterations</code><span> </span>以支持指定公式迭代计算的最多迭代次数</li> 
 <li>新增导出类型<span> </span><span> </span><code>ColorMappingType</code><span> </span>以定义颜色转换枚举类型</li> 
 <li>插入或删除行列时支持自动调整表格区域</li> 
 <li>支持设置与获取工作表标签颜色索引、主题和色调，相关 issue #1283</li> 
 <li>行迭代器新增函数<span> </span><code>GetRowOpts</code><span> </span>支持读取行属性，相关 issue #1296</li> 
</ul> 
<h3 style="text-align:start">兼容性提升</h3> 
<ul> 
 <li>提升与内部包含无效样式计数工作簿的兼容，解决 issue #1211</li> 
 <li>提升与 Google Sheet 的兼容性，解决 issue #1244 和 #1314</li> 
 <li>流式写入器将不再为值为 nil 的单元格写入工作表，解决 issue #1299</li> 
</ul> 
<h3 style="text-align:start">问题修复</h3> 
<ul> 
 <li>修复当数据透视表中值区间与行/列区间包含相同字段时，生成的工作簿损坏问题，解决 issue #1203</li> 
 <li>修复因缺少单元格类型检查导致的获取单元格富文本内容异常问题，解决 issue #1213</li> 
 <li>修复读取单元格值时，因单元格类型推断错误导致的读取结果异常问题，解决 issue #1219</li> 
 <li>修复读取带有 0 占位符数字格式表达式样式的单元格时，值为空的问题，解决 #1312 和 #1313</li> 
 <li>修复部分情况下设置单元格值时，单元格继承行列样式有误的问题，解决 issue #1163</li> 
 <li>修复在不包含视图属性设置的工作表中设置窗格时将出现 panic 的问题</li> 
 <li>修复部分情况下公式引擎多参数公式计算结果有误的问题</li> 
 <li>修复因内部页眉页脚属性定义顺序有误导致的生成工作簿损坏问题，解决 issue #1257</li> 
 <li>修复部分情况下单元格赋值失效的问题，解决 issue #1264</li> 
 <li>修复设置工作表视图属性时可能出现的 panic</li> 
 <li>修复部分情况下因工作表核心属性中 dcterms 属性为空，导致生成的工作簿损坏问题</li> 
 <li>修复新建工作表后工作簿属性丢失问题，解决 issue #1298</li> 
</ul> 
<h3 style="text-align:start">性能优化</h3> 
<ul> 
 <li>提高按行赋值和合并单元格的性能，恢复因修复 issue #1129 时导致的性能下降</li> 
 <li>优化了公式计算引擎的性能</li> 
 <li>降低<span> </span><code>AddComment</code><span> </span>添加批注时的内存开销并减少耗时，解决 issue #1310</li> 
</ul> 
<h3 style="text-align:start">其他</h3> 
<ul> 
 <li>Go Modules 依赖模块更新</li> 
 <li>单元测试与文档更新，修复单元测试在 go1.19 下的兼容性问题</li> 
 <li>包含简体中文、英语、法语、俄语、日语、韩语、阿拉伯语、德语和西班牙语的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxuri.me%2Fexcelize" target="_blank">多国语言文档网站</a>更新</li> 
</ul> 
<h3 style="text-align:start">致谢</h3> 
<p style="color:#24292e; text-align:start">感谢 Excelize 的所有贡献者，以下是为此版本提交代码的贡献者列表：</p> 
<ul> 
 <li>@JDavidVR (David)</li> 
 <li>@sceneq</li> 
 <li>@Juneezee (Eng Zer Jun)</li> 
 <li>@MichealJl (jialei)</li> 
 <li>@ww1516123</li> 
 <li>@z-hua (z.hua)</li> 
 <li>@xdlrt (yeshu)</li> 
 <li>@eaglexiang (Eagle Xiang)</li> 
 <li>@MJacred</li> 
 <li>@ReganYue (Regan Yue)</li> 
 <li>@thomascharbonnel (Thomas Charbonnel)</li> 
 <li>@ee0703 (EE)</li> 
 <li>@NaturalGao (NaturalGao)</li> 
 <li>@Sangua633</li> 
</ul>
                                        </div>
                                      
</div>
            