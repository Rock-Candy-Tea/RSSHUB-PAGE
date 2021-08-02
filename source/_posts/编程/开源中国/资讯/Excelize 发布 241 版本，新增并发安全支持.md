
---
title: 'Excelize 发布 2.4.1 版本，新增并发安全支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f35c4f635e7ce77da58e08213c4837e126a.JPEG'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 00:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f35c4f635e7ce77da58e08213c4837e126a.JPEG'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img alt height="253" src="https://oscimg.oschina.net/oscnet/up-f35c4f635e7ce77da58e08213c4837e126a.JPEG" width="450" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize" target="_blank">Excelize</a><span style="background-color:#ffffff; color:#333333"> 是 Go 语言编写的用于操作 Office Excel 文档基础库，基于 ECMA-376，ISO/IEC 29500 国际标准。可以使用它来读取、写入由 Microsoft Excel™ 2007 及以上版本创建的电子表格文档。支持 XLSX / XLSM / XLTM 等多种文档格式，高度兼容带有样式、图片(表)、透视表、切片器等复杂组件的文档，并提供流式读写 API，用于处理包含大规模数据的工作簿。可应用于各类报表平台、云计算、边缘计算等系统。</span><span style="background-color:#ffffff; color:#333333">入选 2020 Gopher China - Go 领域明星开源项目 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FXyLAaqpN-3urYcNmM_vPeg" target="_blank">GSP</a><span style="background-color:#ffffff; color:#333333">)、</span><span style="background-color:#ffffff; color:#333333">2018 开源中国码云 </span><a href="https://gitee.com/xurime/excelize">Gitee 最有价值开源项目 GVP</a><span style="background-color:#ffffff; color:#333333">，目前已成为 Go 语言最受欢迎的 Excel 文档基础库。</span></p> 
<p><span style="background-color:#ffffff; color:#000000">Gitee: </span><a href="https://gitee.com/xurime/excelize">gitee.com/xurime/excelize</a></p> 
<p><span style="background-color:#ffffff; color:#000000">2021年8月2日，社区正式发布了 2.4.1 版本，该版本包含了多项新增功能、错误修复和兼容性提升优化。下面是有关该版本更新内容的摘要，完整的更改列表可查看 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxuri%2Fexcelize%2Fcompare%2Fv2.4.0...v2.4.1" target="_blank">changelog</a><span style="background-color:#ffffff; color:#000000">。</span></p> 
<h2 style="text-align:start">Release Notes</h2> 
<p style="text-align:start">此版本中最显著的变化包括：</p> 
<h3 style="text-align:start">兼容性提示</h3> 
<p style="text-align:start">Go Modules 包引用地址调整为 <code>github.com/xuri/excelize/v2</code></p> 
<h3 style="text-align:start">新增功能</h3> 
<ul> 
 <li>新增流式设置工作表列宽度支持，相关 issue #625</li> 
 <li>新增流式创建合并单元格支持，相关 issue #826</li> 
 <li>公式计算引擎新增 2 项公式函数支持: BESSELK, BESSELY</li> 
 <li>公式计算引擎支持自定义名称引用，相关 issue #856</li> 
 <li>添加图表时支持设置不显示主要横纵坐标轴</li> 
 <li>通过 <code>AddPivotTable</code> 创建数据透视表支持通过自定义名称动态引用数据源</li> 
 <li>以下函数新增支持并发安全调用，相关 issue #861 
  <ul> 
   <li><code>AddPicture</code> 和 <code>GetPicture</code> 并发插入/获取图片</li> 
   <li><code>Rows</code> 和 <code>Cols</code> 并发行/列迭代</li> 
   <li><code>SetSheetRow</code> 并发按行赋值</li> 
   <li><code>SetCellStyle</code> 并发设置单元格样式</li> 
   <li><code>NewStyle</code> 并发创建样式</li> 
  </ul> </li> 
 <li>导出 24 个内部异常消息</li> 
</ul> 
<h3 style="text-align:start">兼容性提升</h3> 
<ul> 
 <li>提升内部默认 XML 命名空间兼容性，修复部分情况下生成文档损坏的问题</li> 
 <li>兼容带有非标准页面布局属性数据类型的电子表格文档，避免打开失败的问题</li> 
 <li>增加内部共享字符表计数</li> 
 <li>解除通过给定的时间设置单元格的值时，需要协调世界时 (UTC) 的限制，相关 issue #409</li> 
 <li>增加对内部 XML 控制字符的兼容</li> 
 <li>重命名导出字段 <code>File.XLSX</code> 为 <code>File.Pkg</code></li> 
 <li>修改 <code>NewSheet</code>, <code>GetSheetIndex</code>, <code>DeleteSheet</code> 对工作表名称大小写不敏感，相关 issue #873</li> 
 <li>修复条件格式与数据透视表的兼容性问题，解决 issue #883</li> 
 <li>改进与页面布局中无效的首页编号属性的兼容性</li> 
 <li><code>SetCellRichText</code> 增加字符数上限检查并修复保留字符丢失问题</li> 
</ul> 
<h3 style="text-align:start">问题修复</h3> 
<ul> 
 <li>修复部分情况下 12/24 制小时时间格式解析异常的问题，解决 issue #823 和 issue #841</li> 
 <li>修复部分情况下无法通过 <code>GetComments</code> 获取批注的问题，解决 issue #825</li> 
 <li>修复设置和获取批注时支持多个批注作者，解决 issue #829 和 #830</li> 
 <li>修复命名空间地址解析异常而产生重复命名空间，导致删除再创建同名工作表后的生成文档损坏问题，解决 issue #834</li> 
 <li>修复当设置工作表分组默认属性 <code>showOutlineSymbols</code>、<code>summaryBelow</code> 和 <code>summaryRight</code> 为 <code>false</code> 时，设置失效的问题</li> 
 <li>修复部分情况下 <code>GetRows</code> 返回冗余工作表尾部空行的问题，解决 issue #842</li> 
 <li>修复部分情况下获取获取单元格的值时，未返回带有公式的空单元格的问题，解决 issue #855</li> 
 <li>修复部分情况下 IF 公式条件运算错误问题，解决 issue #858</li> 
 <li>修复通过 <code>GetRowHeight</code> 获取行高度错误的问题</li> 
 <li>修复部分情况下因范围解析异常导致获取和删除自定义名称错误的问题，解决 issue #879</li> 
 <li>修复设置自定义名称时关联工作表索引错误的问题</li> 
 <li>修复设置列样式时已有单元格样式未被更新的问题，解决 issue #467</li> 
 <li>修复使用非法数据引用范围创建数据透视表时导致的潜在 panic 的问题</li> 
 <li>修复部分情况下读取数字精度异常的问题，解决 issue #848 和 #852</li> 
 <li>修复设置数据验证规则时，部分情况下因未进行 XML 字符转义处理导致生成文档损坏的问题，解决 issue #971</li> 
 <li>修复设置数据验证规则长度校验不准确问题，解决 issue #972</li> 
 <li>修复由时间解析异常导致的，部分情况下读取带有时间或日期数字格式单元格时 CPU 资源占用率过高问题，解决 issue #974</li> 
 <li>修复部分情况下，当自定义数字格式为日期时，月份解析失败的问题</li> 
</ul> 
<h3 style="text-align:start">性能优化</h3> 
<ul> 
 <li>通过 <code>Save</code> 保存或 <code>SaveAs</code> 另存文档时的内占用降低约 19%</li> 
</ul> 
<h3 style="text-align:start">其他</h3> 
<ul> 
 <li>修复潜在的代码安全问题 CWE-190 和 CWE-681</li> 
 <li>Go Modules 依赖模块更新</li> 
 <li>单元测试与文档更新</li> 
 <li>持续集成服务改用 GitHub Action</li> 
 <li>包含简体中文、英语、法语、俄语、日语、韩语、阿拉伯语、德语和西班牙语的多国语言文档网站更新</li> 
</ul>
                                        </div>
                                      
</div>
            