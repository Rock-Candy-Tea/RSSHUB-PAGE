
---
title: 'HTML回顾总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5902'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 03:01:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=5902'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">HTML知识回顾</h1>
<p>由于HTML的知识点相对较少，用一篇文章简单总结一下</p>
<h3 data-id="heading-1">HTML语义化</h3>
<p>按我的理解来说，就是给原来的div起名字，这是HTML5新推出的几种标签。
以前都是<code><div class="header"></code>现在直接就叫<code><header></code>,这样做得好处就是：
1.可以更方便开发者理解里面的内容的意义————增加代码可读性。
2.有助于搜索引擎的脚本对内容收集————SEO搜索引擎优化。</p>
<p>注意：不仅仅是H5新推出的header，footer算作语义化，h1,p,li等等这些有含义的标签都属于HTML语义化。</p>
<p>header页面头部    footer页面脚部    main页面主体       hgroup标题组    nav导航栏<br>
article独立内容   aside侧边栏      section文档区域    figure图像    figcaption图像标题
datalist选项列表  details，summary详情区     progress，meter进度条  time 时间   mark标记</p>
<p>刚刚学习scss，学到了使用BEM命名规则————block__element--modifier
简单来说就是，'父__子--状态'的命名方法能使代码结构更清晰，便于维护。</p>
<h3 data-id="heading-2">块级元素和内联元素</h3>
<p>这个大体来说就是span和div的区别。
<strong>块级元素</strong>：div，h1-h6，table，ul，li，p等，他们独占一行。有宽和高，也会有边框。
<strong>内联元素</strong>：span，a，img等，他们会挨着，直到占满一排才换行，宽和高根据内容而定。</p>
<p>可以通过修改css的dispaly:block或dispaly:inline来使块级元素和内联元素相互转化
也可以通过display:inline-block来使他们成为行内块元素，既可以设定宽高，又不会独占一行而把其他<em>小伙伴</em>挤下去</p>
<h3 data-id="heading-3">表布局</h3>
<p>表table由表，列组，列，行组，行，单元格自底向上构成，</p>
<pre><code class="copyable"><table border="1">//表格
  <tr>
    <th>Month</th>//表标题——列上方的头
    <th>Savings</th>
  </tr>
  <tr>             //表行
    <td>January</td>//每个单元格中的内容
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
</table>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的表格边框间会有空隙，视觉上不同与我们平时使用的表格，可以通过 border-collapse:collapse;的css代码来合并（塌陷）边框。
值得一提的是，塌陷边框的表格之间的边框颜色或形态会相互影响
具体的优先级是：
1.hidden大于一切;
2.之后宽的会覆盖窄的;
3.double大于solid......;
4.cell的大于row的大于row-group的......。</p>
<h3 data-id="heading-4">不常用的HTML标签</h3>
<pre><code class="copyable"><del>:删除线          <sup>:上标        <u>:下划线           <center>:局中
<strong>和<b>都是加粗，但<strong>具有语义化     <em>和<i>都是斜体，但<em>具有语义化
引用标签：blockquote,q,abbr,address,cite
<br>和<wbr>是换行和软换行       <pre>定义预格式化的文本     <code>源代码
<map><area>区域和热区域        <embed><object> 嵌入多媒体   <audio><video>是音乐和视频
<rudy>和<rt>文字标签与注解      <bdo>可以让文字反向     <link>和<meta>标签则分别代表了链接和辅助信息
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">input表单汇总</h3>
<p>在所有input标签外，要定义一个form标签
form标签有如下属性（常用）</p>
<pre><code class="copyable">name        规定表单名称
action      当表单提交时，向哪个地址提交
method      当表单提交时，传递数据的方式（get/post）
target      当表单提交时，在何处打开 action URL。（_blank/_self)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以在form内定义我们想要的input表单
有这些input标签内的type属性可供选择，来生成不同的表单(常用)</p>
<pre><code class="copyable">bbutton       定义可点击的按钮（通常与 JavaScript 一起使用来启动脚本）。
checkbox       定义复选框。
color      定义拾色器。
date           定义 date 控件（包括年、月、日，不包括时间）。
email      定义用于 e-mail 地址的字段。
file       定义文件选择字段和 "浏览..." 按钮，供文件上传。
image       定义图像作为提交按钮。
number     定义用于输入数字的字段。
password   定义密码字段（字段中的字符会被遮蔽）。
radio       定义单选按钮。
reset       定义重置按钮（重置所有的表单值为默认值）。
search     定义用于输入搜索字符串的文本字段。
submit       定义提交按钮。
tel          定义用于输入电话号码的字段。
text       定义一个单行的文本字段（默认宽度为 20 个字符）。
time         定义用于输入时间的控件（不带时区）。
url          定义用于输入 URL 的字段。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这些表单中，也有不同的属性可以选择（常用）</p>
<pre><code class="copyable">checked    单选和复选框的选中状态
autofocus  表单自动获得焦点
disabled   禁用
maxlength  最大字符数
name       表单名称
value      表单内容 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为面试做准备，欢迎补充和评论</p></div>  
</div>
            