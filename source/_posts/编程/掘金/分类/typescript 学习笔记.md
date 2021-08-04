
---
title: 'typescript 学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15a81c4a324e4cd99c7f643776adeff3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 22:29:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15a81c4a324e4cd99c7f643776adeff3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15a81c4a324e4cd99c7f643776adeff3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>记录和学习下<code>ts</code>的基本使用和以供后续排查问题和作为参考手册，单纯看文档比较枯燥，记录一下简单的上手使用的点。</p>
<h1 data-id="heading-0">安装</h1>
<pre><code class="hljs language-js copyable" lang="js">npm install -g typescript
yarn <span class="hljs-built_in">global</span> add typescrpt

mkdir tsproject && cd tsproject && touch index.ts >> echo <span class="hljs-string">"console.log(1)"</span>

<span class="hljs-comment">// 手动编译这个文件</span>
tsc index.ts

<span class="hljs-comment">// 初始化ts项目配置文件</span>
tsc --init

<span class="hljs-comment">// 修改 tsconfig.json</span>
 <span class="hljs-string">"outDir"</span>: <span class="hljs-string">"./src"</span>, 

<span class="hljs-comment">// 或vscode 终端 > 运行任务 > ts > tsconfig.json</span>
tsc -w 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ts</code> 的核心功能就是四个字：<strong>类型约束</strong>。</p>
<h1 data-id="heading-1">核心功能</h1>
<h2 data-id="heading-2">数据类型</h2>
<p>原始数据类型包括：<strong>布尔值、数值、字符串、null、undefined</strong> 以及 <code>ES6</code> 中的新类型 <code>Symbol</code> 和 <code>ES10</code> 中的新类型 <code>BigInt</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 布尔</span>
<span class="hljs-keyword">var</span> flag: <span class="hljs-built_in">Boolean</span> = <span class="hljs-literal">true</span>;

<span class="hljs-comment">// number</span>
<span class="hljs-keyword">var</span> num1: <span class="hljs-built_in">Number</span> = <span class="hljs-number">100</span>;
<span class="hljs-keyword">var</span> num2: <span class="hljs-built_in">Number</span> = <span class="hljs-number">12.3</span>;

<span class="hljs-comment">// string</span>
<span class="hljs-keyword">var</span> str1: <span class="hljs-built_in">String</span> = <span class="hljs-string">"anikin"</span>;

<span class="hljs-keyword">let</span> myFavoriteNumber = <span class="hljs-string">'seven'</span>;
myFavoriteNumber = <span class="hljs-number">7</span>;  <span class="hljs-comment">// 会报错，类型推论，等价于let myFavoriteNumber: string = 'seven';</span>

<span class="hljs-comment">// array</span>
<span class="hljs-keyword">var</span> arr1: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">var</span> arr2: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]; <span class="hljs-comment">// 泛型</span>
<span class="hljs-keyword">var</span> arr3: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>] = [<span class="hljs-string">"anikin"</span>, <span class="hljs-number">100</span>]; <span class="hljs-comment">// 元组类型</span>

<span class="hljs-comment">// enum 枚举类型：将变量的值一一列举出来，变量的取值只限于这些范围</span>
<span class="hljs-built_in">enum</span> Flag &#123;
  <span class="hljs-keyword">default</span>, <span class="hljs-comment">// 默认值是index或者是上一个值+1  0</span>
  success = <span class="hljs-number">1</span>,
  error = -<span class="hljs-number">1</span>,
  last, <span class="hljs-comment">// 0</span>
&#125;
<span class="hljs-keyword">var</span> f1: Flag = Flag.success;
<span class="hljs-comment">// console.log(Flag.default, Flag.last);</span>

<span class="hljs-built_in">enum</span> Days &#123;Sun, Mon, Tue, Wed, Thu, Fri, Sat&#125;;
<span class="hljs-comment">// Days['Sun'] = 0;</span>

<span class="hljs-comment">// any 用处</span>
<span class="hljs-keyword">var</span> box:<span class="hljs-built_in">any</span> = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"app"</span>);
box.style.color = <span class="hljs-string">"red"</span>;

<span class="hljs-comment">// undefined || null</span>
<span class="hljs-keyword">var</span> usrinfo: <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">var</span> num3: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
num3 = <span class="hljs-number">100</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">函数</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 函数声明（Function Declaration）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">show</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;&#125; <span class="hljs-comment">// 无返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">conso</span>(<span class="hljs-params">name: <span class="hljs-built_in">String</span>, age: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>===<span class="hljs-subst">$&#123;age&#125;</span>`</span>;
&#125;

<span class="hljs-comment">// 函数表达式（Function Expression）</span>
<span class="hljs-keyword">const</span> myAdd2 = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>) =></span> x + y;

<span class="hljs-comment">// 匿名</span>
<span class="hljs-keyword">var</span> getInfo = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;&#125;;

<span class="hljs-comment">// 可选参数 age 是可选参数</span>
<span class="hljs-comment">// 可选必须放到最后面</span>
<span class="hljs-comment">// name 是默认参数, 默认参数也是可选参数，如果不是最后一位的还需传参</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">conso2</span>(<span class="hljs-params">name: <span class="hljs-built_in">String</span> = <span class="hljs-string">"zhangsan"</span>, age?: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>===<span class="hljs-subst">$&#123;age&#125;</span>`</span>;
&#125;


<span class="hljs-comment">// 实现函数求和  ...rest:number[] 展开的数组</span>
<span class="hljs-comment">// 剩余参数 init = 1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">initValue: <span class="hljs-built_in">number</span>, ...rest: <span class="hljs-built_in">number</span>[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">var</span> res = initValue;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < rest.length; index++) &#123;
    res += rest[index];
  &#125;
  <span class="hljs-keyword">return</span> res;
&#125;
<span class="hljs-comment">//  add(1,2,3,4,5) </span>

<span class="hljs-comment">// 重载允许一个函数接受不同数量或类型的参数时，作出不同的处理。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span></span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span></span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span></span>): <span class="hljs-title">number</span> | <span class="hljs-title">string</span> | <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(x.toString().split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>));
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> x.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">类</h2>
<p>修饰符：</p>
<ul>
<li><code>public</code> 修饰的属性或方法是公有的，可以在任何地方被访问到，属性和方法默认。</li>
<li><code>private</code> 修饰的属性或方法是私有的，不能在声明它的类的外部访问。</li>
<li><code>protected</code> 修饰的属性或方法是受保护的，它和 <code>private</code> 类似，区别是它在子类中也是允许被访问的</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-comment">// 默认是public</span>
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">static</span> ajaxName: <span class="hljs-built_in">string</span> = <span class="hljs-string">"ajaxNameSpace"</span>; <span class="hljs-comment">// 静态属性</span>

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">n: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = n;
  &#125;

  <span class="hljs-comment">// 静态方法可以访问静态属性</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">ajax</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> Person.ajaxName;
  &#125;

  run(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
  &#125;

  <span class="hljs-comment">// 多态： 父级定义接口但是不去实现，而是由集成它的类去实现这个功能</span>
  <span class="hljs-comment">// 每一个子类都有不同的表现</span>
  size(): <span class="hljs-built_in">number</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">private</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">100</span>;
  <span class="hljs-keyword">readonly</span> school = <span class="hljs-string">'北大附小'</span>; <span class="hljs-comment">// 只读属性</span>
  <span class="hljs-comment">// super 相当于调用父的构造函数</span>
  <span class="hljs-comment">// 初始化父类</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">n: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(n);
  &#125;

  <span class="hljs-keyword">protected</span> work(): <span class="hljs-built_in">string</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"work"</span>;
  &#125;

  run(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"child run"</span> + <span class="hljs-built_in">this</span>.work());
  &#125;
&#125;

<span class="hljs-keyword">var</span> c1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">"zhangsan"</span>);

<span class="hljs-comment">// ts 层面无法访问，但是最终都是转义成为es5的话都是可以运行的,记住：ts只是类型约束</span>
<span class="hljs-comment">// console.log(c1.work());</span>
<span class="hljs-comment">// console.log(c1.age);</span>


<span class="hljs-comment">// 抽象类一般是用来定义标准的</span>
<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">National</span> </span>&#123;
  <span class="hljs-comment">// 抽象方法只能出现在抽象类里面，抽象类只能被继承实现，无法直接实例化</span>
  <span class="hljs-keyword">abstract</span> language(): <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">China</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">National</span> </span>&#123;
  <span class="hljs-keyword">public</span> lan: <span class="hljs-built_in">string</span> = <span class="hljs-string">"汉语"</span>;
  <span class="hljs-function"><span class="hljs-title">language</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.lan;
  &#125;
&#125;

<span class="hljs-keyword">var</span> ch = <span class="hljs-keyword">new</span> China();

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">接口</h2>
<p><strong>接口</strong>：行为和动作的规范，对批量的方法进行约束。</p>
<p><strong>和抽象类的区别：</strong></p>
<ul>
<li>抽象类里面可以有方法的实现，但是接口完全都是抽象的，不存在方法的实现；</li>
<li>子类只能继承一个抽象类，而接口可以被多个实现；</li>
<li>抽象方法可以是<code>public</code>，<code>protected</code>，但是接口只能是<code>public</code>，默认的；</li>
<li>抽象类可以有构造器，而接口不能有构造器</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 属性接口 约束json</span>
<span class="hljs-keyword">interface</span> FullName &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-built_in">string</span>;
  secondName: <span class="hljs-built_in">string</span>;
  age?: <span class="hljs-built_in">number</span>;  <span class="hljs-comment">// 可选属性</span>
&#125;

<span class="hljs-keyword">interface</span> ajaxConfig &#123;
  <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>;
  dataType: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>;
  data?: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// 约束函数类型  返回的类型也是 string</span>
<span class="hljs-keyword">interface</span> encrypt &#123;
  (key: <span class="hljs-built_in">string</span>, <span class="hljs-attr">value</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// 类的类型接口  跟抽象类很像</span>
<span class="hljs-keyword">interface</span> Animal &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  eat(n: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">// 接口的继承实现</span>
<span class="hljs-keyword">interface</span> Cattype <span class="hljs-keyword">extends</span> Animal &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
  say(): <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// </span>
<span class="hljs-keyword">interface</span> Light &#123;
    lightOn(): <span class="hljs-built_in">void</span>;
    lightOff(): <span class="hljs-built_in">void</span>;
&#125;


<span class="hljs-comment">// 接口扩展：接口可以继承接口，很好理解，耦合多个接口到实现一个聚合接口</span>
<span class="hljs-keyword">interface</span> Alarm &#123;
    alert(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> LightableAlarm <span class="hljs-keyword">extends</span> Alarm &#123;
    lightOn(): <span class="hljs-built_in">void</span>;
    lightOff(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">// 不使用接口</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printLabel</span>(<span class="hljs-params">labelInfo: &#123; labels: <span class="hljs-built_in">string</span> &#125;</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(labelInfo);
&#125;

<span class="hljs-comment">// 使用接口</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printLabel2</span>(<span class="hljs-params">name: FullName</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"=====printLabel2"</span>, name);
&#125;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">config: ajaxConfig</span>) </span>&#123;
  <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
  xhr.open(config.type, config.url);
  xhr.send(config.data);
  xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(res);
  &#125;;
&#125;


<span class="hljs-comment">// 函数类型的接口</span>
<span class="hljs-comment">// 基于encrypt这个接口，实现加密的函数类型接口</span>
<span class="hljs-keyword">var</span> md5: encrypt = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">key: <span class="hljs-built_in">string</span>, value: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>.btoa(key) + value;
&#125;;


<span class="hljs-comment">// 类实现2个接口</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-title">implements</span> <span class="hljs-title">Animal</span>,<span class="hljs-title">Light</span> </span>&#123;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span> = <span class="hljs-string">"little kitty"</span>;
  eat(food: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">"eat="</span>, food);
  &#125;
   <span class="hljs-function"><span class="hljs-title">lightOn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Car light on'</span>);
   &#125;
   <span class="hljs-function"><span class="hljs-title">lightOff</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Car light off'</span>);
   &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">泛型</h2>
<p><strong>泛型（Generics）</strong> 是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性。</p>
<p><strong>解决类 接口 方法的复用性 以及对不特定数据类型的支持。</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 1: 泛型函数</span>

<span class="hljs-comment">// 同时返回string 和 number 类型 支持多种类型的函数，传入什么类型 返回什么类型</span>
<span class="hljs-comment">// <T> 表示泛型</span>
<span class="hljs-comment">// 泛型和any 相比：有类型校验</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;
<span class="hljs-comment">// getData<number>(100);</span>


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLength</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arr: T[]</span>): <span class="hljs-title">T</span>[] </span>&#123;
  <span class="hljs-built_in">console</span>.log(arr.length); <span class="hljs-comment">// must be exist;</span>
  <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-comment">// getLength<number>([1, 2]);</span>

<span class="hljs-comment">// 1: 泛型类</span>

<span class="hljs-comment">// 实例化的时候传入的这个类型来决定的</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MinClass</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-attr">list</span>: T[] = [];
  add(value: T): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">this</span>.list.push(value);
  &#125;
  min(): T &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list.sort()[<span class="hljs-number">0</span>];
  &#125;
&#125;

<span class="hljs-comment">// var m1 = new MinClass<number>();</span>
<span class="hljs-comment">// m1.add(10);</span>
<span class="hljs-comment">// m1.add(20);</span>
<span class="hljs-comment">// m1.add(2);</span>
<span class="hljs-comment">// m1.add(21);</span>
<span class="hljs-comment">// m1.add(1);</span>
<span class="hljs-comment">// m1.add(9);</span>
<span class="hljs-comment">// console.log(m1.min());</span>

<span class="hljs-comment">// 3: 泛型接口</span>
<span class="hljs-keyword">interface</span> ConfigData &#123;
  <span class="hljs-comment">// (value: string, key: number): string;</span>
  <T>(value: T): T;
&#125;
<span class="hljs-keyword">var</span> gd: ConfigData = <span class="hljs-function"><span class="hljs-keyword">function</span> <<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;;

<span class="hljs-keyword">interface</span> GenericIdentityFn<T> &#123;
  (arg: T): T;
&#125;
<span class="hljs-keyword">var</span> myIdentity: GenericIdentityFn<<span class="hljs-built_in">number</span>> = <span class="hljs-function"><span class="hljs-keyword">function</span> <<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">return</span> arg;
&#125;;

<span class="hljs-comment">/**
 * 实现案例： 把类当做参数约束类型，这样我们就能清楚的知道使用的具体是哪个泛型类型
 */</span>

<span class="hljs-comment">// 定义一个用户类：实现和数据库字段做一个映射</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
  <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  passwd: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">u: <span class="hljs-built_in">string</span>, p: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.username = u;
    <span class="hljs-built_in">this</span>.passwd = p;
  &#125;
&#125;

<span class="hljs-comment">// 文章类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Arcticle</span> </span>&#123;
  <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  desc: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  status?: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">t: <span class="hljs-built_in">string</span>, d: <span class="hljs-built_in">string</span>, s: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.title = t;
    <span class="hljs-built_in">this</span>.desc = d;
    <span class="hljs-built_in">this</span>.status = s;
  &#125;
&#125;

<span class="hljs-comment">// 数据库实现封装类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MysqlDb</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-comment">// 把类当做参数传递</span>
  add(data: T): <span class="hljs-built_in">boolean</span> &#123;
    <span class="hljs-built_in">console</span>.log(data);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
&#125;

<span class="hljs-keyword">var</span> u = <span class="hljs-keyword">new</span> User(<span class="hljs-string">"zhangsan"</span>, <span class="hljs-string">"231231"</span>);
<span class="hljs-keyword">var</span> arc = <span class="hljs-keyword">new</span> Arcticle(<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"吃饭的描述"</span>);

<span class="hljs-comment">// var db = new MysqlDb<User>();</span>
<span class="hljs-keyword">var</span> db = <span class="hljs-keyword">new</span> MysqlDb<Arcticle>();

db.add(arc);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">案例：实现一个mysql和mondb等业务层的封装</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 封装一个mysql 和 mongdb 统一的封装
 */</span>
<span class="hljs-keyword">const</span> store: <span class="hljs-built_in">any</span> = &#123;&#125;;

<span class="hljs-comment">// curd 接口</span>
<span class="hljs-keyword">interface</span> DBI<T> &#123;
  add(data: T): <span class="hljs-built_in">boolean</span>;
  update(d1: T, <span class="hljs-attr">d2</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">boolean</span>;
  <span class="hljs-keyword">delete</span>(d: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">boolean</span>;
  get(id: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">any</span>[];
&#125;

<span class="hljs-comment">// 要实现泛型接口 这类也必须是泛型</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mysql</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">DBI</span><<span class="hljs-title">T</span>> </span>&#123;
  add(data: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">boolean</span> &#123;
    <span class="hljs-built_in">console</span>.log(data);
    <span class="hljs-keyword">let</span> len = <span class="hljs-built_in">Object</span>.keys(store);
    <span class="hljs-keyword">let</span> id = len.length + <span class="hljs-number">1</span>;
    store[id] = data;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
  update(d1: <span class="hljs-built_in">any</span>, <span class="hljs-attr">d2</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">boolean</span> &#123;
   <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
  <span class="hljs-keyword">delete</span>(d: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">boolean</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
  get(id: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">any</span>[] &#123;
    <span class="hljs-keyword">return</span> store[id];
  &#125;
&#125;

<span class="hljs-comment">// 定义一个用户类和数据库做映射</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Users</span> </span>&#123;
  <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
  passwd: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">u: <span class="hljs-built_in">string</span>, p: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.username = u;
    <span class="hljs-built_in">this</span>.passwd = p;
  &#125;
&#125;

<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Users(<span class="hljs-string">"zhangsan"</span>, <span class="hljs-number">123123123</span>);
<span class="hljs-keyword">var</span> p2 = <span class="hljs-keyword">new</span> Users(<span class="hljs-string">"zhaosi"</span>, <span class="hljs-number">11111</span>);

<span class="hljs-keyword">var</span> db2 = <span class="hljs-keyword">new</span> Mysql<Users>();
db2.add(p1);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">命名空间</h2>
<p><strong>命名空间一个最明确的目的就是解决重名问题。</strong></p>
<p><code>/// <reference path = "SomeFileName.ts" /></code>  的方式<code>3.x</code>之后推荐<code>es</code>模块化导出和引入。</p>
<p><code>com.ts</code>:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//  命名空间 当成一个模块</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> A &#123;
  <span class="hljs-keyword">interface</span> Animal &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    eat(): <span class="hljs-built_in">void</span>;
  &#125;

  <span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog2</span> <span class="hljs-title">implements</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">n: <span class="hljs-built_in">string</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.name = n;
    &#125;

    <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"==========dog eat====="</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-title">implements</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">n: <span class="hljs-built_in">string</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.name = n;
    &#125;

    <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"==========cat eat====="</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>index.ts</code>:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; A &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./com"</span>;
<span class="hljs-keyword">var</span> cc = <span class="hljs-keyword">new</span> A.Cat(<span class="hljs-string">"bb"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">装饰器</h2>
<p>随着 <code>TypeScript</code>和<code>ES6</code>里引入了类，在一些场景下我们需要额外的特性来支持标注或修改类及其成员。 装饰器<code>（Decorators）</code>为我们在类的声明及成员上通过元编程语法添加标注提供了一种方式。</p>
<p>若要启用实验性的装饰器特性，你必须在命令行或<code>tsconfig.json</code>里启用<code>experimentalDecorators</code>编译器选项。</p>
<p><strong>装饰器是一种特殊类型的声明，它能够被附加到类声明，方法， 访问符，属性或参数上。</strong>，分为 <strong>普通装饰器</strong>和<strong>装饰器工厂（可传参）</strong>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ts 中装饰器就是一个方法，可以注入类 方法 属性参数</span>

<span class="hljs-comment">// 普通装饰 类装饰器 param:当前的类 Animal</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logClass</span>(<span class="hljs-params">param: <span class="hljs-built_in">any</span></span>) </span>&#123;
  param.prototype.log = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"log===="</span>);
  &#125;;
&#125;
<span class="hljs-meta">@logClass</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>&#123;
&#125;


<span class="hljs-comment">// 装饰器工厂</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">appConfig</span>(<span class="hljs-params">param: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target: <span class="hljs-built_in">any</span></span>) </span>&#123;
    <span class="hljs-comment">// console.log(target); // HttpClient</span>
    <span class="hljs-comment">// console.log(param);  // 手动传的参: http://www.baidu.com/</span>
  &#125;;
&#125;

<span class="hljs-meta">@appConfig</span>(<span class="hljs-string">"http://www.baidu.com/"</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> </span>&#123;
&#125;


<span class="hljs-comment">// 属性装饰器，装饰属性使用。 有两个参数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeUrl</span>(<span class="hljs-params">parm: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-comment">// target 被装饰的类  atrr 被装饰的属性</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target: <span class="hljs-built_in">any</span>, attr: <span class="hljs-built_in">any</span></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(target, attr);
    target[attr] = parm;
  &#125;;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App2</span></span>&#123;
   <span class="hljs-meta">@changeUrl</span>(<span class="hljs-string">"http://git.100tal.com/"</span>)
   <span class="hljs-keyword">public</span> url: <span class="hljs-built_in">any</span> | <span class="hljs-literal">undefined</span>;
&#125;


<span class="hljs-comment">// 方法装饰器: 装饰方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params">param: <span class="hljs-built_in">any</span></span>) </span>&#123;
 <span class="hljs-comment">// fname 函数名称 getData</span>
 <span class="hljs-comment">// target:对象 HttpClient</span>
 <span class="hljs-comment">// desc: configurable: true,enumerable: true,value: ƒ (),writable: true</span>

<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target: <span class="hljs-built_in">any</span>, fname: <span class="hljs-built_in">string</span>, desc: <span class="hljs-built_in">any</span></span>) </span>&#123;    
    <span class="hljs-comment">// 重写了被装饰的函数，被装饰的函数就不是再执行了</span>
    <span class="hljs-keyword">var</span> oMthod = desc.value; <span class="hljs-comment">// === getData</span>
    desc.value = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) </span>&#123;
      <span class="hljs-comment">// args 捕获外面被装饰函数的参数 [100, 200, 300]</span>
      args = args.map(<span class="hljs-function">(<span class="hljs-params">i: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">String</span>(i));
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"xxx"</span>, args);

      <span class="hljs-comment">// 不要重写 而是扩展了之前的方法，这样子两个都会执行</span>
      oMthod.apply(<span class="hljs-built_in">this</span>, args);
    &#125;;
  &#125;;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HttpClient</span> </span>&#123;
  <span class="hljs-keyword">public</span> url: <span class="hljs-built_in">any</span> | <span class="hljs-literal">undefined</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

  <span class="hljs-meta">@get</span>(<span class="hljs-number">100</span>)
  <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"getData==="</span>, <span class="hljs-built_in">this</span>.url);
  &#125;
&#125;

<span class="hljs-keyword">var</span> http: <span class="hljs-built_in">any</span> = <span class="hljs-keyword">new</span> HttpClient();
http.getData(<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            