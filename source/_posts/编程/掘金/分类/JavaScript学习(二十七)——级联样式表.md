
---
title: 'JavaScript学习(二十七)——级联样式表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a860572f14d4a8f857800d5f82bb000~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:36:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a860572f14d4a8f857800d5f82bb000~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p> </p>
<p><strong>目录</strong></p>
<p><a href="https://juejin.cn/post/6943136583826538509#%E6%A0%B7%E5%BC%8F%E8%A1%A8%E7%AE%80%E4%BB%8B">样式表简介</a></p>
<p><a href="https://juejin.cn/post/6943136583826538509#%E4%BB%80%E4%B9%88%E6%98%AFCSS">什么是CSS</a></p>
<p><a href="https://juejin.cn/post/6943136583826538509#CSS%E8%A7%84%E5%88%99">CSS规则</a></p>
<p><a href="https://juejin.cn/post/6943136583826538509#style%E5%AF%B9%E8%B1%A1">style对象</a></p>
<p><a href="https://juejin.cn/post/6943136583826538509#CSS%E7%9A%84%E7%BB%A7%E6%89%BF">CSS的继承</a></p>
<p><a href="https://juejin.cn/post/6943136583826538509#CSS%E7%BB%A7%E6%89%BF%E7%9A%84%E8%BF%90%E7%94%A8">CSS继承的运用</a></p>
<hr>
<p><strong>对于网页的设计者来说，对HTML语言不会感到陌生，但如果要让页面达到至加美现的效果， 仅使用HTML标记是不够的， 此时就需要在页面中引入CSS样HTML与CSS 的关系是“内容”与“形式”的关系，由HTML确定网页的内定，CSS来实现页面的表现形式。HTML与CSS的完美搭配使页面更加美观、大方、容易维护。</strong><br>
</p>
<h1 data-id="heading-0"><strong>样式表简介</strong></h1>
<p><strong>HTML网页包含网页内容及网页表现方式两个方面。</strong></p>
<p><strong>网页内容主要由显示的文字、图片、窗体元素(文本框、下拉列表框、单选按钮、复选框)组成。</strong></p>
<p><strong>网页表现方式包括 显示网页内容时所使用的颜色、字体、边框以及网页 内容的位置及尺寸等。CSS (网页样式表)就是用于设计和实现网页表现方式的一组描述或定义，具有以下特征:</strong></p>
<p><strong>(1)通过样式表示颜色、字体、背景色、边框及网页内容的位置、尺寸等属性。</strong></p>
<p><strong>(2)样式表由一系列样式组成。</strong></p>
<p><strong>(3)样式表在使用时，可以单独保存为外部样式表文件(扩展名为css)，也可在HTML文件中嵌入样式表(在<head></head>中使用<style></style>定义)，或者在HTML标记中直接设置样式表(使用style="..."的方式)。其中，外部样式表文件可有效地将网页内容与其表现方式分离，以方便修改网页的表现方式。在HTML标记中使用样式表时采用的是层叠式原则。</strong></p>
<p> </p>
<h1 data-id="heading-1"><strong>什么是CSS</strong></h1>
<p><strong>CSS是W3C协会为弥补HTML在显示属性设定上的不足而制定的一套扩展样式标准，其全称县 Cascading Style Sheet。CSS 标准中重新定义了HTML中原来的文字显示样式，增加了一些新概念，如类、层等，可以对文字层叠、定位等。所谓“层叠”，实际上就是将显示样式独立于显示的内容，进行分类管理，如分为字体样式、颜色样式等，需要使用样式的HTML文件进行套用。<br>
在CSS还没有引入到页面设计之前，传统的HTML语言要实现页面美化在设计上是十分麻烦的，例如，要设计页面中文字的样式，如果使用传统的HTML语句来设计页面，就不得不在每个需要设计的文字上都定义样式。</strong></p>
<p> </p>
<h1 data-id="heading-2"><strong>CSS规则</strong></h1>
<p><strong>在CSS样式表中包括3部分内容:选择符、属性和属性值。语法格式如下:<br>
选择符&#123;属性:属性值;&#125;</strong></p>
<p><strong>参数说明:<br>
选择符:又称选择器，是CSS中很重要的概念，所有HTML语言中的标记都是通过不同的CSS选择器进行控制的。<br>
属性:主要包括字体属性、文本属性、背景属性、布局属性、边界属性、列表项目属性、表格属性等内容。其中一些属性只有部分浏览器支持，因此使CSS属性的使用变得更加复杂。</strong></p>
<p><strong>属性值:为某属性的有效值。属性与属性值之间以“;”分隔。当有多个属性时，使用“,”分隔。</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a860572f14d4a8f857800d5f82bb000~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h1 data-id="heading-3">style对象</h1>
<p><strong>style对象是HTML对象的一个属性。style对象提供了一组对应于浏览器所支持的CSS样式的属性（如background、fontsize和bordercolor等）。每一个HTML对象都有一个style属性，可以使用该属性访问CSS样式属性。</strong></p>
<p><strong>内联样式使用sye对象属性直接为单个HTML元素指派应用的CSS样式，而使用style对象可以检查这些指派，并进行新的指派或更改已有的指派。要使用style对象，应该在HTML元素上使用style关键字。要获得内联样式的当前设置，应该在style 对象上使用对应的style对象的属性。</strong></p>
<p><strong>烟花效果：</strong><br>
</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"text/javascript"</span>> 
<span class="hljs-comment">//自定义变量及数组，并用数组来保存颜色值，在页面中添加多个层，设置其大小、颜色和初始位置</span>
<span class="hljs-keyword">var</span> col=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">'#ffffff'</span>,<span class="hljs-string">'#fff000'</span>,<span class="hljs-string">'#ffa000'</span>,<span class="hljs-string">'#ff00ff'</span>,<span class="hljs-string">'#00ff00'</span>,<span class="hljs-string">'#0000ff'</span>,<span class="hljs-string">'#ff0000'</span>);
<span class="hljs-keyword">var</span> p=<span class="hljs-string">'<div id="rearDiv" style="position:absolute;top:0px;left:0px">'</span>;
<span class="hljs-keyword">var</span> n=<span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">14</span>;i++)&#123;
n++;
<span class="hljs-keyword">if</span>(n=(col.length-<span class="hljs-number">1</span>)) n=<span class="hljs-number">0</span>;
p=p+<span class="hljs-string">'<div style="position:relative;width:1px;height:1px;background:'</span>+col[n]+<span class="hljs-string">';font-size:3px">.</div>'</span>;

&#125;
p=p+<span class="hljs-string">"</div>"</span>;
<span class="hljs-built_in">document</span>.write(p);
<span class="hljs-keyword">var</span> clrs=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">'#ff0000'</span>,<span class="hljs-string">'#00ff00'</span>,<span class="hljs-string">'#000aff'</span>,<span class="hljs-string">'#ff00ff'</span>,<span class="hljs-string">'#ffa500'</span>,<span class="hljs-string">'#ffff00'</span>,<span class="hljs-string">'#00ff00'</span>,<span class="hljs-string">'#ffffff'</span>,<span class="hljs-string">'#fffff0'</span>);
<span class="hljs-keyword">var</span> sclrs=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">'#ffa500'</span>,<span class="hljs-string">'#55ff66'</span>,<span class="hljs-string">'#AC9DFC'</span>,<span class="hljs-string">'#fff000'</span>,<span class="hljs-string">'#fffff0'</span>);
<span class="hljs-keyword">var</span> peepx;
<span class="hljs-keyword">var</span> peepy;
<span class="hljs-keyword">var</span> step=<span class="hljs-number">5</span>;
<span class="hljs-keyword">var</span> tallystep=<span class="hljs-number">0</span>;
<span class="hljs-keyword">var</span> backcolor=<span class="hljs-string">'ffa000'</span>;
<span class="hljs-keyword">var</span> mtop=<span class="hljs-number">250</span>;
<span class="hljs-keyword">var</span> mleft=<span class="hljs-number">250</span>;
<span class="hljs-comment">//自定义函数dissilient()，调用自定义函数enlarge()和reduce（），用于实现绽放的烟花效果</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dissilient</span>(<span class="hljs-params"></span>)</span>&#123;
peepy=<span class="hljs-built_in">window</span>.document.body.clientHeight/<span class="hljs-number">3</span>;
peepx=<span class="hljs-built_in">window</span>.document.body.clientWidth/<span class="hljs-number">8</span>;
enlarge();
tallystep+=step;
reduce();
t=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-string">"dissilient()"</span>,<span class="hljs-number">20</span>);
&#125;
<span class="hljs-comment">//自定义函数enlarge()，利用正弦值来实现烟花的绽放与缩小</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enlarge</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">for</span>(i=<span class="hljs-number">0</span>;i<rearDiv.all.length;i++)&#123;
<span class="hljs-keyword">var</span> c=<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random()*(clrs.length-<span class="hljs-number">1</span>));
<span class="hljs-keyword">if</span>(tallystep<<span class="hljs-number">90</span>)
rearDiv.all[i].style.background=backcolor;
<span class="hljs-keyword">if</span>(tallystep><span class="hljs-number">90</span>)
rearDiv.all[i].style.background=clrs[c];
rearDiv.all[i].style.top=mtop+peepy*<span class="hljs-built_in">Math</span>.sin((tallystep+i*<span class="hljs-number">5</span>)/<span class="hljs-number">3</span>)
*<span class="hljs-built_in">Math</span>.sin(<span class="hljs-number">550</span>+tallystep/<span class="hljs-number">100</span>);
rearDiv.all[i].style.left=mleft+peepy*<span class="hljs-built_in">Math</span>.cos((tallystep+i*<span class="hljs-number">5</span>)/<span class="hljs-number">3</span>)
*<span class="hljs-built_in">Math</span>.sin(<span class="hljs-number">550</span>+tallystep/<span class="hljs-number">100</span>);
&#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reduce</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">if</span>(tallystep==<span class="hljs-number">220</span>)&#123;
tallystep=-<span class="hljs-number">10</span>;
<span class="hljs-keyword">var</span> k=<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random()*(sclrs.length-<span class="hljs-number">1</span>));
backcolor=sclrs[k];
dtop=<span class="hljs-built_in">window</span>.document.body.clientHeight-<span class="hljs-number">250</span>;
dleft=peepx*<span class="hljs-number">3.5</span>;
mtop=<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random()*dtop);
mleft=<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random()*dleft);
<span class="hljs-built_in">document</span>.all.rearDiv.style.top=mtop+<span class="hljs-built_in">document</span>.body.scrollTop;
<span class="hljs-built_in">document</span>.all.rearDiv.style.left=mleft+<span class="hljs-built_in">document</span>.body.scrollLeft;
<span class="hljs-keyword">if</span>((mtop<<span class="hljs-number">20</span>)||(mleft<<span class="hljs-number">20</span>))&#123;
mtop+=<span class="hljs-number">90</span>;
mleft+=<span class="hljs-number">90</span>;
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>百叶窗：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"text/javascript"</span>> 
<span class="hljs-keyword">var</span> s=<span class="hljs-string">""</span>;
<span class="hljs-keyword">for</span>(i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">16</span>;i++)&#123;
s=s+<span class="hljs-string">'<div id="i'</span>+i+<span class="hljs-string">'" style="position:absolute; left:0px; top:0px;background-color:#0066ff;border:'</span>+<span class="hljs-string">"0.1px"</span>+<span class="hljs-string">''</span>+<span class="hljs-string">"soild"</span>+<span class="hljs-string">''</span>+<span class="hljs-string">"#0066ff"</span>+<span class="hljs-string">'"></div>'</span>;
&#125;
<span class="hljs-built_in">document</span>.write(s);
<span class="hljs-keyword">var</span> speed=<span class="hljs-number">30</span>;
<span class="hljs-keyword">var</span> temp=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
<span class="hljs-keyword">var</span> height=<span class="hljs-built_in">document</span>.body.clientHeight,top=<span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span>(i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">16</span>;i++)&#123;
temp[i]=<span class="hljs-built_in">eval</span>(<span class="hljs-string">"document.all.i"</span>+i+<span class="hljs-string">".style"</span>);
temp[i].width=<span class="hljs-built_in">document</span>.body.clientWidth/<span class="hljs-number">16</span>;
temp[i].height=<span class="hljs-built_in">document</span>.body.clientHeight;
temp[i].left=(i-<span class="hljs-number">1</span>)*<span class="hljs-built_in">parseInt</span>(temp[i].width);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kind</span>(<span class="hljs-params"></span>)</span>&#123;
height-=speed;
<span class="hljs-keyword">for</span>(i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">16</span>;i=i+<span class="hljs-number">2</span>)&#123;
temp[i].clip=<span class="hljs-string">"rect(0 auto+"</span>+height+<span class="hljs-string">" 0)"</span>;
&#125;
top+=speed;
<span class="hljs-keyword">for</span>(i=<span class="hljs-number">2</span>;i<=<span class="hljs-number">16</span>;i=i+<span class="hljs-number">2</span>)&#123;
temp[i].clip=<span class="hljs-string">"rect("</span>+top+<span class="hljs-string">" auto auto auto)"</span>;
&#125;
<span class="hljs-keyword">if</span>(height<=<span class="hljs-number">0</span>)
<span class="hljs-built_in">clearInterval</span>(tim);
&#125;
tim=<span class="hljs-built_in">setInterval</span>(<span class="hljs-string">"kind()"</span>,<span class="hljs-number">100</span>);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h1 data-id="heading-4">CSS的继承</h1>
<p><strong>对于面向对象的程序开发人员来说，对于继承这一概念肯定不会感到陌生， CSS语言中的继承概念并不像C++和Java语言那样复杂，简单地说，就是将所有HTML标记看作是一个容器， 定义在公容器上的CSS样式会自动加载到子级容器中。</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863baa3e0b2b4da29b96238ce91b85f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">CSS继承的运用</h2>
<p><strong>了解了HTML页面的继承关系后，掌握CSS的继承关系就很简单了。CSS样式中的继承关是子标记会维承父标记定义的样式，并且可以在父标记样式的基础上加以修改，这样会产生新的程系指的而子标记的样式风格不会影响到父标记。<br>
CSS继承关系的灵活运用可大大缩减代码的编写量。</strong><br>
</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            