
---
title: 'Lodash 源码解读（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2478'
author: 掘金
comments: false
date: Mon, 03 May 2021 04:35:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=2478'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>书接上文：<a href="https://blog.jack-wjq.cn/blog/fe-framework/lodash1" target="_blank" rel="nofollow noopener noreferrer">Lodash 源码解读（一）</a></p>
<h2 data-id="heading-1">.internal</h2>
<h3 data-id="heading-2">arrayIncludesWith</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 类似 arrayIncludes 的函数
 * 不同之处在于可以传入一个比较函数
 *
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> </span>[array] 需要查找的数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target 需要搜索的值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Function&#125;</span> </span>comparator 对每个元素调用的比较函数
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span> </span>如果 target 被找到则返回 true 否则返回 false
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">arrayIncludesWith</span>(<span class="hljs-params">array, target, comparator</span>) </span>&#123;
  <span class="hljs-comment">// 利用了 JavaScript 在 == 时会自动进行类型转换的特性</span>
  <span class="hljs-comment">// 过滤了 undefined 和 null</span>
  <span class="hljs-keyword">if</span> (array == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> array) &#123;
    <span class="hljs-keyword">if</span> (comparator(target, value)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> arrayIncludesWith;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">arrayLikeKeys</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> isArguments <span class="hljs-keyword">from</span> <span class="hljs-string">'../isArguments.js'</span>;
<span class="hljs-keyword">import</span> isBuffer <span class="hljs-keyword">from</span> <span class="hljs-string">'../isBuffer.js'</span>;
<span class="hljs-keyword">import</span> isIndex <span class="hljs-keyword">from</span> <span class="hljs-string">'./isIndex.js'</span>;
<span class="hljs-keyword">import</span> isTypedArray <span class="hljs-keyword">from</span> <span class="hljs-string">'../isTypedArray.js'</span>;

<span class="hljs-comment">/** 从 Object 的 prototype 上取 hasOwnProperty 用于检测对象本身的属性 */</span>
<span class="hljs-keyword">const</span> hasOwnProperty = <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty;

<span class="hljs-comment">/**
 * 为 array-like 的值创建可枚举属性名的数组
 *
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 需要查询的值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;boolean&#125;</span> </span>inherited 指定返回继承（原型上）的属性名
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Array&#125;</span> </span>返回可枚举属性名的数组
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">arrayLikeKeys</span>(<span class="hljs-params">value, inherited</span>) </span>&#123;
  <span class="hljs-comment">// 判断是否为 array 或 array-like</span>
  <span class="hljs-keyword">const</span> isArr = <span class="hljs-built_in">Array</span>.isArray(value);
  <span class="hljs-keyword">const</span> isArg = !isArr && isArguments(value);
  <span class="hljs-keyword">const</span> isBuff = !isArr && !isArg && isBuffer(value);
  <span class="hljs-keyword">const</span> isType = !isArr && !isArg && !isBuff && isTypedArray(value);
  <span class="hljs-comment">// 如果 value 是 array 或 array-like 则需要收集 index</span>
  <span class="hljs-keyword">const</span> skipIndexes = isArr || isArg || isBuff || isType;
  <span class="hljs-keyword">const</span> length = value.length;
  <span class="hljs-comment">// 实例化一个新数组 长度为 value.length 相同或为 0</span>
  <span class="hljs-comment">// 新数组长度取决于 value 是否为 array 或 array-like</span>
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(skipIndexes ? length : <span class="hljs-number">0</span>);
  <span class="hljs-keyword">let</span> index = skipIndexes ? -<span class="hljs-number">1</span> : length;
  <span class="hljs-comment">// 收集 index</span>
  <span class="hljs-keyword">while</span> (++index < length) &#123;
    result[index] = <span class="hljs-string">`<span class="hljs-subst">$&#123;index&#125;</span>`</span>;
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> value) &#123;
    <span class="hljs-keyword">if</span> (
      <span class="hljs-comment">// 如果 inherited 为 true 则允许遍历继承（原型上）的属性名</span>
      <span class="hljs-comment">// 否则只允许遍历自身的属性名</span>
      (inherited || hasOwnProperty.call(value, key)) &&
      <span class="hljs-comment">// 如果 value 是 array 或 array-like</span>
      <span class="hljs-comment">// 且当前属性名为 length 或当前属性为 index</span>
      <span class="hljs-comment">// 则跳过当前属性名</span>
      !(
        skipIndexes &&
        <span class="hljs-comment">// Safari 9 在严格模式下 arguments.length 是可枚举的</span>
        (key === <span class="hljs-string">'length'</span> ||
          <span class="hljs-comment">// 跳过 index</span>
          isIndex(key, length))
      )
    ) &#123;
      result.push(key);
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> arrayLikeKeys;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>arrayLikeKeys</code> 函数的作用比较难直接通过阅读源码来理解，所以需要逐行解析一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isArr = <span class="hljs-built_in">Array</span>.isArray(value);
<span class="hljs-keyword">const</span> isArg = !isArr && isArguments(value);
<span class="hljs-keyword">const</span> isBuff = !isArr && !isArg && isBuffer(value);
<span class="hljs-keyword">const</span> isType = !isArr && !isArg && !isBuff && isTypedArray(value);
<span class="hljs-keyword">const</span> skipIndexes = isArr || isArg || isBuff || isType;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一连串的或且非运算，为了判断 <code>value</code> 是否为 <code>array/array-like</code>，如果是则需要收集 <code>index</code> 至 <code>result</code> 中，否则不需要。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> length = value.length;
<span class="hljs-keyword">const</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(skipIndexes ? length : <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要收集 <code>index</code> 则实例化一个与 <code>value</code> 等长的数组，否则实例化一个长度为 <code>0</code> 的数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> index = skipIndexes ? -<span class="hljs-number">1</span> : length;
<span class="hljs-keyword">while</span> (++index < length) &#123;
  result[index] = <span class="hljs-string">`<span class="hljs-subst">$&#123;index&#125;</span>`</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理，如果需要收集 <code>index</code>，则需要将 <code>index</code> 初始化为 <code>-1</code>，从左向右遍历，否则跳过收集 <code>index</code> 的过程（遍历）。</p>
<p>但是可以看到后面使用了 <code>for...in</code> 遍历 <code>value</code> 的 <code>key</code>，<code>index</code> 应该也是会被遍历出来的，为什么还是使用了一个 <code>while</code> 循环来遍历 <code>index</code> 呢？</p>
<p>这里涉及到了一个比较深入的知识点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">100</span>);
arr[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>;
arr[<span class="hljs-number">50</span>] = <span class="hljs-number">50</span>;
arr[<span class="hljs-number">99</span>] = <span class="hljs-number">99</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> index <span class="hljs-keyword">in</span> arr) &#123;
  <span class="hljs-built_in">console</span>.log(index);
&#125;
<span class="hljs-comment">// => 0</span>
<span class="hljs-comment">// => 50</span>
<span class="hljs-comment">// => 99</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在数组为稀疏数组时，<code>for...in</code> 不会遍历所有 <code>index</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> value) &#123;
  <span class="hljs-keyword">if</span> (
    (inherited || hasOwnProperty.call(value, key)) &&
    !(skipIndexes && (key === <span class="hljs-string">'length'</span> || isIndex(key, length)))
  ) &#123;
    result.push(key);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>value</code> 上的其他属性需要用 <code>for...in</code> 遍历，由于 <code>for...in</code> 还会遍历 <code>value</code> 原型上的属性，所以还需要对属性做一层判断。</p>
<pre><code class="hljs language-js copyable" lang="js">inherited || hasOwnProperty.call(value, key);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>inherited</code> 为 <code>true</code> 时允许遍历原型上的属性，否则只允许遍历自身属性。</p>
<pre><code class="hljs language-js copyable" lang="js">!(skipIndexes && (key === <span class="hljs-string">'length'</span> || isIndex(key, length)));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>value</code> 为 <code>array/array-like</code> 时，<code>index</code> 已经被遍历过，所以在这里要跳过。</p>
<p>但是 <code>Safari 9</code> 在严格模式下 <code>arguments.length</code> 是可枚举的，所以会被遍历到，需要剔除。</p>
<p>最终所有符合条件的属性名都会被 <code>push</code> 到 <code>result</code> 中并返回。</p>
<p><code>arrayLikeKeys</code> 函数引入了 <code>isArguments</code>、<code>isBuffer</code>、<code>isIndex</code>、<code>isTypedArray</code> 函数，所以这些函数的实现也需要了解一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> getTag <span class="hljs-keyword">from</span> <span class="hljs-string">'./.internal/getTag.js'</span>;
<span class="hljs-keyword">import</span> isObjectLike <span class="hljs-keyword">from</span> <span class="hljs-string">'./isObjectLike.js'</span>;

<span class="hljs-comment">/**
 * 检测 value 是否为 arguments 对象
 *
 * <span class="hljs-doctag">@since </span>0.1.0
 * <span class="hljs-doctag">@category <span class="hljs-variable">Lang</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 需要检测的值
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span> </span>如果 value 为 arguments 对象则返回 true 否则返回 false
 * <span class="hljs-doctag">@example</span>
 *
 * isArguments(function() &#123; return arguments &#125;())
 * // => true
 *
 * isArguments([1, 2, 3])
 * // => false
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArguments</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> isObjectLike(value) && getTag(value) == <span class="hljs-string">'[object Arguments]'</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> isArguments;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>isArguments</code> 函数又引入了 <code>isObjectLike</code> 和 <code>getTag</code> 函数，所以这些函数的实现也需要了解一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 检测 value 是否为 object-like
 * object-like 的 value 不为 null 且 typeof 的结果为 "object"
 *
 * <span class="hljs-doctag">@since </span>4.0.0
 * <span class="hljs-doctag">@category <span class="hljs-variable">Lang</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 需要检测的值
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span> </span>如果 value 为 object-like 则返回 true 否则返回 false
 * <span class="hljs-doctag">@example</span>
 *
 * isObjectLike(&#123;&#125;)
 * // => true
 *
 * isObjectLike([1, 2, 3])
 * // => true
 *
 * isObjectLike(Function)
 * // => false
 *
 * isObjectLike(null)
 * // => false
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObjectLike</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// JavaScript 历史遗留问题</span>
  <span class="hljs-comment">// typeof null === "object"</span>
  <span class="hljs-comment">// 在最初的 JavaScript 中 值是以 32 位为一个内存单元存储的</span>
  <span class="hljs-comment">// 每个内存单元包含 1~3 位类型标记和值的实际数据内容</span>
  <span class="hljs-comment">// 类型标记为 000 的值为 object 实际数据内容为对象的引用</span>
  <span class="hljs-comment">// null 表示空值 即 32 位全为 0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && value !== <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> isObjectLike;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 从 Object 的 prototype 上取 toString 用于获取类型标记 */</span>
<span class="hljs-keyword">const</span> toString = <span class="hljs-built_in">Object</span>.prototype.toString;

<span class="hljs-comment">/**
 * 获取 value 的 toStringTag
 *
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 需要检测的值
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;string&#125;</span> </span>返回 toStringTag
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTag</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// 利用了 JavaScript 在 == 时会自动进行类型转换的特性</span>
  <span class="hljs-comment">// 过滤了 undefined 和 null</span>
  <span class="hljs-keyword">if</span> (value == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> value === <span class="hljs-literal">undefined</span> ? <span class="hljs-string">'[object Undefined]'</span> : <span class="hljs-string">'[object Null]'</span>;
  &#125;
  <span class="hljs-keyword">return</span> toString.call(value);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> getTag;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鉴于 <code>isBuffer</code>、<code>isIndex</code>、<code>isTypedArray</code> 函数较为复杂，请看下回分解。</p></div>  
</div>
            