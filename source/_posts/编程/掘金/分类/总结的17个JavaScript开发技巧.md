
---
title: '总结的17个JavaScript开发技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa22128d0464a5f8bebf2bbfbc5010c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 17:03:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa22128d0464a5f8bebf2bbfbc5010c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">async/await</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 标准用法:</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testAwait</span> (<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            resolve(x);
        &#125;, <span class="hljs-number">2000</span>);
    &#125;);
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">helloAsync</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> x = <span class="hljs-keyword">await</span> testAwait (<span class="hljs-string">"hello world"</span>);
<span class="hljs-built_in">console</span>.log(x);

<span class="hljs-comment">// 或者:</span>
<span class="hljs-comment">// var x = testAwait ("hello world");//此处x是一个Promise对象</span>
<span class="hljs-comment">// x.then(function(value)&#123;</span>
<span class="hljs-comment">// console.log(value);</span>
<span class="hljs-comment">// &#125;);</span>
&#125;
helloAsync ();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">宽松相等 ==</h2>
<pre><code class="hljs language-js copyable" lang="js">[ ] == [ ] <span class="hljs-comment">// false 2 3 解析：两个引用类型，==比较的是引用地址</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">== 和 ! 优先级</h2>
<pre><code class="hljs language-js copyable" lang="js">[ ] == ![ ] <span class="hljs-comment">// true</span>

<span class="hljs-comment">/*
    解析：
    (1)! 的优先级高于== ，右边Boolean([])是true,取返等于 false
    (2)一个引用类型和一个值去比较 把引用类型转化成值类型，左边0
    (3)所以 0 == false 答案是true
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">数字与字符串相加减</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'5'</span> + <span class="hljs-number">3</span>
<span class="hljs-string">'5'</span> - <span class="hljs-number">3</span>
<span class="hljs-comment">// 解析：加号有拼接功能，减号就是逻辑运算</span>
<span class="hljs-comment">// 巩固：typeof (+"1") // "number" 对非数值+—常被用来做类型转换相当于Number()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">补零</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> FillZero = <span class="hljs-function">(<span class="hljs-params">num, len</span>) =></span> num.toString().padStart(len, <span class="hljs-string">"0"</span>);
<span class="hljs-keyword">var</span> num = FillZero(<span class="hljs-number">156</span>, <span class="hljs-number">5</span>);  <span class="hljs-comment">// FillZero(数字, 位数)</span>
<span class="hljs-comment">// num => "00156"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">是否为空数组</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [];
<span class="hljs-keyword">var</span> flag = <span class="hljs-built_in">Array</span>.isArray(arr) && !arr.length;
<span class="hljs-comment">// flag => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">是否为空对象</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;&#125;;
<span class="hljs-keyword">var</span> flag = DataType(obj, <span class="hljs-string">"object"</span>) && !<span class="hljs-built_in">Object</span>.keys(obj).length;  <span class="hljs-comment">// Object.keys(data).length !== 0</span>
<span class="hljs-comment">// flag => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">数组比较大小</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
b = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
c = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>];

a == b
a === b
a > c
a < c

<span class="hljs-comment">/*
    答案：false, false, false, true
    解析：相等（==）和全等（===）还是比较引用地址
    引用类型间比较大小是按照字典序比较，就是先比第一项谁大，相同再去比第二项。
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">String.fromCharCode()</h2>
<p>方法返回根据指定的UTF-16代码单元序列创建的字符串</p>
<pre><code class="copyable">let letterArr = []
// 选出26个字母
for (let i = 65; i < 91; i++) &#123;
    letterArr.push(String.fromCharCode(i))
&#125;
letterArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">数组去重</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [...new <span class="hljs-built_in">Set</span>([<span class="hljs-number">0</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>])];
<span class="hljs-comment">// arr => [0, 2, null]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">if多条件判断</h2>
<p>觉得这个简直不要太好用，代码看起来舒服多了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 冗余</span>
<span class="hljs-keyword">if</span> (x === <span class="hljs-string">'a'</span> || x === <span class="hljs-string">'b'</span> || x === <span class="hljs-string">'c'</span> || x ===<span class="hljs-string">'d'</span>) &#123;
    <span class="hljs-comment">// something </span>
&#125;

<span class="hljs-comment">// 简洁</span>
<span class="hljs-comment">// 返回的是布尔值</span>
<span class="hljs-keyword">if</span> ([<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'d'</span>].includes(x)) &#123;
    <span class="hljs-comment">// something </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">优化if else，switch</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> code; <span class="hljs-comment">// code有多个值 1 2 3 4 5, 分别做不一样的事情</span>

<span class="hljs-comment">// 常见 if 写法, 看起来密密麻麻，简直让人头皮发麻</span>
<span class="hljs-keyword">if</span> (code === <span class="hljs-number">1</span>) &#123;
  TodoA();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (code === <span class="hljs-number">2</span>) &#123;
  TodoB();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (code === <span class="hljs-number">3</span>) &#123;
  TodoC();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (code === <span class="hljs-number">4</span>) &#123;
  TodoD();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (code === <span class="hljs-number">5</span>) &#123;
  TodoE();
&#125;

<span class="hljs-comment">// switch 优化一下, 这样的代码本身也没什么，只是可读性差一些，看起来有点费劲</span>
<span class="hljs-keyword">switch</span> (code) &#123;
  <span class="hljs-keyword">case</span> <span class="hljs-number">1</span>:
    TodoA();
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:
    TodoB();
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">3</span>:
    TodoC();
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
    TodoD();
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">5</span>:
    TodoE();
    <span class="hljs-keyword">break</span>;

  <span class="hljs-keyword">default</span>:
    <span class="hljs-keyword">break</span>;
&#125;

<span class="hljs-comment">// 最后的最后,巧用对象来“优雅”解决这一长串代码</span>
<span class="hljs-keyword">const</span> codeNum = &#123;
  <span class="hljs-number">1</span>: TodoA,
  <span class="hljs-number">2</span>: TodoB,
  <span class="hljs-number">3</span>: TodoC,
  <span class="hljs-number">4</span>: TodoD,
  <span class="hljs-number">5</span>: TodoE,
&#125;
<span class="hljs-keyword">if</span> (codeNum[code]) &#123;
  codeNum[code]();
&#125;

<span class="hljs-comment">// 看看这代码，简直不要太简洁，又可以舒舒服服躺着摸鱼了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">find</h2>
<p>方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。</p>
<p>语法：<strong>array.find(mapfuc)</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> array = [<span class="hljs-number">0</span>,<span class="hljs-number">12</span>,<span class="hljs-number">22</span>,<span class="hljs-number">55</span>,<span class="hljs-number">44</span>]
<span class="hljs-built_in">console</span>.log(array.find(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> item >= <span class="hljs-number">18</span>)) <span class="hljs-comment">// 22</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">提前退出机制</h2>
<p>相信大家看过这样一份代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">form</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (form) &#123;
        <span class="hljs-keyword">let</span> flag = form.status;
        <span class="hljs-keyword">if</span> (flag) &#123;
            <span class="hljs-comment">// something code</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>当一个条件所需的值位于某个值下的时候，我们就要进行两次判断</strong></p>
<p>那我们换一种写法呢</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">form</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!form && !form.status) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// something code</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家都知道，<strong>且运算符（&）</strong> 只有当<strong>两者为真值</strong>时才为<strong>true</strong>，那如果if这个语句为假，程序就不会执行其他代码。</p>
<h2 data-id="heading-14">对象变量属性</h2>
<p>这是什么意思呢？红宝书中是这样解释<strong>可计算属性</strong>的：
<strong>在引入可计算属性之前，如果想使用变量的值作为属性，那么必须先声明对象，然后使用中括号语法来添加属性。换句话说，不能在对象字面量中直接动态命名属性。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa22128d0464a5f8bebf2bbfbc5010c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> flag = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    [flag ? <span class="hljs-string">"c"</span> : <span class="hljs-string">"d"</span>]: <span class="hljs-number">2</span>
&#125;;
<span class="hljs-comment">// obj => &#123; a: 0, b: 1, d: 2 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于这个写法，我也有用于axios中，</p>
<p>用于动态控制axios的<strong>params(get请求)，data(post请求)</strong> --------- 对象键值可以使用 <strong>[变量或表达式]</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> method = plat == <span class="hljs-string">'xxx'</span> ? <span class="hljs-string">'get'</span> : <span class="hljs-string">'post'</span>;  <span class="hljs-comment">// 当 plat等于某个值时是get请求,否则为post请求</span>

axios(&#123;
　　method, <span class="hljs-comment">// 请求方式</span>
　 [ method == <span class="hljs-string">'get'</span> ? <span class="hljs-string">'params'</span> : <span class="hljs-string">'data'</span> ]: data <span class="hljs-comment">// 对象键值可以使用 [ 变量或表达式 ]  data就是传回后端的数据</span>
&#125;).then(<span class="hljs-function">() =></span> &#123;&#125;).catch(<span class="hljs-function">() =></span> &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">函数退出代替条件分支退出</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (flag) &#123;
    Func();
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-comment">// 换成</span>
<span class="hljs-keyword">if</span> (flag) &#123;
    <span class="hljs-keyword">return</span> Func();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">格式化金钱</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> formatMoney = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num.toString().replace(<span class="hljs-regexp">/\B(?=(\d&#123;3&#125;)+(?!\d))/g</span>, <span class="hljs-string">","</span>);
<span class="hljs-keyword">let</span> money = formatMoney(<span class="hljs-number">986542135</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'money ==> '</span>, money);  <span class="hljs-comment">// ""986,542,135""</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            