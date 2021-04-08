
---
title: '【前端见外】我解决了一个看似非常愚蠢的JS问题！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f235820ebce6440085953539da1f9213~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 21:46:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f235820ebce6440085953539da1f9213~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文作者：Alexander Troup</p>
<p>翻译：尴尬风流</p>
<p>原文链接：<a href="https://javascript.plainenglish.io/solving-a-stupid-javascript-problem-aa54e26e3605" target="_blank" rel="nofollow noopener noreferrer">Solving a stupid JavaScript problem</a></p>
<p>个人翻译，转载请注明出处，文章中有什么问题欢迎大家在评论中指出</p>
</blockquote>
<p>故事要从 Tomasz Lakomy 发的一条推特讲起，他问了一个问题。假如你在面试时，面试官问了你这样一道问题，你该怎么办。</p>
<img alt="image-20210405213759025" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f235820ebce6440085953539da1f9213~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>关于在面试中如何应对这个问题，我觉得要看这个问题的关注点是什么。如果问题的关注点是tree变量的最终值是什么的话，那么可以直接让面试官滚蛋，或者我可能会先复制到浏览器的控制台运行一下，看看结果，然后再让面试官滚蛋。</p>
<p>然而如果问题的关键在于，面试官想看看你会如何解决这个问题，那么这就有趣多了，并且会引出很多关于JavaScript语言和编译器工作方式的奇葩之处。因此，在这篇文章中，我将深入研究这个奇葩的东西，并看看能从中引出哪些有趣的东西。</p>
<p>我还在Twitch上发布了一篇文章，详述了解决这个问题的过程。文章虽然很长，但却给了大家提供了另外一个视角，让大家了解如何一步一步地解决这类问题。</p>
<h2 data-id="heading-0">整体思想</h2>
<p>首先我们把它复制到代码框中，这样也方便各位读者复制粘贴到控制台执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>, d = b, u = b;
<span class="hljs-keyword">const</span> tree = ++d * d*b * b++ +
              + --d+ + +b-- +
                 + +d*b+ +
                     u
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我第一眼就注意到了这么几件事。首先有一些为了应对JavaScript编译器的小把戏，我们都知道，JavaScript编译器通常会在每行末尾加上分号，除非当前行的表达式并不完整。在这段代码中，每行末尾的 <code>+</code> 告诉编译器不要终止这个语句。</p>
<p>代码的第一行所做的只是创建了三个变量，并将它们都赋值为3。3是b的初始值，所以当我们将b的值拷贝给其他变量时，会首先创建一个新的变量，然后把3赋值给这个新的变量（译者注：即值传递）。如果JavaScript通过引用来对变量赋值的话，那么每一个新的变量都会指向之前使用的变量，但不会自己全部创建一个值（译者注：即引用传递）。</p>
<blockquote>
<p>阅读更多：<a href="https://medium.com/nodesimplified/javascript-pass-by-value-and-pass-by-reference-in-javascript-fcf10305aa9c" target="_blank" rel="nofollow noopener noreferrer">JavaScript中的值传递和引用传递</a></p>
</blockquote>
<h2 data-id="heading-1">操作符优先级和结合性</h2>
<p>以下所谈的一些概念是解决这个问题的钥关键所在。我将会解释每一个概念，但总的说来，它们决定了一个JavaScript表达式求值的顺序。</p>
<h3 data-id="heading-2">操作符优先级</h3>
<p>提问：下面两个表达式有什么区别？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">3</span> + <span class="hljs-number">5</span> * <span class="hljs-number">5</span>

<span class="hljs-number">5</span> * <span class="hljs-number">5</span> + <span class="hljs-number">3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个表达式的结果是相同的，任何学过最基本的数学知识的人都知道，乘法的优先级要高于加法。有这样一个叫做<code>BODMAS</code>的口诀，即先括号（Bracket）、再按顺序（Order）、先乘除（Division & Multiplication）、后加减（Addition & Subtraction）。在JavaScript中，有类似的概念，称为运算符优先级，它指的是我们在对表达式求值时，应该遵循怎样的顺序。如果我们想要先计算 <code>3 + 5</code> 的值，我们只需要进行如下的操作：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">( <span class="hljs-number">3</span> + <span class="hljs-number">5</span> ) * <span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 <code>()</code> 运算符的优先级高于 <code>*</code>，因此括号中的表达式将会先被计算。</p>
<p>每一个JavaScript操作符都有一个优先级，在刚刚我们要解决的问题表达式中有这么多的操作符，我们首先要做的就是看哪些操作符优先级更高，会先被计算。尤其是 <code>++</code> 和 <code>--</code> 这两个操作符会改变变量 <code>b</code>和 <code>d</code> 的值，我们需要知道这两个操作符与表达式中的其他部分在被计算时的先后顺序。</p>
<blockquote>
<p>阅读更多：<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence" target="_blank" rel="nofollow noopener noreferrer">JavaScript操作符优先级表</a></p>
</blockquote>
<h3 data-id="heading-3">结合性</h3>
<p>结合性用于确定在一个表达式中哪些操作符的优先级是相同的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">a + b + c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的表达式中，不需要判断运算符的优先级，因为我们只有一个运算符。因此，我们是以 <code>(a+b)+c</code> 的方式还是以 <code>a+(b+c)</code> 的方式来计算呢？</p>
<p>我知道最后的答案是一样的，但是编译器需要知道，这样它才能计算出表达式的结果，并继续计算其他部分。在这种情况下，编译器会选择<code>(a+b)+c</code>这种方案，因为 <code>+</code> 运算符是左结合的，也就是说它会先计算两个优先级相同的运算符中，左边的（第一个）运算符两侧的值。</p>
<p>“为什么不让所有的运算符都是左结合的呢？”， 你也许会这样问。</p>
<p>我们来看下面这个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">a = b + c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们让所有运算符都是左结合的话，那么就会得到：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(a = b) + c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这看起来也太奇怪了，而且并不是我想要表达的意思。如果我们想让这个表达式只使用左结合来实现的话，我们需要这样做。</p>
<pre><code class="hljs language-javas copyable" lang="javas">a + b = c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就变成了 <code>(a+b)=c</code>，或者更明确的说，我们先做 <code>a+b</code>，然后将 <code>c</code> 赋值给该结果。</p>
<p>如果我们这样写的话，JavaScript编译器就会完全懵了，我们之所以对不同操作符采用不同的结合性，是为了让代码更易读。当你读到 <code>a = b + c</code> 的时候，表达式的顺序更容易被人所接受。尽管实际上这里同时运用了左结合（<code>+</code>）和右结合（<code>=</code>）的操作符，但是对人来说，读起来却更加自然，容易接受。</p>
<p>你现在可能已经注意到，对于 <code>a = b + c</code>，有一个结合性的问题。当两个操作符有不同的结合性的情况下，你怎么知道先求哪部分表达式的值呢？答案就是哪个运算符的优先级更高就先计算哪个部分！在这个例子中，<code>+</code> 运算符优先级高，所以它先被执行。</p>
<p>我在结尾的注释中加入了更详细的解释。</p>
<h4 data-id="heading-4">理解刚刚的表达式是如何被计算的</h4>
<p>现在我们对这些概念有了一个基本的认识，我们可以开始解决我们的问题。在刚刚的表达式中，有许多各种各样的操作符，没有括号来帮助理解，对我们脆弱的大脑是一种摧残。因此，让我们增加一些括号来帮助理解。我们要做的就是列出所有使用到的运算符，以及它们的优先级和结合性。</p>


















































<table><thead><tr><th align="center">变量x、y和操作符</th><th align="center">优先级（数值越大优先级越高）</th><th align="center">结合性（左/右）</th></tr></thead><tbody><tr><td align="center">x++</td><td align="center">18</td><td align="center">不相关</td></tr><tr><td align="center">x--</td><td align="center">18</td><td align="center">不相关</td></tr><tr><td align="center">++x</td><td align="center">17</td><td align="center">右</td></tr><tr><td align="center">--x</td><td align="center">17</td><td align="center">右</td></tr><tr><td align="center">+x</td><td align="center">17</td><td align="center">左</td></tr><tr><td align="center">*</td><td align="center">15</td><td align="center">左</td></tr><tr><td align="center">x + y</td><td align="center">14</td><td align="center">左</td></tr><tr><td align="center">=</td><td align="center">3</td><td align="center">右</td></tr></tbody></table>
<h4 data-id="heading-5">括号</h4>
<p>这里值得一提的是，将括号加在正确的位置上是一件很棘手的事情。我可以保证我每一步的计算都是都是正确的，但这并不能保证我的括号加的位置永远是正确的！如果有人知道有什么工具可以自动加括号，请告诉我。</p>
<p>让我们弄清楚表达式的计算顺序，并加上括号来帮助理解。我将一步一步地展示我是如何得出最终结果的，基本上遵循的就是按照优先级的原则来逐步计算。</p>
<h4 data-id="heading-6">处理<code>x++</code>运算符和<code>x--</code>运算符</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = ++d * d*b * (b++) +
 + --d+ + +(b--) +
 + +d*b+ +
 u
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">处理<code>+</code>、<code>++x</code>、<code>--x</code>运算符</h4>
<p>我们在这里有一个小小的问题，我会先计算 <code>+</code> 运算符，等一会我们遇到问题时再去解决。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = ++d * d*b * (b++) +
 + --d+ (+(+(b--))) +
 (+(+(d*b+ (+
 u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在到了比较难办的地方。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = ++d * d*b * (b++) +
              + --d+ (+(+(b--))) +
                  (+(+(d*b+ (+
                        u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我把出现问题的地方（第二行开头<code>+ --d</code>）标了出来。<code>--</code>和 <code>+()</code> 有相同的优先级。那么，我们应该按照怎样的顺序计算呢？让我用更简单的方式来说清楚这个问题。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> d = <span class="hljs-number">10</span>
<span class="hljs-keyword">const</span> answer = + --d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一定要注意，这里的 <code>+</code> 并不是加法（二元运算），而是一元运算的 <code>+</code>，也就是正数的意思。这和 <code>-1</code> 没什么区别，只不过它是 <code>+1</code>。</p>
<blockquote>
<p>译者注： 上面的话是关键，第二行中间3个加号中，只有第一个加号是二元运算，后两个均为一元运算。</p>
</blockquote>
<p>答案就是，我们会按照从右到左的顺序进行计算（先减减，再加），因为这种优先级的运算符是右结合的。</p>
<blockquote>
<p>译者注：因为一元运算符需要一个操作数</p>
</blockquote>
<p>所以这一部分表达式写成了：<code>+ (--d)</code></p>
<p>为了帮助你理解，试想下假设所有的操作符都是一样的，在这种情况下，<code>+ +1</code>和<code>(+ (+1))</code>相同，同理<code>1-1-1</code>和<code>((1-1)-1)</code>也相同，你注意到右结合操作符和左结合操作符的不同了吗？</p>
<p>将这个逻辑应用到解决我们的表达式求值问题上，就得到了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = ++d * d*b * (b++) +
             (+ (--d)) + (+(+(b--))) +
                 (+(+(d*b+ (+
                       u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后把 <code>++x</code>运算符的括号加上：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = (++d) * d*b * (b++) +
         (+ (--d)) + (+(+(b--))) +
             (+(+(d*b+ (+
                   u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">处理<code>*</code>运算符</h4>
<p>我们又要处理结合性的问题，但这次都是同一个运算符，而且都是左结合的。和上一步相比，这简直是小菜一碟！</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tree = ((((++d) * d) * b) * (b++)) +
                 (+ (--d)) + (+(+(b--))) +
                    (+(+((d*b) +
                          (+u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经到了可以开始计算的阶段。我们还可以为赋值操作符添加额外的括号，但我认为这样做属于画蛇添足，所以我没有使用它。请注意，上面的表达式只是一个更复杂的 <code>x = a + b + c</code>。</p>
<p>我们其实可以省略掉一些一元运算符，但我现在要把它们留在其中，以防万一。</p>
<p>通过将表达式分割成多个部分，我们可以从各个部分开始逐步进行计算。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>, d = b, u = b;
 
<span class="hljs-keyword">const</span> treeA = ((((++d) * d) * b) * (b++))
<span class="hljs-keyword">const</span> treeB = (+ (--d)) + (+(+(b--)))
<span class="hljs-keyword">const</span> treeC = (+(+((d*b) + (+u))))
<span class="hljs-keyword">const</span> tree = treeA + treeB + treeC
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经完成了这些工作，我们可以计算各个部分的值了。从 <code>treeA</code> 开始</p>
<h4 data-id="heading-9">计算TreeA</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>, d = b, u = b;
<span class="hljs-keyword">const</span> treeA = (((++d) * d) * b) * (b++)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先要做的是计算 <code>++d</code>，它既会返回 <code>4</code> ，又会将<code>d</code> 自加一。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 4</span>

((<span class="hljs-number">4</span> * d) * b) * (b++)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来要计算<code>4乘d</code>，我们知道此时 <code>d</code>是<code>4</code>，所以4乘4是<code>16</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 4</span>

(<span class="hljs-number">16</span> * b) * (b++)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有趣的来了，我们要在 <code>b</code> <strong>自加一之前乘b</strong>，因为我们要从左到右进行计算。<code>16 * 3 = 48</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 4</span>

<span class="hljs-number">48</span> * (b++)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面我们谈到 <code>++</code> 比 <code>*</code> 有更高的运算符优先级，所以可以写成 <code>48 * b++</code> ，但这里值得注意的是，因为 <code>b++</code> 是先返回值再自加一，而不是先自加一再返回值。因此，虽然b的结尾是4，但我们要乘的值将是<code>3</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 4</span>

<span class="hljs-number">48</span> * <span class="hljs-number">3</span>

<span class="hljs-comment">// b = 4</span>
<span class="hljs-comment">// d = 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而48*3结果是 <code>144</code>，所以第一部分计算完了，此时b和d的值都是4，表达结果是144</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">4</span>, d = <span class="hljs-number">4</span>, u = <span class="hljs-number">3</span>;
 
<span class="hljs-keyword">const</span> treeA = <span class="hljs-number">144</span>
<span class="hljs-keyword">const</span> treeB = (+ (--d)) + (+(+(b--)))
<span class="hljs-keyword">const</span> treeC = (+(+((d*b) + (+u))))
<span class="hljs-keyword">const</span> tree = treeA + treeB + treeC
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">计算TreeB</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> treeB = (+ (--d)) + (+(+(b--)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个表达式中我们会发现，一元运算符并没有发挥什么实际的作用。如果我们把它们省略掉，就可以大大简化表达式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 4</span>
<span class="hljs-comment">// d = 4</span>

<span class="hljs-keyword">const</span> treeB = (--d) + (b--)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剩余部分的表达式我们会感觉似曾相识。--d将返回3，而b--将返回4，表达式计算后，b和d的值都变成了3。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> treeB = <span class="hljs-number">3</span> + <span class="hljs-number">4</span>

<span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以最初的问题简化成了这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>, d= <span class="hljs-number">3</span>, u = <span class="hljs-number">3</span>;
 
<span class="hljs-keyword">const</span> treeA = <span class="hljs-number">144</span>
<span class="hljs-keyword">const</span> treeB = <span class="hljs-number">7</span>
<span class="hljs-keyword">const</span> treeC = (+(+((d*b) + (+u))))
<span class="hljs-keyword">const</span> tree = treeA + treeB + treeC
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">计算TreeC</h4>
<p>终于到了主场了!</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 3</span>
<span class="hljs-comment">// u = 3</span>

<span class="hljs-keyword">const</span> treeC = (+(+((d*b) + (+u))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们从清除那些讨厌的一元运算符开始吧</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 3</span>
<span class="hljs-comment">// u = 3</span>

<span class="hljs-keyword">const</span> treeC = (+(+((d*b) + u)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>干掉了一个，这里有大量的括号，处理起来要小心一点。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// b = 3</span>
<span class="hljs-comment">// d = 3</span>
<span class="hljs-comment">// u = 3</span>

<span class="hljs-keyword">const</span> treeC = (d*b) + u
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就很容易了。3*3是9，9+3是12，只剩最后一步了。</p>
<h3 data-id="heading-12">答案出来了！</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>, d= <span class="hljs-number">3</span>, u = <span class="hljs-number">3</span>;
 
<span class="hljs-keyword">const</span> treeA = <span class="hljs-number">144</span>
<span class="hljs-keyword">const</span> treeB = <span class="hljs-number">7</span>
<span class="hljs-keyword">const</span> treeC = <span class="hljs-number">12</span>
<span class="hljs-keyword">const</span> tree = treeA + treeB + treeC
<span class="copy-code-btn">复制代码</span></code></pre>
<p>144+7+12是163。答案是163。</p>
<h3 data-id="heading-13">总结</h3>
<p>JavaScript经常让你喜忧参半。但是，如果了解了语言是如何组织在一起的，你就可以从底层来理解他为什么会是这个样子。</p>
<p>此外，解决问题的过程可能比答案更具有启发意义，你在解决问题时想出的种种解决方案会让你收获颇丰。</p>
<p>值得一说的是，我在推理的过程中，不断使用浏览器控制台验证其正确性，并且跟注重于从结果反向推断，而不是正向去思考这个问题。</p>
<p>即使知道如何解决这个问题，在解决问题的过程中也遇到了许许多多的语法歧义的问题，相信你在看这棵树（表达式）的时候也会产生相同的疑问！我记录了其中的一些，不过每一个问题都值得单独写一篇文章！</p>
<p>在此，我也要向 AnthonyPAlicea 表示赞扬，没有他的课程，我永远也搞不清楚这些东西，同时也要感谢 tlakomy 提出了这个问题。</p>
<blockquote>
<p>我建立了一个技术交流群，每天会在群里发技术名词相关的英语小卡片，大家可以加「xiedaimala03」进群，记得备注「程序员英语」，交流技术的同时也顺便学点英语，何乐而不为呢！</p>
<p>也欢迎大家关注公众号「前端见外」获取每日英语小卡片。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            