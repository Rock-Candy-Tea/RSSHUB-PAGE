
---
title: '面试官_ 翻译翻译什么 TM 叫 react diff'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=165'
author: 掘金
comments: false
date: Sun, 02 May 2021 21:26:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=165'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>回答要有逻辑, 从 react 渲染设计思想, 面临的问题, diff 算法原理, 有哪些问题, 可能解决的办法 角度出发</p>
<p>浏览器性能瓶颈是 DOM, react 是采用虚拟 DOM 思想, 当需要重新渲染, 将新旧 DOM 数快照对比,找出变化的部分,尽可能较少 DOM 的变更, 而将一个树形结构转化成另一种树形结构, 通常算法复杂度是 On3 次方, 于是结合前端使用场景特征进行了算法优化</p>
<ol>
<li>首选前端很少有节点跨层级移动</li>
<li>拥有相同类型的组件会生成相似的结构</li>
<li>对于同一层级节点, 他们可以通过唯一 ID 区分</li>
</ol>
<p>首先会一层层比较, (通过 updateDepth 控制), 假如同层发现不同,销毁 结点及其下面所有结点, 哪怕其子节点是可复用的</p>
<p>然后同层级比较过程中, diff 提供了 插入/删除/移动三个操作, 而判断依据的唯一 ID 就是 标签类型, 或者组件的 key 属性. 通过唯一 key 可以判断新老集合中是否存在相同的节点, 如果存在相同节点, 会将新旧快照的索引进行对比, 新快照节点索引 > 旧快照节点索引，才需要进行移动操作。 脑补打扑克朝着一个方向码牌, 比如 J,K,Q, A -> J,Q,K,A 只需要把 K 移动到 Q 后面就成了一条龙了(我猜测他们的灵感就是来源扑克 hh)</p>
<p>但这个朝着一个方向的算法存在一个问题, 假如是把最后一个节点移动到第一个节点, 但会是把前面一些节点移动到 最后一个节点后面. 所以要避免这个场景</p>
<p>我猜测未来如果需要解决这个场景, 会增加双向 diff</p></div>  
</div>
            