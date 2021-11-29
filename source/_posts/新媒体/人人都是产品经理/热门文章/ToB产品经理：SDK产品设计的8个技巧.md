
---
title: 'ToB产品经理：SDK产品设计的8个技巧'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/Chg0Im5b4pwDbKYiYolW.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 08 Mar 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/Chg0Im5b4pwDbKYiYolW.jpg'
---

<div>   
<blockquote><p>SDK是TOB产品的一个重要组成部分，可以简单理解提供给程序员帮助他们创建软件。那么如何设计SDK产品，它又有什么设计技巧呢？本文将为大家揭晓。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-3482762 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/Chg0Im5b4pwDbKYiYolW.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>SDK是对很多非科班出身的产品经理而言是陌生的，但对于ToB产品领域，许许多多的ToB产品都需要面向公司级开发者提供自己的SDK产品。</p>
<p>当然，SDK首先是面向开发者的，所以称之为ToD产品更精确，但是从ToB产品的大范畴来说，SDK是ToB大产品范畴的一部分，所以在此划入大ToB产品的类别。</p>
<p>那么SDK是什么？SDK有什么设计套路吗？让我们一一来拆解。</p>
<h2 id="toc-1">一、SDK是什么？</h2>
<p>维基百科对SDK的定义：</p>
<blockquote><p>SDK：软件开发工具包（Software Development Kit, SDK）一般是一些被软件工程师用于为特定的软件包、软件框架、硬件平台、操作系统等创建应用软件的开发工具的集合。</p></blockquote>
<p>SDK的定义比较拗口，我们简化一下就是：“SDK是程序员创建软件的开发工具的集合”。</p>
<p>这样就清晰了，我们再明确几个重点：</p>
<h3>1. 程序员</h3>
<p>SDK是程序员开发出来的，也是要提供给程序员使用的。可谓：从开发者来，到开发者去。</p>
<h3>2. 创建软件</h3>
<p>SDK是用来帮助程序员创建软件的，用来帮助程序员编程的。</p>
<h3>3. 集合</h3>
<p>SDK是一个开发工具的集合，这里要强调它是一个集合，它不止包含单纯的功能模块文件，它还包含这些库文件的使用接口、说明文档、使用Demo等内容。</p>
<p><b>总之，SDK是这么一种存在：</b></p>
<p>假如你是ToB公司的产品策划同学，你们公司为客户公司的开发者提供一些功能，这些功能可能是QQ登录组件、支付宝支付组件、通信通道组件···等各类模块，你公司提供的这些功能模块就以SDK的形式存在，提供给客户公司的程序员。</p>
<p>客户公司的程序员拿到你们公司的这套SDK后，你就可以根据里面的说明文档，调用提供的接口，使用SDK中的库文件（lib格式、dll格式、so格式等）进行编程，把你们提供的功能集成到自己的软件中，使他们的软件具备了SDK提供的功能。</p>
<h2 id="toc-2">二、常见的SDK有哪些？</h2>
<h3>1. 在Windows 系统下</h3>
<p>有许多的SDK供开发者使用，在Windows 系统开发出各种个样的产品；</p>
<h3>2. 在Android系统下</h3>
<p>有官方不断推出的Android SDK，供Android开发者在Android系统上开发出各种个样的产品。</p>
<h3>3. 第三方公司提供的SDK</h3>
<p>例如：在2010年腾讯提供开放战略要将腾讯的社交能力开放给行业，就是我们常见的QQ分享、微信好友分享、朋友圈分享等功能，这些功能在Android系统上就可以通过SDK的形式提供给开发者。</p>
<p>在这里，我们要重点分享的，也是ToB产品经理需要策划的，就是第三类。</p>
<h2 id="toc-3">三、SDK存在的意义是什么？</h2>
<p><b>答案是：效率。</b></p>
<p>SDK将常用的功能封装后，以组件的形式存在，让其他项目开发者，只需要简单集成SDK，调用几个接口，就可以使用SDK中已封装的功能。<b>不再需要重复造轮子，可以大大提高开发效率。</b></p>
<p><b>尤其在移动游戏领域：</b></p>
<p>许多游戏产品能够在几个月内完成开发，一个重要原因就是能够直接调用 支付组件、语音组件、安全组件、数据通信组件等SDK，开发者只需要将核心精力放在游戏玩法的开发商。大大缩短游戏研发周期。</p>
<h2 id="toc-4">四、企业用户对SDK产品的诉求是怎样的？</h2>
<p><b>他们希望：</b></p>
<blockquote><p>能够以最短的时间完成接入，能够以最简单的方法完成SDK验证，使用SDK提供的功能。与此同时，在SDK运行过程中，还要有足够高的稳定性、兼容性，对APP的性能影响要足够小。</p></blockquote>
<h2 id="toc-5">五、SDK产品的存在形式</h2>
<p>目前的ToB产品大部分都在为移动产品尤其Android产品提供产品功能，所以我们这里以Android产品为例进行说明。</p>
<p><b>一款SDK产品大概包含以下内容：</b></p>
<h3>1. SDK功能模块</h3>
<p>在移动开发领域，可以大概了解以下概念，对于以C/C++语言为核心的native层开发，我们一般会提供.so格式的动态链接库文件；对于以java语言为核心的jave层开发，我们一般会提供.jar类型的库文件；对于以C#语言为核心的Unity等游戏开发，我们一般会提供.cs格式的功能模块。</p>
<p>SDK功能模块包含了核心的功能实现。</p>
<h3>2. API接口</h3>
<p>有了SDK模块，程序员需要调用这些SDK模块以使用其中的功能。那怎么调用呢？就需要用到我们提供的API接口。API接口是一些函数，开发者将你提供的SDK加载到自己的工程中，通过对这些接口进行调用，就可以使用SDK中的功能了。</p>
<h3>3. 文档</h3>
<p>SDK模块怎么加载？API接口怎么调用？这其中需要注意什么？这些都需要通过文档的形式向开发者阐明。</p>
<h3>4. Demo</h3>
<p>即使有了上面的功能模块、API接口和文档，开发者使用你的SDK产品依然是很抽象的，所以最好能给一个工程Demo，这个Demo中有详细的示例代码来说明怎么在工程中使用SDK，让开发者能够一目了然，快速编码。</p>
<h2 id="toc-6">六、SDK产品设计的 8 大技巧</h2>
<p>SDK的开发工作是由技术同学完成，但他们更关注的是功能的实现。产品经理负责最终将SDK这个产品形态，进行产品化包装，然后作为产品提供给外部企业使用。</p>
<p>所以产品经理应该对外部厂商对SDK产品的使用场景有最敏感的把握，然后把这些关注点转化为产品上的需求，将这些用户体验层面的要求融入到技术同学的SDK开发过程中。</p>
<p><b>那么，对于企业用户的开发者，他们在使用SDK产品时有哪些关注点？</b></p>
<p><b>ToB产品经理在策划SDK产品时有哪些窍门？我们来总结SDK产品设计的8大技巧：</b></p>
<h3>1. 接口越少越好</h3>
<p>在客户的产品研发过程中，SDK的调用只是其中的一个小环节，他们的开发者对SDK产品的诉求是，用最短的时间完成接入，能够稳定的使用SDK提供的功能。所以，怎样保证SDK调用简单。方法是，接口越少越好。最好只需调用1-2个简单接口就可以完成接入。SDK接入的耗时最好不超过半天。</p>
<h3>2.  要有简单的Demo</h3>
<p>为SDK提供一份简单的Demo，可以说已成为SDK产品的必需品。对于客户开发者，在调用SDK时，参照提供的可运行的Demo工程接入SDK，会事半功倍，接入成功率大大提高。</p>
<h3>3. 要有清晰的文档</h3>
<p>一份好的SDK产品，其简明的接入文档是必不可少的。文档的描述需要清晰条理，描述清楚开发者在接入SDK过程中可能遇到的问题。</p>
<p>格式方面，最好使用markdown格式，这种结构化的文档形式，在移植到官网平台上展现时，可以采用更标准的统一格式，也可以采用结构化的展现形式。</p>
<h3>4. 体积越小越好</h3>
<p>开发者许多时候会集成5个甚至10个以上的SDK，所以如果每个SDK的体积都比较大，最终会对自己的项目体积或者APP包的体积影响过大。因此，这就要求在开发SDK的时候一定关注体积大小，精简代码与功能，以最精简的形态提供最核心的功能。</p>
<h3>5. 全面适配各种场景</h3>
<p>SDK作为工程项目的组件，就需要适配各种各样的工程项目场景。以移动开发项目为例，就至少需要提供Android、iOS两种类型的SDK版本。再以移动游戏开发为例，需要适配各种各样的引擎语言，比如SDK需要支持Cocos引擎、Unity引擎、虚幻引擎等。</p>
<h3>6. 足够的稳定性和兼容性</h3>
<p>SDK作为第三方组件，对于客户来说是不太可控的。他们不清楚SDK内部的逻辑，也不可更改SDK的逻辑。一旦接入到自己的APP项目中，这就相当于一个黑盒的存在。一旦这个SDK出现crash情况，将会危及自己的APP的运行。所以他们对于SDK的稳定性和兼容性是非常在意的。</p>
<p><b>要想保证SDK的稳定性和兼容性，需要做到两点：</b></p>
<ul>
<li>第一，在研发SDK时，从原理上多下功夫，在基础机制上保证SDK是能够适配各种机型、能够适配各种场景的。</li>
<li>第二，在对外推出之前，还需要进行全面的测试，在各种机型上，在各种场景下，对SDK进行全面的测试。</li>
</ul>
<p><b>这里还有一个小Tips，在客户使用SDK前，可以提醒开发者自己可控SDK是否运行。</b>方便如果出现问题，也可以及时通过后台开关关闭SDK的调用。</p>
<h3>7. 接入自测要简单</h3>
<p>SDK的接入完成后，开发者需要验证SDK接入是否成功。最基础的方法是，提供给开发者一个教程，开发者自己查看日志等方法，观察是否接入成功。</p>
<p><b>还有两个产品化成都更高的方法：</b></p>
<p><b>第一，本地接入，Web实时数据验证</b></p>
<p>在后台根据SDK接入后的数据上报情况，在Web端实时将接入检测结果呈现给开发者。开发者只需要在本地简单运行接入了SDK的项目工程就OK。简单方便，受欢迎。</p>
<p>案例：tdw.qq.com</p>
<p><img data-action="zoom" class="size-full wp-image-3482726 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/JsgPLCZEzfhatlLkT8dM.png" alt width="1240" height="734" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">腾讯数据大师SDK接入验收功能</div>
<p><b>第二，Web一体化安装SDK</b></p>
<p>有些SDK产品不再让开发者进行复杂的接入，直接要求开发者将APP上传，然后统一将SDK打入到APP里面，通过机器化的SDK打入方式，免去了人为接入可能存在的误操作等情况，将SDK的接入过程也免除了，这种方法只要最终提示打入成功，就代表接入SDK成功，更简单稳定。</p>
<p>案例：gameguard.nprotect.com</p>
<h3>8. 保障数据安全</h3>
<p>SDK接入后，在客户的工程中作为一个第三方黑盒的存在。所有公司都会很担心SDK是否有后门，是否会获取各种敏感数据上报。另外，尤其对于运行在海外的项目，欧盟出台了GDPR政策后，对数据的采集权、对用户的隐私权，都有更严格的要求，所以务必引起重视。</p>
<p><strong>针对SDK数据安全问题，SDK产品设计过程中，需要做到3点：</strong></p>
<ul>
<li><b>第一，严格管理数据采集。</b>SDK在开发过程中，需要做到：不需要的数据坚决不采集，因业务需要采集到的数据务必进行严格加密处理，谨防数据泄漏。</li>
<li><b>第二，在产品宣传过程中打消客户顾虑。</b>在宣传时，重点呈现SDK数据权限问题，向客户承诺数据采集的严谨性和数据存储的保密性。打消客户的顾虑。</li>
<li><b>第三，在客户使用SDK时提醒客户注意数据隐私问题。</b>你的客户需要提醒自己的用户会采集哪些数据，并需要经过用户同意之后，才能使用SDK产品。</li>
</ul>
<p>以上即是SDK产品设计的 8大技巧，客户最关注，产品设计也最亟需解决。</p>
<h2 id="toc-7">七、一些ToB类的SDK产品案例：</h2>
<p>下面列举一下SDK产品案例，可以用来对比学习：</p>
<p><b>（1）友盟：</b>https://www.umeng.com/</p>
<p><img data-action="zoom" class="alignnone size-full wp-image-3482727 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/RqiQYxHCyLvaqKlsvnx2.png" alt width="1240" height="598" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">友盟 SDK下载</div>
<p><b>（2）Gvoice：</b>https://gcloud.qq.com/product/6</p>
<p><img data-action="zoom" class="alignnone size-medium wp-image-3482728 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/vbkQXK2lkszhPzPPcZTJ.png" alt width="1240" height="697" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">GVoice SDK下载</div>
<p><b>（3）游密：</b>https://www.youme.im/</p>
<p><img data-action="zoom" class="alignnone size-full wp-image-3482729 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/sxFuALEVLndjXdslgrv1.png" alt width="1240" height="580" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">游密 SDK下载</div>
<p><b>（4）百度云SDK：</b>https://cloud.baidu.com/</p>
<p><img data-action="zoom" class="size-full wp-image-3482730 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/LWuOQ7AtiN6NdngMK8kW.png" alt width="1240" height="621" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">百度云</div>
<p><b>（5）腾讯YSDK：</b>https://open.tencent.com/</p>
<p><img data-action="zoom" class="size-full wp-image-3482724 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/6iEry3vEKngspd95t7Ml.png" alt width="1240" height="735" referrerpolicy="no-referrer"></p>
<div class="image-caption" style="text-align: center;">YSDK</div>
<h2 id="toc-8">八、总结一句话</h2>
<p>SDK产品形态是ToB产品化的重要组成部分，产品经理可以在SDK产品设计的过程中使用上述的8大技巧，与公司一起推出高度产品化的SDK产品。</p>
<p> </p>
<p>作者：赞德，腾讯产品经理，ToB方向。个人微信号xanderfriend；公众号：赞德说（xander_talk），欢迎交流。</p>
<p>本文由 @赞德 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3482488" data-author="829970" data-avatar="http://image.woshipm.com/wp-files/2019/01/ToXwzQzRFtl0th5lXlzz.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            