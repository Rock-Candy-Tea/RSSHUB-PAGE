
---
title: '100行代码实现数组的splice方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9347'
author: 掘金
comments: false
date: Thu, 20 May 2021 18:40:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=9347'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">splice基本了解</h2>
<p>在JavaScript中Array提供了许多方法供我们使用，splice是我们经常会使用到的一个方法。</p>
<p>要实现一个splice方法，我们首先看一下 <code>splice </code>定义 和 用法</p>
<p>定义vs用法:
splice()方法向从数组中添加删除项目，然后返回被删除的项目。</p>
<p><strong>语法</strong>
<code>arrayObject.splice(index,howmany,item1,.....,itemX)</code></p>





















<table><thead><tr><th>参数</th><th>描述</th></tr></thead><tbody><tr><td>index</td><td>必需。整数，规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。</td></tr><tr><td>howmany</td><td>必需。要删除的项目数量。如果设置为 0，则不会删除项目。</td></tr><tr><td>item1, ..., itemX</td><td>可选。向数组添加的新项目。</td></tr></tbody></table>













<table><thead><tr><th>返回值</th><th>描述</th></tr></thead><tbody><tr><td>Array</td><td>包含被删除项目的新数组，如果有的话。</td></tr></tbody></table>
<p><strong>Tips</strong>：splice() 方法与 slice() 方法的作用是不同的，splice() 方法会直接对原数组进行修改。</p>
<p>在清楚了splice方法的基本概念后，首先我们试着来实现一个简易版的</p>
<ol>
<li>拷贝删除的元素</li>
<li>移动删除元素后面的元素</li>
<li>插入新的元素</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">//splice</span>
      <span class="hljs-built_in">Array</span>.prototype.splice = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
        startIndex,
        deleteCount,
        ...addElements
      </span>) </span>&#123;
        <span class="hljs-keyword">let</span> argumentLen = <span class="hljs-built_in">arguments</span>.length;
        <span class="hljs-keyword">let</span> array = <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">this</span>);
        <span class="hljs-keyword">let</span> len = array.length;
        <span class="hljs-keyword">let</span> deleteArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(deleteCount);

        <span class="hljs-comment">//拷贝删除的元素</span>
        sliceDeleteElements(arra, startIndex, deleteCount, deleteArr);
        <span class="hljs-comment">//移动删除元素后面的元素</span>
        movePostElements(array, startIndex, len, deleteCount, addElements);
        <span class="hljs-comment">//插入新的元素</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < addElements.length; i++) &#123;
          array[startIndex+i] = addElements[i];
        &#125;
        array.length = len - deleteCount + addElements.length;
        <span class="hljs-keyword">return</span> deleteArr;
      &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">拷贝删除的元素</h2>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> sliceDeleteElements = <span class="hljs-function">(<span class="hljs-params">array, startIndex, deleteCount, deleteArr</span>) =></span> &#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;i<deleteCount;i++)&#123;
          <span class="hljs-keyword">let</span> index = startIndex + i
          <span class="hljs-keyword">if</span>(index <span class="hljs-keyword">in</span> array) &#123;
            <span class="hljs-keyword">let</span> current = array[index];
            deleteArr[i] = current;
          &#125;
        &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">移动删除元素后面的元素</h2>
<ul>
<li>添加的元素和删除的元素个数相等时</li>
<li>添加元素个数大于删除元素时</li>
<li>添加元素个数小于删除元素时</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//移动删除元素后面的元素</span>
      <span class="hljs-comment">//相等时</span>
      <span class="hljs-keyword">const</span> movePostElements = <span class="hljs-function">(<span class="hljs-params">
        array,
        startIndex,
        len,
        deleteCount,
        addElements
      </span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (deleteCount === addElements.length) <span class="hljs-keyword">return</span>;
      &#125;;
      <span class="hljs-comment">//小于</span>
      <span class="hljs-keyword">const</span> movePostElements = <span class="hljs-function">(<span class="hljs-params">
        array,
        startIndex,
        len,
        deleteCount,
        addElements
      </span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (deleteCount > addElements.length) &#123;
          <span class="hljs-comment">//删除的元素比新增的元素多，后面的元素向前移动</span>
          <span class="hljs-comment">//一共需要向前挪动 len - startIndex - deletecount</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = startIndex + deleteCount; i < len; i++) &#123;
            <span class="hljs-keyword">let</span> formIndex = i;
            <span class="hljs-comment">//将要挪动的目标位置</span>
            <span class="hljs-keyword">if</span> (formIndex <span class="hljs-keyword">in</span> array) &#123;
              array[toIndex] = array[formIndex];
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-keyword">delete</span> array[toIndex];
            &#125;
          &#125;
        &#125;
        <span class="hljs-comment">//当前长度为len + addElements - deleteCount</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = lem - <span class="hljs-number">1</span>; i > len + addElements.length - deleteCount; i--) &#123;
          <span class="hljs-keyword">delete</span> array[i];
        &#125;
      &#125;;
      <span class="hljs-comment">//添加大于删除</span>
      <span class="hljs-keyword">const</span> movePostElements = <span class="hljs-function">(<span class="hljs-params">
        array,
        startIndex,
        len,
        deleteCount,
        addElements
      </span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (deleteCount < addElements.length) &#123;
          <span class="hljs-comment">//删除的元素比新增的元素少，元素整体后前移动</span>
          <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = len - <span class="hljs-number">1</span>;i>=startIndex+deleteCount;i--)&#123;
            <span class="hljs-keyword">let</span> formIndex  = i;
            <span class="hljs-comment">//将要挪动的目标位置</span>
            <span class="hljs-keyword">let</span> toIndex = i + (addElements.length -deleteCount);
            <span class="hljs-keyword">if</span>(formIndex <span class="hljs-keyword">in</span> apply)&#123;
              array[toIndex] = array[formIndex];
            &#125; <span class="hljs-keyword">else</span>&#123;
              <span class="hljs-keyword">delete</span> array[toIndex]
            &#125;
          &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">阻止用户传来的不正确的数组边界值（参数）</h2>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">// 处理用户传来的不争取的startindex，deletecount。</span>
      <span class="hljs-keyword">const</span> computeStartIndex = <span class="hljs-function">(<span class="hljs-params">startIndex, len</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (startIndex < <span class="hljs-number">0</span>) &#123;
          <span class="hljs-keyword">return</span> startIndex + len > <span class="hljs-number">0</span> ? startIndex + len : <span class="hljs-number">0</span>
        &#125;
        <span class="hljs-keyword">return</span> startIndex >= len ? len : startIndex
      &#125;
      <span class="hljs-comment">//删除数字处理</span>
      <span class="hljs-keyword">const</span> computeDeleteCount = <span class="hljs-function">(<span class="hljs-params">startIndex,len,deleteCount,argumentLen</span>) =></span> &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">1</span>)&#123;
          <span class="hljs-keyword">return</span> len - startIndex
        &#125;
        <span class="hljs-keyword">if</span>(deleteCount < <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
        <span class="hljs-keyword">if</span>(deleteCount > len - deleteCount) <span class="hljs-keyword">return</span> len - startIndex;
        <span class="hljs-keyword">return</span> deleteCount
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">如果数组是只读的或者是不可改变的做处理</h2>
<ul>
<li>密封对象：不可扩展的对象，可以修改属性值，不能添加删除方法和属性  configurable属性值为false</li>
<li>冻结对象：在密封对象的基础上不能修改属性值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.isSealed(array) && deleteCount !== addElements.length)&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span> (<span class="hljs-string">'this object is a sealed object'</span>)
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.isFrozen(array) && (deleteCount > <span class="hljs-number">0</span> || addElements.length > <span class="hljs-number">0</span>))&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span> (<span class="hljs-string">'this object is a Frozen object'</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>初入前端门，小白菜一枚，记录自己学习路径，希望可以激励自己，希望大家可以轻喷，有不对地方可以指出会及时改成奥！谢谢大家</strong></p>
<p>参考：
<a href="https://github.com/sanyuan0704/my_blog/blob/master/blogs/javascript/js-array/008.md" target="_blank" rel="nofollow noopener noreferrer">三元大神 blog </a> (强烈推荐)</p>
<p><a href="https://github.com/v8/v8/blob/ad82a40509c5b5b4680d4299c8f08d6c6d31af3c/src/js/array.js#L660" target="_blank" rel="nofollow noopener noreferrer"> V8数组 splice 源码</a></p>
<p><a href="https://www.w3school.com.cn/jsref/jsref_splice.asp" target="_blank" rel="nofollow noopener noreferrer"> w3 School JavaScript plice</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/splice" target="_blank" rel="nofollow noopener noreferrer"> MDN
文档 Array Splice</a></p></div>  
</div>
            