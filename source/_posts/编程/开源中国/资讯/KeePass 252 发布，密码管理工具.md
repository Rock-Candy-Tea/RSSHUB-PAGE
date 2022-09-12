
---
title: 'KeePass 2.52 发布，密码管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2924'
author: 开源中国
comments: false
date: Mon, 12 Sep 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2924'
---

<div>   
<div class="content">
                                                                                            <p>KeePass 是一个免费开源的密码管理器，它帮助你以安全的方式管理密码。你可以把你所有的密码放在一个数据库中，用一个主密码或一个密钥文件锁定。因此，你只需要记住一个主密码或选择密钥文件来解锁整个数据库。数据库使用非常安全的加密算法（AES/Rijndael, Twofish）进行加密。</p> 
<p>KeePass 2.52 正式发布，这是一个稳定的版本，KeePass 2.52 主要更新内容是用户界面和集成的增强，以及其他各种小的新功能和改进。该版本具体更新内容如下：</p> 
<h3>新功能</h3> 
<ul> 
 <li>在条目对话框的工具菜单中增加了 Copy Initial Password（复制初始密码）命令；它复制（到剪贴板）打开对话框时的密码</li> 
 <li>当选择多个条目（至少包含一个附件）时，附件的数量现在显示在条目菜单的 "附件" 子菜单中</li> 
 <li>增加了 "Alt. item background color" 选项（支持 "关闭"、"打开默认颜色 "和 "打开自定义颜色 "等状态）；它结合了之前的两个选项 "Use alternating item background colors" 和 "Custom alt. item color"</li> 
 <li><code>&#123;C:...&#125;</code>现在可以包含平衡大括号</li> 
 <li>在自动类型条目选择对话框中，"Sequence - Comments" 栏中的值现在可以被取消引用</li> 
 <li>条目密码最后被更改的时间现在显示在 “历史” 标签页上的条目对话框中</li> 
 <li><code>&#123;FIREFOX&#125;</code> 占位符和 URL(s) 菜单（'Open with ...' 命令）现在支持检测 Microsoft Store 版本的 Firefox</li> 
 <li>增加了对导入 1Password 8.7 1PUX 文件的支持</li> 
 <li>增加了对导入 Key Folder 1.22 XML 文件的支持</li> 
 <li>Sticky Password XML 导入：增加了对导入组和过期日期的支持。</li> 
 <li>Steganos Password Manager CSV 导入：增加了对双引号新编码的支持</li> 
 <li>Bitwarden JSON 导入：基于时间的一次性密码生成器设置现在自动转换</li> 
 <li>KeePass 现在检查 "KeePass.exe.config" 文件，并在发现问题时显示警告信息</li> 
 <li>对于开发构建：增加了显示 GC 信息的命令</li> 
 <li>插件现在可以订阅主密钥变更事件</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li>将 "Save Attached File(s) To" 命令移到条目菜单的 "Attachments" 子菜单中，并将其更名为 "Save File(s) To"</li> 
 <li>现在只有当所选条目中至少有一个附件时，保存附件文件的命令才可用</li> 
 <li>改进数据库修改状态和导入/同步后的 UI 更新</li> 
 <li>改进了选项对话框中某些组合框的下拉菜单宽度调整</li> 
 <li>改进了受保护的二进制文件、UUID 的散列性能</li> 
 <li>改进了与空数组有关的性能</li> 
 <li>改进了 Mono 框架的版本检测</li> 
 <li>TrlUtil：改进了预览对话框的更新性能</li> 
 <li>各种 UI 文本的改进</li> 
 <li>各种代码优化</li> 
 <li>其他小的改进</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>修正了在某些情况下导致最小化的主窗口恢复为正常窗口而不是最大化窗口的错误。</li> 
 <li>输入对话框中的 "帮助" 菜单项和输入字符串字段对话框中的 "帮助" 按钮现在可以打开正确的帮助部分。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkeepass.info%2Fnews%2Fn220909_2.52.html" target="_blank">https://keepass.info/news/n220909_2.52.html</a></p>
                                        </div>
                                      
</div>
            