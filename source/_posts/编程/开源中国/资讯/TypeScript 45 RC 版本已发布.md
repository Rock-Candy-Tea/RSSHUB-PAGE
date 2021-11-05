
---
title: 'TypeScript 4.5 RC 版本已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1105/071943_4E83_5430600.gif'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 07:23:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1105/071943_4E83_5430600.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TypeScript 4.5 候选版本 (RC) 现已发布，官方表示，从现在开始到 TypeScript 4.5 稳定发布，除了关键的 bug 修复外不会有更多的变化。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本主要更新：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>实验性功能：在夜间版本支持  Node.js 运行 ECMAScript 模块</li> 
 <li>从 node_modules 支持<span> </span><code>lib</code></li> 
 <li>新的<span> </span><code>Awaited</code> 类型和对<span> </span><code>Promise</code><span> </span>对象的优化</li> 
 <li>模板字符串可以用作判断符</li> 
 <li>引入 es2022 模块（可以在异步函数之外使用 await）</li> 
 <li>移除 Conditional Types 的尾部递归</li> 
 <li>禁用省略型 Import ，加入新的 Import 类型修饰符</li> 
 <li>现在可以检查一个对象是否有一个私有字段</li> 
 <li>支持 Import 断言</li> 
 <li>对所有系统的<span> </span><span style="color:#333333">Node.js<span> </span></span>引入<span> </span><code>realpathSync.native</code><span> </span>函数， 减少项目加载时间（Windows 少了 5-13%） 。</li> 
 <li>两个新的代码补全功能：<span style="color:#333333">重写或实现类中的方法的</span>片段补全、JSX 属性的代码补全</li> 
 <li>编辑器对未解析的类型会直接展示原名（之前版本是用<span> </span><code>any</code><span> </span>来代替未解析的类型）。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本的重大特性是支持 Node 12 运行 ECMAScript 模块，不过出于稳定性和用户体验，此功能暂时只在夜间版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fnightly-builds.html" target="_blank">nightly releases）</a>上发布。在语言编辑方面，4.5 引入了更多用于方法实现和重写的代码补全。除此之外，4.5 版本还解决了对 package.json 文件过度 realpath 调用引发的性能回归问题，且此修复被反向移植到 TypeScript 4.4.4 中。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">实验性：在夜间版本支持  Node.js 运行 ECMAScript 模块</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在过去的几年里，Node.js 一直致力于支持运行 ECMAScript 模块 (ESM)。 但是，Node.js 生态的基础建立在 CommonJS (CJS) 模块系统之上，两大模块的差别让 Node.js 的适配变得异常困难。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在，此功能可用了，不过仅在 TypeScript 的夜间版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fnightly-builds.html" target="_blank">nightly releases</a>）中可用 ， TypeScript 4.5 暂不可用。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的代码片段自动补全</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">类中的方法补全</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在在重写或实现类中的方法时提供代码片段补全。在实现接口的方法，或覆盖子类中的方法时，TypeScript 不仅完成方法名称，还完成方法体的完整签名和大括号。完成后，光标将跳转到方法的主体中。</p> 
<p><br> <img alt height="593" src="https://static.oschina.net/uploads/space/2021/1105/071943_4E83_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">JSX 属性的代码补全</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">为 JSX 属性带来了片段补全：在 JSX 标签中写出一个属性时，TypeScript 已经为这些属性提供了建议；通过片段补全，可以通过添加初始化程序，并将光标放在正确的位置来节省时间。<br> <img alt height="263" src="https://static.oschina.net/uploads/space/2021/1105/072022_ifCE_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">需要注意的事项</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><code>lib.d.ts</code> 变更</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TypeScript 4.5 包含对其内置声明文件的更改，这些更改可能会影响您的编译。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><code>Awaited</code><span> </span>改动的影响</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在在<span> </span><code>lib.d.ts</code><span> </span>中使用了await，可能会导致某些泛型类型的变化，这可能会导致不兼容。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">别忘了在<span> </span><code>tsconfig.json</code><span> </span>的检查编译器选项（<code>compilerOptions</code>）。</h4> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">条件类型的可分配性被限制</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TypeScript 不再允许将类型分配给使用<span> </span><code>infer</code><span> </span>或分布式的条件类型，这会导致重大的性能问题。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详细更新内容可查看更新公告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-5-rc%2F%23breaking-changes" target="_blank">原文</a>。</p>
                                        </div>
                                      
</div>
            