
---
title: 'TypeScript 4.3 Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0406/160359_bc1Q_2720166.gif'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 07:08:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0406/160359_bc1Q_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TypeScript 4.3 Beta 已发布。此版本更新亮点包括：支持自动补全 import 语句、改进 Template String Type（模板字符串类型）、<code>@link</code>标签的编辑器支持、引入<code>static</code>索引签名功能等。</p> 
<h2>支持自动补全 import 语句</h2> 
<p>通过利用 auto-imports 功能（原理是提供所有可能的导出，并在文件顶部自动插入导入语句），当开发者输入 import 关键字后即可生成完整的导入语句，其中包括所要编写的路径。</p> 
<p><img height="306" src="https://static.oschina.net/uploads/space/2021/0406/160359_bc1Q_2720166.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>改进 Template String Type</h2> 
<p>Template String Type（模板字符串类型）是最近版本才引入的类型构造，这些类型可以通过级联来构造新的类似字符串的类型：</p> 
<pre>type Color = "red" | "blue";
type Quantity = "one" | "two";

type SeussFish = `$&#123;Quantity | Color&#125; fish`;
// same as
//   type SeussFish = "one fish" | "two fish"
//                  | "red fish" | "blue fish";</pre> 
<p>或匹配其他类似字符串类型的模式：</p> 
<pre>declare let s1: `$&#123;number&#125;-$&#123;number&#125;-$&#123;number&#125;`;
declare let s2: `1-2-3`;

// Works!
s1 = s2;</pre> 
<p>此版本的改进包括：在 TypeScript 推断模板字符串类型的时候，当模板字符串由类似字符串字面量的类型在上下文中类型化时，它将尝试为该表达式指定模板类型。</p> 
<pre>function bar(s: string): `hello $&#123;string&#125;` &#123;
    // Previously an error, now works!
    return `hello $&#123;s&#125;`;
&#125;</pre> 
<p>另一项改进为 TypeScript 现在可以更好地关联不同看的模板字符串类型，并在它们之间进行推断。</p> 
<pre>declare let s: string;
declare function f<T extends string>(x: T): T;

// Previously: string
// Now       : `hello-$&#123;string&#125;`
let x2 = f(`hello $&#123;s&#125;`);</pre> 
<h2><code>@link</code>标签的编辑器支持</h2> 
<p>TypeScript 现在支持解析<code>@link</code>标签链接的声明。</p> 
<pre>/**
 * This function depends on &#123;@link bar&#125;
 */
function foo() &#123;

&#125;

function bar() &#123;

&#125;</pre> 
<h2>引入<code>static</code>索引签名功能</h2> 
<p>索引签名 (Index Signatures) 支持在某个值上设置比类型显式声明更多的属性。</p> 
<pre>class Foo &#123;
    hello = "hello";
    world = 1234;

    // This is an index signature:
    [propName: string]: string | number | undefined;
&#125;

let instance = new Foo();

// Valid assigment
instance["whatever"] = 42;

// Has type 'string | number | undefined'.
let x = instance["something"];</pre> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-3-beta%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            