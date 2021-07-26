
---
title: 'CSS 进阶之熟悉又陌生的 content'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 16:14:03 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>陈晨，微医云服务团队前端工程师，一位“生命在于静止”的程序员。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在开发中遇到类似清除浮动、小图标、替换内容等场景时不可避免会遇到 content 属性，一般就是百度下解决方案，甚少细究到底，在看《CSS 世界》这本书时看了下 content 章节，今天这里就详细介绍下 content 的使用机制。<br>
content 属性用于与 :before 及 :after 伪元素配合使用，来插入生成内容。使用 content 属性插入的内容都是匿名的可替换元素。首先我们先了解下什么是可替换元素呢？</p>
<h2 data-id="heading-1">替换元素</h2>
<p>首先看下图片加载：</p>
<pre><code class="copyable"><img src="1.jpg">
<!--替换-->
<img src="2.jpg">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改了 img 的 src 属性，导致显示的图片发生了变化。这种通过修改某个属性值呈现的内容就可以被替换的元素就称为“替换元素”。</p>
<p>典型的替换元素：<code><img></code>、<code><video></code>、<code><iframe></code>、<code><textarea></code> 和 <code><input></code>。</p>
<h3 data-id="heading-2">替换元素的尺寸计算规则</h3>
<p>替换元素的尺寸计算规则有三种尺寸：</p>
<ul>
<li>固有尺寸：替换内容原本的尺寸</li>
<li>HTML 尺寸：HTML 原生属性 width 和 height</li>
<li>CSS 尺寸：通过 CSS 设置的宽高属性</li>
</ul>
<p>下面我们以 img 为例：</p>
<pre><code class="copyable"><img src="../assets/test1.jpeg">
<img width="300" height="200" class="img-test" src="../assets/test1.jpeg">
<img class="img-box" width="300" height="200" src="../assets/test1.jpeg">

.img-box &#123;
  height: 100px;
  width: 200px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b52a880a18e42a6a72750a227ff3e30~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
第一张图：默认显示原图尺寸 267 * 200；<br>
第二张图：设置了 HTML 尺寸 width 和 height，显示图片 300 * 200；<br>
第三张图：设置了 CSS 尺寸 200 * 100。</p>
<p>由此可见尺寸显示规则优先级为 CSS 尺寸 > HTML 尺寸 > 固有尺寸。</p>
<h3 data-id="heading-3">替换元素和 content 是什么关系呢？</h3>
<p>替换元素之所以为替换元素，就是因为其内容可替换，即盒模型中的 content box 可替换。CSS 的 content 属性就用于替换内容，也可以说，content 属性决定了是替换元素还是非替换元素。代码如下：</p>
<pre><code class="copyable"><img width="300" height="200" class="img-test" src="../assets/test1.jpeg">

.img-test:hover &#123;
 content: url('../assets/test2.jpg');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baf64eca886d478fbf376c94423ee2b4~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
此时鼠标悬浮的时候图片为 ’../assets/test2.jpg‘，使用 content 属性替换了 img 的 content box。<br>
需要注意的是 content 属性改变的仅仅是视觉呈现，当我们以右键或其他形式保存这张图片的时候，所保存的还是原来 src 对应的图片。</p>
<h2 data-id="heading-4">content 的使用场景</h2>
<p>content 的定义中就提到过是和 :before 及 :after 伪元素配合使用。:before 及 :after 是最常见的伪元素，想必大家都不陌生。</p>
<p>再简单介绍下 :before 和 :after：</p>
<ul>
<li>默认 display: inline；</li>
<li>必须设置 content 属性，否则无效；</li>
<li>默认 user-select: none，即 :before 和 :after 的内容无法被用户选中；</li>
<li>不可通过 dom 使用，就是本身不存在的页面元素，HTML 源代码里，找不到它们，但从视觉上，却能看到它们的存在。</li>
</ul>
<p>下面我们看一下主要使用场景：</p>
<h3 data-id="heading-5">插入字符</h3>
<p>使用 content 插入字符一般是给空元素设置默认值，类似 input 的 placeholder 属性一样，只在元素没有内容的时候展示，代码如下：</p>
<pre><code class="copyable"><p>有内容的段落</p>
<p></p>

<!--:empty 是一个 CSS 选择器，当元素里面无内容的时候进行匹配-->
p:empty::before &#123;
  content: '空元素内容';
  color: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a883c27da110412f9dbf74dc83b98b2e~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">辅助元素生成</h3>
<p>此时核心点不在于 content 生成的内容，而是伪元素本身。通常我们会把 content
的属性值设置为空字符串，使用其他 CSS 代码来生成辅助元素，或实现图形效果，或实现特定布局。</p>
<h4 data-id="heading-7">图形效果</h4>
<p>使用 ::after 伪元素插入匿名替换元素，设置 content 为空，此元素没有内容，通过 CSS 样式来达到想要的图形效果。代码如下：</p>
<pre><code class="copyable"><div class="content-box"></div>

.content-box &#123;
  height: 100px;
  width: 200px;
  border-radius: 10px;
  position: relative;
  background: #fff;
&#125;
.content-box::after &#123;
  content: '';
  position: absolute;
  top: 100%;
  right: 16px;
  width: 4px;
  height: 16px;
  border-width: 0;
  border-right: 12px solid #fff;
  border-radius: 0 0 32px 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e58b7f0a034161bdb8556f02daa2b2~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">清除浮动</h4>
<p>清除浮动主要是为了解决，父元素因为子级元素浮动引起的内部高度为 0 的问题，代码如下：</p>
<pre><code class="copyable"><div class="info-box clear">
  <div class="left">左</div>
  <div class="right">右</div>
</div>

.clear::after &#123;
 content: '';
 display: block;
 clear: both;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面三者缺一不可：</p>
<ul>
<li>content: ''：通过 ::after 给元素添加一个空的伪元素。</li>
<li>clear: both：清除浮动，使得元素周围两边都不浮动。</li>
<li>display: block：clear 只对块级元素生效。</li>
</ul>
<p>通过添加元素清除浮动，触动 BFC，使元素的高能够自适应子盒子的高。</p>
<h3 data-id="heading-9">图片生成</h3>
<p>直接用 url 功能符显示图片，既可以在文字前后添加图片，又可以直接替换文字。</p>
<p>图片直接替换文字，代码如下：</p>
<pre><code class="copyable"><p class="img-test">文字</p>

.img-test &#123;
  display: block;
  height: 20px;
  width: 20px;
  border-radius: 100%;
  content: url('../assets/test2.jpg');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文字前后添加图片，代码如下：</p>
<pre><code class="copyable"><!--方案一 -->
.img-test::after &#123;
  content: url('../assets/test2.jpg');
&#125;

<!--方案二 -->
.img-test::after &#123;
  content: '';
  display: block;
  height: 20px;
  width: 20px;
  background: url('../assets/test2.jpg');
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案一中伪元素通过 content 设置图片，图片的尺寸不好控制，显示图片为原尺寸，比较模糊，一般使用方案二背景图片的方式，可以按需设置尺寸。</p>
<h3 data-id="heading-10">attr 属性值内容生成</h3>
<p>使用 attr 获取元素属性值达到效果，一般用于获取 a 标签的连接，代码如下：</p>
<pre><code class="copyable"><a class="baidu-link" href="https://baidu.com"> 百度一下，你就知道!</a>

.baidu-link::after &#123;
  content: " (" attr(href) ") "
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aae5e74d03040f392a26b9ab8adfc3a~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">字符内容生成</h3>
<p>content 字符内容生成就是直接写入字符内容，中英文都可以，比较常见的应用就是配合 @font-face 规则实现图标字体效果。</p>
<h4 data-id="heading-12">@font-face 规则</h4>
<p>@font-face 规则指定一个用于显示文本的自定义字体；字体能从远程服务器或者用户本地安装的字体加载。它的属性和字体相似，如下：</p>

































<table><thead><tr><th>字体描述符</th><th>描述</th></tr></thead><tbody><tr><td>font-family</td><td>必需：所指定的字体名字将会被用于 font 或 font-family 属性</td></tr><tr><td>src</td><td>必需：远程字体文件位置的 url 或者用户计算机上的字体名称</td></tr><tr><td>font-style</td><td>对于 src 所指字体的样式</td></tr><tr><td>font-weight</td><td>字体粗细</td></tr><tr><td>font-stretch</td><td>定义应如何拉伸字体</td></tr><tr><td>unicode-range</td><td>该字体支持 Unicode 字符的范围</td></tr></tbody></table>
<p>使用 @font-face 规则的代码如下：</p>
<pre><code class="copyable"><!--format 属性是帮助浏览器识别字体的-->
@font-face &#123;font-family: "iconfont";
  src: url('iconfont.eot'); /* IE9*/
  src: url('iconfont.eot#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('iconfont.woff') format('woff'), /* chrome, firefox */
  url('iconfont.ttf') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+*/
  url('iconfont.svg#iconfont') format('svg'); /* iOS 4.1- */
&#125;

<!--html-->
<div class="look-more">查看更多</div>

<!--css-->
.look-more &#123;
  font-size: 14px;
  &::after &#123;
    font-size: 14px;
    font-family: 'iconfont';
    content: '\e6a7';
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f974560cdbe4b4182e310a1bf5f0c34~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，“查看更多”后面的箭头就是上面定义的字体图标。</p>
<p>当然 @font-face 也有不可避免的兼容性问题，可根据需要使用此规则，支持度如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59077c49488a47e0b74f2602ea129a2e~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">计数器</h3>
<p>content 的计数器是使用 CSS 代码实现随着元素数目增多，数值也跟着变大的效果。功能非常强大、实用，且不具有可替代性。</p>
<p>计数器包含两个属性和一个方法：</p>
<ol>
<li>counter-reset：“计数器-重置”的意思，主要作用就是给计数器起个名字。也告诉从哪个数字开始计数，默认值是 0，值可以为负数。</li>
</ol>
<pre><code class="copyable"><!--计数器名字为 counter，默认值为 0-->
.count-test &#123; counter-reset: counter; &#125;

<!--计数器名字为 counter，初始计数为 2-->
.count-test &#123; counter-reset: counter 2; &#125;

<!--多个计数器同时命名，使用空格分隔-->
.count-test &#123; counter-reset: counter 2 counterpre -1; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>counterincrement：“计数器递增”的意思，值为 counter-reset 的 1 个或多个关键字，后面可以跟随数字，表示每次计数的变化值，默认变化值为 1，值可以为负数。</li>
</ol>
<pre><code class="copyable"><!--counter 计数器默认递增 1-->
counter-increment: counter;

<!--counter 计数器递增 2-->
counter-increment: counter 2;

<!--counter 计数器递增 2，counterpre 计数器递减 -1-->
counter-increment: counter 2 counterpre -1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>“普照规则”：普照源（counter-reset）唯一，每普照（counter-increment）一次，普照源增加一次计数值。</p>
<pre><code class="copyable"><p class="counter"></p>

<!--counter-increment 普照源 <p> 标签，初始值为 2，counter-reset 值增加，默认递增 1，最终显示为 3-->
.counter &#123;
 counter-reset: counter 2;
 counter-increment: counter;
&#125;
.counter:before &#123;
 content: counter(counter);
&#125;

<!-- counter-increment 直接设置在伪元素上普照自身，和上述一样显示 3-->
.counter &#123;
 counter-reset: counter 2;
&#125;
.counter:before &#123;
 counter-increment: counter;
 content: counter(counter);
&#125;

<!--父元素和子元素都被 counter-increment 普照 1 次，递增了两次，最终显示为 4-->
.counter &#123;
 counter-reset: counter 2;
 counter-increment: counter;
&#125;
.counter:before &#123;
 counter-increment: counter;
 content: counter(counter);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>counter()/counters()：都是计数方法，显示计数，counters 用于嵌套计数。</li>
</ol>
<pre><code class="copyable"><!--name 就是 counter-reset 的名称-->
counter(name)

<!--style 值就是 list-style-type 支持的那些值，可以是英文等-->
counter(name, style)

<!--string 参数为字符串（需要引号包围的，是必需参数），表示子序号的连接字符串。例如，1.1 的 string 就是'.'，1-1 就是'-'-->
counters(name, string)

counters(name, string, style)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般用于类似目录以及规律变化的计数，下面以层级目录为例，代码如下：</p>
<pre><code class="copyable"><div class="reset">
    <div class="counter">替换元素
        <div class="reset">
            <div class="counter">替换元素的尺寸计算规则</div>
            <div class="counter">替换元素和 content 是什么关系呢？</div>
        </div>
    </div>
    <div class="counter">content 的使用场景
        <div class="reset">
            <div class="counter">插入字符</div>
            <div class="counter">辅助元素生成</div>
            <div class="counter">图片生成</div>
            <div class="counter">attr 属性值内容生成</div>
            <div class="counter">字符内容生成</div>
            <div class="counter">计数器</div>
        </div>
    </div>
</div>

.reset &#123;
  counter-reset: counter;
&#125;
.counter:before &#123;
  content: counters(counter, '.') '. ';
  counter-increment: counter;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>counter 默认值为 0，默认递增为  1；</li>
<li>第一个 reset 下面有两个兄弟 conter 标签，递增则为 1 和 2;</li>
<li>第一个 counter 下面有 reset 标签，嵌套了一层重置计数，则有 1.1、1.2 等；</li>
<li>同理第二个 counter 下面有 2.1、2.2 等。</li>
</ul>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04fe87fa65ca4d52b59ecbb798515c3f~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">总结</h2>
<p>了解 CSS 的 content 属性，布局有了更多的可能性，有助于日常开发中根据需要使用一些布局小技巧，使布局简洁明了。</p>
<h2 data-id="heading-15">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fpseudo-element-roundup%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/pseudo-element-roundup/" ref="nofollow noopener noreferrer">css-tricks.com/pseudo-elem…</a></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b13582f9fe54791a0f37420637f9051~tplv-k3u1fbpfcp-watermark.image" alt="未命名_自定义px_2021-07-25-0.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            