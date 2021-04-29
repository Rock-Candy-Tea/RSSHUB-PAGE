
---
title: '谈谈装饰器模式在js中的应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208c2558984443b4880f08562e15da4b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 01:44:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208c2558984443b4880f08562e15da4b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>最近项目中使用了装饰器模式的思想，虽然装饰器听起来很简单，学习了一些资料之后，发现装饰器设计模式是一种在项目中使用频率很高的一种设计思想。本文希望通过以点带面的形式，对装饰器如何优雅的在项目中应用做一个总结～</p>
</blockquote>
<h1 data-id="heading-0">装饰器概念</h1>
<p>在开发过程中，很多时候我们不想要类的功能一开始就很庞大，一次性包含很多职责（毕竟程序员一直恪守着封装抽象bababa等概念）。这个时候我们可以使用装饰器模式。动态的给某个对象添加一些职责，并且不会影响从这个类派生的其他对象。</p>
<p>在传统的面向对象开发中，给对象添加功能时，我们通常会采用继承的方式，继承的方式目的是为了复用，但是随之而来也带来一些问题：</p>
<p>（1）父类和子类存在强耦合的关系，当父类改变时，子类也需要改变；</p>
<p>（2）子类需要知道父类中的细节，至少需要知道接口名，从而进行复用或复写，这样其实破坏了封装性；</p>
<p>（3）继承的方式，可能会创建出大量子类。比如现在有BBA三种类型的汽车，构造了一个汽车基类，三个三种类型的汽车。现在需要给汽车装上雾灯、前大灯、导航仪、刮雨器，如果采用继承的方式，那么就要构建3*4个类。但是如果把雾灯、前大灯、导航仪、刮雨器动态地添加到汽车上，那么只需要增加4个类。这种采用动态添加职责的方式就是装饰器。</p>
<p>装饰器的目的就是在不改变原来类的基础上，为其在运行期间动态的添加职责。</p>
<h1 data-id="heading-1">用AOP装饰函数</h1>
<p>这里为什么要讨论到AOP呢？我们后面来回答这个疑问。</p>
<p>我们先回顾一下OOP（Object Oriented Programing），OOP作为面向对象编程模式，取得了巨大的成功应用，主要思想是封装、继承和多态。</p>
<p>而AOP是一种新的编程方式，它和OOP不同，OOP把系统看成多个对象的交互，AOP把系统分为不同的关注点，或者称之为切面（Aspect）。</p>
<p>AOP（Aspect Oriented Programing），意为面向切面编程，通过预编译方式和动态代理的方式实现程序功能时统一维护的一种技术。 主要就是把与业务逻辑无关的功能抽离开来，这些与业务逻辑无关的功能常见有数据统计、函数执行时间、权限控制、异常处理等。把这些功能抽离出来后，再在通过动态切入的方式注入业务逻辑中。这样做的好处是可以保证业务内部的高内聚和业务模块之间的低耦合，从而可以方便复用与业务逻辑无关的模块。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208c2558984443b4880f08562e15da4b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里为什么要把装饰器和AOP结合起来讨论呢？</p>
<p>从上面的描述中，会发现AOP和装饰器模式概念很像，但装饰器注重的是装饰，而AOP注重的是横切面统一维护。两者其实最终都是要解决同一个问题，就是提高编程的低耦合与高可复用性。</p>
<p>说了这么多，还是有点抽象，我们来看看实际例子，如何使用AOP在项目中应用。</p>
<h1 data-id="heading-2">AOP的实现（ES5版）</h1>
<p>AOP是Java Spring中最重要的功能之一，使用过的同学一定知道，其内分为3种通知，before（前置通知）、after（后置通知）、arround（环绕通知）。我们来模拟AOP中before和after的实现。</p>
<h2 data-id="heading-3">before（前置通知）</h2>
<p>顾名思义，就是在函数调用之前执行。</p>
<pre><code class="copyable">Function.prototype.before = function (beforefn) &#123;
  var __self = this;
  return function () &#123;
    beforefn.apply(this, arguments);
    return __self.apply(this, arguments);
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">after（后置通知）</h2>
<p>与before相反，在函数调用之后执行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Function</span>.prototype.after = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">afterfn</span>) </span>&#123;
  <span class="hljs-keyword">var</span> __self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> ret = __self.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    afterfn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    <span class="hljs-keyword">return</span> ret;
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">日志记录上报例子</h2>
<p>接下来我们以数据上报为例子，讲讲如何用AOP来装饰函数。</p>
<p>比如页面有一个分享按钮，点开之后会弹出分享框分享给某人，点击完毕后，需要进行数据上报。这个时候，通常的方式，我们会这样去实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"share"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"share"</span>></span>点击打开分享框<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span> 
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> showShare = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"打开分享框"</span>);
        log(<span class="hljs-string">"打开分享框"</span>);
    &#125;;
    <span class="hljs-keyword">var</span> log = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">tag</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"上报标签为: "</span> + getAttribute(<span class="hljs-string">"tag"</span>));
    &#125;;
    <span class="hljs-keyword">var</span> getAttribute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>) && <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>).getAttribute(<span class="hljs-string">'tag'</span>);
    &#125;
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"button"</span>).onclick = showShare;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span> 
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 可以看到showShare函数中，既负责打开弹出，又负责上报统计，这是两个层面的内容，耦合在了一起，使用AOP分离后，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"login"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button"</span>></span>点击打开分享框<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> showShare = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"打开分享框"</span>);
    &#125;;
    <span class="hljs-keyword">var</span> log = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"上报标签为: "</span> + getAttribute(<span class="hljs-string">"tag"</span>));
    &#125;;
    <span class="hljs-keyword">var</span> getAttribute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>) && <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'button'</span>).getAttribute(<span class="hljs-string">'tag'</span>);
    &#125;
    showShare = showShare.after(log); <span class="hljs-comment">// 打开分享框之后上报数据</span>
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"button"</span>).onclick = showShare;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span> 
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据上报功能在行数后执行，当然，如果希望在函数前执行，则调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">showShare = showShare.before(log); <span class="hljs-comment">// 打开分享框之后上报数据</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，讲不同职责的功能严格分离开来，避免耦合正是AOP要实现的目标，也是装饰器的效果。</p>
<p>我们再举一个例子：ajax请求，是每个项目必不可少的，那么怎么用AOP来实现呢？</p>
<h2 data-id="heading-6">使用AOP解耦ajax参数</h2>
<p>在项目中使用ajax请求，通常，我们可能会封装一个统一的请求库，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ajax = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, url, param</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.dir(param);
  <span class="hljs-comment">// 发送 ajax 请求的代码略</span>
&#125;;
ajax(<span class="hljs-string">"get"</span>, <span class="hljs-string">"http:// xxx.com/userinfo"</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"sven"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ajax函数在项目中一直运转良好，和后台的合作也一直非常愉快，直到有一天，我们的网站收到了CSRF攻击，解决CSRF攻击最好的方式就是给HTTP请求加上一个token参数。现在的任务是要给每个ajax函数都加上token，这个时候我们第一个想到的肯定是需要去修改下ajax的函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ajax = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, url, param</span>) </span>&#123;
  param = param || &#123;&#125;;
  Param.Token = getToken(); <span class="hljs-comment">// 发送 ajax 请求的代码略...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然解决了这个问题，但是我们ajax库就变得不可复用了，每个ajax请求都带上了token，虽然在我的项目中没有问题，但是如果要移植到其他项目，或者进行开源，token就显得冗余了，也许另外一个项目不需要token，也有可能生成的token方式不一样。</p>
<p>为了解决这个问题，我们还是要把ajax还原为一个纯净的函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ajax = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, url, param</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(param);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 然后，使用AOP的before进行装饰，把token参数加到param中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> getToken = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"Token"</span>;
&#125;;
ajax = ajax.before(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, url, param</span>) </span>&#123;
  param.Token = getToken();
&#125;);
ajax(<span class="hljs-string">"get"</span>, <span class="hljs-string">"http:// xxx.com/userinfo"</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"sven"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，用AOP的方式给ajax动态加上了token参数，使ajax保持了请求功能的单一性，提高了ajax的复用性，下次如果要在其他项目中使用到，就可以不用做任何修改了。</p>
<p> </p>
<h1 data-id="heading-7">AOP的实现（ES7版）</h1>
<p>前面其实是使用ES5的语法模拟了AOP的实现，在JS新一代的语言中，已经实现了装饰器的语法糖，Vscode的源码中更是使用了装饰器来实现了依赖注入的模式。那么，AOP与装饰器的结合，又是如何使用的呢？</p>
<h2 data-id="heading-8">日志记录上报例子</h2>
<h3 data-id="heading-9">log装饰器实现</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log</span>(<span class="hljs-params">target, name, decriptor</span>) </span>&#123;
  <span class="hljs-keyword">var</span> _origin = decriptor.value;
  decriptor.value = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Calling <span class="hljs-subst">$&#123;name&#125;</span> with `</span>, <span class="hljs-built_in">arguments</span>);
    <span class="hljs-keyword">return</span> _origin.apply(<span class="hljs-literal">null</span>, <span class="hljs-built_in">arguments</span>);
  &#125;;

  <span class="hljs-keyword">return</span> decriptor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">调用装饰器</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; log &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./log"</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  @log
  <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params">nick</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`hi <span class="hljs-subst">$&#123;nick&#125;</span>`</span>;
  &#125;
&#125;

<span class="hljs-keyword">var</span> person = <span class="hljs-keyword">new</span> Person();
person.say(<span class="hljs-string">"小明"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">使用AOP解耦ajax参数</h1>
<h2 data-id="heading-12">ajax参数装饰器</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getToken</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"token"</span>;
&#125;
<span class="hljs-comment">// 给ajax添加token参数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">decorateToken</span>(<span class="hljs-params">target, name, descriptor</span>) </span>&#123;
  <span class="hljs-keyword">let</span> method = descriptor.value;
  descriptor.value = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args</span>) </span>&#123;
    args[<span class="hljs-number">2</span>].token = getToken();
    method.apply(<span class="hljs-built_in">this</span>, args);
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">调用装饰器</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Util</span> </span>&#123;
  @decorateToken
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">ajax</span>(<span class="hljs-params">type, url, param</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"param is "</span>, param);
  &#125;
&#125;

Util.ajax(<span class="hljs-string">"get"</span>, <span class="hljs-string">"http://baidu.com"</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"test"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到给ajax添加上了参数：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f78418efbfac4874b97ad52fce5139e9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">总结</h1>
<p>装饰器模式，随着ES7和Typescript语法糖的支持，越来越渗透到前端领域的开发中，JS这门语言也越来越庞大，以前只有在Java或py等用的AOP，也可以通过装饰器模式，应用到了JS中。</p>
<p>通过对装饰器的研究，挺有感触，很多时候我们会大谈某某设计模式，但是在代码中的应用其实很少，而当项目逐渐庞大时，耦合度也越来越高，历史包袱越来越重，我们更加难以迈出一步做重构。</p>
<p>本文通过列举了日志上报、ajax请求的例子，展示了装饰器其实是一个非常常用且nice的设计模式，有时候一个不起眼的功能，通过稍微的"装饰"（例如应用某种设计模式），会变得优雅与纯净。编写优雅的代码，是一个程序员需要一直追求的目标与超越。</p>
<p>参考文章：</p>
<p><a href="https://juejin.im/post/6844903838172839943" target="_blank" rel="nofollow noopener noreferrer">juejin.im/post/684490…</a></p>
<p>《Javascript设计模式与开发实战》</p></div>  
</div>
            