
---
title: 'JavaScript实现二分搜索树（递归）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7710996ea88c409ebbe3c58212ba5cd3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 18:55:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7710996ea88c409ebbe3c58212ba5cd3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 什么是二分搜索树</h2>
<p>二分搜索树(Binary Search Tree, BST)，属于树形数据结构的一种，二叉搜索树或者是一棵空树，或者是具有下列性质的二叉树，它的定义如下：</p>
<ol>
<li>若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；</li>
<li>若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；</li>
<li>任意节点的左、右子树也分别为二叉查找树；</li>
<li>没有键值相等的节点；</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7710996ea88c409ebbe3c58212ba5cd3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">优点</h3>
<ol>
<li>相比于其他数据结构的优势在于有着高效的插入、删除、查找操作，平均时间复杂度为O(logn)</li>
<li>可以方便地回答数据之间的关系的问题：如min，max，floor，ceil，rank，select</li>
</ol>





























<table><thead><tr><th></th><th>插入</th><th>删除</th><th>查找</th></tr></thead><tbody><tr><td>普通数组</td><td>O(n)</td><td>O(n)</td><td>O(n)</td></tr><tr><td>顺序数组</td><td>O(n)</td><td>O(n)</td><td>O(logn)</td></tr><tr><td>二分搜索树</td><td>O(logn)</td><td>O(logn)</td><td>O(logn)</td></tr></tbody></table>
<blockquote>
<p>普通数组插入O(n)：这里实现的是无重复元素的数据结构，所以普通数组插入时需要先查找是否已经存在该元素，如果存在则更新，不存在则插入。</p>
</blockquote>
<h3 data-id="heading-2">局限性</h3>
<ol>
<li>不能随机访问</li>
<li>二分搜索树为<code>不平衡树</code>，若树分布极不平衡，则会大大影响时间性能
同样的数据，可以对应不同的二分搜索树，如果节点数和树深度相同（类似链表），则所有操作退化为O(n)
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f696790dfc94ca48a3ba350c6912e44~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>可改进为平衡二叉搜索树，如红黑树等.本文不做探讨</p>
</blockquote>
</li>
</ol>
<h2 data-id="heading-3">2. JavaScript实现BST</h2>
<p>以下为构建一个无重复元素的二分搜索树（类似字典），可以通过查找 key 得到 value</p>
<p>👇以下为主要结构</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 构造节点  </span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">key, value</span>)</span> &#123;
<span class="hljs-built_in">this</span>.key = key
<span class="hljs-built_in">this</span>.value = value
<span class="hljs-built_in">this</span>.left = <span class="hljs-literal">null</span>
<span class="hljs-built_in">this</span>.right = <span class="hljs-literal">null</span>
    &#125;
&#125;
<span class="hljs-comment">// 构造二分搜索树</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BST</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">root = <span class="hljs-literal">null</span></span>)</span> &#123;
<span class="hljs-built_in">this</span>.root = root
<span class="hljs-built_in">this</span>.count = <span class="hljs-number">0</span>
&#125;
  <span class="hljs-comment">// 主要方法</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">key</span>)</span>&#123;&#125; <span class="hljs-comment">// 插入</span>
  <span class="hljs-function"><span class="hljs-title">search</span>(<span class="hljs-params">key</span>)</span>&#123;&#125; <span class="hljs-comment">// 查找 </span>
  <span class="hljs-function"><span class="hljs-title">preOrder</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 前序遍历</span>
  <span class="hljs-function"><span class="hljs-title">inOrder</span>(<span class="hljs-params"></span>)</span>&#123;&#125;  <span class="hljs-comment">// 中序遍历</span>
  <span class="hljs-function"><span class="hljs-title">postOrder</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 后序遍历</span>
  <span class="hljs-function"><span class="hljs-title">levelOrder</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 广度优先遍历（层序）</span>
  <span class="hljs-function"><span class="hljs-title">searchMin</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 查找最小</span>
  <span class="hljs-function"><span class="hljs-title">searchMax</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 查找最大</span>
<span class="hljs-function"><span class="hljs-title">deleteMin</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 删除最小</span>
  <span class="hljs-function"><span class="hljs-title">deleteMax</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// 删除最大</span>
  <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">key</span>)</span>&#123;&#125; <span class="hljs-comment">// 删除</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.1 插入</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 向以node为根的二叉搜索树中，插入节点(key, value)</span>
<span class="hljs-comment">// 返回根节点</span>

<span class="hljs-comment">// 递归实现</span>
<span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">key, value</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.root = <span class="hljs-built_in">this</span>._insert(<span class="hljs-built_in">this</span>.root, key, value)
&#125;
<span class="hljs-function"><span class="hljs-title">_insert</span>(<span class="hljs-params">node, key, value</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> node = <span class="hljs-keyword">new</span> Node(key, value)
  &#125;
  <span class="hljs-keyword">if</span> (key === node.key) &#123;
    node.value = value
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key < node.key) &#123;
    node.left = <span class="hljs-built_in">this</span>._insert(node.left, key, value)
  &#125; <span class="hljs-keyword">else</span> &#123;
    node.right = <span class="hljs-built_in">this</span>._insert(node.right, key, value)
  &#125;
  <span class="hljs-keyword">return</span> node
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2 查找</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 向以node为根的二叉搜索树中，搜索是否包含key的节点。</span>
<span class="hljs-comment">// 包含返回node，不包含则返回null</span>
<span class="hljs-function"><span class="hljs-title">search</span>(<span class="hljs-params">key</span>)</span> &#123;
  <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">this</span>.root
  <span class="hljs-keyword">while</span> (node !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (key === node.key) &#123;
      <span class="hljs-keyword">return</span> node
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key > node.key) &#123;
      node = node.right
    &#125; <span class="hljs-keyword">else</span> &#123;
      node = node.left
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.3 遍历</h3>
<p>二分搜索树遍历分为两大类，<code>深度优先遍历</code>和<code>广度优先遍历</code>。</p>
<p><code>深度优先遍历</code>分为三种，先序遍历、中序遍历、后序遍历。（以根的位置划分）
先序遍历：根左右
中序遍历：左根右
后序遍历：左右根</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 先序遍历（递归）</span>
<span class="hljs-function"><span class="hljs-title">preOrder</span>(<span class="hljs-params">node = <span class="hljs-built_in">this</span>.root, arr = []</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
    arr.push(node.key)
    <span class="hljs-built_in">this</span>.preOrder(node.left, arr)
    <span class="hljs-built_in">this</span>.preOrder(node.right, arr)
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">// 中序遍历（递归）</span>
<span class="hljs-function"><span class="hljs-title">inOrder</span>(<span class="hljs-params">node = <span class="hljs-built_in">this</span>.root, arr = []</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-built_in">this</span>.inOrder(node.left, arr)
    arr.push(node.key)
    <span class="hljs-built_in">this</span>.inOrder(node.right, arr)
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">// 后序遍历（递归）</span>
<span class="hljs-function"><span class="hljs-title">postOrder</span>(<span class="hljs-params">node = <span class="hljs-built_in">this</span>.root, arr = []</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-built_in">this</span>.postOrder(node.left, arr)
    <span class="hljs-built_in">this</span>.postOrder(node.right, arr)
    arr.push(node.key)
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">// 广度优先遍历（层级）</span>
<span class="hljs-function"><span class="hljs-title">levelOrder</span>(<span class="hljs-params"></span>)</span> &#123; 
  <span class="hljs-keyword">const</span> stack = []
  <span class="hljs-keyword">const</span> arr = []
  stack.push(<span class="hljs-built_in">this</span>.root)
  <span class="hljs-keyword">while</span> (stack.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">let</span> node = stack.shift() <span class="hljs-comment">// 先进先出</span>
    arr.push(node.key)
    node.left && stack.push(node.left)
    node.right && stack.push(node.right)
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.4 删除</h3>
<ol>
<li>
<p>查找要删除的节点
（1）如果该节点不存在，则返回null
（2）如果该节点存在，则继续</p>
</li>
<li>
<p>判断</p>
<p>（1）当节点没有子节点，那么只需要将从父节点指向它的链接指向变为null</p>
<p>（2）当节点只有左子树时，父节点指向该节点的子节点</p>
<p>（2）当节点只有右子树时，父节点指向该节点的子节点</p>
<p>（3）【重点】当节点包含左右子树时，该节点替换为左子树中最大的节点或<strong>右子树中最小的节点</strong>（1962年，Hubbard deletion）</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e1048f205ae4dbb9c53b8648133300d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">key</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.root = <span class="hljs-built_in">this</span>._deleteNode(<span class="hljs-built_in">this</span>.root, key)
&#125;
<span class="hljs-function"><span class="hljs-title">_deleteNode</span>(<span class="hljs-params">node, key</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (key > node.key) &#123;
    node.right = <span class="hljs-built_in">this</span>._deleteNode(node.right, key)
    <span class="hljs-keyword">return</span> node
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key < node.key) &#123;
    node.left = <span class="hljs-built_in">this</span>._deleteNode(node.left, key)
    <span class="hljs-keyword">return</span> node
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// key === node.key</span>
    <span class="hljs-keyword">if</span> (node.left === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">return</span> node.right
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (node.right === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">return</span> node.left
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 左右节点均不为空</span>
      <span class="hljs-keyword">let</span> rightMinNode = <span class="hljs-built_in">this</span>.searchMin(node.right)
      <span class="hljs-keyword">let</span> successor = <span class="hljs-keyword">new</span> Node(rightMinNode.key, rightMinNode.value)
      successor.left = node.left
      successor.right = <span class="hljs-built_in">this</span>.deleteMin(node.right)
      <span class="hljs-keyword">return</span> successor
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// delete(key) 需要调用searchMin()，deleteMin()（均为递归）</span>
<span class="hljs-function"><span class="hljs-title">searchMin</span>(<span class="hljs-params">node = <span class="hljs-built_in">this</span>.root</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (node.left === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> node
  &#125;
  node = node.left
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.searchMin(node)
&#125;

<span class="hljs-function"><span class="hljs-title">deleteMin</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 删除以node为根节点的最小节点</span>
  <span class="hljs-comment">// 返回删除后的根节点</span>
  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.root === <span class="hljs-literal">null</span>)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.root = <span class="hljs-built_in">this</span>._deleteMin(<span class="hljs-built_in">this</span>.root)
&#125;
<span class="hljs-function"><span class="hljs-title">_deleteMin</span>(<span class="hljs-params">node</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(node.left === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> node.right
  &#125; 
  node.left = <span class="hljs-built_in">this</span>._deleteMin(node.left)
  <span class="hljs-keyword">return</span> node
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">更多</h3>
<p>除了对数据进行增删改查，二分搜索树还可以回答数据之间的顺序性问题。（具体实现略）</p>
<ul>
<li>minimum、maximum</li>
<li>successor（后继）、predecessor（前驱）</li>
<li>floor（地板）、ceil（天花板）</li>
<li>rank（58是排名第几的元素）、select（排名第10的元素是谁）</li>
</ul>
<h2 data-id="heading-9">3. 不同设计的BST</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c605f962219c4893b69e10a2dc468420~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">4. 参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoding.imooc.com%2Flearn%2Flist%2F71.html" target="_blank" rel="nofollow noopener noreferrer" title="https://coding.imooc.com/learn/list/71.html" ref="nofollow noopener noreferrer">慕课刘宇波【算法与数据结构 】 </a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fdata-structures%2Fbinary-search-tree.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/data-structures/binary-search-tree.html" ref="nofollow noopener noreferrer">菜鸟教程-数据结构</a>：具体的实现过程图示，nice！</p></div>  
</div>
            