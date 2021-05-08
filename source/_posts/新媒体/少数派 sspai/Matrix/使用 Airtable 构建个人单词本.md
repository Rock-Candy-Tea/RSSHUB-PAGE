
---
title: '使用 Airtable 构建个人单词本'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/05/02/35706cca8c6962d08d7edfc8bfff94c2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sun, 02 May 2021 15:32:38 GMT
thumbnail: 'https://cdn.sspai.com/2021/05/02/35706cca8c6962d08d7edfc8bfff94c2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p>词到用时方恨少，这句话说的就是第一次写论文的时候的我。口语表达需要用到的词，真的比书面表达的词少很多。但是，在平时的论文阅读的过程中，总能发现一些「陌生词」，而这些陌生词往往用得非常的巧妙，在英语语境中，是更能precisely 地表达语义。我就是一直在思考这个问题，如何才能收藏起来以便以后为我所用呢？</p><p>本文就是提出这么一个免费的解决方案，来帮助我们摘抄陌生词，形成自己的词典，并能方便地查看和温故。当然，我们的目标还是希望能够多平台覆盖和同步的，不然实用意义就变少了。</p><h2>Airtable as a Database</h2><p>首先要解决的第一个问题，就是如何把想要的单词摘抄并存储起来。这里，很多的单词翻译软件都有自己的单词本功能，但是同步功能基本上都是付费的功能。对我这种低频使用者而言，不太实惠。</p><p>我考虑了使用在线表格作为后端的存储，Airtable 就是这个领域的佼佼者了，并且它提供的基于 HTTP 的 API 接口方便和其他的软件交互完成存储和访问，就非常地符合我们的需求。</p><p>你需要做的准备有以下的几点：</p><ul><li>准备一个 Airtable 的账户，新建一个 Table，并将主 sheet 命名为 Main</li><li>根据以下的 scheme 建立表头</li></ul><pre class="language-"><code># Name - Field Type
Query - Long text
Translation - Single line text
isWord - Check box
Explains - Long text
US-Phonetic - Single line text
UK-Phonetic - Single line text
Count - Number - Integer</code></pre><ul><li>最后，你需要获取 Airtable 相关的 API Token。</li></ul><p>访问 https://airtable.com/api，点击对应的 Table，选择左侧的 AUTHENTICATION，点击右上角的 show API key，你就能找到对应的 <code><your table id></code> 和 <code><your app token></code>。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/02/35706cca8c6962d08d7edfc8bfff94c2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/02/35706cca8c6962d08d7edfc8bfff94c2.png" referrerpolicy="no-referrer"></figure><ul><li>(可选) 在 Airtable 里增加 Gallery View，制作你自己的单词卡片，点击 Share View 可获取访问链接</li></ul><h2>Youdao as a Translator</h2><p>当选择了「陌生词」后，我们需要做的是存储它原词的同时，存储其对应的中文翻译。当然，这个版本也可以离线完成，通过 Airtable Automation 或者 Serverless Function 可以做到。但是前者需要付费订阅 Pro，后者使得平台更复杂化了。后来实际考虑，其实这个也放在本地完成就是可以的，从某种程度上来说也更简单一些。</p><p>首先，要做的获取有道智云 AI 开放平台的接口密钥。你需要访问：https://ai.youdao.com/doc.s#guide ，根据上述的指南注册开发者账号并获取密钥，上述官方有详细的图解步骤，我在这里就不重复了。关于价格，有道云文本翻译服务是48元/百万字符，每月调用量清零。换句话说，每月100万字符以下翻译免费，对于我们翻译几个单词来说，实在是绰绰有余。更详细的价格可以参考<a href="https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/%E4%BA%A7%E5%93%81%E5%AE%9A%E4%BB%B7/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-%E4%BA%A7%E5%93%81%E5%AE%9A%E4%BB%B7.html">官方定价文档</a>。</p><p>最终你获得的有两个关键的字符串：<code><your app key></code> and <code>your app scret</code>, 这里的 app 指的是有道智云 AI 开放平台上面的一个实例。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/02/1dfa24f29527ecb63bff3a68f9ed720f.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/02/1dfa24f29527ecb63bff3a68f9ed720f.png" referrerpolicy="no-referrer"></figure><h2>JSBox as a Client</h2><p>好了，万事俱备，只欠东风。接下来，就是通过 HTTP 接口，把「陌生词」存储到 Airtable 中。</p><p>这里，由于选择了本地调用有道云的接口，因此需要比较复杂的 JS 代码才能构建出 API 访问的参数，否则其实可以使用更轻量级的 捷径app 来完成这样的动作的。所以，我终于不得不选择 JSBox 作为 Client 调用接口。对于读者来说的好消息是，JSBox 免费下载且 1.x 版本的功能免费且我们只需要用到 1.x 版本的功能。对于我来说，我开发这个 workflow 专门买了JSBox，—_—</p><p>关于调用的代码，我已经全部开源并放到这个 <a href="https://gist.github.com/Wsine/4d68c4c0a06cc9219a79fc9d169b07ab">Gist</a> 里面了，文末我也放置了一份相同的作为附录，以便不方便访问 Gist 的读者们访问。</p><p>在 JSBox 里面，选择 New Project，名称可以自定义，Type 选择 JSBox script 即可，把开源的代码粘贴到里面，并替换其中的对应的密钥即可。</p><pre class="language-"><code><your app key> -> 你的有道云应用ID
<your app secret> -> 你的有道云应用密钥
<your table id> -> 你的Airtable的表格ID
<your app token> -> 你的Airtable的API Token</code></pre><p>为了在调用菜单里简化一级跳转逻辑，我们还需要借助 捷径APP 调用 JSBox</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/02/b79c174c8a85233fa92141190d6ae12f.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/02/b79c174c8a85233fa92141190d6ae12f.png" referrerpolicy="no-referrer"></figure><h2>Workflow Demo</h2><p>由于我阅读论文的设备是 iPad，因此这里用 iPad 做个演示。在你喜欢的论文阅读软件中选中相应的单词/短语，通过系统分享菜单选择对应的捷径。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/02/c85e09d3ba7472fe9f2608bdf59b49d6.gif" data-original="https://cdn.sspai.com/2021/05/02/c85e09d3ba7472fe9f2608bdf59b49d6.gif" referrerpolicy="no-referrer"></figure><p>对应的 Gallery View 的单词卡效果是这样子的，而且对响应式网站有适配，写论文的时候它给了我很大的帮助。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/02/d3ef86aaa1cdadef22350d26ebf5c162.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/02/d3ef86aaa1cdadef22350d26ebf5c162.png" referrerpolicy="no-referrer"></figure><p>理论上，这个 worflow 也支持句子摘抄和翻译，新增一个 Gallery View 和 Filtering 就可以，只不过我没有这个需求而已。</p><p>好了，以上就是全部的内容。感谢阅读。</p><h2>附录</h2><p><a href="https://gist.github.com/Wsine/4d68c4c0a06cc9219a79fc9d169b07ab#file-lexicon-js"><strong>lexicon.js</strong></a></p><pre class="language-javascript"><code>const CryptoJS = require("crypto-js")

function uuidv4() &#123;
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) &#123;
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  &#125;);
&#125;

var entrance = null
var query = null
if ($context.text) &#123;
  query = $context.text
  entrance = 'jsbox'
&#125; else if (Object.keys($context.query).length) &#123;
  query = $context.query.word
  entrance = 'shortcut'
&#125; else &#123;
  console.log('Please execute via share sheet')
  $context.close()
  $app.close()
&#125;
console.log('query', query)

const appkey = '<your app key>'
const salt = uuidv4()
console.log('salt:', salt)
const curtime = (Math.round(new Date().getTime() / 1000)).toString()
console.log('curtime:', curtime)
const appsecret = '<your app secret>'
var input = query
if (query && query.length > 20) &#123;
  input = query.slice(0, 10) + query.length + query.slice(query.length - 10, query.length)
&#125;
console.log('input:', input)
var concat = appkey + input + salt + curtime + appsecret
console.log('concat:', concat)
const sign = CryptoJS.SHA256(concat).toString()
console.log('sign:', sign)

var formData = &#123;
  q: query,
  from: 'en',
  to: 'zh-CHS',
  appKey: appkey,
  salt: salt,
  sign: sign,
  signType: 'v3',
  curtime: curtime,
  strict: 'true'
&#125;

if (query) &#123;
  $http.post(&#123;
    url: "https://openapi.youdao.com/api",
    form: formData,
    handler: function (resp) &#123;
      var ydreq = resp.data
      console.log(ydreq)
      var field = &#123;
        Query: ydreq['query'],
        Translation: ydreq['translation'].join('\n'),
        isWord: ydreq['isWord'],
        Count: 1
      &#125;
      if (ydreq['isWord']) &#123;
        field['Explains'] = ydreq['basic']['explains'].join('\n')
        field['US-Phonetic'] = ydreq['basic']['us-phonetic']
        field['UK-Phonetic'] = ydreq['basic']['uk-phonetic']
      &#125;
      $http.post(&#123;
        url: "https://api.airtable.com/v0/<your table id>/Main",
        header: &#123;
          'Authorization': 'Bearer <your app token>',
          'Content-Type': 'application/json'
        &#125;,
        body: &#123;
          records: [&#123;
            fields: field
          &#125;]
        &#125;,
        handler: function(resp) &#123;
          var atreq = resp.data
          console.log(atreq)
          var display = 'Created: ' + atreq.records[0].id
          if (entrance === 'shortcut') &#123;
            $intents.finish(display)
          &#125; else if (entrance === 'jsbox') &#123;
            $ui.preview(&#123;
              title: "AirTable API Response",
              text: display
            &#125;);
          &#125;
        &#125;
      &#125;);
    &#125;
  &#125;)
&#125;</code></pre></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>7</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2781" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E4%BD%BF%E7%94%A8%20Airtable%20%E6%9E%84%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%95%E8%AF%8D%E6%9C%AC%E3%80%91%E4%BD%BF%E7%94%A8Airtable%E6%9E%84%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%95%E8%AF%8D%E6%9C%AC%E8%AF%8D%E5%88%B0%E7%94%A8%E6%97%B6%E6%96%B9%E6%81%A8%E5%B0%91%EF%BC%8C%E8%BF%99%E5%8F%A5%E8%AF%9D%E8%AF%B4%E7%9A%84%E5%B0%B1%E6%98%AF%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%86%99%E8%AE%BA%E6%96%87%E7%9A%84%E6%97%B6%E5%80%99%E7%9A%84%E6%88%91%E3%80%82%E5%8F%A3%E8%AF%AD%E8%A1%A8%E8%BE%BE%E9%9C%80%E8%A6%81%E7%94%A8%E5%88%B0%E7%9A%84%E8%AF%8D%EF%BC%8C%E7%9C%9F%E7%9A%84%E6%AF%94%E4%B9%A6%E9%9D%A2%E8%A1%A8%E8%BE%BE%E7%9A%84%E8%AF%8D%E5%B0%91%E5%BE%88%E5%A4%9A%E3%80%82%E4%BD%86%E6%98%AF%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-617" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E4%BD%BF%E7%94%A8%20Airtable%20%E6%9E%84%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%95%E8%AF%8D%E6%9C%AC%E3%80%91%E4%BD%BF%E7%94%A8Airtable%E6%9E%84%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%95%E8%AF%8D%E6%9C%AC%E8%AF%8D%E5%88%B0%E7%94%A8%E6%97%B6%E6%96%B9%E6%81%A8%E5%B0%91%EF%BC%8C%E8%BF%99%E5%8F%A5%E8%AF%9D%E8%AF%B4%E7%9A%84%E5%B0%B1%E6%98%AF%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%86%99%E8%AE%BA%E6%96%87%E7%9A%84%E6%97%B6%E5%80%99%E7%9A%84%E6%88%91%E3%80%82%E5%8F%A3%E8%AF%AD%E8%A1%A8%E8%BE%BE%E9%9C%80%E8%A6%81%E7%94%A8%E5%88%B0%E7%9A%84%E8%AF%8D%EF%BC%8C%E7%9C%9F%E7%9A%84%E6%AF%94%E4%B9%A6%E9%9D%A2%E8%A1%A8%E8%BE%BE%E7%9A%84%E8%AF%8D%E5%B0%91%E5%BE%88%E5%A4%9A%E3%80%82%E4%BD%86%E6%98%AF%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            