
---
title: 'PC客户端数据埋点分享'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xJQnvIkp6b7ZuAGa24xV.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 16 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xJQnvIkp6b7ZuAGa24xV.jpg'
---

<div>   
<blockquote><p>编辑导语：移动互联网时代，PC互联网的客户端埋点几乎很少有能直接拿出来用的一套方案，因此，作者基于其经验进行了分享，我们一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4882073 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xJQnvIkp6b7ZuAGa24xV.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、起因</h2>
<p>移动互联网时代，无论是Android、iOS还是小程序，都有很多成熟的解决方案，无需花费很多的时间去处理埋点的事情，而且基于第三方提供的SDK进行埋点，在数据处理和分析上也有很大的优势。</p>
<p>但是在之前的PC互联网时代，除了网页端有百度统计、谷歌分析等，客户端的埋点似乎没有一套能拿出来可供大家讨论的解决方案，我就基于我的工作经验和理解，给大家分享一下PC客户端的埋点。</p>
<h2 id="toc-2">二、PC客户端的埋点一般统计什么？</h2>
<p>首先，在PC上，我们得知道我们需要统计些什么内容。</p>
<p>一个PC客户端，无论是工具类的还是内容类的，我们都希望知道我们提供的服务的效果。那么，我们从一个客户端安装、运行到最终被卸载来看看。</p>
<p>就拿产品使用较多的工具“Axure RP”来举例吧。如果“Axure RP”是我们自己的软件，首先我们需要知道被安装了，之后，我们关注激活情况，也就是使用，到最后，被卸载了，这一整个环节，构成了一个生命周期。</p>
<p><strong>重点来了，对于这个生命周期，所有你想知道的关于“Axure RP”的情况你都可以统计到。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/V2oJCskXfR4jUfBSawb1.png" alt width="715" height="425" referrerpolicy="no-referrer"></p>
<h3>1. 软件的安装</h3>
<p>在PC客户端安装的过程中，流程一般是这样的：</p>
<ol>
<li>运行安装包</li>
<li>弹出安装界面提供给用户操作</li>
<li>执行安装过程-写注册表、启动项、计划任务等</li>
<li>执行安装过程-创建安装的文件夹（3和4可以交换）</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/38rOUKtNv7PaCbaSgHz1.png" alt width="509" height="251" referrerpolicy="no-referrer"></p>
<p>在这个环节，我们一般需要知道：</p>
<ul>
<li>安装包被运行了</li>
<li>在安装界面用户做了哪些操作</li>
<li>我们的安装过程是否正常执行</li>
<li>我们最终是否安装成功</li>
</ul>
<p>在PC上，只要我们的安装包运行起来了，无论是弹出安装界面、写注册表还是创建文件，这些都是安装包可以控制的，所以我们能通过安装包进程，将整个安装环节的所有数据记录下来发送到我们的后台并记录下来<strong>（这里要重点记住，由于安装是一次性的动作，所以统计一定要发实时的）</strong>。</p>
<h3>2. 软件的使用</h3>
<p>软件的使用，包括启动软件、使用功能和退出软件。</p>
<p>在PC上，软件的启动有很多种方式，例如开机自启动、计划任务、手动点击快捷方式，我们继续以“Axure RP”举例，当我们装上了“Axure RP”后，会在桌面、开始菜单中，创建快捷方式（有些程序会在任务栏上也创建），同时，会将后缀名为“rp”的文件默认打开方式调整为“Axure RP”。</p>
<p><strong>对于启动，</strong>我们就有了三种方式：桌面快捷方式、开始菜单快捷方式和默认软件打开，所以我们需要统计软件是否被启动了，是如何启动的。</p>
<p><strong>对于使用功能，</strong>当软件运行起来后，其进程就会启动，这个时候就跟移动端的应用类似，我们需要统计一系列事件，每个功能的使用情况、功能状态、付费、登录等一系列信息。</p>
<p>区别于移动端的是，在PC上一般这些统计都是做单点统计，例如统计弹窗的弹出、功能的点击、某个状态，对于相互关联的一组事件统计是比较复杂的，需要定义结构体，在一条统计中包含很多组字段信息，因为没有成熟的SDK集成，所以基本都要自己定义埋点，复用性较差。</p>
<p>这部分统计分为公共统计和专用统计。公共统计就是基本信息，常用的是用户标识、用户基本信息、计算机硬件信息和其他的可复用的；专用统计就是针对你的功能，你想了解哪些情况，针对性进行埋点统计。</p>
<p><strong>对于软件退出，</strong>这就比较简单了，是正常退出还是异常退出？软件使用了多久退出？</p>
<h3>3. 软件的卸载</h3>
<p>软件卸载的流程包括启动卸载程序、用户操作、删除注册表及文件等操作、完成卸载。</p>
<p>在这个过程中，我们主要关注两方面的信息，一方面是用户怎么卸载的？是主动使用卸载程序，还是通过一些管理软件进行卸载？</p>
<p>另一方面是用户为什么要卸载，这个时候我们可以在卸载的界面中给用户提供选择，以获取用户的反馈。</p>
<h2 id="toc-3">三、该怎么埋点？</h2>
<h3>1. 埋点的分类</h3>
<p><strong>（1）时效性</strong></p>
<p>PC客户端一般情况下都比较复杂，子功能很多，可统计的内容很多，为了节省带宽，我们不可能每次都实时将数据传输回来，而且很多时效性不是很强的功能没有必要实时上报。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/MEdb5a82HAJfZNzVpXKb.png" alt width="557" height="207" referrerpolicy="no-referrer"></p>
<p>①实时统计</p>
<p>当功能触发时或达到一定条件，立即将统计回传，一般情况下用于时效性比较强的功能，例如活跃统计、营收类统计，我们需要实时分析并调整策略。</p>
<p>②延时统计</p>
<p>统计不立即回传，将统计积累，达到一定的条件或者一定的时间，统一将这部分统计回传，一般情况用于时效性不强的功能，例如采集设备信息、获取某些功能的状态、常规功能的统计。</p>
<p>这部分统计使用范围比较广，一般都是隔日发送，有一天的延迟，统计的信息晚一天不会对分析产生较大的影响。</p>
<p><strong>（2）埋点的作用</strong></p>
<p>①常规的基础统计</p>
<p>每次统计都需要发送，可以理解为公用统计，这部分统计是将几乎所有的统计都需要的部分包括进来，封装成一个统一的部分，每次发送统计都会带上这些内容，方便管理，节省后续埋点时间。</p>
<p>②功能统计</p>
<p>针对特定功能，当功能被使用或者生效的时候，我们需要统计效果或者状态，可以理解为专用统计，不同于移动端，PC一般没有第三方提供的SDK，需要每个专用统计自己埋点，维护大量的统计内容，不过在一个公司内部，可以统一设计规范，方便维护。</p>
<p><strong>（3）数据类型</strong></p>
<p>①结构体</p>
<p>统计连贯的事件，各项信息之间的关联很重要。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Mm4lOqzRqgfOkCxRHPnw.png" alt width="629" height="103" referrerpolicy="no-referrer"><span style="font-size: 16px;">②计数</span></p>
<p>统计某个行为发生的次数。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ajav5AkW45SDdV0mVD8w.png" alt width="639" height="53" referrerpolicy="no-referrer"></p>
<p>③字符串</p>
<p>统计内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pHfekHijpaFV8p1b84hj.png" alt width="629" height="5" referrerpolicy="no-referrer"></p>
<p>④整形</p>
<p>统计数值，也可用来统计状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/O8M75mGDE82Ygf2oQb36.png" alt width="623" height="17" referrerpolicy="no-referrer"></p>
<p>⑤布尔型</p>
<p>统计需要判断的类型，一般使用场景较少，为了方便计算，大部分被整形和字符串替代。</p>
<h3>2. 数据埋点实例</h3>
<p><strong>（1）软件安装</strong></p>
<p>场景：统计安装过程中的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TSwcrsxzyXG1uHZhAfx8.png" alt width="499" height="389" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/vQvp2xgLyRo2sniAY9f6.png" alt width="574" height="204" referrerpolicy="no-referrer"></p>
<p><strong>（2）软件的使用</strong></p>
<p>场景：软件启动后，用户使用了分享功能，将自己做的原型分享到了云端，最后用户关闭了软件。</p>
<p>要注意的是，软件启动和关闭，看需要是可以调整的，如果你只是想知道是不是启动了，来判断活跃，那么仅仅需要启动的时候发送个整型的值标识即可。</p>
<p>如果想知道更详细的信息，比如启动方式、启动时间等等，可以定义结构体，将这一刻更多的信息发送回来，可灵活定义。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/GEhFciBvnczD2KgCZU8P.png" alt width="730" height="275" referrerpolicy="no-referrer"></p>
<p><strong>（3）软件卸载</strong></p>
<p>卸载跟软件安装类似，这里就不赘述了。</p>
<p>在这里，如果希望收集用户的卸载原因，可以定义一个字符串，将用户填写的内容上报，这种形式的数据如果太多，不太利于分析，所以看产品情况可灵活设置。</p>
<p> </p>
<p>本文由 @山有木兮 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4870323" data-author="344271" data-avatar="https://static.woshipm.com/APP_U_202010_20201005092823_3139.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            