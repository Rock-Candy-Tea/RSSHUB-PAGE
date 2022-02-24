
---
title: '如何将WGCNA导出的基因共表达网络进行可视化（cytoscape软件的使用）'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/18922188-9c1fc328484b916f.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/18922188-9c1fc328484b916f.png'
---

<div>   
<p>WGCNA分析过程中，你可以得到edge和node的文件，里面有你某一个module里所有基因相互之间的connectivity的weight值，根据这些值你可以将它们之间的作用关系进行可视化，这里就需要用到一个软件，Cytoscape。</p>
<p>cytoscape软件下载网址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcytoscape.org%2F" target="_blank">https://cytoscape.org/</a><br>
下载方法相当简单，安装也相当简单。我用的是win10系统，这里不再赘述安装过程。（安装方法同安装微信/QQ）</p>
<p>先来看看我们的edge文件吧，它应该是一个csv文件（有些教程说需要node文件和edge文件，但实际上我认为只需要edge文件，因为node文件里只有基因名，而没有weight值）：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="605" data-height="246"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-9c1fc328484b916f.png" data-original-width="605" data-original-height="246" data-original-format="image/png" data-original-filesize="32157" src="https://upload-images.jianshu.io/upload_images/18922188-9c1fc328484b916f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这里我的基因list里有1014个基因，相互作用的connectivity有几十万个条，当然不可能将几十万条关系网都画出来，根本看不清，画出来就是一大坨，而且电脑有可能会挂。<strong>所以在使用cytoscape前，最好按照weight值进行排序，选取weight值在某一个范围内的来进行可视化。</strong>这里Source和target的意思是“某一个基因作用于另一个基因”。我选取的是weight值大于0.35的，因为最大也才是0.44。这里一共是800多个connectivity，实际上也很多了。（我感觉如果你想看清每一条edge，最多不能超过100条）</p>
<p>打开cytoscape后，是这样的界面：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1920" data-height="991"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-67502de23cbda566.png" data-original-width="1920" data-original-height="991" data-original-format="image/png" data-original-filesize="280692" src="https://upload-images.jianshu.io/upload_images/18922188-67502de23cbda566.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>点击File>>>Import>>>Network from File,然后选择你的edge文件。然后会弹出：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1102" data-height="576"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-113c3a0808979c03.png" data-original-width="1102" data-original-height="576" data-original-format="image/png" data-original-filesize="154704" src="https://upload-images.jianshu.io/upload_images/18922188-113c3a0808979c03.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果你的文件里Source,Target,Weight三列没有问题，这个过程并不会报错，然后点击OK。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1918" data-height="992"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-ef67d37009a2a9ba.png" data-original-width="1918" data-original-height="992" data-original-format="image/png" data-original-filesize="287321" src="https://upload-images.jianshu.io/upload_images/18922188-ef67d37009a2a9ba.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这时右上方会展示出你的网络图。这个网络图太难看了，我们需要把它优化一下（鼠标滚动可以放大缩小）。首先点击最左侧一栏的“Style”,然后在弹出的页面里点击“Default”旁边的箭头，可以选择不同的样式，目前这个蓝色框框太丑了：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1915" data-height="688"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-83a7169076980f43.png" data-original-width="1915" data-original-height="688" data-original-format="image/png" data-original-filesize="420646" src="https://upload-images.jianshu.io/upload_images/18922188-83a7169076980f43.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>然后在左边控制栏里：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="616" data-height="908"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-e9197463f8913b8d.png" data-original-width="616" data-original-height="908" data-original-format="image/png" data-original-filesize="133278" src="https://upload-images.jianshu.io/upload_images/18922188-e9197463f8913b8d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>比如我选择了“Gradient1”的模板样式，然后调整了node的颜色、渐变的模式（放射渐变还是线性渐变）、背景颜色调成白色（原来是黑色），还有基因label的文字大小：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1920" data-height="1023"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-2933b4570a3c3e4f.png" data-original-width="1920" data-original-height="1023" data-original-format="image/png" data-original-filesize="606886" src="https://upload-images.jianshu.io/upload_images/18922188-2933b4570a3c3e4f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>那么你的weight值该怎么进行可视化呢？</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="610" data-height="843"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-f5d6c4fbc844db7f.png" data-original-width="610" data-original-height="843" data-original-format="image/png" data-original-filesize="162134" src="https://upload-images.jianshu.io/upload_images/18922188-f5d6c4fbc844db7f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>调整后：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1918" data-height="797"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-71ad9307db3f7ba4.png" data-original-width="1918" data-original-height="797" data-original-format="image/png" data-original-filesize="553502" src="https://upload-images.jianshu.io/upload_images/18922188-71ad9307db3f7ba4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">这样一来，你的edge线就有粗有细了</div>
</div>
<p>调整基本的颜色和形状外，你还可以将你的source node和target node展示出来，即展示这些相互作用是哪些基因作用于哪些基因：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="571" data-height="727"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-aa6e40e4c7c7f5ef.png" data-original-width="571" data-original-height="727" data-original-format="image/png" data-original-filesize="123500" src="https://upload-images.jianshu.io/upload_images/18922188-aa6e40e4c7c7f5ef.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>调整后：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1920" data-height="671"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-8904298c7fcd4896.png" data-original-width="1920" data-original-height="671" data-original-format="image/png" data-original-filesize="499893" src="https://upload-images.jianshu.io/upload_images/18922188-8904298c7fcd4896.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这样一来，你的edge的粗细不一样了，而且还表明了从哪些基因作用于哪些基因。</p>
<p>那么如果你对其中某一个基因感兴趣，想把它用不同的颜色展示出来，该怎么做呢？首先你要点击你想改颜色的node,然后你可以在左边node栏里：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="585" data-height="847"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-9d1300c12463f1cc.png" data-original-width="585" data-original-height="847" data-original-format="image/png" data-original-filesize="98919" src="https://upload-images.jianshu.io/upload_images/18922188-9d1300c12463f1cc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>更改后，你会发现你选择的node的颜色不一样了：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1919" data-height="707"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-0c93868325a58f0d.png" data-original-width="1919" data-original-height="707" data-original-format="image/png" data-original-filesize="580936" src="https://upload-images.jianshu.io/upload_images/18922188-0c93868325a58f0d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>到这一步你会发现，我有100多个基因，800多条connectivity，我怎么能知道每一个node都对应了多少条connectivity?你可以在你原始的edge文件里自己去计算，当然很麻烦，那还有一个方法可以让你直接获得这个数据，点击最上面的工具栏“Layout”,选择“degree sorted circle layout”，然后你会发现页面右下角会出现：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1311" data-height="371"><img data-original-src="//upload-images.jianshu.io/upload_images/18922188-4e78c0d3b1c2934e.png" data-original-width="1311" data-original-height="371" data-original-format="image/png" data-original-filesize="72922" src="https://upload-images.jianshu.io/upload_images/18922188-4e78c0d3b1c2934e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>你可以点击“degree”上面的黑色文件似的向外的箭头，那是“export”，就会得到一个表格，里面有所有的基因和它对应的edge数量。</p>
<p><strong>最后不要忘记保存你的图：File>>>Export>>>Network to File/Network to image.</strong></p>
  
</div>
            