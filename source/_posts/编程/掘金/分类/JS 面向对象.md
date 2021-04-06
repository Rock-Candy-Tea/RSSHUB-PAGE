
---
title: 'JS 面向对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f9ef5dce034c719ec3755ea8493f0f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 05:20:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f9ef5dce034c719ec3755ea8493f0f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">面向对象</h1>
<blockquote>
<p>最近在复习 javascript 基础知识，特此给自己记录下来，一次搞定对象</p>
</blockquote>
<ul>
<li>类：封装、多态、继承</li>
<li>构造函数、实例、对象字面量</li>
<li>命名空间</li>
<li>内置对象、宿主对象、本地对象</li>
</ul>
<blockquote>
<p>首先 JS 中没有类，都是基于原型的。无论是 ES5/ES6 中引入的 class 只是基于原型继承模型的语法糖。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f9ef5dce034c719ec3755ea8493f0f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">构造函数</h2>
<p>本身就是一个函数，为了规范<strong>一般将首字母大写</strong>，区别在于 使用 <strong>new 生成实例的函数就是构造函数</strong>，直接调用的就是 普通函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ********** 手写 new 的几个步骤 ********** //</span>
<span class="hljs-comment">// 1、创建一个新对象，</span>
<span class="hljs-comment">// 2、把 构造函数的 prototype 赋值给新对象的 proto,</span>
<span class="hljs-comment">// 3、把构造函数的 this 指向新对象并返回结果</span>
<span class="hljs-comment">// 4、判断如果结果是对象则 返回 ，否则返回 新对象</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNew</span>(<span class="hljs-params">fn, ...args</span>) </span>&#123;
  <span class="hljs-keyword">let</span> newobj = &#123;&#125;;
  newobj.__proto__ = fn.prototype;
  <span class="hljs-keyword">let</span> resObj = fn.apply(newobj, args);
  <span class="hljs-comment">// 判断如果结果是对象则 返回 ，否则返回 新对象</span>
  <span class="hljs-keyword">return</span> resObj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> ? resObj : newobj;
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parsen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"龙哥"</span>;
  <span class="hljs-built_in">this</span>.age = <span class="hljs-string">"18"</span>;
&#125;
Parsen.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;;
<span class="hljs-keyword">var</span> parsen = myNew(Parsen);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">原型和原型链</h2>
<h3 data-id="heading-3">原型模式</h3>
<p>原型是在构造函数中的
<strong>每声明一个函数的时候：</strong>
浏览器会在内存中创建一个对象，对象中新增一个 <code>constructor</code>  属性，浏览器把 <code>constructor</code>  属性指向 构造函数，构造函数.prototype 赋值给对象。</p>
<p>Javascript 对象从原型继承方法和属性，而<code>Object.prototype</code>在继承链的顶部。Javascript prototype 关键字还可以用于向构造函数添加新值和方法。</p>
<p><strong>原型链：</strong>
代码读取某个属性的时候，首先在实例中找到了则返回，如果没有找到，则继续在 实例的原型对象(<strong>proto</strong>)中搜索，直到找到为止。还没找到则继续 原型对象的原型对象上找。 直到最后 Object 为止，返回 null</p>
<h3 data-id="heading-4">关系</h3>
<ul>
<li>prototype：函数的一个属性：是一个对象 &#123;&#125;</li>
<li><strong>proto</strong>：是对象 Object 的一个属性：对象 &#123;&#125;</li>
<li>**每个对象实例都有一个 __**<em><strong>proto__</strong></em>  ，它指向构造函数的 prototype</li>
<li><strong>以上关系可以使用 console.log 去测试</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;
&#125;;
<span class="hljs-keyword">var</span> t = <span class="hljs-keyword">new</span> Test();

<span class="hljs-comment">// 因为 对象的 __proto__ 保存着该对象构造函数的 prototype 所以</span>
t.__proto__ === Test.prototype <span class="hljs-comment">// true</span>

Test.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype <span class="hljs-comment">// true： 这样一个链式调用形成 - 原形链</span>

<span class="hljs-built_in">Object</span>.prototype.__proto__ <span class="hljs-comment">// null  原形链顶层为 null</span>

<span class="hljs-comment">/************* 原形链 *****************/</span>

Test.prototype.b = <span class="hljs-number">2</span>; <span class="hljs-comment">// 给构造函数的原型添加一个 属性b=2</span>
<span class="hljs-built_in">Object</span>.prototype.c = <span class="hljs-number">3</span>
<span class="hljs-built_in">console</span>.log(test)
<span class="hljs-comment">// 画一下这个关系链：</span>
<span class="hljs-comment">// test:</span>
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//     a: 1,</span>
<span class="hljs-comment">//     __proto__: Test.prototype = &#123;</span>
<span class="hljs-comment">//         b: 2,</span>
<span class="hljs-comment">//         __proto__: Oject.prototype = &#123;</span>
<span class="hljs-comment">//         c:3</span>
<span class="hljs-comment">//         没有 __proto__</span>
<span class="hljs-comment">//         &#125;</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// 原形链： 沿着__proto__为节点去找构造函数prototype 连起来的一个链条， 一层一层往上寻找 直到 null</span>

<span class="hljs-built_in">console</span>.log(test.constructor) <span class="hljs-comment">// Test()&#123;&#125;</span>
其实 test.constructor 指向的就是 实例化 test 对象的构造函数
所以：<span class="hljs-title">constructor</span> 是可以被赋值修改的，


/************* 特殊性 *****************/
<span class="hljs-title">Function</span>、<span class="hljs-title">Object</span>：函数 对象
<span class="hljs-title">Test</span>.<span class="hljs-title">__proto__</span> === <span class="hljs-title">Function</span>.<span class="hljs-title">prototype</span> // <span class="hljs-title">true</span>
<span class="hljs-title">Function</span>.<span class="hljs-title">__proto__</span> === <span class="hljs-title">Function</span>.<span class="hljs-title">prototype</span> // <span class="hljs-title">true</span>  因为函数自己构造了自己
<span class="hljs-title">Object</span>.<span class="hljs-title">__proto__</span> === <span class="hljs-title">Function</span>.<span class="hljs-title">prototype</span> // <span class="hljs-title">true</span>

/************* 属性的查找 *****************/
// <span class="hljs-title">test</span> => &#123;a: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;
test.hasOwnProperty(<span class="hljs-string">'a'</span>) <span class="hljs-comment">// true    查找当前对象上的原型属性</span>
test.hasOwnProperty(<span class="hljs-string">'b'</span>) <span class="hljs-comment">// true</span>
test.hasOwnProperty(<span class="hljs-string">'c'</span>) <span class="hljs-comment">// false    是继承过来的所以没有</span>

<span class="hljs-string">'a'</span> <span class="hljs-keyword">in</span> test <span class="hljs-comment">// true   in: 链上查找</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Class</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/************ ES5 定义类 ******************/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">User</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-comment">// 添加函数</span>
User.prototype.showUser = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;;
<span class="hljs-comment">// 使用</span>
<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> User(<span class="hljs-string">"my.yang"</span>);
user.showUser();

<span class="hljs-comment">/************ ES6 定义类 ******************/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-comment">// 其实就是在 Person 的 prototype 上添加了属性和方法</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-function"><span class="hljs-title">showName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
  &#125;
&#125;

<span class="hljs-keyword">const</span> person = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"My.Yang"</span>);
person.showName();

<span class="hljs-comment">/******************* 类的实例 ***************************/</span>

<span class="hljs-comment">// 实例的属性除了 this 定义在本身，其他都是定义在原型上</span>
<span class="hljs-built_in">console</span>.log(person.hasOwnProperty(<span class="hljs-string">"name"</span>)); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person.hasOwnProperty(<span class="hljs-string">"showName"</span>)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(person.__proto__.hasOwnProperty(<span class="hljs-string">"showName"</span>)); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 与 ES5 一样，类的所有实例共享一个原型对象。</span>
<span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"long"</span>);
<span class="hljs-keyword">var</span> a2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"mmmmm"</span>);
<span class="hljs-built_in">console</span>.log(a1.__proto__ === a2.__proto__);

<span class="hljs-comment">// 所以不推荐直接通过 __proto__ 添加私有属性和方法，因为 共享的实例都会受到影响</span>

<span class="hljs-comment">/****************注意点：********************/</span>
<span class="hljs-comment">// 1、类和模块的内部默认使用严格模式</span>
<span class="hljs-comment">// 2、不存在变量提升  提前访问会报错 ReferenceError</span>

<span class="hljs-comment">// 静态方法：static</span>
<span class="hljs-comment">// 添加 static 关键字，表示该方法不会被【实例】继承，只能通过类.直接调用，但是可以被 子类继承 extends</span>

<span class="hljs-comment">// 私有方法和属性</span>
<span class="hljs-comment">// 私有方法：通过内部使用 _xxx、_func 的方式来定义</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、创建了一个 名为 User 的函数，该函数将成为类声明的结果
2、在 User.prototype 中存储所有方法，例如 showUser ( 跟 ES5 一样把函数存到 prototype 上 )
3、类必须使用 new ，否则无法调用类构造函数 报错
4、类方法 是不可以枚举的</p>
<h2 data-id="heading-6">继承</h2>
<p>Class 使用 <strong>extends</strong>实现继承，比 ES5 通过修改原型链实现继承，要清晰和方便很多。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ColorPoint</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Point</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y, color</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(x, y); <span class="hljs-comment">// 调用父类的constructor(x, y)</span>
    <span class="hljs-built_in">this</span>.color = color;
  &#125;
  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.color + <span class="hljs-string">" "</span> + <span class="hljs-built_in">super</span>.toString(); <span class="hljs-comment">// 调用父类的toString()</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：
子类必须在 constructor 中先调用 super(),否则新建实例就会报错。ReferenceError
主要是 解决 this 问题，需要先把 父类属性和方法加到 this 上，然后再用子类构造函数修改 this 。</p>
<p>使用 Object.getPrototypeOf() 判断 类是否继承了另一个类
<code>Object.getPrototypeOf(Xxxx) === XXX</code></p>
<p><strong>super 既可以当作函数又可以是对象</strong>
当作函数： super() 代表 父类的构造函数。 => A.prototype.constructor.call(this)</p>
<p>当作对象：super 在普通方法中，指向 父类的原型对象 A.prototype；在静态方法中 指向父类。</p>
<h3 data-id="heading-7">1、原型链继承</h3>
<p><strong>直接让子类的原型对象 prototype 指向父类实例</strong>，当子类实例找不到对应的属性和方法时，就会往它的原型对象(父类实例上找)，从而实现对父类的属性和方法的继承。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"我是小样"</span>;
&#125;
<span class="hljs-comment">// 给父类添加方法</span>
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;;
<span class="hljs-comment">// 子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

Child.prototype = <span class="hljs-keyword">new</span> Parent(); <span class="hljs-comment">// 直接把父类实例赋给 子类的 原型对象</span>
Child.prototype.constructor = Child; <span class="hljs-comment">// 根据原型链的规则,顺便绑定一下constructor, 这一步不影响继承, 只是在用到constructor时会需要</span>

<span class="hljs-keyword">const</span> child = <span class="hljs-keyword">new</span> Child();
child.name; <span class="hljs-comment">// 我是小样</span>
child.getName(); <span class="hljs-comment">// 我是小样</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：【<strong>子类相互影响</strong>】 子类实例原型都指向父类实例，因此 某个 子类实例修改了 父类引用方法或函数的时候 会影响所有子类。 <strong>同时无法向父类构造函数传参</strong>。</p>
<h3 data-id="heading-8">2、构造函数继承</h3>
<p><strong>在子类构造函数中执行 父类构造函数并绑定子类 this</strong>, 使得 父类中的属性能够赋值到子类的 this 上。这样就 避免实例之间共享一个原型实例，又能向父类构造函数传参。
缺点很明显： <strong>继承不了父类原型上的属性和方法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = [name];
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">"参数1"</span>); <span class="hljs-comment">// 执行父类构造方法并绑定子类的this, 使得父类中的属性能够赋到子类的this上</span>
&#125;

<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">const</span> child2 = <span class="hljs-keyword">new</span> Child();
child1.name[<span class="hljs-number">0</span>] = <span class="hljs-string">"foo"</span>;
<span class="hljs-built_in">console</span>.log(child1.name); <span class="hljs-comment">// ['foo']</span>
<span class="hljs-built_in">console</span>.log(child2.name); <span class="hljs-comment">// ['zhangsan']</span>
child2.getName(); <span class="hljs-comment">// 报错,找不到getName(), 构造函数继承的方式 继承不到父类原型上的属性和方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3、组合式继承</h3>
<p>说白了就是 把上面两个整合在一起, prototype、构造函数调用父类 call</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = [name];
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">"参数"</span>); <span class="hljs-comment">// 改变 Parent this 指向，并带参数</span>
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent(); <span class="hljs-comment">// 把父类实例 赋值给 子类原型</span>
Child.prototype.constructor = Child;

<span class="hljs-keyword">var</span> child = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">var</span> child2 = <span class="hljs-keyword">new</span> Child();
child1.name = <span class="hljs-string">"yang"</span>;
<span class="hljs-built_in">console</span>.log(child1.name); <span class="hljs-comment">// yang</span>
<span class="hljs-built_in">console</span>.log(child2.name); <span class="hljs-comment">// 参数</span>
child2.getName(); <span class="hljs-comment">// 参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点： 每次创建子类实例都<strong>执行了两次构造函数</strong>【Parent.call() 和 new Parent()】,导致子类创建实例时，原型中会<strong>存在两份相同的属性和方法</strong>，很不优雅。</p>
<h3 data-id="heading-10">4、寄生式组合继承【终极方案】</h3>
<p>为了解决 组合式继承 构造函数被执行两次的问题，我们将 <strong>指向父类实例改为指向 拷贝的父类原型</strong>，去掉一次构造函数的执行，并且 不会相互影响。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">主要是把原来的 ，其他都一样。
Child.prototype = <span class="hljs-keyword">new</span> Parent() => Child.prototype = Parent.prototype
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是 问题又出来了，<strong>子类原型和父类原型都指向同一个对象，那还是会相互影响</strong>。
所以：给 父类原型做一个 浅拷贝
<code>Child.prototype = Object.create(Parent.prototype)</code>
到这里 ES5 的所有继承都有了，<strong>babel 对 ES6 继承的转换也是 使用了 寄生组合式继承</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = [name];
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 构造函数继承</span>
  Parent.call(<span class="hljs-built_in">this</span>, <span class="hljs-string">"zhangsan"</span>);
&#125;
<span class="hljs-comment">//原型链继承</span>
<span class="hljs-comment">// Child.prototype = new Parent()</span>
Child.prototype = <span class="hljs-built_in">Object</span>.create(Parent.prototype); <span class="hljs-comment">//将`指向父类实例`改为`指向父类原型`</span>
Child.prototype.constructor = Child;

<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">const</span> child = <span class="hljs-keyword">new</span> Child();
<span class="hljs-keyword">const</span> parent = <span class="hljs-keyword">new</span> Parent();
child.getName(); <span class="hljs-comment">// ['zhangsan']</span>
parent.getName(); <span class="hljs-comment">// 报错, 找不到getName()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们回顾一下实现过程：</p>
</blockquote>
<ol>
<li>一开始最容易想到的是<strong>原型链继承</strong>，通过把子类实例的原型指向父类实例来继承父类的属性和方法，但原型链继承的缺陷在于对子类实例继承的引用类型的修改会影响到所有的实例对象以及无法向父类的构造方法传参。</li>
<li>因此我们引入了<strong>构造函数继承</strong>, 通过在子类构造函数中调用父类构造函数并传入子类 this 来获取父类的属性和方法，但构造函数继承也存在缺陷，构造函数继承不能继承到父类原型链上的属性和方法。</li>
<li>所以我们综合了两种继承的优点，提出了<strong>组合式继承</strong>，但组合式继承也引入了新的问题，它每次创建子类实例都执行了两次父类构造方法，我</li>
<li>们通过将子类原型指向父类实例改为子类原型指向父类原型的浅拷贝来解决这一问题，也就是最终实现 —— <strong>寄生组合式继承</strong></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            