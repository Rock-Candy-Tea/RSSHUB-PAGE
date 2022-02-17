
---
title: 'TypeScript 4.6 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4487'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4487'
---

<div>   
<div class="content">
                                                                                            <p>TypeScript 4.6 首个 RC 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F" target="_blank">已发布</a>。</p> 
<p><strong>新特性概览</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">支持在</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank"><code><span>super</span><span>()</span></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">前执行构造函数代码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23cfa-destructured-discriminated-unions" target="_blank">面向 Destructured Discriminated Unions（可辨识联合类型）提供控制流分析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23improved-depth-checks" target="_blank">优化递归深度检查 (Recursion Depth Checks)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23indexed-access-inference-improvements" target="_blank">优化索引访问类型 (Indexed Access Inference) 的推导</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23dependent-parameters-cfa" target="_blank">面向 Dependent Parameters（依赖参数类型）提供控制流分析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23target-es2022" target="_blank"><code><span>--</span><span>target es2022</span></code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23syntax-errors-js" target="_blank">对 JavaScript 文件引入更多语法检查</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23typescript-trace-analyzer" target="_blank">引入新的性能分析工具：TypeScript Trace Analyzer</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23breaking-changes" target="_blank">破坏性变更</a></li> 
</ul> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">支持在</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank"><code><span>super</span><span>()</span></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">前执行构造函数代码</a></strong></p> 
<p>此特性允许在 super 调用前去执行没有引用 this 的代码，这是由于 JavaScript 的限制，super 前不能调用 this，TypeScript 之前出于实现的原因，规定不能执行所有代码。</p> 
<p><strong>示例</strong></p> 
<pre><code class="language-javascript">class Base &#123;
    // ...
&#125;

class Derived extends Base &#123;
    someProperty = true;

    constructor() &#123;
        // error!
        // have to call 'super()' first because it needs to initialize 'someProperty'.
        doSomeStuff();
        super();
    &#125;
&#125;</code></pre> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23typescript-trace-analyzer" target="_blank">新的性能分析工具：TypeScript Trace Analyzer</a></strong></p> 
<p>TypeScript 提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fwiki%2FPerformance%23performance-tracing" target="_blank"><code><span>--</span><span>generateTrace</span></code>flag</a><span style="background-color:#ffffff; color:#333333"> 来生成编译器在本次编译工作中的耗时占比，或者用于诊断 TypeScript 编译器的问题。虽然</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fwiki%2FPerformance%23performance-tracing" target="_blank"><code><span>--</span><span>generateTrace</span></code></a><span style="background-color:#ffffff; color:#333333">生成了有价值的信息，但在现有的跟踪可视化工具中阅读效果不好。</span></p> 
<p>最近发布的 TypeScript Trace Analyzer 可更直观、更清晰地展示报告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Ftypescript-analyze-trace" target="_blank">详情点此查看</a>。</p> 
<p style="text-align:left"><strong><code><span>--</span><span>target es2022</span></code></strong></p> 
<p style="color:#333333; text-align:left">TypeScript 的<code><span>--</span><span>target</span></code> 选项已支持<code><span>es2022</span></code>。</p> 
<p style="color:#333333; text-align:left">这意味着像类字段 (class fields) 这样的特性现在会有一个可以保留的稳定输出 target，亦意味着可使用新的内置功能如 ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fat" target="_blank"><code><span>at</span><span>()</span></code> method on <code><span>Array</span></code>s</a><span style="background-color:#ffffff; color:#333333">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FhasOwn" target="_blank"><code><span>Object</span><span>.</span><span>hasOwn</span></code></a> 和<span style="background-color:#ffffff; color:#333333"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FError%23rethrowing_an_error_with_a_cause" target="_blank">the <code><span>cause</span></code> option on <code><span>new</span><span><span> </span></span><span>Error</span></code></a>。</p> 
<p style="color:#333333; text-align:left"><em>延伸阅读：<a href="https://www.oschina.net/news/178445/es2022-preview" target="_blank">ECMAScript 2022 预览</a></em></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23syntax-errors-js" target="_blank">对 JavaScript 文件引入更多语法检查</a></strong></p> 
<p>这是 4.6 版本的主要特性，在 TypeScript 中引入的 JavaScript 文件，现在会提示其语法错误，如重复声明、对 export 声明使用了修饰符、在 switch case 语句出现多次的 default case 等。<span style="background-color:#ffffff; color:#121212">类似于 TypeScript 文件，可通过</span><code>@ts-nocheck</code><span style="background-color:#ffffff; color:#121212">来禁用对此文件的类型检查。</span></p> 
<p>示例</p> 
<pre><code class="language-javascript">const foo = 1234;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.

// ...

const foo = 5678;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.</code></pre> 
<pre><code class="language-javascript">function container() &#123;
    export function foo() &#123;
//  ~~~~~~
// error: Modifiers cannot appear here.

    &#125;
&#125;</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            