
---
title: 'IntelliJ IDEA 2021.3.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1805'
author: 开源中国
comments: false
date: Sat, 29 Jan 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1805'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2021.3.2 现已可用，该版本带来了一些小的功能改进和修复：</p> 
<ul> 
 <li>在 macOS上，当 File | New 被调用时，⌘N 会像预期的那样打开 <em>Generate </em>弹出窗口 <span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-286810" target="_blank">IDEA-286810</a><span style="color:#27282c">]</span></li> 
 <li><em>在 支持屏幕阅读器 </em>复选框下，添加了启用此选项时 <em>Ctrl+TAB / Ctrl+Shift+TAB </em>快捷方式行为更改的注释 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-285040" target="_blank">IDEA-285040</a> ]</li> 
 <li>修复了 WSL2 导致 maven 项目无限同步的问题 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-286579" target="_blank">IDEA-286579</a> ]</li> 
 <li>修复了影响 YouTrack 集成的问题，现在 <em>Post to Bugtracker </em>操作正常起作用 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-266608" target="_blank">IDEA-266608</a> ]。</li> 
 <li>修复了导致不必要的索引重新扫描的问题  [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-284043" target="_blank">IDEA-284043</a> ]<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-283690" target="_blank"> </a></li> 
 <li>修复了几个 UI 冻结：[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-285928" target="_blank">IDEA-285928</a> ]、[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-285303" target="_blank">IDEA-285303</a> ]、[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-284083" target="_blank">IDEA-284083</a> ]、[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-284362" target="_blank">IDEA-284362</a> ]、[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-286489" target="_blank">IDEA-286489</a> ]。</li> 
 <li><em>View as binary </em>选项现在可用于调试器中的多个变量 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-285052" target="_blank">IDEA -285052 </a>]</li> 
 <li><em>Git Branches </em>弹出窗口中的数据现在会正确显示 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-286795" target="_blank">IDEA-286795</a> ]；[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-285766" target="_blank">IDEA-285766</a> ]</li> 
 <li>修复了在 Rebase 对话框中， <em>Rebase </em>按钮被禁用<em>的问题 [ </em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-282538" target="_blank">IDEA-282538</a> ]</li> 
 <li>修复了 YAML 文件的问题：[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-247565" target="_blank">IDEA-247565]</a>；[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-264436" target="_blank">IDEA-264436</a> ]</li> 
 <li>修复了 UI 外观问题 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-280937" target="_blank">IDEA-280937</a> ]、[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-284849" target="_blank">IDEA -284849 </a>]</li> 
 <li>IDE 不再建议安装不需要的插件 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-283690" target="_blank">IDEA-283690</a> ]</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F01%2Fintellij-idea-2021-3-2%2F" target="_blank">https://blog.jetbrains.com/idea/2022/01/intellij-idea-2021-3-2/</a></p>
                                        </div>
                                      
</div>
            