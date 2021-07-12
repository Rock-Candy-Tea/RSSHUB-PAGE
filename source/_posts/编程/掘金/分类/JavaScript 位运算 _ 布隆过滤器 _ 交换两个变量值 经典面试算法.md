
---
title: 'JavaScript 位运算 _ 布隆过滤器 _ 交换两个变量值 经典面试算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875b9b4681e443a5a1bdca0c4a5c0e63~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 05:18:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875b9b4681e443a5a1bdca0c4a5c0e63~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<h1 data-id="heading-0">面试题目</h1>
<h3 data-id="heading-1">1.如何交换两个变量的值？</h3>
<p><strong>方法1</strong>：我们平时都用的，整个中间变量：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> mid 

mid = x 

x = y 

y = mid

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法2</strong>：借助位运算，不需要任何辅助空间</p>
<p><strong>但是这个有缺陷！！只能转换Number类型哦</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875b9b4681e443a5a1bdca0c4a5c0e63~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>方法3</strong>：不需要任何辅助空间<strong>强烈推荐！！！</strong></p>
<p>这个方法可以转换任何类型</p>
<pre><code class="hljs language-js copyable" lang="js">
x = [y,y=x][<span class="hljs-number">0</span>]

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">比较大小</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/511dc87429044e30aa26ea9134174604~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee0565e471c34e59b6411cadd859dda6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c84c6817e00c4f3e90a602ba5b797a73~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">其他</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flolitasian.blog.csdn.net%2Farticle%2Fdetails%2F105301924" target="_blank" rel="nofollow noopener noreferrer" title="https://lolitasian.blog.csdn.net/article/details/105301924" ref="nofollow noopener noreferrer">JavaScrip 判断数组元素 | 位运算 经典面试算法</a></p>
<hr>
<h1 data-id="heading-4">布隆过滤器</h1>
<blockquote>
<p><strong>介绍哈希函数</strong></p>
</blockquote>
<p>哈希函数又叫散列函数,哈希函数的输入域可以是非常大的范围,但是输出域是固定范围。</p>
<p>哈希函数的性质：</p>
<p>1、典型的哈希函数都拥有无限的输入值域</p>
<p>2、输入值相同时,返回值一样。</p>
<p>3、输入值不同时,返回值可能一样,也可能不一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3daa3d11113e4c5f92782bae78ff9b5d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>算一下哈，如果把所有的黑名单都存到数据库中，![在这里插入图片描述](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimg-blog.csdnimg.cn%2F20200404144005653.png" target="_blank" rel="nofollow noopener noreferrer" title="https://img-blog.csdnimg.cn/20200404144005653.png" ref="nofollow noopener noreferrer">img-blog.csdnimg.cn/20200404144…</a> =200x)</p>
<p>我算了一下也就是需要5.8T的空间来存嘛。</p>
<p>但是！！！题目中说给你的空间不超过30G！！！所以你就不能直接存数据库里了，你就得用到布隆过滤器的知识了。</p>
<p><strong>我只会系统的讲一下什么是布隆过滤器，想深入了解的自己去查</strong></p>
<p>布隆过滤器可精确的代表一个集合，可精确判断某一元素是否在此集合中，<strong>精确程度由用户的具体设计决定</strong>，做到100%的精确即正确是不可能的。<strong>布隆过滤器的优势在于,利用很少的空间，可以做到精确率较高。</strong></p>
<h3 data-id="heading-5">原理</h3>
<ul>
<li>
<p>当你的url加入之后，bitarray就相当于一个包含了所有的url的集合。</p>
<ul>
<li>
<p>设立一个bitarray的二进制数组，数组一项大小为1比特，初始时候全都为0</p>
</li>
<li>
<p>一个URL，我们通过k个哈希函数将其计算。得出k个结果。将计算结果放入哈希表bitarray之中，如果结果在哈希表中为0，我们哈希表该位置设为1</p>
</li>
</ul>
</li>
<li>
<p>当你要查找某个url是否在其中，你只需要将这个url经过你所设定的k个哈希函数的计算，</p>
</li>
</ul>
<p>看看结果所对应的哈希表上的位置，如果k个位置均为1，则证明你要检测的这个url在bitarray；反正有一个位置为0，就证明这个网页不在bitarray中。</p>
<p>这样我们就能感觉到缺陷了，因为会产生误判，就是可能这个网页它没在黑名单里，但是经过k个哈希函数计算之后所在的k个位置却都是1，被认为是在黑名单中。</p>
<p>![在这里插入图片描述](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimg-blog.csdnimg.cn%2F20200404145306353.jpg%3Fx-oss-process%3Dimage%2Fwatermark%2Ctype_ZmFuZ3poZW5naGVpdGk%2Cshadow_10%2Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw%2Csize_16%2Ccolor_FFFFFF%2Ct_70" target="_blank" rel="nofollow noopener noreferrer" title="https://img-blog.csdnimg.cn/20200404145306353.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" ref="nofollow noopener noreferrer">img-blog.csdnimg.cn/20200404145…</a> =600x)</p>
<h3 data-id="heading-6">布隆过滤器如何设置？</h3>
<p>说了布隆过滤器会产生误判，那怎么知道误判的概率呢。回到这个题：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb14a8dba9e34e9ab651f760aa93470d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>先看这个题目中的数据：</strong></p>
<p>黑名单url个数：100亿</p>
<p>url大小：64B</p>
<p>允许失误率：0.01%</p>
<p>空间限制：30G</p>
<ul>
<li>
<p><strong>bitarray：受黑名单url个数和允许失误率的影响。</strong></p>
<ul>
<li>公式：</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9665cbd7a94a4e63b412777853458345~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">- m：bitarray大小（bitarray一项的大小为1比特）

- n：样本数量

- p：允许失误率



- 在这个题里边n = 100 亿，p=0.01%，求出 m = 19.19n，向上取整20n，20n比特也就是![在这里插入图片描述](https://img-blog.csdnimg.cn/20200404152319845.png =200x)

- <font color=sienna>23G比要求的30G少哦。比起存在数据库里需要6000G，少很多了哦。</font>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><strong>散列函数：数量受bitarray大小和样本数量的影响；函数设计受url大小影响</strong></p>
<ul>
<li>数量公式：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfb41fe5f3204426b8b88ddc40fd3c06~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">  - k：散列函数的个数

  - m：bitarray大小（bitarray一项的大小为1比特）

  - n：样本数量
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>本题中m = 20n，求得k为14，也就是你最少需要设立14个散列函数</li>
</ul>
</li>
<li>
<p>精确程度</p>
<ul>
<li>公式：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18f8c7725b684bfd82691b0b52864245~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">  -  本题中n = 100亿，m = 20n ， k =14 ，计算之后 实际的失误率为0.006%

  - <font color=sienna>比题目要求的0.01%还低哦。</font>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-7">适用情况</h3>
<p><strong>容忍一定程度的失误率，对空间要求较严格</strong></p>
<ul>
<li>
<p>网页黑名单系统</p>
</li>
<li>
<p>垃圾邮件过滤系统</p>
</li>
<li>
<p>爬虫的网址判断重复系统</p>
</li>
</ul></div>  
</div>
            