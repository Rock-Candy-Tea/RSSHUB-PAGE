
---
title: 'C#设计模式 之 原型模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9edbcf64f8a4ce38092a9169dcd45a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 06:42:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9edbcf64f8a4ce38092a9169dcd45a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力。</a></p>
<blockquote>
<p>别名：克隆模式、Prototype</p>
</blockquote>
<h1 data-id="heading-0">一，意图</h1>
<p>  用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。</p>
<hr>
<h1 data-id="heading-1">二，动机</h1>
<p>   在程序设计中，经常面临着“某些结构复杂的对象”的创建工作；由于需求的变化，这些对象经常面临着剧烈的变化，但是它们却拥有比较稳定一致的接口。</p>
<p><strong>问题来了：</strong>
  如何创建易变类的实体对象？</p>
<p><strong>解决方案：</strong>
  采用“原型克隆”的方法来做，它是的我们可以非常灵活地动态创建“拥有某些稳定接口”的新对象 -- 所需工作仅仅是注册一个新类的对象（原型），然后在任何需要的地方不断的Clone</p>
<p><strong>要点：</strong>
  原型设计模式用于隔离类对象的使用者和具体类型（易变类）之间的耦合关系，它要求这些易变类拥有稳定的接口。</p>
<hr>
<h1 data-id="heading-2">三，结构</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9edbcf64f8a4ce38092a9169dcd45a1~tplv-k3u1fbpfcp-watermark.image" alt="1.1" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>原型 （Prototype） 接口将对克隆方法进行声明。 通常情况下， 其中只会有一个名为 clone克隆的方法。</li>
<li>具体原型 （Concrete Prototype） 类将实现克隆方法。 除了将原始对象的数据复制到克隆体中之外， 该方法有时还需处理克隆过程中的极端情况， 例如克隆关联对象和梳理递归依赖等等。</li>
<li>客户端 （Client） 可以复制实现了原型接口的任何对象。</li>
</ol>
<hr>
<h1 data-id="heading-3">四，优缺点</h1>
<p><strong>优点：</strong></p>
<ul>
<li>可以克隆对象， 而无需与它们所属的具体类相耦合。</li>
<li>可以克隆预生成原型， 避免反复运行初始化代码。</li>
<li>可以更方便地生成复杂对象。</li>
<li>可以用继承以外的方式来处理复杂对象的不同配置。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>克隆包含循环引用的复杂对象可能会非常麻烦。</li>
</ul>
<hr>
<h1 data-id="heading-4">五，应用场景</h1>
<p><strong>适用性：</strong></p>
<ul>
<li>当一个系统应该独立于它的产品创建，构成和表示时，要使用原型模式；以及当要实例化的类是在运行时刻指定时，</li>
<li>为了创建一个与产品类层次平行的工厂类层次时</li>
<li>当一个类的实例只能有几种不同状态的组合中的一种时。建立相应数目的原型并克隆他们可能比每次用合适的状态手工实例化该类更方便。</li>
</ul>
<hr>
<h1 data-id="heading-5">六，代码实现</h1>
<p><strong>实现方式：</strong></p>
<ol>
<li>创建一个原型管理器：原型管理器是一个关联存储器，它返回一个与给定关键字匹配的原型。</li>
<li>实现克隆操作：原型设计模式最困难的部分在于正确实现Clone操作。C#语言为我们提供<code>this.MemberwiseClone();</code>来实现浅拷贝。而深拷贝我们可以通过序列化去实现。</li>
<li>初始化克隆对象：在不同的情况下，客户程序使用需要不同的初始值，所以一些原型可能要多个初始化参数。</li>
</ol>
<p>拓展：什么是“浅拷贝和深拷贝”？</p>
<ul>
<li>浅拷贝：克隆对象和原对象共享引用类型的变量 （引用类型同指向一个内存）</li>
<li>深拷贝：克隆一个对象时依次克隆它的实例变量 （所有数据间没有任何关系）</li>
</ul>
<p>可以简单理解为，浅拷贝是<code>     List<int> a = new List<int>();  List<int> b = a;</code> , 集合a，b同指向一个内存修改a中的值即修改了b中的值；而深拷贝是<code>    List<int> a = new List<int>();      List<int> b = new List<int>(a);</code>  new了一个集合b并且将a中的数据全部复制过去了，此时a，b没有任何关系。</p>
<p><strong>示例代码：</strong></p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">class</span> <span class="hljs-title">Program</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Main</span>(<span class="hljs-params"><span class="hljs-built_in">string</span>[] args</span>)</span>
    &#123;
        Person p1 = <span class="hljs-keyword">new</span> Person();
        p1.Age = <span class="hljs-number">22</span>;
        p1.Name = <span class="hljs-string">"Czhenya"</span>;
        p1.IdInfo = <span class="hljs-keyword">new</span> IdInfo(<span class="hljs-number">111</span>);

        <span class="hljs-comment">// 对p1执行一个浅拷贝，并将其赋值给p2。</span>
        Person p2 = p1.ShallowCopy();
        <span class="hljs-comment">// 对p1做一个深度拷贝，并把它赋值给p3。</span>
        Person p3 = p1.DeepCopy();

        Console.WriteLine(<span class="hljs-string">"----- p1, p2, p3的原始值: -----"</span>);

        Console.WriteLine(<span class="hljs-string">"--- 原数据 P1 :"</span>);
        DisplayValues(p1);
        Console.WriteLine(<span class="hljs-string">"--- 浅拷贝 P2 :"</span>);
        DisplayValues(p2);
        Console.WriteLine(<span class="hljs-string">"--- 深拷贝 P3 :"</span>);
        DisplayValues(p3);

        <span class="hljs-comment">// 更改p1属性的值并显示p1的值</span>
        p1.Age = <span class="hljs-number">33</span>;
        p1.Name = <span class="hljs-string">"Czy"</span>;
        p1.IdInfo.IdNumber = <span class="hljs-number">222</span>;

        Console.WriteLine();
        Console.WriteLine(<span class="hljs-string">"----- 对原数据p1 进行修改后 p1、p2、p3的值: -----"</span>)

        Console.WriteLine(<span class="hljs-string">"+++ 原数据 P1 :"</span>);
        DisplayValues(p1);
        Console.WriteLine(<span class="hljs-string">"+++ 浅拷贝 P2 :"</span>);
        DisplayValues(p2);
        Console.WriteLine(<span class="hljs-string">"+++ 深拷贝 P3 :"</span>);
        DisplayValues(p3);

        Console.ReadKey();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">DisplayValues</span>(<span class="hljs-params">Person p</span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">"姓名: &#123;0:s&#125;, 年龄: &#123;1:d&#125;, ID: &#123;2:d&#125;"</span>, p.Name, p.Age
    &#125;

&#125;

<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 原类型 -- 需要被拷贝的类</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Person</span>
&#123;
    <span class="hljs-comment">// 多种类型数据，查看拷贝后的数据</span>
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">int</span> Age;
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">string</span> Name;
    <span class="hljs-keyword">public</span> IdInfo IdInfo;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 浅拷贝</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> MemberwiseClone -- 按成员拷贝(复制引用类型的地址，而不是new)</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><returns></span><span class="hljs-doctag"></returns></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Person <span class="hljs-title">ShallowCopy</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">return</span> (Person)<span class="hljs-keyword">this</span>.MemberwiseClone();
    &#125;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 深拷贝</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><returns></span><span class="hljs-doctag"></returns></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Person <span class="hljs-title">DeepCopy</span>(<span class="hljs-params"></span>)</span>
    &#123;
        Person clone = (Person)<span class="hljs-keyword">this</span>.MemberwiseClone();
        <span class="hljs-comment">// int Age 这种简单类型不需要管，在MemberwiseClone处理了</span>
        <span class="hljs-comment">// 引用类型</span>
        clone.IdInfo = <span class="hljs-keyword">new</span> IdInfo(IdInfo.IdNumber);
        <span class="hljs-keyword">return</span> clone;
    &#125;
&#125;

<span class="hljs-comment">// 作为引用类型的数据</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">IdInfo</span>
&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">int</span> IdNumber;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">IdInfo</span>(<span class="hljs-params"><span class="hljs-built_in">int</span> idNumber</span>)</span>
    &#123;
        <span class="hljs-keyword">this</span>.IdNumber = idNumber;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00cf00f7d4c41ce9891b9432c816ff3~tplv-k3u1fbpfcp-watermark.image" alt="1.2" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>设计模式系列博文示例代码工程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodechina.csdn.net%2FCzhenya%2Fcsharp_design_patterns" target="_blank" rel="nofollow noopener noreferrer" title="https://codechina.csdn.net/Czhenya/csharp_design_patterns" ref="nofollow noopener noreferrer">链接</a></p>
<hr>
<hr></div>  
</div>
            