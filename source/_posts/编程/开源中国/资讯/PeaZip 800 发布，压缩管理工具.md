
---
title: 'PeaZip 8.0.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=0'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=0'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p>该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p>PeaZip 8.0.0 正式发布，该版本更新内容如下：</p> 
<p>后端：</p> 
<p>PEA 1.01</p> 
<ul> 
 <li>增加了函数的退出代码，以便与第三方软件和脚本更容易集成；</li> 
 <li>在 batch_report 和 hidden_report 模式下运行 PEA 会自动保存任务日志，而不需要用户进一步交互；</li> 
 <li>修正：hidden 模式和 hidden_report 模式在隐藏前不会闪现图形用户界面；</li> 
 <li>更新了在线文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fpea_help.pdf" target="_blank">https://peazip.github.io/pea_help.pdf</a> ；</li> 
</ul> 
<p>CAB (Windows)</p> 
<ul> 
 <li>在高级选项卡中选择自定义格式，现在可以在自定义可执行文件的下拉菜单中选择 "CAB" 预设，以使用 Windows 的 makecab.exe 工具；</li> 
</ul> 
<p>代码</p> 
<ul> 
 <li>各种修复和改进</li> 
</ul> 
<p>文件管理器</p> 
<ul> 
 <li>增加了对 .xappx 和各种 Open Packaging Conventions 文件类型（.3mf, .vsdx, .mmzx, .asx, .slx, .scdoc）的支持；</li> 
 <li>默认支持只读，要启用写入支持，请在主菜单 "选项">"设置">"归档管理器" 中勾选 "Edit non-canonical archive types"；</li> 
 <li>增加了搜索字段的文本补全；</li> 
 <li>Checksum/哈希文件现在可以被设置为执行单一算法（更快），默认为 SHA256；</li> 
 <li>在选项>设置>文件管理器中，可以选择一次执行所有算法，或一次执行所有常用算法；</li> 
 <li>在文件管理器屏幕上拖动单个归档文件，现在无需进一步互动即可打开归档；</li> 
 <li>改进了“预览”和“打开”功能；</li> 
 <li>如果没有选择任何东西，预览会将当前目录作为输入；</li> 
 <li>为了避免与 "预览" 操作子菜单混淆，"提取和打开" 子菜单现在可以在选项>设置>档案管理器中启用/禁用；</li> 
 <li>改进了主菜单中的随机密码生成器，工具>创建随机密码/密钥文件，默认长度现在是12个字符</li> 
 <li>改进了文件名的智能排序；</li> 
 <li>改进了状态栏</li> 
</ul> 
<p>压缩与解压缩</p> 
<ul> 
 <li>现在可以编辑现有的 7Z 压缩 sfx 文档；</li> 
 <li>改进的 “TAR before” 选项，在压缩步骤之前将多个输入保存到 TAR 档案；</li> 
 <li>现在可以自定义在系统上双击与 PeaZip 关联的文件类型时要执行的默认操作；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html%23software_development_log" target="_blank">https://peazip.github.io/changelog.html#software_development_log</a></p>
                                        </div>
                                      
</div>
            