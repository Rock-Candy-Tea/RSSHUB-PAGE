
---
title: 'TypeScript 4.8 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1715'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1715'
---

<div>   
<div class="content">
                                                                                            <p>TypeScript 4.8 首个 RC 已发布。开发团队表示，从现在开始到发布 TypeScript 4.8 稳定版本，预计除了修复重要错误之外不会有进一步的变化。</p> 
<p>主要更新内容包括：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23smarter-type-narrowing-and-simplifications" target="_blank">改进交叉类型、联合类型兼容性，以及类型收窄功能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23infer-types-template-strings" target="_blank">改进对<code><span>infer</span></code>模板字符串类型中的类型推理</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23build-watch-incremental-improvements" target="_blank">增强<code><span>--</span><span>build</span></code>,<code>--watch</code><code>--incremental</code>性能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23object-array-comparison-errors" target="_blank">优化比较对象和数组字面量时的错误提示</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23inference-binding-patterns" target="_blank">改进绑定类型中的类型推导</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23file-watching-fixes" target="_blank">修复文件监视功能（尤其是跨<span> </span><code><span>git checkout</span></code>的场景</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23file-watching-fixes" target="_blank">）</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23find-all-refs-improvements" target="_blank">增强 Find-All-References 性能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23exclude-globs-auto-import" target="_blank">从自动导入中排除特定文件</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F%23correctness-changes" target="_blank">正确性修复和兼容性变化</a></li> 
</ul> 
<hr> 
<p><strong>交叉类型与联合类型的类型收窄增强</strong></p> 
<p>TypeScript 4.8 版本对<code>--strictNullChecks</code>进行了进一步增强，主要体现在联合类型与交叉类型，以及类型收窄地表现上。</p> 
<p>举例来说，作为 TypeScript 类型系统中的 Top Type ，unknown 类型包含所有的其他类型，实际上 unknown 和<code>&#123;&#125; | null | undefined</code>的效果是一致的：独特意义的 null、undefined 类型，加上万物起源的<code>&#123;&#125;</code>。</p> 
<p><strong>模板字符串类型中的 infer 提取</strong></p> 
<p>在 4.7 版本中 TypeScript 支持了 infer extends 语法，使得我们可以直接一步就 infer 到预期类型的值，而不需要再次进行条件语句判断：</p> 
<pre><code class="language-text">type FirstString<T> =
    T extends [infer S, ...unknown[]]
        ? S extends string ? S : never
        : never;
​
// 基于 infer extends
type FirstString<T> =
    T extends [infer S extends string, ...unknown[]]
        ? S
        : never;
</code></pre> 
<p>4.8 版本在此基础上进行了进一步地增强，当 infer 被约束为一个原始类型，那么它现在会尽可能将 infer 的类型信息推导到字面量类型的级别：</p> 
<pre><code class="language-text">// 此前为 number，现在为 '100'
type SomeNum = "100" extends `$&#123;infer U extends number&#125;` ? U : never;
​
// 此前为 boolean，现在为 'true'
type SomeBool = "true" extends `$&#123;infer U extends boolean&#125;` ? U : never;
</code></pre> 
<p>同时，TypeScript 会检查提取出的值能否重新映射回初始的字符串，如 SomeNum 中会检查<code>String(Number("100"))</code>是否等于<code>"100"</code>，在下面这个例子中就是因为无法重新映射回去，而导致只能推导到 number 类型：</p> 
<pre><code class="language-text">// String(Number("1.0")) → "1"，≠ "1.0"
type JustNumber = "1.0" extends `$&#123;infer T extends number&#125;` ? T : never; 
</code></pre> 
<p><strong>绑定类型中的类型推导</strong></p> 
<p>TypeScript 中的泛型填充也会受到其调用方的影响，如以下示例：</p> 
<pre><code class="language-text">declare function chooseRandomly<T>(x: T,): T;
​
const res1 = chooseRandomly(["linbudu", 599, false]);
</code></pre> 
<p>此时 res1 的类型与函数的泛型 T 会被推导为<code>Array<string | number | boolean></code>，但如果我们换一个方法：</p> 
<pre><code class="language-text">declare function chooseRandomly<T>(x: T,): T;
​
const [a, b, c] = chooseRandomly(["linbudu", 599, false]);
</code></pre> 
<p>此时 a、b、c 被推导为了 string、number、boolean 类型，也就是说此时函数的泛型被填充为<code>[string, number, boolean]</code>这么个元组类型。</p> 
<p>这一泛型填充方式被称为绑定模式（Binding Pattern），而在 4.8 版本中，禁用了基于绑定模式的类型推导，因为其对泛型的影响并不始终正确：</p> 
<pre><code class="language-text">declare function f<T>(x?: T): T;
​
const [x, y, z] = f();
</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-8-rc%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            