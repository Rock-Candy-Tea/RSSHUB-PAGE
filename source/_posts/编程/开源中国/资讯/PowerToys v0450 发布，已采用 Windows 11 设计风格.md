
---
title: 'PowerToys v0.45.0 发布，已采用 Windows 11 设计风格'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8581'
author: 开源中国
comments: false
date: Sat, 04 Sep 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8581'
---

<div>   
<div class="content">
                                                                                            <p>PowerToys 0.45 版本中的目标主要集中在稳定性更新和优化、安装程序更新、一般错误修复和可访问性改进。主要更新内容如下：</p> 
<h3>更改日志</h3> 
<ul> 
 <li>移除了 ModuleImageLink</li> 
 <li>用 combobox 替换了主题 radiobuttons 设置</li> 
 <li>StyleCop 和警告的修复</li> 
 <li>删除了未使用的命名空间别名</li> 
 <li>标准化 System.Text.Json 上的 .NET JSON</li> 
 <li>修正了各种 .xaml 破损的链接和图标</li> 
 <li>更新了 "编辑布局" 和 "创建自定义布局" 控件的名称属性，使其不包括私有的 Unicode 字符</li> 
 <li>将 <code>bitmask</code> 变量从 size_t 改为 uint64_t，这将使 PowerToys 能够支持每个布局超过 40 个区域</li> 
 <li>调整了遥测数据，以更好地分辨 PowerToys Run 在开机时的启动情况</li> 
 <li>插件 "Direct activation phrase"设置改名为 "Direct activation string"</li> 
 <li>变化时更新环境变量</li> 
</ul> 
<h3>常规</h3> 
<ul> 
 <li>使用 Fluent UX 更新了设置和 OOBE 窗口，与即将推出的 Windows 11 界面保持一致</li> 
 <li>在设置中增加了显示版本历史的按钮</li> 
 <li>签署了 PowerToysSetupCustomActions.dll</li> 
 <li>改进了更新可用和更新就绪信息</li> 
 <li>改进了自动更新的体验</li> 
 <li>将 OOBE 主题颜色与设置主题颜色对齐</li> 
 <li>将 "以管理员身份重启" 按钮的标签调整为 "以管理员身份重启 PowerToys"，以避免歧义</li> 
 <li>在设置侧边栏增加了彩色图标</li> 
 <li>修正了 OOBE 中 Microsoft Docs 和 PowerToys 发行说明链接无法通过键盘导航的可访问性问题</li> 
 <li>修正了设置标题的对齐方式</li> 
 <li>修正了安装 PowerToys 时文件使用中的问题引起的错误</li> 
 <li>修正了当 PowerToys 以管理员身份运行时，从开始菜单打开设置的问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FPowerToys%2Freleases%2Ftag%2Fv0.45.0" target="_blank">https://github.com/microsoft/PowerToys/releases/tag/v0.45.0</a></p>
                                        </div>
                                      
</div>
            