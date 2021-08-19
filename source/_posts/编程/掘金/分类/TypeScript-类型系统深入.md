
---
title: 'TypeScript-类型系统深入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7031'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 23:31:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=7031'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">类型保护</h2>
<p>我们通常在 JavaScript 中通过判断来处理⼀些逻辑，在 TypeScript 中这种条件语句块还有另外⼀ 个特性：根据判断逻辑的结果，缩⼩类型范围（有点类似断⾔），这种特性称为 类型保护 ，触发条件：</p>
<ul>
<li>逻辑条件语句：if else elseif</li>
<li>特定的关键字：typeof instanceof in ....</li>
</ul>
<h3 data-id="heading-1">typeof</h3>
<p>我们知道 typeof 可以返回某个数据的类型，在 TypeScript 在 if 、 else 代码块中能够把 typeof 识别为类型保护，推断出适合的类型</p>
<pre><code class="copyable">function fn(a:string|number)&#123;
    a.substring(1); // 不能保证a就是字符串
    if(typeof a === 'string')&#123;
        a.substring(1);
    &#125;else&#123;
        a.toFixed(1)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">instanceof</h3>
<p>与typeof类似，instanceof也可以被TypeScript识别为类型保护</p>
<pre><code class="copyable">function fn(a:Date|Array<any>)&#123;
   
    if(a instanceof Array)&#123;
        a.push(1);
    &#125;else&#123;
        a.getFullYear();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">in</h3>
<p>in 也是一样的</p>
<pre><code class="copyable">interface IA &#123; 
    x: string; 
    y: string; 
&#125; 

interface IB &#123; 
    a: string; 
    b: string; 
&#125;

function fn(arg:IA | IB)&#123;
    if('x' in arg)&#123;
        arg.x; //ok
        arg.a; //error
    &#125;else&#123;
        arg.a; //ok
        arg.x; //error
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">字面量类型保护</h3>
<p>如果类型为字面量类型，那么还可以通过该字面量类型的字面值进行推断</p>
<pre><code class="copyable">interface IA &#123; 
    type: 'IA'; 
    x: string; 
    y: string; 
&#125; 
interface IB &#123; 
    type: 'IB'; 
    a: string; 
    b: string; 
&#125; 
function fn(arg: IA | IB) &#123; 
    if (arg.type === 'IA') &#123; 
        // ok 
        arg.x; 
        // error 
        arg.a; 
    &#125; else &#123; 
        // ok 
        arg.a; 
        // error 
        arg.x; 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">自定义类型保护</h3>
<p>有时候，以上方式都不能满足一些特殊情况，我们可以自定义类型保护的规则</p>
<pre><code class="copyable">function canEach(data:any):data is Element[] | NodeList&#123;
    return data.forEach !== undefined;
&#125;

function fn(elements:Element[]|NodeList|Element)&#123;
    if(canEach(elements))&#123;
        elements.forEach((el:Element)=>&#123;
            el.classList.add('box')
        &#125;);
    &#125;else&#123;
        elements.classList.add('box')
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>data is Element[]|NodeList 是⼀种类型谓词，格式为： xx is XX ，返回这种类型的函数就可以 被 TypeScript 识别为类型保护</p>
<h2 data-id="heading-6">类型操作</h2>
<p>TypeScript 提供了⼀些⽅式来操作类型这种数据，但是需要注意的是，类型数据只能作为类型来使⽤，⽽不能作为程序中的数据，这是两种不同的数据，⼀个⽤在编译检测阶段，⼀个⽤于程序执⾏阶段</p>
<h3 data-id="heading-7">typeof</h3>
<p>在TypeScript中,typeof有两种作用：</p>
<ul>
<li>获取数据的类型</li>
<li>捕获数据的类型</li>
</ul>
<pre><code class="copyable">let str = 'str'

// 如果是 let 把 'string' 作为值
lte t = typeof str;
// 如果是 type，把 'string' 作为类型
type strType = typeof str;

let str2: strType = 'str'; 
let str3: typeof str1 = 'str';
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">key of</h3>
<p>获取类型的所有 key 集合</p>
<pre><code class="copyable">interface Person &#123; 
    name: string; 
    age: number
&#125;
type personKeys = keyof Person; 
// 等同：type personKeys = "name" | "age" 

let p1 = &#123; name: 'zMouse', age: 35 &#125; 

function getPersonVal(k: personKeys) &#123; 
    return p1[k]; 
&#125; 

/** 等同： 
    function getPersonVal(k: 'name'|'age') &#123; 
        return p1[k]; 
    &#125; 
*/ 

getPersonVal('name'); //正确 
getPersonVal('gender'); //错误

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">in</h3>
<p>针对类型进行操作的话，内部使用的for...in对类型进行遍历</p>
<pre><code class="copyable">interface Person &#123; 
    name: string; 
    age: number; 
&#125; 
type personKeys = keyof Person; 
type newPerson = &#123; [k in personKeys]: number; 
    /** 等同 
        [k in 'name'|'age']: number; 
   也可以写成 
        [k in keyof Person]: number; */ 
&#125; 
/** 
    type newPerson = &#123; name: number; age: number; &#125; 
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意： in 后⾯的类型值必须是 string 或者 number 或者 symbol</strong></p>
<h2 data-id="heading-10">类型兼容</h2>
<p>TypeScript 的类型系统是基于结构⼦类型的，它与名义类型（如：java）不同（名义类型的数据类型 兼容性或等价性是通过明确的声明或类型的名称来决定的）。这种基于结构⼦类型的类型系统是基于组 成结构的，只要具有相同类型的成员，则两种类型即为兼容的。</p>
<pre><code class="copyable">class Person &#123; 
    name: string; 
    age: number; 
&#125; 

class Cat &#123;
    name: string; 
    age: number; 
&#125;

function fn(p: Person) &#123; 
    p.name; 
&#125; 

let xiaohua = new Cat(); // ok，

因为 Cat 类型的结构与 Person 类型的结构相似，所以它们是兼容的 
fn(xiaohua);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            