
---
title: 'Tor Browser 11.0 发布，弃用 V2 Onion Services'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1110/065942_7atl_4937141.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 07:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1110/065942_7atl_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Tor Browser 是一个基于 Firefox ESR (Firefox with extended support) 的 Web 浏览器，默认配置通过 Tor 和 Vidalia 实现了个人隐私保护和匿名。</p> 
<p>Tor Browser 11.0 近日正式发布。这是第一个基于 Firefox ESR 91 的稳定版本，并包括对 Tor 0.4.6.8 的重要更新。</p> 
<p><img alt height="365" src="https://static.oschina.net/uploads/space/2021/1110/065942_7atl_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Tor Browser 有了新面貌</h3> 
<p>今年早些时候，Firefox 的用户界面进行了大幅度的重新设计，旨在简化浏览器、精简菜单，并采用了全新的标签设计。Firefox ESR 91 也首次将新的设计引入了 Tor Browser。</p> 
<p>Tor 浏览器中的每一块自定义用户界面都经过了现代化处理，以配合 Firefox 的新外观和体验。这包括更新颜色、排版和按钮等基本要素，到重新绘制每个图标以匹配新的风格。</p> 
<p><img alt height="365" src="https://static.oschina.net/uploads/space/2021/1110/070001_Us9Z_4937141.jpeg" width="700" referrerpolicy="no-referrer"></p> 
<h3>最终弃用 V2 Onion Services</h3> 
<p>去年就曾宣布 V2 Onion Services 将在 2021 年年底被弃用，自 10.5 版本发布以来，Tor Browser 一直在警告那些访问 V2 洋葱网站的用户。如今这一天终于到来了，自更新到 Tor 0.4.6.8 后，V2 洋葱服务在 Tor Browser 中不再可用，用户将收到一个 “Invalid Onion Site Address”（无效的洋葱网站地址）的错误。</p> 
<p><img alt height="365" src="https://static.oschina.net/uploads/space/2021/1110/070026_zqNB_4937141.jpeg" width="700" referrerpolicy="no-referrer"></p> 
<p>收到这个错误并不代表你的浏览器存在任何问题，相反，该问题出在访问的网站本身。如果你愿意，你可以通知网站的管理员，并鼓励他们尽快升级到 V3 服务。</p> 
<p>虽然都是以 .onion 结尾，但更安全的 V3 地址有 56 个字符，而 V2 的长度仅为 16 个字符。</p> 
<h3>已知问题</h3> 
<p>Tor Browser 11.0 中的一些已知问题：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40671" target="_blank">Bug 40671</a>: 字体无法渲染</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40679" target="_blank">Bug 40679</a>: 在 macOS 上首次启动 esr91 时功能缺失</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40667" target="_blank">Bug 40667</a>: AV1 视频在 Windows 8.1 中显示为损坏的文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40677" target="_blank">Bug 40677</a>: 更新到 11.0a9 后，一些附加组件就不处于激活状态了，每次启动都需要禁用-重启</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40666" target="_blank">Bug 40666</a>: 切换 svg.disable 会影响 NoScript 设置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fapplications%2Ftor-browser%2F-%2Fissues%2F40690" target="_blank">Bug 40690</a>: 当隐私浏览模式关闭时，浏览器 chrome 会中断</li> 
 <li>……</li> 
</ul> 
<h3>其他更新内容</h3> 
<ul> 
 <li>构建系统 
  <ul> 
   <li>Windows + OS X + Linux 
    <ul> 
     <li>更新 Go 到 1.16.9</li> 
     <li>移除 projects/clang-source</li> 
     <li>更改 bsaes 的 git url</li> 
     <li>使用 bullseye 来构建 https-everywhere</li> 
     <li>使用系统的 Python 3 来构建 https-everywhere</li> 
    </ul> </li> 
   <li>Windows + Linux 
    <ul> 
     <li>更新 binutils 到 2.35.2</li> 
    </ul> </li> 
   <li>Windows 
    <ul> 
     <li>在 win32 的 mingw 中从 SJLJ 异常处理切换到 Dwarf2</li> 
     <li>更新 Windows 工具链，以切换至 mozilla91</li> 
     <li>使用 Python 3 来运行 pe_checksum_fix.py</li> 
    </ul> </li> 
   <li>macOS 
    <ul> 
     <li>更新 macOS 的工具链，以切换至 mozilla91</li> 
    </ul> </li> 
   <li>Linux 
    <ul> 
     <li>将 Linux 的 GCC 升级至 10.3.0</li> 
     <li>更新 Linux 工具链，以切换至 mozilla91</li> 
     <li>暂时禁止在 Linux 上使用 rlbox</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.torproject.org%2Fnew-release-tor-browser-11-0" target="_blank">https://blog.torproject.org/new-release-tor-browser-11-0</a></p>
                                        </div>
                                      
</div>
            