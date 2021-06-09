
---
title: 'js冻结一个对象Object.defineProperty-Object.freeze-Object.seal-Object.preventExtensions'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/179a3c2c83ca47128e04803ee8a3626a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:35:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/179a3c2c83ca47128e04803ee8a3626a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/179a3c2c83ca47128e04803ee8a3626a~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer">
<strong>如果在开发中我不想让别人对obj对象添加或删除元素 可以砸子做？</strong></p>
<blockquote>
<p>当该属性的<code>configurable键值为true时</code>该属性的描述才能被修改 同时该属性也能从对应的对象上被删除<br>
就是说如果<code>configurable值为false时</code>属性就无法从对象上面删除 这个方法 仅能使对象内的 元素无法被删除 依旧可以在新对象中添加新的对象</p>
</blockquote>
<p>看代码示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.defineProperty(obj,<span class="hljs-string">"prop"</span>,&#123;
     <span class="hljs-attr">configurable</span>:<span class="hljs-literal">false</span>,  <span class="hljs-comment">//configurable属性为true时 该属性的秒速符才能被修改 同时该属性也能从对应的对象上被删除 </span>
     <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,    <span class="hljs-comment">//enumerable  属性为true时 该属性才会出现在对象的枚举属性中</span>
     <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,      <span class="hljs-comment">//表示 是否可以修改属性的值 </span>
     <span class="hljs-attr">value</span>:<span class="hljs-string">""</span>             <span class="hljs-comment">//该属性的值 可以是任何有效的js 值(数值，对象，函数)</span>
&#125;)
<span class="hljs-comment">//这样设置以后 prop属性就变成了不能删除 不能重新修改特性 不可枚举 不能修改的属性值的属性</span>
 <span class="hljs-comment">//  示例代码 </span>
    <span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"东东"</span>&#125;
    <span class="hljs-built_in">Object</span>.defineProperty(obj,<span class="hljs-string">"name"</span>,&#123;
        <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,
        <span class="hljs-attr">configurable</span>:<span class="hljs-literal">false</span>
    &#125;)
    <span class="hljs-comment">// 修改 </span>
    obj.name = <span class="hljs-string">"收购腾讯"</span>;
    <span class="hljs-built_in">console</span>.log(obj.name);      <span class="hljs-comment">//东东 </span>
    <span class="hljs-comment">// 添加新的属性  </span>
    obj.address = <span class="hljs-string">"青岛"</span>
    <span class="hljs-built_in">console</span>.log(obj.address);   <span class="hljs-comment">//青岛</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">Object.freeze(person);</h3>
<blockquote>
<p>冻结的对象既不可扩展，又是密封的，而且对象，数据属性的[ [Writable] ]特性会被设置为false。<br>
如果定义[ [Set] ]函数，访问器属性仍然是可写的。ES5定义的Object. freeze()方法可以用来冻结对象。</p>
</blockquote>
<p>代码所示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"大黄"</span>
    &#125;;
    <span class="hljs-built_in">Object</span>.freeze(person);     <span class="hljs-comment">//冻结了这个对象 </span>
    person.age = <span class="hljs-number">18</span>;           <span class="hljs-comment">//新添加一个age属性 没有起效果</span>
    <span class="hljs-built_in">console</span>.log(person.age);   <span class="hljs-comment">//undefined</span>
    <span class="hljs-keyword">delete</span> person.name;        <span class="hljs-comment">//删去name属性 没有起效果</span>
    <span class="hljs-built_in">console</span>.log(person.name);  <span class="hljs-comment">//"大黄"</span>
    person.name = <span class="hljs-string">"咪咪"</span>;      <span class="hljs-comment">//改变已有的属性 没起到效果 </span>
    <span class="hljs-built_in">console</span>.log(person.name);  <span class="hljs-comment">//"大黄"</span>
    <span class="hljs-comment">// Object. isFrozen()方法用于检测冻结对象。因为冻结对象既是密封的又是不可扩展的，</span>
    <span class="hljs-comment">// 所以用Object.isExtensible()和Object.isSealed ()检测冻结对象将分别返回false和true。</span>
    <span class="hljs-keyword">var</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"老王"</span>
    &#125;;
    alert(<span class="hljs-built_in">Object</span>.isExtensible(person)); <span class="hljs-comment">//true</span>
    alert(<span class="hljs-built_in">Object</span>.isSealed(person));     <span class="hljs-comment">//false</span>
    alert(<span class="hljs-built_in">Object</span>.isFrozen(person));     <span class="hljs-comment">//false</span>
    <span class="hljs-built_in">Object</span>.freeze(person);
    alert(<span class="hljs-built_in">Object</span>.isExtensible(person)); <span class="hljs-comment">//false</span>
    alert(<span class="hljs-built_in">Object</span>.isSealed(person));     <span class="hljs-comment">//true</span>
    alert(<span class="hljs-built_in">Object</span>.isFrozen(person));     <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">Object.seal()</h3>
<blockquote>
<p>这个方法封闭(密封)一个对象 阻止添加新属性 并将所有的属性标记为不可配置<br>
当前属性的值 只要原来的可写的 就可以改变<br>
一个对象是可拓展的(可以添加新的属性)<br>
<code>1 </code>密封一个对象会让这个对象变得不能添加新属性<br>
且所有已有的属性会变得 不可配置(属性不可配置的效果 即属性不可删除)<br>
<code>2</code> 以及一个数据属性 不能被重新定义成为访问器属性 或者反之<br>
但属性的值仍然可以修改<br>
<code>3</code> 尝试删除一个密封对象的属性或者<br>
将某个密封对象的属性从数据属性 转换为访问器属性 结果会静默抛出TypeError</p>
</blockquote>
<p>看示例代码</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"收购百度"</span>
    &#125;
    <span class="hljs-built_in">Object</span>.seal(person);     <span class="hljs-comment">//封闭这个对象</span>

    person.age = <span class="hljs-number">19</span>;
    <span class="hljs-built_in">console</span>.log(person.age); <span class="hljs-comment">//undefined</span>
                             <span class="hljs-comment">//无法给密封对象添加属性</span>
    <span class="hljs-keyword">delete</span> person.name;
    <span class="hljs-built_in">console</span>.log(person.name);<span class="hljs-comment">//收购百度</span>
                             <span class="hljs-comment">//无法修改密封对象中的属性。</span>
    <span class="hljs-comment">//使用Object.isSealed() 方法确定对象是否被密封 而且由于被密封的对象不可扩展，</span>
    <span class="hljs-comment">//所以Object.isExtensible() 检测也会返回 false。</span>
    <span class="hljs-keyword">var</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"老王"</span>
    &#125;
    <span class="hljs-built_in">Object</span>.seal(person);

    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isSealed(person)); <span class="hljs-comment">//true</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isExtensible(person)); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">es5的防止篡改对象</h3>
<blockquote>
<p>但是要注意，一旦把对象定义为防篡改对象，就无法撤销了。<br>
默认情况下，所有对象都是可以扩展的。也就是说，任何时候都可以向对象中添加属性和方法</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//Object.preventExtensions() 方法</span>
            <span class="hljs-comment">//1 改变这一行为 不能再添加属性或者方法。</span>
            <span class="hljs-comment">//2 虽然不能扩展该对象，但是不影响原有的属性，原有的属性仍然可以进行修改或者删除。</span>
            <span class="hljs-keyword">var</span> person = &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">"收购腾讯"</span>
            &#125;
            <span class="hljs-built_in">Object</span>.preventExtensions(person); <span class="hljs-comment">//将person设置为不可扩展对象</span>
            person.money = <span class="hljs-number">14</span>;
            <span class="hljs-built_in">console</span>.log(person);              <span class="hljs-comment">//&#123;name: "收购腾讯"&#125;</span>
            <span class="hljs-built_in">console</span>.log(person.money);        <span class="hljs-comment">//undefined</span>
            person.name = <span class="hljs-string">"收购阿里 "</span>;
            <span class="hljs-built_in">console</span>.log(person.name);         <span class="hljs-comment">//收购阿里</span>
    <span class="hljs-comment">//使用 Object.isExtensible() 方法可以确定该对象是否为可扩展对象。    </span>
        <span class="hljs-keyword">var</span> p = &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"老王"</span>
        &#125;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isExtensible(p)); <span class="hljs-comment">//ture</span>
        <span class="hljs-built_in">Object</span>.preventExtensions(p);         <span class="hljs-comment">//将p设置为不可扩展对象</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isExtensible(p)); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">es6 常量冻结</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//常量冻结 </span>
    <span class="hljs-keyword">const</span> esObj = &#123;         <span class="hljs-comment">//这里是一个对象</span>
        <span class="hljs-attr">name</span>:<span class="hljs-string">"es6"</span>,
        <span class="hljs-attr">year</span>:<span class="hljs-number">2015</span>
    &#125;
    <span class="hljs-comment">//Object.freeze(esObj);  //加上这一句 则下面的log&#123;name:"es6",year:2015&#125;</span>
    esObj.name =<span class="hljs-string">"es2015"</span>;
    <span class="hljs-built_in">console</span>.log(esObj)       <span class="hljs-comment">//&#123;name:"es2015", year:2015&#125;</span>

    <span class="hljs-keyword">const</span> arr = [<span class="hljs-string">'es6'</span>,<span class="hljs-string">'es7'</span>,<span class="hljs-string">'es8'</span>];   <span class="hljs-comment">//这是一个数组 </span>
    <span class="hljs-comment">//Object.freeze(arr)     //冻结</span>
    arr[<span class="hljs-number">0</span>] = <span class="hljs-string">'es2015'</span>
    <span class="hljs-built_in">console</span>.log(arr)         <span class="hljs-comment">//["es2015","es7","es8"]</span>
    <span class="hljs-comment">/*
     上面的代码说明 对象和数组 这类引用数据类型 因为在栈内存中存的引用地址 所以其堆内存中的内容是会被改变的 
     若不想被改变 加 freeze()方法冻结 
    */</span>
   <span class="hljs-keyword">const</span> esObj =&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">"es6"</span>,
    <span class="hljs-attr">year</span>:<span class="hljs-string">'2015'</span>,
    <span class="hljs-attr">extension</span>:[<span class="hljs-string">"es7"</span>,<span class="hljs-string">"es8"</span>,<span class="hljs-string">"es9"</span>]
   &#125;
   <span class="hljs-built_in">Object</span>.freeze(esObj);
   esObj.extension[<span class="hljs-number">0</span>] = <span class="hljs-string">"es2016"</span>
   <span class="hljs-built_in">console</span>.log(esObj)
   <span class="hljs-comment">/*
   &#123;name: "es6", year: "2015", extension: Array(3)&#125;
    extension: Array(3)
    0: "es2016"
    1: "es8"
    2: "es9"
   */</span>
   <span class="hljs-comment">//说明freeze的冻结只是 浅层次的 内部的数组还是会改变 这！！！ </span>
   <span class="hljs-comment">//看下面封装一下函数  定义一个myFreeze</span>
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFreeze</span>(<span class="hljs-params">obj</span>)</span>&#123;
       <span class="hljs-built_in">Object</span>.freeze(obj);
       <span class="hljs-built_in">Object</span>.keys(Obj).forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>)</span>&#123;  <span class="hljs-comment">//Object.keys()方法会返回一个当前对象属性所组成的数组</span>
           <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj[key] === <span class="hljs-string">"object"</span>)&#123;    <span class="hljs-comment">//如果key对应的属性的值是一个对象的话</span>
            myFreeze(obj[key])                  <span class="hljs-comment">//那么再次冻结 递归 再次执行 </span>
           &#125;
       &#125;)
   &#125;
   
   <span class="hljs-comment">//方法2</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">meFreeze</span>(<span class="hljs-params">obj</span>)</span>&#123;
        <span class="hljs-comment">//判断参数是否为object </span>
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj)&#123;
                <span class="hljs-keyword">if</span>(obj.hasOwnProperty(key))&#123;
                    <span class="hljs-built_in">Object</span>.defineProperty(obj,key,&#123;
                        <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,  <span class="hljs-comment">//只读属性</span>
                    &#125;)
                    <span class="hljs-built_in">Object</span>.seal(obj)     <span class="hljs-comment">//封闭对象 </span>
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> obj
   &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：在对防篡改对象或者冻结对象时，在非严格模式和严格模式下，抛出的结果不一样 如果有错误或者不严谨的地方，请留言备注，十分感谢，对作者也是一种鼓励。</p></div>  
</div>
            