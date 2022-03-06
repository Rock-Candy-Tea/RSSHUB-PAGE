
---
title: 'Android Studio Dolphin Canary 5 发布，支持调试 Kotlin 协程'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-472a74303c37b41086eae918c79376540b2.png'
author: 开源中国
comments: false
date: Sun, 06 Mar 2022 07:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-472a74303c37b41086eae918c79376540b2.png'
---

<div>   
<div class="content">
                                                                                            <p>Android Studio - 海豚 | 2021.3.1 Canary 5 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2022%2F03%2Fandroid-studio-dolphin-canary-5-now.html" target="_blank">已发布</a>，现在可在 Canary 和 Dev 频道中使用，该版本的最大新特性就是支持调试 Kotlin 协程。</p> 
<h3>新特性</h3> 
<h4>支持调试 Kotlin 协程</h4> 
<p style="margin-left:0px">Android Studio Dolphin 增加了对在 Android 项目中调试 Kotlin 协程的支持，类似于 IntelliJ IDEA 2021.3 及更高版本中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Fdebug-kotlin-coroutines.html" target="_blank">的调试功能。</a>注意：该功能适用于 kotlinx-coroutine-core <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKotlin%2Fkotlinx.coroutines%2Freleases%2Ftag%2F1.6.0" target="_blank">1.6.0</a> 或更高版本。</p> 
<p style="margin-left:0px"><img alt height="331" src="https://oscimg.oschina.net/oscnet/up-472a74303c37b41086eae918c79376540b2.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">在 <strong>Suspend</strong> 函数中设置断点时，请确保断点将 <strong>Suspend </strong>设置为 <strong>All</strong>。 </p> 
<p style="margin-left:0px">当应用程序遇到断点时，可以在<strong> Coroutines </strong>选项卡中看到按调度程序分组的协程及其阶段。使用 Variables 选项卡可以在每个断点处调查协同程序中可用的局部变量和字段的值。</p> 
<p style="margin-left:0px"><img alt height="191" src="https://oscimg.oschina.net/oscnet/up-b98a879ef9245281a4ff0e6b8d2cd2380af.png" width="640" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><img alt height="468" src="https://oscimg.oschina.net/oscnet/up-7d1f5229b52096367d2132ac33873a016d2.png" width="640" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span>已知的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<h4><span><span><span><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span>工具菜单中缺少 Firebase 选项</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<div>
 <span><span><span><span style="color:rgba(0, 0, 0, 0.87)"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>从 Android Studio Dolphin Canary 5 开始，工具菜单中缺少的 Firebase 选项可以通过执行 <span><span><span>double-shift </span></span></span>搜索或 <span><span><span>ctrl-shift-a </span></span></span>查找操作，然后搜索“ <span><span><span>firebase</span></span></span> ”来找到。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
</div> 
<div>
  
</div> 
<div>
 更多修复项可在 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%2Ffixed-bugs%2Fstudio%2F2021.3.1%23android-studio-dolphin-canary-3-2021.3.1.5" target="_blank">发行公告</a>中查看。
</div>
                                        </div>
                                      
</div>
            