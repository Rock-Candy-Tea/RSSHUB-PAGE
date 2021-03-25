
---
title: 'JavaScript学习（三十）——Cookie'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3299'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:35:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=3299'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>HTTP协议最早不保存访问网页的静态信息，不需要记录不同访客的独特需求。尽管这样的设计是高效的，但存在一定的弊端，因为服务器不记录每个用户的信息，所以Web浏览器将每一次访问都看作是一个全新的会话。也就是说，在浏览器和服务器之间完成一次会话后，就丢弃了连接，浏览器和服务器都不会保持两次会话之间的状态。这样影响到了用户与网站之间的交互。现在的Web浏览器多用Cookie来维护用户的状态信息，Cookie 是唯一一种在无序的页面中保护用户状态的方法。本章将详细介绍如何使用Cookie保存状态。</strong></p>
<h1 data-id="heading-0"><strong>了解Cookie</strong></h1>
<p><strong>Cookie是Web服务器保存在用户计算机上的文本文件的小块用户信息，每当用户访问Web服务器时，保存在用户计算机上的相关Cookie由客户端读取到服务器端，服务器瑞根据Cookie 信息为用户制定服务，例如，访客访问某网站时在页面中体现用户登录次数等。从本质上讲，Cookie可以看作身份证，但它不能作为代码执行，也不会传送病毒，且为用户所专有，并只能由提供它的服务器中取。Cookie保存的信息片段以“名/值”对的形式储存，一个网站只能取得它放在用户 计算机中的信息。无法从其他的Cookie文件中取得信息，也无法得到用户计算机上的其他任何信息。所以从这点上来进Cookie本身不存在安全隐患。<br>
同时，Cookie 是浏览器提供的一种机制， 它将document对象的cookie属性提供给JavaScript,可以由JavaScript对其进行控制，而Cookie并非JavaScript本身的性质。不同的浏览器对Cookie的实现也不一样，但其性质是相同的。<br>
Cookie是与Web站点而不是某个具体页面相关联的，所以无论用户访问该站点的任何一个页面，浏览器和Web服务器都交换Cookie 信息，用户访问其他站点时，每个站点都可能向用户发送一个Cookie,而浏览器会将这些Cookie分别保存。<br>
Cookie包括临时和永久两种方式，临时的Cookie只对当前的浏览器会话可用，永久的Cookie将在客户计算机上自动生成一个文本文件，所以在当前浏览器之外也可以使用。永久的Cookie是存储于用户硬盘的一个文件， 这个文件通常对应于一个域名， 当浏览器再次访问这个域名时，便使这个Cokie可用。因此，Cookie 可以跨越一个域名下的多个网页，但不能跨越多个域名使用。</strong></p>
<h2 data-id="heading-1"><strong>Cookie的形式</strong></h2>
<p><strong>Cookie是由name=value形式成队存在的，一个Cookie字符串最多可以存储20对name=value，Cookie字符串必须以分号作为结束符。</strong></p>
<h2 data-id="heading-2"><strong>Cookie的属性</strong></h2>
<p><strong>Cookie包括name、expires、path、 domain和secure这5个属性，其中name属性是必选属性，而其余个属性为可选属性。<br>
name属性  Cookie属性中唯必需设置的属性为name属性，表示Cookie的名称。<br>
expires 属性 Cookie的epires属性指定Cookie在删除之前要在客户机上保持多长时间，如果不使用expires属性，Cookie 只对当前浏览器会话有用，当用户关闭当前浏览器时，Cookie就会自动消失。<br>
path属性<br>
path属性决定Cookie对于服务器上的其他网页的可用性，一般情况下，Cookie 对于同一目录下的所有页面都可用。当设置path属性后，Cookie 只对指定路径以及子路径下的所有网页有效。<br>
domain属性<br>
许多服务器都由多台服务器组成，domain属性主要设置相同域的多台服务器共享个Cookie,例如，如果Web服务器a1需要与Web服务器a2共享Cokie,那么需要将a1的Cokie的domin设置为a2,这样al创建的Cookie就可以应用于a1和a2域的其他Wob服务器。</strong><br>
<strong>secure 属性</strong></p>
<p><strong>Internet连接本身是不安全的，为了保证Internet上的数据安全，会使用SSL协议加密数据并使用安全连接传输数据，一般支持SSL的网站以HTTPS开头，Cookie的secure属性表示Cookie只能通过使用HTTPS或其他安全协议的Internet连接来传输。如果secure属性不出现，就意味着Cookie在网络上未加密发送。</strong></p>
<h2 data-id="heading-3"><strong>Cookie 的主要用途</strong></h2>
<p><strong>Cookie可以帮助Web服务器保存有关访客的信息，简单地说，Cookie 是-种保持Web服务器连续性的方法。在大多数情况下，当用户浏览器向Web服务器提出请求时,有必要让Web服务器在用户请求某个页面时对用户进行身份识别。这里使用Cookie尤为方便，它提供了相关的标识信息，可以帮助服务器确定如何处理浏览器的请求。</strong></p>
<p><strong>保存登录状态<br>
可以将登录成功的用户相关信息存储在Cookie中，这样此用户下次访问时可以不需要重新登录Cookie还可以设置过期时间，当超过时间期限后，Cookie就会自动消失，这样提示用户登录的时间也可以进行限制。<br>
跟踪用户行为<br>
有一些网站可以根据访客的信息进行不同的处理，例如，可以根据用户的IP地址报告当前此用户所在地的天气情况等。<br>
创建购物车<br>
在一些商务网站中，Cookie 可以记录用户曾经浏览过的商品的相关信息，最后在结账时可以统一提交。<br>
实施民意测验<br>
一个实施民意测验的站点可以利用Cookie 来表示此用户是否已经参加了投票，可以设置Cookie的值为一个布尔类型的值，初始值为false,如果该访客已经进行投票，则设置Cookie值为true,这样可以避免该用户重复投票。但是如果用户删除本地的Cookie值，用户依然可以进行重复投票操作。</strong></p>
<h2 data-id="heading-4"><strong>Cookie的优点</strong></h2>
<p><strong>Cookie最大的优点在于它的持久性，当一个Cookie在用户的浏览器上被设置时，可以存留几天、几月，甚至几年，这样便于保存访问信息和用户状态，当此用户每次返回站点时，页面设置更加人性化。 同时Cookie可以保持访客状态，可以存储用户在一个站点上已经访问的页面及其次数、查看过的广告等。</strong></p>
<p><strong>Cookie经常与JavaSeript语言起使用。 JavaScript 语言中可以编写读取、写入、编辑Cookie的函数，使得Cookie在JavaScript语言中的操作非常简便，同时两者的结合可以使网页更具动态效果。</strong></p>
<h2 data-id="heading-5"><strong>Cookie的缺点</strong></h2>
<p><strong>Cookie除了具有以上优点之外，缺点也是有目共睹的，主要集中在安全性等方面。<br>
简要介绍Cookie的缺点。<br>
禁用Cookie<br>
Cookie是可以被禁用的，如果用户在本地将Cookie 禁用，当用户再次访问在本地设置网站时，网站中使用Cookie实现的功能就不可以使用。<br>
不同浏览器Cookie不可共享<br>
如果用户使用不同浏览器浏览相同页面时，不可以共享Cookie。所以不同浏览器之间的Cookie是不能相互访问的。例如，如果一个用户正使用Mozilla浏览器浏览某个网页，当该用户再次切换到IE浏览器，即使浏览同一页面，Cookie 依然不可使用。<br>
删除Cookie <br>
与禁用Cookie相似，如果用户刪除保存在本地的Cookie,当用户再次浏览此网站时，网站中使用Cookie的某些功能将不可以使用。Cookie被存储到用户的计算机中与其他文件没有区别，这个Cookie文件极有可能被删除。</strong><br>
</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            