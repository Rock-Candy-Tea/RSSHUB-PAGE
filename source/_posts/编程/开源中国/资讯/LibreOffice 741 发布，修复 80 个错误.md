
---
title: 'LibreOffice 7.4.1 发布，修复 80 个错误'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0916/072255_yMb0_5430600.png'
author: 开源中国
comments: false
date: Fri, 16 Sep 2022 07:27:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0916/072255_yMb0_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>开源办公套件 LibreOffice 7.4.1 已发布，这是 LibreOffice 7.4 的第一个维护版本，在LibreOffice 7.4 发布三周后推出，修复在此期间发现的各种错误。</p> 
<p>根据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.documentfoundation.org%2FReleases%2F7.4.1%2FRC1" target="_blank">RC1</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.documentfoundation.org%2FReleases%2F7.4.1%2FRC2" target="_blank">RC2</a> 的变更日志，7.4.1 小型维护更新总共解决了 80 个错误。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D91764" target="_blank">tdf#91764</a> RTL：无法使用搜索对话框找到阿拉伯语、希伯来语变音符号 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D103492" target="_blank">tdf#103492</a> 当句子以英语单词开头时，阿拉伯语单词在文本框中的格式不正确 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D114790" target="_blank">tdf#114790</a> 在对话框中，货币字段值无法在右侧对齐 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D119246" target="_blank">tdf#119246</a> 尺寸对话框在“线距”、“左向导”和“右向导”字段中的值错误 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D120972" target="_blank">tdf#120972</a> 在标尺中使用小数点选项卡创建的列在 docx 文件中未对齐 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D124076" target="_blank">tdf#124076</a> 框架边框中对象水平对齐的预览已交换左右图像 [J</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D126754" target="_blank">tdf#126754</a> 字体特征对话框：“字体特征”对话框中分数的 OpenType 标记错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D129631" target="_blank">tdf#129631</a> FILEOPEN：RTF：如果颜色发生变化，段落边框将被删除 </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D130795" target="_blank">tdf#130795</a> FILEOPEN：电子表格需要很长时间才能打开</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D133123" target="_blank">tdf#133123</a> Python模块uno.py覆盖导入，导致后续导入cairosvg模块失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D133299" target="_blank">tdf#133299</a> 为 Calc 中的图像设置默认锚模式的选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D135991" target="_blank">tdf#135991</a> 希伯来文本随机消失和重新出现</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.documentfoundation.org%2Fshow_bug.cgi%3Fid%3D141652" target="_blank">tdf#141652</a> 文件保存：DOCX：RT 后图像失真</li> 
 <li>...</li> 
</ul> 
<p><img height="501" src="https://static.oschina.net/uploads/space/2022/0916/072255_yMb0_5430600.png" width="1123" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><strong>7.4 版本新功能</strong></p> 
<p style="margin-left:0px"><span style="color:#000000"><strong>GENERAL</strong></span></p> 
<ul> 
 <li><span style="color:#000000">支持 WebP 图像和 EMZ/WMZ 文件</span></li> 
 <li><span style="color:#000000">ScriptForge 脚本库的帮助页面</span></li> 
 <li><span style="color:#000000">Extension Manager 的 Search field</span></li> 
 <li><span style="color:#000000">性能和兼容性改进</span></li> 
</ul> 
<p style="margin-left:0px"><span style="color:#000000"><strong>WRITER</strong></span></p> 
<ul> 
 <li><span style="color:#000000">脚注区域中更好的更改跟踪</span></li> 
 <li><span style="color:#000000">编辑后的列表显示更改跟踪中的原始数字</span></li> 
 <li><span style="color:#000000">新的连字符排版设置</span></li> 
</ul> 
<p style="margin-left:0px"><span style="color:#000000"><strong>CALC</strong></span></p> 
<ul> 
 <li><span style="color:#000000">支持电子表格中的 16,384 列</span></li> 
 <li><span style="color:#000000">下拉 AutoSum 小部件中的额外功能</span></li> 
 <li><span style="color:#000000">新增用于搜索工作表名称的菜单项</span></li> 
</ul> 
<p style="margin-left:0px"><span style="color:#000000"><strong>IMPRESS</strong></span></p> 
<ul> 
 <li><span style="color:#000000">新增对文档主题的支持</span></li> 
</ul> 
<p> </p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.documentfoundation.org%2Fblog%2F2022%2F09%2F15%2Flibreoffice-741-community%2F" target="_blank">更新公告</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.libreoffice.org%2Fdownload" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            