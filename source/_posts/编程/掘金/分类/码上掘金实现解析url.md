
---
title: '码上掘金实现解析url'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3814'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:52:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=3814'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h2 data-id="heading-0">介绍</h2>
<p>url参数的解析是工作和实际开发中常常用到的例子，因此我们是十分十分有必要动手实践掌握它，网上有许多的设计过程和例子，此处我将设计一个比较简单的例子，希望大家耐心看完整个设计过程。如果大家有任何疑问和难题都可以评论区留言，我会第一时间解决和处理的。谢谢各位观众老爷的支持。</p>
<h2 data-id="heading-1">码上掘金地址</h2>
<p><span href="https://code.juejin.cn/pen/7144650835866157071" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144650835866157071" data-src="https://code.juejin.cn/pen/7144650835866157071" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-2">核心功能讲解</h2>
<pre><code class="hljs language-ini copyable" lang="ini">function resolveLru(str) &#123;
  let <span class="hljs-attr">arr1</span> = str.split(<span class="hljs-string">"?"</span>)[<span class="hljs-number">1</span>]
  let <span class="hljs-attr">arr2</span> = arr1.split(<span class="hljs-string">"&"</span>)
  let <span class="hljs-attr">obj</span> = arr2.reduce((begin,item)=>&#123;
    //<span class="hljs-attr">name</span>=dzp
    let <span class="hljs-attr">arr3</span> = item.split(<span class="hljs-string">"="</span>)
    begin<span class="hljs-section">[arr3[0]]</span> = arr3<span class="hljs-section">[1]</span>
    return begin
  &#125;,&#123;&#125;)
  return obj
&#125;

let <span class="hljs-attr">obj</span> = resolveLru(<span class="hljs-string">"http://www.baidu.com?name=dzp&age=22"</span>)
console.log(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>设计一个函数，参数的传递是url参数字符串</li>
<li>首先我们通过split切割到?位置，后面的字符串就是关键的对象部分</li>
<li>接着，我们通过split切割&,将对象的key和value进行分割，此时所有的对象字符串都保存到了一个数组中</li>
<li>最后，我们通过数组的reduce方法进行对象的收集操作，完成。</li>
<li>返回最终的解析对象。</li>
</ol>
<h2 data-id="heading-3">总结</h2>
<p>上面就是我通过个人的模拟实现的解析url参数的过程，主要的核心就是使用splic进行字符串的切割过程，最后配合reduce的设计完成的，希望大家可以亲自动手实践进行模拟操作，这样会更加熟练使用其过程，当然使用正则表达式也是可以完成的，大家加油。</p></div>  
</div>
            