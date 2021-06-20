
---
title: 'JS设计模式 - 工厂模式与抽象工厂模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7996758d366464fb1b08951c8dbcbbb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 02:33:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7996758d366464fb1b08951c8dbcbbb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与更文挑战的第19天，活动详情查看</strong>： <a href="https://juejin.cn/post/6967194882926444557" target="_blank"><strong>更文挑战</strong></a></p>
<p><a name="user-content-nXYPS" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-0">1. 构造函数模式</h1>
<p><a name="user-content-YdWaV" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-1">(1) JS中创建新对象的三种常用方法</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> newObject = &#123;&#125;;
 
<span class="hljs-keyword">var</span> newObject = <span class="hljs-built_in">Object</span>.create( <span class="hljs-built_in">Object</span>.prototype );
 
<span class="hljs-keyword">var</span> newObject = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();

<span class="hljs-comment">//上面的三中方式创建出来的新对象等同，Object.create(null)是一个简单的对象，不具有其他任何的属性。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-iRd3r" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">(2) 创建新属性的四中方式</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">newObject.someKey = <span class="hljs-string">"Hello World"</span>;
 
newObject[<span class="hljs-string">"someKey"</span>] = <span class="hljs-string">"Hello World"</span>;
 
<span class="hljs-built_in">Object</span>.defineProperty( newObject, <span class="hljs-string">"someKey"</span>, &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"for more control of the property's behavior"</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
&#125;);
 
<span class="hljs-built_in">Object</span>.defineProperties( newObject, &#123;
  <span class="hljs-string">"someKey"</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"Hello World"</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>
  &#125;,
 
  <span class="hljs-string">"anotherKey"</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"Foo bar"</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>
  &#125;
 
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​<br>
<a name="user-content-bC5cF" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-3">(3) 用法</h2>
<p><a name="user-content-HJqtq" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-4">普通方式（最实用）</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.model = model;
    <span class="hljs-built_in">this</span>.year = year;
    <span class="hljs-built_in">this</span>.miles = miles;
    <span class="hljs-built_in">this</span>.output= <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">"走了"</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">"公里"</span>;
    &#125;;
&#125;
 
<span class="hljs-keyword">var</span> car_benchi = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">'benchi'</span>, <span class="hljs-string">'2017'</span>, <span class="hljs-string">'300'</span>);
<span class="hljs-keyword">var</span> car_aodi = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">'aodi'</span>, <span class="hljs-string">'2016'</span>, <span class="hljs-string">'600'</span>);
 
<span class="hljs-built_in">console</span>.log(car_benchi.output === car_benchi.output); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么最后判断函数是否为同一个对象，因为之前在网上看到文章有说到这种方式在创建新对象的时候会创建多个匿名函数，造成内存问题。注意这里说的是这个匿名函数，不是output变量。<br></p>
<p>现在我们将上面new的方式用普通的函数实现，因为这个是需要用来和prototype & 工厂模式方式进行比较</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123;
    <span class="hljs-keyword">var</span> object = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
 
    <span class="hljs-comment">/*prototype*/</span>
    <span class="hljs-built_in">Object</span>.defineProperty( object, <span class="hljs-string">"__proto__"</span>, &#123;
        <span class="hljs-attr">value</span>: Car.prototype,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>
    &#125;)
 
    object.model = model;
    object.year = year;
    object.miles = miles;
 
    object.output = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">"走了"</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">"公里"</span>;
        &#125;.call(<span class="hljs-built_in">this</span>);
    &#125;
 
    <span class="hljs-keyword">return</span> object;
&#125;
 
<span class="hljs-keyword">var</span> car_benchi =  Car(<span class="hljs-string">'benchi'</span>, <span class="hljs-string">'2017'</span>, <span class="hljs-string">'300'</span>);
<span class="hljs-keyword">var</span> car_aodi =  Car(<span class="hljs-string">'aodi'</span>, <span class="hljs-string">'2016'</span>, <span class="hljs-string">'600'</span>);
 
<span class="hljs-built_in">console</span>.log(car_benchi.output === car_benchi.output); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于创建的对象使用的是Object.create(null)，以及__proto__属性使用Object.defineProperty的原因是什么呢？<br></p>
<p>因为使用new创建的对象是具有原型链的，所以我需要使用__proto__,然后这个属性是可写，不可枚举，不可配置的。至于为什么是不可配置的，是因为当我使用var object = &#123;&#125; / new Object()的时候，我是用defineProperty是不起效果的。所以用了 Object.create(null)的方式，这个也是今天自己测试的时候注意到的。<br></p>
<p>Note： 开发过程中一般不允许操作__proto__的，尽管现在大部分浏览器引起都已经支持。<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7996758d366464fb1b08951c8dbcbbb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<a name="user-content-uVCGA" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-5">prototype</h3>
<p>解决上面的问题其实可以将output函数提到最外层也可以，只是这样不好维护，而且污染了全局变量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.model = model;
    <span class="hljs-built_in">this</span>.year = year;
    <span class="hljs-built_in">this</span>.miles = miles;
&#125;
 
Car.prototype.output= <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">"走了"</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">"公里"</span>;
&#125;;
 
<span class="hljs-keyword">var</span> car_benchi = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">'benchi'</span>, <span class="hljs-string">'2017'</span>, <span class="hljs-string">'300'</span>);
<span class="hljs-keyword">var</span> car_aodi = <span class="hljs-keyword">new</span> Car(<span class="hljs-string">'aodi'</span>, <span class="hljs-string">'2016'</span>, <span class="hljs-string">'600'</span>);
 
<span class="hljs-built_in">console</span>.log(car_aodi.output === car_benchi.output); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这里是在Car.prototype上添加了一个新的方法。因为针对多个对象共享只有找到公共点，那就是原型链上的Car.prototype。切记不要重新赋值Car.prototype,因为如果改了的话，原型链会被破坏。<br>​</p>
<h2 data-id="heading-6">(4) 总结</h2>
<p>本人现在用到prototype的地方基本上是为了一些js内置对象的扩展，例如如期格式，数组变化，因为这样可以让我省去时间去为每个对象进行修改。<br>
<br>构造函数的本质我认为还是在它的原型链，是为了找共同点，因为原型链是大家共有的，而且是一个js原生的对象。不用我们自己去维护。
<br><br><br></p>
<p><a name="user-content-oSbqN" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-7">2. 工厂模式</h1>
<p>工厂模式类比到现实生活中的工厂，可以产生大量相似的商品，去做同样的事情，实现同样的效果。但是这样的话岂不是感觉完全可以用构造函数模式实现，而且我还可以拥有原型链。<br>​</p>
<p>现在假设有一家工厂之前只可以加工生产奔驰一款车，那么它的生产过程是一个工厂模式还是构造函数模式呢。这个很难说，为什么呢？因为如果它每一个阶段只会生产一个型号的车，那么我们是不是可以当作是一个构造函数模式，因为现在所做的事情都是一样的，同样的输入输出。我们是不是可以把这个工厂直接看作是一个new，每一次生产出一个新的奔驰车。说到这里请看一下上面的那个new的方式用普通的函数实现，我们现在的工厂就是在做这样的事情（如果不适用new的话），当前情况下，本人认为二者是相等的。<br>​</p>
<p>好了现在，我们的工厂在生产新的产品的时候发现之前的一款车有很好的市场，所以在开发新的汽车型号的时候，还要生产以前的汽车，现在我们在使用之前的方法不行了。因为我需要有不同的输入输出。那么我们先将上面的方式改写一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car</span>(<span class="hljs-params">model, year, miles, version</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">carBasicInformation</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> object = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
 
        <span class="hljs-comment">/*prototype*/</span>
        <span class="hljs-built_in">Object</span>.defineProperty( object, <span class="hljs-string">"__proto__"</span>, &#123;
            <span class="hljs-attr">value</span>: Car.prototype,
            <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>
        &#125;)
 
        object.model = model;
        object.year = year;
        object.miles = miles;
 
        object.output = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">"走了"</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">"公里"</span>;
            &#125;.call(<span class="hljs-built_in">this</span>);
        &#125;
 
        <span class="hljs-keyword">return</span> object;
    &#125;
 
    <span class="hljs-comment">//0001型号有导航系统</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car_0001</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> car_0001 = carBasicInformation(model, year, miles);
        car_0001.omnirange = <span class="hljs-string">'omnirange_01'</span>; 
 
        <span class="hljs-keyword">return</span> car_0001;
    &#125;
 
    <span class="hljs-comment">//0002型号没有导航系统 </span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Car_0002</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> car_0002 = carBasicInformation(model, year, miles);
 
        <span class="hljs-keyword">return</span> car_0002;
    &#125;
 
    <span class="hljs-keyword">switch</span> (version) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'0001'</span>:
            <span class="hljs-keyword">return</span> Car_0001();
        <span class="hljs-keyword">case</span> <span class="hljs-string">'0002'</span>:
            <span class="hljs-keyword">return</span> Car_0002();
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">break</span>; <span class="hljs-comment">//当然工厂肯定不会什么都不做。</span>
    &#125;
&#125;
 
<span class="hljs-keyword">var</span> aodi_0001 =  Car(<span class="hljs-string">'benchi'</span>, <span class="hljs-string">'2017'</span>, <span class="hljs-string">'300'</span>, <span class="hljs-string">'0001'</span>);
<span class="hljs-keyword">var</span> aodi_0002 =  Car(<span class="hljs-string">'aodi'</span>, <span class="hljs-string">'2016'</span>, <span class="hljs-string">'600'</span>, <span class="hljs-string">'0002'</span>);
 
<span class="hljs-built_in">console</span>.log(aodi_0001.omnirange); <span class="hljs-comment">//omnirange_01</span>
<span class="hljs-built_in">console</span>.log(aodi_0002.omnirange); <span class="hljs-comment">//undeinfed</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我认为现在这个应用方式才是工厂模式的意义，在于不同的输入输出。可能会有人提问到，我完全可以在把这些判断逻辑写到以前的new car()的内部去判断，那么我岂不是还是构造函数模式？<br></p>
<p>确实是这样，那么我们来分析一下这个判断的逻辑是个什么东西。是说需要两种不同的车型，这是一个业务逻辑，我们将上面的代码对应到工厂的角色中，Car是工厂，Car_0001和Car_0002是两个不同的组。判断逻辑是市场部的工作人员。Car_0001和Car_0002是构造函数模式，因为我做的是同一个东西，判断逻辑肯定是市场部的人在分析市场需求得到的。那么跟据面向对象也好，还是模块话开发也好，Car_0001和Car_0002是不是应该只做自己的事情，毕竟每种车生产什么车，肯定是业务逻辑决定代码结构。如果我们将所有的内容放在一起，改了car_0001的东西会不会影响到car_0002的内容，同时也违反了开放-封闭原则，而且以后有了新的型号生产，是不是还需要改已经稳定了两种型号的代码，维护起来很负责。<br>
<br>提到开放-封闭原则：软件实体应该是可扩展，而不可修改的。也就是说，对扩展是开放的，而对修改是封闭的。那么如果有了新的型号，我们还是需要去修改上面的代码，因为啥，因为业务逻辑判断就是这样。<br></p>
<p>所以上面的代码也不是完善的，还是需要修改的。相信大家还记的上面的信息prototype。我们可在上面添加新的东西而且不影响其他的功能。<br>​<br><br>
<a name="user-content-v7B72" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-8">3. 抽象工厂模式</h1>
<p>对于工厂模式的进一步就是抽象工厂。现在我们先思考一下上面的需求，需要添加新的version，但是又不想修改已经稳定的代码，但是还是有着共同的东西，总结一句话就是‘求同存异’。<br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//求同</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">basicCarInformation</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123; <span class="hljs-comment">//这个地方其实可以不用这么复杂，只是本人太懒，直接将上面的代码copy了。</span>
    <span class="hljs-keyword">var</span> object = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
 
        <span class="hljs-comment">/*prototype*/</span>
        <span class="hljs-built_in">Object</span>.defineProperty( object, <span class="hljs-string">"__proto__"</span>, &#123;
            <span class="hljs-attr">value</span>: basicCarInformation.prototype,
            <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>
        &#125;)
 
        object.model = model;
        object.year = year;
        object.miles = miles;
 
        object.output = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model + <span class="hljs-string">"走了"</span> + <span class="hljs-built_in">this</span>.miles + <span class="hljs-string">"公里"</span>;
            &#125;.call(<span class="hljs-built_in">this</span>);
        &#125;
 
        <span class="hljs-keyword">return</span> object;
&#125;
 
inheritAbstactFactory.prototype.basicCarInformation = basicCarInformation;
 
<span class="hljs-comment">//存异</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inheritAbstactFactory</span>(<span class="hljs-params">option, version</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">model, year, miles</span>) </span>&#123;
        <span class="hljs-keyword">var</span> basicInformation = basicCarInformation(model, year, miles);
        basicInformation.option = option;
        basicInformation.version = version;
 
        <span class="hljs-keyword">return</span> basicInformation;
    &#125;
&#125;
 
<span class="hljs-keyword">var</span> CarFactory0001 = inheritAbstactFactory(&#123;<span class="hljs-attr">omnirange</span> : <span class="hljs-string">'omnirange_01'</span>&#125;, <span class="hljs-string">'aodi_0001'</span>);
 
<span class="hljs-keyword">var</span> aodi_0001 =  CarFactory0001(<span class="hljs-string">'benchi'</span>, <span class="hljs-string">'2017'</span>, <span class="hljs-string">'300'</span>);
aodi_0001.output();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们再有新的version，只需要执行var CarFactory0001 = inheritAbstactFactory(&#123;omnirange : 'omnirange_01'&#125;, 'aodi_0001');添加新的version，就好了。<br></p>
<p>注意： var basicInformation = basicCarInformation(model, year, miles); 这一行的实现可以是内部函数，或者使用寄生构造函数的方式。这里采用prototype是为了对比面向对象语言，现在basicCarInformation就是base类，inheritAbstactFactory抽象类，CarFactory0001继承抽象类的子类，具体的不同可以由子类自己去创建。当然可以使用另外两种方式，毕竟工厂模式的关注点不在这里。<br></p>
<p>上面的求同是一个构造函数模式，存异是工厂模式（求同是基础）。二者的关注点不同。<br>​<br><br>
<a name="user-content-RpsZf" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-9">4. 抽象工厂的应用</h1>
<p>（摘抄与 <a href="https://addyosmani.com/resources/essentialjsdesignpatterns/book/index.html#factorypatternjavascript" target="_blank" rel="nofollow noopener noreferrer">design pattern</a>）当应用于以下情况时，工厂模式可能特别有用：<br></p>
<ul>
<li>当我们的对象或组件设置涉及高度的复杂性时</li>
<li>当我们需要根据我们所处的环境轻松生成不同的对象实例时</li>
<li>当我们正在处理许多共享相同属性的小对象或组件时</li>
<li>使用其他对象的实例组合对象时，只需要满足API合约（又名 duck typing）的工作。这对于解耦是有用的。</li>
</ul>
<p>分析一下上面的几句话：</p>
<ul>
<li>高度的负复杂性指的就是上面的逻辑判断</li>
<li>需求的变化</li>
<li>求同存异，许多共享并不是全部共享，因为全部共享的话就直接构造函数模式了</li>
<li>这里的的意义是说care的只是输入输出，至于对象是否与原型链相关不在意，就好像call,apply的用法。就是一种duck typing。</li>
</ul>
<p><a href="https://blog.csdn.net/It_rod/article/details/78636588" target="_blank" rel="nofollow noopener noreferrer"><br></a></p></div>  
</div>
            