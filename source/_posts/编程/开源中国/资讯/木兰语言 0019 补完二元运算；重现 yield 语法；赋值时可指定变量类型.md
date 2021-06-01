
---
title: '木兰语言 0.0.19 补完二元运算；重现 yield 语法；赋值时可指定变量类型'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3b5c535133e780be2ad37633d1e8f1f48ac.png'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 11:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3b5c535133e780be2ad37633d1e8f1f48ac.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>这两周过的飞快，先上木兰代码截图，省得像上次似的一堆误会。</p> 
<p><img alt height="199" src="https://oscimg.oschina.net/oscnet/up-3b5c535133e780be2ad37633d1e8f1f48ac.png" width="253" referrerpolicy="no-referrer"></p> 
<p>这是完成了的第二批悬赏任务之一的成果：</p> 
<ul> 
 <li>￥188 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3SNP3%253Ffrom%253Dproject-issue" target="_blank">【进阶】重现所有 yield 相关语法</a></li> 
 <li>￥128 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3RQ0C%253Ffrom%253Dproject-issue" target="_blank">重现语法——赋值时指定变量类型</a></li> 
 <li>￥100 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3RQ0A%253Ffrom%253Dproject-issue" target="_blank">补完二元表达式（bin_expr）的四个运算符</a></li> 
</ul> 
<p>下面主要记下合作期间的一些发现。</p> 
<p>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fpulls%2F19" target="_blank">实现二元运算符时</a> ，发现与 Python 中的优先级有不同，需更全面评估。如位左移 << ，木兰中的优先级低于 < 而 python 相反。1<2<<3 在木兰中为 8 而 Python 为 True。</p> 
<p>另外发现，之前在实现语法树生成木兰源码时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F372021884" target="_blank">误以为木兰不支持链式运算</a> ，但现在发现是支持的：</p> 
<div> 
 <pre><code class="language-text">> 1<2<3
true
> 1<2<0
false</code></pre> 
</div> 
<p>此任务中，合作者还对代码作了格式化。</p> 
<p>重现 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fpulls%2F21" target="_blank">yield 语法时</a> ，在推敲标识符命名中发现至今重现的木兰语法规则的一个规律：表达式可以是声明的一部分，而声明不会是表达式的一部分。不知这规律是否常见。</p> 
<p>另外，向合作者学习了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3TC3H%253Ffrom%253Dproject-issue" target="_blank">yield 更多功能</a> 。</p> 
<p>重现 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fpulls%2F23" target="_blank">赋值时指定变量类型时</a> ，更有意外发现。<code>a:str</code> 可以在交互环境下运行，但不能在源码中运行，后发现是交互环境中为了支持不用 print 就输出表达式的值而导致的副效应。</p> 
<p>之后，在因上面而加的语法规则的设计意图尚不明确的情况下，我出了个馊用例：</p> 
<div> 
 <pre><code class="language-text">a=10
b=(a:int)
print(b)</code></pre> 
</div> 
<p>随后发现 <code>(a:int)</code> 这一语法与 lambda 表达式有关（在早先任务列表中被列在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI1SEU5%253Ffrom%253Dproject-issue" target="_blank">功能不确定</a> 部分 ），于是商议决定将此部分内容回退后另开任务解决，以免此任务滚雪球式扩大。</p> 
<p>随着合作者对项目越来越熟悉，非常期待今后的技术交流和探讨。</p> 
<p>在项目维护方面，修复了跨平台路径导致的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3RNBQ%253Ffrom%253Dproject-issue" target="_blank">windows 下测试问题</a> ，同时修复了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fcommit%2Fe26477ba527c300f5f5fe339263ed323d27e5606" target="_blank">Docstring 生成木兰源码</a> 的用例。 并在解决 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3SBUA%253Ffrom%253Dproject-issue" target="_blank">流水线测试问题</a> 时发现了一个 rply 木兰定制版在 PyPI 发布缺失 whl 文件（库安装时会在 linux 下构建不过）的问题。</p> 
<hr> 
<h3><strong><em>附：代码量统计</em></strong></h3> 
<p>主要部分的代码行数统计，格式为：上次->现在。</p> 
<ul> 
 <li>木兰代码量 3157 -> 3201 
  <ul> 
   <li>运行环境，实现与测试大部为木兰代码：582</li> 
   <li>木兰测试用例，包括部分实用小程序（如井字棋）：2575 -> 2619</li> 
  </ul> </li> 
</ul> 
<p> </p> 
<ul> 
 <li>Python 代码量（木兰实现、测试框架、语法树生成木兰中的 Python 测试代码）：3612 -> 3794 
  <ul> 
   <li><code>分析器/语法分析器.py</code> 此次格式化代码有额外添加行数：1055 -> 1144</li> 
   <li><code>分析器/语法树.py</code>：225 -> 267</li> 
   <li><code>生成/木兰.py</code>：239 -> 242</li> 
   <li><code>分析器/词法分析器.py</code>：216 -> 231</li> 
   <li><code>测试/期望值表.py</code>：173 -> 177</li> 
   <li><code>交互.py</code>，交互环境（REPL）：150 -> 149</li> 
   <li><code>测试/unittest/报错.py</code>：124 -> 126</li> 
   <li><code>分析器/语法树处理.py</code>：114 -> 119</li> 
   <li><code>分析器/语法成分.py</code>，从语法分析器中提取出来的枚举常量：85 -> 88</li> 
   <li>未变 
    <ul> 
     <li><code>环境.py</code>，定义全局方法： 275</li> 
     <li><code>功用/反馈信息.py</code>：175</li> 
     <li><code>中.py</code>，主程序：95</li> 
     <li><code>测试/运行所有.py</code>，检验所有木兰测试代码片段：75</li> 
     <li><code>测试/unittest/生成.py</code>，语法树生成木兰源码相关测试：60</li> 
     <li><code>测试/unittest/语法树.py</code>，确保生成的语法树与原始版本一致，拆分报错部分：58</li> 
     <li><code>功用/调试辅助.py</code>，：57</li> 
     <li><code>setup.py</code>, 34</li> 
     <li><code>测试/unittest/交互.py</code>，交互环境相关测试：28</li> 
     <li><code>分析器/错误.py</code>：28</li> 
     <li><code>测试/unittest/所有用例.py</code>：24</li> 
    </ul> </li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            