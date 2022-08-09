
---
title: 'DeepFake换脸诈骗怎么破？让他侧个身'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220809/9f8a1877-6010-4f43-8bb0-189536eb7f95.gif'
author: 快科技（原驱动之家）
comments: false
date: Tue, 09 Aug 2022 19:00:00 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220809/9f8a1877-6010-4f43-8bb0-189536eb7f95.gif'
---

<div>   
<p>DeepFake被用到了电信诈骗里，该怎么破？</p>
<p>让他转过头，看看他的侧脸就好了。</p>
<p style="text-align: center"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="492" src="https://img1.mydrivers.com/img/20220809/9f8a1877-6010-4f43-8bb0-189536eb7f95.gif" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>DeepFake一直以来都存在着这样一个漏洞：当伪造的人脸完全侧着（转90°）时，真实性就会急剧下降。</p>
<p>为什么会出现这样的结果呢？</p>
<p>外网有这么一篇文章，解析了为什么在侧脸的情况下，面部伪造的效果大打折扣。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/1467a51f-fb2d-46c5-bb18-4f27fa868f5b.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="89" src="https://img1.mydrivers.com/img/20220809/S1467a51f-fb2d-46c5-bb18-4f27fa868f5b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>侧脸失真的原因</p>
<p>横向限制</p>
<p>使用DeepFake换脸，当人脸是侧角度时，真实性会急剧下降。</p>
<p>这是因为大多数基于2D的面部对齐算法，视捕捉到侧视图的特征点数量仅为主视图的50%-60%。</p>
<p>以“Joint Multi-view Face Alignment in the Wild”中的Multi-view Hourglass面部对齐模型为例。</p>
<p>通过从面部识别特征点，以此为学习数据来训练模型。</p>
<p>从图中可以看出，正面对齐时识别到68个特征点数量，而在侧面对齐时，仅仅识别到39个特征点数量。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/b80732ea-62fa-4194-a33d-92677232df2a.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="429" src="https://img1.mydrivers.com/img/20220809/Sb80732ea-62fa-4194-a33d-92677232df2a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>侧面轮廓视图隐藏了50%特征点，这不仅会妨碍识别，还会干扰训练的准确性以及后续人脸的合成。</p>
<p>DeepFake专家Siwei Lyu博士表示：</p>
<p>对于当前的DeepFake技术来说，侧脸确实是一个大问题。面部对齐网络（facial alignment network）对于正面效果非常好，但对于侧面效果不太好。这些算法有一个基本的限制：如果你只覆盖你的脸的一部分，对齐机制就可以很好地工作，并且在这种情况下非常强大，但是当你转身时，超过一半的特征点丢失了。</p>
<p>普通人影像资料“沙漠”</p>
<p>换脸要达到比较逼真的效果，还得经过大量的训练，这意味着需要有足够的训练数据。</p>
<p>外网就有人通过训练大量的数据，将杰瑞·宋飞人脸替换到到《低俗小说》(1994) 中的场景中。</p>
<p>获得的侧脸图像也很难看出破绽：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/cab21f19-1432-45b6-89b0-349567ca5e29.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="260" src="https://img1.mydrivers.com/img/20220809/Scab21f19-1432-45b6-89b0-349567ca5e29.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但是达到如此逼真的效果，是经过了大量数据的训练，在上述这个例子中，电视节目“Seinfeld”就为此次训练提供了长达66个小时的可用镜头。</p>
<p>而相比之下，除了电影演员之外，普通人的影像资料都少之又少，并且在平时拍照记录时，很少有人会记录完全呈90°的侧脸照。</p>
<p>因此，通过DeepFake伪造的人脸很轻易就在侧脸时露出破绽。</p>
<p>也有网友在Hacker News上调侃道：</p>
<p>最近去一家不知名的银行办了张卡，竟然需要我的侧身照，当时我还很疑惑，现在我终于知道为什么了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/d898790f-7d67-4baa-af16-1d9747be6e0c.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="43" src="https://img1.mydrivers.com/img/20220809/Sd898790f-7d67-4baa-af16-1d9747be6e0c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>用手在面前晃动也可以识别伪造的脸</p>
<p>视频通话时判断对方是不是DeepFake伪造的，除了通过侧脸判断，还有一个小方法：用手在面前晃动。</p>
<p>如果是伪造的人脸，手与脸部图像的叠加可能会出现错乱，并且手在晃动过程中会出现延迟现象。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/fc330092-9148-4737-a23c-48d92b62c24c.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="264" src="https://img1.mydrivers.com/img/20220809/Sfc330092-9148-4737-a23c-48d92b62c24c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△在换脸寡姐和X教授时，手和面部叠加发生错乱</p>
<p>实时的DeepFake都会面临这样一个问题：需要将真实的遮挡物叠加到不真实的面部图像上，一般称这个操作为“遮罩”或“背景去除”。</p>
<p>并且，实时DeepFake模型需要能够根据要求随意执行抠图，达到可令人信服的水平。</p>
<p>但往往也会有很多混淆的遮挡物来影响“抠图”的过程，比如说具有人脸特征的遮挡物会给模型造成“困扰”，使其“抠图”过程很难进行。</p>
<p>用手在伪造的脸前晃动，遮挡物的快速移动会给“抠图”带来很大的困难，从而造成很大的延迟，并且会影响叠加的质量。</p>
<p>One More Thing</p>
<p>换脸犯罪并不遥远，已经有媒体报道过有嫌疑犯通过DeepFake换脸进行IT工作的远程面试，以试图侵入公司，获取他们的客户或财务数据，以及企业IT数据和专业信息等。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220809/fefa9870-6840-4a23-b003-627822d68b9a.png" target="_blank"><img alt="DeepFake换脸诈骗怎么破？让他侧个身" h="120" src="https://img1.mydrivers.com/img/20220809/Sfefa9870-6840-4a23-b003-627822d68b9a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>美国联邦调查局（FBI）曾致函其互联网犯罪投诉中心，称收到过多起投诉，有人利用窃取的信息和深度伪造的视频、语音申请远程技术工作。</p>
<p>在联邦机构5月份报告中描述的案例中，一些换脸嫌疑人通过几层空壳公司进行操作，这使得识别他们的身份变得更加困难。</p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：若风</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/huanlian.htm">换脸</a><a href="https://news.mydrivers.com/tag/zhapian.htm">诈骗</a><a href="https://news.mydrivers.com/tag/ai.htm">AI</a>  </p>
        
</div>
            