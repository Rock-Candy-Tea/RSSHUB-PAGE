
---
title: 'JS训练营(一) _ 异步编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4100'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 13:45:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4100'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第17天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>面对大厂，熟练掌握JS和深厚的算法基础是必备的，而网络、浏览器相关的知识点也是重点考察的范围，今天开始逐一分析JS基础、V8引擎、Webkit、JSCore等等知识点并深入各个细节。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>本文需要复习的基础目录：</p>
<ul>
<li>
<p>1.用MVVM框架时为什么要在列表组件中写key的作用</p>
</li>
<li>
<p>2.['1', '2', '3'].map(parseInt) what & why</p>
</li>
<li>
<p>3.什么是防抖和节流？有什么区别？如何实现</p>
</li>
<li>
<p>4.Set、Map、WeakSet 和 WeakMap 的区别</p>
</li>
<li>
<p>5.深度优先遍历和广度优先遍历，如何实现</p>
</li>
<li>
<p>6.ES5/ES6 的继承除了写法以外还有什么区别</p>
</li>
<li>
<p>7.setTimeout、Promise、Async/Await 的区别</p>
</li>
<li>
<p>8.Async/Await 如何通过同步的方式实现异步</p>
</li>
<li>
<p>9.将数组扁平化并去除其中重复数据</p>
</li>
<li>
<p>10.JS 异步解决方案的发展历程以及优缺点</p>
</li>
</ul>
<h2 data-id="heading-1">1.用MVVM框架时为什么要在列表组件中写key的作用</h2>
<p>首先，这种提示在小程序也会经常爆出黄字警告，但并不是非带不可，在不带key的情况下，对于简单列表页渲染来说diff节点更快是没有错误的。但是这并不是key的作用。在Vue.js文档也说明了这个默认的模式是高效的，但是只适用于不依赖子组件状态或临时 DOM 状态 (例如：表单输入值) 的列表渲染输出。
key是给每一个vnode的唯一id,可以依靠key,更准确, 更快的拿到oldVnode中对应的vnode节点。</p>
<h3 data-id="heading-2">更准确</h3>
<p>因为带key就不是就地复用了，在sameNode函数 a.key === b.key对比中可以避免就地复用的情况。所以会更加准确。</p>
<h3 data-id="heading-3">更快</h3>
<p>利用key的唯一性生成map对象来获取对应节点，比遍历方式更快。(这个观点，就是我最初的那个观点。从这个角度看，map会比遍历更快。)</p>
<p>vue和react都是采用diff算法来对比新旧虚拟节点，从而更新节点。在vue的diff函数中（建议先了解一下diff算法过程）。
在交叉对比中，当新节点跟旧节点头尾交叉对比没有结果时，会根据新节点的key去对比旧节点数组中的key，从而找到相应旧节点（这里对应的是一个key => index 的map映射）。如果没找到就认为是一个新增节点。而如果没有key，那么就会采用遍历查找的方式去找到对应的旧节点。一种一个map映射，另一种是遍历查找。相比而言。map映射的速度更快。
vue部分源码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue项目  src/core/vdom/patch.js  -488行</span>
<span class="hljs-comment">// 以下是为了阅读性进行格式化后的代码</span>

<span class="hljs-comment">// oldCh 是一个旧虚拟节点数组</span>
<span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) &#123;
  oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
&#125;
<span class="hljs-keyword">if</span>(isDef(newStartVnode.key)) &#123;
  <span class="hljs-comment">// map 方式获取</span>
  idxInOld = oldKeyToIdx[newStartVnode.key]
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 遍历方式获取</span>
  idxInOld = findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
&#125;

<span class="hljs-comment">// 创建map函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span> (<span class="hljs-params">children, beginIdx, endIdx</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i, key
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  <span class="hljs-keyword">for</span> (i = beginIdx; i <= endIdx; ++i) &#123;
    key = children[i].key
    <span class="hljs-keyword">if</span> (isDef(key)) map[key] = i
  &#125;
  <span class="hljs-keyword">return</span> map
&#125;

<span class="hljs-comment">// 遍历寻找 sameVnode 是对比新旧节点是否相同的函数</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findIdxInOld</span> (<span class="hljs-params">node, oldCh, start, end</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start; i < end; i++) &#123;
      <span class="hljs-keyword">const</span> c = oldCh[i]

      <span class="hljs-keyword">if</span> (isDef(c) && sameVnode(node, c)) <span class="hljs-keyword">return</span> i
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个性能提升的前提有一句“刻意依赖默认行为”，也就是说不是说你不带key就会有性能提升，主要是为了提升diff【同级比较】的效率。自己想一下自己要实现前后列表的diff，如果对列表的每一项增加一个key，即唯一索引，那就可以很清楚的知道两个列表谁少了谁没变。而如果不加key的话，就只能一个个对比了。</p>
<h2 data-id="heading-4">2.['1', '2', '3'].map(parseInt) what & why ?</h2>
<p>答案是[1, NaN, NaN]。
首先让我们回顾一下，map函数的第一个参数callback：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> new_array = arr.map(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callback</span>(<span class="hljs-params">currentValue[, index[, array]]</span>) </span>&#123; 
    <span class="hljs-comment">// Return element for new_array </span>
&#125;[, thisArg])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个callback一共可以接收三个参数，其中第一个参数代表当前被处理的元素，而第二个参数代表该元素的索引。
而parseInt则是用来解析字符串的，使字符串成为指定基数的整数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(string, radix)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接收两个参数，第一个表示被处理的值（字符串），第二个表示为解析时的基数。
了解这两个函数后，我们可以模拟一下运行情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'1'</span>, <span class="hljs-number">0</span>) <span class="hljs-comment">//radix为0时，且string参数不以“0x”和“0”开头时，按照10为基数处理。这个时候返回1</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'2'</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">//基数为1（1进制）表示的数中，最大值小于2，所以无法解析，返回NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'3'</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">//基数为2（2进制）表示的数中，最大值小于3，所以无法解析，返回NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>map函数返回的是一个数组，所以最后结果为[1, NaN, NaN]</p>
<h2 data-id="heading-5">3.什么是防抖和节流？有什么区别？如何实现？</h2>
<p>这个我在之前的文章有专门介绍过：
解读js函数防抖与函数节流</p>
<h3 data-id="heading-6">1.防抖</h3>
<p>触发高频事件后n秒内函数只会执行一次，如果n秒内高频事件再次被触发，则重新计算时间</p>
<p>思路：</p>
<p>每次触发事件时都取消之前的延时调用方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn</span>) </span>&#123;
      <span class="hljs-keyword">let</span> timeout = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 创建一个标记用来存放定时器的返回值</span>
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">clearTimeout</span>(timeout); <span class="hljs-comment">// 每当用户输入的时候把前一个 setTimeout clear 掉</span>
        timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 然后又创建一个新的 setTimeout, 这样就能保证输入字符后的 interval 间隔内如果还有字符输入的话，就不会执行 fn 函数</span>
          fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
        &#125;, <span class="hljs-number">500</span>);
      &#125;;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'防抖成功'</span>);
    &#125;

    <span class="hljs-keyword">var</span> inp = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'inp'</span>);
    inp.addEventListener(<span class="hljs-string">'input'</span>, debounce(sayHi)); <span class="hljs-comment">// 防抖</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.节流</h3>
<p>高频事件触发，但在n秒内只会执行一次，所以节流会稀释函数的执行频率</p>
<p>思路：</p>
<p>每次触发事件时都判断当前是否有等待执行的延时函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn</span>) </span>&#123;
      <span class="hljs-keyword">let</span> canRun = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 通过闭包保存一个标记</span>
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!canRun) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 在函数开头判断标记是否为true，不为true则return</span>
        canRun = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 立即设置为false</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 将外部传入的函数的执行放在setTimeout中</span>
          fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
          <span class="hljs-comment">// 最后在setTimeout执行完毕后再把标记设置为true(关键)表示可以执行下一次循环了。当定时器没有执行的时候标记永远是false，在开头被return掉</span>
          canRun = <span class="hljs-literal">true</span>;
        &#125;, <span class="hljs-number">500</span>);
      &#125;;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params">e</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(e.target.innerWidth, e.target.innerHeight);
    &#125;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'resize'</span>, throttle(sayHi));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4.Set、Map、WeakSet 和 WeakMap 的区别？</h2>
<h3 data-id="heading-9">Set</h3>
<h4 data-id="heading-10">1.成员不能重复</h4>
<h4 data-id="heading-11">2.只有健值，没有健名，有点类似数组。可以遍历，方法有add, delete,has</h4>
<h3 data-id="heading-12">weakSet</h3>
<ul>
<li>1.成员都是对象</li>
<li>2.成员都是弱引用，随时可以消失。可以用来保存DOM节点，不容易造成内存泄漏</li>
<li>3.不能遍历，方法有add, delete,has</li>
</ul>
<h3 data-id="heading-13">Map</h3>
<ul>
<li>1.本质上是健值对的集合，类似集合</li>
<li>2.可以遍历，方法很多，可以干跟各种数据格式转换</li>
</ul>
<h3 data-id="heading-14">weakMap</h3>
<ul>
<li>1.直接受对象作为健名（null除外），不接受其他类型的值作为健名</li>
<li>2.健名所指向的对象，不计入垃圾回收机制</li>
<li>3.不能遍历，方法同get,set,has,delete</li>
</ul>
<h2 data-id="heading-15">5.深度优先遍历和广度优先遍历，如何实现？</h2>
<h3 data-id="heading-16">深度优先遍历（DFS）</h3>
<p>深度优先遍历（Depth-First-Search），是搜索算法的一种，它沿着树的深度遍历树的节点，尽可能深地搜索树的分支。当节点v的所有边都已被探寻过，将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已探寻源节点到其他所有节点为止，如果还有未被发现的节点，则选择其中一个未被发现的节点为源节点并重复以上操作，直到所有节点都被探寻完成。
简单的说，DFS就是从图中的一个节点开始追溯，直到最后一个节点，然后回溯，继续追溯下一条路径，直到到达所有的节点，如此往复，直到没有路径为止。
DFS 可以产生相应图的拓扑排序表，利用拓扑排序表可以解决很多问题，例如最大路径问题。一般用堆数据结构来辅助实现DFS算法。
注意：深度DFS属于盲目搜索，无法保证搜索到的路径为最短路径，也不是在搜索特定的路径，而是通过搜索来查看图中有哪些路径可以选择。
步骤：</p>
<ul>
<li>1.访问顶点v；</li>
<li>2.依次从v的未被访问的邻接点出发，对图进行深度优先遍历；直至图中和v有路径相通的顶点都被访问；</li>
<li>3.若此时途中尚有顶点未被访问，则从一个未被访问的顶点出发，重新进行深度优先遍历，直到所有顶点均被访问过为止；</li>
</ul>
<p>实现：</p>
<pre><code class="hljs language-js copyable" lang="js">Graph.prototype.dfs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> marked = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-built_in">this</span>.vertices.length; i++) &#123;
        <span class="hljs-keyword">if</span> (!marked[<span class="hljs-built_in">this</span>.vertices[i]]) &#123;
            dfsVisit(<span class="hljs-built_in">this</span>.vertices[i])
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfsVisit</span>(<span class="hljs-params">u</span>) </span>&#123;
        <span class="hljs-keyword">let</span> edges = <span class="hljs-built_in">this</span>.edges
        marked[u] = <span class="hljs-literal">true</span>
        <span class="hljs-built_in">console</span>.log(u)
        <span class="hljs-keyword">var</span> neighbors = edges.get(u)
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<neighbors.length; i++) &#123;
            <span class="hljs-keyword">var</span> w = neighbors[i]
            <span class="hljs-keyword">if</span> (!marked[w]) &#123;
                dfsVisit(w)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">广度优先遍历（BFS）</h3>
<p>广度优先遍历（Breadth-First-Search）是从根节点开始，沿着图的宽度遍历节点，如果所有节点均被访问过，则算法终止，BFS 同样属于盲目搜索，一般用队列数据结构来辅助实现BFS
BFS从一个节点开始，尝试访问尽可能靠近它的目标节点。本质上这种遍历在图上是逐层移动的，首先检查最靠近第一个节点的层，再逐渐向下移动到离起始节点最远的层
步骤：</p>
<ul>
<li>
<p>创建一个队列，并将开始节点放入队列中</p>
</li>
<li>
<p>若队列非空，则从队列中取出第一个节点，并检测它是否为目标节点</p>
</li>
<li>
<p>若是目标节点，则结束搜寻，并返回结果</p>
</li>
<li>
<p>若不是，则将它所有没有被检测过的字节点都加入队列中</p>
</li>
<li>
<p>若队列为空，表示图中并没有目标节点，则结束遍历</p>
</li>
</ul>
<p>实现：</p>
<pre><code class="hljs language-js copyable" lang="js">Graph.prototype.bfs = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">v</span>) </span>&#123;
    <span class="hljs-keyword">var</span> queue = [], marked = []
    marked[v] = <span class="hljs-literal">true</span>
    queue.push(v) <span class="hljs-comment">// 添加到队尾</span>
    <span class="hljs-keyword">while</span>(queue.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">var</span> s = queue.shift() <span class="hljs-comment">// 从队首移除</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.edges.has(s)) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'visited vertex: '</span>, s)
        &#125;
        <span class="hljs-keyword">let</span> neighbors = <span class="hljs-built_in">this</span>.edges.get(s)
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<neighbors.length;i++) &#123;
            <span class="hljs-keyword">var</span> w = neighbors[i]
            <span class="hljs-keyword">if</span> (!marked[w]) &#123;
                marked[w] = <span class="hljs-literal">true</span>
                queue.push(w)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">6.ES5/ES6 的继承除了写法以外还有什么区别</h2>
<p>JavaScript相比于其他面向类的语言，在实现继承时并没有真正对构造类进行复制，当我们使用var children = new Parent()继承父类时，我们理所当然的理解为children ”为parent所构造“。实际上这是一种错误的理解。严格来说，JS才是真正的面向对象语言，而不是面向类语言。它所实现的继承，都是通过每个对象创建之初就存在的prototype属性进行关联、委托，从而建立练习，间接的实现继承，实际上不会复制父类。
ES5最常见的两种继承：原型链继承、构造函数继承</p>
<h3 data-id="heading-19">1.原型链继承</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 定义父类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.name = name;
    &#125;

    Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;;

    <span class="hljs-comment">// 定义子类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Children</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.age = <span class="hljs-number">24</span>;
    &#125;

    <span class="hljs-comment">// 通过Children的prototype属性和Parent进行关联继承</span>

    Children.prototype = <span class="hljs-keyword">new</span> Parent(<span class="hljs-string">'程序员思语'</span>);

    <span class="hljs-comment">// Children.prototype.constructor === Parent.prototype.constructor = Parent</span>

    <span class="hljs-keyword">var</span> test = <span class="hljs-keyword">new</span> Children();

    <span class="hljs-comment">// test.constructor === Children.prototype.constructor === Parent</span>

    test.age <span class="hljs-comment">// 24</span>
    test.getName(); <span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以发现，整个继承过程，都是通过原型链之间的指向进行委托关联，直到最后形成了”由构造函数所构造“的结局。</p>
<h3 data-id="heading-20">2.构造函数继承</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 定义父类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.language = [<span class="hljs-string">'javascript'</span>, <span class="hljs-string">'react'</span>, <span class="hljs-string">'node.js'</span>];
        <span class="hljs-built_in">this</span>.value = value;
    &#125;

    <span class="hljs-comment">// 定义子类</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Children</span>(<span class="hljs-params"></span>) </span>&#123;
        Parent.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    &#125;

    <span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> Children(<span class="hljs-number">666</span>);
    test.language <span class="hljs-comment">// ['javascript', 'react', 'node.js']</span>
    test.value <span class="hljs-comment">// 666</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造继承关键在于，通过在子类的内部调用父类，即通过使用apply()或call()方法可以在将来新创建的对象上获取父类的成员和方法。</p>
<h3 data-id="heading-21">ES6的继承</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 定义父类</span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father</span> </span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.name = name;
            <span class="hljs-built_in">this</span>.age = age;
        &#125;

        <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我叫:<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>， 今年<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>岁`</span>);
        &#125;
    &#125;;

    <span class="hljs-comment">// 通过extends关键字实现继承</span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father</span> </span>&#123;&#125;;
    <span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> Son(<span class="hljs-string">'程序员思语'</span>, <span class="hljs-number">3000</span>);
    son.show(); <span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6中新增了class关键字来定义类，通过保留的关键字extends实现了继承。实际上这些关键字只是一些语法糖，底层实现还是通过原型链之间的委托关联关系实现继承。</p>
<h3 data-id="heading-22">总结</h3>
<p>区别于ES5的继承，ES6的继承实现在于使用super关键字调用父类，反观ES5是通过call或者apply回调方法调用父类。</p>
<h2 data-id="heading-23">7.setTimeout、Promise、Async/Await 的区别</h2>
<p>注意区分这三者在事件循环中的区别，事件循环中分为宏任务队列和微任务队列。其中settimeout的回调函数放到宏任务队列里，等到执行栈清空以后执行；promise.then里的回调函数会放到相应宏任务的微任务队列里，等宏任务里面的同步代码执行完再执行；async函数表示函数里面可能会有异步方法，await后面跟一个表达式，async方法执行时，遇到await会立即执行表达式，然后把表达式后面的代码放到微任务队列里，让出执行栈让同步代码先执行。</p>
<h3 data-id="heading-24">1. setTimeout</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>)    <span class="hljs-comment">//1. 打印 script start</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'settimeout'</span>)    <span class="hljs-comment">// 4. 打印 settimeout</span>
&#125;)    <span class="hljs-comment">// 2. 调用 setTimeout 函数，并定义其完成后执行的回调函数</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>)    <span class="hljs-comment">//3. 打印 script start</span>
<span class="hljs-comment">// 输出顺序：script start->script end->settimeout</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">2. Promise</h3>
<p>Promise本身是同步的立即执行函数， 当在executor中执行resolve或者reject的时候, 此时是异步操作， 会先执行then/catch等，当主栈完成后，才会去调用resolve/reject中存放的方法执行，打印p的时候，是打印的返回结果，一个Promise实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>)
<span class="hljs-keyword">let</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>)
    resolve()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1 end'</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>)
&#125;)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'settimeout'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>)
<span class="hljs-comment">// 输出顺序: script start->promise1->promise1 end->script end->promise2->settimeout</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当JS主线程执行到Promise对象时，</p>
<ul>
<li>
<p>promise1.then() 的回调就是一个 task</p>
</li>
<li>
<p>promise1 是 resolved或rejected: 那这个 task 就会放入当前事件循环回合的 microtask queue</p>
</li>
<li>
<p>promise1 是 pending: 这个 task 就会放入 事件循环的未来的某个(可能下一个)回合的 microtask queue 中</p>
</li>
<li>
<p>setTimeout 的回调也是个 task ，它会被放入 macrotask queue 即使是 0ms 的情况</p>
</li>
</ul>
<h3 data-id="heading-26">3. async/await</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async1 start'</span>);
    <span class="hljs-keyword">await</span> async2();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async1 end'</span>)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async2'</span>)
&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>);
async1();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>)

<span class="hljs-comment">// 输出顺序：script start->async1 start->async2->script end->async1 end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>async 函数返回一个 Promise 对象，当函数执行的时候，一旦遇到 await 就会先返回，等到触发的异步操作完成，再执行函数体内后面的语句。可以理解为，是让出了线程，跳出了 async 函数体。</p>
<p>await的含义为等待，也就是 async 函数需要等待await后的函数执行完成并且有了返回结果（Promise对象）之后，才能继续执行下面的代码。await通过返回一个Promise对象来实现同步的效果。</p>
<h2 data-id="heading-27">8.Async/Await 如何通过同步的方式实现异步</h2>
<p>js 是单线程的，可以使用 async await 用于把异步请求变为同步请求的方式，第一个请求的返回值作为后面一个请求的参数,其中每一个参数都是一个promise对象。</p>
<p>例如：这种情况工作中会经常遇到</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-keyword">await</span> A();
    <span class="hljs-keyword">var</span> b = <span class="hljs-keyword">await</span> B(a);
    <span class="hljs-keyword">var</span> c = <span class="hljs-keyword">await</span> C(b);
    <span class="hljs-keyword">var</span> d = <span class="hljs-keyword">await</span> D(c);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setTimeout 主要用户异步队列的形式，当然其中又分为宏观队列以及微观队列（Promise.then,process.nextTick等），比如隔1000ms执行一段逻辑代码（实际中不一定是1000ms后执行，需要考虑主任务的执行时间）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;, <span class="hljs-number">0</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;, <span class="hljs-number">1000</span>)
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)
    resolve()
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">9.将数组扁平化并去除其中重复数据</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr.flat(<span class="hljs-literal">Infinity</span>))).sort(<span class="hljs-function">(<span class="hljs-params">a,b</span>)=></span>&#123; <span class="hljs-keyword">return</span> a-b&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单demo：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.flat= <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> [].concat(...this.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> (<span class="hljs-built_in">Array</span>.isArray(item) ? item.flat() : [item])));
&#125;

<span class="hljs-built_in">Array</span>.prototype.unique = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> [...new <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">this</span>)]
&#125;

<span class="hljs-keyword">const</span> sort = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b;

<span class="hljs-built_in">console</span>.log(arr.flat().unique().sort(sort)); <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">10.JS 异步解决方案的发展历程以及优缺点</h2>
<h3 data-id="heading-30">1. 回调函数（callback）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// callback 函数体</span>
&#125;, <span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：回调地狱，不能用 try catch 捕获错误，不能 return
回调地狱的根本问题在于：</p>
<ul>
<li>缺乏顺序性：回调地狱导致的调试困难，和大脑的思维方式不符</li>
<li>嵌套函数存在耦合性，一旦有所改动，就会牵一发而动全身，即（控制反转）</li>
<li>嵌套函数过多的多话，很难处理错误</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">ajax(<span class="hljs-string">'XXX1'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// callback 函数体</span>
    ajax(<span class="hljs-string">'XXX2'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// callback 函数体</span>
        ajax(<span class="hljs-string">'XXX3'</span>, <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// callback 函数体</span>
        &#125;)
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：解决了同步的问题（只要有一个任务耗时很长，后面的任务都必须排队等着，会拖延整个程序的执行。）</p>
<h3 data-id="heading-31">2. Promise</h3>
<p>Promise就是为了解决callback的问题而产生的。</p>
<p>Promise 实现了链式调用，也就是说每次 then 后返回的都是一个全新 Promise，如果我们在 then 中 return ，return 的结果会被 Promise.resolve() 包装</p>
<p>优点：解决了回调地狱的问题</p>
<pre><code class="hljs language-js copyable" lang="js">ajax(<span class="hljs-string">'XXX1'</span>)
  .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-comment">// 操作逻辑</span>
      <span class="hljs-keyword">return</span> ajax(<span class="hljs-string">'XXX2'</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-comment">// 操作逻辑</span>
      <span class="hljs-keyword">return</span> ajax(<span class="hljs-string">'XXX3'</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-comment">// 操作逻辑</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：无法取消 Promise ，错误需要通过回调函数来捕获</p>
<h3 data-id="heading-32">3. Generator</h3>
<p>特点：可以控制函数的执行，可以配合 co 函数库使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">fetch</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">yield</span> ajax(<span class="hljs-string">'XXX1'</span>, <span class="hljs-function">() =></span> &#123;&#125;)
    <span class="hljs-keyword">yield</span> ajax(<span class="hljs-string">'XXX2'</span>, <span class="hljs-function">() =></span> &#123;&#125;)
    <span class="hljs-keyword">yield</span> ajax(<span class="hljs-string">'XXX3'</span>, <span class="hljs-function">() =></span> &#123;&#125;)
&#125;
<span class="hljs-keyword">let</span> it = fetch()
<span class="hljs-keyword">let</span> result1 = it.next()
<span class="hljs-keyword">let</span> result2 = it.next()
<span class="hljs-keyword">let</span> result3 = it.next()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">4. Async/await</h3>
<p>async、await 是异步的终极解决方案</p>
<p>优点：代码清晰，不用像 Promise 写一大堆 then 链，处理了回调地狱的问题</p>
<p>缺点：await 将异步代码改造成同步代码，如果多个异步操作没有依赖性而使用 await 会导致性能上的降低。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 以下代码没有依赖性的话，完全可以使用 Promise.all 的方式</span>
  <span class="hljs-comment">// 如果有依赖性的话，其实就是解决回调地狱的例子了</span>
  <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'XXX1'</span>)
  <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'XXX2'</span>)
  <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'XXX3'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面来看一个使用 await 的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">async</span> () => &#123;
  a = a + <span class="hljs-keyword">await</span> <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>, a) <span class="hljs-comment">// -> '2' 10</span>
&#125;
b()
a++
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>, a) <span class="hljs-comment">// -> '1' 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果对于以上代码你可能会有疑惑，让我来解释下原因</p>
<p>首先函数 b 先执行，在执行到 await 10 之前变量 a 还是 0，因为 await 内部实现了 generator ，generator 会保留堆栈中东西，所以这时候 a = 0 被保存了下来</p>
<p>因为 await 是异步操作，后来的表达式不返回 Promise 的话，就会包装成 Promise.reslove(返回值)，然后会去执行函数外的同步代码同步代码执行完毕后开始执行异步代码，将保存下来的值拿出来使用，这时候 a = 0 + 10。</p>
<p>上述解释中提到了 await 内部实现了 generator，其实 await 就是 generator 加上 Promise的语法糖，且内部实现了自动执行 generator。如果你熟悉 co 的话，其实自己就可以实现这样的语法糖。</p></div>  
</div>
            