
---
title: 'GNU Octave 7.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7263'
author: 开源中国
comments: false
date: Tue, 02 Aug 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7263'
---

<div>   
<div class="content">
                                                                                            <p>GNU Octave 7.2.0 发布，现已可供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foctave.org%2Fdownload.html" target="_blank">下载</a>。这是一个错误修复版本，具体更新内容如下：</p> 
<p><strong>改进和修复</strong></p> 
<ul> 
 <li>检查 broadcastable inplace operators 时避免越界索引（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F38466" target="_blank">bug＃38466</a>）</li> 
 <li><code>hdl2struct.m</code>：修复<code>uibuttongroups</code>的保存（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62266" target="_blank">bug＃62266</a>）</li> 
 <li><code>isprime.m</code>和<code>__isprimelarge__.cc</code>：轻微的性能调整</li> 
 <li><code>factor.m</code>：性能调整以避免在某些情况下出现 division</li> 
 <li><code>nchoosek.m</code>：修复某些整数输入的 freeze-up（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62319" target="_blank">bug＃62319</a>）</li> 
 <li><code>nchoosek.m</code>：恢复浮点输入的快速路径代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62319" target="_blank">bug #62319</a>）</li> 
 <li><code>betainc.m</code>：使用复杂的技术来计算指数以避免不准确（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62329" target="_blank">bug＃62329</a>）</li> 
 <li><code>ls.m</code>：修复 UNIX 平台上对<code>\</code>的处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62282" target="_blank">bug #62282</a>）</li> 
 <li><code>ls.m</code>：在 Windows 上使用 glob 模式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62282" target="_blank">bug #62282</a>）</li> 
 <li><code>findobj.m</code>：修复图形句柄的输入验证（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62378" target="_blank">bug #62378</a>）</li> 
 <li><code>newplot.m</code>: 退回 changeset fdd58773ac02 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F61945" target="_blank">bug #61945</a> )</li> 
 <li><code>__print_parse_opts__.m</code>：在所有情况下为 print warnings 初始化变量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62287" target="_blank">bug #62287</a>）</li> 
 <li><code>datenum.m</code>：正确处理具有前导单例维度的数组（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62407" target="_blank">bug #62407</a>）</li> 
 <li>停止在<code>uimenu</code>句柄上调用<code>reset()</code>时的错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62425" target="_blank">bug #62425</a>）</li> 
 <li>设置轴限制时在空输入上发出更多信息错误消息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62541" target="_blank">bug #62541</a>）</li> 
 <li><code>msgbox.m</code>：允许图标的“自定义”<code>cdata</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62445" target="_blank">bug #62445</a>）</li> 
 <li>修复嵌套函数和匿名函数的内存泄漏（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62459" target="_blank">bug #62459</a>）</li> 
 <li><code>__wglob__</code>：在 Windows 上保留 trailing file 分隔符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62414" target="_blank">bug #62414</a>）</li> 
 <li><code>mkoctfile.m</code>：修剪系统输出周围的空白（换行符）</li> 
 <li><code>plot</code>：不赞成使用数字来选择线条颜色（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62470" target="_blank">bug #62470</a>）</li> 
 <li>改变将变量作为函数使用时的错误信息的措辞（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62552" target="_blank">bug #62552</a>）</li> 
 <li><code>inputParser.m</code>：适应关于输出参数数量的解释器更改（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62420" target="_blank">bug＃62420</a>）</li> 
 <li><code>inputParser.m</code>：正确处理可选参数的单元格默认值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62639" target="_blank">bug #62639</a>）</li> 
 <li>解析关键字时存储 token ID，而不是关键字 ID（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62587" target="_blank">bug #62587</a>）</li> 
 <li><code>canonicalize_file_name</code>：不要将映射的网络驱动器转换为 UNC 路径（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62576" target="_blank">bug #62576</a>）</li> 
 <li><code>regexp</code>：在访问之前检查 pattern length（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62704" target="_blank">bug #62704</a>）</li> 
 <li><code>randmtzig.cc</code>：添加缺失的<code>#include <ctime></code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62750" target="_blank">bug＃62750</a>）</li> 
</ul> 
<p><strong>GUI</strong></p> 
<ul> 
 <li>修复在关闭修改后的文件时删除尾随空格的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62271" target="_blank">bug #62271</a>）</li> 
 <li>替换 GUI 中弃用的<code>QDesktopWidget</code>的使用。</li> 
 <li>修复打开<code>fixed_point_format</code>时变量编辑器中的显示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62544" target="_blank">bug #62544</a>）</li> 
 <li>修复在编辑器中保存较短内容时的文件长度（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fbugs%2F%3F62588" target="_blank">bug #62588</a>）</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foctave.org%2Fnews%2Frelease%2F2022%2F07%2F28%2Foctave-7.2.0-released.html" target="_blank">https://octave.org/news/release/2022/07/28/octave-7.2.0-released.html</a></p>
                                        </div>
                                      
</div>
            