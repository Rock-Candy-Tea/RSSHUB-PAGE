
---
title: '从λ演算到函数式编程聊闭包(1)：闭包概念在Java_PHP_JS中形式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2402'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 06:05:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=2402'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是闭包</h2>
<p>如果让谷哥找一下“闭包”这个词，会发现网上关于闭包的文章已经不计其数</p>
<p><strong>维基百科</strong>上对闭包的解释就很经典：<br>
<code>在计算机科学中**，闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数**。**这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外**。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。 Peter J. Landin 在1964年将术语闭包定义为**一种包含环境成分和控制成分的实体。   [百度百科：](http://baike.baidu.com/link?url=WWhvx0W_VK2XI-OP3OFD2Iz09amJg-mrTUCXiXmrnDYp12txFOB3Kydth0-GOZ9pdn4G6pM00CAL3AKKz5mSdq)**   </code><strong>闭包是可以包含自由（未绑定到特定对象）变量的代码块</strong>；这些变量不是在这个代码块内或者任何全局上下文中定义的，而是在定义代码块的环境中定义（局部变量）。“闭包” 一词来源于以下两者的结合：要执行的代码块（由于自由变量被包含在代码块中，这些自由变量以及它们引用的对象没有被释放）和为自由变量提供绑定的计算环境（作用域）。</p>
<p>闭包概念:</p>
<p>　　<strong>闭包就是有权访问另一个函数作用域中变量的函数</strong>**.**</p>
<p>分析这句话:</p>
<p>　　1.<strong>闭包是定义在函数中的函数</strong>.</p>
<p>　　2.<strong>闭包能访问包含函数的变量</strong>.</p>
<p>　　3.<strong>即使包含函数执行完了, 被闭包引用的变量也得不到释放.</strong></p>
<p>在 Scala、Scheme、Common Lisp、Smalltalk、Groovy、JavaScript、Ruby、 Python、Go、Lua、objective c、swift 以及Java（Java8及以上）等语言中都能找到对闭包不同程度的支持。</p>
<h2 data-id="heading-1">抽象代数中的闭包</h2>
<p>在离散数学（具体的说是抽象代数）里，<strong>如果对一个集合中的每个元素执行某个运算操作，得到的结果还是这个集合的元素，那么就说该集合在这个运算操作下构成闭包</strong>。例如，整数集合在减法运算下构成闭包；但是自然数在减法运算下不构成闭包。</p>
<h3 data-id="heading-2">封闭的定义</h3>
<p>　　有了集合和运算的概念，就可以定义封闭的概念了。</p>
<p>　　非正式地，如果定义于集合A上的运算+的运算结果仍然属于A，那么运算+对于集合A是封闭的。下面给出“封闭”的一个半形式化定义：</p>
<p>　　如果对于任意a1,a2∈A，有a1+a2∈A，那么说二元运算+对于集合A是封闭的。（⊙,+ 与”，“或”）</p>
<p>　　例如“+”对于N+是封闭的，因为任意两个正整数的和结果仍然是正整数；但是“>”对于N+不是封闭的，例如3和5属于N+，但是：3>5=>2∉N+。</p>
<h3 data-id="heading-3">闭包性质</h3>
<p>　　一个集合满足闭包性质当且仅当这个集合在某个运算或某些运算的搜集下是封闭的，其中“某些运算的搜集下封闭”是指这个集合单独闭合在每个运算之下。</p>
<p>　　值得一提的是，之前这条定义往往被作为一条公理引入一个代数结构，叫做“闭包公理”。但是现代集合论往往将运算形式化的定义为集合间的运算，所以将其作为公理引入代数结构是多余的（因为可以通过其它公理间接定义闭包公理），但是对于子集是否闭合的问题，闭包公理仍然有意义。</p>
<p>如此讲下去呢，哎，肯你说。我勒去…好高大上啊，完全看不懂！！！…………好吧。！！至此，打住……关于</p>
<h2 data-id="heading-4">函数式编程中的闭包</h2>
<p>在这一章节开始之前，我需要再和大家明确一个比较纠结的事实，就是在函数式编程领域中当说到“闭包”时，也有可能是指数学领域中闭包的概念，这是因为函数式编程在基础理论与抽象代数有一定亲缘性，所以当在函数式语言著作中讨论“闭包”时，有可能是在抽象数学的上下文中讨论的。然而，在表述上可能会有微妙变化。在函数式语言领域对于数学闭包常用的表述是“如果一个运算的结果仍然能被此运算作用，则这个运算是封闭的”，要注意这只不过是上文提到的“闭包”概念的另一种等价表述而已，如果我们将这个运算的所有结果看做一个集合，那么就可以等价表述说这个运算在这个集合上是封闭的。</p>
<p>而我下面所要阐述的闭包是一种截然不同的概念。所以，当在函数式语言的著作中看到“闭包”时，需要根据上下文环境小心区分其表述哪种概念。</p>
<h3 data-id="heading-5">Lambda演算与自由变量</h3>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFunctional_programming" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Functional_programming" ref="nofollow noopener noreferrer"><strong>函数式编程语言</strong></a><strong>的基础是<a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLambda_calculus" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Lambda_calculus" ref="nofollow noopener noreferrer">lambda演算</a>，这是一套用于研究函数定义、应用和递归的形式系统</strong>，由数学家丘奇在20世纪30年代引入。如果您不太熟悉lambda演算，那么维基百科相关页面是很好的快速入门资料，请原谅我不会完整描述lambda演算（因为已经有很多可以<a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLambda_calculus" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Lambda_calculus" ref="nofollow noopener noreferrer">参考的资料</a>）。</p>
<blockquote>
<p>简单来说lambda演算将计算过程看过一系列的函数代换，例如，下面是加运算的lambda函数（假设+运算已经定义）：λx.λx+y</p>
<p>lambda演算就是反复将函数应用于实际值，并用实际值代替参数，最终得出结果。例如计算7+2：(λx.λx+y)7 2=>(λy.7+y)2=>7+2=>9</p>
<p>首先用第一个参数（7）代替最外层函数的参数（x），然后用第二个参数（2）代替第二层函数的参数（y），最终得到计算结果。</p>
<p>鉴于如果下面大量使用lambda演算描述问题大家可能会崩溃（我也会崩溃），我将改用函数式语言scheme（Lisp的一个方言）来进行问题描述。注意其实scheme在本质上与lambda演算是等价的，只是看起来更好懂，例如不需要遵循lambda演算一个变态的规定：每个函数只允许有一个参数（虽然任何多参数函数式程序都可以通过Currying过程化归为等价的lambda演算）。</p>
<p>下面是用scheme程序对上述lambda演算的等价表示：(define (f x y) (+ x y))</p>
<p>可以这样计算7+2：(f 7 2);Value: 9</p>
<p>下面看一个稍微复杂点的例子：(define (f x) (lambda (y) (+ x y)))</p>
<p>这里定义了函数f，接受一个参数x，特别要注意它的返回值：不是一个值而是一个匿名函数。如果我们把这个函数单独拿出来：(lambda (y) (+ x y))</p>
<p>可以看到，这个匿名函数接收一个参数y，但是却没有参数x！也就是说，如果脱离上下文执行这个函数，则x处于未指定状态，我们说对于这个函数，y是绑定的，而x是自由的。</p>
</blockquote>
<p>一般地：x是一个函数的函数体中的变量，如果x被这个函数的参数指定，则x是绑定于这个函数的，否则说x对于此函数是自由的。</p>
<p>下面可以看到，变量的绑定和自由概念是理解闭包本质的一把钥匙。关于这方面的内容，推荐阅读：《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Frubylouvre%2Farchive%2F2012%2F05%2F03%2F2481252.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/rubylouvre/archive/2012/05/03/2481252.html" ref="nofollow noopener noreferrer">闭包漫谈（从抽象代数及函数式编程角度）</a>》</p>
<h3 data-id="heading-6">程序语言的闭包性质</h3>
<blockquote>
<p>继续上面的scheme程序，我们已经定义了函数f：(define (f x) (lambda (y) (+ x y)))</p>
<p>如果我们运行下面程序：(f 7);Value 13: #[compound-procedure 13]</p>
<p>可以看到，f返回了一个过程（匿名函数），按照函数演算规则，这个函数应该是：(lambda (y) (+ 7 y))</p>
<p>那么下面的运算就很直观了：((f 7) 2);Value: 9</p>
<p>注意这里有一个非常重要的地方（也是闭包性质的关键），那就是这个运算执行了两个函数：f和匿名函数。而f的作用域为(f 7)，这就是说，其实在(f 7)之后，f这个函数就结束了，而x（这里被赋值为7）是f的私有变量（绑定于f），那么程序设计语言的设计者就有两种选择：</p>
<ul>
<li>
<p>第一，在函数超出其作用域后立即销毁其绑定变量，如果是这样的话，((f 7) 2) 是无法得出结果的，因为在外层的f运算结束后，存放数值“7”的变量就被释放了，所以匿名函数无法得到其自由变量x的值；</p>
</li>
<li>
<p>第二，如果一个函数返回另一个函数，而被返回函数又需要外层函数的变量时，不会立即释放这个变量，而是允许被返回的函数引用这些变量。支持这种机制的语言称为支持闭包机制，而这个内部函数连同其自由变量就形成了一个闭包。</p>
</li>
</ul>
<p>显然scheme的设计者做了第二种选择。</p>
<p>上面的这段话不太好理解，但是请务必多读几遍，因为，这就是闭包的全部。</p>
</blockquote>
<p>在程序语言中，<strong>闭包就是一种语法糖，它以很自然的形式，把我们的目的和我们的目的所涉及的资源全给自动打包在一起，以某种自然、尽量不让人误解的方式让人来使用</strong><code>。</code>至于其具体实现，我个人意见，在不影响使用的情况下，不求甚解即可。在很多情况下，需要在一段代码里去访问外部的局部变量，不提供这种语法糖，需要写非常多的代码，有了闭包这个语法糖，就不用写这么多代码，自然而然的就用了。</p>
<h3 data-id="heading-7">java闭包，推荐阅读《深入理解Java闭包概念》</h3>
<p>简单理解：<strong>闭包能够将一个方法作为一个变量去存储，这个方法有能力去访问所在类的自由变量。</strong></p>
<p>Java中闭包实现，关键点：</p>
<ul>
<li>
<p>如何用变量去存储方法？</p>
</li>
<li>
<p>java中能够保存方法的变量指的就是普通的对象</p>
</li>
<li>
<p>如何让这个普通对象能够访问所在类的自由变量？</p>
</li>
<li>
<p>纯天然的解决办法是：内部类。内部类能够访问外部类的所有属性及方法。</p>
</li>
<li>
<p>隐藏具体实现是内部类的作用之一，如何保证隐藏具体实现的同时还能将闭包传递到外部使用？</p>
</li>
</ul>
<p>让内部类实现通用接口，然后将内部类对象向上转型为接口类型。</p>
<p>上述解决办法就是Java最常用的闭包实现办法（内部类+接口）</p>
<pre><code class="copyable">public class Milk &#123;  
    public final static String name = "纯牛奶";//名称  
    private static int num = 16;//数量  
    public Milk()  
    &#123;  
        System.out.println(name+"：16/每箱");  
    &#125;   
    /** 
     * 闭包 
     * @return 返回一个喝牛奶的动作 
     */  
    public Active HaveMeals()  
    &#123;  
        return new Active()  
                &#123;  
                    public void drink()  
                    &#123;  
                        if(num == 0)  
                        &#123;  
                            System.out.println("木有了，都被你丫喝完了.");  
                            return;  
                        &#125;  
                        num--;  
                        System.out.println("喝掉一瓶牛奶");  
                    &#125;  
                &#125;;  
    &#125;  
    /** 
     * 获取剩余数量 
     */  
    public void currentNum()  
    &#123;  
        System.out.println(name+"剩余："+num);  
    &#125;  
&#125;  
/** 
 * 通用接口 
 */  
interface Active  
&#123;  
    void drink();  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">php闭包</h3>
<p>php中，闭包（Closure）又叫做匿名函数，也就是没有定义名字的函数。</p>
<pre><code class="copyable">//例一
//在函数里定义一个匿名函数，并且调用它
function printStr() &#123;
    // 定义一个闭包，并把它赋给变量 $func 
    $func = function( $str ) &#123;
        echo $str;
    &#125;;
    $func( 'some string' );
&#125;
printStr();

//例二
//在函数中把匿名函数返回，并且调用它
function getPrintStrFunc() &#123;
    $func = function( $str ) &#123;
        echo $str;
    &#125;;
    return $func;
&#125;
$printStrFunc = getPrintStrFunc();
$printStrFunc( 'some string' );

//例三
//把匿名函数当做参数传递，并且调用它
function callFunc( $func ) &#123;
    $func( 'some string' );
&#125;
$printStrFunc = function( $str ) &#123;
    echo $str;
&#125;;
callFunc( $printStrFunc );
//也可以直接将匿名函数进行传递。如果你了解js，这种写法可能会很熟悉
callFunc( function( $str ) &#123;
    echo $str;
&#125; );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">javascript闭包</h3>
<pre><code class="copyable">function f(x)&#123;
    return function(y) &#123;
        return x + y;
    &#125;;
&#125;
var lam = f(7);
console.log(lam(2));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于java，闭包用的真的不多，在JS，闭包是必考题。下篇讲解JS闭包：《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2016_0316_7712.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2016_0316_7712.html" ref="nofollow noopener noreferrer">从抽象代数漫游函数式编程(2)：话说JavaScript闭包</a>》</p>
<p>参考文章：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Frubylouvre%2Farchive%2F2012%2F05%2F03%2F2481252.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/rubylouvre/archive/2012/05/03/2481252.html" ref="nofollow noopener noreferrer">闭包漫谈（从抽象代数及函数式编程角度）</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.codinglabs.org%2Fhtml%2Fclosure-perspective-of-abstract-mathematic-and-functional-language.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.codinglabs.org/html/closure-perspective-of-abstract-mathematic-and-functional-language.html" ref="nofollow noopener noreferrer">www.codinglabs.org/html/closur…</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fbrendaneich.com%2F2008%2F04%2Fpopularity%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://brendaneich.com/2008/04/popularity/" ref="nofollow noopener noreferrer">Brendan Eich的自述</a> <a href="https://link.juejin.cn/?target=http%3A%2F%2Fbrendaneich.com%2F2008%2F04%2Fpopularity%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://brendaneich.com/2008/04/popularity/" ref="nofollow noopener noreferrer">brendaneich.com/2008/04/pop…</a></p>
<p>深入理解Java闭包概念 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fjava%2FjavaBase%2F7967.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/java/javaBase/7967.html" ref="nofollow noopener noreferrer">www.zhoulujun.cn/html/java/j…</a></p>
<p>转载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/" ref="nofollow noopener noreferrer">本站</a>文章《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2015_0814_240.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2015_0814_240.html" ref="nofollow noopener noreferrer">从λ演算到函数式编程聊闭包(1)：闭包概念在Java/PHP/JS中形式</a>》,<br>
请注明出处：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2FECMAScript%2Fjs6%2F2015_0814_240.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/ECMAScript/js6/2015_0814_240.html" ref="nofollow noopener noreferrer">www.zhoulujun.cn/html/webfro…</a></p></div>  
</div>
            