
---
title: '浅谈Vue的diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee61ee7077a84dacb3bc4085153f7e4e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 01:54:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee61ee7077a84dacb3bc4085153f7e4e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>diff算法，可以说是Vue的一个比较核心的内容，之前只会用Vue来进行一些开发，具体的核心的内容其实涉猎不多，最近正好看了下这方面的内容，简单聊下Vue2.0的diff算法的实现吧，具体从几个实现的函数来进行分析</p>
<h2 data-id="heading-1">虚拟Dom(virtual dom)</h2>
<p>virtual DOM是将真实的DOM的数据抽取出来，以对象的形式模拟树形结构
比如以下是我们的真实DOM</p>
<pre><code class="copyable"><div>
   <p>1234</p>
   <div>
       <span>1111</span>
   </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据真实DOM生成的虚拟DOM如下</p>
<pre><code class="copyable"> var Vnode = &#123;
     tag: 'div',
     children: [
         &#123;
             tag: 'p',
             text: '1234'
         &#125;,
         &#123;
             tag: 'div',
             children:[
                 &#123;
                     tag: 'span',
                     text: '1111'
                 &#125;
             ]
         &#125;
     ]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">原理</h2>
<p>diff的原理就是当前的真实的dom生成一颗virtual DOM也就是虚拟DOM，当虚拟DOM的某个节点的数据发生改变会生成一个新的Vnode, 然后这个Vnode和旧的oldVnode对比，发现有不同，直接修改在真实DOM上</p>
<h2 data-id="heading-3">实现过程</h2>
<p>diff算法的实现过程核心的就是patch，其中的patchVnode, sameVnode以及updateChildren方法值得我们去关注一下，下面依次说明</p>
<h3 data-id="heading-4">patch方法</h3>
<p>patch的核心逻辑是比较两个Vnode节点，然后将差异更新到视图上， 比对的方式是同级比较， 而不是每个层级的循环遍历，如果比对之后得到差异，就将这些差异更新到视图上，比对方式示例图如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee61ee7077a84dacb3bc4085153f7e4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">sameVnode函数</h3>
<p>sameVnode的作用是判断两个节点是否相同，判断相同的根据是key值，tag(标签)，isCommit(注释),是否input的type一致等等，这种方法有点瑕疵，面对v-for下的key值使用index的情况，可能也会判断是可复用节点。
建议别使用index来作为key值。</p>
<h3 data-id="heading-6">patchVnode函数</h3>
<pre><code class="copyable">//传入几个参数， oldVnode代表旧节点， vnode代表新节点， readOnly代表是否是只读节点
function patchVnode (
    oldVnode,
    vnode,
    insertedVnodeQueue,
    ownerArray,
    index,
    removeOnly
  ) &#123;
    if (oldVnode === vnode) &#123;         //当旧节点和新节点一致时，无需比较，返回
      return
    &#125;

    if (isDef(vnode.elm) && isDef(ownerArray)) &#123;   
      // clone reused vnode
      vnode = ownerArray[index] = cloneVNode(vnode)
    &#125;

    const elm = vnode.elm = oldVnode.elm

    if (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
      if (isDef(vnode.asyncFactory.resolved)) &#123;
        hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
      &#125; else &#123;
        vnode.isAsyncPlaceholder = true
      &#125;
      return
    &#125;

    //静态树的重用元素

//如果vnode是克隆的，我们才会这样做

//如果新节点没有被克隆，则表示呈现函数已经被克隆

//通过hot-reload-api重置，我们需要做一个适当的重新渲染。
    if (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
    ) &#123;
      vnode.componentInstance = oldVnode.componentInstance
      return
    &#125;

    let i
    const data = vnode.data
    if (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) &#123;
      i(oldVnode, vnode)
    &#125;

    const oldCh = oldVnode.children
    const ch = vnode.children
    if (isDef(data) && isPatchable(vnode)) &#123;
      for (i = 0; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
      if (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
    &#125;
    if (isUndef(vnode.text)) &#123;
      if (isDef(oldCh) && isDef(ch)) &#123;
        if (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
      &#125; else if (isDef(ch)) &#123;
        if (process.env.NODE_ENV !== 'production') &#123;
          checkDuplicateKeys(ch)
        &#125;
        if (isDef(oldVnode.text)) nodeOps.setTextContent(elm, '')
        addVnodes(elm, null, ch, 0, ch.length - 1, insertedVnodeQueue)
      &#125; else if (isDef(oldCh)) &#123;
        removeVnodes(oldCh, 0, oldCh.length - 1)
      &#125; else if (isDef(oldVnode.text)) &#123;
        nodeOps.setTextContent(elm, '')
      &#125;
    &#125; else if (oldVnode.text !== vnode.text) &#123;
      nodeOps.setTextContent(elm, vnode.text)
    &#125;
    if (isDef(data)) &#123;
      if (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的实现逻辑是：</p>
<ol>
<li>新旧节点一样的时候，不需要做改变，直接返回</li>
<li>如果新旧都是静态节点，并且具有相同的key，当vnode是克隆节点或是v-once指令控制的节点时，只需要把oldVnode.elm和oldVnode.child都复制到vnode上</li>
<li>判断vnode是否是注释节点或者文本节点，从而做出以下处理
<ol>
<li>当vnode是文本节点或者注释节点的时候，当vnode.text!== oldVnode.text的时候，只需要更新vnode的文本内容；</li>
<li>oldVnode和vndoe都有子节点， 如果子节点不相同，就调用updateChildren方法，具体咋实现，下文有</li>
<li>如果只有vnode有子节点，判断环境，如果不是生产环境，调用checkDuplicateKeys方法，判断key值是否重复。之后在oldVnode上添加当前的ch</li>
<li>如果只有oldVnode上有子节点，那就调用方法删除当前的节点</li>
</ol>
</li>
</ol>
<h3 data-id="heading-7">updateChildren函数</h3>
<p>updateChildren，顾名思义，就是更新子节点的方法，从以上的patchVnode的方法，可以看出，当新旧节点都有子节点的时候，会执行这个方法。下面我们来了解下它的实现逻辑，也会有一些大家可能有看到过类似的示例图，先看下代码</p>
<pre><code class="copyable">function updateChildren (parentElm, oldCh, newCh, insertedVnodeQueue, removeOnly) &#123;
    let oldStartIdx = 0
    let newStartIdx = 0
    let oldEndIdx = oldCh.length - 1
    let oldStartVnode = oldCh[0]
    let oldEndVnode = oldCh[oldEndIdx]
    let newEndIdx = newCh.length - 1
    let newStartVnode = newCh[0]
    let newEndVnode = newCh[newEndIdx]
    let oldKeyToIdx, idxInOld, vnodeToMove, refElm

    // removeOnly is a special flag used only by <transition-group>
    // to ensure removed elements stay in correct relative positions
    // during leaving transitions
    const canMove = !removeOnly

    if (process.env.NODE_ENV !== 'production') &#123;
      checkDuplicateKeys(newCh)
    &#125;

    while (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      if (isUndef(oldStartVnode)) &#123;
        oldStartVnode = oldCh[++oldStartIdx] // Vnode has been moved left
      &#125; else if (isUndef(oldEndVnode)) &#123;
        oldEndVnode = oldCh[--oldEndIdx]
      &#125; else if (sameVnode(oldStartVnode, newStartVnode)) &#123;
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
        oldStartVnode = oldCh[++oldStartIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; else if (sameVnode(oldEndVnode, newEndVnode)) &#123;
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
        oldEndVnode = oldCh[--oldEndIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; else if (sameVnode(oldStartVnode, newEndVnode)) &#123; // Vnode moved right
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
        canMove && nodeOps.insertBefore(parentElm, oldStartVnode.elm, nodeOps.nextSibling(oldEndVnode.elm))
        oldStartVnode = oldCh[++oldStartIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; else if (sameVnode(oldEndVnode, newStartVnode)) &#123; // Vnode moved left
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
        canMove && nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
        oldEndVnode = oldCh[--oldEndIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; else &#123;
        if (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
        idxInOld = isDef(newStartVnode.key)
          ? oldKeyToIdx[newStartVnode.key]
          : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
        if (isUndef(idxInOld)) &#123; // New element
          createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, false, newCh, newStartIdx)
        &#125; else &#123;
          vnodeToMove = oldCh[idxInOld]
          if (sameVnode(vnodeToMove, newStartVnode)) &#123;
            patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
            oldCh[idxInOld] = undefined
            canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
          &#125; else &#123;
            // same key but different element. treat as new element
            createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, false, newCh, newStartIdx)
          &#125;
        &#125;
        newStartVnode = newCh[++newStartIdx]
      &#125;
    &#125;
    if (oldStartIdx > oldEndIdx) &#123;
      refElm = isUndef(newCh[newEndIdx + 1]) ? null : newCh[newEndIdx + 1].elm
      addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
    &#125; else if (newStartIdx > newEndIdx) &#123;
      removeVnodes(oldCh, oldStartIdx, oldEndIdx)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我们先定义几个参数，oldStartIdx(旧节点首索引)，oldEndIdx(旧节点尾索引)，oldStartVnode(旧节点首元素)， oldEndVnode(旧节点尾元素)；同理，newStartIdx等四项即为新节点首索引等。</p>
<p>看下while循环里面的操作，也是核心内容
在判断是同一节点之后，节点也需要继续进行patchVnode方法</p>
<ol>
<li>
<p>如果旧首元素和新首元素是相同节点，旧首索引和新首索引同时右移</p>
</li>
<li>
<p>如果旧尾元素和新尾元素是相同节点，旧尾索引和新尾索引同时左移</p>
</li>
<li>
<p>如果旧首元素点跟新尾元素是同一节点，根据方法上传过来的readonly判断，如果是false, 那就把旧首元素移到旧节点的尾索引的后一位，同时旧首索引右移，新尾索引左移</p>
</li>
<li>
<p>如果旧尾元素点跟新首元素是同一节点，根据方法上传过来的readonly判断，如果是false, 那就把旧尾元素移到旧节点的首索引前一位，同时旧尾索引左移，新首索引右移</p>
</li>
<li>
<p>如果以上都不符合
判断是否oldCh中有和newStartVnode的具有相同的key的Vnode，如果没有找到，说明是新的节点，创建一个新的节点，插入即可</p>
<p>如果找到了和newStartVnode具有相同的key的Vnode，命名为vnodeToMove，然后vnodeToMove和newStartVnode对比，如果相同，那就两者再去patchVnode, 如果removeOnly是false，则将找到的和newStartVnode具有相同的key的Vnode，叫vnodeToMove.elm, 移动到oldStartVnode.elm之前</p>
<p>如果key值相同，但是节点不相同，则创建一个新的节点</p>
</li>
</ol>
<p>在经过了While循环之后，如果发现新节点数组或者旧节点数组里面还有剩余的节点，根据具体情况来进行删除或者新增的操作</p>
<p>当oldStartIdx > oldEndIdx的时候，表明，oldCh先遍历完成，那就说明还有新的节点多余，新增新的节点</p>
<p>当newStartIdx > newEndIdx的时候，说明新节点最先遍历完，旧节点还有剩余，于是删除剩余的节点</p>
<p>下面来看下示例图</p>
<ol>
<li>原始节点（以oldVnode为旧节点， Vnode为新节点， diff为最后经过diff算法之后生成的节点数组）</li>
</ol>
<p>![image.png](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fp3-juejin.byteimg.com%2Ftos-cn-i-k3u1fbpfcp%2F9f6b03212bff45a1a2d6db5b819f6983~tplv-k3u1fbpfcp-watermark.imag" target="_blank" rel="nofollow noopener noreferrer" title="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f6b03212bff45a1a2d6db5b819f6983~tplv-k3u1fbpfcp-watermark.imag" ref="nofollow noopener noreferrer">p3-juejin.byteimg.com/tos-cn-i-k3…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bc6455868a84d4494c8113a1ee07b0d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>循环第一次， 这里我们发现旧尾元素跟新首元素一致，于是，旧尾元素D移动到旧首索引的前面，也就是在A的前面，同时，旧尾索引左移，新首索引右移，示例图如下</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4e7d6433c2140308494b0eff1e55412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3. 循环第二次，新首元素和旧首元素一致，这时候两元素位置不动，新旧首索引同时往右移动</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fa1e0396cd4eaba89724f20bfc4a6a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>循环第三次，发现旧元素里发现没有与当前元素相同的节点，于是新增，将F放在旧首元素之前，同理，第四次循环一致，两次循环之后生成的新的示例图</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365b631dceb041e7b3767ff360c476a8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>循环第五次，如同第二次循环</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/124dc29551e74a76a97d087b198d3098~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>循环第六次，newStartIdx再次右移</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9fb2bc12bd54ab7bc4947f702f03c64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
7. 经过上次移动，newStartIdx > newEndIdx, 已经退出while循环，证明那就是newCh先遍历完成， oldCh还有多余的节点，多余的直接删除，于是最后的出来的节点</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8b2a0e377f9432c88782f565ffb273e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是几个diff算法相关的函数，以及diff算法的实现过程</p>
<h2 data-id="heading-8">结语</h2>
<p>diff算法是虚拟DOM的核心一部分，同层比较，通过新老节点的对比，将改动的地方更新到真实DOM上。</p>
<p>具体实现的方法是patch， patchVnode以及updateChildren</p>
<p>patch的核心是，如果新节点有，旧节点没有，新增； 旧节点有，新节点没有， 删除；如果都存在，判断是否是相同，相同则调用patchVnode进行下一步比较</p>
<p>patchVnode核心是：如果新旧节点不是注释或者文本节点，新节点有子节点，而旧节点没有子节点，则新增子节点；新节点没有子节点，而旧节点有子节点，则删除旧节点下的子节点；如果二者都有子节点，则调用updateChildren方法</p>
<p>updateChildren的核心则是，新旧节点对比，进行新增，删除或者更新。</p>
<p>这里只是初步的解释了Vue2.0版本的diff算法，其中的更加深层的原理以及Vue3.0的diff算法有没有什么改变还有待学习。</p></div>  
</div>
            