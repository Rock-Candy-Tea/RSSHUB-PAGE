
---
title: 'TypeScript 内置工具详谈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1937'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 21:46:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=1937'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>TypeScript 提供了几种实用程序类型来助力常见的类型转换。这些实用程序是全局可用的。</p>
</blockquote>
<p>也就是说全局声明了一些<code>Type</code>, 调用<code>Type</code>就可以方便地进行一些类型转换或者创建新的类型。<br>
不会这些函数一样能写<code>TypeScript</code><strong>你不会真的就不看下文了吧🤣？</strong>, 但是掌握后能让你写<code>TypeScript</code>事半功倍。 且掌握这些内置<code>Type</code>是十分必要的。</p>
<p>本文章主要对一些比较少用或者难理解的类型做了比较详细的说明。比如 <code>ThisType<T></code> 等</p>
<h2 data-id="heading-1"><a id="user-content-#Partial" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">1、Partial 将一个类型的属性全部变为可选</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Partial<T> = &#123;
    [P in keyof T]?: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看出来该<code>Type</code>使用时需要传入一个泛型<code>T</code>。内部遍历<code>T</code>的所有属性然后创建一个新的 <code>Type</code>，新的<code>Type</code>的所有属性使用 <code>?</code> 标识，使之为可选。</p>
<p><code>keyof</code>会遍历一个<code>Interface</code>的所有属性名称(key), 生成一个联合类型 <code>"name" | "age" ...</code>，然后可以得到下面代码</p>
<p><code>P in "name" | "age"</code> 这就很明白能看出来了，表明了<code>P</code>为右侧类型</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">interface UserInfo &#123;
    name:string;
    age:number;
&#125;

// 这里会将 UserInfo 所有的属性变为可选
const foo:Partial<UserInfo> = &#123;
    name:"张三" 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2"><a id="user-content-#Required" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">2、Required 将一个类型的属性全部变为必选</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Required<T> = &#123;
    [P in keyof T]-?: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该<code>Type</code>和<code>Partial</code>刚好是相反的。 从上面的代码中可以看出来该<code>Type</code>实用时需要传入一个泛型<code>T</code>。内部使用<code>-?</code>将<code>T</code>的每个属性去除可选标识使之变成为必填。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">interface UserInfo &#123;
    name?:string;
    age?:number;
&#125;

// 这里会将 UserInfo 所有可选的属性变为必选
const foo:Required<UserInfo> = &#123;
    name:"张三",
    age:18
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><a id="user-content-#Readonly" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">3、Readonly 将一个类型的属性全部变为只读状态</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Readonly<T> = &#123;
    readonly [P in keyof T]: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看出来该<code>Type</code>实用时需要传入一个泛型<code>T</code>。内部使用<code>readonly</code>将<code>T</code>的每个属性去除可选标识使之变成为只读。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">interface UserInfo &#123;
    name?:string;
    age?:number;
&#125;
 
const foo:Readonly<UserInfo> = &#123;
    name:"张三",
    age:18
&#125;
foo.name = '李四';// error: 无法分配到 "name" ，因为它是只读属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><a id="user-content-#Record" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">4、Record 构造一个字面量对象 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Record<K extends keyof any, T> = &#123;
    [P in K]: T;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Record</code> 用于方便地构造一个字面量对象。其作用和 <code>&#123; [propName:string]:any &#125;</code> 有些许类似。</p>
<p><code>Record</code> 只需要传入两个 <code>Type</code> 即可创建一个新的 <code>Type</code>，相比于 <code>&#123; [propName:string]:any &#125;</code> 能方便一些。当然除了方便外功能也比它强大，因为<code>Record</code>第一个参数可接收一组<code>key</code>，这样就可以做到定义出一个完整的 <code>Type</code> 了。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 这是通过 interface 定义出来的。
interface UserInfo &#123;
    name:string;
    age:number;
&#125;

// 我们用 Record 来实现一遍 UserInfo 。
// 注意：后面一个形参和 UserInfo 的是不一样的，因为 Record 第二个参数只能接受一个类型。所以这里要么用 any，要么用这种联合类型。
type UserInfoT = Record<"name" | "age", string | number>

// 结果
// type UserInfoT = &#123;
//     name:string | number;
//     age:string | number;
// &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"><a id="user-content-#Pick" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">5、Pick 从一个 Type 中选取一些属性来构造一个新的对象 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Pick<T, K extends keyof T> = &#123;
    [P in K]: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Pick</code> 也用于方便地构造一个字面量对象。其作用和 <code>Record</code> 有些许类似。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">interface UserInfo &#123;
    name:string;
    age:number;
&#125;

// 这时候我们只需要 UserInfo 的 name 属性。
type UserInfoT = Pick<UserInfo, "name">
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6"><a id="user-content-#Omit" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">6、Omit 从一个对象类型中删除一些属性来构造一个新的对象 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>日常使用中<code>Omit</code> 是一个使用频率可能比较高的。和 <code>Pick</code> 刚刚相反，用于排除不需要的属性。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">interface UserInfo &#123;
    name:string;
    age:number;
&#125;

// 这时候我们不需要 UserInfo 的 name 属性。
type UserInfoT = Omit<UserInfo, "name">
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7"><a id="user-content-#Exclude" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">7、Exclude 排除一个联合类型中的某一些类型来构造一个新 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Exclude<T, U> = T extends U ? never : T;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面说的 <code>Omit</code> 和 <code>Pick</code> 都是对一个字面量对象 <code>Type</code> 的操作。如果要对一个联合类型操作的话需要用到 <code>Exclude</code> 和 <code>Extract</code></p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 排除掉 "name"
type UserInfoT = Exclude<"name" | "age", "name">;

// 等价于
type UserInfoA = "age";
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8"><a id="user-content-#Extract" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">8、Extract 提取出一个联合类型中的某一些类型来构造一个新 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Extract<T, U> = T extends U ? T : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和 <code>Exclude</code> 恰好相反。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 从 T1 中 提取出 T2
type T1 = "name" | "age" | "hob";
type T2 = "name" | "age";
type UserInfoT = Extract<T1, T2>;

// 等价于
type UserInfoA = "name" | "age";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然是提出哪为啥不直接用定义好的 T2？</p>
<p>因为这样可以保证 <code>UserInfoT</code> 的类型一定是在 <code>T1</code> 中存在的;</p>
<h2 data-id="heading-9"><a id="user-content-#NonNullable" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">9、NonNullable 从类型中排除 null 和 undefined 来构造一个新的 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type NonNullable<T> = T extends null | undefined ? never : T;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 从 UserInfoK 中 排除掉 null | undefined 
type UserInfoK = NonNullable<"name" | "hob" | undefined>;

// 等价于
type UserInfoKA = "name" | "hob";
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10"><a id="user-content-#Parameters" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">10、Parameters 从 [函数 Type] 的形参构造一个数组 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type Parameters<T extends (...args: any) => any> = T extends (...args: infer P) => any ? P : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>infer</code>标识一个待推导类型，上面定义的意思是：如果 T 为函数类型，那就返回函数的形参。</p>
<p>ps: <code>infer</code>和变量似的，先定义一个 <code>infer P</code> 然后 Ts 就会自动推导函数的形参或者返回值、或者数组元素等，然后开发者在合适的位置使用定义好的<code>infer P</code>即可。</p>
<p><strong>一个简单的<code>infer</code>案例。</strong></p>
<p>加入有这样一个需求：需要将数组类型的 <code>Type</code> 变为联合类型。其他类型的则不变。这样我们就可以写一个这样的 <code>Type</code></p>
<pre><code class="copyable">type ArrayToUnion<T> = T extends Array<infer Item> ? Item : T;

const a:ArrayToUnion<[string, number]> = "111"; // a: string | number
const b:ArrayToUnion<string | number> = "111"; // a: string | number
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个案列的<code>a</code>变量可以看出作用，<code>a</code>变量的类型定义为<code>ArrayToUnion<[string, number]></code>，这里传入的是个数组<code>[string, number]</code>被<code>ArrayToUnion</code>处理为了<code>string | number</code>。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数
function getUserInfo(id:string, group:string)&#123;&#125;

// 获取到函数需要的形参 Type[]
type GetUserInfoArg = Parameters<typeof getUserInfo>;
   
const arg:GetUserInfoArg = [ "001", "002" ];

getUserInfo(...arg);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ps: 上面代码中的<code>typeof</code>是 ts 提供的操作符不是 js 中的那个<code>typeof</code>，只能用到 ts 的类型定义中,
所以使用<code>typeof getUserInfo</code>才能指向函数<code>Type</code></p>
<h2 data-id="heading-11"><a id="user-content-#ConstructorParameters" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">11、ConstructorParameters 从定义的[构造函数]的形参构造数组 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type ConstructorParameters<T extends abstract new (...args: any) => any> = T extends abstract new (...args: infer P) => any ? P : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现原理完全和 <code>Parameters</code> 一样，只不过这个方法接受的事一个类。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">class User&#123;
    constructor(id:string, group:string)&#123;&#125;
&#125;

type NewUserArg =  ConstructorParameters<typeof User>;

const arg:NewUserArg = [ "001", "002"];

new User(...arg);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12"><a id="user-content-#ReturnType" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">12、ReturnType 用函数 Type 的返回值定义一个新的 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>infer</code> 实现。比 <code>Parameters</code> 更简单，可以去看上面的 <code>Parameters</code> 就能明白这段代码意思。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数 Type
type GetUserInfo = ()=>string;

const rt:ReturnType<GetUserInfo> = 'xxx';
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13"><a id="user-content-#InstanceType" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">13、InstanceType 从一个构造函数的实例定义一个新的 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type InstanceType<T extends abstract new (...args: any) => any> = T extends abstract new (...args: any) => infer R ? R : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>infer</code> 实现。和<code>ReturnType</code>实现原理完全一样。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数 Type
type GetUserInfo = ()=>string;

const rt:ReturnType<GetUserInfo> = 'xxx';
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14"><a id="user-content-#ThisParameterType" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">14、ThisParameterType 提取函数 Type 的 this 参数生成一个新的 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type ThisParameterType<T> = T extends (this: infer U, ...args: any[]) => any ? U : unknown;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面定义看出该 <code>Type</code> 对函数的第一个形参 <code>this</code> 做了<code>infer</code>推导。然后返回了推导出来的<code>this</code>。
不清楚<code>infer</code>的话，往上翻，去仔细看看<code>Parameters</code>一节的说明。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数，并且定义函数 this 类型。 
function getUserInfo(this:&#123; name:string &#125;)&#123;&#125;

const getUserInfoArgThis: ThisParameterType<typeof getUserInfo> = &#123;
    name:"王"
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15"><a id="user-content-#OmitThisParameter" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">15、OmitThisParameter 忽略函数 Type 的 this 参数，生成一个新的函数 Type</a></h2>
<p><strong>定义</strong></p>
<pre><code class="copyable">type OmitThisParameter<T> = unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个<code>Type</code>看着略微复杂。咋们拆一下看就会简单很多。</p>
<p>首先说明一下这个<code>Type</code>的这些判断都是干嘛的。</p>
<p>上面定义意思是：如果传入的<code>T</code>没有<code>this</code>参数就直接返回<code>T</code>,如果有<code>this</code>参数就继续进行判断，</p>
<p>第二层判断为：如果T不是函数那也会直接返回<code>T</code>,最后是重新定义了一个函数然后返回。其中使用<code>infer</code>定义了我们所需要的形参和返回值。</p>
<p>这里在座的各位可能会在<code>(...args: infer A) => infer R ? (...args: A) => R : T</code>这里产生疑惑。</p>
<p>上面的写法会直接把<code>this</code>参数过滤掉，为了证实这点，我们可以实现一下：</p>
<pre><code class="copyable">type NoThis<T> = T extends (...args: infer A) => infer R ? A : T

const a:NoThis<typeof getUserInfo>; // a: [id: string]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中我们直接返回了推导的<code>A</code>，得到了形参<code>A</code>的类型。这里面是不会包含<code>this</code>的。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数
function getUserInfo(this:&#123; name:string &#125;, id:string)&#123;&#125;

// 去除 getUserInfo 函数 this 参，然后创建出来了一个新类型
const aaa: OmitThisParameter<typeof getUserInfo> = (id:string)=>&#123;&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16"><a id="user-content-#ThisType" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">16、ThisType 给对象标记 this 接口</a></h2>
<p>这个类型在 lib.d.ts 中定义的就是一个<code>&#123;&#125;</code>空标签，所以用的时候往往比较困惑。特别是没注意看到官网上写的必须开启<code>--noImplicitThis</code>时才可以用的时候。就算你看到了，但是你在他们案例中如果不注意的话还是搞不懂，因为官方案例中设置了这个编译规则 <code>// @noImplicitThis: false</code>。</p>
<p><code>noImplicitThis</code> 规则开启后在函数中的<code>this</code>在不定义的情况下不能使用，相当于严格模式，默认情况下<code>noImplicitThis</code>的值为<code>false</code>，除非手动开启，否则<code>ThisType</code>毫无作用。</p>
<p><strong>使用案例</strong></p>
<pre><code class="copyable">// 定义一个函数
function getUserInfo(this:&#123; name:string &#125;, id:string)&#123;&#125;

// 去除 getUserInfo 函数 this 参，然后创建出来了一个新函数类型
const aaa: OmitThisParameter<typeof getUserInfo> = (id:string)=>&#123;&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17"><a id="user-content-#Uppercase" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">17、Uppercase 将字符串中的每个字符转换为大写</a></h2>
<p>这是对字符串的操作，所有对字符串的操作在 lib.d.ts 中都找不到具体的定义，文档上说是为了提升性能。</p>
<pre><code class="copyable">type MyText = "Hello, world" 
type A = Uppercase<MyText>; // type A = "HELLO, WORLD"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18"><a id="user-content-#Lowercase" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">18、Lowercase 将字符串中的每个字符转换为小写 </a></h2>
<pre><code class="copyable">type MyText = "Hello, world" 
type A = Lowercase<MyText>; // type A = "hello, world"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19"><a id="user-content-#Capitalize" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">19、Capitalize 将字符串中的第一个字符转换为大写</a></h2>
<pre><code class="copyable">type MyText = "hello, world" 
type A = Capitalize<MyText>; // type A = "Hello, world"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20"><a id="user-content-#Uncapitalize" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">20、Uncapitalize 将字符串中的第一个字符转换为小写</a></h2>
<pre><code class="copyable">type MyText = "Hello, world" 
type A = Uncapitalize<MyText>; // type A = "hello, world"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是全部的内容啦~</p>
<p><strong>一款 javascript AST 节点操作插件推荐：</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwangzongming%2Fqnn-object-ast-handle" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wangzongming/qnn-object-ast-handle" ref="nofollow noopener noreferrer">qnn-object-ast-handle</a> -使用操作 js 字面量对象的方式来操作代码文件。使 AST 节点操作变得毫不费力。</p></div>  
</div>
            