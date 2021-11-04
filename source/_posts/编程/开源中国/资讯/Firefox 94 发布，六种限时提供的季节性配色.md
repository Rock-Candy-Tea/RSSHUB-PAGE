
---
title: 'Firefox 94 发布，六种限时提供的季节性配色'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b462835d0b4be48d6fe61c10ae813f9511f.gif'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 07:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b462835d0b4be48d6fe61c10ae813f9511f.gif'
---

<div>   
<div class="content">
                                                                                            <p>Firefox 94 现已发布，具体更新内容如下：</p> 
<h4>New</h4> 
<ul> 
 <li>v94 中包含了六种限时提供的有趣的季节性配色，用户可以找到一种颜色来适应（或提升）自己的每一种心情。</li> 
</ul> 
<p><img alt height="263" src="https://oscimg.oschina.net/oscnet/up-b462835d0b4be48d6fe61c10ae813f9511f.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>Firefox macOS 现在使用 Apple 的低功耗模式在 YouTube 和 Twitch 等网站上播放全屏视频，这大大延长了长时间观看时的电池寿命。</p> </li> 
 <li> <p>在此版本中，高级用户可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.mozilla.org%2Fkb%2Funload-inactive-tabs-save-system-memory-firefox" target="_blank">about:unloads</a> 通过手动卸载 tabs 而不关闭它们来释放系统资源。</p> </li> 
 <li> <p>在 Windows 上的中断减少，因为 Firefox 不会提示用户进行更新。相反，即使 Firefox 关闭，后台代理也会下载并安装更新。</p> </li> 
 <li> <p>在 Linux 上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmozillagfx.wordpress.com%2F2021%2F10%2F30%2Fswitching-the-linux-graphics-stack-from-glx-to-egl%2F" target="_blank">改进了 WebGL 性能</a>并降低了功耗。</p> </li> 
 <li> <p>为了更好地保护所有 Firefox 用户免受诸如 Spectre 之类的 side-channel 攻击，该版本引入了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhacks.mozilla.org%2F2021%2F05%2Fintroducing-firefox-new-site-isolation-security-architecture%2F" target="_blank">Site Isolation</a>。</p> </li> 
 <li> <p>正在推出与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fproducts%2Fvpn%2F" target="_blank">Mozilla VPN</a> 集成的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faddons.mozilla.org%2Ffirefox%2Faddon%2Fmulti-account-containers%2F" target="_blank">Firefox Multi-Account Containers</a> 扩展。这使得用户可以为每个容器使用不同的服务器位置。</p> </li> 
 <li> <p>默认情况下，当你使用菜单、按钮或三键命令退出浏览器或关闭窗口时，Firefox 不再发出警告。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.mozilla.org%2Fkb%2Fhow-configure-close-tab-warnings-firefox" target="_blank">更多详情</a>）</p> </li> 
 <li> <p>现在，Firefox 在 Windows 11 上运行时支持新的 Snap Layouts 菜单。</p> </li> 
</ul> 
<h4><strong>Fixed</strong></h4> 
<ul> 
 <li> <p>减少了使用 performance.mark() 和 performance.measure() API 与大量性能条目的开销。</p> </li> 
 <li> <p>修改了加载期间的 paint suppression，以极大地提高 Site Isolation 模式下的热加载性能。</p> </li> 
 <li> <p>Javascript 内存使用量略有减少。</p> </li> 
 <li> <p>Javascript 属性枚举加快。</p> </li> 
 <li> <p>实现了更好的垃圾收集调度，这改进了一些 pageload benchmarks。</p> </li> 
 <li> <p>减少了 HTTPS 连接的套接字轮询期间的 CPU 使用率。</p> </li> 
 <li> <p>更快的存储初始化。</p> </li> 
 <li> <p>通过减少主线程 I/O 改进了 cold startup。</p> </li> 
 <li> <p>关闭 devtools 现在比以往任何时候都可以回收更多的内存。</p> </li> 
 <li> <p>通过为加载和显示图像设置更高的优先级，改善了页面负载（尤其是在 Site Isolation 模式下）。</p> </li> 
 <li> <p>各种<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fsecurity%2Fadvisories%2Fmfsa2021-48%2F" target="_blank">安全修复</a>。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fen-US%2Ffirefox%2F94.0%2Freleasenotes%2F" target="_blank">https://www.mozilla.org/en-US/firefox/94.0/releasenotes/</a></p>
                                        </div>
                                      
</div>
            