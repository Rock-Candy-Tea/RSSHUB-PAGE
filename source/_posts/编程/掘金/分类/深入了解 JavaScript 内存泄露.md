
---
title: '深入了解 JavaScript 内存泄露'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1937'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 01:15:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=1937'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><strong>这篇文章是针对浏览器的 JavaScript 脚本，Node.js 大同小异，这里不涉及到 Node.js 的场景。当然 Node.js 作为服务端语言，必然更关注内存泄漏的问题。</strong></p>
<p>用户一般不会在一个 Web 页面停留太久，即使有一点内存泄漏，重载页面内存也会跟着释放。而且浏览器也有自动回收内存的机制，所以也不会特别关注内存泄漏的问题。</p>
<p>但是作为开发人员的我们如果对内存泄漏没有什么概念，有时候还是有可能因为内存泄漏，导致页面卡顿。了解了内存泄漏，就知道该如何避免内存泄漏，这也是我们提升前端技能的必经之路。</p>
<h2 data-id="heading-0">目录</h2>
<h4 data-id="heading-1">内存的概念</h4>
<h4 data-id="heading-2">内存的生命周期</h4>
<h4 data-id="heading-3">内存泄漏是如何产生的</h4>
<h4 data-id="heading-4">造成内存泄漏的场景</h4>
<h4 data-id="heading-5">如何查找内存泄漏</h4>
<hr>
<h3 data-id="heading-6">内存的概念</h3>
<p>内存是计算机中重要的部件之一，它是与CPU进行沟通的桥梁。计算机中所有程序的运行都是在内存中进行的，因此内存的性能对计算机的影响非常大。内存(Memory)也被称为[内部存储器]其作用是用于暂时存放CPU中的运算数据，以及与[硬盘]等[外部存储器]交换的数据。只要计算机在运行中，CPU就会把需要运算的数据调到内存中进行运算，当运算完成后CPU再将结果传送出来，内存的运行也决定了计算机的稳定运行。 内存是由[内存芯片]、电路板、[金手指]等部分组成的。</p>
<h3 data-id="heading-7">内存的生命周期</h3>
<p>内存也是有<strong>生命周期</strong>的，不管什么程序语言，一般可以按顺序分为三个周期：</p>
<ul>
<li>
<p>分配期</p>
<p>分配所需要的内存</p>
</li>
<li>
<p>使用期</p>
<p>使用分配到的内存（读、写）</p>
</li>
<li>
<p>释放期</p>
<p>不需要时将其释放和归还</p>
</li>
</ul>
<p>内存分配 -> 内存使用 -> 内存释放。</p>
<h3 data-id="heading-8">内存泄漏是如何产生的</h3>
<h3 data-id="heading-9">造成内存泄漏的场景</h3>
<h3 data-id="heading-10">如何查找内存泄漏</h3>
<h2 data-id="heading-11">什么是内存泄漏？</h2>
<blockquote>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fzh.wikipedia.org%252Fwiki%252F%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA%25E7%25A7%2591%25E5%25AD%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6" ref="nofollow noopener noreferrer">计算机科学</a>中，<strong>内存泄漏</strong>指由于疏忽或错误造成程序未能释放已经不再使用的<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fzh.wikipedia.org%252Fwiki%252F%25E5%2586%2585%25E5%25AD%2598" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E5%86%85%E5%AD%98" ref="nofollow noopener noreferrer">内存</a>。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。</p>
</blockquote>
<p>如果内存不需要时，没有经过生命周期的<strong>释放期</strong>，那么就存在<strong>内存泄漏</strong>。</p>
<p>内存泄漏简单理解：无用的内存还在占用，得不到释放和归还。比较严重时，无用的内存会持续递增，从而导致整个系统卡顿，甚至崩溃。</p>
<h2 data-id="heading-12">JavaScript 内存管理机制</h2>
<blockquote>
<p>像 C 语言这样的底层语言一般都有底层的内存管理接口，比如 <code>malloc()</code>和<code>free()</code>。相反，JavaScript是在创建变量（对象，字符串等）时自动进行了分配内存，并且在不使用它们时“自动”释放。 释放的过程称为垃圾回收。这个“自动”是混乱的根源，并让JavaScript（和其他高级语言）开发者错误的感觉他们可以不关心内存管理。</p>
</blockquote>
<p>JavaScript 内存管理机制和内存的<strong>生命周期</strong>是一一对应的。首先需要<strong>分配内存</strong>，然后<strong>使用内存</strong>，最后<strong>释放内存</strong>。</p>
<p>其中 JavaScript 语言<strong>不需要程序员手动</strong>分配内存，绝大部分情况下也不需要手动释放内存，对 JavaScript 程序员来说通常就是使用内存（即使用变量、函数、对象等）。</p>
<h3 data-id="heading-13">内存分配</h3>
<p>JavaScript 定义变量就会自动分配内存的。<strong>我们只需了解 JavaScript 的内存是自动分配的就足够了</strong>。</p>
<p>看下内存自动分配的例子：</p>
<pre><code class="copyable">// 给数值变量分配内存
let number = 123; 
// 给字符串分配内存
const string = "xianshannan"; 
// 给对象及其包含的值分配内存
const object = &#123;
  a: 1,
  b: null
&#125;; 
// 给数组及其包含的值分配内存（就像对象一样）
const array = [1, null, "abra"]; 
// 给函数（可调用的对象）分配内存
function func(a)&#123;
  return a;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">内存使用</h3>
<blockquote>
<p>使用值的过程实际上是对分配内存进行<strong>读取与写入</strong>的操作。读取与写入可能是写入一个变量或者一个对象的属性值，甚至传递函数的参数。</p>
</blockquote>
<p>根据上面的内存自动分配例子，我们继续内存使用的例子：</p>
<pre><code class="copyable">// 写入内存
number = 234;
// 读取 number 和 func 的内存，写入 func 参数内存
func(number);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">内存回收</h3>
<p>前端界一般称<strong>垃圾内存回收</strong>为 <code>GC</code>（Garbage Collection，即垃圾回收）。</p>
<p><strong>内存泄漏一般都是发生在这一步，JavaScript 的内存回收机制虽然能回收绝大部分的垃圾内存，但是还是存在回收不了的情况，如果存在这些情况，需要我们手动清理内存。</strong></p>
<p>以前一些老版本的浏览器的 JavaScript 回收机制没那么完善，经常出现一些 bug 的内存泄漏，不过现在的浏览器基本都没这些问题了，已过时的知识这里就不做深究了。</p>
<p>这里了解下现在的 JavaScript 的垃圾内存的两种回收方式，熟悉下这两种算法可以帮助我们理解一些内存泄漏的场景。</p>
<h4 data-id="heading-16">引用计数垃圾收集</h4>
<blockquote>
<p>这是最初级的垃圾收集算法。此算法把“对象是否不再需要”简化定义为“对象有没有其他对象引用到它”。如果没有引用指向该对象（零引用），对象将被垃圾回收机制回收。</p>
</blockquote>
<p>看下下面的例子，“这个对象”的内存被回收了吗？</p>
<pre><code class="copyable">// “这个对象”分配给 a 变量
var a = &#123;
  a: 1,
  b: 2,
&#125;
// b 引用“这个对象”
var b = a; 
// 现在，“这个对象”的原始引用 a 被 b 替换了
a = 1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前执行环境中，“这个对象”内存还没有被回收的，需要手动释放“这个对象”的内存（当然是还没离开执行环境的情况下），例如：</p>
<pre><code class="copyable">b = null;
// 或者 b = 1，反正替换“这个对象”就行了
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样引用的"这个对象"的内存就被回收了。</p>
<p>ES6 把<strong>引用</strong>有区分为<strong>强引用</strong>和<strong>弱引用</strong>，这个目前只有再 Set 和 Map 中才有。</p>
<p><strong>强引用</strong>才会有<strong>引用计数</strong>叠加，只有引用计数为 0 的对象的内存才会被回收，所以一般需要手动回收内存（手动回收的前提在于<strong>标记清除法</strong>还没执行，还处于当前执行环境）。</p>
<p>而<strong>弱引用</strong>没有触发<strong>引用计数</strong>叠加，只要引用计数为 0，弱引用就会自动消失，无需手动回收内存。</p>
<h4 data-id="heading-17">标记清除法</h4>
<blockquote>
<p>当变量进入执行环境时标记为“进入环境”，当变量离开执行环境时则标记为“离开环境”，被标记为“进入环境”的变量是不能被回收的，因为它们正在被使用，而标记为“离开环境”的变量则可以被回收</p>
</blockquote>
<p>环境可以理解为我们的作用域，但是全局作用域的变量只会在页面关闭才会销毁。</p>
<pre><code class="copyable">// 假设这里是全局变量
// b 被标记进入环境
var b = 2;
function test() &#123;
  var a = 1;
  // 函数执行时，a 被标记进入环境
  return a + b;
&#125;
// 函数执行结束，a 被标记离开环境，被回收
// 但是 b 就没有被标记离开环境
test();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">JavaScript 内存泄漏的一些场景</h2>
<p>JavaScript 的内存回收机制虽然能回收绝大部分的垃圾内存，但是还是存在回收不了的情况。程序员要让浏览器内存泄漏，浏览器也是管不了的。</p>
<p><strong>下面有些例子是在执行环境中，没离开当前执行环境，还没触发标记清除法。所以你需要读懂上面 JavaScript 的内存回收机制，才能更好理解下面的场景。</strong></p>
<h3 data-id="heading-19">意外的全局变量</h3>
<pre><code class="copyable">// 在全局作用域下定义
function count(number) &#123;
  // basicCount 相当于 window.basicCount = 2;
  basicCount = 2;
  return basicCount + number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过在 eslint 帮助下，这种场景现在基本没人会犯了，eslint 会直接报错，了解下就好。</p>
<h3 data-id="heading-20">被遗忘的计时器</h3>
<p>无用的计时器忘记清理是新手最容易犯的错误之一。</p>
<p>就拿一个 vue 组件来做例子。</p>
<pre><code class="copyable"><template>
  <div></div>
</template>

<script>
export default &#123;
  methods: &#123;
    refresh() &#123;
      // 获取一些数据
    &#125;,
  &#125;,
  mounted() &#123;
    setInterval(function() &#123;
      // 轮询获取数据
      this.refresh()
    &#125;, 2000)
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的组件销毁的时候，<code>setInterval</code> 还是在运行的，里面涉及到的内存都是没法回收的（浏览器会认为这是必须的内存，不是垃圾内存），需要在组件销毁的时候清除计时器，如下：</p>
<pre><code class="copyable"><template>
  <div></div>
</template>

<script>
export default &#123;
  methods: &#123;
    refresh() &#123;
      // 获取一些数据
    &#125;,
  &#125;,
  mounted() &#123;
    this.refreshInterval = setInterval(function() &#123;
      // 轮询获取数据
      this.refresh()
    &#125;, 2000)
  &#125;,
  beforeDestroy() &#123;
    clearInterval(this.refreshInterval)
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">被遗忘的事件监听器</h3>
<p>无用的事件监听器忘记清理是新手最容易犯的错误之一。</p>
<p>还是继续使用 vue 组件做例子。</p>
<pre><code class="copyable"><template>
  <div></div>
</template>

<script>
export default &#123;
  mounted() &#123;
    window.addEventListener('resize', () => &#123;
      // 这里做一些操作
    &#125;)
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的组件销毁的时候，resize 事件还是在监听中，里面涉及到的内存都是没法回收的（浏览器会认为这是必须的内存，不是垃圾内存），需要在组件销毁的时候移除相关的事件，如下：</p>
<pre><code class="copyable"><template>
  <div></div>
</template>

<script>
export default &#123;
  mounted() &#123;
    this.resizeEventCallback = () => &#123;
      // 这里做一些操作
    &#125;
    window.addEventListener('resize', this.resizeEventCallback)
  &#125;,
  beforeDestroy() &#123;
    window.removeEventListener('resize', this.resizeEventCallback)
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞👍收藏加关注😊，希望点赞多多多多...</strong></p></div>  
</div>
            