
---
title: '前端面试常备09：你应该知道的CSS选择器知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/813e718fa3bc45acb14295a7f7c61f94~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 18:34:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/813e718fa3bc45acb14295a7f7c61f94~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>选择器是CSS规则的一部分, 且位于CSS声明块的前面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/813e718fa3bc45acb14295a7f7c61f94~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择器可以按类别简单的分为:</p>
<ul>
<li><code>简单选择器(Simple Selectors)</code>: 通过元素类型, class, id匹配一个或多个元素</li>
<li><code>属性选择器(Attribute selectors)</code>: 通过 属性 / 属性值 匹配一个或多个元素。</li>
<li><code>伪类(Pseudo-classes)</code>: 匹配处于确定状态的一个或多个元素，比如被鼠标指针悬停的元素，或当前被选中或未选中的复选框，或元素是 DOM 树中一父节点的第一个子节点。</li>
<li><code>伪元素(Pseudo-elements)</code>: 匹配处于相关的确定位置的一个或多个元素, 例如每个段落的第一个字, 或者某个元素之前生成的内容.</li>
<li><code>组合器(Combinators)</code>: 以有效的方式组合两个或更多的选择器用于非常特定的选择的方法。</li>
<li><code>多用选择器(Multiple Selectors)</code>: 以逗号分开的多个选择器放在一个CSS规则下</li>
</ul>
<h2 data-id="heading-0">简单选择</h2>
<ul>
<li>元素选择器: <code>p</code>, <code>div</code>, <code>span</code> 等</li>
<li>类选择器(<code>.</code>): <code>.name</code>, <code>.header</code> 等</li>
<li>ID选择器(<code>#</code>): <code>#id</code>, <code>#root</code>等</li>
<li>通用选择器(<code>*</code>):: <code>*</code></li>
</ul>
<h2 data-id="heading-1">组合器</h2>
<ul>
<li><code>A,B</code>: 匹配满足A或B的任意元素.</li>
<li><code>A B</code>: 匹配<code>B是A的后代节点</code>的任意元素</li>
<li><code>A > B</code>: 匹配<code>B是A的直接子节点</code>的任意元素</li>
<li><code>A + B</code>: 匹配<code>B是A的下一个兄弟节点</code>的任意元素</li>
<li><code>A ~ B</code>: 匹配<code>B是A之后的兄弟节点</code>的任意元素</li>
</ul>
<h2 data-id="heading-2">属性选择器</h2>
<p>属性选择器根据元素的属性和属性值来匹配元素. 通用语法是<code>[*]</code>. 根据匹配属性值的方式分为:</p>
<ul>
<li>存在和值属性选择器</li>
<li>子串值属性选择器</li>
</ul>
<h3 data-id="heading-3">存在和值(Presence and Value)属性选择器</h3>
<p>这些属性选择器会尝试匹配精确的属性值:</p>
<ul>
<li><code>[attr]</code>: 选择包含<code>attr</code>属性的所有元素, 不论值为何</li>
<li><code>[attr=val]</code>: 选择包含<code>attr</code>为<code>val</code>值的所有元素</li>
<li><code>[arrt~=val]</code>: 选择存在<code>attr</code>属性且值包含(以空格间隔出多个值)<code>val</code>的所有元素, 比如class类</li>
</ul>
<h3 data-id="heading-4">子串(Substring value)属性选择器</h3>
<p>这种情况的属性选择器也被称为"伪正则选择器", 因为他们提供类似<code>regular expression</code>的灵活匹配方式:</p>
<ul>
<li><code>[attr|=val]</code>: 选择attr属性的值以val（包括val）或val-开头的元素（-用来处理语言编码）。</li>
<li><code>[attr^=val]</code>: 选择attr属性的值以val开头（包括val）的元素。</li>
<li><code>[attr$=val]</code>: 选择attr属性的值以val结尾（包括val）的元素。</li>
<li><code>[attr*=val]</code>: 选择attr属性的值中包含字符串val的元素。</li>
</ul>
<h2 data-id="heading-5">选择器优先级</h2>
<ul>
<li>优先级规则 1: 最近的祖先样式比其他祖先样式优先级高(就近原则)</li>
<li>优先级规则 2: "直接样式"比"祖先样式"优先级高</li>
<li>优先级规则 3: 内联样式 > ID 选择器 > 类选择器 = 属性选择器 = 伪类选择器 > 标签选择器 = 伪元素选择器</li>
<li>优先级规则 4: ：计算选择符中 ID 选择器的个数（a），计算选择符中类选择器、属性选择器以及伪类选择器的个数之和（b），计算选择符中标签选择器和伪元素选择器的个数之和（c）。按 a、b、c 的顺序依次比较大小，大的则优先级高，相等则比较下一个。若最后两个的选择符中 a、b、c 都相等，则按照"就近原则"来判断。</li>
<li>优先级规则 5:属性后插有 !important 的属性拥有最高优先级。若同时插有 !important，则再利用规则 3、4 判断优先级</li>
</ul>
<blockquote>
<p><strong>权重计算需要注意的一点细节</strong><br>
在学习过程中，你可能发现给选择器加权值的说法，即 ID 选择器权值为 100，类选择器权值为 10，标签选择器权值为 1，当一个选择器由多个 ID 选择器、类选择器或标签选择器组成时，则将所有权值相加，然后再比较权值。</p>
<p>这种说法其实是有一点小问题。比如一个由 11 个类选择器组成的选择器和一个由 1 个 ID 选择器组成的选择器指向同一个标签，按理说 110 > 100，应该应用前者的样式，然而事实是应用后者的样式。</p>
<p>错误的原因是：<strong>选择器的权值不能进位</strong>。还是拿刚刚的例子说明。11 个类选择器组成的选择器的总权值为 110，但因为 11 个均为类选择器，所以其实总权值最多不能超过 100， 你可以理解为 99.99，所以最终应用后者样式。</p>
</blockquote>
<h2 data-id="heading-6">伪类和伪元素</h2>
<p>伪类（pseudo-class） 是一个以冒号(:)作为前缀，被添加到一个选择器末尾的关键字，当你希望样式在特定状态下才被呈现到指定的元素时，你可以往元素的选择器后面加上对应的伪类。</p>
<p>伪元素用于创建一些不在文档树中的元素，并为其添加样式。比如说，我们可以通过::before 来在一个元素前增加一些文本，并为这些文本添加样式。虽然用户可以看到这些文本，但是这些文本实际上不在文档树中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb070758eca49a498f7b9a0f8d07054~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于单冒号和双冒号:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b4bce3402f43fe84998e28d611cb94~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">伪类</h3>
<h4 data-id="heading-8">状态</h4>
<ul>
<li><code>:link</code>: 选择未访问的链接</li>
<li><code>:visited</code>: 选择已访问的链接</li>
<li><code>:hover</code>: 选择鼠标指针浮动在其上的元素</li>
<li><code>:active</code>: 选择活动的链接</li>
<li><code>:focus</code>: 选择获取焦点的输入字段</li>
</ul>
<h4 data-id="heading-9">结构化</h4>
<ul>
<li><code>:not</code>: 用于匹配不符合参数选择器的元素</li>
<li><code>:first-child</code>: 匹配第一个子元素</li>
<li><code>:last-child</code>: 匹配最后一个子元素</li>
<li><code>:first-of-type</code>:匹配属于其复原的某个特定类型的子元素的每个元素</li>
<li><code>:last-of-type</code>:匹配元素的最后一个子元素。</li>
<li><code>:nth-child</code>: 根据元素的位置匹配一个或多个元素, 可以接受 an+b 的参数</li>
<li><code>:nth-last-child</code>: 与<code>:nth-child</code>类似, 不同之处在于它是从最后一个子元素开始计数</li>
<li><code>:nth-of-type</code>: 与<code>:nth-child</code>相似, 不同之处在于只匹配特定类型的元素</li>
<li><code>:nth-last-type</code>: 与 <code>nth-of-type</code> 相似，不同之处在于它是从最后一个子元素开始计数的。</li>
<li><code>:only-child</code>: 当元素是其父元素中唯一一个子元素时，<code>:only-child</code> 匹配该元素。</li>
<li><code>:only-of-type</code>:当元素是其父元素中唯一一个特定类型的子元素时，:only-child 匹配该元素。</li>
<li><code>:target</code>: 当 URL 带有锚名称，指向文档内某个具体的元素时，:target 匹配该元素。简单的说, 就是锚点激活的状态</li>
</ul>
<h4 data-id="heading-10">表单</h4>
<ul>
<li><code>:checked</code>: 被选中的 input 标签(radio/checkbox)</li>
<li><code>:default</code>: 默认选中的元素</li>
<li><code>:disabled</code>: 禁用的表单元素</li>
<li><code>:empty</code>: 没有子元素的元素(子元素包含文本节点, HTML 元素或者一个空格)</li>
<li><code>:enabled</code>:没有设置 disabled 属性的表单元素</li>
<li><code>:in-range</code>:匹配在指定区域内元素</li>
<li><code>:out-of-range</code>:匹配不在指定区域内的元素</li>
<li><code>:indeterminate</code>:当某组中的单选框或复选框还没有选取状态时，:indeterminate 匹配该组中所有的单选框或复选框。</li>
<li><code>:valid</code>:条件验证正确的表单元素。</li>
<li><code>:invalid</code>:条件验证错误的表单元素</li>
<li><code>:optional</code>:匹配具有 optional 属性点的表单元素</li>
<li><code>:required</code>:与<code>:optional</code> 相反匹配设置了<code>required</code>属性的表单元素。</li>
<li><code>:read-only</code>:匹配设置了只读属性的元素，表单元素可以通过设置“readonly” 属性来定义元素只读</li>
<li><code>:read-write</code>:匹配处于编辑状态的元素。</li>
<li><code>:scope</code>(处于试验阶段):匹配处于 style 作用域下的元素。当 style 没有设置 scope 属性时，style 内的样式会对整个 html 起作用</li>
</ul>
<h4 data-id="heading-11">语言</h4>
<ul>
<li><code>:dir()</code>(处于试验阶段): 匹配指定阅读方向的元素</li>
<li><code>:lang()</code>: 匹配设定了特定语言的元素</li>
</ul>
<h4 data-id="heading-12">其他</h4>
<ul>
<li><code>:root</code>: 匹配文档的根元素</li>
<li><code>:fullscreen</code>匹配全屏模式下的元素</li>
</ul>
<h3 data-id="heading-13">伪元素</h3>
<ul>
<li><code>::before/:before</code>:在被选元素之前插入</li>
<li><code>::after/:after</code>: 在被元素后插入内容</li>
<li><code>::first-letter/:first-letter</code>::first-letter 匹配元素中文本的首字母。被修饰的首字母不在文档树中。</li>
<li><code>::first-line/:first-line</code>:匹配元素中第一行的文本。这个伪元素只能用在块元素中，不能用在内联元素中</li>
<li><code>::selection</code>: 匹配用户被用户选中或者处于高亮状态的部分,在火狐浏览器使用时需要添加-moz 前缀。该伪元素只支持双冒号的形式。</li>
<li><code>::placeholder</code>:匹配占位符的文本，只有元素设置了 placeholder 属性时，该伪元素才能生效。</li>
<li><code>::backdrop</code>(处于试验阶段):于改变全屏模式下的背景颜色，全屏模式的默认颜色为黑色。该伪元素只支持双冒号的形式</li>
</ul>
<p>其中属于css3新增的有:</p>
<ul>
<li><code>p:first-of-type</code></li>
<li><code>p:last-of-type</code></li>
<li><code>p:only-of-type</code></li>
<li><code>p:only-child</code></li>
<li><code>p:nth-child(2)</code></li>
<li><code>:enabled</code></li>
<li><code>:disabled</code></li>
<li><code>:checked</code></li>
<li><code>::before</code></li>
<li><code>::after</code></li>
<li><code>::first-line</code></li>
<li><code>::first-letter</code></li>
</ul>
<h2 data-id="heading-14">参考链接</h2>
<ul>
<li><a href="http://www.alloyteam.com/2016/05/summary-of-pseudo-classes-and-pseudo-elements/" target="_blank" rel="nofollow noopener noreferrer">总结伪类与伪元素</a></li>
<li><a href="https://segmentfault.com/a/1190000013424772" target="_blank" rel="nofollow noopener noreferrer">CSS 选择器，一篇就够了</a></li>
<li><a href="https://www.runoob.com/w3cnote/css-style-priority.html" target="_blank" rel="nofollow noopener noreferrer">CSS 样式优先级</a></li>
</ul></div>  
</div>
            