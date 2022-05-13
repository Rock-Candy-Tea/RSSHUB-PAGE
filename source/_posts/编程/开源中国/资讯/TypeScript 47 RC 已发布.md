
---
title: 'TypeScript 4.7 RC 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0513/072626_3yJj_5430600.gif'
author: 开源中国
comments: false
date: Fri, 13 May 2022 07:31:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0513/072626_3yJj_5430600.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TypeScript 4.7 首个 RC 版本已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F" target="_blank">发布</a>。该版本主要新功能如下：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23esm-nodejs" target="_blank">Node.js 中的 ECMAScript 模块支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23control-over-module-detection" target="_blank">模块检测控制</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23control-flow-analysis-for-computed-properties" target="_blank">计算属性的控制流分析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23improved-function-inference-in-objects-and-methods" target="_blank">改进的对象和方法中的函数推理</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23instantiation-expressions" target="_blank">实例化表达式</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23extends-constraints-on-infer-type-variables" target="_blank"><code>extendsinfer</code> 类型变量的约束</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23optional-variance-annotations-for-type-parameters" target="_blank">类型参数的可选方差注释</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23resolution-customization-with-modulesuffixes" target="_blank">分辨率定制与 <code>moduleSuffixes</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23resolution-mode" target="_blank"><code>resolution-mode</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23go-to-source-definition" target="_blank">转到源定义</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23group-aware-organize-imports" target="_blank">Groups-Aware 组织导入</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23object-method-snippet-completions" target="_blank">对象方法片段完成</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23breaking-changes" target="_blank">其他重大变化</a></li> 
</ul> 
<h2>转到源定义（Go to Source Definition）</h2> 
<p>TypeScript 4.7 包含对名为Go To Source Definition的新实验性编辑器命令的支持。它类似于Go To Definition，但从不在声明文件中返回结果。相反，它会尝试找到相应的实现文件（比如 .js 或者 .ts）并在其中找到定义——即使这些文件通常被隐藏。</p> 
<p>当你需要查看从库中导入的函数的实现，而不是文件中的类型声明时，该功能通常会派上用场。</p> 
<p><img alt height="467" src="https://static.oschina.net/uploads/space/2022/0513/072626_3yJj_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>对象方法片段完成（Object Method Snippet Completions）</h2> 
<p>TypeScript 现在为对象方法提供片段完成。当完成对象中的成员时，TypeScript 将为方法的名称提供一个典型的完成条目，并为完整的方法定义提供一个单独的完成条目</p> 
<p><img alt height="305" src="https://static.oschina.net/uploads/space/2022/0513/072653_gjIK_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>更多内容将在稳定版发布后作介绍，关于 TypeScript 4.7 RC 版本的更多内容可请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7-rc%2F%23breaking-changes" target="_blank">官方博客。</a></p>
                                        </div>
                                      
</div>
            