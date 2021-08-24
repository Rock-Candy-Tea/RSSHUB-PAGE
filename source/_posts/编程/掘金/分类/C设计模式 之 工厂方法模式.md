
---
title: 'C#设计模式 之 工厂方法模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b01a34c32345378ab2950b7d620a61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 06:37:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b01a34c32345378ab2950b7d620a61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力。</a></p>
<blockquote>
<p>别名：虚拟构造器、Factory Method</p>
</blockquote>
<h1 data-id="heading-0">一，意图</h1>
<p>  用于创建对象的接口，让子类决定创建哪一个类。工厂方法模式使一个类的实例化延迟到子类。</p>
<hr>
<h1 data-id="heading-1">二，动机</h1>
<p>   在软件系统中，经常面临着"某个对象‘’的创建工作；由于需求的变化，这个对象的具体实现经常面临着剧烈的变化，但是它却拥有这比较稳定的接口。</p>
<p><strong>问题来了：</strong>
    如何应对这种变化？如何提供一种“封装机制”来隔离出 “这个易变对象” 的变化，从而保持系统中的 “其他依赖改对象” 不随这需求的改变而改变呢？</p>
<p><strong>举例理解：</strong>
  绝地求生中有很多车（轿车，吉普车，蹦蹦等），我现在需要一个测试车工具类，测试这些车的功能（启动，转向，停止等）。而这个车测试类需要可以测试所有满足车的抽象类的车的具体类（即便后面在增加几种类型，这个测试类也不需要改变）。</p>
<p><strong>解决方案：</strong>
  创建一个车类型的接口和车类型的工厂接口。然后每种具体的车(轿车，吉普...)都去实现车类型的接口，然后在创建一个自己的工厂并实现类型的工厂接口。
  这样不管后面需要增加什么样的车，只有他满足车的接口都可以按照这这种方式实现。</p>
<p><strong>归纳总结：</strong>
  工厂方法模式通过面向对象的手法，将所要创建的具体对象工作延迟到子类，从而实现一种扩展（而非更改）的策略，较好地解决了这种紧耦合的关系。</p>
<hr>
<h1 data-id="heading-2">三，结构</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b01a34c32345378ab2950b7d620a61~tplv-k3u1fbpfcp-watermark.image" alt="工厂方法" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>产品 （Product） 将会对接口进行声明。 对于所有由创建者及其子类构建的对象， 这些接口都是通用的。</li>
<li>具体产品 （Concrete Products） 是产品接口的不同实现。</li>
<li>创建者 （Creator） 类声明返回产品对象的工厂方法。 该方法的返回对象类型必须与产品接口相匹配。</li>
</ol>
<p>你可以将工厂方法声明为抽象方法， 强制要求每个子类以不同方式实现该方法。 或者， 你也可以在基础工厂方法中返回默认产品类型。
PS：虽然它的名字是创建者， 但他最主要的职责并不是创建产品。一般来说， 创建者类包含一些与产品相关的核心业务逻辑。 工厂方法将这些逻辑处理从具体产品类中分离出来。  比如，你们公司有一个给程序员培训的部门。 但是， 公司的主要工作还是编写代码， 而非培训程序员。
4. 具体创建者 （Concrete Creators） 将会重写基础工厂方法， 使其返回不同类型的产品。
PS: 并不一定每次调用工厂方法都会创建新的实例。 工厂方法也可以返回缓存、 对象池或其他来源的已有对象。</p>
<hr>
<h1 data-id="heading-3">四，优缺点</h1>
<p><strong>优点：</strong></p>
<ul>
<li>你可以避免创建者和具体产品之间的紧密耦合。</li>
<li>单一职责原则。 你可以将产品创建代码放在程序的单一位置， 从而使得代码更容易维护。</li>
<li>开闭原则。 无需更改现有客户端代码， 你就可以在程序中引入新的产品类型。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>应用工厂方法模式需要引入许多新的子类， 代码可能会因此变得更复杂。 最好的情况是将该模式引入创建者类的现有层次结构中。</li>
</ul>
<hr>
<h1 data-id="heading-4">五，应用场景</h1>
<p><strong>适用性：</strong></p>
<ul>
<li>当一个类不知道它所必须创建对象的类的时候</li>
<li>当一个类希望由它的子类来指定它所创建的对象的时候</li>
<li>当你在写代码的过程中， 如果无法预知对象确切类别及其依赖关系时， 可使用工厂方法。( 例如， 如果需要向应用中添加一种新产品， 你只需要开发新的创建者子类， 然后重写其工厂方法即可。)</li>
</ul>
<p><strong>对照：</strong></p>
<ul>
<li>工厂方法模式解决“单个对象”的需求变化；</li>
<li>抽象工厂模式解决“系列对象”的需求变化；</li>
<li>生成器模式  解决“对象部分”的需求变化；</li>
</ul>
<p> <strong>工厂方法模式主要用于隔离类对象的使用者和具体类型之间的耦合关系。面对一个经常变化的具体类型，紧耦合关系会导致程序的脆弱。</strong></p>
<hr>
<h1 data-id="heading-5">六，代码实现</h1>
<p><strong>实现方式：</strong></p>
<ol>
<li>让所有产品都遵循同一接口。 该接口必须声明对所有产品都有意义的方法。（所有子类都能用上）</li>
<li>在创建类中添加一个空的工厂方法。 该方法的返回类型必须遵循通用的产品接口。(上面声明的那个接口)</li>
<li>在创建类代码中找到对于构造函数的所有引用。 将它们依次替换为对于工厂方法的调用， 同时将创建方法(new)的代码移入工厂方法。</li>
<li>为工厂方法中的每种产品编写一个工厂子类， 然后在子类中重写工厂方法， 并将基本方法中的相关创建代码移动到工厂方法中。</li>
<li>如果应用中的产品类型太多， 那么为每个产品创建子类工作量就很大， 这时你也可以在子类中在找出几个类的共同点创建一个基类。</li>
</ol>
<p><strong>示例代码：</strong></p>
<ol>
<li>还是以上面说的那个测试车为例：首先有个抽象车类(此类包含的所有声明必顶对所有子类都有意义【比如：声明了一个测试耗油量的方法，若此时你需要测试的车中有电动车，那么这个方法就不应该声明在抽象类(接口)中】)</li>
</ol>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 车的抽象(接口)</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>
&#123;
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 启动</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">StartUp</span>(<span class="hljs-params"></span>)</span>;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 转向</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Turn</span>(<span class="hljs-params"></span>)</span>;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 停车</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Stop</span>(<span class="hljs-params"></span>)</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建一个工厂方法接口</li>
</ol>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 车工厂</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">class</span> <span class="hljs-title">CarFactory</span>
&#123;
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 创建车</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> Car <span class="hljs-title">CreateCar</span>(<span class="hljs-params"></span>)</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.创建具体车类 -- 实现1创建接口</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 吉普车</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">class</span> <span class="hljs-title">JiPuCar</span> : <span class="hljs-title">Car</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">StartUp</span>(<span class="hljs-params"></span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">"--- 吉普车 启动 ---"</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Stop</span>(<span class="hljs-params"></span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">"--- 吉普车 停下 ---"</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Turn</span>(<span class="hljs-params"></span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">"--- 吉普车 转向 ---"</span>);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.创建具体车类（对应3）的工厂类 -- 实现2创建接口</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 吉普车工厂</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">JiPuCarFactory</span> : <span class="hljs-title">CarFactory</span>
&#123;

    <span class="hljs-comment">// 若只需要测试一种车完全没有必要使用工厂方法设计模式,</span>
    <span class="hljs-comment">// 直接在测试对象中写 Car c = new Car(); 就可以了.</span>

    <span class="hljs-comment">// 若需要测试固定类型(数量)的车也不需要使用工厂方法设计模式,</span>
    <span class="hljs-comment">// 直接将测试方法中new 或者作为参数传进来就可以了.</span>

    <span class="hljs-comment">// 当需要测试不定类型(数量)的车时, 才符合使用这种设计模式.</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> Car <span class="hljs-title">CreateCar</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> JiPuCar();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>放到测试框架中进行测试：</li>
</ol>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 车测试框架 -- 所有车都可以被测试</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">class</span> <span class="hljs-title">CarTestFramework</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">BuildTestCar</span>(<span class="hljs-params">CarFactory carFactory</span>)</span>
    &#123;
        Car c1 = carFactory.CreateCar();
        c1.StartUp();
        c1.Turn();
        c1.Stop();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.启动测试框架，查看测试结果</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">class</span> <span class="hljs-title">Program</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Main</span>(<span class="hljs-params"><span class="hljs-built_in">string</span>[] args</span>)</span>
    &#123;
        CarTestFramework carTestFramework = <span class="hljs-keyword">new</span> CarTestFramework();
        carTestFramework.BuildTestCar(<span class="hljs-keyword">new</span> JiPuCarFactory());

        Console.ReadKey();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1f3eac14864339962145fcb631e89a~tplv-k3u1fbpfcp-watermark.image" alt="测试结果" loading="lazy" referrerpolicy="no-referrer">
按照此逻辑，当再有其他车需要进行测试时，只需要按照3,4步骤中实现对应的具体车类和对应的工厂类即可，进行测试。这样就保证了有需求增加时只需要我们拓展（新建类）而不需要修改现有的代码。</p>
<hr>
<p>设计模式系列文示例代码工程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodechina.csdn.net%2FCzhenya%2Fcsharp_design_patterns" target="_blank" rel="nofollow noopener noreferrer" title="https://codechina.csdn.net/Czhenya/csharp_design_patterns" ref="nofollow noopener noreferrer">链接</a></p>
<hr>
<hr></div>  
</div>
            