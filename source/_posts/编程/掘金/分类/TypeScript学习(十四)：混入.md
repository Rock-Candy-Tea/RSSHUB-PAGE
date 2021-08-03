
---
title: 'TypeScript学习(十四)：混入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1899'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 08:54:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=1899'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">何为混入</h2>
<p>简单地可以理解为，往一个对象( 类 )里面添加一些属性及值。</p>
<p>以下面为例，往 Base 类(对象) 中混入 Scale 属性。</p>
<pre><code class="copyable">type Constructor = new (...arg: any[]) => &#123;&#125;

// 这里利用 泛型 + extends 对 Base类型进行了收束，必须其为一个类
// 因为只有类才可以被继承
function Scale<TBase extends Constructor>(Base: TBase)&#123;
    return class Scaling extends Base&#123;
        _scale = 0
        get Scale(): number&#123;
            return this._scale
        &#125;
        setScale(scale: number)&#123;
            this._scale = scalse
        &#125;
    &#125;
&#125;

// 使用
class Sprite &#123;
    name = "";
    x = 0;
    y = 0;
    
    constructor(name:string)&#123;
        this.name = name
    &#125;
&#125;
const EightBitSprite = Scale(Sprite);
const ins = new EightBitSprite("Bird");
ins.setScale(0.8)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Constrained Mixins</h1>
<p>在混入的过程中，可能需要调用基类特定的方法。而在上述案例中，我们是不能得到基类的潜在(属性)信息。那么，为了开发便利，需要基类具有特定属性的类型。</p>
<p>原理：TS/JS 的构造函数是可以返回一个对象的，利用这种特性，可以“添加” 我们需要访问的特定属性。并且，由于类型是不会侵入JS的，因此这种做法没有问题。</p>
<p>具体如下：</p>
<pre><code class="copyable">// T 默认为一个空对象
// 这里只是单纯地，利用构造函数可以返回一个对象的特性来限制 混入的对象
// 除 枚举类型 外，TS 是不会侵入 JS 的运行时，因此类型会被完全移除，
// 可以看一下最后编译出来的 JS 内容
type GConstructor<T = &#123;&#125;> = new (...arg: any[]) => T


// 三种需要混入的属性

type Positionable = GConstructor<&#123; setPosition: (x:number, y:number) => void &#125;>;

// 类也可以用作类型，那么当然可以当做泛型
type Spritable = GConstructor<Sprite>

type Loggable = GConstructor<&#123; print: () => void &#125;>

// 挑选第一个混入
function Jumpable<TBase extends Positionable>(Base: TBase)&#123;
    return class Jumpable extends Base&#123;
        Jump(x:number, y:number)&#123;
            // 这里就有类型提示了
            // 开发者可以明确地知道需要用到的 Base 类的特定属性
            this.setPosition(x, y)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">可选择的模式 Alternative Pattern</h2>
<p>上述案例都是单个混入。那么<strong>混入多个对象</strong>呢？</p>
<p>下述案例直接在运行时往原型上混入对象，以确保类型系统与运行时一致。</p>
<pre><code class="copyable">class Jumpable&#123;
    Jump()&#123;&#125;
&#125;

class Duckable&#123;
    ducn()&#123;&#125;
&#125;

class Sprite&#123;
    x = 0;
    y = 0;
&#125;

interface Sprite extends Jumpable, Duckable &#123;&#125;
applyMixin(Sprite, [Jumpable, Duckable])

// 
function applyMixin(derivedCtor: any, constructors: any[])&#123;
    constructors.forEach( baseCtor =>&#123;
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => &#123;
           Object.defineProperty( 
            derivedCtor.prototype, 
            name, 
            Object.getOwnPropertyDescriptor(baseCtor.prototype, name) ||
            object.create(null)
            )    
        &#125;)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">限制</h2>
<h3 data-id="heading-4">不能使用装饰器完成混入</h3>
<pre><code class="copyable">const Pausable = (target: typeof Player) => &#123;
    return calss Pausable extends target&#123;
        shouldFreeze = false
    &#125;
&#125;

@Pausable
class Player&#123;
    x = 0;
    y = 0
&#125;

const player = new Player()

// carsh
// The Player class does not have the decorator's type merged:
player.shouldFreeze
<span class="copy-code-btn">复制代码</span></code></pre>
<p>补救方法</p>
<pre><code class="copyable">type FreezablePlayer = Player & &#123; shouldFreeze: boolean &#125;;

const playerTwo = (new Player() as unknown) as FreezablePlayer;

playerTwo.shouldFreeze;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">静态属性的混入</h3>
<p>下面写法中 Gen 的 泛型 T  与 base() 函数中的泛型 T 的作用域不同，因此会导致出错。</p>
<p>具体情况如下：</p>
<pre><code class="copyable">function base<T>() &#123;    return class Base &#123;        static prop: T;    &#125;&#125;
// crash
// Base class expressions cannot reference class type parameters.
// 即，不能使用泛型 混入 静态类型
class Gen<T> extends base<T>() &#123;&#125;class Spec extends Gen<string> &#123;&#125;
// JSX 写法
<string>Spec.prop;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绕过上述机制的方法：</p>
<p>利用函数，使得 泛型的作用域保持一致</p>
<pre><code class="copyable">function base<T>() &#123;  
    return class Base &#123;    
        static prop: T;  
    &#125;
&#125;

function derived<T>() &#123;  
    return class Derived extends base<T>() &#123;    
        static anotherProp: T;  
    &#125;
&#125;

class Spec extends derived<string>() &#123;&#125;
class AnotherSpec extends derived<number>() &#123;&#125;

Spec.prop; // string

Spec.anotherProp; // string
AnotherSpec.prop; // number
Spec.anotherProp; // number
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            