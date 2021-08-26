
---
title: '浅谈 Dart 类与类的基本方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3811'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 03:58:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=3811'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、Dart 语言</h2>
<p>Dart 是一门面向对象的语言。</p>
<p>Dart 语言中所有的变量引用都是一个对象，并且所有的对象都对应一个类的实例。无论是数字、函数和<code>null</code> ，都是一个对象，所有对象继承自<code>Object</code>类。</p>
<p>在 Dart 2.13 及以上版本，如果开启空安全（sound null safety）那么除了<code>null</code>之外的所有类都继承自 <code>Object</code>。</p>
<h3 data-id="heading-1">Object</h3>
<p>Object 具有下列特性：</p>
<ul>
<li>两个属性：<code>hashCode</code>和<code>runtimeType</code>；</li>
<li>两个方法：<code>noSuchMethod</code>和<code>toString</code>；</li>
<li>操作符：Operator</li>
</ul>
<h4 data-id="heading-2">hashCode</h4>
<p>hashCode 是 read-only 属性的 int 类型数据，因为 Dart 所有的变量引用均继承于<code>Object</code>，所以每个变量引用都有自己的<code>hashCode</code>。<code>hashCode</code>的设计目的是为了提高 Dart VM 引擎在解析数据结构时的效率，并且参与判断对象的逻辑运算，与操作符 operator 相辅相成。考察如下代码：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">void</span> main() &#123;
    P p1 = P(<span class="hljs-string">"yo"</span>,<span class="hljs-string">"no"</span>);
    P p2 = P(<span class="hljs-string">"yo"</span>,<span class="hljs-string">"no"</span>);
  
    <span class="hljs-built_in">print</span>(p1 == p2);
    <span class="hljs-built_in">print</span>(p1.hashCode);
    <span class="hljs-built_in">print</span>(p2.hashCode);
    
    <span class="hljs-built_in">Map</span><P, <span class="hljs-built_in">String</span>> myMap = &#123;&#125;;
    myMap[p1] = <span class="hljs-string">"first Item"</span>;

    <span class="hljs-built_in">print</span>(myMap.containsKey(p2));
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-keyword">var</span> naam;
    <span class="hljs-keyword">var</span> kaam;
    P(<span class="hljs-keyword">this</span>.naam, <span class="hljs-keyword">this</span>.kaam);
    
    <span class="hljs-meta">@override</span>
    <span class="hljs-built_in">int</span> <span class="hljs-keyword">get</span> hashCode &#123;
        <span class="hljs-built_in">int</span> result = <span class="hljs-number">11</span> * naam.hashCode;
        result = <span class="hljs-number">13</span> * (result + kaam.hashCode);
        <span class="hljs-keyword">return</span> result;
    &#125; 
    
    <span class="hljs-meta">@override</span>
    <span class="hljs-built_in">bool</span> <span class="hljs-keyword">operator</span> == (<span class="hljs-built_in">dynamic</span> otherObj) &#123;
        <span class="hljs-keyword">return</span> (otherObj <span class="hljs-keyword">is</span> P) && (otherObj.naam == naam) && (otherObj.kaam == kaam);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码重写了<code>P</code>对象的比较相等的逻辑，从而令<code>p1</code>和<code>p2</code>的比较结果返回为<code>true</code>。但同时需要重写<code>hashCode</code>的逻辑，否则返回值仍旧为<code>false</code>。</p>
<p>Dart 建议<code>hashCode</code>和<code>Operator</code>如有必要重写其中之一，那么另一个也需要重写，从而令哈希映射正常工作，否则<code>Operator</code>重写无效。</p>
<h4 data-id="heading-3">runtimeType</h4>
<p><code>runtimeType</code>是 read-only 属性，表达数据结构在运行时的类型。<code>runtimeType</code>涉及 Dart VM 运行机制，此处留坑以后再来填。</p>
<h4 data-id="heading-4">noSuchMethod</h4>
<p>当调用对象上不存在的方法时，就会触发<code>noSuchMethod</code>，考察如下代码：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">void</span> main() &#123;
    P p = P();
    <span class="hljs-built_in">print</span>(p.add(<span class="hljs-number">888</span>));
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-meta">@override</span>
    noSuchMethod(Invocation invocation) => 
        <span class="hljs-string">'Got the <span class="hljs-subst">$&#123;invocation.memberName&#125;</span> with arguments <span class="hljs-subst">$&#123;invocation.positionalArguments&#125;</span>'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 DartPad 编辑器运行上述代码，发现并未触发<code>noSuchMethod</code>方法， 而是直接抛出了编译错误。实际<code>noSuchMethod</code>触发需要有两个条件：</p>
<ul>
<li>调用方必须是<code>dynamic</code>类型；</li>
<li>调用方具有被调用方法的定义但未实现，同时<code>noSuchMethod</code>也被重写；</li>
</ul>
<p>所以只有如下两种情况，才会触发<code>noSuchMethod</code>：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-built_in">dynamic</span> p = P();
    Q q = Q(); <span class="hljs-comment">// 该情况下，q 可以是 Q 类型，也可以是 dynamic</span>
    <span class="hljs-built_in">print</span>(p.add(<span class="hljs-number">123</span>));
    <span class="hljs-built_in">print</span>(q.add(<span class="hljs-number">123</span>));
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-meta">@override</span>
    noSuchMethod(Invocation invocation) => <span class="hljs-string">'Got the <span class="hljs-subst">$&#123;invocation.memberName&#125;</span> with arguments <span class="hljs-subst">$&#123;invocation.positionalArguments&#125;</span>'</span>;
    &#125;
    
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Q</span> </span>&#123;
    miss(<span class="hljs-built_in">int</span> data);
    <span class="hljs-meta">@override</span>
    noSuchMethod(Invocation invocation) => <span class="hljs-string">'Got the <span class="hljs-subst">$&#123;invocation.memberName&#125;</span> with arguments <span class="hljs-subst">$&#123;invocation.positionalArguments&#125;</span>'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">toString</h4>
<p><code>toString</code>方法使用字符串来表达对象的信息，也可以在将数字转换为字符串的场景下使用。开发者也可以重写 <code>toString</code>方法，以加入自定义内容。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">void</span> main() &#123;
    P p = P();
    p.toString();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-meta">@override</span>
    toString() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'this is custom text'</span>
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">二、Dart 类与基本方法</h2>
<h3 data-id="heading-7">1.类的定义和构造函数</h3>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">String</span> name;
    <span class="hljs-built_in">int</span> age;
    
    P(<span class="hljs-built_in">String</span> dataName, <span class="hljs-built_in">int</span> dataAge) &#123;
        name = dataName;
        age = dataAge;
    &#125; 
    
    <span class="hljs-built_in">bool</span> isOld() &#123;
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">30</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>;
    &#125; 
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> P(<span class="hljs-string">'tom'</span>, <span class="hljs-number">12</span>);
    <span class="hljs-built_in">print</span>(p.name);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，声明了<code>P</code>类，P 中含有两个属性：<code>name</code>和<code>age</code>。同时也声明了构造函数，通过向构造函数传入参数从而创建实例<code>p</code>。</p>
<p>创建实例仍然使用传统的<code>new</code>方法，但在 Dart 2 以上版本，<code>new</code>关键字可以省略，同时构造函数也可以用语法糖简化，代码写法如下：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">String</span> name;
    <span class="hljs-built_in">int</span> age;
    
    P(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age);
    
    <span class="hljs-built_in">bool</span> isOld() &#123;
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">30</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>;
    &#125;
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">var</span> p = P(<span class="hljs-string">'tom'</span>, <span class="hljs-number">12</span>);
    <span class="hljs-built_in">print</span>(p.name); <span class="hljs-comment">// tom</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">命名构造函数</h4>
<p>除默认的构造函数外，Dart 提供命名构造函数方法。代码如下：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">String</span> name;
    <span class="hljs-built_in">int</span> age;
    
    P(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age);
    
    P.init(<span class="hljs-built_in">String</span> dataName, <span class="hljs-built_in">int</span> dataAge) &#123;
        name = dataName;
        age = dataAge;
    &#125; 
    
    <span class="hljs-built_in">bool</span> isOld() &#123;
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">30</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>;
    &#125;
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">var</span> p = P.init(<span class="hljs-string">'tom'</span>, <span class="hljs-number">12</span>);
    <span class="hljs-built_in">print</span>(p.name); <span class="hljs-comment">// tom</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命名构造函数的功能看起来与默认构造函数的功能类似，那设计该机制的目的是什么呢？原因是 Dart 不支持构造函数的重载，无法使用不同的参数来执行构造方法，所以提供命名构造函数的机制来实现多方式创建实例。</p>
<h4 data-id="heading-9">工厂构造函数</h4>
<p>除了上述两种构造函数外，Dart 还提供第三种构造函数：工厂构造函数。它的使用场景是：如果调用构造函数时，如果实例已存在，不会重新创建实例，而是使用已存在的实例，保证环境内只有一个实例存在，也就是单例模式。考察如下代码：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">String</span> name;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">dynamic</span>> _cache = &#123;&#125;;
    
    <span class="hljs-keyword">factory</span> P(<span class="hljs-built_in">String</span> name) &#123;
        <span class="hljs-keyword">if</span> (_cache.containsKey(name)) &#123;
            <span class="hljs-keyword">return</span> _cache[name];
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">final</span> p = P._internal(name);
            _cache[name] = p;
            <span class="hljs-keyword">return</span> p;
        &#125;
    &#125;
    
    P._internal(<span class="hljs-keyword">this</span>.name);
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">final</span> p = P(<span class="hljs-string">'tom'</span>);
    <span class="hljs-built_in">print</span>(p.name);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂构造函数不允许访问<code>this</code>，所以<code>_cache</code>的形态必须是<code>static</code>。每次创建实例时，如果实例已经在<code>_cache</code>中存在，那么返回已存在的实例。换句话说，工厂构造函数并没有自动创建实例，而是把决定权交给开发者。</p>
<h3 data-id="heading-10">2.类的属性和方法</h3>
<h4 data-id="heading-11">静态变量和静态方法</h4>
<p>和大多数语言一样，Dart 提供静态变量和静态方法：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-keyword">static</span> age;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">bool</span> isOld() &#123;
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">30</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态方法无法使用<code>this</code>，也不能访问非静态成员，类的实例也无法调用静态方法，并且静态变量只有在被使用的时候才会初始化。</p>
<h4 data-id="heading-12">私有属性和私有方法</h4>
<p>Dart 不提供类似<code>public</code>、<code>protected</code>等关键字，在变量前添加下划线即可声明私有：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">int</span> _age;
    P(<span class="hljs-keyword">this</span>._age);
    
    <span class="hljs-built_in">bool</span> _isOld() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>._age > <span class="hljs-number">30</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>; 
    &#125; 
    
    <span class="hljs-built_in">bool</span> isOld() &#123; 
        <span class="hljs-keyword">return</span> _isOld(); 
    &#125;
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">final</span> p = P(<span class="hljs-number">20</span>);
    <span class="hljs-built_in">print</span>(p._age);     <span class="hljs-comment">// error</span>
    <span class="hljs-built_in">print</span>(p._isOld()); <span class="hljs-comment">// error </span>
    <span class="hljs-built_in">print</span>(p.isOld());  <span class="hljs-comment">// false </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例无法直接调用私有方法，但是可以通过调用公有方法的形式间接调用私有方法。</p>
<h3 data-id="heading-13">3.类的继承</h3>
<h4 data-id="heading-14">构造函数</h4>
<p>Dart 通过<code>extends</code>关键字实现继承，子类继承父类中公有的属性和方法，不会继承构造函数，所以子类的构造函数需通过<code>super</code>关键字来调用或改造父类的构造函数：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">num</span> name;
    <span class="hljs-built_in">num</span> age;
    
    P(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age);
    P.xxx(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age); &#125;

<span class="hljs-comment">// class Q extends P &#123;</span>
<span class="hljs-comment">//     Q(num name, num age): super(name, age); </span>
<span class="hljs-comment">// &#125; </span>

<span class="hljs-comment">// class Q extends P &#123; </span>
<span class="hljs-comment">//     num sex; </span>
<span class="hljs-comment">//     Q(num sex, num name, num age): super.xxx(name, age) &#123;</span>
<span class="hljs-comment">//         this.sex = sex;</span>
<span class="hljs-comment">//     &#125; </span>
<span class="hljs-comment">// &#125; </span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Q</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">P</span> </span>&#123; 
    <span class="hljs-built_in">num</span> sex; 
    Q(<span class="hljs-built_in">num</span> sex, <span class="hljs-built_in">num</span> name, <span class="hljs-built_in">num</span> age): <span class="hljs-keyword">super</span>(name, age) &#123; 
        <span class="hljs-keyword">this</span>.sex = sex;
    &#125;
&#125;

<span class="hljs-keyword">void</span> main() &#123;
    <span class="hljs-keyword">final</span> q = Q(<span class="hljs-number">12</span>, <span class="hljs-number">13</span>, <span class="hljs-number">14</span>);
    <span class="hljs-built_in">print</span>(q.sex); <span class="hljs-comment">// 12 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码演示了子类中三种构造函数的表现：</p>
<ul>
<li>直接复用父类构造函数</li>
<li>复用和改造父类默认构造函数</li>
<li>复用和改造父类命名构造函数</li>
</ul>
<h4 data-id="heading-15">子类调用父类方法</h4>
<p>如果子类需要调用父类方法，同样使用<code>super</code>关键字，此时方法内部的<code>this</code>指向子类：</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123;
    <span class="hljs-built_in">num</span> name;
    <span class="hljs-built_in">num</span> age; 
    
    P(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age); 
    
    <span class="hljs-built_in">bool</span> childCheck() &#123; 
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">20</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>; 
    &#125; 
&#125; 

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Q</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">P</span> </span>&#123; 
    Q(<span class="hljs-built_in">num</span> name, <span class="hljs-built_in">num</span> age): <span class="hljs-keyword">super</span>(name, age); 
    
    <span class="hljs-built_in">bool</span> check() &#123; 
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.check(); 
    &#125; 
&#125;

<span class="hljs-keyword">void</span> main() &#123; 
    <span class="hljs-keyword">final</span> a = Q(<span class="hljs-number">12</span>, <span class="hljs-number">13</span>); 
    <span class="hljs-built_in">print</span>(a.childCheck()); <span class="hljs-comment">// false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">子类重写父类方法</h4>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">P</span> </span>&#123; 
    <span class="hljs-built_in">num</span> name; 
    <span class="hljs-built_in">num</span> age; 
    
    P(<span class="hljs-keyword">this</span>.name, <span class="hljs-keyword">this</span>.age); 
    
    <span class="hljs-built_in">bool</span> check() &#123; 
        <span class="hljs-keyword">return</span> age > <span class="hljs-number">20</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>; 
    &#125; 
&#125; 

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Q</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">P</span> </span>&#123; 
    Q(<span class="hljs-built_in">num</span> name, <span class="hljs-built_in">num</span> age): <span class="hljs-keyword">super</span>(name, age); 
    
    <span class="hljs-meta">@override</span>
    <span class="hljs-built_in">bool</span> childCheck() &#123; 
        <span class="hljs-keyword">return</span> age == <span class="hljs-number">13</span> ? <span class="hljs-keyword">true</span> : <span class="hljs-keyword">false</span>; 
    &#125; 
&#125;

<span class="hljs-keyword">void</span> main() &#123; 
    <span class="hljs-keyword">final</span> a = Q(<span class="hljs-number">12</span>, <span class="hljs-number">13</span>); 
    <span class="hljs-built_in">print</span>(a.childCheck()); <span class="hljs-comment">// true </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子类在重写父类方法时，只要方法名称与父类相同，便可实现逻辑重写，<code>@override</code>为可选项，对于复杂逻辑的类功能建议添加。</p></div>  
</div>
            