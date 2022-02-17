
---
title: 'Visual Studio 2022 17.2 预览版 1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://attachments.tower.im/tower/816aabed57ba88818546d45bfeb74ea7?version=auto'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 00:10:00 GMT
thumbnail: 'https://attachments.tower.im/tower/816aabed57ba88818546d45bfeb74ea7?version=auto'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">伴随着 <a href="https://www.oschina.net/news/182797/visual-studio-2022-17-1-released">Visual Studio 2022 17.1 正式版发布</a>，17.2 第一个预览版也已发布，咱们先初步介绍一下 17.2 的新内容概要，详细内容还得看正式版：</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start"><strong>Web 工具</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>连接的服务中的 "添加依赖关系" 对话框现在具有搜索功能。</li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start"><strong>Git 工具</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fline-staging-blog" target="_blank">支持行过渡，一种交互式过渡，</a><span> </span>能够直接从编辑器和差异视图暂存特定的行和/或代码块。</li> 
 <li>Azure DevOps 连接检测功能增强，使<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2Fplease-dont-remove-the-legacy-work-item-experience%2F818686" target="_blank">相关工作项</a>更易于提交。</li> 
 <li>Visual Studio 在  Windows 上使用 64 位 Git 。</li> 
</ul> 
<h2><strong>.NET 效率</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">编译器中的新更改不允许在结构内部使用无参数构造函数。 我们添加了一个新的代码修复程序，它将自动修复此问题。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 .NET 7.0 中添加了一个名为<span> </span><code>StringSyntaxAttribute</code><span> </span>的新属性，该属性使用户能指定字符串表示的数据类型，例如 JSON、Regex 或 DateTime， Visual Studio 将根据字符串表示的数据类型进行对应的语法突出显示。</li> 
 <li>双击内联参数或类型提示，可立即插入参数或类型名称。</li> 
 <li>添加了一个新的重构，用于删除不必要的 lambda 表达式并直接调用方法组。 将光标置于不必要的 lambda 上， 按 Ctrl +<span> </span><code>.</code><span> </span>(句号)，触发“快速操作和重构”菜单， 选择 "删除不必要的 lambda 表达式"。</li> 
 <li>在 c # 11 中添加了转化为<span> </span><strong>原始字符串文本</strong>（raw string） 的新语言功能，可将普通或逐字（normal or verbatim）字符串文本转换为原始字符串文本。 若要使用原始字符串文本，请将项目文件中的语言版本设置为 "预览"：<span> </span><code><LangVersion>preview</LangVersion></code><span> </span>，然后将光标置于正常或逐字的字符串上按 Ctrl +<span> </span><code>.</code><span> </span>(句号)，触发“快速操作和重构”菜单， 选择 "转换为原始字符串"。<span><img alt="转换为原始字符串" src="https://attachments.tower.im/tower/816aabed57ba88818546d45bfeb74ea7?version=auto" referrerpolicy="no-referrer"></span></li> 
</ul> 
<h2 style="color:#000000; margin-left:0px; margin-right:0px; text-align:start"><strong>Razor (ASP.NET Core) 编辑器</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的 Razor 编辑器支持代码段。</li> 
 <li>新的 Razor 编辑器支持 "包装 div" ，快捷方式 Shift + Alt + W。</li> 
</ul> 
<h2 style="color:#000000; margin-left:0px; margin-right:0px; text-align:start"><strong>调试和诊断</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了对依赖跟踪点的支持。</li> 
 <li>现在可以设置依赖于跟踪点和 viseversa 的任何断点。</li> 
 <li>如果在跟踪点上 depedent 断点，则只会在命中跟踪点后命中。 (在输出窗口中打印跟踪/日志消息后)</li> 
</ul> 
<p>发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes-preview" target="_blank">https://docs.microsoft.com/en-us/visualstudio/releases/2022/release-notes-preview</a></p>
                                        </div>
                                      
</div>
            