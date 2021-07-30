
---
title: 'Android Studio'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 08:00:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Android Studio 2020.3.1（代号"Arctic Fox"）已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%2F" target="_blank">发布</a>。</p> 
<p>从 2020.3.1 起，Android Studio 开始启用新的版本号命名方案。事实上，2020.3.1 就是原计划的 4.3。<a href="https://www.oschina.net/news/142143/android-studio-arctic-fox-beta" target="_blank">谷歌称</a>采用新的方案主要是为了与 IntelliJ 的版本对齐。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png" referrerpolicy="no-referrer"></p> 
<p>新的版本号总共由四部分构成，分别是：</p> 
<blockquote> 
 <p><strong><Year of IntelliJ Version>.<IntelliJ major version>.<Studio major version>.<Studio minor/patch version></strong></p> 
</blockquote> 
<ol> 
 <li>年份：与上游保持一致（即所使用的 IntelliJ 的发布年份）</li> 
 <li>IntelliJ 主版本号：与上游保持一致（所使用的 IntelliJ 的主要版本号）</li> 
 <li>AS 的主版本号：从 1 开始，每发布一个主要版本就增加 1</li> 
 <li>AS 的补丁版本号：如果主要版本发布补丁更新，则会使用第四位数字</li> 
</ol> 
<p>因此通过 Android Studio 2020.3.1 的版本号，用户马上就能知道此版本基于 IntelliJ 2020.3，并且是该系列的首个主要版本更新。另外，为了更方便引用每个版本，在新的方案下，每个主要版本都会获得一个代号，根据动物名称从 A 到 Z 递增（与 Ubuntu 的做法类似）。Android Studio 2020.3.1 的代号为 Arctic Fox，下一个主要版本的代号为 Bumblebee。</p> 
<p>Android Studio 2020.3.1 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio" target="_blank">https://developer.android.com/studio</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-fac7d08dc4cb63a0f8f34d0ab208ee8b33c.png" referrerpolicy="no-referrer"></p> 
<h2>Android Studio 2020.3.1 更新亮点</h2> 
<h3>Android Gradle plugin 7.0.0</h3> 
<p>AS 2020.3.1 使用了最新的 Android Gradle plugin 7.0，新版本的 Android Gradle 插件包括许多更新，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%2Fgradle-plugin%237-0-0" target="_blank">详情点此查看</a>。</p> 
<h3>单元测试开始使用 Gradle test runner</h3> 
<p>为了提升测试执行的整体一致性，Android Studio 现在默认使用 Gradle 运行所有单元测试。在许多情况下，此更改不会影响在 IDE 中的测试工作流。</p> 
<p>例如，当单击上下文菜单中的 <strong>Run </strong>命令（在右键单击某个测试类时可见）或其对应的 gutter action 时 ，Android Studio 将默认使用 Gradle 运行配置来运行单元测试。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-78cf2aca39366ac776587e15ebb6cc3fca4.png" referrerpolicy="no-referrer"></p> 
<h3>支持 Jetpack Compose 工具</h3> 
<p>为预览和测试使用 Jetpack Compose 的应用程序提供额外支持 。</p> 
<ul> 
 <li>Compose preview</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/0519/112739_xLZv_2720166.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>Interactive preview</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/0730/075528_83BV_2720166.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>Deploy to device</li> 
 <li>Live Edit of literals</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/0730/075548_6L58_2720166.gif" referrerpolicy="no-referrer"></p> 
<h3>响应式布局模板</h3> 
<p>Android Studio Arctic Fox 现在包含一个新的布局模板，可调整大小以适应各种显示尺寸和应用，例如手机、可折叠设备、平板电脑和分屏模式。创建新项目或模块时，选择响应式活动模板以创建具有动态调整大小的组件的布局。</p> 
<h3><img src="https://static.oschina.net/uploads/space/2021/0730/072800_hB4C_2720166.png" referrerpolicy="no-referrer"></h3> 
<h3>新的后台任务检查器</h3> 
<p>现在可以使用新的后台任务检查器来可视化、监控和调试应用程序的后台<strong> </strong>worker。首先，将应用程序部署到运行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fjetpack%2Fandroidx%2Freleases%2Fwork" target="_blank">WorkManager library</a> 2.5.0 或更高版本的设备，然后从菜单栏中选择 <strong>View</strong> > <strong>Tool Windows</strong> > <strong>App Inspection。</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%2F" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            