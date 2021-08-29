
---
title: 'JavaScript的装箱📦拆箱'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/674f04a032574be59c395216733fbd02~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:49:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/674f04a032574be59c395216733fbd02~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/674f04a032574be59c395216733fbd02~tplv-k3u1fbpfcp-watermark.image" alt="91qmzewe20q41wupnnge.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>思考下面一个问题：</p>
<h2 data-id="heading-0">为什么num.attr赋值时，没有报错？为什么后面打印num.attr值为undefined？</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> num = <span class="hljs-number">42</span>;
num.attr = <span class="hljs-string">'str'</span>;
<span class="hljs-built_in">console</span>.log(num.attr); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们首先要知道JavaScript中的基本类型有哪些？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// number, string, boolean, undefine, null, symbol, bigint</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这些原始值通过字面量的方式创建的时候没有方法和属性，我们如果需要使用它们就必须使用包装器，而自动装箱就是为了解决这一问题的。</p>
<h2 data-id="heading-1">自动装箱 autoboxing</h2>
<p>自动装箱就是当我们在操作js的基本数据类型（undefined，null除外）时，如<code>str.length</code>，JavaScript会将原始类型包装到对应的对象中，这个新对象链接到相关内置<.prototype>，因此我们可以在原始类型调用原型方法。</p>
<p>回到上面问题：
<code>num.attr</code>当我们给<code>number</code>类型赋值不报错，就是因为执行了下面的动作：</p>
<ul>
<li>创建临时的Number类型的一个实例</li>
<li>调用这个实例对象的赋值方法</li>
<li>拆箱，销毁这个实例</li>
</ul>
<p>代码表示就是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> num = <span class="hljs-number">42</span>;
cosnt _num = New <span class="hljs-built_in">Number</span>(<span class="hljs-number">42</span>); <span class="hljs-comment">// 创建num的临时实例对象</span>
_num.attr = <span class="hljs-string">'str'</span>; <span class="hljs-comment">// 给这个对象增加属性attr并赋值‘str’</span>
_null = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 销毁这个实例</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，我们在进行<code>num.attr</code>赋值的时候，实际上是在操作这个临时的实力对象，所以不会报错。 而当我们再次访问<code>num.attr</code>的时候，会生成新的临时实例对象，所以访问到的属性值是<code>undefined</code>。</p>
<h2 data-id="heading-2">手动装箱</h2>
<p>我们可以通过<code>new</code>操作符来完成手动装箱，例如:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">123</span>);
<span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'str'</span>);
New <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">true</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过要慎重使用手动装箱，可能会有意外的效果，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> bool = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">false</span>);
<span class="hljs-keyword">if</span> (bool) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了true'</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了fasle'</span>);
&#125;
<span class="hljs-comment">// 此时执行结果是 - 执行了true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时<code>bool</code>的值是<code>false</code>，但是<code>new Boolean</code>返回的对象是真值，你可以通过下面这样解决这个问题：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
<span class="hljs-keyword">if</span> (bool.valueOf())
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">拆箱</h2>
<p>上面有提到拆箱，也是存在自动拆箱和手动拆箱，当自动装箱完成，临时实例对象会调用<code>.valueOf()</code>或<code>.toString()</code>来返回原始值。当然你也可以手动调用，实现手动拆箱，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> numObj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">1122</span>);
<span class="hljs-keyword">const</span> strObj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'str'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> numObj); <span class="hljs-comment">// ‘object’</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> strObj); <span class="hljs-comment">// ‘object’</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> numObj.valueOf()); <span class="hljs-comment">// 'number'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> strObj.toString()); <span class="hljs-comment">// 'string'</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">写在最后</h2>
<p>准备后面慢慢总结和巩固自己的知识，也欢迎大家一起学习，如果有不准缺的地方，还欢迎大佬指正。
当然如果上面的文章对您有帮助，还请点赞支持下，万分感谢🙏。</p>
<h2 data-id="heading-5">引用</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjavascript.plainenglish.io%2Fjavascript-boxing-wrappers-5b5ff9e5f6ab" target="_blank" rel="nofollow noopener noreferrer" title="https://javascript.plainenglish.io/javascript-boxing-wrappers-5b5ff9e5f6ab" ref="nofollow noopener noreferrer"># JavaScript Boxing Wrappers</a></p></div>  
</div>
            