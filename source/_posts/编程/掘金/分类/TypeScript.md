
---
title: 'TypeScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9113'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 03:21:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=9113'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">静态类型与动态类型</h2>
<p>在动态语言JS中，变量是没有类型的。而存放在里面的值是有类型的</p>
<pre><code class="copyable">let foo = 100
foo = '张三' // foo, 此时变为字符串类型
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>类型安全：强类型、弱类型（是否允许隐式类型转换：'100' - 50 ，这里其实是可以计算的）</li>
<li>类型检查：静态类型、动态类型（是否允许修改变量的类型）</li>
</ul>
<h2 data-id="heading-1">基本数据类型</h2>
<pre><code class="copyable">// 原始数据类型

const a: string = 'foobar'

const b: number = 100 // NaN Infinity

const c: boolean = true // false

// 在非严格模式（strictNullChecks）下，
// string, number, boolean 都可以为空
// const d: string = null
// const d: number = null
// const d: boolean = null

const e: void = undefined

const f: null = null

const g: undefined = undefined

// Symbol 是 ES2015 标准中定义的成员，
// 使用它的前提是必须确保有对应的 ES2015 标准库引用
// 也就是 tsconfig.json 中的 lib 选项必须包含 ES2015
const h: symbol = Symbol()

// Promise

// const error: string = 100
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">作用域</h2>
<ul>
<li>默认文件中的成员会作为全局成员</li>
<li>多个文件中有相同成员就会出现冲突</li>
</ul>
<pre><code class="copyable">// const a = 123

// 解决办法1: IIFE 提供独立作用域
    (function () &#123;
      const a = 123
    &#125;)()

// 解决办法2: 在当前文件使用 export，也就是把当前文件变成一个模块
// 模块有单独的作用域
    const a = 123
    export &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Object 类型</h2>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

// object 类型是指除了原始类型以外的其它类型
const foo: object = function () &#123;&#125; // [] // &#123;&#125;

// 如果需要明确限制对象类型，则应该使用这种类型对象字面量的语法，或者是「接口」
const obj: &#123; foo: number, bar: string &#125; = &#123; foo: 123, bar: 'string' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">数组类型</h2>
<pre><code class="copyable">// 数组类型的两种表示方式

const arr1: Array<number> = [1, 2, 3]

const arr2: number[] = [1, 2, 3]

// 案例 -----------------------

// 如果是 JS，需要判断是不是每个成员都是数字
// 使用 TS，类型有保障，不用添加类型判断
function sum (...args: number[]) &#123;
  return args.reduce((prev, current) => prev + current, 0)
&#125;

sum(1, 2, 3) // => 6
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">元组（Tuple）</h2>
<pre><code class="copyable">const tuple: [number, string] = [18, 'zce']

// const age = tuple[0]
// const name = tuple[1]

const [age, name] = tuple

// ---------------------

const entries: [string, number][] = Object.entries(&#123;
  foo: 123,
  bar: 456
&#125;)

const [key, value] = entries[0]
// key => foo, value => 123
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">枚举（Enum）</h2>
<pre><code class="copyable">// 用对象模拟枚举
// const PostStatus = &#123;
//   Draft: 0,
//   Unpublished: 1,
//   Published: 2
// &#125;

// 标准的数字枚举
// enum PostStatus &#123;
//   Draft = 0,
//   Unpublished = 1,
//   Published = 2
// &#125;

// 数字枚举，枚举值自动基于前一个值自增
// enum PostStatus &#123;
//   Draft = 6,
//   Unpublished, // => 7
//   Published // => 8
// &#125;

// 字符串枚举
// enum PostStatus &#123;
//   Draft = 'aaa',
//   Unpublished = 'bbb',
//   Published = 'ccc'
// &#125;

// 常量枚举，不会侵入编译结果
const enum PostStatus &#123;
  Draft,
  Unpublished,
  Published
&#125;

const post = &#123;
  title: 'Hello TypeScript',
  content: 'TypeScript is a typed superset of JavaScript.',
  status: PostStatus.Draft // 3 // 1 // 0
&#125;

// PostStatus[0] // => Draft
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">函数类型</h2>
<pre><code class="copyable">function func1 (a: number, b: number = 10, ...rest: number[]): string &#123;
  return 'func1'
&#125;

func1(100, 200)

func1(100)

func1(100, 200, 300)

// -----------------------------------------

const func2: (a: number, b: number) => string = function (a: number, b: number): string &#123;
  return 'func2'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">任意类型（弱类型）</h2>
<ul>
<li>any 类型是不安全的</li>
</ul>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

function stringify (value: any) &#123;
  return JSON.stringify(value)
&#125;

stringify('string')

stringify(100)

stringify(true)

let foo: any = 'string'

foo = 100

foo.bar()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">隐式类型推断</h2>
<ul>
<li>虽然有类型推断，但还是建议，为每个变量添加明确的类型标注</li>
</ul>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

let age = 18 // number

// age = 'string'

let foo

foo = 100

foo = 'string'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">类型断言</h2>
<ul>
<li>2种方式，但更建议用as</li>
</ul>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

// 假定这个 nums 来自一个明确的接口
const nums = [110, 120, 119, 112]

const res = nums.find(i => i > 0)

// const square = res * res

const num1 = res as number

const num2 = <number>res // JSX 下不能使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">接口</h2>
<p>约定对象中的结构，约定了必须要有其成员。有点类似前后端配合的接口文档</p>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

interface Post &#123;
  title: string
  content: string
&#125;

function printPost (post: Post) &#123;
  console.log(post.title)
  console.log(post.content)
&#125;

printPost(&#123;
  title: 'Hello TypeScript',
  content: 'A javascript superset'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">可选成员、只读成员、动态成员</h2>
<p>？表示可有可无</p>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

// -------------------------------------------

interface Post &#123;
  title: string
  content: string
  subtitle?: string
  readonly summary: string
&#125;

const hello: Post = &#123;
  title: 'Hello TypeScript',
  content: 'A javascript superset',
  summary: 'A javascript'
&#125;

// hello.summary = 'other'

// ----------------------------------

interface Cache &#123;
  [prop: string]: string
&#125;

const cache: Cache = &#123;&#125;

cache.foo = 'value1'
cache.bar = 'value2'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">类（Class）</h2>
<pre><code class="copyable">class Person &#123;
  name: string // = 'init name'
  age: number
  
  constructor (name: string, age: number) &#123;
    this.name = name
    this.age = age
  &#125;

  sayHi (msg: string): void &#123;
    console.log(`I am $&#123;this.name&#125;, $&#123;msg&#125;`)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">类的访问修饰符</h2>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

class Person &#123;
  public name: string // = 'init name'
  private age: number
  protected gender: boolean
  
  constructor (name: string, age: number) &#123;
    this.name = name
    this.age = age
    this.gender = true
  &#125;

  sayHi (msg: string): void &#123;
    console.log(`I am $&#123;this.name&#125;, $&#123;msg&#125;`)
    console.log(this.age)
  &#125;
&#125;

class Student extends Person &#123;
  private constructor (name: string, age: number) &#123;
    super(name, age)
    console.log(this.gender)
  &#125;

  static create (name: string, age: number) &#123;
    return new Student(name, age)
  &#125;
&#125;

const tom = new Person('tom', 18)
console.log(tom.name)
// console.log(tom.age)
// console.log(tom.gender)

const jack = Student.create('jack', 18)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">类的只读属性</h2>
<p>public（默认）、private、protected、readonly</p>
<pre><code class="copyable">export &#123;&#125; // 确保跟其它示例没有成员冲突

class Person &#123;
  public name: string // = 'init name'
  private age: number
  // 只读成员
  protected readonly gender: boolean
  
  constructor (name: string, age: number) &#123;
    this.name = name
    this.age = age
    this.gender = true
  &#125;

  sayHi (msg: string): void &#123;
    console.log(`I am $&#123;this.name&#125;, $&#123;msg&#125;`)
    console.log(this.age)
  &#125;
&#125;

const tom = new Person('tom', 18)
console.log(tom.name)
// tom.gender = false
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">类与接口</h2>
<pre><code class="copyable">interface Eat &#123;
  eat (food: string): void
&#125;

interface Run &#123;
  run (distance: number): void
&#125;

class Person implements Eat, Run &#123;
  eat (food: string): void &#123;
    console.log(`优雅的进餐: $&#123;food&#125;`)
  &#125;

  run (distance: number) &#123;
    console.log(`直立行走: $&#123;distance&#125;`)
  &#125;
&#125;

class Animal implements Eat, Run &#123;
  eat (food: string): void &#123;
    console.log(`呼噜呼噜的吃: $&#123;food&#125;`)
  &#125;

  run (distance: number) &#123;
    console.log(`爬行: $&#123;distance&#125;`)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">抽像类</h2>
<ul>
<li>不包含具体实现，比如大的类</li>
<li>只能被继承，只能new</li>
</ul>
<pre><code class="copyable">abstract class Animal &#123;
  eat (food: string): void &#123;
    console.log(`呼噜呼噜的吃: $&#123;food&#125;`)
  &#125;

  abstract run (distance: number): void
&#125;

class Dog extends Animal &#123;
  run(distance: number): void &#123;
    console.log('四脚爬行', distance)
  &#125;

&#125;

const d = new Dog()
d.eat('嗯西马')
d.run(100)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">泛型</h2>
<p>定义函数，接口时，没有指定具体类型，等使用时，再去指定</p>
<pre><code class="copyable">function createNumberArray (length: number, value: number): number[] &#123;
  const arr = Array<number>(length).fill(value)
  return arr
&#125;

function createStringArray (length: number, value: string): string[] &#123;
  const arr = Array<string>(length).fill(value)
  return arr
&#125;

function createArray<T> (length: number, value: T): T[] &#123;
  const arr = Array<T>(length).fill(value)
  return arr
&#125;

// const res = createNumberArray(3, 100)
// res => [100, 100, 100]

const res = createArray<string>(3, 'foo')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">类型声明</h2>
<p>使用时 declare 对应的声明</p>
<pre><code class="copyable">import &#123; camelCase &#125; from 'lodash'
import qs from 'query-string'

qs.parse('?key=value&key2=value2')

// declare function camelCase (input: string): string

const res = camelCase('hello typed')
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            