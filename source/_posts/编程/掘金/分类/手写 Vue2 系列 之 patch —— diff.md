
---
title: '手写 Vue2 系列 之 patch —— diff'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e33a7fe85fa84adf9fd7ec21be93d232~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 16:13:33 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e33a7fe85fa84adf9fd7ec21be93d232~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇文章 <a href="https://juejin.cn/post/6981224810386833422" target="_blank" title="https://juejin.cn/post/6981224810386833422">手写 Vue2 系列 之 初始渲染</a> 中完成了原始标签、自定义组件、插槽的的初始渲染，当然其中也涉及到 v-bind、v-model、v-on 指令的原理。完成首次渲染之后，接下来就该进行后续的更新了：</p>
<p>响应式数据发生更新 -> setter 拦截到更新操作 -> dep 通知 watcher 执行 update 方法 -> 进而执行 updateComponent 方法更新组件 -> 执行 render 生成新的 vnode -> 将 vnode 传递给 vm._update 方法 -> 调用 patch 方法 -> 执行 patchVnode 进行 DOM diff 操作 -> 完成更新</p>
<h1 data-id="heading-1">目标</h1>
<p>所以，本篇的目标就是实现 DOM diff，完成后续更新。涉及知识点只有一个：DOM diff。</p>
<h1 data-id="heading-2">实现</h1>
<p>接下来就开始实现 DOM diff，完成响应式数据的后续更新。</p>
<h2 data-id="heading-3">patch</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 负责组件的首次渲染和后续更新
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VNode&#125;</span> </span>oldVnode 老的 VNode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VNode&#125;</span> </span>vnode 新的 VNode
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (oldVnode && !vnode) &#123;
    <span class="hljs-comment">// 老节点存在，新节点不存在，则销毁组件</span>
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">if</span> (!oldVnode) &#123; <span class="hljs-comment">// oldVnode 不存在，说明是子组件首次渲染</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">if</span> (oldVnode.nodeType) &#123; <span class="hljs-comment">// 真实节点，则表示首次渲染根组件</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 后续的更新</span>
      patchVnode(oldVnode, vnode)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">patchVnode</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 对比新老节点，找出其中的不同，然后更新老节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>oldVnode 老节点的 vnode
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 新节点的 vnode
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-comment">// 如果新老节点相同，则直接结束</span>
  <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span>

  <span class="hljs-comment">// 将老 vnode 上的真实节点同步到新的 vnode 上，否则，后续更新的时候会出现 vnode.elm 为空的现象</span>
  vnode.elm = oldVnode.elm

  <span class="hljs-comment">// 走到这里说明新老节点不一样，则获取它们的孩子节点，比较孩子节点</span>
  <span class="hljs-keyword">const</span> ch = vnode.children
  <span class="hljs-keyword">const</span> oldCh = oldVnode.children

  <span class="hljs-keyword">if</span> (!vnode.text) &#123; <span class="hljs-comment">// 新节点不存在文本节点</span>
    <span class="hljs-keyword">if</span> (ch && oldCh) &#123; <span class="hljs-comment">// 说明新老节点都有孩子</span>
      <span class="hljs-comment">// diff</span>
      updateChildren(ch, oldCh)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ch) &#123; <span class="hljs-comment">// 老节点没孩子，新节点有孩子</span>
      <span class="hljs-comment">// 增加孩子节点</span>
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 新节点没孩子，老节点有孩子</span>
      <span class="hljs-comment">// 删除这些孩子节点</span>
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 新节点存在文本节点</span>
    <span class="hljs-keyword">if</span> (vnode.text.expression) &#123; <span class="hljs-comment">// 说明存在表达式</span>
      <span class="hljs-comment">// 获取表达式的新值</span>
      <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">JSON</span>.stringify(vnode.context[vnode.text.expression])
      <span class="hljs-comment">// 旧值</span>
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> oldValue = oldVnode.elm.textContent
        <span class="hljs-keyword">if</span> (value !== oldValue) &#123; <span class="hljs-comment">// 新老值不一样，则更新</span>
          oldVnode.elm.textContent = value
        &#125;
      &#125; <span class="hljs-keyword">catch</span> &#123;
        <span class="hljs-comment">// 防止更新时遇到插槽，导致报错</span>
        <span class="hljs-comment">// 目前不处理插槽数据的响应式更新</span>
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">updateChildren</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * diff，比对孩子节点，找出不同点，然后将不同点更新到老节点上
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>ch 新 vnode 的所有孩子节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>oldCh 老 vnode 的所有孩子节点
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">ch, oldCh</span>) </span>&#123;
  <span class="hljs-comment">// 四个游标</span>
  <span class="hljs-comment">// 新孩子节点的开始索引，叫 新开始</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 新结束</span>
  <span class="hljs-keyword">let</span> newEndIdx = ch.length - <span class="hljs-number">1</span>
  <span class="hljs-comment">// 老开始</span>
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 老结束</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
  <span class="hljs-comment">// 循环遍历新老节点，找出节点中不一样的地方，然后更新</span>
  <span class="hljs-keyword">while</span> (newStartIdx <= newEndIdx || oldStartIdx <= oldEndIdx) &#123; <span class="hljs-comment">// 根为 web 中的 DOM 操作特点，做了四种假设，降低时间复杂度</span>
    <span class="hljs-comment">// 新开始节点</span>
    <span class="hljs-keyword">const</span> newStartNode = ch[newStartIdx]
    <span class="hljs-comment">// 新结束节点</span>
    <span class="hljs-keyword">const</span> newEndNode = ch[newEndIdx]
    <span class="hljs-comment">// 老开始节点</span>
    <span class="hljs-keyword">const</span> oldStartNode = oldCh[oldStartIdx]
    <span class="hljs-comment">// 老结束节点</span>
    <span class="hljs-keyword">const</span> oldEndNode = oldCh[oldEndIdx]
    <span class="hljs-keyword">if</span> (sameVNode(newStartNode, oldStartNode)) &#123; <span class="hljs-comment">// 假设新开始和老开始是同一个节点</span>
      <span class="hljs-comment">// 对比这两个节点，找出不同然后更新</span>
      patchVnode(oldStartNode, newStartNode)
      <span class="hljs-comment">// 移动游标</span>
      oldStartIdx++
      newStartIdx++
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVNode(newStartNode, oldEndNode)) &#123; <span class="hljs-comment">// 假设新开始和老结束是同一个节点</span>
      patchVnode(oldEndNode, newStartNode)
      <span class="hljs-comment">// 将老结束移动到新开始的位置</span>
      oldEndNode.elm.parentNode.insertBefore(oldEndNode.elm, oldCh[newStartIdx].elm)
      <span class="hljs-comment">// 移动游标</span>
      newStartIdx++
      oldEndIdx--
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVNode(newEndNode, oldStartNode)) &#123; <span class="hljs-comment">// 假设新结束和老开始是同一个节点</span>
      patchVnode(oldStartNode, newEndNode)
      <span class="hljs-comment">// 将老开始移动到新结束的位置</span>
      oldStartNode.elm.parentNode.insertBefore(oldStartNode.elm, oldCh[newEndIdx].elm.nextSibling)
      <span class="hljs-comment">// 移动游标</span>
      newEndIdx--
      oldStartIdx++
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVNode(newEndNode, oldEndNode)) &#123; <span class="hljs-comment">// 假设新结束和老结束是同一个节点</span>
      patchVnode(oldEndNode, newEndNode)
      <span class="hljs-comment">// 移动游标</span>
      newEndIdx--
      oldEndIdx--
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 上面几种假设都没命中，则老老实的遍历，找到那个相同元素</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 跳出循环，说明有一个节点首先遍历结束了</span>
  <span class="hljs-keyword">if</span> (newStartIdx < newEndIdx) &#123; <span class="hljs-comment">// 说明老节点先遍历结束，则将剩余的新节点添加到 DOM 中</span>

  &#125;
  <span class="hljs-keyword">if</span> (oldStartIdx < oldEndIdx) &#123; <span class="hljs-comment">// 说明新节点先遍历结束，则将剩余的这些老节点从 DOM 中删掉</span>

  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">sameVNode</h2>
<blockquote>
<p>/src/compiler/patch.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 判断两个节点是否相同
 * 这里的判读比较简单，只做了 key 和 标签的比较
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVNode</span>(<span class="hljs-params">n1, n2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n1.key == n2.key && n1.tag === n2.tag
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">结果</h1>
<p>好了，到这里，虚拟 DOM 的 diff 过程就完成了，如果你能看到如下效果图，则说明一切正常。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e33a7fe85fa84adf9fd7ec21be93d232~tplv-k3u1fbpfcp-watermark.image" alt="Jun-18-2021 09-11-18.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，页面已经完全做到响应式数据的初始渲染和后续更新。其中关于 Computed 计算属性的内容仍然没有正确的显示出来，这很正常，因为还没实现这个功能，所以接下来就会去实现 conputed 计算属性，也就是下一篇内容 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">手写 Vue2 系列 之 computed</a>。</p>
<h1 data-id="heading-8">关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank" title="https://juejin.cn/user/1028798616461326">掘金账号</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F359669053" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/359669053" ref="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-9">链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/column/6960553066101735461" target="_blank" title="https://juejin.cn/column/6960553066101735461">精通 Vue 技术栈的源码原理</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F359669053%2Fchannel%2Fdetail%3Fcid%3D178493" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/359669053/channel/detail?cid=178493" ref="nofollow noopener noreferrer">配套视频</a></p>
</li>
<li>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank" title="https://juejin.cn/pin/6958238190398341134">学习交流群</a></p>
</li>
</ul></div>  
</div>
            