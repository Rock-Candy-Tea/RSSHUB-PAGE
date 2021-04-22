
---
title: '学习JavaScript红宝书（十三）——操作符（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7384'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 23:11:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=7384'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">位操作符</h1>
<p>位操作符用于数值的底层操作，也就是操作内存中表示数据的比特（位）。ECMAScript 中的所有数值都以 IEEE 754 64 位格式存储，但位操作并不直接应用到 64 位表示，而是先把值转换为 32 位整数，再进行位操作，之后再把结果转换为 64 位。对开发者而言，就好像只有 32 位整数一样，因为 64 位整数存储格式是不可见的。所以只需要考虑 32 位整数即可。</p>
<p>有符号整数使用 32 位的前 31 位表示整数值。第 32 位表示数值的符号，如 0 表示正，1 表示负。这一位称为符号位（sign bit）。</p>









































































<table><thead><tr><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th><th>0</th></tr></thead><tbody><tr><td>符号位</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>
<h2 data-id="heading-1">正值</h2>
<p>正值以二进制格式存储。一共 31 位，每一位都是 2 的幂。第一位（第 0 位）表示 2 的 0 次方，第二位表示 2 的 1 次方，依此类推。空位以 0 填充。</p>
<p>比如，数值 18 的二进制格式为 00000000000000000000000000010010，精简为 10010。后者是用到的 5 个有效位：</p>

































<table><thead><tr><th>1</th><th>0</th><th>0</th><th>1</th><th>0</th></tr></thead><tbody><tr><td>1*2**4</td><td>0*2**3</td><td>0*2**2</td><td>1*2**1</td><td>0*2**0</td></tr><tr><td>16</td><td>0</td><td>0</td><td>2</td><td>0</td></tr><tr><td></td><td>和为 18</td><td></td><td></td><td></td></tr></tbody></table>
<h2 data-id="heading-2">负值</h2>
<p>负值以二补数（补码）的二进制编码存储。二补数通过三个步骤计算得到：</p>
<ol>
<li>得到绝对值的二进制</li>
<li>把 1 都变成 0，0 都变成 1，获得一补数（反码）</li>
<li>给结果加 1</li>
</ol>
<p>基于上述步骤确定-18 的二进制表示：</p>
<p>18 的绝对值</p>
<p>0000 0000 0000 0000 0000 0000 0001 0010</p>
<p>计算一补数，即反转每一位的二进制值：</p>
<p>1111 1111 1111 1111 1111 1111 1110 1101</p>
<p>最后，给一补数加 1：</p>
<p>1111 1111 1111 1111 1111 1111 1110 1110</p>
<p>                                                                    1</p>
<hr>
<p>1111 1111 1111 1111 1111 1111 1110 1110</p>
<p>不过在把负值输出为一个二进制字符串时，我们会得到一个前面加了减号的绝对值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num = -<span class="hljs-number">18</span>;
<span class="hljs-built_in">console</span>.log(num.toString(<span class="hljs-number">2</span>)); <span class="hljs-comment">// "-10010"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>默认情况下，ECMAScript 中的所有整数都表示为有符号数。不过，确实存在无符
号整数。对无符号整数来说，第 32 位（第 31 位）不表示符号，因为只有正值。无符号整数比有符号
整数的范围更大，因为符号位被用来表示数值了。</p>
</blockquote>
<p>在对 ECMAScript 中的数值应用位操作符时，后台会发生转换：64 位数值会转换为 32 位数值，然后执行位操作，最后再把结果从 32 位转换为 64 位存储起来。这个转换导致了一个奇特的副作用，特殊值 NaN 和 Infinity 在位操作中会被当成 0 处理。</p>
<p>如果将位操作符应用到非数值，会先用 Number()转换。最终结果是数值。</p>
<h2 data-id="heading-3">按位非</h2>
<p>用~表示，返回数值的一补数（反码）。
按位非可以返回数值的负值并减 1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num1 = <span class="hljs-number">25</span>; <span class="hljs-comment">// 二进制00000000000000000000000000011001</span>
<span class="hljs-keyword">let</span> num2 = ~num1; <span class="hljs-comment">// 二进制11111111111111111111111111100110</span>
<span class="hljs-built_in">console</span>.log(num2); <span class="hljs-comment">// -26</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且这个操作比直接下面这样的速度要快得多：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num1 = <span class="hljs-number">25</span>;
<span class="hljs-keyword">let</span> num2 = -num1 - <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(num2); <span class="hljs-comment">// "-26"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">按位与</h2>
<p>用&表示。按位与会将两个数的每个位对齐，然后基于真值表中的规则，贵每一位执行与操作。</p>






























<table><thead><tr><th>第一个数值的位</th><th>第二个数值的位</th><th>结 果</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr></tbody></table>
<p>我们对数值 25 和 3 进行按位与：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> result = <span class="hljs-number">25</span> & <span class="hljs-number">3</span>;
<span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个过程发生了什么呢？</p>
<p>    25 = 0000 0000 0000 0000 0000 0000 0001 1001</p>
<p>      3 = 0000 0000 0000 0000 0000 0000 0000 0011</p>
<hr>
<p>AND = 0000 0000 0000 0000 0000 0000 0000 0001</p>
<h2 data-id="heading-5">按位或</h2>
<p>用|表示。遵循</p>



































<table><thead><tr><th>第一个数值的位</th><th>第二个数值的位</th><th>结 果</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>其他都和按位与一样，不再重复举例。</td><td></td><td></td></tr></tbody></table>
<h2 data-id="heading-6">按位异或</h2>
<p>用^表示。遵循</p>



































<table><thead><tr><th>第一个数值的位</th><th>第二个数值的位</th><th>结 果</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>同上</td><td></td><td></td></tr></tbody></table>
<h2 data-id="heading-7">左移</h2>
<p>左移操作符用<<表示。会按照指定的位数将数值的所有位向左移动。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> oldValue = <span class="hljs-number">2</span>;
<span class="hljs-keyword">let</span> newValue = oldValue << <span class="hljs-number">5</span>; <span class="hljs-comment">// 64</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数值 2 的二进制是：
10
左移 5 位后得到了：
1000000
这个二进制数的十进制是 64。</p>
<p>左移会保留操作数的符号。如果刚才操作的是-2，得到的就是-64。</p>
<h2 data-id="heading-8">有符号右移</h2>
<p>有符号右移用>>表示。它会将所有的 32 位都往右移，同时保留符号。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> oldValue = <span class="hljs-number">64</span>; <span class="hljs-comment">// 等于二进制1000000</span>
<span class="hljs-keyword">let</span> newValue = oldValue >> <span class="hljs-number">5</span>; <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">无符号右移</h2>
<p>无符号右移用>>>表示。对于正数，操作和有符号右移一样。对于负数则不同。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> oldValue = -<span class="hljs-number">64</span>; <span class="hljs-comment">// 等于二进制11111111111111111111111111000000</span>
<span class="hljs-keyword">let</span> newValue = oldValue >>> <span class="hljs-number">5</span>; <span class="hljs-comment">// 等于十进制134217726</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为 64 的二进制表示是 11111111111111111111111111000000，右移 5 位得到 00000111111111111111111111111110，转换为十进制的 134 217 726。</p>
<h1 data-id="heading-10">相等操作符</h1>
<p>ECMAScript 提供了两组相等操作符，可以按需使用。</p>
<p>第一组是等于和不等于，他们在比较之前执行转换。
第二组是全等和不全等，他们在比较之前不转换。</p>
<h2 data-id="heading-11">等于==和不等于!=</h2>
<p>等于操作符用==表示，如果操作数相等则返回 true，否则返回 false。</p>
<p>不等于操作符用！=表示，如果操作数不相等则返回 true，否则返 false。</p>
<p>这两个操作符都会先进行类型转换（也叫强制类型转换）再确定操作数是否相等。</p>
<p>他们都遵循如下规则：</p>
<ol>
<li>
<p>如果任一操作数是布尔值，则将其转换为数值再比较是否相等。false 转换为 0，true 转换
为 1。</p>
</li>
<li>
<p>如果一个操作数是字符串，另一个操作数是数值，则尝试将字符串转换为数值，再比较是否
相等。</p>
</li>
<li>
<p>如果一个操作数是对象，另一个操作数不是，则调用对象的 valueOf()方法取得其原始值，再
根据前面的规则进行比较。</p>
</li>
</ol>
<p>在进行比较时，这两个操作符会遵循如下规则。</p>
<ol>
<li>
<p>null 和 undefined 相等。</p>
</li>
<li>
<p>null 和 undefined 不能转换为其他类型的值再进行比较。</p>
</li>
<li>
<p>如果有任一操作数是 NaN，则相等操作符返回 false，不相等操作符返回 true。记住：即使两
个操作数都是 NaN，相等操作符也返回 false，因为按照规则，NaN 不等于 NaN。</p>
</li>
<li>
<p>如果两个操作数都是对象，则比较它们是不是同一个对象。如果两个操作数都指向同一个对象，
则相等操作符返回 true。否则，两者不相等。</p>
</li>
</ol>
<p>下面是特殊情况的总结：</p>





















































<table><thead><tr><th>表达式</th><th>结果</th></tr></thead><tbody><tr><td>null == undefined</td><td>true</td></tr><tr><td>"NaN" == NaN</td><td>false</td></tr><tr><td>5 == NaN</td><td>false</td></tr><tr><td>NaN == NaN</td><td>false</td></tr><tr><td>NaN != NaN</td><td>true</td></tr><tr><td>false == 0</td><td>true</td></tr><tr><td>true = 1</td><td>true</td></tr><tr><td>true == 2</td><td>false</td></tr><tr><td>undefined == 0</td><td>false</td></tr><tr><td>null == 0</td><td>false</td></tr><tr><td>"5" == 5</td><td>true</td></tr></tbody></table>
<h2 data-id="heading-12">全等和不全等</h2>
<p>他们在比较相等时不转换操作数。所以他们也要判断数据类型是否相等。</p>
<p>另外，虽然 null == undefined 是 true（因为这两个值类似），但 null === undefined 是 false，因为它们不是相同的数据类型。</p>
<h1 data-id="heading-13">条件操作符</h1>
<p>也被一些人叫做三元操作符。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">variable = boolean_expression ? true_value : false_value;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 boolean_expression 是 true ， 则赋值 true_value ； 如果 boolean_expression 是 false，则赋值 false_value。</p>
<p>活用它可以让代码变得简洁：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> max = num1 > num2 ? num1 : num2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是也不过在条件内过多嵌套条件，会让代码变得难以阅读。</p>
<h1 data-id="heading-14">逗号操作符</h1>
<p>一般用来同时声明多个变量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num1 = <span class="hljs-number">1</span>,
  num2 = <span class="hljs-number">2</span>,
  num3 = <span class="hljs-number">3</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种少见的情况：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num = (<span class="hljs-number">5</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>, <span class="hljs-number">0</span>); <span class="hljs-comment">// num 的值为0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，num 将被赋值为 0，因为 0 是表达式中最后一项。这种情况很少见，但确实存在。</p>
<h1 data-id="heading-15">赋值操作符</h1>
<p>简单赋值用等于号（=）表示，将右手边的值赋给左手边的变量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> num = <span class="hljs-number">10</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复杂赋值使用乘性、加性或位操作符后跟等于号（=）表示：</p>
<ol>
<li>乘后赋值（*=）</li>
<li>除后赋值（/=）</li>
<li>取模后赋值（%=）</li>
<li>加后赋值（+=）</li>
<li>减后赋值（-=）</li>
<li>左移后赋值（<<=）</li>
<li>右移后赋值（>>=）</li>
<li>无符号右移后赋值（>>>=）</li>
</ol>
<p>这些操作符仅仅是简写语法，使用它们不会提升性能。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            