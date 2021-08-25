
---
title: 'C#设计模式 之 适配器模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53df5446b89544c3b941621b9147eeec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 06:00:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53df5446b89544c3b941621b9147eeec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力。</a></p>
<blockquote>
<p>别名：封装器模式、Adapter</p>
</blockquote>
<h1 data-id="heading-0">一，意图</h1>
<p>   将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口兼容而不能一起工作的那些类可以一起工作。</p>
<hr>
<h1 data-id="heading-1">二，动机</h1>
<p>   在程序设计中，由于应用环境的变化，常常需要将“一些现存的对象”放在新的环境中应用，但是新环境要求的接口是这些现存对象所不满足的。</p>
<p>   有时为复用而设计的工具箱类不能够被复用的原因仅仅是因为它的接口与专业应用领域所需要的接口不适配。</p>
<p><strong>问题来了：</strong>
  如何应对这种“迁移的变化”？如何既能引用现有对象的良好实现，同时又能满足新的应用环境所要求的接口？</p>
<p><strong>举例理解：</strong>
  我们要做一个数据图表展示系统，使用的是XML格式的文件。后来由于市场需求的增加，我们需要引用第三方库来做数据分析，而此时第三方库使用的是JSON格式，那么此时我们怎么办？</p>
<p>有两种方式：</p>
<ol>
<li>修改第三方库使其支持XML文件。（若没有第三方库源码，好像就没办法了；或者即便是有源码去）</li>
<li>将XML格式文件转换为JSON格式，提供个第三方库引用。（实现JSON和XML的相互转换）</li>
</ol>
<p>很明显方法2实现起来要比1各个方面都好很多（实现简单，提升工作效率，保证原有逻辑不变，使主逻辑便于后续维护），这便是适配器模式。</p>
<p><strong>解决方案：</strong>
  适配器模式主要应用于“希望复用一些现存的类，但是接口又与复用环境要求不一致”的情况，在遗留代码复用，类库迁移等方面非常有用。</p>
<p><strong>适配器模式本身要求我们尽可能地使用“面向接口的编程方式”，这样才能在后期很方便地适配。</strong></p>
<hr>
<h1 data-id="heading-2">三，结构</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53df5446b89544c3b941621b9147eeec~tplv-k3u1fbpfcp-watermark.image" alt="1.1" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>客户端 （Client） 是包含当前程序业务逻辑的类。</li>
<li>客户端接口 （Client Interface） 描述了其他类与客户端代码合作时必须遵循的协议。</li>
<li>服务 （Service） 中有一些功能类 （通常来自第三方或遗留系统）。 客户端与其接口不兼容， 因此无法直接调用其功能。</li>
<li>适配器 （Adapter） 是一个可以同时与客户端和服务交互的类： 它在实现客户端接口的同时封装了服务对象。 适配器接受客户端通过适配器接口发起的调用， 并将其转换为适用于被封装服务对象的调用。</li>
<li>客户端代码只需通过接口与适配器交互即可， 无需与具体的适配器类耦合。 因此， 你可以向程序中添加新类型的适配器而无需修改已有代码。 这在服务类的接口被更改或替换时很有用： 你无需修改客户端代码就可以创建新的适配器类。</li>
</ol>
<hr>
<h1 data-id="heading-3">四，优缺点</h1>
<p><strong>优点：</strong></p>
<ul>
<li><strong>单一职责原则</strong>：你可以将接口或数据转换代码从程序主要业务逻辑中分离。</li>
<li><strong>开闭原则</strong>： 只要客户端代码通过客户端接口与适配器进行交互， 你就能在不修改现有客户端代码的情况下在程序中添加新类型的适配器。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li><strong>代码整体复杂度增加</strong> ：因为需要新增一系列接口和类。 有时直接更改服务类使其与其他代码兼容会更简单。</li>
</ul>
<hr>
<h1 data-id="heading-4">五，应用场景</h1>
<p><strong>适用性：</strong></p>
<ul>
<li>当你希望使用某个类， 但是其接口与其他代码不兼容时， 可以使用适配器模式。</li>
</ul>
<p>适配器模式允许你创建一个中间层类， 其可作为代码与遗留类、 第三方类或提供怪异接口的类之间的转换器。</p>
<ul>
<li>
<p>当需要创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类。（即那些接口可能不一定兼容的类）</p>
</li>
<li>
<p>确保至少有两个类的接口不兼容：
一个无法修改 （通常是第三方、 遗留系统或者存在众多已有依赖的类） 的功能性服务类。
一个或多个将受益于使用服务类的客户端类。</p>
</li>
</ul>
<hr>
<h1 data-id="heading-5">六，代码实现</h1>
<p><strong>实现方式：</strong></p>
<ol>
<li>声明客户端接口， 描述客户端如何与服务交互。</li>
<li>创建遵循客户端接口的适配器类。 所有方法暂时都为空。</li>
<li>在适配器类中添加一个成员变量用于保存对于服务对象的引用。 通常情况下会通过构造函数对该成员变量进行初始化， 但有时在调用其方法时将该变量传递给适配器会更方便。</li>
<li>依次实现适配器类客户端接口的所有方法。 适配器会将实际工作委派给服务对象， 自身只负责接口或数据格式的转换。</li>
<li>客户端必须通过客户端接口使用适配器。 这样一来，就可以在不影响客户端代码的情况下修改或扩展适配器。</li>
</ol>
<p><strong>示例代码：</strong></p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">class</span> <span class="hljs-title">Project</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Main</span>(<span class="hljs-params"><span class="hljs-built_in">string</span>[] args</span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">"正常使用："</span>);
        Shoot shoot = <span class="hljs-keyword">new</span> Shoot();
        shoot.FireBullet();
        Console.WriteLine();

        Console.WriteLine(<span class="hljs-string">"对象适配："</span>);
        Cannon cannon = <span class="hljs-keyword">new</span> Cannon(shoot);
        cannon.FireGun();
        Console.WriteLine();


        Console.WriteLine(<span class="hljs-string">"类适配器："</span>);
        CannonClass cannonClass = <span class="hljs-keyword">new</span> CannonClass();
        cannonClass.FireGun();

        Console.ReadKey();
    &#125;

&#125;

<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 发射类 -- 被修饰的类 （被希望复用的现存的类）</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 包含对发射子弹的封装：</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 比如：发射速度，生效距离</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">class</span> <span class="hljs-title">Shoot</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">FireBullet</span>(<span class="hljs-params"></span>)</span>
    &#123;
        Console.WriteLine(<span class="hljs-string">" --- 被适配类 发射子弹 --- "</span>);
    &#125;
&#125;


<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 后续添加的接口 -- 需要适配的目标接口</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">interface</span> <span class="hljs-title">ICannon</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">FireGun</span>(<span class="hljs-params"></span>)</span>;
&#125;

<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 对象适配器 -- 实现目标接口，适配发射类</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">class</span> <span class="hljs-title">Cannon</span> : <span class="hljs-title">ICannon</span>
&#123;
    <span class="hljs-keyword">private</span> Shoot _Shoot;

    <span class="hljs-comment">//public Cannon()</span>
    <span class="hljs-comment">//&#123;</span>
    <span class="hljs-comment">//    this._Shoot = new Shoot();</span>
    <span class="hljs-comment">//&#125;</span>

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Cannon</span>(<span class="hljs-params">Shoot shoot</span>)</span>
    &#123;
        <span class="hljs-keyword">this</span>._Shoot = shoot;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">FireGun</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">this</span>._Shoot.FireBullet();
        <span class="hljs-comment">//使用一些Shoot的属性，来确定要发射什么样的炮弹</span>
        Console.WriteLine(<span class="hljs-string">" --- 对象适配 发射炮弹 --- "</span>);
    &#125;
&#125;

<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 类适配器 -- 实现目标接口，适配发射类</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> 只能借用继承来实现，不能多继承而且是紧耦合 （很少使用）</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
<span class="hljs-keyword">class</span> <span class="hljs-title">CannonClass</span> : <span class="hljs-title">Shoot</span>, <span class="hljs-title">ICannon</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">FireGun</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">base</span>.FireBullet();
        <span class="hljs-comment">//使用一些Shoot的属性，来确定要发射什么样的炮弹</span>
        Console.WriteLine(<span class="hljs-string">" --- 类适配器 发射炮弹 --- "</span>);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/338026cc035b4d4ea4a041ffbc3fd8ab~tplv-k3u1fbpfcp-watermark.image" alt="测试结果" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>设计模式系列博文示例代码工程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodechina.csdn.net%2FCzhenya%2Fcsharp_design_patterns" target="_blank" rel="nofollow noopener noreferrer" title="https://codechina.csdn.net/Czhenya/csharp_design_patterns" ref="nofollow noopener noreferrer">链接</a></p>
<hr>
<hr></div>  
</div>
            