
---
title: '「缺省」这个词是如何从英语 "Default" 翻译过来的？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=3355'
author: 知乎
comments: false
date: Sat, 03 Sep 2022 15:09:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=3355'
---

<div>   
Victor Yeh的回答<br><br><p data-pid="vdzXpOcJ">要知道以前电脑是面向程序员的，最少也是面向操作员的，不是面向门外汉的。所以用词准确性非常重要，好不好听不重要，是否容易理解不重要。</p><p data-pid="cfNQYJDa">用「默认」来翻译 default 很好理解，但是不准确。因为很多词都可以有类默认值的意思，比如  preset value 和 default value 等等。这些词汇对于外行来说，都是「默认值」，但是对于程序员来说，这两个词差异可大了。</p><p data-pid="VmaPmbz3">preset value 是「预设值」，其中 preset 的词源是 pre- (在……之前) + set (设置) ，即预先设置。 default value 字面意思是「消除错误的值」，其中 default 的词源是 de- (消除) + fault (错误) 。</p><p data-pid="byvyV5WD">有什么区别呢？ </p><p data-pid="c80OH9rt">如果预先设置一个值，就是 preset value （预设值），后面如果没人设置了，那么自然就「默认」以前预设的值了。这显然是「默认值」。</p><p data-pid="0MDvJGQq">另一种情况是这样：你没有预先设置一个值，而是直接让用户去填空，填上一个值。如果这个用户操作出错，导致没有填上这个值，或者用户填的值是错误的（比如让你输入数字你却输入字母），那么我这个程序就要主动地去消除这个错误，也就是填上这个 default value （消除错误的值）。这显然也算是「默认值」，但是这是事后弥补，而非事前预设，所以 <b><u>default value 是仅当「缺少」和「省略」的时候才使用的值，故名「缺省值」</u></b>。其实曾经我还见过「补缺值」「除错值」等译名。</p><p><br></p><p data-pid="eLVg_1ue">预设值（preset value）：</p><div class="highlight"><pre><code class="language-cpp"><span><span class="cp">#include</span> <span class="cpf"><iostream></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><string></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><algorithm></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><cstdlib></span><span class="cp">

<span class="k">using</span> <span class="k">namespace</span> <span class="n">std</span><span class="p">;</span>

<span class="kt">int</span> <span class="nf">main</span><span class="p">()</span>
<span class="p">&#123;</span>
<span class="kt">long</span> <span class="kt">int</span> <span class="n">number</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span> <span class="c1">// 预设值  preset value</span>
<span class="kt">bool</span> <span class="n">isNumber</span> <span class="o">=</span> <span class="nb">true</span><span class="p">;</span>
<span class="n">string</span> <span class="n">input</span><span class="p">;</span>
<span class="n">cin</span> <span class="o">>></span> <span class="n">input</span><span class="p">;</span>
<span class="n">for_each</span><span class="p">(</span><span class="n">input</span><span class="p">.</span><span class="n">begin</span><span class="p">(),</span> <span class="n">input</span><span class="p">.</span><span class="n">end</span><span class="p">(),</span> <span class="p">[</span><span class="o">&</span><span class="p">](</span><span class="kt">char</span> <span class="n">ch</span><span class="p">)&#123;</span> <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">isdigit</span><span class="p">(</span><span class="n">ch</span><span class="p">))</span> <span class="n">isNumber</span> <span class="o">=</span> <span class="nb">false</span><span class="p">;</span> <span class="p">&#125;);</span>
<span class="k">if</span> <span class="p">(</span><span class="n">isNumber</span><span class="p">)</span>
<span class="p">&#123;</span>
<span class="n">number</span> <span class="o">=</span> <span class="n">strtol</span><span class="p">(</span><span class="n">input</span><span class="p">.</span><span class="n">c_str</span><span class="p">(),</span> <span class="nb">NULL</span><span class="p">,</span> <span class="mi">10</span><span class="p">);</span>
<span class="p">&#125;</span>
<span class="n">cout</span> <span class="o"><<</span> <span class="n">number</span> <span class="o"><<</span> <span class="n">endl</span><span class="p">;</span>
<span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">&#125;</span>
</span></span></span></span></span></code></pre></div><p><br></p><p data-pid="Y7sExuUt">缺省值（default value）：</p><div class="highlight"><pre><code class="language-cpp"><span><span class="cp">#include</span> <span class="cpf"><iostream></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><string></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><algorithm></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><cstdlib></span><span class="cp">

<span class="k">using</span> <span class="k">namespace</span> <span class="n">std</span><span class="p">;</span>

<span class="kt">int</span> <span class="nf">main</span><span class="p">()</span>
<span class="p">&#123;</span>
<span class="kt">long</span> <span class="kt">int</span> <span class="n">number</span><span class="p">;</span>
<span class="kt">bool</span> <span class="n">isNumber</span> <span class="o">=</span> <span class="nb">true</span><span class="p">;</span>
<span class="n">string</span> <span class="n">input</span><span class="p">;</span>
<span class="n">cin</span> <span class="o">>></span> <span class="n">input</span><span class="p">;</span>
<span class="n">for_each</span><span class="p">(</span><span class="n">input</span><span class="p">.</span><span class="n">begin</span><span class="p">(),</span> <span class="n">input</span><span class="p">.</span><span class="n">end</span><span class="p">(),</span> <span class="p">[</span><span class="o">&</span><span class="p">](</span><span class="kt">char</span> <span class="n">ch</span><span class="p">)&#123;</span> <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">isdigit</span><span class="p">(</span><span class="n">ch</span><span class="p">))</span> <span class="n">isNumber</span> <span class="o">=</span> <span class="nb">false</span><span class="p">;</span> <span class="p">&#125;);</span>
<span class="k">if</span> <span class="p">(</span><span class="n">isNumber</span><span class="p">)</span>
<span class="p">&#123;</span>
<span class="n">number</span> <span class="o">=</span> <span class="n">strtol</span><span class="p">(</span><span class="n">input</span><span class="p">.</span><span class="n">c_str</span><span class="p">(),</span> <span class="nb">NULL</span><span class="p">,</span> <span class="mi">10</span><span class="p">);</span>
<span class="p">&#125;</span>
<span class="k">else</span>
<span class="p">&#123;</span>
<span class="n">number</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span> <span class="c1">// 缺省值 default value</span>
<span class="p">&#125;</span>
<span class="n">cout</span> <span class="o"><<</span> <span class="n">number</span> <span class="o"><<</span> <span class="n">endl</span><span class="p">;</span>
<span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">&#125;</span>
</span></span></span></span></span></code></pre></div><p><br></p><p data-pid="mwb2tBsC">预设值与缺省值：</p><div class="highlight"><pre><code class="language-cpp"><span><span class="kt">int</span> <span class="n">x</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span> <span class="c1">// 预设值 preset value</span>
<span class="k">if</span> <span class="p">(</span><span class="n">t</span> <span class="o"><</span> <span class="mi">3</span><span class="p">)</span>
<span class="p">&#123;</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">7</span><span class="p">;</span>
<span class="p">&#125;</span>
<span class="k">else</span> <span class="k">if</span> <span class="p">(</span><span class="n">t</span> <span class="o"><</span> <span class="mi">20</span><span class="p">)</span>
<span class="p">&#123;</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">8</span><span class="p">;</span>
<span class="p">&#125;</span>

<span class="kt">int</span> <span class="n">y</span><span class="p">;</span>
<span class="k">switch</span> <span class="p">(</span><span class="n">s</span><span class="p">)</span>
<span class="p">&#123;</span>
<span class="k">case</span> <span class="mi">1</span><span class="o">:</span>
<span class="n">y</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
<span class="k">break</span><span class="p">;</span>
<span class="k">case</span> <span class="mi">2</span><span class="o">:</span>
<span class="n">y</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span>
<span class="k">break</span><span class="p">;</span>
<span class="k">case</span> <span class="mi">3</span><span class="o">:</span>
<span class="n">y</span> <span class="o">=</span> <span class="mi">15</span><span class="p">;</span>
<span class="k">break</span><span class="p">;</span>
<span class="k">default</span><span class="o">:</span>
<span class="n">y</span> <span class="o">=</span> <span class="mi">20</span><span class="p">;</span> <span class="c1">// 缺省值 default value</span>
<span class="k">break</span><span class="p">;</span>

<span class="p">&#125;</span>
</span></code></pre></div>  
</div>
            