
---
title: 'TS 高级类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=865'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 23:18:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=865'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">交叉类型</h4>
<pre><code class="hljs language-js copyable" lang="js">T & U
示例：
type IPerson &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
&#125;

type IMan &#123;
  <span class="hljs-attr">love</span>: string;
  age: number;
&#125;
type mixin = IPerson & IMan
<span class="hljs-comment">//&#123;</span>
<span class="hljs-comment">//  name: string;</span>
<span class="hljs-comment">//  age: number;</span>
<span class="hljs-comment">//  love: string;</span>
<span class="hljs-comment">//&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">联合类型</h4>
<pre><code class="hljs language-js copyable" lang="js">T | U

interface IPerson &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
&#125;

interface IMan &#123;
  <span class="hljs-attr">love</span>: string;
  age: number;
&#125;

type me = IPerson | IMan;
<span class="hljs-comment">//&#123;</span>
<span class="hljs-comment">//  age: number;</span>
<span class="hljs-comment">//&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">类型断言/类型保护</h4>
<pre><code class="hljs language-js copyable" lang="js">断言 <span class="hljs-keyword">as</span>
保护 is
interface IPerson &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isIPerson</span>(<span class="hljs-params">obj: IPerson | IMan</span>): <span class="hljs-title">obj</span> <span class="hljs-title">is</span> <span class="hljs-title">IPerson</span> </span>&#123;
  <span class="hljs-keyword">return</span> (obj <span class="hljs-keyword">as</span> IPerson).name !== <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">属性</h4>
<pre><code class="hljs language-js copyable" lang="js">只读属性 readonly
任意属性 any
可选属性 ?
强制解析 ！
interface Person &#123;
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">条件类型</h3>
<pre><code class="hljs language-js copyable" lang="js">Exclude<T, U> -- 从T中剔除可以赋值给U的类型。
Extract<T, U> -- 提取T中可以赋值给U的类型。
NonNullable<T> -- 从T中剔除<span class="hljs-literal">null</span>和<span class="hljs-literal">undefined</span>。
ReturnType<T> -- 获取函数返回值类型。
InstanceType<T> -- 获取构造函数类型的实例类型。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Partial类型</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//将所有类型变成可选</span>

type User = &#123;
    <span class="hljs-attr">id</span>: number,
    <span class="hljs-attr">name</span>: string
&#125;

type PartialUser = MyPartial<User>

<span class="hljs-comment">//PartialUser => &#123;</span>
    id?: number,
    name?: string
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">pick<Type, Keys>函数</h3>
<pre><code class="hljs language-js copyable" lang="js">Pick

<span class="hljs-keyword">const</span> User = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"张三"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;
<span class="hljs-keyword">const</span> nameValue = pick(User, <span class="hljs-string">"name"</span>)<span class="hljs-comment">//胡先生</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Omit</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//找到泛型T中除了K以外的其他属性</span>
type Props = &#123; <span class="hljs-attr">name</span>: string; age: number; visible: boolean &#125;;
type omitTy = Omit<Props, <span class="hljs-string">'age'</span>>;
<span class="hljs-comment">//omitTy => &#123; age: number; visible: boolean&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Record</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//用于构建一个对象类型，将一种类型的属性映射到另一种类型</span>

interface OneTy &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
&#125;

type KeyTy = <span class="hljs-string">"keyone"</span> | <span class="hljs-string">"keytwo"</span> 
type RcTy = Record<KeyTy, OneTy>;

<span class="hljs-comment">// 结果</span>
<span class="hljs-function"><span class="hljs-params">ReTy</span> =></span> &#123;
  <span class="hljs-attr">keyone</span>: &#123;
   <span class="hljs-attr">name</span>: string;
   age: number;
  &#125;,
  <span class="hljs-attr">keytwo</span>: &#123;
   <span class="hljs-attr">name</span>: string;
   age: number;
  &#125;,
&#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Exclude<Type, ExcludedUnion></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//在联合类型中排除一个类型构建新类型</span>
type T1 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>  
<span class="hljs-comment">//type T1 = "c"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Extract</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//类型交集 和Exclude相反</span>
type T2 = Extract<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>,  <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>  
<span class="hljs-comment">//type T2 = "a" | "b"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">ReturnType</h3>
<pre><code class="hljs language-js copyable" lang="js">type T3 = ReturnType<<span class="hljs-function">() =></span> string>;  
<span class="hljs-comment">// type T3 = string</span>
type T4 = ReturnType<<span class="hljs-function">(<span class="hljs-params">s: string</span>) =></span> <span class="hljs-keyword">void</span>>;  
<span class="hljs-comment">// type T4 = void</span>
type T5 = ReturnType<(<T><span class="hljs-function">() =></span> T)>;  
<span class="hljs-comment">// type T5 = &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            