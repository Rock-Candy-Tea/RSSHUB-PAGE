
---
title: 'TypeScript 4.3 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9949cb6e4e2df415bc5d9e93f7361d4a07b.gif'
author: 开源中国
comments: false
date: Sat, 15 May 2021 00:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9949cb6e4e2df415bc5d9e93f7361d4a07b.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TypeScript 4.3 RC  现已发布。从现在开始到发布 TypeScript 4.3 稳定版，除了关键的 bug 修复外，不会进行任何其他更改。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>支持为读和写属性单独指定类型。不过，读属性的类型必须可分配给写属性的类型。换句话说，getter 的类型必须可以分配给 setter。这确保了某种程度的一致性，因此一个属性总是可以被分配给它自己。</li> 
</ul> 
<pre><code>class Thing &#123;
    #size = 0;

    get size(): number &#123;
        return this.#size;
    &#125;

    set size(value: string | number | boolean) &#123;
        let num = Number(value);

        // Don't allow NaN and stuff.
        if (!Number.isFinite(num)) &#123;
            this.#size = 0;
            return;
        &#125;

        this.#size = num;
    &#125;
&#125;</code></pre> 
<ul> 
 <li>增加了 override 关键字，当一个方法被标记为 override 时，TypeScript 将始终确保基类中存在一个相同名称的方法。同时 提供 --noImplicitOverride 标志，当这个选项被打开时，除非明确地使用 override 关键字，否则覆盖基类中的任何方法都会成为一个错误。</li> 
</ul> 
<pre><code>class SomeComponent &#123;
    setVisible(value: boolean) &#123;
        // ...
    &#125;
    someHelperMethod() &#123;
        // ...
    &#125;
&#125;
class SpecializedComponent extends SomeComponent &#123;
    
    override setVisible(value: boolean) &#123;
        // ...
    &#125;

    override show() &#123;
    //  ~~~~~~~~
    // Error! This method can't be marked with 'override' because it's not declared in 
    //'SomeComponent'.
        // ...
    &#125;

    // Oops! We weren't trying to override here,
    // we just needed to write a local helper method.
    someHelperMethod() &#123;
        // ...
    &#125;

    // ...
&#125;</code></pre> 
<ul> 
 <li>模板字符串类型改进。当 TypeScript 看到一个模板字符串传递给一个需要字面类型的表达式时，它将尝试给这个表达式一个模板类型。另外，TypeScript 现在可以更好地关联，并在不同的模板字符串类型之间进行推断。</li> 
</ul> 
<pre><code>function bar(s: string): `hello $&#123;string&#125;` &#123;
    // Previously an error, now works!
    return `hello $&#123;s&#125;`;
&#125;

declare let s1: `$&#123;number&#125;-$&#123;number&#125;-$&#123;number&#125;`;
declare let s2: `1-2-3`;
declare let s3: `$&#123;number&#125;-2-3`;
declare let s4: `1-$&#123;number&#125;-3`;
declare let s5: `1-2-$&#123;number&#125;`;
declare let s6: `$&#123;number&#125;-2-$&#123;number&#125;`;

// Now *all of these* work!
s1 = s2;
s1 = s3;
s1 = s4;
s1 = s5;
s1 = s6;</code></pre> 
<ul> 
 <li>TypeScript 4.3 扩展了类中哪些元素可以被赋予 #private 名称，以使它们在运行时真正私有。除了属性之外，方法和访问器也可以被赋予私有。</li> 
</ul> 
<pre><code>class Foo &#123;
    #someMethod() &#123;
        //...
    &#125;

    get #someValue() &#123;
        return 100;
    &#125;

    publicMethod() &#123;
        // These work.
        // We can access private-named members inside this class.
        this.#someMethod();
        return this.#someValue;
    &#125;

    static #someMethod() &#123;
        // ...
    &#125;
&#125;

new Foo().#someMethod();
//        ~~~~~~~~~~~
// error!
// Property '#someMethod' is not accessible
// outside class 'Foo' because it has a private identifier.

new Foo().#someValue;
//        ~~~~~~~~~~
// error!
// Property '#someValue' is not accessible
// outside class 'Foo' because it has a private identifier.

Foo.#someMethod();
//  ~~~~~~~~~~~
// error!
// Property '#someMethod' is not accessible
// outside class 'Foo' because it has a private identifier.</code></pre> 
<ul> 
 <li>ConstructorParameters 类型帮助器现在可以在抽象类上工作。</li> 
</ul> 
<pre><code>abstract class C &#123;
    constructor(a: string, b: number) &#123;
        // ...
    &#125;
&#125;

// Has the type '[a: string, b: number]'.
type CParams = ConstructorParameters<typeof C>;</code></pre> 
<ul> 
 <li>泛型的上下文范围缩小。这使得 TypeScript 可以接受更多的模式，有时甚至可以捕捉错误。</li> 
</ul> 
<pre><code>function makeUnique<T>(collection: Set<T> | T[], comparer: (x: T, y: T) => number): Set<T> | T[] &#123;
  // Early bail-out if we have a Set.
  // We assume the elements are already unique.
  if (collection instanceof Set) &#123;
    return collection;
  &#125;

  // Sort the array, then remove consecutive duplicates.
  collection.sort(comparer);
  for (let i = 0; i < collection.length; i++) &#123;
    let j = i;
    while (j < collection.length && comparer(collection[i], collection[j + 1]) === 0) &#123;
      j++;
    &#125;
    collection.splice(i + 1, j - i);
  &#125;
  return collection;
&#125;</code></pre> 
<ul> 
 <li>在 strictNullChecks 下，检查条件中的 Promise 是否为 "truthy" 将触发一个错误。</li> 
</ul> 
<pre><code>async function foo(): Promise<boolean> &#123;
    return false;
&#125;

async function bar(): Promise<string> &#123;
    if (foo()) &#123;
    //  ~~~~~
    // Error!
    // This condition will always return true since
    // this 'Promise<boolean>' appears to always be defined.
    // Did you forget to use 'await'?
        return "true";
    &#125;
    return "false";
&#125;</code></pre> 
<ul> 
 <li>现在，索引签名可以被声明为静态的。同样的规则适用于类的静态索引签名，即每个其他的静态属性都必须与索引签名兼容。</li> 
</ul> 
<pre><code>class Foo &#123;
    static hello = "hello";
    static world = 1234;
    static prop = true;
    //     ~~~~
    // Error! Property 'prop' of type 'boolean'
    // is not assignable to string index type
    // 'string | number | undefined'.

    static [propName: string]: string | number | undefined;
&#125;

// Valid.
Foo["whatever"] = 42;

// Has type 'string | number | undefined'
let x = Foo["something"];</code></pre> 
<ul> 
 <li>作为增量构建的一部分而生成的 .tsbuildinfo 文件大大缩小。</li> 
 <li>TypeScript 4.3还对增量模式和观察模式做了一些改变，使项目的第一次构建与普通的构建一样快。</li> 
 <li>现在，开始写一个没有路径的导入语句时，TypeScript 会提供一个可能的导入列表。当提交完成时，TypeScript 会完成完整的导入语句，包括要写的路径。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9949cb6e4e2df415bc5d9e93f7361d4a07b.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>TypeScript 现在支持@link标签，并会尝试解决它们所链接的声明。这意味着开发者可以将鼠标悬停在 @ 链接标签中的名字上，并获得快速的信息，或者使用 go-to-definition 或 find-all-references 等命令。</li> 
</ul> 
<pre><code>/**
 * This function depends on &#123;@link bar&#125;
 */
function foo() &#123;

&#125;

function bar() &#123;

&#125;</code></pre> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-3-rc%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            