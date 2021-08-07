
---
title: '我与bootstrape select使用摩拳擦掌'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa753a738a204762bfb69b06bfd70e09~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 17:14:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa753a738a204762bfb69b06bfd70e09~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>

<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa753a738a204762bfb69b06bfd70e09~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>看看上面的效果是bootstrape使用的效果。虽然不是很好看，但是符合bootstrape的风格。来看看普通的select的样式</p>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79d53111abcc4201baee4c35ef0a32c1~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>bootstrape下的select和普通select在bootstrape风格对比</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98babe9f19ab4b738797cbfc0448fcf1~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/004f0e4d813446249bcdf04b76274aa2~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">引入</h2>
<ul>
<li>首先我们肯定得引入jQuery和bootstrape的相关js和css，在此基础上我们引入两个东西</li>
</ul>
<pre><code class="copyable">bootstrap-select.min.css
bootstrap-select.min.js
components-bootstrap-select.min.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">页面书写</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd158aecac142cab960a6157884530e~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>其中class属性必须包含bs-select ,且select属性中含有一下属性</li>
</ul>
<pre><code class="copyable">data-live-search（必须）
data-size="6"（可选）
id（必须）
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>data-live-search 是用于搜索的，本章搜索没实现，以后再详细设计，但是这个属性必须有。源码里根据他选择搜索的。</p>
</li>
<li>
<p>data-size 是设置数字，意思就是下拉框内容超过几条是开始出现滚动条。</p>
</li>
<li>
<p>id用于识别这个下拉框的</p>
</li>
</ul>
<h2 data-id="heading-2">Ajax请求加载select数据</h2>
<ul>
<li>项目中的select多数情况下都是动态数据加载的，那么下一步开始讨论动态数据的加载问题。首先肯定是发送请求。然后在ajax请求成功后的回调地方处理我们的动态数据加载问题。</li>
</ul>
<pre><code class="copyable">//调用公共插值方法
createSelectDate(siteDate,"site_id");
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">createSelectDate</h1>
<ul>
<li>
<p>这个方法我们需要传入两个参数，第一个是我们需要加载的数据，第二个使我们的数据加载在select的id</p>
</li>
<li>
<p>在来看看经过处理后我们的select</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc07e1adcba6420ea0c962b5c711bf9c~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>仔细观察发现ul  是页面显示的数据，select是我们真正的数据，所以我们只需要向这两个地方填充数据就行了。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce750c53b5814bb0b95fc079141cd625~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a36800869fdb4329bcd5d1715479e27a~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>向select加入数据很简单，通过ID加入，
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9112ac48fdcd483a8670cab78b617d6c~tplv-k3u1fbpfcp-watermark.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>关键是如何获取新的select即ul,经过实践通过以下方法就行。</li>
</ul>
<pre><code class="copyable">var $selectUl = $($($("button[data-id='"+select_id+"']").parent().children().get(1)).children().get(1));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后向新的对象添加内容</li>
</ul>
<pre><code class="copyable">$newSelect.append("<li data-original-index="+(index+1)+" class><a tabindex='0' class style data-tokens='null' role='option' aria-disabled='false' aria-selected='false'><span class='text'>"+value.site_name+"</span><span class='fa fa-check check-mark'></span></a></li>");
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">清空select选中值</h2>
<ul>
<li>用了这个之后我们会遇到问题，我们无法清空新select的内容，这就很尴尬。研究半天决定强行删除</li>
</ul>
<pre><code class="copyable">$("button[role='button'][data-id='"+select_id+"']").attr("title","请选择...");//selected active
$("button[role='button'][data-id='"+select_id+"'] span:first").text("请选择...");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们只需要调用相应的方法就行了。</p></div>  
</div>
            