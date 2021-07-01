
---
title: '深度操作系统 deepin 20.2.2 发布，新版应用商店上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f0a794c03723d0bc14216852f30ff2caaad.png'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f0a794c03723d0bc14216852f30ff2caaad.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>深度操作系统 deepin 20.2.2 现已发布。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.deepin.org%2Fzh%2F2021%2F06%2F29%2Fdeepin-20-2-2%2F" target="_blank">官方发布公告指出</a>，20.2.2 上线了全新的应用商店，清新的视觉设计、化繁为简的交互、丰富的功能、支持使用安卓应用，带来更好的应用管理及使用体验。系统支持安全启动，确保设备引导受信任的软件，为系统安全保驾护航。跟随上游升级内核版本，适配更多GPU型号及显卡，提升系统稳定性和兼容性。更新深度全家桶应用，优化及修复更多功能，提升整体使用体验。</p> 
<p><strong>全新的应用商店</strong></p> 
<p>新版应用商店上线！清新的视觉设计、化繁为简的交互，带来整体使用体验的提升。内容呈现可视化，更合理的应用分类，支持按照应用评分、下载量、更新时间维度进行排序，更方便的获取不同类型应用。支持批量安装应用，一键可安装多款应用，节省安装时间。上线安卓容器功能及安卓应用，丰富社区生态，满足办公、学习、游戏等场景下的使用需求。</p> 
<blockquote> 
 <p>注：安卓容器使用安卓应用，目前只支持Kernel 5.10（LTS）内核，Kernel 5.12（Stable）内核下的使用还在处理中，敬请期待！</p> 
</blockquote> 
<p><img src="https://oscimg.oschina.net/oscnet/up-f0a794c03723d0bc14216852f30ff2caaad.png" referrerpolicy="no-referrer"></p> 
<p><strong>系统支持安全启动</strong></p> 
<p>为了更全面的保障设备使用安全，深度操作系统获取了安全启动证书，成为国内首个获得该证书的Linux发行版。在BIOS（只针对UEFI-BIOS）界面选择安全启动模式（Secure Boot）后，系统安装时只会引导签名过的内核，同时确保设备引导仅使用原始设备制造商信任的软件，为系统安装、使用保驾护航。国内首个获取安全启动证书的Linux发行版。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-9bb76b3fa9f6d6b2ab3e8442862b3a4e840.png" referrerpolicy="no-referrer"></p> 
<p><strong>更强大内核版本</strong></p> 
<p>Stable内核升级到Kernel 5.12版本，LTS内核 Kernel 5.10也跟随上游小版本更新，系统稳定性和兼容性进一步提升。深度操作系统支持选择双内核进行安装，同时也支持手动升级内核版本。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-227d18769558bc901a924f8a8c22926bfd2.png" referrerpolicy="no-referrer"></p> 
<p><strong>系统更新日志：</strong></p> 
<p>DDE</p> 
<ul> 
 <li>新增多种生物认证方式，包括登陆、锁屏、控制中心-帐户下的认证</li> 
 <li>修复双屏热插拔高概率进入锁屏的问题</li> 
 <li>修复任务栏下的蓝牙背景框颜色异常的问题</li> 
 <li>修复通知中心打开崩溃的问题</li> 
 <li>修复扩展模式下点击主副屏图标时，控制中心位置偏移的问题</li> 
 <li>修复账户密码输入错误后，提示信息未汉化的问题</li> 
</ul> 
<p>文件管理器</p> 
<ul> 
 <li>新增支持自定义图片屏保</li> 
 <li>新增文件夹列表视图在铺满屏时，右键菜单支持新建</li> 
 <li>修复复制大量小文件到U盘（ntfs）中时中断复制，无法删除U盘所有的文件的问题</li> 
 <li>修复切换藏语时，外设属性显示截断的问题</li> 
 <li>修复文件管理器下安全移除光驱时提示"设备没有正常移除"，且不会移除光驱选项的问题</li> 
 <li>修复拖拽文件到ext4格式的USB移动硬盘时出现错误的问题</li> 
 <li>修复文件选择对话框开启保险箱，不能拖拽内容到保险箱的问题</li> 
 <li>修复从smb/ftp中拖拽多层级文件夹到本地时出现文管崩溃的问题</li> 
 <li>修复手机目录内无法使用历史功能的前进、后退键的问题</li> 
 <li>修复在gerrit上复制下载地址后进入文管中，选择文件夹进行重命名时粘贴复制文本信息出现崩溃的问题</li> 
 <li>修复调整文管宽度至最小时点击任意侧边栏目录，进入搜索状态后输入框文字出现重叠的问题</li> 
 <li>修复选择桌面、视频、音乐或者其他普通目录，窗口上的地址显示未居中的问题</li> 
 <li>修复复制途中剪切源文件夹目录到其他目录中，点击暂停按钮后文管崩溃的问题</li> 
 <li>修复内存泄露的问题</li> 
 <li>修复右上角菜单列表缺失部分选项的问题</li> 
 <li>修复在只读文件夹下选择文件ctrl+x、ctrl+v到其他目录中，ctrl+z出现错误提示的问题</li> 
 <li>修复DOCK清空回收站与文管清空回收站逻辑不一致的问题</li> 
 <li>修复卸载光驱后再挂载光驱，计算界面光驱磁盘空间信息展示错误的问题</li> 
 <li>修复回收站还原同名文件后，标记信息的文件标记错误的问题</li> 
 <li>修复进度弹窗上点击跳过后弹窗仍显示不消失的问题</li> 
 <li>修复选中标记栏目的2个文件夹，右键-打开方式-选择默认程序，点击确认无反应的问题</li> 
 <li>修复在剪切文件途中选择ftp中的文件右键，等待一段时间后系统卡死的问题</li> 
 <li>修复删除新建文件夹和子目录下为新建文件夹的文件夹，回收站内新建文件夹名称自动增加文字的问题</li> 
 <li>修复图片与缩略图对应不上的问题</li> 
 <li>修复计算机页面未隐藏应该隐藏的盘符问题</li> 
 <li>修复文件添加标记后修改字体大小，文件名字大小不会被修改的问题</li> 
 <li>修复重复发送同一个文件到vfat格式的U盘，点击替换会提示写入失败的问题</li> 
 <li>修复通过文件选择对话框开启的保险箱，保险箱属性创建时间为空的问题</li> 
 <li>修复ftp/smb文件修改原文件名称后，最近使用中访问记录未实时消失的问题</li> 
 <li>修复在桌面向ext4重复发送同一个文件，不出现重复文件提示框的问题</li> 
 <li>修复挂载ftp后从dock栏卸载，文管页面不会自动切换到默认目录仍显示ftp目录的问题</li> 
 <li>修复在文管的设置中勾选“全文搜索”，会在./config/deepin/dde-desktop创建索引的问题</li> 
 <li>修复连接4K屏时设置屏幕缩放比≧1.25，文管右边栏图标UI显示过大的问题</li> 
 <li>修复切换藏语后，壁纸库设置壁纸显示截断的问题</li> 
 <li>修复smb目录内文件夹右键-以管理员打开，打开的目录提示挂载失败的问题</li> 
</ul> 
<p>浏览器</p> 
<ul> 
 <li>新增部分扩展程序功能</li> 
 <li>优化搜索下面的显示框样式</li> 
 <li>优化支持从Chrome中导入书签</li> 
 <li>修复将网页另存到本地后，打开html文件显示错乱的问题</li> 
 <li>修复网页另存在本地后打开，标签名称乱码的问题</li> 
 <li>修复设置页面左侧导航栏菜单不统一的问题</li> 
 <li>修复部分图片在浏览器中显示不清楚的问题</li> 
</ul> 
<p>输入法</p> 
<ul> 
 <li>新增语言支持，包括简、繁、正、英、维、藏</li> 
 <li>优化首位输入法及快捷键处理</li> 
 <li>修复切换用户后，中文输入法消失的问题</li> 
 <li>修复系统语言切换为维吾尔语/藏语时，右键菜单-皮肤的子菜单未翻译的问题</li> 
 <li>修复输入法升级过程中输入法属性设置界面被打开的问题</li> 
 <li>修复同时按快捷键ctrl+shift，无法灵活切换输入法的问题</li> 
 <li>修复多次编辑输入法配置重启后，出现无效输入窗口无法切换输入法的问题</li> 
 <li>修复安装完sunpinyin后不弹出对应配置窗口的问题</li> 
 <li>修复点击输入法设置按钮多次，重复弹出多个配置窗口的问题</li> 
 <li>修复切换语言概率性出现输入法弹窗和提示安装某种包通知的问题</li> 
 <li>修复输入法管理列表样式问题</li> 
 <li>修复安装fcitx-pinyin，弹出旧输入法配置窗口的问题</li> 
 <li>修复Alt键识别为Super键的问题</li> 
 <li>修复首次安装小企鹅五笔拼音输入法后，弹出2个配置窗口的问题</li> 
 <li>修复小企鹅五笔拼音输入法安装后，未自动添加到输入法列表中的问题</li> 
 <li>修复使用华宇拼音输入法时无状态栏，且无法打开华宇配置界面的问题</li> 
</ul> 
<p>帮助手册</p> 
<ul> 
 <li>新增下载器文档内容</li> 
 <li>修复14号字体下左侧菜单项被遮挡的问题</li> 
 <li>修复搜索框左侧有异常竖线的问题</li> 
 <li>修复切换到英语语言后，搜索结果界面有部分icon不显示的问题</li> 
</ul> 
<p>下载器</p> 
<ul> 
 <li>优化应用界面的字体显示跟随系统设置而改变</li> 
 <li>修复下载器扩展进程图标和名称显示异常的问题</li> 
 <li>修复使用不同的下载方式，软件解析的资源名称、大小不一致的问题</li> 
 <li>修复部分类型的下载任务异常的问题</li> 
 <li>修复启动项里面的下载器的图标展示不准确的问题</li> 
 <li>修复概率性出现无法调用下载器下载的问题</li> 
</ul> 
<p>控制中心</p> 
<ul> 
 <li>修复插入鼠标时禁用触控板的开关打开，拔掉鼠标触控板未恢复的问题</li> 
 <li>修复无法成功删除账户的问题</li> 
 <li>修复双指双击触控板后任务栏异常的问题</li> 
 <li>修复扩展模式点击主副屏图标时控制中心位置偏移的问题</li> 
 <li>修复智能镜像源开关时开时关的问题</li> 
</ul> 
<p>相册</p> 
<ul> 
 <li>修复设置维语后，相册、时间线界面排版混乱的问题</li> 
 <li>修复删除、导入新照片、时间线选择按钮错位的问题</li> 
 <li>修复在查看图片界面主菜单退出，会关闭应用的问题</li> 
</ul> 
<p>截图录屏</p> 
<ul> 
 <li>修复截图录屏部分未翻译成对应维语和藏语的问题</li> 
</ul> 
<p>音乐</p> 
<ul> 
 <li>修复搜索结果页【播放所有】无法点击的问题</li> 
</ul> 
<p>画板</p> 
<ul> 
 <li>修复调节4K屏缩放比为2.0及2.0以上时，取色器内颜色响应迟缓的问题</li> 
 <li>修复打开画板后首次点击打印按钮或ctrl+p，未调出打印预览的问题</li> 
</ul> 
<p>看图</p> 
<ul> 
 <li>修复窗口圆角不随控制中心的窗口圆角设置变化的问题</li> 
</ul> 
<p>安装器</p> 
<ul> 
 <li>修复概率性出现系统无法安装的问题</li> 
 <li>修复/boot/efi/EFI路径下没有deepin的启动项的问题</li> 
 <li>修复语言选择对话框会覆盖到滚动条的问题</li> 
 <li>修复键盘布局总会根据语言刷新修改后的键盘布局</li> 
</ul> 
<p>邮箱</p> 
<ul> 
 <li>修复回复邮件点击发送或保存草稿后，客户端崩溃的问题</li> 
 <li>修复绑定pop3账号后关闭客户端再启动，邮件丢失的问题</li> 
 <li>修复往来邮件中删除邮件，应用出现崩溃的问题</li> 
 <li>修复单封邮件导出问题</li> 
 <li>修复邮件正文上图标随屏滚动的问题</li> 
 <li>修复聚合邮件下点击选中邮件，鼠标中键滚动无响应的问题</li> 
 <li>修复点击查看多封在加载的邮件，邮件正文一直在加载不显示的问题</li> 
 <li>修复修改字体大小后邮件正文区域显示2个滚动条，底部控件栏未置底显示的问题</li> 
 <li>修复同步接收到新邮件时，聚合邮件列表未刷新的问题</li> 
 <li>修复聚合列表邮件自动展开的问题</li> 
</ul> 
<p>软件包安装器</p> 
<ul> 
 <li>修复点击安装崩溃的问题</li> 
</ul> 
<p>硬件适配</p> 
<ul> 
 <li>新增支持不同GPU型号，包括A10、A10G、A30、PG506-232、RTX A4000、RTX A5000、T400、T600</li> 
 <li>新增适配rtl8852ae网卡，提升网络使用体验</li> 
</ul> 
<p><strong>镜像下载</strong> </p> 
<ul> 
 <li>官方：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcdimage.deepin.com%2Freleases%2F20.2.2%2Fdeepin-desktop-community-20.2.2-amd64.iso" target="_blank">http://cdimage.deepin.com/releases/20.2.2/deepin-desktop-community-20.2.2-amd64.iso</a></li> 
 <li>OSDN：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fosdn.net%2Fprojects%2Fdeepin%2Fstorage%2F20.2.2" target="_blank">https://osdn.net/projects/deepin/storage/20.2.2</a></li> 
 <li>SourceForge：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fdeepin%2Ffiles%2F20.2.2%2Fdeepin-desktop-community-20.2.2-amd64.iso" target="_blank">https://sourceforge.net/projects/deepin/files/20.2.2/deepin-desktop-community-20.2.2-amd64.iso</a></li> 
 <li>百度网盘：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1gVmDkYyQTfQYZb_p1MvUHQ" target="_blank">https://pan.baidu.com/s/1gVmDkYyQTfQYZb_p1MvUHQ</a>（提取码: n7uk）</li> 
 <li>Google Drive：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F151KDDRyvx8QTijB8LdloV-ByHlwGotRa%3Fusp%3Dsharing" target="_blank">https://drive.google.com/drive/folders/151KDDRyvx8QTijB8LdloV-ByHlwGotRa</a></li> 
 <li>BT：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mediafire.com%2Ffolder%2F8rafnt1zqihru%2Fdeepin_20.2.2" target="_blank">https://www.mediafire.com/folder/8rafnt1zqihru/deepin_20.2.2</a></li> 
</ul>
                                        </div>
                                      
</div>
            