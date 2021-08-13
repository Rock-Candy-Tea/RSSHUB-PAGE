
---
title: 'Object 类型在ES6中的升级优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1295'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:58:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=1295'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h2 data-id="heading-0">优化部分</h2>
<ol>
<li>
<p>对象属性变量式声明。</p>
<p>ES6 可以直接以变量形式声明对象属性或者方法。比传统的键 值对形式声明更加简洁，更加方便，语义更加清晰。</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> [apple, orange] = [<span class="hljs-string">'red appe'</span>, <span class="hljs-string">'yellow orange'</span>]; 
<span class="hljs-keyword">let</span> myFruits = &#123;apple, orange&#125;; <span class="hljs-comment">//  myFruits = &#123;apple: 'red appe', orange: 'yellow orange'&#125;;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尤其在对象解构赋值(或者模块输出变量时，这种写法的好处体现的最为明显</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> &#123;keys, values, entries&#125; = <span class="hljs-built_in">Object</span>; 
<span class="hljs-keyword">let</span> MyOwnMethods = &#123;keys, values, entries&#125;; 
<span class="hljs-comment">// MyOwnMethods = &#123;keys: keys, values: values, entries: entries&#125; </span>
可以看到属性变量式声明属性看起来更加简洁明了。
方法也可以采用简洁写法： 
<span class="hljs-keyword">let</span> ES5Fun = &#123; <span class="hljs-attr">method</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125; &#125;; <span class="hljs-keyword">let</span> ES6Fun = &#123; <span class="hljs-function"><span class="hljs-title">method</span>(<span class="hljs-params"></span>)</span>&#123;&#125; &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>对象的解构赋值 ES6 对象也可以像数组解构赋值那样，进行变量的解构赋值</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> &#123;apple, orange&#125; = &#123;<span class="hljs-attr">apple</span>: <span class="hljs-string">'red appe'</span>, <span class="hljs-attr">orange</span>: <span class="hljs-string">'yellow orange'</span>&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>对象的扩展运算符(...)</li>
</ol>
<p>ES6 对象的扩展运算符和数组扩展运算符用法本质上差别不大， 毕竟数组也就是特殊的 对象。对象的扩展运算符一个最最常用也最好用的用处就在于可以 轻松的取出一个目标对象内部全部或者部分的可遍历属性，从而进行对象的合并和分解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> &#123;apple, orange, ...otherFruits&#125; = &#123;<span class="hljs-attr">apple</span>: <span class="hljs-string">'red apple'</span>, <span class="hljs-attr">orange</span>: <span class="hljs-string">'yellow orange'</span>, <span class="hljs-attr">grape</span>: <span class="hljs-string">'purple grape'</span>, <span class="hljs-attr">peach</span>: <span class="hljs-string">'sweet peach'</span>&#125;;
<span class="hljs-comment">// otherFruits &#123;grape: 'purple grape', peach: 'sweet peach'&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// 注意: 对象的扩展运算符用在解构赋值时，扩展运算符只能用在最有一个参数 (otherFruits 后面不能再跟其他参数)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> moreFruits = &#123;<span class="hljs-attr">watermelon</span>: <span class="hljs-string">'nice watermelon'</span>&#125;;
<span class="hljs-keyword">let</span> allFruits = &#123;apple, orange, ...otherFruits, ...moreFruits&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>super 关键字 ES6 在 Class 类里新增了类似 this 的关键字super。同 this 总是指向当前函数所在的对象不同，super 关键字总是指向当前函数所在对象的原型对象。</li>
</ol>
<h2 data-id="heading-1">升级部分</h2>
<ol>
<li>ES6 在 Object 原型上新增了 is()方法，做两个目标对象的相等比较，用来完善'==='方 法。'==='方法中 NaN === NaN //false 其实是不合理的，Object.is 修复了这个小 bug。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">NaN</span>, <span class="hljs-literal">NaN</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>ES6 在 Object 原型上新增了 assign()方法，用于对象新增属性或者多个对象合并。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;; 
<span class="hljs-keyword">const</span> source1 = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> source2 = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;; 
<span class="hljs-built_in">Object</span>.assign(target, source1, source2); 
target <span class="hljs-comment">// &#123;a:1, b:2, c:3&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: assign（）合并的对象 target 只能合并 source1、source2 中的自身属性，并不会合并 source1、source2 中的继承属性，也不会合并不可枚举的属性，且无法正确复制 get 和 set 属性（会直接执行 get/set 函数，取 return 的值）。</p>
<ol start="3">
<li>
<p>ES6 在 Object 原型上新增了 getOwnPropertyDescriptors()方法，此方法增强了 ES5 中getOwnPropertyDescriptor()方法，可以获取指定对象所有自身属性的描述对象。结合 defineProperties()方法，可以完美复制对象，包括复制 get 和 set 属性。</p>
</li>
<li>
<p>ES6 在 Object 原型上新增了 getPrototypeOf()和 setPrototypeOf()方法，用来获取或设 置当前对象的 prototype 对象。这个方法存在的意义在于，ES5 中获取设置 prototype 对像是通 过 <code>__proto__</code> 属性来实现的，然而<code>__proto__</code>属性并不是 ES 规范中的明文规定的属性，只是浏览器各大产商“私自”加上去的属性，只不过因为适用范围广而被默认使用了，再非浏览器 环境中并不一定就可以使用，所以为了稳妥起见，获取或设置当前对象的 prototype 对象时，都应该采用 ES6 新增的标准用法。</p>
</li>
<li>
<p>ES6 在 Object 原型上还新增了 Object.keys()，Object.values()，Object.entries()方法， 用来获取对象的所有键、所有值和所有键值对数组。</p>
</li>
</ol></div>  
</div>
            