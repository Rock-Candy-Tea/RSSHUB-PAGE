
---
title: 'CSS 字体属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=754'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 05:43:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=754'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>css fonts(字体)属性用于定义字体系列，大小，粗细，和文字样式(如斜体)</p>
<h3 data-id="heading-0">字体系列</h3>
<p>css 使用font-family属性定义文本的字体系列</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123; <span class="hljs-attribute">font-family</span>:<span class="hljs-string">"微软雅黑"</span>; &#125;
<span class="hljs-selector-tag">div</span> &#123; <span class="hljs-attribute">font-family</span>:Arial,<span class="hljs-string">"Microsoft Yahei"</span>,<span class="hljs-string">"微软雅黑"</span>; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>各种字体之间必须使用英文状态下的逗号隔开</li>
<li>一般情况下，如果有空格隔开的多个单词组成的字体，加引号</li>
<li>尽量使用系统默认自带字体，保证在任何用户的浏览器中都能正确显示</li>
<li>最常见的几个字体:body&#123;font-family:'Microsoft Yahei',tahoma,arial,'Hiragino Sans GB';&#125;</li>
</ul>
<blockquote>
<p>如果写有三种字体，第一种找不到用第二种，第二种找不到第三种</p>
</blockquote>
<h3 data-id="heading-1">字体大小</h3>
<p>css 使用font-size属性定义字体大小</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>px(像素)大小是我们网页的最常用的单位</li>
<li>谷歌浏览器默认的文字大小为16px;</li>
<li>不用浏览器可能默认显示的字号大小不一致，我们尽量给一个明确值大小，不要默认大小</li>
<li>可以给body指定整个页面文字的大小</li>
</ul>
<blockquote>
<p>标题标签比较特殊，需要单独指定文字大小</p>
</blockquote>
<h3 data-id="heading-2">字体粗细</h3>
<p>css 使用gont-weight属性设置文本字体的粗细</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">font-weight</span>:bold;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>font-weight：normal | bold | bolder | lighter | </p>
</blockquote>





























<table><thead><tr><th>属性值</th><th align="left">描述值</th></tr></thead><tbody><tr><td>normal：</td><td align="left">正常的字体。相当于数字值400</td></tr><tr><td>bold</td><td align="left">粗体。相当于数字值700。</td></tr><tr><td>bolder</td><td align="left">定义比继承值更重的值</td></tr><tr><td>lighter</td><td align="left">定义比继承值更轻的值</td></tr><tr><td>integer</td><td align="left">用数字表示文本字体粗细。取值范围：100,200,300,400,500,600,700,800,900</td></tr></tbody></table>
<ul>
<li>学会让加粗标签(比如h和strong等)不加粗，或者其他标签加粗</li>
<li>实际开发时，我们更喜欢用数字表示粗细</li>
</ul>
<h3 data-id="heading-3">文字样式</h3>
<p>css 使用font-style 属性设置文本的风格</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">font-style</span>:normal;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th>属性值</th><th align="left">解释</th></tr></thead><tbody><tr><td>normal</td><td align="left">指定文本字体样式为正常的字体</td></tr><tr><td>italic</td><td align="left">指定文本字体样式为斜体。对于没有设计斜体的特殊字体，如果要使用斜体外观将应用oblique</td></tr><tr><td>oblique</td><td align="left">指定文本字体样式为倾斜的字体。人为的使文字倾斜，而不是去选取字体中的斜体字</td></tr></tbody></table>
<blockquote>
<p>注意：平时我们很少给文字加斜体，反而要给斜体标签(em,i)改为不倾斜字体</p>
</blockquote>
<h3 data-id="heading-4">字体复合属性</h3>
<p>字体属性可以把以上文字样式综合来写，这样可以更节约代码</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
<span class="hljs-attribute">font</span>: font-style font-weight font-size/line-height font-family; 
&#125;

<span class="hljs-selector-tag">p</span> &#123;
           <span class="hljs-attribute">font</span>:italic <span class="hljs-number">800</span> <span class="hljs-number">5px</span> <span class="hljs-string">"宋体"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用font属性时，必须按上面的语法格式中的顺序书写，不能更换顺序，并且各个属性间以空格隔开</li>
<li>不需要设置的属性可以省略(取默认值)，但必须保留font-size和font-family属性，否则font属性将不起作用</li>
</ul></div>  
</div>
            