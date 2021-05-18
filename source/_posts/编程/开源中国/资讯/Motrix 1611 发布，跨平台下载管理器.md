
---
title: 'Motrix 1.6.11 发布，跨平台下载管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2743'
author: 开源中国
comments: false
date: Tue, 18 May 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2743'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Motrix 是一款全能的下载工具，支持下载 HTTP、FTP、BT、磁力链等资源。</p> 
<p>Motrix 1.6.11 正式发布，该版本更新内容如下：</p> 
<ul> 
 <li>新特性：新应用图标</li> 
 <li>新特性：新任务详细信息面板 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F921" target="_blank">#921</a></li> 
 <li>新特性：菜单栏托盘速度计（仅适用于macOS） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F720" target="_blank">#720</a></li> 
 <li>新特性：支持Apple Silicon M1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F836" target="_blank">#836</a>，感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fshatyuka" target="_blank">@Shatyuka</a></li> 
 <li>新特性：重新设计的 Motrix Scheme <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F716" target="_blank">#716</a></li> 
 <li>新特性：偏好设置——Tracker 添加了 CDN源</li> 
 <li>新特性：偏好设置——传输设置 添加了更多速度选项</li> 
 <li>新特性：完全重置下载会话记录，清空所有任务</li> 
 <li>新特性：偏好设置——BT设置 持续播种</li> 
 <li>新特性：偏好设置——BT设置 将磁力链接保存为种子文件</li> 
 <li>新特性：任务进度信息显示连接种子数</li> 
 <li>新特性：新增加了一个 aria2 的默认 UA</li> 
 <li>新特性：国际化新增了波兰语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F731" target="_blank">#731</a></li> 
 <li>新特性：国际化新增了匈牙利语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F754" target="_blank">#754</a></li> 
 <li>新特性：国际化新增了希腊语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F774" target="_blank">#774</a></li> 
 <li>新特性：国际化新增了意大利语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F794" target="_blank">#794</a></li> 
 <li>新特性：国际化新增了罗马尼亚语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F844" target="_blank">#844</a></li> 
 <li>新特性：国际化新增了阿拉伯语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F833" target="_blank">#833</a>， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F919" target="_blank">#91</a></li> 
 <li>新特性：偏好设置—实验室适配深色模式</li> 
 <li>新特性：任务详情文件面板支持修改选择下载的文件</li> 
 <li>修复：菜单点击新增任务 uri 参数错误</li> 
 <li>修复：偏好设置——运行模式 仅在 macOS 中显示</li> 
 <li>修复：停止 BT 任务播种通知错乱 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fissues%2F604" target="_blank">#604</a></li> 
 <li>修复：将 TrackersListCollection other.txt 替换为 http.txt <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Fpull%2F809" target="_blank">#809</a></li> 
 <li>修复：系统托盘菜单的崩溃问题</li> 
 <li>修复：引擎无法退出的问题</li> 
 <li>修复：偏好设置实验室页面使用 iframe 替换 webview</li> 
 <li>修复：应用界面阴影不完整的问题</li> 
 <li>修复：macOS Big Sur 托盘图标颜色</li> 
 <li>修复：函数重载错误，无法触发 EngineClient 中绑定的事件</li> 
 <li>修复：停止做种的参数错误</li> 
 <li>修复：替换了应用信息弹层的应用图标</li> 
 <li>修复：任务详情弹层关闭按钮不易点击的问题</li> 
 <li>修复：应用自动更新异常处理的问题</li> 
 <li>修复：自动切换主题尝试适配 Windows 和 Linux</li> 
 <li>修复：新增任务时任务重命名触发了重命名规则的问题</li> 
 <li>修复：移除任务时打开状态的任务详情未自动关闭的问题</li> 
 <li>修复：信息提醒被任务详情遮挡的问题</li> 
 <li>修复：任务详情下载进度图例未居中的问题</li> 
 <li>优化：调整了任务条目的最小高度</li> 
 <li>优化：任务进度信息字体样式</li> 
 <li>优化：表单提交动作位置固定</li> 
 <li>优化：引擎守护进程重构为 Node 子进程</li> 
 <li>优化：使用 @electron/remote 替换 Electron Remote 模块</li> 
 <li>优化：暂停任务使用强制暂停</li> 
 <li>优化：主菜单应用退出逻辑</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagalwood%2FMotrix%2Freleases" target="_blank">https://github.com/agalwood/Motrix/releases</a></p>
                                        </div>
                                      
</div>
            