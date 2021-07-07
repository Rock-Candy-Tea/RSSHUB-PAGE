
---
title: '勇敢猿猿，不怕困难！！！---手写Promise（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7873'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 06:20:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=7873'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">这部分是手写Promsie的重头戏，没看我手写Promise（上）的同学，请先看完</h3>
<p><a href="https://juejin.cn/post/6981067302221381640" target="_blank">勇敢猿猿，不怕困难！！！---手写Promise（上）</a></p>
<h3 data-id="heading-1">重头戏</h3>
<ul>
<li>紧接上回，我们把promise基本特点已经写完了，这篇开始写调用<code>.then</code>方法返回一个新的Promise实例等进阶的promise特点</li>
<li><code>.then</code>方法在调用时，里面有两个函数参数（onfulfilled和onrejected），分别是在promise实例成功/失败时调用。而且这两个函数的执行是否成功，也决定着返回的新的实例的状态。只要这个两个函数执行报错，那么新实例的就会执行rejec函数，变为失败状态。</li>
<li>还有一点就是新的promise实例的状态也取决于返回的是否是一个新的promise实例来决定</li>
<li><code>.then</code> 方法如果没传第一个函数参数或者第二个函数参数，系统默认传一个函数参数，成功的函数没传的话，直接传一个返回本身，失败的函数没传，就抛出一个异常，可以供下一个<code>.then</code>继续执行</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype = &#123;
          <span class="hljs-comment">//是否是自定义</span>
          <span class="hljs-attr">customize</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">constructor</span>: <span class="hljs-built_in">Promise</span>,
          <span class="hljs-comment">// 执行then的时候，是异步执行,会返回一个新的Promise实例</span>
           <span class="hljs-attr">then</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
            <span class="hljs-comment">//处理onfulfilled/onrejected不传值的情况</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onfulfilled !== <span class="hljs-string">'function'</span>) &#123;
              onfulfilled = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onfulfilled</span>(<span class="hljs-params">value</span>) </span>&#123;
                <span class="hljs-keyword">return</span> value;
              &#125;;
            &#125;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> onrejected !== <span class="hljs-string">'function'</span>) &#123;
              onrejected = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onrejected</span>(<span class="hljs-params">reason</span>) </span>&#123;
                <span class="hljs-keyword">throw</span> reason;
              &#125;;
            &#125;
<span class="hljs-comment">//self是原始promise实例</span>
            <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
            <span class="hljs-comment">//promise是新的promise实例</span>
            <span class="hljs-keyword">var</span> promise=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve,reject</span>)</span>&#123;
            <span class="hljs-keyword">switch</span> (self.PromiseState) &#123;
                <span class="hljs-comment">//知道状态的情况</span>
                <span class="hljs-keyword">case</span> <span class="hljs-string">'fullfilled'</span>:
                  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    <span class="hljs-keyword">try</span> &#123;
                      <span class="hljs-keyword">var</span> x = onfulfilled(self.PromiseResult);
                      resolvePromise(promise, x, resolve, reject);
                      <span class="hljs-comment">//还得判断x是不是promise实例</span>
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                      <span class="hljs-comment">//报错就执行reject</span>
                      reject(err);
                    &#125;
                  &#125;);
                  <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> <span class="hljs-string">'rejected'</span>:
                  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    <span class="hljs-keyword">try</span> &#123;
                      <span class="hljs-keyword">var</span> x = onrejected(self.PromiseResult);
                      resolvePromise(promise, x, resolve, reject);
                    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                      reject(error);
                    &#125;
                  &#125;);
                  <span class="hljs-keyword">break</span>;
                <span class="hljs-comment">/* 
                不知道实例状态的时候(executor函数中是一个异步操作)
                此时我们应该把基于then传入的方法存起来,在执行resolve/reject函数时，通知其执行
                */</span>
                <span class="hljs-keyword">default</span>:
                  <span class="hljs-comment">// self.onFulfilledCallbacks.push(onfulfilled);</span>
                  <span class="hljs-comment">// self.onRejectedCallbacks.push(onrejected);</span>
                  <span class="hljs-comment">//存放匿名函数的好处就是可以接收onfulfilled/onrejected返回值，判断其是否报错</span>
                  self.onFulfilledCallbacks.push(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">PromiseResult</span>) </span>&#123;
                    <span class="hljs-keyword">try</span> &#123;
                      <span class="hljs-keyword">var</span> x = onfulfilled(PromiseResult);
                      resolvePromise(promise, x, resolve, reject);
                    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                      reject(error);
                    &#125;
                  &#125;);
                  self.onRejectedCallbacks.push(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">PromiseResult</span>) </span>&#123;
                    <span class="hljs-keyword">try</span> &#123;
                      <span class="hljs-keyword">var</span> x = onrejected(PromiseResult);
                      resolvePromise(promise, x, resolve, reject);
                    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                      reject(error);
                    &#125;
                  &#125;);
                  <span class="hljs-keyword">break</span>;
              &#125;
            &#125;)
            <span class="hljs-comment">//返回一个新的promise实例</span>
            <span class="hljs-keyword">return</span> promise;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>这是统一处理基于then返回新实例的成功和失败</p>
</li>
<li>
<p>首先判断返回值和当前的创建的新实例是否一样，一样的话就会产生死循环。</p>
</li>
<li>
<p>根据Promise A+ 规范知道，是否是一个promise实例，有几点条件</p>
<ul>
<li>必须是函数或者对象</li>
<li>必须有<code>.then</code>方法</li>
</ul>
</li>
<li>
<p>这样的话，如果<code>.then</code>方法的两个函数参数的返回值不是一个promise实例的话，直接就把新的promise实例就变为成功态了，如果是一个promise实例，则必须判断是否满足以上的条件，然后再根据执行resolve/reject判断新的promise实例的状态</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 
          promise:处理的那个promise实例
          x:执行onfulfilled/onrejected拿到的结果
          resolve:promsie变成功
          reject:promise变失败

         */</span>
 <span class="hljs-comment">//统一处理基于then返回新实例的成功和失败</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise, x, resolve, reject</span>) </span>&#123;
          <span class="hljs-comment">//如果返回值和当前的创建的新实例一样，形成死循环</span>
          <span class="hljs-keyword">if</span> (x === promise) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise #<Promise>'</span>);
          &#125;
          <span class="hljs-keyword">if</span> ((x !== <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span>) || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>) &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">var</span> then = x.then;
              <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123;
                <span class="hljs-comment">//走到这一步，返回结果一定是一个新的promsie实例</span>
                then.call(
                  x,
                  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">y</span>) </span>&#123;
                    resolve(y);
                  &#125;,
                  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">r</span>) </span>&#123;
                    reject(r);
                  &#125;
                );
              &#125; <span class="hljs-keyword">else</span> &#123;
                resolve(x);
              &#125;
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error);
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            resolve(x);
          &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            