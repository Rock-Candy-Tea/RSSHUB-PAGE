
---
title: '你写过哪些实用的Python代码？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic2.zhimg.com/v2-3a4b3e4af4a3663f6c3896202cc22007_720w.jpg?source=b1748391'
author: 知乎
comments: false
date: Thu, 09 Jun 2022 16:36:28 GMT
thumbnail: 'https://pic2.zhimg.com/v2-3a4b3e4af4a3663f6c3896202cc22007_720w.jpg?source=b1748391'
---

<div>   
朱卫军的回答<br><br><p data-pid="pJ-TaQkF">Python这门语言很适合用来写些实用的小脚本，跑个自动化、爬虫、算法什么的，非常方便。</p><p data-pid="biO1_tlc">这也是很多人学习Python的乐趣所在，可能只需要花个礼拜入门语法，就能用第三方库去解决实际问题。我在Github上就看到过不少Python代码的项目，几十行代码就能实现一个场景功能，非常实用。</p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-3a4b3e4af4a3663f6c3896202cc22007_720w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="300" data-rawheight="300" data-default-watermark-src="https://pic3.zhimg.com/v2-1f86b82d2ac2e249afa1d1637a186ed0_720w.jpg?source=b1748391" class="content_image" referrerpolicy="no-referrer"></figure><p data-pid="mxdjK7UQ">比方说仓库Python-master里的几个简单例子：</p><h2>1、创建二维码</h2><div class="highlight"><pre><code class="language-python3"><span><span class="kn">import</span> <span class="nn">pyqrcode</span>
<span class="kn">import</span> <span class="nn">png</span>
<span class="kn">from</span> <span class="nn">pyqrcode</span> <span class="kn">import</span> <span class="n">QRCode</span>

<span class="c1"># Text which is to be converted to QR code</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Enter text to convert"</span><span class="p">)</span>
<span class="n">s</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">": "</span><span class="p">)</span>
<span class="c1"># Name of QR code png file</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Enter image name to save"</span><span class="p">)</span>
<span class="n">n</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">": "</span><span class="p">)</span>
<span class="c1"># Adding extension as .pnf</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">n</span> <span class="o">+</span> <span class="s2">".png"</span>
<span class="c1"># Creating QR code</span>
<span class="n">url</span> <span class="o">=</span> <span class="n">pyqrcode</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<span class="c1"># Saving QR code as  a png file</span>
<span class="n">url</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">url</span><span class="o">.</span><span class="n">png</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">scale</span><span class="o">=</span><span class="mi">6</span><span class="p">)</span>
</span></code></pre></div><h2>2、从图片中截取文字</h2><div class="highlight"><pre><code class="language-python3"><span><span class="c1"># extract text from a img and its coordinates using the pytesseract module</span>
<span class="kn">import</span> <span class="nn">cv2</span>
<span class="kn">import</span> <span class="nn">pytesseract</span>

<span class="c1"># You need to add tesseract binary dependency to system variable for this to work</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="s2">"img.png"</span><span class="p">)</span>
<span class="c1"># We need to convert the img into RGB format</span>
<span class="n">img</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">img</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2RGB</span><span class="p">)</span>

<span class="n">hI</span><span class="p">,</span> <span class="n">wI</span><span class="p">,</span> <span class="n">k</span> <span class="o">=</span> <span class="n">img</span><span class="o">.</span><span class="n">shape</span>
<span class="nb">print</span><span class="p">(</span><span class="n">pytesseract</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span><span class="n">img</span><span class="p">))</span>
<span class="n">boxes</span> <span class="o">=</span> <span class="n">pytesseract</span><span class="o">.</span><span class="n">image_to_boxes</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">boxes</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">" "</span><span class="p">)</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="p">[</span><span class="mi">3</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="p">[</span><span class="mi">4</span><span class="p">])</span>
    <span class="n">cv2</span><span class="o">.</span><span class="n">rectangle</span><span class="p">(</span><span class="n">img</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">hI</span> <span class="o">-</span> <span class="n">y</span><span class="p">),</span> <span class="p">(</span><span class="n">w</span><span class="p">,</span> <span class="n">hI</span> <span class="o">-</span> <span class="n">h</span><span class="p">),</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">),</span> <span class="mf">0.2</span><span class="p">)</span>

<span class="n">cv2</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="s2">"img"</span><span class="p">,</span> <span class="n">img</span><span class="p">)</span>
<span class="n">cv2</span><span class="o">.</span><span class="n">waitKey</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span></code></pre></div><h2>3、判断闰年</h2><div class="highlight"><pre><code class="language-python3"><span><span class="k">def</span> <span class="nf">is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">):</span>
    <span class="n">leap</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="k">if</span> <span class="n">year</span> <span class="o">%</span> <span class="mi">4</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">leap</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">if</span> <span class="n">year</span> <span class="o">%</span> <span class="mi">100</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">leap</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="n">year</span> <span class="o">%</span> <span class="mi">400</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">leap</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="k">return</span> <span class="n">leap</span>


<span class="n">year</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">"Enter the year here: "</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">))</span>
</span></code></pre></div><h2>4、简易日历</h2><div class="highlight"><pre><code class="language-python3"><span><span class="kn">from</span> <span class="nn">tkinter</span> <span class="kn">import</span> <span class="o">*</span>
<span class="kn">import</span> <span class="nn">calendar</span>

<span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
<span class="c1"># root.geometry("400x300")</span>
<span class="n">root</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Calendar"</span><span class="p">)</span>

<span class="c1"># Function</span>

<span class="k">def</span> <span class="nf">text</span><span class="p">():</span>
    <span class="n">month_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">month</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
    <span class="n">year_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">year</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
    <span class="n">cal</span> <span class="o">=</span> <span class="n">calendar</span><span class="o">.</span><span class="n">month</span><span class="p">(</span><span class="n">year_int</span><span class="p">,</span> <span class="n">month_int</span><span class="p">)</span>
    <span class="n">textfield</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">END</span><span class="p">)</span>
    <span class="n">textfield</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">INSERT</span><span class="p">,</span> <span class="n">cal</span><span class="p">)</span>


<span class="c1"># Creating Labels</span>
<span class="n">label1</span> <span class="o">=</span> <span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s2">"Month:"</span><span class="p">)</span>
<span class="n">label1</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">column</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>

<span class="n">label2</span> <span class="o">=</span> <span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s2">"Year:"</span><span class="p">)</span>
<span class="n">label2</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">column</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="c1"># Creating spinbox</span>
<span class="n">month</span> <span class="o">=</span> <span class="n">Spinbox</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">from_</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">to</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">8</span><span class="p">)</span>
<span class="n">month</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">column</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">padx</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>

<span class="n">year</span> <span class="o">=</span> <span class="n">Spinbox</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">from_</span><span class="o">=</span><span class="mi">2000</span><span class="p">,</span> <span class="n">to</span><span class="o">=</span><span class="mi">2100</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="n">year</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">column</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">padx</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="c1"># Creating Button</span>
<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s2">"Go"</span><span class="p">,</span> <span class="n">command</span><span class="o">=</span><span class="n">text</span><span class="p">)</span>
<span class="n">button</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">column</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">padx</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="c1"># Creating Textfield</span>
<span class="n">textfield</span> <span class="o">=</span> <span class="n">Text</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s2">"red"</span><span class="p">)</span>
<span class="n">textfield</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">columnspan</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>


<span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
</span></code></pre></div><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-b67a419b395127366d4b98382db921a9_1440w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="462" data-rawheight="430" data-default-watermark-src="https://pic2.zhimg.com/v2-e7923c4e486fec1aecb53033fc6ded40_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-b67a419b395127366d4b98382db921a9_r.jpg?source=b1748391" referrerpolicy="no-referrer"></figure><h2>5、打印图片分辨率</h2><div class="highlight"><pre><code class="language-python3"><span><span class="k">def</span> <span class="nf">jpeg_res</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
   <span class="sd">""""This function prints the resolution of the jpeg image file passed into it"""</span>

   <span class="c1"># open image for reading in binary mode</span>
   <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span><span class="s1">'rb'</span><span class="p">)</span> <span class="k">as</span> <span class="n">img_file</span><span class="p">:</span>

       <span class="c1"># height of image (in 2 bytes) is at 164th position</span>
       <span class="n">img_file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">163</span><span class="p">)</span>

       <span class="c1"># read the 2 bytes</span>
       <span class="n">a</span> <span class="o">=</span> <span class="n">img_file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

       <span class="c1"># calculate height</span>
       <span class="n">height</span> <span class="o">=</span> <span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o"><<</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">a</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

       <span class="c1"># next 2 bytes is width</span>
       <span class="n">a</span> <span class="o">=</span> <span class="n">img_file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

       <span class="c1"># calculate width</span>
       <span class="n">width</span> <span class="o">=</span> <span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o"><<</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">a</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

   <span class="nb">print</span><span class="p">(</span><span class="s2">"The resolution of the image is"</span><span class="p">,</span><span class="n">width</span><span class="p">,</span><span class="s2">"x"</span><span class="p">,</span><span class="n">height</span><span class="p">)</span>

<span class="n">jpeg_res</span><span class="p">(</span><span class="s2">"img1.jpg"</span><span class="p">)</span>
</span></code></pre></div><p data-pid="gT1rExMe">这个项目只是作者平时工作用到的一些小脚本，可能也会帮助到你。作者虽然不是程序员，但他这种用代码解决问题的习惯会极大的提升效率，也会迸发出更多的创新思维。我觉得这样的代码每个人都可以写出来，只要慢慢积累多练习就可以。</p><a href="http://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s%3F__biz%3DMzA3ODYwNDkzOQ%3D%3D%26mid%3D2659071334%26idx%3D1%26sn%3D045e9f45659360f3f898c9909f234aff%26chksm%3D84caaa82b3bd23941c83e605556856c78c5fac146fd014f40609b4d71cc550c37e8525622102%26token%3D1112099561%26lang%3Dzh_CN%23rd" data-draft-node="block" data-draft-type="link-card" data-image="https://pica.zhimg.com/v2-f8408cfcd3c31a54c1e33f33571a4b7f_qhd.jpg?source=b1748391" data-image-width="1056" data-image-height="449" class=" wrap external" target="_blank" rel="nofollow noreferrer">Python-master实用脚本合集下载</a><p data-pid="QcpQ7q0P">我平时也在知乎分享了很多代码和技术文章，这里贴出来希望对你会有帮助。</p><h2>6、我的代码库</h2><h3>（1）Pandas & Numpy数据处理</h3><p data-pid="b82XjP5x"><a href="https://zhuanlan.zhihu.com/p/267208129" class="internal">在pandas中使用数据透视表</a></p><p data-pid="HWvhVL8E"><a href="https://zhuanlan.zhihu.com/p/258699675" class="internal">高效的5个pandas函数，你都用过吗？</a></p><p data-pid="aJJp3nAV"><a href="https://zhuanlan.zhihu.com/p/231591842" class="internal">6个pandas数据处理小技巧，提升效率必备</a></p><p data-pid="fqWi9ONL"><a href="https://zhuanlan.zhihu.com/p/185044102" class="internal">高效的10个Pandas函数，你都用过了吗？</a></p><p data-pid="SIIR7b_h"><a href="https://www.zhihu.com/question/37180159/answer/761102349" class="internal">如何系统地学习Python 中 matplotlib, numpy, scipy, pandas？</a></p><p data-pid="DNg2HKaN"><a href="https://www.zhihu.com/question/360375438/answer/932490349" class="internal">用python爬虫爬去数据直接用excel处理就好，为什么还用pandas来处理？</a></p><p data-pid="U9LxKuu0"><a href="https://zhuanlan.zhihu.com/p/98094833" class="internal">干货 | 50题带你玩转numpy</a></p><p data-pid="aW5Iq2rN"><a href="https://zhuanlan.zhihu.com/p/125696272" class="internal">Numpy基础20问</a></p><p data-pid="jSfskQ07"><a href="https://zhuanlan.zhihu.com/p/136342642" class="internal">Numpy进阶之排序小技巧</a></p><h3>（2）数据可视化</h3><p data-pid="C-_7Mf56"><a href="https://www.zhihu.com/question/26620885/answer/1095912069" class="internal">好看的数据可视化的图片是怎么样做的？</a></p><p data-pid="idEQl0s2"><a href="https://www.zhihu.com/question/24590883/answer/729452252" class="internal">哪些 Python 库让你相见恨晚？</a></p><p data-pid="JvEWkKHx"><a href="https://www.zhihu.com/question/39684179/answer/785341703" class="internal">Python中除了matplotlib外还有哪些数据可视化的库？</a></p><p data-pid="GNkyFGoO"><a href="https://zhuanlan.zhihu.com/p/113312256" class="internal">使用pyecharts绘制词云图-淘宝商品评论展示</a></p><p data-pid="MaOPDRJi"><a href="https://zhuanlan.zhihu.com/p/81553421" class="internal">数据可视化，Seaborn画图原来这么好看</a></p><p data-pid="WmY_SvnD"><a href="https://zhuanlan.zhihu.com/p/130510767" class="internal">seaborn常用的10种数据分析图表</a></p><p data-pid="NMuAo4XD"><a href="https://zhuanlan.zhihu.com/p/162013514" class="internal">Superset，基于web的开源BI工具，github三万star</a></p><p data-pid="YHMF5gwT"><a href="https://zhuanlan.zhihu.com/p/80410924" class="internal">教你用pyecharts制作交互式桑基图，赶快学起来吧！</a></p><p data-pid="6FYjpV_S"><a href="https://zhuanlan.zhihu.com/p/84600119" class="internal">干货 | Bokeh交互式数据可视化快速入门</a></p><h3>（3）空间地理信息</h3><p data-pid="Jkk9048o"><a href="https://zhuanlan.zhihu.com/p/185824432" class="internal">聊一聊Python中优秀的6个地图可视化库</a></p><p data-pid="-QR3Cj5X"><a href="https://zhuanlan.zhihu.com/p/157654529" class="internal">24页PPT | 如何利用python进行地图可视化？</a></p><p data-pid="s5aWLCuh"><a href="https://zhuanlan.zhihu.com/p/80210579" class="internal">geopandas，用python分析地理空间数据原来这么简单！</a></p><p data-pid="pEdkMV0i"><a href="https://zhuanlan.zhihu.com/p/83231415" class="internal">干货 | 使用pyecharts绘制交互式动态地图</a></p><h3>（4）爬虫</h3><p data-pid="YR_EA1I3"><a href="https://zhuanlan.zhihu.com/p/77560712" class="internal">小白如何入门 Python 爬虫？</a></p><p data-pid="x2QeX4P9"><a href="https://zhuanlan.zhihu.com/p/259626718" class="internal">selenium入门详细指南（附淘宝抢购案例）</a></p><p data-pid="GqsnTWbu"><a href="https://zhuanlan.zhihu.com/p/79378718" class="internal">哪吒票房超复联4，100行python代码抓取豆瓣短评，看看网友怎么说</a></p><p data-pid="vX8TeR7H"><a href="https://zhuanlan.zhihu.com/p/83968537" class="internal">使用requests爬取python岗位招聘数据</a></p><p data-pid="1RYQSKc3"><a href="https://zhuanlan.zhihu.com/p/50361592" class="internal">电影《毒液》豆瓣短评 爬虫&分词&词云展示</a></p><p data-pid="S9g6uxUu"><a href="https://www.zhihu.com/question/369762095/answer/1006682849" class="internal">有哪些足不出户，能用十天左右时间掌握的新技能？</a></p><p data-pid="5nXb8I30"><a href="https://zhuanlan.zhihu.com/p/73742321" class="internal">干货！python爬虫100个入门项目</a></p><p data-pid="yTSUsHo9"><a href="https://zhuanlan.zhihu.com/p/75036835" class="internal">干货！python爬虫100个入门项目 续</a></p><h3>（5）自动化办公</h3><p data-pid="dkbKLDWI"><a href="https://www.zhihu.com/question/358012330/answer/963749700" class="internal">用python进行办公自动化都需要学习什么知识呢？</a></p><p data-pid="514zY8nm"><a href="https://zhuanlan.zhihu.com/p/102737358" class="internal">python自动化办公太难？学这些就够用了</a></p><p data-pid="Nn2a_Miq"><a href="https://zhuanlan.zhihu.com/p/104524969" class="internal">python读写excel等数据文件方法汇总</a></p><p data-pid="2PYYgZ-r"><a href="https://zhuanlan.zhihu.com/p/82783751" class="internal">xlwings，让excel飞起来！</a></p><p data-pid="2HfJqi10"><a href="https://www.zhihu.com/question/425433531/answer/1541159992" class="internal">python操作CSV和excel,如何来做?</a></p><p data-pid="zL69BqWS"><a href="https://www.zhihu.com/question/315655985/answer/862065505" class="internal">请教下 Python 高手，如何用 Python 自动化操作 Excel？</a></p><h3>（6）数据科学</h3><p data-pid="H7epz6Bl"><a href="https://www.zhihu.com/question/336897569/answer/763169270" class="internal">使用python进行数据分析工作，要掌握哪些数学知识?</a></p><p data-pid="itkJgFzI"><a href="https://zhuanlan.zhihu.com/p/240797772" class="internal">Vaex ：突破pandas，快速分析100G大数据量</a></p><p data-pid="DuOhL517"><a href="https://zhuanlan.zhihu.com/p/207057233" class="internal">jieba分词-强大的Python 中文分词库</a></p><p data-pid="yMZJgj1t"><a href="https://zhuanlan.zhihu.com/p/78882641" class="internal">numba，让python速度提升百倍</a></p><p data-pid="7yImsjX3"><a href="https://zhuanlan.zhihu.com/p/79628718" class="internal">最全Python数据科学小抄，赶紧收藏吧！</a></p><p data-pid="9A1HpWTR"><a href="https://zhuanlan.zhihu.com/p/81551742" class="internal">看图涨知识，一百天搞定机器学习</a></p><p data-pid="066kRiW3"><a href="https://zhuanlan.zhihu.com/p/82251858" class="internal">Python数据分析案例 | 台风最喜欢在我国哪个省市登陆</a></p><p data-pid="NKwjm-Gg"><a href="https://zhuanlan.zhihu.com/p/85967505" class="internal">pandas_profiling ：教你一行代码生成数据分析报告</a></p><p data-pid="fYsVh2p5"><a href="https://zhuanlan.zhihu.com/p/74080229" class="internal">干货！小白入门Python数据科学全教程</a></p><p data-pid="1zFAKcck"><a href="https://zhuanlan.zhihu.com/p/74616776" class="internal">深入了解机器学习 (Descending into ML)：线性回归</a></p><p data-pid="jM8mdz2V"><a href="https://zhuanlan.zhihu.com/p/74680962" class="internal">机器学习5大数学知识，你必须要掌握！</a></p><p data-pid="ULgx6EY4"><a href="https://zhuanlan.zhihu.com/p/75285353" class="internal">Python机器学习·微教程</a></p><p data-pid="MRlqtcnR"><a href="https://zhuanlan.zhihu.com/p/51812293" class="internal">Keras中的多变量时间序列预测-LSTMs</a></p><p data-pid="ULgG7Pf1"><a href="https://zhuanlan.zhihu.com/p/52914294" class="internal">一文读懂随机森林的解释和实现</a></p><p data-pid="bqRHs47h"><a href="https://zhuanlan.zhihu.com/p/52971768" class="internal">机器学习中的数据缩放-Python Scikit-Learn实现方法</a></p><p data-pid="JJ1Tuntj"><a href="https://zhuanlan.zhihu.com/p/53278304" class="internal">如何使用Python scikit-learn机器学习库做分类和回归预测</a></p><p data-pid="3Ri04Fj3"><a href="https://zhuanlan.zhihu.com/p/59673364" class="internal">机器学习中的泛化能力</a></p><h3>（7）数据库</h3><p data-pid="VOP5epnn"><a href="https://zhuanlan.zhihu.com/p/37552115" class="internal">如何使用python连接数据库？</a></p><p data-pid="2MpgdxYH"><a href="https://zhuanlan.zhihu.com/p/196807781" class="internal">Python sqlite3数据库模块使用攻略</a></p><p data-pid="doJ8xrQZ"><a href="https://zhuanlan.zhihu.com/p/45533287" class="internal">如何通过Python将CSV文件导入MySQL数据库？</a></p><p data-pid="p8C2XiUk"><a href="https://www.zhihu.com/question/323688843/answer/1099641029" class="internal">python与mysql怎么完成大量的数据交互？</a></p><p></p>  
</div>
            