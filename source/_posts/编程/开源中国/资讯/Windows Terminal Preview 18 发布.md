
---
title: 'Windows Terminal Preview 1.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4cf37e9036f7d3beb6e84add66429115d61.png'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 23:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4cf37e9036f7d3beb6e84add66429115d61.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Windows Terminal Preview 1.8 已发布，按照其发布计划，只要新版本进入 Preview 阶段，上一个版本的所有预览功能就会进入稳定阶段，因此 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fterminal%2Freleases%2Ftag%2Fv1.7.1033.0" target="_blank">Windows Terminal v1.7</a> 稳定版也已同步推出。</p> 
<p>Windows Terminal Preview 1.8 更新亮点：</p> 
<ul> 
 <li> <p><strong>Settings UI is default in stable</strong></p> </li> 
</ul> 
<p>settings UI 现在随 Windows Terminal 稳定版一起提供。用户可以通过点击下拉菜单中的设置按钮或输入 Ctrl+，来访问 settings UI。目前， settings UI 的体验还在持续改进当中。</p> 
<p><img alt height="465" src="https://oscimg.oschina.net/oscnet/up-4cf37e9036f7d3beb6e84add66429115d61.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p><strong>Shift+Click 在新窗口中打开一个配置文件</strong></p> </li> 
</ul> 
<p>现在，用户可以按住 Shift 键并单击下拉菜单中的配置文件，在新窗口中打开该配置文件。</p> 
<p><img alt height="430" src="https://oscimg.oschina.net/oscnet/up-31bd5da801649c4946cafce821e8d922bd7.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>Unfocused appearance settings</strong></li> 
</ul> 
<p>用户可以将"unfocusedAppearance"对象添加到其配置文件的 JSON 对象中，并在其中指定外观设置。这些外观设置将在该配置文件打开且 unfocused 时启用。关于如何配置此设置的更多信息可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fwindows%2Fterminal%2Fcustomize-settings%2Fprofile-appearance%23unfocused-appearance-settings" target="_blank">文档网站</a>上找到。</p> 
<pre><code>// Sets the profile's background image opacity to 0.3 when it is unfocused
"unfocusedAppearance": 
&#123;
    "backgroundImageOpacity": 0.3
&#125;,</code></pre> 
<p><img alt height="465" src="https://oscimg.oschina.net/oscnet/up-d83e9663067fe796c6c1f17e75735e57224.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>Window naming</strong>：新增了终端窗口命名功能。</li> 
 <li> <p><strong>Settings UI 更新</strong></p> 
  <ul> 
   <li> <p>Font face dropdown：现在，用户可以使用下拉菜单而不是输入字体名称来选择字体样式。此下拉菜单还具有用于 monospaced 字体和 non-monospaced 字体的过滤器。</p> <p><img alt height="154" src="https://oscimg.oschina.net/oscnet/up-dbcb6a3e5d3cc647f279cc177c3491adb31.png" width="412" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>删除 base layer：由于与 JSON 片段扩展产生的一些架构冲突，开发团队决定从 settings UI 中移除 base layer 页面。其目前正在计划其他的方式来使用 settings UI 一次性编辑所有的配置文件。用户仍然可以使用 settings.json 文件内的"defaults"部分作为变通方法。</p> </li> 
  </ul> </li> 
</ul> 
<p>除了这些更新亮点，新版本还包含其他改进和 Bugfix，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-8-release%2F" target="_blank">详细更新内容查看官方发布公告</a>。</p>
                                        </div>
                                      
</div>
            