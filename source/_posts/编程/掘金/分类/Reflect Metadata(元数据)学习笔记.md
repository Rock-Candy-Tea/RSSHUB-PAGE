
---
title: 'Reflect Metadata(元数据)学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3244'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 22:37:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=3244'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">decorate方法</h3>
<p><code>declare type ClassDecorator = <TFunction exntends Function>(target: TFunction) ⇒ TFunction | void;</code></p>
<p><code>function decorate(decorators: ClassDecorator[], target: Function): Function;</code></p>
<ul>
<li>
<p>对类的装饰</p>
<p>对类的装饰该方法有几个参数, 分别是:</p>
<ul>
<li>@param &#123;Array&#125; decorators - 装饰器的数组</li>
<li>@param &#123;Object&#125; target - 目标对象</li>
<li>@returns 返回应用提供的装饰器后的值</li>
<li>注意: 装饰器应用是与array的位置方向相反, 为从右往左.</li>
</ul>
<p>来个🌰：给TestCkassDecorator类添加或者修改sayName方法</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> classDecorator: ClassDecorator = <span class="hljs-function"><span class="hljs-params">target</span> =></span> &#123;
  target.prototype.sayName = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'veloma'</span>);
<span class="hljs-comment">// return target; 这里可以return也可以不return, 因为target是一个对象引用</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestClassDecorator</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name = <span class="hljs-string">''</span></span>)</span> &#123;&#125;
<span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
&#125;

<span class="hljs-built_in">Reflect</span>.decorate([classDecorator], TestClassDecorator); <span class="hljs-comment">// 对类进行修饰</span>
<span class="hljs-keyword">const</span> t = <span class="hljs-keyword">new</span> TestClassDecorator(<span class="hljs-string">'nihao'</span>);

t.sayName(); <span class="hljs-comment">// veloma</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：<strong>在classDecorator中传入的target, 只能修改其prototype的方法, 不能修改其属性, 因为其属性是</strong><code>ready-only</code></strong></p>
</li>
<li>
<p>对属性或方法的装饰</p>
<p>对属性或方法的修饰有几个参数, 分别是:</p>
<ul>
<li>@param &#123;Array&#125;  decorators - 装饰器的集合</li>
<li>@param &#123;Object&#125; target - 目标对象</li>
<li>@param &#123;string&#125; key - 要装饰的属性名称</li>
<li>@param &#123;Object&#125; descriptor - 该属性的描述</li>
</ul>
<p>注意: descriptor分为两种, 一种是数据描述符, 一种是存取描述符</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 数据描述符</span>
&#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">'aaa'</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
&#125;
<span class="hljs-comment">// 存取描述符</span>
&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>&#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set'</span>) &#125;,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>属性装饰器: AOP编程, 在原方法的后面加上操作</strong></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> propertyDecorator: PropertyDecorator = <span class="hljs-function">(<span class="hljs-params">target, propertyKey</span>) =></span> &#123;
<span class="hljs-keyword">const</span> origin = target[propertyKey];
    target[propertyKey] = <span class="hljs-function">() =></span> &#123;
      origin.call(target);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'added override'</span>);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PropertyAndMethodExample</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticProperty</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'im static property'</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'im one instance method'</span>);
    &#125;
&#125;

<span class="hljs-comment">// 装饰PropertyAndMethodExample的staticProperty方法(静态方法)</span>
<span class="hljs-built_in">Reflect</span>.decorate([propertyDecorator], PropertyAndMethodExample, <span class="hljs-string">'staticProperty'</span>);
PropertyAndMethodExample.staticProperty(); <span class="hljs-comment">// im static property \n added override</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法装饰器</strong></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> methodDecorator: MethodDecorator = <span class="hljs-function">(<span class="hljs-params">target, propertyKey, descriptor</span>) =></span> &#123;
<span class="hljs-comment">// 将其描述改为不可编辑</span>
descriptor.configurable = <span class="hljs-literal">false</span>;
descriptor.writable = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">return</span> descriptor;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PropertyAndMethodExample</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticProperty</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'im static property'</span>);
    &#125;

<span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'im one instance method'</span>);
&#125;
&#125;

<span class="hljs-comment">// 获取原descriptor</span>
<span class="hljs-keyword">let</span> descriptor = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(PropertyAndMethodExample.prototype, <span class="hljs-string">'method'</span>);

<span class="hljs-comment">// 获取修改后的descriptor</span>
descriptor = <span class="hljs-built_in">Reflect</span>.decorate([methodDecorator], PropertyAndMethodExample, <span class="hljs-string">'method'</span>, descriptor);
<span class="hljs-comment">// 将修改后的descriptor添加到对应的方法上</span>
<span class="hljs-built_in">Reflect</span>.defineProperty(PropertyAndMethodExample.prototype, <span class="hljs-string">'method'</span>, descriptor);

<span class="hljs-keyword">const</span> example = <span class="hljs-keyword">new</span> PropertyAndMethodExample();
example.method = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'override'</span>); <span class="hljs-comment">// 报错: 因为已经将该方法(属性)的writable描述符设置为false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-1">metadata方法</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">metadataKey</span></span> - 元数据入口的key
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>metadataValue 元数据入口的value
* <span class="hljs-doctag">@returns </span>装饰器函数
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">metadata</span>(<span class="hljs-params">metadataKey: <span class="hljs-built_in">any</span>, metadataValue: <span class="hljs-built_in">any</span></span>) </span>&#123;
    (target: <span class="hljs-built_in">Function</span>): <span class="hljs-built_in">void</span>;
    (target: <span class="hljs-built_in">Object</span>, <span class="hljs-attr">propertyKey</span>: <span class="hljs-built_in">string</span> | symbol): <span class="hljs-built_in">void</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实例</strong></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> nameSymbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'veloma'</span>);

<span class="hljs-comment">// 类元数据</span>
<span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'class'</span>, <span class="hljs-string">'class'</span>);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MetaDataClass</span> </span>&#123;
    <span class="hljs-comment">// 实例属性元数据</span>
    <span class="hljs-meta">@Reflect</span>.metadata(nameSymbol, <span class="hljs-string">'nihao'</span>)
    <span class="hljs-keyword">public</span> name = <span class="hljs-string">'origin'</span>;

    <span class="hljs-comment">// 实例方法元数据</span>
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'getName'</span>, <span class="hljs-string">'getName'</span>)
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-comment">// 静态方法元数据</span>
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'static'</span>, <span class="hljs-string">'static'</span>)
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticMethod</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 创建元数据类的实例</span>
<span class="hljs-keyword">const</span> metadataInstance = <span class="hljs-keyword">new</span> MetaDataClass();

<span class="hljs-comment">// 获取MetaDataClass的name元数据</span>
<span class="hljs-keyword">const</span> value = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'name'</span>, MetaDataClass); <span class="hljs-comment">// undefined</span>
<span class="hljs-comment">// 获取实例中name属性的nameSymbol元数据</span>
<span class="hljs-keyword">const</span> name = <span class="hljs-built_in">Reflect</span>.getMetadata(nameSymbol, metadataInstance, <span class="hljs-string">'name'</span>); <span class="hljs-comment">// nihao</span>
<span class="hljs-comment">// 获取实例中getName属性的getName元数据</span>
<span class="hljs-keyword">const</span> methodVal = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'getName'</span>, metadataInstance, <span class="hljs-string">'getName'</span>); <span class="hljs-comment">// getName</span>
<span class="hljs-comment">// 获取元数据类的staticMethod属性的static元数据</span>
<span class="hljs-keyword">const</span> staticVal = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'static'</span>, MetaDataClass, <span class="hljs-string">'staticMethod'</span>); <span class="hljs-comment">// static</span>

<span class="hljs-built_in">console</span>.log(value, name, methodVal, staticVal); <span class="hljs-comment">// undefined nihao getName static</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">defineMetadata方法</h3>
<p>该方法是<code>metadata</code>的定义版本, 也就是非@版本, 会多穿一个参数<code>target</code>, 表示待装饰的对象</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">metadataKey</span></span> - 设置或获取时的key
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">metadataValue</span></span> - 元数据内容
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> <span class="hljs-variable">target</span></span> - 待装饰的target
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">targetKey</span></span> - target的property
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineMetadata</span>(<span class="hljs-params">metadataKey: <span class="hljs-built_in">any</span>, metadataValue: <span class="hljs-built_in">any</span>, target: <span class="hljs-built_in">Object</span>, targetKey: <span class="hljs-built_in">string</span> | symbol</span>): <span class="hljs-title">void</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DefineMetadata</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticMethod</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
    <span class="hljs-keyword">static</span> staticProperty = <span class="hljs-string">'static'</span>;
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-string">'type'</span>;
<span class="hljs-comment">// 给DefineMetadata设置元数据type, 值为class</span>
<span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'class'</span>, DefineMetadata);
<span class="hljs-comment">// 给DefineMetadata.staticMethod设置元数据type, 值为staticMethod</span>
<span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'staticMethod'</span>, DefineMetadata.staticMethod);
<span class="hljs-comment">// 给DefineMeatadata.prorotype.getName设置元数据type, 值为method</span>
<span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'method'</span>, DefineMetadata.prorotype.getName);
<span class="hljs-comment">// 给DefineMetadata的staticProperty属性设置元数据type, 值为staticProperty</span>
<span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'staticProperty'</span>, DefineMetadata, <span class="hljs-string">'staticProperty'</span>);

<span class="hljs-comment">// 获取DefineMetadata身上的type元数据</span>
<span class="hljs-keyword">const</span> t1 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata); <span class="hljs-comment">// class</span>
<span class="hljs-comment">// 获取DefineMetadata.staticMethod身上的type元数据</span>
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata.staticMethod); <span class="hljs-comment">// staticMethod</span>
<span class="hljs-comment">// 获取DefineMetadata.prototype.getName身上的type元数据</span>
<span class="hljs-keyword">const</span> t3 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata.prototype.getName); <span class="hljs-comment">// method</span>
<span class="hljs-comment">// 获取DefineMetadata上staticProperty属性的type元数据</span>
<span class="hljs-keyword">const</span> t4 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata, <span class="hljs-string">'staticProperty'</span>); <span class="hljs-comment">// staticProperty</span>

<span class="hljs-built_in">console</span>.log(t1, t2, t3, t4); <span class="hljs-comment">// class staticMethod method staticProperty</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: t4定义和获取不一样的地方, 比如t2到t3都有两种写法, 一种就是将target转换为对应的对象且必须是对象, 以t2为例, 也可以写为</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'staticMethods'</span>, DefineMetadata, <span class="hljs-string">'staticMethod'</span>);
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata, <span class="hljs-string">'staticMethod'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: 这两种方式不能混合使用, 比如下面这种是不对的:</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'staticMethod'</span>, DefineMetadata, <span class="hljs-string">'staticMethod'</span>);
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-keyword">type</span>, DefineMetadata.staticMethod);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">hasMetadata方法</h3>
<p>该方法返回布尔值, 表明该target或其原型链上有没有对应的元数据</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">metadataKey</span></span> - 元数据的key
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;Obejct&#125;</span> <span class="hljs-variable">target</span></span> - 定义的对象
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">targetKey</span></span> - 定义对象的属性(重载参数), 可选
* <span class="hljs-doctag">@returns </span>在target或其原型链上返回true.
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasMetadata</span>(<span class="hljs-params">metadataKey: <span class="hljs-built_in">string</span>, target: <span class="hljs-built_in">Object</span>, targetKey?: symbol | <span class="hljs-built_in">string</span></span>): <span class="hljs-title">boolean</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-string">'type'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HasMetadataClass</span> </span>&#123;
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'staticProperty'</span>)
    <span class="hljs-keyword">static</span> staticProperty = <span class="hljs-string">''</span>;
&#125;

<span class="hljs-comment">// 给HasMetadataClass定义一个type元数据, 值为class</span>
<span class="hljs-built_in">Reflect</span>.defineMetadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'class'</span>, HasMetadataClass);
<span class="hljs-keyword">const</span> t1 = <span class="hljs-built_in">Reflect</span>.hasMetadata(<span class="hljs-keyword">type</span>, HasMetadataClass); <span class="hljs-comment">// true</span>
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.hasMetadata(<span class="hljs-keyword">type</span>, HasMetadataClass, <span class="hljs-string">'staticProperty'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(t1, t2); <span class="hljs-comment">// true true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其余的像实例属性/方法, 静态方法都以此类推</p>
<p><strong>hasOwnMetadata方法</strong></p>
<p>跟<code>Object.prototype.hasOwnProperty</code>类似, 是只查找对象上的元数据, 而不会继续想上查找原型链上的, 其余的跟hasMetadata一致</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-string">'type'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'getName'</span>)
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'class'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HasOwnMetadataClass</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'static'</span>)
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticProperty</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'method'</span>)
    <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 判断HasOwnMetadataClass有没有type这个元数据</span>
<span class="hljs-keyword">const</span> t1 = <span class="hljs-built_in">Reflect</span>.hasOwnProperty(<span class="hljs-keyword">type</span>, HasOwnMetadataClass); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 判断HasOwnMetadataClass的staticProperty属性有没有type这个元数据</span>
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.hasOwnMetadata(<span class="hljs-keyword">type</span>, HasOwnMetadataClass, <span class="hljs-string">'staticProperty'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 判断HasOwnMetadataClass.prototype的method属性有没有type这个元数据</span>
<span class="hljs-keyword">const</span> t3 = <span class="hljs-built_in">Reflect</span>.hasOwnMetadata(<span class="hljs-keyword">type</span>, HasOwnMetadataClass.prototype, <span class="hljs-string">'method'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 判断HasOwnMetadataClass.prototype的getName属性有没有type这个元数据</span>
<span class="hljs-keyword">const</span> t4 = <span class="hljs-built_in">Reflect</span>.hasOwnMetadata(<span class="hljs-keyword">type</span>, HasOwnMetadataClass.prototype, <span class="hljs-string">'getName'</span>); <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 判断HasOwnMetadataClass.prototype的getName属性有没有type这个元数据, 这里的结果为true, 因为HasOwnMetadata.prototype上面没有这个属性, 但是HasOwnMetadata的原型链上有getName这个属性</span>
<span class="hljs-keyword">const</span> t5 = <span class="hljs-built_in">Reflect</span>.hasMetadata(<span class="hljs-keyword">type</span>, HasOwnMetadataClass.prototype, <span class="hljs-string">'getName'</span>); <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(t1, t2, t3, t4, t5); <span class="hljs-comment">// true true true false true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: t4和t5的区别</p>
<p><strong>getMetadata方法</strong></p>
<p>这个属性在之前验证各个属性的时候就已经使用过了, 就是用于获取target的元数据值, 会往原型链上找</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">metadataKey</span></span> - 元数据key
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> <span class="hljs-variable">target</span></span> - 元数据定义的target
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">targetKey</span></span> - 可选项, 是否选择target的某个key
* <span class="hljs-doctag">@returns </span>如果找到了元数据则返回元数据值, 否则返回undefined
**/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getMetadata</span>(<span class="hljs-params">metadataKey: <span class="hljs-built_in">string</span>, target: <span class="hljs-built_in">Object</span>, targetKey?: <span class="hljs-built_in">string</span> | symbol</span>): <span class="hljs-title">any</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>getOwnMetadata方法</strong></p>
<p>与hasOwnMetadata和hasMetadata的区别一样, 是否往原型链上找</p>
<p><strong>getMetadataKeys方法</strong></p>
<p>类似<code>Object.keys</code>, 返回该target以及原型链上target的所有元数据的keys</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-string">'type'</span>;
<span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'parent'</span>, <span class="hljs-string">'parent'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'class'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HasOwnMetadataClass</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'static'</span>)
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticProperty</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'bbb'</span>, <span class="hljs-string">'method'</span>)
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'aaa'</span>, <span class="hljs-string">'method'</span>)
    <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 获取HasOwnMetadataClass身上以及原型链上的所有元数据</span>
<span class="hljs-keyword">const</span> t1 = <span class="hljs-built_in">Reflect</span>.getMetadataKeys(HasOwnMetadataClass); <span class="hljs-comment">// type parent</span>
<span class="hljs-comment">// 获取HasOwnMetadataClass中method属性身上的以及原型链上的所有元数据</span>
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.getMetadataKeys(HasOwnMetadataClass.prototype, <span class="hljs-string">'method'</span>); <span class="hljs-comment">// aaa bbb</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>t1很好理解, 因为会向上找原型链的parent, t2好像多了一些东西, desingn: 开头的, 先不管他, 看看aaa 和 bbb 的顺序是和我们添加的顺序是相反的, 还记得之前说过装饰器的顺序是从右到左的, 所以先应用bbb aaa在应用design:</p>
<p><strong>getOwnMetadataKeys方法</strong></p>
<p>跟getMetadataKeys一样, 只是不向原型链中查找</p>
<p><strong>deleteMetadata方法</strong></p>
<p>用于删除元数据</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">/**
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">metadataKey</span></span> - 元数据key
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> <span class="hljs-variable">target</span></span> - 元数据定义的对象
* <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">targetKey</span></span> - 对象对应的key, 可选参数
* <span class="hljs-doctag">@returns </span>如果对象上有该元数据, 返回true, 否则返回false
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deleteMetadata</span>(<span class="hljs-params">metadataKey: <span class="hljs-built_in">string</span>, target: <span class="hljs-built_in">Object</span>, targetKey?: symbol | <span class="hljs-built_in">string</span></span>): <span class="hljs-title">boolean</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-string">'type'</span>;
<span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'class'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DeleteMetadata</span> </span>&#123;
    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-keyword">type</span>, <span class="hljs-string">'static'</span>)
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">staticMethod</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 删除DeleteMetadata身上的type元数据</span>
<span class="hljs-keyword">const</span> res1 = <span class="hljs-built_in">Reflect</span>.deleteMetadata(<span class="hljs-keyword">type</span>, DeleteMetadata); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 删除DeleteMetadata上staticMethod属性身上的type元数据</span>
<span class="hljs-keyword">const</span> res2 = <span class="hljs-built_in">Reflect</span>.deleteMetadata(<span class="hljs-keyword">type</span>, DelteMetadata, <span class="hljs-string">'staticMethod'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 再次删除DelelteMetadata身上的type元数据, 这次返回false, 因为在之前已经删除过了</span>
<span class="hljs-keyword">const</span> res3 = <span class="hljs-built_in">Reflect</span>.deleteMetadata(<span class="hljs-keyword">type</span>, DelteMetadata); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(res1, res2, res3); <span class="hljs-comment">// true true false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>design:</strong></p>
<p>好了还有一个问题没有解决, 就是之前说的在getMetadataKey时出现的<code>design:xxx</code>的内容是怎么来的, 表示什么意思呢?<code>design:type</code> 表示被装饰的对象是什么类型, 比如是字符串? 数字? 还是函数等. <code>design:paramtypes</code> 表示被装饰对象的参数类型, 是一个表示类型的数组, 如果不是函数, 则没有该key.<code>design:returntype</code> 表示被装饰对象的返回值属性, 比如字符串, 数字或函数等.</p>
<p>示例</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-string">'type'</span>, <span class="hljs-string">'class'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">public</span> age: <span class="hljs-built_in">number</span></span>)</span> &#123;&#125;

    <span class="hljs-meta">@Reflect</span>.metadata(<span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>)
    method(): <span class="hljs-built_in">boolean</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
&#125;

<span class="hljs-comment">// 获取A的design:paramtypes元数据</span>
<span class="hljs-keyword">const</span> t1 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'design:paramtypes'</span>, A); <span class="hljs-comment">// [[Function: String], [Function: Number]]</span>
<span class="hljs-comment">// 获取A.prototype上的method属性的design:returntype元数据</span>
<span class="hljs-keyword">const</span> t2 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'design:returntype'</span>, A.prototype, <span class="hljs-string">'method'</span>); <span class="hljs-comment">// [Function: Boolean]</span>
<span class="hljs-comment">// 获取A.prototype上的method属性的design:type元数据</span>
<span class="hljs-keyword">const</span> t3 = <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">'design:type'</span>, A.prototype, <span class="hljs-string">'method'</span>); <span class="hljs-comment">// [Function: Function]</span>

<span class="hljs-built_in">console</span>.log(t1, t2, t3); <span class="hljs-comment">// [[Function: String], [Function: Number], [Function: Boolean], [Function: Function]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意:</p>
<ol>
<li>没有装饰的target是get不到这些metadata的</li>
<li>必须手动指定类型, 无法进行推断, 比如method方法如果不指定, 返回值为<code>boolean</code>, 那么t2将是<code>undefined</code></li>
<li>应用的顺序为: <code>type → paramtypes → returntype</code></li>
</ol></div>  
</div>
            