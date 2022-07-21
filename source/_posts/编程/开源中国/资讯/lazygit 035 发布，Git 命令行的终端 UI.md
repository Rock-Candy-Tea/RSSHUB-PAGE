
---
title: 'lazygit 0.35 发布，Git 命令行的终端 UI'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0721/071447_7e5l_5430600.png'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 07:18:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0721/071447_7e5l_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">lazygit 是一个用于 Git 命令行的简单终端 UI，使用 Go 语言编写，用到了 gocui 库，目的是在命令行提供 Git 的图形界面。</span></p> 
<p><span style="color:#333333">目前 </span> lazygit 发布了 0.35 版本，带来如下更改：</p> 
<ul> 
 <li>支持 <span style="background-color:#ffffff; color:#24292f">Nerd 字体</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f"><img alt height="426" src="https://static.oschina.net/uploads/space/2022/0721/071447_7e5l_5430600.png" width="700" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li> <p><span>滚动条！（非交互式但很酷）</span></p> </li> 
 <li> <p><span>现在可以直接编辑 Diff hunks（通过子进程）</span></p> </li> 
 <li> <p><span>可以打开 lazygit 到关心的面板，例如运行<code>lazygit log</code>打开 lazygit 提交面板。</span></p> </li> 
 <li> <p><span>大多数菜单现在对每个菜单项都有自己的键绑定，这对于高级用户来说应该会加快速度。</span></p> </li> 
 <li> <p><span>现在可以轻松设置/取消设置分支的上游</span></p> </li> 
 <li> <p><span>现在可以选择仅存储未暂存/暂存文件</span></p> </li> 
 <li> <p><span>改进的更新流程</span></p> </li> 
 <li> <p><span>修复了在解析提交消息时重复换行符检索提交消息时，不重复换行符的问题</span></p> </li> 
 <li> <p><span>鉴于很容易意外按错键，一些难以逆转的操作现在具有确认弹出窗口。</span></p> </li> 
 <li> <p><span>'Gone' 分支现在被标记为这样</span></p> </li> 
 <li> <p><span>可以使用 'y' 键复制更多提交属性</span></p> </li> 
 <li> <p><span>现在可以使用常规名称（例如“红色”），而不是仅使用十六进制代码指定自定义提交作者颜色。</span></p> </li> 
 <li> <p><span>提交作者现在可以设置为其他作者或重置为当前 git 用户</span></p> </li> 
 <li> <p><span>可以使用<code>git.autoRefresh</code>配置选项禁用文件的自动刷新</span></p> </li> 
 <li> <p><span>现在可以从合并冲突面板打开文件</span></p> </li> 
 <li> <p><span>现在可以通过<code>gui.timeFormat</code>配置键自定义提交时间格式</span></p> </li> 
 <li> <p><span>在 switch 上记录当前目录而不是 exit</span></p> </li> 
 <li> <p><span>支持 Bitbucket 服务器 PR</span></p> </li> 
 <li> <p><span><code>gui.showBottomLine: false</code>可以在配置中隐藏底线（包含一些键绑定帮助） 。</span></p> </li> 
 <li> <p><span>现在可以默认通过 <code>git.log.showWholeGitGraph: true</code></span>在提交面板中显示整个 git 图</p> </li> 
 <li> <p><span>一些 UI 调整。</span></p> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjesseduffield%2Flazygit%2Freleases%2Ftag%2Fv0.35" target="_blank">https://github.com/jesseduffield/lazygit/releases/tag/v0.35</a></p>
                                        </div>
                                      
</div>
            