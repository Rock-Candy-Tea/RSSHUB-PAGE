
---
title: 'openKylin 0.7.5 更新版本发布，完成 KMRE 适配，并修复 150+ 已知 Bug！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://openkylin.top/upload/202208/1661395016803235.png'
author: 开源中国
comments: false
date: Thu, 25 Aug 2022 15:53:00 GMT
thumbnail: 'https://openkylin.top/upload/202208/1661395016803235.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; text-align:justify"><span style="color:#3e3e3e">自openKylin 0.7版本发布后，社区便积极从各个渠道汇总大家的反馈建议，并针对0.7版本存在的问题进行优化处理。同时，我们也发起了社区活动，邀请大家参与到版本测试中，与我们携手共建。终于，在多方努力下，openKylin0.7.5更新版本操作系统正式发布。</span></p> 
<p><img alt="openKylin（开放麒麟）" src="https://openkylin.top/upload/202208/1661395016803235.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d3d3d; text-align:justify"> </p> 
<p style="color:#222222; text-align:justify"><span>本次版本更新</span><span>共修复了</span><span><span style="color:#3f49b9"><strong>150+</strong></span></span><span>已知Bug，进一步提升了系统稳定性。同时，在生态拓展上积极响应社区用户的反馈需求，集成了</span><span><span style="color:#3f49b9"><strong>麒麟移动运行</strong><strong>环境（</strong><strong>KMRE</strong><strong>）</strong></span><span style="color:#3e3e3e">，</span><span>实现桌面端和移动端的全面打通，</span><span>大幅提升用户体验，丰富了openKylin操作系统应用生态，</span><span style="color:#3e3e3e">欢迎大家下载体验！</span></span></p> 
<p><span><strong>安装方式</strong></span></p> 
<p style="color:#3d3d3d; text-align:justify"><span>1. 通过官网下载全新安装：</span></p> 
<p><span style="color:#0080ff"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openkylin.top%2Fdownloads" target="_blank">https://www.openkylin.top/downloads</a></span></p> 
<p style="color:#222222; text-align:justify"><span>2. 已安装 openKylin 0.7版本的用户通过以下方式升级：</span></p> 
<ul style="list-style-type:none"> 
</ul> 
<pre>$ sudo apt update 
$ sudo apt full-upgrade
</pre> 
<p> </p> 
<p><span><strong>Bug修复日志</strong></span></p> 
<p><span style="color:#1a1a1a"><strong>控制面板</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复特效模式关闭后重新打开控制面板，此时特性模式按钮为打开状态且且透明度调节按钮在最右侧的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复控制面板-鼠标页面的设置不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复设置缩放屏幕或方向后，右下角自动弹出电池模式窗口的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复文档编辑器默认应用为vim，双击txt文件无反应的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复滚轮速度设置为1的时候，滚动一下不是变化三行的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复主题界面没有恢复默认设置选项的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复修改密码没有达到密码规格(8位/2种字符类型)没有修改成功也无文案提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复用户手册无控制面板-触摸屏相关说明的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复自定义快捷键不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复点击输入法设置无反应的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复控制面板系统界面设置缩放不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复控制面板窗口最大化后，下拉菜单/按钮旁边三个点的菜单位置显示错位的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复主题界面光标类型设置不完全生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复系统界面没有显示器相关设置，没有电源相关设置的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复"不保存"设置分辨率/刷新率，控制面板-显示器页面的相应设置没有恢复为之前的设置的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复笔记本设置任意方向后重启设备，登录后为默认的"不旋转"的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复控制面板锁屏壁纸没有默认设置，导致登录界面也不显示背景的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复插上2个显示器桌面显示异常(一个显示器屏幕重叠，另外一个显示屏幕部分黑屏)的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复快捷键列表显示英文的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复Win+P打开系统投屏界面、控制面板-显示器页面设置多屏显示(包括 打开/关闭显示器)设置系统投屏不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复将主题设置为自定义后点击背景，在背景界面将类型设置为图片，再次在主题界面将主题设置为寻光，之后点击背景控制面板闪退的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复特效模式打开设置透明度后，关闭重新打开控制面板和重启系统特效模式按钮状态均显示关闭的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复音效主题-寻光音效未汉化的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复结束应用进程后，系统监视器卡顿的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复特效模式关闭后重新打开控制面板，此时特性模式按钮为打开状态且透明度为最低的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复开启代理按钮后将按钮关闭，此时输入框仍会保留在界面上，重新开关控制面板后消失的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>任务栏</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复开启飞行模式，继续点击蓝牙，蓝牙不能和飞行模式同时开启的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复右键任务栏点击调整位置，设置为上后任务栏仍显示在下，但是上方会空出任务栏位置导致其他组件菜单位置显示在上方的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复每次进入系统第一次无法调整任务栏位置为"上"，调整到其他位置再调整即正常的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复使用系统过程中任务栏存在偏离位置到屏幕上方的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复重启后任务栏消失的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复多次点击侧边栏，侧边栏显示偏离正确位置过多的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复点击任务栏中电源管理图标，电源管理显示偏离正确位置过多中所有固定应用的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【平板模式】修复桌面模式与平板模式来回切换，切换回桌面模式后，任务栏显示异常的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【平板模式】修复打开任意一个应用后，任务栏没有新增该应用窗口的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【RISC-V】修复右键任务栏组件菜单闪退，无法进行操作的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复已打开应用在任务栏的图标显示异常的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复在PC模式下打开任意应用后切换到平板模式，此时使用快捷键或者多任务视图关闭此应用就会清除任务栏</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复右键点击任务栏应用图标，右键菜单样式异常，且位置距离任务栏很远的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打开应用任务栏中没有打开的应用图标的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"> </p> 
<p><span style="color:#1a1a1a"><strong>多任务视图</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打开网络-非应用类窗口再点击多任务视图，此类窗口会显示在多任务视图中的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打开蓝牙-非应用类窗口再点击多任务视图，此类窗口会显示在多任务视图中的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打开声音-非应用类窗口再点击多任务视图，此类窗口会显示在多任务视图中的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>用户手册</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复用户手册仍有部分截图内容与实际控制面板不符的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打开用户手册，在搜索框输入关键字后搜狗输入法隐藏，此时多次点击ctrl+空格无法调出搜狗输入法的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复用户手册不应保留远程桌面 、更新操作（备份 更新）、 安全（安全中心）的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复从手册的搜索框搜到天气 跳转到了undefined页面等的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复部分已移除的应用 在用户手册搜索框还能搜到，比如安全中心便签贴的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复用户手册中系统安装的内容错误的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>系统安装</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【联想扬天/攀升-商祺N174外援机】修复使用全盘或者手动分区安装系统后提示找不到启动设备的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【戴尔latitude 7520】修复部分机型安装后grub文件名存在不同，且无法手动挂载成功的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【联想开天M630Z】修复部分机型安装后无法识别到启动项，需要手动挂载的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【联想天逸510Pro】修复系统自定义安装时，分区后会直接退出安装软件的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【本地安装】修复自定义安装备份还原分区未挂载的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【本地安装】修复不设置efi分区安装系统后无法进入系统的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复安装完毕后提示显示为英文的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>文件管理器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复在打开方式更多应用界面，双击应用不能打开应用，双击不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【RISC-V】修复双击计算机、回收站、openKylin文件夹后打开多个页面的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复多次插拔手机后显示两个手机图标的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复共享文件输入密码后一直提示需要输入密码的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复取消勾选全局排序后选择不同排序方式不成功的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复关于界面样式调用sdk的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复菜单重命名为英文的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复鼠标悬浮在最大化、还原、最小化按钮上时提示未汉化的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>触控板</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复控制面板搜索框中可以搜索出"触控板"中已隐藏/屏蔽的控制面板组件，结果会出现2遍触控板的组件的问题</span></p> </li> 
 <li> <p><span style="color:#333333">修复打开开始菜单中任一软件，鼠标移至窗口标题区，在触摸板上单指点按鼠标箭头没有变为小手图标的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>窗口管理器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复用户手册、文件管理器、U盘启动器、闹钟、计算器、传书、天气、扫描、录音、刻录和看图多一个标题栏的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>开始菜单</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复点击开始菜单有概率性弹出在错误位置（大概点击5次以上就会出现一次位置错误）的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复字母集中选择模式不可用字母样式不对的问题</span></p> </li> 
 <li> <p style="text-align:left"><span><span style="color:#333333">修复</span><span style="color:#000000">功能分类和字母排序模式下，固定到"所有软件"不生效</span><span style="color:#333333">的问题</span></span></p> </li> 
</ul> 
<p><strong style="color:#1a1a1a">登录</strong></p> 
<ul> 
 <li> <p style="text-align:left"><span>修复登录界面默认没有开启小键盘数字键，每次都需要手动开启的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>U盘启动器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复U盘启动器关于窗口有双标题栏的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>打印机</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复没有集成打印机，控制面板打印机界面添加不了打印机的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复打印机提示段错误，控制面板打印机界面点击"添加"无反应的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>侧边栏</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复点击侧边栏系统设置概率性打不开设置界面的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>系统监视器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复在软件商店等应用打开情况下，系统监视器应用程序界面显示无搜索结果的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复搜索一直显示无结果的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>软件更新器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复升级失败后再次升级，窗口提示的已下载升级文件大小偶尔出现倒退情况的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复 使用软件更新器更新完成后，概率没有出现提醒”用户重启系统”文案的提示弹窗的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复软件更新管理器提示"下载软件仓库信息失败"，点击继续后正常更新的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>软件商店</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【虚拟机】【virtualbox】修复无法打开软件商店的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复与开始菜单的卸载应用列表保持不一致的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复软件商店中卸载火狐浏览器后再下载，提示"下载失败，服务异常"的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复填写账号密码点击登录后，没有等待提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复软件商店最小化功能偶现性无效的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>蓝牙</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复移除连接的蓝牙耳机后，再次连接，蓝牙耳机突然在蓝牙界面消失，连接失败的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复蓝牙连接安卓手机后在十几秒内自动断连，再次点击提示连接失败，且发送文件失败的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>网络</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复登录界面连接wifi后，登录桌面任务栏网络工具显示未连接，wifi依旧关闭状态的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复普通用户在详情界面修改网络IP信息时会弹出授权框，如果不进行授权详情界面也会显示修改成功，但是实际未修改的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复WIFI输入错误密码连接失败后没有提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复多次切换平板-PC模式后，系统出现无法识别到网卡问题的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复网络相关窗口窗管三联按键悬浮显示均未汉化的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复普通用户修改WIFI信息需要授权的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复控制面板VPN界面"添加"按钮的点击效果和其他地方不一致的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复开启2.4Ghz热点后，使用其他设备可以正常连接此热点但是无法通过其网络进行上网的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>影音</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复播放没有背景的音频文件时，默认背景界面不会显示鼠标图标的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复影音媒体信息界面右侧滚动条设计不合理，显示不全的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复打开关闭媒体信息后，影音右上角关闭等按钮失去关闭，最大化最小化功能的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>截图</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复可以打开截图应用但无法使用截图功能的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>计算器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复置顶功能不生效的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复存在置顶按钮，但看不到的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>日历</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复更改时区后，任务栏日期同步会延迟半分钟的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复日历窗口可以被拖动的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>全局搜索</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复单例应用最小化后，从搜索无法将原页面呼出的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>锁屏</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复系统不操作等待5分钟必进入锁屏的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复输入5次不会锁定用户的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复在锁屏界面可以使用快捷键调出窗口或者进行窗口切换等操作的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【RISC-V】修复锁屏后无法通过正确密码进入系统的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>刻录</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复刻录应用界面未汉化的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>生物特征管理工具</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复录入指纹界面不进行录入，无录入超时提示的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>天气</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复天气title栏重复的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复天气最小化图标缺失的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复搜索框右键菜单页面显示为英文的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复天气最小化后，点击托盘的天气无法弹出天气的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>录音</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复拖动时录音闪退的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>闹钟</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复闹钟时间到，弹出的闹铃弹窗不在页面右上方的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>USD</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复Win+P打开系统投屏界面无法使用键盘上下键及回车键的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复系统投屏界面显示异常的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复系统投屏界面因背景透明选项显示不明显，且选项重复的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复系统投屏界面点击窗口外任意位置不消失，点击除方向键和enter键以外的键不消失的问题</span></p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><span style="color:#1a1a1a"><strong>账户信息</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复开启开机自动登录重启后自动关闭的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复更改用户密码为123123时不成功且无提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复修改新与旧密码相同无提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复第二次更换本地图片为头像控制面板需要关闭后才显示更换的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>电源管理</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【Mavis 平板】修复设置界面设置睡眠时间与实际生效时间不匹配的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>快捷键</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【平板模式】修复在不是触摸屏的电脑上，切换到平板模式后，之前打开的应用自动最大化，用鼠标无法呼出任务栏，希望对用户有win+D的相应提示的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【HP Pavilion x360笔记本】修复系统未集成截图软件，截图相关快捷键不生效的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>系统主题</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复右键菜单悬浮于二级菜单后，一级菜单高亮非设计稿的灰色的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复由其他主题切换为自定义主题后，壁纸变为纯蓝色图片的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复和印主题默认强调色不为设计稿中的紫色的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>输入输出设备</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复读卡器传输文件至桌面失败时，提示框未汉化的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复系统无法识别拓展坞上的鼠标、键盘的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>更新升级</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复 等待系统到达自动更新时间，更新弹窗中"稍后更新"按钮暂不明确功能的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复任务栏收纳栏存在"更新通知"图标，不明确其功能的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复更新升级后，在登录界面连接网络突现</span><span style="color:#333333">闪屏，很难登录桌面的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>桌面</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复打开多个应用窗口切换平板/PC模式，平板模式桌面存在多个已打开窗口的重复图标的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复从PC模式切换到平板模式后设置屏幕旋转，平板模式桌面没有适配的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【RISC-V】修复右键菜单出现黑色边框的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【平板模式】修复在桌面模式打开多个应用，切换至平板模式后，当前窗口没有最大化的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>声音</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【HP Pavilion x360笔记本】修复系统默认无音频输入输出，接入耳机正常的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">【虚拟机】【virtualbox】修复系统音量固定在17%，无论是向左还是向右拖动都会回弹到17%的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>软件安装器</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">【wayland】修复双击deb包/deb包右键-打开无反应，没有默认使用安装器打开的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>U盘管理工具</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复浅色模式插入U盘后，鼠标光标悬浮在任务栏弹出的的U盘管理工具上，几乎看不到悬浮效果的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>三方应用</strong></span></p> 
<ul> 
 <li> <p><span style="color:#333333">【wayland】修复【wps】打开excel表格，界面表格显得过于紧凑，输入的文字和左边的编号显示不全的问题</span></p> </li> 
</ul> 
<p><span style="color:#1a1a1a"><strong>RISC-V-starfive</strong></span></p> 
<ul> 
 <li> <p style="text-align:left"><span style="color:#333333">修复无法连接有线网络的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复TeXdoctk无法打开的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复无法打开txt文件的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复生物特征管理工具无法打开的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复无浏览器的问题</span></p> </li> 
 <li> <p style="text-align:left"><span style="color:#333333">修复无法打开多任务视图的问题</span></p> </li> 
 <li> <p><span style="color:#333333">修复缺少视频、音频、图像查看软件的问题</span></p> </li> 
</ul> 
<p><span>同时，如有更多Bug反馈，大家可以前往openKylin Gitee提交issue进行反馈。</span></p>
                                        </div>
                                      
</div>
            