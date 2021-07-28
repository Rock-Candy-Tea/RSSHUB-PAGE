
---
title: '阿ken的HTML、CSS的入门指南_CSS3选择器（笔记四）2'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img-blog.csdnimg.cn/20201117143115248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 09:44:24 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20201117143115248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.7  并集选择器</h3>
<p><strong>并集选择器又叫复合选择器</strong><br>
可以选中同时满足多个选择器的元素<br>
并集选择器是各个选择器通过<strong>逗号</strong>连接而成</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>并集选择器<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span> = <span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">h2</span>,<span class="hljs-selector-tag">h3</span>,<span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">color</span>: red;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125; <span class="hljs-comment">/*不同标记组成的并集选择器*/</span>

<span class="hljs-selector-tag">h3</span>,<span class="hljs-selector-class">.special</span>,<span class="hljs-selector-id">#one</span> &#123;
<span class="hljs-attribute">text-decoration</span>: underline;   
&#125;  <span class="hljs-comment">/* 加下划线 */</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>二级标题文本<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>                           <span class="hljs-comment"><!--字体14像素、红色--></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>三级标题文本<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>                           <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"special"</span>></span>段落文本1,加下划线。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>      <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>段落文本2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>                               <span class="hljs-comment"><!--字体14像素、红色--></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span>></span>段落文本3<span class="hljs-tag"></<span class="hljs-name">p</span>></span>                      <span class="hljs-comment"><!--字体14像素、红色、加下划线--></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117143115248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码字号和颜色相同，只是有一个标题和两个段落文本有下划线效果（上述已注明）。</p>
<h3 data-id="heading-1"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>4.3.8  属性选择器</h3>
<ol>
<li><strong>E[att^=value] 属性选择器</strong></li>
</ol>
<p>E[att^=value]属性选择器是指选择名称为E的标记，且该标记定义了 att 属性，att 属性值包含<strong>前缀</strong>为 value 的子字符串。</p>
<p>需要注意的是<strong>E是可以省略的</strong>，<strong>如果省略则表示可以匹配满足条件的任意元素</strong>。\</p>
<p>例如：<code>div\[id^=section]</code>表示匹配包含<code>id</code>属性，且<code>id</code>属性值是以“<code>section</code>”字符串<strong>开头</strong>的<code>div</code>元素。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att^=value] 属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id^=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117143521332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了E[att^=value]属性选择器 “ p[id ^=“one”] ” 。<br>
只要p元素中的 id 属性值是<strong>以“ one ”字符串开头就会被选中</strong>，从而呈现特殊的文本效果。</p>
<ol start="2">
<li><strong>E[att$=value] 属性选择器</strong></li>
</ol>
<p>E[att$=value] 属性选择器是指选择名称为E的标记，且该标记定义了<code>att</code>属性，<code>att</code>属性值包含<strong>后缀</strong>为<code>value</code>的子字符串。</p>
<p><strong>E是可以省略的，如果省略则表示可以匹配满足条件的任意元素</strong>。</p>
<p>例如：<code>div[id$=section]</code>表示匹配包含 id 属性，且<code>id</code>属性值是以“<code>section</code>”字符串<strong>结尾</strong>的<code>div</code>元素。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att$=value]属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id$=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"1one"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/2020111714433132.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了E[att$=value]属性选择器 “ p[id $=“one”] ” 。<br>
只要p元素中的 id 属性值是<strong>以“ one ”字符串结尾就会被选中</strong>，从而呈现特殊的文本效果。</p>
<ol start="3">
<li><strong>E[att*=value] 属性选择器</strong></li>
</ol>
<p><code>E[att*=value]</code>属性选择器是指选择名称为E的标记，且该标记定义了<code>att</code>属性，<strong><code>att</code>属性值包含<code>value</code>的子字符串。</strong></p>
<p><strong>E是可以省略的，如果省略则表示可以匹配满足条件的任意元素</strong>。</p>
<p>例如：<code>div[id*=section]</code>表示匹配包含<code>id</code>属性，且 id 属性值<strong>包含“<code>section</code>”字符串</strong>的<code>div</code>元素。</p>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>E[att*=value]属性选择器的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">p</span><span class="hljs-selector-attr">[id*=<span class="hljs-string">"one"</span>]</span> &#123;
<span class="hljs-attribute">color</span>: pink;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"one1"</span>></span>
天空是蔚蓝色
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two"</span>></span>
窗外有千纸鹤
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>   <span class="hljs-comment"><!-- 属性选择器不定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"1one"</span>></span>
陪我弹琴写歌
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器已定义 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"two2"</span>></span>
每一分每一刻
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  <span class="hljs-comment"><!-- 属性选择器不定义 --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201117144550175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中，使用了<code>E[att*=value]</code>属性选择器 “<code>p[id*=“one”]</code>” 。<br>
只要<code>p</code>元素中的<code>id</code>属性值是<strong>包含“<code>one</code>”字符串就会被选中</strong>，从而呈现特殊的文本效果。</p></div>  
</div>
            