
---
title: 'TypeScript 高级用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6199d040cab4d9f9c5279db7d0918c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 02:45:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6199d040cab4d9f9c5279db7d0918c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>hi，豆皮粉儿们，今天又和大家见面了，本期分享的是由bytedancer“米兰的小铁匠”， 带来的TypeScript高级使用，
适用于对TypeScript已经有所了解或者已经实际用过一段时间的同学，
本文分别从类型、运算符、操作符、泛型的角度来系统介绍常见的TypeScript文章没有好好讲解的功能点，
最后再分享一下作者的实践经历。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6199d040cab4d9f9c5279db7d0918c0~tplv-k3u1fbpfcp-watermark.image" alt="5c6e7105-97d1-46b5-a71f-5958494f9332.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>作者：米兰的小铁匠</p>
</blockquote>
<h2 data-id="heading-0">一、 类型</h2>
<h3 data-id="heading-1"><code>unknown</code></h3>
<p>unknown指的是<strong>不可预先定义的类型</strong>，在很多场景下，它可以替代any的功能同时保留静态检查的能力。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> num: <span class="hljs-built_in">number</span> = <span class="hljs-number">10</span>;
(num <span class="hljs-keyword">as</span> unknown <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).split(<span class="hljs-string">''</span>);          <span class="hljs-comment">// 注意，这里和any一样完全可以通过静态检查</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候unknown的作用就跟any高度类似了，你可以把它转化成任何类型，不同的地方是，在静态编译的时候，unknown不能调用任何方法，而any可以。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> foo: unknown = <span class="hljs-string">'string'</span>;
foo.substr(<span class="hljs-number">1</span>);           <span class="hljs-comment">// Error: 静态检查不通过报错</span>
<span class="hljs-keyword">const</span> bar: <span class="hljs-built_in">any</span> = <span class="hljs-number">10</span>;
bar.substr(<span class="hljs-number">1</span>);                <span class="hljs-comment">// Pass: any类型相当于放弃了静态检查</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unknown的一个使用场景是，避免使用any作为函数的参数类型而导致的静态类型检查bug：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">input: unknown</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(input)) &#123;
    <span class="hljs-keyword">return</span> input.length;    <span class="hljs-comment">// Pass: 这个代码块中，类型守卫已经将input识别为array类型</span>
  &#125;
  <span class="hljs-keyword">return</span> input.length;      <span class="hljs-comment">// Error: 这里的input还是unknown类型，静态检查报错。如果入参是any，则会放弃检查直接成功，带来报错风险</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><code>void</code></h3>
<p>在TS中，void和undefined功能高度类似，可以在逻辑上避免不小心使用了空指针导致的错误</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;          <span class="hljs-comment">// 这个空函数没有返回任何值，返回类型缺省为void</span>
<span class="hljs-keyword">const</span> a = foo();        <span class="hljs-comment">// 此时a的类型定义为void，你也不能调用a的任何属性方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>void和undefined类型最大的区别是，你可以理解为undefined是void的一个子集，当你对函数返回值并不在意时，使用void而不是undefined。举一个React中的实际的例子。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Parent.tsx</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>): <span class="hljs-title">JSX</span>.<span class="hljs-title">Element</span> </span>&#123;
  <span class="hljs-keyword">const</span> getValue = (): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> &#125;;           <span class="hljs-comment">/* 这里函数返回的是number类型 */</span>
  <span class="hljs-comment">// const getValue = (): string => &#123; return 'str' &#125;;        /* 这里函数返回的string类型，同样可以传给子属性 */</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">getValue</span>=<span class="hljs-string">&#123;getValue&#125;</span> /></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Child.tsx</span>
<span class="hljs-keyword">type</span> Props = &#123;
  <span class="hljs-attr">getValue</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>;  <span class="hljs-comment">// 这里的void表示逻辑上不关注具体的返回值类型，number、string、undefined等都可以</span>
&#125;
<span class="hljs-keyword">const</span> Child = <span class="hljs-function">(<span class="hljs-params">&#123; getValue &#125;: Props</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> getValue()&#125;>click<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">never</h3>
<p>never是指没法正常结束返回的类型，一个必定会报错或者死循环的函数会返回这样的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error message'</span>) &#125;  <span class="hljs-comment">// throw error 返回值是never</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;&#125; &#125;  <span class="hljs-comment">// 这个死循环的也会无法正常退出</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>; <span class="hljs-keyword">while</span>(count)&#123; count ++; &#125; &#125;  <span class="hljs-comment">// Error: 这个无法将返回值定义为never，因为无法在静态编译阶段直接识别出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有就是永远没有相交的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> human = <span class="hljs-string">'boy'</span> & <span class="hljs-string">'girl'</span> <span class="hljs-comment">// 这两个单独的字符串类型并不可能相交，故human为never类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过任何类型联合上 never类型，还是原来的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> language = <span class="hljs-string">'ts'</span> | <span class="hljs-built_in">never</span>   <span class="hljs-comment">// language的类型还是'ts'类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于never有如下特性：</p>
<ul>
<li>在一个函数中调用了返回never的函数后，之后的代码都会变成<code>deadcode</code></li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  foo();                  <span class="hljs-comment">// 这里的foo指上面返回never的函数</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>);         <span class="hljs-comment">// Error: 编译器报错，此行代码永远不会执行到</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>无法把其他类型赋给never</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> n: <span class="hljs-built_in">never</span>;
<span class="hljs-keyword">const</span> o: <span class="hljs-built_in">any</span> = &#123;&#125;;
n = o;  <span class="hljs-comment">// Error: 不能把一个非never类型赋值给never类型，包括any</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于never的这个特性有一些很hack的用法和讨论，比如这个知乎下的 <a href="https://www.zhihu.com/question/354601204/answer/888551021" target="_blank" rel="nofollow noopener noreferrer">尤雨溪的回答</a></p>
<h2 data-id="heading-4">二、运算符</h2>
<h3 data-id="heading-5">非空断言运算符 !</h3>
<p>这个运算符可以用在变量名或者函数名之后，用来强调对应的元素是非null|undefined的</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onClick</span>(<span class="hljs-params">callback?: () => <span class="hljs-built_in">void</span></span>) </span>&#123;
  callback!();                <span class="hljs-comment">// 参数是可选入参，加了这个感叹号!之后，TS编译不报错</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看编译后的ES5代码，居然没有做任何防空判断</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onClick</span>(<span class="hljs-params">callback</span>) </span>&#123;
  callback();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个符号的场景，特别适用于我们已经明确知道不会返回空值的场景，从而减少冗余的代码判断，如React的Ref</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>): <span class="hljs-title">JSX</span>.<span class="hljs-title">Elememt</span> </span>&#123;
  <span class="hljs-keyword">const</span> divRef = useRef<HTMLDivElement>();
  useEffect(<span class="hljs-function">() =></span> &#123;
    divRef.current!.scrollIntoView();         <span class="hljs-comment">// 当组件Mount后才会触发useEffect，故current一定是有值的</span>
  &#125;, []);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;divRef&#125;</span>></span>Demo<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">可选链运算符 ?.</h3>
<p>相比上面!作用于编译阶段的非空判断，<code>?.</code>这个是开发者最需要的运行时(当然编译时也有效)的非空判断</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">obj?.prop    obj?.[index]    func?.(args)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>?.用来判断左侧的表达式是否是null | undefined，如果是则会停止表达式运行，可以减少我们大量的&&运算</p>
<p>比如我们写出<code>a?.b</code>时，编译器会自动生成如下代码</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">a === <span class="hljs-literal">null</span> || a === <span class="hljs-built_in">void</span> <span class="hljs-number">0</span> ? <span class="hljs-built_in">void</span> <span class="hljs-number">0</span> : a.b;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里涉及到一个小知识点: <code>undefined</code>这个值在非严格模式下会被重新赋值，使用<code>void 0</code>必定返回真正的undefined</p>
<h3 data-id="heading-7">空值合并运算符 ??</h3>
<p>??与||的功能是相似的，区别在于**??在左侧表达式结果为null或者undefined时，才会返回右侧表达式**</p>
<p>比如我们书写了<code>const b = a ?? 10</code>，生成的代码如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> b = a !== <span class="hljs-literal">null</span> && a !== <span class="hljs-built_in">void</span> <span class="hljs-number">0</span> ? a : <span class="hljs-number">10</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 || 表达式，大家知道的，则对false、''、NaN、0等逻辑空值也会生效，不适于我们做对参数的合并</p>
<h3 data-id="heading-8">数字分隔符_</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> num:<span class="hljs-built_in">number</span> = <span class="hljs-number">1_2_345.6_78_9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_可以用来对长数字做任意的分隔，主要设计是为了便于数字的阅读，编译出来的代码是没有下划线的，请放心食用</p>
<h2 data-id="heading-9">三、操作符</h2>
<h3 data-id="heading-10">键值获取 keyof</h3>
<p>keyof可以获取一个类型所有键值，返回一个联合类型，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">type</span> PersonKey = keyof Person;  <span class="hljs-comment">// PersonKey得到的类型为 'name' | 'age' </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keyof的一个典型用途是限制访问对象的key合法化，因为any做索引是不被接受的</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span> (<span class="hljs-params">p: Person, k: keyof Person</span>) </span>&#123;
  <span class="hljs-keyword">return</span> p[k];  <span class="hljs-comment">// 如果k不如此定义，则无法以p[k]的代码格式通过编译</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结起来keyof的语法格式如下</p>
<pre><code class="copyable">类型 = keyof 类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">实例类型获取 typeof</h3>
<p>typeof 是获取一个对象/实例的类型，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> me: Person = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'gzx'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">16</span> &#125;;
<span class="hljs-keyword">type</span> P = <span class="hljs-keyword">typeof</span> me;  <span class="hljs-comment">// &#123; name: string, age: number | undefined &#125;</span>
<span class="hljs-keyword">const</span> you: <span class="hljs-keyword">typeof</span> me = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'mabaoguo'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">69</span> &#125;  <span class="hljs-comment">// 可以通过编译</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>typeof 只能用在具体的对象上，这与js中的typeof是一致的，并且它会根据左侧值自动决定应该执行哪种行为</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> typestr = <span class="hljs-keyword">typeof</span> me;   <span class="hljs-comment">// typestr的值为"object"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>typeof 可以和keyof一起使用(因为typeof是返回一个类型嘛)，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> PersonKey = keyof <span class="hljs-keyword">typeof</span> me;   <span class="hljs-comment">// 'name' | 'age'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结起来typeof的语法格式如下</p>
<pre><code class="copyable">类型 = typeof 实例对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">遍历属性 in</h3>
<p>in只能用在类型的定义中，可以对枚举类型进行遍历，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 这个类型可以将任何类型的键值转化成number类型</span>
<span class="hljs-keyword">type</span> TypeToNumber<T> = &#123;
  [key <span class="hljs-keyword">in</span> keyof T]: <span class="hljs-built_in">number</span>
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>keyof</code>返回泛型T的所有键枚举类型，<code>key</code>是自定义的任何变量名，中间用<code>in</code>链接，外围用<code>[]</code>包裹起来(这个是固定搭配)，冒号右侧<code>number</code>将所有的<code>key</code>定义为<code>number</code>类型。</p>
<p>于是可以这样使用了</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> obj: TypeToNumber<Person> = &#123; <span class="hljs-attr">name</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">10</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结起来in的语法格式如下</p>
<pre><code class="copyable">[ 自定义变量名 in 枚举类型 ]: 类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">四、泛型</h2>
<p>泛型在TS中可以说是一个非常重要的属性，它承载了从静态定义到动态调用的桥梁，同时也是TS对自己类型定义的元编程。泛型可以说是TS类型工具的精髓所在，也是整个TS最难学习的部分，这里专门分两章总结一下。</p>
<h3 data-id="heading-14">基本使用</h3>
<p>泛型可以用在普通类型定义，类定义、函数定义上，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 普通类型定义</span>
<span class="hljs-keyword">type</span> Dog<T> = &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">type</span>: T &#125;
<span class="hljs-comment">// 普通类型使用</span>
<span class="hljs-keyword">const</span> dog: Dog<<span class="hljs-built_in">number</span>> = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'ww'</span>, <span class="hljs-attr">type</span>: <span class="hljs-number">20</span> &#125;

<span class="hljs-comment">// 类定义</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">type</span>: T;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">type</span>: T</span>)</span> &#123; <span class="hljs-built_in">this</span>.type = <span class="hljs-keyword">type</span>; &#125;
&#125;
<span class="hljs-comment">// 类使用</span>
<span class="hljs-keyword">const</span> cat: Cat<<span class="hljs-built_in">number</span>> = <span class="hljs-keyword">new</span> Cat<<span class="hljs-built_in">number</span>>(<span class="hljs-number">20</span>); <span class="hljs-comment">// 或简写 const cat = new Cat(20)</span>

<span class="hljs-comment">// 函数定义</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swipe</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">value: [T, U]</span>): [<span class="hljs-title">U</span>, <span class="hljs-title">T</span>] </span>&#123;
  <span class="hljs-keyword">return</span> [value[<span class="hljs-number">1</span>], value[<span class="hljs-number">0</span>]];
&#125;
<span class="hljs-comment">// 函数使用</span>
swipe<Cat<<span class="hljs-built_in">number</span>>, Dog<<span class="hljs-built_in">number</span>>>([cat, dog])  <span class="hljs-comment">// 或简写 swipe([cat, dog])</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，如果对一个类型名定义了泛型，那么使用此类型名的时候一定要把泛型类型也写上去。</p>
<p>而对于变量来说，它的类型可以在调用时推断出来的话，就可以省略泛型书写。</p>
<p>泛型的语法格式简单总结如下</p>
<pre><code class="copyable">类型名<泛型列表> 具体类型定义
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">泛型推导与默认值</h3>
<p>上面提到了，我们可以简化对泛型类型定义的书写，因为TS会自动根据变量定义时的类型推导出变量类型，这一般是发生在函数调用的场合的</p>
<pre><code class="copyable">type Dog<T> = &#123; name: string, type: T &#125;

function adopt<T>(dog: Dog<T>) &#123; return dog &#125;;

const dog = &#123; name: 'ww', type: 'hsq' &#125;;  // 这里按照Dog类型的定义一个type为string的对象
adopt(dog);  // Pass: 函数会根据入参类型推断出type为string
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若不适用函数泛型推导，我们若需要定义变量类型则必须指定泛型类型</p>
<pre><code class="copyable">const dog: Dog<string> = &#123; name: 'ww', type: 'hsq' &#125;  // 不可省略<string>这部分
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们想不指定，可以使用泛型默认值的方案</p>
<pre><code class="copyable">type Dog<T = any> = &#123; name: string, type: T &#125;
const dog: Dog = &#123; name: 'ww', type: 'hsq' &#125;
dog.type = 123;    // 不过这样type类型就是any了，无法自动推导出来，失去了泛型的意义
<span class="copy-code-btn">复制代码</span></code></pre>
<p>泛型默认值的语法格式简单总结如下</p>
<pre><code class="copyable">泛型名 = 默认类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">泛型约束</h3>
<p>有的时候，我们可以不用关注泛型具体的类型，如</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fill</span><<span class="hljs-title">T</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">T</span>[] </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(length).fill(value);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数接受一个长度参数和默认值，结果就是生成使用默认值填充好对应个数的数组。我们不用对传入的参数做判断，直接填充就行了，但是有时候，我们需要限定类型，这时候使用<code>extends</code>关键字即可</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">number</span>>(<span class="hljs-params">value: T[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
  value.forEach(<span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;count += v&#125;);
  <span class="hljs-keyword">return</span> count;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样你就可以以<code>sum([1,2,3])</code>这种方式调用求和函数，而像<code>sum(['1', '2'])</code>这种是无法通过编译的</p>
<p>泛型约束也可以用在多个泛型参数的情况</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pick</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params"></span>)</span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的意思是限制了 U 一定是 T 的key类型中的子集，这种用法常常出现在一些泛型工具库中。</p>
<p>extends的语法格式简单总结如下，注意下面的类型既可以是一般意义上的类型也可以是泛型</p>
<pre><code class="copyable">泛型名 extends 类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">泛型条件</h3>
<p>上面提到extends，其实也可以当做一个三元运算符，如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">T <span class="hljs-keyword">extends</span> U? X: Y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里便不限制T一定要是U的子类型，如果是U子类型，则将T定义为X类型，否则定义为Y类型。</p>
<p>注意，生成的结果是<strong>分配式的</strong>。</p>
<p>举个例子，如果我们把X换成T，如此形式：<code>T extends U? T: never</code></p>
<p>此时返回的T，是满足原来的T中包含U的部分，可以理解为T和U的<strong>交集</strong></p>
<p>所以，extends的语法格式可以扩展为</p>
<pre><code class="copyable">泛型名A extends 类型B ? 类型C: 类型D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">泛型推断 infer</h3>
<p>infer的中文是“推断”的意思，一般是搭配上面的泛型条件语句使用的，所谓推断，就是你不用预先指定在泛型列表中，在运行时会自动判断，不过你得先预定义好整体的结构。举个例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Foo<T> = T <span class="hljs-keyword">extends</span> &#123;<span class="hljs-attr">t</span>: infer Test&#125; ? Test: <span class="hljs-built_in">string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首选看extends后面的内容，<code>&#123;t: infer Test&#125;</code>可以看成是一个包含<code>t属性</code>的<strong>类型定义</strong>，这个<code>t属性</code>的value类型通过<code>infer</code>进行推断后会赋值给<code>Test</code>类型，如果泛型实际参数符合<code>&#123;t: infer Test&#125;</code>的定义那么返回的就是<code>Test</code>类型，否则默认给缺省的<code>string</code>类型。</p>
<p>举个例子加深下理解</p>
<pre><code class="copyable">type One = Foo<number>  // string，因为number不是一个包含t的对象类型
type Two = Foo<&#123;t: boolean&#125;>  // boolean，因为泛型参数匹配上了，使用了infer对应的type
type Three = Foo<&#123;a: number, t: () => void&#125;> // () => void，泛型定义是参数的子集，同样适配
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>infer</code>用来对满足的泛型类型进行子类型的抽取，有很多高级的泛型工具也巧妙的使用了这个方法。</p>
<h2 data-id="heading-19">五、泛型工具</h2>
<h3 data-id="heading-20">Partical<T></h3>
<p>此工具的作用就是将泛型中全部属性变为可选的</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Partial<T> = &#123;
        [key <span class="hljs-keyword">in</span> keyof T]?: T[P]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个例子，这个类型定义在下面也会用到</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Animal = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">category</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
  <span class="hljs-attr">eat</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">number</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用Partical包裹一下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> PartOfAnimal = Partical<Animal>;
<span class="hljs-keyword">const</span> ww: PartOfAnimal = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'ww'</span> &#125;; <span class="hljs-comment">// 属性全部可选后，可以只赋值部分属性了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">Record<K, T></h3>
<p>此工具的作用是将K中所有属性值转化为T类型，我们常用它来申明一个普通object对象</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Record<K <span class="hljs-keyword">extends</span> keyof <span class="hljs-built_in">any</span>,T> = &#123;
  [key <span class="hljs-keyword">in</span> K]: T
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里特别说明一下，<code>keyof any</code>对应的类型为<code>number | string | symbol</code>，也就是可以做对象键(专业说法叫索引index)的类型集合。</p>
<p>举个例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> obj: Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>> = &#123; <span class="hljs-string">'name'</span>: <span class="hljs-string">'xiaoming'</span>, <span class="hljs-string">'tag'</span>: <span class="hljs-string">'三好学生'</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">Pick<T, K></h3>
<p>此工具的作用是将T类型中的K键列表提取出来，生成新的子键值对类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Pick<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
  [P <span class="hljs-keyword">in</span> K]: T[P]          
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还是用上面的<code>Animal</code>定义，看一下Pick如何使用</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> bird: Pick<Animal, <span class="hljs-string">"name"</span> | <span class="hljs-string">"age"</span>> = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'bird'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">1</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">Exclude<T, U></h3>
<p>此工具是在T类型中，去除T类型和U类型的交集，返回剩余的部分</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Exclude<T, U> = T <span class="hljs-keyword">extends</span> U ? <span class="hljs-built_in">never</span> : T
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里的extends返回的T是原来的T中和U无交集的属性，而任何属性联合never都是自身，具体可在上文查阅。</p>
<p>举个例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T1 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>;   <span class="hljs-comment">// "c"</span>
<span class="hljs-keyword">type</span> T2 = Exclude<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>; <span class="hljs-comment">// string | number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">Omit<T, K></h3>
<p>此工具可认为是适用于键值对对象的Exclude，它会去除类型T中包含K的键值对</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Omit = Pick<T, Exclude<keyof T, K>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在定义中，第一步先从T的key中去掉与K重叠的key，接着使用Pick把T类型和剩余的key组合起来即可</p>
<p>还是用上面的Animal举个例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> OmitAnimal:Omit<Animal, <span class="hljs-string">'name'</span>|<span class="hljs-string">'age'</span>> = &#123; <span class="hljs-attr">category</span>: <span class="hljs-string">'lion'</span>, <span class="hljs-attr">eat</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'eat'</span>) &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，Omit与Pick得到的结果完全相反，一个是取非结果，一个取交结果。</p>
<h3 data-id="heading-25">ReturnType<T></h3>
<p>此工具就是获取T类型(函数)对应的返回值类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> ReturnType<T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>> 
  = T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => infer R ? R : <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看源码其实有点多，其实可以稍微简化成下面的样子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> ReturnType<T <span class="hljs-keyword">extends</span> func> = T <span class="hljs-keyword">extends</span> () => infer R ? R: <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过使用infer推断返回值类型，然后返回此类型，如果你彻底理解了infer的含义，那这段就很好理解</p>
<p>举个例子</p>
<pre><code class="copyable">function foo(x: string | number): string | number &#123; /*..*/ &#125;
type FooType = ReturnType<foo>;  // string | number
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">Required<T></h3>
<p>此工具可以将类型T中所有的属性变为必选项</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Required<T> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]-?: T[P]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有一个很有意思的语法<code>-?</code>，你可以理解为就是TS中把?可选属性减去的意思。</p>
<p>除了这些以外，还有很多的内置的类型工具，可以参考<a href="https://www.typescriptlang.org/docs/handbook/utility-types.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript Handbook</a>获得更详细的信息，同时Github上也有很多第三方类型辅助工具，如<a href="https://github.com/piotrwitek/utility-types" target="_blank" rel="nofollow noopener noreferrer">utility-types</a>等。</p>
<h2 data-id="heading-27">六、项目实战</h2>
<p>这里分享一些我个人的想法，可能也许会比较片面甚至错误，欢迎大家积极留言讨论</p>
<h3 data-id="heading-28">Q: 偏好使用interface还是type来定义类型？</h3>
<p>A: 从用法上来说两者本质上没有区别，大家使用React项目做业务开发的话，主要就是用来定义Props以及接口数据类型。</p>
<p>但是从扩展的角度来说，type比interface更方便拓展一些，假如有以下两个定义</p>
<pre><code class="copyable">type Name = &#123; name: string &#125;;
interface IName &#123; name: string &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想要做类型的扩展的话，type只需要一个<code>&</code>，而interface要多写不少代码</p>
<pre><code class="copyable">type Person = Name & &#123; age: number &#125;;
interface IPerson extends IName &#123; age: number &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外type有一些interface做不到的事情，比如使用<code>|</code>进行枚举类型的组合，使用<code>typeof</code>获取定义的类型等等。</p>
<p>不过interface有一个比较强大的地方就是可以重复定义添加属性，比如我们需要给<code>window</code>对象添加一个自定义的属性或者方法，那么我们直接基于其Interface新增属性就可以了。</p>
<pre><code class="copyable">declare global &#123;
    interface Window &#123; MyNamespace: any; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总体来说，大家知道TS是类型兼容而不是类型名称匹配的，所以一般不需用面向对象的场景或者不需要修改全局类型的场合，我一般都是用type来定义类型。</p>
<h3 data-id="heading-29">Q: 是否允许any类型的出现</h3>
<p>A: 说实话，刚开始使用TS的时候还是挺喜欢用any的，毕竟大家都是从JS过渡过来的，对这种影响效率的代码开发方式并不能完全接受，因此不管是出于偷懒还是找不到合适定义的情况，使用any的情况都比较多。</p>
<p>随着使用时间的增加和对TS学习理解的加深，逐步离不开了TS带来的类型定义红利，不希望代码中出现any，所有类型都必须要一个一个找到对应的定义，甚至已经丧失了裸写JS的勇气。</p>
<p>这是一个目前没有正确答案的问题，总是要在效率和时间等等因素中找一个最适合自己的平衡。不过我还是推荐使用TS，随着前端工程化演进和地位的提高，强类型语言一定是多人协作和代码健壮最可靠的保障之一，多用TS，少用any，也是前端界的一个普遍共识。</p>
<h3 data-id="heading-30">Q: 类型定义文件(.d.ts)如何放置</h3>
<p>A: 这个好像业界也没有特别统一的规范，我的想法如下：</p>
<ul>
<li>临时的类型，直接在使用时定义</li>
</ul>
<p>如自己写了一个组件内部的Helper，函数的入参和出参只供内部使用也不存在复用的可能，可以直接在定义函数的时候就在后面定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">format</span>(<span class="hljs-params">input: &#123;k: <span class="hljs-built_in">string</span>&#125;[]</span>): <span class="hljs-title">number</span>[] </span>&#123; <span class="hljs-comment">/***/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>组件个性化类型，直接定义在ts(x)文件中</li>
</ul>
<p>如AntD组件设计，每个单独组件的Props、State等专门定义了类型并export出去</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Table.tsx</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TableProps = &#123; <span class="hljs-comment">/***/</span> &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ColumnProps = &#123; <span class="hljs-comment">/***/</span> &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Table</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">/***/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样使用者如果需要这些类型可以通过import type的方式引入来使用。</p>
<ul>
<li>范围/全局数据，定义在.d.ts文件中</li>
</ul>
<p>全局类型数据，这个大家毫无异议，一般根目录下有个typings文件夹，里面会存放一些全局类型定义。</p>
<p>假如我们使用了css module，那么我们需要让TS识别.less文件(或者.scss)引入后是一个对象，可以如此定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.less'</span> &#123;
  <span class="hljs-keyword">const</span> resource: &#123; [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> &#125;;
  <span class="hljs-keyword">export</span> = resource;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而对于一些全局的数据类型，如后端返回的通用的数据类型，我也习惯将其放在typings文件夹下，使用Namespace的方式来避免名字冲突，如此可以节省组件import类型定义的语句</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-keyword">namespace</span> EdgeApi &#123;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> Department &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-built_in">string</span>;
    gmt_create: <span class="hljs-built_in">string</span>;
    gmt_modify: <span class="hljs-built_in">string</span>;
    id: <span class="hljs-built_in">number</span>;
    name: <span class="hljs-built_in">string</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，每次使用的时候，只需要<code>const department: EdgeApi.Department</code>即可，节省了不少导入的精力。开发者只要能约定规范，避免命名冲突即可。</p>
<blockquote>
<p>关于TS用法的总结就结束到这里，感谢大家的观看~</p>
</blockquote>
<p>数据平台前端团队，在公司内负责风神、TEA、Libra、Dorado等大数据相关产品的研发。我们在前端技术上保持着非常强的热情，除了数据产品相关的研发外，在数据可视化、海量数据处理优化、web excel、WebIDE、私有化部署、工程工具都方面都有很多的探索和积累，有兴趣可以与我们联系。</p></div>  
</div>
            