
---
title: '初学ES6记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dbe96b29714fd7a496bd744d9e601c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 19:34:34 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dbe96b29714fd7a496bd744d9e601c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">初学ES6记录...</h2>
<h3 data-id="heading-1">原型链</h3>
<p>在原型链中，实例对象的原型对象也有原型对象并指向的是Object。
为了共享方法
因为ES6之前没有类的继承，所以只能通过原型对象来共享方法</p>
<blockquote>
<p>不能直接把父类的原型对象赋给子类，这样会导致两个原型对象指向相同，而是应该要创建父类的对象实例再赋给子类的原型对象，这样通过原型链才能正确的继承父类的方法而不相互影响。</p>
</blockquote>
<h3 data-id="heading-2">this的指向问题</h3>
<ul>
<li>普通函数中 this指向window</li>
<li>对象方法中 this指向调用的对象</li>
<li>构造函数中 this指向实例对象  原型对象里面的this指向实例对象</li>
<li>定时器函数中 this指向window</li>
<li>立即执行函数中 this指向window</li>
</ul>
<h4 data-id="heading-3">修改this指向的三个函数</h4>
<ul>
<li>call函数可以修改函数运行的this指向  在没有继承之前可以使用子类调用call来使用父类的构造函数。例如：Father.call(this, uname , age , sex );</li>
<li>filter返回的是数组</li>
<li>bind是不调用函数但是改变this指向</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">btn.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.disabled=<span class="hljs-literal">true</span>;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.disabled=<span class="hljs-literal">false</span>;
            &#125;.bind(btn),<span class="hljs-number">3000</span>)
        &#125;)
        <span class="hljs-comment">//bind的使用小栗子</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>some和forEach的区别  在查找单个特定元素例如id的话推荐使用forEach，因为forEach会在找到元素的时候停止遍历，提高运行速度。
在判断条件中加入 return true;</em></p>
<h3 data-id="heading-4">Object-defineProperty</h3>
<p>vue2.js里面的重要技术</p>
<ul>
<li>writable 是否可以修改</li>
<li>configurable 是否允许被删除或再次修改这个属性</li>
<li>enumerable 是否允许遍历</li>
<li>value就是值有就修改没有就直接添加</li>
</ul>
<h3 data-id="heading-5">修改this指向的三种方法</h3>
<ul>
<li>call 调用函数和改变函数内的this指向，可以实现继承</li>
<li>apply 传入的参数必须是数组  可以借助于数学内置对象最大值之类的</li>
<li>bind方法不会调用函数 返回是一个修改过this指向的函数</li>
</ul>
<h3 data-id="heading-6">严格模式</h3>
<p>是IE10 ES5以后才有的 相当于对代码进行一些约束  例如要先声明变量才能赋值</p>
<ul>
<li>严格模式下全局作用域中函数的this指向的是undefined</li>
<li>严格模式下不允许在非函数的代码块内声明函数</li>
<li>严格模式下定时器的this指向window</li>
</ul>
<p>语法 <code> "strict use"</code></p>
<h3 data-id="heading-7">闭包</h3>
<p>就是指一个函数的作用域可以访问另一个函数的作用域、
还延申了函数局部变量的作用域<br>
立即执行函数称为小闭包 因为立即执行函数里面可以使用传入的变量</p>
<h3 data-id="heading-8">深拷贝浅拷贝</h3>
<h5 data-id="heading-9">浅拷贝</h5>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> k <span class="hljs-keyword">in</span> obj)&#123;
          <span class="hljs-comment">//k是属性名 obj[k]是属性值</span>
    o[k]=obj[k];      
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或直接用封装好的函数 assign  Object.assign(o,obj);
但是浅拷贝在复杂数据类型只会把地址拷贝</p>
<h5 data-id="heading-10">深拷贝</h5>
<p>新开辟一份空间来存储数据
手写代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepcopy</span>(<span class="hljs-params">newobj,oldobj</span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> k <span class="hljs-keyword">in</span> oldobj)&#123;
                <span class="hljs-keyword">var</span> item=oldobj[k];
                <span class="hljs-keyword">if</span>(item <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
                    newobj[k]=[];
                    deepcopy(newobj[k],item);
                &#125;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(item <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)&#123;
                    newobj[k]=&#123;&#125;;
                    deepcopy(newobj[k],item);
                &#125;
                <span class="hljs-keyword">else</span>&#123;
                    newobj[k]=item;
                &#125;
            &#125;
        &#125;
  <span class="hljs-comment">//数组也是对象所以要先判断是不是数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">正则表达式 (Regular Expression)</h3>
<p>匹配  替换  提取</p>
<h6 data-id="heading-12">检测文本是否符合正则表达式规范   <code>re.test();</code></h6>
<ul>
<li>边界符 ^ $</li>
<li>量词符 * + ? &#123;a,b&#125;</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">/[abc]/        <span class="hljs-comment">//只要包含其中一个就true</span>
 <span class="hljs-regexp">/^[abc]$/</span>        <span class="hljs-comment">//只要有一个就是true</span>
 <span class="hljs-regexp">/^[a-z]$/</span>        <span class="hljs-comment">//a到z任意一个字母都可以</span>
 <span class="hljs-regexp">/^[a-zA-Z]$/</span>     <span class="hljs-comment">//$字母大写和小写都可以 </span>
 <span class="hljs-regexp">/^a*$/</span>           <span class="hljs-comment">//a出现0次或者更多次</span>
 <span class="hljs-regexp">/^a+$/</span>           <span class="hljs-comment">//a出现1次以上</span>
 <span class="hljs-regexp">/^a?$/</span>           <span class="hljs-comment">//a出现1||0次</span>
 <span class="hljs-regexp">/^a&#123;3&#125;$/</span>         <span class="hljs-comment">//a出现3次</span>
 <span class="hljs-regexp">/^a&#123;3,6&#125;$/</span>         <span class="hljs-comment">//a出现3次以上小于等于6</span>
 <span class="hljs-regexp">/^(abc)&#123;3&#125;$/</span>         <span class="hljs-comment">//abc出现3次</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="b3e9bc77b91f3642b64d63a6356d484.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dbe96b29714fd7a496bd744d9e601c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>菜鸟教程</strong>             在线测试正则表达式和通用正则表达式</p>
<h3 data-id="heading-13">let和const的使用</h3>
<ul>
<li>let声明的变量具有块级作用域</li>
<li>let声明的变量不存在变量提升</li>
<li>let声明的变量存在暂时性死区</li>
<li>const声明的常量具有块级作用域</li>
<li>const声明的常量必须赋值</li>
</ul>
<h3 data-id="heading-14">数组、对象解构</h3>
<p><code>let ary[a,b,c]=[1,2,3]; //数组解构  a=1,b=2,c=3</code></p>
<p><code>let person =&#123;name:'zhangsan',age:20&#125;;  let &#123;name:myname,age:myage&#125;=person;  //对象解构    </code></p>
<h3 data-id="heading-15">箭头函数</h3>
<p><code> const fn=()=>&#123;&#125;   //语法</code></p>
<p><em>箭头函数不绑定this关键字，箭头函数中this指向函数定义位置的上下文this</em></p>
<p><em>剩余参数</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sum=<span class="hljs-function">(<span class="hljs-params">...args</span>)=></span>&#123;
<span class="hljs-keyword">let</span> total=<span class="hljs-number">0</span>;
args.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> total += item);
<span class="hljs-keyword">return</span> total;
&#125;;  <span class="hljs-comment">// 剩余参数（将不定数量的参数表示成一个数组）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>扩展运算符</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ary=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];  
<span class="hljs-built_in">console</span>.log(...ary);<span class="hljs-comment">//拆分成1，2，3</span>
<span class="hljs-keyword">let</span> ary1=[<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>];
<span class="hljs-keyword">let</span> ary2=[...ary,...ary1];  <span class="hljs-comment">//数组合并</span>
ary1.push(...ary);
<span class="hljs-comment">//伪数组变成真正数组</span>
<span class="hljs-keyword">var</span> divs=<span class="hljs-built_in">document</span>.queryseletorAll(<span class="hljs-string">'div'</span>);
<span class="hljs-keyword">var</span> ary=[...divs];  
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">Array的拓展方法</h5>
<pre><code class="hljs language-js copyable" lang="js">array=<span class="hljs-built_in">Array</span>.from(arrylike,<span class="hljs-function"><span class="hljs-params">item</span>=></span>item*<span class="hljs-number">2</span>);<span class="hljs-comment">//from方法形成数组</span>
item=ary.find(<span class="hljs-function"><span class="hljs-params">item</span>=></span>item.id==<span class="hljs-number">2</span>);<span class="hljs-comment">//find方法查找元素</span>
index=ary.findIndex(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;item><span class="hljs-number">15</span>&#125;)<span class="hljs-comment">//findIndex方法查找序号</span>
flag=ary.includes(<span class="hljs-number">2</span>); <span class="hljs-comment">//includes查看是否包含元素</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            