
---
title: '20分钟用原生JavaScript实现键盘打击乐'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4734'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 05:52:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=4734'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">01 - JavaScript Drum Kit</h1>
<blockquote>
<p><a href="https://javascript30.com/" target="_blank" rel="nofollow noopener noreferrer">JavaScript 30</a> 是由 WES BOS 制作的纯 JavaScript 教学，在该教程中一共会实现30个案例。本文用于记录在 DEMO 制作过程中遇到的问题以及思考。本文首发于<a href="https://github.com/aki-yuan/Blog/issues/2" target="_blank" rel="nofollow noopener noreferrer">个人博客</a>，Enjoy Reading！</p>
</blockquote>
<h2 data-id="heading-1">需求</h2>
<p>键盘按下后，播放出对应按键的声音，并且在页面上的按钮显示一个简单的特效。</p>
<p><a href="https://aki-yuan.github.io/Blog/JavaScript30/01%20-%20JavaScript%20Drum%20Kit/index-FINISH.html" target="_blank" rel="nofollow noopener noreferrer">在线 DEMO</a><br><a href="https://github.com/aki-yuan/Blog/tree/main/JavaScript30/01%20-%20JavaScript%20Drum%20Kit" target="_blank" rel="nofollow noopener noreferrer">源码</a></p>
<h2 data-id="heading-2">步骤</h2>
<h3 data-id="heading-3">Step1: 监听键盘事件</h3>
<p>为了让网页在全局下监听键盘，使用 <code>window.addEventListener('keydown', function()&#123;&#125;)</code>。</p>
<p><strong>补充：keydown和keypress的区别</strong></p>
<ul>
<li><code>keydown</code> 会被所有按键触发，但是 <code>keypress</code> 只会被能生成字符值的按键触发。例如：方向键能触发<code>keydown</code>，但是不能触发<code>keypress</code>。</li>
<li><code>keydown</code> 的 event keycode 来说明是哪个按键触发了事件，而 <code>keypress</code> 提供的 keycode 只会说明触发事件是哪个字符。例如：当键盘按下 <code>a</code>，<code>keyboard</code> 会报告 <code>65</code>，而 <code>keypress</code> 会报告 <code>97</code>。值得注意的是，<code>A</code> 在任何的事件中都会报告为<code>65</code>。</li>
</ul>
<h3 data-id="heading-4">Step2: 创建播放函数</h3>
<ol>
<li>利用 <code>keyCode</code> 和 <code>data-key[]</code> 判断按键对应的音频以及div元素。</li>
<li>使对应的div元素添加上 <code>playing</code> 的样式。</li>
<li>将 <code>audio</code> 的播放时间设为0，确保每次播放前音频从头开始。</li>
<li>播放音频。</li>
</ol>
<p><strong>补充1：audio其他常用的属性及方法</strong></p>
<ol>
<li>属性
<ul>
<li>autoplay：布尔值属性；声明该属性，音频会尽快自动播放，不会等待整个音频文件下载完成。</li>
<li>controls：如果声明了该属性，浏览器将提供一个包含声音，播放进度，播放暂停的控制面板，让用户可以控制音频的播放。</li>
<li>loop：布尔属性；如果声明该属性，将循环播放音频。</li>
</ul>
</li>
<li>方法
<ul>
<li>pause：暂停播放。</li>
</ul>
</li>
</ol>
<p><strong>补充2：classList</strong></p>
<ul>
<li>
<p>相比于之前用 js 操控 CSS，例如：</p>
<p><code>document.style.background="red";</code></p>
<p><code>document.style.fontSize="24";</code></p>
<p>相当于【元素的样式被改变了两次】，可能会导致回流和重绘，降低JavaScript性能。</p>
</li>
<li>
<p>必要的时候可以使用 list 列表的形式，例如：</p>
<p><code>document.getElementById("myDIV").classList.add("mystyle");</code></p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">playSound</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">const</span> audio = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">`audio[data-key="<span class="hljs-subst">$&#123;e.keyCode&#125;</span>"]`</span>);
    <span class="hljs-keyword">const</span> key = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">`div[data-key="<span class="hljs-subst">$&#123;e.keyCode&#125;</span>"]`</span>);
    <span class="hljs-keyword">if</span> (!audio) <span class="hljs-keyword">return</span>;

    key.classList.add(<span class="hljs-string">'playing'</span>);
    audio.currentTime = <span class="hljs-number">0</span>;
    audio.play();
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.playing</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.1</span>);
  <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#ffc600</span>;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">1rem</span> <span class="hljs-number">#ffc600</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Step3: 监听transitione结束事件</h3>
<ol>
<li>获取所有包含 <code>className=key</code> 的元素。</li>
<li>当该元件触发特效并结束时触发函数。</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> key = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'.key'</span>));
key.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> key.addEventListener(<span class="hljs-string">'transitionend'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>补充：ArrayForm</strong></p>
<ul>
<li><code>document.querySelectorAll()</code> 获取到的元素是<code>NodeList</code>，虽然 <code>NodeList</code> 不是 <code>Array</code> ，但仍然可以使用 <code>forEach</code> 进行迭代，不过老旧的浏览器较为过时，没有实现 <code>NodeList.forEach()</code> 。可以使用 <code>Array.prototype.forEach()</code> 或 <code>Array.form()</code> 来规避这一问题。</li>
</ul>
<h3 data-id="heading-6">Step4: 创建removeTransition函数</h3>
<ol>
<li>判断传入事件的 <code>peopertyName</code> 是否为 <code>transform</code>，若否则退出。</li>
<li>若为 <code>transform</code>，则移除 <code>playing</code> 样式。</li>
</ol>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeTransition</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(e.propertyName !== <span class="hljs-string">'transform'</span>) <span class="hljs-keyword">return</span>;
  e.target.classList.remove(<span class="hljs-string">'playing'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">思考</h2>
<p>在原案例中使用了CSS的排版语法：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.keys</span> &#123;
    <span class="hljs-attribute">display</span>: flex; <span class="hljs-comment">/* 使用flex要现在元素内声明flex */</span>
    <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>; <span class="hljs-comment">/* 简写，全称为flex: flex-grow｜flex-shrink｜flex-basis*/</span>
    <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>; <span class="hljs-comment">/* vh代表view height, 百分比呈现 */</span>
    <span class="hljs-attribute">align-items</span>: center; <span class="hljs-comment">/* 声明为flex后才有效的属性，垂直居中 */</span>
    <span class="hljs-attribute">justify-content</span>: center;<span class="hljs-comment">/* 声明为flex后才有效的属性，水平居中 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">参阅</h2>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/Document/keydown_event" target="_blank" rel="nofollow noopener noreferrer">Document: keydown event - WebAPIs | MDN</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio" target="_blank" rel="nofollow noopener noreferrer"><audio> - HTML | MDN</a></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/NodeList" target="_blank" rel="nofollow noopener noreferrer">NodeList - Web APIs | MDN</a></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/Element/classList" target="_blank" rel="nofollow noopener noreferrer">Element.classList - Web APIs | MDN</a></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex" target="_blank" rel="nofollow noopener noreferrer">flex - CSS: Cascading Style Sheets | MDN</a></p>
<p><a href="https://guahsu.io/2017/05/JavaScript30-01-Java-Script-Drum-Kit/" target="_blank" rel="nofollow noopener noreferrer">JS30紀錄＆心得 | Gua's Note</a></p>
<p><a href="https://github.com/a90100/JavaScript30/tree/master/01%20-%20JavaScript%20Drum%20Kit" target="_blank" rel="nofollow noopener noreferrer">JavaScript30 | a90100</a></p>
<p>在文章的最后，感谢 <code>WES BOS</code> 等国内外大佬将优秀作品开源，让学习的门槛变得更低，enjoy Coding!</p></div>  
</div>
            