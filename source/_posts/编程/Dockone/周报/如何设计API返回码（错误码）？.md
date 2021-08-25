
---
title: '如何设计API返回码（错误码）？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/1982b7231b7f8813bd44f99cea9328e0.png'
author: Dockone
comments: false
date: 2021-08-25 08:09:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/1982b7231b7f8813bd44f99cea9328e0.png'
---

<div>   
<br><h3>前言</h3>客户端请求API，通常需要通过返回码来判断API返回的结果是否符合预期，以及该如何处理返回的内容等。<br>
<br>相信很多同学都吃过返回码定义混乱的亏，有的API用返回码是int类型，有的是string类型，有的用0表示成功，又有的用1表示成功，还有用“true”表示成功，碰上这种事情，只能说：头疼。<br>
<br>API返回码的设计还是要认真对待，毕竟好的返回码设计可以降低沟通成本以及程序的维护成本。<br>
<h3>HTTP状态码参考</h3>以HTTP状态码为例，为了更加清晰的表述和区分状态码的含义，HTTP状态做了分段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/1982b7231b7f8813bd44f99cea9328e0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/1982b7231b7f8813bd44f99cea9328e0.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于后端开发来说，我们通常见到的都是：<br>
<br>2XX状态码，比如200->请求成功。<br>
<br>5XX状态码，比如502->服务器异常，通常就是服务没正常运行，或者代码执行出错。<br>
<br>通过状态码即可初步判断问题原因，HTTP状态的设计思路值得借鉴。<br>
<h3>参数约定</h3>虽说是返回码设计，但是只有code是不行的，还要有对应的message，让人可以看懂。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/943060cf9868db9a761f9aff79c71761.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/943060cf9868db9a761f9aff79c71761.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参考HTTP状态码的思路，我们对错误码进行分段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/fed851b72f0cdf4b0fea3f684b7b8dfd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/fed851b72f0cdf4b0fea3f684b7b8dfd.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过这样的设计，不论是程序还是人都可以非常方便的区分API的返回结果，关键是统一！<br>
<h3>个性化Message</h3>通常我们的Message都是写给工程师看的，但是在不同的场景下，同样的错误，可能需要给用户看到不一样的错误提示。<br>
<br>比方说20000-29999表示订单创建失败：<br>
<ul><li>20001，订单创建失败，存在进行中的订单</li><li>20002，订单创建失败，上一个订单正在排队创建中</li></ul><br>
<br>这两种错误情况如果是给用户看，可能就只适合看到：很抱歉，您有一个正在进行中的订单，请到我的订单列表中处理。<br>
<br>但是对于API来说，返回的信息又必须是准确的，但用户看到的就必须转译，这个转译的工作调用方可以做，但是通常API提供者来提供个性化的Message能力会更好。<br>
<br>我们可以把转译的消息配置到数据库，并缓存到Redis或者API本机。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/e890ae76d3c97f7e3335bdd19d4587de.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/e890ae76d3c97f7e3335bdd19d4587de.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后在请求处理结束即将返回的时候，根据application_id+code，去匹配替换message。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210824/e72d71f6a63337b9acb64dd0904a06b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210824/e72d71f6a63337b9acb64dd0904a06b4.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这样我们就可以让手机APP的用户、微信小程序的用户、网页下单的企业用户看到不同的消息。<br>
<h3>返回信息的统一处理</h3>有了统一的code，我们就可以通过Nginx或者APM工具统计API请求Code数量及分布信息。<br>
<br>我们可以根据单位时间内99999的数量来做API的异常告警。<br>
<br>我们可以根据Code的返回饼图，帮助我们发现系统、业务流程中的问题。<br>
<br>等等……<br>
<br>总之，好的返回码设计，可以帮助我们提高沟通效率，降低代码的维护成本<br>
<br>原文链接：<a href="https://ken.io/note/api-errorcode-or-resultcode-desgin" rel="nofollow" target="_blank">https://ken.io/note/api-errorc ... esgin</a>，作者：ken
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            