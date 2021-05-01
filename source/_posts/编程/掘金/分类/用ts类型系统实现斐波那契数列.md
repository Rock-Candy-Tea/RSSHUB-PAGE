
---
title: '用ts类型系统实现斐波那契数列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9517f7f6c4a147f49b6d4f015d67e348~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 03:10:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9517f7f6c4a147f49b6d4f015d67e348~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">0x00 我们要做什么</h2>
<pre><code class="copyable">const fib = (n: number): number => (n <= 1 ? n : fib(n - 1) + fib(n - 2));

for (let i = 0; i < 10; i++) &#123;
  console.log(i, fib(i));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们获得如下输出, 完结撒花 ✿✿ヽ(°▽°)ノ✿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9517f7f6c4a147f49b6d4f015d67e348~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83adec21012843d58692d33f9f5fd8b4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>然而我们其实真正想这样做↓↓↓, 也就是使用TS Type解决FIbonacci</strong></p>
<pre><code class="copyable">import &#123; Fib, Add &#125; from "./fib-type";

type one = Fib<1>;

type zero = Fib<0>;

type Two = Add<one, one>;

type Five = Add<Two, Add<Two, one>>;

type Fib5 = Fib<Five>;

type Fib9 = Fib<9>;

type r0 = Fib<Zero>; // type r0= 0

type r1 = Fib<One>; // type r1 = 1

type r2 = Fib<Two>; // type r2 = 1

type r3 = Fib<3>; // type r3 = 2

type r4 = Fib<4>; // type r4 = 3

type r5 = Fib<5>; // type r5 = 5

type r6 = Fib<6>; // type r6 = 8

type r9 = Fib<9>; // type r9 = 34

type sum = Add<r9, r6>; // type sum = 42
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ac757fd08b4cfca9bab738129f91a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2d94090281640aca154419ffd8b55e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">1x00 我们该怎么做</h2>
<p>fib中有基本的<strong>比较, 加法, 循环,</strong> 所以我们也需要使用类型系统依次实现</p>
<h3 data-id="heading-2">1x01 加法</h3>
<p>为了实现加法, 需要先实现一些工具类型</p>
<pre><code class="copyable">// 元组长度
type Length<T extends any[]> = T["length"];

type one = 1;

// 使用extends实现数字相等的比较
type a111 = 0 extends one ? true : false; // type a111 = false
type a112 = 1 extends one ? true : false; // type a112 = true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>range的实现是递归实现的</p>
<pre><code class="copyable">function range(n, list = []) &#123;
  if (n <= 0) return list.length;
  return range(n - 1, [1, ...list]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ts的限制, 没有循环, 只能用递归代替循环, 后面会有几个类似的写法, 记住一点, <strong>递归有几个出口, 对象就有几个key, 每个key就是一个条件</strong></p>
<pre><code class="copyable">// 创建指定长度的元组, 用第二个参数携带返回值

type Range<T extends Number = 0, P extends any[] = []> = &#123;
  0: Range<T, [any, ...P]>;
  1: P;
&#125;[Length<P> extends T ? 1 : 0];

// 拼接两个元组
type Concat<T extends any[], P extends any[]> = [...T, ...P];
type t1 = Range<3>;
// type t1 = [any, any, any]
type Zero = Length<Range<0>>;
// type Zero = 0
type Ten = Length<Range<10>>;
// type Ten = 10
type Five = Length<Range<5>>;
// type Five = 5
type One = Length<Range<1>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现加法就比较容易了, 只需要求两个元组合并后的长度</p>
<pre><code class="copyable">type Add<T extends number, P extends number> = Length<
  Concat<Range<T>, Range<P>>
>;

type Two = Add<One, One>;
// type Two = 2
type Three = Add<One, Two>;
// type Three = 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如何实现减法呢？一般减法和除法都比加法难, 所以我们需要更多的工具</p>
<h3 data-id="heading-3">1x02 比较函数</h3>
<h3 data-id="heading-4">一些工具类型</h3>
<ul>
<li>
<p>Shift：删除第一个元素</p>
</li>
<li>
<p>Append：在元组末尾插入元素</p>
</li>
<li>
<p>IsEmpty / NotEmpty：判断列表为空</p>
<p>// 去除元组第一个元素 [1,2,3] -> [2,3]
type Shift<T extends any[]> = ((...t: T) => any) extends (
_: any,
...Shift: infer P
) => any
? P
: [];</p>
<p>type pp = Shift<[number, boolean, string, Object]>;
// type pp = [boolean, string, Object]
// 向元组中追加
type Append<T extends any[], E = any> = [...T, E];
type IsEmpty<T extends any[]> = Length extends 0 ? true : false;
type NotEmpty<T extends any[]> = IsEmpty extends true ? false : true;
type t4 = IsEmpty<Range<0>>;
// type t4 = true
type t5 = IsEmpty<Range<1>>;
// type t5 = false</p>
</li>
</ul>
<h3 data-id="heading-5">逻辑类型</h3>
<ul>
<li>
<p>And：a && b</p>
<p>// 逻辑操作
type And<T extends boolean, P extends boolean> = T extends false
? false
: P extends false
? false
: true;
type t6 = And<true, true>;
// type t6 = true</p>
<p>type t7 = And<true, false>;
// type t7 = false</p>
<p>type t8 = And<false, false>;
// type t8 = false</p>
<p>type t9 = And<false, true>;
// type t9 = false</p>
</li>
</ul>
<h3 data-id="heading-6">小于等于</h3>
<p>伪代码:</p>
<pre><code class="copyable">function dfs(a, b) &#123;
  if (a.length && b.length) &#123;
    a.pop();
    b.pop();
    return dfs(a, b);
  &#125; else if (a.length) &#123;
    a >= b;
  &#125; else if (b.length) &#123;
    b > a;
  &#125;
&#125;
// 元组的小于等于   T <= P, 同时去除一个元素, 长度先到0的比较小

type LessEqList<T extends any[], P extends any[]> = &#123;
  0: LessEqList<Shift<T>, Shift<P>>;
  1: true;
  2: false;
&#125;[And<NotEmpty<T>, NotEmpty<P>> extends true
  ? 0
  : IsEmpty<T> extends true
  ? 1
  : 2];

// 数字的小于等于
type LessEq<T extends number, P extends number> = LessEqList<
  Range<T>,
  Range<P>
>;

type t10 = LessEq<Zero, One>;
// type t10 = true
type t11 = LessEq<One, Zero>;
// type t11 = false
type t12 = LessEq<One, One>;
// type t12 = true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">1x03 减法</h3>
<h3 data-id="heading-8">列表减法</h3>
<p>默认大减小, 小减大只需要判断下反着来, 然后加个符号就行了, 这里为了简单没有实现</p>
<pre><code class="copyable">// 伪代码
const a = [1, 2, 3];
const b = [4, 5];
const c = [];
while (b.length !== a.length) &#123;
  a.pop();
  c.push(1);
&#125;// c.length === a.length - b.lengthconsole.log(c.length);


// 元组的减法 T - P, 同时去除一个元素, 长度到0时, 剩下的就是结果, 这里使用第三个参数来携带结果, 每次做一次减法, 向第三个列表里面追加
type SubList<T extends any[], P extends any[], R extends any[] = []> = &#123;
  0: Length<R>;
  1: SubList<Shift<T>, P, Append<R>>;
&#125;[Length<T> extends Length<P> ? 0 : 1];

type t13 = SubList<Range<10>, Range<5>>;
// type t13 = 5
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">数字减法</h3>
<p>其实只是将数字转成元组后再比较</p>
<pre><code class="copyable">// 集合大小不能为负数, 默认大减小
// 数字的减法
type Sub<T extends number, P extends number> = &#123;
  0: Sub<P, T>;
  1: SubList<Range<T>, Range<P>>;
&#125;[LessEq<T, P> extends true ? 0 : 1];

type t14 = Sub<One, Zero>;
//   type t14 = 1
type t15 = Sub<Ten, Five>;
// type t15 = 5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们有了这些工具后, 就可以将js翻译为ts</p>
<h2 data-id="heading-10">2x00 Fib: JS函数 --> TS类型</h2>
<p>在js中，我们使用函数</p>
<pre><code class="copyable">const fib = (n: number): number => n <= 1 ? n : fib(n - 1) + fib(n - 2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在ts中，我们使用类型, 其实只是换了一种写法, 万变不离其宗~</p>
<pre><code class="copyable">export type Fib<T extends number> = &#123;
  0: T;
  1: Add<Fib<Sub<T, One>>, Fib<Sub<T, Two>>>;
&#125;[LessEq<T, One> extends true ? 0 : 1];

type r0 = Fib<Zero>;
// type r10= 0
type r1 = Fib<One>;
// type r1 = 1

type r2 = Fib<Two>;
// type r2 = 1

type r3 = Fib<3>;
// type r3 = 2

type r4 = Fib<4>;
// type r4 = 3

type r5 = Fib<5>;
//type r5 = 5

type r6 = Fib<6>;
//   type r6 = 8
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我还有很多好玩的想法, 可惜这里地(dian)方(zan)太少写不下了, 你懂得 \(^o^)/~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b886d2acc8274bbab5e1d6a39a8a2f8e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">其他好玩的</h2>
<p><a href="https://zhuanlan.zhihu.com/p/85655537" target="_blank" rel="nofollow noopener noreferrer">TypeScript类型元编程：实现8位数的算术运算</a></p>
<p><a href="https://link.zhihu.com/?target=https%3A//juejin.cn/post/6867785919693832200" target="_blank" rel="nofollow noopener noreferrer">TypeScript 4.1 新特性:字符串模板类型，Vuex 终于有救了?</a></p>
<h2 data-id="heading-12">广告</h2>
<p>字节前端-教育方向, 想来玩的话可以内推</p>
<p>要是有好玩的岗位, 也可以把我带走... (打杂, 搬砖的就算了)</p></div>  
</div>
            