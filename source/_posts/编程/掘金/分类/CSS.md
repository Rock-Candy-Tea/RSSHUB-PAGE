
---
title: 'CSS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4477'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:41:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=4477'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是CSS</h1>
<p>Cascading Style Sheets简称CSS,层叠样式表是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化
CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。</p>
<h1 data-id="heading-1">诞生历程</h1>
<p>从HTML被发明开始，样式就以各种形式存在。不同的浏览器结合它们各自的样式语言为用户提供页面效果的控制。最初的HTML只包含很少的显示属性。
随着HTML的成长，为了满足页面设计者的要求，HTML添加了很多显示功能。但是随着这些功能的增加，HTML变的越来越杂乱，而且HTML页面也越来越臃肿。于是CSS便诞生了。
1994年哈坤·利提出了CSS的最初建议。而当时伯特·波斯（Bert Bos）正在设计一个名为Argo的浏览器，于是他们决定一起设计CSS。
其实当时在互联网界已经有过一些统一样式表语言的建议了，但CSS是第一个含有“层叠”丰意的样式表语言。在CSS中，一个文件的样式可以从其他的样式表中继承。读者在有些地方可以使用他自己更喜欢的样式，在其他地方则继承或“层叠”作者的样式。这种层叠的方式使作者和读者都可以灵活地加入自己的设计，混合每个人的爱好。<br>
哈坤于1994年在芝加哥的一次会议上第一次提出了CSS的建议，1995年的www网络会议上CSS又一次被提出，博斯演示了Argo浏览器支持CSS的例子，哈肯也展示了支持CSS的Arena浏览器。
同年，W3C组织（World WideWeb Consortium）成立，CSS的创作成员全部成为了W3C的工作小组并且全力以赴负责研发CSS标准，层叠样式表的开发终于走上正轨。有越来越多的成员参与其中，例如微软公司的托马斯·莱尔顿(Thomas Reaxdon)，他的努力最终令Internet Explorer浏览器支持CSS标准。哈坤、波斯和其他一些人是这个项目的主要技术负责人。1996年底，CSS初稿已经完成，同年12月，层叠样式表的第一份正式标准（Cascading style Sheets Level 1）完成，成为w3c的推荐标准。<br>
1997年初，W3C组织负责CSS的工作组开始讨论第一版中没有涉及到的问题。其讨论结果组成了1998年5月出版的CSS规范第二版。</p>
<h2 data-id="heading-2">特点</h2>
<h3 data-id="heading-3">1. 样式丰富</h3>
<h3 data-id="heading-4">2. 多页应用</h3>
<p>CSS样式表理论上不属于任何页面文件，在任何页面文件中都可以将其引用</p>
<h3 data-id="heading-5">3. 层叠</h3>
<p>层叠就是对一个元素多次设置同一个样式，这将使用最后一次设置的属性值。后来定义的样式将对前面的样式设置进行重写，在浏览器中看到的将是最后面设置的样式效果。</p>
<h3 data-id="heading-6">4. 页面压缩</h3>
<p>在使用HTML定义页面效果的网站中，往往需要大量或重复的表格和font元素形成各种规格的文字样式，这样做的后果就是会产生大量的HTML标签，从而使页面文件的大小增加。而将样式的声明单独放到CSS样式表中，可以大大的减小页面的体积，这样在加载页面时使用的时间也会大大的减少。另外，CSS样式表的复用更大程度的缩减了页面的体积，减少下载的时间。</p>
<h2 data-id="heading-7">CSS</h2>
<h3 data-id="heading-8">一、选择器</h3>
<h4 data-id="heading-9">通用选择器：*</h4>
<p>允许您毫无例外地选择所有标签。这个选择器看似毫无意义，但下面我们将看到，通过将其与其他选择器结合使用，它会很有用。因此，以下规则将应用于整个页面，以定义所有元素的文本大小，包括标题（默认情况下具有较大的大小）：</p>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">类型选择器：balise</h4>
<p>正如我们在上面看到的，指出标记的名称使您可以将规则限制为单一类型的标记。因此，要将页面上的所有链接（“ a”标签）涂成蓝色，您可以按照以下示例操作：</p>
<pre><code class="copyable">a &#123;
  color: blue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">后代选择器： balise_mère  balise_descendante</h4>
<p>简单空间也是一种选择器。要将样式限制为页面特定区域中包含的标签，可以使用此选择器。它将仅选择名称为“ beacon_descendante”且包含在“ beacon_mere”中的信标。无论是女孩子标签，孙女标签，孙女标签，标签...好吧，我想您都明白了！请注意，该样式将应用于“ descendant_bags”标签。因此，以下CSS代码将仅选择其他<li>标签中包含的<li>标签。从HTML教程中可以看出，只有子列表的行而不是主列表的行：</p>
<pre><code class="copyable">li li &#123;
  font-size: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">子选择器： balise_mère > balise_fille</h4>
<p>如果您希望规则仅应用于直接子标记，则必须使用“>”选择器。例如，您想在段落内设置图像标签的样式，但如果它在链接内，则不希望设置样式。以下示例代码会将段落中的所有图像移到页面的右侧（例如杂志文章中的插图），但将图像保留在链接内的位置（例如代表ZIP文件的小图像或其他图像）：</p>
<pre><code class="copyable">p > img &#123;
  float: right;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">邻接选择器： balise + balise_suivant_immediatement</h4>
<p>极少见的是，有时您希望为标签赋予一种样式，但前提是该样式必须先于另一个标签。因此，让我们想象一下，您的Web页面由h1标题，后面的介绍性段落，其余部分（标题，段落...）组成。您要斜体页面的介绍性段落。这是您可以执行的操作：</p>
<pre><code class="copyable">h1 + p &#123;
  font-style: italic;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><h1>Titre de la page</h1>
// id = change的p生效斜体样式
<p id='change'>Paragraphe d'introduction concerné par le code CSS ci-dessus, car il est juste après le titre h1.</li>
<h2>Titre du premire chapitre</h1>
<p>Paragraphe non concerné par le code CSS ci-dessus, car il est précédé d'un élément h2.</li>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">选择器分组： sélecteur_1, sélecteur_2</h4>
<p>有时您想将相同的样式应用于多个标签或多个选择器。例如，将所有标题的背景颜色定义为必须为灰色，将文本的颜色定义为必须为蓝色。而不是这样做：</p>
<pre><code class="copyable">h1 &#123;
  background-color: gray;
  color: navy;
&#125;

h2 &#123;
  background-color: gray;
  color: navy;
&#125;

h3 &#123;
  background-color: gray;
  color: navy;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取而代之的是，您可以用逗号分隔标签（通常是选择器）的名称，以将样式定义分组在一起，这样可以避免代码重复。因此，将来您要修改CSS代码时，只需在一个地方进行修改，而不必忘记更改以下规则之一：</p>
<pre><code class="copyable">h1, h2, h3 &#123;
  background-color: gray;
  color: navy;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">类选择器： .classe</h4>
<p>现在，您可以根据其含义将样式分配给某些HTML标记。但是通常您需要更多的控制权，才能更精细地选择标签。您还需要为某些标签定义新的含义，当然还要以不同的方式设置它们的样式。每个HTML标记都可以接收一个“类”属性，您可以在其中输入您选择的名称。它仅对您有意义，并允许您使用CSS样式表进行链接。以下是带有类标记的一些示例：</p>
<pre><code class="copyable"><p      class="introduction"> ... </p>      
<div    class="encadre">      ... </div> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将类别分配给HTML标记后，就可以轻松格式化它们。只需使用“.” 然后是类名。因此，以下是如何快速设置上面刚刚看到的类的样式的方法：</p>
<pre><code class="copyable">.introduction &#123; font-style: italic;&#125;
.encadre      &#123; border: 1px solid black; background: cyan;&#125;
.css          &#123; background: lightgray;&#125;
.important    &#123; color: red;&#125;
.bouton       &#123; border: 1px solid gray; background: lightgray;&#125;
.complement   &#123; float: right;&#125;
.img-legende  &#123; float: right; border: 1px solid black;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在CSS代码中，可以将样式应用于元素的每个类。因此，让我们以“框架”类为例。现在，我们需要两种框：一个简单的信息框和一个警告框。每个框将保留“框”类，但还将分配第二个类来指定框的性质：“信息”或“注意”：</p>
<pre><code class="copyable"><div class="encadre information">
  Information :<br>
  Voici un texte d'information, faites-en ce que vous voulez !
</div>

<div class="encadre attention">
  Information :<br>
  Voici un texte d'information, faites-en ce que vous voulez !
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>视觉上，所有框都将具有黑色边框。但是，这两个信息框和警告框的突出之处在于它们的背景色：浅蓝色表示信息，浅红色表示警告：</p>
<pre><code class="copyable">.encadre &#123;
  border: 1px solid black;
&#125;

.information &#123;
  background: cyan;
&#125;

.attention &#123;
  background: pink;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">ID选择器： #id</h4>
<p>ID几乎与类相同，不同之处在于，ID只能分配给一个元素，也只能分配给一个元素。一个元素只能有一个ID（没有ID列表，用空格分隔）。例如，页面的页眉或页脚就是这种情况：每个HTML页面只能有一个。一页菜单的同上...
在HTML中，通过“ id”属性将ID分配给标签。在CSS中，我们使用#号和ID的名称来赋予其样式。
这是使用ID的HTML和CSS代码的示例。看起来像使用类的代码（在HTML中，“ id = ...”替换了“ class = ...”，而在CSS中，“＃”替换了“。”）：</p>
<pre><code class="copyable"><div id="entete">
  Hello World
</div>

<div id="pied">
  hello world
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">#entete &#123;
  border-bottom: 1px solid black;
&#125;

#pied &#123;
  border-top: 1px solid black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">属性选择器： balise[attribut]</h4>
<p>该选择器使您可以过滤具有特定属性的标签。例如，请记住<a>标记。根据其使用方式，它具有两个作用：</p>
<pre><code class="copyable"><a href="#article">Aller à l'article</a>
<h2><a name="article">Article</a></h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，如果要对链接应用样式，例如下划线，蓝色和鼠标悬停效果...，则可以对<a>标记进行样式设置。但是，锚点也将像链接一样成形，尽管它们不可单击。这就是为什么在HTML页面上，我建议您将锚标记的内容留空的原因。在上面的示例中，建议您在结束</a>标记后移动文本“ Article”。
但是，通过使用属性选择器，可以保持上面的HTML代码，并能够以不同的方式设置链接和锚的样式：</p>
<pre><code class="copyable">a[href] &#123; color: blue; text-decoration: underline; &#125;
a[name] &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还要注意，选择器的“标签”部分可以省略。因此，使用“ [name]”选择器，将选择具有“ name”属性的任何标签，而不仅仅是链接（“ a”标签）。在我们的示例中，我不建议您这样做，因为表单字段也具有name属性，因此样式也将适用于它们。</p>
<h4 data-id="heading-18">确切的属性值选择器： balise[attribut="valeur"]</h4>
<p>为了显示使用此选择器的示例，让我们使用dir属性。此属性具有默认值“ ltr”，表示“从左到右可读的文本”（从左到右）。可以将dir属性与值“ rtl”一起使用，以一种可以从右到左阅读的语言引入文本（“ rtl”代表“从右到左”）。然后，借助CSS中的此选择器，可以以不同的方式显示这些文本：</p>
<pre><code class="copyable"><p> <span dir="rtl">2345</span>6789</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">span[dir="rtl"] &#123;
  background-color: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">包含值的属性选择器： balise[attribut~="valeur"]</h4>
<p>允许您选择标签，其属性“ attribute”包含一个由白色字符（空格，制表符...）分隔的列表，并且其中一个元素等于“ value”。这样就可以模拟具有除“ class”以外的任何属性的类的操作。请记住，HTML元素可以有多个类，用空格隔开，例如“注意框”，“信息框”……因此，以下两行是等效的：</p>
<pre><code class="copyable">.cadre           &#123; ... &#125;
[class~="cadre"] &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，您可以在这两个选择器的前面放置标签名称，以进一步限制所选标签。例如：div.cadre和div[class~="cadre"]是等效的，并将选择器限制为具有“ frame”类的“ div”标签。</p>
<h4 data-id="heading-20">属性选择器以一个值开头： balise[attribut|="valeur"]</h4>
<p>用于选择标签，其属性“ attribute”包含一个由破折号分隔的列表，并且其第一个元素为“ value”。
这对于lang属性很有用，它可以包含以下代码，例如en-US（美国英语），en-GB（英国英语），fr-FR（法国法语），fr-CA（加拿大法语）， fr-BE（比利时法语）...以相同字母开头的语言看起来很相似，因此可以以相同的方式设置样式。示例，无论国家/地区如何，都以不同的方式设置英语和法语的样式：</p>
<pre><code class="copyable">[lang|="en"] &#123; ... &#125;
[lang|="fr"] &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">二、伪类和伪元素</h3>
<h4 data-id="heading-22">伪类</h4>
<p>存在DOM文档中，逻辑上存在但在文档树中却无须标识的“幽灵”分类</p>
<h4 data-id="heading-23">伪元素</h4>
<p>不存在在DOM文档中，是虚拟的元素，是创建新元素。代表某个元素的子元素，这个子元素虽然在逻辑上存在，但却并不实际存在于文档树中</p>
<h3 data-id="heading-24">三、选择优先级</h3>
<p>有一种计算方法可以使您始终确保知道选择器的特异性：</p>
<ul>
<li>a =如果选择器是一个“ style”属性而不是选择器，则为1；否则为0（在HTML中，元素的“ style”属性的值是样式表规则。选择器，所以a = 1，b = 0，c = 0和d = 0）；</li>
<li>b =计算选择器中ID属性的数量（尖锐数量）；</li>
<li>c =计算选择器中其他属性和伪类的数量（以句点开头的类，方括号中的属性，以冒号开头的伪类，而不是以冒号开头的伪元素）；</li>
<li>d =计算选择器中元素名称的数量（标签名称）。</li>
</ul>
<pre><code class="copyable">*              &#123; ... &#125; /* a=0 b=0 c=0 d=0 -> spécificité =    0 */
li             &#123; ... &#125; /* a=0 b=0 c=0 d=1 -> spécificité =    1 */
ul li          &#123; ... &#125; /* a=0 b=0 c=0 d=2 -> spécificité =    2 */
ul ol+li       &#123; ... &#125; /* a=0 b=0 c=0 d=3 -> spécificité =    3 */
h1 + *[rel=up] &#123; ... &#125; /* a=0 b=0 c=1 d=1 -> spécificité =   11 */
ul ol li.red   &#123; ... &#125; /* a=0 b=0 c=1 d=3 -> spécificité =   13 */
li.red.level   &#123; ... &#125; /* a=0 b=0 c=2 d=1 -> spécificité =   21 */
#x34y          &#123; ... &#125; /* a=0 b=1 c=0 d=0 -> spécificité =  100 */
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果两条CSS规则具有相同的特异性，则最后一条获胜。因此，可以在CSS文件甚至第二个CSS文件中进一步覆盖或重新定义规则。</p>
<h3 data-id="heading-25">四、值的类型</h3>
<h4 data-id="heading-26">长度和百分比</h4>
<p>首选相对单位，因为相对单位可以适应查看者（无论是否有视觉障碍）和外围设备（屏幕或印刷品），并禁止绝对单位（例如，除非直接为单个外围设备定义关系）。这些值可以是正数或负数（+/-），值0不需要指定单位。</p>
<ul>
<li>相对长度单位</li>
</ul>
<blockquote>
<ol>
<li>em：字体的高度（或父标签的高度，定义相同的大小时）</li>
<li>ex：小写x字符的高度（'x'）</li>
<li>px：像素大小（在屏幕和纸张上有所不同，但是按比例计算）</li>
</ol>
</blockquote>
<ul>
<li>绝对长度单位</li>
</ul>
<blockquote>
<ol>
<li>cm：厘米（1厘米= 10毫米）</li>
<li>mm：毫米</li>
<li>in：英寸（1英寸= 2.54厘米）</li>
<li>pt：点（1 pt = 1/72 in）</li>
<li>pc：picas（1pc = 12pt）</li>
</ol>
</blockquote>
<ul>
<li>百分比</li>
</ul>
<h4 data-id="heading-27">颜色</h4>
<ul>
<li>对应颜色其英文名称</li>
<li>16进制这种所谓的“ RGB”格式</li>
</ul>
<blockquote>
<ol>
<li>#rgb：如果两个“ r”相等，两个“ g”也相等，那么两个“ b”也可以缩短前面的表示法。保持相同的示例，可以将其编写为：＃0c0;</li>
<li>rgb(x,x,x)注意：如果您在掌握十六进制表示法时遇到问题，则可以使用该表示法在以10为基数的数字中写入数字。三个x是介于0和255之间（含0和255）的整数。然后将前面的示例写为rgb（0.204.0）;</li>
<li>rgb(y%,y%,y%)：最后，如果使用0到100之间的数字比使用0到255之间的数字更舒适，则可以使用此表示法。ys是介于0.0和100.0（含）之间的浮点数。示例：rgb（0％，80％，0％）。</li>
</ol>
</blockquote>
<h3 data-id="heading-28">五、盒子模型</h3>
<ul>
<li>width    ----------块内容的宽度</li>
<li>height   ---------块内容的高度</li>
<li>min-width ------块内容的最小宽度</li>
<li>min-height ------块内容的最小高度</li>
<li>max-width -------块内容的最大宽度</li>
<li>max-height ------块内容的最大高度</li>
<li>border-width -----边框宽</li>
<li>border-style -----边框样式</li>
<li>border-color -----边框颜色</li>
<li>border ----------边框属性：同时具备边框的三个属性才能生效border:1px #ffffff solid</li>
<li>border-top/bottom/left/right --边框精准控制</li>
<li>margin -----------外边距：上>右>下>左 或者 全部</li>
<li>margin-top/bottom/left/right --外边距精准控制</li>
<li>padding ----------内间距： 上>右>下>左 或者 全部</li>
<li>padding-top/bottom/left/right --内间距精准控制</li>
<li>background-color --背景颜色</li>
<li>background-image --背景图片background-image: url('images/fond.png');</li>
<li>background-repeat --背景图片不重复</li>
<li>background-size ----背景图片大小</li>
<li>background-position --背景图片位置</li>
<li>background-attachment -- 背景附着力此属性很少使用，默认值为scroll，可选fixed</li>
<li>background ------五个属性无序简写</li>
</ul>
<h3 data-id="heading-29">六、定位方式</h3>
<p>display</p>
<ul>
<li>flex: 弹性布局；</li>
<li>block : 将标签显示为一个块（在该块之前和之后经过一行）；</li>
<li>inline : 显示内联标签；</li>
<li>none : 不显示块，也不显示其子块（就像标记不存在一样）；</li>
<li>list-item : 此值的使用频率较低，它允许将标签显示为列表行（使该标签好像是<li>一样）</li>
</ul>
<p>overflow</p>
<ul>
<li>visible : 突出的内容是可见的；</li>
<li>hidden : 修剪超出块的内容；</li>
<li>scroll : 滚动条被添加到块中;</li>
<li>auto : 如果内容的大小大于块的大小，则添加一个或多个滚动条;</li>
</ul>
<p>visibility</p>
<ul>
<li>visible : 这是默认值，该块是可见的；</li>
<li>hidden : 该块是隐藏的，但与“ display：none;”不同，该块的位置是保留的。</li>
</ul>
<h3 data-id="heading-30">七、其他属性</h3>
<ul>
<li>字体font</li>
<li>鼠标cursor</li>
<li>阴影box-shadow</li>
<li>绝对相对position</li>
</ul>
<p>...</p>
<h2 data-id="heading-31">参考文献</h2>
<h6 data-id="heading-32">1. 祝红涛，张钦．CSS网络大讲堂：清华大学出版社，2013.05：4</h6>
<h6 data-id="heading-33">2. 维姆莱，波斯．CSS权威教程（第三版）：清华大学出版社，2009.1：第3页</h6></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            