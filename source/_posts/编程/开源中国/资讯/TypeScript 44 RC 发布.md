
---
title: 'TypeScript 4.4 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6657758c482b712352f09ee52bfcc13cce1.png'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 23:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6657758c482b712352f09ee52bfcc13cce1.png'
---

<div>   
<div class="content">
                                                                                            <p>TypeScript 4.4 RC 现已发布。官方表示，从现在开始到 TypeScript 4.4 的稳定发布，预计除了关键的 bug 修复外，不会再有更多的变化。</p> 
<p>可通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FMicrosoft.TypeScript.MSBuild" target="_blank">NuGet</a> 或以下 npm 进行获取：</p> 
<pre>npm install typescript@rc</pre> 
<p>下面是 IDE 或编辑器获取 TypeScript 支持的途径：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DTypeScriptTeam.TypeScript-44rc" target="_blank">下载 Visual Studio 2019/2017</a></li> 
 <li>尝试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Finsiders%2F" target="_blank">Visual Studio Code Insiders</a> 或遵循 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2FDocs%2Flanguages%2Ftypescript%23_using-newer-typescript-versions" target="_blank">Visual Studio Code</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript-Sublime-Plugin%2F%23note-using-different-versions-of-typescript" target="_blank">Sublime Text 3 的说明</a>。</li> 
</ul> 
<p>TypeScript 4.4 的一些主要亮点是：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23cfa-aliased-conditions" target="_blank">提供针对 Aliased Conditions 的控制流分析 (Control Flow Analysis)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23symbol-template-signatures" target="_blank">增加 symbol 类型和模板字符串模式的索引签名</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23use-unknown-catch-variables" target="_blank">Catch 变量中默认使用 <code>unknown</code> 类型 (<code>--useUnknownInCatchVariables</code>)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23exact-optional-property-types" target="_blank">新增 Exact Optional Property 类型 (--exactOptionalPropertyTypes)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23static-blocks" target="_blank">Class <code>static</code> Blocks</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23tsc-help" target="_blank">针对 <code>tsc --help</code> 的升级和改进</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23perf-improvements" target="_blank">性能改进</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23spelling-corrections-js" target="_blank">添加针对 JavaScript 的拼写建议</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23inlay-hints" target="_blank">Inlay 提示</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F%23breaking-changes" target="_blank">破坏性变更</a></li> 
</ul> 
<h4>Inlay 提示</h4> 
<p>TypeScript 提供了对 inlay 提示的支持，这有助于在代码中显示有用的信息，如参数名称和返回类型。你可以将其视为一种友好的“幽灵文本 (ghost text)”。</p> 
<p><img alt height="191" src="https://oscimg.oschina.net/oscnet/up-6657758c482b712352f09ee52bfcc13cce1.png" width="500" referrerpolicy="no-referrer"></p> 
<h4>添加针对 JavaScript 的拼写建议</h4> 
<pre><code>export var inModule = 1
inmodule.toFixed() // errors on exports

function f() &#123;
    var locals = 2
    locale.toFixed() // errors on locals
&#125;
var object = &#123;
    spaaace: 3
&#125;
object.spaaaace // error on read
object.spaace = 2 // error on write
object.fresh = 12 // OK, no spelling correction to offer</code></pre> 
<p>关于此功能的详细信息<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fpull%2F44271" target="_blank">查看此 PR</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-rc%2F" target="_blank">点此查看 TypeScript 4.4 RC 发布公告</a>。</p>
                                        </div>
                                      
</div>
            