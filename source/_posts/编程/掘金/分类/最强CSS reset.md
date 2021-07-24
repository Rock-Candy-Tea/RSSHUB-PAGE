
---
title: '最强CSS reset'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6590'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 21:54:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=6590'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-comment">/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/</span>

<span class="hljs-selector-tag">html</span>, <span class="hljs-selector-tag">body</span>, <span class="hljs-selector-tag">div</span>, <span class="hljs-selector-tag">span</span>, applet, <span class="hljs-selector-tag">object</span>, <span class="hljs-selector-tag">iframe</span>,
<span class="hljs-selector-tag">h1</span>, <span class="hljs-selector-tag">h2</span>, <span class="hljs-selector-tag">h3</span>, <span class="hljs-selector-tag">h4</span>, <span class="hljs-selector-tag">h5</span>, <span class="hljs-selector-tag">h6</span>, <span class="hljs-selector-tag">p</span>, <span class="hljs-selector-tag">blockquote</span>, pre,
<span class="hljs-selector-tag">a</span>, <span class="hljs-selector-tag">abbr</span>, acronym, <span class="hljs-selector-tag">address</span>, big, <span class="hljs-selector-tag">cite</span>, <span class="hljs-selector-tag">code</span>,
<span class="hljs-selector-tag">del</span>, <span class="hljs-selector-tag">dfn</span>, <span class="hljs-selector-tag">em</span>, <span class="hljs-selector-tag">img</span>, <span class="hljs-selector-tag">ins</span>, <span class="hljs-selector-tag">kbd</span>, <span class="hljs-selector-tag">q</span>, s, <span class="hljs-selector-tag">samp</span>,
small, strike, <span class="hljs-selector-tag">strong</span>, sub, <span class="hljs-selector-tag">sup</span>, tt, <span class="hljs-selector-tag">var</span>,
<span class="hljs-selector-tag">b</span>, u, <span class="hljs-selector-tag">i</span>, center,
<span class="hljs-selector-tag">dl</span>, <span class="hljs-selector-tag">dt</span>, <span class="hljs-selector-tag">dd</span>, <span class="hljs-selector-tag">ol</span>, <span class="hljs-selector-tag">ul</span>, <span class="hljs-selector-tag">li</span>,
<span class="hljs-selector-tag">fieldset</span>, <span class="hljs-selector-tag">form</span>, <span class="hljs-selector-tag">label</span>, <span class="hljs-selector-tag">legend</span>,
<span class="hljs-selector-tag">table</span>, <span class="hljs-selector-tag">caption</span>, <span class="hljs-selector-tag">tbody</span>, <span class="hljs-selector-tag">tfoot</span>, <span class="hljs-selector-tag">thead</span>, <span class="hljs-selector-tag">tr</span>, <span class="hljs-selector-tag">th</span>, <span class="hljs-selector-tag">td</span>,
<span class="hljs-selector-tag">article</span>, <span class="hljs-selector-tag">aside</span>, <span class="hljs-selector-tag">canvas</span>, <span class="hljs-selector-tag">details</span>, embed, 
<span class="hljs-selector-tag">figure</span>, <span class="hljs-selector-tag">figcaption</span>, <span class="hljs-selector-tag">footer</span>, <span class="hljs-selector-tag">header</span>, <span class="hljs-selector-tag">hgroup</span>, 
<span class="hljs-selector-tag">menu</span>, <span class="hljs-selector-tag">nav</span>, output, ruby, <span class="hljs-selector-tag">section</span>, <span class="hljs-selector-tag">summary</span>,
<span class="hljs-selector-tag">time</span>, <span class="hljs-selector-tag">mark</span>, <span class="hljs-selector-tag">audio</span>, <span class="hljs-selector-tag">video</span> &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">font</span>: inherit;
<span class="hljs-attribute">vertical-align</span>: baseline;
&#125;
<span class="hljs-comment">/* HTML5 display-role reset for older browsers */</span>
<span class="hljs-selector-tag">article</span>, <span class="hljs-selector-tag">aside</span>, <span class="hljs-selector-tag">details</span>, <span class="hljs-selector-tag">figcaption</span>, <span class="hljs-selector-tag">figure</span>, 
<span class="hljs-selector-tag">footer</span>, <span class="hljs-selector-tag">header</span>, <span class="hljs-selector-tag">hgroup</span>, <span class="hljs-selector-tag">menu</span>, <span class="hljs-selector-tag">nav</span>, <span class="hljs-selector-tag">section</span> &#123;
<span class="hljs-attribute">display</span>: block;
&#125;
<span class="hljs-selector-tag">body</span> &#123;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-tag">ol</span>, <span class="hljs-selector-tag">ul</span> &#123;
<span class="hljs-attribute">list-style</span>: none;
&#125;
<span class="hljs-selector-tag">blockquote</span>, <span class="hljs-selector-tag">q</span> &#123;
<span class="hljs-attribute">quotes</span>: none;
&#125;
<span class="hljs-selector-tag">blockquote</span>:before, blockquote:after,
q:before, q:after &#123;
content: <span class="hljs-string">''</span>;
<span class="hljs-attribute">content</span>: none;
&#125;
<span class="hljs-selector-tag">table</span> &#123;
<span class="hljs-attribute">border-collapse</span>: collapse;
<span class="hljs-attribute">border-spacing</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码片断来自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmeyerweb.com%2Feric%2Ftools%2Fcss%2Freset%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://meyerweb.com/eric/tools/css/reset/" ref="nofollow noopener noreferrer">Eric Meyer的主页</a>。</p>
<p>原文发布在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F95ce69699492" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/95ce69699492" ref="nofollow noopener noreferrer">个人的简书主页</a>，自己转载自己。</p></div>  
</div>
            