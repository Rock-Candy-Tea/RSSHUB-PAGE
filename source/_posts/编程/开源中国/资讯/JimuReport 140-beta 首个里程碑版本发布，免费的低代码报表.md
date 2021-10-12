
---
title: 'JimuReport 1.4.0-beta 首个里程碑版本发布，免费的低代码报表'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 11:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>项目介绍</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">积木报表，一款免费的可视化Web报表工具，像搭建积木一样在线拖拽设计！功能涵盖，数据报表、打印设计、图表报表、大屏设计等！ 秉承“简单、易用、专业”的产品理念，极大的降低报表开发难度、缩短开发周期、节省成本、解决各类报表难题，完全免费的！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.4.0-beta | 2021-10-12</p> 
<p>集成依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.jeecgframework.jimureport<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>jimureport-spring-boot-starter<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.4.0-beta<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">增量SQL</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report`</span>
<span style="color:#d73a49">MODIFY</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`view_count`</span> <span>bigint</span>(<span>15</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span>0</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'浏览次数'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`template`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report`</span>
<span style="color:#d73a49">MODIFY</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`json_str`</span> longtext <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8 <span style="color:#d73a49">COLLATE</span> utf8_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'json字符串'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`type`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_link`</span> 
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`expression`</span> <span>varchar</span>(<span>255</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'表达式'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`link_chart_id`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_field`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`search_format`</span> <span>varchar</span>(<span>50</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询时间格式化表达式'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`search_value`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_param`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`search_format`</span> <span>varchar</span>(<span>50</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'查询时间格式化表达式'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`dict_code`</span>;
<span style="color:#d73a49">UPDATE</span> jimu_report <span style="color:#d73a49">SET</span> json_str=<span style="color:#d73a49">replace</span>(json_str,<span style="color:#032f62">'"subtotal":"totalField"'</span>,<span style="color:#032f62">'"funcname":"SUM"'</span>);
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report`</span>
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`css_str`</span> <span>text</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'css增强'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`view_count`</span>,
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`js_str`</span> <span>text</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'js增强'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`css_str`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_link`</span> 
<span style="color:#d73a49">CHANGE</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`expression`</span> <span style="color:#032f62">`requirement`</span> <span>varchar</span>(<span>255</span>) <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8mb4 <span style="color:#d73a49">COLLATE</span> utf8mb4_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'条件'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`link_chart_id`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_field`</span> 
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`ext_json`</span> <span>text</span>  <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'参数配置'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`search_format`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db_param`</span> 
<span style="color:#d73a49">ADD</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`ext_json`</span>  <span>text</span>  <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'参数配置'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`search_format`</span>;
<span style="color:#d73a49">ALTER</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`jimu_report_db`</span> 
<span style="color:#d73a49">MODIFY</span> <span style="color:#d73a49">COLUMN</span> <span style="color:#032f62">`is_list`</span> <span>varchar</span>(<span>10</span>) <span>CHARACTER</span> <span style="color:#d73a49">SET</span> utf8 <span style="color:#d73a49">COLLATE</span> utf8_general_ci <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#032f62">'0'</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'是否是列表0否1是 默认0'</span> <span style="color:#d73a49">AFTER</span> <span style="color:#032f62">`api_method`</span>;
</code></pre> 
<p>#升级日志</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">首个里程碑版本发布，历经一个月的版本测试和稳定工作。</p> 
</blockquote> 
<p>重点新功能</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持表格设置斑马线背景色</li> 
 <li>支持动态合并格</li> 
 <li>支持导出报表配置</li> 
 <li>查询控件支持树组件</li> 
 <li>支持Nosql数据集mogodb、redis</li> 
 <li>分组小计支持更多规则：求和、最大值、最小值、平均值</li> 
 <li>报表查询条件功能重构：重构查询规则；丰富查询控件类型、控件默认值、支持JS、CSS增强</li> 
 <li>支持导出图片</li> 
 <li>支持分版功能（左右并排两个列表）</li> 
 <li>支持分栏功能</li> 
 <li>支持自定义分页条数</li> 
 <li>支持存储过程</li> 
 <li>表达式优化忽略大小写</li> 
 <li>小数点变成了千分符</li> 
 <li>套打图片支持与表格一同滚动</li> 
 <li>下钻链接支持条件判断</li> 
 <li>积木报表主页面样式修改</li> 
 <li>查询默认值支持系统变量</li> 
 <li>优化分组文本含特殊符号报错</li> 
 <li>支持图表钻取</li> 
</ul> 
<p>Issues处理</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>横向分组下，表头不支持括号等符号<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F418" target="_blank">issues/#418</a></li> 
 <li>使用sqlserver数据库时，提示不支持该SQL转换为分页查询<a href="https://gitee.com/jeecg/JimuReport/issues/I43EK0">issues/I43EK0</a></li> 
 <li>v1.3.64-beta升级至v1.3.7出现报表导出异常,出现字符串越界错误[issues/#I43EOI]<a href="https://gitee.com/jeecg/JimuReport/issues/I43EOI">https://gitee.com/jeecg/JimuReport/issues/I43EOI</a></li> 
 <li>1.3.64-beta、1.3.7 版本 访问sqlserver，如果查询时间稍长，就会报超时<a href="https://gitee.com/jeecg/JimuReport/issues/I43TIT">issues/I43TIT</a></li> 
 <li>调用oracle sql 经常报超时<a href="https://gitee.com/jeecg/JimuReport/issues/I42Z57">issues/I42Z57</a></li> 
 <li>如果yml文件中的pageSize没有设置10，在预览报表时，查询结果仍然是十条结果<a href="https://gitee.com/jeecg/JimuReport/issues/I42978">issues/I42978</a></li> 
 <li>1.3.64-beta PDF导出图片不全<a href="https://gitee.com/jeecg/JimuReport/issues/I41JHS">issues/I41JHS</a></li> 
 <li>导出PDF出现 NullPointerException<a href="https://gitee.com/jeecg/JimuReport/issues/I43VWD">issues/I43VWD</a></li> 
 <li>表达式函数列不能设置数据换行设置后就不显示数据了<a href="https://gitee.com/jeecg/JimuReport/issues/I420FI">issues/I420FI</a></li> 
 <li>小数点变成了千分符<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F413" target="_blank">issues/#413</a></li> 
 <li>设置小数位，导出后，不带小数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F412" target="_blank">issues/#412</a></li> 
 <li>套打图片能与表格一同滚动<a href="https://gitee.com/jeecg/JimuReport/issues/I412JW">issues/I412JW</a></li> 
 <li>1.3.7 报表设计器报错：不支持该SQL转换为分页查询<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F442" target="_blank">issues/#442</a></li> 
 <li>勾选一个列作为查询条件就多一次全量查询<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F450" target="_blank">issues/#450</a></li> 
 <li>1.3.75 版本 sum函数失效<a href="https://gitee.com/jeecg/JimuReport/issues/I44UUL">issues/I44UUL</a></li> 
 <li>复杂SQL解析报SQL注入问题<a href="https://gitee.com/jeecg/JimuReport/issues/I44O9Y">issues/I44O9Y</a></li> 
 <li>查询条件优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2877" target="_blank">issues/2877</a></li> 
 <li>时间组件增加年份类型<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F463" target="_blank">issues/2877</a></li> 
 <li>关于报表查询条件默认值的问题<a href="https://gitee.com/jeecg/JimuReport/issues/I469F5">issues/I469F5</a></li> 
 <li>数值类型太长，科学计数法，SUM时不统计问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F497" target="_blank">issues/#497</a></li> 
 <li>交叉报表导出excel表头中文显示乱码[issues/#406]<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F406" target="_blank">https://github.com/jeecgboot/JimuReport/issues/406</a>)</li> 
 <li>查询下拉框取值,SQL语句中添加报表参数（时间范围）后，查询条件下拉框取值消失<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F464" target="_blank">issues/#464</a></li> 
 <li>升级到1.3.78 下拉单选查询问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F466" target="_blank">issues/#466</a></li> 
 <li>升级到1.3.78版本后 没开启MongoDB 控制台 Exception opening socket[issues/#465](<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F465" target="_blank">https://github.com/jeecgboot/JimuReport/issues/465</a></li> 
 <li>由于sql查询慢,点击SQL解析后30秒超时<a href="https://gitee.com/jeecg/JimuReport/issues/I45ZKK">issues/I45ZKK</a></li> 
 <li>将小数位数设置成0之后 数值类型的千位分隔号无法显示[issues/I4538B](<a href="https://gitee.com/jeecg/JimuReport/issues/I4538B">https://gitee.com/jeecg/JimuReport/issues/I4538B</a></li> 
 <li>=row()函数前有一列空列，预览报表无数据<a href="https://gitee.com/jeecg/JimuReport/issues/I44QLI">issues/I44QLI</a></li> 
 <li>背景图片名称为中文时无法显示<a href="https://gitee.com/jeecg/JimuReport/issues/I44EOT">issues/I44EOT</a></li> 
 <li>设置自动分行换行后，查询出现重叠现象<a href="https://gitee.com/jeecg/JimuReport/issues/I449P3">issues/I449P3</a></li> 
 <li>分组排序 选择 默认 能不能就按原始数据传入的顺序<a href="https://gitee.com/jeecg/JimuReport/issues/I430IC">issues/I430IC</a></li> 
 <li>支持树形菜单查询控件<a href="https://gitee.com/jeecg/JimuReport/issues/I46ION">issues/I46ION</a></li> 
 <li>预览时后端空指针异常<a href="https://gitee.com/jeecg/JimuReport/issues/I453DF">issues/I453DF</a></li> 
 <li>Oracle数据源,回车搜索报表名称<a href="https://gitee.com/jeecg/JimuReport/issues/I44KQ4">issues/I44KQ4</a></li> 
 <li>pgsql数据库下图表钻取配置完后保存失败<a href="https://gitee.com/jeecg/JimuReport/issues/I45I9E">issues/I45I9E</a></li> 
 <li>分版合并列报错<a href="https://gitee.com/jeecg/JimuReport/issues/I450YZ">issues/I450YZ</a></li> 
 <li>表格设置了分版设置Sum函数统计出错<a href="https://gitee.com/jeecg/JimuReport/issues/I45C35">issues/I45C35</a></li> 
 <li>1.3.76版本导出中包含图表报错,如果只有表格是可以的<a href="https://gitee.com/jeecg/JimuReport/issues/I453S2">issues/I453S2</a></li> 
 <li>单元格数据格式，设置成“百分比”，导出excel后，数值会x100倍<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F486" target="_blank">issues/#486</a></li> 
 <li>预览空指针<a href="https://gitee.com/jeecg/JimuReport/issues/I453DF">issues/I453DF</a></li> 
 <li>回车搜索报表名称<a href="https://gitee.com/jeecg/JimuReport/issues/I44KQ4">issues/I44KQ4</a></li> 
 <li>pgsql数据库下图表钻取配置完后保存失败<a href="https://gitee.com/jeecg/JimuReport/issues/I45I9E">issues/I45I9E</a></li> 
 <li>分版空指针异常<a href="https://gitee.com/jeecg/JimuReport/issues/I450YZ">issues/I450YZ</a></li> 
 <li>表格设置了分版设置Sum函数统计出错<a href="https://gitee.com/jeecg/JimuReport/issues/I45C35">issues/I45C35</a></li> 
 <li>导出中包含图表报错<a href="https://gitee.com/jeecg/JimuReport/issues/I453S2">issues/I453S2</a></li> 
 <li>Long类型的日期格式转字符串<a href="https://gitee.com/jeecg/JimuReport/issues/I4696V">issues/I4696V</a></li> 
 <li>日期转换成字符串<a href="https://gitee.com/jeecg/JimuReport/issues/I45UD2">issues/I45UD2</a></li> 
 <li>日期转换成字符串<a href="https://gitee.com/jeecg/JimuReport/issues/I46FIT">issues/I46FIT</a></li> 
 <li>下拉单选无效<a href="https://gitee.com/jeecg/JimuReport/issues/I46A5E">issues/I46A5E</a></li> 
 <li>除法计算有问题，小数值都被截去了<a href="https://gitee.com/jeecg/JimuReport/issues/I46JT8">issues/I46JT8</a></li> 
 <li>导出报表配置<a href="https://gitee.com/jeecg/JimuReport/issues/I44HTO">issues/I44HTO</a></li> 
 <li>日期查询默认当月1号至当前日期<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F454" target="_blank">issues/#454</a></li> 
 <li>导出与预览效果不一致<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F451" target="_blank">issues/#451</a></li> 
 <li>1.3.76 版本导出报 cells<a href="https://gitee.com/jeecg/JimuReport/issues/I46EDS">issues/I46EDS</a></li> 
 <li>纵向分组小计<a href="https://gitee.com/jeecg/JimuReport/issues/I426CB">issues/I426CB</a></li> 
 <li>纵向分组内小计，未选择的字段不进行小计并填充为空<a href="https://gitee.com/jeecg/JimuReport/issues/I45YI9">issues/I45YI9</a></li> 
 <li>表头填充后分割线不可见<a href="https://gitee.com/jeecg/JimuReport/issues/I47FXO">issues/I47FXO</a></li> 
 <li>数值位数多时，Sum函数结果错误<a href="https://gitee.com/jeecg/JimuReport/issues/I47BSG">issues/I47BSG</a></li> 
 <li>API自定义查询条件，报表参数问题：模糊查询“+”号被转成空格字符串<a href="https://gitee.com/jeecg/JimuReport/issues/I46RAJ">issues/I46RAJ</a></li> 
 <li>导出excel图片为空时报错<a href="https://gitee.com/jeecg/JimuReport/issues/I48AZC">issues/I48AZC</a></li> 
 <li>纵向组分小计保留小数位<a href="https://gitee.com/jeecg/JimuReport/issues/I463L4">issues/I463L4</a></li> 
 <li>大数据量导出excel时无法生成多sheet页，且设置page-size-number无效<a href="https://gitee.com/jeecg/JimuReport/issues/I47JR9">issues/I47JR9</a></li> 
 <li>html打印api数据源属性为空，打印显示问题<a href="https://gitee.com/jeecg/JimuReport/issues/I453US">issues/I453US</a></li> 
 <li>Api主子表报表参数设置功能问题<a href="https://gitee.com/jeecg/JimuReport/issues/I48RAJ">issues/I48RAJ</a></li> 
 <li>合计行中百分比无法结算，希望官方添加此计算功能<a href="https://gitee.com/jeecg/JimuReport/issues/I48WM1">issues/I48WM1</a></li> 
 <li>交叉表导出Excel，带有斜线的标题乱码<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F482" target="_blank">issues/#482</a></li> 
 <li>数据带有括号时出错<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F491" target="_blank">issues/#491</a></li> 
 <li>整数数字转大写金额为空白<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F538" target="_blank">issues/#538</a></li> 
 <li>大屏设计器选项卡无法交互<a href="https://gitee.com/jeecg/JimuReport/issues/I44OJP">issues/I44OJP</a></li> 
 <li>在线大屏旋转饼图bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F493" target="_blank">issues/493</a></li> 
 <li>API数据集中配置字典code为外部链接无法获取数据<a href="https://gitee.com/jeecg/JimuReport/issues/I49Y66">issues/I49Y66</a></li> 
 <li>1.3.795-1.3.8-bate版本javabean类型数据源查询模式缺少<a href="https://gitee.com/jeecg/JimuReport/issues/I4BMO8">issues/I4BMO8</a></li> 
 <li>MSsqlserver数据集SQL语句排序<a href="https://gitee.com/jeecg/JimuReport/issues/I4AZV1">issues/I4AZV1</a></li> 
 <li>根据指定的数据源去获取数据字典<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F560" target="_blank">issues/#560</a></li> 
 <li>查询参数运用到单元格表达式中值获取为空<a href="https://gitee.com/jeecg/JimuReport/issues/I4A0A9">issues/I4A0A9</a></li> 
 <li>查询条件模糊查询的删除重新查的问题<a href="https://gitee.com/jeecg/JimuReport/issues/I4BYRK">issues/I4BYRK</a></li> 
 <li>concat函数支持获取param数据<a href="https://gitee.com/jeecg/JimuReport/issues/I4BPZG">issues/I4BPZG</a></li> 
 <li>图形报表开发，三级联动失效问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F547" target="_blank">issues/547</a></li> 
 <li>HTML 打印表格显示不全<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2FJimuReport%2Fissues%2F526" target="_blank">issues/526</a></li> 
 <li>大屏设计文本框SQL刷新时间不起作用<a href="https://gitee.com/jeecg/JimuReport/issues/I4CD16">issues/I4CD16</a></li> 
 <li>大屏设计器里，RTMP播放器出现“flash :rtmpconnectfailure”<a href="https://gitee.com/jeecg/JimuReport/issues/I4C1LR">issues/I4C1LR</a></li> 
 <li>大屏预览时鼠标移入会弹出控件名<a href="https://gitee.com/jeecg/JimuReport/issues/I4910E">issues/I4910E</a></li> 
</ul> 
<p>#代码下载</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport" target="_blank">https://github.com/zhangdaiscott/JimuReport</a></li> 
 <li><a href="https://gitee.com/jeecg/JimuReport">https://gitee.com/jeecg/JimuReport</a></li> 
</ul> 
<p>#技术文档</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>体验官网：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjimureport.com%2F" target="_blank">http://jimureport.com</a></li> 
 <li>快速集成文档 ：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com%2F2078875" target="_blank">http://report.jeecg.com/2078875</a></li> 
 <li>技术文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freport.jeecg.com" target="_blank">http://report.jeecg.com</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JimuReport?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">永久免费，支持各种复杂报表，并且傻瓜式在线设计，非常的智能，低代码时代，这个是你的首选！</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用SpringBoot的脚手架项目，都可以快速集成</li> 
 <li>Web 版设计器，类似于excel操作风格，通过拖拽完成报表设计</li> 
 <li>通过SQL、API等方式，将数据源与模板绑定。同时支持表达式，自动计算合计等功能，使计算工作量大大降低</li> 
 <li>开发效率很高，傻瓜式在线报表设计，一分钟设计一个报表，又简单又强大</li> 
 <li>支持 ECharts，目前支持28种图表，在线拖拽设计，支持SQL和API两种数据源</li> 
 <li>支持分组、交叉，合计、表达式等复杂报表</li> 
 <li>支持打印设计（支持套打、背景打印等）可设置打印边距、方向、页眉页脚等参数 一键快速打印 同时可实现发票套打，不动产证等精准、无缝打印</li> 
 <li>大屏设计器支持几十种图表样式，可自由拼接、组合，设计炫酷大屏</li> 
 <li>可设计各种类型的单据、大屏，如出入库单、销售单、财务报表、合同、监控大屏、旅游数据大屏等</li> 
</ul> 
<p>#系统截图</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>报表设计器（专业一流 数据可视化,解决各类报表难题）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-a2a8557722593e6c5a5e8f015a0df2b70e9.png" referrerpolicy="no-referrer"></li> 
 <li>报表设计器（完全在线设计，简单易用）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-752b454f64ed87c798b3e8a083fbd6622d4.gif" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>打印设计（支持套打、背景打印）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9b6cd73719de68e0e45e1cf95cd6104a103.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-8863ea4e67c02dbd844bb8022652f1be651.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>数据报表（支持分组、交叉，合计等复杂报表）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fe2ac0dfc3933734961924de0538b3049d2.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-be956cbc19287e4df9cc46c9d15e96da99d.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>图形报表（目前支持28种图表）<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-3eda428ef182cb64a1a8e132e4bfeb87718.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-22096123c5b6a10a801967c33cc33a7af11.png" referrerpolicy="no-referrer"></li> 
</ul> 
<p>#功能清单</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─报表设计器
│  ├─数据源
│  │  ├─支持多种数据源，如Oracle,MySQL,SQLServer,PostgreSQL等主流的数据库
│  │  ├─支持SQL编写页面智能化，可以看到数据源下面的表清单和字段清单
│  │  ├─支持参数
│  │  ├─支持单数据源和多数数据源设置
│  │  ├─支持Nosql数据源Redis，MongoDB
│  │  ├─支持存储过程
│  ├─单元格格式
│  │  ├─边框
│  │  ├─字体大小
│  │  ├─字体颜色
│  │  ├─背景色
│  │  ├─字体加粗
│  │  ├─支持水平和垂直的分散对齐
│  │  ├─支持文字自动换行设置
│  │  ├─图片设置为图片背景
│  │  ├─支持无线行和无限列
│  │  ├─支持设计器内冻结窗口
│  │  ├─支持对单元格内容或格式的复制、粘贴和删除等功能
│  │  ├─等等
│  ├─报表元素
│  │  ├─文本类型：直接写文本；支持数值类型的文本设置小数位数
│  │  ├─图片类型：支持上传一张图表；支持图片动态生成
│  │  ├─图表类型
│  │  ├─函数类型
│  │  └─支持求和
│  │  └─平均值
│  │  └─最大值
│  │  └─最小值
│  ├─背景
│  │  ├─背景颜色设置
│  │  ├─背景图片设置
│  │  ├─背景透明度设置
│  │  ├─背景大小设置
│  ├─数据字典
│  ├─报表打印
│  │  ├─自定义打印
│  │  └─医药笺、逮捕令、介绍信等自定义样式设计打印
│  │  ├─简单数据打印
│  │  └─出入库单、销售表打印
│  │  └─带参数打印
│  │  └─分页打印
│  │  ├─套打
│  │  └─不动产证书打印
│  │  └─发票打印
│  ├─数据报表
│  │  ├─分组数据报表
│  │  └─横向数据分组
│  │  └─纵向数据分组
│  │  └─多级循环表头分组
│  │  └─横向分组小计
│  │  └─纵向分组小计
│  │  └─分版
│  │  └─分栏
│  │  └─动态合并格
│  │  └─自定义分页条数
│  │  └─合计
│  │  ├─交叉报表
│  │  ├─明细表
│  │  ├─带条件查询报表
│  │  ├─表达式报表
│  │  ├─带二维码/条形码报表
│  │  ├─多表头复杂报表
│  │  ├─主子报表
│  │  ├─预警报表
│  │  ├─数据钻取报表
│  ├─图形报表
│  │  ├─柱形图
│  │  ├─堆叠柱形图
│  │  ├─折线图
│  │  ├─饼图
│  │  ├─动态轮播图
│  │  ├─折柱图
│  │  ├─散点图
│  │  ├─漏斗图
│  │  ├─雷达图
│  │  ├─象形图
│  │  ├─地图
│  │  ├─仪盘表
│  │  ├─关系图
│  │  ├─图表背景
│  │  ├─图表动态刷新
│  │  ├─图表数据字典
│  ├─参数
│  │  ├─参数配置
│  │  ├─参数管理
│  ├─导入导出
│  │  ├─支持导入Excel
│  │  ├─支持导出Excel、pdf；支持导出excel、pdf带参数
│  ├─打印设置
│  │  ├─打印区域设置
│  │  ├─打印机设置
│  │  ├─预览
│  │  ├─打印页码设置
├─大屏设计器
│  ├─系统功能
│  │  ├─静态数据源和动态数据源设置
│  │  ├─基础功能
│  │  └─支持拖拽设计
│  │  └─支持增、删、改、查大屏
│  │  └─支持复制大屏数据和样式
│  │  └─支持大屏预览、分享
│  │  └─支持系统自动保存数据，同时支持手动恢复数据
│  │  └─支持设置大屏密码
│  │  └─支持对组件图层的删除、组合、上移、下移、置顶、置底等
│  │  ├─背景设置
│  │  └─大屏的宽度和高度设置
│  │  └─大屏简介设置
│  │  └─背景颜色、背景图片设置
│  │  └─封面图设置
│  │  └─缩放比例设置
│  │  └─环境地址设置
│  │  └─水印设置
│  │  ├─地图设置
│  │  └─添加地图
│  │  └─地图数据隔离
│  ├─图表
│  │  ├─柱形图
│  │  ├─折线图
│  │  ├─折柱图
│  │  ├─饼图
│  │  ├─象形图
│  │  ├─雷达图
│  │  ├─散点图
│  │  ├─漏斗图
│  │  ├─文本框
│  │  ├─跑马灯
│  │  ├─超链接
│  │  ├─实时时间
│  │  ├─地图
│  │  ├─全国物流地图
│  │  ├─地理坐标地图
│  │  ├─城市派件地图
│  │  ├─图片
│  │  ├─图片框
│  │  ├─轮播图
│  │  ├─滑动组件
│  │  ├─iframe
│  │  ├─video
│  │  ├─翻牌器
│  │  ├─环形图
│  │  ├─进度条
│  │  ├─仪盘表
│  │  ├─字浮云
│  │  ├─表格
│  │  ├─选项卡
│  │  ├─万能组件
└─其他模块
   └─更多功能开发中。。</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            