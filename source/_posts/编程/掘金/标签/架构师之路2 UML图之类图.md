
---
title: '架构师之路2 UML图之类图'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b42a86758c6a43ac9e8e4a6650a1da75~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 22:53:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b42a86758c6a43ac9e8e4a6650a1da75~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>1.类(Class)封装了数据和行为，是面向对象的重要组成部分，它是具有相同属性、操作、关系的对象集合的总称。<br>
2. 在系统中，每个类具有一定的职责，职责指的是类所担任的任务，即类要完成什么样的功能，要承担什么样的义务。一个类可以有多种职责，设计得好的类一般只有一种职责，在定义类的时候，将类的职责分解成为类的属性和操作（即方法）。<br>
3. 类的属性即类的数据职责，类的操作即类的行为职责</p>
</blockquote>
<h6 data-id="heading-1">在UML类图中，常见的有以下几种关系: <code>泛化（Generalization</code>）, <code>实现（Realization</code>, <code>关联（Association)</code>, <code>聚合（Aggregation）</code>, <code>组合(Composition), 依赖(Dependency)</code></h6>
<h4 data-id="heading-2">1、依赖关系(Dependence)</h4>
<p><strong>依赖关系（Dependence）：</strong> 假设A类的变化引起了B类的变化，则说名B类依赖于A类。</p>
<p>• 依赖关系(Dependency) 是一种使用关系，特定事物的改变有可能会影响到使用该事物的其他事物，在需要表示一个事物使用另一个事物时使用依赖关系。大多数情况下，依 赖关系体现在某个类的方法使用另一个类的对象作为参数。</p>
<p>• 在UML中，依赖关系用带箭头的虚线表示，由依赖的一方指向被依赖的一方。</p>
<div>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b42a86758c6a43ac9e8e4a6650a1da75~tplv-k3u1fbpfcp-watermark.image" alt="依赖关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Driver</span>
</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">drive</span><span class="hljs-params">(Car car)</span>
    </span>&#123;
        car.move();
    &#125;
    ……
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>
</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span>
    </span>&#123;
        ......
    &#125;
    ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>依赖关系有如下三种情况：</p>
<p>1、A类是B类中的（某中方法的）局部变量；</p>
<p>2、A类是B类方法当中的一个参数；</p>
<p>3、A类向B类发送消息，从而影响B类发生变化；</p>
<h4 data-id="heading-3">2、泛化关系（Generalization）</h4>
<p><strong>泛化关系（Generalization）：</strong> A是B和C的父类，B,C具有公共类（父类）A，说明A是B,C的一般化（概括，也称泛化）</p>
<p>• 泛化关系(Generalization)也就是继承关系，也称为“is-a-kind-of”关系，泛化关系用于描述父类与子类之间的关系，父类又称作基类或超类，子类又称作派生类。在UML中，泛 化关系用带空心三角形的直线来表示。</p>
<p>• 在代码实现时，使用面向对象的继承机制来实现泛化关系，如在Java语言中使用extends关键字、在C++/C#中使用冒号“：”来实现。</p>
<div>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f37bd6b4f82149be806781f03d276f60~tplv-k3u1fbpfcp-watermark.image" alt="泛化关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<h6 data-id="heading-4">注意：“ + ” 表示<code>public</code>, “ # ”表示<code>protected</code>, “ - ”表示<code>private</code></h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> 
</span>&#123;
    <span class="hljs-keyword">protected</span> String name;
    <span class="hljs-keyword">protected</span> <span class="hljs-keyword">int</span> age;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span> 
    </span>&#123;
        ……
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">say</span><span class="hljs-params">()</span> 
   </span>&#123;
        ……
    &#125;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> 
</span>&#123;
    <span class="hljs-keyword">private</span> String studentNo;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">study</span><span class="hljs-params">()</span> 
    </span>&#123;
        ……
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在UML当中，对泛化关系有三个要求：</p>
<p>1、子类与父类应该完全一致，父类所具有的属性、操作，子类应该都有；</p>
<p>2、子类中除了与父类一致的信息以外，还包括额外的信息；</p>
<p>3、可以使用父类的实例的地方，也可以使用子类的实例；</p>
<h4 data-id="heading-5">3、关联关系（Association）</h4>
<p><strong>关联关系（Association）:</strong> 类之间的联系，如客户和订单，每个订单对应特定的客户，每个客户对应一些特定的订单，再如篮球队员与球队之间的关联（下图所示）。</p>
<div>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07b42bfa170547edaaaf8d7f09e1a896~tplv-k3u1fbpfcp-watermark.image" alt="关联关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>其中，关联两边的"employee"和“employer”标示了两者之间的关系，而数字表示两者的关系的限制，是关联两者之间的多重性。通常有“ * ”（表示所有，不限），“ 1 ”（表示有且仅有一个），“ 0... ”（表示0个或者多个），“ 0，1 ”（表示0个或者一个），“ n...m ”(表示n到m个都可以),“ m...* ”（表示至少m个）。</p>
<p>• 关联关系(Association) 是类与类之间最常用的一种关系，它是一种结构化关系，用于表示一类对象与另一类对象之间有联系。</p>
<p>• 在UML类图中，用实线连接有关联的对象所对应的类，在使用Java、C#和C++等编程语言实现关联关系时，通常将一个类的对象作为另一个类的属性。</p>
<p>• 在使用类图表示关联关系时可以在关联线上标注角色名。</p>
<p><strong>1) 双向关联:</strong> 默认情况下，关联是双向的。</p>
<div>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c4804cbeaf14ef2ae9e95bf74adbf7c~tplv-k3u1fbpfcp-watermark.image" alt="双向关联" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Customer</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Product[] products;
    ……
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Product</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Customer customer;
    ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2 ) 单向关联:</strong> 类的关联关系也可以是单向的，单向关联用带箭头的实线表示.</p>
<div>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1681e3c431354bf683ec1e021333ad33~tplv-k3u1fbpfcp-watermark.image" alt="单向关联" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Customer</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Address address;
    ……
&#125;
 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Address</span>
</span>&#123;
    ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3) 自关联:</strong> 在系统中可能会存在一些类的属性对象类型为该类本身，这种特殊的关联关系称为自关联。</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32dc3b64264b46e58f0aca214349b77e~tplv-k3u1fbpfcp-watermark.image" alt="Node" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Node nextNode;
    ……
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**4) **<strong>重数性关联:</strong> 重数性关联关系又称为多重性关联关系(Multiplicity)，表示一个类的对象与另一个类的对象连接的个数。在UML中多重性关系可以直接在关联直线上增加一个数字表示与之对应的另一个类的对象的个数。</p>





























<table><thead><tr><th>表示方式</th><th>多重性说明</th></tr></thead><tbody><tr><td>1..1</td><td>表示另一个类的一个对象只与一个该类对象有关系</td></tr><tr><td>0..*</td><td>表示另一个类的一个对象与零个或多个该类对象有关系</td></tr><tr><td>1..*</td><td>表示另一个类的一个对象与一个或多个该类对象有关系</td></tr><tr><td>0..1</td><td>表示另一个类的一个对象没有或只与一个该类对象有关系</td></tr><tr><td>m..n</td><td>表示另一个类的一个对象与最少m、最多n个该类对象有关系 (m<=n)</td></tr></tbody></table>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d19563c92f14426abfcda65de5baad7~tplv-k3u1fbpfcp-watermark.image" alt="重数性关联" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Form</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Button buttons[];
    ……
&#125; 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Button</span>
</span>&#123;
    …
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">4、聚合关系（Aggregation）</h4>
<p><strong>聚合关系（Aggregation）:</strong> 表示的是整体和部分的关系，整体与部分 可以分开.</p>
<p>• 聚合关系(Aggregation) 表示一个整体与部分的关系。通常在定义一个整体类后，再去分析这个整体类的组成结构，从而找出一些成员类，该整体类和成员类之间就形成了聚合 关系。</p>
<p>• 在聚合关系中，成员类是整体类的一部分，即成员对象是整体对象的一部分，但是成员对象可以脱离整体对象独立存在。在UML中，聚合关系用带空心菱形的直线表示。</p>
<div align="center">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf21096ea8cf4f19a507c844a4dfec4d~tplv-k3u1fbpfcp-watermark.image" alt="聚合关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Engine engine;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Car</span><span class="hljs-params">(Engine engine)</span>
   </span>&#123;
        <span class="hljs-keyword">this</span>.engine = engine;
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setEngine</span><span class="hljs-params">(Engine engine)</span>
    </span>&#123;
        <span class="hljs-keyword">this</span>.engine = engine;
    &#125;
    ……
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Engine</span>
</span>&#123;
    ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如：电脑包括键盘、显示器，一台电脑可以和多个键盘、多个显示器搭配，确定键盘和显示器是可以和主机分开的，主机可以选择其他的键盘、显示器组成电脑；</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cda4defc38d43839de9e48ec677a270~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-7">5、组合关系（Composition）</h4>
<p><strong>组合关系（Composition）:</strong> 也是整体与部分的关系，但是整体与部分不可以分开.</p>
<p>• 组合关系(Composition)也表示类之间整体和部分的关系，但是组合关系中部分和整体具有统一的生存期。一旦整体对象不存在，部分对象也将不存在，部分对象与整体对象之 间具有同生共死的关系。</p>
<p>• 在组合关系中，成员类是整体类的一部分，而且整体类可以控制成员类的生命周期，即成员类的存在依赖于整体类。在UML中，组合关系用带实心菱形的直线表示。</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90d6c637be1f43539a7878566b801d52~tplv-k3u1fbpfcp-watermark.image" alt="组合关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Head</span>
</span>&#123;
    <span class="hljs-keyword">private</span> Mouth mouth;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Head</span><span class="hljs-params">()</span>
    </span>&#123;
    mouth = <span class="hljs-keyword">new</span> Mouth();
    &#125;
    ……
&#125;
 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mouth</span>
</span>&#123;
    ……
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">6、实现关系（Implementation)</h4>
<p><strong>实现关系（Implementation）：</strong> 是用来规定接口和实线接口的类或者构建结构的关系，接口是操作的集合，而这些操作就用于规定类或者构建的一种服务。</p>
<p>• 接口之间也可以有与类之间关系类似的继承关系和依赖关系，但是接口和类之间还存在一种实现关系(Realization)，在这种关系中，类实现了接口，类中的操作实现了接口中所 声明的操作。在UML中，类与接口之间的实现关系用带空心三角形的虚线来表示。</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44ea63c0bca14af387138581e4df6b8f~tplv-k3u1fbpfcp-watermark.image" alt="实现关系" loading="lazy" referrerpolicy="no-referrer">
</div>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Vehicle</span> 
</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Ship</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Vehicle</span>
</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span> 
    </span>&#123;
    ……
    &#125;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Vehicle</span>
</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span> 
    </span>&#123;
    ……
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            