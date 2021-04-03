
---
title: '基本CSS技巧，可当作面经'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5805'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 01:47:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5805'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">• 清除浮动的几种方式</h4>
<h6 data-id="heading-1">1.父级div定义 height</h6>
<ul>
<li>原理：父级div手动定义height，就解决了父级div无法自动获取到高度的问题。</li>
<li>优点：简单、代码少、容易掌握</li>
<li>缺点：只适合高度固定的布局，要给出精确的高度，如果高度和父级div不一样时，会产生问题</li>
</ul>
<h6 data-id="heading-2">2.结尾处加空div标签 clear:both</h6>
<ul>
<li>原理：添加一个空div，利用css提高的clear:both清除浮动，让父级div能自动获取到高度</li>
<li>优点：简单、代码少、浏览器支持好、不容易出现怪问题</li>
<li>缺点：不少初学者不理解原理；如果页面浮动布局多，就要增加很多空div，让人感觉很不好</li>
</ul>
<h6 data-id="heading-3">3，父级div定义 伪类:after 和 zoom</h6>
<ul>
<li>原理：IE8以上和非IE浏览器才支持:after，原理和方法2有点类似，zoom(IE转有属性)可解决ie6,ie7浮动问题</li>
<li>优点：浏览器支持好、不容易出现怪问题（目前：大型网站都有使用，如：腾迅，网易，新浪等等）</li>
<li>缺点：代码多、不少初学者不理解原理，要两句代码结合使用才能让主流浏览器都支持</li>
</ul>
<h6 data-id="heading-4">4，父级div定义 overflow:hidden</h6>
<ul>
<li>原理：必须定义width或zoom:1，同时不能定义height，使用overflow:hidden时，浏览器会自动检查浮动区域的高度</li>
<li>优点：简单、代码少、浏览器支持好</li>
<li>缺点：不能和position配合使用，因为超出的尺寸的会被隐藏。</li>
</ul>
<h4 data-id="heading-5">• css选择器有哪些，选择器的权重的优先级</h4>
<h6 data-id="heading-6">选择器类型</h6>
<pre><code class="copyable">1、ID#id
2、class.class
3、标签p
4、通用*
5、属性　　[type="text"]
6、伪类　　：hover
7、伪元素::first-line
8、子选择器、相邻选择器
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">权重计算规则</h6>
<pre><code class="copyable">1. 第一等：代表内联样式，如: style=””，权值为1000。
2. 第二等：代表ID选择器，如：#content，权值为0100。
3. 第三等：代表类，伪类和属性选择器，如.content，权值为0010。
4. 第四等：代表类型选择器和伪元素选择器，如div p，权值为0001。
5. 通配符、子选择器、相邻选择器等的。如*、>、+,权值为0000。
6. 继承的样式没有权值。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">•  解释css sprites ，如何使用？</h4>
<p>CSS Sprites其实就是把网页中一些背景图片整合到一张图片文件中，再利用CSS的“background-image”，“background- repeat”，“background-position”的组合进行背景定位，background-position可以用数字能精确的定位出背景图片的位置。</p>
<p>CSS Sprites为一些大型的网站节约了带宽，让提高了用户的加载速度和用户体验，不需要加载更多的图片</p>
<h6 data-id="heading-9">• 隐藏元素的方法</h6>
<h6 data-id="heading-10"></h6>
<pre><code class="copyable">1. visibivisibility: hidden 隐藏仍占空间
2. opacity: 0 透明 仍占空间
3. position: absolute;
left: -1000;
top: -9000;  在视口不可见，仍占空间
4. display: none; 隐藏，不占空间
5. reansform: scale(0) 缩小到不可见，原来位置被保留
6. H5 的hidden attribute <p hidden></p> =display:none
7. height:0;
overflow: hidden; 无高度，位置保留
8. filter: blur(0) 模糊度=0
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-11">• css3一个冒号和两个冒号的区别</h6>
<h6 data-id="heading-12"></h6>
<p>单冒号(:)用于CSS3伪类,双冒号(::)用于CSS3伪元素，目的是区分伪类和伪元素，css2前无区分，全都是单冒号(:)，对于CSS2之前已有的伪元素，比如:before，单冒号和双冒号的写法::before作用是一样的。</p>
<h6 data-id="heading-13">• 列举所有的伪元素</h6>
<pre><code class="copyable">:before :after  :first-line  :first-letter
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">• 所有伪类</h6>
<pre><code class="copyable">:active向被激活的元素添加样式。
:focus向拥有键盘输入焦点的元素添加样式。
:hover当鼠标悬浮在元素上方时，向元素添加样式。
:link向未被访问的链接添加样式。
:visited向已被访问的链接添加样式。
:first-child向元素的第一个子元素添加样式。
:lang
:last-child
:nth-child(n/odd/even)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">• css的link和import区别</h4>
<p>有4种方式可以在 html 中引入 css。分别为：内联方式、嵌入方式、链接方式、导入方式，其中链接方式使用link引入，导入方式使用import引入。</p>
<h6 data-id="heading-16">link和import两者都是外部引用CSS的方式，但是存在一定的区别：</h6>
<ol>
<li>区别1：link是Xhtml标签，除了加载CSS外，还可以定义RSS等其他事务；@import属于CSS范畴，只能加载CSS。</li>
<li>区别2：link引用CSS时，在页面载入时同时加载；@import需要页面网页完全载入以后加载（不阻塞）。</li>
<li>区别3：link是XHTML标签，无兼容问题；@import是在CSS2.1提出的，低版本的浏览器不支持。</li>
<li>区别4：link支持使用JavaScript控制DOM去改变样式；而@import不支持。</li>
</ol>
<h4 data-id="heading-17">• div+css显示两行或三行文字</h4>
<pre><code class="hljs language-js copyable" lang="js">display: -webkit-box;
-webkit-box-orient: vertical;
-webkit-line-clamp: <span class="hljs-number">3</span>; <span class="hljs-comment">//需要控制的文本行数</span>
overflow: hidden;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>适用范围：
因使用了WebKit的CSS扩展属性，该方法适用于WebKit浏览器及移动端。</p>
<h4 data-id="heading-18">margin重叠问题</h4>
<h6 data-id="heading-19">同向margin的重叠：</h6>
<p>1图片的margin-top与3图片的margin-top发生重叠，2图片的margin-bottom与3图片的margin-bottom发生重叠。这时候重叠之后的margin值由发生重叠两片的最大值决定；如果其中一个出现负值，则由最大的正边距减去绝对值最大的负边距，如果没有最大正边距，则由0减去绝对值最大的负边距。</p>
<p>解决同向重叠的方法：</p>
<ol>
<li>在最外层的div中加入overflow:hidden;zoom:1;</li>
<li>在最外层加入padding:1px; (但会影响整体样式的准确性）</li>
<li>在最外层加入：border:1px solid #cacbcc;</li>
</ol>
<h6 data-id="heading-20">异向重叠问题：</h6>
<p>1图片的margin-bottom与2图片的margin-top发生重叠，这时候重叠之后的margin值由发生重叠两图片的最大值的决定的。</p>
<p>解决异向重叠问题：</p>
<ul>
<li>float:left（只能解决IE6浏览器中的异向重叠问题，可以解决IE8以上、chorme、firefox、opera下的同向重叠问题）</li>
</ul>
<p> </p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            