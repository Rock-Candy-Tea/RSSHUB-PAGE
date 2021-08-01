
---
title: '阿ken的HTML、CSS的入门指南_CSS3选择器（笔记四）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img-blog.csdnimg.cn/20201009164220418.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 18:02:06 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20201009164220418.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>感激相遇 你好 我是阿ken</strong></p>
<p><strong>文章部分内容及图片出自网络，如有问题请与我本人联系(主页有公众号)</strong></p>
<p><strong>本博客暂适用于刚刚接触HTML以及好久不看想要复习的小伙伴</strong></p>
<p><img src="https://img-blog.csdnimg.cn/20201009164220418.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>虽还未踏入社会尚处象牙塔内<br>
却总总陷入迷茫不知所措<br>
有时很渴望有一个信仰能够成为我的精神支柱促使我一路坚持走下去<br>
但苦于一直未果<br>
后来短暂接触了一下这社会环境<br>
也看到了一些很有意思的灵魂<br>
他们大多有趣且人心善良<br>
但却也被生活折腾的一塌糊涂<br>
这好像让我看到了如果再一直浑浑噩噩下去五年十年后自己的影子<br>
稍微明白一点儿父亲的苦<br>
… …<br>
没有人在年少时想要成为一个普通人</strong></p>
<p><strong>下面我们开始步入正题</strong></p>
<h1 data-id="heading-0"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4  CSS选择器</h1>
<h2 data-id="heading-1"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.1  引入CSS样式表</h2>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. <strong>行内式</strong></h3>
<pre><code class="hljs language-html copyable" lang="html"><标记名 style="属性1:属性值1; 属性2:属性值2; 属性3:属性值3;">内容</标记名>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>style</code>是标记的属性</p>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. <strong>内嵌式</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><head>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

选择器&#123;
属性<span class="hljs-number">1</span>:属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>:属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>:属性值<span class="hljs-number">3</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
</head>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此方式放在<code>head</code>标签里</p>
<h3 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>3. <strong>链入式</strong></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><head>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"css文件的路径"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>/></span></span>
</head>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong></p>
<ul>
<li><code>href</code>：可以<strong>是所链接外部样式表的URL，也可以是相对路径或绝对路径</strong>。</li>
<li><code>type</code>：<strong>定义所链接文档的类型</strong>，在这里需要指定为“<code>text/css</code>”，表示链接的外部文件为<code>CSS</code>样式表。</li>
<li><code>rel</code>：<strong>定义当前的文档与被链接文档之间的关系</strong>，在这里需要指定为“<code>stylesheet</code>”，表示被链接的文档是一个样式表文件。</li>
</ul>
<blockquote>
<p>链入式最大的好处是<strong>同一个<code>CSS</code>样式表可以被不同的<code>HTML</code>页面链接使用， 同时一个<code>HTML</code>页面也可以通过多个<code><link></code>标记链接多个<code>CSS</code>样式表。</strong></p>
</blockquote>
<blockquote>
<p>链入式是使用频率最高，也是最实用的CSS样式表，<br>
实现了结构和表现的完全分离，<strong>使得页面的前期制作和后期维护都十分方便。</strong></p>
</blockquote>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.2  CSS选择器样式规则</h2>
<pre><code class="hljs language-css copyable" lang="css">选择器 &#123;
属性<span class="hljs-number">1</span>: 属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>: 属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>: 属性值<span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>选择器用来指定<code>CSS</code>样式作用的HTML对象<br>
大括号内是对该对象设置的具体样式</strong><br>
其中属性和属性值以“键值对”的形式出现<br>
属性和属性值之间用英文“:”连接 ， “键值对”之间用英文“;”连接</p>
<p><strong>注意:</strong></p>
<ol>
<li><strong><code>HTML5</code>标签不严格区分大小写</strong>（<code><p></P></code>都一样），但是**<code>CSS</code>样式中的选择器严格区分大小写，属性和值不区分大小写，按照书写习惯一般将“选择器、属性和值”都采用小写的形式。**</li>
<li><strong>如果属性的值由多个单词组成且中间包含空格，则必须为这个属性值加上英文状态下的引号。</strong></li>
<li><strong><code>CSS</code>代码中空格是不被解析的，花括号及分号前后的空格可有可无。因此可以使用空格键、<code>Tab</code>键、回车键等对样式及进行排版，以增加代码的可读性。</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">h1</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20</span> px;
&#125;  // <span class="hljs-number">20</span>和单位px之间有空格
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上述代码_注意：<strong>属性的值和单位之间是不允许出现空格</strong>的，否则浏览器解析时会出错。</p>
<ol start="4">
<li><strong>多个"属性: 属性值"之间必须用英文分号";"隔开</strong>，最后一个”属性: 属性值“之后可以省略，但加上有利于增加代码可读性以及便于增加新”属性: 属性值“。<br>
为了提高代码可读性，建议增加注释。</li>
</ol>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3  CSS选择器</h2>
<p>要想将CSS样式应用于特定的HTML元素，首先需要找到该目标元素。<br>
在CSS中，执行这一任务的样式规则部分被称为选择器。</p>
<h3 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.1  标记选择器</h3>
<p>标记选择器是指用<code>HTML</code>标记名作为选择器</p>
<pre><code class="hljs language-css copyable" lang="css">标记名 &#123;
属性<span class="hljs-number">1</span>: 属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>: 属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>: 属性值<span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>; 
<span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>; 
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.2  类选择器</h3>
<p><strong>类选择器使用“ . ”进行标识</strong>，后面紧跟类名。</p>
<pre><code class="hljs language-css copyable" lang="css">.类名 &#123;
属性<span class="hljs-number">1</span>: 属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>: 属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>: 属性值<span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>class</code>属性和<code>id</code>选择器类似，只不过<code>class</code>属性可以定义多个属性</strong><br>
拥有相同<code>class</code>属性值的元素，我们可以说它们是一类元素<br>
也<strong>可以同时为一个元素设置多个<code>class</code>属性值，多个值之间使用空格隔开</strong></p>
<p><strong>实例：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>类选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.red</span> &#123;
<span class="hljs-attribute">color</span>: red;
&#125;
                           
<span class="hljs-selector-class">.green</span> &#123;
<span class="hljs-attribute">color</span>: green;
&#125;
                       
<span class="hljs-selector-class">.font22</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">22px</span>;
&#125;     <span class="hljs-comment">/* class后带有font22的  字体像素22 */</span>

<span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">text-decoration</span>: underline;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;           
<span class="hljs-comment">/* 所有p标签内字体:  微软雅黑+下划线 */</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"red"</span>></span>二级标题文本<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>          
<span class="hljs-comment"><!-- 红色 --></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"green font22"</span>></span>段落一文本内容<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 
<span class="hljs-comment"><!-- 字体:绿色+像素22+微软雅黑+下划线 --></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"red font22"</span>></span>段落二文本内容<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   
<span class="hljs-comment"><!-- 字体:红色+像素22+微软雅黑+下划线 --></span>

<span class="hljs-tag"><<span class="hljs-name">P</span>></span>段落三文本内容<span class="hljs-tag"></<span class="hljs-name">p</span>></span>                      
<span class="hljs-comment"><!-- 字体:微软雅黑+下划线 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201117141426679.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见多个标记可以使用同一个类名，这样可以实现不同类型的标记指定相同的样式。<br>
同时一个<code>HTML</code>元素也可以应用多个<code>class</code>类来设置多个样式，在<code>HTML</code>标签中多个类名之间需要用空格隔开，如上述代码中的<code>green font22、red font22</code> 。</p>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.3  id选择器</h3>
<p>通过元素的 id 属性值选中 <strong>唯一</strong> 的一个元素<br>
<strong>记住是选中属性值中唯一的元素</strong><br>
基本语法格式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#id</span>名 &#123;
属性<span class="hljs-number">1</span>: 属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>: 属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>: 属性值<span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>id选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-id">#bold</span> &#123;
<span class="hljs-attribute">font-weight</span>: bold;
&#125;

<span class="hljs-selector-id">#font24</span> &#123;
<span class="hljs-attribute">font-size</span>:<span class="hljs-number">24px</span>;
&#125;

<span class="hljs-selector-id">#bold</span><span class="hljs-selector-id">#font24</span> &#123;
<span class="hljs-attribute">font-weight</span>: bold;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bold"</span>></span>段落1:id="bold",设置粗体文字。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>       <span class="hljs-comment"><!-- 粗体文字 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"font24"</span>></span>段落1:id="font24",设置字号为24px。<span class="hljs-tag"></<span class="hljs-name">p</span>></span> <span class="hljs-comment"><!-- 字号为24px --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"font24"</span>></span>段落1:id="font24",设置字号为24px。<span class="hljs-tag"></<span class="hljs-name">p</span>></span> <span class="hljs-comment"><!-- 字号为24px --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bold font24"</span>></span>段落1:id="bold font24",同时设置粗体和字号为24px。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 无变化 --></span>                     

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201117142051595.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第四行代码即id = "bold font24"这样的写法是错误的，id 选择器并不支持像类选择器那样定义多个值。</p>
<h3 data-id="heading-10"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.4  通配符选择器</h3>
<p><strong>通配符选择器用“ * ”号表示</strong>，能匹配页面中所有的元素\</p>
<p>基本语法格式：</p>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
属性<span class="hljs-number">1</span>: 属性值<span class="hljs-number">1</span>;
属性<span class="hljs-number">2</span>: 属性值<span class="hljs-number">2</span>;
属性<span class="hljs-number">3</span>: 属性值<span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实际网页开发中不建议使用通配符选择器，因为它设置的样式对所有的HTML标记都生效，不管标记是否需要样式，这样反而降低了代码的执行速度。</p>
<h3 data-id="heading-11"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.5  标签指定式选择器(交集选择器)</h3>
<p><strong>又称交集选择器，由两个选择器构成，其中第一个为标记选择器，第二个为<code>class</code>选择器或<code>id</code>选择器，两个选择器之间不能有空格，如<code>h3.special</code>或<code>p#one</code></strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>标签指定式选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">color</span>: blue;
&#125;   <span class="hljs-comment">/*指定下方body标签的第一行文字颜色为蓝色*/</span>

<span class="hljs-selector-class">.special</span> &#123;
<span class="hljs-attribute">color</span>: green;
&#125;                   <span class="hljs-comment">/*指定下方body标签的第三行文字颜色为绿色*/</span>

<span class="hljs-selector-tag">p</span><span class="hljs-selector-class">.special</span> &#123;
<span class="hljs-attribute">color</span>: red;
&#125;<span class="hljs-comment">/*标签指定式选择器*/</span>  <span class="hljs-comment">/*指定下方body标签的第二行文字颜色为红色*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>普通段落文本（蓝色）<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"special"</span>></span>指定了.special类的段落文本（红色）<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"special"</span>></span>指定了.special类的段落文本（绿色）<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>    
               
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117142610373.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.6  后代选择器(和子元素)</h3>
<p>元素之间的关系<br>
父元素：直接包含子元素的元素<br>
子元素：直接被父元素包含的元素<br>
祖先元素：直接或间接包含后代元素的元素，父元素也是祖先元素<br>
后代元素：直接或间接包含祖先元素的元素\</p>
<p><strong>后代元素选择器<br>
作用：<br>
选中指定元素的指定后代元素</strong></p>
<p><strong>语法：<br>
祖先元素 后代元素&#123; &#125;</strong></p>
<p><strong>子元素选择器</strong><br>
作用：选中指定父元素的指定子元素<br>
语法：父元素 > 子元素&#123; &#125;<br>
<strong>后面 9. 关系选择器中会讲到</strong></p>
<p>该选择器用来选择元素或元素组的后代，其<strong>写法就是把外层标记写在前面，内层标记写在后面，中间用空格分隔</strong>。当标记发生嵌套时，内层标记就成为外层标记的后代。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>后代选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span> <span class="hljs-selector-tag">strong</span> &#123;
<span class="hljs-attribute">color</span>: red;
&#125; <span class="hljs-comment">/*后代选择器*/</span>     <span class="hljs-comment">/* 指定的是body标签第一行文字颜色为红色 */</span>

<span class="hljs-selector-tag">strong</span> &#123;
<span class="hljs-attribute">color</span>: blue;
&#125;                    <span class="hljs-comment">/* 指定的是body标签第二行文字颜色为蓝色 */</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>段落文本<span class="hljs-tag"><<span class="hljs-name">strong</span>></span>嵌套在段落中，使用strong标记定义的文本（红色）<span class="hljs-tag"></<span class="hljs-name">strong</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">strong</span>></span>嵌套之外由strong标记定义的文本（蓝色）。<span class="hljs-tag"></<span class="hljs-name">strong</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20201117142931562.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.7  并集选择器</h3>
<p><strong>并集选择器又叫复合选择器</strong><br>
可以选中同时满足多个选择器的元素<br>
并集选择器是各个选择器通过<strong>逗号</strong>连接而成</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>并集选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span> = <span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">h2</span>,<span class="hljs-selector-tag">h3</span>,<span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">color</span>: red;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125; <span class="hljs-comment">/*不同标记组成的并集选择器*/</span>

<span class="hljs-selector-tag">h3</span>,<span class="hljs-selector-class">.special</span>,<span class="hljs-selector-id">#one</span> &#123;
<span class="hljs-attribute">text-decoration</span>: underline;   
&#125;  <span class="hljs-comment">/* 加下划线 */</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>二级标题文本<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>                           <span class="hljs-comment"><!--字体14像素、红色--></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>三级标题文本<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>                           <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"special"</span>></span>段落文本1,加下划线。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>      <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>段落文本2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>                               <span class="hljs-comment"><!--字体14像素、红色--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span>></span>段落文本3<span class="hljs-tag"></<span class="hljs-name">p</span>></span>                      <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117143115248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码字号和颜色相同，只是有一个标题和两个段落文本有下划线效果（上述已注明）。</p>
<h3 data-id="heading-14"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.8  属性选择器</h3>
<ol>
<li><strong>E[att^=value] 属性选择器</strong></li>
</ol>
<p>E[att^=value]属性选择器是指选择名称为E的标记，且该标记定义了 att 属性，att 属性值包含<strong>前缀</strong>为 value 的子字符串。</p>
<p>需要注意的是<strong>E是可以省略的</strong>，<strong>如果省略则表示可以匹配满足条件的任意元素</strong>。\</p>
<p>例如：<code>div\[id^=section]</code>表示匹配包含<code>id</code>属性，且<code>id</code>属性值是以“<code>section</code>”字符串<strong>开头</strong>的<code>div</code>元素。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att^=value] 属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id^=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117143521332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了E[att^=value]属性选择器 “ p[id ^=“one”] ” 。<br>
只要p元素中的 id 属性值是<strong>以“ one ”字符串开头就会被选中</strong>，从而呈现特殊的文本效果。</p>
<ol start="2">
<li><strong>E[att$=value] 属性选择器</strong></li>
</ol>
<p>E[att$=value] 属性选择器是指选择名称为E的标记，且该标记定义了<code>att</code>属性，<code>att</code>属性值包含<strong>后缀</strong>为<code>value</code>的子字符串。</p>
<p><strong>E是可以省略的，如果省略则表示可以匹配满足条件的任意元素</strong>。</p>
<p>例如：<code>div[id$=section]</code>表示匹配包含 id 属性，且<code>id</code>属性值是以“<code>section</code>”字符串<strong>结尾</strong>的<code>div</code>元素。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att$=value]属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id$=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"1one"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/2020111714433132.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了E[att$=value]属性选择器 “ p[id $=“one”] ” 。<br>
只要p元素中的 id 属性值是<strong>以“ one ”字符串结尾就会被选中</strong>，从而呈现特殊的文本效果。</p>
<ol start="3">
<li><strong>E[att*=value] 属性选择器</strong></li>
</ol>
<p><code>E[att*=value]</code>属性选择器是指选择名称为E的标记，且该标记定义了<code>att</code>属性，<strong><code>att</code>属性值包含<code>value</code>的子字符串。</strong></p>
<p><strong>E是可以省略的，如果省略则表示可以匹配满足条件的任意元素</strong>。</p>
<p>例如：<code>div[id*=section]</code>表示匹配包含<code>id</code>属性，且 id 属性值<strong>包含“<code>section</code>”字符串</strong>的<code>div</code>元素。</p>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att*=value]属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id*=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"1one"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117144550175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了<code>E[att*=value]</code>属性选择器 “<code>p[id*=“one”]</code>” 。<br>
只要<code>p</code>元素中的<code>id</code>属性值是<strong>包含“<code>one</code>”字符串就会被选中</strong>，从而呈现特殊的文本效果。</p>
<h3 data-id="heading-15"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.9  关系选择器</h3>
<p><strong>关系选择器主要包括子代选择器和兄弟选择器</strong>，其中子代选择器由符号“>”连接，兄弟选择器由符号“+”和“~”连接。</p>
<ol>
<li><strong>子代选择器（>）</strong></li>
</ol>
<p><strong>子代选择器主要用来选择某个元素的第一级子元素。<br>
例如希望选择只作用于<code>h1</code>元素子元素的<code>strong</code>元素，可以这样写：<code>h1 > strong</code>。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>子代选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">h1</span>><span class="hljs-selector-tag">strong</span> &#123;
<span class="hljs-attribute">color</span>: red;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>心怀梦想，<span class="hljs-tag"><<span class="hljs-name">strong</span>></span>不丢信仰<span class="hljs-tag"></<span class="hljs-name">strong</span>></span><span class="hljs-tag"></<span class="hljs-name">h1</span>></span>          <span class="hljs-comment"><!-- （1） --></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span><span class="hljs-tag"><<span class="hljs-name">em</span>></span><span class="hljs-tag"><<span class="hljs-name">strong</span>></span>看透疾苦，<span class="hljs-tag"></<span class="hljs-name">strong</span>></span><span class="hljs-tag"></<span class="hljs-name">em</span>></span>深爱人间<span class="hljs-tag"></<span class="hljs-name">h1</span>></span> <span class="hljs-comment"><!-- （2） --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117144838290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，（1）中的<code>strong</code>元素为<code>h1</code>元素中的子元素，（2）中的<code>strong</code>元素为<code>h1</code>元素的孙元素，因此代码中设置的样式只对（1）中代码有效。</p>
<ol start="2">
<li><strong>兄弟选择器（+、~）</strong></li>
</ol>
<p><strong>兄弟选择器用来选择与某元素位于同一个父元素之中，且位于该元素之后的兄弟元素。</strong></p>
<p>兄弟选择器分为临近兄弟选择器和普通兄弟选择器两种。</p>
<ol start="2">
<li><strong>临近兄弟选择器</strong></li>
</ol>
<p><strong>该选择器使用加号“+”来；连接前后两个选择器。</strong><br>
选择器中的<strong>两个元素有同一个父亲</strong>，而且<strong>第二个元素必须紧跟第一个元素</strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>临近兄弟选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span>+<span class="hljs-selector-tag">h2</span> &#123;
<span class="hljs-attribute">color</span>: green;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"宋体"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[唐] 黄巢<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>飒飒西风满院栽，蕊寒香冷蝶难来。<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- （1） --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117145034556.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>临近兄弟选择器应用在（1）<br>
从结构中看出p元素后紧邻的第一个兄弟元素所在位置为（1）</p>
<ol start="3">
<li><strong>普通兄弟选择器</strong></li>
</ol>
<p><strong>普通兄弟选择器使用“~”来链接前后两个选择器。</strong><br>
选择器中的<strong>两个元素有同一个父亲，但第二个元素不必紧跟第一个元素。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>普通兄弟选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span>~<span class="hljs-selector-tag">h2</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"宋体"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[唐] 黄巢<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>飒飒西风满院栽，蕊寒香冷蝶难来。<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- （1） --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- （2） --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117145234242.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>临近兄弟选择器应用在（1）、（2）<br>
从结构中看出p元素后紧邻的第一个兄弟元素所在位置为（1）、（2）</p>
<h3 data-id="heading-16"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.10  :empty 选择器</h3>
<p><strong><code>:empty</code>选择器用来选择没有子元素或文本内容为空的所有元素。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>empty 选择器的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">width</span>:<span class="hljs-number">150px</span>;
<span class="hljs-attribute">height</span>:<span class="hljs-number">30px</span>;
&#125;

<span class="hljs-selector-pseudo">:empty</span> &#123;
<span class="hljs-attribute">background-color</span>: <span class="hljs-number">#999</span>;
&#125;  <span class="hljs-comment">/* (1) */</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">p</span>></span>     
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[唐] 黄巢<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>      <span class="hljs-comment"><!-- (2) --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>飒飒西风满院栽，蕊寒香冷蝶难来。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117150108134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(1) 中代码使用" :empty 选择器 "定义(2)空元素p，将其空元素的背景颜色设置为灰色。</p>
<h3 data-id="heading-17"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.11 :target 选择器</h3>
<p><strong><code>:target</code>选择器用于为页面中的某个<code>target</code>元素（该元素的<code>id</code>被当做页面中的超链接来使用）指定样式。只有用户单击了页面中的超链接，并且跳转到<code>target</code>元素后，<code>:target</code>选择器所设置的样式才会起作用。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>target选择器的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="xml">

:target &#123;
background-color: #e5eece;
&#125;

<span class="hljs-tag"></<span class="hljs-name">sty1e</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这是标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#news1"</span>></span>跳转至内容1<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#news2"</span>></span>跳转至内容2<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>请单击上面的链接,:target选择器会突出显示当前活功的HTML锚。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"news1"</span>></span><span class="hljs-tag"><<span class="hljs-name">b</span>></span>内容 1...<span class="hljs-tag"></<span class="hljs-name">b</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"news2"</span>></span><span class="hljs-tag"><<span class="hljs-name">b</span>></span>内容 2...<span class="hljs-tag"></<span class="hljs-name">b</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">b</span>></span>注释：<span class="hljs-tag"></<span class="hljs-name">b</span>></span> Internet Explorer 8 以及更早的版本不支持 :target 选择器。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201210171333245.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当单击“跳转至内容1”或“跳转至内容2”时，所链接到的内容才会被添加背景颜色效果：
<br></p>
<p><img src="https://img-blog.csdnimg.cn/2020121017140539.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.12  伪类选择器</h3>
<ul>
<li><strong>结构化伪类选择器</strong></li>
</ul>
<ol>
<li><strong>:root 选择器</strong></li>
</ol>
<p><strong>:root 选择器用于匹配文档根元素。</strong><br>
<strong>使用 :root 选择器定义的样式，对所有页面元素都生效，对于不需要该样式的元素，可以单独设置样式进行覆盖。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>:root 选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-pseudo">:root</span> &#123;
<span class="hljs-attribute">color</span>: pink;
&#125;

<span class="hljs-selector-tag">h2</span> &#123;
<span class="hljs-attribute">color</span>: red;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>        //（1）
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[唐] 黄巢  飒飒西风满院栽，蕊寒香冷蝶难来。
他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  //（2）

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117150912244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>开始第一步 :root 选择器 将页面中所有的文本设置为粉色，<br>
第二部将 （1）中元素文字设置为红色</p>
<ol start="2">
<li><strong>:not 选择器</strong></li>
</ol>
<p><strong>如果对某个结构使用样式，但是想排除这个结构元素下面的子结构元素，让它不使用这个样式，可以使用 :not 选择器。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>:not选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">body</span> *<span class="hljs-selector-pseudo">:not</span>(<span class="hljs-selector-tag">h3</span>) &#123; // 格式不能变，只有这样才能成功运行
<span class="hljs-attribute">color</span>: orange;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"宋体"</span>;
&#125;           //(<span class="hljs-number">1</span>)

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>      // 唯独<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>未应用(1)中的文本样式  
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[唐] 黄巢<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>飒飒西风满院栽，蕊寒香冷蝶难来。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201210194949561.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(1) 中定义了页面body的文本样式，" body *: not(h3) " 选择器用于排除 body 结构中的子结构元素 h3，使其不应用该文本样式。</p>
<ul>
<li><strong>拓展参考：</strong><br>
<img src="https://img-blog.csdnimg.cn/20201210195047977.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<ol start="3">
<li><strong>:only-child 选择器</strong></li>
</ol>
<p><strong><code>:only-child</code>选择器用于匹配属于某父元素的唯一子元素的元素，也就是说，如果某个父元素仅有一个子元素，则使用 "<code>:only-child</code>选择器 " 可以选择这个子元素。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>:only-child 选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:only-child</span> &#123;
<span class="hljs-attribute">color</span>:red;
&#125;           <span class="hljs-comment">/* (1) */</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
国内电影：
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>一代宗师<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>叶问<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>非诚勿扰<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
美国电影：
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>侏罗纪世界<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
日本动漫：
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>蜡笔小新<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>火影忍者<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>航海王<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117154723457.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码中使用了<code>:only-child</code>选择器 “<code>li:only-child</code>”，用于选择作为<code>ul</code>唯一子元素的<code>li</code>元素，并设置其文本颜色为红色。</p>
<ol start="4">
<li><strong>:first-child 和 :last-child 选择器</strong></li>
</ol>
<p><strong><code>:first-child</code>选择器和<code>:last-child</code>选择器分别用于为父元素中的第一个或者是最后一个子元素设置样式。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>first-child和last-child选择器的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:first</span>-child&#123;
<span class="hljs-attribute">color</span>:pink;
<span class="hljs-attribute">font-size</span>:<span class="hljs-number">16px</span>;
<span class="hljs-attribute">font-family</span>:<span class="hljs-string">"宋体"</span>;
&#125;

<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:last-child</span>&#123;
<span class="hljs-attribute">color</span>:blue;
<span class="hljs-attribute">font-size</span>:<span class="hljs-number">16px</span>;
<span class="hljs-attribute">font-family</span>:<span class="hljs-string">"微软雅黑"</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>题菊花<span class="hljs-tag"></<span class="hljs-name">p</span>></span>     
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>[ 唐 ] 黄巢<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>飒飒西风满院栽，蕊寒香冷蝶难来。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>他年我若为青帝，报与桃花一处开。<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，分别使用了<code>:first-child</code>选择器和<code>:last-child</code>选择器<br>
前者<code>:first-child</code>选择器能定义，后者<code>:last-child</code>选择器无法定义，<strong>该伪类方法比较繁琐</strong>
<br></p>
<p><img src="https://img-blog.csdnimg.cn/20201210201131796.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>之后会更新一下该类选择器如何正确使用</strong></p>
<ol start="5">
<li><strong>:nth-child(n)和:nth-last-child(n)选择器</strong></li>
</ol>
<p><code>:nth-child(n)</code>和<code>:nth-last-child(n)</code>选择器是用来选择<strong>第n个和倒数第n个子元素</strong>的选择器</p>
<p>案例代码可参考4.3.4，把其中<code>:first-child</code>和<code>:last-child</code>更换成<code>:nth-child(n)</code>和<code>:nth-last-child(n)</code>理解即可。</p>
<ol start="6">
<li><strong>:nth-of-type(n)和:nth-last-of-type(n)选择器</strong></li>
</ol>
<p>:nth-of-type(n)和 :nth-last-of-type(n)选择器 用来匹配属于父元素的<strong>特定类型</strong>的<strong>第n个子元素或倒数第n个</strong>子元素</p>
<p><strong>案例同上解释<br>
之后会特意整理出几篇博客讲解伪类选择器细节</strong></p>
<ul>
<li><strong>伪元素选择器</strong></li>
</ul>
<p>所谓伪元素选择器，是针对CSS中已经定义好的伪元素使用的选择器。<br>
CSS中常用的伪元素选择器有:before伪元素选择器和:after伪元素选择器。</p>
<ol>
<li><strong>:before 选择器</strong></li>
</ol>
<p><strong><code>:before</code>伪元素选择器用于在被选元素的内容前面插入内容，必须配合<code>content</code>属性来指定要插入的具体内容。</strong>\</p>
<p>基本语法格式:</p>
<pre><code class="hljs language-css copyable" lang="css">标签名:before &#123;
content:文字/<span class="hljs-built_in">url</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述语法中，被选元素位于"<code>:before</code>"之前，“&#123; &#125;"中的<code>content</code>属性用来指定要插入的具体内容，该内容既可以为文本也可以为图片。</p>
<p>案例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>before选择器的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span>:before &#123;
content: <span class="hljs-string">"我是"</span>;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#c06</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-weight</span>: bold;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>阿ken啊，<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201210202046330.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用了选择器 "<code>:before</code>"，用于在段落前面添加内容，同时使用<code>content</code>属性来指定添加的具体内容。为了使插入效果更美观，还设置了文本样式。</p>
<ol start="2">
<li><strong>:after 选择器</strong></li>
</ol>
<p><strong><code>:after</code>伪元素选择器用于在某个元素之后插入一些内容</strong>，使用方法与<code>:before</code>选择器相同。<br>
案例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>after选择器的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-comment">/*p:after&#123;content:url(images/tu.jpg);&#125;*/</span>
<span class="hljs-selector-tag">p</span>:after&#123;
content:<span class="hljs-built_in">url</span>(<span class="hljs-string">https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3083554353,73017423&fm=26&gp=0.jpg</span>);
&#125;


</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>十五的月亮<span class="hljs-tag"><<span class="hljs-name">br</span>/></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117160152187.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>链接伪类</li>
</ul>
<p>在CSS中，通过链接伪类可以实现不同的链接状态。</p>
<p>所谓伪类并不是真正意义上的类，它的名称是由系统定义的，通常由标记名、类名或id名加":”构成。</p>
<p>超链接标记< a>的伪类有4种</p>

























<table><thead><tr><th>超链接标记< a>的伪类</th><th>含义</th></tr></thead><tbody><tr><td>a:link&#123; CSS样式规则;&#125;</td><td>未访问时超链接的状态</td></tr><tr><td>a:visited&#123; CSS样式规则: &#125;</td><td>访问后超链接的状态</td></tr><tr><td>a:hover&#123; CSS样式规则; &#125;</td><td>鼠标经过、悬停时超链接的状态</td></tr><tr><td>a:active&#123; CSS样式规则; &#125;</td><td>鼠标单击不动时超链接的状态</td></tr></tbody></table>
<p>案例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>链接伪类<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:link</span>, <span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:visited</span> &#123;    <span class="hljs-comment">/*未访问和访问后 都为粉色*/</span>
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">text-decoration</span>: none;<span class="hljs-comment">/*清除超链接默认的下划线*/</span>
&#125;

<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:hover</span> &#123;            <span class="hljs-comment">/*鼠标悬停 时文字颜色是蓝色*/</span>
<span class="hljs-attribute">color</span>: blue;
<span class="hljs-attribute">text-decoration</span>: underline;<span class="hljs-comment">/*鼠标悬停时出现下划线*/</span>
&#125;

<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:active</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#F00</span>;
&#125;<span class="hljs-comment">/*鼠标单击不动 时为红色*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>公司首页<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>公司简介<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>产品介绍<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>联系我们<span class="hljs-tag"></<span class="hljs-name">a</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>特别注意：</strong><br>
<strong>只有按上述定义中 :link, :visited、 :hover、:active顺序定义，一般 :link, :visited 一起定义，如果不按上述顺序定义，将会按上述中的顺序显示，在 :link, :visited之前和 :active 之后的代码将不运行</strong></li>
</ul>
<blockquote>
<p>在实际工作中，通常只需要使用a:link、a:visited、a:hover定义未访问、访问后和鼠标悬停时的链接样式，并且常常对a:link和a:visited定义相同的样式，使未访问和访向后的链接样式保持一致。</p>
</blockquote>
<br>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fcc833552a748c69ab4c3a3af51a3df~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意:</p>
<p>(1) 同时使用链接的4种伤类时，通常按照a:link、a:visited、a:hover和a:active的顺序书写，否则定义的样式可能不起作用。<br>
(2) 除了文本样式之外，链接伪类还常常用于控制超链接的背景、边框等样式。</p>
<h2 data-id="heading-19"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.4  CSS层叠性和继承性</h2>
<ol>
<li>层叠性<br>
所谓层叠性是指多种<code>CSS</code>样式的叠加</li>
<li>继承性<br>
所谓继承性是指书写<code>CSS</code>样式表时，子标记会继承父标记的某些样式</li>
</ol>
<h2 data-id="heading-20"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.5  CSS优先级</h2>
<p>定义<code>CSS</code>样式时，经常<strong>出现两个或更多规则应用在同一元素上，这时就会出现优先级的问题</strong>。</p>





















<table><thead><tr><th>选择器名称</th><th>权重</th></tr></thead><tbody><tr><td>标记选择器</td><td>1</td></tr><tr><td>类选择器</td><td>10</td></tr><tr><td>id选择器</td><td>100</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html">P strong &#123;color:black;&#125;          /*权重为: 1+1*/
strong.blue &#123;color:green;&#125;       /*权重为: 1+10*/
.father strong &#123;color:yellow;&#125;   /*权重为: 10+1*/
p.father strong &#123;color:orange;&#125;  /*权重为: 1+10+1*/
p.father.blue &#123;color:gold;&#125;      /*权重为: 1+10+10*/
#header strong &#123;color:pink;&#125;     /*权重为: 100+1*/
#header strong.blue &#123;color:red;&#125; /*权重为: 100+1+10*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的<code>HTML</code>结构:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"header"</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">strong</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"blue"</span>></span>文本的颜色<span class="hljs-tag"></<span class="hljs-name">strong</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，页面文本将应用权重最高的样式，即文本颜色为红色。</p>
<p>此外，在考虑权重时，还需要注意些特殊的情况。</p>
<ul>
<li>
<p>继承样式的权重为0，即在嵌套结构中，不管父元素样式的权重多大，被子元素维承时，它的权重都为0，也就是说子元素定义的样式会覆盖继承来的样式。\</p>
<p>继承即子元素继承父元素的相关样式属性，如：</p>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background:red;font-size:12px; "</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>测试一下<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的实例中段落的文字就会继承<code>body</code>的样式</p>
<p>例如下面的<code>CSS</code>样式代码:</p>
<pre><code class="hljs language-html copyable" lang="html">strong&#123;color: red;&#125;
#header&#123;color: green;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的<code>HTML</code>结构为:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"header"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"blue"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">strong</span>></span>继承样式不如自已定义<span class="hljs-tag"></<span class="hljs-name">strong</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，虽然<code>#header</code>具有权重100, 但被<code>strong</code>继承时权重为0，而<code>strong</code>选择器的权重虽然仅为1，但它大于继承样式的权重，所以页面中的文本显示为红色。</p>
<ul>
<li>行内样式优先。应用<code>style</code>属性的元素，其行内样式的权重非常高，可以理解为远大于100。总之，它拥有比上面提到的选择器都大的优先级。</li>
<li><strong>权重相同时，<code>CSS</code>遵循就近原则</strong>。也就是说最靠近元素的样式具有最大的优先级，或者说排在最后的样式优先级最大。<br>
例如:</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*CSS文档，文件名为style.css*/</span>
<span class="hljs-selector-id">#header</span>&#123;
<span class="hljs-attribute">color</span>: red;
&#125;  <span class="hljs-comment">/*外部样式*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">// HTML文档结构为:
<span class="hljs-tag"><<span class="hljs-name">doctype</span> <span class="hljs-attr">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>CSS优先极<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"style.css"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-id">#header</span>&#123;
<span class="hljs-attribute">color</span>: gray;
&#125;    <span class="hljs-comment">/*内嵌式样式*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"header"</span>></span>权重相同时，就近优先<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117164528194.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的页面被解析后，段落文本将显示为灰色，即内嵌式样式优先，<br>
这是因为内嵌式比链入的外部样式更靠近<code>HTML</code>元素。<br>
同样的道理，如果同时引用两个外部样式表，则排在下面的样式表具有较大的优先级。</p>
<p>如果此时将内嵌样式更改为:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">color</span>: gray;
&#125; <span class="hljs-comment">/*内嵌式样式*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>权重不同，<code>#header</code>的权重更高，文字将显示为外部样式定义的红色。</p>
<ul>
<li><code>CSS</code>定义了一个<code>!important</code>命令，该命令被赋予最大的优先级。也就是说不管权重如何及样式位置的远近，<code>!important</code>都具有最大优先级。例如:</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* CSS 文档，文件名为style.css */</span>
<span class="hljs-selector-id">#header</span>&#123;<span class="hljs-attribute">color</span>: red<span class="hljs-meta">!important</span>;&#125;  <span class="hljs-comment">/*外部样式表*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">// HTML文档结构为:
<span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>!important命令最优先<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"style.css"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-id">#header</span>&#123;
<span class="hljs-attribute">color</span>: gray;
&#125;   <span class="hljs-comment">/*内嵌式样式*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"header"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color:yellow"</span>></span>
<span class="hljs-comment"><!--行内式CSS样式--></span>天王盖地虎，!important命令最优先
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117165345998.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>怎么不对？？？</p>
</blockquote>
<p>该页面被解析后，段落文本显示为红色，即使用<code>!important</code>命令的样式拥有最大的优先级。<br>
需要注意的是，<strong>important 命令必须位于属性值和分号之间</strong>，否则无效。</p>
<p>需要注意的是，<strong>复合选择器的权重为组成它的基础选择器权重的叠加，但是这种叠加并不是简单的数字之和</strong>。</p>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>复合选择器权重的叠加<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.inner</span>&#123;
<span class="hljs-attribute">text-decoration</span>: line-through;
&#125; <span class="hljs-comment">/*类选择器定义到除线，权重为10*/</span>

<span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">div</span>&#123;
<span class="hljs-attribute">text-decoration</span>: underline;
&#125;<span class="hljs-comment">/*后代选择器定义下划线，权重为11个1的叠加*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inner"</span>></span> 文本的样式<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后文本并没有像预期的那样添加下划线，而显示了类选择器<code>.inner</code>定义的删除线，<br>
<strong>即标记选择器无论怎么叠加，权重都不会高于类选择器<br>
同理类选择器无论怎么叠加，权重都不会高于<code>id</code>选择器</strong></p>
<p><strong>今天阿ken的学习笔记到此就先告一段落啦 我们下次再见</strong><br>
<br>
<strong>PEACE</strong></p>
<br>
<p><img src="https://img-blog.csdnimg.cn/2020100916514644.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>如果累了就给自己加加油<br>
这一路注定孤独</strong></p>
<p><img src="https://img-blog.csdnimg.cn/20201009165157563.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我们都能努力坚持走下去<br>
祝你也祝我</strong></p>
<p><strong>你好，我是阿ken<br>
感谢阅读<br>
博文若有瑕疵请在评论区留言或私聊我  感谢不吝赐教</strong></p></div>  
</div>
            