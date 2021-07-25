
---
title: 'TypeScript学习(九)：Handbook -_ Classes'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9431'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:59:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=9431'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">--strictPropertyInitialization</h3>
<p>参数开启时，calss 的属性必须在构造函数中定义初始值。可以在属性后面添加 ! 来关闭提示。</p>
<pre><code class="copyable">class BadGreeter&#123;
    // Property 'name' has no initializer and is not definitely assigned in the constructor.
    name: string
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">构造函数</h3>
<p><strong>重载</strong></p>
<pre><code class="copyable">class Point &#123;
    constructor(x:number, y:number);
    constructor(s:string)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：构造函数不能有类型参数；构造函数不能返回类型。</strong></p>
<h3 data-id="heading-2">get/set</h3>
<p>1. 只有get，没有set ----> readonly</p>
<p>2. set 参数没有类型，会自动从 get 的返回值推导类型</p>
<p>3. get/set 必须有相同的 Member Visibility，即 private、public、protected</p>
<p><strong>注意：TS 4.3 中 set/get 可以有不同的类型的 value。</strong></p>
<h3 data-id="heading-3">implement</h3>
<p>类必须满足一个特定的 interface，可以实现多个 interface。</p>
<pre><code class="copyable">class C implements A, B&#123;
    // 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<p>1. implement 只检查类是不是可以被作为一个 interface。Mehtod  的类型是不会被 implement 改变的。</p>
<p>下方会报错。直觉上会认为 check 方法的参数 s 必然是一个 string。但实际上 implement 后并不会改变 class 内 mtehod 的类型。s 会被稳定为 any。</p>
<pre><code class="copyable">interface Checkable&#123;
    check(name: string): boolean;
&#125;

class NameChecker implements Checkable&#123;
    check(s)&#123;
        returnt s.toLowercse() === 'ok'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 2. 可选属性</p>
<pre><code class="copyable">interface A&#123;
    x: number;
    y?: number;
&#125;

class C implement A&#123;
    x = 0
&#125;
cosnt c = new C()
// 报错
c.y = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">extends</h3>
<p>衍生类继承基类的所有属性和方法，并且可以扩展。</p>
<p><strong>方法重写 Overriding Methods</strong></p>
<p>衍生类可以重写基类的方法，但是方法必须有相同接口。下方报错。</p>
<pre><code class="copyable">class Base&#123;
    greet()&#123;
    console.log("Hello, World!")
    &#125;
&#125;

class Drived extends Base&#123;
    // 接口不一致 报错
    greet(name: string)&#123;
        console.log(name)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>类的初始化顺序</strong></p>
<p>1. 基类字段初始化</p>
<p>2. 基类构造函数初始化</p>
<p>3. 衍生类字段初始化</p>
<p>4. 衍生类构造函数初始化</p>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Fclasses.html%23inheriting-built-in-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/classes.html#inheriting-built-in-types" ref="nofollow noopener noreferrer">内建类型的继承</a> ---> 适用于ES5</h3>
<p>ES5 中派生类的 this 是由派生类创建，再由基类改造；ES6及以后，派生类的 this 是由基类创建，再由派生类改造。</p>
<p>因此：</p>
<p>1. ES5 中，派生类的某些方法可能不存在</p>
<p>2. instanceof 操作符应用在派生类及其实例的时候会失效；( new MsgError() ) instanceof MsgError ---> false</p>
<pre><code class="copyable">class MsgError extends Error&#123;
    constructor(m:string)&#123;
        super(m);
    &#125;
    sayHello()&#123;
        return this.message
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挽救方法 ( IE10 及其之前都无效 )</p>
<p>手动调整原型链</p>
<pre><code class="copyable">class MsgError extends Error&#123;
    constructor(m:string)&#123;
        super(m)
        // 调整一下原型链
        Object.setPrototyeOf(this, MsgError.prorotype)    
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：MsgError 的子类也要手动设置原型链</strong></p>
<p>**个人理解：**ES6 中衍生类修饰 基类创建的 this，然后衍生类构造函数返回修饰后的 this 。TS 中的表现与 ES6 一样，但是 TS ---> ES5 及以下的时候，旧语法不支持此特性，因此要手动调整原型链。</p>
<h3 data-id="heading-6"><strong>类成员可见度 Member Visiblity</strong></h3>
<p><strong>public</strong>：在 类 的外部任何地方都可以访问类的属性、方法</p>
<p><strong>protected</strong>：只能在  子类 中访问基类的方法、属性，不能在 基类 外部访问</p>
<p>下述情况再不同的 OOP 语言中行为不同。在TS/C#/C++中，下述 Derived2 类的 f2 方法是不合法的。因为直接访问的是 基类的 protected 属性。</p>
<pre><code class="copyable">class Base &#123;
    protected x: number = 1
&#125;
class Derived1 extends Base&#123;
    protected x: number = 5
&#125;
class Derived2 extends Base&#123;
    f1(other: Derived2)&#123;
        other.x = 10
    &#125;

    // Property 'x' is protected and only accessible through an instance of class 'Derived2'. 
    // This is an instance of class 'Base'.
    f2(other: Base)&#123;
        other.x = 10
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>private</strong>：只能在类内部访问属性、方法</p>
<p><strong>在 TS 中，在某一类的一众实例中，其中一个实例的方法可以访问其余实例的私有成员。貌似和private行为相反？</strong></p>
<p>而 Java，C# 之类的语言并不能。</p>
<pre><code class="copyable">class A&#123;
    private x = 10
    public sameAs(other: A)&#123;
        // work
        return other.x === this.x
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>JavaScript的私有属性：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FPrivate%255C_class%255C_fields" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private%5C_class%5C_fields" ref="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></strong></p>
<h3 data-id="heading-7">静态成员</h3>
<p>只能被类的构造函数调用，其实就是构造函数上添加了一众属性、方法。</p>
<p>静态成员也可以使用 plublic，protected，private修饰。</p>
<p><strong>保留字</strong>：name、length、call 等 Function  的属性是不能被定义成静态成员的。</p>
<h3 data-id="heading-8">静态类</h3>
<p>TS 中不存在静态类</p>
<p>JAVA，C# 等语言中，并不允许方法、属性脱离 class 单独存在，因此只能通过 静态类的方法实现 TS/JS 中的功能。</p>
<pre><code class="copyable">// 其他语言的写法
class MyStaticClass&#123;
    static doSomething() &#123;&#125;
&#125;

// TS/JS 的写法一
function doSomething() &#123;&#125;
// TS/JS 的方法二
const MyHelperObject = &#123;
    dosomething() &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">泛型类</h3>
<p><strong>静态方法的类型</strong>：TS 中静态成员是不可以设置泛型的。反向思考一下，如果下方Box 一个实例的 Box.defaultValue 的值被的设为一个 string 类型的。那么另一个实例 Box.defaultValue 的值就成了 string，而不是 number。</p>
<pre><code class="copyable">class Box<T>&#123;
    // Static members cannot reference class type parameters.
    static defaultValue:T
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">运行时 runtime</h3>
<p>TS 并不改变 JS 的运行时逻辑，因此，与 JS 一样会有诡异的行为。</p>
<p>what‘s this in JS?</p>
<h3 data-id="heading-11">箭头函数</h3>
<p>箭头函数的 this 是词法作用域。</p>
<p>1. 可以保证 this 的值永远正确，避免一些诡异行为</p>
<p>2. 占用内存更多，每个使用箭头函数写法的类实例，都会保存一遍 this 的值</p>
<p>3. 在派生类中并不能使用 super.getName。因此箭头函数的写法并不会保存在原型链上</p>
<pre><code class="copyable">class MyClass&#123;
    name = "MyClass"
    getName = () =>&#123;
        return this.name    
    &#125;
&#125;
const c = new MyClass()
const g = c.getName

// Prints "MyClass" instead of crashing
console.log(g())
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12"></h3>
<p><strong>this parameters</strong></p>
<p>this 作为函数的参数时，TS 会抹去 this。</p>
<pre><code class="copyable">// TS 中的写法
function fn(this: SomeType, x:number)&#123;&#125;

// 转化为 JS 后，等价于下方
function fn(x) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在method 中，通过传入 MyClass 类型的 this 参数以保证 方法的 上下文是正确的。同样地，在运行时中，this 参数会被抹去。同样地，在global context 执行 getName 会报错。</p>
<pre><code class="copyable">class MyClass&#123;
    name = "MyClass"
    getName(this: MyClass)&#123;
        return this.name
    &#125;
&#125;

const c = new MyClass()
c.getName()

// crash
const g = c.getName
g()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">this 类型 ---> this Types</h3>
<p>TS 中， class 可以使用 this <strong>类型</strong>。</p>
<pre><code class="copyable">class Box&#123;
    content = string = ""
    sameAs(other:this)&#123;
        return other.content === this.content
    &#125;
&#125;

class DerivedBox extends Box &#123;
    otherContent: string = "?"
&#125;
const base  = new Box
const derived = nwe DerivedBox
derived.sameAs(base)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">this 作为类型守卫</h3>
<p>使用 this 结合 其他类型守卫 手段可以将目标对象收缩到特定的 类型。</p>
<p>下方案例中 this is  Networked & this 理解是 this is (Networked & this)。isNetwork() 函数执行后，更改了 this 的类型，因此 FileRep 类有了 Networked 的类型，即，将对象收缩到特定类型。</p>
<pre><code class="copyable">class FileSystemObejct&#123;
    isFile(): this is FileRep&#123;
        return this instanceof FileRep
    &#125;
    isDirectory():this is Directory &#123;
        reutn this instanceof Directory
    &#125;
    isNetworked(): this is Networked & this&#123;
        return this.networked
    &#125;
    constructor(public path: string, private networked: bolean)&#123;&#125;
&#125;

class FileRep extends FileSystemObject&#123;
    constructor(path:string, public content:string)&#123;
        super(path, false)
    &#125;
&#125;

class Directory extends FileSystemObject&#123;
    children: FileSystemObejct[]
&#125;

interface Networked&#123;
    host: string
&#125;

const fso: FileSystemObject = new FileRep("foo/bar.text", "foo")

if(fso.isFile())&#123;
    // FileRep
    fso.content;
&#125;else if(fso.isDirectory())&#123;
    // Directory
    fso.children
&#125;else if (fso.isNetworked())&#123;
    // Networked & FileSystemObject
    fso.host
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>普遍用法</strong></p>
<p>这个案例中，利用 this is 去移除 value 的 undefined 类型。</p>
<pre><code class="copyable">class Box<T>&#123;
    value?: T
    
    hasValue(): this is &#123;value: T&#125;&#123;
    return this.value !== undefined
    &#125;
&#125;

const box = new Box()
// (property) Box<unknow>.value?: unknown 
box.value = "Gameboy"

if(box.hasValue())&#123;
    // value: unknown
    box.value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">Parameter Properties</h3>
<p>TS 中类的构造函数可以不用给构造函数的变量赋值，TS 会创建与参数类型相同的 类属性，并且在构造函数执行的时候 赋值。</p>
<pre><code class="copyable">class Params&#123;
    cosntructor(
        public readonly x: number,
        protected y: number,
        private z: number
    )&#123;
        // no body necessary
    &#125;
&#125;

const a = new Params(1, 2, 3)
// work
console.log(a.x)

// crash
console.log(a.z)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16"></h3>
<p>类表达式 Class Expressions</p>
<p>下方的类表达式写法与直接声明一个类的效果相同，但是不同的是在表达式中可以省略类的名称。</p>
<pre><code class="copyable">const someClass = class<T> &#123;
    content:T;
    constructor(value:T)&#123;
        this.content = value;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">抽象类与类成员 abstract Classes and Members</h3>
<p>抽象方法或属性并不需要提供其实现，且只能存在抽象类中。抽象类并不能直接被实例化，通常用作基类。其派生类必须实现其类的抽象方法，否则会报错。</p>
<pre><code class="copyable">abstract class Base&#123;
    abstract getName():String;
    printName()&#123;
         console.log(`hello, $&#123;this.getName()&#125;`)
    &#125;
&#125;

// crash
const b = new Base()

class Derived extends Base&#123;
    getName()&#123;
        return "world";
    &#125;
&#125;

const d = new Derived();
// work
d.printName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在某些情况下，可能想接收类的构造函数，并且创建类的实例，但是碰到抽象类会报错。</p>
<p>下方，街上上述抽象类 Base</p>
<pre><code class="copyable">function greet(ctor: typeof Base)&#123;
    // crash 
    const instance = new ctor()
    instance.printName()
&#125;

function greet1(ctor: new () => Base)&#123;
    const instance = new Ctor()
    instance.printName()
&#125;

// work
greet(Derived)
// crash
// Cannot assign an abstract constructor type to a non-abstract constructor type.
greet(Base)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">类之间的关系</h3>
<p>大多数情况下，TS 只会比较类的结构。</p>
<pre><code class="copyable">class Point1&#123;
    x = 0;
    y = 0;
&#125;
class Point2&#123;
    x = 0;
    y = 0;
&#125;
// work
const p: Point1 = new Point2()

class Person&#123;
    name: string;
    age: number;
&#125;
class Employee&#123;
    name: string;
    age: number;
    salary: number;
&#125;
// work
const p1: Person = new Employee()
// crash
const p2: Employee = new Person()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Empty Class：空类没有任何成员，在结构化的类型系统中，空类是任何对象的超类。</p>
<pre><code class="copyable">class Empty&#123;&#125;
function fn(x: Empty)&#123;
    // ...
&#125;

// All OK!
fn(window)
fun(&#123;&#125;)
fn(fn)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">参考</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Fclasses.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/classes.html" ref="nofollow noopener noreferrer">www.typescriptlang.org/docs/handbo…</a></p></div>  
</div>
            