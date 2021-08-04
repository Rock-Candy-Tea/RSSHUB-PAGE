
---
title: 'vue修饰符(事件修饰符、v-model修饰符、键盘修饰符、自定义键盘修饰符)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9642'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 02:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9642'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">事件修饰符</h2>
<p><code>.stop:</code>阻止事件冒泡，相当于调用了 event.stopPropagation()方法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.prevent:</code> 阻止默认行为，相当于调用了 event.preventDefault()方法，比如表单的提交、
a 标签的跳转就是默认事件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">""</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.self:</code>  只有点击元素本身才会触发。比如一个 div里面有个按钮， div 和按钮都有事件，我们点击按钮， div 绑定的方法也会触发，如果 div的 click 加上 self，只有点击到 div 的时候才会触发，变相的算是阻止冒泡。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.self</span>=<span class="hljs-string">"test"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.once:</code> 事件只能触发一次，无论点击多少次，执行第一次之后就不执行了</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.once</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.captrue:</code> 捕获冒泡，即有冒泡发生时，有该修饰符的dom元素会先执行，如果有多个，从外到内依次执行，然后再按自然顺序执行触发的事件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"obj1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"doc"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"obj2"</span> @<span class="hljs-attr">click.capture</span>=<span class="hljs-string">"doc"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"obj3"</span> @<span class="hljs-attr">click.capture</span>=<span class="hljs-string">"doc"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"obj4"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"doc"</span>></span>
                <span class="hljs-comment"><!-- 点击obj4的时候，弹出的顺序为：obj2、obj3、obj4、obj1；因为2有.captrue修饰符，故而先触发事件，由外到内，然后就是4本身触发，最后冒泡事件。--></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">v-model 修饰符</h2>
<p><code>.lazy:</code> 默认情况下，v-model同步输入框的值和数据。可以通过这个修饰符，让光标离开input框数据再同步</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.lazy</span>=<span class="hljs-string">"value"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.number:</code> 自动将用户的输入值转化为数值类型</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"value"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.trim:</code> 过滤输入框首尾的空格</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.trim</span>=<span class="hljs-string">"value"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">键盘修饰符</h2>
<blockquote>
<p>Vue 提供了绝大多数常用的按键码的别名</p>
</blockquote>

<p><code>.enter</code></p>
<p><code>.tab</code></p>
<p><code>.delete</code></p>
<p><code>.esc</code></p>
<p><code>.space</code></p>
<p><code>.up</code></p>
<p><code>.down</code></p>
<p><code>.left</code></p>
<p><code>.right</code></p>
<h2 data-id="heading-3">自定义键盘修饰符</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"按下F5"</span> @<span class="hljs-attr">keyup.f5</span>=<span class="hljs-string">"handle"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            