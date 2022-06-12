
---
title: 'AppCode 2022.2 EAP3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a64a41a3c3220fe3a16f4ed3a2da81c363e.png'
author: 开源中国
comments: false
date: Sun, 12 Jun 2022 07:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a64a41a3c3220fe3a16f4ed3a2da81c363e.png'
---

<div>   
<div class="content">
                                                                                            <p>AppCode 2022.2 EAP3 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fappcode%2F2022%2F06%2Fappcode-2022-2-eap3-concurrency-interoperability-with-objective-c-and-support-for-existential-any%2F" target="_blank">发布</a>，具体更新内容如下：</p> 
<p><strong><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span>与 Objective-C 的并发互操作性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Swift 语言带有一组并发特性，包括异步函数和 actors。Objective-C 语言没有它们，因此异步 API 是通过使用 completion handlers 手动表达的。由于 Swift 和 Objective-C API 之间的紧密集成是 Apple 平台上开发人员体验的重要组成部分，因此 Swift 5.5 增加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0297-concurrency-objc.md" target="_blank">了与 Objective-C 的并发互操作性</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>AppCode 2022.2 现在也支持它，其中包括以下内容：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 Swift 中为 Objective-C 异步函数正确的代码解析。</li> 
 <li>支持 Actor 与 Objective-C 的互操作性。</li> 
 <li>各种 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0297-concurrency-objc.md%23additional-objective-c-attributes" target="_blank">Objective-C 属性</a>，如<code>_Nullable_result</code>,<code>__attribute__((swift_async_error(...)))</code>被正确处理。</li> 
</ul> 
<p><img alt height="233" src="https://oscimg.oschina.net/oscnet/up-a64a41a3c3220fe3a16f4ed3a2da81c363e.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="92" src="https://oscimg.oschina.net/oscnet/up-dfbfb2800629f80ef2d6cde75df840cf230.png" width="500" referrerpolicy="no-referrer"> </p> 
<p><strong>Existential any</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>AppCode 现在支持的另一个新的 Swift 功能是 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0335-existential-any.md" target="_blank">existential<span> </span><code>any</code></a><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>的. IDE 支持的范围包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>正确的代码解析和类型检查。</li> 
 <li>Code completion 和 code generation。</li> 
 <li>对 code formatter 的更改。</li> 
</ul> 
<p><img height="229" src="https://oscimg.oschina.net/oscnet/up-a3eec1ed28acc6a38b1689a7d2dbbc8afec.png" width="500" referrerpolicy="no-referrer"></p> 
<p>完整的发行说明可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FOC-A-223445201%2FAppCode-20222-EAP-3-222296442-build-Release-Notes" target="_blank">在此处</a>获得。</p>
                                        </div>
                                      
</div>
            