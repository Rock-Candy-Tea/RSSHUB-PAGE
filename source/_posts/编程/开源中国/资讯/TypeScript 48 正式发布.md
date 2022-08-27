
---
title: 'TypeScript 4.8 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8792'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8792'
---

<div>   
<div class="content">
                                                                                            <p>TypeScript 4.8 已正式发布。</p> 
<p><strong>自 Beta 和 RC 发布以来的变化</strong></p> 
<p>自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-beta%2F" target="_blank">Beta 测试版</a>发布以来，稳定版现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23exclude-globs-auto-import" target="_blank">支持从自动导入中排除特定文件</a>。测试版的公告没有提到围绕类型签名中未使用的解构别名 (destructuring aliases) 的破坏性变化。此外，Beta 和 RC 发布公告都没有介绍关于在 TypeScript 语法树装饰器的 API 破坏性变化。这些内容在新版发布公告中进行了详细说明。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23smarter-type-narrowing-and-simplifications" target="_blank">改进交叉类型、联合类型兼容性，以及类型收窄功能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23infer-types-template-strings" target="_blank">改进对<code><span>infer</span></code><span> 模板字符串类型中的类型推导</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23build-watch-incremental-improvements" target="_blank">优化<code><span>--</span><span>build</span></code>,<span> </span><code><span>--</span><span>watch</span></code>和<code><span>--</span><span>incremental</span></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23build-watch-incremental-improvements" target="_blank">性能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23object-array-comparison-errors" target="_blank">优化比较对象和数组字面量时的错误提示</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23inference-binding-patterns" target="_blank">改进绑定类型中的类型推导</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23file-watching-fixes" target="_blank">修复文件监视功能（尤其是跨<code><span>git checkout</span></code>的场景）</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23find-all-refs-improvements" target="_blank">增强 Find-All-References 性能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23exclude-globs-auto-import" target="_blank">从自动导入中排除特定文件</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F%23correctness-changes" target="_blank">正确性修复和兼容性变化</a></li> 
</ul> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>交叉类型与联合类型的类型收窄增强</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TypeScript 4.8 版本对<span> </span><code>--strictNullChecks</code><span> </span>进行了进一步增强，主要体现在联合类型与交叉类型，以及类型收窄地表现上。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">举例来说，作为 TypeScript 类型系统中的 Top Type ，unknown 类型包含所有的其他类型，实际上 unknown 和<span> </span><code>&#123;&#125; | null | undefined</code><span> </span>的效果是一致的：独特意义的 null、undefined 类型，加上万物起源的<span> </span><code>&#123;&#125;</code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>模板字符串类型中的 infer 提取</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在 4.7 版本中 TypeScript 支持了 infer extends 语法，使得我们可以直接一步就 infer 到预期类型的值，而不需要再次进行条件语句判断：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#d73a49">type</span> FirstString<T> =
    T <span style="color:#d73a49">extends</span> [infer S, ...unknown[]]
        ? S <span style="color:#d73a49">extends</span> <span>string</span> ? S : never
        : never;
​
<span style="color:#6a737d">// 基于 infer extends</span>
<span style="color:#d73a49">type</span> FirstString<T> =
    T <span style="color:#d73a49">extends</span> [infer S <span style="color:#d73a49">extends</span> <span>string</span>, ...unknown[]]
        ? S
        : never;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4.8 版本在此基础上进行了进一步地增强，当 infer 被约束为一个原始类型，那么它现在会尽可能将 infer 的类型信息推导到字面量类型的级别：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#6a737d">// 此前为 number，现在为 '100'</span>
<span style="color:#d73a49">type</span> SomeNum = <span style="color:#032f62">"100"</span> <span style="color:#d73a49">extends</span> <span style="color:#032f62">`<span>$&#123;infer U <span style="color:#d73a49">extends</span> <span>number</span>&#125;</span>`</span> ? U : never;
​
<span style="color:#6a737d">// 此前为 boolean，现在为 'true'</span>
<span style="color:#d73a49">type</span> SomeBool = <span style="color:#032f62">"true"</span> <span style="color:#d73a49">extends</span> <span style="color:#032f62">`<span>$&#123;infer U <span style="color:#d73a49">extends</span> <span>boolean</span>&#125;</span>`</span> ? U : never;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">同时，TypeScript 会检查提取出的值能否重新映射回初始的字符串，如 SomeNum 中会检查<span> </span><code>String(Number("100"))</code><span> </span>是否等于<span> </span><code>"100"</code>，在下面这个例子中就是因为无法重新映射回去，而导致只能推导到 number 类型：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#6a737d">// String(Number("1.0")) → "1"，≠ "1.0"</span>
<span style="color:#d73a49">type</span> JustNumber = <span style="color:#032f62">"1.0"</span> <span style="color:#d73a49">extends</span> <span style="color:#032f62">`<span>$&#123;infer T <span style="color:#d73a49">extends</span> <span>number</span>&#125;</span>`</span> ? T : never; 
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>绑定类型中的类型推导</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">TypeScript 中的泛型填充也会受到其调用方的影响，如以下示例：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#d73a49">declare</span> <span><span style="color:#d73a49">function</span> <span style="color:#6f42c1">chooseRandomly</span><<span style="color:#6f42c1">T</span>><span>(x: T,)</span>: <span style="color:#6f42c1">T</span></span>;
​
<span style="color:#d73a49">const</span> res1 = chooseRandomly([<span style="color:#032f62">"linbudu"</span>, <span>599</span>, <span style="color:#d73a49">false</span>]);
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此时 res1 的类型与函数的泛型 T 会被推导为<span> </span><code>Array<string | number | boolean></code>，但如果我们换一个方法：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#d73a49">declare</span> <span><span style="color:#d73a49">function</span> <span style="color:#6f42c1">chooseRandomly</span><<span style="color:#6f42c1">T</span>><span>(x: T,)</span>: <span style="color:#6f42c1">T</span></span>;
​
<span style="color:#d73a49">const</span> [a, b, c] = chooseRandomly([<span style="color:#032f62">"linbudu"</span>, <span>599</span>, <span style="color:#d73a49">false</span>]);
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此时 a、b、c 被推导为了 string、number、boolean 类型，也就是说此时函数的泛型被填充为<span> </span><code>[string, number, boolean]</code><span> </span>这么个元组类型。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这一泛型填充方式被称为绑定模式（Binding Pattern），而在 4.8 版本中，禁用了基于绑定模式的类型推导，因为其对泛型的影响并不始终正确：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-text"><span style="color:#d73a49">declare</span> <span><span style="color:#d73a49">function</span> <span style="color:#6f42c1">f</span><<span style="color:#6f42c1">T</span>><span>(x?: T)</span>: <span style="color:#6f42c1">T</span></span>;
​
<span style="color:#d73a49">const</span> [x, y, z] = f();</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            