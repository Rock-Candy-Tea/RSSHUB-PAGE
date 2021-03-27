
---
title: '一次Javascript的计算浮点数精度问题记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc6cdbb30f044374b86143cdd065632c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 00:11:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc6cdbb30f044374b86143cdd065632c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>在最近的项目中，会设计到金额单位的变化，比如分和元之间的互相转换。</p>
<p>但是偶然中在计算<code>4.35 * 100</code>时，返回的结果并不是预期的<code>435</code>，而是<code>434.99999999999994</code>。意识到，可能遇见JavaScript中的经典问--<code>0.1 + 0.2</code>是否等于<code>0.3</code>了。</p>
<h1 data-id="heading-1">原因分析</h1>
<h2 data-id="heading-2"><code>0.1</code>转二进制是无限循环的</h2>
<p>我们知道在计算机中数据都是以二进制来保存的，而将10进制的小数转为二进制数据，采用<strong>乘2取整，顺序排列</strong>。</p>
<blockquote>
<p>具体做法是：用2乘十进制小数，可以得到积，将积的整数部分取出，再用2乘余下的小数 部分，又得到一个积，再将积的整数部分取出，如此进行，直到积中的小数部分为零，或者达到所要求的精度为止。</p>
</blockquote>
<p>比如，例如把<code>0.8125</code>转换为二进制小数：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc6cdbb30f044374b86143cdd065632c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么，根据上面的内容，我们将<code>0.1</code>转换为二进制小数的步骤如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0.1</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.2</span>
<span class="hljs-number">0.2</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.4</span> <span class="hljs-comment">// 注意这里</span>
<span class="hljs-number">0.4</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.8</span>
<span class="hljs-number">0.8</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.6</span>
<span class="hljs-number">0.6</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.2</span>
<span class="hljs-number">0.2</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.4</span> <span class="hljs-comment">// 注意这里，循环开始</span>
<span class="hljs-number">0.4</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.8</span>
<span class="hljs-number">0.8</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.6</span>
<span class="hljs-number">0.6</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.2</span>
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，由于最后一位不是以5结尾（仅<code>0.5 * 2</code>才能得出整数），所以最后得到的二进制数据是一个<strong>无限二进制小数<code>0.00011001100...</code></strong>。</p>
<h2 data-id="heading-3">Javascript的精度</h2>
<p>在Javascript中整数和小数都遵循<code>IEEE 754</code>标准（即标准的<code>double</code>双精度浮点数），使用64位固定长度来表示。</p>
<p>在该规则中，数据在计算机中保存结构如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2612aba66b944bca3b1ec19f7507019~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>sign(符号): 占 1 bit, 表示正负;</li>
<li>exponent(指数): 占 11 bit，表示范围;</li>
<li>mantissa(尾数): 占 52 bit，表示精度，多出的末尾如果是 1 需要进位;</li>
</ul>
<p>再根据下面的公式，我们计算出二进制数据<code>V</code>：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb08a99f80c84608a4fd02fe27e69ac4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里，我们以上面的<code>0.1</code>为例，对应二进制数据<code>0.00011001100...</code>，用科学计数法表示为<code>1.100110011... x 2^(-4)</code>，根据上述公式，S为<code>0</code>(1 bit)，E为<code>-4 + 1023</code>，对应的二进制为<code>01111111011</code>(11 bit)，M为<code>1001100110011001100110011001100110011001100110011010</code>。</p>
<p>这里我们可以看到，<strong><code>0.1</code>的精度在JavaScript中丢失了</strong>。</p>
<p>同样的道理，<code>0.2</code>在JavaScript为<code>0.0011001100110011001100110011001100110011001100110011010</code>，也会存在精度丢失的情况。</p>
<p>那么，<code>0.1+0.2</code>得出二进制数据如下，结果转为10进制则为<code>0.30000000000000004</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 计算过程</span>
<span class="hljs-number">0.00011001100110011001100110011001100110011001100110011010</span>
<span class="hljs-number">0.0011001100110011001100110011001100110011001100110011010</span>

<span class="hljs-comment">// 相加得</span>
<span class="hljs-number">0.01001100110011001100110011001100110011001100110011001110</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">解决方案</h1>
<p>项目出现了问题，就得解决。通过和团队其他伙伴沟通，找到了一个第三方库<a href="https://github.com/nefe/number-precision" target="_blank" rel="nofollow noopener noreferrer">number-precision</a>，来解决这个问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> NP <span class="hljs-keyword">from</span> <span class="hljs-string">'number-precision'</span>

NP.strip(<span class="hljs-number">0.09999999999999998</span>); <span class="hljs-comment">// = 0.1</span>
NP.times(<span class="hljs-number">3</span>, <span class="hljs-number">0.3</span>);              <span class="hljs-comment">// 3 * 0.3 = 0.9, not 0.8999999999999999</span>
NP.divide(<span class="hljs-number">1.21</span>, <span class="hljs-number">1.1</span>);          <span class="hljs-comment">// 1.21 / 1.1 = 1.1, not 1.0999999999999999</span>
NP.plus(<span class="hljs-number">0.1</span>, <span class="hljs-number">0.2</span>);             <span class="hljs-comment">// 0.1 + 0.2 = 0.3, not 0.30000000000000004</span>
NP.minus(<span class="hljs-number">1.0</span>, <span class="hljs-number">0.9</span>);            <span class="hljs-comment">// 1.0 - 0.9 = 0.1, not 0.09999999999999998</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面简单分析下源码。</p>
<h2 data-id="heading-5">NP.strip</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 把错误的数据转正
 * strip(0.09999999999999998)=0.1
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strip</span>(<span class="hljs-params">num: numType, precision = <span class="hljs-number">15</span></span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> +<span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">Number</span>(num).toPrecision(precision));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，这里使用了<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/toPrecision" target="_blank" rel="nofollow noopener noreferrer">toPrecision</a>方法。</p>
<blockquote>
<p>toPrecision以定点表示法或指数表示法表示的一个数值对象的字符串表示，四舍五入到 precision 参数指定的显示数字位数。</p>
</blockquote>
<p>以<code>0.09999999999999998</code>为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0.09999999999999998</span>.toPrecision(<span class="hljs-number">15</span>) <span class="hljs-comment">// 输出字符串："0.100000000000000"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再通过<code>parseFloat</code>方法，将返回的字符串转换为对应的浮点数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseFloat</span>(<span class="hljs-number">0.09999999999999998</span>.toPrecision(<span class="hljs-number">15</span>)) <span class="hljs-comment">// 输出数字：0.1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">NP.times</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 精确乘法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">times</span>(<span class="hljs-params">num1: numType, num2: numType, ...others: numType[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (others.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> times(times(num1, num2), others[<span class="hljs-number">0</span>], ...others.slice(<span class="hljs-number">1</span>));
  &#125;
  <span class="hljs-keyword">const</span> num1Changed = float2Fixed(num1);
  <span class="hljs-keyword">const</span> num2Changed = float2Fixed(num2);
  <span class="hljs-keyword">const</span> baseNum = digitLength(num1) + digitLength(num2);
  <span class="hljs-keyword">const</span> leftValue = num1Changed * num2Changed;

  checkBoundary(leftValue);

  <span class="hljs-keyword">return</span> leftValue / <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, baseNum);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法前半部分，通过递归用于实现两个以上参数相乘。我们主要看后半部分的逻辑。</p>
<p>这里先介绍几个前置函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Return digits length of a number
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*number&#125;</span> </span>num Input number
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">digitLength</span>(<span class="hljs-params">num: numType</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-comment">// Get digit length of e</span>
  <span class="hljs-keyword">const</span> eSplit = num.toString().split(<span class="hljs-regexp">/[eE]/</span>);
  <span class="hljs-keyword">const</span> len = (eSplit[<span class="hljs-number">0</span>].split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">1</span>] || <span class="hljs-string">''</span>).length - +(eSplit[<span class="hljs-number">1</span>] || <span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> len > <span class="hljs-number">0</span> ? len : <span class="hljs-number">0</span>;
&#125;

<span class="hljs-comment">/**
 * 把小数转成整数，支持科学计数法。如果是小数则放大成整数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*number&#125;</span> </span>num 输入数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">float2Fixed</span>(<span class="hljs-params">num: numType</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (num.toString().indexOf(<span class="hljs-string">'e'</span>) === -<span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(num.toString().replace(<span class="hljs-string">'.'</span>, <span class="hljs-string">''</span>));
  &#125;
  <span class="hljs-keyword">const</span> dLen = digitLength(num);
  <span class="hljs-keyword">return</span> dLen > <span class="hljs-number">0</span> ? strip(<span class="hljs-built_in">Number</span>(num) * <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, dLen)) : <span class="hljs-built_in">Number</span>(num);
&#125;

<span class="hljs-comment">/**
 * 检测数字是否越界，如果越界给出提示
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*number&#125;</span> </span>num 输入数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkBoundary</span>(<span class="hljs-params">num: number</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_boundaryCheckingState) &#123;
    <span class="hljs-keyword">if</span> (num > <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER || num < <span class="hljs-built_in">Number</span>.MIN_SAFE_INTEGER) &#123;
      <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;num&#125;</span> is beyond boundary when transfer to integer, the results may not be accurate`</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看出，乘法的逻辑就是先放大，再缩小。先将小数转换为整数，再进行相乘，最后再将结果按照所有相乘数据的小数之和进行缩小。</p>
<h2 data-id="heading-7">NP.divide</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 精确除法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">divide</span>(<span class="hljs-params">num1: numType, num2: numType, ...others: numType[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (others.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> divide(divide(num1, num2), others[<span class="hljs-number">0</span>], ...others.slice(<span class="hljs-number">1</span>));
  &#125;
  <span class="hljs-keyword">const</span> num1Changed = float2Fixed(num1);
  <span class="hljs-keyword">const</span> num2Changed = float2Fixed(num2);
  checkBoundary(num1Changed);
  checkBoundary(num2Changed);
  <span class="hljs-comment">// fix: 类似 10 ** -4 为 0.00009999999999999999，strip 修正</span>
  <span class="hljs-keyword">return</span> times(num1Changed / num2Changed, strip(<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, digitLength(num2) - digitLength(num1))));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除法在乘法的基础之上进行调整，将待操作数据转变为整数，先进行相除。再按照小数位的差值，进行放大&缩小。</p>
<h2 data-id="heading-8">NP.plus和NP.minus</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 精确加法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">plus</span>(<span class="hljs-params">num1: numType, num2: numType, ...others: numType[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (others.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> plus(plus(num1, num2), others[<span class="hljs-number">0</span>], ...others.slice(<span class="hljs-number">1</span>));
  &#125;
  <span class="hljs-keyword">const</span> baseNum = <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, <span class="hljs-built_in">Math</span>.max(digitLength(num1), digitLength(num2)));
  <span class="hljs-keyword">return</span> (times(num1, baseNum) + times(num2, baseNum)) / baseNum;
&#125;

<span class="hljs-comment">/**
 * 精确减法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">minus</span>(<span class="hljs-params">num1: numType, num2: numType, ...others: numType[]</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">if</span> (others.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> minus(minus(num1, num2), others[<span class="hljs-number">0</span>], ...others.slice(<span class="hljs-number">1</span>));
  &#125;
  <span class="hljs-keyword">const</span> baseNum = <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, <span class="hljs-built_in">Math</span>.max(digitLength(num1), digitLength(num2)));
  <span class="hljs-keyword">return</span> (times(num1, baseNum) - times(num2, baseNum)) / baseNum;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加法&减法的逻辑，和乘法类似，也是将数据根据最大的小数数量进行放大，再进行相加/相减，最后再进行数据缩小。</p>
<h1 data-id="heading-9">总结</h1>
<ul>
<li>当10进制小数转为二进制，存在无限循环时，在JavaScript中存在精度丢失</li>
<li>可通过<code>toPrecision</code>方法来进行精度丢失修复</li>
<li>进行数据计算时，先将小数转为整数来计算，再将结果进行放大或缩小</li>
</ul>
<h1 data-id="heading-10">参考资料</h1>
<ul>
<li><a href="https://segmentfault.com/a/1190000016586981" target="_blank" rel="nofollow noopener noreferrer">探寻 JavaScript 精度问题以及解决方案</a></li>
<li><a href="https://github.com/camsong/blog/issues/9" target="_blank" rel="nofollow noopener noreferrer">JavaScript 浮点数陷阱及解法</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            