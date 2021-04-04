
---
title: '木兰语言 0.0.17：着手由 Python 语法树生成木兰源码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2674bdb20a67516e4a8229610c0ec422169.png'
author: 开源中国
comments: false
date: Sun, 04 Apr 2021 10:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2674bdb20a67516e4a8229610c0ec422169.png'
---

<div>   
<div class="content">
                                                                                            <p>刚开始实现从 Python 源码转为木兰源码，现在支持无参数函数定义以及函数调用等，刚在 pypi 发布了 ulang 0.0.17 版本包含此功能。</p> 
<p>下面左侧为 Python 代码，运行 <code>$ 木兰 -兰 XX.py</code> 后生成右侧的对应木兰代码：</p> 
<p><img alt height="96" src="https://oscimg.oschina.net/oscnet/up-2674bdb20a67516e4a8229610c0ec422169.png" width="352" referrerpolicy="no-referrer"></p> 
<p>实现机制是扩展 Python ast 库的 NodeVisitor，对每个相关语法节点编写相关生成规则。以函数定义部分为例，可见 <code>主体</code> 将函数体内声明分行显示并以大括号包围：</p> 
<div> 
 <pre><code class="language-python3">    def visit_FunctionDef(self, 节点):
        self.另起一行(额外=1)
        self.另起一行(节点)
        self.编写('func ')
        self.编写('%s(' % 节点.name)
        self.编写(')')
        self.主体(节点.body)

    def 主体(self, 所有声明):
        self.编写(' &#123;')
        for 声明 in 所有声明:
            self.visit(声明)

        self.另起一行()
        self.编写('&#125;')</code></pre> 
</div> 
<p>函数定义部分（visit_FunctionDef）现在看起来很简单，是因为仅仅复现了无参数函数定义，之后还需添加带参数、应变属性（attr）等等的支持，此部分将会逐渐复杂。主体部分也还需添加相应缩进。</p> 
<p>通过复现这部分由语法树生成木兰源码的功能，从另一方面检验了之前重现的木兰语法。以标识符名称为例：</p> 
<div> 
 <pre><code class="language-python3">    def visit_Name(self, 节点):
        if 节点.id == 'print':
            self.编写('println')
        elif 节点.id == 'chr':
            self.编写('char')
        else:
            self.编写(节点.id)</code></pre> 
</div> 
<p>可见内置函数除了 Python 的 print 和 chr 之外，都沿用了 Python 的名称，这与至今重现的内置函数部分一致。</p> 
<p>与之前复现木兰语法时类似，针对每条语法生成规则编写了对应测试。在功能覆盖上，与之前积累的测试用例有相当交集，今后考虑将木兰测试用例在两部分复用。比如，从 Python 源码开始：</p> 
<div> 
 <pre><code class="language-python3">def echo(number):
    print(number)
echo(2)</code></pre> 
</div> 
<p>转换后检查是否生成了如下目标木兰源码：</p> 
<div> 
 <pre><code class="language-java">func echo(number) &#123;
    println(number)
&#125;
echo(2)</code></pre> 
</div> 
<p>另一面，解析执行上述木兰源码检查结果是否为 2。</p> 
<p>简而言之，对木兰语言的认识对这部分功能的复现有很大帮助，过程比想象中的顺利。当然之后应该会碰到尚未复现的语法功能，且行且看吧。</p>
                                        </div>
                                      
</div>
            