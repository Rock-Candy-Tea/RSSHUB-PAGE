
---
title: '记录TypeScript 的一些基础知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1023'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:30:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=1023'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>下面是TS的一些基础知识，确实有点宽泛，加深自己的理解，之后，还会针对不同的知识点来写文章</p>
<h3 data-id="heading-1">基础类型</h3>
<h4 data-id="heading-2">数组</h4>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> arr1: <span class="hljs-built_in">string</span>[] = [<span class="hljs-string">'123'</span>];

<span class="hljs-keyword">const</span> arr2: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">string</span>> = [<span class="hljs-string">'qwe'</span>];

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">类型断言</h4>
<p>通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。 类型断言好比其它语言里的类型转换，但是不进行特殊的数据检查和解构。 它没有运行时的影响，只是在编译阶段起作用。</p>
<p>有两种方式，一种是尖括号的形式，<类型> xxx,  另一种是as的形式 (xxx as string)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLength</span> (<span class="hljs-params">n: string | number</span>) </span>&#123;
  <span class="hljs-keyword">if</span> ((<string>x).length) &#123;
      <span class="hljs-keyword">return</span> (x <span class="hljs-keyword">as</span> string).length;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> x.toString.length;
      &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">类型推断</h4>
<h3 data-id="heading-5">接口 interface</h3>
<h4 data-id="heading-6">函数类型</h4>
<p>接口除了可以描述普通的对象之外，也可以描述函数类型</p>
<pre><code class="hljs language-js copyable" lang="js">interface SearchFun &#123;
  (source: string, <span class="hljs-attr">str</span>: string): boolean
&#125;
<span class="hljs-comment">// 定义一个函数，该类型就是上面定义的接口</span>
<span class="hljs-keyword">let</span> search: SearchFun = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source: string, str: string</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> source.search(str) > -<span class="hljs-number">1</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">类类型</h4>
<p>总结： 接口和接口之间叫继承， 类和接口之间叫实现</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">interface</span> Fly &#123;
    flys(): <span class="hljs-built_in">void</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TheFly</span> <span class="hljs-title">implements</span> <span class="hljs-title">Fly</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">flys</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
    &#125;
    adb () &#123;
        
    &#125;
&#125;
<span class="hljs-comment">// 2</span>
<span class="hljs-keyword">interface</span> Flys &#123;
  sendFly():<span class="hljs-built_in">void</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> <span class="hljs-title">implements</span> <span class="hljs-title">Fly</span>, <span class="hljs-title">Flys</span> </span>&#123;
  sendFly () &#123;
    
  &#125;
  <span class="hljs-function"><span class="hljs-title">flys</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
  &#125;
&#125;
<span class="hljs-comment">// 定义一个接口，可以继承多个接口</span>
<span class="hljs-keyword">interface</span> MoreFly <span class="hljs-keyword">extends</span> Fly, Flys &#123;
  
&#125;

<span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">类</h2>
<p>类和类之间如果要有继承关系，需要使用extends关键字</p>
<p>子类中可以调用父类中的构造函数，使用的是super关键字</p>
<p>子类中可以重写父类中的方法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// TS 中类的定义和使用</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
  <span class="hljs-title">constructor</span> (<span class="hljs-params">age: <span class="hljs-built_in">number</span> = <span class="hljs-number">12</span></span>) &#123;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'1'</span>;
  &#125;
  sayHi (name: <span class="hljs-built_in">string</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Students</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">age: <span class="hljs-built_in">number</span></span>) &#123;
    <span class="hljs-comment">// 调用父类中的构造函数</span>
    <span class="hljs-built_in">super</span>(age)
  &#125;
  <span class="hljs-comment">// 可以调用父类中的方法</span>
  sayHi () &#123;
      <span class="hljs-built_in">super</span>.sayHi(<span class="hljs-string">'qwe'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">多态</h3>
<p>父类型的引用指向了子类型的对象</p>
<p>不同类型的对象针对相同的方法，产生了不同的行为</p>
<h3 data-id="heading-10">类中成员的修饰符 public private protected readonly</h3>
<p>public 默认的访问修饰符，代表公共的，任何位置都可以访问类中的成员</p>
<p>private修饰符 私有属性，只能在类中使用，不能在类外面使用，特别是子类中也是无法使用的</p>
<p>protected 修饰符，外部是不能使用的，子类中可以使用</p>
<p>readonly 修饰符，对类中的属性进行修饰，但是，不能在外部修改了；但是，构造函数中，可以对只读的属性进行修改</p>
<p>一旦使用readonly进行修饰之后，就有了一个age属性成员</p>
<p>下面的例子，修饰器还可以用在构造函数的参数上</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-attr">name</span>: string
  <span class="hljs-title">constructor</span> (<span class="hljs-params">readonly age: number = <span class="hljs-number">12</span></span>) &#123;
    <span class="hljs-built_in">this</span>.age = age;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'1'</span>;
  &#125;
  sayHi (name: string) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">存取器 get set</h3>
<p>截取对象成员的访问</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-built_in">string</span> = <span class="hljs-string">'liu'</span>
    <span class="hljs-attr">lastName</span>: <span class="hljs-built_in">string</span> = <span class="hljs-string">'yongsheng'</span>

    get fullName () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">'_'</span> + <span class="hljs-built_in">this</span>.lastName;
    &#125;

    set fullName (val) &#123;
        <span class="hljs-keyword">let</span> name = val.split(<span class="hljs-string">'_'</span>);
        <span class="hljs-built_in">this</span>.firstName = name[<span class="hljs-number">0</span>];
        <span class="hljs-built_in">this</span>.lastName = name[<span class="hljs-number">1</span>];
    &#125;
&#125;

<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person();
<span class="hljs-comment">// 注意fullName 不是函数</span>
<span class="hljs-built_in">console</span>.log(p.fullName);

p.fullName = <span class="hljs-string">'abc_qwe'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">静态成员 static</h3>
<p>在类中通过static修饰的属性或者方法</p>
<p>静态成员是通过类名+'.' 的形式来访问的（<code>Person.abc</code>）</p>
<p>这些属性存在于类本身上面而不是实例对象上面</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/*
静态属性，是类对象的属性
非静态属性，是类的实例对象的属性
  static不能出现在构造函数的前面
*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">static</span> name:<span class="hljs-built_in">string</span> = <span class="hljs-string">'lys'</span>
&#125;
<span class="hljs-built_in">console</span>.log(Person.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">抽象类 abstract</h3>
<p>抽象类作为其他派生类的基类使用。</p>
<p>抽象类不能被实例化</p>
<p>抽象类里面的抽象方法，不能有具体的实现</p>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  abstract eat():<span class="hljs-keyword">void</span>
  <span class="hljs-comment">// 报错，不能有具体的实现</span>
  <span class="hljs-comment">// abstract eat():void &#123;</span>
  <span class="hljs-comment">//     console.log('eat');</span>
  <span class="hljs-comment">// &#125;</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-comment">// 重新实现抽象类中的方法</span>
    eat () &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'111'</span>);
    &#125;
&#125;
<span class="hljs-comment">// let bird = new Animal(); 报错，抽象类是不能被实例化的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">TS中的函数</h2>
<h4 data-id="heading-15">可选参数和默认参数</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> fun = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a: <span class="hljs-built_in">string</span> = <span class="hljs-string">'dongfang'</span>, b?: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> </span>&#123;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">剩余参数 ...rest</h4>
<p>rest参数，一定要放在函数声明的时候的所有参数之后</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fun</span> (<span class="hljs-params">a: <span class="hljs-built_in">string</span>, ...args: <span class="hljs-built_in">string</span>[]</span>) </span>&#123;
  
&#125;
Fun(<span class="hljs-string">'q'</span>, <span class="hljs-string">'qw'</span>, <span class="hljs-string">'e'</span>, <span class="hljs-string">'r'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">函数重载</h4>
<p>函数的名字相同，但是函数的参数及个数是不同的</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 函数重载的声明</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span>, y: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> | <span class="hljs-title">number</span> | <span class="hljs-title">undefined</span> </span>&#123;
    // 在实现上我们要注意严格判断两个参数的类型是否相等，而不能简单的写一个 <span class="hljs-title">x</span> + <span class="hljs-title">y</span>
    <span class="hljs-title">if</span> (<span class="hljs-params"><span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span> && <span class="hljs-keyword">typeof</span> y === <span class="hljs-string">'string'</span></span>) </span>&#123;
      <span class="hljs-title">return</span> <span class="hljs-title">x</span> + <span class="hljs-title">y</span>
    &#125; <span class="hljs-title">else</span> <span class="hljs-title">if</span> (<span class="hljs-params"><span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span> && <span class="hljs-keyword">typeof</span> y === <span class="hljs-string">'number'</span></span>) </span>&#123;
      <span class="hljs-keyword">return</span> x + y
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">泛型</h2>
<p>在定义函数，接口，或者类的时候，不能确定要使用的类型，而是在使用的时候，确定要使用的类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 多个泛型参数的函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getMsg</span><<span class="hljs-title">K</span>,<span class="hljs-title">V</span>> (<span class="hljs-params">val1: K, val2: V</span>): <span class="hljs-title">K</span>[] </span>&#123;
  <span class="hljs-keyword">return</span> [val1];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">声明文件</h2></div>  
</div>
            