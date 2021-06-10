
---
title: '深入浅出JavaScript函数式编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4767'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 17:41:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=4767'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>函数式编程是一种强调以函数使用为主的开发风格。这里的函数是数学上<strong>函数</strong>也就是变量的映射，一个函数的值仅决定于函数的参数值，不依赖其他状态。它的目标是<strong>使用函数来抽象作用在数据之上的控制流和操作</strong>，从而在程序中<strong>消除副作用</strong>并<strong>减少对状态的改变</strong>。</p>
<p>函数式编程有以下4个基本概念：</p>
<ul>
<li>声明式编程</li>
<li>纯函数</li>
<li>引用透明</li>
<li>不可变性</li>
</ul>
<h2 data-id="heading-1">函数式编程</h2>
<h3 data-id="heading-2">声明式编程</h3>
<p>函数式编程属于声明式编程范式，只关心数据的映射，与之对应的就是命令式编程范式。命令式编程是面向计算机硬件的抽象，有变量、赋值语句、表达式和控制语句等，而函数式编程是面向数学的抽象，将计算描述为一种表达式来求解。</p>
<p>举个例子：计算一个数组中所有数的平方，命令式编程如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> numArr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < numArr.length; i++) &#123;
    numArr[i] = <span class="hljs-built_in">Math</span>.pow(numArr[i], <span class="hljs-number">2</span>);
&#125;
<span class="hljs-built_in">console</span>.log(numArr); <span class="hljs-comment">// [1, 4, 9, 16, 25, 36, 49, 64, 81]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，命令式编程要很具体的告诉计算机如何去执行任务。</p>
<p>与之相反，声明式编程是将程序的描述与求值分离开。它关注如何使用各种表达式来描述程序逻辑，而不一定要指明其控制流或状态的变化。典型的声明式编程就是SQL。SQL语句是由很多描述查询结果应该是什么样的断言组成，对数据检索的内部机制进行了抽象。</p>
<p>如果使用声明式编程来解决上述问题，只需要对应用在每个数组元素上的行为予以关注，将循环部分交给系统其他部分去控制，因为循环是一种重要的命令控制结构，但很难重用，并且很难插入其他操作中。</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>].map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> <span class="hljs-built_in">Math</span>.pow(num, <span class="hljs-number">2</span>))
<span class="hljs-comment">// [1, 4, 9, 16, 25, 36, 49, 64, 81]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">纯函数</h3>
<p>使用纯函数是函数式编程的大前提。纯函数具有以下特性：</p>
<ul>
<li>相同的输入，永远会得到相同的输出，也就是说在函数求值期间或调用间隔时不依赖外部状态。</li>
<li>不会造成超出其作用域的变化，例如修改全局对象或引用传递的参数。</li>
</ul>
<p>不符合以上条件的函数都是“不纯”的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
    reuturn num++;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然<code>increment</code>函数是不纯的，因为它读取并修改了一个外部变量<code>num</code>。事实上<code>JavaScript</code>这种充满了动态行为与变化的语言内，纯函数的确是很难使用的。但函数式编程在实践上并不限制一切状态的的改变。它只是提供了一个框架来帮助管理和减少可变状态，同时能够将纯函数从不纯的部分中分离出去。</p>
<p>看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPersonFromId</span> (<span class="hljs-params">id</span>) </span>&#123;
    <span class="hljs-keyword">const</span> person = <span class="hljs-built_in">localStorage</span>.getItem(id);
    <span class="hljs-keyword">if</span> (persion !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">`#<span class="hljs-subst">$&#123;elementId&#125;</span>`</span>).innerHTML = <span class="hljs-string">`<span class="hljs-subst">$&#123;person.name&#125;</span> born in <span class="hljs-subst">$&#123;person.birthday&#125;</span>`</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'person not found!'</span>)
    &#125;
&#125;
getPersonFromId(<span class="hljs-string">'440111199*********'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getPersonFromId</code>有如下不符合纯函数的规定地方：</p>
<ul>
<li>函数与一个外部变量（<code>localStorage</code>）进行了交互，但函数签名中并没有声明这个参数。在任何时间点，这个引用可能为<code>null</code>，从而导致完全不同的结果并破坏了程序的“纯度”。</li>
<li>全局变量<code>elementId</code>可能在函数被调用时被改变，难以控制。</li>
<li><code>HTML</code>元素也是全局变量，可能在下次调用的时候就不一样了。</li>
<li>如果没找到这个人，该函数会抛出一个异常，将会导致整个程序的栈回退并突然结束。</li>
</ul>
<p>把<code>getPersonFromId</code>改为纯函数，首先要分离显示与获取这两个行为。当然，与外部交互和<code>DOM</code>交互产生的副作用是不可避免的，但至少可以通过将其从主逻辑中分离出来的方式使它们更易于管理。这需要使用<strong>柯里化</strong>技巧，使用柯里化可以部分传递函数参数，以便将函数的参数减少为一个。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> find = R.curry(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">localStorage</span>, id</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> person = <span class="hljs-built_in">localStorage</span>.getItem(id);
    <span class="hljs-keyword">if</span> (person !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'person not found'</span>);
    &#125;
    <span class="hljs-keyword">return</span> person;
&#125;);
<span class="hljs-keyword">const</span> showMessage = (<span class="hljs-function"><span class="hljs-params">person_</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;person.name&#125;</span> born in <span class="hljs-subst">$&#123;person.birthday&#125;</span>`</span>;
<span class="hljs-keyword">const</span> append = R.curry(<span class="hljs-function">(<span class="hljs-params">elementId, info</span>) =></span> &#123;
    <span class="hljs-built_in">document</span>.querySelector(elementId).inner = info
&#125;)

<span class="hljs-keyword">const</span> getPersonFromId = R.compose(
                            append(<span class="hljs-string">'#person'</span>),
                            csv,
                            find(<span class="hljs-built_in">localStorage</span>));
getPersonFromId(<span class="hljs-string">'440111199*********'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管只是些许的改变，但已经可以显示出几个优势了：</p>
<ul>
<li>有三个可以重用的组件。</li>
<li>将一个长函数分散，大大减少需要维护的代码量。</li>
<li>声明式风格提供了程序需要执行的步骤一个清晰的视图，增强代码可读性。</li>
<li>与<code>HTML</code>交互移动到单独的函数中，将纯函数中的不纯分离出去。</li>
</ul>
<p><strong>柯里化</strong><br>
柯里化是一种参数还没有全部提供前，将其挂起或者延迟函数执行，将多参数函数转换为一元函数序列的技巧。它要求所有参数都被明确地定义。因此，当调用时缺少参数的时候，它会返回一个新的函数，在真正运行前等待外部提供其余的参数。</p>
<p>在函数式编程语言中，柯里化是原生特性，是函数定义中的组成部分。但<code>JavaScript</code>不能原生支持柯里化，因为在缺少参数的情况下调用非柯里化函数会导致缺失参数的实参变成<code>undefined</code>。比如说如果定义一个函数<code>f(a, b, c)</code>，并只在调用时传递<code>a</code>，<code>JavaScript</code>运行时的调用机制会将<code>b</code>和<code>c</code>设为<code>undefined</code>。</p>
<p>所以在<code>JavaScript</code>中需要编写一些代码启动柯里化。比如下面这个二元参数的手动柯里化函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry2</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">firstArg</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">secondArg</span>) </span>&#123;
            <span class="hljs-keyword">return</span> fn(firstArg, secondArg)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，柯里化其实就是一种词法作用域，其返回的函数只不过是接收后续参数的简单嵌套函数包装器。</p>
<h3 data-id="heading-4">引用透明与可置换性</h3>
<p>引用透明是定义一个纯函数较为正确的方式。纯度在这个意义上表明了一个函数的参数和返回值之间映射的关系。因此，如果一个函数对于相同的输入始终产生相同的结果，那么它就是引用透明的。之前的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
    reuturn num++;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使其引用透明，需要删除其依赖的外部变量这一状态，使其成为函数签名中显式定义的参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> increment = <span class="hljs-function">(<span class="hljs-params">num</span>) =></span> ++num;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改完之后，变成了纯函数，对于相同的输入每次都会返回相同的输出。之所以追求这种函数特性，是因为它不仅能使代码更易于测试，还更容易推理整个程序。</p>
<p>引用透明来自数学概念，但编程语言的函数行为与数学上的不同，所以引用透明必须由我们来实现。构建这样的程序更容易推理，因为可以在心中形成一个状态系统的模型，并通过重写或替换来达到期望的输出。具体来说，假设任何程序可以被定义为一组的函数，对于一个给定的输入，会产生一个输出，则可表示为：</p>
<pre><code class="hljs language-js copyable" lang="js">Program = [Input] + [fun1, fun2, fun3, ...] -> Output
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>[fun1, fun2, fun3, ...]</code>是纯的，那么就可以很轻易地将由其产生的值来重写这个程序<code>[val1, val2, val3, ...]</code>而不改变结果。举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> input = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>];
<span class="hljs-keyword">const</span> average = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> divide(sum(arr), size(arr));
average(input); <span class="hljs-comment">// 20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数<code>sum</code>和<code>size</code>都是引用透明的，对于如下给定的输入，可以很容易地重写这个表达式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> average = divide(<span class="hljs-number">60</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// 20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于<code>devide</code>也是纯的，因此可以利用其数学符号进行改写，所以对于当前输入，平均值永远是<code>60/3=20</code>。</p>
<h3 data-id="heading-5">存储不可变的数据</h3>
<p>不可变数据是指那些被创建后不能更改的数据。<code>JavaScript</code>的所有基本类型本质上是不可变的，但引用类型都是可变的,所以如何管理对象的状态是一个大问题。</p>
<p><strong>将对象视为数值</strong><br>
在函数式编程中，将具有不可变的类型成为数值，比如基本类型的字符串和数字。如果能将对象视为数值，那就不比担心它们被篡改。</p>
<p><code>ES6</code>使用<code>const</code>关键字来创建不可变的变量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pi = <span class="hljs-number">3.14</span>;
pi = <span class="hljs-number">3.15</span>; <span class="hljs-comment">//Uncaught TypeError: Assignment to constant variable.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这样还不够，因为这不能防止对象内部状态的改变。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> piObj = &#123;
    <span class="hljs-attr">pi</span>: <span class="hljs-number">3.14</span>
&#125;
piObj.pi = <span class="hljs-number">3.15</span>; <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个好的办法就是采用值对象模式，指的是其相等性不依赖与标识或引用，而只是基于其值，一旦声明，其状态就不可变。在<code>JavaScript</code>中，实现值对象的其中一个办法就是使用函数来保障内部状态的访问，通过返回接口的方式来公开一部分方法给调用者。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">person</span> (<span class="hljs-params">name, contry</span>) </span>&#123;
    <span class="hljs-keyword">let</span> _name = name;
    <span class="hljs-keyword">let</span> _contry = contry;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">getName</span>: <span class="hljs-function">() =></span> _name;
        getContry: <span class="hljs-function">() =></span> _contry;
        toString: <span class="hljs-function">() =></span> _name + <span class="hljs-string">' from '</span> _contry
&#125;

<span class="hljs-keyword">const</span> person1 = person(<span class="hljs-string">'zhang'</span>, <span class="hljs-string">'china'</span>);
person1.toString(); <span class="hljs-comment">// 'zhang from china'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，<code>JavaScript</code>还有一个内部机制，通过控制<code>writable</code>属性来实现的。比如<code>Object.freeze()</code>函数可以使该属性设置为<code>false</code>来阻止对象状态的改变。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> piObj = <span class="hljs-built_in">Object</span>.freeze(&#123; <span class="hljs-attr">pi</span>: <span class="hljs-number">3.14</span> &#125;)
piObj.pi = <span class="hljs-number">3.15</span> <span class="hljs-comment">// 不行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但<code>Object.freeze()</code>是一种浅操作。要解决深层属性不可变问题，需要手动冻结对象的嵌套结构</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isObj = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val && <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepFreeze</span> (<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isObj(obj) && !<span class="hljs-built_in">Object</span>.isFrozen(obj)) &#123;
        <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> deepFreeze(obj[name]);
        <span class="hljs-built_in">Object</span>.freeze(obj);
    &#125;
    <span class="hljs-keyword">return</span> obj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用Lenses定位并修改对象图</strong><br>
<code>deepFreeze</code>函数虽然能增强代码中的不可变水平，但要创建一个永不可变的程序是不现实的。因此比较可行的办法就是由原对象创建新对象，在每次方法调用时返回一个新的对象。</p>
<p><code>Lenses</code>被称为函数式引用，是函数式程序设计中用于访问和不可改变地操作状态数据类型属性的解决方案。从本质上讲，<code>Lenses</code>与写时复制策略类似，即采用一个能够合理管理和赋值状态的内部存储部件。</p>
<p><code>Ramda.js</code>库已经实现了这个方案，比如使用<code>R.lensProp</code>来创建一个包装了<code>piObj</code>的<code>pi</code>属性的<code>Lens</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> piLens = R.lenseProp(<span class="hljs-string">'pi'</span>);
R.view(piLens, piObj); <span class="hljs-comment">// 3.14;</span>

<span class="hljs-keyword">const</span> newPi = R.set(piLens, <span class="hljs-string">'3.15'</span>, piObj);
newPi.pi; <span class="hljs-comment">// 3.15</span>
piObj.pi; <span class="hljs-comment">// 3.14</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Lense</code>之所以有价值，是因为其提供了一种不那么繁琐的操作对象的机制，即使是一些历史遗留或超出控制范围的对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Lenses修改嵌套属性</span>
<span class="hljs-keyword">const</span> person = &#123;
    <span class="hljs-attr">address</span>: &#123;
        <span class="hljs-attr">country</span>: <span class="hljs-string">'china'</span>,
        <span class="hljs-attr">city</span>: <span class="hljs-string">'guangzhou'</span>
    &#125;
&#125;

<span class="hljs-keyword">const</span> cityPath = [<span class="hljs-string">'address'</span>, <span class="hljs-string">'city'</span>];
<span class="hljs-keyword">const</span> cityLens = R.lens(R.path(cityPath), R.assocPath(cityPath));
R.view(cityLens, person); <span class="hljs-comment">// 'guangzhou'</span>

<span class="hljs-keyword">const</span> newPerson = R.set(cityLens, person,  <span class="hljs-string">'shenzhen'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">如何进行函数式编程</h2>
<h3 data-id="heading-7">复杂任务的分解</h3>
<p>从宏观上来讲，函数式编程实际上是分解和组合之间的相互作用。比如<code>getPersonFromId</code>，将其分解为<code>find、csv、append</code>。函数式编程的模块化的概念与单一职责息息相关。也就是说，函数都应该拥有单一的目的，比如<code>average</code>函数。纯度和引用透明会促使你这样思考问题，为了将函数组合在一起，它们必须在输入和输出的形式上形成一致。</p>
<p>而上述用到的<code>R.compose</code>函数则是组合。两个函数的组合是一个新的函数，它拿到一个函数的输出，并将其传递给另外一个函数中。假设有两个函数f和g，它们的关系<code>f * g = f(g(x))</code>，其中g函数的返回值与f的参数之间构建了一个松耦合的且类型安全的联系。两个函数能够组合的条件是，它们必须在参数数目及参数类型上形成一致。</p>
<p>从本质上讲，函数组合是一种将已被分解的简单任务组织成复杂行为的整体过程。举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> words = <span class="hljs-string">'we are family'</span>;
<span class="hljs-keyword">const</span> explode = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span> str.split(<span class="hljs-regexp">/\s+/</span>);
<span class="hljs-keyword">const</span> count = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> arr.length;
<span class="hljs-keyword">const</span> countWords = R.compose(count, explode);
countWords(words); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>countWords</code>函数的调用触发了函数<code>explode</code>的执行并将其输出传给<code>count</code>以计算该数组的长度。组合将输入和输出相链接，创建出函数通道。这段代码直到<code>countWords</code>被调用才会触发求值。组合的结果是等待一个指定参数调用的另一个函数<code>countWords</code>。函数式组合的强大之处在于：将函数的描述与求值分开。</p>
<p><code>compose</code>的实现</p>
<pre><code class="hljs language-js copyable" lang="js">functon <span class="hljs-function"><span class="hljs-title">compose</span>(<span class="hljs-params">...args</span>)</span> &#123;
    <span class="hljs-keyword">const</span> start = args.length - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> i = start;
        <span class="hljs-keyword">let</span> result = args[start].apply(<span class="hljs-built_in">this</span>, args);
        <span class="hljs-keyword">while</span>(i--)&#123;
            <span class="hljs-keyword">return</span> = args[i].call(<span class="hljs-built_in">this</span>, result);
        <span class="hljs-keyword">return</span> result;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>Ramda</code>函数式库的好处之一就是所有函数已经被正确地柯里化，在组合函数管道时更具有通用性。再看下面一个例子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> students = [<span class="hljs-string">'zhao'</span>, <span class="hljs-string">'qian'</span>, <span class="hljs-string">'sun'</span>, <span class="hljs-string">'li'</span>];
<span class="hljs-keyword">const</span> scores = [<span class="hljs-number">90</span>, <span class="hljs-number">88</span>, <span class="hljs-number">97</span>, <span class="hljs-number">80</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到班里成绩最高的学生</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> smarTestStudent = R.compose(
    R.head, <span class="hljs-comment">// 获取第一个元素</span>
    R.pluck(<span class="hljs-number">0</span>), <span class="hljs-comment">// 通过抽取指定的索引的元素构建数组。这里0表示提取学生名字</span>
    R.reverse, <span class="hljs-comment">// 反转数组</span>
    R.sortBy(R.prop[<span class="hljs-number">1</span>]), <span class="hljs-comment">// 根据指定属性进行升序排序</span>
    R.zip);
smarTestStudent(students, scores); <span class="hljs-comment">// 'sun'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用链式来处理数据</h3>
<p>函数链式一种惰性计算的程序，惰性计算的意思就是当需要时才会执行。这可以避免执行一些可能永不会使用的代码，节省<code>CPU</code>。如果写过一些<code>Jquery</code>代码，那么对于链式应该不陌生。链指的是一连串函数的调用，它们共享一个通用的对象返回值就像组合一样，链有助于写出简明扼要的代码，而且它通常多用于函数式和响应式的<code>JavaScript</code>类库。</p>
<p>举例：统计高年级（也就是4年级及以上的）成绩平均数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> school = [
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">92</span> &#125;,
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">93</span> &#125;,
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">94</span> &#125;,
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">95</span> &#125;,
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">96</span> &#125;,
    &#123; <span class="hljs-attr">grade</span>: <span class="hljs-number">6</span>, <span class="hljs-attr">score</span>: <span class="hljs-number">97</span> &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用函数式思维分解这个问题，可以分解为3个主要步骤：</p>
<ul>
<li>筛选出合适的年级</li>
<li>获取对应年级的成绩</li>
<li>计算出它们的平均数</li>
</ul>
<p>使用<code>Lodash</code>组合这些步骤的函数。</p>
<pre><code class="hljs language-js copyable" lang="js">_.chain(school)
    .filter(<span class="hljs-function"><span class="hljs-params">grade</span> =></span> grade.grade > <span class="hljs-number">3</span>)
    .pluck(<span class="hljs-string">'score'</span>)
    .average()
    .value()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_.chain</code>函数可以添加一个输入对象的状态，从而能够将这些输入转换为所需输出的操作链接在一起。与简单地将数组包裹在_(...)对象不同，其强大之处在于可以链接序列中的任何函数。尽管这是一个复杂的程序，但仍然可以避免创建任何变量，并有效地消除所有循环。</p>
<p>使用<code>_.chain</code>的另一个好处就是可以创建具有惰性计算能力的复杂程序，在调用<code>value()</code>前，并不会真正地执行任何操作。这可能会对程序产生巨大的影响，因为在不需要其结果的情况下，可以跳过运行所有函数。链中的每个函数都以一种不可变的方式来处理由上一个函数构建的新数组。</p>
<p>如果是使用过<code>SQL</code>，就会发现这与<code>SQL</code>有相似之处。比如下表<code>Person</code>:</p>





























<table><thead><tr><th align="center">id</th><th align="center">name</th><th align="center">age</th><th align="center">city</th></tr></thead><tbody><tr><td align="center">1</td><td align="center">zhang</td><td align="center">23</td><td align="center">guangzhou</td></tr><tr><td align="center">2</td><td align="center">li</td><td align="center">24</td><td align="center">shenzhen</td></tr><tr><td align="center">3</td><td align="center">qian</td><td align="center">25</td><td align="center">shanghai</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">SELECT p.name, p.age FROM Person
WHERE p.age > <span class="hljs-number">24</span> and p.city IS NOT <span class="hljs-string">'shanghai'</span>
GROUP BY p.name, p.age
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Lodash</code>支持一种被称为<code>mixins</code>的功能，可以用来为核心库扩展新的函数，并使得它们以相同的方式连接：</p>
<pre><code class="hljs language-js copyable" lang="js">_.mixins(&#123;<span class="hljs-string">'select'</span>, _.pluck,
          <span class="hljs-string">'from'</span>,   _.chain,
          <span class="hljs-string">'where'</span>,  _.filter,
          <span class="hljs-string">'groupBy'</span>,_.sortByOrder&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后就能编写出类似<code>SQL</code>的语句</p>
<pre><code class="hljs language-js copyable" lang="js">_.from(persons)
    .where(<span class="hljs-function"><span class="hljs-params">p</span> =></span> p.age > <span class="hljs-number">24</span> && p.city !== <span class="hljs-string">'shanghai'</span>)
    .groupBy([<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>])
    .select(<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>)
    .value();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">结尾</h2>
<p>本文参考：</p>
<ul>
<li>《JavaScript 函数式编程》</li>
<li>《JavaScript函数式编程指南》</li>
<li><a href="https://llh911001.gitbooks.io/mostly-adequate-guide-chinese/content/" target="_blank" rel="nofollow noopener noreferrer">函数式编程指北</a></li>
</ul>
<p>更多文章请移步<a href="https://github.com/zhangwinwin/FEBlog" target="_blank" rel="nofollow noopener noreferrer">楼主github</a>,如果喜欢请点一下star,对作者也是一种鼓励。</p></div>  
</div>
            