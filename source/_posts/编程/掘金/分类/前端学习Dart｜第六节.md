
---
title: '前端学习Dart｜第六节'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9c64236a0743d7bee35ac7bb9f1d46~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 19:37:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9c64236a0743d7bee35ac7bb9f1d46~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>这里是前端学习Dart第六节，本节知识点：<code>Dart函数</code>、<code>Lambda</code>、<code>词法作用域</code>、<code>Javascript作用域</code>、<code>作用域链</code>、<code>闭包</code>、<code>This</code>等。</p>
<p>视频地址：<a href="https://www.bilibili.com/video/BV1KB4y1M7R9/" target="_blank" rel="nofollow noopener noreferrer">传送门</a>。</p>
<h2 data-id="heading-1">函数</h2>
<p>函数的概念是可读，可维护和可重用代码的<code>构建块</code>。函数是一组用于执行特定任务的语句。函数将程序组织成逻辑代码块。一旦定义，就可以调用函数来访问代码。这使得代码可以<code>重用</code>。此外，函数可以轻松读取和维护程序的代码。</p>
<p>函数声明告诉编译器函数的名称，返回类型和参数。函数定义提供函数的实际主体。</p>
<p>看一下基本函数的声明：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9c64236a0743d7bee35ac7bb9f1d46~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>依然是先声明后调用的方式，如果先调用是会报错的。</p>
<blockquote>
<p>Error: Method not found: 'action'.</p>
</blockquote>
<h3 data-id="heading-2">函数的返回值</h3>
<p>与js函数一致，函数是可以返回任意类型数据的，但是Dart中函数是具有返回值类型检查的可以开启。比如下方方式</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23f2cb4872574d96a0006a70046d19bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>无返回值函数可以用<code>void</code>类型检查。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fe69edad5414741a37f25412b2b9921~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">函数的参数</h3>
<p>参数是一种将值传递给函数的机制。参数构成函数签名的一部分。参数值在调用期间传递给函数。除非明确指定，否则传递给函数的值的数量必须与定义的参数数量相匹配。</p>
<p>函数的参数声明有几种方式：</p>
<ol>
<li>必须传的参数</li>
</ol>
<p>在函数调用期间必须将值传递给所需的参数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2578893a2fcb4536a497bc8eb03a04df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到上述函数<code>action</code>声明了两个传入参数（形参），但是在函数调用的时候只传入了一个参数，因为这样声明函数参数是必须传的参数，所以抛了一个错误。</p>
<blockquote>
<p>Error: Too few positional arguments: 2 required, 1 given</p>
</blockquote>
<ol start="2">
<li>参数位置可选</li>
</ol>
<p>要指定可选的位置参数，请使用<code>square 方括号</code> <code>[]</code> 括号。修改一下上面那个例子：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cd48c431013403e98e7c94c2206a1bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到age参数被括了起来之后，调用函数的时候就不报错了，可选位置参数未传入的话<code>默认值是null</code></p>
<p>多个可选位置参数是这样声明的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d775bd29a0742d7bb0341a8087412eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有个注意点：<code>Dart函数中的所有必须参数必须在可选位置参数之前声明</code>。一定要注意。</p>
<p>可选位置参数可以赋予默认值:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc25ca587e2c4ee6bff93c9d0f9ca473~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>默认值必须是编译时常量 const , final则不行，因为final是运行时常量</p>
</blockquote>
<ol start="3">
<li>可选命名参数</li>
</ol>
<p>与位置参数不同，必须在传递值时指定参数名称。<code>Curly brace 花括号</code> <code>&#123;&#125;</code> 可用于指定可选的命名参数。</p>
<p>首先这样的声明方式依然是可选的，可传可不传。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ac95b8434ce4da8b43463e7ee61306b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在传入这个可选命名参数的时候必须使用声明的变量名称</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ca73a3428604494a8b54c3acb83e0fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可选命名参数也支持声明时赋予默认值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2e33d686dd44b3a45287b973ce2731~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意事项：可选命名参数与位置可选参数只能出现一种，不可以两种同时出现。</p>
<ol start="4">
<li>函数作为参数</li>
</ol>
<p>Dart中支持函数作为参数传入函数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48b3a092912d4071a15a229b813cf215~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">箭头函数</h3>
<p>如果函数只包含一个表达式，那么可以使用箭头方式使用。</p>
<p><code>=> expr;</code> 语法是 <code>&#123; return expr; &#125;</code> 的缩写</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/137fbb13703f47f7a4ff9f7591362773~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有一个注意事项：在箭头与分号之间只能出现表达式，而不能是语句，例如：不可以在那里放置if语句，但是可以使用条件表达式。</p>
<p>可以看到箭头函数是具有返回值的，当然你也可以设置void函数返回类型，这样的话就屏蔽掉了返回值。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/823f779e9f02468ebce2eb2cdb6dbe8d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>箭头函数又称之为<code>Lambda函数</code>，那么什么是<code>Lambda</code>呢。</p>
<h3 data-id="heading-5">Lambda</h3>
<p>可知函数的概念为<code>代码块</code>。</p>
<p>首先有一个问题，就是要将一个函数赋值给一个变量要怎么赋值呢，在java前面的版本函数值不可以赋值给一个变量的，后来可以了，但是是类似这个样子的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6337d39f110a490da1a99b97b9d035d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，这个并不是一个很简洁的写法。所以，为了使这个赋值操作更加优雅, 我们可以移除一些没用的声明，就开始了如下演变</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef39f8f1106345d09d19d9037ac90019~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，我们就成功的非常优雅的把<code>一块代码</code>赋给了<code>一个变量</code>。而<code>这块代码</code>，或者说<code>这个被赋给一个变量的函数</code>，就是一个<code>Lambda表达式</code>。</p>
<p>诶，如果上述最后转换成的样子叫做表达式的话，右侧的<code>匿名函数</code>就是<code>Lambda</code>。</p>
<p>匿名函数：</p>
<p>大多数函数都是命名的，例如<code>main()</code>、<code>print()</code>等，我们还可以创建一个无名函数，称为匿名函数，有时候也称为<code>labmbda</code>或者<code>闭包</code>。看一下下面的例子</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68b88aeb25864487b677d0d863ef7e88~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">作用域</h3>
<p>Dart的函数作用域就是<code>词法作用域</code> <code>Lexical scoping</code>。为<code>静态作用域</code>。</p>
<p>无论函数在哪里调用，也无论它如何被调用，他的词法作用域都只有函数被声明时所处的位置决定。</p>
<p>所谓词法作用域就是这样的一个静态的作用域模型，由全局作用域函数创建的作用域和块作用域等组成。</p>
<p>一个 <code>Lexical scoping</code> 内部 是能够访问到 外部 <code>Lexical scoping</code> 中定义的变量的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c08022504004c51b99576fe9f163348~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里出现了未定义该变量的错误警告，可以看出 printName 中定义的变量，对于 main 函数中的变量是不可见的。Dart 和 JavaScript 一样具有<code>链式作用域</code>，也就是说，子作用域可以访问父（甚至是祖先）作用域中的变量，而反过来不行。</p>
<p>从上面的例子我们可以看出，<code>Lexical scoping</code> 实际上是以<code>链式</code>存在的。一个 <code>scope</code> 中可以开一个新的<code> scope</code>，而不同 <code>scope</code> 中是可以允许重名变量的。那么我们在某个 <code>scope</code> 中访问一个变量，究竟是基于什么规则来访问变量的呢。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d291735753774a6e8b62770656048970~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上面这个例子中我们可以看到，在 main 和 firstScope 中都定义了变量 a。我们在 firstScope 中 print，输出了 2 in firstScope 而在 main 中 print 则会输出 1 in mainScope 。</p>
<p>我们已经可以总结出规律了：近者优先。</p>
<p>如果你在某个 <code>scope</code> 中访问一个变量，它首先会看当前 <code>scope</code> 中是否已经定义该变量，如果已经定义，那么就使用该变量。如果当前 <code>scope</code> 没找到该变量，那么它就会在它的上一层 <code>scope</code> 中寻找，以此类推，直到最初的 <code>scope</code>。如果所有 <code>scope</code> 链上都不存在该变量，则会提示 Error：Undefined name 'name'。</p>
<p>Dart <code>scope</code> 中的变量是<code>静态确定的</code>，如何理解呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29ce490497824062be4a407bd9168bc5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到，虽然在 main 的父 <code>scope</code> 中存在变量 a，且已经赋值，但是我们在 main 的 <code>scope</code> 中也定义了变量 a。因为是静态确定的，所以在 print 的时候会优先使用当前 <code>scope</code> 中定义的 a，而这时候 a 的定义在 print 之后，同样也会导致编译器错误：Local variable ‘a’ can’t be referenced before it is declared。</p>
<h3 data-id="heading-7">javascript作用域</h3>
<p>javascript中的<code>作用域</code>说来话长，容我慢慢道来：</p>
<p>首先明确几个概念，javascript中是没有<code>块级作用域</code>的，只有<code>函数作用域</code>和<code>全局作用域</code>，看一下下面javascript的例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3dbeff566f42869d952382e0750571~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到在<code>if</code>的执行块中声明的<code>a</code>，依然可以在执行块外面进行访问。并且绑定在了全局作用域上，这里的<code>this</code>也就是window对象。所以<code>this.a</code>可以输出inke。</p>
<p>Dart中是有<code>块级作用域</code>的，看一下下面这个例子：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/670b1b4dde8f4870be17173512e0e486~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见<code>if</code>执行块中声明的变量是无法在外部进行访问的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7987ddfae0254c7cb034a72c0f6eac3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Dart中的<code>if</code>,<code>while</code>,<code>for</code>等是有<code>块级作用域</code>的，如上图所示，父级作用域中是无法访问子作用域中声明的变量的。</p>
<p>我们可知es6新出了两个东西，<code>let</code>、<code>const</code>。这两个声明变量的方式完全替代了<code>var</code>。可是为什么es6会推出这两种声明变量的方式呢？</p>
<p><code>let</code>、<code>const</code>声明的变量都在当前执行块中进行访问，这里就填补上了javascript没有块级作用域的缺陷。</p>
<p>为什么javascript最开始没有设计块级作用域呢？</p>
<p>翻了至少20篇文章之后，我找到了最接近真实的答案： <code>设计缺陷/bug</code></p>
<p>所以es6补充条案第一条就是let、const。并且基本上我们也不写var了。</p>
<p>我们继续探索，在javascript中只有两种作用域，函数作用域，全局作用域。全局作用域则不必多说。我们主要讲一下函数作用域。</p>
<h3 data-id="heading-8">Scopes</h3>
<blockquote>
<p>这里我要标记一下，下面有些内容我实在是没有找到实在的根据，有一些逻辑实属推断，如有错漏，欢迎指正。</p>
</blockquote>
<p>javascript中的函数也可以在函数内部创建函数，那么<code>scope</code>就会层层嵌套，又由于作用域的特性保留，子作用域可以访问父作用域的变量，所以生成了一条作用域链<code>[[scopes]]</code>，看一下如下例子。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a331a21c38b4458928a286873ee0299~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作用域链的具体表现形式我们debug中看一下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d132966422a480e9088ee667351b147~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到<code>function c </code>中的 <code>Scopes</code>长度为<code>3</code>，说明函数c的作用域链中有三个作用域，算自己本身的作用域的话就是四个。因为这个断点打在了<code>b函数</code>的内部并且是<code> c函数</code>调用的位置。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda95f44a63c40ddb708fd18b2f50032~tplv-k3u1fbpfcp-watermark.image" alt="作用域链.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在函数c内部打印的aa、bb、cc都会先从自身<code>scope</code>寻找，然后向上寻找，直至寻找到顶级作用域<code>global</code>。global举个例子：在浏览器中就是window对象。</p>
<p>这样就比较明白作用链是个什么东西了，而且比较耳熟，相信你们最开始了解原型链的时候也是这么背的，原理呢，其实差不是很多，下一节课就可以深入了解一下原型、继承等等。</p>
<h3 data-id="heading-9">Closure</h3>
<p>这里有人可能有疑问，上面<code>Scopes</code>中长度有三，最后一个Global可以理解，但是为什么函数a和函数b为<code>（Closure）</code>？</p>
<p>这里先给出原因，因为在函数c中调用了函数a和函数b内部的参数，所以函数c中的作用域链中，有函数a和函数b的<code>闭包</code>。</p>
<p>这里一定会有人有疑问：</p>
<blockquote>
<p>我记得闭包应该是什么函数套函数，然后return一个函数的呀。</p>
</blockquote>
<p>其他的先不讲，至少从我上面的例子中就已经推翻你这个结论了。</p>
<p>真实的概念：</p>
<blockquote>
<p>「函数」和「函数内部能访问到的变量」（也叫环境）的总和，就是一个闭包。</p>
</blockquote>
<p>那我们印象里背的<code>return</code>是怎么回事呢。如果不把这个闭包<code>return</code>出来的话，外面就没法调用。。。只有<code>return</code>出来后，就可以在<code>外部上下文</code>进行函数内部变量的访问。</p>
<p>关于闭包还有一个谣言<code>内存泄漏</code>，相信大多数人印象里闭包的<code>缺点</code>一定就是有内存泄漏风险。</p>
<p>说这话的人根本不知道什么是内存泄露。内存泄露是指你用不到（访问不到）的变量，依然占居着内存空间，不能被再次利用起来。</p>
<p>闭包里面的变量明明就是我们需要的变量<code>（lives）</code>，凭什么说是内存泄露？</p>
<p>这个谣言是如何来的？</p>
<p>因为<code> IE</code>。<code>IE</code> 有 bug，IE 在我们使用完闭包之后，依然回收不了闭包里面引用的变量。</p>
<p>这是 IE 的问题，不是闭包的问题。参见司徒正美的这篇文章，<a href="https://www.cnblogs.com/rubylouvre/p/3345294.html" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<p>现在IE已经渐渐退出历史舞台了，所以大家可以更新一下脑海中的观念了。</p>
<h3 data-id="heading-10">This</h3>
<p>这里补充几个小知识点。</p>
<p>在javascript中面我们比较熟悉的东西叫做 <code>this</code>。 <code>this</code>是什么呢？你可能只记得this的指向问题，因为前端面试的时候总是要问对吧，但是我们问的并不是指向问题，而是this是什么？</p>
<p>this是函数当前执行时候的作用域，就像上面的作用域链中的例子中，函数c中的this指向的就是<code>Global作用域</code>。当然，Global作用域也是<code>scopes作用域链</code>中的一环。</p>
<p>我们可以通过<code>apply</code>、<code>call</code>、<code>bind</code>来改变<code>this</code>的<code>指向</code>，这里所说的this指向就是指作用域链中的指向。</p>
<p>这里有人可能会问，如果我apply了一个函数d，怎么办呢？函数d并不在最开始的函数作用域链中，如果你用apply将this指向函数d的话，在<code>作用域链</code>中将多一个<code>Closure</code>。并且将<code>this</code>指向过去。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b65d4734271e45f496b5757ba1fc9e98~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候<code>this就是函数d</code>。</p>
<p>这里顺便提一下Dart中是没有this关键字的。</p>
<h2 data-id="heading-11">END</h2>
<p>在本章节中我们学习了知识点：Dart函数、Lambda、词法作用域、Javascript作用域、作用域链、闭包、This等。</p>
<p>这个系列专栏目测快要结尾了，计划共8-9节。欢迎大家点赞转发。</p></div>  
</div>
            