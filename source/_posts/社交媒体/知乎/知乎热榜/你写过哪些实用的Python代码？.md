
---
title: '你写过哪些实用的Python代码？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=9931'
author: 知乎
comments: false
date: Thu, 09 Jun 2022 15:00:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=9931'
---

<div>   
Jackpop的回答<br><br><p data-pid="fLliMD_4">编程语言的出现和演进都是为了直接或者简洁的改变工作效率，Python的出现并非只能用于数据分析、机器学习。</p><p data-pid="0rOIG9dg">如果仔细琢磨日常的工作 和生活，可以通过一些Python脚本大大的提升效率，同时还可以绕开很多收费工具，节省不少钱。</p><p data-pid="6dAdjNHf">今天，我就来给大家介绍之前写过的一些杀手级脚本，真的是幸福感爆棚！</p><h2><b>1. 图像编辑</b></h2><p data-pid="YqnbiSe5">使用这个自动化脚本，以编程方式编辑你的图像。</p><p data-pid="KebfQRHP">下面是我在编辑图片的常用功能，如模糊、旋转、翻转、合并等。</p><p data-pid="heDILF1q">要实现这些功能，往常都需要安装一些臃肿的软件，但是，一个简单的Python脚本就可以轻松解决。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">ImageDraw</span>
<span class="err">​</span>
<span class="c1"># 合并图像</span>
<span class="n">img1</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">img2</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img102.jpg'</span><span class="p">)</span>
<span class="n">combine</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">blend</span><span class="p">(</span><span class="n">img1</span><span class="p">,</span> <span class="n">img2</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 调整图像大小</span>
<span class="n">resize</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">resize</span> <span class="o">=</span> <span class="n">resize</span><span class="o">.</span><span class="n">resize</span><span class="p">((</span><span class="mi">300</span><span class="p">,</span> <span class="mi">300</span><span class="p">))</span>
<span class="err">​</span>
<span class="c1"># 翻转图像</span>
<span class="n">flip_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">flip_image</span> <span class="o">=</span> <span class="n">flip_image</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">FLIP_LEFT_RIGHT</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 模糊图像</span>
<span class="n">blur_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">blur_image</span> <span class="o">=</span> <span class="n">blur_image</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">BLUR</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 添加阴影</span>
<span class="n">shadow_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">shadow_image</span> <span class="o">=</span> <span class="n">shadow_image</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">EDGE_ENHANCE_MORE</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 裁剪图片</span>
<span class="n">crop_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">crop_image</span> <span class="o">=</span> <span class="n">crop_image</span><span class="o">.</span><span class="n">crop</span><span class="p">((</span><span class="mi">50</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">200</span><span class="p">))</span>
<span class="err">​</span>
<span class="c1"># 增加亮度</span>
<span class="n">bright_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">bright_image</span> <span class="o">=</span> <span class="n">bright_image</span><span class="o">.</span><span class="n">point</span><span class="p">(</span><span class="k">lambda</span> <span class="n">p</span><span class="p">:</span> <span class="n">p</span> <span class="o">+</span> <span class="mi">50</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 添加文字</span>
<span class="n">text_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">text_image</span> <span class="o">=</span> <span class="n">text_image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s1">'RGB'</span><span class="p">)</span>
<span class="n">draw</span> <span class="o">=</span> <span class="n">ImageDraw</span><span class="o">.</span><span class="n">Draw</span><span class="p">(</span><span class="n">text_image</span><span class="p">)</span>
<span class="n">draw</span><span class="o">.</span><span class="n">text</span><span class="p">((</span><span class="mi">10</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> <span class="s2">"Hello World"</span><span class="p">,</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">))</span>
<span class="err">​</span>
<span class="c1"># 旋转图像</span>
<span class="n">rotate_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
<span class="n">rotate_image</span> <span class="o">=</span> <span class="n">rotate_image</span><span class="o">.</span><span class="n">rotate</span><span class="p">(</span><span class="mi">90</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 保存图像</span>
<span class="n">img1</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'img101.jpg'</span><span class="p">)</span>
</span></code></pre></div><h2><b>2. 音频编辑</b></h2><p data-pid="EKKHVtW6">这个自动化脚本将为你编辑音频文件，你可以提取声音、合并声音、播放声音、分割/切割声音等等，通过这个脚本，终于可以扔掉那些付费软件了。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">pydub</span> <span class="kn">import</span> <span class="n">AudioSegment</span>
<span class="kn">from</span> <span class="nn">pydub.utils</span> <span class="kn">import</span> <span class="n">mediainfo</span>
<span class="kn">from</span> <span class="nn">pydub.playback</span> <span class="kn">import</span> <span class="n">play</span>
<span class="err">​</span>
<span class="c1"># 从视频中提取声音</span>
<span class="n">sound</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"video.mp4"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>
<span class="n">sound</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 获取媒体信息</span>
<span class="n">info</span> <span class="o">=</span> <span class="n">mediainfo</span><span class="p">(</span><span class="s2">"musci.wav"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">info</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 播放音频</span>
<span class="n">play</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 合并音频</span>
<span class="n">sound1</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">)</span>
<span class="n">sound2</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">)</span>
<span class="n">combined</span> <span class="o">=</span> <span class="n">sound1</span> <span class="o">+</span> <span class="n">sound2</span>
<span class="n">combined</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music_combined.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 分割音频</span>
<span class="n">sound</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="n">sound_1</span> <span class="o">=</span> <span class="n">sound</span><span class="p">[:</span><span class="mi">10000</span><span class="p">]</span>
<span class="n">sound_2</span> <span class="o">=</span> <span class="n">sound</span><span class="p">[</span><span class="mi">10000</span><span class="p">:]</span>
<span class="n">sound_1</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music_1.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="n">sound_2</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music_2.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 增大或减小音量</span>
<span class="n">sound</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="n">sound_volumn</span> <span class="o">=</span> <span class="n">sound</span> <span class="o">+</span> <span class="mi">10</span>
<span class="n">sound_volumn</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music_volumn.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 为音频添加静音</span>
<span class="n">sound</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="s2">"music.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
<span class="n">sound_silence</span> <span class="o">=</span> <span class="n">sound</span> <span class="o">+</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">silent</span><span class="p">(</span><span class="n">duration</span><span class="o">=</span><span class="mi">1000</span><span class="p">)</span>
<span class="n">sound_silence</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">"music_silence.mp3"</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>
</span></code></pre></div><h2><b>3. 文件加解密</b></h2><p data-pid="tU-P1r9U">工作中，我们经常会产生一些重要的文件，需要限制阅读人员，那么这个脚本就可以提供帮助。</p><p data-pid="WxE8R6UG">这个脚本使用密码学技术对你的文件进行加密，当你需要打开它们时，你可以使用密码解密它们。</p><p data-pid="W5kkarjV">这是一个非常安全的方法来锁定你的文件，因为在没有钥匙的情况下就没办法阅读。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">cryptography.fernet</span> <span class="kn">import</span> <span class="n">Fernet</span>
<span class="err">​</span>
<span class="c1"># 加密函数</span>
<span class="k">def</span> <span class="nf">Lock_file</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="s1">'rb'</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
    <span class="n">f</span> <span class="o">=</span> <span class="n">Fernet</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="n">encrypted_data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">encrypt</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="s1">'wb'</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
        <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">encrypted_data</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"File Lock..."</span><span class="p">)</span>
   
<span class="c1"># 解密函数</span>
<span class="k">def</span> <span class="nf">Unlock_file</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="s1">'rb'</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
    <span class="n">f</span> <span class="o">=</span> <span class="n">Fernet</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="n">decrypted_data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">decrypt</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="s1">'wb'</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
        <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">decrypted_data</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"File Unlock..."</span><span class="p">)</span>
    
<span class="n">key</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Enter the key: "</span><span class="p">)</span>
<span class="n">Lock_file</span><span class="p">(</span><span class="s1">'test.txt'</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span>
<span class="n">Unlock_file</span><span class="p">(</span><span class="s1">'test.txt'</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span>
</span></code></pre></div><h2><b>4. 录屏工具</b></h2><p data-pid="oPBmtZOi">录屏是现如今使用非常频繁的一类工具，但是，目前很多录屏软件都收费，有的导出时会在视频上添加水印。</p><p data-pid="7waPDcrS">所以，知乎上也经常看到有不少人迫切需求无水印、免费的录屏软件。</p><p data-pid="y74PjiQF">其实，一个Python脚本就可以搞定！</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">import</span> <span class="nn">pyautogui</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">cv2</span>
<span class="kn">import</span> <span class="nn">keyboard</span>
<span class="err">​</span>
<span class="k">def</span> <span class="nf">Screen_Recording</span><span class="p">():</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="c1"># Press R to Start Recording</span>
        <span class="k">if</span> <span class="n">keyboard</span><span class="o">.</span><span class="n">is_pressed</span><span class="p">(</span><span class="s1">'r'</span><span class="p">):</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Recording Has been Started..."</span><span class="p">)</span>
            <span class="c1"># resolution</span>
            <span class="n">capture_area</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1920</span><span class="p">,</span> <span class="mi">1080</span><span class="p">)</span> 
            
            <span class="n">codec</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">VideoWriter_fourcc</span><span class="p">(</span><span class="o">*</span><span class="s1">'mp4v'</span><span class="p">)</span>
            <span class="n">filename</span> <span class="o">=</span> <span class="s2">"Your_Recording.mp4"</span>
<span class="err">​</span>
            <span class="n">fps</span> <span class="o">=</span> <span class="mf">60.0</span>
            <span class="n">output_video</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">VideoWriter</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">codec</span><span class="p">,</span> <span class="n">fps</span><span class="p">,</span> <span class="n">capture_area</span><span class="p">)</span>
            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">image</span> <span class="o">=</span> <span class="n">pyautogui</span><span class="o">.</span><span class="n">screenshot</span><span class="p">()</span>
                <span class="n">Image_frame</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
                <span class="n">Image_frame</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">Image_frame</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2RGB</span><span class="p">)</span>
                <span class="n">output_video</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">Image_frame</span><span class="p">)</span>
                <span class="n">cv2</span><span class="o">.</span><span class="n">waitKey</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
                <span class="c1"># Press Q button to Stop recording</span>
                <span class="k">if</span> <span class="n">keyboard</span><span class="o">.</span><span class="n">is_pressed</span><span class="p">(</span><span class="s1">'q'</span><span class="p">):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"Recording Has been Stopped..."</span><span class="p">)</span>
                    <span class="k">break</span>
            <span class="n">output_video</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
            <span class="n">cv2</span><span class="o">.</span><span class="n">destroyAllWindows</span><span class="p">()</span>
<span class="n">Screen_Recording</span><span class="p">()</span>
</span></code></pre></div><h2><b>5. 从PDF中提取表格</b></h2><p data-pid="B1K6xMPF">从PDF中提取表格是一项复杂的任务，通过OCR技术效果一般都不太理想，手动重新建个表格工作量又比较大。</p><p data-pid="GGNsKKWI">这个脚本将简单地从你的PDF中提取表格，它不仅 可以提取单个PDF的表格，还可以从多个PDF中一个一个地提取表格。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">import</span> <span class="nn">camelot</span>
<span class="n">table</span> <span class="o">=</span> <span class="n">camelot</span><span class="o">.</span><span class="n">read_pdf</span><span class="p">(</span><span class="s1">'test.pdf'</span><span class="p">,</span> <span class="n">pages</span><span class="o">=</span><span class="s1">'1-2'</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 获取表的总数</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Total tables: "</span><span class="p">,</span> <span class="n">table</span><span class="o">.</span><span class="n">n</span><span class="p">)</span> 
<span class="nb">print</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 把表格导出为CSV</span>
<span class="n">table</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">'table1.csv'</span><span class="p">)</span>
<span class="n">table</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">'table2.csv'</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 把表格导出为Excel</span>
<span class="n">table</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="s1">'table1.xlsx'</span><span class="p">)</span>
<span class="c1"># Export Table to HTML</span>
<span class="n">table</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">to_html</span><span class="p">(</span><span class="s1">'table1.html'</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 一次性提取和导出表</span>
<span class="n">table</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s1">'tables.csv'</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="s1">'csv'</span><span class="p">,</span> <span class="n">compress</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="err">​</span>
<span class="n">table</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">parse</span><span class="p">([</span><span class="s1">'Date'</span><span class="p">,</span> <span class="s1">'Description'</span><span class="p">,</span> <span class="s1">'Amount'</span><span class="p">])</span>
</span></code></pre></div><h2><b>6. 办公自动化</b></h2><p data-pid="SGof2hI_">你是否想象过你也可以用Python将MS Office软件自动化？</p><p data-pid="AyEogfvx">Office三件套Word、PPT、Excel是绝大多数人在工作和学习中都会用到的工具，但是，目前很多人还都是手动处理一些重复的工作，效率非常低。</p><p data-pid="vo3bngyH">这个脚本就可以解放你的双手，实现MS Office的自动化。</p><div class="highlight"><pre><code class="language-python"><span><span class="c1"># Excel自动化</span>
<span class="kn">import</span> <span class="nn">xlrd</span>
<span class="n">wb</span> <span class="o">=</span> <span class="n">xlrd</span><span class="o">.</span><span class="n">open_workbook</span><span class="p">(</span><span class="s1">'test.xlsx'</span><span class="p">)</span>
<span class="n">worksheet</span> <span class="o">=</span> <span class="n">wb</span><span class="o">.</span><span class="n">sheet_by_index</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c1"># 根据行、列读取数据</span>
<span class="nb">print</span><span class="p">(</span><span class="n">worksheet</span><span class="o">.</span><span class="n">cell_value</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
<span class="c1"># read whole row</span>
<span class="nb">print</span><span class="p">(</span><span class="n">worksheet</span><span class="o">.</span><span class="n">row_values</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span>
<span class="err">​</span>
<span class="c1"># 读取整列</span>
<span class="nb">print</span><span class="p">(</span><span class="n">worksheet</span><span class="o">.</span><span class="n">col_values</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
<span class="err">​</span>
<span class="c1"># 写入Excel</span>
<span class="n">worksheet</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'Hello'</span><span class="p">)</span>
<span class="n">wb</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'test.xlsx'</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># Word自动化</span>
<span class="kn">import</span> <span class="nn">docx</span>
 
<span class="n">doc</span> <span class="o">=</span> <span class="n">docx</span><span class="o">.</span><span class="n">Document</span><span class="p">(</span><span class="s2">"zen_of_python.docx"</span><span class="p">)</span>
 
<span class="c1"># 逐段读取</span>
<span class="n">text</span> <span class="o">=</span> <span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">paragraphs</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 逐表读取</span>
<span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">tables</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">table</span><span class="o">.</span><span class="n">rows</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">cell</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">cells</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># 写入Word文档</span>
<span class="n">doc</span><span class="o">.</span><span class="n">add_paragraph</span><span class="p">(</span><span class="s2">"Hello World"</span><span class="p">)</span>
<span class="n">doc</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">"test.docx"</span><span class="p">)</span>
<span class="err">​</span>
<span class="c1"># PowerPoint自动化</span>
<span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>
<span class="err">​</span>
<span class="c1"># 浏览幻灯片</span>
<span class="n">PP</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="s1">'file.pptx'</span><span class="p">)</span>
<span class="k">for</span> <span class="n">slide</span> <span class="ow">in</span> <span class="n">PP</span><span class="o">.</span><span class="n">slides</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">shape</span> <span class="ow">in</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">paragraph</span> <span class="ow">in</span> <span class="n">shape</span><span class="o">.</span><span class="n">text_frame</span><span class="o">.</span><span class="n">paragraphs</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">paragraph</span><span class="o">.</span><span class="n">runs</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>
<span class="c1"># 写入PPT</span>
<span class="n">PP</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">()</span>
<span class="n">title_slide_layout</span> <span class="o">=</span> <span class="n">PP</span><span class="o">.</span><span class="n">slide_layouts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">slide</span> <span class="o">=</span> <span class="n">PP</span><span class="o">.</span><span class="n">slides</span><span class="o">.</span><span class="n">add_slide</span><span class="p">(</span><span class="n">title_slide_layout</span><span class="p">)</span>
<span class="n">title</span> <span class="o">=</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="o">.</span><span class="n">title</span>
<span class="n">title</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="s2">"Medium Article"</span>
<span class="n">PP</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'file.pptx'</span><span class="p">)</span>
</span></code></pre></div><h2><b>7. 图片转PDF</b></h2><p data-pid="pFIxG-bV">这个简单的自动化脚本帮助你将你的图像转换为PDF格式。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="k">def</span> <span class="nf">Images_Pdf</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">output</span><span class="p">):</span>
    <span class="n">images</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">filename</span><span class="p">:</span>
        <span class="n">im</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">im</span> <span class="o">=</span> <span class="n">im</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s1">'RGB'</span><span class="p">)</span>
        <span class="n">images</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">im</span><span class="p">)</span>
    
    <span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="n">save_all</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">append_images</span><span class="o">=</span><span class="n">images</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span>
<span class="n">Images_Pdf</span><span class="p">([</span><span class="s2">"test1.jpg"</span><span class="p">,</span> <span class="s2">"test2.jpg"</span><span class="p">,</span> <span class="s2">"test3.jpg"</span><span class="p">],</span> <span class="s2">"output.pdf"</span><span class="p">)</span>
</span></code></pre></div><h2><b>8. 文本转语音</b></h2><p data-pid="D_-73dQ4">它使用谷歌文本转语音API，将你的文本内容转换为人工智能机器人的声音。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">pygame</span> <span class="kn">import</span> <span class="n">mixer</span>
<span class="kn">from</span> <span class="nn">gtts</span> <span class="kn">import</span> <span class="n">gTTS</span>
<span class="err">​</span>
<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
   <span class="n">tts</span> <span class="o">=</span> <span class="n">gTTS</span><span class="p">(</span><span class="s1">'Like This Article'</span><span class="p">)</span>
   <span class="n">tts</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'output.mp3'</span><span class="p">)</span>
   <span class="n">mixer</span><span class="o">.</span><span class="n">init</span><span class="p">()</span>
   <span class="n">mixer</span><span class="o">.</span><span class="n">music</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s1">'output.mp3'</span><span class="p">)</span>
   <span class="n">mixer</span><span class="o">.</span><span class="n">music</span><span class="o">.</span><span class="n">play</span><span class="p">()</span>
    
<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">"__main__"</span><span class="p">:</span>
   <span class="n">main</span><span class="p">()</span>
</span></code></pre></div><h2><b>9. 图片压缩</b></h2><p data-pid="Ku8byl6i">有些网站会对图片的大小进行严格的限制，比如，一些报考网站。</p><p data-pid="PsLk9wbC">这时候，就需要用到图片压缩工具。</p><p data-pid="Wo89qKE5">但是，很多压缩工具对图片的质量影响较大。</p><p data-pid="GSPHFuqt">这个脚本把你的照片压缩成较小的尺寸而质量不变。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">import</span> <span class="nn">PIL</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="kn">from</span> <span class="nn">tkinter.filedialog</span> <span class="kn">import</span> <span class="o">*</span>
<span class="n">fl</span><span class="o">=</span><span class="n">askopenfilenames</span><span class="p">()</span>
<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">fl</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">"result.jpg"</span><span class="p">,</span> <span class="s2">"JPEG"</span><span class="p">,</span> <span class="n">optimize</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">quality</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span>
</span></code></pre></div><h2><b>10. 图像加水印</b></h2><p data-pid="lQRklOxB">这个简单的脚本可以给任何图片加水印。</p><p data-pid="PWxYCRAk">你可以设置文本、位置和字体。</p><div class="highlight"><pre><code class="language-python"><span><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">ImageFont</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">ImageDraw</span>
<span class="k">def</span> <span class="nf">watermark_img</span><span class="p">(</span><span class="n">img_path</span><span class="p">,</span><span class="n">res_path</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">pos</span><span class="p">):</span>
    <span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">img_path</span><span class="p">)</span>
    <span class="n">wm</span> <span class="o">=</span> <span class="n">ImageDraw</span><span class="o">.</span><span class="n">Draw</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
    <span class="n">col</span><span class="o">=</span> <span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
    <span class="n">wm</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">pos</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">col</span><span class="p">)</span>
    <span class="n">img</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
    <span class="n">img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">res_path</span><span class="p">)</span>
<span class="n">img</span> <span class="o">=</span> <span class="s1">'initial.jpg'</span>
<span class="n">watermark_img</span><span class="p">(</span><span class="n">img</span><span class="p">,</span> <span class="s1">'result.jpg'</span><span class="p">,</span><span class="s1">'IshaanGupta'</span><span class="p">,</span> <span class="n">pos</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
</span></code></pre></div><p data-pid="o6hdAgPN">上面介绍了10个场景，都是日常工作和生活中经常会遇到的。之前大多数同学都会选择寻求一些繁琐的工具，甚至付费，最终效果也不太理想。</p><p data-pid="4QFN0jgK">通过简单的Python脚本，其实就可以彻底解决我们的问题，还可以解放双手，大大的提高效率，感兴趣的赶紧试一下吧！</p><p data-pid="Su-UfXo-">最后，欢迎大家添加<b>vx：code_7steps</b>和我进行技术交流！</p><hr><h2>更多优秀内容</h2><a data-draft-node="block" data-draft-type="link-card" href="https://www.zhihu.com/answer/2488881745" data-image="https://pica.zhimg.com/v2-785568cda65cee6919453010d196d4fd_720w.jpg?source=b1748391" data-image-width="1920" data-image-height="1020" class="internal">大家都是怎么自学Python爬虫的呢？</a><p><br></p><a data-draft-node="block" data-draft-type="link-card" href="https://www.zhihu.com/answer/2414985932" class="internal">python中self与__init__怎么解释能让小白弄懂？</a><p><br></p><a data-draft-node="block" data-draft-type="link-card" href="https://www.zhihu.com/answer/2512274830" data-image="https://pic3.zhimg.com/v2-f91904c8f51ca5e71b057d5eac070734_720w.jpg?source=b1748391" data-image-width="1233" data-image-height="778" class="internal">如何最简单、通俗地理解Python的面向对象？</a><p></p>  
</div>
            