
---
title: 'wxPython 4.2.0 发布，流行的跨平台 Python GUI 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0826/160307_GDZt_2720166.png'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 07:10:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0826/160307_GDZt_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>自上次发布 4.1.1 稳定版后，wxPython 已接近两年没有更新过。因此，wxPython 开发团队在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwxpython.org%2Fnews%2F2022-08-07-wxpython-411-release%2Findex.html" target="_blank">宣布 4.2.0 </a>的更新时，第一句话就是关于“项目死亡”的辟谣：</p> 
<blockquote> 
 <p><em>"Rumors of my death are only slightly exaggerated"<br> "关于我死亡的谣传稍微有点夸大了"</em></p> 
 <p><img src="https://static.oschina.net/uploads/space/2022/0826/160307_GDZt_2720166.png" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p>团队已将 wxPython 4.2.0 发布到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2FwxPython%2F4.2.0" target="_blank"> PyPI</a>，并将部分附加文件上传至 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fextras.wxpython.org%2FwxPython4%2Fextras%2F" target="_blank">Extras</a>。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li>​​使用 wxWidgets 3.2.0 构建</li> 
 <li>对构建脚本进行小调整，以确保在非 Windows 平台上，默认使用的编译器和 flag 与 wxWidgets 使用的一致（加上 Python 所需的 flag）。如果需要，可以通过在环境中设置 CC 和 CXX 来覆盖编译器命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FPhoenix%2Fissues%2F1247" target="_blank">#1247</a></li> 
 <li>修复在 Windows 上<code>time_t</code><span> 始终被当作 32 位值的问题</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FPhoenix%2Fissues%2F1910" target="_blank">#1910</a></li> 
 <li>添加 wx.FullScreenEvent 和 wx.EVT_FULLSCREEN.</li> 
 <li>移除老旧、仅适用于 OSX 的 wx.webkit 模块</li> 
 <li>修复在 Windows 上使用 Python 3.10 构建 wxPython 出现的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FPhoenix%2Fissues%2F2016" target="_blank">#2016</a></li> 
 <li>修复使用<span>深色主题时 lib.plot 中的不可见文本</span></li> 
 <li>支持更新的 PyMuPDF 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FPhoenix%2Fissues%2F2205" target="_blank">#2205</a></li> 
 <li>使用 MinGW 工具链构建 wxPython 得到了一些简化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FPhoenix%2Fissues%2F2211" target="_blank">#2211</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwxpython.org%2Fnews%2F2022-08-07-wxpython-411-release%2Findex.html" target="_blank">详情查看发布公告</a>。</p> 
<p>wxPython 是流行的跨平台 Python GUI 库，封装了 wxWidgets。开发者使用 wxPython 可为他们的 Python 应用创建原生用户界面，这些应用程序在 Windows、Mac 和 Linux 或其他类 unix 系统上几乎不需要修改即可运行。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-faa64af251f05d2c5a54cb56a5353d5c9ff.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            