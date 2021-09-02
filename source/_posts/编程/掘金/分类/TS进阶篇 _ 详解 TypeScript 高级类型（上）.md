
---
title: 'TS进阶篇 _ 详解 TypeScript 高级类型（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d3273ccda7436a8d1e48fce01825a0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 17:30:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d3273ccda7436a8d1e48fce01825a0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>TypeScript中除了基本类型之外，还定义了很多高级类型，高级类型包括<strong>字面量类型、联合类型、交叉类型、索引类型、映射类型、条件类型、this类型</strong>等。因为内容太多，所以这篇文章先来介绍前三个类型，其余类型会在高级类型的下篇介绍。</p>
<p><strong>系列文章：</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6997202777046777893" target="_blank" title="https://juejin.cn/post/6997202777046777893">TS入门篇 | 为什么学习 TypeScript ？</a></li>
<li><a href="https://juejin.cn/post/6997576373728444446" target="_blank" title="https://juejin.cn/post/6997576373728444446">TS入门篇 | 详解 TypeScript 数据类型</a></li>
<li><a href="https://juejin.cn/post/6998318291420708900" target="_blank" title="https://juejin.cn/post/6998318291420708900">TS入门篇 | 详解 TypeScript 枚举类型</a></li>
<li><a href="https://juejin.cn/post/6998690233067765796" target="_blank" title="https://juejin.cn/post/6998690233067765796">TS入门篇 | 详解 TypeScript 函数类型</a></li>
<li><a href="https://juejin.cn/post/6999804146148704263" target="_blank" title="https://juejin.cn/post/6999804146148704263">TS入门篇 | 详解 TypeScript 接口类型</a></li>
<li><a href="https://juejin.cn/post/7000182870404759589" target="_blank" title="https://juejin.cn/post/7000182870404759589">TS入门篇 | 详解 TypeScript 类类型</a></li>
</ul>
<h2 data-id="heading-0">一、字面量类型</h2>
<p>在 TypeScript 中，字面量不仅可以表示值，还可以表示类型，即所谓的字面量类型。TypeScript 支持 3 种字面量类型：字符串字面量类型、数字字面量类型、布尔字面量类型。对应的字符串字面量、数字字面量、布尔字面量分别拥有与其值一样的字面量类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> str: <span class="hljs-string">'hello world'</span> = <span class="hljs-string">'hello world'</span>;
<span class="hljs-keyword">let</span> num: <span class="hljs-number">996</span> = <span class="hljs-number">996</span>;
<span class="hljs-keyword">let</span> bool: <span class="hljs-literal">true</span> = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1. 字面量类型的使用</h3>
<h4 data-id="heading-2">（1）字符串字面量</h4>
<p>字符串字面量类型其实就是字符串常量，与字符串类型不同的是它是具体的值：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Name = <span class="hljs-string">"TS"</span>;
<span class="hljs-keyword">const</span> name1: Name = <span class="hljs-string">"test"</span>; <span class="hljs-comment">// error 不能将类型"test"分配给类型"TS"</span>
<span class="hljs-keyword">const</span> name2: Name = <span class="hljs-string">"TS"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，定义单个的字面量类型并没有太大用处，它的应用场景是可以把多个字面量类型组合成一个联合类型，用来描述拥有明确成员的实用的集合：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Direction = <span class="hljs-string">"north"</span> | <span class="hljs-string">"east"</span> | <span class="hljs-string">"south"</span> | <span class="hljs-string">"west"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDirectionFirstLetter</span>(<span class="hljs-params">direction: Direction</span>) </span>&#123;
  <span class="hljs-keyword">return</span> direction.substr(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
&#125;
getDirectionFirstLetter(<span class="hljs-string">"test"</span>); <span class="hljs-comment">// error 类型"test"的参数不能赋给类型“Direction”的参数</span>
getDirectionFirstLetter(<span class="hljs-string">"east"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们使用四个字符串字面量类型组合成了一个联合类型，这样编译器就会检查我们使用的参数是否是指定的字面量类型集合中的成员。通过这种方式，可以将函数的参数限定为更具体的类型。这不仅提升了代码的可读性，还保证了函数的参数类型。</p>
<h4 data-id="heading-3">（2）数字字面量</h4>
<p>数字字面量类型和字符串字面量类型差不多，都是指定类型为具体的值：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Age = <span class="hljs-number">18</span>;
<span class="hljs-keyword">interface</span> Info &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: Age;
&#125;
<span class="hljs-keyword">const</span> info: Info = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"TS"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">28</span> <span class="hljs-comment">// error 不能将类型“28”分配给类型“18”</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">（3）布尔字面量</h4>
<p>布尔字面量和上面的两个类似，不在多说：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> success: <span class="hljs-literal">true</span>
<span class="hljs-keyword">let</span> fail: <span class="hljs-literal">false</span>
<span class="hljs-keyword">let</span> value: <span class="hljs-literal">true</span> | <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于布尔值只有true和false两种，所以以下两种类型意思一样的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> value: <span class="hljs-literal">true</span> | <span class="hljs-literal">false</span>
<span class="hljs-keyword">let</span> value: <span class="hljs-built_in">boolean</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. 字面量类型的拓宽</h3>
<p>在ES6中提出了两个新的声明变量的关键字：let和const，那当他们定义的变量的值相同时，变量的类型是一样的吗？
​</p>
<p>先来看使用const定义变量的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"hello world"</span>;
<span class="hljs-keyword">const</span> num = <span class="hljs-number">996</span>;
<span class="hljs-keyword">const</span> bool = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里const定义了三个不能变的常量，在不写类型注解的情况下，TypeScript 会推断出它的类型为赋值字面量的类型。这样就不能再改变变量的值。
​</p>
<p>再来看使用let定义变量的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> str = <span class="hljs-string">"hello world"</span>;
<span class="hljs-keyword">let</span> num = <span class="hljs-number">996</span>;
<span class="hljs-keyword">let</span> bool = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里没有写注解的变量的类型就变成了赋值字面量类型的父类型，比如str的类型是字符串字面量类型"hello world"的父类型string，num的类型是数字字面量类型996的父类型number，bool的类型是布尔字面量类型false的父类型boolean。这样就意味着，我们可以给这三个变量分别赋值string、number、boolean类型的值：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">str = <span class="hljs-string">"hello TypeScript"</span>;
num = <span class="hljs-number">666</span>;
bool = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种<strong>将字面量类型转换为其父类型的设计就是字面量类型的拓宽。</strong> 通过 let 或 var 定义的变量、函数形参、对象的非只读属性，如果指定了初始值且未显式添加类型注解，那么它们推断出来的类型就是指定的初始值字面量类型拓宽后的类型，这就是字面量类型拓宽。
​</p>
<p>下面通过一个例子来理解一下字面量类型拓宽：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'hello'</span>; <span class="hljs-comment">// 类型是 string</span>
<span class="hljs-keyword">let</span> strFun = <span class="hljs-function">(<span class="hljs-params">str = <span class="hljs-string">'hello'</span></span>) =></span> str; <span class="hljs-comment">// 类型是 (str?: string) => string;</span>


<span class="hljs-keyword">const</span> specifiedStr = <span class="hljs-string">'hello'</span>; <span class="hljs-comment">// 类型是 'this is string'</span>
<span class="hljs-keyword">let</span> str2 = specifiedStr; <span class="hljs-comment">// 类型是 'string'</span>
<span class="hljs-keyword">let</span> strFun2 = <span class="hljs-function">(<span class="hljs-params">str = specifiedStr</span>) =></span> str; <span class="hljs-comment">// 类型是 (str?: string) => string;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一段代码中通过let定义了字符串str，是一个形参，并且没有显式的声明其类型，属于是类型拓宽，所以变量和形参推断出类型为string。
​</p>
<p>第二段代码中通过const定义了字符串specifiedStr，这个字符串是常量，不能进行修改，所以specifiedStr的类型为hello字面量类型，后面的str2遍历和strFun2函数形参被赋值了字面量类型的常量，并且没有显式的声明其类型，所以变量、形参的类型都被拓宽了，并没有被指定为它对应的字面量类型。这也是符合我们预期的。</p>
<h2 data-id="heading-6">二、联合类型</h2>
<h3 data-id="heading-7">1. 联合类型的使用</h3>
<p>如果希望属性为多种类型之一，如字符串或者数组，这时联合类型就派上用场了（它使用 | 作为标记，如 string | number）。**联合类型可以理解为多个类型的并集。**联合类型用来表示变量、参数的类型不是某个单一的类型，而可能是多种不同的类型的组合：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatCommandline</span>(<span class="hljs-params">command: <span class="hljs-built_in">string</span>[] | <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> line = <span class="hljs-string">''</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> command === <span class="hljs-string">'string'</span>) &#123;
    line = command.trim();
  &#125; <span class="hljs-keyword">else</span> &#123;
    line = command.join(<span class="hljs-string">' '</span>).trim();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>联合类型表示一个值可以是几种类型之一，用竖线 | 分隔每个类型，所以 number | string | boolean 表示一个值可以是number、string、boolean类型中的任意一种。
​</p>
<p>可以使用类型别名抽离联合类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Command = <span class="hljs-built_in">string</span>[] | <span class="hljs-built_in">string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. 类型缩减</h3>
<p>说完了联合类型的基本使用，那如果定义的联合类型的包含数字类型和数字字面量类型这种情况，会有什么效果呢？实际上，由于数字类型是数字字面量类型的父类型，所以最后会缩减为数字类型。同样string和boolean在这种情况下也会发生类型缩减。
​</p>
<p>看下面的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> UnionNum = <span class="hljs-number">1</span> | <span class="hljs-built_in">number</span>;  <span class="hljs-comment">// 类型是number</span>
<span class="hljs-keyword">type</span> UniomStr = <span class="hljs-string">"string"</span> | <span class="hljs-built_in">string</span>;  <span class="hljs-comment">// 类型是string</span>
<span class="hljs-keyword">type</span> UnionBool = <span class="hljs-literal">false</span> | <span class="hljs-built_in">boolean</span>;   <span class="hljs-comment">// 类型是boolean</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，TypeScript会对类型进行缩减，将字面量类型去掉，保留原始类型。
​</p>
<p>但是这样也会造成一个问题：编译器只能提示我们定义的变量是那个原始的类型：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d3273ccda7436a8d1e48fce01825a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
不过，TypeScript提供了一种方式来控制类型缩减，只需给父类型添加"<strong>& &#123;&#125;</strong>"即可：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe532c695992459f90b615cdcb85a677~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时，其他字面量类型就不会被缩减，在编辑器中字符串字面量str1、str2等就可以自动提示出来了。
​</p>
<p>除此之外，当联合类型的成员是接口类型，并满足其中一个接口的属性是另一个接口属性的子集，这个属性也会进行类型缩减：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> UnionInterface = &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span>
&#125; | &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span> | <span class="hljs-string">"25"</span>,
  [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 <code>"18"</code> 是 <code>"18" | "25"</code> 的子集，所以age属性的类型会变成 <strong>"18" | "25"。</strong></p>
<h3 data-id="heading-9">3. 可辨识联合类型</h3>
<p>可以把单例类型、联合类型、类型保护和类型别名这几种类型进行合并，来创建一个叫做<strong>可辨识联合类型</strong>，它也可称作<strong>标签联合</strong>或<strong>代数数据类型</strong>。
​</p>
<p>所谓单例类型，可以理解为符合单例模式的数据类型，比如枚举成员类型，字面量类型。
​</p>
<p>可辨识联合类型要求具有两个要素：</p>
<ul>
<li>具有普通的单例类型属性。</li>
<li>一个类型别名，包含了那些类型的联合。</li>
</ul>
<p><strong>可辨识联合类型就是为了保证每个case都能被处理。</strong></p>
<p>来看一个例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;    <span class="hljs-comment">// 具有辨识性的属性</span>
  size: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Rectangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"rectangle"</span>; <span class="hljs-comment">// 具有辨识性的属性</span>
  height: <span class="hljs-built_in">number</span>;
  width: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;   <span class="hljs-comment">// 具有辨识性的属性</span>
  radius: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> Shape = Square | Rectangle | Circle; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个例子中，我们的 Shape 即可辨识联合类型，它是三个接口的联合，而这三个接口都有一个 kind 属性，且每个接口的 kind 属性值都不相同，能够起到标识作用。 函数内应该包含联合类型中每一个接口的 case。</p>
<p>如果函数内没有包含联合类型中每一个接口的 case。希望编译器应该给出提示。有以下两种完整性检查的方法：<strong>使用 strictNullChecks</strong>和<strong>使用 never 类型</strong>。</p>
<h4 data-id="heading-10">（1）使用 strictNullChecks</h4>
<p>对上面的例子加一种接口：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
  size: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Rectangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"rectangle"</span>;
  height: <span class="hljs-built_in">number</span>;
  width: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
  radius: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Triangle &#123;
  <span class="hljs-attr">kind</span>: <span class="hljs-string">"triangle"</span>;
  bottom: <span class="hljs-built_in">number</span>;
  height: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">type</span> Shape = Square | Rectangle | Circle | Triangle; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，Shape 联合有四种接口，但函数的 switch 里只包含三个 case，这个时候编译器并没有提示任何错误，因为当传入函数的是类型是 Triangle 时，没有任何一个 case 符合，则不会有 return 语句执行，那么函数是默认返回 undefined。所以可以利用这个特点，结合 strictNullChecks编译选项，可以开启 strictNullChecks，然后让函数的返回值类型为 number，那么当返回 undefined 的时候，就会报错：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">s: Shape</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-comment">// error Function lacks ending return statement and return type does not include 'undefined'</span>
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法简单，但是对旧代码支持不好，因为strictNullChecks这个配置项是2.0版本才加入的，如果使用的是低于这个版本的，这个方法并不会有效。</p>
<h4 data-id="heading-11">（2）使用 never 类型</h4>
<p>当函数返回一个错误或者不可能有返回值的时候，返回值类型为 never。所以可以给 switch 添加一个 default 流程，当前面的 case 都不符合的时候，会执行 default 后的逻辑：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assertNever</span>(<span class="hljs-params">value: <span class="hljs-built_in">never</span></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Unexpected object: "</span> + value);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (s.kind) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>:
      <span class="hljs-keyword">return</span> s.size * s.size;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>:
      <span class="hljs-keyword">return</span> s.height * s.width;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> assertNever(s); <span class="hljs-comment">// error 类型“Triangle”的参数不能赋给类型“never”的参数</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>采用这种方式，需要定义一个额外的 asserNever 函数，但是这种方式不仅能够在编译阶段提示遗漏了判断条件，而且在运行时也会报错。</p>
<h2 data-id="heading-12">三、交叉类型</h2>
<h3 data-id="heading-13">1. 交叉类型的使用</h3>
<p>交叉类型是将多个类型合并为一个类型。 这让我们可以把现有的多种类型叠加到成为一种类型，合并后的类型将拥有所有成员类型的特性。<strong>交叉类型可以理解为多个类型的交集。</strong></p>
<p>可以使用“&”操作符来声明交叉类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Overlapping = <span class="hljs-built_in">string</span> & <span class="hljs-built_in">number</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们仅仅把原始类型、字面量类型、函数类型等原子类型合并成交叉类型，是没有任何意义的，因为不会有变量同时满足这些类型，那这个类型实际上就等于never类型。</p>
<h3 data-id="heading-14">2. 交叉类型的使用场景</h3>
<p>上面说了一般情况下使用交叉类型是没有意义的，那什么时候该使用交叉类型呢？下面就来看看交叉类型的使用场景。</p>
<h4 data-id="heading-15">（1）合并接口类型</h4>
<p>将多个接口类型合并成为一个类型是交叉类型的一个常见的使用场景。这样就能相当于实现了接口的继承，也就是所谓的合并接口类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125; & &#123;
<span class="hljs-attr">height</span>: <span class="hljs-built_in">number</span>;
  weight: <span class="hljs-built_in">number</span>;
&#125; & &#123;
<span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> person: Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"zhangsan"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">height</span>: <span class="hljs-number">180</span>,
  <span class="hljs-attr">weight</span>: <span class="hljs-number">60</span>,
  <span class="hljs-attr">id</span>: <span class="hljs-number">123456</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们通过交叉类型使Person同时拥有了三个接口类型中的5个属性。
​</p>
<p>那如果两个接口中的同一个属性定义了不同的类型会发生了什么情况呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125; & &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">string</span>;
height: <span class="hljs-built_in">number</span>;
  weight: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个接口中都拥有age属性，并且类型分别是number和string，那么在合并后，age的类型就是string & number，就是一个 never 类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125; & &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">string</span>;
height: <span class="hljs-built_in">number</span>;
  weight: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> person: Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"zhangsan"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,   <span class="hljs-comment">// Type 'number' is not assignable to type 'never'.ts(2322)</span>
  <span class="hljs-attr">height</span>: <span class="hljs-number">180</span>,
  <span class="hljs-attr">weight</span>: <span class="hljs-number">60</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果同名属性的类型兼容，比如一个是 number，另一个是 number 的子类型、数字字面量类型，合并后 age 属性的类型就是两者中的子类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125; & &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>;
height: <span class="hljs-built_in">number</span>;
  weight: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> person: Person = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"zhangsan"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,  <span class="hljs-comment">// Type '20' is not assignable to type '18'.ts(2322)</span>
  <span class="hljs-attr">height</span>: <span class="hljs-number">180</span>,
  <span class="hljs-attr">weight</span>: <span class="hljs-number">60</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里第二个接口中的age是一个数字字面量类型，它是number类型的子类型，所以合并之后的类型为字面量类型18。</p>
<h4 data-id="heading-16">（2）合并联合类型</h4>
<p>交叉类型另外一个常见的使用场景就是合并联合类型。可以合并多个联合类型为一个交叉类型，这个交叉类型需要同时满足不同的联合类型限制，也就是提取了所有联合类型的相同类型成员：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> A = <span class="hljs-string">"blue"</span> | <span class="hljs-string">"red"</span> | <span class="hljs-number">996</span>;
<span class="hljs-keyword">type</span> B = <span class="hljs-number">996</span> | <span class="hljs-number">666</span>;
<span class="hljs-keyword">type</span> C = A & B;
<span class="hljs-keyword">const</span> c: C = <span class="hljs-number">996</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果多个联合类型中没有相同的类型成员，那么交叉出来的类型就是never类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> A = <span class="hljs-string">"blue"</span> | <span class="hljs-string">"red"</span>;
<span class="hljs-keyword">type</span> B = <span class="hljs-number">996</span> | <span class="hljs-number">666</span>;
<span class="hljs-keyword">type</span> C = A & B;
<span class="hljs-keyword">const</span> c: C = <span class="hljs-number">996</span>; <span class="hljs-comment">// Type 'number' is not assignable to type 'never'.ts(2322)</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            