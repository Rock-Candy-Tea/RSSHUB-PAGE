
---
title: '草蟒（Python 中文版）3.10 公测版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2241'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 19:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2241'
---

<div>   
<div class="content">
                                                                                            <p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grasspy.cn" target="_blank"><span>草蟒（Python中文版）3.10公测版</span></a></span><span>已于近日上线，</span><span><a href="https://gitee.com/laowu2019_admin/cpython"><span>源代码库</span></a></span><span>也已在码云公开，欢迎大家试用并反馈，待收集到一定数量的反馈并做适当修改和补充后就会推出正式版。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>关注草蟒的朋友们可能知道之前有一个草蟒3.8.0，此版本可以说是编程语言中文化的试水之作，已经停止更新。草蟒3.10吸取了前作的经验教训，解决了一些基本汉化问题，是两年来的探索努力和社区支持的成果，笔者打算提供长期维护和更新。</span></p> 
<pre style="margin-left:.8rem; margin-right:.8rem; text-align:left"><span><span style="color:#000000">套路</span> <span style="color:#000000">问候</span>(<span style="color:#000000">谁</span>):</span>
<span>    <span style="color:#000000">打印</span>(<span style="color:#000000">谁</span>, <span style="color:#22a2c9">'你吃了吗？'</span>)</span>
<span>    </span>
<span><span style="color:#000000">问候</span>(<span style="color:#22a2c9">'小美'</span>)    <span style="color:#aa5500"># 结果：小美 你吃了吗？</span></span></pre> 
<pre style="margin-left:.8rem; margin-right:.8rem; text-align:left"><span>>>> 导入 日时</span>
<span>>>> 日时.〇日期.今日().转字符串()</span>
<span>'周一 2022 年 3 月 21 日 00:00:00'</span></pre> 
<pre style="margin-left:.8rem; margin-right:.8rem; text-align:left"><span><span style="color:#aa5500"># 画一个五角星</span></span>
<span><span>​</span></span>
<span><span style="color:#000000">从</span> <span style="color:#000000">海龟</span> <span style="color:#000000">导入</span> <span style="color:#981a1a">*</span></span>
<span><span>​</span></span>
<span><span style="color:#000000">颜色</span>(<span style="color:#22a2c9">'黄色'</span>, <span style="color:#22a2c9">'红色'</span>)</span>
<span><span>​</span></span>
<span><span style="color:#000000">开始填充</span>()</span>
<span><span style="color:#000000">取</span> <span style="color:#000000">i</span> <span style="color:#000000">于</span> <span style="color:#000000">范围</span>(<span style="color:#116644">5</span>): </span>
<span>    <span style="color:#000000">前进</span>(<span style="color:#116644">200</span>)</span>
<span>    <span style="color:#000000">右转</span>(<span style="color:#116644">144</span>)</span>
<span><span style="color:#000000">结束填充</span>()</span>
<span><span>​</span></span>
<span><span style="color:#000000">完成</span>()</span>
</pre> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>关键字汉化简单说明</span></h3> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>相比于之前的版本，Python 3.10 的关键字汉化要更简单。Python 官网提供了一个关于如何更改语法的</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevguide.python.org%2Fgrammar%2F" target="_blank"><span>检查清单</span></a></span><span>。我们只需增加中文关键字，因此实际上只涉及一个关键步骤，如下所示（假设使用Windows 10平台，具体修改请参见源代码）：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修改 </span><span><code>Grammar/python.gram</code></span><span>和</span><span><code>Tools/peg_generator/pegen/c_generator.py</code></span><span>，然后在cmd中运行 </span><span><code>build.bat --regen</code></span><span>，以重新生成</span><span><code>Parser/parser.c</code></span><span>。</span></p> </li> 
</ul> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>Lib/keyword.py 的重新生成可以在编译前或编译后进行，只需修改 </span><span><code>Tools/peg_generator/pegen/keywordgen.py</code></span><span>，具体生成命令请参见 keyword.py 文件最开始的说明。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>特殊汉字符号（〇、々、匚、爻）说明</span></h3> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>英语编程语言中通常利用字母的大小写来区分不同类型的标识符，另外还通过加后缀（例如 s）来区分名词性概念的单复数（即区分个体与集合）。作为一门翻译过来的编程语言，草蟒借用了四个汉字来从形式和视觉上表现上述现象。</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>〇</span></strong></span><span>：类名以 </span><span><code>〇</code></span><span> 开头，对应英语中类名以大写字母开头；建议读作 ou。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>爻</span></strong></span><span>：异常（包括警告）名以 </span><span><code>爻</code></span><span>（视为两个 ×）开头，建议读作 cha。各种异常也是类，但如果同样以 〇 开头，那么在编辑器中输入全局类名的第一个字 〇 时，将跳出大量异常类（有 60 多个），非常影响编程体验，故对异常命名另作规定。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>匚</span></strong></span><span>：全局常量名以 </span><span><code>匚</code></span><span>开头，对应英语中的全大写常量名；建议读作 chang。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>々</span></strong></span><span>：在需要区分个体与集合的情况下，在个体名词后加 </span><span><code>々</code></span><span> 表示集合对象（例如列表、字典等），对应英语中的后缀 s；建议读作 es。</span></p> </li> 
</ul> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>使用这些汉字符号之后，标识符的汉化更加简便，不仅能顺利地继承原语言的优势，而且以极小的代价丰富了中文编程语言的语汇。为了支持这些汉字符号的输入，我们需要对输入法进行自定义设置。另外，以上规定皆为一般原则，某些情况下不排除变通处理。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>以上规则不仅适用于python的汉化，也能很自然地应用于其他编程语言的汉化，示例参见笔者对go语言导出标识符的处理（</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F467399939" target="_blank"><span>如何汉化go语言</span></a></span><span>）。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>中文编程语言发展之路</span></h3> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>何谓中文编程？笔者认为，主要使用中文（包括中文关键字或保留字）开发计算机程序就是中文编程。相应地，中文编程语言就是支持主要使用中文进行程序开发的计算机编程语言。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>近年来，关于中文编程的讨论和实践很是热闹，B站和头条上不时能看到新推出的中文编程语言或环境。由此可见，民间对中文编程语言的呼声很高。然而，令人失望的是，大厂和学界对此需求直接无视。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>要发展中文编程语言，主要有两条路：自研和汉化。自研语言的门槛非常高，需要非凡的能力、精力和/或财力，就算大厂也很难确保成功，普通人更不必考虑。汉化则不然，无论程序员还是编程爱好者，只要懂一点英语就能参与。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>在等候自研中文编程语言佳音的同时，有志之士不妨投入汉化事业？</span></p>
                                        </div>
                                      
</div>
            