
---
title: '手把手教你用飞书 Webhook 打造一个消息推送 Bot'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/editor/u_/c4o2rflb34tc99fgtqq0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Thu, 02 Sep 2021 02:05:08 GMT
thumbnail: 'https://cdn.sspai.com/editor/u_/c4o2rflb34tc99fgtqq0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><h3><strong>Matrix 首页推荐</strong></h3><p><a href="https://sspai.com/matrix">Matrix</a> 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。</p><p>文章代表作者个人观点，少数派仅对标题和排版略作修改。</p><hr><h2>前言</h2><p>作为一个互联网的「数字难民」，我最讨厌的就是在工作中使用微信。因为微信本质上并不属于<strong>工作性质</strong>的 IM（Instant Message，即时通讯）工具，但却成为国内大多数领导所偏爱的传声筒：糟糕的文件传输限制、被人诟病的超大空间占用、机械难用的群组管理方式等……微信这些罄竹难书的 N 宗罪无疑早就被和我一样的数字难民们用优美的中国话从产品到人描述了个遍。</p><p>使用了企业微信之后，我发现虽然已经没有微信那样的不堪，勉强能够胜任日常的工作沟通与交流，但我仍觉得似乎被什么东西束缚住了，尤其对于我这种喜欢折腾的人来说少了点自由的 ♂ 气息，比如在所谓的「自动化」方面。</p><p>自动化（Automation）一词其实是一个很大的概念，但顾名思义其实就是将需要人为、机械且重复的行为，通过软件或编码的方式来实现同样的效果，这个过程就是自动化。具体来说就是：每小时给我发送当前的天气预报、每天早晨准时给我发送少数派早报的标题内容、每个周定时备份我 XXX 项目下的所有文件等等。</p><p>因为企业微信面向的主要还是像公司这样的集体组织，无法提供适应个人层面的自动化服务或接口，如果需要进行相关内部的应用开发必须要由公司企业微信的管理员去操作。</p><p>直到我遇上了<a href="https://www.feishu.cn/" target="_blank">飞书</a>。它在满足了日常工作协作的需要的同时，还留有让喜欢折腾的数字玩家们进一步探索的地方，比如：Webhook。</p><h2>创建自定义机器人</h2><p>飞书允许用户在群组中创建一个自定义机器人，将其他渠道的消息通过 Webhook 的方式推送至该群组中。</p><p>Webhook 顾名思义即网络钩子，也称为用户自定义 HTTP 回调函数（user-defined HTTP callbacks），通常用于监听某些行为事件，当事件触发时会向用户指定的目标地址发送信息。</p><p>这段话对于大多数没有计算机基础知识的读者来说可能难以理解，但却无关紧要，因为我们只需要可以将其理解为「中间人」即可：</p><blockquote><p><strong>张三</strong> 到百货商场买东西，<strong>店员</strong> 告知他要买的东西暂时没货了，可以先登记一下他的联系方式，补货后第一时间通知他过来购买。</p></blockquote><blockquote><p>过了一段时间 <strong>进货</strong> 之后，店员根据留下的 <strong>联系方式</strong> 联系了张三，告知其到货了可以过来购买了。</p></blockquote><p>这是我们在日常生活中很常见的一种场景，也和整个 Webhook 的运作流程类似：</p><ul><li>张三：即飞书群</li><li>店员：即 Webhook，用以监听是否进货，并且根据登记的联系方式进行通知</li><li>是否进货：触发条件（Trigger）</li><li>联系方式：目标地址（URL）</li></ul><p>因此，飞书的自定义机器人本质上也就是提供了这样 <strong>「监听-通知」</strong> 的行为逻辑，让用户能够将消息转发到飞书上。</p><p>创建一个自定义机器人的方式很简单，你只需要在飞书界面进行「点击加号-创建群组-设置-群机器人」几步操作。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rflb34tc99fgtqq0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rflb34tc99fgtqq0.png" referrerpolicy="no-referrer"></figure><p>然后再点击「添加机器人」按钮进入到添加界面，选择第一位的「自定义机器人即可」。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rftb34tc9hb98big.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rftb34tc9hb98big.png" referrerpolicy="no-referrer"></figure><p>添加完成之后我们只需要默认下一步即可。</p><h2>定制消息类型</h2><p>创建自定义机器人仅表明我们搭起了一个中转的「驿站」，但我们还需要能够向这个驿站发送相关的消息才能让其帮我们实现转发。</p><p>飞书目前支持的消息类型主要有如文本、富文本、交互式卡片等，不同的消息类型对应着不同格式的 JSON 数据。</p><figure class="table"><table><tbody><tr><td><strong>参数 (msg_type)</strong></td><td><strong>消息类型</strong></td></tr><tr><td>text</td><td>文本</td></tr><tr><td>post</td><td>富文本</td></tr><tr><td>image</td><td>图片</td></tr><tr><td>share_chat</td><td>分享群名片</td></tr><tr><td>interactive</td><td>消息卡片</td></tr></tbody></table></figure><h3>什么是 JSON？</h3><p>JSON（JavaScript Object Notation，即 JavaScript 对象表示法），是目前在 Web 领域里被广泛用于数据传递与交换的文件格式之一。JSON 通常由键值对构成，就像这样：</p><pre class="language-json"><code>&#123;
    "id": 1,
    "name": "100gle",
    "site": "https://sspai.com/u/100gle/posts",
    "social_media": ["sspai", "Github"],
    "product": &#123;
        "name": "Python 自学手册",
        "url": "https://sspai.com/series/148/list"
    &#125;
&#125;
</code></pre><p>而我们的消息也是需要以这种格式来发送，当中包含的是关于该消息的类型、内容、其他参数等信息。</p><h3>普通文本</h3><p>在飞书所支持的几种消息类型里，最简单的莫过于普通文本。其对应的 JSON 格式比较简单：</p><pre class="language-json"><code>&#123;
  "msg_type": "text", // 指定消息类型
  "content": &#123;  // 消息内容主体
    "text": "your-message"
  &#125;
&#125;
</code></pre><p>最后呈现的效果也是我们在日常使用微信沟通时看到的那种样式。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rg5b34tc9c8ndqbg.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rg5b34tc9c8ndqbg.png" referrerpolicy="no-referrer"></figure><h3>富文本</h3><p>如果你需要给消息内容增添一些样式，如链接、图片等，那么你可以选择富文本消息类型。</p><p>富文本主要就类似于 Markdown 的语法，同样具备所见即所得的特点，能够很好地渲染成 HTML 元素。但飞书支持的富文本元素主要就四种：</p><ul><li><code>text</code>：普通文本</li><li><code>a</code>：超链接</li><li><code>at</code>：<code>@</code> 符号</li><li><code>img</code>：图片</li></ul><p>因为 <code>at</code> 标签需要获取到目标用户的 ID 参数而 <code>img</code> 需要事先将图片上传到其他接口，所以会相对复杂一些，有需要的朋友可以自己探索。</p><p>相比于普通文本样式来说，富文本样的 JSON 样式相对复杂一些：</p><pre class="language-json"><code>&#123;
  "msg_type": "post",
  "content": &#123;
    "post": &#123;
      "zh-CN": &#123;
        "title": "富文本消息测试！",
        "content": [
          [
            &#123;
              "tag": "text",
              "text": "你的小可爱上线了！"
            &#125;,
            &#123;
              "tag": "a",
              "text": "点击查看",
              "href": "https://sspai.com/u/100gle/updates"
            &#125;
          ]
        ]
      &#125;
    &#125;
  &#125;
&#125;
</code></pre><p>由于飞书支持 i18n（internationalization）国际化显示，所以需要将内容填写在对应语言下面，比如上述的<code>zh-CN</code>。但如果我们没有翻译成其他语言的需要，那就只需要在例子中的 <code>zh-CN</code> 的部分填写内容即可：</p><ul><li><code>title</code> 表示标题</li><li><code>content</code> 表示所有内容，每一行内容是包含了若干元素标签的数组</li></ul><p>最后就可以呈现出如下样式：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rg5b34tc9hb98bj0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rg5b34tc9hb98bj0.png" referrerpolicy="no-referrer"></figure><h3>消息卡片</h3><p>消息类型里最为复杂的是交互式消息卡片。</p><p>因为消息卡片的规范较多，以至于飞书官方专门用了一定篇幅的 <a href="https://open.feishu.cn/document/ukTMukTMukTM/uczM3QjL3MzN04yNzcDN?op_tracking=hc" target="_blank">文档</a> 来告知开发者如何去设计消息卡片。</p><p>简单来说，消息卡片主要由两部分构成：<strong>消息头</strong>和<strong>消息主体内容</strong>。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rgdb34tc9c8ndqc0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rgdb34tc9c8ndqc0.png" referrerpolicy="no-referrer"><figcaption>图源<a href="https://open.feishu.cn/document/ukTMukTMukTM/uczM3QjL3MzN04yNzcDN" target="_blank">飞书开放平台文档</a></figcaption></figure><p>基本的消息卡片结构所对应的 JSON 样式为：</p><pre class="language-json"><code>&#123;
  "msg_type": "interactive",
  "card": &#123;
    "config": &#123;
      "wide_screen_mode": true
    &#125;,
    "header": &#123;
      "title": &#123;
        "tag": "plain_text",
        "content": "this is header" // 标题内容
      &#125;,
      "template": "red" // 标题主题颜色
    &#125;,
    "elements": [
      // 卡片消息主体内容
      // &#123;module-1&#125;,
      // &#123;module-2&#125;,
      // &#123;module-3&#125;,
      // ......
      // &#123;module-N&#125;
    ]
  &#125;
&#125;
</code></pre><p>消息头主要就是带有色块的标题，用以增强信息的视觉锚点<sup class="ss-footnote" href="https://open.feishu.cn/document/ukTMukTMukTM/ukTNwUjL5UDM14SO1ATN" title="卡片标题-最佳实践" footnote-id="1">1</sup>，对应 <code>header</code> 部分的内容。通常我们只需要填写当中的 <code>content</code> 的标题内容以及 <code>template</code> 标题主题颜色即可定下消息卡片的标题展示效果。</p><p>让消息卡片变得复杂的原因是在于消息主体内容，因为主体内容从形式上就像是 HTML 元素，可以进行多种组合，所以这一部分主要都在 <code>elements</code> 中进行填写。</p><p>但在实际的使用过程中我们不会手动去编写对应的消息内容，而是通过飞书的 <a href="https://open.feishu.cn/tool/cardbuilder?from=cotentmodule" target="_blank">卡片搭建工具</a> 来帮助我们做出想要的样式。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rglb34tc9c8ndqcg.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rglb34tc9c8ndqcg.png" referrerpolicy="no-referrer"></figure><p>在这个设计工具中，我们可以在「模块组件」中去搭建适合自己需要的消息卡片；同时，我们也可以在「卡片模板」中选择飞书为我们已经内置好的卡片模板，根据自己的需要去对模板进行调整。</p><p>但无论你是打算用哪种方式，最后只需要能在预览中显示无误，就可以直接将右侧的代码预览中的内容复制粘贴到前面基础结构 JSON 中的 <code>card</code> 部分即可。</p><p>这里我就基于前面已选择的模板进行简单调整，然后实现一个少数派社区文章推荐的消息卡片样式：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rh5b34tc99fgtqqg.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rh5b34tc99fgtqqg.png" referrerpolicy="no-referrer"></figure><p>最后将右侧的代码直接复制拷贝，然后经由程序推送至 Webhook 后再转发到飞书上。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rhdb34tc98oi4060.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rhdb34tc98oi4060.png" referrerpolicy="no-referrer"></figure><h2>为你的消息机器人加上安全设置</h2><p>由于只要我们通过向 Webhook 地址发送网络请求就能够将消息推送至飞书，因此倘若不经意间 Webhook 地址被泄露在互联网上，那么很有可能会接收到许多垃圾消息，也容易埋下未知的信息安全隐患。这就好比你出门时却不锁门一样让人惴惴不安。</p><p>因此在使用飞书 Webhook 推送消息的基础上，最好是加上相关的安全策略或设置以提升安全性。在飞书的官方文档里飞书提供了三种安全策略，并且三种方式可以<strong>叠加设置</strong>。安全等级由低到高依次是：</p><ol><li><strong>自定义关键词</strong>：只推送包含特定关键词的消息</li><li><strong>IP 白名单</strong>：只推送由白名单 IP 发送的消息</li><li><strong>安全密钥</strong>：只推送带有指定密钥信息的消息</li></ol><p>其中，前两种方式比较简单，我们只需要勾选之后就可以直接设置，但添加的数量最大限制都为 10 个。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rhlb34tc98oi406g.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rhlb34tc98oi406g.png" referrerpolicy="no-referrer"></figure><p>最后一种方式需要我们能够生成密钥，并在推送消息的 HTTP 请求中携带上关于密钥的信息参数。生成密钥最快捷的方式就是通过代码来实现，因为飞书开发者文档中给出了不同编程语言的示例 Demo，虽然可能不一定覆盖到所有编程语言，但其生成密钥的方式都是大同小异的：</p><ol><li>将当前时间戳和签名校验码通过换行符 <code>\n</code> 拼接在一起作为密钥字符串签名</li><li>使用 <a href="https://zh.wikipedia.org/wiki/HMAC" target="_blank">HMAC-SHA256 算法</a> 对该字符串签名进行加密</li><li>最后使用 <a href="https://zh.wikipedia.org/wiki/Base64" target="_blank">Base64 编码</a> 对加密后的字符串签名进行编码，便于作为参数传递</li></ol><p>经过以上三步生成密钥之后，我们就可以在发送消息推送时带上安全密钥以便飞书服务器校验。这里我基于飞书官方的 Python 示例进行简单修改，仅供参考：</p><pre class="language-python"><code>#!/usr/bin/env python3
# coding:utf-8

# feishu.py

import base64
import hashlib
import hmac
from datetime import datetime

import requests

WEBHOOK_URL = "your-webhook-url"
WEBHOOK_SECRET = "your-webhook-sign-secret"
timestamp = int(datetime.now().timestamp())

def gen_sign(secret):
    # 拼接时间戳以及签名校验
    string_to_sign = '&#123;&#125;\n&#123;&#125;'.format(timestamp, secret)

    # 使用 HMAC-SHA256 进行加密
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()

    # 对结果进行 base64 编码
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign

def main():
    sign = gen_sign(WEBHOOK_SECRET)
    params = &#123;
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "text",
        "content": &#123;"text": "点火发射！"&#125;,
    &#125;

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：&#123;result['msg']&#125;")
        return
    print("消息发送成功")

if __name__ == '__main__':
    main()
</code></pre><p>有了校验之后即便 Webhook 地址泄露了，但只要没有拿到我们的签名校验就无法生成密钥，也就无法往我们的消息机器人推送消息了，这就使得安全性得到进一步保障。</p><p>但以上生成密钥的过程都是在程序中完成，如果你是想要在开启签名校验的安全设置情况下，使用其他 APP 将消息转发至飞书，那么需要对应的 APP 支持密钥生成的同时，还需要能定制对应的 JSON 请求体。</p><h2>应用</h2><p>飞书群组里的自定义机器人的功能可能没有像 Telegram Bot 那样丰富，其主要用途还是作为一个<strong>消息推送</strong>的中心，将其他来源的信息或消息经过 Webhook 转发到飞书群组里，所以像今日运势、流量监控、异常警告等场景就非常适合使用飞书自定义机器人来实现自动化。</p><p>实现自动化的途径可以通过代码、APP 或是其他第三方服务，根据个人需要去选择、尝试。</p><h3>自动推送消息</h3><p>作为一个每周五下班都不带电脑回家的开发 boy 来说，为了避免有时需要改 Bug 或是访问公司服务器资源时我需要用到公司电脑的情况发生，我通常都会使用公司的 VPN 和微软的远程桌面工具连接到我在公司所使用的 Windows 笔记本电脑，这样我就只需要远程操作即可。</p><p>但实现远程操作的前提是：我必须知道我所使用的那台笔记本的内网 IP 地址是什么。</p><p>所以我就根据飞书的开发文档用 Python 编写了一个脚本，接着配合微软的任务计划程序，在每周五下午 19 点时运行并获取电脑当前的内网 IP 地址，并通过自定义机器人推送到飞书。</p><p>这里我基于前面安全设置部分的代码进行了一些改动，将其封装了进了一个名为 <code>LarkBot</code> 的类中，所以这个类包含前面所涉及的安全校验和消息发送两部分功能：</p><pre class="language-python"><code># !/usr/bin/env python3
# coding:utf-8

# larkbot.py

import base64
import hashlib
import hmac
from datetime import datetime

import requests

class LarkBot:
    def __init__(self, secret: str) -> None:
        if not secret:
            raise ValueError("invalid secret key")
        self.secret = secret

    def gen_sign(self, timestamp: int) -> str:
        string_to_sign = '&#123;&#125;\n&#123;&#125;'.format(timestamp, self.secret)
        hmac_code = hmac.new(
            string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
        ).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')

        return sign

    def send(self, content: str) -> None:
        timestamp = int(datetime.now().timestamp())
        sign = self.gen_sign(timestamp)

        params = &#123;
            "timestamp": timestamp,
            "sign": sign,
            "msg_type": "text",
            "content": &#123;"text": content&#125;,
        &#125;
        resp = requests.post(url=WEBHOOK_URL, json=params)
        resp.raise_for_status()
        result = resp.json()
        if result.get("code") and result["code"] != 0:
            print(result["msg"])
            return
        print("消息发送成功")
</code></pre><p>由于我是用代码来实现，所以创建密钥会相对方便，因此开启签名校验的同时，在创建 <code>LarkBot</code> 的实例化对象的过程中携带上安全校验的字符串代码，否则会抛出异常；</p><p>其次，在前面一部分章节示例中的 <code>main()</code> 函数代码都被封装到了 <code>send()</code> 方法里，于是我们只需要创建好 <code>LarkBot</code> 对象后再调用该方法并传入一个想要发送的内容字符串，就可以将消息推送至飞书：</p><pre class="language-python"><code>def main():
    WEBHOOK_SECRET = "your-webhook-secret"
    bot = LarkBot(secret=WEBHOOK_SECRET)
    bot.send(content="我是一只高级鸽子！")

if __name__ == '__main__':
    main()
</code></pre><p>当中的 <code>content</code> 部分是可替换的，你可以替换成符合你需要的内容，比如今日运势、头条文章、热搜 TOP10 等等，只要你能获取得到相关内容或数据，并转换成字符串即可。但因为我是需要获取到工位上的电脑 IP，所以上面部分就改成了：</p><pre class="language-python"><code>def main():

    import re
    import subprocess

    WEBHOOK_SECRET = "...."

    # 利用正则表达式获取 IP 字符串
    IPV4_PATTERN = r"IPv4.*: (?P.*)\n"
    ipconfig = subprocess.run(
      "ipconfig", capture_output=True, text=True).stdout
    ip = re.search(IPV4_PATTERN, ipconfig).group("ip")

    bot = LarkBot(secret=WEBHOOK_SECRET)
    bot.send(content=f"当前工位的电脑 IP 是：&#123;ip&#125;")

if __name__ == '__main__':
    main()
</code></pre><p>这里我通过调用 Windows 上查看网络内容的 <code>ipconfig</code> 命令获取到输出的内容后，再通过正则表达式去将包含特定 IP 的那一串文本中的数字部分抓出来，并推送。</p><p>之后我将整个脚本保存成一个 <code>.py</code> 代码文件后，通过定时任务添加计划，当达到触发时限，则会通过指定的 Python 解释器可执行程序来执行该脚本。</p><h3>Webhook 转发 Webhook</h3><p>在少数派的作（鸽）者（子）群中曾看到了我派编辑部「六个汉堡」代言人路中南想要通过<strong>通知滤盒（Android）</strong>这一 APP 将群里的一些消息转发至飞书的想法，也这是飞书自定义机器人一个不错的适用场景。</p><span class="ss-application" app-id="15141"> </span><p> </p><p>关联阅读：</p><ul><li><a href="https://sspai.com/post/59502" target="_blank">App+1 | 解决 Android 通知管理难题，用正则表达式过滤无关推送：通知滤盒</a></li><li><a href="https://sspai.com/post/60536" target="_blank">微信群聊不是法外之地：用通知滤盒降低敏感词「炸群」风险</a></li></ul><p>因为通知滤盒在 2.0 版本之后有了添加了 Webhook 的功能（需要付费订阅或买断高级版），所以本质上也是和飞书类似，将过滤的消息进行转发。</p><p>需要说明的是：由于通知滤盒的 Webhook 功能<strong>仍处于开放测试阶段</strong>，尚有不少的 BUG，仅能发送 POST 请求，而无法发送 GET 请求；并且目前也无法在通知滤盒里直接定制发送的请求体内容，因此只能使用飞书 <a href="https://www.feishu.cn/hc/zh-CN/articles/360024984973#lineguid-PTu2Sl" target="_blank">旧版的自定义机器人</a> 来实现消息转发。</p><p>当我们进入到通知滤盒后，点击左下角的规则，并选择「增强-Webhook」创建一个新的配置。在填写配置信息的过程中，可以根据你自己的实际需要来指定特定特定的 APP、内容和时间，以及手机处于何种状态时才会转发的条件，还有最后要转发的目标 Webhook 地址。</p><p>因为是转发微信的相关消息，所以这里我将 APP 设置为包含微信，然后内容设置为一串测试的正则表达式。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2rhtb34tc9c8ndqd0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/editor/u_/c4o2rhtb34tc9c8ndqd0.png" referrerpolicy="no-referrer"></figure><p>保存之后我们只要每次接收到了相关消息，通知滤盒就会直接将消息转发到飞书上了。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_/c4o2ri5b34tc9c8ndqdg.gif" data-original="https://cdn.sspai.com/editor/u_/c4o2ri5b34tc9c8ndqdg.gif" referrerpolicy="no-referrer"></figure><p>除了消息滤盒，你还可以将其替换成 <strong>任意支持 Webhook</strong> 的 APP 或是服务，比如 QQ、IFTTT、Github 等，实现 Webhook 转 Webhook 最终将消息发送至飞书的「套娃玩法」。</p><h2>结尾</h2><p>长久以来我一直觉得国内的软件或平台在自动化和 API 开放化上做得比国外的差：</p><ul><li>一方面，厂商都不愿将成本投入到这只属于「少数玩家」的需求开发。毕竟有自动化需求的往往只是一小撮人，而这部分功能无论是开发还是维护却都是有着不小的成本开销，收益不成正比；</li><li>另一方面，就是想要实现「生态垄断」。无论是链接跳转还是下载 APP，处处表露着厂商想要获取流量并构造自己生态（或服务）壁垒的封闭行径，而开放就意味着会造成用户流失。</li></ul><p>所以有的时候我很喜欢 Telegram、Slack、Todolist、Toggl 等软件有着很好开放性，在能够集成很多第三方软件的同时，又放开 API 并有着丰富的文档供喜欢折腾的玩家们去自由发挥。</p><p>而飞书是国内为数不多具有开放性的工具或平台之一。</p><p>相比于微信、企业微信来说尽管它可能还只是个勇于挑战「老大哥」的「黄毛小子」，但在使用的过程中不难发现它确实解决掉了一些我们在使用「垄断式」即时通讯软件的痛点，也满足了「少数派玩家」们折腾的心愿。</p><p>因此无论是像公司这样的集体组织，还是像我们一样的独立个人用户，都能在日常使用飞书的过程中受益。</p><p>> 下载少数派 <a href="https://sspai.com/page/client">客户端 </a>、关注 <a href="https://sspai.com/s/J71e">少数派公众号 </a>，了解更妙的数字生活 🍃</p><p>> 想申请成为少数派作者？<a href="https://sspai.com/apply/writing" target="_blank">冲！</a></p></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>40</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-4019" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E7%94%A8%E9%A3%9E%E4%B9%A6%20Webhook%20%E6%89%93%E9%80%A0%E4%B8%80%E4%B8%AA%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%20Bot%E3%80%91%E4%BD%9C%E4%B8%BA%E4%B8%80%E4%B8%AA%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E3%80%8C%E6%95%B0%E5%AD%97%E9%9A%BE%E6%B0%91%E3%80%8D%EF%BC%8C%E6%88%91%E6%9C%80%E8%AE%A8%E5%8E%8C%E7%9A%84%E5%B0%B1%E6%98%AF%E5%9C%A8%E5%B7%A5%E4%BD%9C%E4%B8%AD%E4%BD%BF%E7%94%A8%E5%BE%AE%E4%BF%A1%E3%80%82%E5%9B%A0%E4%B8%BA%E5%BE%AE%E4%BF%A1%E6%9C%AC%E8%B4%A8%E4%B8%8A%E5%B9%B6%E4%B8%8D%E5%B1%9E%E4%BA%8E%E7%9C%9F%E6%AD%A3%E6%84%8F%E4%B9%89%E4%B8%8A%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%80%A7%E8%B4%A8%E7%9A%84IM%EF%BC%88InstantMessage%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F09%2F02%2F672c8d0495ff0d57491213f5369ceb5d.jpeg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-4298" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E7%94%A8%E9%A3%9E%E4%B9%A6%20Webhook%20%E6%89%93%E9%80%A0%E4%B8%80%E4%B8%AA%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%20Bot%E3%80%91%E4%BD%9C%E4%B8%BA%E4%B8%80%E4%B8%AA%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E3%80%8C%E6%95%B0%E5%AD%97%E9%9A%BE%E6%B0%91%E3%80%8D%EF%BC%8C%E6%88%91%E6%9C%80%E8%AE%A8%E5%8E%8C%E7%9A%84%E5%B0%B1%E6%98%AF%E5%9C%A8%E5%B7%A5%E4%BD%9C%E4%B8%AD%E4%BD%BF%E7%94%A8%E5%BE%AE%E4%BF%A1%E3%80%82%E5%9B%A0%E4%B8%BA%E5%BE%AE%E4%BF%A1%E6%9C%AC%E8%B4%A8%E4%B8%8A%E5%B9%B6%E4%B8%8D%E5%B1%9E%E4%BA%8E%E7%9C%9F%E6%AD%A3%E6%84%8F%E4%B9%89%E4%B8%8A%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%80%A7%E8%B4%A8%E7%9A%84IM%EF%BC%88InstantMessage%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            