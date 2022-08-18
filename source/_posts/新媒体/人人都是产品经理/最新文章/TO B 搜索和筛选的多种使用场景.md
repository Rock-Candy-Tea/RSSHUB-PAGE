
---
title: 'TO B 搜索和筛选的多种使用场景'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/f2C5fRuxH4hsZsqMz948.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 18 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/f2C5fRuxH4hsZsqMz948.jpg'
---

<div>   
<blockquote><p>
编辑导语：随着B端项目越来越普及，企业也逐渐意识到产品的视觉效果、功能的好用性及用户体验的友好性等等。本文作者通过自身在工作中的实战经验，分享了关于B端产品中的搜索及筛选的不同使用场景，一起来看一下吧。
</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5568682" src="https://image.woshipm.com/wp-files/2022/08/f2C5fRuxH4hsZsqMz948.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近B端一词在互联网中的呼声很高，对于B端和C端而言，面向的用户是不一样的，常用的硬件设备也有所区分，C端移动端偏多，B端则是网页端偏多，当然也会有移动端的B端项目。</p>
<p>我在B端行业中实战多年，也见证了B端产品在各个方面发生了很多的变化，比如从原本B端产品比较注重功能的实现，只要功能能使用，在页面的视觉上以及功能是否好用上都没有看得很重。</p>
<p>而现在随着B端项目越来越普及，企业也逐渐意识到产品的视觉效果、功能的好用性以及用户体验的友好性等等，多方面地考虑一个产品的实现，从多维度做好产品，使用户使用达到能用性、好用性、易用性的效果。</p>
<p>B端项目更多的是针对实际业务情况而展开设计和研发的，所以一个需求的制定是会提前与对应的客户讨论，一个需求的开发是需要多次确认需求后而进行的。定制化开发的需求，对于用户来说，自己也会有一个预期的结果；而对于企业研发的普遍使用的B端项目而言，需求是需要通过用户调研以及市场调研等多方面考量。</p>
<p>今天我将会通过自身在工作中的实战经验，分享关于B端产品中的搜索以及筛选的不同使用场景，看似简单的功能，实际上也并不简单，下面我们一起来看看吧！</p>
<h2 id="toc-1">一、搜索和筛选的定义</h2>
<p><strong>搜索是用户指定任意条件（文本、语音等），平台对此条件进行检索后，展示对应内容。</strong></p>
<p><strong>筛选是平台为用户提供指定条件，用户可以选择查看符合一类或多类条件下的内容。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/xwXTtjmkJcvzEd6BCfdl.jpeg" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、搜索的使用场景</h2>
<p>搜索功能一般来说是用户在自己有目标的情况下，知道想要查询的目标（准确的目标或者模糊的目标），通过输入文本关键词实现查询目标。搜索的样式基本一致，只是在交互上会略有不同，使用的场景有两类。</p>
<h3><strong>1. 使用场景：在特定的页面搜索</strong></h3>
<p>特定的页面指的是在摸一个模块加入搜索的功能，例如在数据列表页面加入搜索的功能，搜索的目标只在该模块该内容中进行搜索，搜索的信息具有局限性，当然也是更加准确的搜索用户想要的目标信息。</p>
<p><strong>案例分享：</strong></p>
<p>下图是一个关于部门管理的列表页面，此页面加入了搜索的功能，搜索是通过<strong>输入部门关键词，</strong>这里的搜索有限定输入特定的字段信息，对于列表中的字段类型会有很多，在搜索的时候，可以通过控制某个字段或者某几个字段的信息来展开搜索。</p>
<p><strong>交互场景01：</strong>搜索后面带有“搜索”按钮，代表输入关键词信息后，需要点击“搜索”按钮，列表中的数据才会发生变化，才会真正的搜索目标信息，这种情况对于列表数据多的情况下会采用。</p>
<p><strong>交互场景02：</strong>搜索只有一个文本输入框，没有按钮可点击，这样的搜索交互是通过输入关键词后，列表中的信息会根据输入的关键词实时查询，搜索结果更快更及时，这种交互一般对于数据信息比较少的情况下会比较友好，加载的速度更快。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/s0gPj9EbcoQBF7GEXKTZ.jpeg" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<h3><strong>2. 使用场景：全局搜索</strong></h3>
<p>对于系统中模块分类较多，所涉及到的内容比较全面的，B端系统也会选择全局搜索，全局搜索在C端很常见，只需要在全局搜索框中输入自己模糊的目标信息，系统会根据输入的关键信息搜索出各个模块所对应的目标字段，如果分类较多，界面还可以根据分类tab分别归类不同模块的内容。</p>
<p><strong>案例分享：</strong></p>
<p>下图是一个关于B端系统全局搜索的界面，需求是根据关键词搜索出所有权责清单中的事项，界面中搜索框作为显眼的模块，通过输入的关键词搜索出所有带有关键词的事项，事项分别处于不同的清单，采用标签区分，因为此项目中只对不同清单中的事项做搜索，所以没有采用tab标签的形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/UuAQR4GSVvEYwYeTLifn.jpeg" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p>带有tab分类的搜索结果案例也有很多，例如google、百度搜索，以及飞书里面的全文检索等等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/WLsyuFgmlVUuRGb7KAuj.png" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（google）</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/SRl7sx29fRAitofSBER8.png" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（飞书文档）</p>
<h2 id="toc-3">三、筛选的使用场景</h2>
<p>我们最常见的筛选是给出特定的条件，用户直接选择对应的条件即可实现筛选，也就是现在常用的<strong>普通筛选</strong>，但是随着B端业务的复杂性逐渐增强，简单的筛选已经无法满足现在复杂的业务需求了，后面开始引进<strong>高级筛选</strong>的功能，在不同的需求情况下会选择采用不同的筛选模式，以便于更好地实现功能，满足用户的不同需求。</p>
<h3><strong>1. 普通筛选</strong></h3>
<p>普通的筛选是直接给出固定的条件，用户只需要选择一个条件或者多个条件，实现数据筛选的目的。所给的条件是数据中一些特定的值，是用户高频筛选的值，客户也会提出对某类条件进行筛选的功能，在B端项目中，这些筛选条件客户本身是更熟悉需求的，所以这类条件一般由客户提供。</p>
<p><strong>案例分享：</strong></p>
<p>如下图是关于人员管理的数据列表页面，页面中有“部门”和“状态”两个筛选条件，是通过点击出现下拉框出现对应的条件的值，当选中对应的条件值，列表中就会出现对应的目标值，这里的筛选和搜索功能是一起使用的，当然也可以单独分开使用，也是需要根据实际业务场景区分搭配使用搜索和筛选的功能。</p>
<p>注意：搜索和筛选多种功能同时使用时，需要考虑所过滤后的数据是求并集还是交集的问题。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/Pyr0p1ZkFleEHumxc2zb.jpeg" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<h3><strong>2. 高级筛选</strong></h3>
<p>高级筛选是在基础筛选的基础上加入了自定义的功能，原理都是在特定的条件下选择目标值进行筛选，只是通过用户自定义需要添加的筛选的条件，这样的筛选方式更加灵活，可以满足很多复杂的筛选需求，并且一次开发，长久使用，后续新增筛选条件只需要在筛选中加入特定的条件即可，并且筛选的操作达到了一致性，操作位置集中管理，方便用户使用。</p>
<p><strong>案例分享：</strong></p>
<p>如下图（底部具体的清单详情页面我做了处理，不方便透露项目）在对应的功能模块添加一个筛选的按钮，点击筛选按钮出现设置筛选条件的下拉框，默认状态只有一个“添加条件”的按钮，点击“添加条件”上面会出现选择条件的框，会有不同的筛选值可选择，前后一一对应结果，且可以添加多个条件。</p>
<p>并且可选择|所选值包含与不包含的关系，在添加多个条件后，右上角有一个外加的筛选条件“符合以下——所有条件/任一条件”也就是对所设置的筛选的条件取值的关系，是选择取并集还是交集的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/Afe1IiaXmL0EyKpIw953.jpeg" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p>这类高级筛选的实际案例中也有很多，例如飞书里面的筛选、黑帕云里面的筛选等等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/KE2HpX1DCoIHjugWpF7D.png" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">(飞书)</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/XtoHrp5SSj6aMragm7qB.png" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">(飞书)</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="TO B 搜索和筛选的多种使用场景" src="https://image.woshipm.com/wp-files/2022/08/7HYDAKTrDIrmcxLq5uSm.png" alt="TO B 搜索和筛选的多种使用场景" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">(黑帕云)</p>
<h2 id="toc-4">四、总结</h2>
<p>在B端项目中，搜索和筛选基本上可以说是必不可少的功能，B端产品中大多数是对功能和数据的管理，数据一般会比较丰富，所以这两个功能常被使用。</p>
<p>随着B端业务的复杂性增强，传统的功能模式以及交互模式以及无法完全的满足现有的需求，所以需要在原来的基础上做更好的优化，使其更好的满足现有的需求，也是操作和管理更加简单，使开发更简单更容易维护。</p>
<p>以上是我对近期所做的项目中所遇到的搜索和筛选功能的总结与分享，希望对处于B端的设计小伙伴有所帮助，也希望大家指出文章中的不足之处，期待和大家一起学习进步！</p>
<p> </p>
<p>本文由 @设计小余 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5568408" data-author="1131797" data-avatar="https://image.woshipm.com/wp-files/2021/08/318nVsgz69UPnNMipSIh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            