
---
title: '利用 n8n 打造飞书 RSS 推送机器人'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/05/16/7d985623e60bdcbc40efad212c35d9cd.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Tue, 17 May 2022 02:35:26 GMT
thumbnail: 'https://cdn.sspai.com/2022/05/16/7d985623e60bdcbc40efad212c35d9cd.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-6dd0eb6a><div class="update-wrap" data-v-6dd0eb6a></div><div class="content wangEditor-txt minHeight" data-v-6dd0eb6a><h2>前言</h2><p>本文介绍了基于开源自动化平台 n8n 搭建自动化流程，实现监控 RSS 更新并推送到飞书消息的功能。</p><p>文末会列举一些实现此工作流的其他方式，包括发送请求和接收提醒的手段。与此同时，n8n 还可以通过模块组合，实现更多更复杂的功能，本文只作为抛砖引玉。</p><p>阅读本文可能需要一定 Linux 基础知识。</p><h2>n8n 是什么</h2><p>n8n 是一个开源的自动化流程搭建工具，可以实现类似 IFTTT 的效果，比如「如果明天下雨，就推送要带伞的消息」。优点是开源、可以自己部署并将信息都储存在本地，同时可以与 Github、Telegram、Slack 等各种服务实现联动，以搭建自动化工作流。</p><h2>利用 Docker 安裝 n8n</h2><p>n8n 可以直接下载 Win 或是 Mac 版本，快速在本地使用，但如果想更稳定地长期运行，更适合部署在云服务器、树莓派或 NAS 等工具上。</p><p>这里以在云服务器上使用 Docker 进行部署为例，更多安装方式可参考 <a href="https://docs.n8n.io/hosting/installation/">Installation guides for n8n</a>。</p><p>假设已经安装好了 Docker，那么 n8n 的部署就非常简单，先新建一个文件夹储存数据。</p><pre class="language-shell"><code># 创建数据储存文件夹
mkdir ~/n8n-data</code></pre><p>复制运行下面的代码，利用 Docker 安装 n8n。如果云服务器有防火墙，需要把对应的端口打开，这里需要打开云服务器的 TCP 端口 <code>5678</code>。</p><pre class="language-shell"><code># 利用Docker安装运行n8n
docker run -d \
--name n8n --restart unless-stopped \
-p 5678:5678 \
-v ~/n8n-data:/home/node/.n8n \
-e GENERIC_TIMEZONE="Asia/Shanghai" \
n8nio/n8n </code></pre><p>稍作等待，等 Docker 安装完成后，如果一切顺利，访问 <code>服务器ip地址:5678</code> 就能看到 n8n 的运行页面了，初次进入需要创建账号密码。</p><figure class="image ss-img-wrapper image_resized" style="width:664px;"><img src="https://cdn.sspai.com/2022/05/16/7d985623e60bdcbc40efad212c35d9cd.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/7d985623e60bdcbc40efad212c35d9cd.png" referrerpolicy="no-referrer"><figcaption>n8n 主界面</figcaption></figure><p>点击右上角的 New blank workflow 即可开始创建，也可以从软件提供的 Workflow 示例中，选择自己想部署的自动化流程。</p><p>这里以搭建一个 RSS 更新自动推送到飞书的机器人为例，展示 n8n 的一些使用方式。</p><h2>搭建飞书 RSS 推送机器人</h2><p>以下是我配置好的一个流程模板，复制以下内容粘贴到 n8n 新建 workflow 的页面。</p><pre class="language-javascript"><code>&#123;
  "nodes": [
    &#123;
      "parameters": &#123;
        "url": "https://sspai.com/feed"
      &#125;,
      "name": "RSS Feed Read",
      "type": "n8n-nodes-base.rssFeedRead",
      "typeVersion": 1,
      "position": [
        160.5,
        440
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "conditions": &#123;
          "number": [
            &#123;
              "value1": "=&#123;&#123;new Date($node[\"Latest Read\"].data[\"latestRead\"]).getTime()&#125;&#125;",
              "value2": "=&#123;&#123;new Date($node[\"RSS Feed Read\"].data[\"isoDate\"]).getTime()&#125;&#125;"
            &#125;
          ],
          "boolean": [],
          "string": [
            &#123;
              "value1": "=&#123;&#123;$json[\"title\"]&#125;&#125;",
              "operation": "contains"
            &#125;
          ]
        &#125;
      &#125;,
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        560,
        440
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "functionCode": "const staticData = this.getWorkflowStaticData('global');\n\nif (items.length > 0) &#123;\n  staticData.latestRead = items[0].json.isoDate || staticData.latestRead;\n&#125;\n\n\nreturn items;"
      &#125;,
      "name": "Write Latest Read",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        760,
        340
      ]
    &#125;,
    &#123;
      "parameters": &#123;&#125;,
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "typeVersion": 1,
      "position": [
        750,
        580
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "triggerTimes": &#123;
          "item": [
            &#123;
              "mode": "everyX",
              "value": 1
            &#125;
          ]
        &#125;
      &#125;,
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "typeVersion": 1,
      "position": [
        -40,
        440
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "requestMethod": "POST",
        "options": &#123;
          "batchInterval": 3000,
          "batchSize": 1
        &#125;,
        "bodyParametersUi": &#123;
          "parameter": [
            &#123;
              "name": "msg_type",
              "value": "interactive"
            &#125;,
            &#123;
              "name": "card",
              "value": "=&#123;\n  \"config\": &#123;\n    \"wide_screen_mode\": true\n  &#125;,\n  \"header\": &#123;\n    \"template\": \"black\",\n    \"title\": &#123;\n      \"content\": \"&#123;&#123;$json[\"title\"]&#125;&#125;\",\n      \"tag\": \"plain_text\"\n    &#125;\n  &#125;,\n  \"elements\": [\n    &#123;\n      \"tag\": \"div\",\n      \"text\": &#123;\n        \"content\": \"&#123;&#123;$json[\"contentSnippet\"]&#125;&#125;\",\n        \"tag\": \"lark_md\"\n      &#125;\n    &#125;,\n    &#123;\n      \"tag\": \"hr\"\n    &#125;,\n    &#123;\n      \"elements\": [\n        &#123;\n          \"content\": \"[阅读原文](&#123;&#123;$json[\"link\"]&#125;&#125;)\",\n          \"tag\": \"lark_md\"\n        &#125;\n      ],\n      \"tag\": \"note\"\n    &#125;\n  ]\n&#125;"
            &#125;
          ]
        &#125;,
        "headerParametersUi": &#123;
          "parameter": [
            &#123;
              "name": "Content-Type",
              "value": "application/json"
            &#125;
          ]
        &#125;
      &#125;,
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1000,
        340
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "functionCode": "const staticData = this.getWorkflowStaticData('global');\n\nlatestRead = staticData.latestRead;\n\nfor (let item of items) &#123;\n  item.json.latestRead = latestRead || '2022-05-05';\n  //item.json[\"content:encodedSnippet\"] = item.json[\"content:encodedSnippet\"].replace(/[\\r\\n]/g,\"\\\\n\");\n&#125;\n\nreturn items;"
      &#125;,
      "name": "Latest Read",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        360,
        440
      ]
    &#125;
  ],
  "connections": &#123;
    "RSS Feed Read": &#123;
      "main": [
        [
          &#123;
            "node": "Latest Read",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;,
    "IF": &#123;
      "main": [
        [
          &#123;
            "node": "Write Latest Read",
            "type": "main",
            "index": 0
          &#125;
        ],
        [
          &#123;
            "node": "NoOp",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;,
    "Write Latest Read": &#123;
      "main": [
        [
          &#123;
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;,
    "Cron": &#123;
      "main": [
        [
          &#123;
            "node": "RSS Feed Read",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;,
    "Latest Read": &#123;
      "main": [
        [
          &#123;
            "node": "IF",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;
  &#125;
&#125;</code></pre><p>粘贴后可以看到如下的界面：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/b611439eb6277acb1073574f95078282.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/b611439eb6277acb1073574f95078282.png" referrerpolicy="no-referrer"><figcaption>粘贴代码得到的 RSS 推送工作流</figcaption></figure><p>这里有几处可以配置，第一处是 <strong>Cron</strong>，设置自动化流程触发的频率，每隔 X 时间间隔运行一次，图中设置为每隔一小时运行。在获取 RSS 时，运行频率不宜过高。如果访问过于频繁，一方面会给对方服务器造成较大负担，同时可能被服务器禁止访问。</p><figure class="image ss-img-wrapper image_resized" style="width:300px;"><img src="https://cdn.sspai.com/2022/05/16/8e0c0c70dc86fc3237706969083cbb31.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/8e0c0c70dc86fc3237706969083cbb31.png" referrerpolicy="no-referrer"><figcaption>Cron 模块设置触发频率</figcaption></figure><p>第二个是在 <strong>RSS Feed Read</strong> 处，填写想订阅的 RSS 地址，这里以少数派 RSS 为例，填写完后点击Excute node，先运行一次获取数据，方便后续设置。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/a8a614d6d4211892b1dbed8f2b9e5939.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/a8a614d6d4211892b1dbed8f2b9e5939.png" referrerpolicy="no-referrer"><figcaption>在 URL 处填写想订阅的 RSS 源</figcaption></figure><p>第三处（可选）<strong>IF</strong> 处，设置是否需要针对标题或内容等进行过滤，默认不过滤。</p><figure class="image ss-img-wrapper image_resized" style="width:299px;"><img src="https://cdn.sspai.com/2022/05/16/a89be40e644f4a4ed347967d7caafb77.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/a89be40e644f4a4ed347967d7caafb77.png" referrerpolicy="no-referrer"><figcaption>IF 模块进行条件判断</figcaption></figure><p>这时先转到飞书，在<strong>飞书桌面端</strong>，打开一个群（建议先创建一个单人的群进行调试），打开<strong>设置</strong>，找到<strong>群机器人</strong>，并点击<strong>添加机器人</strong>，选择自定义机器人加入群聊，详细操作可以参照 <a href="https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN?lang=zh-CN">飞书自定义机器人指南</a>。</p><figure class="image ss-img-wrapper image_resized" style="width:484px;"><img src="https://cdn.sspai.com/2022/05/16/115af9bfdb812a1911f46d84618cd0f3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/115af9bfdb812a1911f46d84618cd0f3.png" referrerpolicy="no-referrer"><figcaption>取得飞书自定义机器人 webhook 地址</figcaption></figure><p>最后在 <strong>HTTP Request</strong> 处填入飞书机器人 webhook 地址。</p><figure class="image ss-img-wrapper image_resized" style="width:298px;"><img src="https://cdn.sspai.com/2022/05/16/e7b758a0638da105cf2f1d2ebb5f8cf3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/e7b758a0638da105cf2f1d2ebb5f8cf3.png" referrerpolicy="no-referrer"><figcaption>HTTP Request 模块发送 HTTP 请求</figcaption></figure><p>填写完成后 Excute node 尝试运行，一切顺利的话就能在飞书中看到推送来的RSS消息了。</p><figure class="image ss-img-wrapper image_resized" style="width:300px;"><img src="https://cdn.sspai.com/2022/05/16/1857b90061db3560b4d8d546b80be328.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/1857b90061db3560b4d8d546b80be328.jpeg" referrerpolicy="no-referrer"><figcaption>机器人在飞书中推送了消息卡片</figcaption></figure><p>这里使用了卡片的形式展示消息，若是想调整消息展示样式，可以参考少数派文章 <a href="https://sspai.com/post/68578">手把手教你用飞书 Webhook 打造一个消息推送 Bot</a>。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/259e637689f7b363310c9f7efe289e44.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/259e637689f7b363310c9f7efe289e44.png" referrerpolicy="no-referrer"><figcaption>配置过程一图流</figcaption></figure><h2>消息机器人安全设置</h2><p>由于采用 Webhook 的形式，请务必保管好 Webhook 链接，如果泄露可能会导致被推送垃圾信息。为了进一步加道保险，飞书提供了三种安全设置方式，分别是<strong>自定义关键词</strong>、<strong>IP 白名单</strong>和<strong>签名校验</strong>。</p><p>前两种方式非常好理解，也都很好设置。自定义关键词是只有当消息中至少含有一个预设的关键词时，才会进行消息推送；IP 白名单则是只推送名单中来源的 IP 所发送的请求。但是这两种方式也有一定的局限性：</p><ul><li>关键词有时使消息不够简洁</li><li>部署在本地树莓派等设备上时，IP 地址不固定，无法指定</li><li>关键词和 IP 白名单各自最多只能添加十个条目</li></ul><p>因此这里详细介绍一下在 n8n 中进行签名校验的配置方式。飞书的签名需要将「timestamp + "\n" + 密钥」组合起来当作签名密钥，采用 Hmac SHA256 算法计算签名，再进行 Base64 编码。在发送消息请求时，需要增加对应的 <code>timestamp</code> 和 <code>sign</code>  字段。</p><pre class="language-javascript"><code>// 开启签名验证后发送文本消息的请求示例
&#123;
        "timestamp": "1599360473",
        "sign": "xxxxxxxxxxxxxxxxxxxxx",
        "msg_type": "text",
        "content": &#123;
                "text": "The message content is here"
        &#125;
&#125;</code></pre><p>在 n8n 中，可以使用 <strong>Crypto</strong> 模块利用密钥生成签名，复制以下代码粘贴到配置界面，可以得到生成飞书签名用的模块组合。</p><pre class="language-javascript"><code>&#123;
  "nodes": [
    &#123;
      "parameters": &#123;
        "action": "hmac",
        "type": "SHA256",
        "value": "=&#123;&#123;''&#125;&#125;",
        "dataPropertyName": "sign",
        "secret": "=&#123;&#123;$json[\"timestamp\"]+'\\n'+$json[\"secret\"]&#125;&#125;",
        "encoding": "base64"
      &#125;,
      "name": "Crypto",
      "type": "n8n-nodes-base.crypto",
      "typeVersion": 1,
      "position": [
        -80,
        440
      ]
    &#125;,
    &#123;
      "parameters": &#123;
        "values": &#123;
          "string": [
            &#123;
              "name": "timestamp",
              "value": "=&#123;&#123;Math.round(new Date().getTime()/1000)&#125;&#125;"
            &#125;,
            &#123;
              "name": "secret"
            &#125;
          ]
        &#125;,
        "options": &#123;&#125;
      &#125;,
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        -280,
        440
      ]
    &#125;
  ],
  "connections": &#123;
    "Set": &#123;
      "main": [
        [
          &#123;
            "node": "Crypto",
            "type": "main",
            "index": 0
          &#125;
        ]
      ]
    &#125;
  &#125;
&#125;</code></pre><p>将上面新增的两个模块按下图方式进行拖拽连接：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/138dfcccfb035d3d8d00aba51871391d.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/138dfcccfb035d3d8d00aba51871391d.png" referrerpolicy="no-referrer"><figcaption>拖拽模块两端的点即可将模块进行连接</figcaption></figure><p>从飞书机器人设置界面中，勾选<strong>签名校验</strong>得到密钥，填写在 <strong>Set</strong> 模块中。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/3233c38919b18b0b6d07ae8f4dd806a0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/3233c38919b18b0b6d07ae8f4dd806a0.png" referrerpolicy="no-referrer"><figcaption>勾选签名校验后记得点保存</figcaption></figure><p>接下来将 <strong>Latest Read</strong> 模块中的代码替换为以下内容，储存计算出的签名，方便在请求的时候调用。</p><pre class="language-json"><code>// JS code in the Latest Read Module
const staticData = this.getWorkflowStaticData('global');

latestRead = staticData.latestRead;

for (let item of items) &#123;
  item.json.latestRead = latestRead || '2022-05-05';
  item.json.timestamp = $item("0").$node["Crypto"].json["timestamp"];
  item.json.sign = $item("0").$node["Crypto"].json["sign"];
&#125;

return items;</code></pre><p>最后在 <strong>HTTP Request</strong> 模块中增加校验用的字段：Body Parameters → Add Parameter，添加两个参数，Name 分别为 <code>timestamp</code> 和 <code>sign</code>，Value 处点击右侧 Add Expression，分别选择两个对应字段的值。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/e65578dd8092858cb4664d55f60ef0ce.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/e65578dd8092858cb4664d55f60ef0ce.png" referrerpolicy="no-referrer"><figcaption>选择变量的时候可以逐级展开列表，找到目标字段</figcaption></figure><p>这样一番倒腾，给飞书机器人模块增加了签名校验，使得信息推送更加安全。当一切配置妥当后，别忘了点击界面右上角的激活，让工作流开始自动运行。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/05/16/df0afac5f82d8849ed77812f91712cd1.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/05/16/df0afac5f82d8849ed77812f91712cd1.png" referrerpolicy="no-referrer"><figcaption>n8n 配置飞书密钥验证一图流</figcaption></figure><h2>后记</h2><p>本文介绍了如何用 n8n 打造一个飞书 RSS 推送机器人。订阅什么样的 RSS 来源，可以是网站自身提供的 RSS 地址，也可以利用 RSShub 将各种奇怪的网站转化为 RSS，甚至是利用 kill-the-newsletter 将任意 Newsletter 邮件转化为 RSS 进行追踪。</p><p>同时，实现类似工作流的手段还有很多。对于 n8n 这部分，可以使用 IFTTT、Integrately，或是 Github Action 等，实现工作流中「监控 RSS 更新并发送 Webhook 请求」这部分；对于接收提醒，文中利用了飞书作为展示消息的界面，而 n8n 也支持连接到 Telegram、Slack 等通讯软件，或是通过 Send Email 模块实现邮件通知，以及发送到 Cubox、flomo 等各种支持 Webhook 的工具中。</p><p>更多功能，更多组合，尽请探索，把闲置的云服务器或是积灰的树莓派等折腾起来吧。</p><h2>参考资料</h2><ul><li><a href="https://sspai.com/post/68578" target="_blank">手把手教你用飞书 Webhook 打造一个消息推送 Bot - 少数派</a></li><li><a href="https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN?lang=zh-CN" target="_blank">自定义机器人指南 - 飞书开放平台</a></li><li><a href="https://www.jkg.tw/p3609/" target="_blank">輕鬆架一套類 IFTTT 的自動化工作流 n8n - jkgtw's blog</a></li><li><a href="https://docs.n8n.io/" target="_blank">n8n Documentation</a></li></ul></div><div class="update-details-wrap" data-v-6dd0eb6a></div><!----></div><div style="border:1px solid transparent;" data-v-6dd0eb6a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6dd0eb6a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>19</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-559" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E5%88%A9%E7%94%A8%20n8n%20%E6%89%93%E9%80%A0%E9%A3%9E%E4%B9%A6%20RSS%20%E6%8E%A8%E9%80%81%E6%9C%BA%E5%99%A8%E4%BA%BA%E3%80%91%E5%89%8D%E8%A8%80%E6%9C%AC%E6%96%87%E4%BB%8B%E7%BB%8D%E4%BA%86%E5%9F%BA%E4%BA%8E%E5%BC%80%E6%BA%90%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B9%B3%E5%8F%B0n8n%E6%90%AD%E5%BB%BA%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%81%E7%A8%8B%EF%BC%8C%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7RSS%E6%9B%B4%E6%96%B0%E5%B9%B6%E6%8E%A8%E9%80%81%E5%88%B0%E9%A3%9E%E4%B9%A6%E6%B6%88%E6%81%AF%E7%9A%84%E5%8A%9F%E8%83%BD%E3%80%82%E6%96%87%E6%9C%AB%E4%BC%9A%E5%88%97%E4%B8%BE%E4%B8%80%E4%BA%9B%E5%AE%9E%E7%8E%B0%E6%AD%A4%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%9A%84%E5%85%B6%E4%BB%96%E6%96%B9%E5%BC%8F%EF%BC%8C%E5%8C%85%E6%8B%AC%E5%8F%91%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F05%2F17%2Faede586f60a73fcff7864dec104cc496.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-3682" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E5%88%A9%E7%94%A8%20n8n%20%E6%89%93%E9%80%A0%E9%A3%9E%E4%B9%A6%20RSS%20%E6%8E%A8%E9%80%81%E6%9C%BA%E5%99%A8%E4%BA%BA%E3%80%91%E5%89%8D%E8%A8%80%E6%9C%AC%E6%96%87%E4%BB%8B%E7%BB%8D%E4%BA%86%E5%9F%BA%E4%BA%8E%E5%BC%80%E6%BA%90%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B9%B3%E5%8F%B0n8n%E6%90%AD%E5%BB%BA%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%81%E7%A8%8B%EF%BC%8C%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7RSS%E6%9B%B4%E6%96%B0%E5%B9%B6%E6%8E%A8%E9%80%81%E5%88%B0%E9%A3%9E%E4%B9%A6%E6%B6%88%E6%81%AF%E7%9A%84%E5%8A%9F%E8%83%BD%E3%80%82%E6%96%87%E6%9C%AB%E4%BC%9A%E5%88%97%E4%B8%BE%E4%B8%80%E4%BA%9B%E5%AE%9E%E7%8E%B0%E6%AD%A4%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%9A%84%E5%85%B6%E4%BB%96%E6%96%B9%E5%BC%8F%EF%BC%8C%E5%8C%85%E6%8B%AC%E5%8F%91%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            