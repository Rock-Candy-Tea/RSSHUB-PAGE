
---
title: '海绵宝宝邀您品鉴-JS设计模式(结构型)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7983'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 01:46:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=7983'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">Structural Design Patterns 结构型设计模式</h2>
<h3 data-id="heading-1">关于结构型设计模式</h3>
<p>结构型设计模式主要关注的是 <code>对象组合</code>，也就是实例之间如何互相引用</p>
<h3 data-id="heading-2">结构型设计模式的分类</h3>
<ul>
<li>Adapter 适配器模式</li>
<li>Bridge 桥接模式</li>
<li>Composite 组合模式</li>
<li>Decorator 装饰者模式</li>
<li>Facade 外观模式</li>
<li>Flyweight 享元模式</li>
<li>Proxy 代理模式</li>
</ul>
<h3 data-id="heading-3">适配器模式</h3>
<h4 data-id="heading-4">真实的案例</h4>
<p>想象一下，我们在家中经常会用到插头，比如说手机充电器、电视机插头、电风扇插头、电饭锅插头等，举个例子，我们的电磁炉插头，一般都是三孔插头，某天，我们兴致勃勃，突发奇想想要吃火锅，巴拉巴拉一通搞完所有食材，然后将电磁炉放在桌子的正中央，结果发现我们的插座竟然不支持三孔，这个时候我们就很容易想要去找带有三孔插座的拖线板，然后拖线板的插头是两孔的，这样就能过满足我们的干饭需求了，这个时候，我们找到了拖线板A，A其实是一个整体，暴露出去一个接口（三孔插头），而拖线板A这里其实充当的是适配器的作用，也就是中间做了些包装，使得插座可以调用A暴露出来的接口</p>
<h4 data-id="heading-5">简而言之</h4>
<p>适配器模式允许您将不兼容的对象包装在适配器中以使其与另一个类兼容</p>
<h4 data-id="heading-6">维基百科</h4>
<blockquote>
<p>In software engineering, the adapter pattern is a software design pattern that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.</p>
</blockquote>
<p>在软件工程中，适配器模式是一种软件设计模式，它允许将现有类的接口用作另一个接口。 它通常用于使现有类与其他类一起工作，而无需修改其源代码</p>
<h4 data-id="heading-7">编程案例</h4>
<p>我们来玩一个游戏，游戏中有一个猎人，然后他猎杀狮子</p>
<p>首先我们有一个狮子的接口，所有类型的狮子都会执行一个方法，比如说吼叫</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AfricanLion</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">roar</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AsianLion</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">roar</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后猎人有狩猎的方法，狩猎的过程中狮子可能会吼叫，而对于不同的狮子它们暴露出来的方法是一样的，都是吼叫，具体应该怎么吼，可以在每只狮子内部的 <code>roar</code> 方法中实现</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hunter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">hunt</span>(<span class="hljs-params">lion</span>)</span> &#123;
    <span class="hljs-comment">// ... some code before</span>
    lion.roar();
    <span class="hljs-comment">// ... some code after</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们想在游戏中加入一只野狗，然后猎人也可以狩猎野狗，但是我们不能直接狩猎，因为野狗没有吼叫这个接口，野狗只会吠叫，所以为了使猎人狩猎的接口兼容，我们可以创建一个适配器</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WildDog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">bark</span>(<span class="hljs-params"></span>)</span> &#123;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WildDogAdapter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">dog</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.dog = dog;
  &#125;

  <span class="hljs-function"><span class="hljs-title">roar</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.dog.bark();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以将野狗加入我们的狩猎游戏中，通过调用 <code>WildDogAdapter</code></p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> wildDog = <span class="hljs-keyword">new</span> WildDog();
<span class="hljs-keyword">const</span> wildDogAdapter = <span class="hljs-keyword">new</span> WildDogAdapter(wildDog);

<span class="hljs-keyword">const</span> hunter = <span class="hljs-keyword">new</span> Hunter();
hunter.hunt(wildDogAdapter);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">什么时候使用</h4>
<p>当我们需要去适配第三方接口或者是封装一些旧接口的时候，可以让两个毫不相关的类一起运行，提高了类的复用，但是随着额外对象的创建，存在一定的开销，如果没有必要采用适配器模式，可以进行重构，否则需要完善好文档</p>
<h3 data-id="heading-9">桥接模式</h3>
<h4 data-id="heading-10">真实的案例</h4>
<p>假设你有一个包含很多个页面的网站，而且你还得允许用户更改网站的主题，你会怎么处理呢？为每个主题创建每个页面的多个副本吗？还是只是单独创建主题，根据用户的偏好来加载不同的页面呢？这个时候就用到了桥接模式</p>
<h4 data-id="heading-11">简而言之</h4>
<p>桥接模式组合优于继承，实现的细节是从一个层次结构推送到另一个具有单独层次结构的对象中</p>
<h4 data-id="heading-12">维基百科</h4>
<blockquote>
<p>The bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from its implementation so that the two can vary independently"</p>
</blockquote>
<p>桥接模式是软件工程中使用的一种设计模式，旨在“将抽象与其实现分离，以便两者可以独立变化”</p>
<h4 data-id="heading-13">编程案例</h4>
<p>从上面的例子中来实现我们的网页示例，这里我们有网页层次结构</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">About</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">theme</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.theme = theme;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getContent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'About page in '</span> + <span class="hljs-built_in">this</span>.theme.getColor();
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Careers</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">theme</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.theme = theme;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getContent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Careers page in '</span> + <span class="hljs-built_in">this</span>.theme.getColor();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们有单独的主题结构</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DarkTheme</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getColor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Dark Black'</span>;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LightTheme</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getColor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Off white'</span>;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AquaTheme</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getColor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Light blue'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以将两者层次的组合在一起</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> darkTheme = <span class="hljs-keyword">new</span> DarkTheme();

<span class="hljs-keyword">const</span> about = <span class="hljs-keyword">new</span> About(darkTheme);
<span class="hljs-keyword">const</span> careers = <span class="hljs-keyword">new</span> Careers(darkTheme);

<span class="hljs-built_in">console</span>.log(about.getContent()); <span class="hljs-comment">// "About page in Dark Black"</span>
<span class="hljs-built_in">console</span>.log(careers.getContent()); <span class="hljs-comment">// "Careers page in Dark Black"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">什么时候使用</h4>
<p>当你需要独立管理各组成成分的时候，把抽象化和实现化进行解耦，提高可扩充性，但是大量的类的添加将会导致开发成本的增加和性能的下降</p>
<h3 data-id="heading-15">组合模式</h3>
<h4 data-id="heading-16">真实的案例</h4>
<p>每个公司都是由员工组成的。 每个员工都有相同的特征，即有薪水，有一些责任，可能会或可能不会向某人报告，可能有也可能没有下属等。</p>
<h4 data-id="heading-17">简而言之</h4>
<p>组合模式允许你以统一的方式处理单个对象</p>
<h4 data-id="heading-18">维基百科</h4>
<blockquote>
<p>In software engineering, the composite pattern is a partitioning design pattern. The composite pattern describes that a group of objects is to be treated in the same way as a single instance of an object. The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies. Implementing the composite pattern lets clients treat individual objects and compositions uniformly.</p>
</blockquote>
<p>在软件工程中，复合模式是一种分区设计模式。 组合模式描述了一组对象的处理方式与对象的单个实例相同。 复合的目的是将对象“组合”成树结构以表示部分-整体层次结构。 实现复合模式可以让你统一处理单个对象和组合</p>
<h4 data-id="heading-19">编程案例</h4>
<p>以我们的员工为例。 这里我们有不同的员工类型</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Developer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, salary</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.salary = salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">setSalary</span>(<span class="hljs-params">salary</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.salary = salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getSalary</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getRoles</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.roles;
  &#125;

  <span class="hljs-function"><span class="hljs-title">develop</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">/* */</span>
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Designer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, salary</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.salary = salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;

  <span class="hljs-function"><span class="hljs-title">setSalary</span>(<span class="hljs-params">salary</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.salary = salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getSalary</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.salary;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getRoles</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.roles;
  &#125;

  <span class="hljs-function"><span class="hljs-title">design</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">/* */</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们有一个由几种不同类型的员工组成的组织</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Organization</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.employees = [];
  &#125;

  <span class="hljs-function"><span class="hljs-title">addEmployee</span>(<span class="hljs-params">employee</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.employees.push(employee);
  &#125;

  <span class="hljs-function"><span class="hljs-title">getNetSalaries</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> netSalary = <span class="hljs-number">0</span>;

    <span class="hljs-built_in">this</span>.employees.forEach(<span class="hljs-function"><span class="hljs-params">employee</span> =></span> &#123;
      netSalary += employee.getSalary();
    &#125;);

    <span class="hljs-keyword">return</span> netSalary;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们可以这样使用</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> john = <span class="hljs-keyword">new</span> Developer(<span class="hljs-string">'John Doe'</span>, <span class="hljs-number">12000</span>);
<span class="hljs-keyword">const</span> jane = <span class="hljs-keyword">new</span> Designer(<span class="hljs-string">'Jane'</span>, <span class="hljs-number">10000</span>);

<span class="hljs-keyword">const</span> organization = <span class="hljs-keyword">new</span> Organization();
organization.addEmployee(john);
organization.addEmployee(jane);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'总薪水: '</span>, organization.getNetSalaries()); <span class="hljs-comment">// 总薪水: 22000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">什么时候使用</h4>
<p>当你需要表示对象-整体层次结构，希望用户忽略组合对象和单个对象的不同，统一的使用组合结构中的所有对象方法，反之，我们如果创建太多对象，系统的性能反而会下降</p>
<h3 data-id="heading-21">装饰器模式</h3>
<h4 data-id="heading-22">真实的案例</h4>
<p>想象一下，您经营一家提供多种服务的汽车服务店。 现在你如何计算要收取的账单？ 您选择一项服务并动态地不断添加所提供服务的价格，直到获得最终成本。 在这里，每种类型的服务都是一个装饰器</p>
<h4 data-id="heading-23">简而言之</h4>
<p>装饰器模式允许您通过将对象包装在装饰器类的对象中，在运行时动态更改对象的行为</p>
<h4 data-id="heading-24">维基百科</h4>
<blockquote>
<p>In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern.</p>
</blockquote>
<p>在面向对象的编程中，装饰器模式是一种设计模式，它允许将行为静态或动态地添加到单个对象中，而不会影响来自同一类的其他对象的行为。 装饰器模式对于遵守单一职责原则通常很有用，因为它允许在具有独特关注领域的类之间划分功能</p>
<h4 data-id="heading-25">编程案例</h4>
<p>让我们以咖啡为例。 首先我们有一个简单的<code>coffee</code> 来实现 <code>coffee</code> 接口</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SimpleCoffee</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getCost</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">10</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getDescription</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'Simple coffee'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们希望使代码可扩展，以便在需要时允许选项对其进行修改。 让我们做一些附加功能（装饰器）</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MilkCoffee</span> </span>&#123;
  <span class="hljs-comment">// 牛奶咖啡</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">coffee</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.coffee = coffee;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getCost</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getCost() + <span class="hljs-number">2</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getDescription</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getDescription() + <span class="hljs-string">', milk'</span>;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WhipCoffee</span> </span>&#123;
  <span class="hljs-comment">// 手磨咖啡</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">coffee</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.coffee = coffee;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getCost</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getCost() + <span class="hljs-number">5</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getDescription</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getDescription() + <span class="hljs-string">', whip'</span>;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VanillaCoffee</span> </span>&#123;
  <span class="hljs-comment">// 香草咖啡</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">coffee</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.coffee = coffee;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getCost</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getCost() + <span class="hljs-number">3</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getDescription</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.coffee.getDescription() + <span class="hljs-string">', vanilla'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在让我们泡杯咖啡</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> someCoffee;

someCoffee = <span class="hljs-keyword">new</span> SimpleCoffee();
<span class="hljs-built_in">console</span>.log(someCoffee.getCost()); <span class="hljs-comment">// 10</span>
<span class="hljs-built_in">console</span>.log(someCoffee.getDescription()); <span class="hljs-comment">// Simple Coffee</span>

someCoffee = <span class="hljs-keyword">new</span> MilkCoffee(someCoffee);
<span class="hljs-built_in">console</span>.log(someCoffee.getCost()); <span class="hljs-comment">// 12</span>
<span class="hljs-built_in">console</span>.log(someCoffee.getDescription()); <span class="hljs-comment">// Simple Coffee, milk</span>

someCoffee = <span class="hljs-keyword">new</span> WhipCoffee(someCoffee);
<span class="hljs-built_in">console</span>.log(someCoffee.getCost()); <span class="hljs-comment">// 17</span>
<span class="hljs-built_in">console</span>.log(someCoffee.getDescription()); <span class="hljs-comment">// Simple Coffee, milk, whip</span>

someCoffee = <span class="hljs-keyword">new</span> VanillaCoffee(someCoffee);
<span class="hljs-built_in">console</span>.log(someCoffee.getCost()); <span class="hljs-comment">// 20</span>
<span class="hljs-built_in">console</span>.log(someCoffee.getDescription()); <span class="hljs-comment">// Simple Coffee, milk, whip, vanilla</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">什么时候使用</h4>
<p>当你需要动态地给某个对象添加一些额外的职责时，装饰器模式是一种实现继承的替代方案，在不改变原对象的基础上，通过对其进行包装扩展，使原有对象可以满足用户的更复杂需求，而不会影响从这个类中派生的其他对象，但是多层的装饰会比较复杂</p>
<h3 data-id="heading-27">外观模式</h3>
<h4 data-id="heading-28">真实的案例</h4>
<p>你是怎么打开电脑的？ “按下电源按钮” 你说！ 这就是你所深信不疑的，因为您使用的是计算机在外部提供的开机接口，在内部它必须做很多事情才能实现。 这个复杂子系统的简单接口是一个外观模式</p>
<h4 data-id="heading-29">简而言之</h4>
<p>外观模式为复杂的子系统提供了一个简化的接口</p>
<h4 data-id="heading-30">维基百科</h4>
<blockquote>
<p>A facade is an object that provides a simplified interface to a larger body of code, such as a class library.</p>
</blockquote>
<p>外观是一个对象，它为更大的代码结构体（例如类库）提供简化的接口</p>
<h4 data-id="heading-31">编程案例</h4>
<p>以上面的计算机为例， 这里有一个 <code>Computer</code> 类</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Computer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getElectricShock</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Ouch!'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">makeSound</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Beep beep!'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">showLoadingScreen</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Loading..'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">bam</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Ready to be used!'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">closeEverything</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Bup bup bup buzzzz!'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">sooth</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Zzzzz'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">pullCurrent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Haaah!'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们来定义 <code>Computer</code> 的外观</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ComputerFacade</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">computer</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.computer = computer;
  &#125;

  <span class="hljs-function"><span class="hljs-title">turnOn</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.computer.getElectricShock();
    <span class="hljs-built_in">this</span>.computer.makeSound();
    <span class="hljs-built_in">this</span>.computer.showLoadingScreen();
    <span class="hljs-built_in">this</span>.computer.bam();
  &#125;

  <span class="hljs-function"><span class="hljs-title">turnOff</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.computer.closeEverything();
    <span class="hljs-built_in">this</span>.computer.pullCurrent();
    <span class="hljs-built_in">this</span>.computer.sooth();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在让我们使用外观提供的接口</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> computer = <span class="hljs-keyword">new</span> ComputerFacade(<span class="hljs-keyword">new</span> Computer());
computer.turnOn(); 
<span class="hljs-comment">// Ouch! </span>
<span class="hljs-comment">// Beep beep! </span>
<span class="hljs-comment">// Loading.. </span>
<span class="hljs-comment">// Ready to be used!</span>
computer.turnOff(); 
<span class="hljs-comment">// Bup bup bup buzzz! </span>
<span class="hljs-comment">// Haaah! </span>
<span class="hljs-comment">// Zzzzz</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">什么时候使用</h4>
<p>经典的三层结构，在数据访问层和业务逻辑层、业务逻辑层和表示层之间建立外观Facade，增加外观Facade可以提供一个简单的接口，减少子系统之间的依赖，提高了灵活性和安全性，但是不符合开闭原则，继承和重写都比较复杂</p>
<h3 data-id="heading-33">享元模式</h3>
<h4 data-id="heading-34">真实的案例</h4>
<p>你有没有从某个摊位喝过早茶？ 他们通常会制作很多份的早茶，所以一般都会一锅煮，给你来一杯茶后，并将其余的留给任何其他客户，以节省资源，例如 空气等。享元模式就是关于共享的</p>
<h4 data-id="heading-35">简而言之</h4>
<p>它用于通过尽可能多地与相似对象共享来最小化内存使用或计算开销</p>
<h4 data-id="heading-36">维基百科</h4>
<blockquote>
<p>In computer programming, flyweight is a software design pattern. A flyweight is an object that minimizes memory use by sharing as much data as possible with other similar objects it is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory.</p>
</blockquote>
<p>在计算机编程中，享元是一种软件设计模式。 享元是一种通过与其他类似对象共享尽可能多的数据来最小化内存使用的对象，当简单的重复表示会使用不可接受的内存量时，它是一种使用大量对象的方法</p>
<h4 data-id="heading-37">编程案例</h4>
<p>以上面我们喝茶为例子， 首先我们有 <code>Tea</code> 类和 <code>TeaMaker</code> 制茶人</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KarakTea</span> </span>&#123;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TeaMaker</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.availableTea = &#123;&#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">make</span>(<span class="hljs-params">preference</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.availableTea[preference] = <span class="hljs-built_in">this</span>.availableTea[preference] || (<span class="hljs-keyword">new</span> KarakTea());
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.availableTea[preference];
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们有创建订单以及为客户服务的 <code>TeaShop</code></p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TeaShop</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">teaMaker</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.teaMaker = teaMaker;
    <span class="hljs-built_in">this</span>.orders = [];
  &#125;

  <span class="hljs-function"><span class="hljs-title">takeOrder</span>(<span class="hljs-params">teaType, table</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.orders[table] = <span class="hljs-built_in">this</span>.teaMaker.make(teaType);
  &#125;

  <span class="hljs-function"><span class="hljs-title">serve</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.orders.forEach(<span class="hljs-function">(<span class="hljs-params">order, index</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Serving tea to table#'</span> + index);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以这样使用，此时如果你的 <code>teaType</code> 没有改变的话，使用的就是现有的创建的 <code>KarakTea</code> 实例</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> teaMaker = <span class="hljs-keyword">new</span> TeaMaker();
<span class="hljs-keyword">const</span> shop = <span class="hljs-keyword">new</span> TeaShop(teaMaker);

shop.takeOrder(<span class="hljs-string">'less sugar'</span>, <span class="hljs-number">1</span>);
shop.takeOrder(<span class="hljs-string">'more milk'</span>, <span class="hljs-number">2</span>);
shop.takeOrder(<span class="hljs-string">'without sugar'</span>, <span class="hljs-number">5</span>);

shop.serve();
<span class="hljs-comment">// Serving tea to table# 1</span>
<span class="hljs-comment">// Serving tea to table# 2</span>
<span class="hljs-comment">// Serving tea to table# 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">什么时候使用</h4>
<p>运用共享技术有效地支持大量细粒度对象的复用。系统只使用少量的对象，而这些对象都很相似，状态变化很小，可以实现对象的多次复用，如果一个应用程序使用了大量的对象，而这些大量的对象造成了很大的存储开销时就应该考虑使用享元模式，提高效率，但是需要注意需要分离出内部和外部的状态，且外部状态具有固有化的性质</p>
<h3 data-id="heading-39">代理模式</h3>
<h4 data-id="heading-40">真实的案例</h4>
<p>您是否曾经使用门禁卡通过门？ 打开那扇门有多种选择，即可以使用门禁卡或密码或指纹或钥匙打开它。 这扇门的主要功能是打开，但在它上面添加了一个代理来添加一些功能。 让我使用下面的代码示例更好地解释它</p>
<h4 data-id="heading-41">简而言之</h4>
<p>使用代理模式，一个类代表另一个类的功能</p>
<h4 data-id="heading-42">维基百科</h4>
<blockquote>
<p>A proxy, in its most general form, is a class functioning as an interface to something else. A proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes. Use of the proxy can simply be forwarding to the real object, or can provide additional logic. In the proxy extra functionality can be provided, for example caching when operations on the real object are resource intensive, or checking preconditions before operations on the real object are invoked.</p>
</blockquote>
<p>代理，就其最一般的形式而言，是一个充当其他事物接口的类。 代理是一个包装器或代理对象，你调用它来访问幕后的真实服务对象。 代理的使用可以简单地转发到真实对象，或者可以提供额外的逻辑。 在代理中可以提供额外的功能，例如当真实对象上的操作是资源密集型时缓存，或者在调用真实对象上的操作之前检查先决条件</p>
<h4 data-id="heading-43">编程案例</h4>
<p>以上面开始我们开门为例， 首先，我们有 <code>Door</code> 类 和 门上的一些方法</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LabDoor</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">open</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Opening lab door'</span>);
  &#125;

  <span class="hljs-function"><span class="hljs-title">close</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Closing the lab door'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们有一个代理来保护我们想要打开的门</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Security</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">door</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.door = door;
  &#125;

  <span class="hljs-function"><span class="hljs-title">open</span>(<span class="hljs-params">password</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.authenticate(password)) &#123;
      <span class="hljs-built_in">this</span>.door.open();
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Oh no! password failed!'</span>);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">authenticate</span>(<span class="hljs-params">password</span>)</span> &#123;
    <span class="hljs-keyword">return</span> password === <span class="hljs-string">'qwerdf'</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">close</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.door.close();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以这样使用</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> door = <span class="hljs-keyword">new</span> Security(<span class="hljs-keyword">new</span> LabDoor());
door.open(<span class="hljs-string">'invalid'</span>); <span class="hljs-comment">// Oh no! password failed!</span>

door.open(<span class="hljs-string">'qwerdf'</span>); <span class="hljs-comment">// Opening lab door</span>
door.close(); <span class="hljs-comment">// Closing lab door</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">什么时候使用</h4>
<p>当我们需要在到达目标对象之前，做一些额外的逻辑，可以考虑使用代理模式，代理模式能将代理对象与被调用对象分离，降低了系统的耦合度。代理模式在客户端和目标对象之间起到一个中介作用，这样可以起到保护目标对象的作用，代理对象可以扩展目标对象的功能；通过修改代理对象就可以了，符合开闭原则，但是代理模式由于不是直接访问，所以在时间上存在一定的开销，最直接的例子就是前端在请求后端接口时中间会有一层转发的动作，主要目的是为了保护后端接口不被暴露</p>
<h2 data-id="heading-45">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsohamkamani%2Fjavascript-design-patterns-for-humans" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sohamkamani/javascript-design-patterns-for-humans" ref="nofollow noopener noreferrer">Javascript 设计模式</a></li>
<li>《Javascript设计模式——张容铭》</li>
</ul></div>  
</div>
            