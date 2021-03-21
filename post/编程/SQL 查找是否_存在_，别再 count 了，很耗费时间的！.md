
---
title: SQL 查找是否_存在_，别再 count 了，很耗费时间的！
categories: 
    - 编程
    - 掘金 - 收藏集
author: 掘金 - 收藏集
comments: false
date: Fri, 26 Feb 2021 00:08:20 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><ul>
<li>目前多数人的写法</li>
<li>优化方案</li>
<li>总结</li>
</ul>
<p>根据某一条件从数据库表中查询 『有』与『没有』，只有两种状态，那为什么在写SQL的时候，还要SELECT count(*) 呢？</p>
<p>无论是刚入道的程序员新星，还是精湛沙场多年的程序员老白，都是一如既往的count
目前多数人的写法
多次REVIEW代码时，发现如现现象：
业务代码中，需要根据一个或多个条件，查询是否存在记录，不关心有多少条记录。普遍的SQL及代码写法如下</p>
<h4 data-id="heading-0">SQL写法:</h4>
<pre><code class="copyable">SELECT count(*) FROM table WHERE a = 1 AND b = 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">Java写法:</h4>
<pre><code class="copyable">int nums = xxDao.countXxxxByXxx(params);
if ( nums > 0 ) {
  //当存在时，执行这里的代码
} else {
  //当不存在时，执行这里的代码
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉很OK，没有什么问题
优化方案
推荐写法如下：</p>
<h4 data-id="heading-2">SQL写法:</h4>
<pre><code class="copyable">SELECT 1 FROM table WHERE a = 1 AND b = 2 LIMIT 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">Java写法:</h4>
<pre><code class="copyable">Integer exist = xxDao.existXxxxByXxx(params);
if ( exist != NULL ) {
  //当存在时，执行这里的代码
} else {
  //当不存在时，执行这里的代码
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SQL不再使用count，而是改用LIMIT 1，让数据库查询时遇到一条就返回，不要再继续查找还有多少条了
业务代码中直接判断是否非空即可</p>
<h4 data-id="heading-4">总结</h4>
<p>根据查询条件查出来的条数越多，性能提升的越明显，在某些情况下，还可以减少联合索引的创建。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            