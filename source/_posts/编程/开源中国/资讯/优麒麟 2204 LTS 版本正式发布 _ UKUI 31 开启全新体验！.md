
---
title: '优麒麟 22.04 LTS 版本正式发布 _ UKUI 3.1 开启全新体验！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0374c4be38c124d6353f7953859f76a451a.png'
author: 开源中国
comments: false
date: Fri, 22 Apr 2022 06:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0374c4be38c124d6353f7953859f76a451a.png'
---

<div>   
<div class="content">
                                                                                            <p>2022 年 4 月 22 日，优麒麟团队正式发布新版本 <strong>22.04 LTS</strong>。22.04 是继 14.04、16.04、18.04 和 20.04 之后的第五个长期支持（LTS）版本，官方将提供 3 年的技术支持。</p> 
<p><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-0374c4be38c124d6353f7953859f76a451a.png" referrerpolicy="no-referrer"></p> 
<p>与上一版本相比，此次更新版本新增了显示剩余充电时间、复杂触摸手势及操作动画教学、系统浅色模式设置、微信在线登录和支持开启个人热点等新功能。进一步优化了任务栏区域展现形式、任务栏启动时间、通知弹窗动画和文件管理器侧边栏层级，并修复了 Ctrl+Q 无法关闭音乐程序、刻录应用内存泄漏风险等已知问题。</p> 
<p>秉承一切以用户为主的理念，优麒麟持续优化交互体验和系统稳定性。本次更新版本默认搭载 <strong>Linux 5.15 LTS 内核</strong>和全新 <strong>UKUI 3.1</strong> 桌面环境，并对<strong>多款麒麟自研应用进行了全面升级</strong>。</p> 
<h4><strong>最新 Linux 5.15 LTS 内核 - 兼容性更高、更稳定</strong></h4> 
<p><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-d127e1b8eb1ff1e5040c6002ff33e5a80b3.png" referrerpolicy="no-referrer"></p> 
<p><strong>重要更新:</strong></p> 
<ul> 
 <li> <p>改进的 NTFS 文件系统支持；</p> </li> 
 <li> <p>新的 SMB3 文件服务器 (KSBMD)；</p> </li> 
 <li> <p>为基于 AMD Zen 3 的 APU 添加了温度监控支持；</p> </li> 
 <li> <p>华硕 ACPI 平台配置文件支持；</p> </li> 
 <li> <p>改进了对英特尔第 12 代 CPU 的支持；</p> </li> 
 <li> <p>合并了 Realtek RTL8188EU WiFi 驱动程序以替换之前的 Realtek WiFi 驱动程序。</p> </li> 
</ul> 
<h4><strong>全新 UKUI 3.1 桌面环境</strong></h4> 
<p>UKUI 3.1 以“寻光”为主题，引入了时尚且富有科技感的“大圆角设计”和“光影变换”的设计理念，启用全新 logo 设计，让系统变得更具个性与品味。除了主题的更新之外，全新 UKUI 3.1 还在系统交互体验上进行了升级优化，让你的整体操作也更加舒适、简单和自由，给你带来崭新体验！</p> 
<p><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-d2a0707254fc44cd4ec48b2b3153d6f4a5e.png" referrerpolicy="no-referrer"></p> 
<h4><strong>自研应用全面升级</strong></h4> 
<p>在本次发布的 22.04 LTS 版本操作系统中，还针对麒麟计算器、麒麟截图、麒麟影音、麒麟录音、麒麟摄像头等<strong>十余款麒麟自研应用进行了全面升级，不仅丰富了应用功能，还对已有功能和组件进行了优化，进一步提升你的使用体验</strong>。</p> 
<p><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-7a0f079d0a6d952e7425ed5c0bf7bd55711.png" referrerpolicy="no-referrer"></p> 
<p><strong>安装方式</strong></p> 
<p>1.目前，优麒麟用户和其他 Linux 爱好者均可以通过<strong>优麒麟官网</strong>或<strong>镜像站</strong>在线下载安装优麒麟 22.04 LTS 版本。</p> 
<p>2.已安装 20.04 Pro SP1 正式版的用户可以通过如下方法更新至 22.04 LTS 版本：</p> 
<ul> 
 <li>打开终端输入以下命令：</li> 
</ul> 
<pre><code>$ sudo apt update
$ sudo apt upgrade
$ sudo do-release-upgrade --allow-third-party -d
</code></pre> 
<p><strong>注意:</strong></p> 
<ol> 
 <li> <p>跨版本升级，由于底层库变动，可能导致一些应用无法打开等未知问题；</p> </li> 
 <li> <p>升级过程中，有需要选择的地方，除非有特殊需求，一般按回车即可。</p> </li> 
</ol> 
<p><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-a370d2b6ff1eef61a57582fec583263dbce.gif" referrerpolicy="no-referrer"></p> 
<h2><strong>系统功能改进与 BUG 修复日志</strong></h2> 
<p><strong>桌面环境改动</strong></p> 
<p><strong>开始菜单</strong></p> 
<ul> 
 <li> <p>新增应用收藏功能</p> </li> 
 <li> <p>新增最近文件模块，能快速打开最近编辑的文档</p> </li> 
 <li> <p>支持隐藏数据上传接口的具体调用方式，暴露接口限制指定应用可以访问，增加系统安全性</p> </li> 
 <li> <p>优化排序类别切换和放大到全屏菜单操作动效</p> </li> 
</ul> 
<p><strong>任务栏</strong></p> 
<ul> 
 <li> <p>新增打开应用区及托盘区的控件三态</p> </li> 
 <li> <p>支持任意拖拽图标位置</p> </li> 
 <li> <p>优化用户因切换产生的异步感，采用全新统一界面交互模式</p> </li> 
 <li> <p>优化任务栏启动时间</p> </li> 
 <li> <p>优化任务栏区域的使用，采用全新二合一展现形式</p> </li> 
</ul> 
<p><strong>电源管理</strong></p> 
<ul> 
 <li> <p>新增电池平衡模式策略</p> </li> 
 <li> <p>新增显示剩余充电时间的功能</p> </li> 
 <li> <p>新增在低电量或电池状态下自动开启节能模式功能</p> </li> 
 <li> <p>新增极低电量保护行为，保证在极低电量的时候提示用户充电</p> </li> 
 <li> <p>支持在托盘界面便捷拖动改变电池策略功能</p> </li> 
 <li> <p>支持自定义切换电源电池性能、平衡、节能三种策略模式</p> </li> 
 <li> <p>支持自定义低电量</p> </li> 
</ul> 
<p><strong>侧边栏</strong></p> 
<ul> 
 <li> <p>支持快捷操作常用功能，如投屏、蓝牙、亮度调节等</p> </li> 
 <li> <p>优化删除通知交互动效</p> </li> 
 <li> <p>优化通知中心逻辑，将未查看到的所有消息收纳到侧边栏</p> </li> 
</ul> 
<p><strong>通知</strong></p> 
<ul> 
 <li> <p>新增通知协议配置，支持自定义通知消息常驻，驻留时间，关闭消息等功能</p> </li> 
 <li> <p>支持点击消息实时跳转至应用界面功能</p> </li> 
 <li> <p>优化通知弹窗，超时消失后入驻侧边栏，便捷查看</p> </li> 
 <li> <p>优化通知弹窗动画</p> </li> 
</ul> 
<p><strong>搜索</strong></p> 
<ul> 
 <li> <p>新增搜索便签本内容功能</p> </li> 
 <li> <p>支持键盘操作搜索结果</p> </li> 
 <li> <p>优化文件索引内存占用，峰值不超过500m</p> </li> 
 <li> <p>优化磁盘io占用，通过inotify信号增加缓冲队列和合并处理</p> </li> 
</ul> 
<p><strong>用户配置服务（USD）</strong></p> 
<ul> 
 <li> <p>支持主题切换</p> </li> 
 <li> <p>支持毛玻璃显示效果</p> </li> 
</ul> 
<p><strong>网络</strong></p> 
<ul> 
 <li> <p>新增agent功能，实现用户隔离</p> </li> 
 <li> <p>新增多网卡选项，支持有线多网卡管理</p> </li> 
 <li> <p>新增创建无线热点功能，支持4G、5G</p> </li> 
 <li> <p>新增网络配置详情页，支持用户直接新建配置</p> </li> 
 <li> <p>新增对ttls类型企业网络的支持</p> </li> 
 <li> <p>支持关闭 / 开启有线网卡</p> </li> 
 <li> <p>优化有线列表排序，提升性能</p> </li> 
</ul> 
<p><strong>触摸屏方案</strong></p> 
<ul> 
 <li> <p>新增复杂触摸操作动画演示功能</p> </li> 
 <li> <p>新增双指连续滚动列表和页面功能</p> </li> 
 <li> <p>新增四指打开全局搜索和切换各应用窗口功能</p> </li> 
 <li> <p>新增“更多手势”功能，支持用户快捷查询系统所有触摸手势</p> </li> 
 <li> <p>支持单指操作呼出侧边栏、展示所有任务窗口等场景功能</p> </li> 
</ul> 
<p><strong>多任务视图</strong></p> 
<ul> 
 <li> <p>支持新建/删除工作区</p> </li> 
 <li> <p>支持应用窗口自由移动至各工作区</p> </li> 
</ul> 
<p><strong>控制面板</strong></p> 
<ul> 
 <li> <p>新增系统浅色模式设置</p> </li> 
 <li> <p>实现多屏场景下，智能检测并提示当前显示器类型</p> </li> 
 <li> <p>支持修改计算机名</p> </li> 
 <li> <p>支持修改用户昵称</p> </li> 
 <li> <p>支持多种登录选项，新增生物识别认证</p> </li> 
 <li> <p>支持寻光、启典、和印三套系统主题自由切换</p> </li> 
 <li> <p>支持自定义屏保程序</p> </li> 
 <li> <p>支持自定义桌面背景显示方式</p> </li> 
 <li> <p>支持自定义设置apt代理服务和端口</p> </li> 
 <li> <p>优化异常提示文案以及显示效果</p> </li> 
</ul> 
<p><strong>蓝牙</strong></p> 
<ul> 
 <li> <p>新增多文件传输功能</p> </li> 
 <li> <p>新增蓝牙设备分类功能</p> </li> 
 <li> <p>实现蓝牙托盘、蓝牙设置和服务剥离功能，提高了蓝牙使用流畅度和稳定性</p> </li> 
</ul> 
<p><strong>登录</strong></p> 
<ul> 
 <li> <p>新增网络配置功能</p> </li> 
 <li> <p>新增扫码登陆功能</p> </li> 
 <li> <p>实现人脸、指纹、指纹仪等统一认证功能</p> </li> 
</ul> 
<p><strong>锁屏屏保</strong></p> 
<ul> 
 <li>支持秒级登录，快速进入桌面环境</li> 
</ul> 
<p><strong>生物识别管理</strong></p> 
<ul> 
 <li>新增生物特征应用范围，如登录、授权等</li> 
</ul> 
<p><strong>授权</strong></p> 
<ul> 
 <li>新增生物特征、二维码授权</li> 
</ul> 
<p><strong>系统监视器</strong></p> 
<ul> 
 <li> <p>新增应用进程分类</p> </li> 
 <li> <p>新增服务程序列表</p> </li> 
 <li> <p>实时显示处理器、网络速率</p> </li> 
</ul> 
<p><strong>用户手册</strong></p> 
<ul> 
 <li> <p>新增应用手册搜索功能</p> </li> 
 <li> <p>支持控制面板二级模块跳转</p> </li> 
 <li> <p>优化首页应用分类</p> </li> 
</ul> 
<p><strong>文件管理器</strong></p> 
<ul> 
 <li> <p>新增大文件删除策略，大于 10G 的文件仅支持永久删除</p> </li> 
 <li> <p>优化侧边栏层级</p> </li> 
</ul> 
<p><strong>主题</strong></p> 
<ul> 
 <li> <p>实现第三套和印风格图标主题</p> </li> 
 <li> <p>实现高分辨率下光标跟随缩放</p> </li> 
</ul> 
<p><strong>会话管理器</strong></p> 
<ul> 
 <li> <p>新增系统监视器快速入口</p> </li> 
 <li> <p>支持用户切换功能区分单/多用户场景</p> </li> 
</ul> 
<p><strong>主题框架</strong></p> 
<ul> 
 <li> <p>新增应用三态自由切换主题功能</p> </li> 
 <li> <p>实现平台主题新调色板接口开发</p> </li> 
 <li> <p>实现UKUI 3.1所有基础控件重构开发</p> </li> 
 <li> <p>修复所有控件直角问题</p> </li> 
</ul> 
<p><strong>（托盘）u盘工具</strong></p> 
<ul> 
 <li> <p>适配 UI 主题配色</p> </li> 
 <li> <p>优化设备信息获取、热插拔消息通知显示</p> </li> 
</ul> 
<p><strong>闹钟</strong></p> 
<ul> 
 <li> <p>新增一键静音功能</p> </li> 
 <li> <p>新增设置闹钟稍后提醒功能</p> </li> 
 <li> <p>新增迷你倒计时窗口</p> </li> 
 <li> <p>新增标记最长最短计次间隔功能</p> </li> 
 <li> <p>支持闹钟项右键编辑功能</p> </li> 
 <li> <p>支持自定义铃声</p> </li> 
 <li> <p>优化放大闹钟时间编辑，倒计时设置时间滚轮字体</p> </li> 
 <li> <p>优化倒计时运行UI，提升用户交互体验</p> </li> 
</ul> 
<p><strong>应用软件改动</strong></p> 
<p><strong>天气</strong></p> 
<ul> 
 <li> <p>增加了“是否允许定位”判断</p> </li> 
 <li> <p>添加了背景色调整功能</p> </li> 
 <li> <p>优化搜索下拉框样式</p> </li> 
 <li> <p>优化了主页面的展示布局</p> </li> 
</ul> 
<p><strong>刻录</strong></p> 
<ul> 
 <li> <p>修复了拖拽文件到软件中时可能存在的错误</p> </li> 
 <li> <p>修复了软件内部已知的内存泄露问题</p> </li> 
 <li> <p>更新了用户手册中图片以及相应的解释说明</p> </li> 
</ul> 
<p><strong>计算器</strong></p> 
<ul> 
 <li>增加了进制换算功能</li> 
</ul> 
<p><strong>传书</strong></p> 
<ul> 
 <li>增加了好友&聊天内容搜索功能</li> 
</ul> 
<p><strong>看图</strong></p> 
<ul> 
 <li> <p>新增了左侧可隐藏的侧边栏</p> </li> 
 <li> <p>增加了剪裁功能</p> </li> 
 <li> <p>增加了另存为功能</p> </li> 
 <li> <p>支持图片重命名</p> </li> 
 <li> <p>支持应用内打印</p> </li> 
 <li> <p>支持exr、psd、jfi格式图片</p> </li> 
</ul> 
<p><strong>打印</strong></p> 
<ul> 
 <li> <p>支持打印机属性设置和卸载打印机</p> </li> 
 <li> <p>支持打印机手动、自动适配、驱动下载</p> </li> 
</ul> 
<p><strong>录音</strong></p> 
<ul> 
 <li> <p>新增音频剪裁功能</p> </li> 
 <li> <p>支持录制系统声音</p> </li> 
 <li> <p>优化了菜单栏提示信息</p> </li> 
</ul> 
<p><strong>扫描</strong></p> 
<ul> 
 <li>解决了部分适配问题</li> 
</ul> 
<p><strong>截图</strong></p> 
<ul> 
 <li> <p>增加消息弹框的联动</p> </li> 
 <li> <p>优化绘制工具的功能</p> </li> 
</ul> 
<p><strong>软件商店</strong></p> 
<ul> 
 <li> <p>新增删除自身评价、主菜单设置功能（完成后台自动更新应用以及允许应用更新通知)</p> </li> 
 <li> <p>增加软件图片显示数量，多角度展示软件内容</p> </li> 
 <li> <p>支持搜索框一键清空全部内容</p> </li> 
 <li> <p>优化软件详情页内容及布局调整</p> </li> 
 <li> <p>优化应用更新模块，默认显示待更新软件数量</p> </li> 
</ul> 
<p><strong>U盘启动器</strong></p> 
<ul> 
 <li> <p>添加了右键点击镜像文件，打开U盘启动器</p> </li> 
 <li> <p>更新了用户手册</p> </li> 
</ul> 
<p><strong>摄像头</strong></p> 
<ul> 
 <li> <p>新增了网格线功能</p> </li> 
 <li> <p>新增了连拍功能</p> </li> 
 <li> <p>优化了菜单栏样式</p> </li> 
 <li> <p>优化了设置弹窗样式</p> </li> 
 <li> <p>优化了历史入口打开入口样式</p> </li> 
</ul> 
<p><strong>影音</strong></p> 
<ul> 
 <li>适配高版本qt</li> 
</ul> 
<p><strong>音乐</strong></p> 
<ul> 
 <li> <p>修复了Ctrl+Q无法关闭音乐程序</p> </li> 
 <li> <p>修复了播放音乐进入S4，显示器黑屏后声音会继续播放1-2S</p> </li> 
 <li> <p>修复了右键正在播放中的音乐会概率性应用闪退</p> </li> 
 <li> <p>修复了taglib版本依赖问题</p> </li> 
</ul>
                                        </div>
                                      
</div>
            