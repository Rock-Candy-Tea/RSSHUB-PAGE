
---
title: 'Python 中有什么不容易让人察觉的有趣的事实_'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic1.zhimg.com/v2-3aff6dbd998567e60686173ce84e8a0b_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-04-04 04:11:33
thumbnail: 'https://pic1.zhimg.com/v2-3aff6dbd998567e60686173ce84e8a0b_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic1.zhimg.com/v2-3aff6dbd998567e60686173ce84e8a0b_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">Jackpop，</span><span class="bio">vx：code_7steps | 公众号：平凡而诗意</span>
<a href="https://www.zhihu.com/question/517057824/answer/2402176823" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>提起 Python，绝大多数同学第一印象就是”简单“。</p>
<p>但是，Python 中也有很多有趣、微妙的事情，如果不用心去了解，很容易在开发过程中陷入误区，久久无法自拔。</p>
<p>下面，就介绍几个 Python 中有趣的事情。</p>
<p><strong><strong>1. 微妙的字符串</strong></strong></p>
<div class="highlight">
<pre><code class="language-text">>>> a = "wtf"
>>> b = "wtf"
>>> a is b
True
​
>>> a = "wtf!"
>>> b = "wtf!"
>>> a is b
False
​
>>> a, b = "wtf!", "wtf!"
>>> a is b 
True
</code></pre>
</div>
<p>是不是觉得很神奇？</p>
<p>为什么加上</p>
<p><code>!</code></p>
<p>返回就是</p>
<p><code>False</code></p>
<p>，不加则返回</p>
<p><code>True</code></p>
<p>？</p>
<p>为什么加上</p>
<p><code>!</code></p>
<p>并放置同一行时，又返回</p>
<p><code>True</code></p>
<p>了？</p>
<ul>
<li>这些行为是由于 Cpython 在编译优化时, 某些情况下会尝试使用已经存在的不可变对象而不是每次都创建一个新对象. (这种行为被称作字符串的驻留[string interning])</li>
<li>发生驻留之后, 许多变量可能指向内存中的相同字符串对象. (从而节省内存)</li>
<li>在上面的代码中, 字符串是隐式驻留的. 何时发生隐式驻留则取决于具体的实现. 这里有一些方法可以用来猜测字符串是否会被驻留:</li>
<ul>
<li>所有长度为 0 和长度为 1 的字符串都被驻留.</li>
<li>字符串在编译时被实现 (<code>'wtf'</code> 将被驻留, 但是 <code>''.join(['w', 't', 'f'])</code> 将不会被驻留)</li>
<li>字符串中只包含字母，数字或下划线时将会驻留. 所以 <code>'wtf!'</code> 由于包含 <code>!</code> 而未被驻留.</li>
</ul>
<li>当在同一行将 <code>a</code> 和 <code>b</code> 的值设置为 <code>"wtf!"</code> 的时候, Python 解释器会创建一个新对象, 然后同时引用第二个变量。如果你在不同的行上进行赋值操作, 它就不会“知道”已经有一个 <code>wtf！</code> 对象 (因为 <code>"wtf!"</code> 不是按照上面提到的方式被隐式驻留的). 它是一种编译器优化, 特别适用于交互式环境.</li>
</ul>
<p><strong><strong>2. <code>is</code>和<code>==</code>的区别</strong></strong></p>
<div class="highlight">
<pre><code class="language-text">>>> a = 256
>>> b = 256
>>> a is b
True
​
>>> a = 257
>>> b = 257
>>> a is b
False
​
>>> a = 257; b = 257
>>> a is b
True
</code></pre>
</div>
<ul>
<li><code>is</code> 运算符检查两个运算对象是否引用自同一对象 (即, 它检查两个运算对象是否相同).</li>
<li><code>==</code> 运算符比较两个运算对象的值是否相等.</li>
<li>因此<code>is</code>代表引用相同,<code>==</code>代表值相等. 下面的例子可以很好的说明这点</li>
</ul>
<div class="highlight">
<pre><code class="language-ps1con"><span class="go">>>> [] == []</span>
<span class="go">True</span>
<span class="go">>>> [] is [] # 这两个空列表位于不同的内存地址.</span>
<span class="go">False</span>
</code></pre>
</div>
<p><strong><code>256</code> 是一个已经存在的对象, 而 <code>257</code> 不是</strong></p>
<p>当你启动 Python 的时候, 数值为</p>
<p><code>-5</code></p>
<p>到</p>
<p><code>256</code></p>
<p>的对象就已经被分配好了. 这些数字因为经常被使用, 所以会被提前准备好.</p>
<p>Python 通过这种创建小整数池的方式来避免小整数频繁的申请和销毁内存空间.</p>
<p><strong><strong>3. <code>is not ...</code> 不是 <code>is (not ...)</code></strong></strong></p>
<div class="highlight">
<pre><code class="language-text">>>> 'something' is not None
True
>>> 'something' is (not None)
False
</code></pre>
</div>
<ul>
<li><code>is not</code> 是个单独的二元运算符, 与分别使用 <code>is</code> 和 <code>not</code> 不同.</li>
<li>如果操作符两侧的变量指向同一个对象, 则 <code>is not</code> 的结果为 <code>False</code>, 否则结果为 <code>True</code>.</li>
</ul>
<p><strong><strong>4. 逗号</strong></strong></p>
<div class="highlight">
<pre><code class="language-text">>>> def f(x, y,):
...     print(x, y)
...
>>> def g(x=4, y=5,):
...     print(x, y)
...
>>> def h(x, **kwargs,):
  File "", line 1
    def h(x, **kwargs,):
                     ^
SyntaxError: invalid syntax
>>> def h(*args,):
  File "", line 1
    def h(*args,):
                ^
SyntaxError: invalid syntax
</code></pre>
</div>
<ul>
<li>在 Python 函数的形式参数列表中, 尾随逗号并不一定是合法的.</li>
<li>在 Python 中, 参数列表部分用前置逗号定义, 部分用尾随逗号定义. 这种冲突导致逗号被夹在中间, 没有规则定义它.(译:这一句看得我也很懵逼,只能强翻了.详细解释看下面的讨论帖会一目了然.)</li>
</ul>
<p><strong><strong>5. 真亦假</strong></strong></p>
<div class="highlight">
<pre><code class="language-text">True = False
if True == False:
    print("I've lost faith in truth!")
</code></pre>
</div>
<p>输出：</p>
<div class="highlight">
<pre><code class="language-text">I've lost faith in truth!
</code></pre>
</div>
<ul>
<li>最初, Python 并没有 <code>bool</code> 型 (人们用 0 表示假值, 用非零值比如 1 作为真值). 后来他们添加了 <code>True</code>, <code>False</code>, 和 <code>bool</code> 型, 但是, 为了向后兼容, 他们没法把 <code>True</code> 和 <code>False</code> 设置为常量, 只是设置成了内置变量.</li>
<li>Python 3 由于不再需要向后兼容, 终于可以修复这个问题了, 所以这个例子无法在 Python 3.x 中执行!</li>
</ul>
<p>这里只是举了几个例子，上面的例子是从 Github 上一个非常火热的开源项目<a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//github.com/satwikkansal/wtfpython%23-strings-can-be-tricky-sometimes" target="_blank" rel="nofollow noreferrer">wtfpython</a>节选的，目前该项目已经有 2.8 万 +star，受欢迎程度可见一斑。除了英文版，它还有<a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//github.com/leisurelicht/wtfpython-cn" target="_blank" rel="nofollow noreferrer">中文版</a>。</p>
<p>它收集了 Python 中各种各样奇怪且有趣的事情，感兴趣的同学可以花时间多了解一下。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/517057824">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            