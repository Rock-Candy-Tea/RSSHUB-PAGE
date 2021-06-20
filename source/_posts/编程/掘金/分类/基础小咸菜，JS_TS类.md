
---
title: '基础小咸菜，JS_TS类'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4874'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 08:01:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=4874'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 19 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">基础小咸菜，JS/TS类</h1>
<h2 data-id="heading-1">1 类在JS中的表现(ES6)</h2>
<p>先上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"> params </span>)</span>&#123;
        <span class="hljs-comment">// 实列成员</span>
        <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'name'</span>;
        <span class="hljs-built_in">this</span>.params = params;
        <span class="hljs-built_in">this</span>.testAction = <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'构造函数上的方法'</span>)
        &#125;
    &#125;
    <span class="hljs-comment">// 原型方法,定义在原型对象上</span>
    <span class="hljs-function"><span class="hljs-title">testPublicAction</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是公共方法'</span>)
    &#125;
    <span class="hljs-comment">// 静态方法 定义在类本身上</span>
    <span class="hljs-keyword">static</span> testStaticAction ()&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是静态方法'</span>)
    &#125;

&#125;
<span class="hljs-comment">// es6中没有静态属性，因此添加静态属性可以这么添加</span>
Test.myattr = <span class="hljs-string">"类的静态属性"</span>;
<span class="hljs-comment">// 在原型上定义数据成员</span>
Test.prototype.firistname  = <span class="hljs-string">"在原型上定义数据成员"</span>;

<span class="hljs-keyword">const</span> testone = <span class="hljs-keyword">new</span> Test(<span class="hljs-string">'我是参数'</span>);
<span class="hljs-built_in">console</span>.log(testone.name);
<span class="hljs-built_in">console</span>.log(testone.params);
<span class="hljs-built_in">console</span>.log(testone.firistname); <span class="hljs-comment">// 打印 在原型上定义数据成员</span>
testone.testPublicAction();
<span class="hljs-comment">// testone.testStaticAction();// 静态方法放实例中调用报错</span>
Test.testStaticAction();<span class="hljs-comment">// 正确</span>
testone.testAction();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestTwo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Test</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">paramsOne,paramsTwo</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(paramsOne); <span class="hljs-comment">// 调用继承Test类的构造函数</span>
        <span class="hljs-built_in">this</span>.testTwoName = paramsTwo;
        <span class="hljs-built_in">this</span>.testTwoAction = <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是类testTwo上的方法'</span>)
        &#125;
    &#125;

    <span class="hljs-comment">// 可以在静态方法中通过super调用继承的类上定义的静态方法</span>
    <span class="hljs-keyword">static</span> handExtendsParentAction ()&#123;
        <span class="hljs-built_in">super</span>.testStaticAction();
    &#125;
&#125;

<span class="hljs-keyword">const</span> testtow = <span class="hljs-keyword">new</span> TestTwo(<span class="hljs-string">'我是一个新参数一'</span>,<span class="hljs-string">'我是一个新参数二'</span>);
<span class="hljs-built_in">console</span>.log(testtow)
testtow.testPublicAction();
TestTwo.handExtendsParentAction();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.1 在es6类中的构造函数</h3>
<p><code>constructor</code>会告诉解释器在使用<code>new</code>操作符创建新的实例时调用这个2.函数。</p>
<h3 data-id="heading-3">1.2 实例化</h3>
<p>使用<code>new</code>调用类的构造函数会执行如下操作</p>
<ol>
<li>在内存中创建一个新的对象</li>
<li>在这个新对象内部的__proto__指针被赋值为构造函数的prototype属性</li>
<li>this指向新对象</li>
<li>指向构造函数的代码</li>
<li>如果构造函数返回非控对象这返回该对象；如果为空则返回刚创建的对象</li>
</ol>
<p>补充：其实类也是一种特殊的函数</p>
<h2 data-id="heading-4">2. 继承</h2>
<p>es6实现继承比使用原型链实现继承简单多了，直接使用extends关键字即可</p>
<h3 data-id="heading-5">2.1 <code>super()</code></h3>
<p>派生类使用super关键字引用他们的原型。</p>
<ul>
<li>在静态方法中可以通过<code>super()</code>调用继承类上的定义的静态方法</li>
<li><code>super()</code>只能在派生类构造函数和静态方法中使用</li>
<li>不能单独引用<code>super()</code>关键字，要么用他调用构造函数，要么用它引用静态方法</li>
<li>调用<code>super()</code>会调用父类构造函数，并将返回的实例赋值给this</li>
<li><code>super(</code>)的行为如同调用构造函数，如果需要给父类构造函数传参，则需要手动传入</li>
<li>如果没有定义类构造函数，在实例化派生类会调用super而且会传入所有传给派生类的参数</li>
<li>在类的构造函数中不能再调用<code>super()</code>之前调用this</li>
<li>如果在派生类中显示的定义了构造函数，则要么必须在其中调用super()，要么必须在其中返回一个对象</li>
</ul>
<h3 data-id="heading-6">2.2 抽象基类</h3>
<p>有时候需要这样一个类：提供给其他类继承，但本身不会被实例化
实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseClass</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">new</span>.target === BaseClass)&#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'这是一个抽象基类'</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3 ts的类</h2>
<p>其实ts的类和es6都差不多，多了如下：</p>
<h3 data-id="heading-8">3.1 public</h3>
<p><code>public</code>表示公共的，用来指定在创建实例后可以通过实例访问的，也就是类定义的外部可以访问的属性和方法。默认是 <code>public</code>，但是 <code>TSLint</code> 可能会要求你必须用修饰符来表明这个属性或方法是什么类型的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
  public x: number;
  public y: number;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x: number, y: number</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;
  public <span class="hljs-function"><span class="hljs-title">getPosition</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`(<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.x&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.y&#125;</span>)`</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.2 private</h3>
<p>private修饰符表示私有的，它修饰的属性在类的定义外面是没法访问的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  private age: number;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: number</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent(<span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(p); <span class="hljs-comment">// &#123; age: 18 &#125;</span>
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error 属性“age”为私有属性，只能在类“Parent”中访问</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// error 类型“typeof ParentA”上不存在属性“age”</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: number</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(age);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.age); <span class="hljs-comment">//error 通过 "super" 关键字只能访问基类的公共方法和受保护方法</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.3 protected</h3>
<p>protected修饰符是受保护修饰符，和private有些相似，但有一点不同，protected修饰的成员在继承该类的子类中可以访问，上面那个例子，把父类 Parent 的 age 属性的修饰符 private 替换为 protected：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  protected age: number;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: number</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
  protected <span class="hljs-function"><span class="hljs-title">getAge</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Parent(<span class="hljs-number">18</span>);
<span class="hljs-built_in">console</span>.log(p.age); <span class="hljs-comment">// error 属性“age”为私有属性，只能在类“ParentA”中访问</span>
<span class="hljs-built_in">console</span>.log(Parent.age); <span class="hljs-comment">// error 类型“typeof ParentA”上不存在属性“age”</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age: number</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(age);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.age); <span class="hljs-comment">// undefined</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>.getAge());
  &#125;
&#125;
<span class="hljs-keyword">new</span> Child(<span class="hljs-number">18</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>protected</code>还能用来修饰 <code>constructor</code> 构造函数，加了<code>protected</code>修饰符之后，这个类就不能再用来创建实例，只能被子类继承，这个需求 ES6 的类的时候需要用<code>new.target</code>来自行判断，而 TS 则只需用<code> protected</code> 修饰符即可</p>
<h3 data-id="heading-11">3.4 <code>readonly</code> 修饰符</h3>
<p>在类里可以使用readonly关键字将属性设置为只读</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserInfo</span> </span>&#123;
  readonly name: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> UserInfo(<span class="hljs-string">"Lison"</span>);
user.name = <span class="hljs-string">"haha"</span>; <span class="hljs-comment">// error Cannot assign to 'name' because it is a read-only property</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置为只读的属性，实例只能读取这个属性值，但不能修改。</p>
<h3 data-id="heading-12">3.5 存取器</h3>
<p>这个也就 ES6 标准中的存值函数和取值函数，也就是在设置属性值的时候调用的函数，和在访问属性值的时候调用的函数，用法和写法和 ES6 的没有区别：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserInfo</span> </span>&#123;
  private _fullName: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">fullName</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._fullName;
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">fullName</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`setter: <span class="hljs-subst">$&#123;value&#125;</span>`</span>);
    <span class="hljs-built_in">this</span>._fullName = value;
  &#125;
&#125;
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> UserInfo();
user.fullName = <span class="hljs-string">"Lison Li"</span>; <span class="hljs-comment">// "setter: Lison Li"</span>
<span class="hljs-built_in">console</span>.log(user.fullName); <span class="hljs-comment">// "Lison Li"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3.6 抽象类</h3>
<p>抽象类一般用来被其他类继承，而不直接用它创建实例。抽象类和类内部定义抽象方法，使用abstract关键字</p>
<h3 data-id="heading-14">3.7 类类型接口</h3>
<p>使用接口可以强制一个类的定义必须包含某些内容，先来看个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface FoodInterface &#123;
  <span class="hljs-attr">type</span>: string;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">FoodInterface</span> </span>&#123;
  <span class="hljs-comment">// error Property 'type' is missing in type 'FoodClass' but required in type 'FoodInterface'</span>
  <span class="hljs-keyword">static</span> type: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面接口 <code>FoodInterface</code> 要求使用该接口的值必须有一个 <code>type</code> 属性，定义的类<code>FoodClass</code>要使用接口，需要使用关键字<code>implements</code>。<code>implements</code>关键字用来指定一个类要继承的接口，如果是接口和接口、类和类直接的继承，使用<code>extends</code>，如果是类继承接口，则用<code>implements</code>。</p>
<p>有一点需要注意，接口检测的是使用该接口定义的类创建的实例，所以上面例子中虽然定义了静态属性 <code>type</code>，但静态属性不会添加到实例上，所以还是报错，所以我们可以这样改：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface FoodInterface &#123;
  <span class="hljs-attr">type</span>: string;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodClass</span> <span class="hljs-title">implements</span> <span class="hljs-title">FoodInterface</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">public type: string</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这个需求抽象类实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FoodAbstractClass</span> </span>&#123;
  abstract type: string;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Food</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">FoodAbstractClass</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">public type: string</span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.8 接口继承类</h3>
<p>接口可以继承一个类，当接口继承了该类后，会继承类的成员，但是不包括其实现，也就是只继承成员以及成员类型。接口还会继承类的<code>private</code>和<code>protected</code>修饰的成员，当接口继承的这个类中包含这两个修饰符修饰的成员时，这个接口只可被这个类或他的子类实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  protected name: string;
&#125;
interface I <span class="hljs-keyword">extends</span> A &#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;&#125; <span class="hljs-comment">// error Property 'name' is missing in type 'B' but required in type 'I'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;
  <span class="hljs-comment">// error 属性“name”受保护，但类型“C”并不是从“A”派生的类</span>
  <span class="hljs-attr">name</span>: string;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">D</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> <span class="hljs-title">implements</span> <span class="hljs-title">I</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">3.9 在泛型中使用类类型</h3>
<p>这里我们先来看个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> create = <T>(c: &#123; <span class="hljs-keyword">new</span> (): T &#125;): <span class="hljs-function"><span class="hljs-params">T</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> c();
&#125;;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Info</span> </span>&#123;
  <span class="hljs-attr">age</span>: number;
&#125;
create(Info).age;
create(Info).name; <span class="hljs-comment">// error 类型“Info”上不存在属性“name”</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子里，我们创建了一个一个 create 函数，传入的参数是一个类，返回的是一个类创建的实例，这里有几个点要讲：</p>
<p>参数<code>c</code>的类型定义中，<code>new()</code>代表调用类的构造函数，他的类型也就是类创建实例后的实例的类型。
<code>return new c()</code>这里使用传进来的类 <code>c </code>创建一个实例并返回，返回的实例类型也就是函数的返回值类型。
所以通过这个定义，<code>TS</code> 就知道，调用 <code>create</code> 函数，传入的和返回的值都应该是同一个类类型。</p></div>  
</div>
            