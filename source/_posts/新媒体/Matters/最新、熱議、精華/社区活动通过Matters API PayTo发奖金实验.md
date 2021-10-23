
---
title: '社区活动通过Matters API PayTo发奖金实验'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/97c39e51-bf50-45b3-b0b5-f34c62109cbd.png'
author: Matters
comments: false
date: Wed, 20 Oct 2021 00:02:10 GMT
thumbnail: 'https://assets.matters.news/embed/97c39e51-bf50-45b3-b0b5-f34c62109cbd.png'
---

<div>   
<p>liker io一对多一次性投币，只有第一个被投币对象才能收到提示邮件，而且数据还是错的，害别人白开心一场，也挺囧的😳。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/97c39e51-bf50-45b3-b0b5-f34c62109cbd.png" data-asset-id="97c39e51-bf50-45b3-b0b5-f34c62109cbd" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>去<a href="https://api.like.co/tx/id/" target="_blank">https://api.like.co/tx/id/</a>查区块链id，也只会显示投币对象和投币总数，不会显示每个对象分别被投了多少：</p><figure class="image"><img src="https://assets.matters.news/embed/6f3b253b-30bd-4bc6-84ac-d5a2342a1178.jpeg" data-asset-id="6f3b253b-30bd-4bc6-84ac-d5a2342a1178" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>既然这样，就更别指望被投币对象还能收到<strong>正确的</strong>邮件提示了。。。。。。</p><p><br></p><hr><p><br></p><p>基于以上原理只有考虑去用matters API生成付款链接，再付款了。</p><p>matters api投币支持作者大致原理如下：</p><ol><li>通过PayTo API生成liker land付款完整链接，此时transaction状态为pending</li><li>在liker land付款链接付款完成，full链接自带的redirect_uri参数告知被投币文章，此时付款完成</li><li>transaction完成后，投币文章下方显示投币人圆圈头像。</li></ol><p><br></p><p>比如我要给<a href="https://matters.news/@sabaahprin/%E9%9B%9E%E6%AF%9B%E7%9A%84%E5%A4%A7%E4%BA%8B-d-28-bafyreibmq5dqewziaqqp3ixojy7m3lz2skxfj2ubpvb5exardjtmov72yy" target="_blank">这篇文章</a>投币，流程如下：</p><h2>1 Matters API Pay To</h2><p><strong>1.1 登录</strong></p><p>想要使用Matters API PayTo需要验证登录才可进行，不同于query取出tag、article之类的。所以先用Matters userLogin API 登录。登录API代码如下：</p><pre class="ql-syntax">mutation &#123;
  userLogin(input: &#123;
    email: "matters登录邮箱"
    password: "matter登录密码"
  &#125;) &#123;
    token
  &#125;
&#125;
</pre><p><br></p><p>一旦邮箱和密码匹配，你将会得到一个token用于需要身份验证的API授权使用。</p><figure class="image"><img src="https://assets.matters.news/embed/1b3d7c8c-e26f-43c1-8c14-6319748dde0b.png" data-asset-id="1b3d7c8c-e26f-43c1-8c14-6319748dde0b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>token就是一串看不懂的abcd。。。。。。不用管是什么意思。。。。。。<strong>当然了token会过期，所以不是每一次登录都返回相同的token值.。。。。。。</strong></p><p><br></p><p><strong>1.2 用payto生成付款链接</strong></p><p>当你在登录状态，想给某个用户的某篇文章投币时，就会用到payto api。</p><p><strong>假如我想给<a class="mention" href="https://matters.news/@sabaahprin" target="_blank" data-display-name="雞毛的小事" data-user-name="sabaahprin" data-id="VXNlcjo1MzIyNw">﻿<span>@雞毛的小事</span>﻿</a> 的这篇文章</strong><a href="https://matters.news/@sabaahprin/%E9%9B%9E%E6%AF%9B%E7%9A%84%E5%A4%A7%E4%BA%8B-d-28-bafyreibmq5dqewziaqqp3ixojy7m3lz2skxfj2ubpvb5exardjtmov72yy" target="_blank"><strong>雞毛的大事 (D-28)</strong></a><strong>投币20 ，api代码如下：</strong></p><pre class="ql-syntax">mutation &#123;
 payTo(input: &#123;
    amount: 20
    currency: LIKE
    purpose: donation
    recipientId: VXNlcjo1MzIyNw
    targetId: QXJ0aWNsZToxNjEyOTk
  &#125;) &#123;
    redirectUrl
    transaction &#123;
      fee
      amount
      id
      state
      purpose
      createdAt
      sender &#123;
        displayName
      &#125;
      recipient &#123;
        displayName
      &#125;
    &#125;
  &#125;
&#125;
</pre><p><br></p><p>这一步除了需要Authorization。Authorization就是添加1.1做登录验证的token值到header里面。</p><figure class="image"><img src="https://assets.matters.news/embed/dd7443e0-d80e-401e-a790-caf3b82d2a51.jpeg" data-asset-id="dd7443e0-d80e-401e-a790-caf3b82d2a51" referrerpolicy="no-referrer"><figcaption><span>复杂一点的api还是去postman测试方便点。。。。。。</span></figcaption></figure><p><br></p><p><strong>1.2.1 recipientId是作者的id，id号获取代码如下:</strong></p><pre class="ql-syntax">query &#123;
  user (input: &#123;
    userName: "sabaahprin"
  &#125;) &#123;
    id
    displayName
    userName
    likerId
  &#125;
&#125;
</pre><p>id 和 liker id是两个玩意，别搞错了</p><figure class="image"><img src="https://assets.matters.news/embed/3aec0976-5e14-450a-ba2c-c92f66e904e7.jpeg" data-asset-id="3aec0976-5e14-450a-ba2c-c92f66e904e7" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><strong>1.2.2 targetId是要投币文章的id号：</strong></p><p>获取文章id号代码如下：</p><pre class="ql-syntax">query &#123;
  article (
    input: &#123;
      mediaHash: "bafyreieqsapvitr7xwrir6vqnvnpnnopwfljtai6v7uqceyubzjtye5m6a"
    &#125;) &#123;
    id
    title
    summary
    author &#123;
      id
      displayName
    &#125;
    wordCount
    readTime
  &#125;
&#125;
</pre><p><br></p><p>当然了也可以通过文章media hash获取文章id的同时获取作者id：</p><figure class="image"><img src="https://assets.matters.news/embed/0026bddb-e6fa-4fbe-9069-cc61f7688e35.jpeg" data-asset-id="0026bddb-e6fa-4fbe-9069-cc61f7688e35" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>需要payto的参数（文章id、作者id，验证token）搞好后，就可以生成liker land付款链接：</p><figure class="image"><img src="https://assets.matters.news/embed/dfe30eb5-f302-4758-aa18-70c621d23d27.jpeg" data-asset-id="dfe30eb5-f302-4758-aa18-70c621d23d27" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>完成这一步只是创建了transaction，如果不进入下一步——去like co付款转账，transaction的状态永远都是pending。</p><figure class="image"><img src="https://assets.matters.news/embed/bf0a10c2-5c71-4114-92d2-7a527afa92ad.jpeg" data-asset-id="bf0a10c2-5c71-4114-92d2-7a527afa92ad" referrerpolicy="no-referrer"><figcaption><span>这一步相当于支持作者，需要进入liker land完成支付，如果不完成支付，就永远都是转圈圈的pending状态</span></figcaption></figure><p><br></p><p><strong><u>参数说明：</u></strong></p><ul><li><u>文章id、作者id、作者likerId都可以通过Matters API公开获取</u></li><li><strong><u>用户登录邮箱，登录密码不是API可以随意获取，要保管好，不要泄露天机</u></strong></li><li><strong><u>登录身份验证后得到的token更不能随意泄露，</u></strong><u>Matters API需要验证身份时必备，比如在PayTo时没有token就不能进行下一步</u></li></ul><p><br></p><p><br></p><h2>2 用payto api生成的付款链接付款</h2><p>通过payto api获得的给<strong><a class="mention" href="https://matters.news/@sabaahprin" target="_blank" data-display-name="雞毛的小事" data-user-name="sabaahprin" data-id="VXNlcjo1MzIyNw">﻿<span>@雞毛的小事</span>﻿</a> </strong><a href="https://matters.news/@sabaahprin/%E9%9B%9E%E6%AF%9B%E7%9A%84%E5%A4%A7%E4%BA%8B-d-28-bafyreibmq5dqewziaqqp3ixojy7m3lz2skxfj2ubpvb5exardjtmov72yy" target="_blank"><strong>雞毛的大事 (D-28)</strong></a><strong>投币20</strong>的付款链接长这样：</p><pre class="ql-syntax">https://like.co/in/widget/pay?to=sabaahprin&amount=20&via=matterspool&fee=0&state=e578d2eb-ca3f-40d7-897c-613b31920dde&redirect_uri=https%3A%2F%2Fserver.matters.news%2Fpay%2Flikecoin&blocking=true
</pre><p><br></p><p>该链接把所有参数都用上了。。。。。。</p><ul><li>to：付款人的likerId</li><li>amount：投币金额</li><li>via：传说中的agent。。。。。默认是matterspool</li><li>fee：给matterspool的中介费，默认为0，很良心</li><li>state：付款状态参数</li><li>redirect_uri：返回matters页面，告知投币者投币结果（成功、还是失败）</li><li>blocking：当付款在区块链上确认生成后，激活redirect_uri的Boolean参数</li></ul><p><br></p><p>把参数齐备的付款链接在浏览器打开，付款完成后会页面自动刷新到matters，并告诉你投币成功，即transaction状态由pending转为success。</p><p>同时收到matters邮件，告诉你最近有投币行为：</p><figure class="image"><img src="https://assets.matters.news/embed/2ae6aa62-2bba-4477-9f26-ae2812d5a622.jpeg" data-asset-id="2ae6aa62-2bba-4477-9f26-ae2812d5a622" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>当然了被投币对象的文章下面也会显示投币者头像，因为调用payto api时指定了文章id：</p><figure class="image"><img src="https://assets.matters.news/embed/9b88b040-875f-4d0d-bc02-97bb13bff21e.jpeg" data-asset-id="9b88b040-875f-4d0d-bc02-97bb13bff21e" referrerpolicy="no-referrer"><figcaption><span>以上完成用API给《雞毛的大事 (D-28)》投币20</span></figcaption></figure><p><br></p><p><strong><u>一对一的投币实验，被投币者当然会收到邮件提示。。。。</u></strong></p><p><br></p><h2>3 PayTo一对一多发送实验</h2><p>社区活动完结时，不会只给一个人投钱嘛。。。。。。所以为了完成给一串人发钱，还需要继续实验，顺便看看操作是否顺畅（<strong>比点按钮到底方便了多少</strong>）。</p><p>顺延之前的实验，还是选择python notebook弄吧。。。。。。</p><p><br></p><p><strong>3.1 获取投币对象</strong></p><figure class="image"><img src="https://assets.matters.news/embed/a08c6989-c544-41c3-adbf-5010147fe04e.png" data-asset-id="a08c6989-c544-41c3-adbf-5010147fe04e" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>假如某活动搞完了，有两篇投稿，我先去搜集算奖金需要的数据，整理成以上表格。</p><p>……</p><p><s><u>然后开始算奖金……此处省略很多步……根据自己的算奖金规则该咋算咋算……</u></s></p><p>……</p><p>算完奖金，“活动参加者”1号——小鸡得了28 likecoin；“活动参加者”2号——小码的了30 likecoin。</p><figure class="image"><img src="https://assets.matters.news/embed/4e532a29-0363-4333-8da0-8a92138ca146.png" data-asset-id="4e532a29-0363-4333-8da0-8a92138ca146" referrerpolicy="no-referrer"><figcaption><span>为了方便，奖金就是随机数了。。。。。。</span></figcaption></figure><p>到此为止，奖金算到人头上后开始发……</p><p><br></p><p><strong>3.2 在notebook里面，API略有变化</strong></p><p>之前1对1给<a href="https://matters.news/@sabaahprin/%E9%9B%9E%E6%AF%9B%E7%9A%84%E5%A4%A7%E4%BA%8B-d-28-bafyreibmq5dqewziaqqp3ixojy7m3lz2skxfj2ubpvb5exardjtmov72yy" target="_blank"><strong>雞毛的大事 (D-28)</strong></a>发奖时，在postman里面测试，加上token直接过了。到了python notebook，按照常规加header貌似不行。。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/d2718f67-aff9-4244-bc41-0e011815bf63.png" data-asset-id="d2718f67-aff9-4244-bc41-0e011815bf63" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>按照常规加token不是加在header里面嘛，结果到了notebook不行了，一直说我在以游客身份请求付款。。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/b128a6e2-8650-4b88-b2ba-ce3ec662e8ed.png" data-asset-id="b128a6e2-8650-4b88-b2ba-ce3ec662e8ed" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>刚开始我以为这是matters api cors（Cross-Origin Resource Sharing）造成的，查了半天也没解决问题。后来对比header异同，发现可能是cookie造成的。。。。。。</p><p>login api验证密码登陆后，得到的request header长这样：</p><figure class="image"><img src="https://assets.matters.news/embed/9a13800e-6349-4e10-9e50-c47de534f459.png" data-asset-id="9a13800e-6349-4e10-9e50-c47de534f459" referrerpolicy="no-referrer"><figcaption><span>登陆header里面包含token，这个token要2022年1月才过期。。。。。。。</span></figcaption></figure><p>一般的普通request返回header长这样：</p><figure class="image"><img src="https://assets.matters.news/embed/479f15fb-571b-47f4-9291-aca94eca094f.png" data-asset-id="479f15fb-571b-47f4-9291-aca94eca094f" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>于是就把登陆后获取的cookie放在payto api里面请求：</p><figure class="image"><img src="https://assets.matters.news/embed/74229ce3-57e3-4126-ac30-709612d476ce.png" data-asset-id="74229ce3-57e3-4126-ac30-709612d476ce" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>获取cookies代码长这样：</p><figure class="image"><img src="https://assets.matters.news/embed/61f070de-0379-4336-bab6-63627a44fcf7.png" data-asset-id="61f070de-0379-4336-bab6-63627a44fcf7" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>把header auth换成cookie后，终于不是游客了，返回付款链接给我：</p><figure class="image"><img src="https://assets.matters.news/embed/917938bc-9c75-4563-993e-e51e3c2a8357.png" data-asset-id="917938bc-9c75-4563-993e-e51e3c2a8357" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><strong>3.3 解决了cookie和header的玄学后，就可以模拟发奖了。。。</strong></p><p>把链接弄成可点击的：</p><figure class="image"><img src="https://assets.matters.news/embed/5598af39-539f-4a6f-b64e-0a991088a34e.png" data-asset-id="5598af39-539f-4a6f-b64e-0a991088a34e" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>然后点击url打开浏览器，去liker land付款：</p><figure class="image"><img src="https://assets.matters.news/embed/8e23cd1f-60f5-4d9b-92d3-27a932ef03e8.png" data-asset-id="8e23cd1f-60f5-4d9b-92d3-27a932ef03e8" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>在liker land需要再次确认一次身份。。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/d46c0045-c80a-46b4-86fd-82bf386a7f1c.png" data-asset-id="d46c0045-c80a-46b4-86fd-82bf386a7f1c" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>然后输密码付钱。。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/f7982e8b-cfcd-49ee-9e98-71d4947d3fbb.png" data-asset-id="f7982e8b-cfcd-49ee-9e98-71d4947d3fbb" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>签署付款完成后，我就被redirect回了matters。。。。。。与此同时我也收到了matters邮件提示，我给小鸡支持了28个币。。。。。。</p><p>完成此操作步骤后，再循环去给小码付款。。。。。。</p><p><br></p><hr><p><br></p><figure class="image"><img src="https://assets.matters.news/embed/5b24b600-da95-4cfe-b83e-bf8d3570ee84.png" data-asset-id="5b24b600-da95-4cfe-b83e-bf8d3570ee84" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>以上就是目前思考出来的可以稍微简单一点的发奖金方法，其实原理还是1对1</p><p>本次实验只有2个人，当有100个人等待排队收款时，需要生成100个付款链接，然后挨个签署100次。。。。。。虽然需要签100次，但是双方都会收到邮件提示。。。。。。。</p><p>上一期试验完成后，我收到两笔来自liker land的神秘打款。可能我幸运地当了投币对象的第一人，所以收到了邮件提示。如果我没有在投币列表第一个，我就默默地被投了也不知道。。。。。。。</p><p>所以发收据（邮件提示）相当重要。。。。。。</p><figure class="image"><img src="https://assets.matters.news/embed/fd62a361-227c-4ab7-90e3-1203b738592d.png" data-asset-id="fd62a361-227c-4ab7-90e3-1203b738592d" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>以上办法虽然没有解决一次性签署一对多发钱问题，但是解决了手动输数字投币的问题——再也不用担心手滑输错奖金了。</p><p>然后就是，token要几个月才过期，慢慢发。。。。。。</p>  
</div>
            