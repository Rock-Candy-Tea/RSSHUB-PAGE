
---
title: '谷歌重磅AR功能来袭，融合街景海量数据，目标打造世界级AR体验'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220512/v2_0cd10fa4cd384345a88cce2442c56fda_img_000'
author: 36kr
comments: false
date: Thu, 12 May 2022 10:18:37 GMT
thumbnail: 'https://img.36krcdn.com/20220512/v2_0cd10fa4cd384345a88cce2442c56fda_img_000'
---

<div>   
<p class="image-wrapper"><img data-img-size-val="800,438" src="https://img.36krcdn.com/20220512/v2_0cd10fa4cd384345a88cce2442c56fda_img_000" referrerpolicy="no-referrer"></p> 
<p>近两年，谷歌在AR业务上动作频繁，不仅为谷歌地图、谷歌搜索推出AR功能，还收购了AR显示技术厂商Raxium、从微软和Meta挖角AR/VR人才，还有传闻称谷歌重组的实验室中有半数人在研发代号Project Iris的AR头显。</p> 
<p>如果说，这一切是谷歌为再一次发布AR硬件产品做准备，那么其AR平台ARCore的动向则同样值得关注。目前，谷歌和苹果分别拥有市面上最主流的两大AR平台：ARCore和ARKit。尽管这两家公司在AR研发的公开/秘密动作不断，但ARCore和ARKit平台在近两年的新内容逐渐减少，值得关注的大更新较少。唯一有看点的是ARKit支持LiDAR传感器，该功能提升了3D定位效果，为房间级AR体验带来可能。</p> 
<p>谷歌作为追随者，近两年对于ARCore的更新也比较缓慢。值得注意的是，今年谷歌举办了一场“含AR量”比往年更高的I/O大会，带来多项AR相关更新和展示，包括重磅功能：ARCore Geospatial API，可向AR开发者开放Live View AR定位技术，目的是推动AR室内外导航、LBS AR游戏等丰富的应用场景。除此之外，还公布了谷歌地图的“沉浸视图模式”、Google Lens多重搜索的本地关联模式，展示了AR眼镜在实时翻译场景的用途。</p> 
<h2>Geospatial API重磅发布</h2> 
<p>近年来，LBS AR技术持续发展，应用场景越来越丰富，不再局限于《精灵宝可梦Go》等游戏场景，还可以用在互动艺术展、数字孪生、AR地图、培训指导等场景。早期的AR应用形式主要是独立的内容，由于缺乏对物理环境的3D感知、持续的空间锚定等功能，几乎不可能支持多人AR共享玩法。而在Niantic等公司推动下，构建大规模基于地理位置的3D地图逐渐成为可能，为更优质的LBS AR提供底层技术。</p> 
<p class="image-wrapper"><img data-img-size-val="800,428" src="https://img.36krcdn.com/20220512/v2_66d0e1ddd8134b4b89fd8a582f63e445_img_000" referrerpolicy="no-referrer"></p> 
<p>Niantic通过自家AR应用向用户收集物理环境数据，而谷歌的策略则是依托于谷歌地图、地球的大量数据，因此在构建全球3D视觉定位系统（VPS）方面同样具有强大的竞争力。过去，谷歌一直在谷歌地图中测试这项技术，推出了Live View AR导航等基于视觉定位的功能。而现在，谷歌将Live View技术进一步开放，结合强大的谷歌地图数据库，为室外VPS导航，游戏互动，LBS AR体验带来更多可能性。</p> 
<p>简单来讲，ARCore Geospatial API为开发者带来了Live View的底层技术，包括大规模云锚点功能，以及全球视觉定位系统的访问权限，可用于开发多人共享的AR应用。该技术基于谷歌地球3D模型数据和街景图像数据，原理是将数百亿张街景图像转换为支持VPS定位的3D点云，共提取了数万亿个3D数据。只需不到一秒时间，便可根据3D点云数据定位设备的位置和方向。</p> 
<p class="image-wrapper"><img data-img-size-val="600,338" src="https://img.36krcdn.com/20220512/v2_ba6314ef9f9e480896170e1a12a0028c_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Cloud Anchors本地映射</p> 
<p>在2019年时，谷歌曾推出一个基于地理位置的AR云锚点API：ARCore Cloud Anchors，同样可以在物理位置固定AR，Cloud Anchors却与Geospatial API有明显的区别。通常，ARCore的锚点功能需要在本地创建图像映射，然后再进行定位。相比之下，Geospatial API不仅支持本地3D映射，还通过经纬度和高度来锚定AR内容（覆盖全球超87个国家/地区）。</p> 
<p class="image-wrapper"><img data-img-size-val="400,225" src="https://img.36krcdn.com/20220512/v2_257d4c783d6f43edae1d64f5722a9340_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Geospatial API 3D点云定位</p> 
<p>意味着即使是非本地场景，开发者也无需到现场或扫描物理空间，就能准确定位AR，进而大幅节省LBS AR内容的开发时间和成本。同时，在任何街景地图覆盖的地方，用户都可以用手机相机扫描周围环境，并快速、准确的获取AR导航等内容。</p> 
<h2>将世界变成AR画布</h2> 
<p>据悉，ARCore平台已经支持数十亿台设备，是帮助开发者构建沉浸式AR体验的强大工具。而接下来，为了鼓励更多开发者利用Geospatial API开发AR内容，谷歌发出口号，邀请开发者“将世界变成自己的画布”，以构建全球规模的AR内容。</p> 
<p>谷歌表示：Geospatial API包含了谷歌地图15年来对于现实世界的探索，可帮助开发者构建更身临其境、内容更丰富、更实用的AR应用。</p> 
<p class="image-wrapper"><img data-img-size-val="250,511" src="https://img.36krcdn.com/20220512/v2_99ef82958ac640eabcfa86dd36f00e08_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Geospatial API案例</p> 
<p>目前，一些品牌和开发者已经开始采用该API，NBA、Snap、Lyft也是谷歌Geospatial API的早期合作伙伴，他们将谷歌AR定位技术应用于教育、娱乐、公共事业等场景。而共享电动车公司Bird和Lime利用AR导航来指导用户正确停放电动车/滑板车，而Telstra和埃森哲则利用AR来为体育迷/音乐会观众提供室内导航功能，帮助他们找到自己的座位、摊贩和洗手间。此外，<a class="project-link" data-id="1713119879703045" data-name="DOCO" data-logo="https://img.36krcdn.com/20200511/v2_63d520ddc4424fda8cc2db1b7e980605_img_000" data-refer-type="1" href="https://36kr.com/project/1713119879703045" target="_blank">DOCO</a>MO和Curiosity基于ARCore Geospatial API打造了一款交互式AR游戏。</p> 
<p class="image-wrapper"><img data-img-size-val="300,533" src="https://img.36krcdn.com/20220512/v2_056e35009fc742e3b097fec0a0617bee_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="250,545" src="https://img.36krcdn.com/20220512/v2_97087421d2b147ac9bf233d3e5276047_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Geospatial API案例</p> 
<p>除此之外，谷歌还希望更多开发者基于Geospatial API来为火车站、商场、机场等室内场景打造AR导航/地图。</p> 
<p>无独有偶，从谷歌独立出去的Niantic一直以来都在开发LBS AR游戏，而Niantic本月下旬的开发者大会上也将发布自己的VPS视觉定位系统。当然，我们猜想Niantic的VPS系统也有可能和谷歌合作，毕竟现在内嵌地图系统都是谷歌地图。</p> 
<p>AR云、VPS定位一直都是AR初创公司描述美<a class="project-link" data-id="1678382643426304" data-name="好未来" data-logo="https://img.36krcdn.com/20220331/v2_aa24b8d76e924dc59f39835efae5094c_img_000" data-refer-type="1" href="https://36kr.com/project/1678382643426304" target="_blank">好未来</a>的红海项目，很多初创公司都有描述相关业务，但现在很多公司很多公司都找不到影子，还活下来的也基本上看不到什么有效成果，难度可想而知。</p> 
<p>对谷歌这种掌握大量街景视觉的巨头来说，切入VPS视觉定位有着十足优势。谷歌此举，一方面是对众多初创公司的沉重打击，二是大家都可以基于这一开放的VPS平台展开更多业务。</p> 
<h2>沉浸视图模式</h2> 
<p>早在2021年，谷歌就公布3D地图计划，相比于谷歌地球、街景地图这种全景形式，3D地图观感更加立体，可从多个角度、近距离查看建筑、景点的内外部结构。</p> 
<p class="image-wrapper"><img data-img-size-val="300,169" src="https://img.36krcdn.com/20220512/v2_e9eee3819a93404aaa3390d2043626ba_img_000" referrerpolicy="no-referrer"></p> 
<p>在本届I/O大会上，谷歌正式发布3D地图模式：“Immersive View”（沉浸视图模式），为你在谷歌地图上提供一种探索城市、地标、餐厅、场馆、名胜古迹等地点的新方式。</p> 
<p class="image-wrapper"><img data-img-size-val="500,282" src="https://img.36krcdn.com/20220512/v2_48c0f4ca93754940b2e5b955065bea1f_img_000" referrerpolicy="no-referrer"></p> 
<p>据了解，谷歌的“沉浸视图模式”利用计算机视觉和AI技术开发，将街景和航拍图融合成视觉立体的地图模型，从谷歌官方展示图来看，该模式比传统街景地图更加沉浸、更具互动性，还特别加入一个“时间滑块”功能，允许你查看特定地区在一天中不同时间的外观变化，比如在黄昏时可以看到月光。在查看建筑内部时，“沉浸视图”也可以让你看到室内的大量细节和角度。</p> 
<p>谷歌表示：沉浸视图模式将于今年下旬在安卓和iOS系统推出，首发仅面向部分城市，包括洛杉矶、伦敦、纽约、旧金山和东京，未来还将陆续支持其他城市。</p> 
<p>可以想象，将2D地图升级为3D模型需要时间和成本，想要规模化并不容易。为此，谷歌早前就在探索基于NeRF-W的合成算法，根据2D图片合成逼真、连贯的3D视角，这项技术对于谷歌开发3D地图将起到关键作用。此前青亭网也曾报道过这项技术，包括其背后的原理和细节。</p> 
<h2>Google Lens功能优化</h2> 
<p>除了AR外，谷歌也看好视觉搜索的前景，认为它将成为未来搜索技术的关键部分，甚至可能比语音搜索、移动搜索等技术更加重要。谷歌表示：Google Lens用户平均每个月搜索的次数达80亿，是一年前的三倍。人们对于视觉搜索的需求是存在的，接下来要做的是深入研发，以寻找最有价值的应用场景。</p> 
<p class="image-wrapper"><img data-img-size-val="800,479" src="https://img.36krcdn.com/20220512/v2_ef7828d0629a440cb4d20b463751beee_img_000" referrerpolicy="no-referrer"></p> 
<p>为此，谷歌宣布扩展Google Lens智能镜头的“多重搜索”（multisearch）功能，为其加入“附近搜索”功能，意味着你可以将视觉搜索结果连接到附近的地点。这种更加智能的视觉搜索功能，未来可能与AR眼镜有很好的结合。</p> 
<p>据悉，多重搜索是一种同时用文本和图像来进行搜索的功能，简单来讲就是在视觉搜索基础上，可以进一步设定颜色、附近等关键词，来优化搜索结果。比如，当你看中一条连衣裙的款式，但是想要寻找另一种颜色，便可以利用多重搜索功能扫描这条裙子，然后再输入目标颜色来细化搜索结果。</p> 
<p>而新增的“附近搜索”功能指的是，当你用Google Lens搜索某家连锁餐馆时，可以进一步搜索“我附近”，这家餐馆离你最近的店。甚至，还可以拍摄零件来关联附近五金店，搜连衣裙匹配周围服装店，或是扫描食物照片搜索附近的餐馆菜单/外卖。</p> 
<p class="image-wrapper"><img data-img-size-val="800,439" src="https://img.36krcdn.com/20220512/v2_39e9e46a245645c386782452295035b1_img_000" referrerpolicy="no-referrer"></p> 
<p>除了购物等日常生活场景外，谷歌认为视觉搜索还可以解决社会上的一些问题，比如帮助人们学习环保，帮助救灾人员快速整理捐款等等。而相比于单纯的视觉搜索，多重搜索的好处是支持更复杂的搜索结果，搜索体验更智能。目前，谷歌还在研发在一张图像/场景中同时搜索多个对象的模式，比如扫描书架上的书后，便可查看关于各种书的信息等。随着视觉搜索越来越复杂、智能，其与AR眼镜结合的价值也越来越明显。</p> 
<p>实际上，在去年7月接受外媒GQ采访时，Google Lens产品经理Lou Wang就表示在AR眼镜中集成Lens功能是可行的，未来视觉搜索功能可以像语音搜索那样普及。尽管智能手机生命周期还很长，但如果用AR眼镜就能进行一些简单的视觉搜索，也许可以补充手机的功能，为用户带来更多便利。</p> 
<p class="image-wrapper"><img data-img-size-val="800,533" src="https://img.36krcdn.com/20220512/v2_42bfa9b2ab4049f79c89c91a41bb372c_img_000" referrerpolicy="no-referrer"></p> 
<p>在本届I/O大会上，尽管谷歌并未展示Google Lens在AR眼镜上运行的效果，但还是展示了AR眼镜的另一种场景：实时翻译，可以将自然语言转化为文字，帮助你和周围的人更流畅沟通。当然，目前这似乎只是一个应用概念，从前不久的报道来看，传闻中谷歌的Project Iris原型的体积类似于滑雪护目镜，因此未来谷歌能否在普通眼镜形态的AR硬件中实现强大的功能，令人非常期待。</p> 
<p>参考：</p> 
<p>https://developers.googleblog.com/2022/05/Make-the-world-your-canvas-ARCore-Geospatial-API.html?m=1</p> 
<p>https://blog.google/products/maps/three-maps-updates-io-2022/</p> 
<p class="editor-note">本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/3e-hoVglot1UrVHr6j6EYA">“青亭网”（ID:qingtinwang）</a>，编辑：Esther，36氪经授权发布。</p>  
</div>
            