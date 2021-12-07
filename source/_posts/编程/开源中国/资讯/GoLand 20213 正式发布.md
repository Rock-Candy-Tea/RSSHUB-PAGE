
---
title: 'GoLand 2021.3 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ecf7da634f0b01825e6ecee65a739daa63e.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 07:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ecf7da634f0b01825e6ecee65a739daa63e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GoLand 正式发布了今年的第三个大版本更新 —— <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2021%2F12%2F02%2Fmeet-goland-2021-3%2F" target="_blank">2021.3</a>。此版本的主要变化包括：原生支持 WSL 中的 Go 项目、Inline Function（内联函数）重构，并支持处于测试模式的远程开发。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ecf7da634f0b01825e6ecee65a739daa63e.png" referrerpolicy="no-referrer"></p> 
<p style="color:var(--rs-typography-color-average,rgba(25,25,28,0.7)); margin-left:0px; margin-right:0px; text-align:start">从这个版本开始，保存时<span> </span><code>gofmt</code><span> </span>默认启用。 GoLand 2021.3<span> </span>对调试器进行了一些改进，例如 ARM64 的<span> </span><em>Delve</em>、<em>Show Types</em>（显示类型）选项等。</p> 
<p style="color:var(--rs-typography-color-average,rgba(25,25,28,0.7)); margin-left:0px; margin-right:0px; text-align:start">GoLand 新增了两个用于将字符串转换为数字的后缀，一个用于带有<span> </span><code>testify</code><span> </span>断言的表测试的新模板，以及对结构标记中值的更好补全。</p> 
<p style="color:var(--rs-typography-color-average,rgba(25,25,28,0.7)); margin-left:0px; margin-right:0px; text-align:start">像往常一样，新的 GoLand 版本带来了 Web 开发增强和用于处理数据库的多项新功能。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">WSL 支持</h2> 
<p style="color:rgba(25, 25, 28, 0.7); margin-left:0; margin-right:0; text-align:start">添加了在 WSL 中打开项目和指定其中 SDK 的功能。</p> 
<p style="color:rgba(25, 25, 28, 0.7); margin-left:0px; margin-right:0px; text-align:start">如果在 WSL 中创建了一个新项目（或打开了一个现有项目），GoLand 会告知您必须在 WSL 中为此项目使用 Go SDK。 您可以下载 Go SDK 或在<span> </span><code>\\wsl$</code><span> </span>子目录中选择现有 SDK。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1207/073615_BJPB_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">重构</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Inline Function（内联函数）和<span> </span>Inline Method（内联方法）</strong></p> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0">函数和方法的<span> </span><em>Inline</em>（内联）重构现已可用。 要开始尝试，首先将文本光标置于函数、方法或调用上，然后按<span> </span>Ctrl + Alt + N。</p> 
 <p style="margin-left:0px; margin-right:0px">调用<span> </span><em>Inline</em>（内联）重构时，会打开一个带有多个选项的弹出窗口。 在此弹出窗口中，您还可以打开<span> </span><em>Refactoring Preview</em>（重构预览），它能够帮助您找到方法或函数的所有调用。</p> 
 <p style="margin-left:0px; margin-right:0px"><img src="https://static.oschina.net/uploads/space/2021/1207/073706_l75T_2720166.gif" referrerpolicy="no-referrer"></p> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">补全</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>更好地处理结构标记中的值样式</strong></p> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0">新版本改进了在结构字段中添加标记时<span> </span><em>camelCase</em>、<em>snake_case</em><span> </span>等不同类型复合词的处理方式。</p> 
 <p style="margin-left:0px; margin-right:0px">填写标记时，GoLand 会建议一个包含多个选项的列表。 选择一个选项后，IDE 会记住您的选择，并首先在列表中为此结构中的其他字段建议相同的样式。</p> 
</div> 
<p><img src="https://static.oschina.net/uploads/space/2021/1207/073735_sV30_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">UI 改进</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><em>Variables</em>（变量）选项卡的<span> </span><em>Evaluate expression</em>（评估表达式）栏</strong></p> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0"><em>Debug</em>（调试）工具窗口的<span> </span><em>Variables</em>（变量）选项卡现已提供<span> </span><em>Evaluate expression</em>（评估表达式）功能。</p> 
</div> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>拆分<span> </span>Run（运行）工具窗口中的选项卡</strong></p> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0">现在，将选项卡拖放到高亮显示区域即可拆分<span> </span><em>Run</em>（运行）工具窗口。 要取消拆分窗口，请右键点击顶部窗格并从上下文菜单中选择<span> </span><em>Unsplit</em>（取消拆分）。</p> 
</div> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>新的<span> </span><em>Bookmarks</em>（书签）窗口</strong></p> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0">我们有了新的<span> </span><em>Bookmarks</em>（书签）工具窗口。 从现在开始，您使用<span> </span>F11<span> </span>标记为重要的文件和文件夹都将位于此窗口中。</p> 
</div> 
<p>更多关于新版本的介绍查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fgo%2Fwhatsnew%2F%23ui-improvements" target="_blank">https://www.jetbrains.com/zh-cn/go/whatsnew/#ui-improvements</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fgo%2Fdownload%2F" target="_blank">https://www.jetbrains.com/go/download/</a></p>
                                        </div>
                                      
</div>
            