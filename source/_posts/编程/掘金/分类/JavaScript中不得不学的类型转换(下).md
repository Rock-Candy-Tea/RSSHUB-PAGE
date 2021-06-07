
---
title: 'JavaScript中不得不学的类型转换(下)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c2cef6d9456477cb593c9871147c369~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 00:39:18 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c2cef6d9456477cb593c9871147c369~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上篇文章主要介绍了一下各种数据类型转换成Boolean,Number,String的规则。刻意没有去谈到有关于与运算符相关类型转换。这篇就重点讲一下这方面的知识。</p>
<p>上图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c2cef6d9456477cb593c9871147c369~tplv-k3u1fbpfcp-watermark.image" alt="类型转换下.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一元运算符 +</h2>
<p>一元运算符遵从其他类型转Number规则(ToNumber)。</p>
<p><strong>先判断是不是基本数据类型</strong>,如果是</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9a8458c07ea4b75b03181c46c116b24~tplv-k3u1fbpfcp-watermark.image" alt="tonumber.png" loading="lazy" referrerpolicy="no-referrer">
补充Symbol与BigInt</p>
<p>这两种数据类型都不支持隐式类型转换,会报错。</p>
<p><strong>如果是引用数据类型</strong>,用ToPtimitive(obj,Number)这个方法。</p>
<ul>
<li>如果对象具有 valueOf 方法，且返回一个原始值，则 JavaScript 将这个原始值转换为数字并返回这个数字</li>
<li>否则，如果对象具有 <code>toString</code> 方法，且返回一个原始值，则 JavaScript 将其转换并返回。</li>
<li>否则，JavaScript 抛出一个类型错误异常</li>
</ul>
<p>代码实例</p>
<pre><code class="copyable">console.log(+1);   //1
console.log(+"a"); //NaN
console.log(+true); // 1
console.log(+false); // 0
console.log(+null); // 0
console.log(+undefined); // NaN
console.log(+2n); //error
console.log(+Symbol(1));//error
console.log(+[]); //0
console.log(+[2,3,4]); //NaN
console.log(+&#123;&#125;); //NaN
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析一下+[2,3,4]为什么会是NaN.</p>
<ol>
<li>首先数组不是基本数据类型,直接用<code>ToPtimitive(obj,Number)</code>这个方法。</li>
<li>[2,3,4]有valueOf方法但是返回的不是原始数据类型,所以用<code>toString</code>,返回"1,2,3"。</li>
<li>将"1,2,3"转换为数字发现有非法字符,报错。</li>
</ol>
<h2 data-id="heading-1">二元运算符 +</h2>
<p>当计算value1 + value2时,规则如下</p>
<ul>
<li>lprim = ToPrimitive(value1)</li>
<li>rprim = ToPrimitive(value2)</li>
<li>如果 lprim 是字符串或者 rprim 是字符串，那么返回 ToString(lprim) 和 ToString(rprim)的拼接结果</li>
<li>否则返回 ToNumber(lprim) 和 ToNumber(rprim)的运算结果</li>
</ul>
<p>文字比较难理解,我们通过代码举几个例子演示一下。</p>
<p>相同数据类型相加</p>
<pre><code class="copyable">console.log(1 + 1); //2
console.log("a" + "a"); // "aa"
console.log(true + true); //2
console.log(null + null); //0
console.log(undefined + undefined); //NaN
console.log(Symbol(1) + Symbol(2)); //error
console.log(2n + 3n); //5n
console.log(NaN + NaN); //NaN
console.log(&#123;&#125; + &#123;&#125;); // [object Object][object Object] 
console.log([] + []); //""
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不同类型相加</p>
<p>true(Boolean) + 其他</p>
<pre><code class="copyable">console.log(true + "a"); // "truea"
console.log(true + true);// 2
console.log(true + false);// 1
console.log(true + null);// 1
console.log(true + undefined);// NaN
console.log(true + Symbol(1));// error
console.log(true + 2n);// error
console.log(true + []); // "true" 
console.log(true + [1, 2, 3]); // "true1,2,3" 
console.log(true + &#123;&#125;); // "true[object Object] "
<span class="copy-code-btn">复制代码</span></code></pre>
<p>"a"(String) + 其他</p>
<pre><code class="copyable">console.log("a" + "a"); // "aa"
console.log("a" + true); //"atrue"
console.log("a" + false); //"afalse"
console.log("a" + null); // "anull"
console.log("a" + undefined); // "aundefined"
console.log("a" + Symbol(1)); // error
console.log("a" + 2n); // "a2"
console.log("a" + []); // "a"  
console.log("a" + [1, 2, 3]); //"a1,2,3 "
console.log("a" + &#123;&#125;); // "a[object Object] "
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1(Number) +其他</p>
<pre><code class="copyable">console.log(1 + "a"); // "1a"
console.log(1 + true); // 2
console.log(1 + false); // 1
console.log(1 + null); // 1
console.log(1 + undefined); //NaN
console.log(1 + Symbol(1)); // error
console.log(1 + 2n);//error
console.log(1 + []); // "1"
console.log(1 + [1, 2, 3]); //"11,2,3" 
console.log(1 + &#123;&#125;); // "1[object Object]"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出,这么不同的类型相加,如果仅仅是凭借记忆力去强行记忆的话,很容易就会忘记。</p>
<p>但是我们利用规则来解决这些问题的话,就显得轻而易举了。</p>
<p>这里我们针对一些比较难以理解的输出分析一下。
相同类型相加中的</p>
<pre><code class="copyable">console.log(undefined + undefined); //NaN
console.log(&#123;&#125; + &#123;&#125;); // [object Object][object Object] 
console.log([] + []); //""
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接用规则。</p>
<p><code>undefined + undefined </code></p>
<ul>
<li>
<p>左右两边都属于基本数据类型,所以lprim = undefined,  rprim = undefined。</p>
</li>
<li>
<p>两个都不是字符串,所以返回的是ToNumber(lprim) 和 ToNumber(rprim)的运算结果</p>
</li>
<li>
<p>ToNumber(undefined)是什么? 看ToNumber规则发现是NaN</p>
</li>
<li>
<p>NaN + NaN 最终的结果就是NaN</p>
</li>
</ul>
<p><code>&#123;&#125; + &#123;&#125;</code></p>
<ul>
<li>
<p><code>&#123;&#125;</code>属于引用数据类型,所以用ToPrimitive(obj,Number)。</p>
</li>
<li>
<p>先使用<code>&#123;&#125;</code>的valueOf方法,发现返回的不是原始数据类型,于是用toString方法,返回<code>"[object object]"</code>,字符串类型。</p>
</li>
<li>
<p>左右两边都是字符串类型,返回 ToString(lprim) 和 ToString(rprim)的拼接结果。</p>
</li>
<li>
<p><code>"[object object]"</code> + <code>"[object object]"</code> 最终的结果就是<code>"[object object][object object]"</code></p>
</li>
</ul>
<p><code>[] + []</code>这道美味就留给读者老爷们啦。</p>
<p>另外其他的有关于二元运算符+的类型转换,读者老爷们如果有时间可以试着去做一下。有问题的请在文章下方留言,我会问您解答的,如果我解答不了,我会想办法帮您解答的。</p>
<p>还有一点值得注意的是Symbol类型不能用来运算,从上面的结果也可以看出。BigInt也只能和它自己本身运算。</p>
<h2 data-id="heading-2">==相等</h2>
<p>说实话,这玩意用于类型转换的规则实在太多了,而且也不是很规范,所以我建议大家还是去使用更加标准以及严格的===运算符。</p>
<p>不过考虑到部分读者可能会优点强迫症,这里也贴一下具体的规则。</p>
<p><code>"=="</code> 用于比较两个值是否相等，当要比较的两个值类型不一样的时候，就会发生类型的转换。</p>
<p>关于使用"=="进行比较的时候，具体步骤可以查看<a href="http://es5.github.io/#x11.9.3" target="_blank" rel="nofollow noopener noreferrer">规范11.9.5</a>：</p>
<p>当执行x == y 时：</p>
<p>两边的类型是否相同，相同的话就比较值的大小，例如1==2，返回false
判断的是否是null和undefined，是的话就返回true
判断的类型是否是String和Number，是的话，把String类型转换成Number，再进行比较
判断其中一方是否是Boolean，是的话就把Boolean转换成Number，再进行比较
如果其中一方为Object，且另一方为String、Number或者Symbol，会将Object转换成字符串，再进行比较</p>
<p>妈呀,太多了。</p>
<h2 data-id="heading-3">===相等</h2>
<p>===判断是否相等相对于==来说简化了太多,具体来说就一条。</p>
<p>左右两边类型与值是否都完全一致,是就返回true,否则返回false。</p>
<p>但是===存在两个bug，这两个bug其实也存在与==中</p>
<ul>
<li>=== 认为NaN不等于自身,,但是这并不符合人类正常逻辑思维。</li>
<li>还有就是 === 认为+0 与 -0 是完全相同的。</li>
</ul>
<pre><code class="copyable">console.log(NaN === NaN) // false
console.log(+0 === -0) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是在ES6中,Object新增一个is方法修复了这两个bug。</p>
<p>Object.is()的作用与===类型,也是判断两个变量是否相等,但是它修复了NaN不等于自身以及+0等于-0这两个不符合人类正常逻辑思维的bug。</p>
<p><strong>Object.is(), === 和 == 区别</strong></p>
<ul>
<li>两等号判等，会在比较时进行类型转换。</li>
<li>三等号判等（判断严格），比较时不进行隐式类型转换，（类型不同则会返回false）</li>
<li>使用 Object.is 来进行相等判断时，一般情况下和三等号的判断相同，它处理了一些特殊的情况，比如 -0 和 +0 不再相等，两个 NaN 认定为是相等的。</li>
</ul>
<h2 data-id="heading-4">结语</h2>
<p>感谢您看到这里</p></div>  
</div>
            