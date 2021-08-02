
---
title: '前端自行模拟Mock数据提高开发效率'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=484'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 18:36:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=484'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言</strong>：前后端交互时后端，在没有得到后端数据时，需要自行模拟数据，来展示到页面，这样提高我们的开发效率，同时也向后端请求我们想要的数据格式，最后得到后端数据仅需改变接口即可，这时候用到我们强大的数据模拟
<strong>Mock数据：模拟数据</strong></p>
<h2 data-id="heading-0">一、Mock数据：模拟数据</h2>
<p><strong>mockjs官网</strong>：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmockjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://mockjs.com/" ref="nofollow noopener noreferrer">mockjs.com/</a></p>
<p><strong>mockjs官方文档</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnuysoft%2FMock%2Fwiki%2FGetting-Started" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nuysoft/Mock/wiki/Getting-Started" ref="nofollow noopener noreferrer">github.com/nuysoft/Moc…</a></p>
<p><strong>具体使用方法</strong></p>
<p><strong>第一步 安装mockjs</strong></p>
<blockquote>
<p>npm install mockjs</p>
</blockquote>
<p><strong>第二步 创建一个mock目录生成mock数据</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">例如：course.js
<span class="hljs-keyword">import</span> Mock <span class="hljs-keyword">from</span> <span class="hljs-string">"mockjs"</span>;

<span class="hljs-comment">//mock课程数据</span>
<span class="hljs-keyword">var</span> result=Mock.mock(&#123;
  <span class="hljs-attr">code</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">msg</span>: <span class="hljs-string">"操作成功"</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">current_page</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">last_page</span>: <span class="hljs-number">18</span>,
    <span class="hljs-attr">total</span>: <span class="hljs-number">178</span>,
    <span class="hljs-string">"list|10"</span>: [
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-string">"@id"</span>,  <span class="hljs-comment">//模拟id</span>
        <span class="hljs-string">"price|100-200.1-2"</span>: <span class="hljs-number">100</span>, <span class="hljs-comment">//模拟小数，在计算机中也称浮点数</span>
        <span class="hljs-string">"has_buy|1"</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>], <span class="hljs-comment">//模拟状态值,0,1,2,</span>
        <span class="hljs-attr">title</span>: <span class="hljs-string">"@ctitle"</span>,  <span class="hljs-comment">//模拟中文标题</span>
        <span class="hljs-attr">address</span>: <span class="hljs-string">"@county(true)"</span>,  <span class="hljs-comment">//模拟省市县</span>
        <span class="hljs-string">"teachers_list|1"</span>: [
          &#123;
            <span class="hljs-attr">course_basis_id</span>: <span class="hljs-string">"@id"</span>,
            <span class="hljs-attr">id</span>: <span class="hljs-string">"@id"</span>,
            <span class="hljs-attr">teacher_avatar</span>: <span class="hljs-string">"@image('150x120', '#ff0000', '1909A')"</span>,  <span class="hljs-comment">//模拟图片</span>
            <span class="hljs-attr">teacher_name</span>: <span class="hljs-string">"@cname"</span>  <span class="hljs-comment">//模拟中文姓名</span>
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;);


<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> result;

<span class="hljs-comment">//创建mock的入口文件，并配置请求的接口地址，提交方式，返回的假数据</span>
<span class="hljs-keyword">import</span> Mock <span class="hljs-keyword">from</span> <span class="hljs-string">'mockjs'</span>
<span class="hljs-comment">//导入的模拟数据</span>
<span class="hljs-keyword">import</span> courseData <span class="hljs-keyword">from</span> <span class="hljs-string">"./course"</span>;

<span class="hljs-comment">/**
 * Mock.mock( rurl, rtype, template )
 * rurl:请求的接口地址
 * rtype:提交方式
 * template:返回数据
 */</span>

Mock.mock(<span class="hljs-string">"http://www.1909A.com/coureslist"</span>, <span class="hljs-string">"get"</span>, courseData);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>​ 第三步：将模拟的数据注入到main.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//注入mock</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./mock'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第四步：在要请求的组件中请求数据</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> axios.get(<span class="hljs-string">'http://www.1909A.com/coureslist'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
        <span class="hljs-built_in">console</span>.log(res)
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、easy-mock</h2>
<p>easy-mock：基于mockjs生成在线假数据,是一款可以在线上编辑的数据的工具
但是请求的原因不稳定访问，不建议大家去使用</p>
<p><strong>总结：这样模拟数据插件，更多的是提高了我们前端开发的效率，我们前端即掌握到产品的原型到ui的设计再到后端的接口调节，忽然发现我们前端一人独大了，只要我们充分了解到业务需求我们就可以自行模拟数据，来提高我们的效率，为开发节省时间，给老板省成本，我们获奖金，为用户加体验，认可我们好团队，加油！！！</strong></p></div>  
</div>
            