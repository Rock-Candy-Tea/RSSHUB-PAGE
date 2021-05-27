
---
title: 'Sass 基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca9096494a4e48b7956b1d954ae754d7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 03:02:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca9096494a4e48b7956b1d954ae754d7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Sass 简介</h2>
<h3 data-id="heading-1">什么是 CSS 预处理器？</h3>
<ul>
<li>CSS 预处理器定义了一种新的语言，其基本思想是，用一种专门的编程语言，为 CSS 增加了一些编程的特性，将 CSS 作为目标生成文件，然后开发者就只要使用这种语言进行编码工作。</li>
<li>通俗的说，“CSS 预处理器用一种专门的编程语言，进行 Web 页面样式设计，然后再编译成正常的 CSS 文件，以供项目使用。CSS 预处理器为 CSS 增加一些编程的特性，无需考虑浏览器的兼容性问题”，例如你可以在 CSS 中使用<strong>变量</strong>、<strong>简单的逻辑程序</strong>、<strong>函数</strong>等等在编程语言中的一些基本特性，可以让你的 CSS <strong>更加简洁</strong>、<strong>适应性更强</strong>、<strong>可读性更佳</strong>，<strong>更易于代码的维护</strong>等诸多好处。</li>
</ul>
<h3 data-id="heading-2">什么是 Sass ？</h3>
<p><a href="http://sass-lang.com/" target="_blank" rel="nofollow noopener noreferrer">Sass 官网</a>上是这样描述 Sass 的：</p>
<blockquote>
<ul>
<li>Sass 是一门高于 CSS 的元语言，它能用来清晰地、结构化地描述文件样式，有着比普通 CSS 更加强大的功能。</li>
<li>Sass 能够提供更简洁、更优雅的语法，同时提供多种功能来创建可维护和管理的样式表。</li>
</ul>
</blockquote>
<h5 data-id="heading-3">Sass 前世今生</h5>
<p>Sass 是最早的 CSS 预处理语言，有比 LESS 更为强大的功能，不过其一开始的缩进式语法（Sass 老版本语法，后面课程会详细介绍 ）并不能被大众接受，不过由于其强大的功能和 Ruby on Rails 的大力推动，还是有很多开发者选择了 Sass。</p>
<p>Sass 是采用 <strong>Ruby</strong> 语言编写的一款 CSS 预处理语言，它诞生于2007年，是最大的成熟的 CSS 预处理语言。最初它是为了配合 HAML（一种缩进式 HTML 预编译器）而设计的，因此有着和 HTML 一样的缩进式风格。</p>
<h5 data-id="heading-4">为什么早期不如 LESS 普及？</h5>
<p>虽然缩进式风格可以有效缩减代码量，强制规范编码风格，但它一方面并不为大多数程序接受，另一方面无法兼容已有的 CSS 代码。这也是 Sass 虽然出现得最早，但远不如 LESS 普及的原因。</p>
<h3 data-id="heading-5">Sass和Less有什么区别？</h3>
<h4 data-id="heading-6">不同之处</h4>
<h5 data-id="heading-7">Less环境较Sass简单</h5>
<p>Cass的安装需要安装Ruby环境，Less基于JavaScript，是需要引入Less.js来处理代码输出css到浏览器，也可以在开发环节使用Less，然后编译成css文件，直接放在项目中，有less.app、SimpleLess、CodeKit.app这样的工具，也有在线编辑地址。</p>
<h5 data-id="heading-8">Less使用较Sass简单</h5>
<p>Less 并没有裁剪 CSS 原有的特性，而是在现有 CSS 语法的基础上，为 CSS 加入程序式语言的特性。只要你了解 CSS 基础就可以很容易上手。</p>
<h5 data-id="heading-9">从功能出发，Sass较Less略强大一些</h5>
<p>① sass有变量和作用域:</p>
<blockquote>
<ul>
<li>
<p>$variable，like php；</p>
</li>
<li>
<p>&#123;$variable｝like ruby；</p>
</li>
<li>
<p>变量有全局和局部之分，并且有优先级。</p>
</li>
</ul>
</blockquote>
<p>② sass有函数的概念:</p>
<blockquote>
<ul>
<li>@function和@return以及函数参数（还有不定参）可以让你像js开发那样封装你想要的逻辑。</li>
<li>@mixin类似function但缺少像function的编程逻辑，更多的是提高css代码段的复用性和模块化，这个用的人也是最多的。</li>
<li>ruby提供了非常丰富的内置原生api。</li>
</ul>
</blockquote>
<p>③ 进程控制：</p>
<blockquote>
<ul>
<li>
<p>条件：@if @else；</p>
</li>
<li>
<p>循环遍历：@for @each @while</p>
</li>
<li>
<p>继承：@extend</p>
</li>
<li>
<p>引用：@import</p>
</li>
</ul>
</blockquote>
<p>④ 数据结构：</p>
<blockquote>
<ul>
<li>
<p>$list类型=数组；</p>
</li>
<li>
<p>$map类型=object；</p>
</li>
<li>
<p>其余的也有string、number、function等类型</p>
</li>
</ul>
</blockquote>
<h5 data-id="heading-10">Less与Sass处理机制不一</h5>
<p>前者是通过客户端处理的，后者是通过服务端处理，相比较之下前者解析会比后者慢一点</p>
<h5 data-id="heading-11">关于变量在Less和Sass中的唯一区别就是Less用@，Sass用$。</h5>
<h4 data-id="heading-12">相同之处</h4>
<p>Less和Sass在语法上有些共性，比如下面这些：</p>
<blockquote>
<ul>
<li>
<p>混入(Mixins)——class中的class；</p>
</li>
<li>
<p>参数混入——可以传递参数的class，就像函数一样；</p>
</li>
<li>
<p>嵌套规则——Class中嵌套class，从而减少重复的代码；</p>
</li>
<li>
<p>运算——CSS中用上数学；</p>
</li>
<li>
<p>颜色功能——可以编辑颜色；</p>
</li>
<li>
<p>名字空间(namespace)——分组样式，从而可以被调用；</p>
</li>
<li>
<p>作用域——局部修改样式；</p>
</li>
<li>
<p>JavaScript 赋值——在CSS中使用JavaScript表达式赋值。</p>
</li>
</ul>
</blockquote>
<h4 data-id="heading-13">为什么选择使用Sass而不是Less？</h4>
<blockquote>
<ul>
<li>
<p>Sass在市面上有一些成熟的框架，比如说Compass，而且有很多框架也在使用Sass，比如说Foundation。</p>
</li>
<li>
<p>就国外讨论的热度来说，Sass绝对优于LESS。</p>
</li>
<li>
<p>就学习教程来说，Sass的教程要优于LESS。在国内LESS集中的教程是LESS中文官网，而Sass的中文教程，慢慢在国内也较为普遍。</p>
</li>
<li>
<p>Sass也是成熟的CSS预处理器之一，而且有一个稳定，强大的团队在维护。</p>
</li>
<li>
<p>同时还有Scss对sass语法进行了改良，Sass 3就变成了Scss(sassy css)。与原来的语法兼容，只是用&#123;&#125;取代了原来的缩进。</p>
</li>
<li>
<p>bootstrap（Web框架）最新推出的版本4，使用的就是Sass。</p>
</li>
</ul>
</blockquote>
<h3 data-id="heading-14">Sass 和 SCSS 有什么区别？</h3>
<p><strong>Sass</strong> 和 <strong>SCSS</strong> 其实是同一种东西，我们平时都称之为 <strong>Sass</strong>，两者之间不同之处有以下两点：</p>
<blockquote>
<ul>
<li>
<p>文件扩展名不同，Sass 是以“<strong>.sass</strong>”后缀为扩展名，而 SCSS 是以“<strong>.scss</strong>”后缀为扩展名</p>
</li>
<li>
<p>语法书写方式不同，<strong>Sass 是以严格的缩进式语法</strong>规则来书写，<strong>不带大括号(&#123;&#125;)和分号(;)</strong>，而 SCSS 的语法书写和我们的 <strong>CSS 语法书写方式非常类似</strong>。</p>
</li>
</ul>
</blockquote>
<p>先来看一个示例：</p>
<p><strong>Sass 语法</strong></p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">font</span>-stack: Helvetica, sans-serif  //定义变量
$primary-color: <span class="hljs-number">#333</span> //定义变量

body
  font: <span class="hljs-number">100%</span> $font-stack
  color: $primary-color
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>SCSS 语法</strong></p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">font</span>-stack: Helvetica, sans-serif;
$primary-<span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;

<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">font</span>: <span class="hljs-number">100%</span> $font-stack;
  <span class="hljs-attribute">color</span>: $primary-color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编译出来的 CSS</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">font</span>: <span class="hljs-number">100%</span> Helvetica, sans-serif;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">Sass的基础</h2>
<h3 data-id="heading-16">Sass 的变量</h3>
<h4 data-id="heading-17">Sass 声明变量</h4>
<p>定义变量的语法：在有些编程语言中（如，JavaScript）声明变量都是使用关键词“var”开头，但是在 Sass 不使用这个关键词，而是使用美元符号“<strong>$</strong>”开头：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca9096494a4e48b7956b1d954ae754d7~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图非常清楚告诉了大家，Sass 的变量包括三个部分：</p>
<blockquote>
<ul>
<li>声明变量的符号“$”</li>
<li>变量名称</li>
<li>赋予变量的值</li>
</ul>
</blockquote>
<p>来看一个简单的示例，假设你的按钮颜色可以给其声明几个变量：</p>
<pre><code class="hljs language-css copyable" lang="css">$brand-primary : <span class="hljs-built_in">darken</span>(<span class="hljs-number">#428bca</span>, <span class="hljs-number">6.5%</span>) !default; // <span class="hljs-selector-id">#337ab7</span>
$btn-primary-<span class="hljs-attribute">color</span> : <span class="hljs-number">#fff</span> !default;
$btn-primary-bg : $brand-primary !default;
$btn-primary-<span class="hljs-attribute">border</span> : <span class="hljs-built_in">darken</span>($btn-primary-bg, <span class="hljs-number">5%</span>) !default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果值后面加上!default则表示默认值。</p>
<blockquote>
<p>注：了解 Bootstrap 的 Sass 版本的同学，就一眼能看出，上面的示例代码是 Bootstrap 定义 primarybutton 的颜色。</p>
</blockquote>
<h4 data-id="heading-18">Sass变量的调用</h4>
<p>在 Sass 中声明了变量之后，就可以在需要的地方调用变量。调用变量的方法也非常的简单。</p>
<p><strong>比如在定义了变量</strong></p>
<pre><code class="hljs language-css copyable" lang="css">$brand-primary : <span class="hljs-built_in">darken</span>(<span class="hljs-number">#428bca</span>, <span class="hljs-number">6.5%</span>) !default; // <span class="hljs-selector-id">#337ab7</span>
$btn-primary-<span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span> !default;
$btn-primary-bg : $brand-primary !default;
$btn-primary-<span class="hljs-attribute">border</span> : <span class="hljs-built_in">darken</span>($btn-primary-bg, <span class="hljs-number">5%</span>) !default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在按钮 button 中调用，可以按下面的方式调用</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn-primary</span> &#123;
   <span class="hljs-attribute">background-color</span>: $btn-primary-bg;
   <span class="hljs-attribute">color</span>: $btn-primary-color;
   <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid $btn-primary-border;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编译出来的CSS:</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn-primary</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#337ab7</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#2e6da4</span>;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">Sass普通变量与默认变量</h4>
<h4 data-id="heading-20">普通变量</h4>
<p>定义之后可以在全局范围内使用。</p>
<pre><code class="hljs language-css copyable" lang="css">$fontSize: <span class="hljs-number">12px</span>;
<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">font-size</span>:$fontSize;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的css代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">font-size</span>:<span class="hljs-number">12px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">默认变量</h4>
<p>sass 的默认变量仅需要在值后面加上 !default 即可。</p>
<pre><code class="hljs language-css copyable" lang="css">$baseLineHeight:<span class="hljs-number">1.5</span> !default;
<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">line-height</span>: $baseLineHeight; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的css代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">line-height</span>:<span class="hljs-number">1.5</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sass 的默认变量一般是用来设置默认值，然后根据需求来覆盖的，覆盖的方式也很简单，只需要在默认变量<strong>之前或者之后</strong>重新声明下变量即可。</p>
<pre><code class="hljs language-css copyable" lang="css">$baseLineHeight: <span class="hljs-number">2</span>;
$baseLineHeight: <span class="hljs-number">1.5</span> !default;
<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">line-height</span>: $baseLineHeight; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的css代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">line-height</span>:<span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出现在编译后的 line-height 为 2，而不是我们默认的 1.5。</p>
<p>!default最大的作用是在你开发框架时用的比较广，定义好这个之后，下面的东西，比如背景，或者字体颜色不用定义他会首先执行这个默认的颜色，如果某个地方不想用这个颜色你可以在调用其他你定义好的颜色</p>
<h4 data-id="heading-22">Sass局部变量和全局变量</h4>
<p>Sass 中变量的作用域在过去几年已经发生了一些改变。直到最近，规则集和其他范围内声明变量的作用域才默认为本地。如果已经存在同名的全局变量，从 3.4 版本开始，Sass 已经可以正确处理作用域的概念，并通过创建一个新的局部变量来代替。</p>
<h4 data-id="heading-23">全局变量与局部变量</h4>
<p>先来看一下代码例子：</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">color</span>: orange !default;//定义全局变量(在选择器、函数、混合宏...的外面定义的变量为全局变量)
<span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-attribute">color</span>: $color;//调用全局变量
&#125;
<span class="hljs-selector-tag">em</span> &#123;
    $<span class="hljs-attribute">color</span>: red;//定义局部变量
    <span class="hljs-selector-tag">a</span> &#123;
        <span class="hljs-attribute">color</span>: $color;//调用局部变量
    &#125;
&#125;
<span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">color</span>: $color;//调用全局变量
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css 的结果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-attribute">color</span>: orange;
&#125;
<span class="hljs-selector-tag">em</span> <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">color</span>: orange;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的示例演示可以得知，在元素内部定义的变量不会影响其他元素。如此可以简单的理解成，<strong>全局变量</strong>就是定义在元素外面的变量，如下代码：</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">color</span>:orange !default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>c</mi><mi>o</mi><mi>l</mi><mi>o</mi><mi>r</mi><mtext>就是一个全局变量，而定义在元素内部的变量，比如</mtext><mi mathvariant="normal">‘</mi></mrow><annotation encoding="application/x-tex">color 就是一个全局变量，而定义在元素内部的变量，比如 `</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord cjk_fallback">就</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">全</span><span class="mord cjk_fallback">局</span><span class="mord cjk_fallback">变</span><span class="mord cjk_fallback">量</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">而</span><span class="mord cjk_fallback">定</span><span class="mord cjk_fallback">义</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">元</span><span class="mord cjk_fallback">素</span><span class="mord cjk_fallback">内</span><span class="mord cjk_fallback">部</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">变</span><span class="mord cjk_fallback">量</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">比</span><span class="mord cjk_fallback">如</span><span class="mord">‘</span></span></span></span></span>color:red;` 是一个<strong>局部变量</strong>。</p>
<p>除此之外，Sass 现在还提供一个<code>!global</code>参数。!global 和 !default 对于定义变量都是很有帮助的。我们之后将会详细介绍这两个参数的使用以及其功能。</p>
<h4 data-id="heading-24">全局变量的影子</h4>
<p>当在局部范围（选择器内、函数内、混合宏内...）声明一个已经存在于全局范围内的变量时，局部变量就成为了<strong>全局变量的影子</strong>。基本上，<strong>局部变量只会在局部范围内覆盖全局变量</strong>。</p>
<p>上面例子中的 em 选择器内的变量 $color 就是一个全局变量的影子。</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">color</span>: orange !default;//定义全局变量
<span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-attribute">color</span>: $color;//调用全局变量
&#125;
<span class="hljs-selector-tag">em</span> &#123;
    $<span class="hljs-attribute">color</span>: red;//定义局部变量（全局变量 $<span class="hljs-attribute">color</span> 的影子）
    <span class="hljs-selector-tag">a</span> &#123;
        <span class="hljs-attribute">color</span>: $color;//调用局部变量
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">什么时候声明变量？</h4>
<p>我的建议，创建变量只适用于感觉确有必要的情况下。不要为了某些骇客行为而声明新变量，这丝毫没有作用。只有满足所有下述标准时方可创建新变量：</p>
<blockquote>
<ol>
<li>该值至少重复出现了两次；</li>
<li>该值至少可能会被更新一次；</li>
<li>该值所有的表现都与变量有关（非巧合）。</li>
</ol>
</blockquote>
<p>基本上，没有理由声明一个永远不需要更新或者只在单一地方使用变量。</p>
<h3 data-id="heading-26">Sass嵌套</h3>
<p>Sass 中还提供了选择器嵌套功能，但这也并不意味着你在 Sass 中的嵌套是无节制的，因为你嵌套的层级越深，编译出来的 CSS 代码的选择器层级将越深，这往往是大家不愿意看到的一点。这个特性现在正被众多开发者滥用。</p>
<p>选择器嵌套为样式表的作者提供了一个通过局部选择器相互嵌套实现全局选择的方法，Sass 的嵌套分为三种：</p>
<blockquote>
<ul>
<li>选择器嵌套</li>
<li>属性嵌套</li>
<li>伪类嵌套</li>
</ul>
</blockquote>
<h4 data-id="heading-27">选择器嵌套</h4>
<p>假设我们有一段这样的结构：</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">header</span>>
<<span class="hljs-selector-tag">nav</span>>
    <<span class="hljs-selector-tag">a</span> href=“##”>Home</<span class="hljs-selector-tag">a</span>>
    <<span class="hljs-selector-tag">a</span> href=“##”>About</<span class="hljs-selector-tag">a</span>>
    <<span class="hljs-selector-tag">a</span> href=“##”>Blog</<span class="hljs-selector-tag">a</span>>
</<span class="hljs-selector-tag">nav</span>>
<<span class="hljs-selector-tag">header</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想选中 header 中的 a 标签，那么在 Sass 中，就可以使用选择器的嵌套来实现：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">nav</span> &#123;
  <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">color</span>: red;
    <span class="hljs-selector-tag">header</span> & &#123;
      <span class="hljs-attribute">color</span>:green;
    &#125;
  &#125;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>&</code> 连体符，编译结果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">nav</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">color</span>:red;
&#125;

<span class="hljs-selector-tag">header</span> <span class="hljs-selector-tag">nav</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">color</span>:green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">属性嵌套</h4>
<p>Sass 中还提供属性嵌套，CSS 有一些属性前缀相同，只是后缀不一样，比如：<code>border-top/border-right</code>，与这个类似的还有 <code>margin、padding、font</code> 等属性。假设你的样式中用到了：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">border-top</span>: <span class="hljs-number">1px</span> solid red;
    <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Sass 中我们可以这样写：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">border</span>: &#123;
        top: <span class="hljs-number">1px</span> solid red;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">1px</span> solid green;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">伪类嵌套</h4>
<p>其实<strong>伪类嵌套</strong>和<strong>属性嵌套</strong>非常类似，只不过他需要借助<code>&</code>符号一起配合使用。我们就拿经典的“clearfix”为例吧：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.clearfix</span>&#123;
    &:before,
    &:after &#123;
        content:<span class="hljs-string">""</span>;
        <span class="hljs-attribute">display</span>: table;
    &#125;
    &:after &#123;
        clear:both;
        <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS：</p>
<pre><code class="hljs language-css copyable" lang="css">clearfix:before, .clearfix:after &#123;
    content: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">display</span>: table;
&#125;
<span class="hljs-selector-class">.clearfix</span>:after &#123;
    clear: both;
    <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">Sass混合宏</h3>
<p>如果你的整个网站中有几处小样式类似，比如颜色，字体等，在 Sass 可以使用变量来统一处理，那么这种选择还是不错的。但当你的样式变得越来越复杂，需要重复使用大段的样式时，使用变量就无法达到我们目了。这个时候 Sass 中的混合宏就会变得非常有意义。在这一节中，主要向大家介绍 Sass 的<strong>混合宏</strong>。</p>
<h4 data-id="heading-31">声明混合宏</h4>
<h5 data-id="heading-32">不带参数混合宏</h5>
<p>在 Sass 中，使用“<code>@mixin</code>”来声明一个混合宏。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> border-radius&#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>@mixin</code> 是用来声明<strong>混合宏</strong>的关键词，有点类似 CSS 中的 <code>@media、@font-face</code> 一样。<code>border-radius</code> 是<strong>混合宏</strong>的名称。大括号里面是复用的样式代码。</p>
<h4 data-id="heading-33">调用混合宏</h4>
<p>在 Sass 中通过 <code>@mixin</code> 关键词声明了一个混合宏，那么在实际调用中，其匹配了一个关键词“<code>@include</code>”来调用声明好的混合宏。例如在你的样式中定义了一个圆角的混合宏“<code>border-radius</code>”:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> border-radius&#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一个按钮中要调用定义好的混合宏“<code>border-radius</code>”，可以这样使用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-keyword">@include</span> border-radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">button</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">混合宏的参数</h4>
<p>Sass 的<strong>混合宏</strong>有一个强大的功能，可以传参，那么在 Sass 中传参主要有以下几种情形：</p>
<h5 data-id="heading-35">传一个不带值的参数</h5>
<p>在混合宏中，可以传一个不带任何值的参数，比如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> border-radius($radius)&#123;
  <span class="hljs-attribute">border-radius</span>: $radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在混合宏“<code>border-radius</code>”中定义了一个不带任何值的参数“<code>$radius</code>”。</p>
<p>在调用的时候可以给这个混合宏传一个参数值：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-keyword">@include</span> border-radius(<span class="hljs-number">3px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里表示给混合宏传递了一个“border-radius”的值为“3px”。</p>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-36">传一个带值的参数</h5>
<p>在 Sass 的混合宏中，还可以给混合宏的参数传一个默认值，例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> border-radius($<span class="hljs-attribute">radius</span>:<span class="hljs-number">3px</span>)&#123;
  <span class="hljs-attribute">border-radius</span>: $radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在混合宏<code>“border-radius”</code>传了一个参数“<code>$radius</code>”，而且给这个参数赋予了一个默认值“<code>3px</code>”。</p>
<p>在调用类似这样的混合宏时，会多有一个机会，假设你的页面中的圆角很多地方都是“3px”的圆角，那么这个时候只需要调用默认的混合宏“border-radius”:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn</span> &#123;
  <span class="hljs-keyword">@include</span> border-radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但有的时候，页面中有些元素的圆角值不一样，那么可以随机给混合宏传值，如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-keyword">@include</span> border-radius(<span class="hljs-number">50%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-37">传多个参数</h5>
<p>Sass 混合宏除了能传一个参数之外，还可以传多个参数，如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> center($<span class="hljs-attribute">width</span>,$<span class="hljs-attribute">height</span>)&#123;
  <span class="hljs-attribute">width</span>: $width;
  <span class="hljs-attribute">height</span>: $height;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-built_in">-</span>($height) / <span class="hljs-number">2</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-built_in">-</span>($width) / <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在混合宏“center”就传了多个参数。在实际调用和其调用其他混合宏是一样的：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box-center</span> &#123;
  <span class="hljs-keyword">@include</span> center(<span class="hljs-number">500px</span>,<span class="hljs-number">300px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box-center</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">150px</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">250px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一个特别的参数“<strong>…</strong>”。当混合宏传的参数过多之时，可以使用参数来替代，如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> box-shadow($shadows...)&#123;
  <span class="hljs-keyword">@if</span> length($shadows) >= <span class="hljs-number">1</span> &#123;
    <span class="hljs-attribute">box-shadow</span>: $shadows;
  &#125; <span class="hljs-keyword">@else</span> &#123;
    $shadows: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">#000</span>,.<span class="hljs-number">25</span>);
    <span class="hljs-attribute">box-shadow</span>: $shadow;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实际调用中：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-keyword">@include</span> box-shadow(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">1px</span> rgba(#<span class="hljs-number">000</span>,.<span class="hljs-number">5</span>),<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> rgba(#<span class="hljs-number">000</span>,.<span class="hljs-number">2</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">1px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>), <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-38">混合宏的不足</h5>
<p>混合宏在实际编码中给我们带来很多方便之处，特别是对于复用重复代码块。但其最大的不足之处是会生成冗余的代码块。比如在不同的地方调用一个相同的混合宏时。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> border-radius&#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;

<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-keyword">@include</span> border-radius;
  <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-selector-class">.btn</span> &#123;
  <span class="hljs-keyword">@include</span> border-radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例在“.box”和“.btn”中都调用了定义好的“border-radius”混合宏。先来看编译出来的 CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
  <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-selector-class">.btn</span> &#123;
  -webkit-<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">3px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例明显可以看出，Sass 在调用相同的混合宏时，并不能智能的将相同的样式代码块合并在一起。这也是 Sass 的混合宏最不足之处。</p>
<h3 data-id="heading-39">Sass 继承</h3>
<p>继承对于了解 CSS 的同学来说一点都不陌生，先来看一张图：</p>
<p>[<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/386aee6fa016447fa0ec39acb9b22f80~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">](<a href="http://img.m/" target="_blank" rel="nofollow noopener noreferrer">http://img.m</a></p>
<p>图中代码显示<code>“.col-sub .block li,.col-extra .block li”</code> 继承了 <code>“.item-list ul li”</code>选择器的 <code>“padding : 0;”</code> 和 <code>“ul li”</code> 选择器中的<code> “list-style : none outside none;”</code>以及 * 选择器中的 <code>“box-sizing:inherit;”</code>。</p>
<p>在 Sass 中也具有继承一说，也是继承类中的样式代码块。在 Sass 中是通过关键词 <code>“@extend”</code>来继承已存在的类样式块，从而实现代码的继承。如下所示：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">6px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125;

<span class="hljs-selector-class">.btn-primary</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f36</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-keyword">@extend</span> .btn;
&#125;

<span class="hljs-selector-class">.btn-second</span> &#123;
  <span class="hljs-attribute">background-color</span>: orange;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-keyword">@extend</span> .btn;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来之后：</p>
<pre><code class="hljs language-css copyable" lang="css">//CSS
<span class="hljs-selector-class">.btn</span>, <span class="hljs-selector-class">.btn-primary</span>, <span class="hljs-selector-class">.btn-second</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">6px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125;

<span class="hljs-selector-class">.btn-primary</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f36</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-selector-class">.btn-second</span> &#123;
  <span class="hljs-attribute">background</span>-clor: orange;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从示例代码可以看出，在 Sass 中的继承，可以继承类样式块中所有样式代码，而且编译出来的 CSS 会将选择器合并在一起，形成组合选择器：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.btn</span>, <span class="hljs-selector-class">.btn-primary</span>, <span class="hljs-selector-class">.btn-second</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">6px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">Sass 占位符 %</h3>
<p>Sass 中的占位符 <code>%</code> 功能是一个很强大，很实用的一个功能，这也是我非常喜欢的功能。他可以取代以前 CSS 中的基类造成的代码冗余的情形。因为 <code>%</code> 声明的代码，如果不被 <code>@extend</code> 调用的话，不会产生任何代码。来看一个演示：</p>
<pre><code class="hljs language-css copyable" lang="css">%mt5 &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;
%pt5&#123;
  <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">5px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码没有被 @extend 调用，他并没有产生任何代码块，只是静静的躺在你的某个 SCSS 文件中。只有通过 @extend 调用才会产生代码：</p>
<pre><code class="hljs language-css copyable" lang="css">%mt5 &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;
%pt5&#123;
  <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-selector-class">.btn</span> &#123;
  <span class="hljs-keyword">@extend</span> %mt5;
  <span class="hljs-keyword">@extend</span> %pt5;
&#125;

<span class="hljs-selector-class">.block</span> &#123;
  <span class="hljs-keyword">@extend</span> %mt5;

  <span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-keyword">@extend</span> %pt5;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS</p>
<pre><code class="hljs language-css copyable" lang="css">//CSS
<span class="hljs-selector-class">.btn</span>, <span class="hljs-selector-class">.block</span> &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-selector-class">.btn</span>, <span class="hljs-selector-class">.block</span> <span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">5px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从编译出来的 CSS 代码可以看出，通过 <code>@extend</code> 调用的占位符，编译出来的代码会将相同的代码合并在一起。这也是我们希望看到的效果，也让你的代码变得更为干净。</p>
<h3 data-id="heading-41">Sass混合宏 VS 继承 VS 占位符</h3>
<p>初学者都常常纠结于这个问题“<strong>什么时候用混合宏</strong>，<strong>什么时候用继承</strong>，<strong>什么时候使用占位符</strong>？”其实他们各有各的优点与缺点，先来看看他们使用效果：</p>
<h4 data-id="heading-42">Sass 中的混合宏使用</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> mt($var)&#123;
    <span class="hljs-attribute">margin-top</span>: $var;  
&#125;

<span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-keyword">@include</span> mt(<span class="hljs-number">5px</span>);

    <span class="hljs-selector-tag">span</span> &#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@include</span> mt(<span class="hljs-number">5px</span>);
    &#125;
&#125;

<span class="hljs-selector-class">.header</span> &#123;
    <span class="hljs-attribute">color</span>: orange;
    <span class="hljs-keyword">@include</span> mt(<span class="hljs-number">5px</span>);

    <span class="hljs-selector-tag">span</span>&#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@include</span> mt(<span class="hljs-number">5px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>**总结：**编译出来的 CSS 清晰告诉了大家，他不会自动合并相同的样式代码，如果在样式文件中调用同一个混合宏，会产生多个对应的样式代码，造成代码的冗余，这也是 CSSer 无法忍受的一件事情。不过他并不是一无事处，他可以传参数。</p>
<p><strong>个人建议</strong>：如果你的代码块中涉及到变量，建议使用混合宏来创建相同的代码块。</p>
</blockquote>
<h4 data-id="heading-43">Sass 中继承</h4>
<p>同样的，将上面代码中的混合宏，使用类名来表示，然后通过继承来调用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.mt</span>&#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;  
&#125;

<span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-keyword">@extend</span> .mt;

    <span class="hljs-selector-tag">span</span> &#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@extend</span> .mt;
    &#125;
&#125;

<span class="hljs-selector-class">.header</span> &#123;
    <span class="hljs-attribute">color</span>: orange;
    <span class="hljs-keyword">@extend</span> .mt;

    <span class="hljs-selector-tag">span</span>&#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@extend</span> .mt;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>
<p>**总结：**使用继承后，编译出来的 CSS 会将使用继承的代码块合并到一起，通过组合选择器的方式向大家展现，比如 <code>.mt, .block, .block span, .header, .header span</code>。这样编译出来的代码相对于混合宏来说要干净的多，也是 CSSer 期望看到。但是他不能传变量参数。</p>
</li>
<li>
<p><strong>个人建议</strong>：如果你的代码块不需要专任何变量参数，而且有一个基类已在文件中存在，那么建议使用 Sass 的继承。</p>
</li>
</ul>
</blockquote>
<h4 data-id="heading-44">占位符</h4>
<p>最后来看占位符，将上面代码中的基类 .mt 换成 Sass 的占位符格式：</p>
<pre><code class="hljs language-css copyable" lang="css">%mt&#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;  
&#125;

<span class="hljs-selector-class">.block</span> &#123;
    <span class="hljs-keyword">@extend</span> %mt;

    <span class="hljs-selector-tag">span</span> &#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@extend</span> %mt;
    &#125;
&#125;

<span class="hljs-selector-class">.header</span> &#123;
    <span class="hljs-attribute">color</span>: orange;
    <span class="hljs-keyword">@extend</span> %mt;

    <span class="hljs-selector-tag">span</span>&#123;
        <span class="hljs-attribute">display</span>:block;
        <span class="hljs-keyword">@extend</span> %mt;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>**总结：**编译出来的 CSS 代码和使用继承基本上是相同，只是不会在代码中生成占位符 mt 的选择器。那么占位符和继承的主要区别的，“占位符是独立定义，不调用的时候是不会在 CSS 中产生任何代码；继承是首先有一个基类存在，不管调用与不调用，基类的样式都将会出现在编译出来的 CSS 代码中。”</p>
</blockquote>
<p>来看一个表格：</p>
<p>[<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c6f5ee113294a90981675626fca0c9f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-45">Sass 插值 <code>#&#123;&#125;</code></h3>
<p>使用 CSS 预处理器语言的一个主要原因是想使用 Sass 获得一个更好的结构体系。比如说你想写更干净的、高效的和面向对象的 CSS。Sass 中的插值(Interpolation)就是重要的一部分。让我们看一下下面的例子：</p>
<pre><code class="hljs language-css copyable" lang="css">$properties: (margin, padding);
<span class="hljs-keyword">@mixin</span> set-value($side, $value) &#123;
    <span class="hljs-keyword">@each</span> $prop in $properties &#123;
        #&#123;$prop&#125;-#&#123;$side&#125;: $value;
    &#125;
&#125;
<span class="hljs-selector-class">.login-box</span> &#123;
    <span class="hljs-keyword">@include</span> set-value(top, <span class="hljs-number">14px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它可以让变量和属性工作的很完美，上面的代码编译成 CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.login-box</span> &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">14px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是 Sass 插值中一个简单的实例。当你想设置属性值的时候你可以使用字符串插入进来。另一个有用的用法是构建一个选择器。可以这样使用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> generate-sizes($class, $small, $medium, $big) &#123;
    .#&#123;$class&#125;-small &#123; <span class="hljs-attribute">font-size</span>: $small; &#125;
    .#&#123;$class&#125;-medium &#123; <span class="hljs-attribute">font-size</span>: $medium; &#125;
    .#&#123;$class&#125;-big &#123; <span class="hljs-attribute">font-size</span>: $big; &#125;
&#125;
<span class="hljs-keyword">@include</span> generate-sizes(<span class="hljs-string">"header-text"</span>, <span class="hljs-number">12px</span>, <span class="hljs-number">20px</span>, <span class="hljs-number">40px</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.header-text-small</span> &#123; <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>; &#125;
<span class="hljs-selector-class">.header-text-medium</span> &#123; <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>; &#125;
<span class="hljs-selector-class">.header-text-big</span> &#123; <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦你发现这一点，你就会想到超级酷的 mixins，用来生成代码或者生成另一个 mixins。然而，这并不完全是可能的。第一个限制，这可能会删除用于 Sass 变量的插值。</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">margin</span>-big: <span class="hljs-number">40px</span>;
$<span class="hljs-attribute">margin</span>-medium: <span class="hljs-number">20px</span>;
$<span class="hljs-attribute">margin</span>-small: <span class="hljs-number">12px</span>;
<span class="hljs-keyword">@mixin</span> set-value($size) &#123;
    <span class="hljs-attribute">margin-top</span>: $margin-#&#123;$size&#125;;
&#125;
<span class="hljs-selector-class">.login-box</span> &#123;
    <span class="hljs-keyword">@include</span> set-value(big);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 Sass 代码编译出来，你会得到下面的信息：</p>
<blockquote>
<p>error style.scss (Line 5: Undefined variable: “$margin-".)</p>
</blockquote>
<p>所以，<code>#&#123;&#125;</code>语法并不是随处可用，不能插入已有变量中</p>
<p>你也不能在 mixin 中调用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> updated-status &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#F00</span>;
&#125;
$flag: <span class="hljs-string">"status"</span>;
<span class="hljs-selector-class">.navigation</span> &#123;
    <span class="hljs-keyword">@include</span> updated-#&#123;$flag&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码在编译成 CSS 时同样会报错：</p>
<blockquote>
<p>error style.scss (Line 7: Invalid CSS after "...nclude updated-": expected "&#125;", was "#&#123;$flag&#125;;")</p>
</blockquote>
<p>幸运的是，可以使用 <code>@extend</code> 中使用插值。例如：</p>
<pre><code class="hljs language-css copyable" lang="css">%updated-status &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#F00</span>;
&#125;
<span class="hljs-selector-class">.selected-status</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bold;
&#125;
$flag: <span class="hljs-string">"status"</span>;
<span class="hljs-selector-class">.navigation</span> &#123;
    <span class="hljs-keyword">@extend</span> %updated-#&#123;$flag&#125;;
    <span class="hljs-keyword">@extend</span> .selected-#&#123;$flag&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 Sass 代码是可以运行的，可以动态的插入<code>.class</code>和 <code>%placeholder</code>。当然他们不能接受像 mixin 这样的参数。</p>
<p>上面的代码编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.navigation</span> &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#F00</span>;
&#125;
<span class="hljs-selector-class">.selected-status</span>, <span class="hljs-selector-class">.navigation</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bold;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">Sass 注释</h3>
<p>注释对于一名程序员来说，是极其重要，良好的注释能帮助自己或者别人阅读源码。在 Sass 中注释有两种方式，我暂且将其命名为：</p>
<blockquote>
<ul>
<li>类似 CSS 的注释方式，使用 ”/* ”开头，结属使用 ”*/ ”</li>
<li>类似 JavaScript 的注释方式，使用“//”</li>
</ul>
</blockquote>
<p>两者区别，前者会在编译出来的 CSS 显示，后者在编译出来的 CSS 中不会显示，来看一个示例：</p>
<pre><code class="hljs language-css copyable" lang="css">//定义一个占位符

%mt5 &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-comment">/*调用一个占位符*/</span>

<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-keyword">@extend</span> %mt5;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-comment">/*调用一个占位符*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">Sass 数据类型</h3>
<p>Sass 和 JavaScript 语言类似，也具有自己的数据类型，在 Sass 中包含以下几种数据类型：</p>
<blockquote>
<ul>
<li>数字: 如，1、 2、 13、 10px；</li>
<li>字符串：有引号字符串或无引号字符串，如，"foo"、 'bar'、 baz；</li>
<li>颜色：如，blue、 #04a3f9、 rgba(255,0,0,0.5)；</li>
<li>布尔型：如，true、 false；</li>
<li>空值：如，null；</li>
<li>值列表：用空格或者逗号分开，如，1.5em 1em 0 2em 、 Helvetica, Arial, sans-serif。</li>
</ul>
</blockquote>
<p>SassScript 也支持其他 CSS 属性值（property value），比如 Unicode 范围，或 !important 声明。然而，Sass 不会特殊对待这些属性值，一律视为无引号字符串 (unquoted strings)。</p>
<h4 data-id="heading-48">字符串</h4>
<p>SassScript 支持 CSS 的两种字符串类型：</p>
<blockquote>
<ul>
<li>有引号字符串 (quoted strings)，如 "Lucida Grande" 、'<a href="http://sass-lang.com';/" target="_blank" rel="nofollow noopener noreferrer">sass-lang.com'；</a></li>
<li>无引号字符串 (unquoted strings)，如 sans-serifbold。</li>
</ul>
</blockquote>
<p>在编译 CSS 文件时不会改变其类型。只有一种情况例外，使用 #&#123; &#125;插值语句 (interpolation) 时，有引号字符串将被编译为无引号字符串，这样方便了在混合指令 (mixin) 中引用选择器名。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> firefox-message($selector) &#123;
  <span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.firefox</span> #&#123;$selector&#125;:before &#123;
    content: <span class="hljs-string">"Hi, Firefox users!"</span>;
  &#125;
&#125;
<span class="hljs-keyword">@include</span> firefox-message(<span class="hljs-string">".header"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译为：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span><span class="hljs-selector-class">.firefox</span> <span class="hljs-selector-class">.header</span>:before &#123;
  content: <span class="hljs-string">"Hi, Firefox users!"</span>; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的是：当 deprecated = property syntax 时 （暂时不理解是怎样的情况），所有的字符串都将被编译为无引号字符串，不论是否使用了引号。</p>
</blockquote>
<h4 data-id="heading-49">值列表</h4>
<p>所谓<strong>值列表</strong> (lists) 是指 Sass 如何处理 CSS 中：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">15px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font</span>-face: Helvetica, Arial, sans-serif
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像上面这样通过空格或者逗号分隔的一系列的值。</p>
<p>事实上，独立的值也被视为值列表（只包含一个值的值列表）。</p>
<p>Sass列表函数（Sass list functions）赋予了值列表更多功能（Sass进级会有讲解）：</p>
<blockquote>
<ol>
<li>nth函数（nth function） 可以直接访问值列表中的某一项；</li>
<li>join函数（join function） 可以将多个值列表连结在一起；</li>
<li>append函数（append function） 可以在值列表中添加值；</li>
<li>@each规则（@each rule） 则能够给值列表中的每个项目添加样式。</li>
</ol>
</blockquote>
<p>值列表中可以再包含值列表，比如 <code>1px 2px, 5px 6px</code> 是包含 <code>1px 2px 与 5px 6px</code> 两个值列表的<strong>值列表</strong>。如果内外两层值列表使用相同的分隔方式，要用圆括号包裹内层，所以也可以写成 <code>(1px 2px) (5px 6px)</code>。当值列表被编译为 CSS 时，Sass 不会添加任何圆括号，因为 CSS 不允许这样做。<code>(1px 2px) (5px 6px)</code>与 <code>1px 2px 5px 6px</code> 在编译后的 CSS 文件中是一样的，但是它们在 Sass 文件中却有不同的意义，前者是包含两个值列表的值列表，而后者是包含四个值的值列表。</p>
<p>可以用 () 表示空的列表，这样不可以直接编译成 CSS，比如编译 <code>font-family: ()</code>时，Sass 将会报错。如果值列表中包含空的值列表或空值，编译时将清除空值，比如<code> 1px 2px () 3px</code> 或 <code>1px 2px null 3px</code>。</p>
<h2 data-id="heading-50">Sass 运算</h2>
<p>程序中的运算是常见的一件事情，但在 CSS 中能做运算的，到目前为止仅有<code> calc()</code> 函数可行。但在 Sass 中，运算只是其基本特性之一。在 Sass 中可以做各种数学计算，在接下来的章节中，主要和大家一起探讨有关于 Sass 中的数学运算。</p>
<h3 data-id="heading-51">加法/减法</h3>
<p>加法运算是 Sass 中运算中的一种，在变量或属性中都可以做加法运算。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span> + <span class="hljs-number">8px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">28px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但对于携带不同类型的单位时，在 Sass 中计算会报错，如下例所示：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span> + <span class="hljs-number">1em</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译的时候，编译器会报错：<code>“Incompatible units: 'em' and ‘px'.”</code></p>
<p>减法同加法</p>
<h3 data-id="heading-52">乘法</h3>
<p>Sass 中的乘法运算和前面介绍的加法与减法运算还略有不同。虽然他也能够支持多种单位（比如 em ,px , %），但当一个单位同时声明两个值时会有问题。比如下面的示例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">10px</span> * <span class="hljs-number">2px</span>;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译的时候报<code>“20px*px isn't a valid CSS value.”</code>错误信息。</p>
<p>如果进行乘法运算时，两个值单位相同时，只需要为一个数值提供单位即可。上面的示例可以修改成：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span> * <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Sass 的乘法运算和加法、减法运算一样，在运算中有不同类型的单位时，也将会报错。</p>
<h3 data-id="heading-53">除法</h3>
<p>Sass 的乘法运算规则也适用于除法运算。不过除法运算还有一个特殊之处。众所周知“<strong>/</strong>”符号在 CSS 中已做为一种符号使用。因此在 Sass 中做除法运算时，直接使用“/”符号做为除号时，将不会生效，编译时既得不到我们需要的效果，也不会报错。一起先来看一个简单的示例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span> / <span class="hljs-number">2</span>;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS 如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span> / <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的结果对于大家来说没有任何意义。要修正这个问题，只需要给运算的外面添加一个小括号**( )**即可：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: (<span class="hljs-number">100px</span> / <span class="hljs-number">2</span>);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS 如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了上面情况带有小括号，“/”符号会当作除法运算符之外，如果“/”符号在已有的数学表达式中时，也会被认作除法符号。如下面示例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span> / <span class="hljs-number">2</span> + <span class="hljs-number">2in</span>;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">242px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，在 Sass 除法运算中，当用变量进行除法运算时，“/”符号也会自动被识别成除法，如下例所示：</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">width</span>: <span class="hljs-number">1000px</span>;
$nums: <span class="hljs-number">10</span>;

<span class="hljs-selector-class">.item</span> &#123;
  <span class="hljs-attribute">width</span>: $width / <span class="hljs-number">10</span>;  
&#125;

<span class="hljs-selector-class">.list</span> &#123;
  <span class="hljs-attribute">width</span>: $width / $nums;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.item</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;

<span class="hljs-selector-class">.list</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综合上述，”/ ”符号被当作除法运算符时有以下几种情况：</p>
<blockquote>
<p>•   如果数值或它的任意部分是存储在一个变量中或是函数的返回值。
•   如果数值被圆括号包围。
•   如果数值是另一个数学表达式的一部分。</p>
</blockquote>
<p>如下所示：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">font</span>: <span class="hljs-number">10px</span>/<span class="hljs-number">8px</span>;             // 纯 CSS，不是除法运算
  $<span class="hljs-attribute">width</span>: <span class="hljs-number">1000px</span>;
  <span class="hljs-attribute">width</span>: $width/<span class="hljs-number">2</span>;            // 使用了变量，是除法运算
  <span class="hljs-attribute">width</span>: <span class="hljs-built_in">round</span>(<span class="hljs-number">1.5</span>)/<span class="hljs-number">2</span>;        // 使用了函数，是除法运算
  <span class="hljs-attribute">height</span>: (<span class="hljs-number">500px</span>/<span class="hljs-number">2</span>);          // 使用了圆括号，是除法运算
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">5px</span> + <span class="hljs-number">8px</span>/<span class="hljs-number">2px</span>; // 使用了加（+）号，是除法运算
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">font</span>: <span class="hljs-number">10px</span>/<span class="hljs-number">8px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">250px</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">9px</span>;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Sass 的除法运算还有一个情况。我们先回忆一下，在乘法运算时，如果两个值带有相同单位时，做乘法运算时，出来的结果并不是我们需要的结果。但在除法运算时，如果两个值带有相同的单位值时，除法运算之后会得到一个不带单位的数值。如下所示：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: (<span class="hljs-number">1000px</span> / <span class="hljs-number">100px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">颜色运算</h3>
<p>所有算数运算都支持颜色值，并且是分段运算的。也就是说，红、绿和蓝各颜色分段单独进行运算。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#010203</span> + <span class="hljs-number">#040506</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算公式为 01 + 04 = 05、02 + 05 = 07 和 03 + 06 = 09， 并且被合成为：</p>
<p>如此编译出来的 CSS 为：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#050709</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>算数运算也能将数字和颜色值 一起运算，同样也是分段运算的。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#010203</span> * <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算公式为 01 * 2 = 02、02 * 2 = 04 和 03 * 2 = 06， 并且被合成为：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#020406</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rgb格式的颜色会先转换为十六进制再进行计算：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>) * <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-attribute">background</span>: <span class="hljs-number">#020202</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">字符运算</h3>
<p>在 Sass 中可以通过加法符号<code>“+</code>”来对字符串进行连接。例如：</p>
<pre><code class="hljs language-css copyable" lang="css">$<span class="hljs-attribute">content</span>: <span class="hljs-string">"Hello"</span> + <span class="hljs-string">""</span> + <span class="hljs-string">"Sass!"</span>;
<span class="hljs-selector-class">.box</span>:before &#123;
  content: <span class="hljs-string">" #&#123;$content&#125; "</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>:before &#123;
  content: <span class="hljs-string">" Hello Sass! "</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了在变量中做字符连接运算之外，还可以直接通过 +，把字符连接在一起：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">cursor</span>: e + -resize;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的CSS:</p>
<pre><code class="copyable">div &#123;
  cursor: e-resize;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，如果有引号的字符串被添加了一个没有引号的字符串 （也就是，带引号的字符串在 + 符号左侧）， 结果会是一个有引号的字符串。 同样的，如果一个没有引号的字符串被添加了一个有引号的字符串 （没有引号的字符串在 + 符号左侧）， 结果将是一个没有引号的字符串。 例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span>:before &#123;
  content: <span class="hljs-string">"Foo "</span> + Bar;
  <span class="hljs-attribute">font-family</span>: sans- + <span class="hljs-string">"serif"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译出来的 CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span>:before &#123;
  content: <span class="hljs-string">"Foo Bar"</span>;
  <span class="hljs-attribute">font-family</span>: sans-serif; &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            