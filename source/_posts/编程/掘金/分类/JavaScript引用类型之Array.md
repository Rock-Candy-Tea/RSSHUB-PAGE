
---
title: 'JavaScript引用类型之Array'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef894310dec40f498db15596de1c959~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:45:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef894310dec40f498db15596de1c959~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>JSON是前后端交换文本信息的语法，应用广泛。基于这种语法的特点，后端接口返回得前端渲染的数据不是数组形式的就是对象形式的，所以熟练使用数组和对象的操作方法很重要。</p>
<p><strong>一、不改变原数组的方法</strong></p>
<p>（一）检测方法（非常重要）</p>
<p>可以理解为对数组进行遍历，达到检测目标值终止遍历。检测存在某项达到条件，可以用find()、findIndex和some；检测所有项目都达到条件，使用every()。而这些方法的回调函数，都可以是(item)=>&#123;对item进行检测&#125;的形式。<strong>下面这些检测方法，不会改变原数组。</strong></p>
<p>1、find(）：返回数组中满足提供的测试函数的第一个元素的值，否则返回undefined。</p>
<p>2、findIndex()：返回数组中满足提供的测试函数的第一个元素的<strong>索引</strong>。若没有找到对应元素则返回-1。</p>
<p>3、some()：对数组的每一项运行给定函数，如果该函数对任意一项都返回true，则返回true。</p>
<p>4、every()：对数组的每一项运行给定函数，如果该函数对每一项都返回true，则返回true。</p>
<p>（二）迭代方法（非常重要）</p>
<p>特别是做react的项目，几乎是一定会用到数组的迭代方法的，<strong>下面这些迭代方法，不会改变原数组。</strong></p>
<p>1、forEach():对数组的每一项运行给定函数，没有返回值。</p>
<p>2、filter():对数组的每一项运行给定函数，返回该函数会返回true的项组成的数组。</p>
<p>3、map():对数组的每一项运行给定函数，返回每次调用结果组成的数组。</p>
<p>some()和every()也是迭代方法，归入检测方法就不再列举。过滤数组用filter，重整数据用map，只是想操作值用forEach。</p>
<p>（三）拼接剪切方法</p>
<p>1、colors.concat("yellow")，返回新数组，将接收到的参数添加到当前数组副本的末尾 。</p>
<p>2、colors.slice(1,3)，返回新数组，起始和结束位置之间的项但不包括结束位置的项 。</p>
<p><strong>二、改变数组的方法（非常重要）</strong></p>
<p>react中不直接改变state中的数据，常用不改变原数组的方法。而vue中是可以直接改变data的数据的，使用改变原数组的方法反而更简便。<strong>以下这些方法都是改变数组本身的。</strong></p>
<p>(一）操作方法</p>
<p>1、colors.push("yellow")，在数组前末尾添加项并返回新数组长度 。</p>
<p>2、colors.pop()，移除数组末项并返回该项。</p>
<p>3、colors.shift() ，移除数组第一项并返回该项 。</p>
<p>4、colors.unshift("yellow") ，在数组前端添加项并返回新数组长度 。</p>
<p>5、colors.splice(起始位置、删除项数、插入的项）：这个方法很强大，可以删除、插入或者替换数组元素。</p>
<p>（二）排序方法</p>
<p>1、colors.reverse()，反转数组项顺序 。</p>
<p>2、colors.sort()，默认情况下调用每个数组项的toString()方法转型，比较得到的字符串（字符编码），按升序排序。一般会传入比较方法。</p>
<p><strong>三、归并方法reduce</strong></p>
<p>这个方法很特殊，遍历数组所有项，然后构建一个最新返回的值，这个方法在前端渲染工作中用的比较少。</p>
<p>引用自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FReduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<blockquote>
<p><code>reduce</code>为数组中的每一个元素依次执行<code>callback</code>函数，不包括数组中被删除或从未被赋值的元素，接受四个参数：</p>
<ul>
<li>
<p><code>accumulator 累计器</code></p>
</li>
<li>
<p><code>currentValue 当前值</code></p>
</li>
<li>
<p><code>currentIndex 当前索引</code></p>
</li>
<li>
<p><code>array 数组</code></p>
</li>
</ul>
<p>回调函数第一次执行时，<code>accumulator</code> 和<code>currentValue</code>的取值有两种情况：如果调用<code>reduce()</code>时提供了<code>initialValue</code>，<code>accumulator</code>取值为<code>initialValue</code>，<code>currentValue</code>取数组中的第一个值；如果没有提供 <code>initialValue</code>，那么<code>accumulator</code>取数组中的第一个值，<code>currentValue</code>取数组中的第二个值。</p>
</blockquote>
<p><strong>四、解构赋值用来进行数组合并和拷贝（非常重要）</strong></p>
<p>使用解构赋值进行数组的合并和拷贝不会影响原数组。</p>
<p>1、数组拷贝</p>
<p>拷贝的效果是深拷贝，就是在堆内存中创建了一个新数组，和原数组不是同一个。这个引用类型的简单复制是不一样的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ef894310dec40f498db15596de1c959~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、数组合并</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258e6e65efc84c5ba6f6843a22ed20ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            