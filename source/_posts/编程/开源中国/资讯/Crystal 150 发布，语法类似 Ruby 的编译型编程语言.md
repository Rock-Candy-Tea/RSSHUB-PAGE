
---
title: 'Crystal 1.5.0 发布，语法类似 Ruby 的编译型编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1947'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1947'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Crystal 是一种通用的、面向对象的编程语言，由 Ary Borenszweig、Juan Wajnerman、Brian Cardiff 和 300 多名贡献者设计开发。Crystal 的语法受到 Ruby 的启发，属于编译语言，具有静态类型检查功能，但一般不需要指定变量或方法参数的类型，可实现接近 C/C++ 的性能。它的类型由一个先进的全局类型推理算法来解决。</span></p> 
<p> Crystal 1.5.0 已发布，此版本包含了自 1.4.1 版本以来由 23 位贡献者所做<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpulls%3Fq%3Dis%253Apr%2Bmilestone%253A1.5.0" target="_blank">的 102 项更改。</a>主要内容如下：</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>实现抽象的方法的参数<code class="language-crystal"><span>DEF</span></code>必须与名称匹配</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p>为了提供更好的文档和健壮性，可以将参数与其名称（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2Freference%2F1.5%2Fsyntax_and_semantics%2Fdefault_and_named_arguments.html%23named-arguments" target="_blank">ref</a>）显式关联：</p> 
<pre><code>class Foo
  def foo(name : Int32) : Nil
    p name
  end
end

Foo.new.foo name: 42</code></pre> 
<p>因此，考虑参数的名称是其接口的一部分是必须的。然而，在 1.5.0 之前，编译器不会检查抽象方法的实现与其定义之间的参数名称是否匹配。也就是说，以下示例编译时没有错误或警告：</p> 
<pre><code>abstract class FooAbstract
  abstract def foo(number : Int32) : Nil
end

class Foo < FooAbstract
  def foo(name : Int32) : Nil
    p name
  end
end</code></pre> 
<p>从 1.5.0 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11915" target="_blank">#11915</a> ) 开始，上面的示例将引发警告：</p> 
<pre><code> 6 | def foo(name : Int32) : Nil
             ^---
Warning: positional parameter 'name' corresponds to parameter 'number' of the overridden method FooAbstract#foo(number : Int32), which has a different name and may affect named argument passing</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>实例变量的方法限制</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p> </p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>当一个实例变量被赋值为一个无类型方法参数的值时，该参数被限制为与实例变量共享相同的类型。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>例如以下代码：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>class Foo
  @x : Int64

  def initialize(x)
    @x = x
  end
end</code></pre> 
<p>直到 1.4.1，<code class="language-crystal"><span>x</span></code>in<code class="language-crystal"><span>initialize</span></code>都不受限制，但这会导致几个问题：</p> 
<ul> 
 <li>如果用户传递了一个不正确的参数，例如 Foo.new 'a'，而不是在参数 'a' 中标记错误，它会指责 x 没有正确的类型。</li> 
 <li>例如，如果我们改为传递 Int32，则不会执行自动转换： Foo.new 1 失败。</li> 
 <li>生成的文档没有提供参数 x 类型的提示。</li> 
</ul> 
<p>从 1.5.0 开始，在像 @x = x 这样的赋值中，参数 x 获取了 @x 的类型，有效地解决了上述三个问题。可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F12103" target="_blank">#12103</a> 中阅读详细信息。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>方法参数上允许的注释</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p>现在可以为方法或宏的参数添加注释。作为说明，假设一个 linter 会在未使用参数时发出警告。</p> 
<pre><code>def foo(x); end  # Warning: argument `x` is not used</code></pre> 
<p>然后我们可以向 linter 发出信号，在特定情况下不要警告我们。假设 linter 提供以下注解：</p> 
<pre><code>annotation MaybeUnused; end</code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>将其应用于参数会删除警告（在这个特定的虚构 linter 中）：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div> 
  <pre><code>def foo(@[MaybeUnused] x); end  # OK</code></pre> 
 </div> 
</div> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fissues%2F12039" target="_blank">#12039</a> 中了解详细信息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>元组的常量索引器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p>当使用常量索引元组或命名元组时，类型检查器将正确推断所访问值的精确类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F12012" target="_blank">#12012</a>）。</p> 
<pre><code>KEY = "s"
foo = &#123;s: "String", n: 0&#125;

# Before 1.5.0 this failed; it would assume the type of foo[key] to be (String | Int32)
puts foo[KEY].size</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>加强 <code class="language-crystal"><span>FILE</span><span>.</span><span>TEMPFILE</span></code>安全保障</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>根据  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F12076" target="_blank">#12076</a>，临时文件的创建不允许在文件名的字符串中使用空字符。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>NO_COLOR 合规性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>编译器和解释器支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fno-color.org%2F" target="_blank">NO_COLOR</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2Freference%2F1.5%2Fusing_the_compiler%2Findex.html%23environment-variables" target="_blank">环境变量</a>来禁用终端上的彩色输出。可以通过将任何非空值设置为<code class="language-crystal"><span>NO_COLOR</span></code>来启用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11984" target="_blank">#11984</a> 中可查看详细信息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>向原生 WINDOWS 支持迈出一大步</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Windows 上的并发运行时由功能正常的事件循环 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F12149" target="_blank">#12149</a> ) 支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fissues%2F5430" target="_blank">这跨越了通往原生 Windows 支持</a>的道路上的一项重要检查。此外，现在有一个与 Windows 兼容的<code class="language-crystal"><span>Makefile</span></code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11773" target="_blank">#11773</a> )。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他内容可以在</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>更新公告中查阅：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2F2022%2F07%2F06%2F1.5.0-released.html" target="_blank">https://crystal-lang.org/2022/07/06/1.5.0-released.html</a> 。</p>
                                        </div>
                                      
</div>
            