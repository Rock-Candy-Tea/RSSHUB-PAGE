
---
title: 'TypeScript 4.4 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cff64e4c82e7de0581acd55ff5cb9ea81ec.png'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 23:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cff64e4c82e7de0581acd55ff5cb9ea81ec.png'
---

<div>   
<div class="content">
                                                                                            <p>TypeScript 4.4 已正式发布，开发者可通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FMicrosoft.TypeScript.MSBuild" target="_blank">NuGet</a> 或以下 npm 命令进行获取：</p> 
<pre><code>npm install typescript</code></pre> 
<p>部分更新亮点：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23cfa-aliased-conditions" target="_blank">提供针对 Aliased Conditions 的控制流分析 (Control Flow Analysis)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23symbol-template-signatures" target="_blank">增加 symbol 类型和模板字符串模式的索引签名</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23use-unknown-catch-variables" target="_blank">在 Catch 中的变量默认为<code>unknown</code> (<code>--useUnknownInCatchVariables</code>)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-beta%2F%23exact-optional-property-types" target="_blank">新增 Exact Optional Property 类型</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23exact-optional-property-types" target="_blank"> (<code>--exactOptionalPropertyTypes</code>)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23static-blocks" target="_blank">Class <code>static</code> Blocks</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23tsc-help" target="_blank">针对<code>tsc --help</code>的升级和改进</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23perf-improvements" target="_blank">优化性能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23spelling-corrections-js" target="_blank">针对 JavaScript 的拼写检查</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23inlay-hints" target="_blank">Inlay Hints</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23breaking-changes" target="_blank">破坏性变化</a></li> 
</ul> 
<h3>提供针对 Aliased Conditions 的控制流分析 (Control Flow Analysis)</h3> 
<p>例子，Before typescript 4.4</p> 
<pre><code class="language-javascript">function foo(arg: unknown) &#123;
  if (typeof arg === 'string') &#123;
    // We know this is a string now.
    console.log(arg.toUpperCase())
  &#125;
&#125;
function foo(arg: unknown) &#123;
  const argIsString = typeof arg === 'string'
  if (argIsString) &#123;
    console.log(arg.toUpperCase())
    //              ~~~~~~~~~~~
    // Error! Property 'toUpperCase' does not exist on type 'unknown'.
  &#125;
&#125;</code></pre> 
<p>In TypeScript 4.4</p> 
<pre><code class="language-javascript">function foo(arg: unknown) &#123;
  const argIsString = typeof arg === 'string'
  if (argIsString) &#123;
    console.log(arg.toUpperCase())
    // works just fine
  &#125;
&#125;</code></pre> 
<p>可以看到，在 TypeScript 4.4 中增加了 typeof 检查，并保留了不同类型的类型保护条件。</p> 
<h3>增加 symbol 类型和模板字符串模式的索引签名</h3> 
<p>Before typescript 4.4</p> 
<pre><code class="language-javascript">interface Foo &#123;
  name: string
  [index: number]: unknown
  // ...
&#125;
interface Bar &#123;
  [index: string]: unknown
  // ...
&#125;
// 只支持 string 和 number</code></pre> 
<p><strong>In TypeScript 4.4</strong></p> 
<p>现在支持索引签名类型有</p> 
<ul> 
 <li><code>string</code></li> 
 <li><code>number</code></li> 
 <li><code>symbol</code></li> 
 <li>template string patterns (e.g. <code>hello-$&#123;string&#125;</code> )</li> 
</ul> 
<pre><code class="language-javascript">interface Foo &#123;
  [index: number]: number;
  [k: `hello-$&#123;string&#125;`]: unknown;
  // ...
&#125;
const a: Foo = &#123;
  32: 233,
  'hello-name': 'xxx'
  // correct
  helloname: 0,
  // error!
&#125;</code></pre> 
<h3>在 Catch 中的变量默认为 <code>unknown</code></h3> 
<p>从 TypeScript 4.0 开始就可以给 catch 中变量显式声明类型，通常声明为<code>unknown</code>是最好的做法。现在 TypeScript 4.4 默认设置为 unkown。</p> 
<pre><code class="language-javascript">try &#123;
    executeSomeThirdPartyCode();
&#125;
catch (err) &#123; // err: unknown

    // Error! Property 'message' does not exist on type 'unknown'.
    console.error(err.message);

    // Works! We can narrow 'err' from 'unknown' to 'Error'.
    if (err instanceof Error) &#123;
        console.error(err.message);
    &#125;
&#125;</code></pre> 
<p>如需开启此特性，打开 TypeScript 的 strict 模式。</p> 
<h3>新增 Exact Optional Property 类型</h3> 
<p>Before typescript 4.4</p> 
<pre><code class="language-javascript">interface Person &#123;
  name: string
  age?: number
&#125;
// 等价于
interface Person &#123;
  name: string
  age?: number | undefined
&#125;
const p: Person = &#123;
  name: 'Daniel',
  age: undefined, // This is okay by default.
&#125;</code></pre> 
<p>默认情况下，TypeScript不区分值为 undefined 的存在属性和缺失属性。 虽然这在大多数情况下都有效，但并非所有 JavaScript 代码都做出相同的假设。 <code>Object.assign</code> 、 <code>Object.keys</code> 、对象展开 <code>(&#123; ...obj &#125;)</code> 和 for-in 循环等函数和运算符的行为取决于对象上是否实际存在属性。 </p> 
<p><strong>In TypeScript 4.4</strong> </p> 
<p>在 TypeScript 4.4 中，新标志<code>--exactOptionalPropertyTypes</code>指定可选属性类型应完全按照书面解释，这意味着<code>| undefined</code>不会被添加到类型中：</p> 
<pre><code class="language-javascript">// With 'exactOptionalPropertyTypes' on:
const p: Person = &#123;
    name: "Daniel",
    age: undefined, // Error! undefined isn't a number
&#125;;</code></pre> 
<h3>实验性的 Inlay 提示</h3> 
<p>TypeScript 正在测试编辑器对 inlay 文本的支持，这有助于在代码中内联显示有用的信息，例如参数名称。可以将其视为一种友好的“幽灵文本 (ghost text)”。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cff64e4c82e7de0581acd55ff5cb9ea81ec.png" referrerpolicy="no-referrer"></p> 
<h3>添加针对 JavaScript 的拼写建议</h3> 
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
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            