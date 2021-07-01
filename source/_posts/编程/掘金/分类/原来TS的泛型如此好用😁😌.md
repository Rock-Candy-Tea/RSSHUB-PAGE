
---
title: '原来TS的泛型如此好用😁😌'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2493'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 23:03:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=2493'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在前端开发中，我们不仅要创建一致的定义良好的API，同时也要考虑可重用性。 组件不仅能够支持当前的数据类型，同时也能支持未来的数据类型，这在创建大型系统时为你提供了十分灵活的功能。这时候ts的泛型就起到了关键的作用。</p>
<h2 data-id="heading-0">一：泛型: 基本用法</h2>
<h3 data-id="heading-1">(1): 常规使用</h3>
<p>现在有个需求：封装一个方法，接收一个参数(number类型)，return一个相同类型的result。</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> indentify1 = (args: number): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
       <span class="hljs-keyword">return</span> args;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果接收的类型是number或者string呢？</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> indentify2 = (args: number | string): number | <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
       <span class="hljs-keyword">return</span> args;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果参数类型越来越多怎么处理？泛型可以解决。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> indentify3 = <T>(args: T): <span class="hljs-function"><span class="hljs-params">T</span> =></span> &#123;
        <span class="hljs-keyword">return</span> args;   <span class="hljs-comment">// T类似一个变量保证入参和出参类型一致。</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>泛型起到约束作用。泛型不只可以提供一个。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> indentify4 = <span class="xml"><T, U>(args: T, mes: U): T => &#123;
        return args;  // 提供一个T和U泛型，声明入参类型，指定返回结果类型。
    &#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">(2): 泛型接口</h3>
<p>如上indentify4函数，若是函数返回的是多类型集合，泛型如何处理？</p>
<h4 data-id="heading-3">方法一：返回类型集合</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> indentify5 = <span class="xml"><T, U>(args: T, mes: U): [T,U] => &#123;
        return [args, mes];   // 约束太多，外层对泛型的约束
    &#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">方法二： 泛型接口</h4>
<p>可以提供一个接口，把接口内的参数变为泛型。举个🌰：
定义一个person函数，接收姓名，年龄，性别，是否结婚。最后return。</p>
<pre><code class="hljs language-js copyable" lang="js">    interface IPersonView<T, U, V> &#123;
        <span class="hljs-attr">name</span>: T,
        <span class="hljs-attr">age</span>: U,
        <span class="hljs-attr">sex</span>: T,
        <span class="hljs-attr">isMarray</span>: V
    &#125;
    
    <span class="hljs-keyword">const</span> per = <T, U, V>(name: T, age: U, sex: T, isMarray: V):IPersonView<T, U, V> => &#123;
         let result: IPersonView<T, U, V> = &#123;
             name, age, sex, isMarray
         &#125;
         return result;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出使用泛型接口可以很友好的解决这些问题。便于维护和统一。</p>
<h2 data-id="heading-5">二：常用的操作符</h2>
<h3 data-id="heading-6">(1): extends</h3>
<p>很简单就是继承的意思，让一个类型变量继承我们定义好的类型。在泛型约束中起到了很大的作用。(之后会说到泛型约束）</p>
<h3 data-id="heading-7">(2): keyof</h3>
<p>该操作符可以用于获取某种类型的所有键，其返回类型是联合类型。举个🌰:</p>
<pre><code class="hljs language-js copyable" lang="js">    interface Person &#123;
        <span class="hljs-attr">name</span>: string;
        age: number;
        isMarray: boolean;
    &#125;
    type per1 = keyof Person   <span class="hljs-comment">// string | number | boolean</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三：泛型约束</h2>
<p>有时我们可能希望限制每个类型变量接受的类型数量，这就是泛型约束的作用。起到对类型变量限制作用。</p>
<p>举个🌰：处理字符串或数组时，我们会假设 length 属性是可用的。当我们使用函数并尝试输出参数的长度，会出现一些问题。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> indentify5 = <T>(args: T):<span class="hljs-function"><span class="hljs-params">T</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(args.length);   <span class="hljs-comment">// // 类型“T”上不存在属性“length"</span>
        <span class="hljs-keyword">return</span> args;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出现这个问题的原因是，因为ts编译器不知道，不能识别T上是否含有某个属性。我们可以定义一个类型，让类型变量extends。</p>
<pre><code class="hljs language-js copyable" lang="js">    interface ILength &#123;
        <span class="hljs-attr">length</span>: number   <span class="hljs-comment">// 定义一个接口包含length</span>
    &#125;
    
    <span class="hljs-keyword">const</span> indentify6 = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">T</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">ILength</span>></span>(args: T):T => &#123;
        console.log(args.length);  // number
        return args;
    &#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>当然了：对上面这种情况我们也可以定义数组类型来解决。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> indentify7 = <T>(args: T[]): T[] => &#123;
        <span class="hljs-built_in">console</span>.log(args.length);
        <span class="hljs-keyword">return</span> args;
    &#125;
    
    <span class="hljs-keyword">const</span> indentify8 = <T>(args: <span class="hljs-built_in">Array</span><T>): <span class="hljs-built_in">Array</span><T> => &#123;
        <span class="hljs-built_in">console</span>.log(args.length);
        <span class="hljs-keyword">return</span> args;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以通过keyof来确实对象上的键是否存在。举个🌰：</p>
<pre><code class="hljs language-js copyable" lang="js">    声明一个类型接口。
    interface Ip &#123;
        <span class="hljs-attr">name</span>: string,
        <span class="hljs-attr">sex</span>: string,
        <span class="hljs-attr">age</span>: number
    &#125;
    <span class="hljs-comment">// 通过 keyof 操作符，我们就可以获取指定类型的所有键，之后我们就可以结合extends约束</span>
    <span class="hljs-comment">//即限制输入的属性名包含在 keyof 返回的联合类型中</span>
    
    <span class="hljs-keyword">const</span> indentify9 = <span class="xml"><IPerson, K extends keyof Ip>(obj: Ip , key: K): Ip[k] &#123;
        return obj[key];
    &#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">泛型工具</h2>
<h3 data-id="heading-10">(1):  Partial</h3>
<p>将某个类型里的所有属性变成非必需属性。</p>
<pre><code class="hljs language-js copyable" lang="js">    type Partial<T> = &#123;
        [P <span class="hljs-keyword">in</span> keyof T]?: T[P];   <span class="hljs-comment">// 把！变成？</span>
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个🌰：</p>
<pre><code class="hljs language-js copyable" lang="js">    interface IPerson &#123;
        <span class="hljs-attr">name</span>: string,
        <span class="hljs-attr">age</span>: number
    &#125;
    Partial<IPerson> ===  interface IPerson &#123;
                              name?: string | <span class="hljs-literal">undefined</span>,
                              <span class="hljs-attr">age</span>: number | <span class="hljs-literal">undefined</span>
                          &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">(2): Exclude</h3>
<p><strong>将T中某些属于U的类型移除掉</strong></p>
<pre><code class="hljs language-js copyable" lang="js">     type Exclude<T, U> = T <span class="hljs-keyword">extends</span> U ? never : T; 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">    type T = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span>>   <span class="hljs-comment">// "b" | "c"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">(3): ReturnType</h3>
<p>ReturnType 的作用是用于获取函数 T 的返回类型。</p>
<pre><code class="hljs language-js copyable" lang="js">type T1 = ReturnType<<span class="hljs-function">() =></span> <span class="hljs-built_in">String</span>>  <span class="hljs-comment">// string</span>
type T2 = ReturnType<<span class="hljs-function">(<span class="hljs-params">args: <span class="hljs-built_in">String</span></span>) =></span> <span class="hljs-keyword">void</span>>  <span class="hljs-comment">// void</span>
type T3 = ReturnType<<T><span class="hljs-function">() =></span> T>; <span class="hljs-comment">// &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是一些简单的使用，有不足欢迎大家指出。</p></div>  
</div>
            