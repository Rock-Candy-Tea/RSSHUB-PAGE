
---
title: '木兰 0.0.17.3 支持不需 __init__ 的 super 调用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-350141ac6f575e6fe744200d39dd7ab152e.png'
author: 开源中国
comments: false
date: Fri, 07 May 2021 15:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-350141ac6f575e6fe744200d39dd7ab152e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>接续 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F369268306" target="_blank">前文</a>，试着调整了几次优先级排序，除了 <code>super</code> 需在 <code>(</code> 之下以外，没看出其他门道，于是暂时将两者分别放在优先级排序最高与最低，现在所有测试用例能通过，以观后效吧。个人感觉由于优先级与语法规则的勾连，想要生成一个针对某一优先级设置的测试用例颇为烧脑，先搁置吧。</p> 
<p>接着，既然做到了 super 语法，就在语法树生成木兰源码部分功能中复现了 super。先上 Python 与转换出的木兰源码对比：</p> 
<p><img alt height="531" src="https://oscimg.oschina.net/oscnet/up-350141ac6f575e6fe744200d39dd7ab152e.png" width="549" referrerpolicy="no-referrer"></p> 
<p>可见，在调用父类的构造方法时，相较 Python 需要 <code>__init__()</code>，木兰中可以略去，参数直接传给 super，与 Java 等其他常用语言类似。</p> 
<p>复现了这一转换功能后，发现还需复现对此语法的支持，是通过 NameFixPass 这一语法树修改步骤的 visit_Call 实现。</p> 
<p>完成后，前文的 <code>super(演示, self).__init__()</code>，现在只需 <code>super()</code>。0.0.17.3 发布在 PyPI（pip install ulang 安装）</p> 
<p>回头看对比图，个人猜度，木兰的这个设计与 self 可用 $ 代替、<strong><code>__init()__</code></strong> 可用类名代替等一道，都是为了方便开发者进行类型相关操作并让代码更可读。</p> 
<hr> 
<h3><em><strong>附：代码量统计</strong></em></h3> 
<p>主要部分的代码行数统计，格式为：上次->现在。</p> 
<ul> 
 <li>木兰代码量 3050 -> 3096 
  <ul> 
   <li>运行环境，实现与测试大部为木兰代码：582</li> 
   <li>木兰测试用例，包括部分实用小程序（如井字棋）：2468 -> 2514</li> 
  </ul> </li> 
 <li>Python 代码量（木兰实现、测试框架、语法树生成木兰中的 Python 测试代码）：3381 -> 3436 
  <ul> 
   <li><code>分析器/语法分析器.py</code>：1049 -> 1055</li> 
   <li><code>生成/木兰.py</code>：206 -> 213</li> 
   <li><code>分析器/语法树处理.py</code>：91 -> 114</li> 
   <li>未变 
    <ul> 
     <li><code>分析器/语法树.py</code>：225</li> 
     <li><code>分析器/词法分析器.py</code>：216</li> 
     <li><code>功用/反馈信息.py</code>：175</li> 
     <li><code>环境.py</code>，定义全局方法： 175</li> 
     <li><code>交互.py</code>，交互环境（REPL）：148</li> 
     <li><code>测试/期望值表.py</code>：144</li> 
     <li><code>测试/unittest/报错.py</code>：124</li> 
     <li><code>中.py</code>，主程序：95</li> 
     <li><code>分析器/语法成分.py</code>，从语法分析器中提取出来的枚举常量：85</li> 
     <li><code>测试/运行所有.py</code>，检验所有木兰测试代码片段：71</li> 
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
            