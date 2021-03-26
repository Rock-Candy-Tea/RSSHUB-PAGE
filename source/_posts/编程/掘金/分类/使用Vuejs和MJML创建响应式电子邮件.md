
---
title: '使用Vue.js和MJML创建响应式电子邮件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46c856e2d620474f858a5d9c2b105133~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 07:47:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46c856e2d620474f858a5d9c2b105133~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>博客原文：</strong><a href="https://blog.zhangbing.site/2021/03/19/creating-responsive-emails-using-mjml/" target="_blank" rel="nofollow noopener noreferrer">blog.zhangbing.site/2021/03/19/…</a></p>
</blockquote>
<p>MJML是一种现代的电子邮件工具，使开发人员可以在所有设备和邮件客户端上创建美观、响应迅速的出色电子邮件。这种标记语言是为了减少编写响应式电子邮件的痛苦而设计的。</p>
<p>它的语义语法使其易于使用。它还具有功能丰富的标准组件，可缩短开发时间。在本教程中，我们将使用MJML构建漂亮的响应式邮件，并在多个邮件客户端上进行测试。</p>
<h2 data-id="heading-0">开始MJML</h2>
<p>你可以使用npm安装MJML，以将其与Node.js或CLI结合使用：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> npm install -g mjml</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">构建我们的电子邮件</h2>
<p>首先，请创建一个名为 <code>email.mjml</code> 的文件，尽管你也可以选择其他任何名称。创建文件后，我们的响应式电子邮件将分为以下几部分：</p>
<ul>
<li>公司header</li>
<li>图片header</li>
<li>Email介绍</li>
<li>栏目部分</li>
<li>图标</li>
<li>社交图标</li>
</ul>
<h3 data-id="heading-2">栏目</h3>
<p>这些部分是我们响应式电子邮件的框架。如上所示，我们的电子邮件将分为六个部分，在我们的 <code>email.mjml</code> 文件中：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">mjml</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-body</span>></span>
    <span class="hljs-comment"><!-- 公司 Header --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#f0f0f0"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- 图片 Header --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#f0f0f0"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Email 介绍 --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fafafa"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- 栏目部分 --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"white"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- 图标 --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fbfbfb"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- 社交图标 --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#f0f0f0"</span>></span><span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mjml</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面可以看到，我们正在使用两个MJML组件：<code>mj-body</code> 和 <code>mj-section</code>。<code>mj-body</code> 定义了我们电子邮件的起点，而 <code>mj-section</code> 定义了一个包含其他组件的节。</p>
<p>对于定义的每个部分，还定义了具有各自十六进制值的 <code>background-color</code> 属性。</p>
<h3 data-id="heading-3">公司 Header</h3>
<p>我们电子邮件的此部分仅在中心横幅位置包含我们的公司/品牌名称：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 公司 Header --></span>
<span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#f0f0f0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span>  <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
        <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
        <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span>
        <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>
    Central Park Cruise
    <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mj-column</code> 组件是用来定义一个列。<code>mj-text</code> 组件用于我们的文本内容，并采取字体样式、字体大小、颜色等样式属性。</p>
<h3 data-id="heading-4">图片 Header</h3>
<p>在本部分中，我们将有一个背景图片和一段文字，它们应代表我们的公司口号。我们还会有一个号召性用语按钮，指向一个包含更多详细信息的页面。</p>
<p>要添加图片标题，你必须将该部分的背景颜色替换为 <code>background-url</code>。与第一个标题相似，你将不得不在垂直和水平方向上居中放置文本，padding保持不变。</p>
<p>按钮的 <code>href</code> 设置按钮的位置。为了让背景在列中呈现全宽，将列宽设置为600px，<code>width=“600px"</code>。</p>
<p>我们的电子邮件的这一部分将只包含我们的公司/品牌名称的中心横幅位置。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Image Header --></span>
<span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-url</span>=<span class="hljs-string">"https://ca-times.brightspotcdn.com/dims4/default/2af165c/2147483647/strip/true/crop/2048x1363+0+0/resize/1440x958!/quality/90/?url=https%3A%2F%2Fwww.trbimg.com%2Fimg-4f561d37%2Fturbine%2Forl-disneyfantasy720120306062055"</span>
            <span class="hljs-attr">background-size</span>=<span class="hljs-string">"cover"</span>
            <span class="hljs-attr">background-repeat</span>=<span class="hljs-string">"no-repeat"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span>  <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span>
             <span class="hljs-attr">color</span>=<span class="hljs-string">"#fff"</span>
             <span class="hljs-attr">font-size</span>=<span class="hljs-string">"40px"</span>
             <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>></span>Christmas Discount<span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-button</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#F63A4D"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>
      See Promotions
    <span class="hljs-tag"></<span class="hljs-name">mj-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要使用图像header，我们将向 <code>jms -section</code> 组件添加 <code>background-url</code> 属性，然后使用 <code>background-size</code> 和 <code>background-repeat</code> 属性设置图像的样式。</p>
<p>对于我们的口号文本块，我们使用 <code>align</code> 属性将文本在水平和垂直方向上居中对齐。你还可以根据需要设置文本颜色，字体大小，字体系列等。</p>
<p>号召性用语按钮是使用 <code>mj-button</code> 组件实现的。<code>background-color</code> 属性允许我们指定按钮的背景色，然后使用 <code>href</code> 指定链接或页面的位置。</p>
<h3 data-id="heading-5">Email件介绍</h3>
<p>简介文字将由标题，主体文字和号召性用语组成。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Intro text --></span>
<span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fafafa"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"400px"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
             <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
             <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>
             <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>Ultimate Christmas Experience<span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"#525252"</span>></span>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rutrum enim eget magna efficitur, eu semper augue semper. Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus lectus, sit amet suscipit nibh. Proin nec commodo purus. Sed eget nulla elit. Nulla aliquet mollis faucibus.
    <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-button</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#F45E43"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>Learn more<span class="hljs-tag"></<span class="hljs-name">mj-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">栏目部分</h3>
<p>在这封邮件的部分，我们会有两栏：一栏是描述性的图片，二栏是我们的文字块，用来补充第一部分的图片。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Side image --></span>
<span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"white"</span>></span>
  <span class="hljs-comment"><!-- Left image --></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200px"</span>
              <span class="hljs-attr">src</span>=<span class="hljs-string">"https://navis-consulting.com/wp-content/uploads/2019/09/Cruise1-1.png"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
  <span class="hljs-comment"><!-- right paragraph --></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
             <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
             <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>
             <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>
      Amazing Experiences
    <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"#525252"</span>></span>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
      Proin rutrum enim eget magna efficitur, eu semper augue semper. 
      Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus 
      lectus.
    <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>左侧的第一列使用 <code>mj-image</code> 组件指定要使用的图像。该图像可以是本地文件，也可以是远程托管的图像（在我们的情况下是这样）。</p>
<p>右侧的第二列包含两个文本块，一个用于我们的标题，另一个用于主体文本。</p>
<h3 data-id="heading-7">图标</h3>
<p>图标部分将分为三列。你还可以添加更多内容，具体取决于你希望电子邮件的外观。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Icons --></span>
<span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fbfbfb"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x0l.png"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x01.png"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x0s.png"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每列都有其自己的 <code>mj-image</code> 组件，用于渲染图标图像。</p>
<h3 data-id="heading-8">社交图标</h3>
<p>本部分将包含指向我们的社交媒体帐户的图标。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#e7e7e7"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-social</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-social-element</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"instagram"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-social</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>MJML带有 <code>mj-social</code> 组件，可轻松用于显示社交媒体图标。在我们的电子邮件中，我们使用了 Twitter <code>mj-social-element</code>。</p>
<h2 data-id="heading-9">全部放在一起</h2>
<p>至此，我们已经实现了所有部分，完整的 <code>email.mjml</code> 应该如下所示：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">mjml</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">mj-body</span>></span>
    <span class="hljs-comment"><!-- Company Header --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#f0f0f0"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span>  <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
                 <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
                 <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span>
                 <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>
          Central Park Cruises
        <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Image Header --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-url</span>=<span class="hljs-string">"https://ca-times.brightspotcdn.com/dims4/default/2af165c/2147483647/strip/true/crop/2048x1363+0+0/resize/1440x958!/quality/90/?url=https%3A%2F%2Fwww.trbimg.com%2Fimg-4f561d37%2Fturbine%2Forl-disneyfantasy720120306062055"</span>
                <span class="hljs-attr">background-size</span>=<span class="hljs-string">"cover"</span>
                <span class="hljs-attr">background-repeat</span>=<span class="hljs-string">"no-repeat"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span>  <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span>
                 <span class="hljs-attr">color</span>=<span class="hljs-string">"#fff"</span>
                 <span class="hljs-attr">font-size</span>=<span class="hljs-string">"40px"</span>
                 <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>></span>Christmas Discount<span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-button</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#F63A4D"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>
          See Promotions
        <span class="hljs-tag"></<span class="hljs-name">mj-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Email Introduction --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fafafa"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"400px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
                 <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
                 <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>
                 <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>Ultimate Christmas Experience<span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"#525252"</span>></span>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rutrum enim eget magna efficitur, eu semper augue semper. Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus lectus, sit amet suscipit nibh. Proin nec commodo purus. Sed eget nulla elit. Nulla aliquet mollis faucibus.
        <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-button</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#F45E43"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>Learn more<span class="hljs-tag"></<span class="hljs-name">mj-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Columns section --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"white"</span>></span>
      <span class="hljs-comment"><!-- Left image --></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200px"</span>
                  <span class="hljs-attr">src</span>=<span class="hljs-string">"https://navis-consulting.com/wp-content/uploads/2019/09/Cruise1-1.png"</span>/></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
      <span class="hljs-comment"><!-- right paragraph --></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">font-style</span>=<span class="hljs-string">"bold"</span>
                 <span class="hljs-attr">font-size</span>=<span class="hljs-string">"20px"</span>
                 <span class="hljs-attr">font-family</span>=<span class="hljs-string">"Helvetica Neue"</span>
                 <span class="hljs-attr">color</span>=<span class="hljs-string">"#626262"</span>></span>
          Amazing Experiences
        <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-text</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"#525252"</span>></span>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
          Proin rutrum enim eget magna efficitur, eu semper augue semper. 
          Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus 
          lectus.
        <span class="hljs-tag"></<span class="hljs-name">mj-text</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Icons --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fbfbfb"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x0l.png"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x01.png"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://191n.mj.am/img/191n/3s/x0s.png"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
    <span class="hljs-comment"><!-- Social icons --></span>
    <span class="hljs-tag"><<span class="hljs-name">mj-section</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#e7e7e7"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mj-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mj-social</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">mj-social-element</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"instagram"</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">mj-social</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">mj-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">mj-section</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">mj-body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mjml</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">运行我们的应用程序</h2>
<p>现在我们已经完成了电子邮件的构建，我们可以继续对其进行编译以查看其外观。为此，我们在终端中键入以下内容：</p>
<pre><code class="hljs language-shell copyable" lang="shell">mjml -r email.mjml -o .
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>-r</code>：允许MJML读取和编译我们的 <code>mjml</code> 文件</li>
<li><code>-o .</code>：告诉MJML将编译后的 <code>mjml</code> 输出保存到同一目录中</li>
</ul>
<p>MJML完成编译后，你现在应该在同一目录中看到一个 <code>email.html</code> 文件。 使用你喜欢的电子邮件客户端或浏览器打开它，它的外观应类似于下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46c856e2d620474f858a5d9c2b105133~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">总结</h2>
<p>正如我们刚才看到的，MJML帮助我们生成跨多个浏览器和客户机响应的高质量、漂亮的HTML电子邮件。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            