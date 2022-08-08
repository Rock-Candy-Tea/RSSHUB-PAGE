
---
title: '用 Scriptable 做个 iTerm 风格小部件'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/08/06/ea09e8ddc87a5d47237e9ce6c8ae6cb7.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Mon, 08 Aug 2022 02:13:35 GMT
thumbnail: 'https://cdn.sspai.com/2022/08/06/ea09e8ddc87a5d47237e9ce6c8ae6cb7.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-557a067a><div class="update-wrap" data-v-557a067a></div><div class="content wangEditor-txt minHeight" data-v-557a067a><p>iOS 平台可以自定义小部件的 app 有很多，有那么几种是和代码相关的，例如 JSBox、Taio 和本文的这款 Scriptable。不用码的小部件，可以根据 app 提供的方式进行自定义，而用码的小部件，则可以完全根据自己的需求来写规则，并且可以组合不同类型的信息。有码就有了更强大的自定义属性，但同时又一定程度上提高了门槛。这时候就会出现很多已经写好的示例提供给使用者，不想研究的人开箱即用，懂码的人也可以根据需求自己改改。</p><p>虽然 Scriptable有官方推荐的小部件库，但是有一些小部件是无法做到开箱即用的，例如本文要讲的这一款 iTermWidget。这是一款长的像 iTerm 的 Widget。iTerm 是一款  macOS 平台的命令行工具。命令行就是用纯文字敲出来和展示出来的东西，而 iTerm 通过区分不同代码的颜色来让信息更加易读，这样的展示方式成为了一种特色，才出现了现在这个小部件。</p><p>想要一个这样的小组件，是因为其他 App 自带的小部件所能展示信息的方式比较有限，通常我只能选择开发者做好的样子。而这款 iTermWidget 最大的特点就是字小，意味着展示的信息够多。其次它没有过多复杂的展现方式，仅仅是依靠文字和换行颜色，从信息的传达上不够直观但足够简洁。可以拥有展示多达 6 行信息的小部件（并且还可以进一步自定义），是我一直想要的。</p><p>正常情况下，在软件自带的 Gallery 里面「GET」到这个小组件后直接运行，<strong>是没有办法成功的</strong>。我在前两次下载这个 Scriptable 的时候就败在了这一步，当时就删掉了。这款软件内的小部件都是用 JavaScript 来写的，没有代码基础的人就完全无从下手。而刚好最近我在学 JavaScript，心想也许能解决之前没有搞懂的问题，想再尝试一下。但不用担心，下面的内容不涉及到 JavaScript 的具体语法等内容，仅仅是一些通俗易懂的常规操作。</p><h2>仅需3步，让它先跑起来</h2><p>在摸索了一番之后，终于搞清楚了能让小部件先成功显示出来的步骤，总结为以下三点，比较适合没有代码基础的朋友跟着尝试一下：</p><ol><li>将 6 个基本信息填入「TODO」</li><li>配置一个 Cache.js 文件</li><li>获取一个属于你自己的 OpenWeatherMap API KEY</li></ol><p>完成以上三步，再运行小部件，就能看到示例当中运行成功的样子了。</p><h2>零、下载 iTermWidget</h2><p>首先，在 App Store 下载 Scriptable，这款软件是完全免费的。</p><p>然后，在 Gallery 中下载好这个 iTermWidget 。点击「Scripts」页面里小部件右边的「···」，进入代码的页面。不要怕码，下面会一点点告诉怎样做，就像改稿子一样。</p><h2>一、将6个基本信息填入「TODO」</h2><p>小部件所展示的信息源自每个使用者的信息库，因此作者设定了这 6 个 「TODO」项，让大家根据自己的实际情况来进行预定义。（但是这也造成了这款 Widget 无法开箱即用的结果）</p><p>打开代码即可看到第 26 行就标出了 「TODO」的字样，作者已经把需要预定义的内容罗列在了这里，下面让我们来一一填入：</p><blockquote><p>注意！下方只需替换「TODO」这四个字母，它两边的「’」符号是要保留的！</p></blockquote><ol><li>NAME： 就是你想要给自己起的名字，任意即可，哪怕保留「TODO」也是可以的。</li><li>WEATHE_API_KEY：这个内容比较复杂，留在第三部分展开来讲。</li><li>WORK_CALENDAR_NAME：这是你要展示的个人日历的名称，我用的是「work」，你可以根据自己的实际情况填写，注意，这里开始就需要和日历一一对应了，如果有误，是跑不成功的。</li><li>PERSONAL_CALENDAR_NAME：同上，我用的是「personal」。</li><li>PERIOD_CALENDAR_NAME：作者默认加了这项，作为男生我其实没有用到，所以「先」简单同「Personal」，仅是为了跑成功。</li><li>PERIOD_EVENT_NAME：这一项是具体日历时间的名称，我没有，所以我随意写了个「p」（这一项写错了也是不影响代码跑成功的）</li></ol><p>好了，你已经填写好了需要预定义的内容了（第 2 项需要在后面展开说），接下来该进入下一步了。</p><figure class="image ss-img-wrapper image_resized" style="width:257px;"><img src="https://cdn.sspai.com/2022/08/06/ea09e8ddc87a5d47237e9ce6c8ae6cb7.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/ea09e8ddc87a5d47237e9ce6c8ae6cb7.jpeg" referrerpolicy="no-referrer"></figure><h2>二、配置 Cache.js 文件</h2><p>这个 iTermWidget 的运行需要用到缓存，简单说就是这个程序需要依赖另一个小程序作为工具。而这一个 Cache.js 文件，也不需要大家写，有作者 (EvanDColeman) 已经写好了，直接拿来用就好了。</p><p>1. 在 Scriptable 中点击右上角新建一个文件</p><p>2. 将所有代码（为了不影响观感，贴在了文章最后）复制粘贴进这个文件</p><p>3. 点击「Done」，退出，并重命名为「 Cache」即可。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/08/06/17db723787b9cf8714954b4e154b5128.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/17db723787b9cf8714954b4e154b5128.jpeg" referrerpolicy="no-referrer"><figcaption>这两个文件同时存在，才能顺利运行</figcaption></figure><h2>三、获取一个 OpenWeatherMap 的 API KEY</h2><p>OpenWeatherMap 是一个获取天气信息的服务。而要想从这个服务商获取到天气信息，就需要注册一下，生成一个属于你的 API KEY，来去向这个服务商索取这项服务。为什么要有这个 KEY 呢，因为这项服务，会根据使用次数和功能的多少来进行收费。（所以各位要保存好自己的 KEY，不要透露给别人。）但对于普通使用者来说，免费的额度是完全完全够用了（大概是每天1000次，个人用户一天肯定是不会超的），因此我们只需要去生成这个 API KEY，就接近成功了。</p><ol><li>访问 openweathermap.org，注册一个账号。</li><li>登陆之后，点击「Pricing」，别怕，是「购买」一个「不用花钱」的服务。</li><li>点击「Subscribe One Call by Call」，这里需要填入一下自己的付款信息，但是最终是不需要付款的，只有使用次数超过了免费额度才会扣钱，后面会说避免扣款的方法。</li><li>都确认好之后，右上角个人名称，下拉菜单中的「My API keys」，进入到 API KEY 的管理页面。</li><li>我已经忘记是否有一个默认 KEY 了，如果没有，那么就点一下 「Generate」，就会出现一个随机码形式的一个 KEY，这个 KEY 可要保存好。</li><li>将这个 KEY 填入到第一大步骤中的第 2 条，那么「TODO」的部分就全部完成了。</li><li><strong>别急！</strong>还差一小步，可以帮你避免万一被扣费的步骤！点击名字的「My Service」后，可以在上方看到一个「Billing plans」，可以看到已订阅的「One Call by Call」，将「Calls per day」改成 1000，就是免费额度的上限。那么这样子就不怕超额度扣费了。</li></ol><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/08/06/540a67278c6e8c9e2433b1adff536c8a.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/540a67278c6e8c9e2433b1adff536c8a.jpeg" referrerpolicy="no-referrer"><figcaption>绿色遮盖的部分，就是属于个人的 API KEY 了，一定要保存好不要外泄</figcaption></figure><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/08/06/9e3e81fea31f6c0f4571a138a94ffccc.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/9e3e81fea31f6c0f4571a138a94ffccc.png" referrerpolicy="no-referrer"><figcaption>将 Calls per day 设置成 1000， 就不会突破免费额度了</figcaption></figure><h2>完成，显示。</h2><p>好了，当完成了以上三步之后，在主屏幕设置好这个小组件，然后运行这个 Script，稍作等待，就可以看到这个小组件能够顺利展示内容了。那么，自定义这个 iTermWidget 的第一步就达到了。上述的讲述过程，完全照顾了不懂代码的朋友（因为我也不怎么懂）。而如果想要深度的自定义一下，只需要后续再稍微摸一点代码的规律。</p><figure class="image ss-img-wrapper image_resized" style="width:446px;"><img src="https://cdn.sspai.com/2022/08/06/62fd7432dea3aca081edab9cefd40c9c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/62fd7432dea3aca081edab9cefd40c9c.png" referrerpolicy="no-referrer"><figcaption>完成以上三步，主屏幕就会正常显示这个示例了。</figcaption></figure><h2>后续</h2><p>其实如果你仔细的读了 iTermWidget 的介绍页面，会发现作者已经写好了配置步骤（但仅有上面提到的两项内容，他默认了大家懂得如何填写 openweathermap 的 apikey ），只不过第一次尝试下载下来点击发现不好用，就想什么鬼啊就删掉了（正如前两次的我）。而这一次我仔细看了之后发现只需要简单配置一下就好了。只不过第三步作者没有明说，对于不了解 API KEY 的朋友确实有点小小的门槛。</p><p>接下来可以对显示内容进行自定义，比如最初步的，可以关注一下：</p><ol><li>第 90 行显示的红字内容，就是 iTermWidget 上面第一行的文字，可以自行调整。</li><li>第 96 行显示的就是第二行的文字， $&#123;NAME&#125; 就是会被TODO第一项所替代，而它左右两个反括号「`」内的红色文字就是剩余的显示文字，可以替换成其他文字或者 EMOJI 表情也可以。比如</li></ol><p>更加「有用」的自定义，当然是替换掉整一行的显示内容啦。比如经过我稍稍的调整，显示出了以下的内容：删掉了一些日历，然后补充了一个展示行情的内容。这一块内容就需要进一步处理码了，我也在思考需要加一些什么内容进去比较好，同时也要想想如何实现以及如何讲述（比如这个显示的行情，我就是把组件库里面的 Crypto 部分码摘过来改吧改吧实现的）。</p><p>希望我能在短期内研究出其他自定义的方式，并且能用简单的不用深入理解码、仅仅靠复制粘贴，就能实现最终的效果。</p><p>这个文章也许有（二），但也不一定。</p><figure class="image ss-img-wrapper image_resized" style="width:471px;"><img src="https://cdn.sspai.com/2022/08/06/f5d966da2123a31527545a5bd1c0e1d9.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/08/06/f5d966da2123a31527545a5bd1c0e1d9.jpeg" referrerpolicy="no-referrer"><figcaption>目前只保留了这三行，未来还会继添加更多信息</figcaption></figure><hr><p>来自 EvanDColeman 的 Cache.js，<a href="https://github.com/evandcoleman/scriptable">https://github.com/evandcoleman/scriptable</a></p><pre class="language-javascript"><code>// NOTE: This script was written by evandcoleman: https://github.com/evandcoleman/scriptable

class Cache &#123;
  constructor(name) &#123;
    this.fm = FileManager.iCloud();
    this.cachePath = this.fm.joinPath(this.fm.documentsDirectory(), name);

    if (!this.fm.fileExists(this.cachePath)) &#123;
      this.fm.createDirectory(this.cachePath);
    &#125;
  &#125;
  async read(key, expirationMinutes) &#123;
    try &#123;
      const path = this.fm.joinPath(this.cachePath, key);
      await this.fm.downloadFileFromiCloud(path);
      const createdAt = this.fm.creationDate(path);

      if (expirationMinutes) &#123;
        if ((new Date()) - createdAt > (expirationMinutes * 60000)) &#123;
          this.fm.remove(path);
          return null;
        &#125;
      &#125;

      const value = this.fm.readString(path);

      try &#123;
        return JSON.parse(value);
      &#125; catch (error) &#123;
        return value;
      &#125;
    &#125; catch (error) &#123;
      return null;
    &#125;
  &#125;
  write(key, value) &#123;
    const path = this.fm.joinPath(this.cachePath, key.replace('/', '-'));
    console.log(`Caching to $&#123;path&#125;...`);

    if (typeof value === 'string' || value instanceof String) &#123;
      this.fm.writeString(path, value);
    &#125; else &#123;
      this.fm.writeString(path, JSON.stringify(value));
    &#125;
  &#125;
&#125;

module.exports = Cache;</code></pre></div><div class="update-details-wrap" data-v-557a067a></div><!----></div><div style="border:1px solid transparent;" data-v-557a067a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-557a067a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>10</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>3</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-7962" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E7%94%A8%20Scriptable%20%E5%81%9A%E4%B8%AA%20iTerm%20%E9%A3%8E%E6%A0%BC%E5%B0%8F%E9%83%A8%E4%BB%B6%E3%80%91iOS%E5%B9%B3%E5%8F%B0%E5%8F%AF%E4%BB%A5%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B0%8F%E9%83%A8%E4%BB%B6%E7%9A%84app%E6%9C%89%E5%BE%88%E5%A4%9A%EF%BC%8C%E6%9C%89%E9%82%A3%E4%B9%88%E5%87%A0%E7%A7%8D%E6%98%AF%E5%92%8C%E4%BB%A3%E7%A0%81%E7%9B%B8%E5%85%B3%E7%9A%84%EF%BC%8C%E4%BE%8B%E5%A6%82JSBox%E3%80%81Taio%E5%92%8C%E6%9C%AC%E6%96%87%E7%9A%84%E8%BF%99%E6%AC%BEScriptable%E3%80%82%E4%B8%8D%E7%94%A8%E7%A0%81%E7%9A%84%E5%B0%8F%E9%83%A8%E4%BB%B6%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F08%2F06%2Fb1f3c88a1933c106874ccb6839dae516.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-9826" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E7%94%A8%20Scriptable%20%E5%81%9A%E4%B8%AA%20iTerm%20%E9%A3%8E%E6%A0%BC%E5%B0%8F%E9%83%A8%E4%BB%B6%E3%80%91iOS%E5%B9%B3%E5%8F%B0%E5%8F%AF%E4%BB%A5%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B0%8F%E9%83%A8%E4%BB%B6%E7%9A%84app%E6%9C%89%E5%BE%88%E5%A4%9A%EF%BC%8C%E6%9C%89%E9%82%A3%E4%B9%88%E5%87%A0%E7%A7%8D%E6%98%AF%E5%92%8C%E4%BB%A3%E7%A0%81%E7%9B%B8%E5%85%B3%E7%9A%84%EF%BC%8C%E4%BE%8B%E5%A6%82JSBox%E3%80%81Taio%E5%92%8C%E6%9C%AC%E6%96%87%E7%9A%84%E8%BF%99%E6%AC%BEScriptable%E3%80%82%E4%B8%8D%E7%94%A8%E7%A0%81%E7%9A%84%E5%B0%8F%E9%83%A8%E4%BB%B6%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            