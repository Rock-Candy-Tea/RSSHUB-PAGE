
---
title: 'TypeScript高级用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=958'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 00:08:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=958'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<p>TypeScript 是 JavaScript 的类型的超集，它可以编译成纯 JavaScript。编译出来的 JavaScript 可以运行在任何浏览器上。TypeScript 编译工具可以运行在任何服务器和任何系统上。笔者使用typescript也差不多快一年了，使用Ts也感受颇深，Ts无疑增强我们代码的规范性和可维护性，但是也同时增加了我们的开发负担，但是其实对一个项目的长期而言，我认为这是值得的，这篇文章我们来讲一下Ts的高级用法，适合刚接触Ts的同学但是学的没有那么深的同学，至于我们的vue源码分析，我先暂更一周，在以后的时间将会继续讲到。</p>
<h4 data-id="heading-1">一、类型</h4>
<h6 data-id="heading-2">1. unknow</h6>
<p>unknown 指的是不可预先定义的类型，在很多场景下，它可以替代 any 的功能同时保留静态检查的能力。</p>
<pre><code class="copyable">const num: number = 10;
(num as string).split('') // error 类型 "number" 到类型 "string" 的转换可能是错误的，因为两种类型不能充分重叠。如果这是有意的，请先将表达式转换为 "unknown"。
(num as unknown as string).split('')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候 unknown 的作用就跟 any 高度类似了，你可以把它转化成任何类型，不同的地方是，在静态编译的时候，unknown 不能调用任何方法，而 any 可以。</p>
<pre><code class="copyable">const foo: unknown = 'string';
foo.substr(1);   // Error: 静态检查不通过报错
const bar: any = 10;
bar.substr(1);// Pass: any类型相当于放弃了静态检查
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unknown 的一个使用场景是，避免使用 any 作为函数的参数类型而导致的静态类型检查 bug：</p>
<pre><code class="copyable">function test(input: unknown): number &#123;
  if (Array.isArray(input)) &#123;
    return input.length;    // Pass: 这个代码块中，类型守卫已经将input识别为array类型
  &#125;
  return input.length;      // Error: 这里的input还是unknown类型，静态检查报错。如果入参是any，则会放弃检查直接成功，带来报错风险
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-3">2. enum</h6>
<p>枚举的话可以增强我们代码的可读性，例如我在业务中需要个后端传一个回答问题的类型type，回复文本的话需要传一个1，回复图片的会传2，如果直接在调用接口的时候传一个2那肯定会让别人看上去很疑惑，如此一来我们可以定义一个枚举,需要传值例如传一个视频，我们可以传AnswerMessageType.video,而且在写接口规范参数类型的时候我们可以规定这个type为AnswerMessageType，如此一来你要是传个7就肯定不能通过的。</p>
<pre><code class="copyable">/**
 * 回复问题的消息类型
 */
 export enum AnswerMessageType &#123;
    text = 0,
    pictrue = 1,
    video = 2,
    voice = 3,
    file = 4,
    /**
     * Srceent Rock 链接
     */
    srlink = 6
  &#125;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-4">3. void</h6>
<p>在 TS 中，void 和 undefined 功能高度类似，可以在逻辑上避免不小心使用了空指针导致的错误。
void 和 undefined 类型最大的区别是，你可以理解为 undefined 是 void 的一个子集，当你对函数返回值并不在意时，使用 void 而不是 undefined。举一个 React 中的实际的例子。</p>
<pre><code class="copyable">// Parent.tsx
const  Parent: FC = () => &#123;
    const getValue = (): number => &#123; return 2 &#125;;   /* 这里函数返回的是number类型 */
    // const getValue = (): string => &#123; return 'str' &#125;;/* 这里函数返回的string类型，同样可以传给子属性 */
    return <Child getValue=&#123;getValue&#125; />
&#125;
// Child.tsx
type Props = &#123;
  getValue: () => void;  // 这里的void表示逻辑上不关注具体的返回值类型，number、string、undefined等都可以
&#125;
function Child(&#123; getValue &#125;: Props) => <div>&#123;getValue()&#125;</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">运算符</h4>
<h6 data-id="heading-6">1. 非空断言运算符 ！</h6>
<p>这个运算符可以用在变量名或者函数名之后，用来强调对应的元素是非 null|undefined 的</p>
<pre><code class="copyable">function onClick(callback?: () => void) &#123;
    callback();// 参数是可选入参，加了这个感叹号!之后，TS编译不报错
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个符号的场景，特别适用于我们已经明确知道不会返回空值的场景，从而减少冗余的代码判断，如 React 的 Ref。以下是笔者工作中写的一个自定义hook,左右两个div,左边放图片，右边是一段文字文字的多少是不确定的，左边的图片根据右边的盒子来计算大小，如下使用了多个ref，但是我们在一些情况写可以！来判断e.target！或者divRef.current！来进行一个书写</p>
<pre><code class="copyable">export function useCalcImg() &#123;
  const [maxWidth, setMaxWidth] = useState(0)
  const [maxHeight, setMaxHeight] = useState(0)
  const [imgWidth, setImgWidth] = useState(0)
  const [imgHeiht, setImgHeight] = useState(0)
  const imgRef = useRef(null)
  const divRef = useRef<HTMLDivElement>()
  const handleImgLoad = useCallback((e) => &#123;
    let img = e.target as HTMLImageElement
    setImgWidth(img.naturalWidth)
    setImgHeight(img.naturalHeight)
  &#125;, [])
  const calc = () => &#123;
    if (maxWidth && imgWidth && imgRef.current) &#123;
      let div = divRef.current
      setTimeout(() => &#123;
        let &#123; width, height &#125; = Util.calc.fixedImgScale(imgWidth, imgHeiht, div.clientWidth, div.clientHeight)
        imgRef.current.width = width
        imgRef.current.height = height
        removeClass(imgRef.current, 'hidden')
      &#125;, 100)
      imgRef.current.width = 100
    &#125;
  &#125;

  const imgRefCallback = useCallback((img) => &#123;
    imgRef.current = img
  &#125;, [])
  useEffect(() => &#123;
    calc()
  &#125;, [imgRef, divRef, maxWidth, imgHeiht])
  const refCallback = useCallback((e) => &#123;
    divRef.current = e
    if (e) &#123;
      const &#123; clientWidth, clientHeight &#125; = e
      setMaxWidth(clientWidth)
      setMaxHeight(clientHeight)
    &#125;
  &#125;, [])
  return &#123;
    imgRefCallback,
    handleImgLoad,
    refCallback
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">2. 可选链操作运算符 ？</h6>
<p>相比上面!作用于编译阶段的非空判断，?.这个是开发者最需要的运行时(当然编译时也有效)的非空判断。</p>
<pre><code class="copyable">// 例如后端有个参数标识flag,有标识的时候传flag: 1, 没有标识的时候不传
data?.flag
<span class="copy-code-btn">复制代码</span></code></pre>
<p>?.用来判断左侧的表达式是否是 null | undefined，如果是则会停止表达式运行，可以减少我们大量的&&运算。</p>
<p>比如我们写出a?.b时，编译器会自动生成如下代码</p>
<pre><code class="copyable">let b = a !== null && a !== void 0 ? a : 10;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">三、操作符</h4>
<h6 data-id="heading-9">1. keyof</h6>
<p>keyof 可以获取一个类型所有键值，返回一个联合类型，如下：</p>
<pre><code class="copyable">type Person = &#123;
  name: string;
  age: number;
&#125;
type PersonKey = keyof Person;  // PersonKey得到的类型为 'name' | 'age'
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">2. typeof</h6>
<p>typeof 是获取一个对象/实例的类型，如下</p>
<pre><code class="copyable">interface Person &#123;
    name: string,
    age: number
&#125;
const people: Person = &#123;
    name: 'thl',
    age: 22
&#125;
const P = typeof people // &#123; name: string, age: number | undefined &#125;
const me: typeof people = &#123; name: 'wsy', age: 21 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-11">3. in</h6>
<p>in 只能用在类型的定义中，可以对枚举类型进行遍历，如下：</p>
<pre><code class="copyable">// 这个类型可以将任何类型的键值转化成number类型
type TypeToNumber<T> = &#123;
  [key in keyof T]: number
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keyof返回泛型 T 的所有键枚举类型，key是自定义的任何变量名，中间用in链接，外围用[]包裹起来(这个是固定搭配)，冒号右侧number将所有的key定义为number类型。</p>
<pre><code class="copyable">const person: TypeToNumber<Person> = &#123;name: 21, age: 21&#125;
// [ 自定义变量名 in 枚举类型 ]: 类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">四、泛型</h4>
<p>泛型在 TS 中可以说是一个非常重要的属性，它承载了从静态定义到动态调用的桥梁，同时也是 TS 对自己类型定义的元编程。泛型可以说是 TS 类型工具的精髓所在，也是整个 TS 最难学习的部分。
基本使用</p>
<pre><code class="copyable">// 普通类型定义
type Person<T> = &#123; name: string, type: T &#125;
// 普通类型使用
const person: Person<number> = &#123; name: 'ww', type: 20 &#125;

// 类定义
class People<T> &#123;
  private type: T;
  constructor(type: T) &#123; this.type = type; &#125;
&#125;
// 类使用
const people: People<number> = new People<number>(20); // 或简写 const people = new People(20)

// 函数定义
function swipe<T, U>(value: [T, U]): [U, T] &#123;
  return [value[1], value[0]];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如深度克隆</p>
<pre><code class="copyable">export function deepCopy<T extends Record<any, any>>(data: T): T &#123;
  const t = typeOf(data)
  let o

  if (t === 'array') &#123;
    o = []
  &#125; else if (t === 'object') &#123;
    o = &#123;&#125;
  &#125; else &#123;
    return data
  &#125;

  if (t === 'array') &#123;
    for (let i = 0; i < ((data as any) as any[]).length; i++) &#123;
      o.push(deepCopy(data[i]))
    &#125;
  &#125; else if (t === 'object') &#123;
    for (let i in data) &#123;
      o[i] = deepCopy(data[i])
    &#125;
  &#125;
  return o
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">五、高级泛型</h4>
<h6 data-id="heading-14">1. Partial</h6>
<p>此工具的作用就是将泛型中全部属性变为可选的。</p>
<pre><code class="copyable">type Partial<T> = &#123;
    [P in keyof T]?: T[P]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子,此时happy这个方法可以不传</p>
<pre><code class="copyable">type Person = &#123;
    name: string
    age: number
    happy: () => void
&#125;
const me: Partial<Person> = &#123;
    name: 'thl',
    age: 22
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">2、Record<K, T></h6>
<p>此工具的作用是将 K 中所有属性值转化为 T 类型，我们常用它来申明一个普通 object 对象。</p>
<pre><code class="copyable">type Record<K extends keyof any,T> = &#123;
  [key in K]: T
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子</p>
<pre><code class="copyable">const me: Record<string, string> = &#123; 'name': 'thl', 'tag': '打工人' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-16">3. Pick<T, K></h6>
<p>此工具的作用是将 T 类型中的 K 键列表提取出来，生成新的子键值对类型。</p>
<pre><code class="copyable">type Pick<T, K extends keyof T> = &#123;
  [P in K]: T[P]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子</p>
<pre><code class="copyable">interface Person &#123;
    name: string
    age: number
    do: () => void
&#125;
type PeopleInfo =  Pick<Person, 'name' | 'age'>// 将name和age两个类型提取出来，不用从新定义类型
const me: Person &#123; name: 'thl', age: 22&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17">4: Exclude<T, U></h6>
<p>此工具是在 T 类型中，去除 T 类型和 U 类型的交集，返回剩余的部分。</p>
<pre><code class="copyable">type Exclude<T, U> = T extends U ? never : T
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子</p>
<pre><code class="copyable">type PersonOne = &#123;
    name: string
    age: number
    sleep: () => void
&#125;
type PersonTwo = &#123;
    name: string
    age: number
    eat: () => void
&#125;

type Person = Exclude<PersonOne, PersonTwo> 
等价于type PersonDo = &#123;
   sleep: () => void
   eat: () => void
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18">5. Omit<T, K></h6>
<p>此工具可认为是适用于键值对对象的 Exclude，它会去除类型 T 中包含 K 的键值对。</p>
<pre><code class="copyable">type Omit = Pick<T, Exclude<keyof T, K>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子</p>
<pre><code class="copyable">type Person = Omit<PersonOne, 'age'>
const me: Person = &#123;
    name: 'thl',
    sleep: () => console.log('i will')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">6. ReturnType</h6>
<p>此工具就是获取 T 类型(函数)对应的返回值类型：</p>
<pre><code class="copyable">type ReturnType<T extends (...args: any) => any>
  = T extends (...args: any) => infer R ? R : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看源码其实有点多，其实可以稍微简化成下面的样子：</p>
<pre><code class="copyable">type ReturnType<T extends func> = T extends () => infer R ? R: any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子</p>
<pre><code class="copyable">function foo(x: string | number): string | number &#123;// Todo&#125;
type FooTyp
e = ReturnType<foo>;  // string | number
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-20">7. Parameters</h6>
<p>此工具就是获取T类型（函数）对应的参数类型</p>
<pre><code class="copyable">type Parameters<T> = T extends (...args:string[]) => any ? string[] : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老规矩举个栗子</p>
<pre><code class="copyable">type Fn = (a: string, b: number) => void
type FnParams = Parameters<Fn>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实还有一些高级类型这里就不一一列举了，有兴趣的可以去逛下官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org" ref="nofollow noopener noreferrer">www.typescriptlang.org</a></p>
<h4 data-id="heading-21">总结</h4>
<p>Ts的使用有很多技巧，我们在日常使用中可能没有那么容易遇到，在我们阅读一些源码的时候就会了解到很多，还有一个需要总结的问题是关于type和interface的区别和我们如何选择的问题，本质上没有什么区别，
从扩展的角度上来看，type比interface好些,使用&可以少些一些代码</p>
<pre><code class="copyable">type Person = &#123;
    name: string
    age: number
&#125;
// 扩展
type NewPerson = Person & &#123;do: () => void&#125;
interface People &#123;
    happyStatus: true
    eat: () => void
&#125;
// 扩展
interface NewPeople extends People &#123;
    name: string
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外 type 有一些 interface 做不到的事情，比如使用 | 进行枚举类型的组合，使用typeof获取定义的类型等等。</p>
<p>不过 interface 有一个比较强大的地方就是可以重复定义添加属性，比如我们需要给window对象添加一个自定义的属性或者方法，那么我们直接基于其 Interface 新增属性就可以了。</p>
<pre><code class="copyable">declare global &#123;
    interface Window &#123; MyNamespace: any; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>个人习惯一般我使用type多一些</p>
<p>以上就是文章的全部内容了，下周周末我可能会继续总结vue源码系列或者分析react中hook的源码，到时候看情况而定把。最近买了一本高程4准备巩固一下基础，勇敢牛牛，不怕困难。</p></div>  
</div>
            