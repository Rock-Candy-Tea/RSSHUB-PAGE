
---
title: '【记录】js数组'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8850'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 00:38:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=8850'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">合并数组array.push.apply()</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2Forphaned%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fpush" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/orphaned/Web/JavaScript/Reference/Global_Objects/Array/push" ref="nofollow noopener noreferrer">obj.func.apply(obj,argv)</a> 。</p>
<p>apply方法的第一个参数是函数运行时所在的作用域，第二个参数是传递给函数的参数，可以是一个数组，同时也可以是arguments对象</p>
<pre><code class="copyable">var arr1=[1,2];
var arr2=[3,4,5];
arr2.push.apply(arr2,arr1);//[1,2,3,4,5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用arr2.push这个函数实例的apply方法，同时把arr1当作参数传入，这样arr2.push这个方法就会遍历arr1数组的所有元素，将arr1的元素存入arr2数组，使arr2数组发生改变。</p>
<p><strong>eg1:</strong></p>
<p>a=[];a.push([1,2,3])，那么你得到的是[[1 2 3]]</p>
<p>[].push.apply(a,[1,2,3])，那么你得到的是[1 2 3]</p>
<p><strong>eg2:</strong> 将两个数组合并到一个新数组</p>
<pre><code class="copyable">const arr1 = [
  &#123;
    "deleted_at": null
  &#125;,
  &#123;
    "created_at": "2021-07-22T05:54:17.000Z",
  &#125;
];
const arr2 = [
  &#123;
    "url": "https://music.163.com/#/artist?id=2116",
  &#125;,
  &#123;
    "type": 200,
  &#125;
];

let arry = [];

//方法1:arry.push(...arr1, ...arr2);

//方法2：
arry.push.apply(arry,arr1)
arry.push.apply(arry,arr2)

console.log(arry)

// 打印的值：
[
  &#123; deleted_at: null &#125;,
  &#123; created_at: '2021-07-22T05:54:17.000Z' &#125;,
  &#123; url: 'https://music.163.com/#/artist?id=2116' &#125;,
  &#123; type: 200 &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            