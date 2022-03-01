
---
title: 'TypeScript 4.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5348'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 08:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5348'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TypeScript 4.6 现已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F" target="_blank">发布。</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>新特性概览</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">支持在</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23code-before-super" target="_blank"><code><span>super</span><span>()</span></code>前执行构造函数代码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23cfa-destructured-discriminated-unions" target="_blank">面向 Destructured Discriminated Unions（可辨识联合类型）提供控制流分析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23improved-depth-checks" target="_blank">优化递归深度检查 (Recursion Depth Checks)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23indexed-access-inference-improvements" target="_blank">优化索引访问类型 (Indexed Access Inference) 的推导</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23dependent-parameters-cfa" target="_blank">面向 Dependent Parameters（依赖参数类型）提供控制流分析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23target-es2022" target="_blank"><code><span>--</span><span>target es2022</span></code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23no-void-0-react-jsx" target="_blank">删除了<code><span>react</span><span>-</span><span>jsx</span></code>中不必要的参数</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23jsdoc-name-suggestions" target="_blank">JSDoc Name Suggestions</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23syntax-errors-js" target="_blank">对 JavaScript 文件引入更多语法检查</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23typescript-trace-analyzer" target="_blank">引入新的性能分析工具：TypeScript Trace Analyzer</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23breaking-changes" target="_blank">破坏性变更</a></li> 
</ul> 
<p><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>自 Beta 版和 RC 版以来有什么新变化？</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </strong></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>beta 版时错过了 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23cfa-destructured-discriminated-unions" target="_blank">面向 Destructured Discriminated Unions（可辨识联合类型）提供控制流分析</a> <span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>和 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23target-es2022" target="_blank"><code><span>--</span><span>target es2022</span></code></a><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>两个特性的添加。自 beta 版以来，另外一个值得注意的变化是，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23no-void-0-react-jsx" target="_blank">删除了<code><span>react</span><span>-</span><span>jsx</span></code>模式中的<code><span>void</span> <span>0</span></code>参数</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>自 RC 以来进行的一项更改是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23jsdoc-name-suggestions" target="_blank">对不匹配的 JSDoc 参数名称的建议</a>。同时</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>还进行了一些内部重构，修复了某些问题，纠正了一些奇怪的错误消息，并在某些情况下将类型检查性能提高了 3%。可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fpull%2F47738" target="_blank">在此处阅读有关该更改的更多信息</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23code-before-super" target="_blank">支持在</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F%23code-before-super" target="_blank"><code><span>super</span><span>()</span></code>前执行构造函数代码</a></strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此特性允许在 super 调用前去执行没有引用 this 的代码，这是由于 JavaScript 的限制，super 前不能调用 this，TypeScript 之前出于实现的原因，规定不能执行所有代码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>示例</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-javascript"><span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">Base</span> </span>&#123;
    <span style="color:#6a737d">// ...</span>
&#125;

<span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">Derived</span> <span style="color:#d73a49">extends</span> <span style="color:#6f42c1">Base</span> </span>&#123;
    someProperty = <span style="color:#005cc5">true</span>;

    <span style="color:#d73a49">constructor</span>() &#123;
        <span style="color:#6a737d">// error!</span>
        <span style="color:#6a737d">// have to call 'super()' first because it needs to initialize 'someProperty'.</span>
        doSomeStuff();
        <span style="color:#d73a49">super</span>();
    &#125;
&#125;</code></pre> 
<ul> 
 <li style="text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23typescript-trace-analyzer" target="_blank">新的性能分析工具：TypeScript Trace Analyzer</a></strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TypeScript 提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fwiki%2FPerformance%23performance-tracing" target="_blank"><code><span>--</span><span>generateTrace</span></code>flag</a><span style="background-color:#ffffff; color:#333333"> 来生成编译器在本次编译工作中的耗时占比，或者用于诊断 TypeScript 编译器的问题。虽然</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fwiki%2FPerformance%23performance-tracing" target="_blank"><code><span>--</span><span>generateTrace</span></code></a><span style="background-color:#ffffff; color:#333333">生成了有价值的信息，但在现有的跟踪可视化工具中阅读效果不好。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最近发布的 TypeScript Trace Analyzer 可更直观、更清晰地展示报告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Ftypescript-analyze-trace" target="_blank">详情点此查看</a>。</p> 
<ul> 
 <li style="text-align:left"><strong><code><span>--</span><span>target es2022</span></code></strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TypeScript 的<code><span>--</span><span>target</span></code> 选项已支持<code><span>es2022</span></code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这意味着像类字段 (class fields) 这样的特性现在会有一个可以保留的稳定输出 target，亦意味着可使用新的内置功能如 ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fat" target="_blank"><code><span>at</span><span>()</span></code> method on <code><span>Array</span></code>s</a><span style="background-color:#ffffff; color:#333333">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FhasOwn" target="_blank"><code><span>Object</span><span>.</span><span>hasOwn</span></code></a> 和<span style="background-color:#ffffff; color:#333333"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FError%23rethrowing_an_error_with_a_cause" target="_blank">the <code><span>cause</span></code> option on <code><span>new</span><span><span> </span></span><span>Error</span></code></a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>延伸阅读：<a href="https://www.oschina.net/news/178445/es2022-preview" target="_blank">ECMAScript 2022 预览</a></em></p> 
<ul> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: left;"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6-rc%2F%23syntax-errors-js" target="_blank">对 JavaScript 文件引入更多语法检查</a></strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这是 4.6 版本的主要特性，在 TypeScript 中引入的 JavaScript 文件，现在会提示其语法错误，如重复声明、对 export 声明使用了修饰符、在 switch case 语句出现多次的 default case 等。<span style="background-color:#ffffff; color:#121212">类似于 TypeScript 文件，可通过</span><code>@ts-nocheck</code><span style="background-color:#ffffff; color:#121212">来禁用对此文件的类型检查。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">示例</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-javascript"><span style="color:#d73a49">const</span> foo = <span>1234</span>;
<span style="color:#6a737d">//    ~~~</span>
<span style="color:#6a737d">// error: Cannot redeclare block-scoped variable 'foo'.</span>

<span style="color:#6a737d">// ...</span>

<span style="color:#d73a49">const</span> foo = <span>5678</span>;
<span style="color:#6a737d">//    ~~~</span>
<span style="color:#6a737d">// error: Cannot redeclare block-scoped variable 'foo'.</span></code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-javascript"><span><span style="color:#d73a49">function</span> <span style="color:#6f42c1">container</span>() </span>&#123;
    <span style="color:#d73a49">export</span> <span><span style="color:#d73a49">function</span> <span style="color:#6f42c1">foo</span>() </span>&#123;
<span style="color:#6a737d">//  ~~~~~~</span>
<span style="color:#6a737d">// error: Modifiers cannot appear here.</span>

    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-6%2F" target="_blank">详情查看发布公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            