
---
title: '我对ts泛型的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37b770bd11784abf9b0cd2eb16df0b39~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:07:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37b770bd11784abf9b0cd2eb16df0b39~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在学习ts源码的时候，发现很多泛型还是看不懂，于是想写一篇文章，总结一下常用的泛型。</p>
<h1 data-id="heading-0">基础必备知识</h1>
<h2 data-id="heading-1">联合类型vs交叉类型</h2>
<pre><code class="copyable">// 联合类型
interface Bird &#123;
  name: string;
  fly(): void;
&#125;
interface Person &#123;
  name: string;
  talk(): void;
&#125;
type BirdPerson = Bird | Person;
let p: BirdPerson = &#123; name: "zfeng", fly() &#123;&#125; &#125;; 
let p1: BirdPerson = &#123; name: "zfeng", talk() &#123;&#125; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>联合类型使用 “｜”表示或的关系， 满足其中的一个情况即可。</p>
<pre><code class="copyable">interface Bird &#123;
  name: string;
  fly(): void;
&#125;
interface Person &#123;
  name: string;
  talk(): void;
&#125;
type BirdPerson = Bird & Person;
let p: BirdPerson = &#123; name: "zhufeng", fly() &#123;&#125;, talk() &#123;&#125; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>交叉类型使用“&”，表示与的关系，需要满足所有的情况。</p>
<p>\</p>
<h2 data-id="heading-2">内置条件类型</h2>
<pre><code class="copyable">type Extract<T, U> = T extends U ? T : never;
type Exclude<T, U> = T extends U ? never : T;
type NonNullable<T> = T extends null | undefined ? never : T;

type N = NonNullable<string | number | null | undefined>;// 删除null和undifined;
type E = Exclude<string | number, string>; // 排除关系 输出 string;
type I = Extract<string | number, string>; // 包含关系 输出 number;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">函数的类型推断</h2>
<h3 data-id="heading-4">获取函数返回值的类型</h3>
<pre><code class="copyable">type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

function getUserInfo(name: string, age: number) &#123;
  return &#123; name, age &#125;;
&#125;
type UserInfo = ReturnType<typeof getUserInfo>;

const userA: UserInfo = &#123;
  name: "zhufeng",
  age: 10,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">获取函数参数的类型</h3>
<pre><code class="copyable">type Parameters<T> = T extends (...args: infer R) => any ? R : any;
function getUserInfo(name: string, age: number) &#123;
  return &#123; name, age &#125;;
&#125;
type T1 = Parameters<typeof getUserInfo>;  // [name: string, age: number]
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">泛型进阶</h1>
<p>很多人对于泛型的理解还停留在基础的层面，我讲站在<strong>集合的视角</strong>去理解一下什么叫泛型。</p>
<p>\</p>
<h2 data-id="heading-7">案例一： 字段的提取</h2>
<p>给定一个接口 Persion, 里面有name,age,visiable,三个字段，现在的<strong>要求是：得到一个新的接口，里面只有name,age。</strong></p>
<p><strong>一般人常见的思路：</strong></p>
<pre><code class="copyable">interface Person &#123;
  name: string;
  age: number;
  visiable: boolean;
&#125;

interface Person1 &#123;
  name: string;
  age: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们从写一个接口，就可以达到要求。但是这样子的写法，显得十分冗余。其实ts提供了方法，让我们可以实现，让我们一起看一下的例子。</p>
<h3 data-id="heading-8">方式一： Pick 提取字段</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37b770bd11784abf9b0cd2eb16df0b39~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">// pick 的原理
// type Pick<T, K extends keyof T> = &#123; [P in K]: T[P] &#125;;
interface Person &#123;
  name: string;
  age: number;
  visiable: boolean;
&#125;
type Person1 = Pick<Person, 'name'|'age'> ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Person1 就包含 name,age 字段。</p>
<h3 data-id="heading-9">方式二：Omit 反向获取</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba70d1a843824dd596e8de94dd09d66c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">interface Person &#123;
  name: string;
  age: number;
  visiable: boolean;
&#125;
type Exclude<T, U> = T extends U ? never : T;
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
type Person2 = Omit<Person, "age">;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\</p>
<h2 data-id="heading-10">案例二： 两个接口的操作</h2>
<p>我们把一个接口当作一个集合，那么两个集合的操作主要有：<strong>并集，交集，差集。</strong></p>
<h3 data-id="heading-11">交集</h3>
<p>\</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc072a3b62ed44ddb90b1e4a3ca83e0d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">type Extract<T, U> = T extends U ? T : never;
type Intersection<T extends object, U extends object> = Pick<
  T,
  Extract<keyof T, keyof U> & Extract<keyof U, keyof T>
>;

type C1 = &#123; name: string; age: number; visible: boolean &#125;;
type C2 = &#123; name: string; age: number; sex: number &#125;;

type C3 = Intersection<C1, C2>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>交集的定义：</strong> <strong>对于给定的两个集合，返回一个包含两个集合中共有元素的新集合。</strong></p>
<p>通过Intersection实现交集，可以获得一个新接口，C3只包含 name.age。如上图。</p>
<p>\</p>
<h3 data-id="heading-12">差集</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062a192a23b8444fae6353dcc2090588~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">type Exclude<T, U> = T extends U ? never : T;
type Diff<T extends object, U extends object> = Pick<
  T,
  Exclude<keyof T, keyof U>
>;

type C1 = &#123; name: string; age: number; visible: boolean &#125;;
type C2 = &#123; name: string; age: number; sex: number &#125;;

type C11 = Diff<C1, C2>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>差集的定义：对于给定的两个集合，返回一个包含所有存在于第一个集合且不存在于第二个集合的元素的新集合。</strong></p>
<p>通过Diff实现差集，可以获得一个新接口，接口只有visiable。如上图。</p>
<h2 data-id="heading-13">并集</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc71b69be35d463bb32d4e9623b518ae~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>\</p>
<p><strong>并集的定义：对于给定的两个集合，返回一个包含两个集合中所有元素的新集合。</strong></p>
<p>通过Merge实现并集，可以获得一个新接口，接口包含C1，C2 的所有属性。如上图。</p>
<pre><code class="copyable">//Compute的作用是将交叉类型合并
type Compute<A extends any> = A extends Function ? A : &#123; [K in keyof A]: A[K] &#125;;
type Omit<T, K> = Pick<T, Exclude<keyof T, K>>;
type Merge<O1 extends object, O2 extends object> = Compute< O1 & Omit<O2, keyof O1>>;
type C1C2 = Merge<C1, C2>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\</p>
<h3 data-id="heading-14">特殊的情况：Overwrite（覆盖）</h3>
<pre><code class="copyable">type C1 = &#123; name: string; age: number; visible: boolean &#125;;
type C2 = &#123; name: string; age: string; sex: number &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>C1,C2做merge, C1中有age,类型为number，C2中有age,类型为string, <strong>那么合并之后，age是string,还是number类型呢？</strong></p>
<hr>
<p><strong>Overwrite 泛型，解决了谁覆盖谁的问题。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f5425a6c0eb42debcfe6b4f77d6f802~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>\</p>
<h3 data-id="heading-15"></h3>
<pre><code class="copyable">type C1 = &#123; name: string; age: number; visible: boolean &#125;;
type C2 = &#123; name: string; age: string; sex: number &#125;;

type Overwrite<
  T extends object,
  U extends object,
  I = Diff<T, U> & Intersection<U, T>
> = Pick<I, keyof I>;
  
type overwrite = Overwrite<C1, C2>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\</p></div>  
</div>
            