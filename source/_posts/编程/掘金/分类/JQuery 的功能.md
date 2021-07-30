
---
title: 'JQuery 的功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f9aa81f95c4a2a8a06d8474b6e68b9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 00:49:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f9aa81f95c4a2a8a06d8474b6e68b9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f9aa81f95c4a2a8a06d8474b6e68b9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>jQuery是世界上最长寿的JavaScript函数库，从2006年发布至今依然有人使用jQuery，全世界浏览量排名在前面的网站，有百分之90%都在使用jQuery（不相信这个数据可以查看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftrends.builtwith.com%2Fjavascript%2FjQuery" target="_blank" rel="nofollow noopener noreferrer" title="https://trends.builtwith.com/javascript/jQuery" ref="nofollow noopener noreferrer">网站</a>），所以有必要去了解jQuery。</p>
<h3 data-id="heading-0">获取页面元素</h3>
<p>想要获取页面元素，按照JS原生代码需要这么获取：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'元素'</span>)
<span class="hljs-comment">//or</span>
<span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'选择器元素'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看着很长，代码多的话写起来挺麻烦的，而jQuery就十分简洁：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> element = $(<span class="hljs-string">'选择器元素'</span>)
<span class="hljs-comment">//例子：</span>
$(<span class="hljs-built_in">document</span>)<span class="hljs-comment">//选择整个文档</span>
$(<span class="hljs-string">'#myId'</span>)<span class="hljs-comment">//选择ID名为myId的网页元素</span>
$(<span class="hljs-string">'div.myClass'</span>)<span class="hljs-comment">//选择class名为myClass的div元素</span>
$(<span class="hljs-string">'input[namw=first]'</span>)<span class="hljs-comment">//选择name属性等于first的input元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>jQuery还有属于特有的表达：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'a:first'</span>)<span class="hljs-comment">//选择网页中的第一个a元素</span>
$(<span class="hljs-string">'tr:odd'</span>)<span class="hljs-comment">//选择表格的奇数行</span>
$(<span class="hljs-string">'#myForm:input'</span>)<span class="hljs-comment">//选择表单中的input元素</span>
$(<span class="hljs-string">'div:visible'</span>) <span class="hljs-comment">//选择可见的div元素</span>
$(<span class="hljs-string">'div:gt(2)'</span>) <span class="hljs-comment">// 选择所有的div元素，除了前三个</span>
$(<span class="hljs-string">'div:animated'</span>) <span class="hljs-comment">// 选择当前处于动画状态的div元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">jQuery链式操作</h3>
<p>jQuery的特点之一，就是选择页面的某一元素，把要对这个元素进行的操作，全都连接在一起，以链条的形式写出来，如：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'div'</span>).find(<span class="hljs-string">'h3'</span>).eq(<span class="hljs-number">2</span>).html(<span class="hljs-string">'hello'</span>);

<span class="hljs-comment">//可以分解成下面的样子</span>

$(<span class="hljs-string">'div'</span>)<span class="hljs-comment">//找到div元素</span>
.find(<span class="hljs-string">'h3'</span>)<span class="hljs-comment">//在div元素里选择其中的h3元素</span>
.eq(<span class="hljs-number">2</span>)选择第三个h3元素
.html(<span class="hljs-string">'Hello'</span>)<span class="hljs-comment">//将它的内容改为Hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">jQuery创建元素</h3>
<p>创建元素如果是原生JS代码，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'元素'</span>)<span class="hljs-comment">//创建元素</span>
<span class="hljs-built_in">document</span>.body.append(element)<span class="hljs-comment">//将创建的元素添加进body</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样看起来很长，而jQuery的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> element = $(<span class="hljs-string">'<元素>内容</元素>'</span>)<span class="hljs-comment">//创建元素</span>
$(<span class="hljs-string">'body'</span>).append(element)<span class="hljs-comment">//将创建的元素添加进body</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比下来jQuery十分的简洁。</p>
<h3 data-id="heading-3">jQuery移动元素</h3>
<p>可以操作文档，使文档里的某一元素移动到指定的位置，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//第一种</span>
$(<span class="hljs-string">'div'</span>).inserAfter($(<span class="hljs-string">'p'</span>))
$(<span class="hljs-string">'div'</span>).inserBefore($(<span class="hljs-string">'p'</span>))
<span class="hljs-comment">//第二种</span>
$(<span class="hljs-string">'p'</span>).after($(<span class="hljs-string">'div'</span>))
$(<span class="hljs-string">'p'</span>).Before($(<span class="hljs-string">'div'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这两种看起来差不多，但差别在于，根据链式操作，就可以知道第一种返回的对象是div元素，第二种返回的对象是p元素。</p>
<p>还有 <code>appendTo()</code> 、 <code>prependTo()</code> 、 <code>append()</code> 和 <code>prepend()</code> 这四种和上面的差不多。</p>
<h3 data-id="heading-4">jQuery修改元素属性</h3>
<p>jquery修改元素属性一般是 <code>attr()</code> 和 <code>removeAttr()</code></p>
<p>html如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>DOM-obj<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://bilibili.com"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"aid"</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"a标签的title属性值"</span>></span>点我<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是原生JS代码，修改元素属性如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> aNode = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'aid'</span>);
aNode.setAttribute(<span class="hljs-string">'href'</span>,<span class="hljs-string">'http://xiedaimala.com'</span>); <span class="hljs-comment">// 设置元素的href属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而jQuery如下：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#aid'</span>).attr(<span class="hljs-string">'href'</span>,<span class="hljs-string">'http://xiedaimala.com'</span>)
$(<span class="hljs-string">'#aid'</span>).attr(<span class="hljs-string">'href'</span>)<span class="hljs-comment">//如果没有第二个值，就会返回该属性的值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>甚至还可以一次性设置多个属性：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#aid'</span>).attr(&#123;<span class="hljs-string">'href'</span>:<span class="hljs-string">'http://xiedaimala.com'</span>,<span class="hljs-string">'title'</span>:<span class="hljs-string">'hello world'</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然， <code>removeAttr()</code> 如字面一样，可以删除属性，如：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#aid'</span>).removeAttr(<span class="hljs-string">'href'</span>)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            