
---
title: 'kotlin高阶函数'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://juejin.cn/post/6992185916181708808'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 04:54:54 GMT
thumbnail: 'https://juejin.cn/post/6992185916181708808'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在Kotlin中，高阶函数即指：将函数用作一个函数的参数或者返回值的函数。</p>
<h1 data-id="heading-0">1. 将函数用作函数参数的情况的高阶函数</h1>
<p>这里介绍字符串中的sumBy&#123;&#125;高阶函数。先看一看源码：</p>
<h2 data-id="heading-1">1.1、将函数用作函数参数的情况的高阶函数</h2>
<p>这里介绍字符串中的sumBy&#123;&#125;高阶函数。先看一看源码</p>
<pre><code class="copyable">// sumBy函数的源码
public inline fun CharSequence.sumBy(selector: (Char) -> Int): Int &#123;
    var sum: Int = 0
    for (element in this) &#123;
        sum += selector(element)
    &#125;
    return sum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码说明：</p>
<ol>
<li>大家这里可以不必纠结<code>inline</code>，和<code>sumBy</code>函数前面的<code>CharSequence.</code>。因为这是<code>Koltin</code>中的<code>内联函数</code>与<code>扩展功能</code>。在后面的章节中会给大家讲解到的。这里主要分析高阶函数，故而这里不多做分析。</li>
<li>该函数返回一个<code>Int</code>类型的值。并且接受了一个<code>selector()</code>函数作为该函数的参数。其中，<code>selector()</code>函数接受一个<code>Char</code>类型的参数，并且返回一个<code>Int</code>类型的值。</li>
<li>定义一个<code>sum</code>变量，并且循环这个字符串，循环一次调用一次<code>selector()</code>函数并加上<code>sum</code>。用作累加。其中<code>this</code>关键字代表字符串本身。</li>
</ol>
<p>所以这个函数的作用是：<strong>把字符串中的每一个字符转换为<code>Int</code>的值，用于累加，最后返回累加的值</strong></p>
<p>例：</p>
<pre><code class="copyable">val testStr = "abc"
val sum = testStr.sumBy &#123; it.toInt() &#125;
println(sum)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">1.2 将函数用作一个函数的返回值的高阶函数</h2>
<p>这里使用官网上的一个例子来讲解。<code>lock()</code>函数，先看一看他的源码实现</p>
<pre><code class="copyable">fun <T> lock(lock: Lock, body: () -> T): T &#123;
    lock.lock()
    try &#123;
        return body()
    &#125;
    finally &#123;
        lock.unlock()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码说明：</p>
<ol>
<li>
<p>这其中用到了<code>kotlin</code>中<code>泛型</code>的知识点，这里赞不考虑。我会在后续的文章为大家讲解。</p>
</li>
<li>
<p>从源码可以看出，该函数接受一个<code>Lock</code>类型的变量作为参数<code>1</code>，并且接受一个无参且返回类型为<code>T</code>的函数作为参数<code>2</code>.</p>
</li>
<li>
<p>该函数的返回值为一个函数，我们可以看这一句代码<code>return body()</code>可以看出。</p>
<p>例：使用<code>lock</code>函数，下面的代码都是伪代码，我就是按照官网的例子直接拿过来用的</p>
<pre><code class="copyable">fun toBeSynchronized() = sharedResource.operation()
val result = lock(lock, ::toBeSynchronized) 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>其中，<code>::toBeSynchronized</code>即为对函数<code>toBeSynchronized()</code>的引用，其中关于双冒号<code>::</code>的使用在这里不做讨论与讲解。</p>
<p>上面的写法也可以写作：</p>
<pre><code class="copyable">val result = lock(lock, &#123;sharedResource.operation()&#125; )
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">1.3 高阶函数的使用</h2>
<p>​        在上面的两个例子中，我们出现了<code>str.sumBy&#123; it.toInt &#125;</code>这样的写法。其实这样的写法在前一章节<code>Lambda使用</code>中已经讲解过了。这里主要讲高阶函数中对<code>Lambda语法</code>的简写。从上面的例子我们的写法应该是这样的：</p>
<p>从上面的例子我们的写法应该是这样的：</p>
<pre><code class="copyable">str.sumBy( &#123; it.toInt &#125; )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是根据<code>Kotlin</code>中的约定，即当函数中只有一个函数作为参数，并且您使用了<code>lambda</code>表达式作为相应的参数，则可以省略函数的小括号<code>()</code>。故而我们可以写成：</p>
<pre><code class="copyable">str.sumBy&#123; it.toInt &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个约定，即当函数的最后一个参数是一个函数，并且你传递一个<code>lambda</code>表达式作为相应的参数，则可以在圆括号之外指定它。故而上面例<code>2</code>中的代码我们可写成：</p>
<p>val result = lock(lock)&#123;     sharedResource.operation() &#125;</p>
<h1 data-id="heading-4">2. 自定义高阶函数</h1>
<p>我记得在上一章节中中我们写了一个例子：</p>
<pre><code class="copyable">// 源代码
fun test(a : Int , b : Int) : Int&#123;
    return a + b
&#125;

fun sum(num1 : Int , num2 : Int) : Int&#123;
    return num1 + num2
&#125;

// 调用
test(10,sum(3,5)) // 结果为：18

// lambda
fun test(a : Int , b : (num1 : Int , num2 : Int) -> Int) : Int&#123;
    return a + b.invoke(3,5)
&#125;

// 调用
test(10,&#123; num1: Int, num2: Int ->  num1 + num2 &#125;)  // 结果为：18
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出上面的代码中，直接在我的方法体中写死了数值，这在开发中是很不合理的，并且也不会这么写。上面的例子只是在阐述<code>Lambda</code>的语法。接下来我另举一个例子：</p>
<p>例：传入两个参数，并传入一个函数来实现他们不同的逻辑</p>
<p>例：</p>
<pre><code class="copyable">private fun resultByOpt(num1 : Int , num2 : Int , result : (Int ,Int) -> Int) : Int&#123;
    return result(num1,num2)
&#125;

private fun testDemo() &#123;
    val result1 = resultByOpt(1,2)&#123;
        num1, num2 ->  num1 + num2
    &#125;

    val result2 = resultByOpt(3,4)&#123;
        num1, num2 ->  num1 - num2
    &#125;

    val result3 = resultByOpt(5,6)&#123;
        num1, num2 ->  num1 * num2
    &#125;

    val result4 = resultByOpt(6,3)&#123;
        num1, num2 ->  num1 / num2
    &#125;

    println("result1 = $result1")
    println("result2 = $result2")
    println("result3 = $result3")
    println("result4 = $result4")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="copyable">result1 = 3
result2 = -1
result3 = 30
result4 = 2  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子是根据传入不同的<code>Lambda</code>表达式，实现了两个数的<code>+、-、*、/</code>。
当然了，在实际的项目开发中，自己去定义高阶函数的实现是很少了，因为用系统给我们提供的高阶函数已经够用了。不过，当我们掌握了<code>Lambda</code>语法以及怎么去定义高阶函数的用法后。在实际开发中有了这种需求的时候也难不倒我们了。</p>
<h1 data-id="heading-5">4. 常用标准高阶函数使用</h1>
<h2 data-id="heading-6">4.1 TODO函数</h2>
<p>这个函数不是一个高阶函数，它只是一个抛出异常以及测试错误的一个普通函数。</p>
<p>这个函数不是一个高阶函数，它只是一个抛出异常以及测试错误的一个普通函数。</p>
<blockquote>
<p>此函数的作用：显示抛出<code>NotImplementedError</code>错误。<code>NotImplementedError</code>错误类继承至<code>Java</code>中的<code>Error</code>。我们看一看他的源码就知道了：</p>
</blockquote>
<pre><code class="copyable">public class NotImplementedError(message: String = "An operation is not implemented.") : Error(message)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TODO</code>函数的源码</p>
<pre><code class="copyable">@kotlin.internal.InlineOnly
public inline fun TODO(): Nothing = throw NotImplementedError()
​
@kotlin.internal.InlineOnly
public inline fun TODO(reason: String): Nothing = 
throw NotImplementedError("An operation is not implemented: $reason")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例说明：</p>
<pre><code class="copyable">fun main(args: Array<String>) &#123;
    TODO("测试TODO函数，是否显示抛出错误")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<p><img src="https://juejin.cn/post/6992185916181708808" alt="image-20210803172339305" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">4.2 run()</h2>
<p><code>run</code>函数这里分为两种情况讲解，因为在源码中也分为两个函数来实现的。采用不同的<code>run</code>函数会有不同的效果。</p>
<h4 data-id="heading-8">4.2.1、run()</h4>
<p>我们看下其源码：</p>
<pre><code class="copyable">public inline fun <R> run(block: () -> R): R &#123;
  contract &#123;
       callsInPlace(block, InvocationKind.EXACTLY_ONCE)
  &#125;
  return block()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们只关心<code>return block()</code>这行代码。从源码中我们可以看出，<code>run</code>函数仅仅是执行了我们的<code>block()</code>，即一个<code>Lambda</code>表达式，而后返回了执行的结果。</p>
<p><strong>用法1：</strong></p>
<blockquote>
<p>当我们需要执行一个<code>代码块</code>的时候就可以用到这个函数,并且这个代码块是独立的。即我可以在<code>run()</code>函数中写一些和项目无关的代码，因为它不会影响项目的正常运行。</p>
</blockquote>
<p>例: 在一个函数中使用</p>
<pre><code class="copyable">private fun testRun1() &#123;
    val str = "kotlin"
​
    run&#123;
        val str = "java"   // 和上面的变量不会冲突
        println("str = $str")
    &#125;
​
    println("str = $str")
&#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">str = java
str = kotlin
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用法2：</strong></p>
<blockquote>
<p>因为<code>run</code>函数执行了我传进去的<code>lambda</code>表达式并返回了执行的结果，所以当一个业务逻辑都需要执行同一段代码而根据不同的条件去判断得到不同结果的时候。可以用到<code>run</code>函数</p>
</blockquote>
<p>例：都要获取字符串的长度。</p>
<pre><code class="copyable">val index = 3
val num = run &#123;
    when(index)&#123;
        0 -> "kotlin"
        1 -> "java"
        2 -> "php"
        3 -> "javaScript"
        else -> "none"
    &#125;
&#125;.length
println("num = $num")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="copyable">num = 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这个例子没什么实际的意义。</p>
<h2 data-id="heading-9">4.2.2、T.run()</h2>
<p>其实<code>T.run()</code>函数和<code>run()</code>函数差不多，关于这两者之间的差别我们看看其源码实现就明白了：</p>
<pre><code class="copyable">public inline fun <T, R> T.run(block: T.() -> R): R &#123;
    contract &#123;
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    &#125;
    return block()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码中我们可以看出，<code>block()</code>这个函数参数是一个扩展在<code>T</code>类型下的函数。这说明我的<code>block()</code>函数可以可以使用当前对象的上下文。所以当我们传入的<code>lambda</code>表达式想要使用当前对象的上下文的时候，我们可以使用这个函数。</p>
<p><strong>用法：</strong></p>
<blockquote>
<p>这里就不能像上面<code>run()</code>函数那样当做单独的一个<code>代码块</code>来使用。</p>
</blockquote>
<p>例：</p>
<pre><code class="copyable">val str = "kotlin"
str.run &#123;
    println( "length = $&#123;this.length&#125;" )
    println( "first = $&#123;first()&#125;")
    println( "last = $&#123;last()&#125;" )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="copyable">length = 6
first = k
last = n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在其中，可以使用<code>this</code>关键字，因为在这里它就代码<code>str</code>这个对象，也可以省略。因为在源码中我们就可以看出，<code>block</code>() 就是一个<code>T</code>类型的扩展函数。</p>
<p>这在实际的开发当中我们可以这样用：</p>
<p>例： 为<code>TextView</code>设置属性。</p>
<pre><code class="copyable">val mTvBtn = findViewById<TextView>(R.id.text)
mTvBtn.run&#123;
    text = "kotlin"
    textSize = 13f
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4.3 with()函数</h2>
<p>其实<code>with()</code>函数和<code>T.run()</code>函数的作用是相同的，我们这里看下其实现源码：</p>
<pre><code class="copyable">public inline fun <T, R> with(receiver: T, block: T.() -> R): R &#123;
    contract &#123;
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    &#125;
    return receiver.block()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们可以看出和<code>T.run()</code>函数的源代码实现没有太大的差别。故而这两个函数的区别在于：</p>
<blockquote>
<ol>
<li><code>with</code>是正常的高阶函数，<code>T.run()</code>是扩展的高阶函数。</li>
<li><code>with</code>函数的返回值指定了<code>receiver</code>为接收者。</li>
</ol>
</blockquote>
<p>故而上面的<code>T.run()</code>函数的列子我也可用<code>with</code>来实现相同的效果：</p>
<p>例：</p>
<pre><code class="copyable">val str = "kotlin"
with(str) &#123;
    println( "length = $&#123;this.length&#125;" )
    println( "first = $&#123;first()&#125;")
    println( "last = $&#123;last()&#125;" )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="copyable">length = 6
first = k
last = n
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">4.4 T.apply()函数</h2>
<p>我们先看下<code>T.apply()</code>函数的源码：</p>
<pre><code class="copyable">public inline fun <T> T.apply(block: T.() -> Unit): T &#123;
    contract &#123;
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    &#125;
    block()
    return this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>T.apply()</code>源码中在结合前面提到的<code>T.run()</code>函数的源码我们可以得出,这两个函数的逻辑差不多，唯一的区别是<code>T,apply</code>执行完了<code>block()</code>函数后，返回了自身对象。而<code>T.run</code>是返回了执行的结果。</p>
<p>故而： <code>T.apply</code>的作用除了实现能实现<code>T.run</code>函数的作用外，还可以后续的再对此操作。下面我们看一个例子：</p>
<p>例：为<code>TextView</code>设置属性后，再设置点击事件等</p>
<pre><code class="copyable">val mTvBtn = findViewById<TextView>(R.id.text)
mTvBtn.apply&#123;
    text = "kotlin"
    textSize = 13f
    ...
&#125;.apply&#123;
    // 这里可以继续去设置属性或一些TextView的其他一些操作
&#125;.apply&#123;
    setOnClickListener&#123; .... &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者：设置为<code>Fragment</code>设置数据传递</p>
<h2 data-id="heading-12">4.5 T.also()函数</h2>
<p>关于<code>T.also</code>函数来说，它和<code>T.apply</code>很相似，。我们先看看其源码的实现：</p>
<pre><code class="copyable">public inline fun <T> T.also(block: (T) -> Unit): T &#123;
    contract &#123;
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    &#125;
    block(this)
    return this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的源码在结合<code>T.apply</code>函数的源码我们可以看出： <code>T.also</code>函数中的参数<code>block</code>函数传入了自身对象。故而这个函数的作用是用用<code>block</code>函数调用自身对象，最后在返回自身对象</p>
<p>这里举例一个简单的例子，并用实例说明其和<code>T.apply</code>的区别</p>
<p>例：</p>
<pre><code class="copyable">"kotlin".also &#123;
    println("结果：$&#123;it.plus("-java")&#125;")
&#125;.also &#123;
    println("结果：$&#123;it.plus("-php")&#125;")
&#125;
​
"kotlin".apply &#123;
    println("结果：$&#123;this.plus("-java")&#125;")
&#125;.apply &#123;
    println("结果：$&#123;this.plus("-php")&#125;")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他们的输出结果是相同的：</p>
<pre><code class="copyable">结果：kotlin-java
结果：kotlin-php
​
结果：kotlin-java
结果：kotlin-php
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的实例我们可以看出，他们的区别在于，<code>T.also</code>中只能使用<code>it</code>调用自身,而<code>T.apply</code>中只能使用<code>this</code>调用自身。因为在源码中<code>T.also</code>是执行<code>block(this)</code>后在返回自身。而<code>T.apply</code>是执行<code>block()</code>后在返回自身。这就是为什么在一些函数中可以使用<code>it</code>,而一些函数中只能使用<code>this</code>的关键所在</p>
<h2 data-id="heading-13">4.6 let函数</h2>
<p>在前面讲解<code>空安全、可空属性</code>章节中，我们讲解到可以使用<code>T.let()</code>函数来规避空指针的问题。</p>
<p>故而今天来说一下他的源码实现：</p>
<pre><code class="copyable">public inline fun <T, R> T.let(block: (T) -> R): R &#123;
    contract &#123;
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    &#125;
    return block(this)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">let函数是参数化类型T的扩展函数，在let块内可以通过it来访问，返回值为let块的最后一行，或者指定return表达式。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let的作用主要在于3点：</p>
<ul>
<li>对当前的作用域的最后一行或者retuan语句负责</li>
<li>空安全检测</li>
<li>对链式的结果进行操作</li>
</ul>
<p>从上面的源码中我们可以得出，它其实和<code>T.also</code>以及<code>T.apply</code>都很相似。而<code>T.let</code>的作用也不仅仅在使用<code>空安全</code>这一个点上。用<code>T.let</code>也可实现其他操作</p>
<p>例：</p>
<pre><code class="copyable">"kotlin".let &#123;
    println("原字符串：$it")         // kotlin
    it.reversed()
&#125;.let &#123;
    println("反转字符串后的值：$it")     // niltok
    it.plus("-java")
&#125;.let &#123;
    println("新的字符串：$it")          // niltok-java
&#125;
​
"kotlin".also &#123;
    println("原字符串：$it")     // kotlin
    it.reversed()
&#125;.also &#123;
    println("反转字符串后的值：$it")     // kotlin
    it.plus("-java")
&#125;.also &#123;
    println("新的字符串：$it")        // kotlin
&#125;
​
"kotlin".apply &#123;
    println("原字符串：$this")     // kotlin
    this.reversed()
&#125;.apply &#123;
    println("反转字符串后的值：$this")     // kotlin
    this.plus("-java")
&#125;.apply &#123;
    println("新的字符串：$this")        // kotlin
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果看是否和注释的结果一样呢：</p>
<pre><code class="copyable">原字符串：kotlin
反转字符串后的值：niltok
新的字符串：niltok-java
​
原字符串：kotlin
反转字符串后的值：kotlin
新的字符串：kotlin
​
原字符串：kotlin
反转字符串后的值：kotlin
新的字符串：kotlin
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">4.7 repeat()函数</h2>
<p>首先，我们从这个函数名就可以看出是关于<code>重复</code>相关的一个函数，再看起源码，从源码的实现来说明这个函数的作用：</p>
<pre><code class="copyable">public inline fun repeat(times: Int, action: (Int) -> Unit) &#123;
    contract &#123; callsInPlace(action) &#125;
​
    for (index in 0..times - 1) &#123;
        action(index)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码我们可以看出这个函数的作用是：</p>
<blockquote>
<p>根据传入的重复次数去重复执行一个我们想要的动作(函数)</p>
</blockquote>
<p>例：</p>
<pre><code class="copyable">repeat(5)&#123;
    println("我是重复的第$&#123;it + 1&#125;次，我的索引为：$it")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="copyable">我是重复的第1次，我的索引为：0
我是重复的第2次，我的索引为：1
我是重复的第3次，我的索引为：2
我是重复的第4次，我的索引为：3
我是重复的第5次，我的索引为：4
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            