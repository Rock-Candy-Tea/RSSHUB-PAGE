
---
title: 'Ubuntu 22.10 将更换沿用 18 年的 Gedit 文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0531/083437_7BSi_4937141.png'
author: 开源中国
comments: false
date: Tue, 31 May 2022 00:38:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0531/083437_7BSi_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Ubuntu 22.10（代号 "Kinetic Kudu"）是 Canonical 正在开发的下一个系统版本。在本月<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiscourse.ubuntu.com%2Ft%2Fproposal-gnome-text-editor-as-default-text-editor%2F28286" target="_blank">月初</a>，Ubuntu 核心开发者 Jeremy Bicha 就曾提议使用 Text Editor 作为系统默认文本编辑器，替换已使用多年的 Gedit。如今不到一个月的时间，开发团队就已完成了相关工作。</p> 
<p><img alt height="131" src="https://static.oschina.net/uploads/space/2022/0531/083437_7BSi_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Text Editor 是一个 GTK4 应用程序，自 3 月份 GNOME 42 发布以来一直作为 GNOME 核心应用程序集合的一部分。这个新的应用程序的包名是 <code>gnome-text-editor</code>，它取代了 Ubuntu 中包名为 <code>gedit</code> 的文本编辑器。</p> 
<p>后者 Gedit 在 2004 年发布的首个 Ubuntu 版本中就已内置在系统中，已沿用 18 年之久。如今 Gedit 将被新版文本编辑器 Text Editor 取代。</p> 
<p><img alt height="335" src="https://static.oschina.net/uploads/space/2022/0531/083446_wZ7o_4937141.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p><em><strong>（左：Gedit；右：Text Editor）</strong></em></p> 
<p>Gedit 初始发行于 1999 年，距今已有 23 年历时，目前最新的版本为 40.1。Gedit 最具特色的地方就是有一个灵活的插件系统，用户可以根据需要添加新功能。不过该文本编辑器在 2017 年还曾出现过没有开发者维护的情况发生。</p> 
<p>新的 Text Editor 则使用了 GTK4 和 libaadwita（Ubuntu 22.10 将完全拥抱 libaadwita）；遵守了新的桌面标准的黑暗模式；并且比 Gedit 更遵循 GNOME 的设计准则。</p> 
<p>而且 Gedit 目前最受欢迎的插件在 Text Editor 中都已成为内置功能。Text Editor 也具备更好的自动保存功能、集成了对 Vim 键绑定的支持、支持 .editorconfig 和 modelines 等，可以说优势更加明显。</p> 
<p><img alt height="501" src="https://static.oschina.net/uploads/space/2022/0531/083427_IW6f_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>对 Text Editor 感兴趣的用户现在也可以在 Ubuntu 22.04 中安装它，提前体验一下新版文本编辑器，安装方式也十分简单，仅需在终端运行以下命令：</p> 
<p><code>sudo apt install gnome-text-editor</code></p> 
<p>需要注意的是，安装后你会看到两个文本编辑器应用程序，并且都显示为 “Text Editor”，但两者图标不同。</p> 
<p><img alt height="289" src="https://static.oschina.net/uploads/space/2022/0531/083457_CFWc_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>对于未来升级至 Ubuntu 22.10 的 Gedit 用户来说，你们也无需过度担心，在 Ubuntu 22.10 中还是可以通过 <code>apt install gedit</code> 来正常安装 Gedit 的。</p> 
<p>目前 Ubuntu 22.10 正在积极开发中，按照官方开发进度，Ubuntu 22.10 将于今年 10 月 20 日发布。</p>
                                        </div>
                                      
</div>
            