
---
title: 'Typescript的Enums'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2101'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 20:43:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=2101'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>大家好，这是一个更文挑战。这是我参与8月更文挑战的第<code>8</code>天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>ts为js引入了一个新的概念Enums，我们一起看看怎么使用的吧！！</p>
</blockquote>
<h2 data-id="heading-0">Enums：全称Enumerations</h2>
<blockquote>
<p>用来定义一些<strong>带名字的常量</strong>。 使用枚举可以清晰地表达意图或创建一组有区别的用例。 TypeScript支持<strong>数字</strong>的和基于<strong>字符串</strong>的枚举。</p>
</blockquote>
<blockquote>
<p>注意： ts支持<strong>数字</strong>和<strong>字符串</strong>的枚举</p>
</blockquote>
<h3 data-id="heading-1">定义enums变量: 以enums关键字开头,<strong>变量名（首字母大写）</strong></h3>
<pre><code class="hljs language-js copyable" lang="js">enum Pet &#123;
    Dog,
    Cat,
    Goldfish
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，默认的<code>Dog</code>的值为<code>0</code>,<code>Cat</code>的值为<code>1</code>,...以此类推, 默认值是以自增长的</p>
<p><strong>1. 现在要是给Dog一个默认值，那后面的值会是什么呢？</strong></p>
<pre><code class="hljs language-js copyable" lang="js">enum Pet &#123;
    Dog=<span class="hljs-number">4</span>,
    Cat,
    Goldfish
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 <code>Dog</code>的值为<code>4</code>,<code>Cat</code>的值为<code>5</code>,...以自增长的方式给后面的赋值</p>
<p><strong>2. 要是不想让他们的值是自增长的呢？ 可以给每个赋一个值</strong></p>
<pre><code class="hljs language-js copyable" lang="js">enum Pet &#123;
    Dog=<span class="hljs-number">4</span>,
    Cat=<span class="hljs-number">2</span>,
    Goldfish=<span class="hljs-number">34</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 <code>Dog</code>的值为<code>4</code>,<code>Cat</code>的值为<code>2</code>，<code>Goldfish</code>的值为<code>34</code>，<strong>都为数字类型</strong></p>
<p><strong>3. Enum的值也可以是都是字符串类型</strong></p>
<pre><code class="hljs language-js copyable" lang="js">enum Pet &#123;
    Dog=<span class="hljs-string">"hahah"</span>,
    Cat=“lalal”,
    Goldfish=“enenen”
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 <code>Dog</code>的值为<code>hahah</code>,<code>Cat</code>的值为<code>lalal</code>，<code>Goldfish</code>的值为<code>enenen</code>，<strong>都为字符串类型</strong></p>
<p><strong>4. Enum的值可以字符串和数字混合用吗？理论上可以，但是不建议</strong></p>
<pre><code class="hljs language-js copyable" lang="js">enum Pet &#123;
    Dog=<span class="hljs-string">"hahah"</span>,
    Cat=<span class="hljs-number">44</span>,
    Goldfish=“enenen”
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这种做法不建议</p>
<p><strong>4. Enum的值还可以是<code>函数</code>，但是只有一个函数的时候要放在<code>最后一个</code>，否则会<code>出错</code></strong></p>
<blockquote>
<p>注意事项： <strong>函数要有<code>返回值</code></strong></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">22</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 下面这个是错❌的</span>
enum Pet &#123;
    Dog=getName(),
    Cat,
    Goldfish
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 下面这个是对的</span>
enum Pet &#123;
    Dog,
    Cat,
    Goldfish=getName()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，默认的<code>Dog</code>的值为<code>0</code>,<code>Cat</code>的值为<code>1</code>,<code>Goldfish</code>的值为<code>22</code></p>
<p><strong>5. enum可以计算</strong></p>
<pre><code class="hljs language-js copyable" lang="js">enum Animal &#123;
    Head,
    Eye,
    Leg
&#125;

enum People &#123;
   <span class="hljs-attr">Head</span>: Animal.Head,
   <span class="hljs-attr">Eye</span>:<span class="hljs-number">1</span>+<span class="hljs-number">1</span>,
   <span class="hljs-attr">Leg</span>:<span class="hljs-number">2</span>*<span class="hljs-number">2</span>,
   <span class="hljs-attr">Mouth</span>:Head
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Animal</code>里面的值我们都知道分别是：<code>Head</code>的值为<code>0</code>,<code>Eye</code>的值为<code>1</code>,<code>Leg</code>的值为<code>2</code>，那<code>People</code>的值分别是什么呢？<code>Head</code>的值为<code>0</code>,<code>Eye</code>的值为<code>2</code>,<code>Leg</code>的值为<code>4</code>，<code>Mouth</code>的值为<code>0</code></p>
<h2 data-id="heading-2">总结</h2>
<ol>
<li>为什么使用enum？</li>
</ol>
<blockquote>
<p>Enums使得代码更加语义话，能够被更好的维护</p>
</blockquote>
<ol start="2">
<li>什么时候使用？</li>
</ol>
<blockquote>
<p>变量的值在一个固定的范围区间内，比如：红绿灯，只有3种。年级，1-9年级。键盘上的上下左右，只有4个按键...，诸如此类的，有固定范围的都可以定义为enum类型</p>
</blockquote>
<p>希望各位看官喜欢这篇关于ts的enums入门的文章！！！</p></div>  
</div>
            