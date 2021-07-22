
---
title: '《JS数组对象去重》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9479'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:38:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=9479'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">const arr = [
      &#123;id: 1, parentid: 0&#125;,
      &#123;id: 2, parentid: 1&#125;,
      &#123;id: 3, parentid: 1&#125;,
      &#123;id: 3, parentid: 1&#125;,
      &#123;id: 4, parentid: 2&#125;,
      &#123;id: 5, parentid: 2&#125;,
      &#123;id: 6, parentid: 0&#125;,
      &#123;id: 6, parentid: 0&#125;,
      &#123;id: 7, parentid: 0&#125;,
  ];
  /** 数组对象去重方法一 */
  let obj1 = &#123;&#125;;
  let res1 = [];
  arr.forEach((item)=> &#123;
    if(!obj1[item.id]) &#123;
        res1.push(item);
        obj1[item.id] = true;
    &#125;
  &#125;);
  console.log(res1);

  /** 数组对象去重方法二 */
  let obj2 = &#123;&#125;;
  let res2 = [];
  res2 = arr.reduce((prev, item) => &#123;
    obj2[item.id] ? '': obj2[item.id] = true && prev.push(item);
    return prev;
  &#125;, [])
  console.log(res2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>reduce 的用法：</p>
<p>reduce()方法接收一个函数作为累加器，reduce为数组中每一个元素依次执行回调函数，不包括数组中被删除或从未被赋值的元素，回调函数接收的四个参数：初始值（上一次回调的返回值）、当前元素、当前索引、原数组。</p>
<p>语法：arr.reduce(callback, [initialValue])</p>
<p>callback中的4个参数：</p>
<ol>
<li>previousValue：上一次调用回调返回的值，或者是提供的初始值initialValue</li>
<li>currentValue：数组中当前被处理的元素</li>
<li>index：当前元素在数组中的索引</li>
<li>array：调用的数组</li>
</ol>
<p>initialValue：作为第一次调用callback的第一个参数</p></div>  
</div>
            