
---
title: '虚拟dom和diff算法--6（手写子节点更新策略）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8846'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 00:15:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=8846'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>写在前面，笔记来源于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1iX4y1K72v%3Fp%3D28%26spm_id_from%3DpageDriver" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1iX4y1K72v?p=28&spm_id_from=pageDriver" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1iX…</a> 侵删<br>
完全是学习笔记，有问题请指正</p>
<p>我们前面说到，diff算法是按照：</p>
<pre><code class="copyable">新前新后
旧前旧后
新后旧前
新前旧后
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的顺序来进行查询命中的</p>
<pre><code class="copyable">export default function updataChildren(parentElm,oldCh,newCh)&#123;

console.log('我是updataChildren',parentElm,oldCh,newCh)

// 旧前

let oldStartIdx = 0;

// 新前

let newStartIdx = 0;

// 旧后

let oldEndIdx = oldCh.length-1;

// 新后

let newEndIdx = newCh.length-1;

\


// 真正的旧前旧后节点

let oldStartVnode = oldCh[0]

let oldEndVnode = oldCh[oldEndIdx]

// 真正的新前新后节点

let newStartVnode = newCh[0]

let newEndVnode = newCh[newEndIdx]

\


&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>updateChildren.js:</p>
<pre><code class="copyable">import patchVnode from '../patchVnode.js'

import createElement from '../createElement.js'

// 判断是否是同一个虚拟节点

function checkSameVnode(a, b) &#123;

return a.sel == b.sel && a.key == b.key

&#125;

export default function updataChildren(parentElm, oldCh, newCh) &#123;

// console.log('我是updataChildren',parentElm,oldCh,newCh)

// 旧前

let oldStartIdx = 0;

// 新前

let newStartIdx = 0;

// 旧后

let oldEndIdx = oldCh.length - 1;

// 新后

let newEndIdx = newCh.length - 1;

\


// 真正的旧前旧后节点

let oldStartVnode = oldCh[0]

let oldEndVnode = oldCh[oldEndIdx]

// 真正的新前新后节点

let newStartVnode = newCh[0]

let newEndVnode = newCh[newEndIdx]

let keyMap = null

// 开始大while

while (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;

// 这里的if是在处理被标识为undefined的虚拟节点

if (oldStartVnode == null || oldCh[oldStartIdx] == undefined) &#123;

oldStartVnode = oldCh[++oldStartIdx]

&#125; else if (oldEndVnode == null || oldCh[oldEndIdx] == undefined) &#123;

oldEndVnode = oldCh[--oldEndIdx]

&#125; else if (newStartVnode == null || newCh[newStartIdx] == undefined) &#123;

newStartVnode = newCh[++newStartIdx]

&#125; else if (newEndVnode == null || newCh[newEndIdx] == undefined) &#123;

newEndVnode = new [--newEndIdx]

&#125;

// 旧前新前

else if (checkSameVnode(oldStartVnode, newStartVnode)) &#123;

console.log('1新前旧前')

// 是同一个节点

patchVnode(oldStartVnode, newStartVnode)

// 注意，这里对比的是节点，oldStartIdx是指针，也就是下标标号

oldStartVnode = oldCh[++oldStartIdx]

newStartVnode = newCh[++newStartIdx]

// 新前旧前匹配成功之后=>指针顺位后移

// 新后旧后

&#125; else if (checkSameVnode(newEndVnode, oldEndVnode)) &#123;

console.log('2新后旧后')

patchVnode(oldEndVnode, newEndVnode)

oldEndVnode = oldCh[--oldEndIdx]

newEndVnode = newCh[--newEndIdx]

// 新后旧后匹配成功之后=>指针顺位前移

// 新后旧前

&#125; else if (checkSameVnode(newEndVnode, oldStartVnode)) &#123;

console.log('3新后旧前')

patchVnode(oldStartVnode, newEndVnode)

\


// 创建真实节点并插入,创建旧前节点

parentElm.insertBefore(oldStartVnode.elm, oldEndVnode.elm.nextSibling)

oldStartVnode = oldCh[++oldStartIdx]

newEndVnode = newCh[--newEndIdx]

// 新后旧前匹配成功是将旧前匹配到虚拟节点标识undefined，将该节点挪动到真实dom的旧后之后

\


// 如何移动节点？？只要插入一个已经在dom树上的节点，就会被移动

&#125; else if (checkSameVnode(newStartVnode, oldEndVnode)) &#123;

// 新前旧后

console.log('4新前旧后')

\


patchVnode(newStartVnode, oldEndVnode)

parentElm.insertBefore(oldEndVnode.elm, oldStartVnode.elm)

oldEndVnode = oldCh[--oldEndIdx]

newStartVnode = newCh[++newStartIdx]

\


// 新前旧后是将新前匹配到的虚拟节点标识undefined并且将该节点挪动到真实dom的新前之前

&#125; else &#123;

// 四种命中都没找到的情况，也是当前这个diff算法的最后的一个逻辑啦，也是最复杂的diff算法中最复杂的情况了！！！！

\


// 寻找key的map，制作keyMap的一个映射对象，这样就不用每次都遍历老对象了

if (!keyMap) &#123;

keyMap = &#123;&#125;

// 从oldStartIdx开始，到oldEndIdx结束，去创建keymap映射对象

for (let i = oldStartIdx; i <= oldEndIdx; i++) &#123;

const key = oldCh[i].key

if (key != undefined) &#123;

keyMap[key] = i

&#125;

&#125;

&#125;

console.log(1111,keyMap, newStartVnode)

// 寻找当前newStartIdx这项在keyMap中的映射的位置序号

const idxInOld = keyMap[newStartVnode.key]

console.log(idxInOld)

// 判断，如果idxInOld是undefined，就表示是全新的节点，在旧的里面没有，新的里面有

if (idxInOld == undefined) &#123;

parentElm.insertBefore(createElement(newStartVnode),oldStartVnode.elm)

&#125; else &#123;

// 如果不是全新的节点，就需要移动

// debugger

const elmToMove = oldCh[idxInOld]

console.log(1, elmToMove)

// if(elmToMove.elm.nodeType == 1)&#123;

patchVnode(elmToMove, newStartVnode)

// 把这个节点设置为undefined，表示我处理完了这个节点

oldCh[idxInOld] = undefined

// 移动 调用insertBefore()

parentElm.insertBefore(elmToMove.elm, oldStartVnode.elm)

// &#125;

&#125;

// 指针下移，只移动新的头

newStartVnode = newCh[++newStartIdx]

// newStartIdx++

&#125;

&#125;

// old结束之后，要看看new里面是否还有剩余节点，也就是在末尾新增

if (newStartIdx <= newEndIdx) &#123;

// 说明要增加

console.log('new还有剩余节点')

// debugger

// const before = newCh[newEndIdx + 1] == null ? null : newCh[newEndIdx + 1].elm

// console.log(before)

for (let i = newStartIdx; i <= newEndIdx; i++) &#123;

// newCh[i]此时还只是虚拟节点，还没有称为真正的dom，所以要调用createElement()将虚拟节点变成真实的dom节点

parentElm.insertBefore(createElement(newCh[i]), oldCh[oldStartIdx].elm)

// insertBefore可以自动识别null，如果是null，就会自动排到队尾去，和appendChild()是一致的

&#125;

&#125; else if (oldStartIdx <= oldEndIdx) &#123;

// new循环结束，old还有，将old中剩余节点删除

// 需要注意的是，这里的删除只能删除old中的节点，不能删除结尾的，就是说这个情况只能删除结尾被匹配到的，不能匹配结尾就匹配不到的节点，这个情况会出现死循环，这个在上面的else中进行处理

console.log('old还有剩余节点')

// 批量删除oldStartIdx和oldEndIdx之间的节点们

for (let i = oldStartIdx; i <= oldEndIdx; i++) &#123;

if (oldCh[i]) &#123;

parentElm.removeChild(oldCh[i].elm)

&#125;

&#125;

&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这节好难。也遇到了好多bug，后面会再整理一下：<br>
1.四判定的具体逻辑<br>
2.剩余项===>增加/删除 的逻辑</p></div>  
</div>
            