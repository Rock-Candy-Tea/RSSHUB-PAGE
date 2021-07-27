
---
title: 'HTML5(一)——新增元素和属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/280556811d47490da45309a9af86b35e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 20:30:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/280556811d47490da45309a9af86b35e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>自 H5 诞生以来，在 html4.0 中有些元素已被 H5 废弃，但是在 H5 中添加了很多新元素以及功能，今天我们学习 H5 中新增的元素和属性都有哪些？</p>
<h1 data-id="heading-0">新增语义结构标签</h1>





























































































<table><thead><tr><th>标签</th><th>描述</th></tr></thead><tbody><tr><td>article</td><td>定义页面独立的内容区域。</td></tr><tr><td>aside</td><td>定义页面的侧边栏内容。</td></tr><tr><td>bdi</td><td>允许您设置一段文本，使其脱离其父元素的文本方向设置。</td></tr><tr><td>command</td><td>定义命令按钮，比如单选按钮、复选框或按钮</td></tr><tr><td>details</td><td>用于描述文档或文档某个部分的细节</td></tr><tr><td>dialog</td><td>定义对话框，比如提示框</td></tr><tr><td>summary</td><td>标签包含 details 元素的标题</td></tr><tr><td>figure</td><td>规定独立的流内容（图像、图表、照片、代码等等）。</td></tr><tr><td>figcaption</td><td>定义 figure 元素的标题</td></tr><tr><td>footer</td><td>定义 section 或 document 的页脚。</td></tr><tr><td>header</td><td>定义了文档的头部区域</td></tr><tr><td>mark</td><td>定义带有记号的文本。</td></tr><tr><td>meter</td><td>定义度量衡。仅用于已知最大和最小值的度量。</td></tr><tr><td>nav</td><td>定义导航链接的部分。</td></tr><tr><td>progress</td><td>定义任何类型的任务的进度。</td></tr><tr><td>ruby</td><td>定义 ruby 注释（中文注音或字符）。</td></tr><tr><td>rt</td><td>定义字符（中文注音或字符）的解释或发音。</td></tr><tr><td>rp</td><td>在 ruby 注释中使用，定义不支持 ruby 元素的浏览器所显示的内容。</td></tr><tr><td>section</td><td>定义文档中的节（section、区段）。</td></tr><tr><td>time</td><td>定义日期或时间。</td></tr><tr><td>wbr</td><td>规定在文本中的何处适合添加换行符。</td></tr></tbody></table>
<p>新增标签使用时根据描述内容，在适当的地方使用新标签，应用的时候和其他标签是一样的，H5 新增标签使得网页结构更清晰明了，建议大家使用新增元素。</p>
<h1 data-id="heading-1">新增表单元素</h1>





















<table><thead><tr><th>标签</th><th>描述</th></tr></thead><tbody><tr><td>datalist</td><td>input标签定义选项列表。请与 input 元素配合使用该元素，来定义 input 可能的值。</td></tr><tr><td>keygen</td><td>keygen 标签规定用于表单的密钥对生成器字段。</td></tr><tr><td>output</td><td>output 标签定义不同类型的输出，比如脚本的输出。</td></tr></tbody></table>
<p>datalist属性规定form或input域应该拥有自动完成功能，当input聚焦时，浏览器应该在域中显示填写的选项。</p>
<p>使用 input 元素与 datalist 元素绑定，使用时如下：</p>
<pre><code class="copyable"><form action="">
 <input type="text" list="schooltype">
 <datalist id="schooltype">
  <option value="欧亚驾校">欧亚驾校</option>
  <option value="鹏程驾校">鹏程驾校</option>
  <option value="学车网">学车网</option>
 </datalist>    
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keygen 元素用于提供用户验证的方法，表单提交时，keygen生成表单密钥对，一个是公钥，一个是私钥，私钥存储在客户端，公钥通过带有keygen字段的表单发送给服务器。目前已被H5废弃，我们作为了解就好。</p>
<p>使用实例如下：</p>
<pre><code class="copyable"><form action="">
 用户名<input type="text" name="user" /><br>
 密码<input type="password" name="se"> <br>
 加密<keygen name="security"><br>
 <input type="submit" value="提交">
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>output 元素用于不同类型的输出，对输出结果的展示，如对两个数值相加，并展示结果，代码如下：</p>
<pre><code class="copyable"><form action="" oninput = "x.value=parseInt(a.value)+parseInt(b.value)">
 <input type="range" id="a" step="1" min="0" max="100"> + 
 <input type="text" id="b" value="50">=
 <output name="x" ></output> 
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述form处添加oninput事件，对数值parseInt进行取整运算。</p>
<h1 data-id="heading-2">新增表单属性</h1>
<p>H5中新增表单属性指 form 和 input 元素新增属性。</p>
<p><strong>form新属性及意义</strong></p>
<ul>
<li>autocomplete ：规定form域自动完成功能。</li>
<li>novalidate ：规定提交表单时是否验证域。</li>
</ul>
<p><strong>input新增类型和属性</strong></p>









































































<table><thead><tr><th>新的输入类型</th><th>新的输入属性</th></tr></thead><tbody><tr><td>color</td><td>autocomplete</td></tr><tr><td>date</td><td>-   autofocus</td></tr><tr><td>datetime</td><td>form</td></tr><tr><td>datetime-local</td><td>formaction</td></tr><tr><td>email</td><td>formenctype</td></tr><tr><td>month</td><td>formmethod</td></tr><tr><td>number</td><td>formnovalidate</td></tr><tr><td>range</td><td>formtarget</td></tr><tr><td>search</td><td>height 和 width</td></tr><tr><td>tel</td><td>list</td></tr><tr><td>url</td><td>min 和 max</td></tr><tr><td>week</td><td>multiple</td></tr><tr><td>autofocus</td><td>pattern (regexp)</td></tr><tr><td></td><td>placeholder</td></tr><tr><td></td><td>required</td></tr><tr><td></td><td>step</td></tr></tbody></table>
<p>input 和 form 的 autocomplete属性</p>
<p>属性规定 form 或 input 在当前域下拥有自动完成功能，通俗地讲就是元素聚焦时，会自动展示之前输入过的内容，内容是根据当前域名下之前使用过的数据。示例如下：</p>
<pre><code class="copyable"><form action="demo_form.asp" method="get" autocomplete="on">
 First name: <input type="text" name="fname" /><br />
 Last name: <input type="text" name="lname" /><br />
 E-mail: <input type="email" name="email" autocomplete="on" /><br />
 <input type="submit" />
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面上显示如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/280556811d47490da45309a9af86b35e~tplv-k3u1fbpfcp-zoom-1.image" alt="HTML5(一)——新增元素和属性" loading="lazy" referrerpolicy="no-referrer"></p>
<p>表单重写属性：</p>
<ul>
<li>formaction - 重写表单的 action 属性</li>
<li>formenctype - 重写表单 enctype 属性</li>
<li>formmethod - 重写表单 method 属性</li>
<li>formnovalidate - 重写表单 novalidate 属性</li>
<li>formtarget - 重写表单的 target 属性</li>
</ul>
<p>min、max、step属性</p>
<p>三者用于对数字、日期类型输入框的限制和约束。</p>
<ul>
<li>min - 规定允许设置的最小值。</li>
<li>max - 规定允许设置的最大值。</li>
<li>step - 规定合法的数字间隔。</li>
</ul>
<p>使用示例，请参照上output处的实例。</p>
<p>multipel属性：规定输入域中可选择多个值。适用于 email 和 file 两种类型。</p>
<p>pattern属性：验证input域的模式。模式pattern是正则表达式，适用于text、search、url、email、password。</p>
<h1 data-id="heading-3">废除的标签</h1>
<p>以下是一些在H5中已废弃的元素。</p>
<p>acronym、applet、basefont、big、center、dir、font、frame、frameset、noframes、strike、tt。</p></div>  
</div>
            