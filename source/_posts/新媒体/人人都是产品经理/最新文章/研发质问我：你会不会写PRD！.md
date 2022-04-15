
---
title: '研发质问我：你会不会写PRD！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/ihEbfmeWzHsnOv4NXuQR.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 15 Apr 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/ihEbfmeWzHsnOv4NXuQR.jpg'
---

<div>   
<blockquote><p>编辑导语：产品经理有一个工作内容叫做需求分析（PRD），主要是看业务上有哪些不合适的地方，并且提出方案去完善。在这篇文章里，作者便通过分析一个实际例子中存在的问题，像我们分享了如何写好需求文档，需要注意什么，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5396900" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/ihEbfmeWzHsnOv4NXuQR.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近和一些初入刚入门的产品或者想要进入产品岗位的人交流。发现很多人都是在自学Axure、去练习软件的使用和交互的设计。</p>
<p>昨晚有个朋友把他的原型发给我，想让我帮忙看下问题。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/KE3NDeSMzyNEmxB2xxEh.png" alt width="615" height="566" referrerpolicy="no-referrer"></p>
<p>其实这里第一个问题就是他不知道自己的问题在哪里，这本身就是一个比较致命的问题。</p>
<p>产品经理有一个工作内容叫做需求分析，去看业务上有哪些不合适的地方，并且提出方案去完善。</p>
<p>暂且抛开这些，我们今天先来看下PRD到底应该怎么写。</p>
<h2 id="toc-1">01</h2>
<p>这是这位同学的需求文档，我简单截2张图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/xfhnpI0VK6Bl7Oh8ga7Z.png" alt width="899" height="415" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/Yx2FRLUsitzHZz0ZILxZ.png" alt width="899" height="454" referrerpolicy="no-referrer"></p>
<p>乍一看挺像那么回事的，但其实不管是逻辑上、还是原型交互上，仔细看都会有问题。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/OWIM8YKZTmPk5zWpMHQ2.png" alt width="897" height="783" referrerpolicy="no-referrer"></p>
<p>以登录页面的需求描述为例：</p>
<p>1）图中1、2两部分的逻辑是有冲突的。1讲的是账号没有填写的时候，点击登录按钮会给予提示“账号不能为空”；而2讲的是登录按钮在账号密码未填写时是不可点击的。</p>
<p>那请问当账号和密码都没有填写的时候是可点击还是不可点击呢？</p>
<p>如果可以点击，那点击后的提示是提示账号不能为空还是密码不能为空呢？</p>
<p>2）图中3是指密码错误时候给予提示：密码错误请重新输入。看起来逻辑是正确的，但业务场景上是有问题的。</p>
<p>这样表述代表着你已经默认账号是正确的。</p>
<p>那是否会存在A用户的账号是ningshu，B用户的账户是ninshu。当A在账户上填写的是B用户的账户，那密码不可能正确。</p>
<p>因为错误其实不在密码上，而是在账户上。所以更准确的说法应该是：账号或密码可能有误，请重新输入。</p>
<p>3）图中4部分是指账号不存在的时候，输入框下方会进行提示：无此账号，请重新输入。</p>
<p>第一，<strong>没有触发条件</strong>，是需要研发监控输入框，每输入一个字符就去数据库查询是否有这个账户吗？显然不合适。</p>
<p>第二，哪怕你的触发条件是在光标离开输入框之后也不合适。因为判断账号信息应该在登录按钮时一起来判断，<strong>原本在一个操作上完整判断的事情不合适分开来处理。</strong></p>
<p>4）图中5部分只讲了自动登录，那什么时候自动登录会被取消呢？</p>
<p>是保持7个自然日的自动登录，如果用户登录后会重新更新7自然日的token记录，超出7个自然日不登录会被取消自动登录？还是其他的一些条件？</p>
<p>5）整个文档从逻辑上就有问题，在讲某一个页面组件，比如“账号输入框”的时候会出现其他组件的逻辑判断（输入框提示账号不能为空）。</p>
<p>你在和研发沟通的时候，研发的思维是跳跃着来，并且本身是登录按钮的逻辑被打散拆到了账号输入框、密码输入框等不同地方，对于单个组件的<strong>逻辑是不连续</strong><strong>的</strong>。</p>
<p>6）登录按钮在页面上讲过有很多错误提示的情况。那请问这些<strong>错误提示的优先级是什么？</strong></p>
<p>就像我们上面刚刚提到过的，既有账号不能为空，也有密码不能为空。那当账号密码都为空的情况下应该给予什么样的错误提示呢？</p>
<p>……</p>
<p>其实这里面还有很多问题，就不一一详细来说了。</p>
<h2 id="toc-2">02</h2>
<p>需求文档到底应该怎么写？</p>
<p>首先我们得理解原型是原型，需求文档（下面简称为PRD）是需求文档。像这种原型边上做标注的方式是可以的，但标注完也不是完整的PRD。</p>
<p>PRD是给谁看的？PRD评审其实根据不同业务或者重要程度参与的人每次都可能不一样。</p>
<p>参与者会是以下11个岗位的其中1个或多个。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/sEwZ9e88PeHYoBVs9VPZ.png" alt width="892" height="881" referrerpolicy="no-referrer"></p>
<p>当有这么多人参与进行PRD评审的时候，第一件事情不是讲具体的功能点事什么。</p>
<p>而是要和大家沟通为什么做这件事情，做这件事情对我们的业务有什么样的好处？也就是常说的<strong>需求目标是什么</strong>？</p>
<p>只有大家达成共识的时候，在接下来的PRD评审过程里，才能让研发和其他部门的人和你是在一个频道上思考的。</p>
<h2 id="toc-3">03</h2>
<p>PRD文档是用于给研发进行开发所使用的，所以这里就有一个非常关键的原则——<strong>没有任何歧义的部分。</strong></p>
<p>1就是1，2就是2，<strong>不能模凌两可</strong>，这样研发才能很好地把代码写出来，千万不能让研发去猜。</p>
<p>就像我们刚刚上面聊到的，登录按钮的错误提醒是有优先级的，你可以这样写：</p>
<blockquote><p>当账户和密码两者有一个没有输入的情况下，点击登录按钮时，在下方提示：账号或密码不能为空。</p>
<p>当账户和密码输入后，点击登录按钮时，系统按以下顺序进行判断：</p>
<p>1.账户是否存在</p>
<p>存在：进行第2条规则判断</p>
<p>不存在：下方提示文案：“该账号不存在”</p>
<p>2.判断密码是否正确</p>
<p>不正确：下方提示文案：“账号或密码错误,请重新输入”</p>
<p>正确：toast提示：“登录成功”并跳转页面进入管理后台首页</p></blockquote>
<p>把所有的情况都写出来，这样研发看起来是没有争议的。当然，更好的做法是写User Case，如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/fu8orYEia7lPe18IRZwP.png" alt width="896" height="997" referrerpolicy="no-referrer"></p>
<p>User Case 是拿来干嘛的？是用来描述什么角色通过某某系统能做什么事情的流程体现，User Case 的书写也是产品经理对用户需求深刻理解的体现。</p>
<h2 id="toc-4">04</h2>
<p>需求文档的书写上还有很多需要写的，比如你需求中的<strong>完整业务流程图</strong>、<strong>分角色甬道图</strong>、<strong>详细需求清单</strong>等。</p>
<p>如果涉及到系统安全性部分还需要有<strong>安全性需求</strong>，比如接口的加密、账户的单点登录、单位时间内多次接口访问时需要进行人机交验、用户输入不能注入SQL、代码等。</p>
<p>如果<strong>涉及到一些法律上的部分</strong>，需要法务进行协助的需求。比如用户隐私、用户所输入的安全性交验，是否涉黄涉暴涉政等。</p>
<p>详细的内容一篇文章说不完，我们后面再慢慢详细说。</p>
<p> </p>
<p>本文由 @宁叔爱思考 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Pexels，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5393789" data-author="1416893" data-avatar="http://image.woshipm.com/wp-files/2022/04/8wr4pjgpq6ANIYj1wQpd.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            