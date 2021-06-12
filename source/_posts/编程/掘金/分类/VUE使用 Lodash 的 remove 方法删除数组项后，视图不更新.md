
---
title: 'VUE使用 Lodash 的 remove 方法删除数组项后，视图不更新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5964'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:47:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=5964'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>想从数组中按照某种筛选条件移除数组的一个元素时，很容易想到使用splice或者filter来操作：</p>
<pre><code class="copyable">/* 从数组arr中移除值为val的元素 */
let index = arr.indexOf(val)
index !== -1 && arr.splice(index, 1)
 
/* 从数组arr中移除满足predicate条件的元素 */
arr = arr.filter(predicate)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要删除数组中某项数据时，如果用 <code>splice</code>，需要知道当前被删除项的下标 <code>index</code>，先用唯一标记节点 <code>id</code> 找到对应的 <code>index</code>，再进行移除操作。过程略微繁琐，所以我想到了用 <code>Lodash</code> 的 <code>remove</code></p>
<pre><code class="copyable">/* 从数组arr中移除满足predicate条件的元素 */
_.remove(arr, predicate)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是好景不长，在控制台中看到数组已经被成功移除了，但页面上依然显示了那个被我删掉的元素，真是个打不死的小强！而且我确定一定以及肯定该数组进行了双向绑定。带着疑惑上网一搜，果不其然， <code>Lodash</code> 的 <code>remove</code>有坑！！！ <a href="https://juejin.cn/post/6844903711571968007" target="_blank">点击查看原理解析</a></p>
<p>原因就是：vue通过改造观察数组的原型方法使它操作对应方法时会触发更新响应，而<code>Lodash</code> 的 <code>remove</code>方法使用 <code>Array</code> 原型中的 <code>splice</code> 方法对数组进行操作，因此不会触发响应更新。</p>
<p>最后我只能又乖乖的用 <code>splice</code> 来实行数组的移除了...</p></div>  
</div>
            