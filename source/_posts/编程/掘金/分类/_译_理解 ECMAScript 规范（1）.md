
---
title: '_译_理解 ECMAScript 规范（1）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5b2e9b285485aa7e7b9e14b20f820~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 22:29:01 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5b2e9b285485aa7e7b9e14b20f820~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>译者: 李松峰</p>
<blockquote>
<p>翻译本文的目的是尝试给出 ECMAScript 规范中核心术语的译法，供同好品评。</p>
</blockquote>
<p>在这篇文章里，我们会从规范中找一个简单的功能，借以理解规范中的符号。开始吧！</p>
<h2 data-id="heading-0">前言</h2>
<p>即便你懂 JavaScript，阅读其规范也会让人畏缩。</p>
<p>让我们从一个具体的例子开始，然后通过规范去理解它。下面的代码演示了 <code>Object.prototype.hasOwnProperty </code>的用法：</p>
<pre><code class="copyable">const o = &#123; foo: 1 &#125;;
o.hasOwnProperty('foo'); // true
o.hasOwnProperty('bar'); // false
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>o</code>并没有一个叫<code>hasOwnProperty</code>的属性，因此要沿原型链向上查找。于是，在<code>o </code>的原型<code>Object.prototype</code>上找到了它。</p>
<p>为描述<code>Object.prototype.property</code>的工作原理，规范使用了类似伪代码的说明：</p>
<blockquote>
<p><code>Object.prototype.hasOwnProperty(V)</code><br>
在以参数 V 调用<code>hasOwnProperty</code>方法时，将执行以下步骤：<br>
1.令<code>P</code>为?<code>ToPropertyKey(V)</code>；<br>
2.令<code>O</code>为?<code>ToObject(this 值)</code>；<br>
3.返回<code>? HasOwnProperty(O, P)</code>。</p>
</blockquote>
<p>以及</p>
<blockquote>
<p><code>HasOwnProperty(O, P)</code><br>
抽象操作<code>HasOwnProperty</code>用于确定对象是否有一个以指定属性为键的自有属性。返回布尔值。这个操作以参数<code>O</code>和<code>P</code>调用，其中<code>O</code>是对象,<code>P</code>是属性键。这个抽象操作执行以下步骤。<br>
1.断言:<code>Type(O)</code>为<code>Object</code>；<br>
2.断言:<code>IsPropertyKey(P)</code>为<code>true</code>；<br>
3.令<code>desc</code>为<code>? O.[[GetOwnProperty]](p)</code>；<br>
4.若<code>desc</code>为<code>undefined</code>，返回<code>false</code>；<br>
5.返回<code>true</code>。</p>
</blockquote>
<p>什么是“抽象操作”？<code>[[]]</code>里面的东西表示什么？为什么把一个<code>?</code>放在函数前面？“断言”又是什么意思？</p>
<h2 data-id="heading-1">语言类型与规范类型</h2>
<p>规范使用了<code>undefined</code>、<code>true</code> 和<code>false</code>这些我们在 JavaScript 中已经知道的值。这些都是<a href="https://tc39.es/ecma262/#sec-ecmascript-language-types" title="语言值" target="_blank" rel="nofollow noopener noreferrer">语言值</a>，即规范中定义的语言类型的值。</p>
<p>规范内部也使用语言值，比如某个内部数据类型的字段可能包含<code>true</code>或<code>false</code>。相对而言，JavaScript 引擎通常不会在内部使用语言值。例如，如果 JavaScript 引擎是用 C++写的，那通常会使用 C++的<code>true</code>和<code>false</code>，而这并不是 JavaScript 语言值<code>true</code>和<code>false</code>的内部表示。</p>
<p>除了语言类型，规范也有自己的<a href="https://tc39.es/ecma262/#sec-ecmascript-specification-types" title="规范类型" target="_blank" rel="nofollow noopener noreferrer">规范类型</a>。规范类型是只存在于规范中的类型，JavaScript 语言中不存在。JavaScript 引擎不需要（但完全可以）实现它们。本文将介绍规范类型记录（Record）及其子类型完成记录（Completion Record）。</p>
<h2 data-id="heading-2">抽象操作</h2>
<p><a href="https://tc39.es/ecma262/#sec-abstract-operations" title="抽象操作" target="_blank" rel="nofollow noopener noreferrer">抽象操作</a>是 ECMAScript 规范定义的函数，定义它们的目的是为了让规范更简洁。JavaScript 引擎不必在内部实现这些函数。这些函数不能直接在 JavaScript 中调用。</p>
<h2 data-id="heading-3">内部栏位及内部方法</h2>
<p><a href="https://tc39.es/ecma262/#sec-object-internal-methods-and-internal-slots" title="内部栏位（slot）和内部方法" target="_blank" rel="nofollow noopener noreferrer">内部栏位（slot）和内部方法</a>包含在<code>[[]]</code>中。</p>
<p>内部栏位是 JavaScript 对象或规范类型的数据成员，用于存储对象的状态。内部方法是 JavaScript 对象的内部成员函数。</p>
<p>比如，每个 JavaScript 对象都有一个内部栏位<code>[[Prototype]]</code>和一个内部方法<code>[[GetOwnProperty]]</code>。</p>
<p>内部栏位和内部方法不能在 JavaScript 中使用。换句话说，不能访问<code>o.[[Prototype]]</code>或调用<code>o.[[GetOwnProperty]]()</code>。JavaScript引擎可以为了内部使用实现它们，但不是必需的。</p>
<p>有时候内部方法也会委托到名字类似的抽象操作，比如普通对象（ordinary object）的<code>[[GetOwnProperty]]</code>：</p>
<blockquote>
<p>[<code>[[GetOwnProperty]](p)</code>] <br>
在以属性键<code>P</code>调用内部方法<code>[[GetOwnProperty]]</code>时，将执行以下步骤：<br>
1.返回<code>! OrdinaryGetOwnProperty(O, P)</code>。</p>
</blockquote>
<p>（下一篇文章会介绍这里的叹号表示什么意思。）</p>
<p><code>OrdinaryGetOwnProperty</code>不是内部方法，因为它不与任何对象关联，而是以接收参数的形式取得要操作的对象。</p>
<p><code>OrdinaryGetOwnProperty</code>前面的“ordinary”（普通）表示它只操作普通对象。ECMAScript 对象要么是普通对象（ordinary），要么是异质对象（exotic）。普通对象必须具有一组被称为基本内部方法（essential internal methods）的方法所定义的默认行为。如果某个对象修改了默认行为（即覆盖或重写了一个或多个基本内部方法。——译者注），那它就是异质对象。</p>
<p>大家最熟悉的<code>Array</code>就是异质对象，因为其<code>length</code>属性的行为与默认行为不同：设置数组的<code>length</code>属性可能会从数组中删除元素。</p>
<p>这里给出了所有<a href="https://tc39.es/ecma262/#table-5" title="基本内部方法" target="_blank" rel="nofollow noopener noreferrer">基本内部方法</a>（普通对象 11 个，函数对象 2 个。——译者注）。</p>
<h2 data-id="heading-4">完成记录</h2>
<p>前面例子中出现的问号和叹号表示什么意思？要理解它们，需要先理解<a href="https://tc39.es/ecma262/#sec-completion-record-specification-type" title="完成记录" target="_blank" rel="nofollow noopener noreferrer">完成记录</a>（Completion Record）！</p>
<p>完成记录是一种规范类型（只在规范中使用）。JavaScript 引擎不需要实现对应的内部数据类型。</p>
<p>完成记录是一种记录类型（Record），而记录具有一组固定的命名字段。完成记录具有以下 3 个字段。</p>
<p><img alt="截屏2021-03-28 下午3.27.57.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5b2e9b285485aa7e7b9e14b20f820~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所有抽象操作都会隐式返回一个完成记录。即便一个抽象操作看起来返回简单类型（如 Boolean）的值，这个值也会被隐式包装在一个<code>normal</code>类型（正常完成）的完成记录中返回（参见<a href="https://tc39.es/ecma262/#sec-implicit-completion-values" title="隐式完成值" target="_blank" rel="nofollow noopener noreferrer">隐式完成值</a>）。</p>
<blockquote>
<p>注 1：规范本身在这方面也不是完全一致。有一些辅助函数会返回裸值，而这些值将直接被使用，无需从完成记录中提取。不过这种情况在上下文中通常能够一目了然。<br>
注 2：规范编辑也在致力于更显式地处理完成记录。</p>
</blockquote>
<p>如果某个算法抛出异常，则意味着返回的完成记录的<code>[[Type]]</code>为<code>throw</code>，<code>[[Value]]</code>为异常对象。我们这里不讨论<code>break</code>、<code>continue</code>和<code>return</code>类型（规范中没有相应的例子，因为这几种类型不能跨函数。——译者注）。</p>
<p><strong>ReturnIfAbrupt(argument)</strong> 表示执行如下步骤：</p>
<blockquote>
<p>1.若<code>argument</code>为硬性完成，返回<code>argument</code>；<br>
2.设<code>argument</code>为<code>argument.[[Value]]</code>。</p>
</blockquote>
<p>换句话说，对于完成记录，如果是硬性完成，则立即返回；如果是正常完成，则提取完成记录的值。</p>
<p><code>ReturnIfAbrupt</code>看起来虽然像函数调用，但它不是。<code>ReturnIfAbrup</code>会导致它所在位置的函数返回，而不是<code>ReturnIfAbrupt</code>本身返回。<code>ReturnIfAbrupt</code>有点像 C 语言中的宏。</p>
<p><code>ReturnIfAbrupt</code>可以这样用：</p>
<blockquote>
<p>1.令<code>obj</code>为<code>Foo()</code>；（<code>obj</code>是一个完成记录。）<br>
2.<code>ReturnIfAbrupt(obj)</code>；<br>
3.<code>Bar(obj)</code>。（如果到了这一步，<code>obj</code>已经变成了从完成记录中提取出来的值。）</p>
</blockquote>
<p>现在该说到<a href="https://tc39.es/ecma262/#sec-returnifabrupt-shorthands" title="问号" target="_blank" rel="nofollow noopener noreferrer">问号</a>了：<code>? Foo()</code>等价于<code>ReturnIfAbrupt(Foo())</code>。显然，使用简写（<code>?</code>）可以省去每次都明确写出错误处理代码的麻烦。</p>
<p>类似地，“令<code>val</code>为<code>! Foo()</code>”等价于：</p>
<blockquote>
<p>1.令<code>val</code>为<code>Foo()</code>；（<code>val</code>是一个完成记录。）<br>
2.断言：<code>val</code>非硬性完成；<br>
3.设<code>val</code>为<code>val.[[Value]]</code>。</p>
</blockquote>
<p>（换句话说，叹号表示从正常完成记录中提取值。——译者注 ）</p>
<p>知道了这些之后，就可以把前面的<code>Object.prototype.hasOwnProperty</code>以完整但冗余的形式重写如下：</p>
<blockquote>
<p><strong>Object.prototype.hasOwnProperty(V)</strong><br>
1.令<code>P</code>为<code>ToPropertyKey(V)</code>；<br>
2.若<code>P</code>为硬性完成，返回<code>P</code>；<br>
3.设<code>P</code>为<code>P.[[Value]]</code>；<br>
4.令<code>O</code>为<code>ToObject(this 值)</code>；<br>
5.若<code>O</code>为硬性完成，返回<code>O</code>；<br>
6.设<code>O</code>为<code>O.[[Value]]</code>；<br>
7.令<code>temp</code>为<code>HasOwnProperty(O, P)</code>；<br>
8.若<code>temp</code>为硬性完成，返回<code>temp</code>；<br>
9.设<code>temp</code>为<code>temp.[[Value]]</code>；<br>
10.返回<code>NormalCompletion(temp)</code>。</p>
</blockquote>
<p>把抽象操作<code>HasOwnProperty()</code>重写如下：</p>
<blockquote>
<p><strong>HasOwnProperty(O, P)</strong>\</p>
</blockquote>
<p>1.断言：<code>Type(O)</code>为<code>Object</code>；<br>
2.断言：<code>IsPropertyKey(P)</code>为<code>true</code>；<br>
3.令<code>desc</code>为<code>O.[[GetOwnProperty]](p)</code>；<br>
4.若<code>desc</code>为硬性完成，返回<code>desc</code>；<br>
5.设<code>desc</code>为<code>desc.[[Value]]</code>；<br>
6.若<code>desc</code>为<code>undefined</code>，返回<code>NormalCompletion(false)</code>；<br>
7.返回<code>NormalCompletion(true)</code>。</p>
<p>进而把内部方法<code>O.[[GetOwnProperty]]</code>以不带叹号的形式重写如下：</p>
<blockquote>
<p><strong>O.[[GetOwnProperty]]</strong><br>
1.令<code>temp</code>为<code>OrdinaryGetOwnProperty(O, P)</code>；<br>
2.断言:<code>temp</code>非硬性完成；<br>
3.令<code>temp</code>为<code>temp.[[Value]]</code>；<br>
4.返回<code>NormalCompletion(temp)</code>；</p>
</blockquote>
<p>这里假设<code>temp</code>是个新的临时变量，不与任何其他变量冲突。</p>
<p>这里也用到了前面说的当返回语句返回非完成记录时，实际上返回值将被隐式包装在一个<code>NormalCompletion</code>中。</p>
<p><strong>扩展学习：返回<code>? Foo()</code></strong></p>
<p>规范中使用“返回<code>? Foo()</code>”这种写法，为什么还要加个问号呢？</p>
<p>“返回<code>? Foo()</code>”扩展后是：</p>
<blockquote>
<p>1.令<code>temp</code>为<code>Foo()</code>；<br>
2.若<code>temp</code>为硬性完成，返回<code>temp</code>；<br>
3.设<code>temp</code>为<code>temp.[[Value]]</code>；<br>
4.返回<code>NormalCompletion(temp)</code>。</p>
</blockquote>
<p>这跟“返回<code>Foo()</code>”没有区别：即无论硬性完成还是正常完成，行为都一样。</p>
<p>写成“返回<code> ? Foo()</code> ”仅仅是出于编辑方便的考虑，为了更明确地表示返回的<code>Foo()</code>是一个完成记录。</p>
<h2 data-id="heading-5">断言</h2>
<p>规范中的“断言”提示算法中不变的条件。添加这些“断言”是为了明确起见，不要求实现。换句话说，实现不需要检查这些条件。</p>
<h2 data-id="heading-6">挑战</h2>
<p>抽象操作也会委托给其他抽象操作（见下图），但根据本文的介绍，大家应该能推断出这些操作最终干了什么事。这里面会碰到属性描述符（Property Descriptor），也是一种规范类型。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2245a1939354fe496d4ae2fa504218f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">小结</h2>
<p>我们通过规范看到了一个简单的方法<code>Object.prototype.hasOwnProperty</code>和它调用的抽象操作，知道了<code>?</code>和<code>!</code>与错误处理有关，也了解了语言类型、规范类型、内部栏位和内部方法。</p>
<p><a href="https://v8.dev/blog/understanding-ecmascript-part-1" title="原文链接" target="_blank" rel="nofollow noopener noreferrer">原文链接</a></p>
<p>欢迎关注「 字节前端 ByteFE 」简历投递联系邮箱「 <a href="mailto:tech@bytedance.com">tech@bytedance.com</a> 」</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            