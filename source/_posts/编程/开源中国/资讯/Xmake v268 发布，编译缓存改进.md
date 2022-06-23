
---
title: 'Xmake v2.6.8 发布，编译缓存改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1945'
author: 开源中国
comments: false
date: Thu, 23 Jun 2022 11:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1945'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2447" target="_blank">#2447</a>: 添加 qt.qmlplugin 规则和 qmltypesregistrar 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2446" target="_blank">#2446</a>: 支持 target 分组安装</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2469" target="_blank">#2469</a>: 产生 vcpkg-configuration.json</li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li>添加<span> </span><code>preprocessor.linemarkers</code><span> </span>策略去禁用 linemarkers 去加速 ccache/distcc</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2389" target="_blank">#2389</a>: 改进<span> </span><code>xmake run</code><span> </span>支持并行运行目标程序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2417" target="_blank">#2417</a>: 切换 option/showmenu 的默认值，默认开启</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2440" target="_blank">#2440</a>: 改进安装包的失败错误信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2438" target="_blank">#2438</a>: 确保生成的 vsxmake 工程不会随机变动</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2434" target="_blank">#2434</a>: 改进插件管理器，允许多插件管理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2421" target="_blank">#2421</a>: 改进配置选项菜单</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2425" target="_blank">#2425</a>: 添加<span> </span><code>preprocessor.gcc.directives_only</code><span> </span>策略</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2455" target="_blank">#2455</a>: 改进 emcc 的优化选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2467" target="_blank">#2467</a>: 支持回退到原始文件编译，兼容 msvc 预处理器的一些问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2452" target="_blank">#2452</a>: 添加 build.warning 策略</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2435" target="_blank">#2435</a>: 修复无法搜索带有<span> </span><code>.</code><span> </span>的包名</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2445" target="_blank">#2445</a>: 修复 windows 上 ccache 构建失败问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2452" target="_blank">#2452</a>: 修复 ccache 下，警告无法输出的问题</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            