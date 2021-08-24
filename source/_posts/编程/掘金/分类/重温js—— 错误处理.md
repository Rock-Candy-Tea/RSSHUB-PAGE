
---
title: '重温js—— 错误处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/311092616eb64515adf99b6108ac2aec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 20:19:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/311092616eb64515adf99b6108ac2aec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>在开发的过程中，遇见错误是很正常的。但是我要知道的是，错误发生的原因和如何去处理错误呢？</p>
</blockquote>
<h1 data-id="heading-0">出现错误的原因</h1>
<blockquote>
<p>在代码的书写中，出现的原因有，代码本身<strong>书写错误</strong>和<strong>运行错误</strong></p>
</blockquote>
<h2 data-id="heading-1">书写错误</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/311092616eb64515adf99b6108ac2aec~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>主流的代码编辑器，如果你的代码是编写错误，那么编辑器一般会提示你报错了，并且给出修改的建议。</p>
</blockquote>
<h2 data-id="heading-2">运行错误</h2>
<blockquote>
<p>代码运行错误分为<strong>运行时候报错</strong>和<strong>预期结果不对</strong></p>
</blockquote>
<h3 data-id="heading-3">运行时报错</h3>
<p>代码的书写中，我们可能没有报错，但是代码在执行的过程中发现错误了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7453c31199154907ad8d6d93a5084a12~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
上面的代码中，我们定义了一个变量，然后当中函数的方法来调用，最后输出一个结果。但是运行期间却报错了，并且下面的代码也是没有执行的，原因是代码报错了会<strong>阻止</strong>程序的运行。我们大家都知道js的解释性语言，代码解释一句然后执行一句，所以后面的代码是不能够直接执行的。</p>
<h3 data-id="heading-4">预期结果不符合</h3>
<p>这个错误是比较难发现的，代码能够正常运行，只是结果不对，我们的逻辑不对。如：</p>
<pre><code class="copyable">function sum (a, b)&#123;
  return a + b;
&#125;
const res  = sum(1, '2');
console.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78b7ccb2ac4e41848d0c190ff73dd26b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的代码我们代码本身没有错，运行也没有报错，只是结果不对，那对于这种问题我们怎么来解决呢？</p>
<h1 data-id="heading-5">解决预期不符合的方法</h1>
<blockquote>
<p>解决这种预期不符合的方法有以下两种， <code>console.log 关键地方输出</code> 和<code>debugger来调试</code></p>
</blockquote>
<h2 data-id="heading-6">console.log 关键地方输出</h2>
<p>使用的方式很简单，在觉得有问题的地方，打印出结果来看就行。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76f880eeec894455a9e64436df3d5931~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
对于这种方法，个人觉得并不是很好，如果代码量多，并且调用的地方多，<code>console.log</code> 就要写很多遍，找到问题后，又需要把这个删除，感觉工作量有点大。</p>
<h2 data-id="heading-7">debugger来调试</h2>
<p>其实启动<code>debugger</code>的方式很简单,在我们的代码中直接书写<code>debugger</code>或者在编辑器的右边打<code>红色的点</code>(vscode为例),然后运行debugger模式。就可以启动<code>debugger</code>;<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/230e990566294419a2224f903eeb82c1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
这个是启动node环境的，还可以在浏览器环境启动。启动的方式也是类似。debugger可以在右侧看到你当前变量的值和类型。非常的方便对于调试。</p>
<h1 data-id="heading-8">抛出错误</h1>
<p>对于我们已经知道代码会报错，我们可以抛出错误。让使用的人知道。<br>
<strong>语法</strong></p>
<pre><code class="copyable">throw new 错误对象
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>常见的错误对象有：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d26687d0374646419152171c11c5117c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
详情请<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Error" ref="nofollow noopener noreferrer">查看</a></p>
</blockquote>
<p>我们可以把我们的代码改造一下：</p>
<pre><code class="copyable">function sum (a, b)&#123;
  if(isNaN(a))&#123;
    throw new TypeError('a must be a number')
  &#125;
  if(isNaN(b))&#123;
    throw new TypeError('b must be a number')
  &#125;
  return a + b;
&#125;

const res  = sum(1, '2');

console.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdef193f8861492d8d8e73072ccbbb0e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>错误堆栈信息</strong><br>
错误堆栈的运行过程是这样的，<code>全局 ---> 局部1 --->局部2</code>. 然而错误的显示信息是 <code>局部2--->局部1--->全局</code>,所以在报错信息的第一行就是我们实际代码throw 的 error。</p>
<h1 data-id="heading-9">捕捉错误</h1>
<p>既然我们可以手动抛出错误，那么必然也是可以进行手动来捕捉错误的。<br>
<strong>语法</strong></p>
<pre><code class="copyable">try&#123;

&#125;catch(错误对象)&#123;

&#125;finally&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>catch</code> 和 <code>finally</code> 可以省略。</p>
<p>改造一下代码。</p>
<pre><code class="copyable">function sum(a, b) &#123;
  if (typeof a !== 'number') &#123;
    throw new TypeError('a must be a number')
  &#125;
  if (typeof b !== 'number') &#123;
    throw new TypeError('b must be a number')
  &#125;
  return a + b;
&#125;
try &#123;
  const res = sum(1, '2');
  console.log(res);
&#125; catch (err) &#123;
  console.log(err);
&#125; finally &#123;
  console.log('一定执行的代码')
&#125;
console.log('其他全局的代码');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26a0d97375a642af80d1e4d9949d4b57~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            